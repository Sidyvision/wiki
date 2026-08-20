---
title: "Rapport conjoint Studio–Gardien — étude du dépôt (2026-08-20)"
type: rapport-conjoint
date: 2026-08-20
statut: remis-a-inbox
cible: Sidy
cosignataires:
  - "Studio (R&D, exploration)"
  - "Gardien (vigilance, contrôle protocolaire)"
---

# Rapport conjoint Studio–Gardien — étude du dépôt

**Date :** 2026-08-20
**Cosignataires :**
— **Studio** (pôle R&D, rôle exploration & documentation)
— **Gardien** (pôle Vigilance, rôle contrôle protocolaire & signalement)

**Points de départ communs :** `CLAUDE.md` racine (protocole V2, Restauration
étendue, rév. 2026-08-12) · fiche des trois territoires
(`doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md`,
`status: adopte`) · exploration structurelle du dépôt · inventaire de `raw/`.

**Posture conjointe :** exploration, consignation et contrôle. **Aucun verdict
rendu** — toute qualification métaphysique, tout arbitrage engageant, est réservé
à Sidy (Cmd 12, et Cmd 13 pour la porte humaine sur ce qui engage). Ce rapport
documente et signale ; il ne tranche pas.

**Chaîne de production :** ce rapport unifie (a) le rapport d'exploration
préliminaire de Studio (`_inbox/rapport-studio-exploration-preliminaire.md`,
commit `8713e52`), (b) la fiche d'étude R&D
(`atelier/rd/infrastructure/etude-depot-cartographie-inventaire-raw-2026-08-20.md`,
commit `6d0d43c`) et (c) la fiche de préparation du Gardien
(`atelier/rd/infrastructure/rapport-conjoint-etat-depot-2026-08-20.md`,
commit `c8809a9`). Il s'y substitue comme document de référence unique pour la
session du 2026-08-20.

---

## 1. Introduction

### 1.1 Objectifs

1. **État des lieux du dépôt** — cartographie des circuits, du pôle R&D et de
   l'outillage déterministe ; état des vérifications mécaniques.
2. **Examen de `raw/`** — inventaire et classification des ressources brutes,
   signalement des dépôts du jour non encore qualifiés.
3. **Contrôle protocolaire (pôle Vigilance)** — étanchéité des circuits,
   conformité des Sceaux, discipline des sources, intégrité du flux
   Discernement → R&D → Doctrine, convention des annales.
4. **Recommandations conjointes** — priorités soumises à Sidy, aucune exécution.

### 1.2 Méthodologie

- **Lecture préalable** du protocole racine et des protocoles locaux (§II bis),
  de la fiche des trois territoires (cadre du flux), des rapports amont.
- **Vérification mécanique indépendante** (règle §VIII.2 : fiabilité d'action ≠
  fiabilité narrative) : le pôle Vigilance a **rejoué** les scripts déterministes
  (`verifier-invariants.py`, `Graphe/generer-cartographie.py --verifier`) plutôt
  que de reconduire l'auto-rapport de Studio. Les chiffres ci-dessous sont les
  chiffres **mesurés au moment de la rédaction conjointe**.
- **Inspection git** : `git status`, `git log`, avance sur `origin`.
- **Contrôle d'étanchéité** : recherche dirigée des références inter-circuits
  interdites, puis qualification de chaque occurrence (wikilink actif vs mention
  en prose vs exception défensive signalée).

### 1.3 Périmètre et limites

- **Aucune modification hors `_inbox/` et `rd/`** (contrainte de session). Le
  présent rapport est déposé dans `_inbox/` et n'écrit dans aucun circuit.
- L'inventaire de `raw/` s'appuie sur les **métadonnées** (noms, tailles, dates) ;
  l'extraction de texte PDF n'a pas été tentée en session. Les deux dépôts du jour
  restent donc non qualifiés (point ouvert n°7).
- **Aucun commit ni push** n'a été effectué pour ce rapport : l'opération
  d'intégration (commit/push) est une porte humaine (§IX étapes 5-6, Cmd 13),
  laissée à la discrétion de Sidy.

