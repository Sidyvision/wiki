#!/usr/bin/env python3
# =============================================================================
# convertir-jabre-munqidh.py — al-Munqidh min aḍ-ḍalāl, trad. Farid Jabre
# (UNESCO, Beyrouth, 1959) : partie FRANÇAISE du scan archive.org
# `raw/almunqidminadala00ghaz.pdf` (pp. 1-122) → `textes/`.
#
#   Verdict Sidy du 2026-09-15 : « go, scan de 1959, le français d'abord ».
#   La partie arabe (pp. 125-172) N'EST PAS traitée ici : sa couche texte est du
#   bruit (recodage LuraDocument), elle relèvera d'un OCR `ara` en seconde passe.
#
#   CE QU'IL FAIT : `pdftotext` (poppler) sur la couche texte native, page par
#   page, SANS AUCUNE correction — la sortie est reçue telle quelle (règle
#   d'immuabilité). Seuls ajouts : un cartouche par fichier et un marqueur
#   `<!-- page N -->` avant chaque page (convention des conversions Tilak).
#   Déterministe, sans LLM, sans réseau ; ne touche jamais à `raw/`.
#
#   GARDES, bloquantes :
#     - refus si une destination existe déjà (jamais d'écrasement) ;
#     - contrôle de complétude : la somme des pages écrites = les 122 pages
#       extraites, chaque page dans un seul fichier ;
#     - Cmd 15 : refus si un caractère invisible ou de contrôle est extrait.
#
#   Usage :
#     python3 atelier/rd/outillage/convertir-jabre-munqidh.py          # constate
#     python3 atelier/rd/outillage/convertir-jabre-munqidh.py --ecrire
# =============================================================================

import argparse
import re
import subprocess
import sys
from pathlib import Path

PDF = "raw/almunqidminadala00ghaz.pdf"
SORTIE = "textes/ghazali-munqidh-jabre-1959"
DERNIERE_PAGE_FR = 122

# (fichier, intitulé, première page, dernière page) — pages PDF, qui coïncident
# avec la pagination imprimée (« — 60 — » en p. 60).
SECTIONS = [
    ("munqidh-00-front-matter", "Pages de titre, Commission, table des matières", 1, 10),
    ("munqidh-01-introduction-jabre", "Introduction de Farid Jabre", 11, 52),
    ("munqidh-02-ouvrages-authentiques", "Les ouvrages de Ghazâlî dont l'authenticité ne fait pas de doute", 53, 54),
    ("munqidh-03-partie-1", "Première partie — Introduction et position du problème", 55, 62),
    ("munqidh-04-partie-2", "Deuxième partie — Les sophistes et le problème radical de la connaissance", 63, 66),
    ("munqidh-05-partie-3", "Troisième partie — Les catégories des chercheurs (scolastique, philosophie, ta'lîm, voie mystique)", 67, 102),
    ("munqidh-06-partie-4", "Quatrième partie — La réalité de la prophétie", 103, 107),
    ("munqidh-07-partie-5", "Cinquième partie — Raison de mon retour à l'enseignement", 108, 122),
]

INTERDITS = re.compile(r"[\u200b-\u200f\u202a-\u202e\u2060\ufeff­\x00-\x08\x0b\x0e-\x1f]")


def extraire(racine):
    out = subprocess.run(
        ["pdftotext", "-f", "1", "-l", str(DERNIERE_PAGE_FR), str(racine / PDF), "-"],
        capture_output=True, text=True, check=True).stdout
    pages = out.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    if len(pages) != DERNIERE_PAGE_FR:
        sys.exit(f"REFUS : {len(pages)} pages extraites, {DERNIERE_PAGE_FR} attendues")
    return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/root/wiki")
    ap.add_argument("--ecrire", action="store_true")
    a = ap.parse_args()
    racine = Path(a.repo).resolve()
    pages = extraire(racine)

    couvertes = [n for _, _, d, f in SECTIONS for n in range(d, f + 1)]
    if sorted(couvertes) != list(range(1, DERNIERE_PAGE_FR + 1)):
        sys.exit("REFUS : découpage incomplet ou chevauchant")
    sales = [i + 1 for i, p in enumerate(pages) if INTERDITS.search(p)]
    if sales:
        sys.exit(f"REFUS Cmd 15 : caractères invisibles/contrôle pages {sales}")

    sortie = racine / SORTIE
    for nom, titre, d, f in SECTIONS:
        cible = sortie / f"{nom}.md"
        if cible.exists():
            sys.exit(f"REFUS : {cible} existe déjà (jamais d'écrasement)")
        n = sum(len(pages[i - 1]) for i in range(d, f + 1))
        print(f"  {nom}.md  pp. {d}-{f}  {n} car.")
        if not a.ecrire:
            continue
        corps = [f'---\nsource: "{PDF}"\nsection: "{nom}"\npages_pdf: {d}-{f}\n---\n\n# {titre}\n']
        for i in range(d, f + 1):
            corps.append(f"\n<!-- page {i} -->\n\n{pages[i - 1].rstrip()}\n")
        sortie.mkdir(parents=True, exist_ok=True)
        cible.write_text("".join(corps), encoding="utf-8")
    total = sum(len(p) for p in pages)
    print(f"  total : {DERNIERE_PAGE_FR} pages, {total} caractères — contrôle de complétude ✓")
    print("  écrit." if a.ecrire else "  (constat seul — relancer avec --ecrire)")


if __name__ == "__main__":
    main()
