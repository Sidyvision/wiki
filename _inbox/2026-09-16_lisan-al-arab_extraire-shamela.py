#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrait le texte du Lisan al-Arab (Shamela book_id 1687) du CSV de la
categorie 30 (al-gharib wa-l-ma'ajim) du jeu de donnees MoMonir/shamela_books_text.

Sortie :
  - <out>/lisan-al-arab_shamela_pages.tsv   (une ligne = une page imprimée)
  - <out>/lisan-al-arab_shamela_texte.txt   (lecture continue, marqueurs [جN صM])
  - <out>/juz-01.txt .. juz-15.txt          (un fichier par volume)
  - <out>/rapport.txt                       (mesures brutes)

Aucune correction du texte : extraction fidele, octet pour octet dans le champ
`text` (les tabulations internes sont remplacees par un espace et les sauts de
ligne par l'espace, pour tenir une ligne par page).
"""
import csv, sys, os, hashlib, collections, re

BOOK_ID = "1687"
CSV = "/tmp/lisan/cat30.csv"
OUT = "/tmp/lisan/extract"

def esc(s):
    return (s or "").replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()

def main():
    os.makedirs(OUT, exist_ok=True)
    pages = []
    titles = collections.Counter()
    metas = {}
    total = 0
    with open(CSV, newline="", encoding="utf-8") as fh:
        r = csv.DictReader(fh)
        print("champs:", r.fieldnames, file=sys.stderr)
        for row in r:
            total += 1
            bid = (row.get("book_id") or "").strip()
            if bid != BOOK_ID:
                continue
            titles[(row.get("book_title") or "").strip()] += 1
            metas["edition"] = (row.get("edition") or "").strip()
            metas["publisher"] = (row.get("publisher") or "").strip()
            metas["category"] = (row.get("category") or "").strip()
            pages.append(row)
    print("lignes lues dans le CSV :", total, file=sys.stderr)
    print("pages retenues (book_id %s) : %d" % (BOOK_ID, len(pages)), file=sys.stderr)

    def vkey(p):
        v = (p.get("volume_number") or "").strip()
        try:
            return (0, float(v))
        except ValueError:
            return (1, 0.0)

    def pkey(p):
        pn = (p.get("page_number") or "").strip()
        try:
            return float(pn)
        except ValueError:
            return -1.0

    pages.sort(key=lambda p: (vkey(p), pkey(p)))

    # 1) TSV page par page
    with open(os.path.join(OUT, "lisan-al-arab_shamela_pages.tsv"), "w", encoding="utf-8") as f:
        f.write("volume\tpage\ttexte\tnote_bas_de_page\n")
        for p in pages:
            f.write("%s\t%s\t%s\t%s\n" % (
                (p.get("volume_number") or "").strip(),
                (p.get("page_number") or "").strip(),
                esc(p.get("text")),
                esc(p.get("foot_note"))))

    # 2) texte continu + 3) un fichier par volume
    vols = collections.defaultdict(list)
    for p in pages:
        vols[(p.get("volume_number") or "").strip()].append(p)

    def nom_volume(v):
        try:
            return "juz-%02d.txt" % int(float(v))
        except ValueError:
            return "juz-%s.txt" % re.sub(r"[^0-9A-Za-z]", "_", v)

    with open(os.path.join(OUT, "lisan-al-arab_shamela_texte.txt"), "w", encoding="utf-8") as g:
        g.write("# لسان العرب — ابن منظور — ط. دار صادر، الثالثة 1414هـ (نص المكتبة الشاملة)\n")
        g.write("# texte extrait du jeu de donnees MoMonir/shamela_books_text (book_id 1687)\n")
        g.write("# marqueur : [ج<volume> ص<page>] ; les notes de bas de page suivent le texte de la page\n\n")
        for v in sorted(vols, key=lambda x: vkey({"volume_number": x})):
            lp = sorted(vols[v], key=pkey)
            fname = nom_volume(v)
            with open(os.path.join(OUT, fname), "w", encoding="utf-8") as h:
                h.write("# المجلد %s\n\n" % v)
                for p in lp:
                    bloc = "[ج%s ص%s]\n%s\n" % (v, (p.get("page_number") or "").strip(), (p.get("text") or "").strip())
                    fn = (p.get("foot_note") or "").strip()
                    if fn:
                        bloc += "\n[حاشية]\n%s\n" % fn
                    bloc += "\n"
                    g.write(bloc)
                    h.write(bloc)

    # 4) mesures brutes
    lignes = []
    lignes.append("livre : %s" % (titles.most_common(1)[0][0] if titles else "?"))
    for k in ("edition", "publisher", "category"):
        lignes.append("%s : %s" % (k, metas.get(k, "")))
    lignes.append("pages (lignes) : %d" % len(pages))
    lignes.append("volumes : %d" % len(vols))
    for v in sorted(vols, key=lambda x: vkey({"volume_number": x})):
        lp = sorted(vols[v], key=pkey)
        pns = [pkey(p) for p in lp]
        num = [x for x in pns if x >= 0]
        lignes.append("  volume %-4s pages=%-5d page_min=%-6s page_max=%-6s trous=%d" % (
            v, len(lp),
            ("%g" % min(num)) if num else "-",
            ("%g" % max(num)) if num else "-",
            (int(max(num) - min(num) + 1 - len(num)) if num else 0)))
    car = sum(len(p.get("text") or "") for p in pages)
    lignes.append("caracteres de texte (champ text) : %d" % car)
    lignes.append("caracteres de notes : %d" % sum(len(p.get("foot_note") or "") for p in pages))
    with open(os.path.join(OUT, "rapport.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print("\n".join(lignes))

if __name__ == "__main__":
    main()
