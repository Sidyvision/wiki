---
title: "Registre des chantiers — carte vivante des travaux ouverts du dépôt"
type: registre
tags: [atelier, rd, registre, chantiers, pilotage]
created: 2026-09-01
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
  - "[[atelier/rd/veille/registre]]"
  - "[[atelier/rd/cahiers/bilan-2026-08-15-pont-agents]]"
  - "[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]"
  - "[[atelier/rd/infrastructure/2026-08-20_pistes-developpement-infrastructure]]"
---

# Registre des chantiers du dépôt

> **Ce que cette pièce est.** La carte vivante de **tous** les chantiers ouverts du
> dépôt, tous domaines confondus, tenue au pôle R&D sur demande de Sidy (2026-09-01).
> Elle existe pour une raison précise : jusqu'ici les pistes vivaient éclatées entre six
> registres locaux tenus à jour de façon inégale, et **aucun n'avait de vue d'ensemble** —
> un agent reprenant le fil à froid ne pouvait pas savoir où en étaient les choses.
>
> **Ce qu'elle n'est pas.** Elle **recense, elle n'absorbe pas.** Aucun contenu ne migre
> ici : chaque chantier reste instruit dans sa fiche et dans son circuit. Le registre ne
> porte que le pointeur, le statut et la prochaine action. Il ne recopie jamais une entrée
> du registre des problèmes, une scrutation de veille, un discernement, ni une valeur
> qu'un script calcule — il pointe.
>
> **Ce qu'elle ne décide pas.** Aucun verdict, aucune priorité doctrinale (Cmd 12), aucune
> décision engageante (Cmd 13). Les priorités portées sur les lignes d'ingénierie sont
> **proposées**, jamais tranchées.

## Comment lire ce registre

- **Identifiants stables**, jamais réutilisés ni renumérotés : `INS-` Instrument ·
  `INF-` infrastructure & agents · `OUT-` outillage & scripts · `BIB-` bibliothèque ·
  `CAS-` études de cas · `PRO-` process & protocole · `DOC-` doctrinal. Cet ID est la
  poignée greppable : il survit à un changement de titre et se cite depuis une entrée
  d'annales, une file de tâches ou un message d'agent.
- **Statuts** (mêmes mots que le registre des problèmes) : `ouvert` · `en-cours` ·
  `bloque` (une dépendance externe empêche d'avancer) · `attente-verdict` (rien ne manque
  sauf la décision de Sidy) · `clos` · `caduc` (le chantier n'a plus d'objet).
- **Discipline** : ce registre est **révisable en place**, à la différence des cahiers
  append-only. Un chantier clos n'est jamais supprimé (Cmd 10) : il garde son ID et
  descend en §9 avec sa date. L'historique, c'est git et les annales.
- **Instruit ou seulement recensé** (2026-09-01) : un chantier d'ingénierie qui entre
  en instruction reçoit un **triptyque** `intent.md` / `spec.md` / `plan.md` dans un
  dossier de son domaine (`atelier/rd/<domaine>/<id>-<slug>/`, voir
  `atelier/CLAUDE.md` §Nomenclature et le gabarit
  [[atelier/rd/outillage/gabarit-triptyque-chantier]]). La colonne *Triptyque* porte
  le pointeur ; vide = chantier recensé, pas encore instruit — ce n'est pas un défaut,
  c'est un état. Le registre **pointe, il n'absorbe pas** : aucun contenu du triptyque
  n'est recopié ici.
- **Vérification avant inscription** : aucune ligne n'est inscrite sans avoir été
  confrontée au disque et à `git log`. Ce qui n'a pas pu l'être va en §8, **jamais
  asserté ouvert**.

## Entretien

Quiconque **ouvre, fait avancer ou clôt** un chantier met à jour sa ligne **dans la même
passe que son entrée d'annales** (Cmd 9). On ne crée pas une obligation nouvelle : on
greffe une ligne sur un rituel déjà respecté. La désignation d'un agent responsable d'une
revue périodique est une décision engageante (Cmd 13) — elle est en §Points ouverts.

---

## 0. Vue d'ensemble

