---
title: "Briefing — Transition Ornith → Qwen3.6-27B-FP8 (état au 2026-07-01)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, qwen, vllm, gpu-cloud, runbook, transition]
created: 2026-07-01
updated: 2026-07-01
---

# Briefing — Transition du modèle local : Ornith → Qwen3.6-27B-FP8

> Document destiné à **Claude Code** pour le mettre à jour sur l'historique, les décisions prises
> et les actions concrètes à mener. À lire avant toute manipulation du Pod RunPod ou de
> l'environnement vLLM.

---

## 1. Contexte général

L'objectif du projet est de **remplacer Opus (API Anthropic payante au token)** par un **modèle
open-source hébergé sur GPU cloud à l'heure** pour motoriser Claude Code dans les tâches
d'intégration du dépôt wiki (`_inbox/`). Le workflow reste identique ; seul le moteur change. La
lecture lourde et la production de contenu doctrinal restent sur Claude.ai (forfait).

Infrastructure validée :
- **Serveur Hetzner** (`root@Wiki`) : hôte du dépôt `/root/wiki`, du client `claude`, des scripts.
  2 vCPU / 3,7 Go RAM / aucun GPU → **pas d'inférence ici**.
- **GPU cloud RunPod** : inférence uniquement (vLLM). Éphémère, aucun secret du dépôt n'y est déposé.
- **Tunnel SSH Hetzner ↔ Pod** : Claude Code parle à `http://localhost:8000` sur le Hetzner, qui
  est relayé chiffré vers le Pod. Le port 8000 de vLLM n'est **jamais** exposé publiquement.

Architecture :
```
[iPad/Termius] ──ssh──> [Hetzner "Wiki"]  ──tunnel SSH──>  [RunPod Pod GPU]
                         /root/wiki                          vLLM sert le modèle
                         client `claude`                     port 8000 (API Anthropic)
                         scripts, git
```

---

## 2. Historique des tests — Ornith-1.0-9B (2026-06-29)

### 2.1 Architecture déployée (validée, à réutiliser)

| Paramètre | Valeur |
|---|---|
| Fournisseur | RunPod — **Pods** (PAS Serverless — le Serverless n'a pas de SSH/tunnel) |
| GPU | 1× RTX A6000, 48 Go VRAM |
| Image | `vllm/vllm-openai:latest` |
| Container disk | 50 Go |
| Volume persistant | 50 Go, monté sur `/workspace` |
| Coût observé | ≈ 0,50 $/h |
| TCP exposé | **port 22 uniquement** (jamais le 8000) |

Variables d'environnement du conteneur (RunPod) :
- `VLLM_API_KEY` = `sk-$RUNPOD_POD_ID` (auto-généré par RunPod)
- `HF_HOME` = `/workspace/huggingface`

### 2.2 Correctifs critiques découverts lors du test (tous intégrés au runbook)

**Authentification** : Claude Code envoie nativement `x-api-key`, mais vLLM n'accepte que
`Authorization: Bearer <clé>` → 401 systématique sans correctif. Solution : variable
`ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"`.

**Taille de contexte** : le prompt système de Claude Code seul pèse ≈ 27 000 tokens ; des tours
réels ont atteint 143 000 tokens. `--max-model-len 32768` et `65536` échouent (erreur 500).
Plancher retenu : **`--max-model-len 131072`**.

**SSH dans l'image vLLM** : l'image `vllm/vllm-openai` ne contient pas de serveur SSH.
Il faut l'installer **après chaque redémarrage** du conteneur. Le **port TCP externe SSH change
à chaque restart** → toujours vérifier l'onglet Connect → Direct TCP ports avant de relancer un tunnel.

**`pkill -f vllm` interdit** : cette commande cible le PID 1 du conteneur → redémarre tout le
conteneur (sshd perdu, overrides rechargés). Pour changer la config vLLM : modifier les overrides
dans le dashboard RunPod + bouton Restart Pod.

### 2.3 Résultats des tests Ornith

**Test atelier** (lot `meta/`, frontmatter allégé, sans Sceau Recteur) : **VERDICT 8 ✓ / 0 ✗**
— Ornith équivaut à Opus byte pour byte sur ce lot.

**Test doctrinal** (fiche `doctrinal/`, Sceau Recteur complet, `cross_links`, étanchéité) :
- Premier run avec consigne large (« intègre `_inbox/` ») : **échec total** — discours halluciné
  dès la 1re réponse (caractères chinois, fausse citation coranique, tableaux incohérents) et
  **aucune action réelle exécutée**.
- Second run avec consigne unitaire (une fiche à la fois) : **VERDICT 12 ✓ / 0 ✗**.

**Leçons clés à retenir pour tout futur modèle local** :
1. *Fiabilité d'action ≠ fiabilité narrative* : le discours peut se dégrader (langues mêlées,
   fuite `</think>`, contradictions) **pendant que les écritures restent correctes**.
