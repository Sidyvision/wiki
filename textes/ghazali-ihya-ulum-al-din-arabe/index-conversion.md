---
title: "Ihyâ' 'ulûm al-dîn — texte arabe intégral (conversion)"
type: ressource
tags: [ghazali, ihya, arabe, conversion, soufisme]
created: 2026-09-14
sources:
  - raw/9472.pdf
---

# Ihyâ' 'ulûm al-dîn — إحياء علوم الدين — texte arabe intégral

Conversion du texte arabe complet de l'`Ihyâ' 'ulûm al-dîn` d'Abû Hâmid
al-Ghazâlî, d'après `raw/9472.pdf` (3384 pages PDF, producteur calibre 3.40.1,
couche texte native — non océrisé).

## Chaîne

Script reproductible : `atelier/rd/outillage/convertir-ghazali-ihya.py`
(déterministe, sans LLM, sans réseau ; ne touche jamais à `raw/`).

1. **`pdftotext`** (poppler) — et non pymupdf, contrairement aux trois
   conversions antérieures du dépôt. Motif mesuré : sur ce PDF, pymupdf
   restitue les mots de chaque ligne **en ordre inverse**. Relevé page 30 —
   pymupdf rend « ... المهلكات ربع في ذكرناه ما وأكثر » (phrase à l'envers)
   là où pdftotext rend « وأكثر ما ذكرناه في ربع المهلكات ... » (ordre
   logique). Les conversions antérieures portaient sur des PDF latins, où le
   défaut ne se manifeste pas. Pour tout PDF arabe natif, `pdftotext` fait foi.
2. **Normalisation NFKC** — le PDF stocke l'arabe en formes de présentation
   (U+FB50–FDFF, U+FE70–FEFF), non en arabe standard (U+0600–06FF) : 254
   formes de présentation contre 70 caractères standard sur la page 30. Sans
   NFKC aucune recherche n'aboutit : « ربع » ne s'apparie pas à sa forme de
   présentation.
3. **Retrait des contrôles bidirectionnels** (LRE, RLE, PDF, LRM, RLM, LRO,
   RLO, isolats) — 1562 occurrences pour 55 000 caractères en extraction
   brute. Ce n'est pas une correction du texte, que la règle d'immuabilité
   interdirait : ces marques n'appartiennent pas à l'œuvre, elles sont
   injectées par la couche de rendu pour piloter l'affichage bidirectionnel,
   au même titre que les formes de présentation. Le Cmd 15 en interdit
   l'introduction dans le dépôt.

4. **Unification du yâ'** (U+06CC vers U+064A) — voir *Statut* ci-dessous.
   Appliquée sur verdict de Sidy du 2026-09-14 ; ce n'est pas un défaut de
   l'étape par défaut du script, qui ne l'applique que sur demande explicite.

Commande exacte de cette conversion, pour reproduction :

    python3 atelier/rd/outillage/convertir-ghazali-ihya.py --unifier-ya

Contrôle après chaîne, sur 5 605 597 caractères : **0** contrôle bidi
résiduel, **0** invisible interdit par le Cmd 15, **0** forme de présentation
résiduelle, **0** yâ' U+06CC résiduel.

## Découpage — par juz', imposé par la mesure

Le découpage par kitâb (les quarante livres) a été sondé sur l'intégralité du
texte normalisé, puis **écarté** : les têtes de kitâb ne se distinguent pas des
citations en cours de texte. Sur 31 lignes commençant par « كتاب », des titres
(« كتاب أسرار الزكاة ») voisinent avec des citations (« كتاب الحج وبيت المقدس
أيضا له فضل كبير خرج ابن عمر من »). Aucun motif déterministe ne les sépare.

Les ancres de pagination du tirage, elles, sont **complètes et monotones** :
1706 ancres relevées pour 1709 pages imprimées, les trois absentes étant la
page 1 de chacun des juz' 2, 3 et 4.

| Juz' | Pages imprimées | Fichiers |
|---|---|---|
| 1 | 361 | 8 |
| 2 | 387 | 8 |
| 3 | 414 | 9 |
| 4 | 547 | 11 |
| **Total** | **1709** | **36** |

Le texte est donc découpé par juz', puis par tranches de 50 pages imprimées.
Le rapport est d'environ deux pages PDF pour une page imprimée.

**Ce découpage est celui du tirage arabe, non la structure doctrinale** en
quatre rub' (`'ibâdât`, `'âdât`, `muhlikât`, `munjiyât`) et quarante kitâb.
Cette structure ne se documente pas ici : elle relève d'une fiche portant le
Sceau, en circuit `doctrinal/`.

## Repères de page

Chaque page PDF est précédée d'un commentaire portant les trois repères :

    <!-- pdf 30 | juz 1 | صفحة 15 -->

Le repère `juz`/`صفحة` permet la citation par volume et page du **tirage**,
et non par page PDF — seule forme de renvoi stable.

## Statut

Texte **born-digital**, non océrisé : la qualité de caractère est celle de la
composition d'origine, sans les défauts propres à l'OCR. Deux points relevés
à l'extraction — le premier subsiste, le second est tranché :

- **Ligatures lâm-alif suivies de tanwîn** disjointes par `pdftotext`
  (`اشتغالاً` rendu `اشتغا ً`), environ 185 occurrences pour 300 pages. C'est
  le prix de `pdftotext` ; il a été retenu contre l'inversion des mots par
  pymupdf, incomparablement plus grave.
- **Yâ' persan U+06CC** — **unifié vers U+064A. Verdict de Sidy, 2026-09-14.**
  Constat à l'appui : le codepoint était entièrement prédit par la position
  dans le mot — initiale U+06CC=5312 / U+064A=0 ; médiane U+06CC=18332 /
  U+064A=214 ; finale U+06CC=81 / U+064A=7788. Aucune graphie arabe ne
  distingue le yâ' selon sa position : il s'agissait d'une correspondance de
  police, de la même classe que les formes de présentation. L'unification
  n'ajoute ni ne retranche rien au texte : 201 930 + 67 068 = 268 998
  occurrences, longueur totale inchangée à 5 605 597 caractères.
  Effet mesuré sur l'appariement — `ينبغي` passe de 0 à 804 occurrences, et
  `إحياء علوم الدين`, le titre même de l'ouvrage, de 0 à 24 : avant
  unification il ne s'appariait dans aucune des deux graphies, parce qu'il
  mêlait les deux au sein d'un même mot. Le texte est désormais appariable
  avec tout autre texte arabe du dépôt.
  Résiduel après unification : **0** occurrence de U+06CC.

Ce texte est le **texte de référence** du chantier Ghazâlî, et il l'est seul.
La traduction anglaise de Fazl-ul-Karim déposée en `raw/` n'a pas été
convertie : sa conversion a été écartée par verdict de Sidy le 2026-09-14, au
motif que la démarche dont elle procède en rend l'usage à peu près stérile.
Le motif est consigné en circuit `doctrinal/`, non ici — cette page ne porte
pas le Sceau et ne qualifie rien.

## Fichiers

| Fichier | Juz' | Pages imprimées |
|---|---|---|
| `juz-1-pages-001-050.md` | 1 | 1–50 |
| `juz-1-pages-051-100.md` | 1 | 51–100 |
| `juz-1-pages-101-150.md` | 1 | 101–150 |
| `juz-1-pages-151-200.md` | 1 | 151–200 |
| `juz-1-pages-201-250.md` | 1 | 201–250 |
| `juz-1-pages-251-300.md` | 1 | 251–300 |
| `juz-1-pages-301-350.md` | 1 | 301–350 |
| `juz-1-pages-351-361.md` | 1 | 351–361 |
| `juz-2-pages-001-050.md` | 2 | 1–50 |
| `juz-2-pages-051-100.md` | 2 | 51–100 |
| `juz-2-pages-101-150.md` | 2 | 101–150 |
| `juz-2-pages-151-200.md` | 2 | 151–200 |
| `juz-2-pages-201-250.md` | 2 | 201–250 |
| `juz-2-pages-251-300.md` | 2 | 251–300 |
| `juz-2-pages-301-350.md` | 2 | 301–350 |
| `juz-2-pages-351-387.md` | 2 | 351–387 |
| `juz-3-pages-001-050.md` | 3 | 1–50 |
| `juz-3-pages-051-100.md` | 3 | 51–100 |
| `juz-3-pages-101-150.md` | 3 | 101–150 |
| `juz-3-pages-151-200.md` | 3 | 151–200 |
| `juz-3-pages-201-250.md` | 3 | 201–250 |
| `juz-3-pages-251-300.md` | 3 | 251–300 |
| `juz-3-pages-301-350.md` | 3 | 301–350 |
| `juz-3-pages-351-400.md` | 3 | 351–400 |
| `juz-3-pages-401-414.md` | 3 | 401–414 |
| `juz-4-pages-001-050.md` | 4 | 1–50 |
| `juz-4-pages-051-100.md` | 4 | 51–100 |
| `juz-4-pages-101-150.md` | 4 | 101–150 |
| `juz-4-pages-151-200.md` | 4 | 151–200 |
| `juz-4-pages-201-250.md` | 4 | 201–250 |
| `juz-4-pages-251-300.md` | 4 | 251–300 |
| `juz-4-pages-301-350.md` | 4 | 301–350 |
| `juz-4-pages-351-400.md` | 4 | 351–400 |
| `juz-4-pages-401-450.md` | 4 | 401–450 |
| `juz-4-pages-451-500.md` | 4 | 451–500 |
| `juz-4-pages-501-547.md` | 4 | 501–547 |

Le PDF de `raw/` demeure la source de vérité : cette conversion est une sortie
de machine, et toute citation critique exige le retour au fichier d'origine.
