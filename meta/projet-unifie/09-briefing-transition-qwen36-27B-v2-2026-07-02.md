---
title: "Briefing v2 — Transition Ornith → Qwen3.6-27B-FP8 (état au 2026-07-02, diagnostic cause racine)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, qwen, vllm, gpu-cloud, runbook, transition, diagnostic]
created: 2026-07-01
updated: 2026-07-02
---

> ⚠️ SUPERSEDED par `09-briefing-transition-qwen36-27B-v3-2026-07-03.md` (2026-07-03).
> Deux règles de ce document sont ERRONÉES : (1) `sleep infinity` comme Container Start Command
> ne fonctionne pas avec l'image vLLM (ENTRYPOINT fixe `vllm serve`) ; (2) la régression Claude
> Code ≥ 2.1.154 n'y est pas mentionnée. Voir la v3 et `11-…`. Conservé pour historique.

# Briefing v2 — Transition Ornith → Qwen3.6-27B-FP8

> Document destiné à **Claude Code**. Remplace la v1 (`09-briefing-transition-qwen36-27B-2026-07-01.md`).
> La session du 2026-07-02 a rencontré une série de blocages dont la **cause racine a été identifiée**
> (§4). La procédure §6 repart sur une base saine. À lire avant toute manipulation du Pod RunPod.

---

## 1. Contexte général (inchangé depuis v1)

Objectif : **remplacer Opus (API payante)** par **Qwen3.6-27B-FP8 auto-hébergé** (vLLM sur RunPod)
pour motoriser Claude Code dans les tâches d'intégration `_inbox/` du wiki. Workflow inchangé, seul
le moteur change.

```
[iPad/Termius] ──ssh──> [Hetzner "Wiki"]  ──tunnel SSH──>  [RunPod Pod GPU]
                         /root/wiki                          vLLM sert le modèle
                         client `claude`                     port 8000 (API Anthropic)
```

Modèle retenu : **`Qwen/Qwen3.6-27B-FP8`** (Apache 2.0, ~31 Go, FP8 officiel, parser
`qwen3_coder`, contexte natif 262K). Justification complète en v1 §3.

Les 3 différences avec le runbook Ornith (`05-…`) restent : nom du modèle, parser
`qwen3_coder` (au lieu de `qwen3_xml`), taille du téléchargement (~31 Go au lieu de ~19).

---

## 2. Historique Ornith (rappel court)

- Tests conclus 2026-06-29 : atelier **8 ✓ / 0 ✗**, doctrinal **12 ✓ / 0 ✗** (au 2e run, consigne
  unitaire). Verdict d'usage : non convaincant (dérive narrative rapide, échec total du 1er run
  doctrinal sur consigne large, 9B sous le seuil de fiabilité agentique).
- Règles toujours en vigueur pour tout modèle local : **jamais d'auto-accept**, **verdict par
  script `compare` uniquement**, sessions courtes, consignes unitaires sur le doctrinal.

---

## 3. Chronologie des blocages de la session 2026-07-02

Résumé factuel, utile pour comprendre le diagnostic :

1. **A6000 #1** (image passée à `vllm/vllm-openai:latest`) : erreur
   `NVIDIA driver too old (12040)` — vLLM 0.24.0 exige CUDA plus récent que le GPU hôte.
2. Changement d'image vers `v0.19.1` → **le Pod est devenu indisponible** ; nouveau Pod créé.
3. **A6000 #2** : `Free memory 3.63/47.53 GiB` au démarrage — 44 Go déjà occupés, **aucun
   processus visible** dans nvidia-smi. Interprété (à tort) comme "GPU défaillant".
4. **A100 #1** (1,40 $/h) : même symptôme — 76/79 Go occupés à froid. `ps aux` a enfin révélé le
   coupable : `vllm serve Qwen/Qwen3-8B ... --gpu-memory-utilization 0.95` lancé automatiquement.
5. Chaque `kill` du processus fantôme fermait la session SSH (process parent du proxy) et le
   conteneur redémarrait… en relançant le même Qwen3-8B.
6. Bascule sur l'image `runpod/pytorch` (pas de vLLM auto) : VRAM enfin à 0 ✓, mais il a fallu
   réinstaller vLLM à la main → cascade d'échecs disque : `No space left` (container disk 5 Go),
   `Disk quota exceeded` (quota 50 Go du volume, protocole xet), `Encrypted volume cannot be
   resized`, `Bus error`, `[Errno 5] I/O error` (NFS).
