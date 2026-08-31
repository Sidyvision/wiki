#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
detecter-non-tracke.py — Constat mécanique des fichiers non trackés par git,
classés par circuit du dépôt.

Principe (même famille que verifier-invariants.py) : DÉTERMINISTE, sans LLM, sans
réseau. Il ne corrige rien, ne supprime rien, ne stage rien — il constate. Un
fichier non tracké n'est pas en soi une anomalie (brouillon en cours, asset
déposé avant sa fiche) ; ce script rend visible ce qui, sinon, reste implicite
d'une session à l'autre.

Usage :
    python3 detecter-non-tracke.py [--racine /root/wiki] [--json]

Codes de sortie :
    0  aucun fichier non tracké
    1  au moins un fichier non tracké (constat, pas une erreur de dépôt)
    2  erreur d'exécution du script lui-même (ex. pas un dépôt git)
"""

import argparse
import json
import subprocess
import sys

# Dossiers de service, jamais un circuit — un fichier non tracké ici n'a pas
# vocation à être classé par circuit (raw/ = dépôts en attente, _inbox/ = idem).
# Note (2026-08-31) : Graphe/ a déménagé sous atelier/rd/outillage/graphe/ — il
# relève désormais normalement du circuit atelier, retiré de cet ensemble.
DOSSIERS_HORS_CIRCUIT = {"raw", "_inbox", ".git"}

# Circuits reconnus par le protocole (CLAUDE.md §I). Note : verifier-invariants.py
# n'en connaît que 4 (doctrinal, atelier, label, meta) — hermeneutique/ existe au
# dépôt sans être couvert par son CIRCUITS. Ce script le traite comme un circuit à
# part entière pour ne pas reproduire l'angle mort ; voir registre-problemes.md
# si un fichier hermeneutique/ apparaît ici sans jamais avoir été trackè.
CIRCUITS = {"doctrinal", "atelier", "label", "hermeneutique", "meta"}


def lister_non_trackes(racine):
    """Retourne les chemins (relatifs à racine) non trackés par git : fichiers
    jamais ajoutés (??) et fichiers modifiés non stagés/commités."""
    out = subprocess.run(
        ["git", "-C", racine, "status", "--porcelain"],
        capture_output=True, text=True, check=True,
    )
    entrees = []
    for ligne in out.stdout.splitlines():
        if not ligne.strip():
            continue
        statut, chemin = ligne[:2], ligne[3:]
        # Un rename porcelain ("R  old -> new") — ne garder que la cible.
        if " -> " in chemin:
            chemin = chemin.split(" -> ", 1)[1]
        entrees.append((statut.strip(), chemin))
    return entrees


def classer(chemin):
    tete = chemin.split("/")[0]
    if tete in DOSSIERS_HORS_CIRCUIT:
        return "hors-circuit"
    if tete in CIRCUITS:
        return tete
    if "/" not in chemin:
        return "racine"
    return "hors-circuit-inconnu"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        entrees = lister_non_trackes(args.racine)
    except subprocess.CalledProcessError as e:
        print(f"ERREUR — git status a échoué : {e}", file=sys.stderr)
        return 2
    except FileNotFoundError:
        print("ERREUR — git introuvable dans l'environnement.", file=sys.stderr)
        return 2

    par_circuit = {}
    for statut, chemin in entrees:
        circuit = classer(chemin)
        par_circuit.setdefault(circuit, []).append((statut, chemin))

    if args.json:
        print(json.dumps(
            {c: [{"statut": s, "chemin": p} for s, p in v] for c, v in par_circuit.items()},
            ensure_ascii=False, indent=2,
        ))
        return 1 if entrees else 0

    if not entrees:
        print("  Aucun fichier non tracké.")
        return 0

    print(f"  {len(entrees)} fichier(s) non tracké(s), par circuit :\n")
    for circuit in sorted(par_circuit):
        items = par_circuit[circuit]
        marque = " ⚠" if circuit == "hors-circuit-inconnu" else ""
        print(f"  [{circuit}]{marque} {len(items)}")
        for statut, chemin in sorted(items, key=lambda t: t[1]):
            print(f"    {statut:3s} {chemin}")
        print()

    if "hors-circuit-inconnu" in par_circuit:
        print("  ⚠ des chemins ci-dessus n'appartiennent à aucun circuit reconnu "
              "(doctrinal/atelier/label/hermeneutique/meta) ni aux dossiers de "
              "service usuels — à vérifier : nouveau dossier racine ? faute de "
              "frappe de chemin ?")

    return 1


if __name__ == "__main__":
    sys.exit(main())
