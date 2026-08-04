#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
carte-du-depot.py — Cartographie mécanique du dépôt (artefact dérivé).

OBJET
    Produire une carte factuelle et compacte de l'état réel du dépôt, destinée
    à être déposée comme fichier de projet côté session de conception
    (claude.ai), afin de supprimer les angles morts : slugs inconnus, tags
    orphelins, correspondances manquées faute de visibilité sur ce qui existe.

PRINCIPES (non négociables)
    1. DÉTERMINISTE. Bibliothèque standard seule. Aucun LLM, aucun réseau,
       aucune dépendance externe. Deux exécutions sur un même arbre produisent
       un octet-pour-octet identique (hors horodatage d'en-tête).
    2. LECTURE SEULE sur les circuits. Le script n'écrit QUE son fichier de
       sortie. Il ne modifie, ne déplace, ne supprime rien.
    3. AUCUN JUGEMENT. Le script recopie et compte ; il ne résume pas, ne
       qualifie pas, n'interprète pas. Les en-têtes de section sont reproduits
       littéralement, jamais synthétisés.
    4. ARTEFACT DÉRIVÉ. Le dépôt fait foi. En cas de divergence entre la carte
       et le dépôt, c'est la carte qui a tort. Elle est régénérable à volonté
       et ne doit jamais être éditée à la main.
    5. HORS CORPS DOCTRINAL. Sortie en `meta/`, jamais dans `doctrinal/`.

USAGE
    python3 carte-du-depot.py
    python3 carte-du-depot.py --repo /root/wiki --sortie meta/carte-du-depot.md
    python3 carte-du-depot.py --par-circuit        # un fichier par circuit
    python3 carte-du-depot.py --max-titres 12      # plafond d'en-têtes H2/fiche

SORTIE
    Un fichier Markdown (ou un par circuit avec --par-circuit), structuré en
    sections : inventaire par circuit, index des tags, index des en-têtes,
    discernements ouverts, marqueurs to-source, liens morts, fiches orphelines,
    statistiques.

CE QUE LE SCRIPT NE FAIT PAS
    Il ne vérifie aucun invariant structurel : c'est le rôle de
    `verifier-invariants.py`, qui reste seul juge de paix. La carte décrit,
    le linter contrôle. Les deux sont indépendants.
"""

import argparse
import os
import re
import sys
from collections import defaultdict, Counter
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Circuits parcourus, dans l'ordre d'affichage.
CIRCUITS = ["doctrinal", "hermeneutique", "atelier", "label", "meta"]

# Répertoires jamais parcourus, quel que soit leur emplacement.
EXCLUS = {".git", ".obsidian", "_inbox", "raw", "node_modules", "__pycache__",
          ".trash", ".venv"}

# Clés de frontmatter reproduites dans l'inventaire.
CLES_INVENTAIRE = ["title", "type", "status", "tradition_cadre", "created",
                   "updated", "sources_count"]

# ---------------------------------------------------------------------------
# Lecture et analyse
# ---------------------------------------------------------------------------


def lire(chemin):
    """Lit un fichier en UTF-8, tolérant aux octets invalides."""
    try:
        with open(chemin, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError as e:
        return None if e else None


def separer_frontmatter(texte):
    """
    Sépare le frontmatter YAML du corps.
    Retourne (dict_frontmatter, corps, frontmatter_present: bool).
    Parseur volontairement minimal : clés scalaires et listes inline `[...]`,
    ce qui couvre le Sceau Recteur. Toute autre construction est ignorée
    plutôt qu'interprétée.
    """
    if not texte.startswith("---"):
        return {}, texte, False
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}, texte, False
    bloc = texte[3:fin]
    corps = texte[fin + 4:]
    fm = {}
    for ligne in bloc.splitlines():
        ligne = ligne.rstrip()
        if not ligne or ligne.lstrip().startswith("#"):
            continue
        if ligne.startswith(" ") or ligne.startswith("\t"):
            continue  # continuation / bloc imbriqué : non interprété
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_\-]*)\s*:\s*(.*)$', ligne)
        if not m:
            continue
        cle, val = m.group(1), m.group(2).strip()
        fm[cle] = val
    return fm, corps, True


def valeur_nue(v):
    """Retire guillemets encadrants d'une valeur scalaire."""
    if v is None:
        return ""
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def liste_inline(v):
    """Extrait les éléments d'une liste YAML inline `[a, b, c]`."""
    if not v:
        return []
    v = v.strip()
    if not (v.startswith("[") and v.endswith("]")):
        return []
    interieur = v[1:-1].strip()
    if not interieur:
        return []
    # découpe sur les virgules hors crochets
    elements, courant, profondeur = [], "", 0
    for c in interieur:
        if c == "[":
            profondeur += 1
        elif c == "]":
            profondeur -= 1
        if c == "," and profondeur == 0:
            elements.append(courant)
            courant = ""
        else:
            courant += c
    if courant.strip():
        elements.append(courant)
    return [valeur_nue(e) for e in elements if valeur_nue(e)]


RE_WIKILINK = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]')
RE_H2 = re.compile(r'^##\s+(?!#)(.+?)\s*$', re.MULTILINE)
RE_DISCERNEMENT_STATUT = re.compile(
    r'\*\*Statut\*\*\s*:\s*([^\n\r|]+)', re.IGNORECASE)


