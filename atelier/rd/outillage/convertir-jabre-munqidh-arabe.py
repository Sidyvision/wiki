#!/usr/bin/env python3
# =============================================================================
# convertir-jabre-munqidh-arabe.py — al-Munqidh min aḍ-ḍalāl, TEXTE ARABE de
# l'édition Jabre (UNESCO, Beyrouth, 1959), pp. PDF 125-175 du scan
# `raw/almunqidminadala00ghaz.pdf` → `textes/ghazali-munqidh-jabre-1959/`.
#
#   Verdict Sidy du 2026-09-15 : « go, lance la passe arabe du Munqidh ».
#   Seconde passe de convertir-jabre-munqidh.py (partie française).
#
#   POURQUOI UN OCR NEUF. La couche texte arabe du scan est du bruit (recodage
#   LuraDocument : l'arabe y est rendu en caractères latins). Essai du
#   2026-09-15 sur les pp. 126 et 150 : `tesseract -l ara`, 300 dpi, --psm 6 →
#   I1 = 0,00 et 0,34 % (mesurer-qualite-ocr-arabe.py), phrases lisibles.
#   Le prétraitement x2 + Otsu retenu pour les Futûḥât (OUT-08) n'est pas
#   nécessaire ici : l'impression de Beyrouth est nette.
#
#   ORDRE DE LECTURE. Le texte arabe est relié à l'arabe : dans le PDF, sa
#   pagination imprimée DÉCROÎT (p. PDF 126 → « 55 », 166 → « 15 »). Relation
#   constatée : page imprimée = 181 − page PDF. Le fichier produit suit l'ORDRE
#   DE LECTURE (page PDF décroissante) et chaque page porte les deux numéros.
#
#   SEUL RETRAIT : les invisibles du Cmd 15 (U+200B-U+200F, U+202A-U+202E,
#   U+2066-U+2069, U+FEFF) injectés par le moteur de rendu bidirectionnel de
#   Tesseract — couche d'extraction, non œuvre (règle d'immuabilité amendée le
#   2026-09-14, §II). Leur nombre est compté page par page et rapporté ; rien
#   d'autre n'est touché.
#
#   GARDES, bloquantes : pas d'écrasement ; langue `ara` installée ; zéro
#   invisible résiduel ; chaque page du périmètre traitée une fois.
#
#   Usage :
#     python3 atelier/rd/outillage/convertir-jabre-munqidh-arabe.py --cache DIR          # OCR + constat
#     python3 atelier/rd/outillage/convertir-jabre-munqidh-arabe.py --cache DIR --ecrire
#   Le cache garde les sorties OCR brutes : une seconde exécution ne refait pas l'OCR.
# =============================================================================

import argparse
import re
import subprocess
import sys
from pathlib import Path

PDF = "raw/almunqidminadala00ghaz.pdf"
SORTIE = "textes/ghazali-munqidh-jabre-1959/munqidh-08-texte-arabe.md"
PREMIERE, DERNIERE = 125, 175          # périmètre PDF (arabe + table arabe)
DECALAGE = 181                          # page imprimée = DECALAGE − page PDF
INVISIBLES = re.compile(r"[\u200b-\u200f\u202a-\u202e\u2066-\u2069\ufeff]")


def ocr(racine, page, cache):
    brut = cache / f"p{page:03d}.txt"
    if brut.exists():
        return brut.read_text(encoding="utf-8")
    base = cache / f"img{page:03d}"
    subprocess.run(["pdftoppm", "-r", "300", "-gray", "-f", str(page), "-l", str(page),
                    str(racine / PDF), str(base)], check=True)
    img = next(cache.glob(f"img{page:03d}-*.pgm"))
    subprocess.run(["tesseract", str(img), str(cache / f"p{page:03d}"), "-l", "ara",
                    "--psm", "6"], check=True, capture_output=True)
    img.unlink()
    return brut.read_text(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/root/wiki")
    ap.add_argument("--cache", required=True, help="dossier des sorties OCR brutes (hors dépôt)")
    ap.add_argument("--ecrire", action="store_true")
    a = ap.parse_args()
    racine = Path(a.repo).resolve()
    cache = Path(a.cache); cache.mkdir(parents=True, exist_ok=True)
    cible = racine / SORTIE
    if cible.exists():
        sys.exit(f"REFUS : {cible} existe déjà (jamais d'écrasement)")
    langues = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True).stdout.split()
    if "ara" not in langues:
        sys.exit("REFUS : langue tesseract `ara` non installée")

    ordre = list(range(DERNIERE, PREMIERE - 1, -1))      # ordre de lecture
    pages, total_inv = [], 0
    for p in ordre:
        brut = ocr(racine, p, cache)
        n_inv = len(INVISIBLES.findall(brut))
        propre = INVISIBLES.sub("", brut).strip()
        total_inv += n_inv
        pages.append((p, DECALAGE - p, n_inv, propre))
        tete = propre.splitlines()[0][:50] if propre else "(vide)"
        print(f"  PDF {p:3d}  impr. {DECALAGE - p:3d}  invisibles retirés {n_inv:3d}  | {tete}")
    if any(INVISIBLES.search(t) for *_, t in pages):
        sys.exit("REFUS Cmd 15 : invisibles résiduels")
    if sorted(p for p, *_ in pages) != list(range(PREMIERE, DERNIERE + 1)):
        sys.exit("REFUS : périmètre incomplet")
    print(f"  {len(pages)} pages, {total_inv} invisibles retirés au total")
    if not a.ecrire:
        print("  (constat seul — relancer avec --ecrire)")
        return
    corps = [f'---\nsource: "{PDF}"\nsection: "munqidh-08-texte-arabe"\n'
             f'pages_pdf: {PREMIERE}-{DERNIERE}\nlangue: ara\nordre: lecture (page PDF decroissante)\n---\n\n'
             f'# المنقذ من الضلال — texte arabe (édition Jabre, 1959)\n']
    for p, impr, n_inv, t in pages:
        corps.append(f"\n<!-- page {p} — arabe p. {impr} -->\n\n{t}\n")
    cible.write_text("".join(corps), encoding="utf-8")
    print(f"  écrit : {SORTIE}")


if __name__ == "__main__":
    main()
