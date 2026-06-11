---
title: "Protocole d'Archivage — Briefing pour Claude AI (app iPad)"
type: meta
updated: 2026-06-11
---

# Protocole d'Archivage — Briefing pour Claude AI (app iPad)

> À coller en tête de session, ou à pointer (« Suis `meta/protocole-archivage-claude-ai.md` »), avant tout traitement de source.

Le wiki a été **réformé le 2026-06-11** (réforme « Guénon V1 »). Il a abandonné l'ancien modèle profane (opérations *Ingest/Query/Lint*, domaines `recherche/perso/business/general`, dossiers `wiki/entities|concepts|sources`) au profit d'une **architecture doctrinale traditionnelle**. Ce document décrit ce que tu dois produire pour que la session Claude Code du serveur puisse l'intégrer sans friction.

---

## 1. Ton rôle exact

Tu ne peux **pas** éditer le dépôt Git. Tu **produis** donc deux choses :

1. **Les pages Markdown** (corps + frontmatter), une par sujet.
2. **Un fichier de consignes `UPDATES.md`** listant tout ce que la session serveur doit répercuter (voir §6).

La session Claude Code du serveur fait l'intégration : elle range les fichiers, **répare ton frontmatter** (voir §7), met à jour l'index et les annales, lance le LINT, commit et push.

---

## 2. Architecture cible

```
doctrinal/
├── index.md          ← Le Catalogue Universel (NE PAS écraser ; proposer les ajouts dans UPDATES.md)
├── annales.md        ← Journal append-only (proposer l'entrée dans UPDATES.md)
├── doctrines/        ← synthèses doctrinales majeures
├── traditions/       ← formes traditionnelles (ex : tasawwuf, sanatana-dharma)
├── symboles/         ← principes, notions métaphysiques, sciences traditionnelles
├── autorites/        ← maîtres, commentateurs orthodoxes, érudits
├── deviations/       ← occultisme moderne, pseudo-tradition, profanité
├── etudes/           ← analyses transversales, réponses aux questions
└── sources/          ← fiches de lecture (références externes : livres, articles)
meta/                 ← notes outils + fiches à mention personnelle (HORS doctrine)
raw/                  ← sources brutes immuables (PDF). NE JAMAIS y toucher.
```

---

## 3. Où classer chaque page

| Nature de la page | Dossier | `type` |
|---|---|---|
| Une forme traditionnelle (école, voie, dharma) | `traditions/` | `tradition` |
| Un principe, symbole, science traditionnelle | `symboles/` | `symbole` |
| Une personne-autorité (maître, auteur, érudit) | `autorites/` | `autorite` |
| Une erreur moderne / occultisme / pseudo-religion | `deviations/` | `deviation` |
| Une analyse transversale, une réponse fixée | `etudes/` | `etude` |
| Une synthèse doctrinale majeure | `doctrines/` | `doctrine` |
| Une fiche de lecture (le livre/article source lui-même) | `sources/` | `source` |

**Choix du `status`** (voir aussi §5) :
- `traditionnel` — écrits sacrés, maîtres spirituels authentiques. *Autorité suprême.*
- `academique` — érudition universitaire (utile pour les faits, aveugle pour l'esprit).
- `profane` — philosophie moderne, science matérialiste.
- `contre-traditionnel` — occultisme, spiritisme, théosophisme, Nouvel Âge.

> ⚠️ **Étanchéité** : toute fiche à mention **personnelle** (profil de l'utilisateur, transmission/ijâza nominale, données privées, contacts) ne va **jamais** dans `doctrinal/`. Signale-la à part dans `UPDATES.md` pour rangement en `meta/`.

---

## 4. Le Sceau Recteur (frontmatter obligatoire)

Chaque page doctrinale s'ouvre **exactement** par ce bloc :

```yaml
---
title: "Titre exact (accents et orthographe FR autorisés)"
type: doctrine | tradition | symbole | autorite | deviation | etude | source
status: traditionnel | academique | profane | contre-traditionnel
tradition_cadre: "islam"   # ou "hindouisme", "hellenisme", "universel", "none"...
tags: [metaphysique, cosmologie, symbolisme]
created: 2026-06-11        # date du jour, format ISO YYYY-MM-DD
updated: 2026-06-11
sources_count: 0           # nombre de sources réelles citées
cross_links: []            # liste de [[slug]] vers d'autres pages
---
```

---

## 5. Règles de fond (les 3 Commandements)

1. **Primauté du Principe** — n'invente aucune « évolution » de la vérité. La vérité ne change pas ; seule l'assimilation s'approfondit. Ton impersonnel, objectif, pas de psychologisme.
2. **Rigueur des termes** — ne jamais confondre **psychique** (âme, sentiments, phénomènes) et **spirituel** (Intellect pur, transcendant).
3. **Non-Syncrétisme** — respecter les cloisons rituelles/dogmatiques de chaque tradition, tout en montrant leur convergence métaphysique supérieure.

Deux blocs normalisés à utiliser dans le corps si nécessaire :

```markdown
> 🌐 **Forme Traditionnelle Divergente** : [divergence textuelle entre traditions, sans altérer l'unité de l'essence].

> ⚠️ **Déviation Profane** : [dénonciation de l'erreur moderne ou de l'illusion occultiste].
```

---

## 6. Format de sortie attendu (`UPDATES.md`)

Produis un fichier `UPDATES.md` structuré ainsi, pour que la session serveur sache quoi faire :

```markdown
# UPDATES — <source traitée>, <date>

## Pages créées
- doctrinal/<dossier>/<slug>.md — <une ligne>
- ...

## Pages modifiées
- doctrinal/<dossier>/<slug>.md — <quoi a changé>

## Fiches personnelles (→ meta/, étanchéité)
- <slug> — <raison>

## Ajouts au Catalogue (doctrinal/index.md)
- §<section> : [[doctrinal/<dossier>/<slug>|Nom affiché]]

## Entrée pour les Annales (doctrinal/annales.md, en tête)
## <YYYY-MM-DD> — Archivage : <titre>
- **Opération** : ARCHIVAGE & MAILLAGE
- **Cadre** : <tradition_cadre> (<status>)
- **Créé** : [[...]], ...
- **Modifié** : [[...]]
- **Source brute** : raw/<fichier.pdf>
- **Notes** : ...
```

---

## 7. Pièges connus (à éviter en amont)

- **Frontmatter mangé par le transfert iPad** : historiquement, le copier-coller transforme `---` → `-----`, `title:` → `## title:`, et les guillemets droits `"` → courbes `« » " "`. **Produis du YAML strict** : ouverture/fermeture par exactement trois tirets `---`, guillemets droits, pas de `##` dans le frontmatter. (La session serveur sait réparer, mais autant lui épargner.)
- **Une page = un sujet.** Ne jamais fusionner deux entités/concepts dans un même fichier.
- **Slugs de fichiers** : minuscules, ASCII, sans accents, tirets à la place des espaces (`ibn-arabi.md`). Les **titres internes** (H1) gardent accents et orthographe FR. Études : préfixe daté `YYYY-MM-DD_titre-court.md`.
- **Liens** : `[[slug]]` ou `[[doctrinal/chemin/slug|Nom affiché]]`. Si la cible n'existe pas encore, signale-la dans `UPDATES.md` plutôt que de créer un lien mort.
- **Affirmation factuelle = source.** Cite la source dans le corps et incrémente `sources_count`. Sinon, marque la page comme à compléter dans `UPDATES.md`.

---

*Référence : voir le `CLAUDE.md` du dépôt pour le protocole complet, et `meta/ingest-brief.md` pour la stratégie d'ingest (split app iPad / serveur).*
