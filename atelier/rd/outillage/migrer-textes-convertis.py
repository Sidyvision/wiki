#!/usr/bin/env python3
# =============================================================================
# migrer-textes-convertis.py — de `raw/` (masqué) vers `textes/` (versionné)
#
#   Chantier PRO-08, plan visé par Sidy le 2026-09-02 :
#   « textes/ validé, dédoublonne avant migration, et amende le §II ».
#
#   POURQUOI CE SCRIPT EXISTE. `/raw/*` est dans `.gitignore` : les 708 fichiers
#   Markdown convertis (corpus Guénon, Jurjani, Avalon, Shayegan, Vâlsan) ne se
#   synchronisent jamais vers Obsidian. Sidy ne peut les lire que depuis le
#   terminal — c'est-à-dire au poste où il ne travaille pas.
#
#   CE QU'IL FAIT : il COPIE, il ne déplace jamais (Cmd 10). `raw/` demeure
#   intact, binaires et pièces nominatives compris — c'est tout l'objet de la
#   seconde voie.
#
#   TROIS GARDES, toutes BLOQUANTES :
#     G1  données personnelles  → le fichier n'est pas migré, et il est nommé
#     G2  collision de destination → refus global, jamais d'écrasement
#     G3  hors corpus            → signalé, non migré
#
#   Mode par défaut : --constater. Il n'écrit RIEN. Même discipline que
#   publier-manifeste-instrument.sh.
#
#   Usage :
#     python3 atelier/rd/outillage/migrer-textes-convertis.py            # constate
#     python3 …/migrer-textes-convertis.py --migrer
#     python3 …/migrer-textes-convertis.py --eprouver-gardes             # §VII
# =============================================================================

import argparse
import hashlib
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from collections import defaultdict
from pathlib import Path

