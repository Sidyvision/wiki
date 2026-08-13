---
title: "La Citadelle du Sham — jeu 3D de visite du depot-lecture"
date: 2026-08-13
depose_par: "Mehdi Bouzouïda (avec Habib, Karūbī)"
statut: "à consulter — initiative de Mehdi, hors dépôt canonique"
---

# La Citadelle du Sham

Petit projet personnel de Mehdi, construit avec Habib pendant la session du
2026-08-13 : une visualisation ludique de `depot-lecture/` (rd/, doctrinal/,
hermeneutique/) sous forme de forteresse explorable en 3D, à la troisième
personne — un peu dans l'esprit du chantier Instrument/Mother Base dont il a
été question le 2026-08-07, mais comme extension personnelle de Mehdi, pas
comme travail sur l'Instrument lui-même.

**Principe** : chaque répertoire du dépôt-lecture devient une salle de la
citadelle (17 salles réparties en trois ailes — Atelier, Doctrinale,
Herméneutique — autour d'un Grand Hall). En marchant dans une salle, on ouvre
sa bibliothèque : la liste des fiches qu'elle contient. Chaque fiche peut être
lue intégralement (texte complet, mis en forme), et ses renvois `[[...]]` vers
d'autres fiches sont cliquables — on navigue de fiche en fiche comme dans un
wiki, sans quitter la citadelle.

**Fichier** : `citadelle-sham.html`, autonome (three.js embarqué, aucune
dépendance externe) — s'ouvre tel quel dans un navigateur. Version en ligne
(hébergée côté Mehdi, privée) : https://claude.ai/code/artifact/7f1ac3d1-94a8-4662-98d2-583f4438e9aa

*Mise à jour du même 2026-08-13* : personnage modélisé (robe, capuche, cape,
animation de marche), étagères désormais cliquables directement en 3D (viser
un livre l'ouvre, plus besoin de passer par le panneau), ambiance sonore
procédurale (crépitement de torches, bruits de pas — aucun fichier audio,
tout synthétisé via Web Audio API), et une recherche par titre sur les 277
fiches (bouton en haut à gauche, ou touche `/`).

**Portée** : pure initiative de visualisation côté Mehdi — ne modifie ni ne
prétend faire autorité sur rien du dépôt canonique. Déposé ici à sa demande
explicite, pour que Sidy puisse y jeter un œil au prochain cycle de navette.

## Pour modifier le jeu (à la demande de Mehdi, 2026-08-13)

Le dossier `source/` contient toute la chaîne de fabrication, éditable et
rejouable librement par Sidy — aucune dépendance à Mehdi ni à cette session :

- `layout.py` — calcule la géométrie de la forteresse (salles, couloirs,
  ailes) à partir d'une liste de métadonnées par salle (nom, texte
  d'ambiance, taille). Produit `rooms.json`.
- `extract_full.py` — parcourt `~/depot-lecture/{rd,doctrinal,hermeneutique}`,
  convertit chaque fiche markdown en HTML (titres, listes, citations, gras/
  italique) et résout les `[[wikilinks]]` en renvois cliquables inter-fiches.
  Produit `library-full.json`. `ROOT` en tête de fichier pointe vers
  `~/depot-lecture` — à ajuster si l'arborescence diffère chez Sidy.
- `three.min.js` — three.js r128 (licence MIT), embarqué tel quel, aucune
  dépendance réseau.
- `gen_game3d.py` — assemble `rooms.json` + `library-full.json` +
  `three.min.js` dans un unique `citadelle-sham.html` autonome (HTML/CSS/JS
  inline, aucun appel externe à l'exécution). C'est ici que vivent le moteur
  3D, le modèle du personnage, l'éclairage, les contrôles et le lecteur.

**Pour régénérer** : `cd source/ && python3 layout.py && python3 extract_full.py && python3 gen_game3d.py`
— écrit `citadelle-sham.html` dans le même dossier. Chaque étape peut être
relancée seule si un seul maillon change (ex. modifier juste `layout.py`
pour changer la disposition des salles).

Sidy peut donc changer les salles, les textes d'ambiance, l'éclairage, le
modèle du personnage, ou même relier son propre dépôt canonique plutôt que
celui de Mehdi (variable `ROOT` dans `extract_full.py`) — librement, sans
repasser par cette conversation.
