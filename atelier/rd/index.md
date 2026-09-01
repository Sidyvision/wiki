---
title: "Pôle R&D de l'atelier — charte du lieu"
type: index
tags: [atelier, rd, infrastructure, souverainete]
created: 2026-08-08
updated: 2026-09-01
sources: []
links: []
---

# Pôle R&D de l'atelier (`atelier/rd/`)

Ouvert le 2026-08-08 sur verdict de Sidy (Option C, nom `rd/`, phase 1
partielle). Ce pôle n'est **pas un sixième circuit** : il vit à l'intérieur du
circuit `atelier/`, dont il hérite le Sceau (§V.a) et le régime de liens
(§VI). Proposition d'origine :
(cf. Domaine Réservé, fiche le pôle R&D de l'atelier) (brouillon visé pour son architecture par le verdict).

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
├── registre-chantiers.md  ← carte vivante de TOUS les chantiers ouverts du dépôt
│                             (ouvert 2026-09-01) — recense et pointe, n'absorbe rien
│   (la racine du pôle ne porte que ces deux fichiers : toute fiche vit dans
│    un sous-dossier, assaini le 2026-09-01)
├── instrument/        ← l'Instrument (migration depuis atelier/projets/, fiche par fiche)
├── infrastructure/    ← setup réel : serveur, agents, hardware/software
│                         (destination de la transposition Mother Base §5 bis)
│   └── monitoring-archive/  ← archive .txt du rapport monitoring quotidien
│                              (rétention 40 j, ouvert 2026-08-18)
├── audio/             ← ingénierie son GÉNÉRIQUE (bancs d'essai, chaînes, mesures) ;
│                         l'ingénierie PAR MORCEAU reste au label
├── outillage/         ← scripts, leur documentation, leurs bancs de test
├── veille/            ← veille externe R&D (GitHub, arXiv, dépôts) —
│                         ouvert 2026-08-18, hebdomadaire, qualitatif
├── cahiers/           ← cahiers append-only : registre-problemes.md (ouvert
│                         2026-08-08, échecs/blocages), journal-optimisations.md
│                         (ouvert 2026-08-30, réussites — miroir du registre),
│                         bilan-pont 2026-08-15, comptes-rendus de sessions ;
│                         cahiers d'expérience à venir (phase 2)
├── incidents/         ← rapports d'incident (contamination Unicode 2026-08-22,
│                         crash gateway 2026-08-25) ; cf. Cmd 15 du protocole racine
├── bibliotheque/      ← catalogue de la bibliothèque physique (déplacé de
│                         `meta/` le 2026-08-22), fiches `index-livre`
│                         transcrites des index et glossaires photographiés,
│                         validateur et générateur du lexique unifié
└── citadelle-du-sham/ ← prototype 3D reçu au sas, versé ici le 2026-08-22
```

### `bibliotheque/` — instrument de repérage (ouvert 2026-08-22)

| pièce | rôle |
|---|---|
| `catalogue-bibliotheque.md` | recension des ouvrages possédés (ex-`meta/bibliotheque-physique.md`) |
| `index-<slug>.md` | un index ou glossaire transcrit par ouvrage — `terme → page`, aucun contenu doctrinal |
| `valider-index-livres.py` | contrôles bloquants : Cmd 15, pages numériques, couverture photo, doublons signalés jamais fusionnés |
| `generer-glossaire-unifie.py` | lexique unifié dérivé — refuse de générer si le validateur bloque |
| `glossaire-unifie.md` | **artefact dérivé, jamais édité à la main** |

Usage : savoir *où chercher*. La levée d'un `to-source` reste la vérification du
texte primaire par Sidy (§VII) — l'instrument dit où regarder, jamais quoi
conclure. `doctrinal/` ne lie jamais vers `atelier/` : la consultation est
humaine, sans wikilink.

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
| Veille externe R&D (GitHub, arXiv, dépôts scrutés) | `rd/veille/` (ouvert 2026-08-18, hebdomadaire) |
| Sandbox (éprouve de montages issus de veille) | **hors dépôt** (`/root/sandbox-rd/`) |

La frontière `meta/` ↔ `rd/` suit la règle existante : jamais de fait personnel
ni de motif sensible dans une page neutre ; `rd/` reçoit ce qui est publiable
dans le dépôt.
## État du pôle — résumé (2026-09-01)

Le pôle est **ouvert et actif** depuis le 2026-08-08 (verdict Sidy : Option C, nom `rd/`,
phase 1 partielle). Ce qui est acquis :

- **le lieu** — la présente charte, l'arborescence, le Sceau atelier étendu (types
  `experience | infrastructure | outillage`, champ optionnel `statut_experience`), le
  régime de liens, les annales de l'atelier au Cmd 9 ;
- **la migration** du 2026-08-08 — 16 fiches de `atelier/projets/` versées ici fiche par
  fiche, stubs `deprecated` avec pointeur conservés côté `projets/` (Cmd 10) ;
- **les cahiers de laboratoire** — registre des problèmes (2026-08-08),
  journal des optimisations (2026-08-30), tous deux append-only ;
- **les extensions successives** — veille externe et sandbox hors dépôt (2026-08-18),
  archive du monitoring quotidien (2026-08-18), bibliothèque (2026-08-22), incidents
  (2026-08-22), citadelle du Shâm (2026-08-22).

Ce qui n'est **pas** acquis : la discipline de laboratoire complète (bloc 🧪 Expérience,
règle de reproduction — phase 2) et l'automatisation de la veille infrastructure
(phase 3 : décisions tranchées, aucun automatisme écrit).

**Assainissement de la racine du pôle (2026-09-01, verdict Sidy).** Cinq fiches vivaient
à la racine de `rd/`, hors de toute arborescence déclarée et sans lien entrant. Trois
portaient du **fait personnel dans une page neutre** — l'interdit du §VI — et sont versées
au Domaine Réservé avec leur historique git ; deux, neutres, sont classées dans le
sous-dossier de leur nature. Deux fiches restées côté `rd/` portaient le même défaut à
l'intérieur de leur corps : les blocs concernés ont été retirés, la matière étant conservée
au Domaine Réservé (Cmd 10 — déplacement, jamais suppression sèche).

Le versant **publiable** de la matière versée est écrit en propre, et indexé ici :

- [[atelier/rd/infrastructure/2026-08-23_deploiement-veille-infrastructure-quotidienne]] —
  le script de veille quotidienne existe et est exécutable ; **aucun des trois jobs cron
  qu'une fiche déclarait créés n'est déclaré dans aucun profil aujourd'hui**. Même motif
  que l'incident du 2026-08-17 qui a fait naître le champ `infra_verif`.
- [[atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe]] — quels contrôles
  mécaniques le dépôt possède, lequel appeler, et ce qui manque encore.
- Pour la troisième fiche versée, la contrepartie **existait déjà** :
  [[atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes]]. Aucune
  quatrième fiche n'a été créée — une page = un sujet (Cmd 4).

Classées par leur nature : [[atelier/rd/infrastructure/synthese-deploiement-memoire]] et
[[atelier/rd/cahiers/2026-08-30_session-corrections-rapports-rotation-hmac]].

**Où lire la suite.** Le détail chronologique de tout ce qui s'est ouvert entre le
2026-08-08 et le 2026-08-31 — qui vivait ici et alourdissait la charte — est déplacé sans
retouche dans [[atelier/rd/cahiers/2026-09-01_jalon-chronologie-phase1-rd]]. L'**état
vivant des chantiers**, lui, est tenu dans [[atelier/rd/registre-chantiers]] : c'est là
qu'un agent qui reprend le fil doit regarder en premier.