---

## 2. État des lieux du dépôt (synthèse R&D)

### 2.1 Structure générale et cartographie des circuits

Le dépôt (`/root/wiki`, remote `git@github.com:Sidyvision/wiki.git`, branche
`main`) suit le protocole V2 : **cinq circuits étanches** (`doctrinal/`,
`atelier/`, `label/`, `hermeneutique/`) plus le Domaine Réservé `meta/` (qui
n'est **pas** un sixième circuit), et des lieux transversaux (`_inbox/`, `raw/`,
`Graphe/`, scripts racine).

Comptages `.md` constatés au 2026-08-20 (fichiers de contenu, `.venv` exclu) :

| Circuit | .md | Index | Annales (dern. entrée) | Remarque |
|---|---|---|---|---|
| **doctrinal** | 260 | `index.md` | à jour, 2026-08-20 (lot kabbale) | le plus volumineux |
| **meta** | 118 | `meta-index.md` | 2026-08-16 | Domaine Réservé, pas un circuit |
| **atelier** | 92 | `index.md` | à jour, 2026-08-19 | contient le pôle `rd/` |
| **hermeneutique** | 22 | `index.md` | 2026-08-16 en tête ; +9 lignes non committées | `expression/` nouveau |
| **label** | 13 | `index.md` | 2026-08-08 | le moins peuplé, le plus ancien sans activité |

**Observations par circuit (synthèse R&D de Studio) :**
- **doctrinal** : très actif — lot kabbale du 2026-08-20 (Sefer Yetsira Ramban +
  Traité Émanation Gauche + état des lieux kabbale + amorce de rapprochement
  Palais de la Sainteté / ḥaḍarāt).
- **hermeneutique** : le nouveau sous-dossier `expression/` (registre créé par la
  fiche des trois territoires) contient sa première fiche
  (`2026-08-20_barzakh-onirique-interface-litteraire.md`), **non committée**.
- **label** : annales les plus anciennes (2026-08-08) ; 13 fiches — statut
  opératif (production/distribution) plutôt que documentaire.
- **meta** : les 12 hermes-prompts d'agents sont présents et nommés
  (01-ar-music → 12-commerce-profitability).

### 2.2 Le pôle R&D (`atelier/rd/`)

Ouvert 2026-08-08 sur verdict (Option C). Mission : consignation systématique de
tout travail d'ingénierie ; finalité de **souveraineté** (entretien,
optimisation, émancipation progressive des intermédiaires de service tiers).
68 fichiers `.md` répartis en six sous-pôles :

- `instrument/` — 16 fiches migrées de `projets/` + specs (anneau zodiacal,
  axe 38°, prototype html, donnees.yaml, manifest).
- `infrastructure/` — 14 fiches + projet `bureau/` (TUI : app.py + modules +
  services + tests) + `monitoring-archive/` (rétention 40 j, 3 archives 08-17/18/19).
- `audio/` — vide (`.gitkeep`), bancs d'essai génériques à venir.
- `outillage/` — scripts déterministes + fiches méthode/spec + `.snapshots-rd/`.
- `veille/` — ouvert 2026-08-18 : `cordis/` (équations, méthodes,
  implémentations-github, notes-lecture), index, registre.
- `cahiers/` — `registre-problemes.md` (append-only, ~1200 lignes), bilan
  pont-agents 2026-08-15, 12 brouillons extension zodiacale, 2 propositions.

### 2.3 Outillage déterministe (famille `verifier-invariants.py`)