def analyser_fiche(racine, chemin_abs):
    """Retourne un dict décrivant une fiche, sans aucun jugement."""
    rel = os.path.relpath(chemin_abs, racine).replace(os.sep, "/")
    slug = rel[:-3] if rel.endswith(".md") else rel
    texte = lire(chemin_abs)
    if texte is None:
        return None
    fm, corps, fm_present = separer_frontmatter(texte)

    tags = liste_inline(fm.get("tags", ""))
    sources = liste_inline(fm.get("sources", ""))
    cross = liste_inline(fm.get("cross_links", ""))
    links = liste_inline(fm.get("links", ""))

    # wikilinks du corps (hors frontmatter)
    cibles_corps = [c.strip() for c in RE_WIKILINK.findall(corps)]
    # wikilinks déclarés en frontmatter
    cibles_fm = []
    for brut in sources + cross + links:
        cibles_fm.extend(c.strip() for c in RE_WIKILINK.findall(brut))

    titres = [t.strip() for t in RE_H2.findall(corps)]

    to_source = []
    if "to-source" in " ".join(sources).lower():
        to_source.append("frontmatter sources: to-source")
    for i, ligne in enumerate(corps.splitlines(), start=1):
        if "to-source" in ligne.lower() or "to_source" in ligne.lower():
            extrait = ligne.strip()
            if len(extrait) > 160:
                extrait = extrait[:157] + "..."
            to_source.append("L%d : %s" % (i, extrait))

    statut_discernement = ""
    if valeur_nue(fm.get("type", "")) == "discernement":
        m = RE_DISCERNEMENT_STATUT.search(corps)
        if m:
            statut_discernement = m.group(1).strip()

    return {
        "slug": slug,
        "circuit": rel.split("/", 1)[0] if "/" in rel else "(racine)",
        "fm": fm,
        "fm_present": fm_present,
        "tags": tags,
        "titres": titres,
        "cibles": cibles_corps + cibles_fm,
        "cibles_corps": cibles_corps,
        "to_source": to_source,
        "statut_discernement": statut_discernement,
        "octets": len(texte.encode("utf-8")),
        "lignes": texte.count("\n") + 1,
    }


def parcourir(racine):
    """
    Parcourt les circuits et retourne la liste des fiches analysées.
    Les cartes déjà générées (tag `genere`) sont exclues : sans quoi le script
    s'inventorierait lui-même, faussant compteurs, tags et `to-source`.
    """
    fiches = []
    for circuit in CIRCUITS:
        base = os.path.join(racine, circuit)
        if not os.path.isdir(base):
            continue
        for dossier, sousdossiers, fichiers in os.walk(base):
            sousdossiers[:] = sorted(
                d for d in sousdossiers if d not in EXCLUS and not d.startswith("."))
            for nom in sorted(fichiers):
                if not nom.endswith(".md"):
                    continue
                f = analyser_fiche(racine, os.path.join(dossier, nom))
                if f is None:
                    continue
                if "genere" in f["tags"]:
                    continue  # carte produite par ce script : jamais inventoriée
                fiches.append(f)
    return fiches


