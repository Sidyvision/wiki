---
title: "Index de conversion — al-Munqidh min aḍ-ḍalāl, trad. Farid Jabre (1959)"
type: ressource
tags: [conversion, ghazali, munqidh, jabre, francais]
created: 2026-09-15
sources:
  - "raw/almunqidminadala00ghaz.pdf"
---

# al-Munqidh min aḍ-ḍalāl (Erreur et délivrance) — traduction de Farid Jabre

Al-Ghazâlî, *al-Munqidh min aḍ-ḍalāl*, traduction française avec introduction et
notes par **Farid Jabre**, Collection UNESCO d'œuvres représentatives, série arabe,
Commission internationale pour la traduction des chefs-d'œuvre, **Beyrouth, 1959**.
Scan de l'Internet Archive (`archive.org/details/almunqidminadala00ghaz`, 2015,
exemplaire de l'University of California, Los Angeles), 180 pages PDF.

**Verdict de Sidy du 2026-09-15** : « go, scan de 1959, le français d'abord ».

## Ce qui est versé, ce qui ne l'est pas

| Pages PDF | Contenu | État |
|---|---|---|
| 1–10 | Titres, Commission, table des matières | versé |
| 11–52 | Introduction de Jabre (époque, biographie, date et lieu, occasion et but, analyse, interprétation) | versé |
| 53–54 | Liste des ouvrages authentiques de Ghazâlî | versé |
| 55–122 | **Le traité**, en cinq parties | versé |
| 123–124 | Pages blanches | — |
| 125–172 | **Texte arabe original** | **non versé** — seconde passe |
| 173–181 | Table arabe, pages de garde | non versé |

La **couche texte arabe est inutilisable** : le recodage LuraDocument du scan a
rendu l'arabe en caractères latins sans signification (« jl 4«JcS î^i … »). Elle
relèvera d'un OCR `tesseract -l ara`, mesuré avec les outils du dépôt. **Attention
pour cette passe** : les pages arabes sont reliées à la manière arabe, leur
pagination imprimée décroît dans l'ordre du PDF (p. 126 → « 55 », p. 166 → « 15 ») :
l'ordre de lecture est l'inverse de l'ordre du fichier.

## Chaîne

Script déterministe : `atelier/rd/outillage/convertir-jabre-munqidh.py` (sans LLM,
sans réseau, ne touche jamais à `raw/`).

1. **`pdftotext`** (poppler) sur la **couche texte native** du PDF, pp. 1–122,
   découpée en pages sur les sauts de page.
2. **Aucune correction.** Seuls ajouts : un cartouche par fichier (`source`,
   `section`, `pages_pdf`), un titre, et un marqueur `<!-- page N -->` avant chaque
   page — convention des conversions Tilak.
3. **Gardes**, éprouvées le 2026-09-15 (§VII) :
   - refus d'écraser un fichier existant — **vu refuser** à la seconde exécution ;
   - complétude — les 122 pages dans exactement un fichier chacune, 208 979 caractères ;
   - Cmd 15 — refus de tout caractère invisible ou de contrôle ; **vu refuser** trois
     cas fabriqués (espace de largeur nulle, tiret virtuel, caractère de contrôle), et
     accepter un texte propre. Sur l'extraction réelle : **zéro**.

Commande exacte : `python3 atelier/rd/outillage/convertir-jabre-munqidh.py --ecrire`

## Pagination

La page PDF **coïncide avec la page imprimée** du livre (« — 60 — » en p. 60,
« — 122 — » en p. 122). Une seule anomalie : la p. 77 porte « — 11 — », **erreur de
lecture de l'OCR d'origine** pour 77, non un décalage.

## Qualité — ce qu'il faut savoir avant de citer

L'OCR d'origine (2015) est **lisible mais désordonné** :

- **Mise en page éclatée** : les lignes justifiées sont souvent coupées en
  fragments, et l'ordre des fragments est parfois brouillé, surtout dans les notes.
  Une citation doit être **recomposée à la lecture** et, en cas de doute, vérifiée
  sur le scan.
- **Notes de bas de page mêlées au corps** : l'appel « (1) » et le texte de la note
  se trouvent parfois au milieu d'une phrase du traité.
- **Coquilles d'OCR récurrentes**, conservées : « V » pour « l' » (« V Œuvre »),
  « renseignement » pour « l'enseignement », « F » pour « l' », « PÉlu » pour
  « l'Élu », « £indïq » / « ^indïq » pour *zindīq*, « taHïm » pour *ta'līm*.
- Translittérations diacritées approximatives (« Ghazàli », « Ghazâli »,
  « Ghazâlï »).

Règle d'immuabilité : on ne corrige pas en place. Une meilleure conversion (OCR
neuf du scan) remplacerait celle-ci, datée.

## Fichiers

| Fichier | Contenu | Pages |
|---|---|---|
| `munqidh-00-front-matter.md` | Titres, Commission, table | 1–10 |
| `munqidh-01-introduction-jabre.md` | Introduction du traducteur | 11–52 |
| `munqidh-02-ouvrages-authentiques.md` | Ouvrages dont l'authenticité ne fait pas de doute | 53–54 |
| `munqidh-03-partie-1.md` | I. Introduction et position du problème | 55–62 |
| `munqidh-04-partie-2.md` | II. Les sophistes et le problème radical de la connaissance | 63–66 |
| `munqidh-05-partie-3.md` | III. Les catégories des chercheurs — ch. I scolastique (*kalām*), ch. II « philosophie » (*falsafa*), ch. III *ta'līm*, ch. IV voie mystique | 67–102 |
| `munqidh-06-partie-4.md` | IV. La réalité de la prophétie | 103–107 |
| `munqidh-07-partie-5.md` | V. Raison de mon retour à l'enseignement | 108–122 |

## Autre édition présente dans `raw/`, écartée

`raw/La Délivrance de l'Erreur Al Ghazali.pdf` — la **même traduction de Jabre**,
réédition Hakîkat Kitâbevi, Istanbul, 2013 (66 pages, texte numérique propre).
Écartée sur verdict de Sidy : l'éditeur y a **inséré des formules de bénédiction**
dans les phrases de Jabre (sa propre notice le déclare), et elle ne porte ni
l'introduction ni les notes. Ces ajouts ne relèvent pas de la couche d'extraction et
ne pourraient donc pas être retirés (règle d'immuabilité, §II). Elle reste
utilisable comme **aide à la relecture** de l'OCR de 1959. Si elle devait être
versée, la garde G1 la refuserait — **faux positif** : l'adresse électronique et le
téléphone de l'éditeur figurent en page de garde.
