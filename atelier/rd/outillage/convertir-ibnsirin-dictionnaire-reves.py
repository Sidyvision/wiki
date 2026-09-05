#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convertir-ibnsirin-dictionnaire-reves.py — Conversion PDF → Markdown du
Dictionnaire des rêves d'Ibn Seerîn (Al-Akili).

Convertit le scan `raw/IbnSirin_dictionary_of_dreams.pdf` (552 pages) en
markdown découpé par section, vers `textes/ibn-sirin-dictionary-of-dreams/`.

Principe (même famille que migrer-textes-convertis.py, decouper-ouvrage-chapitres.py) :
DÉTERMINISTE, sans LLM. Il ne touche jamais à `raw/` (immuable, hors git) : il
lit la couche texte du PDF et écrit la conversion dans `textes/`. La coupe entre
le versé et l'inversé est inchangée : `raw/` reste la source de vérité, `textes/`
porte le texte converti versionné.

Chaîne : extraction de la couche texte du PDF (Adobe Acrobat 8 Paper Capture —
OCR anglais intégré), page par page via pymupdf, puis découpage par section
(front matter, lettres du dictionnaire A-Z avec pages).

Motif : conversion demandée par Sidy le 2026-09-05, versée au sas puis intégrée
côté Claude Code ; ce script est le reproductible conservé dans
atelier/rd/outillage/ (le binaire et la conversion restent gérés ailleurs).

Usage :
    # depuis la racine du dépôt (/root/wiki)
    source /root/.venv-pdf/bin/activate   # fournit pymupdf
    python3 atelier/rd/outillage/convertir-ibnsirin-dictionnaire-reves.py