Scripts déterministes, ni LLM ni réseau : `detecter-non-tracke.py`,
`archiver-monitoring-quotidien.py`, `verifier-coherence-infrastructure.py`,
`generer-manifeste.py`, plus deux enveloppes `-cron.sh` (arguments fixés en dur —
leçon tirée du bug des jobs `no_agent` qui ne transmettent aucun argument).
Racine : `verifier-invariants.py` (vérificateur d'invariants) et
`carte-du-depot.py`. `Graphe/generer-cartographie.py` génère la vue cartographique
(avec garde `--verifier` bloquante sur frontmatter).

### 2.4 Vérifications mécaniques rejouées (2026-08-20)

**`verifier-invariants.py --racine /root/wiki` → 18 erreurs, 62 avertissements.**

- **Erreurs C1 (18)** : 16 proviennent d'**un seul fichier**,
  `rd/infrastructure/traitement-avertissements-isoles-rapport-2026-08-18.md`, dont
  les motifs d'exemple entre doubles crochets sont lus comme liens réels —
  **auto-pollution déjà consignée** au registre-problèmes (entrée 2026-08-18).
  Restent 2 C1 réels : `doctrinal/annales.md` (crochets vides) et
  `doctrinal/autorites/rene-guenon.md` (lien non résolu).
- **Avertissements (62)** — décomposition mesurée ce jour :
  - **B1 ×15** : clés de frontmatter manquantes sur les **3 fiches du lot kabbale**
    (`status`, `tradition_cadre`, `created`, `updated`, `sources`, et `type` pour
    l'une) — Sceau Recteur incomplet.
  - **B0 ×1** : `rd/infrastructure/analyse-temporelle-code-meta-raisonnement-ia-2026-08-19.md`
    — **aucun frontmatter** du tout.
  - **A2 ×1** : `hermeneutique/annales.md` — **rupture d'ordre** : l'entrée
    2026-08-20 apparaît après 2026-08-04 (ligne 270). Convention attendue : plus
    récent en haut. Signature d'une insertion en **queue** au lieu de l'en-tête.
  - **A3 ×2** : `doctrinal/annales.md` et `hermeneutique/annales.md` —
    `updated:` antérieur à l'entrée la plus récente (2026-08-20). Cmd 8.
  - **A5 ×1** : `atelier/annales.md:518` — double ligne vide avant un séparateur,
    signature possible d'un ajout mécanique en fin de fichier plutôt qu'une
    insertion en en-tête.

> **Note de convergence (Vigilance)** : le rapport de Studio comptait
> **58 avertissements** plus tôt dans la journée ; la passe conjointe en mesure
> **62**. La dérive (+4 : A2 + A3×2 + A5) est imputable aux **écritures non
> committées du jour dans les annales** (lot islamofuturisme + entrée atelier),
> survenues entre les deux mesures. Ce n'est pas une contradiction entre les deux
> pôles, c'est la trace mécanique d'un lot en cours.

**`Graphe/generer-cartographie.py --verifier` → 4 anomalies bloquantes
(frontmatter), confirmées à l'identique par le pôle Vigilance :**

| Fichier | Champs manquants |
|---|---|
| `doctrinal/discernement/2026-08-20_traite-emanation-gauche-isaac-ha-kohen.md` | status, created, updated (+ tradition_cadre, sources) |
| `doctrinal/sources/sefer-yetsira-ramban_source.md` | status, updated (+ tradition_cadre, sources) |
| `doctrinal/sources/traite-emanation-gauche-isaac-ha-kohen_source.md` | type, status, updated (+ tradition_cadre, sources) |
| `rd/infrastructure/analyse-temporelle-code-meta-raisonnement-ia-2026-08-19.md` | frontmatter absent |

Les trois premières concernent le lot kabbale du jour ; la quatrième une fiche
veille de la veille. **Ces 4 anomalies bloquent l'écriture du manifeste** de
cartographie.

**Autres contrôles (fiche de préparation Gardien) :**
- **Bureau TUI** : `pytest tests/` dans le venv du projet → **10 passed**.
  Cohérent avec le bilan pont-agents du 08-15.
- **Cron** : 3 jobs actifs et sains (profil studio) —
  `monitoring-infrastructure-quotidien` (12:00), `coherence-infrastructure-brute`
  (12:05, no-agent, réparé le 08-18), `archiver-monitoring-quotidien` (12:10,
  rétention 40 j). Tous en `last run: ok` au 08-19.
- **Sandbox** : `/root/sandbox-rd/` **existe mais est vide** (l'étude du jour le
  disait absent — correction apportée par la préparation Gardien : le dossier
  existe, aucun contenu).

### 2.5 État git

- Remote : `git@github.com:Sidyvision/wiki.git`, branche `main`.
- **Working tree non propre** — lot islamofuturisme du jour en cours :
  `M doctrinal/annales.md`, `M hermeneutique/annales.md`,
  `?? doctrinal/sources/elbenni-dreaming-ummah-islamofuturism-2025.md`
  (fiche source complète, Sceau conforme),
  `?? hermeneutique/expression/` (fiche barzakh onirique).
- **Branche en avance de 3 commits sur `origin`, non poussés** :
  `6d0d43c` (étude du dépôt), `c8809a9` (préparation Gardien + annales atelier),
  `8713e52` (rapport Studio à inbox).
- Le lot kabbale est committé (`2b97608`, `72345a9`, `edfc0ad`) mais ses 3 fiches
  gardent des frontmatter incomplets (anomalies bloquantes ci-dessus).

---

## 3. Examen de `raw/` (ressources nouvelles, classification)

**Volume :** 444 fichiers — 392 `.md`, 45 `.pdf`, 3 `.jpeg`, 1 `.sh`, 1 `.html`,
1 `.gitkeep`, 1 répertoire « ChatGPT historique ». ≈ 328–392 Mo selon mesure.

### 3.1 Corpus Guénon (sous-dossiers thématiques)

16 dossiers correspondant aux ouvrages, format transcriptions `.md` par chapitre
+ index de l'œuvre (≈392 fichiers), organisés par `raw/organize_guenon.sh`
(2026-08-13). Du plus fourni au plus mince : Le Théosophisme (68), Aperçu sur
l'initiation (52), Le Règne de la Quantité (44), Études sur l'Hindouïsme (39),
Initiation et Réalisation Spirituelle (34), Le Symbolisme de la Croix (31), La
Grande Triade (28), Les Principes du Calcul Infinitésimal (26), Les états
multiples de l'être (20), Aperçus sur l'Ésotérisme islamique et le Taoïsme (14),
Le Roi du Monde (12), La Crise du Monde Moderne (9), Autorité Spirituelle et
Pouvoir Temporel (7), Autres ressources (4).

**Anomalie :** dossier **doublon** « Autorité Spirituelle et Pouvoir Temporel »
(avec espace en fin de nom, 2 fichiers) à côté du dossier canonique (7 fichiers).

### 3.2 Ressources nouvelles (août 2026)

**Nature doctrinale / sources primaires :**

| Fichier | Date | État |
|---|---|---|
| `sefer_yetsira_-_Ramban.pdf` + `.md` | 2026-08-20 | intégré (fiche source + état des lieux kabbale) |
| `traite-emanation-gauche-isaac-ha-kohen.md` | 2026-08-20 | intégré (lot kabbale, annales du jour) |
| `Hashiya-Issue-01-Elbenni.pdf` | 2026-08-20 07:11 | fiche source créée, **non committée** |
| `maymaniya_p1.pdf` (≈67 Mo) | 2026-08-20 08:09 | **nature non examinée** |
| `claudes-constitution.pdf` (≈1 Mo) | 2026-08-20 08:11 | **nature non examinée** |
| `Large_language_models_for_automated_Isla.pdf` | 2026-08-10 | papier académique LLM/islam, non fiché |
| `islam-and-artificial-intelligence.pdf` | juin | idem, plus ancien |
| `religions-16-00549-with-cover.pdf` | — | non fiché |
| `LA FIN DES TEMPS MODERNES` (astrologie traditionnelle) | — | non fiché |

**Nature spirituelle / rituelle (juin) :** Awrad Ibn Arabi, Wazifa, Dua Laylatul
Qadr, Salat al-Kaffarat, Prayer 15th Shabān, مولد الرسول الأعظم, إجازة-94/95,
Al-Hadj-Cheikh-Belmadi-2017, shams-al-maarif (58 Mo), universal-man,
Jesus_And_Enoch_In_Ibn_'arabi.

**Nature ingénierie / R&D :**
- `A Programming Paradigm for Spatiotemporal Composability.pdf` (2026-08-16) —
  paradigme Cordis, déjà en veille (`rd/veille/cordis/`).
- Manuels studio (juin) : 1073SPX (notice + traduit), Model12 (OM EFS RevH3),
  Revox A77 ×3, distressor, Logic Pro iPad.
- 2 factures Woodbrass (2026-08-18) : Tascam Model12, Neve 1073SPX — nature
  administrative.
- `organize_guenon.sh` — script logé en `raw/` ; la charte `rd/` destine les
  scripts déterministes à `rd/outillage/`. Déplacement à la discrétion de Sidy.

**Nature herméneutique / culture :**
- `TheArtOfDeathStranding(Ru-TO-Eng).pdf` (62 Mo, 2026-08-13) — déjà fiché
  (`hermeneutique/death-stranding/art-of-death-stranding`).
- `Interview with Russell Elevado - Gearspace.pdf` — herméneutique du mix,
  candidat `hermeneutique/` ou `label/`, à qualifier.

**Nature enseignement / logique :** Isaghuji ×3 (dont Cours01 2026-08-11
« Introduction Pédagogique — Mehdi »), Intro to Logic (Zaytuna College),
Intro_to_Logic-FULL.

**Nature administrative / personnelle (signalée, hors circuit) :** relevés de
compte ×7 + relevé annuel de frais au nom de Sidy, `ChatGPT historique` (41 Mo),
`Body_Types_Book.pdf`, `grr-academix-2026.pdf`. Maintien en `raw/` à la
discrétion de Sidy.

### 3.3 `raw/assets/`

4 fichiers : `routing-schema.html`, `studio-principal-vue-generale.jpeg`,
`theme-natal-sidy-astrodienst-2026-08-08.jpeg`, un jpeg sans nom descriptif.
**Le thème natal est une donnée personnelle sensible.**

---

## 4. Points ouverts et anomalies (table conjointe)

| # | Point | Gravité | Nature |
|---|---|---|---|
| 1 | Frontmatter incomplet — 3 fiches du lot kabbale (Sceau Recteur) | **bloquante** | mécanique / Sceau |
| 2 | Fiche veille 2026-08-19 sans frontmatter | **bloquante** | mécanique |
| 3 | Lot islamofuturisme non committé (4 éléments git) | en cours | workflow |
| 4 | `hermeneutique/annales.md` — rupture d'ordre A2 (entrée 08-20 insérée en queue au lieu de l'en-tête) | moyenne | convention d'insertion |
| 5 | `UPDATES.md` / `MASTER-UPDATE.md` référencés par le protocole mais absents du dépôt | moyenne | référence morte / cohérence |
| 6 | `/root/sandbox-rd/` existe mais **vide** — athanor non éprouvé à ce jour | moyenne | cohérence doc/runtime |
| 7 | `maymaniya_p1.pdf` + `claudes-constitution.pdf` (dépôts du jour) non qualifiés | à qualifier | raw/ |
| 8 | Documents bancaires + thème natal en `raw/` — maintien à la main de Sidy | discrétion | données personnelles |
| 9 | `atelier/R/` — dossier vide, homonyme de `rd/` | basse | clarification |
| 10 | Doublon dossier « Autorité Spirituelle et Pouvoir Temporel » (espace finale) | basse | hygiène |
| 11 | `organize_guenon.sh` logé en `raw/` au lieu de `rd/outillage/` | basse | convention |
| 12 | Branche `main` en avance de 3 commits sur `origin`, non poussée | basse | git |
| 13 | Annales `doctrinal`/`hermeneutique` : `updated:` non remontés (A3 ×2) | basse | Cmd 8 |
| 14 | `atelier/annales.md:518` — signature d'ajout mécanique en fin de fichier (A5) | basse | convention d'insertion |
| 15 | Rapport d'avertissements auto-polluant (16/18 erreurs C1) — déjà au registre | documentée | outillage |
| 16 | Formulation inversée du sens de lien dans `symboles/manvantara.md` (« doctrinal → projet ») | basse | rigueur des termes / à clarifier |
| 17 | `doctrinal/index.md` liste des joints vers `hermeneutique/` (sens en principe interdit) | basse | zone grise / à clarifier |
| 18 | Caractère invisible U+200D (ZWJ) dans « H‍ermes » — 150+ occurrences dans tous les circuits ; convention stylistique du dépôt, mais signalée comme « injection potentielle » par les gardes de lecture d'agents | basse | convention à documenter / faux positif outillage |

**Rappel de lecture :** les gravités sont des qualifications de travail, pas des
verdicts. Les points « bloquants » le sont **mécaniquement** (ils empêchent la
régénération du manifeste de cartographie), pas doctrinalement.

---

## 5. Section Vigilance (contrôle protocolaire)

Le pôle Gardien a procédé aux contrôles suivants, indépendamment de l'auto-rapport
de Studio. Posture : **signalement, jamais décision.**

### 5.1 Étanchéité des circuits (§VI)

Recherche dirigée des références interdites (doctrinal → hermeneutique, doctrinal
→ meta, doctrinal → atelier/rd, tout circuit → meta), puis qualification de
chaque occurrence.

**Résultat : aucune violation active de lien constatée.** Les occurrences relevées
se répartissent en trois catégories conformes ou à clarifier :

- **Mentions en prose (backticks), sans wikilink actif** — ex.
  `traditions/madhhab-maliki.md` citant `meta/bibliotheque-physique.md`
  (conforme à la discipline des sources : bibliothèque physique d'abord) ;
  `symboles/manvantara.md` et `discernement/2026-07-26_zodiaque-fonction-barzakh.md`
  citant des fiches `rd/instrument/` en prose.
- **Exceptions défensives / généalogiques signalées** — ex.
  `discernement/2026-08-12_nen-pacte-restriction-ascetique.md`, qui porte un
  « Rappel de cadrage (Cmd 3) » explicite : le joint part de `hermeneutique/`
  vers `doctrinal/`, hozo exclu. Conforme à la lettre du protocole.
- **Deux zones grises à clarifier (sans verdict) :**
  - **(a)** `doctrinal/index.md` tient une section « Herméneutique — joints
    ouverts depuis `hermeneutique/` » qui référence des fiches du circuit
    herméneutique. Le protocole pose `doctrinal/` → `hermeneutique/` : **jamais**.
    S'agit-il d'une exception d'index (hub de navigation) ou d'un écart ? À
    qualifier par Sidy.
  - **(b)** `symboles/manvantara.md` formule le sens du lien ainsi : « Lien à
    sens unique uniquement (**doctrinal → projet**), jamais l'inverse ». Or le
    protocole (§VI et `doctrinal/CLAUDE.md`) autorise le sens inverse :
    `rd/` → `doctrinal/` en sens unique, `doctrinal/` → `rd/` étant interdit.
    La **formulation est inversée** par rapport à la lettre. Rigueur des termes
    (Cmd 2) ; à corriger ou à clarifier.

### 5.2 Conformité des Sceaux

- **3 fiches du lot kabbale intégrées avec Sceau Recteur incomplet** (champs
  `status`/`created`/`updated`/`tradition_cadre`/`sources`, et `type` pour l'une).
  C'est le point de conformité le plus saillant du jour : des fiches doctrinales
  **déjà consignées aux annales** portent un frontmatter que le vérificateur
  rejette. Réparation mécanique possible, à valider.
- **1 fiche veille sans frontmatter** (`analyse-temporelle-code-meta-raisonnement-ia-2026-08-19.md`).
- Ces 4 fiches sont la **cause unique** du blocage du manifeste de cartographie.

### 5.3 Discipline des sources (§VII)

- Le marqueur `to-source` est **largement présent** dans `doctrinal/symboles/`
  (plusieurs dizaines d'occurrences). C'est **conforme** : le marqueur est le
  régime légitime d'un fait sans source vérifiée. Sa **levée** requiert la
  vérification du texte primaire par l'utilisateur (ou citation exacte d'une
  autorité contrôlée) — jamais sur la seule foi d'un modèle. La densité du
  marqueur est un état des lieux, pas une anomalie.
- Aucune reprise non flaguée d'un persona IA détectée dans le lot récent.
- Les 2 dépôts du jour (`maymaniya_p1.pdf`, `claudes-constitution.pdf`) sont
  **non qualifiés** ; aucune fiche ne les affirme sans source.

### 5.4 Intégrité du flux Discernement → R&D → Doctrine

Cadre : fiche des trois territoires (`status: adopte`, 2026-08-11). Régime :
spéculation `speculatif` → chantier `exploratoire` → adoption/archivage, chaque
transition sous validation humaine (Cmd 6 à l'entrée, Cmd 12/13 à la sortie).

- **Aucun passage en force constaté** dans les éléments récents : aucune théorie
  érigée en doctrine sans verdict ; la fiche des trois territoires elle-même porte
  son verdict d'adoption daté.
- La distinction **Doctrine (transmission descendante du Principe) / Théorie
  (articulation ascendante d'un phénomène)** est respectée dans les productions
  récentes du pôle R&D, qui se qualifient en `brouillon`/`exploratoire`.
- **Observation structurelle** : le Laboratoire-Sandbox (`/root/sandbox-rd/`)
  existe mais est **vide** — l'athanor n'a encore éprouvé aucun montage. Ce n'est
  pas un écart (rien n'oblige à ce qu'il soit peuplé), mais c'est le lieu désigné
  de la phase exploratoire ; son vide est documenté comme état.

### 5.5 Convention des annales (append-only, insertion)

- **`hermeneutique/annales.md` — rupture d'ordre (A2)** : l'entrée 2026-08-20
  apparaît **après** l'entrée 2026-08-04, en violation de la convention
  « plus récent en haut ». C'est la signature d'une insertion en **queue** au lieu
  de l'insertion après le bloc d'introduction (`<!-- INSERTION: EN-TÊTE -->`).
  À rétablir.
- **`atelier/annales.md` (A5)** : double ligne vide avant un séparateur, signature
  possible d'un ajout mécanique en fin de fichier. À vérifier.
- **`updated:` non remontés (A3 ×2)** dans `doctrinal/annales.md` et
  `hermeneutique/annales.md` (Cmd 8 : toute écriture remonte `updated:`).
- **Rappel** : un `Update` d'annales qui échoue ne doit **jamais** être suivi d'un
  `Write` global. Les annales restent append-only.

### 5.6 Autres signalements

- **`UPDATES.md` / `MASTER-UPDATE.md`** : le protocole (§I, §IX) et plusieurs
  fiches (bilan pont-agents, charte `rd/`) y renvoient, mais **aucun n'existe**
  dans le dépôt (recherche `find` négative). Référence morte ou convention à
  rétablir. À clarifier.
- **`atelier/R/`** : dossier vide, homonyme de `rd/`. Fusion, suppression (Cmd 10 :
  stub avec pointeur, jamais de suppression sèche) ou intention distincte à
  documenter.
- **Rigueur terminologique (Cmd 2, mineur)** : la fiche Studio §1.1 parle de
  « quatre circuits canoniques + label + meta ». Le protocole V2 (§II) parle de
  **cinq circuits étanches** (doctrinal, atelier, label, hermeneutique) + meta
  Domaine Réservé. Formulation à harmoniser pour éviter toute lecture d'un
  « sixième circuit ».
- **Caractère invisible U+200D (point 18)** : contrôle dirigé sur l'ensemble du
  dépôt (tous fichiers `.md`/`.py`/`.sh`/`.html`, `.git` et `.venv` exclus) —
  **toutes** les occurrences sont un ZWJ inséré dans le mot « H‍ermes »
  (H + ZWJ + ermes), y compris dans `CLAUDE.md` racine, `meta/CLAUDE.md`, les
  annales et la fiche adoptée des trois territoires. Lecture Vigilance : c'est une
  **convention stylistique délibérée et cohérente du dépôt**, pas une injection.
  Conséquence outillage : les gardes de lecture d'agents qui signalent ces fichiers
  comme « prompt injection potentielle » produisent un **faux positif**, et ce
  signal a contribué à la dispersion documentée dans la fiche d'incident du jour
  (`rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint.md`,
  non trackée, à committer). **À documenter** comme convention connue (pour que
  les futurs agents ne la poursuivent pas) ; la décision de la retirer ou de la
  conserver appartient à Sidy — le pôle Vigilance ne tranche pas.

---

## 6. Recommandations conjointes (priorités)

Soumises à Sidy. **Aucune exécution** par les pôles ; chaque item requiert sa
validation (Cmd 12/13, §IX).

**P1 — bloquant mécanique (rétablir le manifeste de cartographie) :**
1. Compléter le Sceau Recteur des **3 fiches du lot kabbale**
   (`status`/`created`/`updated`/`tradition_cadre`/`sources`, + `type` pour la
   fiche source du Traité).
2. Donner un frontmatter complet à la **fiche veille 2026-08-19**.

**P2 — convention des annales :**
3. Rétablir l'**insertion en en-tête** de l'entrée 2026-08-20 dans
   `hermeneutique/annales.md` (actuellement en queue) et remonter `updated:` dans
   les annales concernées (A3).
4. Clarifier la **référence morte `UPDATES.md`/`MASTER-UPDATE.md`** (rétablir la
   convention ou corriger les renvois).

**P3 — hygiène de structure :**
5. Fusionner le **doublon** « Autorité Spirituelle et Pouvoir Temporel » (espace
   finale) vers le dossier canonique, avec note/stub (Cmd 10).
6. Statuer sur **`atelier/R/`** (fusion avec `rd/`, stub, ou intention distincte).
7. Déplacer **`organize_guenon.sh`** vers `rd/outillage/` avec note de provenance.

**P4 — gouvernance des données et du workflow :**
8. **Qualifier les 2 PDF du jour** (`maymaniya_p1.pdf`, `claudes-constitution.pdf`).
9. Statuer sur les **données personnelles en `raw/`** (relevés bancaires, thème
   natal) — le dépôt est canonique ; maintien ou déplacement relève de la
   gouvernance.
10. **Committer le lot islamofuturisme** quand jugé prêt, puis **pousser** la
    branche (3 commits en avance sur `origin`).

**P5 — clarifications structurelles (sans urgence) :**
11. Clarifier le **sens de lien** dans `symboles/manvantara.md` (formulation
    inversée) et le statut de la section herméneutique de `doctrinal/index.md`.
12. **Éprouver le sandbox-rd** (athanor) si un chantier exploratoire s'ouvre ; à
    défaut, documenter son vide comme état.

---

## 7. Conclusion

Le dépôt est **structurellement sain** : les cinq circuits sont en place, le pôle
R&D est constitué et outillé, les vérificateurs déterministes fonctionnent et la
chaîne de contrôle (Graphe, invariants, cron) est active. Les constats du jour se
concentrent sur **un unique point mécaniquement bloquant** (4 frontmatter
incomplets, dont 3 du lot kabbale déjà consigné aux annales) et sur un **petit
nombre de conventions d'insertion des annales** mal appliquées sur les écritures
non committées du jour.

Le pôle Vigilance n'a relevé **aucune violation active d'étanchéité**, **aucune
infiltration de vocabulaire**, **aucun passage en force du flux
Discernement → R&D → Doctrine**. Deux zones grises (sens de lien, section
herméneutique de l'index doctrinal) et une référence morte (`UPDATES.md`) sont
documentées pour clarification.

Les deux pôles s'accordent sur la priorité : **P1** (rétablir les Sceaux pour
libérer le manifeste), puis **P2** (convention des annales). Le reste est hygiène
et gouvernance, sans urgence doctrinale.

*Rapport conjoint d'exploration et de contrôle — observations consignées, aucune
qualification rendue. Les verdicts et arbitrages restent réservés à Sidy
(Cmd 12), la porte humaine sur ce qui engage demeure (Cmd 13).*

---

— **Studio** (R&D, exploration)
— **Gardien** (vigilance, contrôle protocolaire)
