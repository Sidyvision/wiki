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
  D4  placement interdit — annotation posee dans un wikilink ou dans un
      titre (H1..H6). Ratifie au protocole le 2026-09-08 (CLAUDE.md SVII,
      regles de placement des annotations).
      LE CODE N'EST PAS UN CAS DE D4 : il est masque AVANT la recherche des
      balises, de sorte qu'une balise dans du code n'est jamais lue comme une
      annotation — ce qui est la semantique juste. Une branche D4 « dans du
      code » a d'abord ete ecrite, puis RETIREE le 2026-09-08 : le masquage
      amont la rendait inatteignable, et un controle qui ne peut pas se
      declencher est la forme muette meme que le SVII interdit.
  D6  genre hors de son circuit — un `data-genre` valide en soi mais pose la
      ou son circuit ne l'admet pas (`oeuvre` dans doctrinal/, `dispositif`
      dans atelier/). Ouvert le 2026-09-09 avec le vocabulaire propre a
      `hermeneutique/`.
  D5  occurrence unique — le meme terme annote deux fois dans la meme fiche.
      L'annotation type le terme, elle ne le compte pas : la seconde pose
      n'apprend rien et double le poids du terme a la lecture machine.

Et un controle de vocabulaire : la convention est CLOSE a trois elements.

SIGNALEMENTS (non bloquants — le script sort 0)
-----------------------------------------------
  S1  doublon de referent possible — deux cles coannotees dans une meme fiche
      dont l'une est COMPOSANT de l'autre : `burckhardt` et `titus-burckhardt`
      designent la meme personne sous deux cles, et D5 ne le voit pas, car il
      compte par CLE et jamais par REFERENT.
      C'est un SIGNALEMENT et non un refus, parce que la meme forme couvre un
      rapport parfaitement legitime : `yuga` et `kali-yuga` sont un genre et
      une espece, non un doublon. Distinguer les deux est un JUGEMENT, reserve
      a Sidy (Cmd 12) — le controle montre la paire, il ne tranche pas.