Qualité OCR : médiocre (en-têtes mués en glyphes illisibles, ligatures
recollées `Ifone`/`Ifthe`, translittérations arabes approximatives). Sortie
brute de machine — aide au repérage, jamais texte critique ; toute citation
exige le retour au scan. Documenté dans textes/.../index-conversion.md.
"""
import os
import pymupdf

PDF = "raw/IbnSirin_dictionary_of_dreams.pdf"
OUT = "textes/ibn-sirin-dictionary-of-dreams"


def page_text(doc, i):
    """Texte de la page PDF i (0-indexé), nettoyé des octets nuls."""
    return doc[i].get_text().replace("\x00", "")


# Bornes (page PDF 1-indexée) : (début, fin, fichier, titre de section).
# Les bornes de lettres proviennent des pages-en-tête lettres réelles repérées
# page à page lors de la conversion (2026-09-05) — vérifiées continues.
SECTIONS = [
    (2, 39, "00-front-matter", "Front matter: titre, préface, Ibn Seerin, forward, introduction, guide"),
    (40, 63, "01-a", "A"),
    (64, 103, "02-b", "B"),
    (104, 146, "03-c", "C"),
    (147, 172, "04-d", "D"),
    (173, 188, "05-e", "E"),
    (189, 220, "06-f", "F"),
    (221, 236, "07-g", "G"),
    (237, 258, "08-h", "H"),
    (259, 268, "09-i", "I"),
    (269, 275, "10-j", "J"),
    (276, 285, "11-k", "K"),
    (286, 300, "12-l", "L"),
    (301, 337, "13-m", "M"),
    (338, 345, "14-n", "N"),
    (346, 353, "15-o", "O"),
    (354, 385, "16-p", "P"),
    (386, 388, "17-q", "Q"),
    (389, 407, "18-r", "R"),
    (408, 464, "19-s", "S"),
    (465, 492, "20-t", "T"),
    (493, 496, "21-u", "U"),
    (497, 503, "22-v", "V"),
    (504, 522, "23-w", "W"),
    # Pas de section X (l'ouvrage n'en a pas).
    (523, 524, "24-y", "Y"),
    (525, 526, "25-z", "Z"),
    (527, 527, "26-blank", "Page blanche (séparateur)"),
    (528, 550, "27-index", "Index of Entries (489-508) + General Index (509-511)"),
    (551, 552, "28-bibliographie", "Bibliography (512)"),
]

FRONT = [
    "---",
    'title: "Index de conversion — Ibn Seerin\'s Dictionary of Dreams (Al-Akili)"',
    "type: ressource",
    "tags: [conversion, ocr, dictionnaire-des-reves, ibn-sirin, reves, islam]",
    "created: 2026-09-05",
    "sources:",
    '  - "raw/IbnSirin_dictionary_of_dreams.pdf"',
    "---",
    "",
]

# Bloc d'entête index-conversion : écrit tel quel, wrappé, pour coller
# exactement à la version committée (bit-identique requis — le contenu
# pur comptant, le wrappage est celui de la conversion d'origine).
INDEX_HEADER = (
    "# Ibn Seerin's Dictionary of Dreams — Muhammad M. Al-Akili\n"
    "\n"
    "Conversion PDF → Markdown du scan `raw/IbnSirin_dictionary_of_dreams.pdf` (552 pages).\n"
    "\n"
    "**Chaîne** : extraction de la couche texte du PDF (Adobe Acrobat 8 Paper Capture — OCR\n"
    "anglais intégré), page par page via pymupdf, puis découpage par section.\n"
    "\n"
    "**Statut** : sortie brute de machine, non relue par un humain. L'OCR du PDF est très\n"
    "défectueux : les en-têtes de pages sont souvent mués en casseau de glyphes illisible\n"
    "(`1N1'RUlJU(;1'1UN` pour INTRODUCTION), certaines lettres-clés (`Ifone`, `Ifthe`, `a/her`,\n"
    "`o/one`) sont recollées, et les translittérations arabes sont approximatives. À traiter\n"
    "comme une aide au repérage, jamais comme un texte critique — toute citation exige le\n"
    "retour au scan.\n"
    "\n"
    "Chaque fichier conserve les marqueurs `<!-- page N -->` renvoyant à la page du PDF.\n"
    "\n"
    "## Fichiers\n"
    "\n"
    "| Fichier | Section | Pages PDF |\n"
    "|---|---|---|\n"
)


def render(title, start, end):
    """Rendu markdown d'une section, avec frontmatter et marqueurs <!-- page N -->."""
    doc = pymupdf.open(PDF)
    parts = [
        "---", f"source: {PDF}",
        f'section: "{title}"',
        f"pages_pdf: {start}-{end}",
        "---", "", f"# {title}", "",
    ]
    for p in range(start - 1, end):
        parts.append(f"<!-- page {p+1} -->")
        parts.append("")
        parts.append(page_text(doc, p).rstrip())
        parts.append("")
    doc.close()
    return "\n".join(parts)


def main():
    os.makedirs(OUT, exist_ok=True)
    files = []
    for start, end, fn, title in SECTIONS:
        with open(f"{OUT}/{fn}.md", "w", encoding="utf-8") as f:
            f.write(render(title, start, end))
        files.append((fn, title, start, end))

    # index-conversion.md : header wrappé bit-identique à HEAD + tableau
    lines = []
    lines += FRONT
    lines.append(INDEX_HEADER.rstrip())
    # pas de ligne vide entre le séparateur du tableau et les lignes de données
    for fn, title, start, end in files:
        lines.append(f"| `{fn}.md` | {title} | {start}-{end} |")
    lines.append("")
    lines.append(
        "Le PDF original reste la source de vérité : "
        "`raw/IbnSirin_dictionary_of_dreams.pdf`."
    )
    lines.append(
        "Le dossier `textes/` est versionné ; `raw/` est hors git."
    )
    with open(f"{OUT}/index-conversion.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Écrit {len(files)+1} fichiers dans {OUT}")
    for fn, title, start, end in files:
        print(
            f"  {fn}.md  pages {start}-{end}  "
            f"{os.path.getsize(f'{OUT}/{fn}.md')} octets"
        )


if __name__ == "__main__":
    main()