# ---------------------------------------------------------------------------
# Rendu
# ---------------------------------------------------------------------------


def echapper_pipe(s):
    return s.replace("|", "\\|")


def tronquer(s, n):
    s = s.strip()
    return s if len(s) <= n else s[:n - 1] + "…"


def rendre_entete(racine, nb_fiches, portee):
    horodatage = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return """---
title: "Carte du dépôt — inventaire mécanique{suffixe}"
type: meta
tags: [outillage, carte, derive, genere]
created: {date}
updated: {date}
sources: []
links: []
---

# Carte du dépôt — inventaire mécanique{suffixe}

> **ARTEFACT DÉRIVÉ — NE JAMAIS ÉDITER À LA MAIN.**
> Généré par `carte-du-depot.py` (script déterministe, stdlib seule, aucun LLM,
> aucun réseau) le {horodatage}, sur `{racine}`.
> Portée : {portee}. {nb} fiches parcourues.
>
> **Le dépôt fait foi.** En cas de divergence entre cette carte et les fichiers
> réels, c'est la carte qui a tort : la régénérer. Elle décrit, elle ne
> contrôle pas — les invariants structurels relèvent de
> `verifier-invariants.py`, seul juge de paix.
>
> Aucun contenu de ce fichier n'est le produit d'un jugement : les titres, les
> en-têtes et les statuts sont reproduits littéralement depuis les fiches.

""".format(date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
           horodatage=horodatage, racine=racine, nb=nb_fiches,
           portee=portee, suffixe="")


def rendre_inventaire(fiches):
    out = ["## I. Inventaire par circuit\n"]
    par_circuit = defaultdict(list)
    for f in fiches:
        par_circuit[f["circuit"]].append(f)
    for circuit in CIRCUITS:
        lot = par_circuit.get(circuit)
        if not lot:
            continue
        out.append("### `%s/` — %d fiches\n" % (circuit, len(lot)))
        out.append("| slug | type | status | updated | src | title |")
        out.append("|---|---|---|---|---|---|")
        for f in sorted(lot, key=lambda x: x["slug"]):
            fm = f["fm"]
            out.append("| `%s` | %s | %s | %s | %s | %s |" % (
                f["slug"],
                valeur_nue(fm.get("type", "—")) or "—",
                valeur_nue(fm.get("status", "—")) or "—",
                valeur_nue(fm.get("updated", "—")) or "—",
                valeur_nue(fm.get("sources_count", "—")) or "—",
                echapper_pipe(tronquer(valeur_nue(fm.get("title", "(sans titre)")), 90)),
            ))
        out.append("")
    return "\n".join(out)


def rendre_tags(fiches):
    out = ["## II. Index des tags\n",
           "*Matériau brut des correspondances : un même tag porté par des fiches "
           "de circuits ou de domaines différents signale un rapprochement possible "
           "que nul n'a encore instruit.*\n"]
    index = defaultdict(list)
    for f in fiches:
        for t in f["tags"]:
            index[t].append(f["slug"])
    if not index:
        out.append("*(aucun tag relevé)*\n")
        return "\n".join(out)
    out.append("| tag | n | fiches |")
    out.append("|---|---|---|")
    for tag in sorted(index, key=lambda t: (-len(index[t]), t)):
        slugs = sorted(index[tag])
        rendu = ", ".join("`%s`" % s for s in slugs)
        if len(rendu) > 400:
            rendu = ", ".join("`%s`" % s for s in slugs[:8]) + \
                    ", … (+%d)" % (len(slugs) - 8)
        out.append("| `%s` | %d | %s |" % (echapper_pipe(tag), len(slugs), rendu))
    out.append("")
    return "\n".join(out)


def rendre_titres(fiches, max_titres):
    out = ["## III. Index des en-têtes de section (H2)\n",
           "*Reproduits littéralement. Donne le contenu réel de chaque fiche sans "
           "passer par un résumé.*\n"]
    for f in sorted(fiches, key=lambda x: x["slug"]):
        if not f["titres"]:
            continue
        titres = f["titres"]
        suffixe = ""
        if max_titres and len(titres) > max_titres:
            suffixe = " … (+%d)" % (len(titres) - max_titres)
            titres = titres[:max_titres]
        out.append("- `%s` — %s%s" % (
            f["slug"],
            " · ".join(tronquer(t, 70) for t in titres),
            suffixe))
    out.append("")
    return "\n".join(out)


