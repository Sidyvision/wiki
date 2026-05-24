# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Nature du dépôt

Wiki personnel en français. **Aucun build, aucun test, aucun outil** — uniquement du contenu Markdown structuré. Toutes les interactions se font via les quatre opérations ci-dessous. Toute requête de l'utilisateur doit être interprétée comme l'une d'elles ; si l'opération n'est pas évidente, demander avant d'agir.

## Opérations

### INGEST
Transformer un contenu brut (placé dans `raw/`, collé dans le chat, ou pointé par URL) en une ou plusieurs pages wiki conformes.
- Identifier les types (`entity`, `concept`, `source`, `analysis`) et le domaine.
- **Une page par sujet** — ne jamais mélanger deux entités/concepts dans un même fichier.
- Présenter le plan (titres, slugs, domaines, types) avant d'écrire quoi que ce soit.
- Lier systématiquement vers les pages existantes via `[[slug]]`. Si la cible n'existe pas, créer un stub minimal (frontmatter + `#stub` dans `tags`) plutôt qu'un lien mort.
- Citer toute affirmation factuelle dans `sources`.
- Mettre à jour `wiki/index.md` et ajouter une entrée à `wiki/log.md`.

### QUERY
Répondre à une question en s'appuyant **uniquement** sur le contenu du wiki.
- Lire les pages pertinentes avant de répondre — ne pas répondre de mémoire.
- Citer les pages utilisées sous la forme `[[slug]]`.
- Si l'information manque, le dire explicitement et proposer un INGEST.
- Ne pas modifier de pages pendant un QUERY.

### LINT
Vérifier la conformité d'une page, d'un domaine ou de l'ensemble du wiki.
- Frontmatter complet et valide (tous les champs présents, dates ISO).
- Domaine ∈ {recherche, perso, business, lecture, general}.
- Type ∈ {entity, concept, source, analysis}.
- Liens `[[...]]` qui pointent vers des pages existantes.
- `sources` non vide pour toute affirmation factuelle (sinon tag `#stub`).
- Slug du fichier en kebab-case ASCII, sans accents.
- Pas de fuite de domaine (voir COMPARTIMENTALISER).
- Rapporter les violations sans les corriger automatiquement ; demander avant d'éditer.

### COMPARTIMENTALISER
Garantir l'étanchéité entre domaines.
- Une page appartient à **exactement un** domaine.
- Liens autorisés : d'un domaine sensible (`perso`, `business`) vers un domaine moins sensible (`general`, `lecture`, `recherche`). L'inverse doit être explicitement signalé à l'utilisateur.
- Ne **jamais** copier de contenu `perso` ou `business` dans une page d'un autre domaine sans demander.
- En cas de doute sur le domaine d'une nouvelle page, demander avant de créer le fichier.
- Lors d'un INGEST sur du contenu brut mêlant plusieurs domaines : éclater en plusieurs pages, une par domaine.

## Frontmatter YAML obligatoire

Toute page de contenu (`wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/analyses/`, `wiki/logs/`) doit commencer par ce bloc — tous les champs sont obligatoires, même vides :

```yaml
---
title:        # chaîne libre, telle qu'affichée
type:         # entity | concept | source | analysis | log
domain:       # recherche | perso | business | lecture | general
tags: []      # liste de mots-clés en kebab-case
created:      # YYYY-MM-DD, immuable
updated:      # YYYY-MM-DD, mis à jour à chaque modification de fond
sources: []   # liste de [[slug-source]] ou d'URLs
links: []     # liste de [[slug]] vers d'autres pages du wiki
---
```

Les méta-pages `wiki/index.md`, `wiki/log.md`, `wiki/overview.md` ont leur propre frontmatter allégé (`type: meta`).

## Domaines