# --- G1 : les motifs de donnée personnelle -----------------------------------
#
#   ⚠ `IBAN` est posé sur BORNE DE MOT. Un premier balayage d'instruction, sans
#   bornes et insensible à la casse, avait signalé « IBAN » dans *Le Roi du
#   Monde* : c'était « Liban ». Un contrôle qui n'est pas éprouvé sur ce qu'il
#   prétend attraper fait porter des soupçons faux.
MOTIFS_PERSONNELS = [
    ("adresse e-mail", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("IBAN",           re.compile(r"\b[A-Z]{2}[0-9]{2}[ ]?[A-Z0-9]{4}[ ]?[A-Z0-9]{4}")),
    ("téléphone FR",   re.compile(r"\b0[1-9](?:[ .-]?[0-9]{2}){4}\b")),
    ("téléphone int.", re.compile(r"\+[0-9]{1,3}[ .-]?(?:[0-9][ .-]?){8,}")),
]

# --- G3 : hors corpus. Liste EXPLICITE, jamais une heuristique. --------------
#
#   Classer automatiquement ce qui est « un texte de source » n'est pas à la
#   portée d'un script : il le devinerait, et devinerait mal. La liste est donc
#   nommée, courte, et chaque entrée porte son motif.
HORS_CORPUS = {
    "Build Your Own Perplexity with Exa.md":
        "article technique (moteur de recherche), sans rapport avec le corpus",
}


def slug(texte, garder_extension=False):
    """Minuscules ASCII, sans accents, tirets (§III du protocole racine).

    Supprime au passage le piège NFD/NFC : les dossiers de `raw/` portent leurs
    noms en Unicode DÉCOMPOSÉ, où un chemin tapé à la main l'est en composé.
    L'accès littéral y échoue sur « No such file or directory » sans rien dire
    de plus — rencontré deux fois le 2026-09-02."""
    ext = ""
    if garder_extension and texte.lower().endswith(".md"):
        texte, ext = texte[:-3], ".md"
    t = unicodedata.normalize("NFKD", texte)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("'", "-").replace("’", "-").replace("&", "-et-")
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-").lower()
    t = re.sub(r"-{2,}", "-", t)
    return (t or "sans-nom") + ext


def empreinte(chemin):
    return hashlib.md5(chemin.read_bytes()).hexdigest()


def controler_personnel(chemin):
    """G1. Rend la liste des motifs trouvés (vide = propre)."""
    try:
        texte = chemin.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ["illisible"]
    return [nom for nom, rx in MOTIFS_PERSONNELS if rx.search(texte)]


def destination(rel):
    """`raw/<Dossier>/<Fichier>.md` → `<dossier-slug>/<fichier-slug>.md`.
    Un fichier à la racine de `raw/` va dans `divers/`."""
    parties = rel.parts
    if len(parties) == 1:
        return Path("divers") / slug(parties[0], True)
    # `Downloads/<Corpus>/<f>.md` : c'est le CORPUS qui nomme, pas `Downloads`.
    utiles = [p for p in parties[:-1] if p.lower() != "downloads"]
    dossier = slug(utiles[-1]) if utiles else "divers"
    return Path(dossier) / slug(parties[-1], True)


def collecter(racine_raw):
    """Enumère, contrôle, dédoublonne. Rend un rapport complet, sans rien écrire."""
    fichiers = sorted(p for p in racine_raw.rglob("*.md") if p.is_file())
    rap = {"total": len(fichiers), "refuses": [], "hors_corpus": [],
           "doublons": [], "a_migrer": [], "collisions": []}

    # G1 et G3 d'abord : ce qui est écarté ne participe pas au dédoublonnage.
    retenus = []
    for f in fichiers:
        if f.name in HORS_CORPUS:
            rap["hors_corpus"].append((f, HORS_CORPUS[f.name]))
            continue
        motifs = controler_personnel(f)
        if motifs:
            rap["refuses"].append((f, motifs))
            continue
        retenus.append(f)

    # Dédoublonnage, sur verdict de Sidy (2026-09-02) : AVANT migration.
    #   Règle de conservation — le verdict dit quoi faire, non lequel garder :
    #   entre deux copies identiques au bit près, on conserve celle qui n'est
    #   PAS sous `Downloads/`, ce dossier étant un dépôt de téléchargement et
    #   non un corpus rangé. À égalité, le premier chemin par ordre
    #   alphabétique — déterministe, donc rejouable.
    par_empreinte = defaultdict(list)
    for f in retenus:
        par_empreinte[empreinte(f)].append(f)

    gardes = []
    for _, groupe in sorted(par_empreinte.items()):
        if len(groupe) == 1:
            gardes.append(groupe[0])
            continue
        hors_dl = [f for f in groupe if "downloads" not in str(f).lower()]
        garde = sorted(hors_dl or groupe, key=lambda p: str(p))[0]
        gardes.append(garde)
        for f in groupe:
            if f != garde:
                rap["doublons"].append((f, garde))

    # G2 : collision de destination. Deux fichiers DIFFÉRENTS sur un même
    # chemin cible — fusionner deux dossiers de même slug est licite, écraser
    # un fichier ne l'est pas.
    par_dest = defaultdict(list)
    for f in sorted(gardes, key=lambda p: str(p)):
        dest = destination(f.relative_to(racine_raw))
        par_dest[dest].append(f)
        rap["a_migrer"].append((f, dest))
    for dest, sources in sorted(par_dest.items()):
        if len(sources) > 1:
            rap["collisions"].append((dest, sources))
    return rap


def imprimer(rap, racine_raw):
    r = lambda p: str(p.relative_to(racine_raw)) if isinstance(p, Path) else str(p)
    print("=" * 92)
    print("PRO-08 — migration des textes convertis : raw/ (masqué) → textes/ (versionné)")
    print("=" * 92)
    print(f"  fichiers .md examinés      : {rap['total']}")
    print(f"  refusés (donnée personnelle): {len(rap['refuses'])}")
    print(f"  hors corpus (non migrés)   : {len(rap['hors_corpus'])}")
    print(f"  doublons écartés           : {len(rap['doublons'])}")
    print(f"  À MIGRER                   : {len(rap['a_migrer'])}")
    somme = (len(rap["refuses"]) + len(rap["hors_corpus"])
             + len(rap["doublons"]) + len(rap["a_migrer"]))
    print(f"  contrôle du compte         : {somme} == {rap['total']} "
          f"{'✓' if somme == rap['total'] else '✗ ÉCART'}")

    if rap["refuses"]:
        print("\n── G1 : REFUSÉS pour donnée personnelle ──")
        for f, motifs in rap["refuses"]:
            print(f"   ✗ {r(f)}  [{', '.join(motifs)}]")
    if rap["hors_corpus"]:
        print("\n── G3 : hors corpus, signalés et non migrés ──")
        for f, motif in rap["hors_corpus"]:
            print(f"   · {r(f)}\n     {motif}")
    if rap["doublons"]:
        print(f"\n── Doublons écartés ({len(rap['doublons'])}) — l'original reste dans raw/ (Cmd 10) ──")
        for f, garde in rap["doublons"][:8]:
            print(f"   · {r(f)}\n     ≡ conservé : {r(garde)}")
        if len(rap["doublons"]) > 8:
            print(f"   … et {len(rap['doublons']) - 8} autres")
    if rap["collisions"]:
        print("\n── G2 : COLLISIONS DE DESTINATION — migration REFUSÉE ──")
        for dest, sources in rap["collisions"]:
            print(f"   ✗ {dest}")
            for s in sources:
                print(f"       ← {r(s)}")
    return not rap["collisions"]


def eprouver(racine_raw):
    """§VII — un contrôle dont on n'a pas vu l'échec n'est pas vérifié.
    Chaque garde reçoit la faute exacte qu'elle doit attraper, dans une COPIE
    jetable ; le dépôt vivant n'est jamais touché."""
    print("=" * 92)
    print("PRO-08 — épreuve des gardes (copie jetable ; raw/ n'est pas touché)")
    print("=" * 92)
    resultats = []
    with tempfile.TemporaryDirectory(prefix="eprouve-pro08-") as tmp:
        bac = Path(tmp) / "raw"
        (bac / "corpus-temoin").mkdir(parents=True)
        (bac / "corpus-temoin" / "a.md").write_text("Texte propre.\n", encoding="utf-8")

        base = collecter(bac)
        ok = (len(base["a_migrer"]) == 1 and not base["refuses"])
        resultats.append(("état sain accepté", ok))

        # G1 — une adresse e-mail doit faire refuser le fichier.
        (bac / "corpus-temoin" / "b.md").write_text(
            "Écrire à quelqu-un@example.org pour la suite.\n", encoding="utf-8")
        r1 = collecter(bac)
        resultats.append(("G1 refuse une adresse e-mail",
                          any("adresse e-mail" in m for _, m in r1["refuses"])))

        # G1 bis — « Liban » ne doit PAS être pris pour un IBAN.
        (bac / "corpus-temoin" / "b.md").write_text(
            "les Druses du Liban, et le Vieux de la Montagne.\n", encoding="utf-8")
        r1b = collecter(bac)
        resultats.append(("G1 ne confond pas « Liban » avec IBAN", not r1b["refuses"]))
        (bac / "corpus-temoin" / "b.md").unlink()

        # G2 — deux fichiers DIFFÉRENTS sur une même destination.
        (bac / "Corpus Témoin").mkdir()
        (bac / "Corpus Témoin" / "A.md").write_text("Autre contenu.\n", encoding="utf-8")
        r2 = collecter(bac)
        resultats.append(("G2 refuse une collision de destination", bool(r2["collisions"])))
        shutil.rmtree(bac / "Corpus Témoin")

        # G3 — le fichier hors corpus est écarté, nommé, non migré.
        nom = next(iter(HORS_CORPUS))
        (bac / "corpus-temoin" / nom).write_text("hors sujet\n", encoding="utf-8")
        r3 = collecter(bac)
        resultats.append(("G3 écarte le fichier hors corpus", len(r3["hors_corpus"]) == 1))
        (bac / "corpus-temoin" / nom).unlink()

        # Dédoublonnage — la copie sous Downloads/ est celle qu'on écarte.
        (bac / "Downloads").mkdir()
        (bac / "Downloads" / "a.md").write_text("Texte propre.\n", encoding="utf-8")
        r4 = collecter(bac)
        garde_hors_dl = (len(r4["doublons"]) == 1
                         and "downloads" in str(r4["doublons"][0][0]).lower()
                         and "downloads" not in str(r4["doublons"][0][1]).lower())
        resultats.append(("dédoublonnage : conserve la copie hors Downloads/", garde_hors_dl))

    print()
    for nom, ok in resultats:
        print("  {}  {}".format("OK  " if ok else "ÉCHEC", nom))
    tout = all(ok for _, ok in resultats)
    print("\n" + "=" * 92)
    print("VERDICT : les gardes observent quelque chose de réel." if tout
          else "VERDICT : garde(s) INOPÉRANTE(S) — elles n'attrapent pas ce qu'elles gardent.")
    print("=" * 92)
    return 0 if tout else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/root/wiki")
    ap.add_argument("--migrer", action="store_true", help="copie réellement (défaut : constate)")
    ap.add_argument("--eprouver-gardes", action="store_true")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    raw, textes = repo / "raw", repo / "textes"

    if args.eprouver_gardes:
        return eprouver(raw)

    rap = collecter(raw)
    sain = imprimer(rap, raw)
    if not sain:
        print("\nMigration REFUSÉE : résoudre les collisions d'abord.")
        return 1
    if not args.migrer:
        print("\n(constat seul — relancer avec --migrer pour copier)")
        return 0

    for src, dest in rap["a_migrer"]:
        cible = textes / dest
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, cible)          # COPIE : `raw/` demeure intact (Cmd 10)
    print(f"\n✓ {len(rap['a_migrer'])} fichier(s) copié(s) vers {textes}")
    print("  raw/ est inchangé — copie, jamais déplacement (Cmd 10).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
