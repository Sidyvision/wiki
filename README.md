# Wiki

Wiki personnel en français, uniquement du contenu Markdown structuré.

## Structure

- `raw/` — contenus bruts à transformer (notes collées, exports, fichiers sources)
  - `assets/` — pièces jointes (images, PDF, etc.)
- `wiki/` — pages publiées
  - `entities/` — personnes, organisations, lieux, objets
  - `concepts/` — idées, théories, méthodes
  - `sources/` — références citées (livres, articles, vidéos)
  - `analyses/` — synthèses et raisonnements
  - `logs/` — journaux datés
  - `index.md` — sommaire navigable
  - `log.md` — journal des opérations
- `schema/` — gabarits de frontmatter et règles de validation

## Utilisation

Voir [CLAUDE.md](CLAUDE.md) pour les opérations supportées (INGEST, QUERY, LINT, COMPARTIMENTALISER) et le frontmatter obligatoire.
