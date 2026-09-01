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
- **`rd/instrument/` et le dépôt frère (scission du 2026-09-01, chantier INF-13)** :
  ce dossier garde la **doctrine, l'architecture, la donnée et le producteur** —
  fiches v0.1/v0.2/v0.3, jalons, mises en regard, `instrument-donnees.yaml`,
  `assets-instrument/`, les triptyques `ins-*/` ; `generer-manifeste.py` reste en
  `rd/outillage/`. Le **rendu** (interface, code Three.js) vit au dépôt frère
  `Sidyvision/instrument` (privé). Ligne de coupe : producteur/consommateur, jamais
  Instrument/reste — c'est le sens unique `dépôt → manifeste → interface` du §VII
  racine (règle 5) exprimé en infrastructure. Le manifeste est **poussé d'ici**,
  jamais tiré de là-bas ; le dépôt frère n'a aucun droit d'écriture sur ce dépôt et
  n'y établit aucune correspondance (Cmd 3, Cmd 12). Aucune fiche n'a été supprimée :
  `instrument-prototype.html` subsiste en stub `deprecated` avec pointeur (Cmd 10).
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

**Dossiers de chantier — règle AJOUTÉE le 2026-09-01** (verdict Sidy, ouverture du
triptyque `intent`/`spec`/`plan`). Il ne s'agit pas de la clarification d'une règle
préexistante : la nomenclature ci-dessus est de forme plate et **muette** sur les
dossiers imbriqués. Le §II bis du protocole racine voulant que ce fichier porte la
lettre complète des règles propres au circuit, l'ajout est daté et signalé comme tel
— la version monolithique archivée du 2026-08-12 ne peut pas en rendre compte.

Un chantier d'ingénierie du pôle `rd/` qui passe de *recensé* à *instruit* reçoit un
dossier dans son domaine, nommé par son identifiant de registre en minuscules :

```
atelier/rd/<domaine>/<id-en-minuscules>-<slug>/
├── intent.md   ← pourquoi
├── spec.md     ← quoi
└── plan.md     ← comment
```

Exemple : `atelier/rd/instrument/ins-02-axe-unifie/`. Les trois fichiers portent des
noms nus, le dossier les désambiguïse. Précédent de sous-dossier dans ce circuit :
`assets-instrument/`. La lettre complète du triptyque — périmètre, modèles des trois
fiches, clause de non-emprunt au lexique Sashimono — vit dans
`atelier/rd/outillage/gabarit-triptyque-chantier.md` ; le pointeur vers chaque dossier
est porté par la ligne du chantier dans `atelier/rd/registre-chantiers.md`.

**Rapport au Cmd 6** (« pas d'écriture sans plan validé ») : pour un chantier
d'ingénierie `rd/`, **le `plan.md` visé par Sidy *est* le plan du Cmd 6**. Aucune
obligation nouvelle n'est créée ; une obligation existante reçoit une forme
consultable à froid. Tant qu'un `plan.md` n'est pas visé, aucun code n'est écrit pour
ce chantier.

Les fichiers `spec-<slug>.md` déjà présents en `rd/outillage/` et `rd/instrument/`
sont **conservés en place** et adoptés par pointeur au fil de l'eau, chantier par
chantier : aucun renommage de masse (Cmd 10, réversibilité).

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
- **`chantier` (champ optionnel, ouvert 2026-09-01)** : identifiant de registre
  (`chantier: INS-02`) reliant une fiche à sa ligne dans
  `atelier/rd/registre-chantiers.md`. Obligatoire sur les trois fiches d'un dossier
  de chantier (voir Nomenclature), facultatif ailleurs. Même précédent d'amendement
  du Sceau que `statut_experience` et `infra_verif`.
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
