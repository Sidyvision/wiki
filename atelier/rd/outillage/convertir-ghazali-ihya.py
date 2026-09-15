#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convertir-ghazali-ihya.py — Conversion PDF → Markdown de l'`Ihyâ' 'ulûm al-dîn`
d'al-Ghazâlî, texte arabe intégral.

Convertit `raw/9472.pdf` (3384 pages PDF, born-digital calibre 3.40.1) vers
`textes/ghazali-ihya-ulum-al-din-arabe/`.

Principe (même famille que convertir-ibnsirin-dictionnaire-reves.py) :
DÉTERMINISTE, sans LLM, sans réseau. Il ne touche jamais à `raw/` (immuable,
hors git) : il lit la couche texte du PDF et écrit la conversion dans `textes/`.

CHAÎNE — et pourquoi elle diffère des conversions précédentes du dépôt :

  1. `pdftotext` (poppler), PAS pymupdf.
     Motif mesuré, non théorique : sur ce PDF pymupdf restitue les mots de
     chaque ligne EN ORDRE INVERSE. Relevé page 30 —
       pymupdf   : «... المهلكات ربع في ذكرناه ما وأكثر»   (phrase à l'envers)
       pdftotext : «وأكثر ما ذكرناه في ربع المهلكات ...»   (ordre logique)
     Les trois conversions antérieures du dépôt emploient pymupdf ; elles
     portaient sur des PDF latins, où le défaut ne se manifeste pas. Pour tout
     PDF arabe natif, c'est `pdftotext` qui fait foi.

  2. Normalisation NFKC.
     Le PDF stocke l'arabe en FORMES DE PRÉSENTATION (U+FB50-FDFF, U+FE70-FEFF)
     et non en arabe standard (U+0600-06FF) : relevé page 30, 254 formes de
     présentation contre 70 caractères standard. Sans NFKC, aucune recherche
     n'aboutit — «ربع» ne s'apparie pas à «رﺑﻊ».

  3. Retrait des contrôles bidi (U+202A LRE, U+202B RLE, U+202C PDF, U+200E/F).
     Mesuré : 1562 occurrences pour 55k caractères en extraction brute.
     Ce n'est PAS une correction du texte — que la règle d'immuabilité
     interdirait. Ces marques n'appartiennent pas à l'œuvre : elles sont
     injectées par la couche de rendu pour piloter l'affichage bidirectionnel,
     exactement comme les formes de présentation. Le Cmd 15 en interdit
     l'insertion dans le dépôt ; les laisser passer serait les y introduire.

DÉCOUPAGE — par juz', imposé par la mesure et non choisi :
  Le découpage par kitâb (40 livres) a été sondé sur l'intégralité du texte
  normalisé. Les têtes de kitâb ne se distinguent pas des citations en cours de
  texte : sur 31 lignes commençant par «كتاب», on relève des titres
  («كتاب أسرار الزكاة») mêlés à des citations («كتاب الحج وبیت المقدس أیضا له
  فضل كبیر خرج ابن عمر من»). Aucun motif déterministe ne les sépare.
  En revanche les ancres de pagination du tirage sont COMPLÈTES et MONOTONES :
  1706 ancres relevées pour 1709 pages imprimées, les 3 absentes étant la
  page 1 de chacun des juz' 2, 3 et 4. Elles donnent 4 césures sûres et une
  pagination citable. Le texte est donc découpé par juz', puis par tranches de
  pages imprimées à l'intérieur de chaque juz'.
  Conséquence : le découpage porté par ce fichier est celui du TIRAGE arabe,
  pas la structure doctrinale en quatre rub' / quarante kitâb. Cette structure
  se documente dans une fiche `doctrinal/sources/`, pas dans `textes/`.

YÂ' PERSAN — TRANCHÉ. Verdict de Sidy, 2026-09-14 : unifier.
  Le PDF emploie U+06CC (yâ' persan) là où l'arabe emploie U+064A. Mesuré sur
  400 pages, le codepoint est ENTIÈREMENT prédit par la position dans le mot :
      initiale  U+06CC=5312   U+064A=0
      médiane   U+06CC=18332  U+064A=214
      finale    U+06CC=81     U+064A=7788
  Aucune graphie arabe ne distingue le yâ' selon sa position : c'était une
  correspondance de police, même classe que les formes de présentation déjà
  normalisées.
  Le défaut du drapeau `--unifier-ya` reste OFF : le verdict porte sur CE lot,
  non sur l'outil, qui sert d'autres PDF. La conversion versée dans textes/ a
  été produite AVEC le drapeau, et index-conversion.md porte la commande
  exacte — c'est là que se lit ce qui a été fait, ici ce qui est possible.
  Effet mesuré : substitution 1 pour 1, longueur totale inchangée
  (201930 + 67068 = 268998 occurrences). Sur l'appariement, « ينبغي » passe de
  0 à 804 occurrences et le titre « إحياء علوم الدين » de 0 à 24 : avant
  unification ils ne s'appariaient dans AUCUNE des deux graphies, parce qu'ils
  mêlaient les deux au sein d'un même mot.

Usage :
    # depuis la racine du dépôt (/root/wiki)
    python3 atelier/rd/outillage/convertir-ghazali-ihya.py
    python3 atelier/rd/outillage/convertir-ghazali-ihya.py --unifier-ya
    python3 atelier/rd/outillage/convertir-ghazali-ihya.py --sonde   # mesures seules

Réutilisable tel quel pour tout PDF arabe natif : --pdf et --sortie sont libres.
"""
import argparse
import os
import re
import subprocess
import sys
import unicodedata

PDF_DEFAUT = "raw/9472.pdf"
OUT_DEFAUT = "textes/ghazali-ihya-ulum-al-din-arabe"

# Contrôles bidirectionnels injectés par la couche de rendu.
# U+200E/U+200F sont nommés par le Cmd 15 ; U+202A-U+202E et les isolats
# U+2066-U+2069 ne le sont pas — ils sont retirés au même titre, mais la
# distinction est tenue dans l'instrument de mesure (indice I7 distinct).
BIDI = "".join(chr(c) for c in
        (0x202A, 0x202B, 0x202C, 0x202D, 0x202E,
         0x2066, 0x2067, 0x2068, 0x2069, 0x200E, 0x200F))
INVISIBLES_CMD15 = "".join(chr(c) for c in
        (0x200B, 0x200C, 0x200D, 0xFEFF))

YA_PERSAN, YA_ARABE = chr(0x06CC), chr(0x064A)

# «الجزء : N ¦ الصفحة : N» — l'ordre des champs varie selon le rendu bidi ;
# le motif est desserré sur les séparateurs. Vérifié : même rendement (1706)
# que le motif rigide, donc desserrer n'introduit pas de faux positifs.
ANCRE = re.compile(r"الجزء\s*[:¦\s]*(\d+)\s*[:¦\s]*الصفحة\s*[:¦\s]*(\d+)")

PAGES_PAR_FICHIER = 50  # pages imprimées par fichier de sortie


def extraire(pdf):
    """Couche texte du PDF via pdftotext, page par page (séparateur \\f)."""
    r = subprocess.run(["pdftotext", pdf, "-"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"pdftotext a échoué sur {pdf} : {r.stderr.strip()}")
    return r.stdout.split("\f")


def nettoyer(texte, unifier_ya=False):
    """NFKC puis retrait des invisibles. Jamais d'autre modification."""
    t = unicodedata.normalize("NFKC", texte)
    t = t.replace("\x00", "")
    for c in BIDI + INVISIBLES_CMD15:
        t = t.replace(c, "")
    if unifier_ya:
        t = t.replace(YA_PERSAN, YA_ARABE)
    return t


def decouper(pages, unifier_ya=False):
    """Associe chaque page PDF au (juz', page imprimée) de sa dernière ancre.

    L'ancre figure sur la page PDF où la page imprimée s'achève ; les pages
    PDF sans ancre héritent de la position courante. Le report est explicite
    et vérifiable — aucune interpolation.
    """
    out, juz, pimp = [], None, None
    for i, p in enumerate(pages, 1):
        t = nettoyer(p, unifier_ya)
        m = ANCRE.findall(t)
        if m:
            juz, pimp = int(m[-1][0]), int(m[-1][1])
        out.append({"pdf": i, "juz": juz, "page": pimp, "texte": t})
    return out


def ecrire(entrees, sortie, unifier_ya):
    os.makedirs(sortie, exist_ok=True)
    par_juz = {}
    for e in entrees:
        par_juz.setdefault(e["juz"], []).append(e)
    fichiers = []
    for juz in sorted(k for k in par_juz if k is not None):
        lot = par_juz[juz]
        pmax = max(e["page"] for e in lot if e["page"])
        for debut in range(1, pmax + 1, PAGES_PAR_FICHIER):
            fin = min(debut + PAGES_PAR_FICHIER - 1, pmax)
            bloc = [e for e in lot if e["page"] and debut <= e["page"] <= fin]
            if not bloc:
                continue
            nom = f"juz-{juz}-pages-{debut:03d}-{fin:03d}.md"
            corps = [f"# الجزء {juz} — الصفحات {debut}-{fin}", ""]
            for e in bloc:
                corps.append(f"<!-- pdf {e['pdf']} | juz {e['juz']} | "
                             f"صفحة {e['page']} -->")
                corps.append(e["texte"].strip())
                corps.append("")
            texte = "\n".join(corps) + "\n"
            # Garde Cmd 15 : rien d'invisible ne sort de ce script.
            for c in BIDI + INVISIBLES_CMD15:
                assert c not in texte, f"invisible résiduel dans {nom}"
            with open(os.path.join(sortie, nom), "w", encoding="utf-8") as f:
                f.write(texte)
            fichiers.append((nom, len(bloc), len(texte)))
    return fichiers


def sonder(entrees):
    """Mesures rapportées, jamais de verdict (Cmd 12)."""
    anc = [(e["juz"], e["page"]) for e in entrees if e["page"]]
    uniq = sorted(set(anc))
    print(f"pages PDF                 : {len(entrees)}")
    print(f"pages imprimées ancrées   : {len(uniq)}")
    for j in sorted({a for a, _ in uniq}):
        pp = sorted(p for a, p in uniq if a == j)
        trous = sorted(set(range(1, max(pp) + 1)) - set(pp))
        print(f"  juz {j} : {len(pp)}/{max(pp)} pages"
              f"  manquantes={trous if len(trous) < 10 else str(trous[:10]) + '...'}")
    print(f"monotonie (juz,page)      : {uniq == sorted(uniq)}")
    tot = sum(len(e["texte"]) for e in entrees)
    res_bidi = sum(e["texte"].count(c) for e in entrees for c in BIDI)
    res_inv = sum(e["texte"].count(c) for e in entrees for c in INVISIBLES_CMD15)
    pres = sum(1 for e in entrees for c in e["texte"]
               if 0xFB50 <= ord(c) <= 0xFDFF or 0xFE70 <= ord(c) <= 0xFEFF)
    y6 = sum(e["texte"].count(YA_PERSAN) for e in entrees)
    y4 = sum(e["texte"].count(YA_ARABE) for e in entrees)
    print(f"caractères après chaîne   : {tot}")
    print(f"contrôles bidi résiduels  : {res_bidi}")
    print(f"invisibles Cmd 15 résid.  : {res_inv}")
    print(f"formes de présentation    : {pres}")
    print(f"yâ' U+06CC / U+064A       : {y6} / {y4}")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", default=PDF_DEFAUT)
    ap.add_argument("--sortie", default=OUT_DEFAUT)
    ap.add_argument("--unifier-ya", action="store_true",
                    help="unifie U+06CC vers U+064A (défaut : non — "
                         "question soumise au verdict)")
    ap.add_argument("--sonde", action="store_true",
                    help="mesure sans écrire")
    a = ap.parse_args()

    pages = extraire(a.pdf)
    entrees = decouper(pages, a.unifier_ya)
    sonder(entrees)
    if a.sonde:
        return 0
    fichiers = ecrire(entrees, a.sortie, a.unifier_ya)
    print(f"\nfichiers écrits           : {len(fichiers)} dans {a.sortie}/")
    for nom, npages, taille in fichiers[:5]:
        print(f"  {nom}  {npages} pages PDF  {taille} car.")
    if len(fichiers) > 5:
        print(f"  ... ({len(fichiers) - 5} autres)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
