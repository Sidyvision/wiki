#!/usr/bin/env python3
# =============================================================================
# verser-dossier-textes.py — versement CIBLÉ d'un dossier (ou d'un fichier) de
# `raw/` vers `textes/`, sans relancer la migration globale.
#
#   POURQUOI CE SCRIPT EXISTE (2026-09-15). `migrer-textes-convertis.py --migrer`
#   recopie TOUT `raw/` : il écraserait les nettoyages consignés dans `textes/`
#   depuis l'amendement du 2026-09-14 (règle d'immuabilité, §II). Pour verser un
#   corpus nouveau, il faut une copie limitée à ce corpus. Écrit d'abord comme
#   script ponctuel pour *Orient et Occident*, conservé ici comme outil sur
#   consigne de Sidy (« on conserve toute pièce d'outillage »).
#
#   Il RÉUTILISE les fonctions de migrer-textes-convertis.py (slug, destination,
#   contrôle G1) : même nommage, mêmes gardes, aucune règle dupliquée.
#
#   GARDES, bloquantes :
#     G1  donnée personnelle → refus, fichier nommé
#     G2  destination existante → refus (jamais d'écrasement) ; passer --nom
#         pour verser un fichier seul sous un nom distinct
#     C15 caractère invisible (zéro-largeur, bidi, BOM) → refus
#   Après copie : contrôle octet par octet (filecmp), rapporté.
#
#   Usage :
#     python3 atelier/rd/outillage/verser-dossier-textes.py "raw/Orient et Occident"
#     python3 …/verser-dossier-textes.py "raw/Orient et Occident" --verser
#     python3 …/verser-dossier-textes.py "raw/<fichier>.md" \
#         --vers orient-et-occident --nom page-228.md --verser
#   Les chemins de `raw/` sont en NFD : le script résout le nom par slug, de
#   sorte qu'un chemin tapé en NFC aboutit.
# =============================================================================

import argparse
import filecmp
import importlib.util
import shutil
import sys
from pathlib import Path

INVISIBLES = "​‌‍⁠﻿‪‫‬‭‮‎‏"


def charger_migration(repo):
    chemin = repo / "atelier/rd/outillage/migrer-textes-convertis.py"
    spec = importlib.util.spec_from_file_location("migration", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def resoudre(repo, m, cible):
    """Trouve le chemin réel sous raw/ malgré le piège NFD/NFC."""
    raw = repo / "raw"
    rel = Path(cible)
    if rel.parts and rel.parts[0] == "raw":
        rel = Path(*rel.parts[1:])
    courant = raw
    for part in rel.parts:
        fils = [p for p in courant.iterdir()
                if m.slug(p.name, p.is_file()) == m.slug(part, part.lower().endswith(".md"))]
        if len(fils) != 1:
            sys.exit(f"REFUS : « {part} » introuvable ou ambigu sous {courant}")
        courant = fils[0]
    return raw, courant


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cible", help="dossier ou fichier .md sous raw/")
    ap.add_argument("--repo", default="/root/wiki")
    ap.add_argument("--vers", default=None, help="dossier de textes/ (défaut : slug du dossier source)")
    ap.add_argument("--nom", default=None, help="nom de destination (fichier seul)")
    ap.add_argument("--verser", action="store_true", help="copie réellement (défaut : constate)")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    m = charger_migration(repo)
    raw, src = resoudre(repo, m, a.cible)

    fichiers = sorted(src.glob("*.md")) if src.is_dir() else [src]
    if a.nom and len(fichiers) != 1:
        sys.exit("REFUS : --nom ne vaut que pour un fichier seul")
    plan, refus = [], []
    for f in fichiers:
        if a.vers or a.nom:
            dossier = a.vers or m.destination(f.relative_to(raw)).parent.name
            dest = repo / "textes" / dossier / (a.nom or m.slug(f.name, True))
        else:
            dest = repo / "textes" / m.destination(f.relative_to(raw))
        motifs = m.controler_personnel(f)
        texte = f.read_text(encoding="utf-8", errors="replace")
        if motifs:
            refus.append(f"G1  {f.name} [{', '.join(motifs)}]")
        if any(c in texte for c in INVISIBLES):
            refus.append(f"C15 {f.name} : caractère invisible")
        if dest.exists():
            refus.append(f"G2  {dest.relative_to(repo)} existe déjà")
        plan.append((f, dest))

    for f, dest in plan:
        print(f"  {f.name}\n    → {dest.relative_to(repo)}")
    if refus:
        print("\nVERSEMENT REFUSÉ :")
        for r in refus:
            print("  ✗", r)
        return 1
    if not a.verser:
        print(f"\n{len(plan)} fichier(s) — constat seul, relancer avec --verser")
        return 0
    for f, dest in plan:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)            # COPIE : raw/ demeure intact (Cmd 10)
    identiques = sum(filecmp.cmp(f, d, shallow=False) for f, d in plan)
    print(f"\n✓ {len(plan)} fichier(s) versé(s) ; identiques octet pour octet : {identiques}/{len(plan)}")
    return 0 if identiques == len(plan) else 2


if __name__ == "__main__":
    sys.exit(main())
