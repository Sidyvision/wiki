بسم الله الرحمن الرحيم

# CLAUDE.md — Protocole local : circuit `hermeneutique/`

> **Statut : méthode à l'essai** (éclatement expérimental du 2026-08-12, verdict
> Sidy). Ce fichier porte la lettre complète des règles **propres** au circuit
> `hermeneutique/` — Sceau, nomenclature, règles de liens, clause de plasticité.
> Les règles **transversales** (étanchéité inter-circuits, discipline des sources,
> double contrôle sashimono/Gizeh, commandements absolus, supervision des agents)
> restent dans le `CLAUDE.md` racine, **toujours chargé** quel que soit le dossier
> de travail — ce fichier ne s'y substitue pas, il le complète. En cas de doute ou
> de silence de ce fichier sur un point, le `CLAUDE.md` racine fait foi. Version
> pré-éclatement intégrale : `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md`.

-----

## Objet du circuit

Espace de traitement et de navigation de ce qui relève du **domaine
intermédiaire**. Les médiums de fiction (jeu vidéo, manga, anime, théâtre, série,
film, roman…) y sont considérés comme des **interfaces** offertes à un ordre de
possibilités subtiles, non comme de simples objets culturels. Double fonction
assumée : lecture herméneutique, et bureau de Direction Artistique en amont de
`label/direction-artistique/`.

Le circuit accueille en outre l'**expression** d'idées et intuitions personnelles
— notamment issues d'expériences post-khalwa déjà versées en
`doctrinal/discernement/` — dont la formulation emprunte au vocabulaire de ces
œuvres et qui ne peuvent, à ce titre, être portées par le circuit doctrinal. Les y
accueillir, c'est les situer à leur état propre pour en apprécier la juste
portée : **ce n'est jamais lever un garde-fou.**

## Nomenclature

`hermeneutique/auteurs/<slug>.md` ; `hermeneutique/<slug-oeuvre>/<slug-oeuvre>.md`
pour la fiche-hub (nom du dossier redoublé) ; `hermeneutique/<slug-oeuvre>/<slug>.md`
pour les figures, dispositifs et analyses ; `hermeneutique/expression/<slug>.md`.
`index.md` est **réservé** à l'index du circuit.

## Le Sceau herméneutique

```yaml
---
title: "Titre exact"
type: oeuvre | auteur | figure | dispositif | concept | analyse
registre: analyse | expression
medium: jeu-video | anime | manga | theatre | serie | film | roman
oeuvre: "slug-de-loeuvre-parente"   # vide sur la fiche oeuvre et sur expression/ hors-œuvre
createur: "Nom du créateur"          # surtout renseigné sur la fiche oeuvre
statut_analyse: brouillon | en-cours | developpe
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
liens: []                            # internes au circuit
cles_doctrinales: []                 # sens unique vers doctrinal/, suggéré 🔍 par défaut
discernement: []                     # sens unique vers doctrinal/discernement/ (obligatoire si registre: expression et matière issue d'un discernement existant)
liens_label: []                      # sens unique optionnel vers label/direction-artistique/
liens_atelier: []                    # sens unique vers atelier/etudes-de-cas/ et atelier/rd/
---
```

- `type: oeuvre` = fiche-hub d'une œuvre (une par œuvre, porte `createur`) ; les
  autres types portent `oeuvre:` (slug de la fiche-hub).
- **`type: auteur`** — créateur réel, transverse à plusieurs œuvres ; vit en
  `hermeneutique/auteurs/`, porte `oeuvre: ""`, liste ses œuvres dans `liens:`.
  Emprunte la **forme d'archivage** de `doctrinal/autorites/` sans en partager la
  fonction : aucun statut d'autorité conféré ni supposé (Cmd 3).
- **`type: figure`** — remplace `personnage` ; couvre aussi les entités non
  personnelles fonctionnant comme telles. Substitution réversible (Art. 5 Sashimono).
- **`type: dispositif`** — lieu, vaisseau, appareil, système, interface ou
  institution de l'œuvre, tenu pour support opératoire de sa thèse.
- **Sagas** — un continuum de plusieurs opus reçoit **une seule fiche-hub**
  `type: oeuvre` ; le détachement d'un opus relève du Cmd 4, au cas par cas.
- **`liens_atelier`** — sens unique vers `atelier/etudes-de-cas/` et `atelier/rd/`
  seulement. L'inverse est interdit : aucune étude de cas ni fiche `rd/` ne pointe
  ici.
- **`registre`** distingue les deux régimes de production du circuit :
  - `analyse` — lecture d'une œuvre ou d'un de ses éléments ;
  - `expression` — formulation d'une idée propre à l'utilisateur, l'œuvre servant
    de langage et non d'objet. Ces fiches vont en `hermeneutique/expression/`
    quand elles ne relèvent d'aucune œuvre unique.
- **`discernement`** : toute fiche `registre: expression` dont la matière provient
  d'une expérience déjà versée au dépôt **doit** pointer vers la ou les fiches
  `doctrinal/discernement/` correspondantes (sens unique). La fiche du circuit
  **ne clôt jamais** un discernement et n'en modifie pas le statut : elle en
  développe une expression, sans effet doctrinal (Cmd 12, verdicts réservés).
- `statut_analyse` qualifie la **maturité du travail** — distinct du `status`
  doctrinal, qui juge une valeur de vérité traditionnelle (sans objet ici).
- `cles_doctrinales` : wikilinks vers `doctrinal/`, **sens unique**, **suggérés
  (🔍) par défaut**. Une clé ne devient « établie » qu'après une fiche
  `discernement/` tranchée par l'utilisateur (Cmd 3, Cmd 12).
- `liens_label` : sens unique optionnel vers `label/direction-artistique/`, quand
  une idée germée ici se concrétise en fiche label.
- `doctrinal/` → `hermeneutique/` : **jamais**. Aucune fiche doctrinale, y compris
  de discernement, ne pointe vers ce circuit.

## Portance et garde-fou (Cmd 3)

Tout joint de ce circuit est de portance ***zōsaku*** : il ne porte rien, et sa
dépose ne touche pas l'ossature. Le ***hozo*** y est **exclu en toute
circonstance** ; le *kumiko* exige une fiche `discernement` validante ; le
*kari-kumi* est l'état ordinaire. Toute `cle_doctrinale` invoquée est
**obligatoirement** accompagnée, dans le corps de la fiche, d'un bloc 🪵
**Restitution** complet — dont le champ « ce que le joint n'établit pas » est
**non facultatif** : une restitution sans limite déclarée est invalide et doit
être retirée au contrôle VIGILANCE. Confrontation Gizeh requise si la matière
touche au polaire, à l'axial, au septénaire ou au métrologique (voir CLAUDE.md
racine §VII, double contrôle systématique).

## Clause de plasticité (structurelle)

La souplesse de ce circuit tient à ce qu'une idée peut y exister et mûrir *sans
rien engager doctrinalement* — non à ce que les outils de discernement y soient
suspendus. Le domaine intermédiaire est par nature ambivalent : la grille des 11
marqueurs de contre-initiation reste disponible en référence, et tout passage où
une production (humaine ou IA) encouragerait l'abandon du discernement critique,
ou présenterait une expérience comme irréversible et soustraite à toute
vérification, doit être signalé avec la même fermeté qu'ailleurs (précédent :
`doctrinal/annales.md` [2026-06-20], signalement dissolution identitaire).
