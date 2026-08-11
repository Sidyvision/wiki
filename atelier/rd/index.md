---
title: "Pôle R&D de l'atelier — charte du lieu"
type: index
tags: [atelier, rd, infrastructure, souverainete]
created: 2026-08-08
updated: 2026-08-11
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
d'ingénierie — technique, matérielle, logicielle, outillage, infrastructure —
a vocation à y laisser trace. Horizon : que le dépôt devienne
un véritable laboratoire ; visée : la souveraineté des moyens.

**Nature du pôle** (précision Sidy, 2026-08-08) : `rd/` est dédié aux aspects
**ingénierie / technique / mécanique** de l'infrastructure — informatique,
studio audio, etc. Ce n'est **pas un département d'expression créative** au
sens strict ; la créativité n'y existe que sous sa forme ingénieriale (la
résolution de problème). Les œuvres, leur écriture, leur direction artistique
relèvent du label — jamais de `rd/`.

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
└── cahiers/           ← cahiers append-only : registre-problemes.md (ouvert
                          2026-08-08), cahiers d'expérience à venir (phase 2)
```

## Régime des deux sous-régimes de l'atelier

- **référence** : `atelier/materiel/`, `atelier/entretiens/` — ce qu'on consulte ;
- **recherche** : `atelier/rd/` et `atelier/etudes-de-cas/` — ce qu'on instruit.

## Ce qui vit où (frontières)

| Matière | Destination |
|---|---|
| Specs, itérations, notes d'impact de l'Instrument | `rd/instrument/` (migration de `projets/`) |
| Architecture générique du serveur et des agents, bancs, mesures | `rd/infrastructure/` (ex. [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]], [[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]]) |
| Motifs des décisions, credentials, prompts d'agents | **reste en `meta/projet-unifie/`** (sensible — §VI) |
| Ingénierie d'une œuvre, par morceau | **reste au label** (`label/musique/ingenierie/`) |
| Expression créative : œuvre, écriture, direction artistique | **label** (direction-artistique / production) — jamais `rd/` |
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
  `album-personnel.md` resté en `projets/` a été déplacé le même jour vers
  `label/production/` (verdict Sidy : création artistique, non R&D) — stub
  `deprecated` avec pointeur, 4 liens entrants `materiel/` coupés (étanchéité).
- **Non inclus dans la phase 1 partielle** (viennent ensuite) :
  la discipline de laboratoire complète (bloc 🧪 Expérience, règle de
  reproduction) — phase 2 ; l'agent de veille
  infrastructure (phase 3, sur désignation de Sidy).
- **Registre des problèmes ouvert le 2026-08-08** (verdict Sidy, premier cahier
  concret de la phase 2) : [[atelier/rd/cahiers/registre-problemes]] — append-only, format
  Symptôme brut / Diagnostic / Résolution / Compréhension tirée / Liens / Statut ;
  amorcé rétroactivement avec 3 entrées de la session de migration. Tout problème,
  erreur ou blocage rencontré dans les travaux du pôle doit y être consigné ; un
  échec se consigne comme un succès (règle 3 du laboratoire).
- **Outillage déterministe (session du 2026-08-11)** :
  [[atelier/rd/outillage/spec-detecter-non-tracke|detecter-non-tracke.py]] —
  constat des fichiers non trackés par git, classé par circuit (même famille
  que `verifier-invariants.py`, ni LLM ni réseau).
