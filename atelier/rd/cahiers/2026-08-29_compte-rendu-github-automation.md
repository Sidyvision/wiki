---
title: Compte-rendu — Automatisation GitHub & Webhook R&D
type: infrastructure
created: 2026-08-29
updated: 2026-08-29
tags:
- atelier
- rd
- infrastructure
- github
- webhook
- automation
- gardien
sources: []
links:
- '[[atelier/rd/index.md]]'
- '[[atelier/rd/infrastructure/]]'
- '[[meta/protocole-archives/changelog-CLAUDE.md]]'
---

# Automatisation GitHub & Webhook — R&D (2026-08-29)

## Contexte
Intégration complète du dépôt `Sidyvision/wiki` à GitHub avec automatisation du workflow Studio → Gardien.

## Infrastructure mise en place

### 1. GitHub CLI & Authentification
- Installation `gh` (v2.98.0).
- Authentification via **Personal Access Token** (scopes : `repo`, `workflow`, `read:org`, `admin:public_key`).
- `git` déjà configuré (`sidyvision` / `5q7spz6b8v@privaterelay.appleid.com`).

### 2. GitHub Actions (`.github/workflows/`)
| Workflow | Fichier | Rôle |
|---|---|---|
| **Lint & Validate** | `lint-and-validate.yml` | Frontmatter YAML, liens internes, structure dossiers (`wiki/`, `raw/`, `schema/`). Requis pour merge sur `main`. |
| **Deploy Pages** | `pages.yml` | Build MkDocs Material → GitHub Pages (`https://sidyvision.github.io/wiki/`). |

### 3. Issue Templates (`.github/ISSUE_TEMPLATE/`)
Alignés sur le workflow séquentiel **Studio → Gardien → Rapport Conjoint** :
- `studio-exploration.yml` (labels `studio`, `inbox`)
- `gardien-vigilance.yml` (labels `gardien`, `vigilance`)
- `rapport-conjoint.yml` (labels `rapport`, `studio`, `gardien`)

### 4. Labels créés
`studio` (bleu), `gardien` (orange), `rapport` (vert), `vigilance` (rouge), `inbox` (violet), `dependencies`, `github-actions`, `python`, `documentation`, `infrastructure`.

### 5. Dependabot (`.github/dependabot.yml`)
MAJ hebdomadaire (lundi 09:00) pour `github-actions` et `pip`.

### 6. Branch Protection (`main`)
- Status check requis : job `lint` (workflow Lint & Validate).
- 1 review approuvante obligatoire (dismiss stale).
- Force push / suppression bloqués.

### 7. Webhook temps réel → Agent Gardien
- **Subscription Hermes** : `github-wiki-push` (événement `push`).
- **Prompt** : notifie le Gardien pour vérification de vigilance (protocole CLAUDE.md).
- **Delivery** : `origin` (retour dans la session appelante).

### 8. Tunnel public (Cloudflare)
- `cloudflared tunnel --url http://localhost:8644`
- **URL publique** : `https://chronicle-raised-zones-admit.trycloudflare.com` (éphémère, à documenter hors-dépôt)
- Webhook GitHub configuré sur : `.../webhook/github-wiki-push`
- Secret HMAC : rotation requise (exposé en clair dans cette fiche, voir registre [2026-08-30])

## Bilan
Le dépôt est maintenant **professionnel, automatisé, et couplé au workflow R&D** :
- Qualité garantie à chaque push (lint bloquant).
- Publication web automatique (Pages).
- Notification instantanée du Gardien sans intervention humaine.
- Dépendances maintenues à jour.
- Protection de la branche principale.

## Prochaines étapes possibles
1. Webhook vers Hermes pour déclencher l'agent Gardien automatiquement (déjà prêt).
2. GitHub Project (board) : colonnes `Inbox` → `Studio` → `Gardien` → `Rapport` → `Fait`.
3. Codespaces pour éditer depuis l'iPad sans cloner localement.

---

*Consigné le 2026-08-29 dans le cadre du pôle R&D — Infrastructure / Souveraineté des moyens.*