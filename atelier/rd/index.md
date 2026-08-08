---
title: "Pôle R&D de l'atelier — charte du lieu"
type: index
tags: [atelier, rd, infrastructure, souverainete]
created: 2026-08-08
updated: 2026-08-08
sources: []
links: []
---

# Pôle R&D de l'atelier (`atelier/rd/`)

Ouvert le 2026-08-08 sur verdict de Sidy (Option C, nom `rd/`, phase 1
partielle). Ce pôle n'est **pas un sixième circuit** : il vit à l'intérieur du
circuit `atelier/`, dont il hérite le Sceau (§V.a) et le régime de liens
(§VI). Proposition d'origine :
[[meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08|le pôle R&D de
l'atelier]] (brouillon visé pour son architecture par le verdict).

## Mission (verdict du 2026-08-08)

> « Tout ce qui en relève doit systématiquement y être consigné avec comme but
> l'entretien, le développement qualitatif, l'optimisation à mesure de
> l'infrastructure globale hardware/software, l'émancipation progressive de
> tout intermédiaire de service tiers par souveraineté des moyens de
> production / déploiement / information. Un des agents sera chargé de veiller
> à cette tâche spécifique. »

Le pôle est donc un **lieu de consignation systématique** : tout travail
d'ingénierie — technique, musicale, matérielle, logicielle, outillage,
infrastructure — a vocation à y laisser trace. Horizon : que le dépôt devienne
un véritable laboratoire ; visée : la souveraineté des moyens.

## Arborescence

```
atelier/rd/
├── index.md           ← la présente charte
├── instrument/        ← l'Instrument (migration depuis atelier/projets/, fiche par fiche)
├── infrastructure/    ← setup réel : serveur, agents, hardware/software
│                         (destination de la transposition Mother Base §5 bis)
├── audio/             ← ingénierie son GÉNÉRIQUE (bancs d'essai, chaînes, mesures) ;
│                         l'ingénierie PAR MORCEAU reste au label
├── outillage/         ← scripts, leur documentation, leurs bancs de test
└── cahiers/           ← cahiers d'expérience, append-only (ouverts en phase 2)
```

## Régime des deux sous-régimes de l'atelier

- **référence** : `atelier/materiel/`, `atelier/entretiens/` — ce qu'on consulte ;
- **recherche** : `atelier/rd/` et `atelier/etudes-de-cas/` — ce qu'on instruit.

## Ce qui vit où (frontières)

| Matière | Destination |
|---|---|
| Specs, itérations, notes d'impact de l'Instrument | `rd/instrument/` (migration de `projets/`) |
| Architecture générique du serveur et des agents, bancs, mesures | `rd/infrastructure/` |
| Motifs des décisions, credentials, prompts d'agents | **reste en `meta/projet-unifie/`** (sensible — §VI) |
| Ingénierie d'une œuvre, par morceau | **reste au label** (`label/musique/ingenierie/`) |
| Fiches machines, manuels, routing | **reste en `atelier/materiel/`** (référence) |
| Scripts déterministes du dépôt et leur documentation | `rd/outillage/` |

La frontière `meta/` ↔ `rd/` suit la règle existante : jamais de fait personnel
ni de motif sensible dans une page neutre ; `rd/` reçoit ce qui est publiable
dans le dépôt.

## État de la phase 1 partielle

- **Ouvert** : le lieu (présente charte + arborescence), le Sceau atelier étendu
  (§V.a : types `experience | infrastructure | outillage`, champ optionnel
  `statut_experience`), le régime de liens (§VI : `rd/` hérite du régime de
  `projets/`), l'élargissement de `liens_atelier` (§V.d), les annales de
  l'atelier au Cmd 9.
- **Migration effectuée le 2026-08-08** (fiche par fiche, §IV) : 16 fiches de
  `atelier/projets/` migrées vers `rd/instrument/` (15) et `rd/outillage/` (1),
  slugs conservés ; chaque ancienne fiche subsiste en stub `deprecated` avec
  pointeur (Cmd 10) ; assets (`assets-instrument/`), données
  (`instrument-donnees.yaml`, `wiki-manifest.json`), prototype et script
  `generer-manifeste.py` déplacés avec les fiches ; liens entrants repointés.
  Reste en `projets/` : `album-personnel.md` (arbitrage `rd/` vs `label/`, §IV —
  à trancher, verdict Sidy).
- **Non inclus dans la phase 1 partielle** (viennent ensuite) :
  la discipline de laboratoire (bloc 🧪 Expérience, cahiers
  d'expérience, règle de reproduction) — phase 2 ; l'agent de veille
  infrastructure (phase 3, sur désignation de Sidy).
