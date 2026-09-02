---
title: "textes/ — le cabinet de lecture du dépôt"
type: infrastructure
chantier: PRO-08
tags: [textes, sources, conversions, obsidian, infrastructure]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/infrastructure/pro-08-textes-convertis-versionnes/intent]]"
---

# `textes/` — le cabinet de lecture du dépôt

> **Ce que ce dossier est.** La **source primaire convertie**, telle qu'elle a
> été reçue, mise à portée du poste CONSULTATION. Ouvert le 2026-09-02 sur
> verdict de Sidy (chantier PRO-08) : « `textes/` validé, dédoublonne avant
> migration, et amende le §II ».
>
> **Ce qu'il n'est PAS — et le point est aussi important que le premier.**
> `textes/` **n'est pas un sixième circuit**. Il ne porte aucun Sceau, n'entre
> dans aucun régime de liens (§VI), et **n'est la cible d'aucun wikilink**. Le
> graphe l'ignore, et le vérificateur d'invariants l'exempte du contrôle B0 par
> une ligne nommée dans `PREFIXES_SANS_FM`.

## Pourquoi il existe

Ces textes vivaient sous `raw/`, que le `.gitignore` exclut. Ils ne se
synchronisaient donc **jamais** vers Obsidian : Sidy ne pouvait les lire que
depuis le terminal, c'est-à-dire au poste où il ne travaille pas — alors même
que des dizaines de fiches doctrinales les citent en source.

Les deux motifs de l'exclusion ont été **mesurés** avant d'être écartés : 14 Mo
de Markdown contre 2,6 Go pour `raw/` entier (le volume est fait des binaires),
et **zéro** donnée personnelle sur les 708 fichiers examinés. Le motif de
confidentialité, lui, **tient pleinement pour les binaires** — factures
nominatives, exports — qui restent hors git. C'est tout l'objet de la coupe.

## La règle d'immuabilité

**Un texte de `textes/` ne se corrige pas.** Il est reçu, non édité. Une
conversion meilleure le **remplace**, datée et signalée ; une coquille d'OCR
n'est pas corrigée en place, sans quoi le dossier cesserait d'être une source
pour devenir une interprétation.

Ce qui se dit d'un texte se dit **ailleurs** : dans une fiche `doctrinal/source`,
qui porte le Sceau et le statut.

## Provenance

Copiés depuis `raw/` par `atelier/rd/outillage/migrer-textes-convertis.py`, qui
**copie et ne déplace jamais** (Cmd 10) : les originaux demeurent.

- **708** fichiers examinés · **560** migrés
- **147 doublons** écartés — dédoublonnage sur verdict de Sidy. Entre deux copies
  identiques au bit près, on conserve celle qui n'est **pas** sous `Downloads/`,
  ce dossier étant un dépôt de téléchargement et non un corpus rangé. Il
  redoublait intégralement *Symboles de la Science sacrée* (91) et *Études sur
  l'Hindouisme* (39).
- **1 fichier hors corpus** signalé et non migré (`Build Your Own Perplexity with
  Exa.md` — article technique).
- **0 refus** pour donnée personnelle.

## Noms

Minuscules ASCII, sans accents, tirets (§III du protocole racine). Ce n'est pas
une coquetterie : les dossiers de `raw/` portent leurs noms en Unicode
**décomposé** (NFD), là où un chemin tapé à la main l'est en composé (NFC). Un
accès littéral y échoue sur « No such file or directory » **sans rien dire de
plus** — le piège a été rencontré deux fois le 2026-09-02. La normalisation le
supprime à la racine.

## Ce que contient le dossier

| corpus | fichiers |
|---|---|
| `apercu-sur-l-initiation/` | 50 |
| `apercus-sur-l-esoterisme-islamique-et-le-taoisme/` | 14 |
| `autorite-spirituelle-et-pouvoir-temporel/` | 9 |
| `autres-ressources/` | 4 |
| `divers/` | 21 |
| `etudes-sur-l-hindouisme/` | 39 |
| `formes-traditionnelles-et-cycles-cosmiques-rene-guenon/` | 32 |
| `initiation-et-realisation-spirituel/` | 34 |
| `introduction-generale-a-l-etude-des-doctrines-hindoues-rene-guenon/` | 1 |
| `l-esoterisme-de-dante-rene-guenon-ed-gallimard-1957/` | 9 |
| `l-homme-et-son-devenir-selon-le-vedanta-rene-guenon/` | 27 |
| `la-crise-du-monde-moderne/` | 9 |
| `la-grande-triade/` | 27 |
| `la-lumiere-daryush-shayegan/` | 1 |
| `le-regne-de-la-quantite/` | 42 |
| `le-roi-du-monde/` | 12 |
| `le-symbolisme-de-la-croix/` | 31 |
| `le-theosophisme-histoire-d-une-pseudo-religion/` | 67 |
| `les-disciplines-spirituelles-daryush-shayegan/` | 1 |
| `les-etats-multiples-de-l-etre/` | 19 |
| `les-principes-du-calcul-infinitesimal/` | 26 |
| `les-quatre-mondes-daryush-shayegan/` | 1 |
| `symboles-de-la-science-sacree-rene-guenon/` | 84 |

## Second versement du 2026-09-02 — les deux Tilak

Les conversions de *The Arctic Home in the Vedas* (1903) et *The Orion* (1893),
arrivées au sas `_inbox/` le matin même, ont été versées ici **le jour où
`textes/` a été validé**. Elles ne venaient donc pas de `raw/` mais du sas, et
c'est le premier cas d'usage du régime nouveau : **une conversion n'a plus à
transiter par un dossier masqué**.

- `tilak-the-arctic-home-in-the-vedas-1903/` — 16 fichiers (13 chapitres, front
  matter, index général, index de conversion)
- `tilak-the-orion-1893/` — 12 fichiers (8 chapitres, préface, sommaire, front
  matter, index de conversion)

**Non migrés, et pour la même règle que le dédoublonnage** : les deux fichiers
monolithiques (`9566.md`, `orion-tilak-1893.md`) qui portent le texte entier d'un
seul tenant. Ils redoublent intégralement les chapitres.

⚠️ **Qualité d'OCR médiocre et inégale** sur ces deux corpus — « CHAPTER ITIL »
pour III, « AGRAHAY ANA » pour *Agrahāyaṇa*, « Big-Veda » pour *Ṛg-Veda*, passages
en devanāgarī translittéré illisibles. La règle d'immuabilité s'applique : **on ne
corrige pas**, on remplace par une conversion meilleure, datée. Ce qui est établi
sur ces textes l'est dans les fiches `doctrinal/sources/`, qui portent le statut.

## Ce qui reste ouvert

Le **régime des futurs** textes convertis — passent-ils encore par `raw/`, ou
directement du sas vers `textes/` ? Question posée à Sidy, **non tranchée** :
c'est elle qui décidera si le problème peut se reformer.
