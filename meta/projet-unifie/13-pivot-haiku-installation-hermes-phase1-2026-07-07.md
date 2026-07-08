---
title: "13 — Pivot Haiku & Procédure Phase 1 révisée : Installation Hermes Agent (2026-07-07)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, hermes, haiku, decisions, runbook]
created: 2026-07-07
updated: 2026-07-07
---

# 13 — Pivot Haiku & Procédure Phase 1 révisée : Installation Hermes Agent

> **Remplace `12-procedure-installation-hermes-phase1-2026-07-03.md`**, qui pointait Hermes vers
> l'endpoint RunPod/vLLM. Suite au constat du 2026-07-06 (Claude Code + Haiku en production pour
> l'intégration `_inbox/`, coût quasi-équivalent à Qwen sans la contrainte de déploiement de Pod),
> Hermes est reconfiguré pour utiliser **directement l'API Anthropic (Haiku)** — même moteur que
> Claude Code aujourd'hui. Document destiné à Claude Code (Termius, `root@Wiki`).

---

## 1. Ce que ce pivot change

| | Avant (doc 12) | Maintenant |
|---|---|---|
| Moteur de Hermes | Qwen3.6-27B-FP8 auto-hébergé (RunPod/vLLM) | Claude Haiku via API Anthropic directe |
| Connexion | Tunnel SSH + script `tunnel-runpod.sh` | Aucune — appel HTTPS direct à `api.anthropic.com` |
| Dépendances infra | Pod RunPod à démarrer/éteindre, GPU à choisir | Aucune |
| Coût | Gratuit à l'usage (hors GPU-heure du Pod) | **Facturé au token**, comme Claude Code aujourd'hui |
| Décisions GPU/Serverless (note-optimisation §3.1/3.2) | Ouvertes, à trancher en Phase 3 | **Sans objet pour l'instant** — mises de côté, pas annulées (voir §4) |

**Point structurel** : Hermes traite l'API Anthropic comme *fournisseur de premier rang* — pas
comme un endpoint personnalisé. C'est même plus direct que ne l'était le montage vLLM. Et le bug
Claude Code ≥ 2.1.154 (`role:"system"` rejeté) documenté dans la note d'optimisation était une
incompatibilité **spécifique à l'émulation Anthropic de vLLM** — il ne concerne pas ce chemin :
l'API Anthropic réelle gère ça nativement. Le pin `@2.1.150` reste sans risque à garder, mais n'est
plus une nécessité structurelle pour ce montage.

---

## 2. Procédure Phase 1 révisée

### Étape A — Récupérer la clé Anthropic déjà en service

Claude Code charge déjà une clé API Anthropic depuis `~/.bashrc` (protocole `CLAUDE.md` §VIII).
La réutiliser est le chemin le plus simple :

```bash
grep ANTHROPIC_API_KEY ~/.bashrc
```

*Option propre (non bloquante)* : créer une clé **dédiée à Hermes** dans la Console Anthropic,
pour distinguer plus tard, dans le suivi de facturation, ce que consomme Claude Code de ce que
consomme Hermes. À faire maintenant ou plus tard, sans impact sur la suite.

### Étape B — Installer Hermes Agent

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc
hermes doctor
```

*Ce que ça fait* : identique à l'étape C du document 12 — installe `uv`, Python 3.11, et Hermes
sous `~/.hermes/`. `hermes doctor` doit à ce stade signaler l'absence de provider configuré.

### Étape C — Configurer le modèle (Anthropic direct)

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # celle de l'étape A
hermes model
```

Répondre à l'assistant interactif :
- **Provider** → `Anthropic`
- **Méthode d'authentification** → **clé API (pay-per-token)** — *pas* OAuth Claude Max (ce chemin
  est réservé aux abonnements Max avec crédits « extra usage » achetés en plus, non applicable ici)
- **Modèle** → `claude-haiku-4-5-20251001`

Résultat attendu dans `~/.hermes/config.yaml` :
```yaml
model:
  default: claude-haiku-4-5-20251001
  provider: anthropic
```

Aucune longueur de contexte à préciser manuellement — le contexte natif des modèles Anthropic
dépasse largement le plancher de 64 000 tokens exigé par Hermes pour l'usage agentique (contrainte
qui posait problème avec Ollama/vLLM, sans objet ici).

### Étape D — Première conversation CLI

```bash
hermes
```

Poser une question avec appel d'outil réel (ex. *« Liste les fichiers du répertoire courant »*) et
vérifier que Hermes invoque effectivement l'outil plutôt que de décrire l'action en texte. Sur ce
chemin natif Anthropic, le tool-calling est le format que Claude gère nativement — pas
d'équivalent à l'inconnue `qwen3_coder` de la procédure précédente.

### Étape E — Diagnostic

```bash
hermes doctor
```
Doit être propre.

### Étape F — Extinction

Rien à éteindre côté infra — pas de Pod, pas de tunnel. Fermer la session `hermes` normalement.

---

## 3. Critère de sortie (inchangé)

Repris du briefing 10 (§7) : conversations CLI stables, `hermes doctor` propre. Le test de
tool-calling (§2 Étape D) est la validation à consigner avant la Phase 2 (Tailscale + Hermex).

---

## 4. Ce qui est mis de côté, pas abandonné

- **Transition Qwen/RunPod** : plus urgente, mais l'infrastructure (Pod A100, procédure de
  déploiement, briefing 09) reste documentée et réactivable si le besoin d'indépendance totale
  vis-à-vis d'une API payante redevient prioritaire.
- **Décisions GPU (A6000/A100) et mode d'hébergement (Pod/permanent/Serverless)** de la note
  d'optimisation §3.1–3.2 : sans objet tant que Hermes tourne sur Anthropic direct. À rouvrir
  seulement si un retour au self-hosted est décidé.
- **Vigilance de coût nouvelle** : contrairement au montage Qwen (inférence gratuite, seul le
  GPU-heure comptait), Hermes sur Haiku facture **chaque échange au token** — y compris les
  usages personnels/récréatifs (Phase 7) et les cron, pas seulement l'intégration `_inbox/`. Le
  volume d'usage total (pas seulement les cycles d'ingestion) devient donc un facteur de coût à
  surveiller une fois la gateway en service (Phase 3+).
- **Vérification formelle du verdict Haiku** : le constat du 2026-07-06 est un test informel
  réussi. Rien n'empêche de continuer sur cette base, mais si vous souhaitez à un moment
  formaliser ce verdict avec le même sérieux que pour Ornith (script `compare`, cycles `_inbox/`
  réels, comparaison mécanique plutôt que ressenti), l'outillage existe déjà et resterait
  applicable — à votre discrétion, non bloquant pour la suite.

---

## 5. Ce qui ne change pas

Les principes du briefing 10 restent intégralement en vigueur, quel que soit le moteur : boutons
`clarify` avant toute intégration/push, `compare` comme seul arbitre mécanique, isolation des
domaines (wiki / infra / personnel) par canal et sub-agent, mémoire de Hermes opérationnelle
jamais doctrinale, arbitrage final réservé à Sidy.
