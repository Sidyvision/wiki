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