def rendre_discernements(fiches):
    out = ["## IV. Discernements\n",
           "*Statut recopié depuis le bloc 🔍 de chaque fiche. Le verdict "
           "appartient à l'humain (Cmd 12) ; ce tableau ne fait que l'afficher.*\n"]
    lot = [f for f in fiches if valeur_nue(f["fm"].get("type", "")) == "discernement"]
    if not lot:
        out.append("*(aucune fiche `type: discernement`)*\n")
        return "\n".join(out)
    out.append("| slug | status (fm) | statut du bloc 🔍 | created | updated |")
    out.append("|---|---|---|---|---|")
    for f in sorted(lot, key=lambda x: x["slug"]):
        fm = f["fm"]
        out.append("| `%s` | %s | %s | %s | %s |" % (
            f["slug"],
            valeur_nue(fm.get("status", "—")) or "—",
            echapper_pipe(tronquer(f["statut_discernement"] or "—", 40)),
            valeur_nue(fm.get("created", "—")) or "—",
            valeur_nue(fm.get("updated", "—")) or "—",
        ))
    out.append("")
    return "\n".join(out)


def rendre_to_source(fiches):
    out = ["## V. Marqueurs `to-source` en attente\n",
           "*Chaque ligne est une affirmation non encore vérifiée sur source "
           "primaire (Cmd 5). Leur levée est humaine et manuelle.*\n"]
    total = 0
    corps = []
    for f in sorted(fiches, key=lambda x: x["slug"]):
        if not f["to_source"]:
            continue
        corps.append("- `%s` (%d)" % (f["slug"], len(f["to_source"])))
        for item in f["to_source"][:6]:
            corps.append("  - %s" % tronquer(item, 150))
        if len(f["to_source"]) > 6:
            corps.append("  - … (+%d)" % (len(f["to_source"]) - 6))
        total += len(f["to_source"])
    if not corps:
        out.append("*(aucun marqueur relevé)*\n")
        return "\n".join(out)
    out.append("**Total : %d marqueurs sur %d fiches.**\n" %
               (total, len([f for f in fiches if f["to_source"]])))
    out.extend(corps)
    out.append("")
    return "\n".join(out)


def rendre_liens(fiches):
    out = ["## VI. Liens morts et fiches orphelines\n",
           "*Signalement brut. Un lien mort peut être une coquille de slug ou une "
           "fiche annoncée mais non déposée — le script ne tranche pas.*\n"]
    connus = {f["slug"] for f in fiches}
    # index par nom court, pour repérer les liens non préfixés du chemin
    par_nom = defaultdict(list)
    for s in connus:
        par_nom[s.rsplit("/", 1)[-1]].append(s)

    morts = defaultdict(list)
    entrants = Counter()
    for f in fiches:
        for cible in f["cibles"]:
            c = cible.strip().rstrip("/")
            if c in connus:
                entrants[c] += 1
            elif c in par_nom and len(par_nom[c]) == 1:
                entrants[par_nom[c][0]] += 1  # lien par nom court, résolvable
            else:
                morts[f["slug"]].append(c)

    if morts:
        out.append("### Liens non résolus\n")
        for slug in sorted(morts):
            cibles = sorted(set(morts[slug]))
            out.append("- `%s` → %s" % (
                slug, ", ".join("`%s`" % tronquer(c, 60) for c in cibles[:10])
                + (" … (+%d)" % (len(cibles) - 10) if len(cibles) > 10 else "")))
        out.append("")
    else:
        out.append("### Liens non résolus\n\n*(aucun)*\n")

    orphelines = sorted(s for s in connus
                        if entrants[s] == 0 and not s.endswith("/index")
                        and not s.endswith("/annales"))
    out.append("### Fiches sans lien entrant (%d)\n" % len(orphelines))
    if orphelines:
        for s in orphelines:
            out.append("- `%s`" % s)
    else:
        out.append("*(aucune)*")
    out.append("")
    return "\n".join(out)


