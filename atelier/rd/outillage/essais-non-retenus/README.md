---
title: "Essais non retenus — détection des bâbs des Futūḥāt"
type: outillage
tags: [rd, outillage, ocr, arabe, ibn-arabi, essai-non-retenu]
created: 2026-09-02
updated: 2026-09-02
sources:
  - "raw/Al Futuhat Al Makkiyya - maymaniya_p1.pdf"
links:
  - "[[atelier/rd/outillage/spec-ocr-scan-vers-markdown]]"
---

# Essais non retenus — découpage des *Futūḥāt* par bâb

> **Ces deux scripts ne sont pas en service.** Ils sont conservés parce qu'ils
> documentent un **refus motivé** (spec §8) et parce qu'ils resserviraient si
> un scan de meilleure qualité, ou un index arabe indépendant, devenait
> disponible. Ne pas les brancher sur la chaîne de production en l'état.

## Ce qu'ils font

- `ordinaux-arabes.py` — lit un ordinal arabe écrit en toutes lettres
  (« الثامن والعشرون » = 28), avec tolérance aux graphies fautives de l'OCR.
  Deux entrées : `parse_ordinal()` (lecture stricte) et `candidates()` (toutes
  les lectures plausibles, pour laisser une contrainte externe trancher).
- `apparier-suite-croissante.py` — apparie une liste de jeux de candidats à
  une suite strictement croissante de rangs, par programmation dynamique.

## Pourquoi ils n'ont pas suffi

Mesuré le 2026-09-02 sur les 779 pages du tome 1 :

| | index (p. 27-46) | corps (p. 47-779) |
|---|---|---|
| lignes candidates | 403 | 131 |
| rangs appariés | 253 | ~50 |
| fautes constatées | — | bâbs 75 et 81 sur la même page 617 |

Les en-têtes du corps sont calligraphiés et ornementés ; l'OCR les rend en
bouillie. Le détecteur confond en outre les mentions au fil du texte
(« dans ce bâb ») avec de vrais en-têtes.

## Quatre leçons transposables

1. **Ne pas normaliser, énumérer.** Le kāf de l'OCR vaut tantôt ṯāʾ
   (`الثالك` = الثالث), tantôt lām (`الاوك` = الاول). Une substitution simple ne
   peut pas rendre les deux ; il faut énumérer les lectures — exactement la
   leçon de la table `AMBIG` pour les chiffres romains.
2. **N'élargir que sur ce que l'OCR a détruit, jamais sur ce qu'il a lu.**
   Premier essai : en supposant toute dizaine et toute centaine possiblement
   perdues, chaque ligne devenait compatible avec presque tout rang et la
   contrainte de séquence dérivait (le bâb 1 s'accrochait au onzième).
3. **L'appariement glouton est faux ici.** « الثامن والعشرون » donne `{18, 28}` :
   le glouton prend toujours 18. Seul un appariement global sur toute la suite
   choisit juste.
4. **Back-pointers vers une table mutable = chaîne corrompue.** La
   reconstruction réutilisait une même ligne pour deux rangs (bâbs 5 et 15
   pointant la même ligne). Chaîner des nœuds immuables.

## Ce qu'il faudrait pour reprendre

- Un scan de meilleure définition sur les pages d'en-tête, **ou**
- une table des bâbs saisie indépendamment (le juge externe qu'exige le §5),
  contre laquelle apparier au lieu de deviner.
