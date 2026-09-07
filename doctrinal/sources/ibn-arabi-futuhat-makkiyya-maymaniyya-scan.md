---
title: "Al-Futūḥāt al-Makkiyya — édition Maymaniyya, les quatre volumes (scan)"
type: source
status: traditionnel
tradition_cadre: "islam"
tags: [ibn-arabi, futuhat, maymaniyya, arabe, scan, corpus]
created: 2026-09-07
updated: 2026-09-07
sources:
  - "raw/Al Futuhat Al Makkiyya - maymaniya_p1.pdf"
  - "raw/maymaniya_p2.pdf"
  - "raw/maymaniya_p3.pdf"
  - "raw/maymaniya_p4.pdf"
sources_count: 4
cross_links: ["[[doctrinal/autorites/ibn-arabi]]", "[[doctrinal/sources/osman-yahia-histoire-classification-1964]]"]
---

# Al-Futūḥāt al-Makkiyya — édition Maymaniyya, les quatre volumes (scan)

> **Cette fiche décrit le scan, non son texte.** Elle recense la source physique
> telle qu'elle est au dépôt : quatre volumes, leur pagination, leurs bornes. Elle
> **ne verse aucun texte** et **ne fonde aucune citation** : l'OCR disponible est
> jugé structurellement corrompu, et rien ici n'autorise à citer la *Futūḥāt* sur
> sa foi (Cmd 5). Ce qu'elle établit, elle l'établit par `pdfinfo` et par la
> lecture des pages de charnière.

## Identification

*Al-Futūḥāt al-Makkiyya* de Muḥyī al-Dīn Ibn ʿArabī, dans l'édition du Caire dite
**Maymaniyya** (al-Maṭbaʿa al-Maymaniyya), lithographie ancienne en quatre volumes.
C'est l'édition de référence classique, celle dont la pagination est citée par la
littérature akbarienne avant l'édition critique d'Osman Yahia.

## État du corpus au dépôt

Les quatre volumes sont présents et **intègres**. Contrôle : la taille sur disque
égale exactement la longueur totale déclarée par l'en-tête de linéarisation de
chaque PDF, et `pdfinfo` ne lève aucune erreur de syntaxe.

| volume | fichier | octets | pages scannées |
|---|---|---|---|
| I | `raw/Al Futuhat Al Makkiyya - maymaniya_p1.pdf` | 69 671 947 | 779 |
| II | `raw/maymaniya_p2.pdf` | 64 737 591 | 704 |
| III | `raw/maymaniya_p3.pdf` | 52 852 379 | 575 |
| IV | `raw/maymaniya_p4.pdf` | 49 773 548 | 572 |
| | **total** | | **2 630** |

Commande : `pdfinfo <chemin> | grep Pages` sur les quatre chemins ci-dessus.

Ce sont des **pages scannées**, non la pagination imprimée. La distinction n'est
pas théorique : pour le **volume I**, l'écart est mesuré à **16 pages** — la page
PDF 300 porte le folio ٢٨٤ (284), la page PDF 700 porte le folio ٦٨٤ (684). Donc
**folio = page PDF − 16** pour le corps de ce volume ; les pages liminaires ne
suivent pas cette numérotation, et l'écart des volumes II à IV n'a pas été mesuré.

> **Conséquence pratique, apprise à ses dépens.** Toute page citée doit dire
> **laquelle** des deux numérotations elle emploie. Le 2026-09-07, une comparaison
> d'échantillons OCR a été présentée sous l'intitulé « page 300 » — entendu comme
> page PDF par la machine, comme folio par le lecteur : **rien ne se recoupait**, et
> le désaccord venait de l'étiquette, non du texte. Écrire « page PDF n » ou
> « folio n », jamais « page n ».

Les noms de fichiers sont hétérogènes — le premier porte un intitulé long, les
trois autres un nom court. `raw/` étant immuable, ils sont cités tels quels et
n'ont pas été renommés.

