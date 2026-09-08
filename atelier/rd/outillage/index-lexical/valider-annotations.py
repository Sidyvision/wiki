#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validateur de la convention d'annotation HTML (CLAUDE.md, §VII).

Le HTML ne porte jamais l'existence d'un lien, seulement son typage. Ce
validateur garde cette regle : il refuse toute annotation que le graphe ne
verrait pas deja par ailleurs.

Trois refus, chacun eprouve en bac a sable avant d'etre cru (§VII, Epreuve
des controles) :

  D1  annotation non appariee — un `data-terme` / `data-nom` qui ne figure
      ni dans les `tags:` de la fiche, ni comme cible d'un wikilink qu'elle
      porte. Sans appariement, le HTML deviendrait porteur : refus.
  D2  Unicode invisible dans une annotation — U+200B/200C/200D/FEFF/200E/200F.
      Premier outillage mecanique du Cmd 15. PORTEE : les attributs `data-`
      et le balisage d'annotation SEULEMENT, non le depot entier.
  D3  plancher de non-vacuite — un terme annote qui ne produit aucune entree
      dans l'index. C'est la lecon de `glossaire-unifie.md` : un index vide
      n'est pas un index vert.

Et un controle de vocabulaire : la convention est CLOSE a trois elements.

Aucun LLM dans la boucle. Lecture seule : ce script n'ecrit jamais.
"""
import argparse, importlib.util, json, re, sys, unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent


def _generateur():
    """Le generateur porte la definition de « matiere du depot ».

    On l'importe plutot que de la recopier : deux definitions qui
    divergent, c'est le controle qui ment sans se plaindre.
    """
    sys.dont_write_bytecode = True  # pas de __pycache__ dans le depot
    s = importlib.util.spec_from_file_location(
        "gen_index_lexical", ICI / "generer-index-lexical.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m

VERSION = "1.0"
ELEMENTS_CLOS = ("dfn", "span", "abbr")
# Vocabulaire clos. Etendu le 2026-09-08 sur verdict de Sidy : les quatre
# genres d'origine ne savaient typer ni les ecoles (darsana), ni les cycles,
# ni les principes metaphysiques — trois categories massives de doctrinal/.
GENRES_CLOS = {"autorite", "lieu", "ouvrage", "entite",
               "ecole", "cycle", "principe"}
# Cmd 15 : ce detecteur NOMME les points de code, il ne les porte pas.
# Les ecrire litteralement ici ferait du garde-fou lui-meme une infraction —
# c'est le controle qui l'a trouve sur sa propre premiere version.
INVISIBLES = {"\u200b": "U+200B", "\u200c": "U+200C", "\u200d": "U+200D",
              "\ufeff": "U+FEFF", "\u200e": "U+200E", "\u200f": "U+200F"}

RE_BALISE = re.compile(r"<(dfn|span|abbr)\b([^>]*)>", re.IGNORECASE)
RE_ATTR = re.compile(r'([a-zA-Z-]+)\s*=\s*"([^"]*)"')
RE_WL = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]")
RE_FM = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
RE_TAGS = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.MULTILINE)


def normaliser(txt: str) -> str:
    """Repli NFD : meme forme normalisee que le generateur."""
    d = unicodedata.normalize("NFD", txt)
    d = "".join(c for c in d if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9-]+", "", d.lower().replace("_", "-"))


def lire(f: Path):
    texte = f.read_text(encoding="utf-8")
    m = RE_FM.match(texte)
    fm, corps = (m.group(1), texte[m.end():]) if m else ("", texte)
    mt = RE_TAGS.search(fm)
    tags = set()
    if mt:
        tags = {normaliser(t.strip().strip('"\'')) for t in mt.group(1).split(",")}
    liens = {normaliser(Path(x.strip()).name) for x in RE_WL.findall(texte)}
    return texte, corps, {k for k in (tags | liens) if k}


def valider(racine: Path, chemin_index: Path):
    anomalies, annotes, n_fiches, n_annot = [], set(), 0, 0

    suivis = _generateur().fichiers_suivis(racine)
    if suivis is None:
        print("  git indisponible : parcours integral.", file=sys.stderr)

    for f in sorted(racine.rglob("*.md")):
        rel = str(f.relative_to(racine))
        if rel.startswith(("textes/", "raw/", "_inbox/")):
            continue
        # Un arbre ignore par git (.graphify-venv/, graphify-out/) n'est pas
        # matiere : le valider donnerait un vert sur ce que personne ne clone.
        if suivis is not None and rel not in suivis:
            continue
        texte, corps, apparies = lire(f)
        balises = list(RE_BALISE.finditer(corps))
        if not balises:
            continue
        n_fiches += 1
        for b in balises:
            n_annot += 1
            elem, brut = b.group(1).lower(), b.group(2)
            attrs = dict(RE_ATTR.findall(brut))

            # D2 — Unicode invisible dans l'annotation (portee : le balisage)
            for ch, nom in INVISIBLES.items():
                if ch in b.group(0):
                    anomalies.append(("D2", rel, "%s dans l'annotation %r"
                                      % (nom, b.group(0)[:60])))

            # vocabulaire clos
            if elem not in ELEMENTS_CLOS:
                anomalies.append(("VOC", rel, "element `%s` hors convention" % elem))
                continue
            if elem == "abbr":
                if not attrs.get("title"):
                    anomalies.append(("VOC", rel, "<abbr> sans title"))
                continue

            cle = attrs.get("data-terme") or attrs.get("data-nom")
            if elem == "span" and "data-nom" not in attrs:
                continue                      # span ordinaire, hors convention
            if elem == "dfn" and "data-terme" not in attrs:
                anomalies.append(("VOC", rel, "<dfn> sans data-terme")); continue
            if elem == "dfn" and not attrs.get("data-tradition"):
                anomalies.append(("VOC", rel, "<dfn data-terme=%r> sans data-tradition" % cle))
            if "data-nom" in attrs:
                g = attrs.get("data-genre")
                if g not in GENRES_CLOS:
                    anomalies.append(("VOC", rel, "data-genre=%r hors vocabulaire clos" % g))

            # D1 — appariement
            if normaliser(cle or "") not in apparies:
                anomalies.append(("D1", rel,
                    "%r n'est ni un tag ni la cible d'un wikilink de la fiche" % cle))
            else:
                annotes.add(normaliser(cle))

    # D3 — plancher de non-vacuite
    if not chemin_index.exists():
        anomalies.append(("D3", str(chemin_index), "index absent"))
    else:
        data = json.loads(chemin_index.read_text(encoding="utf-8"))
        termes = data.get("termes", {})
        if not termes:
            anomalies.append(("D3", str(chemin_index), "l'index ne contient aucun terme"))
        for cle in sorted(annotes):
            e = termes.get(cle)
            if e is None:
                anomalies.append(("D3", str(chemin_index),
                    "le terme annote %r ne produit aucune entree dans l'index" % cle))
            elif "annotation" not in e.get("roles", []):
                # Le trou du glossaire : l'entree existe (par `tag`), mais la
                # recolte d'annotation n'a rien mordu. Vert en apparence,
                # aveugle en fait.
                anomalies.append(("D3", str(chemin_index),
                    "le terme %r est indexe mais sans role `annotation` : "
                    "la recolte n'a pas vu le HTML" % cle))

    return anomalies, n_fiches, n_annot


def main():
    ap = argparse.ArgumentParser(description="Validateur des annotations HTML.")
    ap.add_argument("--racine", default="/root/wiki")
    ap.add_argument("--index", default=None)
    a = ap.parse_args()
    racine = Path(a.racine).resolve()
    idx = Path(a.index) if a.index else (
        racine / "atelier/rd/outillage/index-lexical/index-lexical.json")

    anomalies, n_fiches, n_annot = valider(racine, idx)
    print("valider-annotations v%s — %d fiches annotees, %d annotations."
          % (VERSION, n_fiches, n_annot))
    if not anomalies:
        print("OK — aucune anomalie.")
        return 0
    for code, ou, quoi in anomalies:
        print("REFUS %s | %s | %s" % (code, ou, quoi), file=sys.stderr)
    print("%d anomalie(s)." % len(anomalies), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
