#!/usr/bin/env python3
"""Émettre le jeu d'évaluation d'INF-16 — script déterministe, sans LLM.

La **fiche est la source de vérité** :
`atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/eval-jeu-de-taches-2026-09-16.md`.
Ce script ne fait que l'extraire et l'emballer, en portant l'empreinte de la fiche : un jeu
d'évaluation non traçé ne vaut pas mieux qu'une mesure non datée.

Trois gardes refusent, et leur refus s'observe (§VII, Épreuve des contrôles)
--------------------------------------------------------------------------
- **Garde A — bloc de tâches absent.** Pas de bloc `TACHES:DEBUT` / `TACHES:FIN`, ou bloc
  illisible : refus (code 2), rien n'est écrit.
- **Garde B — tâche malformée ou doublon.** Une tâche sans `id`, `famille`, `question`,
  `attendu`, `source`, une famille hors `F1`–`F4`, ou un `id` en double : refus, rien n'est
  écrit. Un jeu d'évaluation qui contient un doublon compte deux fois la même réponse.
- **Garde C — sortie dans le dépôt.** Refus, comme pour le jeu de données : l'artefact
  dérivé se garde hors du dépôt.

Usage
-----
    python3 atelier/rd/outillage/generer-jeu-evaluation.py --rapport
    python3 atelier/rd/outillage/generer-jeu-evaluation.py
    python3 atelier/rd/outillage/generer-jeu-evaluation.py --fiche <autre-fiche.md>

Bibliothèque standard uniquement. Python 3.10+.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

FICHE_DEFAUT = ("atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/"
                "eval-jeu-de-taches-2026-09-16.md")
SORTIE_DEFAUT = "/root/sandbox-rd/inf-16-dataset"
FAMILLES = {"F1", "F2", "F3", "F4"}
CHAMPS = ("id", "famille", "question", "attendu", "source")

BLOC = re.compile(r"<!--\s*TACHES:DEBUT\s*-->\s*```json\s*(.*?)\s*```\s*<!--\s*TACHES:FIN\s*-->", re.S)


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Jeu d'évaluation d'INF-16 (déterministe).")
    ap.add_argument("--racine", default="/root/wiki", help="racine du dépôt (défaut : /root/wiki)")
    ap.add_argument("--fiche", default=FICHE_DEFAUT, help="fiche source (relative à la racine)")
    ap.add_argument("--sortie", default=SORTIE_DEFAUT, help=f"répertoire de sortie (défaut : {SORTIE_DEFAUT})")
    ap.add_argument("--rapport", action="store_true", help="n'écrit rien : compte et rapporte")
    args = ap.parse_args(argv)

    racine = pathlib.Path(args.racine).resolve()
    sortie = pathlib.Path(args.sortie).resolve()
    chemin_fiche = pathlib.Path(args.fiche)
    if not chemin_fiche.is_absolute():
        chemin_fiche = racine / chemin_fiche

    # --- Garde C : la sortie ne s'écrit jamais dans le dépôt -----------------
    if sortie == racine or racine in sortie.parents:
        print(f"REFUS — la sortie « {sortie} » est à l'intérieur du dépôt « {racine} ».", file=sys.stderr)
        print("  Motif : l'artefact dérivé se garde hors du dépôt.", file=sys.stderr)
        return 2

    if not chemin_fiche.is_file():
        print(f"REFUS — fiche introuvable : {chemin_fiche}.", file=sys.stderr)
        return 2
    octets = chemin_fiche.read_bytes()
    texte = octets.decode("utf-8")

    # --- Garde A : bloc de tâches présent et lisible -------------------------
    m = BLOC.search(texte)
    if not m:
        print("REFUS — bloc de tâches absent ou illisible dans la fiche.", file=sys.stderr)
        print("  Attendu : <!-- TACHES:DEBUT --> ```json [ … ] ``` <!-- TACHES:FIN -->.", file=sys.stderr)
        print("  Rien n'a été écrit.", file=sys.stderr)
        return 2
    try:
        taches = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"REFUS — le bloc de tâches n'est pas un JSON valide : {e}.", file=sys.stderr)
        return 2
    if not isinstance(taches, list) or not taches:
        print("REFUS — le bloc de tâches doit être une liste non vide.", file=sys.stderr)
        return 2

    # --- Garde B : champs requis, familles connues, identifiants uniques -----
    vus: set[str] = set()
    for i, t in enumerate(taches, 1):
        if not isinstance(t, dict):
            print(f"REFUS — tâche n°{i} : ce n'est pas un objet.", file=sys.stderr)
            return 2
        manquants = [c for c in CHAMPS if not str(t.get(c, "")).strip()]
        if manquants:
            print(f"REFUS — tâche n°{i} : champ(s) manquant(s) ou vide(s) : {', '.join(manquants)}.",
                  file=sys.stderr)
            return 2
        if t["famille"] not in FAMILLES:
            print(f"REFUS — tâche {t['id']} : famille « {t['famille']} » hors vocabulaire "
                  f"({', '.join(sorted(FAMILLES))}).", file=sys.stderr)
            return 2
        if t["id"] in vus:
            print(f"REFUS — identifiant en double : {t['id']} — un doublon compte deux fois "
                  f"la même réponse.", file=sys.stderr)
            return 2
        vus.add(t["id"])

    par_famille: dict[str, int] = {}
    for t in taches:
        par_famille[t["famille"]] = par_famille.get(t["famille"], 0) + 1

    manifeste = {
        "objet": "Jeu d'évaluation d'INF-16 (quatre familles : terminologie, refus, "
                 "non-syncrétisme, stabilité)",
        "genere_le_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fiche_source": {
            "chemin": str(chemin_fiche.relative_to(racine)) if racine in chemin_fiche.parents else str(chemin_fiche),
            "sha256": sha256_octets(octets),
        },
        "outil": {
            "chemin": "atelier/rd/outillage/generer-jeu-evaluation.py",
            "sha256": sha256_octets(pathlib.Path(__file__).read_bytes()),
        },
        "comptage": {"taches": len(taches), "par_famille": dict(sorted(par_famille.items()))},
        "avertissement": "Ne mesure aucune performance métier : la charge de référence "
                         "(U1-U5) n'est pas arrêtée. Voir la fiche, §« Ce que ce jeu ne dit pas ».",
    }

    if args.rapport:
        print(json.dumps(manifeste["comptage"], ensure_ascii=False, indent=2))
        print("\n--rapport : rien n'a été écrit.")
        return 0

    sortie.mkdir(parents=True, exist_ok=True)
    chemin_jsonl = sortie / "taches.jsonl"
    with chemin_jsonl.open("w", encoding="utf-8") as f:
        for t in taches:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    manifeste["sortie"] = {
        "jsonl": str(chemin_jsonl),
        "octets": chemin_jsonl.stat().st_size,
        "sha256": sha256_octets(chemin_jsonl.read_bytes()),
    }
    (sortie / "manifeste-evaluation.json").write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Tâches    : {len(taches)} ({', '.join(f'{k}={v}' for k, v in sorted(par_famille.items()))})")
    print(f"JSONL     : {chemin_jsonl} ({manifeste['sortie']['octets']} octets)")
    print(f"Empreinte fiche : {manifeste['fiche_source']['sha256'][:16]}…")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
