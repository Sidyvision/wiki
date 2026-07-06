---
title: "12 — Procédure Phase 1 : Installation Hermes Agent + validation CLI (2026-07-03)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, hermes, qwen, runbook]
created: 2026-07-03
updated: 2026-07-03
---

# 12 — Procédure Phase 1 : Installation Hermes Agent + validation CLI

> Document destiné à **Claude Code** (session Termius sur `root@Wiki`). Prolonge le briefing
> `10-briefing-infrastructure-hermes-agent-2026-07-03.md` et la
> `note-optimisation-hermes-2026-07-03.md`. Prérequis : Phase 0 terminée (endpoint vLLM
> Qwen3.6-27B-FP8 opérationnel, double régression 8✓/12✓ — cf. `09-briefing-…-v3.md`).
> **Mode pédagogique** : chaque commande est accompagnée de ce qu'elle fait et pourquoi.

---

## 0. Décisions prises pour cette phase

La `note-optimisation-hermes-2026-07-03.md` laissait trois points ouverts. Pour ne pas bloquer le
démarrage de la Phase 1, les résolutions provisoires suivantes s'appliquent — **à reconsidérer en
Phase 3**, pas maintenant :

- **GPU** : on **garde le Pod A100 tel quel** pour cette phase. Le changer pour un A6000
  impliquerait de redéployer un nouveau Pod et de retélécharger le modèle (~10 min) pour un gain
  nul en Phase 1 (validation CLI ponctuelle, pas de charge). L'arbitrage A100/A6000 n'a d'impact
  réel qu'en usage **permanent** (gateway) → reporté à la Phase 3.
- **Mode d'hébergement** : **Pod à la demande** (on démarre/arrête autour des sessions), comme
  recommandé par la note. Le Serverless reste à tester spécifiquement avant la Phase 3.
- **Timing** : les deux préalables de confort de la note (script de tunnel, décisions ci-dessus)
  sont traités dans cette procédure — rien ne bloque plus.

---

## 1. Étape A — Vérifier / redémarrer le Pod RunPod

Dans le dashboard RunPod : si le Pod est **Stopped**, cliquer **Resume**. Comme le volume de
100 Go (non chiffré) conserve le modèle déjà téléchargé, le redémarrage est rapide — surveiller
l'onglet **Logs** jusqu'à `Application startup complete` (quelques minutes, pas les ~10 min du
premier boot).

Relever la nouvelle adresse dans **Connect → Direct TCP ports** : `<IP>` et `<PORT>` externe.
**Rappel** : ce port change à chaque redémarrage du Pod (règle consolidée du briefing 09, §4).

---

## 2. Étape B — Créer le script de tunnel paramétrable

Ce script évite de retaper la commande de tunnel à la main à chaque fois que le port RunPod
change. Il tue l'ancien tunnel local sur le port 8000, puis en remonte un nouveau vers l'IP/port
donnés en argument.

```bash
cat > ~/tunnel-runpod.sh << 'EOF'
#!/bin/bash
# Usage : ./tunnel-runpod.sh <IP> <PORT>
IP="$1"; PORT="$2"
if [ -z "$IP" ] || [ -z "$PORT" ]; then
  echo "Usage : $0 <IP> <PORT>"
  exit 1
fi
# Tue un éventuel tunnel existant sur le port local 8000
pkill -f "ssh -N -f -L 8000:127.0.0.1:8000" 2>/dev/null
sleep 1
ssh -N -f -L 8000:127.0.0.1:8000 root@"$IP" -p "$PORT" -i ~/.ssh/id_ed25519
echo "Tunnel monté : localhost:8000 -> $IP:$PORT"
sleep 1
curl -s http://localhost:8000/v1/models -H "Authorization: Bearer $VLLM_API_KEY" \
  && echo "✅ Endpoint répond." \
  || echo "⚠️ Endpoint ne répond pas — vérifier le Pod (Logs RunPod)."
EOF
chmod +x ~/tunnel-runpod.sh
```

*Ce que ça fait* : `pkill` referme proprement un tunnel resté ouvert d'une session précédente (sinon
le port 8000 local est déjà pris et le nouveau tunnel échoue silencieusement). `ssh -N -f -L`
ouvre un tunnel en arrière-plan (`-f`) sans ouvrir de shell (`-N`), qui redirige tout ce qui arrive
sur `localhost:8000` vers `127.0.0.1:8000` côté Pod. Le `curl` final vérifie immédiatement que ça
fonctionne.

**Utilisation** (avec l'IP:PORT relevés à l'étape A) :
```bash
export VLLM_API_KEY="sk-<POD_ID>"   # la même clé que lors du déploiement du Pod (briefing 09)
~/tunnel-runpod.sh <IP> <PORT>
```

---

