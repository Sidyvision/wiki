---
title: "Post-Scriptum — Hook pre-commit corrigé"
type: outillage
statut_experience: reproduit
created: 2026-08-22
updated: 2026-08-22
references:
  - "[[atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination]]"
---

# Post-Scriptum — Hook pre-commit corrigé

## Bug initial

Le pre-commit hook installé lors de l'incident ZWJ ne détectait pas les fichiers
contaminés. Le script créait des fichiers de test dans `/tmp/` (hors dépôt),
donc `git add` échouait et le hook ne scannait rien.

## Correction

Le hook vérifie désormais :
1. Les fichiers en staging (commande `git diff --cached --name-only`)
2. Les fichiers du working tree en général (fallback si staging vide)
3. Utilise `perl` pour la détection (regex Unicode native, plus fiable que `grep -P`)

## Recommandation

Éviter les scripts de test dans `/tmp/` pour les hooks git — utiliser des fichiers
temporaires dans le dépôt (ex: `.git/test-*.md`) ou mocker `git diff --cached`.

---
**Ajouté** : 2026-08-22 (post-correction hook)
