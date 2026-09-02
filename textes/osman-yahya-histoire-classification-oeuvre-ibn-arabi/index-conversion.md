---
title: "Conversion — Osman Yahia, Histoire et classification de l'œuvre d'Ibn 'Arabi"
type: conversion
tags: [conversion, ocr, bibliotheque, ibn-arabi, osman-yahia]
created: 2026-09-02
updated: 2026-09-02
sources:
  - "raw/Histoire et Classification de l’oeuvre d'Ibn Arabi-Osman Yahya.pdf"
links:
  - "[[atelier/rd/outillage/spec-ocr-scan-vers-markdown]]"
---

# Conversion — Osman Yahia, *Histoire et classification de l'œuvre d'Ibn 'Arabi*

> **Sortie de machine, non relue.** Texte de repérage, jamais texte critique
> (spec §1). La lecture du texte primaire reste humaine. En attente de verdict
> au sas `_inbox/`.

## Source

| | |
|---|---|
| Fichier | `raw/Histoire et Classification de l’oeuvre d'Ibn Arabi-Osman Yahya.pdf` |
| Pages PDF | 696 |
| Édition | Institut français de Damas (page de titre, p. 1 du scan) |
| Nature | Scan avec couche texte Acrobat ClearScan **écartée** (voir ci-dessous) |

## Chaîne appliquée

```
bash atelier/rd/outillage/ocr-scan-vers-markdown.sh \
     "raw/Histoire et Classification de l’oeuvre d'Ibn Arabi-Osman Yahya.pdf" \
     _inbox/osman-yahya-histoire-classification-oeuvre-ibn-arabi.md \
     "Osman Yahia — Histoire et classification de l'œuvre d'Ibn 'Arabi" fra

python3 atelier/rd/outillage/decouper-ouvrage-chapitres.py \
     _inbox/osman-yahya-histoire-classification-oeuvre-ibn-arabi.md \
     _inbox/conversions/chapitres-osman-yahya osman-yahya 30 --langue=fr
```

Durée OCR : 29 min (24 pages/minute, `-l fra`).

## Pourquoi la couche texte existante a été écartée

Le PDF portait un OCR Acrobat ClearScan. Comparaison `pdftotext` contre
`tesseract` sur la p. 50 (spec §6, épreuve obligatoire avant choix) :

| | ClearScan | tesseract `-l fra` |
|---|---|---|
| nombres | `1 89`, `1 9 1`, `1 06`, `2 1 8` | `189`, `191`, `106`, `218` |
| mots | `lffJiza`, `1nanquant`, `d on1aine`, `cour.s` | `Iǧāza`, `manquant`, `domaine`, `cours` |

Rédhibitoire : ce volume **est** un répertoire de numéros d'ouvrages ; des
nombres brisés le rendent inexploitable. Second essai, `-l fra+ara` : l'ajout
de l'arabe dégrade les italiques latines (`Fihris` → `17/715`) sans rendre
l'arabe pour autant. Retenu : **`-l fra` seul**.

`markitdown` (Microsoft) a été éprouvé le même jour sur ce fichier : il lit la
couche ClearScan — donc reproduit ses défauts — et invente en outre de faux
tableaux Markdown à partir des colonnes de chiffres du répertoire. Écarté ici.

## Découpage — 18 sections

| Fichier | Section | Pages PDF |
|---|---|---|
| `00-front-matter` | liminaire | 1-29 |
| `01-partie-premiere` | I<sup>re</sup> partie (sources) | 30-31 |
| `02-chapitre-01` | Les sources directes | 32-51 |
| `03-chapitre-02` | Les sources indirectes | 52-67 |
| `04-chapitre-03` | Résultats acquis | 68-87 |
| `05-chapitre-04` | Classification des ouvrages | 88-107 |
| `06-chapitre-05` | Documentation sur Ibn 'Arabi | 108-131 |
| `07-partie-deuxieme` | II<sup>e</sup> partie (les œuvres) | 132-133 |
| `08-repertoire` | **Répertoire général** | 134-527 |
| `09-addenda` | Addenda A/B/C/D | 528-539 |
| `10-partie-troisieme` | III<sup>e</sup> partie (tables) | 540-551 |
| `11-table-ouvrages` | Table des ouvrages du R.G. | 552-595 |
| `12-table-correspondances` | Table des correspondances | 596-627 |
| `13-table-noms-propres` | Table des noms propres | 628-671 |
| `14-table-noms-ouvrages` | Table des noms d'ouvrages | 672-681 |
| `15-table-manuscrits` | Table des manuscrits par bibliothèque | 682-693 |
| `16-table-ouvrages-imprimes` | Tables ouvrages imprimés/commentés/traduits | 694-695 |
| `17-index` | fin | 696 |

## Contrôles passés

**1. Intégrité (mécanique, bloquant).** 696 pages réparties / 696 lues,
aucune manquante, aucune dupliquée, code de sortie 0. Re-vérifié après copie
au sas.

**2. Contrôle externe — pagination imprimée (spec §5).** Le numéro de page
imprimé dans le titre courant a été confronté au numéro de page PDF sur tout
le volume : **576 pages sur 594 vérifient `imprimé = pdf + 5`**, décalage
rigoureusement constant. Les 18 exceptions sont des coquilles d'OCR sur le
numéro lui-même (`18]` pour 181, `299` pour 229), non des ruptures de
pagination. Le plan général du volume (p. 2-4) confirme indépendamment
l'ordre et la nature des sections.

**3. Pages sans texte.** 11 pages (5, 29, 31, 67, 87, 107, 131, 133, 541,
669, 695), toutes vérifiées à la source par analyse des pixels : 5 blanches
nettes, 6 ne portant que du bruit de scan (~0,05 % de pixels sombres), dont
rien n'émerge même en `--psm 3` et `--psm 11`. Aucune perte.

## Limites connues de cette sortie

- Les passages en **graphie arabe sont illisibles** (choix `-l fra` assumé).
- Les **translittérations diacritées sont approximatives** : `Iǧāza` est rendu
  tantôt `l'Igaza`, tantôt `l'ISaza`, `Muṣannafāt` → `Musannafat`. Ne jamais
  citer une translittération d'après cette sortie sans retour au scan.
- Aucune extraction d'images ni de tableaux.
- Le **Répertoire général** (394 pages) reste d'un seul tenant : il est
  organisé par numéros d'ouvrage (1 à 851), non par chapitres. Un découpage
  par tranches de numéros serait possible s'il devenait utile.
