---
title: Journal des sessions
type: meta
updated: 2026-05-24
---

# Journal des sessions

Entrées chronologiques inverses (la plus récente en haut). **Une entrée par session de travail**, ajoutée systématiquement à la fin de chaque opération INGEST / LINT / COMPARTIMENTALISER.

Distinct de `wiki/logs/` qui stocke des pages de type `log` (événements datés conservés comme contenu).

## Format d'une entrée

```markdown
## YYYY-MM-DD — opération

- **Opération** : INGEST | QUERY | LINT | COMPARTIMENTALISER
- **Domaine(s)** : ...
- **Créé** : [[slug-1]], [[slug-2]]
- **Modifié** : [[slug-3]]
- **Supprimé / déprécié** : —
- **Notes** : remarques utiles à la session suivante.
```

---

<!-- entrées ci-dessous, plus récente en premier -->

## 2026-06-02 — mise à jour onboarding

- **Opération** : maintenance méta (hors INGEST/QUERY/LINT/COMPARTIMENTALISER)
- **Domaine(s)** : —
- **Créé** : —
- **Modifié** : `schema/onboarding.md` (section Obsidian → résolue, auto-pull activé ; table infra ; prochaines étapes)
- **Supprimé / déprécié** : —
- **Notes** : synchro Obsidian iPad désormais automatique (pull on startup + intervalle). Reste à faire : persister `ANTHROPIC_API_KEY`, alimenter `raw/`, premier INGEST.