def rendre_stats(fiches):
    out = ["## VII. Statistiques\n"]
    par_circuit = Counter(f["circuit"] for f in fiches)
    par_type = Counter(valeur_nue(f["fm"].get("type", "(absent)")) or "(absent)"
                       for f in fiches)
    par_status = Counter(valeur_nue(f["fm"].get("status", "(absent)")) or "(absent)"
                         for f in fiches)
    sans_fm = [f["slug"] for f in fiches if not f["fm_present"]]

    out.append("| circuit | fiches |")
    out.append("|---|---|")
    for c in CIRCUITS:
        if par_circuit.get(c):
            out.append("| `%s/` | %d |" % (c, par_circuit[c]))
    out.append("| **total** | **%d** |" % len(fiches))
    out.append("")

    out.append("| type | n |")
    out.append("|---|---|")
    for t, n in sorted(par_type.items(), key=lambda kv: (-kv[1], kv[0])):
        out.append("| `%s` | %d |" % (echapper_pipe(t), n))
    out.append("")

    out.append("| status | n |")
    out.append("|---|---|")
    for s, n in sorted(par_status.items(), key=lambda kv: (-kv[1], kv[0])):
        out.append("| `%s` | %d |" % (echapper_pipe(s), n))
    out.append("")

    if sans_fm:
        out.append("**Fiches sans frontmatter (%d)** — signalement, "
                   "aucune correction :\n" % len(sans_fm))
        for s in sans_fm:
            out.append("- `%s`" % s)
        out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Entrée
# ---------------------------------------------------------------------------


def construire(fiches, racine, portee, max_titres):
    parties = [
        rendre_entete(racine, len(fiches), portee),
        rendre_inventaire(fiches),
        rendre_tags(fiches),
        rendre_titres(fiches, max_titres),
        rendre_discernements(fiches),
        rendre_to_source(fiches),
        rendre_liens(fiches),
        rendre_stats(fiches),
        "---\n\n*Fin de la carte. Régénérer par "
        "`python3 carte-du-depot.py` après toute intégration.*\n",
    ]
    return "\n".join(parties)


def main():
    p = argparse.ArgumentParser(
        description="Cartographie mécanique du dépôt (artefact dérivé, lecture seule).")
    p.add_argument("--repo", default=".", help="racine du dépôt (défaut : .)")
    p.add_argument("--sortie", default="meta/carte-du-depot.md",
                   help="chemin du fichier de sortie, relatif à --repo")
    p.add_argument("--par-circuit", action="store_true",
                   help="un fichier par circuit, suffixé par le nom du circuit")
    p.add_argument("--max-titres", type=int, default=15,
                   help="plafond d'en-têtes H2 listés par fiche (0 = illimité)")
    args = p.parse_args()

    racine = os.path.abspath(args.repo)
    if not os.path.isdir(racine):
        sys.stderr.write("Erreur : %s n'est pas un répertoire.\n" % racine)
        return 2

    fiches = parcourir(racine)
    if not fiches:
        sys.stderr.write(
            "Aucune fiche trouvée. Circuits attendus : %s\n" % ", ".join(CIRCUITS))
        return 1

    ecrits = []
    if args.par_circuit:
        base, ext = os.path.splitext(args.sortie)
        par_circuit = defaultdict(list)
        for f in fiches:
            par_circuit[f["circuit"]].append(f)
        for circuit in CIRCUITS:
            lot = par_circuit.get(circuit)
            if not lot:
                continue
            chemin = os.path.join(racine, "%s-%s%s" % (base, circuit, ext))
            os.makedirs(os.path.dirname(chemin), exist_ok=True)
            with open(chemin, "w", encoding="utf-8") as fh:
                fh.write(construire(lot, racine, "circuit `%s/`" % circuit,
                                    args.max_titres))
            ecrits.append((chemin, len(lot)))
    else:
        chemin = os.path.join(racine, args.sortie)
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, "w", encoding="utf-8") as fh:
            fh.write(construire(fiches, racine, "dépôt complet", args.max_titres))
        ecrits.append((chemin, len(fiches)))

    for chemin, n in ecrits:
        taille = os.path.getsize(chemin)
        print("Écrit : %s (%d fiches, %d octets)" % (chemin, n, taille))
    print("Rappel : artefact dérivé. Le dépôt fait foi. "
          "Les invariants relèvent de verifier-invariants.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
