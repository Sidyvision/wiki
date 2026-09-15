#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nettoyer-sauts-de-page-textes.py — retrait des sauts de page `pdftotext` (U+000C)
dans les conversions de `textes/`.

DÉTERMINISTE, sans LLM, sans réseau. `--appliquer` est requis pour écrire :
sans lui, le script se contente de rapporter (Cmd 12).

Justification, et sa limite. La règle du dépôt veut qu'un texte de `textes/` ne
se corrige pas — une meilleure conversion le remplace, datée. Le verdict de Sidy
du 2026-09-14 l'amende : `textes/` peut être corrigé **lorsque c'est
qualitativement justifié**. Ce script ne s'autorise que du cas où la
justification ne tient pas au jugement :

  · U+000C n'appartient pas à l'œuvre. Il est injecté par la couche
    d'extraction, au même titre que les contrôles bidirectionnels et les formes
    de présentation retirés lors de la conversion de l'Ihyâ' arabe (motif
    consigné en `textes/ghazali-ihya-ulum-al-din-arabe/index-conversion.md`,
    étape 3). Le retirer n'est pas corriger un texte : c'est retirer ce que la
    machine y a mis.
  · Il ne porte aucune information propre. Chaque occurrence est immédiatement
    suivie du marqueur `<!-- page N -->` de la conversion, qui dit la même
    chose en clair et se cherche par `grep`.

GARDE-FOU : le script ne touche QUE les lignes dont U+000C est le seul contenu.
Une occurrence accolée à du texte porterait peut-être autre chose, et relève
alors du verdict, non de l'automatisme — elle est rapportée et laissée.

La ligne est remplacée par une ligne VIDE, non supprimée : sa suppression
collerait le dernier paragraphe d'une page au marqueur de la suivante, et
changerait le découpage en blocs du markdown. Retirer l'invisible ne doit rien
déplacer d'autre.

Usage :
    python3 nettoyer-sauts-de-page-textes.py [--racine .] [--appliquer]
"""

import argparse
import sys
from pathlib import Path

SAUT = chr(0x000C)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".")
    ap.add_argument("--appliquer", action="store_true",
                    help="écrire les fichiers ; sans ce drapeau, rapport seul")
    args = ap.parse_args()

    base = Path(args.racine).resolve() / "textes"
    if not base.is_dir():
        print(f"pas de dossier textes/ sous {args.racine}", file=sys.stderr)
        return 2

    touches = seuls = accoles = 0
    for p in sorted(base.rglob("*.md")):
        texte = p.read_text(encoding="utf-8")
        if SAUT not in texte:
            continue
        lignes = texte.split("\n")
        n_seuls = n_accoles = 0
        for i, ligne in enumerate(lignes):
            if SAUT not in ligne:
                continue
            if ligne.strip(SAUT).strip() == "":
                lignes[i] = ""
                n_seuls += 1
            else:
                n_accoles += 1
                print(f"  LAISSÉ (accolé à du texte) : "
                      f"{p.relative_to(base.parent)}:{i + 1}")
        if n_seuls:
            touches += 1
            seuls += n_seuls
            if args.appliquer:
                p.write_text("\n".join(lignes), encoding="utf-8")
        accoles += n_accoles
        print(f"{'modifié' if args.appliquer and n_seuls else 'relevé '} "
              f"{p.relative_to(base.parent)} — {n_seuls} seul(s), {n_accoles} accolé(s)")

    print(f"\n{touches} fichier(s), {seuls} saut(s) de page seuls sur leur ligne, "
          f"{accoles} accolé(s) à du texte (laissés au verdict).")
    if not args.appliquer:
        print("RAPPORT SEUL — relancer avec --appliquer pour écrire.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
