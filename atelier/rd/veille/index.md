---
title: "Veille R&D — charte du lieu"
type: index
tags: [atelier, rd, veille, souverainete]
created: 2026-08-18
updated: 2026-08-18
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]]"
---

# Veille R&D (`atelier/rd/veille/`)

Ouvert le 2026-08-18 sur verdict de Sidy. Ce lieu reçoit les extraits
structurés issus de la veille externe (repos GitHub, papiers,
implémentations) — pas les sources brutes (qui restent en `raw/`).

## Mission

Scruter qualitativement ce qui se fait dans le registre de la
souveraineté logicielle, de la composabilité dynamique, des paradigmes
d'ingénierie réversibles. Archiver les éléments pertinents (code,
équations, méthodes) de façon mesurée, dans le temps long. Ne rien
collecter par volume ; ne retenir que ce qui a une portée reconnue.

## Périmètre

- **Sources** : dépôts GitHub, papiers arXiv, implémentations
  open-source, tout ce qui relève de la souveraineté logicielle, de la
  composabilité, des effets réversibles, des systèmes dynamiques.
- **Latitude** : l'agent (Studio Sound Engineer) a une latitude de
  recherche — pas de liste de dépôts fixes, mais un discernement
  qualitatif au fil de l'eau.
- **Cadence** : hebdomadaire (pas de collecte quotidienne — le temps
  long est la condition de la qualité).

## Règles du lieu

1. **raw/ reste immuable** : les sources brutes (PDF, archives) vivent
   en `raw/` ; `veille/` reçoit les EXTRAITS structurés, une page = un
   sujet.
2. **Une page = un sujet** : pas de fiche fourre-tout. Chaque concept,
   chaque équation, chaque méthode a sa propre page.
3. **Statut** : `statut_experience: exploratoire` pour l'ensemble du
   sous-dossier. Aucune fiche de veille n'est close tant que le projet
   scruté n'a pas été éprouvé en sandbox ou invalidé.
4. **Confinement** : les fiches de veille n'engagent aucun versement
   dans doctrinal/, hermeneutique/, label/. Elles restent dans `rd/`.
   Tout franchissement de circuit passe par validation humaine (Cmd 12).
5. **Registre** : `registre.md` (journal append-only) porte la trace de
   chaque scrutation (quoi, pourquoi, verdict, lien). Une scrutation
   sans verdict n'est pas consignable — on attend d'avoir qualifié
   avant de noter.
6. **Sandbox** : les résultats d'éprouve en sandbox (hors dépôt,
   `/root/sandbox-rd/`) sont synthétisés dans une fiche
   `<projet>/resultats-sandbox.md` — pas le code lui-même, mais le
   compte-rendu de ce qui a été tenté, ce qui a marché, ce qui a échoué,
   pourquoi.

## Arborescence cible

```
atelier/rd/veille/
├── index.md           ← la présente charte
├── registre.md        ← journal append-only des scrutations
├── cordis/            ← premier projet scruté (2026-08-18)
│   ├── equations.md
│   ├── methodes.md
│   ├── notes-lecture.md
│   └── resultats-sandbox.md (à venir)
└── <autres-projets>/  ← un sous-dossier par source externe qualifiée
```

## Articulation avec le reste du dépôt

- **raw/** : sources brutes (PDF, archives). `veille/` en extrait la
  matière structurée.
- **atelier/rd/outillage/** : fiches d'instruction de sources
  spécifiques (ex. Cordis, 2026-08-16). `veille/` reçoit la matière
  extraite ; `outillage/` reçoit la fiche d'instruction globale.
- **atelier/rd/cahiers/** : journal des décisions, propositions,
  registres. La présente charte est une décision ; le `registre.md` de
  veille est un journal de scrutations.
- **Sandbox** (`/root/sandbox-rd/`) : hors dépôt. Les résultats
  d'éprouve sont synthétisés dans `veille/<projet>/resultats-sandbox.md`.

## Liens

- Charte du pôle : [[atelier/rd/index]]
- Proposition d'extension : [[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]]
- Fiche Cordis (source de la présente extension) :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
