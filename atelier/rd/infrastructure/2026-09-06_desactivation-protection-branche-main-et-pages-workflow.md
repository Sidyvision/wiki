---
title: "Désactivation de la protection de branche main et bascule GitHub Pages en mode workflow"
type: infrastructure
tags:
  - github
  - infrastructure
  - pages
  - branche
created: 2026-09-06
updated: 2026-09-06
sources: []
links: []
---

# Désactivation de la protection de branche `main` et bascule GitHub Pages en mode workflow

Deux paramétrages GitHub appliqués au dépôt `Sidyvision/wiki` le 2026-09-06, à la
demande de Sidy. Consignation R&D : deux réglages effectués via l'API GitHub
(`gh api`), vérifiés mécaniquement au moment de l'application (HTTP 204 + relecture
GET).

## 1. Protection de branche `main` — désactivée

**État antérieur** (relevé avant modification) : la branche `main` était sous
protection imposant
- un status check obligatoire `lint` (workflow `lint-and-validate.yml`) avec
  `strict: true` sur les contextes — un commit échouant `lint` était donc bloqué au
  push ;
- une revue de PR requise (`required_pull_request_reviews`, `required_approving_review_count: 0`).

**Motif de la demande de Sidy** : la protection bloquait des sessions au commit/push
(commits refusés, sessions sans push ni commit), perturbant l'arbre de travail.

**Action** : suppression totale de la protection via `DELETE
repos/Sidyvision/wiki/branches/main/protection` → HTTP 204.

**Vérification** : `GET repos/Sidyvision/wiki/branches/main/protection` renvoie
désormais HTTP 404 « Branch not protected ».

**Conséquence** : le push direct sur `main` est libre ; l'arbre de travail peut
commiter/pousser sans passer par un status check ni une revue. Aucun fichier du
dépôt n'a été modifié — c'est un paramétrage côté GitHub uniquement.

## 2. GitHub Pages — bascule `legacy` (Jekyll) → `workflow` (GitHub Actions)

**Cause racine identifiée** : le dépôt hébergeait deux mécanismes de déploiement
Pages concurrents sur le même `main` :
- le workflow local `pages.yml` (« Deploy Wiki to GitHub Pages », MkDocs →
  artifact → `actions/deploy-pages`) qui **réussissait** ;
- le workflow système `pages-build-deployment` (event `dynamic`, déclenché par la
  config Pages du dépôt en mode `legacy`, `source: main/`) qui échouait à l'étape
  « Build with Jekyll » — faute de véritable site Jekyll (`_config.yml`, etc.) dans
  le dépôt.

La config Pages du dépôt étant en `build_type: legacy`, GitHub tentait un build
Jekyll fantôme à chaque push, d'où l'échec chronique et répétitif de
`pages-build-deployment` (run `34044617846`, `33974269194`, … — toutes échouées à
« Build with Jekyll ») sans lien avec nos commits.

**Action** : bascule de la config Pages en mode workflow via `PUT
repos/Sidyvision/wiki/pages` avec `build_type=workflow` → HTTP 204.

**Vérification** : `GET repos/Sidyvision/wiki/pages` renvoie désormais
`build_type: workflow`.

**Conséquence** : le déploiement Pages est exclusivement piloté par `pages.yml`
(workflow GitHub Actions) ; le build Jekyll système n'est plus déclenché. Le site
reste publié sur https://sidyvision.github.io/wiki/.

## Passage à vérifier au prochain push sur `main`

- `pages-build-deployment` ne doit plus apparaître ni échouer ;
- `Deploy Wiki to GitHub Pages` (pages.yml) doit continuer de réussir et le site
  rester publié.

Si le workflow fantôme réapparaissait, le signaler — mais le mode `workflow`
l'élimine normalement (Test non encore passé : dépend d'un prochain push, pas
déclenché depuis la bascule).

---

**Établi par** : Hermes Agent (session INTÉGRATION) — consignation demandée par Sidy.
**Date** : 2026-09-06
**Statut** : actions appliquées et vérifiées ; à confirmer au prochain push.