**48 chantiers ouverts** au 2026-09-02, plus 6 versés en §9 (clos ou caducs) et
6 lignes en §8 (à vérifier, non assertées ouvertes). Décompte mécanique — si vous
modifiez une ligne, ce tableau se recompte, il ne s'estime pas.

| Pôle | ouvert | en-cours | bloqué | attente-verdict | total |
|---|---|---|---|---|---|
| `INS` Instrument | 10 | — | 1 | 3 | **14** |
| `INF` Infrastructure & agents | 7 | 3 | 1 | 3 | **14** |
| `OUT` Outillage & scripts | 5 | — | 1 | — | **6** |
| `BIB` Bibliothèque | 1 | — | 1 | — | **2** |
| `CAS` Études de cas | 1 | — | 1 | — | **2** |
| `PRO` Process & protocole | 3 | — | — | 2 | **5** |
| `DOC` Doctrinal | 4 | — | — | 1 | **5** |
| **Total** | **31** | **3** | **5** | **9** | **48** |

**Ce que ce tableau dit d'abord** : 9 chantiers n'attendent **que** la décision de
Sidy — rien d'autre ne leur manque. 5 sont bloqués par une dépendance qui n'est pas
entre nos mains (une PR amont, une prise de vue, un texte à localiser). C'est là, et non
dans le nombre total, que se lit ce qui peut avancer aujourd'hui.

Le `DOC-01` compte pour une ligne mais recouvre **37 fiches de discernement `speculatif`**
en attente de verdict : elles ne sont ni listées ni hiérarchisées ici (Cmd 12), voir §7.

## 0 bis. Infrastructure — où lire l'état réel

Ce registre **ne recopie aucune valeur** qu'un script calcule ou qu'une archive porte :
une valeur recopiée est une valeur périmée. Il dit **où regarder**.

| Ce qu'on veut savoir | Où c'est établi mécaniquement |
|---|---|
| Invariants du dépôt (Sceaux, liens, étanchéité, annales) | `verifier-invariants.py --racine /root/wiki` |
| Cohérence Hermes/cron réellement appliquée (anti-fabulation) | `atelier/rd/outillage/verifier-coherence-infrastructure.py` + champ `infra_verif` des fiches |
| État du serveur au jour le jour | `atelier/rd/infrastructure/monitoring-archive/` (rétention 40 j) |
| Fichiers présents mais non suivis par git | `atelier/rd/outillage/detecter-non-tracke.py` |
| Architecture serveur et agents | [[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]] |
| Fournisseur d'inférence courant des profils | [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] |
| Échecs, blocages, anomalies et leur résolution | [[atelier/rd/cahiers/registre-problemes]] (append-only) |
| Réussites et optimisations | [[atelier/rd/cahiers/journal-optimisations]] (append-only) |
| Veille externe qualifiée | [[atelier/rd/veille/registre]] (append-only) |
| Incidents caractérisés | `atelier/rd/incidents/` |
| Graphe de cartographie du dépôt | `graphe-cartographie.json`, régénéré par `atelier/rd/outillage/graphe/generer-cartographie.py` |

---