7. Le téléchargement du modèle au **format cache HF standard**
   (`models--Qwen--Qwen3.6-27B-FP8/`) via `hf download` **sans** `--local-dir` a réussi (le format
   plat `--local-dir` n'est pas lu par la huggingface_hub de vllm 0.19.1).

---

## 4. 🎯 Diagnostic — la cause racine

**Le template RunPod "vLLM Latest" possède sa propre commande de démarrage intégrée**, distincte
du champ "Container Start Command" des overrides :

```
vllm serve Qwen/Qwen3-8B --host 0.0.0.0 --port 8000 --dtype auto --enforce-eager \
  --gpu-memory-utilization 0.95 --max-model-len 8128
```

Conséquences en chaîne :
- **Vider les overrides ne désactive PAS cette commande** — le conteneur retombe sur le défaut du
  template et relance Qwen3-8B à chaque démarrage (95 % de la VRAM consommée avant toute action).
- **L'override d'image ne prend pas non plus** sur un Pod lié à ce template (logs : `version
  0.24.0` alors que `v0.19.1` était demandé).
- Le processus fantôme étant parent de la session proxy, le tuer ferme la connexion et le
  conteneur redémarre à l'identique → boucle sans issue.
- Les "GPU défaillants" successifs (A6000, A100) étaient en réalité **le même template** appliqué
  à chaque nouveau Pod.

**Erreur secondaire** : la fuite en avant vers l'image `runpod/pytorch` a échangé un problème
identifié (VRAM occupée) contre un problème structurel (réinstaller vLLM sur NFS avec quota =
fragile : Bus error, I/O error, formats de cache incompatibles).

**Leçon de méthode** : au premier OOM inexpliqué, lancer `ps aux | grep -i vllm` et
`nvidia-smi` AVANT de changer de matériel ou d'image.

---

## 5. Règles RunPod consolidées (v1 + session 2026-07-02)

- **JAMAIS le template "vLLM Latest"** (ni aucun template applicatif) : sa commande de démarrage
  intégrée est prioritaire et invisible depuis les overrides. Toujours partir d'un déploiement
  **Custom** avec image saisie à la main.
- **Image pinnée** : `vllm/vllm-openai:v0.19.1` (jamais `latest` — CUDA incompatible vérifié 2×).
- **État stable = `sleep infinity`** en Container Start Command : le conteneur démarre, ne lance
  rien, ne plante jamais, la session SSH tient. On lance vLLM à la main tant que la config n'est
  pas validée.
- **Volume disk : 100 Go, chiffrement DÉCOCHÉ** (un volume chiffré ne peut pas être
  redimensionné ; 50 Go sont trop justes : modèle 31 Go + marge téléchargement).
- **Téléchargement modèle** : `hf download Qwen/Qwen3.6-27B-FP8` **sans `--local-dir`** (format
  cache HF standard, seul format lu par vLLM). Si `hf` absent :
  `pip install huggingface_hub -q` d'abord.
- **Bug UI RunPod** : ouvrir les overrides réinitialise le Volume disk → régler le volume **en
  dernier**, juste avant Save/Deploy.
- Rappels v1 toujours valides : Pods (jamais Serverless) ; port TCP 22 seul exposé ; le port SSH
  externe change à chaque restart ; sshd à réinstaller après chaque démarrage (proxy
  `ssh.runpod.io` en attendant) ; `pkill`/`kill` sur le process vLLM de démarrage = redémarrage du
  conteneur ; `ANTHROPIC_*` à réexporter dans chaque shell ; `ANTHROPIC_CUSTOM_HEADERS` obligatoire.

---

## 6. Procédure de reprise (base saine)

### Étape A — Terminer le Pod PyTorch actuel
Dashboard RunPod → Terminate (l'approche pip-sur-NFS est abandonnée).

### Étape B — Déployer le Pod proprement
- GPU : **A100 PCIe 80 Go** (~1,40 $/h) — ou A6000 48 Go (~0,50 $/h) si le budget prime ; les
  deux suffisent pour le FP8 de 31 Go.
- **Déploiement Custom, PAS le template vLLM Latest.**
- Container image : `vllm/vllm-openai:v0.19.1`
- Container Start Command : `sleep infinity`
- Container disk : 5 Go · **Volume disk : 100 Go, non chiffré**, monté sur `/workspace`
- Expose TCP : `22`
- Variables : `VLLM_API_KEY=sk-$RUNPOD_POD_ID` · `HF_HOME=/workspace/huggingface`
- ⚠️ Régler le Volume disk en dernier (bug UI), puis Deploy.

### Étape C — Vérifier l'état neutre (connexion proxy)
```bash
ssh <pod-id>-<hash>@ssh.runpod.io -i ~/.ssh/id_ed25519   # copier depuis Connect, jamais retaper
nvidia-smi          # attendu : 0 MiB, aucun processus
ps aux | grep vllm  # attendu : rien (hormis le grep)
```
Si la VRAM n'est pas à 0 ici → STOP, le template a encore fui, ne pas continuer.

### Étape D — Télécharger le modèle (format cache)
```bash
hf download Qwen/Qwen3.6-27B-FP8        # ~31 Go ; si hf absent : pip install huggingface_hub -q
df -h /workspace                         # contrôle d'espace après coup
```

### Étape E — Installer sshd (optionnel mais recommandé, pour le tunnel direct)
```bash
apt update && apt install -y openssh-server && service ssh start
mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMRYQBrXxC3g09bKvLwdWWdZacaQR+k+UPjelSaTR7vy sidyvision-wiki" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

### Étape F — Lancer vLLM à la main
```bash
vllm serve Qwen/Qwen3.6-27B-FP8 \
  --served-model-name Qwen3.6-27B-FP8 \
  --host 127.0.0.1 --port 8000 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3 \
  --trust-remote-code
```
(Le nom `Qwen/Qwen3.6-27B-FP8` + `HF_HOME` déjà posé par les variables du Pod → chargé depuis le
cache local, pas de re-téléchargement.) Attendre `Application startup complete`.

### Étape G — Vérifier l'API (2e session proxy, pour ne pas tuer vLLM)
```bash
curl -s http://127.0.0.1:8000/v1/models -H "Authorization: Bearer sk-<POD_ID>"
curl -s http://127.0.0.1:8000/v1/messages -H "content-type: application/json" \
  -H "Authorization: Bearer sk-<POD_ID>" \
  -d '{"model":"Qwen3.6-27B-FP8","max_tokens":64,"messages":[{"role":"user","content":"dis bonjour"}]}'
```

### Étape H — Tunnel + Claude Code (sur le Hetzner, inchangé)
```bash
ssh -N -f -L 8000:127.0.0.1:8000 root@<IP-du-Pod> -p <PORT-Connect> -i ~/.ssh/id_ed25519

export ANTHROPIC_BASE_URL=http://localhost:8000
export ANTHROPIC_MODEL=Qwen3.6-27B-FP8
export ANTHROPIC_SMALL_FAST_MODEL=Qwen3.6-27B-FP8
export ANTHROPIC_DEFAULT_HAIKU_MODEL=Qwen3.6-27B-FP8
export DISABLE_PROMPT_CACHING=1
export VLLM_API_KEY="sk-<POD_ID>"
export ANTHROPIC_API_KEY="$VLLM_API_KEY"
export ANTHROPIC_AUTH_TOKEN="$VLLM_API_KEY"
export ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"
claude
```

### Étape I — Pérenniser (seulement après validation de F-H)
Remplacer `sleep infinity` par la commande vLLM complète dans les overrides, Restart, revérifier
l'API. Ainsi le Pod redémarre autonome.

### Étape J — Tests
Test trivial (lecture fichier, petite édition, `git status`) puis cycle `prepare → compare`
(scripts `ornith-test.sh` / `ornith-test-doctrinal.sh`), mêmes règles de supervision qu'Ornith.

---

## 7. Sources
- Qwen3.6-27B-FP8 : https://huggingface.co/Qwen/Qwen3.6-27B-FP8
- vLLM ↔ Claude Code : https://docs.vllm.ai/en/stable/serving/integrations/claude_code/
- Runbook Ornith (infra de référence) : `05-runbook-test-ornith-gpu-cloud.md`
- Comptes-rendus : `06-…`, `07-…`, `08-…` ; briefing v1 : `09-briefing-transition-qwen36-27B-2026-07-01.md`
