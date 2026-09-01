---
title: "INS-13 — bandeau zodiacal : spécification"
type: projet
chantier: INS-13
tags: [atelier, rd, instrument, chantier, spec, zodiaque]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/instrument/spec-anneau-zodiacal]]"
  - "[[atelier/rd/instrument/ins-13-bandeau-zodiacal/intent]]"
---

# INS-13 — spécification

> **La spécification de fond n'est pas ici.** Elle vit dans
> [[atelier/rd/instrument/spec-anneau-zodiacal]] (créée le 2026-07-26, révisée le
> 2026-08-25) : fondement de données, géométrie, règle des manifestes. Cette fiche
> **l'adopte par pointeur** comme jambe `spec` du triptyque — elle n'est ni renommée,
> ni déplacée, ni recopiée (Cmd 10, réversibilité ; le registre pointe, il n'absorbe
> pas). Ce qui suit ne fait qu'ajouter ce que le gabarit demande et que la fiche
> d'origine, antérieure à la convention, ne porte pas : les critères d'acceptation
> vérifiables et les cas limites.

## Critères d'acceptation

1. Aucune chaîne de caractère zodiacale (nom de signe, nom de *manzil*, borne de
   degré) n'apparaît dans le code de rendu : `grep` sur les douze noms de signes dans
   `src/` ne renvoie rien.
2. Le bandeau se peuple exclusivement depuis `wiki-manifest.json`.
3. Les 28 *manāzil* sont présents et dans l'ordre ; aucune position vide, aucun
   doublon.
4. Renommer un *manzil* dans `instrument-donnees.yaml`, régénérer, recharger : le
   nouveau libellé s'affiche **sans aucune modification du code de rendu**. C'est le
   critère central — il prouve la chaîne, pas seulement le dessin.
5. La correspondance degré ↔ arc s'affiche comme **établie** (elle l'est : *Futūḥāt*
   ch. 198), sans marqueur 🔍.
6. Aucun ancrage nouveau n'apparaît dans le manifeste avant/après : le décompte
   d'ancrages reste à 23.

## Cas limites

- **Champ `to-source`** (colonne *faṣṣ*, INS-12) : la cellule reste vide ou marquée,
  jamais comblée par déduction du rendu (Cmd 5).
- **Degrés 1 à 10**, sans portion zodiacale : le bandeau ne commence pas à 1 et ne
  fabrique pas de correspondance pour les combler.
- **Manifeste plus ancien que le schéma attendu** : le rendu se dégrade proprement —
  bandeau absent, pas de bandeau faux.

## Ce qui reste `to-source`

Les trois marqueurs de la colonne *faṣṣ* — chantier INS-12, non bloquant ici.