> **Épisode du dépôt, 2026-09-07.** Les volumes II à IV ont d'abord été déposés
> **tronqués** : 3,4 Mo reçus contre 64,7 Mo déclarés pour le volume II, soit
> environ 5 %. Les trois PDF étaient illisibles (`Invalid XRef entry`,
> `Top-level pages object is wrong type`). Redéposés le même jour, ils sont
> intègres. Consigné parce qu'un fichier tronqué de cette façon **s'ouvre sans
> erreur visible dans certains lecteurs** : c'est l'écart entre la taille sur
> disque et le champ `/L` qui le révèle, pas l'apparence du fichier.

## Bornes des bābs par volume — avec leur degré d'attestation

L'édition porte **deux systèmes de numérotation** qu'il ne faut pas confondre : les
**bābs** (chapitres, 560 dans l'œuvre) et les ***juzʾ*** de la division de l'auteur.
Le colophon du volume I les mentionne tous deux dans la même phrase, et précise
« على حسب تجزئة المؤلف » — *selon la division de l'auteur*. **Les numéros de *juzʾ*
ne correspondent pas aux quatre volumes physiques** : le volume I s'achève sur le
*juzʾ* 74 et le volume II s'ouvre sur le *juzʾ* 75.

| charnière | borne | attestation |
|---|---|---|
| I → II | le volume II s'ouvre sur le **bāb 73** | **établie** — colophon du volume I, p. 779 : « ثم المجلد الاول من الفتوحات المكية ويتلوه المجلد الثاني أوله الباب الثالث والسبعون » |
| II → III | le volume III s'ouvre sur le **bāb 301** | **provisoire, source unique** — fihrist du volume III, p. 2, dont la première entrée est le bāb 301. Aucun colophon correspondant n'a été trouvé en fin de volume II (ses dernières pages, 700 à 704, sont des pages d'index) |
| III → IV | le volume IV s'ouvre sur le **bāb 401** | **établie** — colophon du volume III, p. 575 : « ويتلوه المجلد الرابع أوله الباب الحادي وأربعمائة » |
| fin du IV | dernier bāb du volume IV | **non établie** — non relevée sur le scan |

D'où, sous ces réserves : volume I = bābs **1 à 72** (établi) ; volume II = **73 à
300** (fin provisoire) ; volume III = **301 à 400** (début provisoire) ; volume IV =
à partir de **401** (fin non établie).

**L'épreuve posée n'a pas entièrement réussi, et c'est dit plutôt que masqué.** La
règle fixée avant lecture était que les quatre clôtures et les quatre ouvertures
s'accordent deux à deux. Trois lectures manquent : les pages de titre des volumes II
et IV n'ont rendu aucun texte, et le colophon du volume II n'a pas été localisé. Deux
charnières sur trois reposent donc sur un énoncé explicite, la troisième sur une
seule lecture. Les bornes marquées *provisoires* demandent une confirmation à l'œil
sur le scan avant d'être citées.

## Ce que cette fiche ne fait pas

- **Elle ne verse aucun texte.** Aucun contenu de la *Futūḥāt* n'entre dans le dépôt
  par elle. La conversion OCR du volume I existe, hors intégration, et son texte est
  jugé corrompu : il ne fonde aucune citation.
- **Elle ne découpe rien.** Le repérage des 560 bābs dans le corps du texte a été
  tenté puis refusé au dépôt, sur mesures : le taux d'erreur produisait de *fausses*
  références. Les bornes ci-dessus sont d'une autre nature — ce sont quelques
  énoncés explicites lus en clair, non un appariement statistique.
- **Elle ne lève aucun `to-source`.** Disposer du scan n'est pas avoir vérifié une
  citation : la vérification reste humaine, sur le texte primaire.

## Pertinence pour le dépôt

Plusieurs fiches doctrinales citent la *Futūḥāt* par des traductions partielles
(Penot, Gloton, Valsan). Le corpus arabe complet permet désormais, à terme, de
remonter au texte de l'édition de référence — mais seulement par lecture humaine du
scan, page par page, tant qu'aucune conversion fiable n'existe. C'est en cela qu'il
change quelque chose : il rend la vérification *possible*, il ne la fait pas.
