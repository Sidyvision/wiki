---
title: "Index de conversion — Orient et Occident (Guénon)"
type: ressource
tags: [conversion, coupure-web, guenon, orient-et-occident]
created: 2026-09-15
sources:
  - "raw/Orient et Occident/"
---

# Orient et Occident — René Guénon

Coupures web de l'ouvrage entier, prises sur l'**Index de l'œuvre de René Guénon**
(`https://www.index-rene-guenon.org`, sigle `OO`) avec l'extension Obsidian Web
Clipper, déposées dans `raw/Orient et Occident/` le 2026-09-13 et versées ici le
2026-09-15.

## Chaîne

1. **Capture** — Obsidian Web Clipper, une page par chapitre (`created: 2026-09-13`
   au cartouche de chaque coupure).
2. **Versement** — copie simple de `raw/` vers `textes/`, sans aucune modification du
   contenu. Les noms sont normalisés par la fonction `slug()` de
   `atelier/rd/outillage/migrer-textes-convertis.py` (minuscules ASCII, NFD → sans
   accents). Gardes G1 (donnée personnelle) et G2 (collision) rejouées sur le
   seul dossier : **0 refus, 0 collision**.
   - Le script n'a **pas** été lancé en mode `--migrer` global : il recopie les
     571 fichiers de `raw/`, et écraserait ce faisant les nettoyages consignés depuis
     le 2026-09-14 (règle d'immuabilité amendée, §II du protocole racine). Versement
     ciblé, sans écrasement (refus si la destination existe).
3. **Contrôle après coup** — `filecmp` octet par octet : **13 / 13 identiques** à leur
   source. Cmd 15 — **aucun caractère invisible** (zéro-largeur, contrôles
   bidirectionnels, BOM) dans les 13 fichiers.

Rien n'a été retiré ni corrigé : l'habillage du site (tableaux « Options
d'affichage », « Mises à jour récentes ») est conservé tel quel dans les coupures.

## Fichiers

| Fichier | `Chapitre=` | Contenu |
|---|---|---|
| `orient-et-occident-index-de-l-uvre-de-rene-guenon.md` | — | Avant-propos |
| `premiere-partie-illusions-occidentales-…` | 953 | Page de navigation seule |
| `orient-et-occident-index-de-l-uvre-de-rene-guenon-2.md` | 954 | I, ch. I — Civilisation et progrès |
| `la-superstition-de-la-science-…` | 955 | I, ch. II |
| `la-superstition-de-la-vie-…` | 956 | I, ch. III |
| `terreurs-chimeriques-et-dangers-reels-…` | 957 | I, ch. IV |
| `deuxieme-partie-possibilites-de-rapprochement-…` | 958 | Page de navigation seule |
| `orient-et-occident-index-de-l-uvre-de-rene-guenon-3.md` | 959 | II, ch. I — Tentatives infructueuses |
| `l-accord-sur-les-principes-…` | 960 | II, ch. II |
| `constitution-et-role-de-l-elite-…` | 961 | II, ch. III |
| `entente-et-non-fusion-…` | 962 | II, ch. IV |
| `orient-et-occident-index-de-l-uvre-de-rene-guenon-4.md` | 963 | Conclusion — **tronquée** |
| `orient-et-occident-index-de-l-uvre-de-rene-guenon-5.md` | 964 | Addendum — **vide** |

## Lacunes constatées

- **La conclusion s'interrompt au milieu de sa dernière phrase** : « … il y a des
  obligations qui sont » — puis la note 1. La fin manque à la capture, non au livre.
- **L'addendum (`Chapitre=964`) est vide** : la coupure ne porte que le titre et
  l'habillage du site, aucun texte.
- Correction possible : nouvelle capture de ces deux pages, versée **en
  remplacement datée** (règle d'immuabilité). Non faite ici.

## Laissé dans `raw/`, non versé

Treize fichiers `texte.txt`, `texte 2.txt` … `texte 13.txt` (32 octets chacun), qui
ne contiennent que la mention « Shared from Obsidian Web Clipper » — témoins du
partage, sans contenu.