## 1. Instrument (`INS`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Triptyque | Ouvert par |
|---|---|---|---|---|---|---|
| INS-01 | Transcrire le ch. II de Shayegan — pièce manquante en amont de l'unification des axes | `ouvert` | transcription (poste INGEST) | [[atelier/rd/instrument/2026-08-30_reseau-subtil-unification-axes-deux-echelles]] §6 | — | fiche du 2026-08-30 |
| INS-02 | Mode « axe unifié » + champ `echelle` dans le générateur et le prototype | `ouvert` | spécifier avant de coder | même fiche, §4.2 | [[atelier/rd/instrument/ins-02-axe-unifie/intent]] | 2026-08-30 |
| INS-03 | Cieux planétaires ↔ *lokas* — comparaison licite jamais tentée | `ouvert` | ouvrir une fiche `discernement` dédiée (Cmd 3) | même fiche, §6 | — | 2026-08-30 |
| INS-04 | 22 sentiers séphirothiques comme réseau de canaux rayonnant de Tiferet | `bloque` | l'arrangement des sentiers n'est pas fixé au dépôt — instruire en amont | même fiche §3.3 ; `doctrinal/discernement/2026-08-30_nadis-du-coeur-sentiers-sephirothiques-tiferet` (`speculatif`) | — | 2026-08-30 |
| INS-05 | Bifurcation des centres surnuméraires — trois options posées, aucune implémentée | `attente-verdict` | Sidy tranche l'option | même fiche, §7.3 | — | 2026-08-30 |
| INS-06 | Divergences table/planches — deux cellules vides d'*Ājñā* | `attente-verdict` | combler ou laisser : relevé explicitement remis à Sidy | même fiche, §7.5 | — | 2026-08-30 |
| INS-07 | Figuration de la discontinuité — la réserve doctrinale la plus lourde que le rendu actuel ne porte pas | `ouvert` | instruire §7 « dans l'ordre, avant d'écrire une ligne de rendu » | [[atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable]] §8.6 | — | 2026-08-30 |
| INS-08 | Parallèle islamique sur la couronne de la tête (Guénon ch. XX, note 3) — texte non nommé | `ouvert` | localiser la source primaire | fiche du 2026-08-30, §6 | — | 2026-08-30 |
| INS-09 | Rendu d'al-Insān al-Kāmil — proposition non validée dans le prototype | `attente-verdict` | Sidy valide ou révise le rendu | [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]] P2.4 | — | jalon du 2026-08-20 |
| INS-10 | Détail optique de la lentille barzakh (degrés 19-20) | `ouvert` | spécifier | même jalon, P2.5 | — | 2026-08-20 |
| INS-11 | Fondation équivalente aux `hadarat-khams` pour la branche séphirothique (10 Sephiroth, 3 colonnes) — préalable à tout ancrage Kabbale complet | `ouvert` | fiche de fondation, sur source primaire | même jalon, P6.13 ; [[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3]] | — | 2026-08-20 |
| INS-12 | Colonne *faṣṣ* (Fuṣūṣ) de la table des 28 degrés — `to-source` (3 marqueurs restants) | `ouvert` | non bloquant : `instrument-donnees.yaml` ne l'utilise pas | `doctrinal/symboles/table-28-degres-nafas-rahman` | — | 2026-07-01 |
| INS-13 | Bandeau zodiacal horizontal — données déjà sourcées, **rendu manquant** | `ouvert` | implémenter le rendu | [[atelier/index]] §Instrument ; [[atelier/rd/instrument/spec-anneau-zodiacal]] | [[atelier/rd/instrument/ins-13-bandeau-zodiacal/intent]] | 2026-07-27 |
| INS-14 | Versant Sanātana Dharma — la fondation védantique est disponible (ch. X, XV, XVI de *L'Homme et son devenir*), la structure à 4 états n'est **pas encore ancrée** | `ouvert` | ancrer le registre `vedanta` | [[atelier/index]] §Instrument ; [[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16]] | — | 2026-07-16 |

*Suites de [[atelier/rd/instrument/2026-08-29_mise-en-regard-majma-al-bahrayn-registres]] §7 :
non dépouillées dans cette passe → §8.*

## 2. Infrastructure & agents Hermes (`INF`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Triptyque | Ouvert par |
|---|---|---|---|---|---|---|
| INF-01 | Isolation mémoire Hermes par sub-agent (`memory_enabled`) — condition du déploiement du skill Karūbī | `bloque` | dépendance amont : PR #34098 de `hermes-agent` (hors de notre main) | [[atelier/rd/synthese-deploiement-memoire]] §187-189 ; [[atelier/rd/outillage/investigation-isolation-memoire-hermes]] | — | jalon du 2026-08-20, P3.6 |
| INF-02 | Sandbox R&D `/root/sandbox-rd/` — ouverte le 2026-08-18, **encore vide** : aucun montage de veille n'y a été éprouvé | `ouvert` | y éprouver un premier montage issu de la veille | [[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]] | — | 2026-08-18 |
| INF-03 | Phase 3 — automatisation de la veille infrastructure : décisions entièrement tranchées, **aucun automatisme écrit** — confirmé mécaniquement le 2026-09-01 : le script existe et est exécutable, mais **aucun des trois jobs cron qu'une fiche du 2026-08-23 déclarait créés n'est déclaré dans les quatorze profils Hermes** | `attente-verdict` | la proposition de reprise du 2026-08-31 est en `brouillon`, soumise à Sidy | [[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]] ; [[atelier/rd/cahiers/proposition-veille-automatique-studio-2026-08-31]] ; [[atelier/rd/infrastructure/2026-08-23_deploiement-veille-infrastructure-quotidienne]] | — | 2026-08-11, rouvert 2026-08-31 |
| INF-04 | Bureau TUI — vérification en conditions réelles jamais faite | `ouvert` | éprouver, puis consigner | [[atelier/rd/infrastructure/bureau-tui-architecture]] ; [[atelier/rd/cahiers/2026-08-31_rapport-investigation-architecture-modulaire-agents]] | — | jalon du 2026-08-15 |
| INF-05 | Migration des prompts Hermes vers la nomenclature modulaire — **1 rôle aligné sur 12** (`publication`) | `en-cours` | aligner les onze autres | [[atelier/rd/cahiers/2026-08-31_rapport-migration-11-agents-et-contribution-choura]] | — | 2026-08-31 |
| INF-06 | Monitoring de charge en série temporelle — seul un instantané quotidien existe | `ouvert` | spécifier la série | jalon du 2026-08-20, P1.2 | — | 2026-08-20 |
| INF-07 | Fonction réelle du processus `omniroute` (1040 Mo de RAM) | `en-cours` | partiellement documenté depuis (migration 2026-08-26, incident 2026-08-27) — reste à décrire le rôle nominal | [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] ; [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]] | — | jalon du 2026-08-20, P1.1 |
| INF-08 | Reproduction contrôlée de l'incident de robustesse persona-LLM | `ouvert` | reproduire, ou consigner l'abandon | [[atelier/rd/outillage/robustesse-documents-persona-llm]] | — | jalon du 2026-08-20, P4.10 |
| INF-09 | Levier d'action du cycle Choura : le dispositif produit des perspectives, mais sans contribution de Sidy le cycle reste consultatif — **cycle mis en pause par Sidy (2026-09-01, dit en session)** | `ouvert` | reprise sur nouvelle décision de Sidy (hook de contribution, ou abandon) — verdict `attente-verdict` rendu : pause, pas de hook pour l'instant | signalé par le Gardien dans le cycle du 2026-09-01 (cf. Domaine Réservé, dossier `choura/`) | — | 2026-09-01 |
| INF-10 | Contrôle anti-fabulation `coherence-infrastructure-brute` — second job cron en échec, non documenté | `ouvert` | diagnostiquer | [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-08-18]` | — | 2026-08-18 |
| INF-11 | Continuité des tâches et de l'information entre Claude Code, Hermes Terminal et Discord — angle mort structurel (un cron « créé » le 2026-08-17 n'existait pas) | `ouvert` | c'est le motif d'existence du champ `infra_verif` ; reste à couvrir le passage d'information | registre des problèmes, entrée `[2026-08-17]` | — | 2026-08-17 |
| INF-12 | Positions zodiacales 5, 8 et 12 des agents : les douze brouillons existent sur disque (2026-08-15), mais le compte-rendu de chantier les donne « non traitées, en attente de verdict » — contradiction non levée | `attente-verdict` | confronter brouillons et verdict | `atelier/rd/cahiers/brouillons-extension-zodiacale/` ; jalon du 2026-08-20, P4.9 | — | 2026-08-11 |
| INF-13 | Scission du dépôt : le rendu de l'Instrument passe au dépôt frère `Sidyvision/instrument` (privé) — le §VII, *Règle commune des MANIFESTES*, exprimé en infrastructure plutôt qu'en discipline | `en-cours` | **clos pour l'essentiel** : dépôt frère créé, **passé public** le 2026-09-01 (verdict Sidy), `main` protégée avec `enforce_admins` actif et **épreuve réelle du refus faite**. Reste différée (Cmd 13) : l'automatisation du manifeste (PAT + workflow) — l'étage manuel fonctionne | [[atelier/rd/infrastructure/inf-13-scission-depot-instrument/intent]] | [[atelier/rd/infrastructure/inf-13-scission-depot-instrument/intent]] | 2026-09-01 |
| INF-15 | `monitoring-archive-charte.md` n'archive que le job Studio (`41dc3e7e492c`) — le rapport quotidien Publication (`veille-referencement-investigation-08`, mandat §B, investigation documentaire) n'a aucune trace au dépôt ; une session d'INTÉGRATION ne peut traiter ses suggestions de sourcing que si Sidy les recopie à la main dans `_inbox/` | `attente-verdict` | Sidy tranche : étendre la charte au profil `publication`, ou assumer la copie manuelle | [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]` §3 | — | 2026-09-02 |