2. La largeur de consigne est déterminante : une consigne large sur un cas complexe peut faire
   échouer à la fois le discours ET les actions dès le départ.
3. **Jamais d'auto-accept** des modifications. Chaque `Write`/`Update`/Bash doit être relu
   avant exécution.
4. **Toujours clore par une vérification mécanique indépendante** (script `compare`), jamais
   par l'auto-rapport du modèle.

### 2.4 Pourquoi Ornith n'a pas convaincu

Malgré un verdict technique acceptable, le comportement d'Ornith-1.0-9B n'a pas convaincu sur
le plan pratique : dégradation narrative rapide (~30-40 min), premier run doctrinal en échec
total, hallucinations fréquentes. Sa taille (9B) est en dessous du seuil de fiabilité agentique
recommandé (≥ 13B).

---

## 3. Décision : migrer vers Qwen3.6-27B-FP8

### 3.1 Choix et justification

Modèle retenu : **`Qwen/Qwen3.6-27B-FP8`** (Alibaba, Apache 2.0).

Raisons :
- **27B dense** → très au-dessus du seuil de fiabilité agentique (≥ 13B recommandé).
- **FP8 officiel** : checkpoint quantifié nativement par Alibaba, sans perte de qualité
  mesurable (block size 128). Pèse ≈ 27-28 Go → tient confortablement sur le GPU A6000 48 Go
  avec large marge pour le cache KV.
- **Même famille vLLM + même parser `qwen3_coder`** que ce qui était prévu pour Qwen3-27B-FP8
  dans le runbook initial → infrastructure quasi identique.
- **Performances** : égale Claude 4.5 Opus sur Terminal-Bench 2.0 (59.3), scores SWE-bench
  competitive. Conçu explicitement pour l'agentic coding et le tool-use fiable en session longue.
- **Contexte natif** : 262 144 tokens (le `--max-model-len 131072` retenu est déjà confortable).

### 3.2 Différences avec le runbook Ornith (05-…) — les 3 seuls changements

| Point | Ornith (ancien) | Qwen3.6-27B-FP8 (nouveau) |
|---|---|---|
| Nom du modèle | `deepreinforce-ai/Ornith-1.0-9B` | `Qwen/Qwen3.6-27B-FP8` |
| Tool-call parser | `--tool-call-parser qwen3_xml` | `--tool-call-parser qwen3_coder` |
| Taille du téléchargement | ≈ 19 Go | ≈ 27-28 Go |

Tout le reste (image RunPod, variables d'environnement conteneur, tunnel SSH, variables `ANTHROPIC_*`
côté Hetzner, procédure sshd) est **identique** au runbook validé.

---

## 4. État actuel du Pod RunPod (au 2026-07-01)

- **Le Pod existe encore** (visible dans le dashboard RunPod, nom : `additional_turquoise_hookworm-migration`).
- **Container Start Command** déjà mis à jour dans les overrides RunPod (dashboard, section Edit Pod) :
  ```
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
- **Volume persistant 50 Go** (`/workspace`) : toujours monté. Ornith (~19 Go) est encore présent
  dans le cache HuggingFace — **à supprimer avant ou pendant le téléchargement de Qwen** (espace
  insuffisant pour les deux simultanément).
- **Pod stoppé ou en cours** : vérifier le statut dans RunPod et l'état de facturation.

---

## 5. Actions à réaliser (dans l'ordre)

### Étape A — Supprimer le cache Ornith (sur le Pod, connexion proxy RunPod)

Copier la commande SSH depuis l'onglet **Connect** du Pod dans RunPod (format
`ssh <pod-id>-<hash>@ssh.runpod.io -i ~/.ssh/id_ed25519`). **Ne jamais retaper cette commande
à la main** — la copier-coller depuis le dashboard pour éviter les erreurs.

Une fois connecté au conteneur via le proxy RunPod :
```bash
# 1. Vérifier le contenu du cache HF
ls /workspace/huggingface/hub/

# 2. Confirmer la taille (doit être proche de ~19 Go)
du -sh /workspace/huggingface/hub/models--deepreinforce-ai--Ornith-1.0-9B

# 3. Vérifier l'espace avant suppression
df -h /workspace

# 4. Supprimer
rm -rf /workspace/huggingface/hub/models--deepreinforce-ai--Ornith-1.0-9B

# 5. Confirmer l'espace libéré (doit afficher > 27 Go disponibles)
df -h /workspace
```

### Étape B — Redémarrer le Pod (dashboard RunPod)

Dans le dashboard RunPod : bouton **Restart Pod** sur la fiche du Pod.
Les overrides (Container Start Command) ont déjà été mis à jour à l'étape précédente.

### Étape C — Installer sshd (après redémarrage, connexion proxy RunPod)

Récupérer la nouvelle commande SSH depuis **Connect** (le port TCP externe change à chaque restart).
```bash
apt update && apt install -y openssh-server
mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMRYQBrXxC3g09bKvLwdWWdZacaQR+k+UPjelSaTR7vy sidyvision-wiki" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
service ssh start
```

### Étape D — Télécharger Qwen3.6-27B-FP8 (sur le Pod)

```bash
huggingface-cli download Qwen/Qwen3.6-27B-FP8 \
  --local-dir /workspace/huggingface/hub/Qwen3.6-27B-FP8
