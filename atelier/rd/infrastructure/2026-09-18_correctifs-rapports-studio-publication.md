---
title: "Correctifs des rapports Studio et Publication des 2026-09-16 et 2026-09-17 — fiche-contrat"
type: infrastructure
tags: [rd, infrastructure, monitoring, hermes, correctifs, contrat]
created: 2026-09-18
updated: 2026-09-18
sources: []
links:
  - "[[atelier/rd/infrastructure/2026-09-15_execution-propositions-rapport-studio]]"
  - "[[atelier/rd/infrastructure/2026-09-13_correctifs-rapports-studio]]"
  - "[[atelier/rd/infrastructure/monitoring-archive/registre-traitement]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
original: []
infra_verif:
  - profil: studio
    cron_job: monitoring-infrastructure-quotidien
  - profil: publication
    cron_job: veille-referencement-investigation-08
---

# Correctifs des rapports Studio et Publication (09-16 et 09-17) — fiche-contrat

## 1. Motif et cadre

**Consigne de Sidy, en session Claude Code, 2026-09-18** : « exécute les correctifs des
rapports Publication et Studio ».

Quatre rapports étaient en attente, aucun ne portant d'entrée au registre de traitement :
`monitoring-archive/2026-09-16_{41dc3e7e492c,ad3152b237bb}.txt` et
`monitoring-archive/2026-09-17_{41dc3e7e492c,ad3152b237bb}.txt`. Le rapport du 09-17
portant les compteurs de jour et les deltas, il est pris comme état vivant ; celui du
09-16 est relu pour ce qu'il ne redit pas.

Comme les 2026-09-13 et 2026-09-15, cette fiche est le **contrat** du lot : écrite et
commitée **avant** la première écriture d'exécution. Les gestes exécutés sont ceux du §2,
ni plus ni moins ; ce qui n'est pas exécuté l'est pour un motif nommé (§4).

**Ligne de conduite (Cmd 12 / Cmd 13).** Les deux rapports se déclarent eux-mêmes en
propositions (« Suggestions soumises à validation », « toutes PROPOSITION, aucune
décision »). N'est exécuté ici que ce qui est **mécanique et réversible, sans arbitrage** :
une faute de forme dont il n'existe pas de seconde lecture. Tout ce qui demande un verdict
— placement, nomination, convention, recension d'un ouvrage possédé — est **signalé, non
tranché** (§4).

## 2. Le lot exécuté

| Code | Point du rapport | Geste | Portée |
|---|---|---|---|
| **C** | Publication 09-17, signalement C | retrait de l'item vide `""` en queue de `cross_links` | 1 fiche `doctrinal/sources/` |
| **L** | Studio 09-17 P3 (et 09-16 P1b) | normalisation des wikilinks écrits en forme `.md` vers une fiche **existante** — 17 occurrences, 10 fiches | `atelier/rd/` |
| **D′** | Publication 09-17, signalement D (moitié *pointeur*) | renvoi de corps vers `meta/bibliotheque-physique.md` (**tombstone** depuis le 2026-08-22) repointé sur `atelier/rd/bibliotheque/catalogue-bibliotheque.md` | 1 fiche `doctrinal/sources/` |
| **A** | Studio 09-17 P5 | commit nommé des 4 archives de monitoring non suivies (09-16 ×2, 09-17 ×2), chemins stagés un par un | `monitoring-archive/` |
| **J** | règle d'usage du registre | 4 entrées au registre de traitement + entrée au registre des problèmes + annales de circuit | `atelier/rd/`, `doctrinal/` |

## 3. Ce que chaque geste change, exactement

### C — un item de liste vide n'a pas de seconde lecture

`doctrinal/sources/guenon-symbolisme-croix-ch4-directions-espace.md`, l. 11 : le troisième
item de `cross_links` est la chaîne vide `""`. Seule occurrence des cinq circuits. Retiré,
les deux wikilinks réels conservés dans l'ordre. `updated:` remonté au jour.

### L — 17 liens, et le compte du rapport décomposé

Le rapport Studio annonce **48 « liens morts » dont la cible existe sur disque**. La mesure
refaite ce jour (script de cartographie, `--verifier --rapport` en `/tmp`) décompose ces 48
en **deux classes qui n'appellent pas le même geste** :

- **17 occurrences réparables** (10 fiches) : le wikilink porte l'extension `.md` alors que
  la cible est une fiche du dépôt indexée par son chemin sans extension. Forme fautive,
  cible vivante : retrait de l'extension, rien d'autre.