Aucun LLM dans la boucle. Lecture seule : ce script n'ecrit jamais.
"""
import argparse, importlib.util, json, re, sys, unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent


def _invariants():
    """Le controleur racine porte la definition CANONIQUE de « circuit ».

    On l'importe plutot que d'ecrire ici une seconde regle chemin -> circuit :
    deux resolveurs qui divergent, c'est le controle qui ment sans se plaindre
    (meme motif que le partage de `est_ecriture_originale` et de
    `fichiers_suivis`).
    """
    sys.dont_write_bytecode = True
    chemin = ICI.parents[3] / "verifier-invariants.py"
    if not chemin.is_file():
        sys.exit("REFUS — controleur racine introuvable : %s" % chemin)
    s = importlib.util.spec_from_file_location("_invariants", chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


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

VERSION = "1.3"
INV = None
ELEMENTS_CLOS = ("dfn", "span", "abbr")
# Vocabulaire clos. Etendu le 2026-09-08 sur verdict de Sidy : les quatre
# genres d'origine ne savaient typer ni les ecoles (darsana), ni les cycles,
# ni les principes metaphysiques — trois categories massives de doctrinal/.
GENRES_CLOS = {"autorite", "lieu", "ouvrage", "entite",
               "ecole", "cycle", "principe"}

# --- Vocabulaire propre a `hermeneutique/` (etendu le 2026-09-09, verdict Sidy)
# Les sept genres ci-dessus ne savaient nommer ni une oeuvre profane, ni un
# personnage, ni un dispositif d'oeuvre. Plutot que d'inventer des mots, on
# reprend EXACTEMENT le vocabulaire `type:` que `hermeneutique/CLAUDE.md`
# declare deja — il porte sa garde Cmd 3 avec lui :
#   `oeuvre`     — une oeuvre ou une saga (JAMAIS `ouvrage`, reserve au traite
#                  traditionnel : ne pas fondre les deux registres est le fond
#                  meme du Cmd 3) ;
#   `auteur`     — createur reel. Emprunte la FORME de `autorite` sans en
#                  partager la fonction : aucun statut d'autorite confere ni
#                  suppose (hermeneutique/CLAUDE.md) ;
#   `figure`     — personnage, ou entite non personnelle fonctionnant comme tel ;
#   `dispositif` — lieu, vaisseau, appareil, systeme, interface ou institution
#                  de l'oeuvre, tenu pour support operatoire de sa these ;
#   `concept`    — notion propre a l'oeuvre.
# `entite` reste ADMIS ici : une fiche du circuit cite legitimement une entite
# recue en meme temps qu'une figure de fiction, et c'est meme son sujet. La
# distinction entre les deux est un JUGEMENT, reserve a Sidy (Cmd 12) — la
# garde ne la tranche pas, elle ouvre les deux mots.
#   `categorie-editoriale` — la categorie de PUBLICATION ou de CLASSEMENT sous
#                  laquelle une oeuvre parait ou se range : shonen, seinen,
#                  thriller, gothique, comedie, roman. Ajoute le 2026-09-09 sur
#                  verdict de Sidy, et c'est le SEUL mot de ce vocabulaire qui
#                  ne vienne pas du champ `type:` du circuit — il est donc le
#                  seul a devoir porter sa limite dans son nom. Il la porte :
#                  « editoriale » dit que la categorie est celle du marche du
#                  livre et de l'edition, jamais une categorie de connaissance.
#                  Un shonen n'est pas une ecole, et le confondre serait
#                  exactement la faute de categorie que le Cmd 3 poursuit.
#                  NE COUVRE PAS : un metier (`mangaka`), une structure de
#                  production (un studio, un editeur), ni `saga`, que ce
#                  protocole traite deja comme une regle de fiche-hub.
GENRES_HERMENEUTIQUE = {"oeuvre", "auteur", "figure", "dispositif", "concept",
                        "categorie-editoriale"}

# Genres admis par circuit. Un genre VALIDE mais POSE DANS LE MAUVAIS CIRCUIT
# est refuse (D6) : c'est la seule face nouvelle de ce controle, l'inconnu
# etant deja refuse par VOC.
def genres_admis(circuit):
    if circuit == "hermeneutique":
        return GENRES_CLOS | GENRES_HERMENEUTIQUE
    return GENRES_CLOS
# Cmd 15 : ce detecteur NOMME les points de code, il ne les porte pas.
# Les ecrire litteralement ici ferait du garde-fou lui-meme une infraction —
# c'est le controle qui l'a trouve sur sa propre premiere version.
INVISIBLES = {"\u200b": "U+200B", "\u200c": "U+200C", "\u200d": "U+200D",
              "\ufeff": "U+FEFF", "\u200e": "U+200E", "\u200f": "U+200F"}

RE_BALISE = re.compile(r"<(dfn|span|abbr)\b([^>]*)>", re.IGNORECASE)
RE_ATTR = re.compile(r'([a-zA-Z-]+)\s*=\s*"([^"]*)"')
RE_WL = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]")
RE_FM = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
# Wikilink COMPLET (avec ses crochets) : D4 teste un chevauchement de spans,
# la un simple test d'appartenance ne suffirait pas.
RE_WL_SPAN = re.compile(r"\[\[[^\]]*\]\]")
# Titre markdown, en debut de ligne. Le `title:`/H1 est le site canonique de
# la forme originale (SVII, point 3) et l'index l'y recolte deja : annoter
# dedans double le terme sans rien apprendre, et alourdit un titre qui doit
# rester lisible tel quel.
RE_TITRE_LIGNE = re.compile(r"^\s{0,3}#{1,6}\s")
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
    signalements = []

    global INV
    INV = _invariants()
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
        # Le code est masque AVANT la recherche des balises. Une convention
        # CITEE EN PROSE — « `<dfn data-terme ...>` sur les termes » — n'est
        # pas une annotation, et la lire comme telle produit un refus faux.
        # Defaut de la v1.0, trouve le 2026-09-08 quand une entree d'annales
        # a decrit la convention entre chevrons : c'est le piege structurel
        # deja rencontre avec le marqueur d'insertion cite en prose. Le
        # masque preserve les LONGUEURS, donc les offsets restent ceux de
        # `corps` et les positions de D4 demeurent justes.
        gen = _generateur()
        masque_code = gen.RE_CODE.sub(lambda m: "\x00" * len(m.group(0)), corps)
        balises = list(RE_BALISE.finditer(masque_code))
        if not balises:
            continue
        n_fiches += 1
        spans_wl = [(m.start(), m.end()) for m in RE_WL_SPAN.finditer(corps)]
        # D5 : la comparaison se fait avec le `normaliser` DU GENERATEUR, non
        # avec celui d'ici — le local decape jusqu'a [a-z0-9-] et fondrait des
        # cles que le generateur tient pour distinctes. Deux notions de
        # « meme terme » dans une meme chaine, c'est le controle qui ment.
        vus_dans_la_fiche = {}
        for b in balises:
            n_annot += 1
            # Les groupes proviennent du texte MASQUE : on relit la balise
            # dans `corps` aux memes offsets pour en extraire les attributs.
            brut_reel = corps[b.start():b.end()]
            elem = b.group(1).lower()
            attrs = dict(RE_ATTR.findall(brut_reel))

            # D2 — Unicode invisible dans l'annotation (portee : le balisage)
            for ch, nom in INVISIBLES.items():
                if ch in brut_reel:
                    anomalies.append(("D2", rel, "%s dans l'annotation %r"
                                      % (nom, brut_reel[:60])))

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
                admis = genres_admis(INV.circuit_de(rel))
                if g in admis:
                    pass
                elif g in (GENRES_CLOS | GENRES_HERMENEUTIQUE):
                    anomalies.append(("D6", rel,
                        "data-genre=%r est valide, mais son circuit (%s) ne "
                        "l'admet pas" % (g, INV.circuit_de(rel) or "hors circuit")))
                else:
                    anomalies.append(("VOC", rel, "data-genre=%r hors vocabulaire clos" % g))

            # D4 — placement interdit
            deb = b.start()
            fin_ligne = corps.find("\n", deb)
            debut_ligne = corps.rfind("\n", 0, deb) + 1
            ligne = corps[debut_ligne:fin_ligne if fin_ligne >= 0 else len(corps)]
            if RE_TITRE_LIGNE.match(ligne):
                anomalies.append(("D4", rel,
                    "annotation dans un titre : %r" % ligne[:60]))
            if any(a <= deb < z for a, z in spans_wl):
                anomalies.append(("D4", rel,
                    "annotation dans un wikilink : %r" % brut_reel[:60]))

            # D5 — occurrence unique par terme et par fiche
            cle_g = gen.normaliser(cle or "")
            if cle_g:
                if cle_g in vus_dans_la_fiche:
                    anomalies.append(("D5", rel,
                        "terme %r annote une seconde fois (premiere pose "
                        "ligne %d)" % (cle, vus_dans_la_fiche[cle_g])))
                else:
                    vus_dans_la_fiche[cle_g] = corps.count("\n", 0, deb) + 1

            # S1 — doublon de referent possible (signalement, jamais refus)
            if cle_g:
                for autre in vus_dans_la_fiche:
                    if autre == cle_g:
                        continue
                    if (f"-{autre}-" in f"-{cle_g}-"
                            or f"-{cle_g}-" in f"-{autre}-"):
                        signalements.append(("S1", rel,
                            "%r et %r sont coannotes et l'un est composant de "
                            "l'autre : meme referent sous deux cles, ou genre "
                            "et espece ? D5 ne voit pas la difference."
                            % (sorted((autre, cle_g))[0],
                               sorted((autre, cle_g))[1])))

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

    return anomalies, signalements, n_fiches, n_annot


def main():
    ap = argparse.ArgumentParser(description="Validateur des annotations HTML.")
    ap.add_argument("--racine", default="/root/wiki")
    ap.add_argument("--index", default=None)
    a = ap.parse_args()
    racine = Path(a.racine).resolve()
    idx = Path(a.index) if a.index else (
        racine / "atelier/rd/outillage/index-lexical/index-lexical.json")

    anomalies, signalements, n_fiches, n_annot = valider(racine, idx)
    print("valider-annotations v%s — %d fiches annotees, %d annotations."
          % (VERSION, n_fiches, n_annot))
    # Les signalements s'impriment TOUJOURS, y compris quand tout est vert :
    # un signalement tu est un signalement perdu.
    vus = set()
    for code, ou, quoi in signalements:
        if (code, ou, quoi) in vus:
            continue
        vus.add((code, ou, quoi))
        print("SIGNALEMENT %s | %s | %s" % (code, ou, quoi))
    if vus:
        print("%d signalement(s) — non bloquants, verdict reserve (Cmd 12)."
              % len(vus))
    if not anomalies:
        print("OK — aucune anomalie.")
        return 0
    for code, ou, quoi in anomalies:
        print("REFUS %s | %s | %s" % (code, ou, quoi), file=sys.stderr)
    print("%d anomalie(s)." % len(anomalies), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