| Domaine     | Contenu                                                                  |
|-------------|--------------------------------------------------------------------------|
| `recherche` | travaux d'investigation, notes d'étude, articles scientifiques, hypothèses. |
| `perso`     | vie privée, santé, famille, finances personnelles, journal intime.       |
| `business`  | projets professionnels, clients, contrats, stratégie.                    |
| `lecture`   | fiches de lecture (livres, articles, podcasts, vidéos).                  |
| `general`   | définitions générales, références neutres, tout le reste.                |

Le domaine est choisi à la création ; il ne change que par migration explicite (et confirmée par l'utilisateur).

## Format des pages

### Entités — `wiki/entities/<slug>.md`

Un sujet discret : personne, organisation, lieu, produit, événement.

```markdown
---
title: Nom complet de l'entité
type: entity
domain: ...
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
links: [...]
---

# {{title}}

## Identité
Une ou deux phrases qui résument ce qu'est l'entité.

## Faits
- Fait 1 — source : [[slug-source]]
- Fait 2 — source : [[slug-source]]

## Relations
- [[autre-entite]] — nature de la relation.

## Notes
Observations libres, à compléter dans le temps.
```

### Concepts — `wiki/concepts/<slug>.md`

Une idée abstraite, un terme, une définition.

```markdown
---
title: Nom du concept
type: concept
domain: ...
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
links: [...]
---

# {{title}}

## Définition
Une phrase. Pas plus.

## Développement
Explication, distinctions importantes, exemples.

## Concepts liés
- [[concept-x]] — en quoi c'est lié.
- [[concept-y]] — en quoi c'est distinct.

## Sources
Renvoi vers [[source-...]] le cas échéant.
```

### Autres types

- `wiki/sources/<slug>.md` (`type: source`) — référence externe (livre, article, URL), avec auteur, date, accès.
- `wiki/analyses/<slug>.md` (`type: analysis`) — synthèse qui croise plusieurs sources/entités/concepts.
- `wiki/logs/<YYYY-MM-DD>.md` (`type: log`) — événement daté à conserver comme contenu (distinct de `wiki/log.md` qui est le journal opérationnel des sessions).

## Règles absolues

1. **Une page = un sujet.** Ne jamais fusionner deux entités ou deux concepts dans le même fichier.
2. **Pas de page sans frontmatter complet.** Une page incomplète est un échec de LINT, pas un brouillon acceptable.
3. **Aucune affirmation factuelle sans source.** Si la source manque, écrire `to-source` dans `sources` et ajouter `#stub` aux `tags`.
4. **Slugs en kebab-case ASCII**, sans accents ni espaces (`marie-curie.md`, pas `Marie Curie.md`).
5. **Dates en ISO 8601** (`YYYY-MM-DD`). Pas de format français, pas de date relative.
6. **Pas d'écriture sans plan validé.** Lors d'un INGEST, présenter les titres/slugs/domaines avant de créer les fichiers.
7. **Étanchéité des domaines.** Ne jamais l'enfreindre silencieusement — toujours demander en cas de croisement.
8. **`updated` mis à jour à chaque édition de fond.** `created` est immuable.
9. **Journaliser dans `wiki/log.md`** à chaque session : une entrée datée listant créations / modifications / opération exécutée.
10. **Pas de suppression sans confirmation.** Préférer marquer `#deprecated` dans `tags` plutôt que supprimer.

## Méta-pages

- `wiki/index.md` — index global, organisé par domaine puis par type. À tenir synchronisé avec les fichiers réels.
- `wiki/log.md` — journal chronologique inverse des sessions de travail (opérationnel, distinct de `wiki/logs/`).
- `wiki/overview.md` — vue d'ensemble narrative du wiki, mise à jour ponctuellement.

## Structure des répertoires

```
raw/assets/         entrées brutes avant INGEST
schema/             schémas (réservé — non utilisé pour l'instant)
wiki/
  entities/         pages type=entity
  concepts/         pages type=concept
  sources/          pages type=source
  analyses/         pages type=analysis
  logs/             pages type=log (événements datés, contenu)
  index.md          méta : index global
  log.md            méta : journal des sessions
  overview.md       méta : vue d'ensemble
```
