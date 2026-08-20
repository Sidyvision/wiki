---
title: "Étude du dépôt — cartographie, état des index et inventaire raw/ (2026-08-20)"
type: infrastructure
status: brouillon
tags: [atelier, rd, infrastructure, depot, exploration]
created: 2026-08-20
updated: 2026-08-20
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
---

# Étude du dépôt — cartographie, état des index et inventaire raw/

**Date :** 2026-08-20
**Nature :** exploration et documentation (pôle R&D) — observations
consignées, aucun verdict rendu. Collaboration avec Gardien sur l'étude
du dépôt ; points de départ : `CLAUDE.md` racine (V2, Restauration
étendue), fiche des trois territoires
(`doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md`,
adoptée), et `raw/`.

---

## 1. Carte des circuits (état observé)

| Circuit | .md | index | annales | Observations |
|---|---|---|---|---|
| doctrinal | 259 | 363 lignes | à jour (dern. entrée 2026-08-20) | le plus volumineux ; 8 sous-dossiers (autorites, deviations, discernement, etudes, sources, symboles, traditions) |
| meta | 117 | 142 lignes (`meta-index.md`) | à jour (dern. entrée 2026-08-16) | Domaine Réservé ; genealogie, journal, personnel, projet-unifie (hermes-prompts, hermes-skills), protocole-archives, transmissions |
| atelier | 93 | 131 lignes | à jour (dern. entrée 2026-08-19) | materiel, entretiens, etudes-de-cas, projets, **rd/** (5 sous-pôles), et une anomalie `atelier/R/` vide |
| hermeneutique | 21 | 106 lignes | à jour (dern. entrée 2026-08-16) | 6 œuvres (death-stranding, dragon-ball, dr-slump, hunter-x-hunter, metal-gear, 20th-century-boys), auteurs, sources, et `expression/` (nouveau) |
| label | 12 | 63 lignes | dernière entrée 2026-08-08 | direction-artistique, distribution, marketing-communication, production |

**Pôle R&D (`atelier/rd/`)** — charte 2026-08-08, mission de
consignation systématique (verdict cité dans `index.md`) :

- `instrument/` — 16 fiches migrées de `projets/` le 2026-08-08,
  specs anneau zodiacal, axe 38°, prototype, données yaml, manifest.
- `infrastructure/` — setup réel serveur/agents/hardware ; sous-dossier
  `monitoring-archive/` (rétention 40 j, ouvert 2026-08-18, 3 archives
  présentes : 08-17, 08-18, 08-19) ; projet `bureau/` (TUI, app.py +
  modules + services + tests).
- `audio/` — vide (`.gitkeep`) — bancs d'essai génériques à venir.
- `outillage/` — 7 scripts déterministes + specs + `.snapshots-rd/`.
- `veille/` — ouvert 2026-08-18 ; `cordis/` (equations, methodes,
  implementations-github, notes-lecture), `index.md`, `registre.md`.
- `cahiers/` — registre-problemes (append-only), bilan pont-agents
  2026-08-15, brouillons extension zodiacale (12 fichiers),
  propositions phase 3 et extension veille.

**Hors circuits :** `Graphe/` (generer-cartographie.py + html live),
`carte-du-depot.py`, `verifier-invariants.py` (racine), `_inbox/`
(2 dépôts : citadelle-du-sham, interview trame spirituelle),
`_depot-lecture/`, `.claude/`.

## 2. État des vérifications mécaniques (2026-08-20)

- `verifier-invariants.py --racine /root/wiki` → **18 erreurs,
  58 avertissements**. Les erreurs C1 se concentrent sur deux fichiers :
  `rd/infrastructure/traitement-avertissements-isoles-rapport-2026-08-18.md`
  (liens fictifs dans le corps du texte : crochets vides, `x`, `x/y`,
  `meta/...` — motifs d'exemple lus comme liens) et
  `doctrinal/annales.md` (2 crochets vides). Observation : le rapport
  d'avertissements auto-pollue la vérification — écho du finding déjà
  consigné au registre (« rapport auto-polluant », entrée 2026-08-18).
- `Graphe/generer-cartographie.py --verifier` → **4 anomalies
  bloquantes** (frontmatter) :
  1. `doctrinal/discernement/2026-08-20_traite-emanation-gauche-isaac-ha-kohen.md`
     — manque `status`, `created`, `updated` ;
  2. `doctrinal/sources/sefer-yetsira-ramban_source.md` — manque
     `status`, `updated` ;
  3. `doctrinal/sources/traite-emanation-gauche-isaac-ha-kohen_source.md`
     — manque `type`, `status`, `updated` ;
  4. `rd/infrastructure/analyse-temporelle-code-meta-raisonnement-ia-2026-08-19.md`
     — frontmatter absent.
  Les trois premières concernent le lot kabbale du 2026-08-20 ;
  la quatrième une fiche veille du 2026-08-19.

- **État git** : working tree non propre —
  `M doctrinal/annales.md`, `M hermeneutique/annales.md`,
  `?? doctrinal/sources/elbenni-dreaming-ummah-islamofuturism-2025.md`,
  `?? hermeneutique/expression/` (fiche barzakh onirique, 2026-08-20).
  Ces quatre éléments paraissent former le lot islamofuturisme en cours
  (non committé au moment de l'exploration).

## 3. Inventaire raw/ — ressources et nature

**Volume** : 45 fichiers en racine de `raw/` + 16 sous-dossiers
thématiques (corpus Guénon) ; ≈ 328 Mo au total.

### 3.1 Corpus Guénon (sous-dossiers thématiques)

16 dossiers correspondant aux ouvrages : Aperçus sur l'Ésotérisme
islamique et le Taoïsme (14 f.), Aperçu sur l'initiation (52), Autorité
Spirituelle et Pouvoir Temporel (7 + **un doublon** avec espace en fin
de nom, 2 f.), Autres ressources (4), Études sur l'Hindouïsme (39),
Initiation et Réalisation Spirituelle (34), La Crise du Monde Moderne
(9), La Grande Triade (28), Le Règne de la Quantité (44), Le Roi du
Monde (12), Les états multiples de l'être (20), Les Principes du Calcul
Infinitésimal (26), Le Symbolisme de la Croix (31), Le Théosophisme
(68). Format : transcriptions `.md` par chapitre + index de l'œuvre.
Un script `organize_guenon.sh` (2026-08-13) a produit cette
organisation.

### 3.2 Ressources nouvelles (datées d'août 2026, non présentes
dans l'état du 2026-06-02)

**Nature doctrinale / sources primaires :**
- `sefer_yetsira_-_Ramban.pdf` + `sefer-yetsira-ramban.md` (2026-08-20)
  — déjà intégré : fiche source + état des lieux kabbale.
- `traite-emanation-gauche-isaac-ha-kohen.md` (2026-08-20) — déjà
  intégré (lot kabbale, annales 2026-08-20).
- `Hashiya-Issue-01-Elbenni.pdf` (2026-08-20 07:11) — article
  académique « Dreaming the Ummah » ; fiche source créée
  (`doctrinal/sources/elbenni-...`, non committée).
- `maymaniya_p1.pdf` (2026-08-20 08:09, 69 Mo) — nature non examinée
  (extraction PDF non tentée dans cette session) ; taille et date
  suggèrent un dépôt du jour.
- `claudes-constitution.pdf` (2026-08-20 08:11) — idem, dépôt du jour.
- `Large_language_models_for_automated_Isla.pdf` (2026-08-10) — papier
  académique LLM/islam, non encore fiché.
- `islam-and-artificial-intelligence.pdf` (juin) — idem, plus ancien.

**Nature ingénierie / R&D :**
- `A Programming Paradigm for Spatiotemporal Composability.pdf`
  (2026-08-16) — paradigme Cordis, déjà en veille
  (`rd/veille/cordis/`).
- Manuels studio (juin, déjà anciens) : 1073SPX, Model12, Revox A77
  (3 fichiers), distressor, Logic Pro iPad.
- `facture-woodbrass-...` ×2 (2026-08-18) — factures matériel studio
  (Tascam Model12, Neve 1073SPX) — nature administrative.

**Nature administrative / personnelle (signalée, hors circuit) :**
- Relevés de compte ×7 + relevé annuel de frais (2026-08-10) —
  documents bancaires au nom de M. Sidy Lamine Kouyaté. À la discrétion
  de Sidy quant à leur maintien en `raw/`.
- `grr-academix-2026.pdf`, `Body_Types_Book.pdf`, `ChatGPT historique`
  (41 Mo, export).

**Nature spirituelle / rituelle (juin, déjà présents) :** Awrad Ibn
Arabi, Wazifa, Dua Laylatul Qadr, Salat al-Kaffarat, Prayer 15th
Shabān, مولد الرسول الأعظم, إجازة-94/95, Al-Hadj-Cheikh-Belmadi-2017,
shams-al-maarif (58 Mo), universal-man, Jesus_And_Enoch_In_Ibn_'arabi.

**Nature logique / enseignement :** Isaghuji ×3 (dont Cours01
2026-08-11 « Introduction Pédagogique — Mehdi »), Intro to Logic
Zaytuna, LA FIN DES TEMPS MODERNES (astrologie traditionnelle).

**Nature herméneutique / culture :** TheArtOfDeathStranding (62 Mo,
2026-08-13) — déjà fiché en hermeneutique (art-of-death-stranding).
`Interview with Russell Elevado - Gearspace` (juin).

**Script en raw/ :** `organize_guenon.sh` — script utilitaire logé
dans `raw/` ; la charte rd/ prévoit que les scripts déterministes
vivent en `rd/outillage/`. Observation consignée, déplacement éventuel
à la discrétion de Sidy.

## 4. Anomalies et points ouverts (observations, sans verdict)

1. **`atelier/R/`** — dossier vide (2026-08-11), homonyme probable de
   `atelier/rd/`. Candidat à clarification (fusion, suppression ou
   intention distincte).
2. **`raw/Autorité Spirituelle et Pouvoir Temporel ` (avec espace)** —
   doublon du dossier sans espace (2 fichiers vs 7).
3. **4 anomalies frontmatter bloquantes** au générateur de
   cartographie (§2) — lot kabbale 2026-08-20 + fiche veille 2026-08-19.
4. **Working tree git non propre** — lot islamofuturisme en cours
   non committé (§2).
5. **Rapport d'avertissements auto-polluant** — 16 des 18 erreurs
   C1 proviennent des motifs d'exemple entre doubles crochets contenus
   dans le corps du rapport `traitement-avertissements-isoles-rapport-2026-08-18`
   (fait déjà consigné au registre-problèmes, entrée 2026-08-18).
6. **`/root/sandbox-rd/` absent** du système de fichiers au moment de
   l'exploration, bien que la charte rd/ et la proposition d'extension
   veille (2026-08-18) la désignent comme lieu d'épreuve hors dépôt.
7. **`maymaniya_p1.pdf` et `claudes-constitution.pdf`** — dépôts du
   jour (2026-08-20 08:09/08:11), nature non examinée ; extraction PDF
   non tentée (commande refusée en session). À qualifier par Sidy ou
   lors d'une prochaine session.
8. **Documents bancaires en `raw/`** — maintien à la discrétion de
   Sidy (données personnelles dans un dépôt par ailleurs canonique).

## 5. Points d'appui pour la suite

- `CLAUDE.md` racine (V2) : quatre circuits + label + meta, Sceau
  Recteur, régime de liens, commande 9 (annales), commande 10 (jamais
  de suppression sèche), commande 12 (verdicts réservés à Sidy).
- Fiche des trois territoires (adoptée 2026-08-11) : le flux
  Discernement → R&D → Doctrine/Archivage légitime le Laboratoire ;
  cette fiche s'inscrit dans le registre exploratoire (spéculation →
  chantier → qualification réservée).
- `rd/index.md` : frontières matière/destination (tableau « Ce qui vit
  où ») — référence pour tout reclassement futur.
- `rd/cahiers/registre-problemes.md` : append-only, tout problème s'y
  consigne ; les points 1-8 ci-dessus sont des observations candidates,
  non encore inscrites (l'inscription au registre relève d'une décision
  de session, pas d'une exploration).

---

*Fiche d'exploration — observations consignées, aucune qualification
rendue. Les verdicts et arbitrages restent réservés à Sidy (Cmd 12).*
