#!/usr/bin/env python3
"""Constituer le jeu de données d'entraînement d'INF-16 — script déterministe, sans LLM.

Motif : le devis de la rafale RunPod (`atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/
devis-rafale-runpod-2026-09-16.md`, §5) nomme trois préalables. Le premier est le **jeu de
données**. Il se construit par script, jamais à la main — et il se garde **hors du dépôt** :
c'est un artefact dérivé qui porte le corpus.

Ce que le script produit
------------------------
1. un **JSONL neutre** : un enregistrement par fiche, avec sa provenance
   (`{"id", "circuit", "chemin", "sha256", "titre", "texte"}`). Neutre = il ne présume pas de
   la recette d'entraînement (affinage supervisé, pré-entraînement continu, préférences) :
   la mise en forme attend la charge de référence (U1–U5), qui n'est pas arrêtée. Ce qui est
   arrêté ici, c'est le **contenu** et sa **traçabilité**, pas l'emballage.
2. un **manifeste** JSON : comptages, volumes, empreintes, liste des exclusions, horodatage.

Deux gardes refusent, et leur refus a été **observé** (§VII, Épreuve des contrôles)
------------------------------------------------------------------------------
- **Garde A — circuits interdits.** `meta/` est le Domaine Réservé (§VI : aucune matière
  personnelle ne quitte le dépôt, y compris pour un essai, y compris sous forme d'extrait) ;
  `textes/` porte des œuvres reçues dont certaines sont sous droits ; `_inbox/` est un sas.
  Les trois sont **refusés par nom**, avant toute lecture.
- **Garde B — sortie hors du dépôt.** Le jeu de données ne s'écrit **jamais** dans le dépôt :
  un artefact dérivé qui porte le corpus n'a rien à y faire, et il est volumineux. La sortie
  proposée par défaut est `/root/sandbox-rd/inf-16-dataset/`.

Usage
-----
    python3 atelier/rd/outillage/generer-jeu-donnees-entrainement.py --rapport
    python3 atelier/rd/outillage/generer-jeu-donnees-entrainement.py
    python3 atelier/rd/outillage/generer-jeu-donnees-entrainement.py --circuits doctrinal

Aucune dépendance : bibliothèque standard uniquement. Python 3.10+.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

# --- Constantes -------------------------------------------------------------

CIRCUITS_SOUVERAINS = ["doctrinal", "atelier", "hermeneutique", "label", "protocoles"]

#: Refusés par nom, quelle que soit la demande (Garde A).
INTERDITS = {
    "meta": "Domaine Réservé — §VI : aucune matière personnelle ne quitte le dépôt, "
            "y compris pour un essai, y compris sous forme d'extrait",
    "textes": "œuvres reçues converties, dont certaines sous droits — la question "
              "s'est instruit avant tout U4, elle n'est pas tranchée",
    "_inbox": "sas de déchargement — il n'est pas une source, il est une file d'attente",
}

SORTIE_DEFAUT = "/root/sandbox-rd/inf-16-dataset"

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
TITRE_FM = re.compile(r"^title:\s*\"?(.*?)\"?\s*$", re.M)


def sha256_texte(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def sha256_fichier(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for bloc in iter(lambda: f.read(65536), b""):
            h.update(bloc)
    return h.hexdigest()


def decouper(texte: str) -> tuple[str, str]:
    """Rend (titre, corps). Le frontmatter est retiré : il décrit la fiche, il n'est pas
    son propos — et ses clés (`links`, `sources`) sont des métadonnées du dépôt, pas de la
    matière entraînable."""
    titre = ""
    m = FM.match(texte)
    if not m:
        return titre, texte
    mt = TITRE_FM.search(m.group(1))
    if mt:
        titre = mt.group(1).strip()
    return titre, texte[m.end():]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Jeu de données d'entraînement d'INF-16 (déterministe).")
    ap.add_argument("--racine", default="/root/wiki", help="racine du dépôt (défaut : /root/wiki)")
    ap.add_argument("--circuits", default=",".join(CIRCUITS_SOUVERAINS),
                    help=f"circuits à verser (défaut : {','.join(CIRCUITS_SOUVERAINS)})")
    ap.add_argument("--sortie", default=SORTIE_DEFAUT, help=f"répertoire de sortie (défaut : {SORTIE_DEFAUT})")
    ap.add_argument("--rapport", action="store_true", help="n'écrit rien : compte et rapporte")
    ap.add_argument("--sans-frontmatter", dest="sans_fm", action="store_true", default=True)
    ap.add_argument("--avec-frontmatter", dest="sans_fm", action="store_false")
    args = ap.parse_args(argv)

    racine = pathlib.Path(args.racine).resolve()
    sortie = pathlib.Path(args.sortie).resolve()
    demandes = [c.strip() for c in args.circuits.split(",") if c.strip()]

    # --- Garde A : circuits interdits, refusés par nom -----------------------
    for c in demandes:
        if c in INTERDITS:
            print(f"REFUS — circuit « {c} » interdit au jeu de données.", file=sys.stderr)
            print(f"  Motif : {INTERDITS[c]}.", file=sys.stderr)
            print("  Le refus précède toute lecture : rien n'a été ouvert, rien n'a été écrit.",
                  file=sys.stderr)
            return 2

    absents = [c for c in demandes if not (racine / c).is_dir()]
    if absents:
        print(f"REFUS — circuit(s) introuvable(s) : {', '.join(absents)}.", file=sys.stderr)
        return 2

    # --- Garde B : la sortie ne s'écrit jamais dans le dépôt -----------------
    if sortie == racine or racine in sortie.parents:
        print(f"REFUS — la sortie « {sortie} » est à l'intérieur du dépôt « {racine} ».", file=sys.stderr)
        print("  Motif : un artefact dérivé qui porte le corpus se garde hors du dépôt.", file=sys.stderr)
        print("  La sortie par défaut est /root/sandbox-rd/inf-16-dataset/.", file=sys.stderr)
        return 2

    # --- Collecte, déterministe (chemins triés) ------------------------------
    enregistrements: list[dict] = []
    par_circuit: dict[str, dict] = {}
    for circuit in demandes:
        fiches = 0
        caracteres = 0
        for p in sorted((racine / circuit).rglob("*.md")):
            brut = p.read_text(encoding="utf-8", errors="ignore")
            titre, corps = decouper(brut) if args.sans_fm else ("", brut)
            if not corps.strip():
                continue
            enregistrements.append({
                "id": f"{circuit}/{p.relative_to(racine / circuit).as_posix()}",
                "circuit": circuit,
                "chemin": str(p.relative_to(racine)),
                "sha256": sha256_texte(brut),
                "titre": titre,
                "texte": corps,          # déjà séparé : le JSONL est un enregistrement par ligne
            })
            fiches += 1
            caracteres += len(brut)
        par_circuit[circuit] = {"fiches": fiches, "caracteres": caracteres}

    total_car = sum(v["caracteres"] for v in par_circuit.values())
    manifeste = {
        "objet": "Jeu de données d'entraînement d'INF-16 — corpus souverain du dépôt",
        "genere_le_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "outil": {
            "chemin": "atelier/rd/outillage/generer-jeu-donnees-entrainement.py",
            "sha256": sha256_fichier(pathlib.Path(__file__)),
        },
        "racine_lue": str(racine),
        "circuits_verses": demandes,
        "exclusions": {c: INTERDITS[c] for c in INTERDITS},
        "frontmatter_retire": args.sans_fm,
        "comptage": {
            "enregistrements": len(enregistrements),
            "caracteres": total_car,
            "par_circuit": par_circuit,
            "estimation_jetons": {
                "methode": "caractères / ratio, ESTIMATION et non mesure — aucun tokenizer appliqué",
                "a_3_5_car_par_jeton_M": round(total_car / 3.5 / 1e6, 2),
                "a_4_5_car_par_jeton_M": round(total_car / 4.5 / 1e6, 2),
            },
        },
    }

    if args.rapport:
        print(json.dumps(manifeste["comptage"], ensure_ascii=False, indent=2))
        print("\n--rapport : rien n'a été écrit.")
        return 0

    sortie.mkdir(parents=True, exist_ok=True)
    chemin_jsonl = sortie / "corpus-souverain.jsonl"
    with chemin_jsonl.open("w", encoding="utf-8") as f:
        for e in enregistrements:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    manifeste["sortie"] = {
        "jsonl": str(chemin_jsonl),
        "octets": chemin_jsonl.stat().st_size,
        "sha256": sha256_fichier(chemin_jsonl),
    }
    chemin_manifeste = sortie / "manifeste.json"
    chemin_manifeste.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n",
                                encoding="utf-8")

    print(f"JSONL     : {chemin_jsonl} ({manifeste['sortie']['octets'] / 1e6:.1f} Mo)")
    print(f"Manifeste : {chemin_manifeste}")
    print(f"Empreinte : {manifeste['sortie']['sha256'][:16]}…")
    print(f"Enregistrements : {len(enregistrements)} · caractères : {total_car:,}".replace(",", " "))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
