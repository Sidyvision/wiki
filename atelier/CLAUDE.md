بسم الله الرحمن الرحيم

# CLAUDE.md — Protocole local : circuit `atelier/`

> **Statut : méthode à l'essai** (éclatement expérimental du 2026-08-12, verdict
> Sidy). Ce fichier porte la lettre complète des règles **propres** au circuit
> `atelier/` — Sceau, nomenclature, règles de liens, spécificités `rd/`. Les règles
> **transversales** (étanchéité inter-circuits, discipline des sources, double
> contrôle sashimono/Gizeh, commandements absolus, supervision des agents) restent
> dans le `CLAUDE.md` racine, **toujours chargé** quel que soit le dossier de
> travail — ce fichier ne s'y substitue pas, il le complète. En cas de doute ou de
> silence de ce fichier sur un point, le `CLAUDE.md` racine fait foi. Version
> pré-éclatement intégrale : `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md`.

-----

## Structure du circuit

- `materiel/` — Manuels, fiches machines, fiches routing (RÉFÉRENCE).
- `entretiens/` — Interviews de métier (RÉFÉRENCE).
- `etudes-de-cas/` — études de maisons/marques/structures (RECHERCHE comparative).
- `projets/` — **Résiduel** : stubs `deprecated` uniquement, 16 fiches migrées vers
  `rd/` + `album-personnel` (vers `label/`) le 2026-08-08. Ne plus y créer de fiches.
- `rd/` — RECHERCHE & DÉVELOPPEMENT (pôle ouvert 2026-08-08) : `instrument/` ·
  `infrastructure/` · `audio/` · `outillage/` · `cahiers/` · `bibliotheque/`
  (2026-08-22) · `veille/` (2026-08-18) · `incidents/` (2026-08-22) ·
  `citadelle-du-sham/` (2026-08-22). Charte : `rd/index.md`. Carte vivante des
  chantiers : `rd/registre-chantiers.md` (ouvert 2026-09-01).
  Finalité de **souveraineté** : consignation systématique de l'infrastructure
  globale hardware/software, en vue de son entretien, de son développement
  qualitatif, de son optimisation à mesure, et de l'émancipation progressive de
  tout intermédiaire de service tiers.

## Nomenclature

`atelier/<sous-dossier>/<slug>.md` ; études de cas : `atelier/etudes-de-cas/<slug>.md`,
langue selon le framework. Fichiers en minuscules, ASCII, sans accents, tirets `-`.
**Une page = un sujet.**

## Le Sceau atelier

```yaml
---
title: "Titre exact"
type: materiel | manuel | entretien | projet | etude-de-cas | experience | infrastructure | outillage
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
links: []
---
```

- `materiel/` et `entretiens/` ne lient JAMAIS vers `doctrinal/` (ni l'inverse).
- `projets/` et `rd/` PEUVENT pointer vers `doctrinal/` en **sens unique**, tout
  lien signalé. L'inverse est INTERDIT : aucune page doctrinale ne mentionne
  jamais un projet ni une fiche `rd/` (l'Instrument inclus).
- **`rd/` (pôle R&D, ouvert 2026-08-08)** : pour les fiches de régime
  expérimental, champ optionnel `statut_experience: exploratoire | reproduit |
  adopte | abandonne` — la discipline de laboratoire complète (bloc 🧪 Expérience,
  reproduction, cahiers) est ouverte en phase 2. Les types
  `experience | infrastructure | outillage` vivent en `rd/`.
- `rd/infrastructure/` reçoit ce qui est **publiable dans le dépôt** (architecture
  générique, bancs, mesures) — jamais de fait personnel dans une page neutre
  (ce qui est sensible reste en `meta/projet-unifie/`, voir `meta/CLAUDE.md`).
- **`infra_verif` (champ optionnel, ouvert 2026-08-17)** : pour les fiches
  `type: infrastructure` qui documentent une action de configuration Hermes/
  Discord effectivement appliquée (pas seulement planifiée), une liste YAML en
  frontmatter permet la vérification mécanique indépendante de l'affirmation
  narrative de la fiche — motif : `atelier/rd/cahiers/registre-problemes.md`,
  entrée `[2026-08-17]`, une fiche avait affirmé la création d'un job cron
  jamais réellement créé. Champs reconnus par item (au moins un requis) :
  `profil` (obligatoire, nom du profil Hermes), `cron_job` (nom du job attendu),
  `discord_home_channel` (ID numérique attendu), `discord_allowed_channels`
  (liste d'ID numériques attendus, sous-ensemble accepté). Vérifié par
  `atelier/rd/outillage/verifier-coherence-infrastructure.py` (déterministe,
  sans LLM, même famille que `verifier-invariants.py`) :
  ```yaml
  infra_verif:
    - profil: studio
      cron_job: monitoring-infrastructure-quotidien
      discord_home_channel: "1536564394690084925"
  ```

## Journalisation

Annales du circuit : `atelier/annales.md`, y compris le pôle `rd/` — préfixe
greppable `## [YYYY-MM-DD] op | Titre`, une entrée par passe groupée, SHA court du
commit en dernière ligne (Cmd 9 du protocole racine).
