---
title: "Index de conversion — Ibn Seerin's Dictionary of Dreams (Al-Akili)"
type: ressource
tags: [conversion, ocr, dictionnaire-des-reves, ibn-sirin, reves, islam]
created: 2026-09-05
sources:
  - "raw/IbnSirin_dictionary_of_dreams.pdf"
---

# Ibn Seerin's Dictionary of Dreams — Muhammad M. Al-Akili

Conversion PDF → Markdown du scan `raw/IbnSirin_dictionary_of_dreams.pdf` (552 pages).

**Chaîne** : extraction de la couche texte du PDF (Adobe Acrobat 8 Paper Capture — OCR
anglais intégré), page par page via pymupdf, puis découpage par section.

**Statut** : sortie brute de machine, non relue par un humain. L'OCR du PDF est très
défectueux : les en-têtes de pages sont souvent mués en casseau de glyphes illisible
(`1N1'RUlJU(;1'1UN` pour INTRODUCTION), certaines lettres-clés (`Ifone`, `Ifthe`, `a/her`,
`o/one`) sont recollées, et les translittérations arabes sont approximatives. À traiter
comme une aide au repérage, jamais comme un texte critique — toute citation exige le
retour au scan.

Chaque fichier conserve les marqueurs `<!-- page N -->` renvoyant à la page du PDF.

## Fichiers

| Fichier | Section | Pages PDF |
|---|---|---|
| `00-front-matter.md` | Front matter: titre, préface, Ibn Seerin, forward, introduction, guide | 2-39 |
| `01-a.md` | A | 40-63 |
| `02-b.md` | B | 64-103 |
| `03-c.md` | C | 104-146 |
| `04-d.md` | D | 147-172 |
| `05-e.md` | E | 173-188 |
| `06-f.md` | F | 189-220 |
| `07-g.md` | G | 221-236 |
| `08-h.md` | H | 237-258 |
| `09-i.md` | I | 259-268 |
| `10-j.md` | J | 269-275 |
| `11-k.md` | K | 276-285 |
| `12-l.md` | L | 286-300 |
| `13-m.md` | M | 301-337 |
| `14-n.md` | N | 338-345 |
| `15-o.md` | O | 346-353 |
| `16-p.md` | P | 354-385 |
| `17-q.md` | Q | 386-388 |
| `18-r.md` | R | 389-407 |
| `19-s.md` | S | 408-464 |
| `20-t.md` | T | 465-492 |
| `21-u.md` | U | 493-496 |
| `22-v.md` | V | 497-503 |
| `23-w.md` | W | 504-522 |
| `24-y.md` | Y | 523-524 |
| `25-z.md` | Z | 525-526 |
| `26-blank.md` | Page blanche (séparateur) | 527-527 |
| `27-index.md` | Index of Entries (489-508) + General Index (509-511) | 528-550 |
| `28-bibliographie.md` | Bibliography (512) | 551-552 |

Le PDF original reste la source de vérité : `raw/IbnSirin_dictionary_of_dreams.pdf`.
Le dossier `textes/` est versionné ; `raw/` est hors git.