---
title: "Briefing v3 — Transition Ornith → Qwen3.6-27B-FP8 (procédure validée en production, 2026-07-03)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, qwen, vllm, gpu-cloud, runbook, transition, diagnostic]
created: 2026-07-01
updated: 2026-07-03
---

# Briefing v3 — Transition Ornith → Qwen3.6-27B-FP8

> Document destiné à **Claude Code**. Remplace la v2 (`09-…v2-2026-07-02.md`). La session du
> 2026-07-03 a **mené le déploiement à son terme** (double verdict 8✓ / 12✓) et **corrigé deux
> règles erronées de la v2** : le `sleep infinity` en start command (qui ne marche pas avec
> l'image vLLM) et l'absence de mention de la régression Claude Code ≥ 2.1.154. La procédure §6
> ci-dessous est celle **réellement validée en production**. Compte-rendu complet des résultats :
> `11-resultats-qwen36-27b-2026-07-03.md`.

---

## 1. Contexte général (inchangé)

Objectif : **remplacer Opus (API payante)** par **Qwen3.6-27B-FP8 auto-hébergé** (vLLM sur RunPod)
pour motoriser Claude Code dans l'intégration `_inbox/` du wiki. Workflow inchangé, seul le moteur
change.

```
[iPad/Termius] ──ssh──> [Hetzner "Wiki"]  ──tunnel SSH──>  [RunPod Pod GPU]
                         /root/wiki                          vLLM sert le modèle
                         client `claude`                     port 8000
```

Modèle : **`Qwen/Qwen3.6-27B-FP8`** (Apache 2.0, ~31 Go, FP8 officiel, parser `qwen3_coder`,
contexte natif 262K). Les 3 différences avec le runbook Ornith (`05-…`) : nom du modèle, parser
`qwen3_coder` (au lieu de `qwen3_xml`), taille du téléchargement (~31 Go).

---

## 2. Historique Ornith (rappel court)

- Tests 2026-06-29 : atelier **8 ✓ / 0 ✗**, doctrinal **12 ✓ / 0 ✗** (au 2e run, consigne
  unitaire). Non retenu : dérive narrative rapide, échec du 1er run doctrinal sur consigne large,
  9B sous le seuil de fiabilité agentique.
- Règles en vigueur pour tout modèle local : **jamais d'auto-accept**, **verdict par script
  `compare` uniquement**, vigilance sur `annales.md` (append-only).

---

## 3. Diagnostic de la cause racine (session 2026-07-02, confirmé)

**Le template RunPod "vLLM Latest" possède sa propre commande de démarrage intégrée** (`vllm serve
Qwen/Qwen3-8B … --gpu-memory-utilization 0.95`), distincte du champ « Container Start Command » des
overrides et **prioritaire** sur lui. Conséquences :

- Vider les overrides ne désactive pas cette commande → Qwen3-8B se relance à chaque boot et occupe
  ~95 % de la VRAM avant toute action.
- L'override d'image ne prend pas non plus sur un Pod lié à ce template (logs : `0.24.0` au lieu de
  `v0.19.1`).
- Le process fantôme étant parent de la session proxy, le tuer ferme la connexion et le conteneur
  redémarre à l'identique.
- Les « GPU défaillants » successifs (A6000, A100) étaient en fait **le même template** réappliqué.

**Leçon de méthode** : au premier « Free memory » anormal, lancer `ps aux | grep -i vllm` et
`nvidia-smi` AVANT de changer de matériel ou d'image.

---

## 4. Règles RunPod consolidées (validées en production 2026-07-03)

- **JAMAIS de template applicatif** (« vLLM Latest », « Qwen … by Trelis », etc.) : chacun embarque
  une commande de démarrage intégrée prioritaire et invisible. **Toujours un déploiement Custom**,
  image saisie à la main.
- **Image pinnée** : `vllm/vllm-openai:v0.19.1` (jamais `latest` — CUDA incompatible, vérifié).
- **⚠️ CORRECTION v2 — le Container Start Command contient UNIQUEMENT les arguments de
  `vllm serve`**, en commençant directement par le nom du modèle. L'image a pour ENTRYPOINT fixe
  `vllm serve` : tout le champ est appendé comme arguments. Donc :
  - ❌ `sleep infinity` → `vllm serve sleep infinity` → erreur (la v2 était fausse sur ce point).
  - ❌ `;sleep infinity` → `vllm serve ;sleep infinity` → process en échec à 167 % CPU.
  - ✅ `Qwen/Qwen3.6-27B-FP8 --served-model-name … --trust-remote-code` → vLLM sert le modèle.
  (Format identique à celui du compte-rendu Ornith `06-…`, qui commençait déjà par le nom du modèle
  sans `vllm serve` devant.)
- **Volume disk : 100 Go, chiffrement DÉCOCHÉ** (un volume chiffré ne peut pas être redimensionné ;
  50 Go trop justes pour 31 Go de modèle + marge).
- **Téléchargement modèle** : `hf download Qwen/Qwen3.6-27B-FP8` **sans `--local-dir`** (format
  cache HF standard `models--Qwen--…`, seul format lu par vLLM). Si `hf` absent :
  `pip install huggingface_hub -q`.
- **Bug UI RunPod** : ouvrir les overrides réinitialise le Volume disk → régler le volume **en
  dernier**, avant Save/Deploy.
- **⚠️ NOUVEAU — Claude Code ≥ 2.1.154 casse l'endpoint** : injecte `role:"system"` dans
  `messages[]` → erreur 400 de vLLM. Pin `@2.1.150` + `export DISABLE_AUTOUPDATER=1` (sinon il
  remonte seul). Détail : `11-…` §3.2.
- **Auth** : `ANTHROPIC_AUTH_TOKEN` + `ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer <clé>"`.
  Ne PAS aussi poser `ANTHROPIC_API_KEY` (conflit d'auth signalé par Claude Code).
- **Proxy `ssh.runpod.io` instable** : sessions coupées en secondes → opérations longues en
  `nohup … & disown`, et connexion **TCP directe** préférée dès que `sshd` est posé.
- Rappels toujours valides : Pods (pas Serverless pour cet usage tunnel) ; port TCP 22 exposé ;
  port SSH externe change à chaque restart ; sshd à réinstaller après chaque (re)démarrage ;
  `ANTHROPIC_*` à réexporter dans chaque shell.

---

## 5. Procédure validée (production 2026-07-03)

### Étape A — Déployer le Pod (déploiement Custom)
- GPU : **A100 PCIe 80 Go** (~1,40 $/h) — ou A6000 48 Go (~0,50 $/h), les deux tiennent le FP8.
- **Custom, PAS un template applicatif.**
- Container image : `vllm/vllm-openai:v0.19.1`
- Container disk : 5 Go · **Volume disk : 100 Go, NON chiffré**, monté sur `/workspace`
- Expose TCP : `22`
- Variables : `VLLM_API_KEY=sk-$RUNPOD_POD_ID` · `HF_HOME=/workspace/huggingface`
- **Container Start Command** — deux stratégies possibles :
  - **(a) Bootstrap direct (recommandé une fois le modèle en cache)** : coller directement les
    arguments vLLM (voir Étape D) → le Pod sert le modèle dès le boot.
  - **(b) Premier déploiement, modèle pas encore téléchargé** : laisser le champ contenir un
    argument inoffensif qui fait sortir vLLM proprement n'est pas fiable (ENTRYPOINT fixe). Plus
    simple : déployer directement avec les arguments vLLM pointant sur le modèle ; vLLM
    téléchargera lui-même le modèle au premier boot (via `HF_HOME` sur le volume). Surveiller les
    **Logs** RunPod jusqu'à `Application startup complete` (~10 min : téléchargement + chargement).
- ⚠️ Régler le Volume disk en dernier (bug UI), puis Deploy.

### Étape B — (si besoin) Télécharger le modèle à la main
Si tu préfères séparer téléchargement et service, connexion proxy puis :
```bash
hf download Qwen/Qwen3.6-27B-FP8        # sans --local-dir ; si hf absent : pip install huggingface_hub -q
df -h /workspace
```
Lancer les téléchargements longs en `nohup … & disown` (proxy instable).

### Étape C — Vérifier l'état / les logs
Onglet **Logs** du Pod (pas besoin de SSH) → attendre `Application startup complete`.
Si connexion proxy : `nvidia-smi` doit montrer le modèle chargé (≈ 30-40 Go), pas un Qwen3-8B
fantôme. Si un process inattendu occupe la VRAM → le template a fui, STOP.

### Étape D — Arguments vLLM (le contenu du Container Start Command)
```
Qwen/Qwen3.6-27B-FP8 --served-model-name Qwen3.6-27B-FP8 --host 127.0.0.1 --port 8000 --max-model-len 131072 --gpu-memory-utilization 0.90 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --trust-remote-code
```

### Étape E — Installer sshd (pour le tunnel direct, plus stable que le proxy)
```bash
apt update && apt install -y openssh-server && service ssh start
mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMRYQBrXxC3g09bKvLwdWWdZacaQR+k+UPjelSaTR7vy sidyvision-wiki" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```
(Note : sur certaines images `openssh-server` peut manquer des dépôts ; le proxy `ssh.runpod.io`
reste le repli.)

### Étape F — Vérifier l'API
```bash
curl -s http://127.0.0.1:8000/v1/models -H "Authorization: Bearer sk-<POD_ID>"
```
Réponse JSON avec `Qwen3.6-27B-FP8` = OK.

### Étape G — Tunnel depuis le Hetzner
Relever IP:PORT dans Connect → Direct TCP ports, puis sur `root@Wiki` :
```bash
ssh -N -f -L 8000:127.0.0.1:8000 root@<IP-du-Pod> -p <PORT> -i ~/.ssh/id_ed25519
curl -s http://localhost:8000/v1/models -H "Authorization: Bearer sk-<POD_ID>"
```

### Étape H — Brancher Claude Code (sur le Hetzner)
```bash
# Pin obligatoire (régression 2.1.154) :
npm install -g @anthropic-ai/claude-code@2.1.150
export DISABLE_AUTOUPDATER=1

export ANTHROPIC_BASE_URL=http://localhost:8000
export ANTHROPIC_MODEL=Qwen3.6-27B-FP8
export ANTHROPIC_SMALL_FAST_MODEL=Qwen3.6-27B-FP8
export ANTHROPIC_DEFAULT_HAIKU_MODEL=Qwen3.6-27B-FP8
export DISABLE_PROMPT_CACHING=1
export VLLM_API_KEY="sk-<POD_ID>"
export ANTHROPIC_AUTH_TOKEN="$VLLM_API_KEY"
export ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"
# NE PAS poser ANTHROPIC_API_KEY (conflit d'auth).
claude
```

### Étape I — Tests de non-régression
```bash
MODEL_LABEL="Qwen3.6-27B-FP8" bash /root/wiki/meta/projet-unifie/regression-test.sh prepare
# → dans claude : « intègre _inbox/ dans /root/regression-test/sandbox selon UPDATES.md et CLAUDE.md »
bash /root/wiki/meta/projet-unifie/regression-test.sh compare
# idem avec regression-test-doctrinal.sh
```
Supervision : jamais d'auto-accept, relecture de chaque Write/Update, verdict par `compare` seul.

### Étape J — Extinction
Stopper le Pod entre les sessions (~1,40 $/h). Le volume non chiffré conserve le modèle ;
réinstaller sshd et revérifier le port externe au redémarrage.

---

## 6. Sources
- Qwen3.6-27B-FP8 : https://huggingface.co/Qwen/Qwen3.6-27B-FP8
- vLLM ↔ Claude Code : https://docs.vllm.ai/en/stable/serving/integrations/claude_code/
- Régression Claude Code : issue `anthropics/claude-code#63469`, `vllm-project/vllm#44000`
- Runbook Ornith : `05-runbook-test-ornith-gpu-cloud.md` · Résultats : `06-`, `07-`, `08-`, `11-`
