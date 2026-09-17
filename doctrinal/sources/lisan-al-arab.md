---
title: "Ibn Manẓūr — Lisān al-ʿArab (دار صادر, 3ᵉ éd. 1414 h., 15 vol.)"
type: source
status: traditionnel
tradition_cadre: "islam"
tags: [lexique-arabe, ibn-manzur, lisan-al-arab, dar-sadir, racines-arabes, edition-numerique, provenance]
created: 2026-09-17
updated: 2026-09-17
sources: ["to-source"]
sources_count: 1
cross_links: ["[[doctrinal/symboles/formule-al-waha-al-ajal-al-saa]]", "[[doctrinal/sources/gloton-approche-coran-grammaire-lexique]]"]
original: ["لسان العرب"]
---

# *Lisān al-ʿArab* — l'édition de référence du dépôt

> **Statut `traditionnel` : verdict de Sidy du 2026-09-17**, rendu sur question
> expresse. La machine ne l'a pas déduit du genre de l'ouvrage — le protocole
> doctrinal interdit de conclure un `status` et d'aligner une fiche sur ses
> voisines. Le matériau qui lui a été soumis : Ibn Manẓūr (m. 711 h.) compile le
> *Lisān* au VII<sup>e</sup>/XIII<sup>e</sup> siècle à partir de cinq lexiques
> antérieurs ; l'ouvrage est un dictionnaire de langue, antérieur de six siècles à
> la démarche académique moderne, et il est versé ici comme **instrument de
> langue**, non comme enseignement.

## Identification

- **Auteur** : <span data-nom="ibn-manzur" data-genre="autorite">Ibn Manẓūr</span>
  (محمد بن مكرم بن منظور الأفريقي المصري, m. 711 h. / 1311).
- **Titre** : *<span data-nom="lisan-al-arab" data-genre="ouvrage">Lisān al-ʿArab</span>* (لسان العرب).
- **Édition de référence du dépôt** : ط. **دار صادر** — بيروت، **الثالثة 1414 هـ**,
  **15 volumes**, حواشي **اليازجي** (gloses d'al-Yāzijī).
- **Arrangement** : par **dernière radicale**, puis première, puis seconde
  (arrangement d'al-Ṣiḥāḥ) — et non par première radicale. C'est ce qui rend la
  recherche d'une racine coûteuse à la main.

## Les deux témoins versés

Une même impression, tenue par deux témoins de nature différente. Le détail complet
— mesures, empreintes des 41 fichiers, réserves — vit dans `raw/lisan-al-arab/PROVENANCE.md`.

**Témoin A — texte né-numérique** (transcrivible, non vérifiable seul).
المكتبة الشاملة, `book_id` 1687, extrait du jeu de données
`MoMonir/shamela_books_text` (HuggingFace, apache-2.0). **8 116 pages** (une ligne =
une page imprimée), **25,0 M caractères**, notes de bas de page en champ séparé.

| Fichier | Octets | MD5 |
|---|---|---|
| `…_pages.tsv` | 47 449 819 | `7bcbd54e36310427521a6115e3640b22` |
| `…_texte.txt` | 47 554 743 | `d71d9b05ef09975ff09c73803765405a` |

**Témoin B — scan de la même impression** (vérifiable, non transcrivible).
`archive.org/details/1_20240125_20240125_0340`, 15 PDF, **8 197 pages**. Empreinte
du premier volume : `1…j01.pdf`, 26 875 825 octets, `12e318f27a29ea313d8160373004c6e4`.

**Pourquoi les deux ensemble.** Le texte seul ne se vérifie pas ; le scan seul ne se
transcrit pas — l'OCR arabe du dépôt n'est pas citable. Les deux réunis donnent un
texte transcrivible **et** vérifiable sur l'image de la page même.

## La vérification faite, et sa limite

Sur **cinq folios**, dans quatre volumes, le folio imprimé lu sur l'image de la page
PDF de même rang est **le même nombre** — décalage nul entre pagination PDF et
pagination imprimée :

| Volume | Page PDF | Folio imprimé lu |
|---|---|---|
| ج1 | 100 | ١٠٠ = 100 |
| ج3 | 500 | ٥٠٠ = 500 |
| ج8 | 200 | ٢٠٠ = 200 |
| ج11 | 400 | ٤٠٠ = 400 |
| ج15 | 382 | ٣٨٢ = 382 |

Et sur la page imprimée **382 du tome 15**, la colonne de droite de l'image et le
texte extrait se lisent **mot pour mot**, sous le titre courant **و ح ي**.

**La limite, et elle est portée au Sceau (`to-source`).** Cinq folios établissent la
**coïncidence des paginations** ; **les 8 116 pages ne sont pas attestées une par
une**. Une référence prise au témoin A et non revue sur le témoin B reste une
référence non vérifiée. C'est l'objet du marqueur unique porté par cette fiche : il
ne dit pas que la source manque, il dit **jusqu'où la vérification est allée**.

## Signalement — invisibles Unicode dans le témoin A

**1 520 occurrences de U+200C (ZWNJ)**, toutes dans le champ `texte`, aucune dans les
notes, toutes en tête de page — artefact de la source, que l'extraction n'a ni créé
ni retiré. Le texte est **fidèle** ; c'est précisément pourquoi les invisibles y
sont. Ils ne mordront qu'à la première conversion vers `textes/`, qui n'est pas
engagée. La voie de retrait proposée (script déterministe, retrait démontré non
substantiel, garde-fou vu refuser sur faute fabriquée) reste **non engagée** et
réservée au verdict.
