#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
archiver-monitoring-quotidien.py — Copie datée du rapport de monitoring
infrastructure quotidien (job H‍ermes monitoring-infrastructure-quotidien)
vers l'archive R&D, et purge des copies de plus de 40 jours.

Principe (même famille que verifier-invariants.py, detecter-non-tracke.py) :
DÉTERMINISTE, sans LLM, sans réseau. Il ne lit ni ne réécrit le dépôt wiki
lui-même : il copie une sortie déjà produite par H‍ermes vers l'archive, et
supprime les copies dépassant la fenêtre de rétention. Dry-run par défaut ;
--appliquer requis pour tout effet de bord (Cmd 1 : jamais d'auto-accept).

Motif : suggestion Sidy 2026-08-18 (renforcer le monitoring de l'agent
infrastructure en conservant le rapport quotidien en parallèle du canal
Discord, 40 jours de rétention). Voir la fiche charte du dossier d'archive.

Format d'archive : .txt, jamais .md — les rapports citent la sortie brute de
generer-cartographie.py --verifier et verifier-invariants.py, qui contient des
tokens [[...]] littéraux (liens morts signalés). Un .md walké par ces mêmes
scripts s'auto-déclencherait dessus (piège déjà rencontré, voir
registre-problemes.md, entrée 2026-08-18). Le .txt est hors du périmètre des
deux scripts (filtre .endswith(".md")) et ne porte pas de Sceau à maintenir.

Usage :
    python3 archiver-monitoring-quotidien.py \
        --source /root/.hermes/profiles/studio/cron/output \
        --job-id 41dc3e7e492c \
        --archive /root/wiki/atelier/rd/infrastructure/monitoring-archive \
        [--retention-jours 40] [--appliquer]

Sans --appliquer : constat seul (ce qui serait copié, ce qui serait purgé).

Codes de sortie :
    0  exécution correcte (avec ou sans --appliquer)
    1  rien à archiver (source introuvable ou aucune sortie du job trouvée)
    2  erreur d'exécution du script lui-même
"""

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Nom de fichier produit par H‍ermes pour une sortie de job cron :
# "<job_id>_<YYYYMMDD>_<HHMMSS>.txt"
MOTIF_SORTIE = re.compile(r"^([0-9a-f]{12})_(\d{8})_(\d{6})\.txt$")


def lister_sorties(source, job_id):
    """Retourne [(chemin, date)] des sorties .txt du job_id trouvées dans
    source, triées par date croissante. Ne descend pas dans les
    sous-dossiers (le job_id/ contient aussi des .md, hors périmètre)."""
    trouvees = []
    if not source.is_dir():
        return trouvees
    for f in source.iterdir():
        if not f.is_file():
            continue
        m = MOTIF_SORTIE.match(f.name)
        if not m or m.group(1) != job_id:
            continue
        try:
            date = datetime.strptime(m.group(2) + m.group(3), "%Y%m%d%H%M%S")
        except ValueError:
            continue
        trouvees.append((f, date))
    return sorted(trouvees, key=lambda t: t[1])


def lister_archive(archive, job_id):
    """Retourne [(chemin, date)] des copies déjà archivées pour ce job_id,
    au format archive : "<YYYY-MM-DD>_<job_id>.txt"."""
    motif = re.compile(rf"^(\d{{4}}-\d{{2}}-\d{{2}})_{re.escape(job_id)}\.txt$")
    trouvees = []
    if not archive.is_dir():
        return trouvees
    for f in archive.iterdir():
        if not f.is_file():
            continue
        m = motif.match(f.name)
        if not m:
            continue
        try:
            date = datetime.strptime(m.group(1), "%Y-%m-%d")
        except ValueError:
            continue
        trouvees.append((f, date))
    return sorted(trouvees, key=lambda t: t[1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True,
                     help="dossier cron/output du profil H‍ermes")
    ap.add_argument("--job-id", required=True,
                     help="identifiant du job dont on archive la sortie")
    ap.add_argument("--archive", required=True,
                     help="dossier d'archive R&D destination")
    ap.add_argument("--retention-jours", type=int, default=40)
    ap.add_argument("--appliquer", action="store_true",
                     help="sans ce flag : constat seul, aucune écriture ni suppression")
    args = ap.parse_args()

    source = Path(args.source)
    archive = Path(args.archive)

    sorties = lister_sorties(source, args.job_id)
    if not sorties:
        print(f"  Aucune sortie trouvée pour le job {args.job_id} dans {source}.")
        return 1

    deja = {d.strftime("%Y-%m-%d") for _, d in lister_archive(archive, args.job_id)}
    a_copier = [(f, d) for f, d in sorties if d.strftime("%Y-%m-%d") not in deja]

    print(f"  {len(sorties)} sortie(s) source, {len(deja)} déjà archivée(s), "
          f"{len(a_copier)} à copier.")

    for f, d in a_copier:
        cible = archive / f"{d.strftime('%Y-%m-%d')}_{args.job_id}.txt"
        if args.appliquer:
            archive.mkdir(parents=True, exist_ok=True)
            cible.write_bytes(f.read_bytes())
            print(f"    copié  {f.name} -> {cible.name}")
        else:
            print(f"    [dry-run] copierait {f.name} -> {cible.name}")

    seuil = datetime.now() - timedelta(days=args.retention_jours)
    a_purger = [(f, d) for f, d in lister_archive(archive, args.job_id) if d < seuil]
    if a_purger:
        print(f"  {len(a_purger)} copie(s) au-delà de {args.retention_jours} jours.")
        for f, d in a_purger:
            if args.appliquer:
                f.unlink()
                print(f"    purgé  {f.name}")
            else:
                print(f"    [dry-run] purgerait {f.name}")
    else:
        print(f"  Aucune copie au-delà de {args.retention_jours} jours.")

    if not args.appliquer and (a_copier or a_purger):
        print("\n  Constat seul (dry-run) — relancer avec --appliquer pour agir.")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERREUR — {e}", file=sys.stderr)
        sys.exit(2)
