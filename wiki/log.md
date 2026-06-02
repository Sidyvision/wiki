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

## 2026-06-02 — premier INGEST (profil utilisateur)

- **Opération** : INGEST
- **Domaine(s)** : `perso` (page principale + source), `general` (stubs de références)
- **Créé** :
  - perso : [[sidy]], [[chatgpt-export-2026-05-10]]
  - general : [[ibn-arabi]], [[al-ghazali]], [[rene-guenon]], [[platon]], [[sanatana-dharma]], [[ahl-al-sunnah-wa-l-jamaa]], [[tasawwuf]]
- **Modifié** : `wiki/index.md` (sections perso + general)
- **Supprimé / déprécié** : —
- **Source** : export ChatGPT du 2026-05-10 (`raw/`, non versionné).
- **Étanchéité** : liens uniquement `perso → general` (descendants). Aucun lien retour `general → sidy` créé (remontée interdite sans signalement).
- **Notes** : 140 conversations de l'export **non ingérées** (réserve pour futurs INGEST thématiques : spiritualité, symbolisme, rêves, plantes/santé…). PII (téléphone, e-mail) volontairement exclue ; export brut protégé par `.gitignore`. Les 7 stubs `general` sont à enrichir (`#stub`, `to-source`).

## 2026-06-02 — mise à jour onboarding

- **Opération** : maintenance méta (hors INGEST/QUERY/LINT/COMPARTIMENTALISER)
- **Domaine(s)** : —
- **Créé** : —
- **Modifié** : `schema/onboarding.md` (Obsidian → résolu ; clé API → persistée ; table infra ; prochaines étapes)
- **Supprimé / déprécié** : —
- **Notes** : (1) synchro Obsidian iPad désormais automatique (pull on startup + intervalle). (2) `ANTHROPIC_API_KEY` persistée dans `~/.bashrc` — nettoyage de 4 lignes `export` cassées, une seule conservée ; clé hors repo. Reste à faire : alimenter `raw/`, premier INGEST.
