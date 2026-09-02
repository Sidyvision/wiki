#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier-rapports-traites.py — Confronte les rapports Studio archivés
(monitoring-archive/*.txt) au registre de traitement
(monitoring-archive/registre-traitement.md), pour répondre mécaniquement à
une question précédant tout diagnostic : « ce rapport a-t-il déjà été
regardé par quelqu'un ? »

Motif (registre-problemes.md, [2026-09-02]) : deux sessions distinctes
(Sidy en direct, une session Claude Code) ont pu retraiter les mêmes
suggestions d'un même rapport sans que l'une sache que l'autre était déjà
passée. Ce script ne corrige rien et ne juge pas la qualité d'un
traitement — il constate seulement une absence d'entrée, même famille que
detecter-non-tracke.py et verifier-coherence-infrastructure.py :
DÉTERMINISTE, sans LLM, sans réseau.

Limite assumée, non contournée : ce script ne connaît que les rapports
Studio, seuls archivés au dépôt (charte : monitoring-archive-charte.md). Les
rapports Publication (job veille-referencement-investigation-08) ne laissent
aucune trace mécanique tant que INF-15 (registre-chantiers.md) n'est pas
tranché — ce script ne peut donc jamais les vérifier, et le dit en sortie
plutôt que de rester silencieux dessus.

Usage :
    python3 verifier-rapports-traites.py [--racine /root/wiki] [--json]

Codes de sortie :
    0  tous les rapports Studio postérieurs à l'ouverture du registre
       (2026-09-02) ont une entrée de traitement
    1  au moins un rapport Studio postérieur au 2026-09-02 n'a aucune entrée
    2  erreur d'exécution du script lui-même (registre introuvable, etc.)
"""

import argparse
import datetime
import glob
import json
import os
import re
import sys

OUVERTURE_REGISTRE = datetime.date(2026, 9, 2)

MOTIF_ARCHIVE = re.compile(r"^(\d{4}-\d{2}-\d{2})_([0-9a-f]+)\.txt$")
MOTIF_ENTREE = re.compile(
    r"^## \[\d{4}-\d{2}-\d{2}\] traite \| (\S+) \| (\S+) \| rapport du (\d{4}-\d{2}-\d{2})",
    re.MULTILINE,
)


def lister_archives(racine):
    """Retourne [(date, job_id, chemin)] pour chaque .txt de monitoring-archive/,
    trié par date."""
    motif = os.path.join(
        racine, "atelier", "rd", "infrastructure", "monitoring-archive", "*.txt"
    )
    archives = []
    for chemin in glob.glob(motif):
        base = os.path.basename(chemin)
        m = MOTIF_ARCHIVE.match(base)
        if not m:
            continue
        date = datetime.date.fromisoformat(m.group(1))
        archives.append((date, m.group(2), chemin))
    return sorted(archives)


def lire_registre(racine):
    """Retourne l'ensemble des (profil, job_id, date_rapport) déjà consignés
    dans registre-traitement.md. Lève FileNotFoundError si le registre
    n'existe pas."""
    chemin = os.path.join(
        racine,
        "atelier", "rd", "infrastructure", "monitoring-archive",
        "registre-traitement.md",
    )
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    entrees = set()
    for profil, job_id, date_str in MOTIF_ENTREE.findall(texte):
        entrees.add((profil, job_id, datetime.date.fromisoformat(date_str)))
    return entrees


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--racine", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    racine = os.path.abspath(args.racine)

    try:
        entrees = lire_registre(racine)
    except FileNotFoundError:
        print("ERREUR : registre-traitement.md introuvable — "
              "atelier/rd/infrastructure/monitoring-archive/registre-traitement.md",
              file=sys.stderr)
        return 2

    archives = lister_archives(racine)

    hors_perimetre = []
    traites = []
    non_traites = []
    for date, job_id, chemin in archives:
        rel = os.path.relpath(chemin, racine)
        if date < OUVERTURE_REGISTRE:
            hors_perimetre.append(rel)
            continue
        # Le profil des archives Studio n'apparaît pas dans le nom de fichier
        # (seul le job_id y figure) : on accepte toute entrée du bon job_id
        # et de la bonne date, quel que soit le profil consigné.
        trouve = any(j == job_id and d == date for (_, j, d) in entrees)
        (traites if trouve else non_traites).append(rel)

    if args.json:
        print(json.dumps({
            "hors_perimetre": hors_perimetre,
            "traites": traites,
            "non_traites": non_traites,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"Registre : {len(entrees)} entrée(s) de traitement.")
        print(f"Archives Studio : {len(archives)} fichier(s) total, "
              f"dont {len(hors_perimetre)} antérieur(s) à l'ouverture du "
              f"registre ({OUVERTURE_REGISTRE.isoformat()}, hors périmètre).")
        print()
        if non_traites:
            print(f"{len(non_traites)} rapport(s) SANS entrée de traitement :")
            for rel in non_traites:
                print(f"  ! {rel}")
        else:
            print("Tous les rapports du périmètre ont une entrée de traitement.")
        print()
        print("Rappel : ce script ne couvre pas les rapports du profil "
              "publication (non archivés — voir INF-15, registre-chantiers.md).")

    return 1 if non_traites else 0


if __name__ == "__main__":
    sys.exit(main())