```
Durée estimée : 15-30 min selon le débit. Attendre la fin complète.

### Étape E — Attendre le démarrage de vLLM et vérifier l'API

vLLM démarre automatiquement via les overrides au lancement du Pod (ou peut être relancé
manuellement si besoin). Attendre le message « Application startup complete ».

Récupérer la clé API depuis le conteneur :
```bash
cat /proc/1/environ | tr '\0' '\n' | grep VLLM_API_KEY
```

Tester l'endpoint depuis le conteneur :
```bash
curl -s http://127.0.0.1:8000/v1/messages \
  -H "content-type: application/json" \
  -d '{"model":"Qwen3.6-27B-FP8","max_tokens":64,"messages":[{"role":"user","content":"dis bonjour"}]}'
```
Une réponse JSON valide = le serveur est opérationnel.

### Étape F — Monter le tunnel SSH depuis le Hetzner

Sur le serveur Hetzner (`root@Wiki`), relever l'IP et le port depuis **Connect → Direct TCP ports**
du dashboard RunPod, puis :
```bash
ssh -N -f -L 8000:127.0.0.1:8000 root@<IP-du-Pod> -p <PORT> -i ~/.ssh/id_ed25519
```

Vérifier le tunnel :
```bash
curl -s http://localhost:8000/v1/models \
  -H "Authorization: Bearer sk-<valeur-VLLM_API_KEY>"
```

### Étape G — Brancher Claude Code sur Qwen3.6-27B-FP8 (Hetzner)

Dans le shell utilisé pour lancer `claude` :
```bash
export ANTHROPIC_BASE_URL=http://localhost:8000
export ANTHROPIC_MODEL=Qwen3.6-27B-FP8
export ANTHROPIC_SMALL_FAST_MODEL=Qwen3.6-27B-FP8
export ANTHROPIC_DEFAULT_HAIKU_MODEL=Qwen3.6-27B-FP8
export DISABLE_PROMPT_CACHING=1
export VLLM_API_KEY="sk-<valeur-récupérée-étape-E>"
export ANTHROPIC_API_KEY="$VLLM_API_KEY"
export ANTHROPIC_AUTH_TOKEN="$VLLM_API_KEY"
export ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"
claude
```

> ⚠️ Ces variables ne survivent pas à un nouvel onglet/shell — les réexporter dans chaque
> nouveau shell utilisé pour lancer `claude`.

### Étape H — Test trivial puis test de non-régression

Test trivial d'abord (valider la boucle d'outils avant l'intégration réelle) :
- Demander à Claude Code de lire un fichier, faire une petite édition, `git status`.

Test de non-régression ensuite :
- Reprendre le protocole `prepare → compare` (scripts `regression-test.sh` /
  `regression-test-doctrinal.sh`, paramétrés par `MODEL_LABEL`) sur un lot témoin déjà intégré par Opus.
- **Règles de supervision identiques à celles d'Ornith** : jamais d'auto-accept, relire chaque
  Write/Update/Bash avant validation, clore par le script `compare` (jamais par l'auto-rapport
  du modèle).

---

## 6. Pièges connus (tous vérifiés lors des tests Ornith)

- **RunPod : toujours Pods, jamais Serverless** (pas de SSH/tunnel en Serverless).
- **Port SSH externe change à chaque restart** → toujours le relever dans Connect avant de
  relancer le tunnel.
- **`pkill -f vllm` interdit** → passe par les overrides + Restart Pod uniquement.
- **Authentification** : `ANTHROPIC_CUSTOM_HEADERS` obligatoire (401 sans lui).
- **Variables `ANTHROPIC_*` non persistantes** : réexporter dans chaque nouveau shell.
- **Aucun secret du dépôt sur le Pod** : ni clé SSH du dépôt, ni token HF privé.
- **Jamais d'auto-accept des modifications** avec un modèle local.
- **Éteindre le Pod après les tests** pour stopper la facturation (≈ 0,50 $/h).
- **Vérification mécanique toujours en dernier** : script `compare`, jamais l'auto-rapport du modèle.

---

## 7. Sources

- Qwen3.6-27B-FP8 (carte modèle officielle, commandes vLLM) :
  https://huggingface.co/Qwen/Qwen3.6-27B-FP8
- vLLM — intégration Claude Code :
  https://docs.vllm.ai/en/stable/serving/integrations/claude_code/
- Runbook Ornith (référence infrastructure, toujours valable sauf les 3 changements §3.2) :
  `meta/projet-unifie/05-runbook-test-ornith-gpu-cloud.md`
- Compte-rendus des tests Ornith :
  `meta/projet-unifie/06-…`, `07-…`, `08-…`
