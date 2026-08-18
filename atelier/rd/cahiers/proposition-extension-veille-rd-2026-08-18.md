---
title: "Proposition — Extension du mandat R&D : veille externe + sandbox"
type: meta
statut: effectif
created: 2026-08-18
updated: 2026-08-18
tags: [atelier, rd, phase3-extension, veille, sandbox, hermes]
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]]"
  - "[[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]"
---

# Proposition — Extension du mandat R&D : veille externe + sandbox

> **Statut** : `effectif`. Le mandat est tranché verbalement par Sidy
> (2026-08-18) et opérationnellement actif dès cette date. La présente
> fiche en acte la formalisation rétroactive. Les points techniques qui
> restent à instruire (cron, prompt, mécanisme) sont indiqués en §VII ;
> ils ne bloquent pas l'exécution — la veille est effective, le
> mécanisme d'automatisation viendra après.
>
> **Articulation avec la phase 3** : la présente note est une *extension*
> du mandat déjà tranché le 2026-08-11 (cf.
> [[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition
> phase 3]]). Elle ne rouvre rien de ce qui est clos (agent désigné,
> canal, gouvernance Discord). Elle ajoute un nouveau volet — la veille
> externe + sandbox — au volet existant (veille infrastructure interne).

---

## I. Contexte — ce qui motive l'extension

L'analyse du papier Deepseek/Cordis (fiche
[[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]])
a révélé un paradigme d'ingénierie (composabilité spatiotemporelle,
effets réversibles, coeffets réactifs) qui résonne de forme avec la
convention Sashimono du dépôt et qui pourrait nourrir des chantiers
concrets (HMR pour les 12 agents, gestion des dépendances inter-gateways).

Sidy formule le souhait que cette lecture ne reste pas isolée : qu'un
agent garde un œil sur cette étude **et** plus largement sur ce qui se
fait dans le même registre (repos GitHub, papiers, implémentations),
archive qualitativement les éléments intéressants (code, équations,
méthodes), et puisse les éprouver en environnement clos (sandbox) avant
tout versement dans le dépôt.

## II. Décisions tranchées (Sidy, 2026-08-18)

| # | Question | Verdict |
|---|---|---|
| 1 | Articulation avec l'agent désigné (phase 3) | **(a)** — un seul agent (Studio Sound Engineer), mandat élargi |
| 2 | Sandbox | **Isolée** (hors dépôt versionné) |
| 3 | Périmètre de scrutage | **Latitude de recherche** (pas de liste de dépôts fixes) |
| 4 | Cadence veille externe | **Hebdomadaire** |
| 5 | Documentation vs. exécution | Fiche à créer **mais exécution effective dès maintenant** |

## III. Périmètre du nouveau volet

Le mandat du Studio Sound Engineer s'enrichit de trois registres :

| Registre | Cadence | Nature |
|---|---|---|
| Veille infrastructure interne | quotidienne | (existante, phase 3 — 3 scripts + empreinte serveur) |
| **Veille externe R&D** | **hebdomadaire** | scrutage GitHub, arXiv, dépôts signalés ; archivage qualitatif |
| **Sandbox** | **à la demande** (suite à veille) | environnement clos pour éprouver des montages |

**Principe directeur** : démarche qualitative, temps long, mesurée,
réfléchie. Pas de collecte volumétrique, pas de précipitation. Un
élément n'est archivé que s'il a une pertinence reconnue ; un montage
n'est tenté en sandbox que s'il a été qualifié d'abord.

## IV. Architecture des nouveaux lieux dans `atelier/rd/`

```
atelier/rd/
├── index.md           (charte, mise à jour ce jour)
├── veille/            (NOUVEAU — 2026-08-18)
│   ├── index.md       (charte du lieu, périmètre, règles)
│   ├── registre.md    (journal append-only des scrutations)
│   └── <projet>/      (un sous-dossier par source externe qualifiée)
│       ├── equations.md
│       ├── methodes.md
│       └── notes-lecture.md
└── (sandbox est HORS dépôt versionné — voir §V)
```

**Règles du lieu `veille/`** :
- `raw/` reste immuable (sources brutes) ; `veille/` reçoit les EXTRAITS
  structurés, une page = un sujet.
- Tout versement dans `veille/` passe par `_inbox/` puis validation
  humaine (Cmd 9) — sauf première matière issue de la présente
  extension, versée en direct par cohérence avec l'acte d'ouverture.
- `statut_experience: exploratoire` pour l'ensemble du sous-dossier.
- Les fiches de veille n'engagent aucun versement dans doctrinal/,
  hermeneutique/, label/ — elles restent confinées à `rd/`.

## V. Sandbox — hors dépôt

**Verdict** : isolée. Emplacement : `/root/sandbox-rd/` (ou équivalent
hors `/root/wiki/`).

**Règles** :
- Aucun artefact de sandbox n'entre dans le dépôt versionné sans
  verdict humain explicite (Cmd 12).
- La sandbox est un jardin d'essai : on y plante, on observe, on note
  dans `rd/veille/<projet>/resultats-sandbox.md` (fiche de synthèse,
  pas le code).
- Isolation stricte : venv dédié, pas d'accès réseau sortant sauf
  explicite, pas d'écriture hors du répertoire sandbox.
- Chaque chantier sandbox est un sous-dossier nommé (`cordis/`,
  `hmr-agents/`, etc.) avec son propre `README.md` documentant
  l'intention, la méthode, le verdict.

## VI. Gouvernance — articulation avec les commandements

- **Cmd 12/13** : tout versement dans les circuits du dépôt passe par
  validation humaine. La veille R&D signale (Discord #infrastructure ou
  rapport en session) ; elle n'écrit jamais d'office dans les circuits
  doctrinal/hermeneutique/label.
- **Cmd 9** : les annales de l'atelier portent la trace des scrutations
  (une entrée par passe groupée, préfixe `## [YYYY-MM-DD] veille-rd |`).
- **Risque §IV de la phase 3** (surface d'écriture d'un agent) : contenu
  par la règle déjà tranchée — signalement Discord uniquement, jamais
  d'écriture directe au registre, quel que soit le volet (infrastructure
  interne ou veille externe).
- **Règle 9 du protocole racine** (extension `raw/` conditionnelle) :
  non applicable ici, car `veille/` n'est pas `raw/`. Le régime propre
  à `veille/` (§IV ci-dessus) est celui défini par la présente note.

## VII. Ce qui reste à instruire (Cmd 6, non bloquant)

| Chantier | Statut |
|---|---|
| Extension effective du prompt Studio Sound Engineer (section veille R&D) | À instruire |
| Mécanisme de cron hebdomadaire pour la veille externe | À instruire |
| Mise en place effective de `/root/sandbox-rd/` | À instruire |
| Format du rapport hebdomadaire (sections, longueur, canal) | À instruire |

**Non-blocage** : la veille peut démarrer manuellement (c'est le geste
effectif de ce jour) avant que le cron ne soit écrit. L'exécution
précède l'automatisation — le cron viendra formaliser un geste déjà
éprouvé.

## VIII. Première veille — acte d'ouverture (2026-08-18)

La veille est effective dès ce jour. Le premier acte de veille porte sur
le périmètre Cordis/DeepSeek (source de la présente proposition) :
scrutage des repos GitHub du projet, recherche arXiv sur les concepts
clés, extraction qualitative des éléments pertinents. Le résultat de
cette première passe est versé dans `atelier/rd/veille/cordis/`.

## IX. Liens

- Charte du pôle : [[atelier/rd/index]] (mise à jour ce jour)
- Phase 3 d'origine : [[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]]
- Fiche Cordis (source de la présente extension) :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
