---
title: "Index de conversion — The Arctic Home in the Vedas (Tilak, 1903)"
type: ressource
tags: [conversion, ocr, tilak, arctique, vedas, avesta]
created: 2026-09-02
sources:
  - "raw/9566.pdf"
---

# The Arctic Home in the Vedas — B. G. Tilak (1903)

Conversion PDF → Markdown du scan `raw/9566.pdf` (544 pages, édition anglaise
originale). C'est l'ouvrage dont le dépôt possède déjà le sommaire et l'index de
la traduction française (*Origine polaire de la tradition védique*, Arché, Milano,
1979) : `doctrinal/sources/transcription-index-tilak-origine-polaire.md` et
`atelier/rd/bibliotheque/sommaire-origine-polaire.md`. Le découpage ci-dessous a
été **contrôlé contre cette table des matières** : les 13 chapitres correspondent
un à un.

**Chaîne** : `pdftoppm -r 300 -gray` puis `tesseract 5 (eng, --psm 1)`, page par
page, puis découpage par chapitre (`/root/decouper_chapitres.py`).
Le PDF ne portait **aucune couche texte** (scan pur, producteur cairo) : tout le
texte vient de l'OCR.

**Statut** : sortie brute de machine, non relue par un humain. La qualité du scan
est inférieure à celle d'*Orion* ; les pages de sommaire (p.1-31) sont fortement
dégradées, le corps des chapitres est nettement plus propre. Coquilles attendues
sur les translittérations diacritées et les caractères devanāgarī. À traiter comme
aide au repérage, pas comme texte critique.

Chaque fichier conserve les marqueurs `<!-- page N -->` renvoyant à la page du PDF.

## Fichiers

| Fichier | Chapitre (anglais) | Titre français (éd. Arché) | Pages PDF |
|---|---|---|---|
| `arctic-00-front-matter.md` | Titre, préface, sommaire | — | 1-31 |
| `arctic-ch01-prehistoric-times.md` | I. Prehistoric Times | Les temps préhistoriques | 32-50 |
| `arctic-ch02-the-glacial-period.md` | II. The Glacial Period | La période glaciaire | 51-69 |
| `arctic-ch03-the-arctic-regions.md` | III. The Arctic Regions | Les régions arctiques | 70-91 |
| `arctic-ch04-the-night-of-the-gods.md` | IV. The Night of the Gods | La nuit des dieux | 92-110 |
| `arctic-ch05-the-vedic-dawns.md` | V. The Vedic Dawns | Les aubes védiques | 111-155 |
| `arctic-ch06-long-day-and-long-night.md` | VI. Long Day and Long Night | Le long jour et la longue nuit | 156-180 |
| `arctic-ch07-months-and-seasons.md` | VII. Months and Seasons | Mois et saisons | 181-220 |
| `arctic-ch08-the-cows-walk.md` | VIII. The Cows' Walk | La marche des vaches | 221-265 |
| `arctic-ch09-vedic-myths-the-captive-waters.md` | IX. Vedic Myths — The Captive Waters | Mythes védiques. Les eaux captives | 266-335 |
| `arctic-ch10-vedic-myths-the-matutinal-deities.md` | X. Vedic Myths — The Matutinal Deities | Mythes védiques. Les divinités matutines | 336-391 |
| `arctic-ch11-the-avestic-evidence.md` | XI. The Avestic Evidence | Références avestiques | 392-429 |
| `arctic-ch12-comparative-mythology.md` | XII. Comparative Mythology | Mythologie comparée | 430-452 |
| `arctic-ch13-bearing-on-primitive-aryan-culture.md` | XIII. The Bearing of our Results on the History of Primitive Aryan Culture and Religion | Portée de la théorie… | 453-505 |
| `arctic-99-general-index.md` | General Index + Index of Vedic and Avestic Passages | Index | 506-544 |

Le fichier monolithique complet reste disponible : `../9566.md`.

## Signalement

Le chapitre IX (« Les eaux captives », mythe Indra/Vṛtra) est signalé dans
`transcription-index-tilak-origine-polaire.md` comme le plus directement pertinent
pour le dépôt — il correspond ici à `arctic-ch09-vedic-myths-the-captive-waters.md`
(p. 266-335 du PDF, p. 197-244 de l'édition française).
