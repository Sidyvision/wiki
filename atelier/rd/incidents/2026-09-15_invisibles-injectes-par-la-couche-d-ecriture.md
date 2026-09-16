---
title: "Caractères invisibles injectés par la couche d'écriture d'un modèle (U+200B et voisins)"
type: outillage
statut_experience: reproduit
created: 2026-09-16
updated: 2026-09-16
status: resolu
severity: moyen
affected_systems: [wiki, outillage, hook-pre-commit]
---

# Caractères invisibles injectés par la couche d'écriture d'un modèle (U+200B et voisins)

## Résumé

**Date** : 2026-09-15
**Nature** : insertion de véritables caractères Unicode invisibles dans deux fichiers en
cours de rédaction, sans intention ni visibilité pour le rédacteur
**Étendue** : 2 fichiers, jamais commités — `atelier/rd/outillage/convertir-xiyouji-gutenberg.py`
puis `atelier/annales.md`
**Impact au dépôt** : **nul** — rien n'est entré. Le premier cas a été vu par contrôle manuel,
le second refusé par le hook pre-commit
**Statut** : résolu ; deux règles d'écriture en tirent la conséquence

## Ce qui s'est passé

Lors de la conversion du *Xī Yóu Jì* (voir `atelier/annales.md`, entrées du 2026-09-15), le
script `convertir-xiyouji-gutenberg.py` a été écrit avec une table des caractères à détecter,
rédigée sous la forme d'échappements — barre oblique inverse, `u`, puis le code du caractère.

**Ces échappements ont été décodés en caractères réels au moment de l'écriture du fichier.**
Le script destiné à refuser les invisibles en contenait donc six, en clair, dans sa propre
table de contrôle. Le fichier passait toutes ses épreuves : le garde-fou fonctionne sur le
texte converti, pas sur lui-même.

**La faute s'est reproduite dans la foulée** : l'entrée d'annales rédigée pour *décrire* cet
incident contenait à son tour un U+200B, par le même mécanisme, à l'endroit exact où elle
citait la séquence fautive.

## Comment chacun a été arrêté

| Cas | Fichier | Arrêté par | Message |
|---|---|---|---|
| 1 | `convertir-xiyouji-gutenberg.py` | contrôle manuel avant `git add` | relevé de 6 codes (U+200B, U+200C, U+200D, U+FEFF, U+200E, U+200F) |
| 2 | `atelier/annales.md` | **hook pre-commit** | `VIOLATION Cmd 15 — 1 occurrence : atelier/annales.md:42:91 — U+200B ZERO WIDTH SPACE` |

Le hook a bloqué le commit **et** le push, en nommant fichier, ligne, colonne et caractère,
et en prescrivant le nettoyage au `perl -CSD` — jamais au `sed` (incident du 2026-08-22).

## Ce que l'incident apprend

1. **Le garde-fou hérité a mordu pour de bon.** Le hook Cmd 15 était en place depuis le
   2026-08-22 mais n'avait jamais été vu refuser en conditions réelles. C'en est l'épreuve
   (CLAUDE.md racine §VII) : elle n'a pas eu à être fabriquée, elle s'est présentée.
2. **Un contrôle ne se contrôle pas lui-même.** Le script refuse les invisibles du texte
   qu'il convertit, et n'a aucune vue sur son propre corps. Seule une vérification extérieure
   — manuelle ici, le hook ensuite — pouvait l'attraper.
3. **Le vecteur n'est pas le collage ni le PDF**, contrairement aux incidents précédents
   (ZWJ du 2026-08-22, marques de direction de l'OCR des Futūḥāt du 2026-09-09) : c'est la
   **couche d'écriture elle-même**, qui interprète une notation d'échappement au lieu de la
   transcrire. Le risque porte donc sur tout fichier écrit par un modèle, y compris les
   fichiers d'outillage et les annales.

## Règles retenues

1. **Dans le code, un caractère invisible se construit, il ne s'écrit pas** :
   `tuple(chr(c) for c in (0x200B, ...))` et jamais la forme échappée en clair. Appliqué à
   `convertir-xiyouji-gutenberg.py`, avec un commentaire qui en donne le motif.
2. **En prose, un invisible se nomme par son code** — « U+200B » — et jamais par sa notation
   d'échappement, laquelle peut être décodée à l'écriture.
3. **Le hook reste la dernière porte, non la première.** Le contrôle manuel avant `git add`
   demeure dû sur tout fichier neuf écrit dans la session.

## Référence

- Incident fondateur : `atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`
- Correctif du hook : `atelier/rd/incidents/2026-08-22_post-scriptum-hook-corrige.md`
- Cas OCR : `atelier/rd/incidents/2026-09-09_marques-de-direction-ocr-futuhat.md`
- Commandement 15 : `CLAUDE.md` racine, §X