## 3. Étape C — Installer Hermes Agent

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

*Ce que ça fait* : télécharge et installe `uv` (gestionnaire d'environnements Python moderne,
remplace pip/venv), provisionne Python 3.11 si absent, puis installe Hermes sous `~/.hermes/`
(config, logs, skills, mémoire y vivront). Aucun conflit avec l'installation Node.js/Claude Code
existante — Hermes vit dans son propre répertoire.

Recharger le shell pour que la commande `hermes` soit reconnue :
```bash
source ~/.bashrc
hermes doctor
```

*Ce que ça fait* : `hermes doctor` diagnostique l'installation. À ce stade, il doit signaler
**l'absence de provider de modèle configuré** — c'est normal, c'est l'objet de l'étape suivante.

---

## 4. Étape D — Configurer le modèle (endpoint Qwen via le tunnel)

```bash
hermes model
```

Répondre à l'assistant interactif :
- **Provider** → `Custom endpoint (self-hosted / vLLM / etc.)`
- **URL de base** → `http://localhost:8000/v1` *(le `/v1` est la racine OpenAI-compatible ; Hermes
  ajoute lui-même `/chat/completions`)*
- **Clé API** → `sk-<POD_ID>` *(identique à `VLLM_API_KEY` posé côté Pod à l'étape B/briefing 09)*
- **Nom du modèle** → `Qwen3.6-27B-FP8` *(doit correspondre exactement au `--served-model-name`
  du lancement vLLM)*

Cela écrit dans `~/.hermes/config.yaml` et la clé dans `~/.hermes/.env`. Vérifier/compléter
manuellement la longueur de contexte, que l'assistant ne détecte pas toujours automatiquement sur
un endpoint personnalisé :

```yaml
# ~/.hermes/config.yaml
model:
  default: Qwen3.6-27B-FP8
  provider: custom
  base_url: http://localhost:8000/v1
  context_length: 131072   # doit correspondre au --max-model-len du lancement vLLM
```

*Pourquoi ça compte* : Hermes a besoin d'au moins 64 000 tokens de contexte pour un usage
agentique fiable (system prompt + schémas d'outils + état de conversation) ; en dessous, il refuse
de démarrer. Notre endpoint est lancé avec `--max-model-len 131072`, largement suffisant.

---

## 5. Étape E — Première conversation CLI

```bash
hermes
```

Poser une question simple : *« Quel modèle exécutes-tu, et peux-tu lister les fichiers du
répertoire courant ? »*

Deux choses à vérifier dans la réponse :
1. **Cohérence** : la réponse doit être pertinente et arriver en quelques secondes (pas de
   timeout, pas de texte tronqué).
2. **Tool-calling réel** : Hermes doit effectivement invoquer l'outil de listing de fichiers (pas
   décrire en texte ce qu'il *ferait*). C'est le point de vigilance identifié dans la note
   d'optimisation §2 — le tool-calling passe par le parser `qwen3_coder` configuré côté vLLM
   (briefing 09, Étape D), jamais testé jusqu'ici via l'API OpenAI-compatible de Hermes.

Si le tool-calling échoue ou hallucine (décrit une action sans l'exécuter) : c'est un signal
d'alerte sur la compatibilité `qwen3_coder` ↔ Hermes, à documenter avant de poursuivre vers la
Phase 2 — ne pas forcer.

---

## 6. Étape F — Diagnostic final

```bash
hermes doctor
```

Doit être **propre** : aucune alerte sur le provider, le modèle, ou la connectivité.

---

## 7. Étape G — Extinction propre

Fermer la session `hermes` normalement (`/exit` ou `Ctrl+D`). Comme convenu en Pod à la demande,
le Pod RunPod peut être arrêté entre les sessions (mêmes règles que Claude Code, briefing 09
Étape J) — le volume non chiffré conserve le modèle et la config Hermes reste sur le Hetzner,
inchangée au prochain redémarrage.

---

## 8. Critère de sortie de la Phase 1

Repris du briefing 10 (§7) : **conversations CLI stables, `hermes doctor` propre.** Le test de
tool-calling (§5 ci-dessus) est la validation supplémentaire à consigner avant de passer à la
Phase 2 (Tailscale + Hermex + accès mobile).

---

## 9. Vigilance documentaire

Une fois cette phase validée, consigner le résultat dans un compte-rendu daté (même logique que
`06-compte-rendu-test-ornith-…` pour Ornith), et mettre à jour le tableau des phases dans le
briefing 10 (§7) pour cocher la Phase 1. Signaler tout écart par rapport à cette procédure —
notamment si le tool-calling `qwen3_coder` se comporte différemment entre Claude Code (endpoint
Anthropic) et Hermes (endpoint OpenAI-compatible), point identifié comme incertain dans la note
d'optimisation §2.
