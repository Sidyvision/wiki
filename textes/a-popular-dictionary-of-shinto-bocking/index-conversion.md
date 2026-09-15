---
title: "Index de conversion — A Popular Dictionary of Shinto (Brian Bocking)"
type: ressource
tags: [conversion, dictionnaire, shinto, bocking, japon]
created: 2026-09-10
sources:
  - "raw/A-Popular-Dictionary-of-Shinto - Brian Bocking.pdf"
---

# A Popular Dictionary of Shinto — Brian Bocking

Conversion PDF → Markdown de `raw/A-Popular-Dictionary-of-Shinto - Brian Bocking.pdf`
(220 pages, Curzon Press, éd. révisée 1997, Taylor & Francis e-Library 2005).

**Chaîne** : PDF chiffré (RC4) mais impression/copie autorisées — couche texte native
propre, pas de scan ni d'OCR. Extraction page par page via `pdftotext -layout`, marqueurs
`<!-- page N -->` conservés.

**Statut** : sortie brute de machine, non relue par un humain. Aucune correction
orthographique ni typographique appliquée.

**Piège relevé, à ne pas répéter** : les en-têtes courants (« A popular dictionary of
shinto N » sur les pages paires, « Introduction N » sur les pages impaires) sont un
**artefact d'imposition recto/verso constant sur tout l'ouvrage**, sans rapport avec le
contenu réel de la page — y compris en plein corps alphabétique (ex. page 20 porte
l'en-tête « Introduction 13 » alors qu'elle contient les entrées `Bosatsu`, `Bugaku`,
`Bukki`...). Le découpage par lettre ci-dessous a donc été fait sur la **vedette**
détectée par script (ligne centrée, courte, sans point final), jamais sur les en-têtes.

## Correction du 2026-09-15 — retrait des sauts de page U+000C

Les 23 fichiers de tranche portaient **220 sauts de page U+000C** (FORM FEED),
émis par `pdftotext` au passage de chaque page. Ils ont été retirés le
2026-09-15.

**Ce n'est pas une correction du texte**, que la règle d'immuabilité de `textes/`
interdirait. C'est le même motif que le retrait des contrôles bidirectionnels
dans la conversion de l'Ihyâ' arabe
(`textes/ghazali-ihya-ulum-al-din-arabe/index-conversion.md`, étape 3) : ces
marques n'appartiennent pas à l'ouvrage, elles sont émises par la couche
d'extraction pour piloter la mise en page. Ici le repère de page est déjà porté,
en clair et de façon lisible, par le marqueur `<!-- page N -->` qui suivait
immédiatement chacun des 220 sauts — l'invisible ne portait donc aucune
information que le texte ne porte pas déjà.

**Motif propre** : un U+000C invisible fausse les mesures sans s'annoncer. Le
comptage des chapitres de la traduction anglaise de l'Ihyâ' a donné **64 au lieu
de 41** pendant deux tours, parce que la classe `[[:space:]]` d'une ancre `grep`
absorbait ce caractère. Le fait est consigné en
`atelier/rd/incidents/2026-09-14_amortissement-constat-doctrinal-traduction-ihya.md`.

**Chaîne** : `atelier/rd/outillage/nettoyer-sauts-de-page-textes.py`
(déterministe, rapport seul par défaut, `--appliquer` requis pour écrire).

Le script ne touche qu'aux lignes dont le saut de page est **le seul contenu**,
et la ligne devient **vide, elle n'est pas supprimée** — retirer l'invisible ne
doit rien déplacer d'autre. Un saut accolé à du texte est laissé en place et
rapporté au verdict ; le garde-fou a été vu refuser sur un cas fabriqué. Relevé
sur ce corpus : **220 seuls sur leur ligne, 0 accolé**.

**Contrôle après coup**, ligne non vide à ligne non vide contre `git show HEAD` :
23 fichiers, **0 écart de contenu**, **0** saut de page résiduel.

Cette correction est appliquée sur le fondement de l'amendement de la règle
d'immuabilité de `textes/` rendu par Sidy le 2026-09-14 — un texte de `textes/`
est corrigible **lorsque c'est qualitativement justifié**. Voir
`meta/projet-unifie/propositions/proposition-textes-immuabilite-2026-09-15.md`.

## Fichiers

| Fichier | Section | Pages PDF |
|---|---|---|
| `00-front-matter.md` | Titre, copyright, sommaire, « How to use this dictionary », Introduction, suggestions de lecture, remerciements | 1-10 |
| `01-a.md` | A (+ fin des remerciements, signature datée) | 11-16 |
| `02-b.md` | B | 17-20 |
| `03-c.md` | C | 21-23 |
| `04-d.md` | D | 24-28 |
| `05-e.md` | E | 29-30 |
| `06-f.md` | F | 31-34 |
| `07-g.md` | G | 35-39 |
| `08-h.md` | H | 40-51 |
| `09-i.md` | I | 52-59 |
| `10-j.md` | J | 60-68 |
| `11-k.md` | K | 69-92 |
| `12-m.md` | M (aucune entrée L dans ce dictionnaire) | 93-103 |
| `13-n.md` | N | 104-107 |
| `14-o.md` | O (incl. Ō) | 108-113 |
| `15-r.md` | R (aucune entrée P ni Q) | 114-115 |
| `16-s.md` | S | 116-149 |
| `17-t.md` | T | 150-164 |
| `18-u.md` | U | 165-166 |
| `19-w.md` | W (aucune entrée V) | 167 |
| `20-y.md` | Y (aucune entrée X) | 168-175 |
| `21-z.md` | Z | 176 |
| `22-index.md` | Index thématique (13 sections : préfectures, artefacts, concepts, dates, festivals, nourriture, etc.) | 177-220 |

**Absence d'entrées L, P, Q, V, X** : constatée par le script de découpage (progression
alphabétique continue des vedettes, sans rupture), non une lacune de la conversion — le
romaji des termes shintō n'emploie quasiment jamais ces initiales.

Le PDF original reste la source de vérité : `raw/A-Popular-Dictionary-of-Shinto - Brian Bocking.pdf`.
Le dossier `textes/` est versionné ; `raw/` est hors git.