- **30 occurrences non réparables — et qui ne sont pas des fautes** : elles visent
  `atelier/rd/index` (20), `atelier/rd/veille/index` (7), `doctrinal/index` (2),
  `atelier/rd/index.md` (1). Le générateur de cartographie **exclut par construction**
  `index.md`, `annales.md`, `CLAUDE.md`, `README.md` de ses nœuds
  (`FICHIERS_EXCLUS`, l. 134) : un renvoi vers un hub sera toujours compté « lien mort »
  par le graphe, alors que le fichier existe et que `verifier-invariants.py` ne dit rien.
  **Rien à corriger dans les fiches** : c'est une lecture du graphe, même famille que le
  signalement P2 du même rapport (`sources:` lu comme un lien). Porté au §4 comme point
  d'instrument, non comme défaut de dépôt.

Les deux chaînes bibliographiques Gloton (`sources:` des deux fiches du 09-16) sont
**exclues du geste** : ce sont des références textuelles, pas des wikilinks — les convertir
serait une régression.

### D′ — un renvoi qui pointe une pierre tombale

`doctrinal/sources/guenon-recension-seabrook-aventures-arabie.md`, l. 22-24 : « Le recueil
est à ajouter à `meta/bibliotheque-physique.md` ». Cette fiche est un **tombstone** depuis
le 2026-08-22 (verdict Sidy, catalogue déplacé en `atelier/rd/bibliotheque/`). Le chemin
est corrigé ; **l'ajout du recueil au catalogue n'est pas fait** — il affirmerait une
possession, c'est la moitié qui demande un verdict (§4, signalement D).

### A — quatre archives, quatre chemins

`git add` nommant les quatre fichiers un par un (jamais `git add -A`, §7e de la fiche des
trois organes).

## 4. Ce qui n'est pas exécuté, et pourquoi

| Point | Rapport | Motif du report |
|---|---|---|
| **A / A′** — Sceau porté dans `textes/` (`status: to-source` hors vocabulaire, `sources_count: 1` sans `sources:`) | Publication 09-17 | **arbitrage de placement** (Cmd 4/§II) : déplacer vers `doctrinal/sources/` ou dépouiller le cartouche est un verdict. Le rapport lui-même ne le tranche pas. |
| **B** — slug `guenon-symboles-science-sacree` inexistant | Publication 09-17 | trois porteurs réels candidats : **nommer** le bon est une décision. |
| **D** (moitié recension) — 3 œuvres possédées absentes du catalogue | Publication 09-17 et 09-16 (D) | **affirmer une possession** au catalogue relève de Sidy. |
| **E** — forme du marqueur `to-source` sur les `type: source` | Publication 09-17 | « question de forme à trancher **en bloc** » — convention, non faute. |
| **F** — fait personnel en circuit neutre (`technics-su-8080.md:21`) | Publication, 4ᵉ jour | étanchéité §VI : retrait ou déplacement = arbitrage. |
| **Fiches jumelles Burckhardt**, **`cross_links` en forme courte** | Publication 09-16 (C, F) | fusion ou subordination / entériner une convention : verdicts. |
| **2 cibles `label/`** (`album-01`, `site-dans-labsolu`) | les deux profils, 3ᵉ jour | créer la fiche = production de contenu. |
| **71 avertissements C5/C6** | les deux profils | **déjà tranchés** (verdict Sidy 2026-09-10, `7bef4e1`). Le compte doit rester à 71 après la passe. |
| **`stash@{0}`** (P1/P2 Studio) | Studio 09-17 | le danger nommé est le **réflexe de rangement** : ni `pop`, ni renommage, ni suppression. |
| **Décomposition publiée par le script de cartographie** (P1a 09-16), contrôle `status:` élargi (B8), `detecter-nouvelles-fiches-rd.sh`, `verifier-renvois-skills.py` | Studio 09-16 et 09-17 | modifications d'**instrument** : triptyque intent/spec/plan et épreuve par l'échec (§VII) — un chantier, pas un correctif. |
| **File d'écritures : 4 positions inaptes** | Studio 09-17 P4 | hors dépôt (`OUT-17`, contrat du magasin) ; la ligne est déjà ouverte. |

## 5. Contrôles

- `verifier-invariants.py` **avant** : 1744 fichiers, 0 erreur, 71 avertissements.
- `verifier-invariants.py` **après** : à reporter ci-dessous après exécution.
- Cartographie `--verifier` **avant** : 252 avertissements (lien mort 167, isolée 80, lien 5).
- Cartographie `--verifier` **après** : à reporter ci-dessous.

<!-- RESULTATS -->
