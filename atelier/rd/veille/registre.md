---
title: "Registre de veille R&D — journal des scrutations"
type: registre
tags: [atelier, rd, veille, registre]
created: 2026-08-18
updated: 2026-08-18
sources: []
links:
  - "[[atelier/rd/veille/index]]"
---

# Registre de veille R&D

Journal append-only des scrutations menées dans le cadre de la veille
externe. Chaque entrée porte : ce qui a été scruté, pourquoi, le
verdict, le lien vers la matière extraite.

**Règle** : une scrutation sans verdict n'est pas consignable. On attend
d'avoir qualifié avant de noter. Le registre n'est pas un journal de
bord (quoi j'ai fait aujourd'hui) mais un journal de décisions (quoi
j'ai retenu, pourquoi).

---

## [2026-08-18] Scrutation GitHub — implémentations Cordis

**Quoi** : recherche GitHub sur "spatiotemporal composability", "revertible effects", "reactive coeffects".

**Pourquoi** : identifier les implémentations open-source du paradigme Cordis (papier DeepSeek/Peking Univ), qualifier leur pertinence pour le dépôt.

**Verdict** : 7 repos trouvés, tous implémentations du paradigme dans différents langages (JVM, Rust, Go, Wasm, langage de recherche). Les plus pertinents :
- **cordis4j** (JVM, 4★) — implémentation la plus mature
- **spatiotemporal** (Rust, 2★) — articulation avec le borrow checker
- **cordis-wasm** — sandbox Wasm qui *force* le paradigme
- **spatiotemporal-composability-skill** — skill agent pour recomposition à l'exécution (potentiellement pertinent pour Hermes)

**Liens** :
- Matière extraite : `atelier/rd/veille/cordis/implementations-github.md`
- Repos scrutés : voir la fiche ci-dessus

**Questions ouvertes** :
- Quel est le dépôt source Cordis (TypeScript original) ?
- Qui est `inso1337` (auteur de 2 repos) ?
- Le repo `spatiotemporal-composability-skill` est-il une skill Hermes ?

---

## [2026-08-18] Ouverture du lieu

**Quoi** : ouverture de `atelier/rd/veille/` sur verdict de Sidy.
Première scrutation : périmètre Cordis/DeepSeek (source de la présente
extension).

**Pourquoi** : le papier *A Programming Paradigm for Spatiotemporal
Composability* (Shi, Zhang, Cui — Peking University / DeepSeek-AI)
décrit un paradigme d'ingénierie (composabilité spatiotemporelle,
effets réversibles, coeffets réactifs) qui résonne de forme avec la
convention Sashimono du dépôt et qui pourrait nourrir des chantiers
concrets (HMR pour les 12 agents, gestion des dépendances
inter-gateways). La présente extension vise à ne pas laisser cette
lecture isolée : garder un œil sur ce qui se fait dans le même registre,
archiver qualitativement, éprouver en sandbox.

**Verdict** : périmètre qualifié comme pertinent. Matière extraite vers
`cordis/` (équations, méthodes, notes de lecture, implémentations GitHub).
Sandbox à instruire séparément.

**Liens** :
- Matière extraite : `atelier/rd/veille/cordis/`
- Fiche d'instruction globale :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
- Proposition d'extension :
  [[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]]
