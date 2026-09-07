---
title: "OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : plan"
type: outillage
chantier: OUT-08
tags: [atelier, rd, outillage, ocr, arabe, chantier, plan]
created: 2026-09-07
updated: 2026-09-07
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/out-08-ocr-arabe-futuhat/intent]]"
  - "[[atelier/rd/outillage/out-08-ocr-arabe-futuhat/spec]]"
  - "[[atelier/rd/outillage/spec-ocr-scan-vers-markdown]]"
---

# OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : plan

> **Statut** : `execute-partiellement` — les pistes A et B ont été menées le
> 2026-09-07 sous le verdict Cmd 13 de Sidy du même jour. L'étape 6 (conversion
> du tome) reste **non écrite** : elle attend le verdict du critère 1.

## Le fait qui a rouvert le chantier

`/usr/share/tesseract-ocr/5/tessdata/ara.traineddata` fait **1 432 056 octets et
date du 30 octobre 2019** : c'est la variante `tessdata_fast` livrée par Debian,
**la moins précise des trois**. Toute la qualification négative de `spec.md`
(DPI, `--psm`, `--oem`) avait été menée sur ce seul modèle, sans que sa nature
ait été relevée. Le remplacer n'est pas une installation de paquet : c'est un
fichier de données lu par un binaire déjà présent.

Second fait du même ordre : **Pillow 12.3.0 était déjà installé**. La spec
supposait que tout prétraitement d'image exigeait un paquet absent ; binarisation,
agrandissement et redressement s'écrivent avec Pillow seul, sans numpy.

Les deux pistes qui ont effectivement fait bouger la mesure ne coûtaient donc
**aucune installation**. Le verdict Cmd 13 a été demandé et obtenu, mais il n'a
pas encore été consommé.

## Ce qui a été fait

Bac à sable hors dépôt, `/root/out08/`. Les modèles téléchargés vivent dans
`/root/out08/tessdata/` et sont désignés par `--tessdata-dir` : `/usr/share/`
n'a pas été touché, il suffit d'effacer le dossier pour revenir à l'état initial
(Cmd 10).

**Pages d'épreuve fixées avant tout essai** — page 300 (échantillon commun de
`spec.md`) et page 600 (règle déterministe 300 + 300), pour qu'aucun résultat ne
puisse se lire comme une sélection après coup.

**Instrument de mesure** : `atelier/rd/outillage/mesurer-qualite-ocr-arabe.py`,
déterministe, bibliothèque standard seule, sans réseau ni LLM à l'exécution
(§VIII). Il rapporte six indices ; il ne conclut rien (Cmd 12). Son épreuve du
§VII vit dans `eprouver-mesure-ocr-arabe.py`.

## Résultats — I1, violation positionnelle, en %

| variante | page 300 | page 600 |
|---|---|---|
| **témoin** (modèle Debian, `--psm 1`) | 4,72 | 8,13 |
| seuil de passage (moitié du témoin) | ≤ 2,36 | ≤ 4,07 |
| Piste A — meilleur modèle seul (`tessdata` standard) | 2,38 | 5,20 |
| **Piste B — `x2 + Otsu`, `--psm 6`** | **1,56** ✅ | **2,97** ✅ |

**Piste A seule ne passe pas** : elle tient sur la page 300 et échoue sur la 600.
**Piste B passe sur les deux pages**, division par 3,0 et par 2,7.

Trois constats secondaires, tous mesurés :

- `tessdata_best` (12,6 Mo) est **moins bon** que `tessdata` standard (2,5 Mo)
  sur ce scan. Le modèle le plus lourd n'est pas le meilleur ici.
- Les modèles `script/Arabic` sont les pires **et** injectent 89 à 95 caractères
  invisibles interdits par le Cmd 15. Écartés à double titre.
- Le redressement ne sert à rien : l'angle détecté est `+0,00°` sur neuf essais
  sur dix. Le scan n'est pas de travers. Retiré de la chaîne retenue.
- 400 dpi reste négatif, **y compris recombiné au nouveau modèle** — la
  conclusion de `spec.md` sur ce point tient.

## Ce que ces chiffres ne disent pas

Ils ne disent pas que le texte est lisible. Ils classent des sorties pour
désigner celle qu'un humain lira. **La lecture de l'échantillon par la machine
qui a mené ces essais est que le texte reste corrompu** — mots soudés et lettres
fausses subsistent à l'œil, malgré la division par trois de l'indice. Ce constat
est porté ici parce qu'il tempère la mesure, non parce qu'il tranche : le
critère 1 de `spec.md` appartient à Sidy (Cmd 12).

## Ce qui reste à faire

1. **Verdict du critère 1** par Sidy, sur les extraits portés dans `spec.md`.
2. **Si le critère est jugé franchi** : écrire `ocr-futuhat-reprenable.sh`
   (état de reprise page par page, verrou atomique, suppression immédiate de
   l'image), puis convertir. `ocr-scan-vers-markdown.sh` n'est **pas** modifié :
   y ajouter un état changerait le comportement pour tous les autres corpus.
   Budget : ~10 s/page mesurées, soit ~2 h 10 pour le tome 1 et ~7 h 20 pour les
   2 630 pages des quatre tomes.
3. **Si le critère est jugé non franchi** : les pistes C (ImageMagick, seuillage
   adaptatif `-lat` sans équivalent Pillow) et D (numpy + OpenCV, Sauvola) sont
   couvertes par le verdict Cmd 13 et restent ouvertes. Kraken ne l'est pas — il
   tire PyTorch (> 2 Go) sur un disque à 90 %, et suppose un retour distinct.

## Hors périmètre

- **Aucun découpage en bābs** (§8 de `spec-ocr-scan-vers-markdown.md`). Un OCR
  meilleur ne rouvre pas cette question de lui-même : il y faudrait une mesure
  neuve **et** un verdict.
- **Aucun versement dans `textes/`** : DOC-07 n'est pas rouvert par ce chantier.
- **Aucune levée de `to-source`**, aucune fiche doctrinale : ce chantier ne fonde
  aucune citation (Cmd 5).
- **Aucune correction du fichier au sas** : une conversion se remplace, datée,
  elle ne se retouche pas.