## 3. Outillage & scripts (`OUT`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| OUT-02 | Angle mort C3 : `ETANCHEITE_INTERDITE` ne porte que la clé `doctrinal` — un lien `atelier/rd/` → `meta/` n'est **jamais bloquant**, il ne remonte qu'en avertissement C4 | `ouvert` | étendre les clés, ou acter le comportement | registre des problèmes, entrée `[2026-08-15]` (`reporte`) | 2026-08-15 |
| OUT-03 | SRS Hermes-native — format, extraction, révision, espacement non définis | `ouvert` | spécifier | [[atelier/rd/outillage/spec-srs-hermes-native]] ; [[atelier/rd/outillage/2026-08-15_piste-srs-assimilation-protocole]] | verdict Sidy du 2026-08-15 |
| OUT-04 | Trois questions d'applicabilité Cordis, non instruites (HMR des agents Hermes en priorité) | `ouvert` | instruire la première | [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]] ; [[atelier/rd/veille/cordis/notes-lecture]] | 2026-08-16 |
| OUT-05 | Contrôle A6 « corps d'entrée orphelin » du vérificateur — proposé, non implémenté ; l'incident append-only du 2026-08-28 (en-tête d'entrée mangé à l'insertion) n'a été vu par aucun contrôle | `ouvert` | implémenter | [[atelier/rd/cahiers/2026-08-28_compte-rendu-premiere-session-integration-qoder]] | 2026-08-28 |
| OUT-06 | Restes de veille Cordis : dépôt source (TS d'origine), identité du contributeur `inso1337`, nature du repo `spatiotemporal-composability-skill` | `ouvert` | scrutation complémentaire | [[atelier/rd/veille/registre]], entrée `[2026-08-18]` | 2026-08-18 |
| OUT-07 | Speculative decoding (Tencent/AngelSpec) — matériau qualifié, **non exploitable sans GPU local** | `bloque` | rouvrir si un chantier d'inférence GPU locale est ouvert ; re-vérifier l'état du repo avant tout engagement | [[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]] | 2026-08-31 |

## 4. Bibliothèque (`BIB`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| BIB-01 | Appendices non photographiés — aucune fiche possible en l'état | `bloque` | nouvelle prise de vue (geste humain) | [[atelier/rd/bibliotheque/catalogue-bibliotheque]] | 2026-08-22 |
| BIB-02 | *Symboles de la Science sacrée* : couverture d'index à 100 %, mais chapitres non traités en fiches au-delà des XVIII et XXXVII | `ouvert` | choisir les chapitres suivants | même catalogue | 2026-08-22 |

## 5. Études de cas (`CAS`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| CAS-01 | Zellige de la Grande Mosquée — aucune donnée de proportion mesurée : la photographie de terrain n'est pas redressée | `bloque` | reprise du terrain dans de meilleures conditions | [[atelier/etudes-de-cas/zellige-grande-mosquee-paris]] §0 | 2026-08-24 |
| CAS-02 | Quadrivium et Épître 6 des Ikhwān al-Ṣafāʾ (proportions arithmétique/géométrique/harmonique) — point d'entrée signalé, chantier non ouvert | `ouvert` | ouvrir, ou classer | même fiche | 2026-08-24 |

## 6. Process & protocole (`PRO`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| PRO-03 | Types de fiche en usage mais absents du Sceau de `atelier/CLAUDE.md` : `registre` (`rd/veille/registre.md`, le présent fichier), `fiche-rd`, `session` | `ouvert` | régulariser le Sceau, ou aligner les fiches | relevé de la passe du 2026-09-01 | 2026-09-01 |
| PRO-04 | Quatre fichiers `.bak-2026-08-18-pre-C4` suivis par git, référencés nulle part (`atelier/`, `atelier/rd/`, `doctrinal/` ×2) | `attente-verdict` | `deprecated` avec pointeur, ou retrait assumé (Cmd 10) | relevé de la passe du 2026-09-01 | 2026-09-01 |
| PRO-05 | Rétroportage du champ `maturite` sur les fiches `discernement/` — **9 sur 56** le portent ; différé assumé, non borné | `ouvert` | les agents le renseignent au fil de leurs éditions de fond ; le différé n'a pas d'échéance | proposition du 2026-08-27 (cf. Domaine Réservé) | 2026-08-27 |
| PRO-06 | File d'idées pour les agents : dispositif validé le 2026-08-27, **encore vide** — jamais éprouvé en usage réel | `ouvert` | y verser une première idée | `queue-idees.md` (cf. Domaine Réservé) | 2026-08-27 |
| PRO-07 | Nature de `04-sessions-par-fonction-et-backlogs` : cesser d'être un backlog vivant pour devenir mode de travail + aiguillage | `attente-verdict` | refonte documentaire — décision de Sidy | relevé de la passe du 2026-09-01 | 2026-09-01 |

## 7. Doctrinal (`DOC`)

> **Ce tableau recense, il n'instruit ni ne hiérarchise.** Aucune priorité n'est proposée
> sur les lignes doctrinales : l'ordre d'instruction et le verdict appartiennent au
> circuit `doctrinal/` et à Sidy (Cmd 12/13). **Source vivante : `doctrinal/index.md`,
> §VII — Le Registre du Discernement.** Le renvoi ci-dessous est un lien
> `atelier/rd/` → `doctrinal/`, **sens unique, signalé** (§VI du protocole racine) ;
> aucune page doctrinale ne mentionne jamais le présent registre.

| ID | Chantier | Statut | Où il est instruit |
|---|---|---|---|
| DOC-01 | **37 fiches de discernement au statut `speculatif`** sur 56 — verdict en attente. Le décompte est mécanique (`grep '^status:' doctrinal/discernement/*.md`, 2026-09-01) et n'est pas recopié en liste ici : il périmerait aussitôt | `attente-verdict` | [[doctrinal/index]] §VII |
| DOC-02 | Ingests annoncés et non faits : amorce `modes-du-souffle` (items 39-50, Gloton p. 41) ; récit eschatologique complet du ch. 198 ; fiche symbole `lune-noire` ; enrichissement de `ilm-al-nujum` (tables signes/planètes/dignités/maisons) | `ouvert` | poste INGEST ; liste tenue au Domaine Réservé (`04-…`, §E) |
| DOC-03 | Sources primaires à localiser : *ʿUqlat al-mustawfiz*, *Kitāb al-Inshāʾ al-Dawāʾir*, Meftah *Arma Artis* | `ouvert` | discipline des sources, §VII du protocole racine |
| DOC-04 | Citations attribuées non vérifiées (Ibn ʿArabī, al-Ghazālī, le Cheikh) marquées `to-source` — cas le plus net signalé : `symboles/chercheur-manifestant-akbarien` | `ouvert` | levée par vérification primaire humaine, jamais par le modèle |
| DOC-05 | Réserve résiduelle : lien explicite *wirātha* ↔ *aqtāb* non localisé dans le *Futūḥāt* ch. 36 — l'ancrage (c) de l'Instrument en dépend | `ouvert` | [[doctrinal/index]] §VII ; conséquence instrumentale en INS-11 |

## 8. À vérifier — non asserté ouvert

Ce qui n'a pas pu être confronté au disque dans la passe du 2026-09-01. **Rien ici n'est
présenté comme un chantier ouvert** ; l'inscription au registre attend la vérification.

- Suites proposées de [[atelier/rd/instrument/2026-08-29_mise-en-regard-majma-al-bahrayn-registres]] §7
  (« par ordre de maturité ») — non dépouillées.
- [[atelier/rd/outillage/2026-08-13_tour-horizon-corpus-guenon-deblocages]] — tour d'horizon de
  déblocages, statut de chacun non confronté.
- [[atelier/rd/outillage/2026-08-29_mise-en-regard-tenon-mortaise-axe-instrument]] — piste
  probablement liée à INS-02, articulation non établie.
- [[atelier/rd/outillage/spec-generer-cartographie-tolerant]] — le mode tolérant est-il implémenté
  depuis la régénération du 2026-08-31 ?
- Réserves méthodologiques des quatre fiches de phase corpus des études de cas
  (forteresses, dougong, refroidissement passif, Xuankong) — mentions non dépouillées.
- Deux entrées du registre des problèmes rouvrant le même point (Phase 3 veille, deux entrées
  `ouvert` le même jour) : bouclage possible, non confirmé.

## 9. Chantiers clos ou caducs (jamais supprimés — Cmd 10)

| ID | Chantier | Issue | Établi par |
|---|---|---|---|
| OUT-C1 | `graphe-cartographie.json` jamais régénéré, et 10 anomalies bloquantes | **caduc au 2026-08-31** : le graphe a été régénéré (commit `a25e482`) et le pôle intégré au protocole racine §VII. L'entrée du registre des problèmes qui l'affiche encore `ouvert` n'a jamais reçu d'entrée de clôture — c'est le comportement normal d'un cahier append-only, pas une anomalie | vérifié au disque et par `git log`, 2026-09-01 |
| INF-C1 | Crise de crédit API du 2026-08-07 — « tous les agents restent inactifs jusqu'à résolution » | **caduc au 2026-09-01** : sortie de crise par changement de fournisseur d'inférence (bascule OmniRoute du 2026-08-26), non par nouvelle clé. Les agents tournent en continu | [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] ; commits `CHOURA: tour <agent>` du 2026-08-28 au 2026-09-01 |
| PRO-C1 | `hermeneutique/annales.md` — `updated:` antérieur à sa dernière entrée | **clos le 2026-09-01** : corrigé dans la passe d'organisation. Seule erreur réelle que le vérificateur signalait, noyée dans 209 lignes de bruit (motif de OUT-01) | passe du 2026-09-01 |
| OUT-C2 | Périmètre de `verifier-invariants.py` : le script parcourait le disque sans consulter `.gitignore` — 209 des 210 erreurs étaient du bruit de venv tiers, de sorties régénérables et du sas `raw/`, et ce bruit avait masqué la seule erreur vraie du jour | **clos le 2026-09-01** sur verdict de Sidy. Le script interroge désormais git (`ls-files --others --ignored --exclude-standard`) et ne contrôle que ce qui appartient au dépôt ; le périmètre appliqué est annoncé en tête de sortie, jamais silencieux ; `--tout` restitue le comportement antérieur, donc rien n'est hors de portée. Repli sur l'exclusion des dossiers cachés hors dépôt git (bacs à sable). Le dépôt passe de 210 erreurs à **0 erreur, 0 avertissement** sur 709 fiches. `generer-cartographie.py` portait le même défaut (112 anomalies venues du même venv, refus d'écrire le manifeste) — corrigé de même, le graphe se régénère | `verifier-invariants.py` ; guide de déploiement (cf. Domaine Réservé) ; entrée `[2026-09-01]` du registre des problèmes |
| PRO-C2 | Cinq fiches à la racine de `atelier/rd/`, hors arborescence et sans lien entrant ; trois portaient du fait personnel en page neutre (§VI) | **clos le 2026-09-01** sur verdict de Sidy. Les trois fiches versées au Domaine Réservé avec leur historique git ; les deux neutres classées par leur nature (`infrastructure/`, `cahiers/`) ; la racine du pôle ne porte plus que `index.md` et le présent registre. Deux fiches restées côté `rd/` portaient le même défaut **dans leur corps** — blocs retirés, matière conservée au Domaine Réservé. Contreparties neutres écrites et indexées : déploiement de la veille quotidienne, inventaire de l'outillage ; pour la troisième, la contrepartie existait déjà (Cmd 4, pas de quatrième fiche) | passe du 2026-09-01 ; [[atelier/rd/index]] §Assainissement |
| PRO-C3 | Protection de la branche `main` contournable sans review | **clos le 2026-09-01** sur verdict de Sidy. Le fait s'est révélé plus net que la ligne ne le disait : la protection exigeait un contrôle `lint` qui **ne validait rien** — il parcourait un dossier `wiki/` et des sous-dossiers de l'arborescence plate abandonnée le 2026-06-11, tous inexistants, et imprimait « Frontmatter OK » sur zéro fichier. Le workflow exécute désormais `verifier-invariants.py` et l'hygiène Unicode, en bloquant ; vérifié qu'il **peut échouer** (clé de Sceau absente, ZWJ), le CI inspecte 709 fiches. `enforce_admins` reste à `false`, **acté et non subi** : le durcir imposerait un flux par pull request aux treize acteurs qui poussent en direct. Contrepartie : hook `pre-push` versionné qui exécute les mêmes contrôles avant que la faute quitte la machine | `.github/workflows/lint-and-validate.yml` ; [[atelier/rd/outillage/hooks/README]] ; entrée `[2026-09-01]` du registre des problèmes |
| INF-14 | Hébergement du rendu de l'Instrument sur `sidyvision.com` — un dépôt n'est pas une diffusion | **clos le 2026-09-01**, mis en production après validation explicite de Sidy dans la session (Action PUBLICATION, point 4). Le rendu est servi sur `https://sidyvision.com/instrument/`. Trois obstacles levés en chemin, chacun établi par mesure et non déduit : le site n'avait **aucune source versionnée** (déploiement manuel, capture de sauvegarde prise avant tout accès) ; le premier jeton ouvrait un compte **créé le jour même et vide** — le site était détenu par un autre compte ; le montage par proxy est tombé sur le **401 *edge-access*** dont Netlify frappe les `*.netlify.app` des comptes gratuits récents. Montage final : déploiement direct par l'API, page d'accueil et rendu dans le même site — ni proxy, ni build, ni liaison GitHub, ni secret chez un tiers. Les six critères contrôlés en ligne, le premier d'abord : page d'accueil **octet pour octet identique** à la capture. **Second temps le même jour** — Sidy demande la mise à jour automatique : elle est en place, non par liaison Netlify (qui aurait publié la racine du dépôt et **écrasé la page d'accueil**, outre l'OAuth par navigateur) mais par **GitHub Action** dans le dépôt frère, rejouant la même API et le même garde-fou d'empreinte. Éprouvée de bout en bout par `workflow_dispatch` : garde-fou vert, publication faite, et triple contrôle en ligne — page d'accueil intacte, rendu identique au dépôt, manifeste servi à 46 nœuds. **Troisième temps** : `enforce_admins` aligné sur la doctrine du wiki (`false` + garde-fou local, PRO-01), la **porte humaine déplacée dans le `pre-push`** (`PUBLIER=1` exigé pour toute poussée de `src/` sur `main`, puisqu'elle publie en production) — et, au passage, découverte que les deux hooks portaient un motif `grep` qui **ne correspondait jamais** : la faute même de PRO-01, reproduite dans du code neuf, corrigée et éprouvée dans les deux sens | [[atelier/rd/infrastructure/inf-14-hebergement-rendu-sidyvision/plan]] ; `atelier/rd/outillage/publier-instrument-netlify.sh` ; `.github/workflows/publier.yml` du dépôt frère (PR #1) ; capture de référence SHA-1 `6814d7f4…3334` |

---

## Points ouverts soumis à Sidy

Aucun n'est tranché par la machine (Cmd 12/13).

1. **Revue périodique** — désigner l'agent qui tient ce registre à jour hors des passes
   d'intégration. Candidat naturel : le Studio Sound Engineer, qui porte déjà le cron de
   monitoring et le mandat de veille infrastructure. C'est une décision engageante.
2. **OUT-01** — périmètre du vérificateur d'invariants. Priorité haute : le bruit masque
   les erreurs réelles, le cas s'est déjà produit.
3. **PRO-02** — sort des trois fiches à fait personnel logées en page neutre.
4. **PRO-04** — sort des quatre `.bak` suivis par git.
5. **PRO-07** — refonte de la nature du document de backlogs du Domaine Réservé.
6. **Vocabulaire du champ `statut:`** des propositions : aucun n'est établi au dépôt, et
   la seule occurrence existante est précisément celle qui était fausse. L'arrêter relève
   de Sidy ; en attendant, l'état réel de chaque proposition est porté en encart daté dans
   son corps.
