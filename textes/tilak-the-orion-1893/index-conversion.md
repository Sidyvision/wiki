---
title: "Index de conversion — The Orion (Tilak, 1893)"
type: ressource
tags: [conversion, ocr, tilak, orion, vedas]
created: 2026-09-02
sources:
  - "raw/orionortheantiqu021979mbp.pdf"
---

# The Orion, or Researches into the Antiquity of the Vedas — B. G. Tilak (1893)

Conversion PDF → Markdown du scan `raw/orionortheantiqu021979mbp.pdf` (237 pages).

**Chaîne** : `pdftoppm -r 300 -gray` puis `tesseract 5 (eng, --psm 1)`, page par page,
puis découpage par chapitre (`/root/decouper_chapitres.py`).
La couche texte OCR d'origine du PDF (LuraDocument, 2006) était très dégradée ;
elle a été **écartée** au profit d'un OCR neuf, nettement plus fidèle.

**Statut** : sortie brute de machine, non relue par un humain. Coquilles OCR
attendues sur les translittérations sanskrites diacritées (Prajāpati, Kṛttikā…)
et sur les caractères devanāgarī, non reconnus. À traiter comme aide au repérage,
pas comme texte critique.

Chaque fichier conserve les marqueurs `<!-- page N -->` renvoyant à la page du PDF.

## Fichiers

| Fichier | Section | Pages PDF |
|---|---|---|
| `orion-00-front-matter.md` | Page de titre, imprimeur | 1-4 |
| `orion-01-preface.md` | Preface | 5-9 |
| `orion-02-sommaire.md` | Contents | 10 |
| `orion-ch01-introduction.md` | I. Introduction | 11-19 |
| `orion-ch02-sacrifice-alias-the-year.md` | II. Sacrifice alias the Year | 20-39 |
| `orion-ch03-the-krittikas.md` | III. The Krittikas | 40-68 |
| `orion-ch04-agrahayana.md` | IV. Agrahāyana | 69-103 |
| `orion-ch05-the-antelopes-head.md` | V. The Antelope's Head | 104-136 |
| `orion-ch06-orion-and-his-belt.md` | VI. Orion and his Belt | 137-164 |
| `orion-ch07-ribhus-and-vrishakapi.md` | VII. Ribhus and Vrishākapi | 165-205 |
| `orion-ch08-conclusion.md` | VIII. Conclusion + Appendix | 206-237 |

Le fichier monolithique complet reste disponible : `../orion-tilak-1893.md`.

## Rattachement

*The Orion* (1893) est l'ouvrage dont *The Arctic Home in the Vedas* (1903) est la
suite déclarée — voir `doctrinal/sources/transcription-index-tilak-origine-polaire.md`
et `atelier/rd/bibliotheque/sommaire-origine-polaire.md`.
