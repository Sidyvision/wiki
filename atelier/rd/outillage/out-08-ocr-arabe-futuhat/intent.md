---
title: "OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : intention"
type: outillage
chantier: OUT-08
tags: [atelier, rd, outillage, ocr, arabe, chantier, intent]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
  - "[[atelier/rd/outillage/ocr-scan-vers-markdown]]"
  - "[[atelier/rd/outillage/out-08-ocr-arabe-futuhat/spec]]"
---

# OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : intention

## Le besoin

`_inbox/al-futuhat-al-makkiyya-maymaniya-p1.md` — conversion de
`raw/Al Futuhat Al Makkiyya - maymaniya_p1.pdf` (779 p., édition Maymaniyya, tome 1)
par la chaîne actuelle du dépôt (`pdftoppm 300dpi` + `tesseract 5 -l ara`) — donne un
texte **structurellement corrompu** : lettres recomposées au hasard, ordre parfois
inversé, mots agglutinés sans espace. Constat posé dans le plan
`_inbox/MASTER-UPDATE.md` (DOC-07 §2) sur un échantillon à la ligne 5000 ; aucune
citation n'en est possible en l'état (Cmd 5), et c'est le seul texte arabe non
vocalisé du corpus akbarien touché par ce défaut à cette échelle — les corpus latins
(Guénon, Tilak) souffrent de coquilles ponctuelles relisibles caractère par
caractère, pas d'une corruption structurelle.

Ce chantier existe pour **qualifier** ce qui pourrait réduire cette corruption, avant
tout nouvel essai de conversion complète sur les 779 pages.

## Qui le porte

Sidy, verdict rendu à DOC-07 (« (c) nouvel essai d'OCR d'abord », 2026-09-02) — la
machine ne tranche pas la fiabilité d'une source de premier rang (Cmd 12).
Bénéficiaire : tout futur ingest citant la Futūḥāt en édition Maymaniyya t. 1.

## Hors périmètre

- **Les tomes 2 à 4 de la Maymaniyya.** N'ont jamais été déposés au sas ; hors sujet
  tant que le tome 1 lui-même n'est pas résolu.
- **Toute traduction ou paraphrase.** Le dépôt cite déjà la Futūḥāt via des
  traductions publiées vérifiées (Penot) ; ce chantier porte sur le **texte arabe**
  lui-même, aucun substitut.
- **La correction manuelle du texte déjà produit.** Contraire à la règle
  d'immuabilité de `textes/` (une conversion ne se corrige pas, elle se remplace,
  `textes/LISEZ-MOI.md`) — et de toute façon rien n'est encore versé à `textes/`
  pour ce tome.
- **L'installation d'outillage lourd sans verdict.** Une première scrutation
  (§Ce qui reste ouvert) montre que les pistes sérieuses (moteur alternatif,
  prétraitement d'image) demandent des paquets absents du serveur — décision
  d'installation renvoyée à Sidy (Cmd 13), pas prise ici.

## Contraintes doctrinales

- **Cmd 5** (aucune affirmation sans source) : tant que le texte n'est pas fiable, il
  reste hors citation — ce chantier ne produit aucune fiche doctrinale, seulement un
  jugement de qualité technique.
- **Cmd 12** (*upakarana*) : la fiabilité suffisante d'un texte de premier rang pour
  fonder une citation est un verdict de Sidy, jamais de la machine — ce chantier
  prépare des données comparatives, il ne conclut pas « ceci est désormais citable ».
- **Cmd 13** (porte humaine) : toute dépense (API OCR tierce, GPU loué) ou toute
  installation de paquet système est un point de retour nommé, pas une initiative
  autonome.
- **`textes/`, règle d'immuabilité** : si une conversion meilleure aboutit, elle
  **remplace** l'actuelle (datée, signalée), elle ne l'édite pas en place.

## Le signe de réussite

Un `spec.md` qui compare au moins deux pistes concrètes sur un échantillon commun
(la même page test, ou un petit lot de pages), avec un verdict lisible par Sidy :
« telle piste réduit la corruption de X à Y, coût/paquet requis Z » — même si la
conclusion est « aucune piste disponible ne suffit, le tome reste hors dépôt ».

## Ce qui reste ouvert

- **Premier relevé fait dans ce chantier** (bac à sable `/tmp`, hors dépôt, non
  committé) : sur la page 300 (échantillon arbitraire), faire varier le DPI
  (300 → 400) et le mode de segmentation Tesseract (`--psm` 3 défaut, 4, 6) **ne
  change rien à la nature de la corruption** — les mots restent recomposés au
  hasard dans les quatre sorties. Le réglage de paramètres seul ne suffit donc
  probablement pas ; direction à documenter dans `spec.md`.
- **Outillage absent du serveur**, à vérifier avant toute piste : pas
  d'ImageMagick/`convert`, pas d'OpenCV (`cv2`), pas d'`ocrmypdf`, pas de moteur OCR
  alternatif (Kraken, moteur cloud). Toute piste de prétraitement d'image
  (binarisation, redressement, contraste) ou de changement de moteur suppose une
  installation — verdict Sidy avant tout `pip install`/`apt install` (Cmd 13).
  Le PDF a été produit par Adobe Acrobat 6.0 en 2008 (`pdfinfo`) : nature du scan
  source (niveaux de gris, contraste d'origine) non encore examinée.
  Piste ni essayée ni écartée : un moteur cloud (Google Vision, Azure) donnerait
  probablement un résultat net meilleur sur de l'arabe classique non vocalisé, mais
  suppose un compte/crédit tiers — dépense et souveraineté externalisée à trancher
  par Sidy avant tout essai (Cmd 13, finalité de souveraineté du pôle `rd/`).
  Piste `--oem 1` (LSTM seul) contre le défaut : **testée, sans objet** —
  `ara.traineddata` ne porte pas les composants du moteur legacy, le défaut retombe
  déjà sur LSTM seul faute d'alternative installée (détail : `spec.md`).
- **Amplitude du défaut sur l'ensemble du tome.** Le relevé de DOC-07 portait sur un
  seul échantillon (ligne 5000) et celui-ci sur une seule page (300) — rien ne dit
  encore si la corruption est uniforme sur les 779 pages ou si certaines zones (texte
  imprimé net vs. manuscrit/marge) sont mieux traitées. À couvrir dans `spec.md`.
