#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier-invariants.py — Contrôle mécanique des invariants structurels du dépôt.

Principe (Cmd : "le script est le seul verdict autorisé, jamais l'auto-rapport du
modèle") : ce script est DÉTERMINISTE, sans LLM, sans réseau. Il ne corrige rien.
Il constate et il sort en code non nul si un invariant est rompu.

Usage :
    python3 verifier-invariants.py [--racine /root/wiki] [--json] [--strict]

Codes de sortie :
    0  aucune anomalie bloquante
    1  au moins une anomalie bloquante (ERREUR)
    2  erreur d'exécution du script lui-même

Les AVERTISSEMENTS ne font pas échouer le script sauf avec --strict.
"""

import argparse
import json
import os
import re
import sys
from datetime import date

# --------------------------------------------------------------------------
# Configuration des invariants
# --------------------------------------------------------------------------

# Fichiers d'annales connus (chronologique inverse strict, append-only).
# `meta-annales.md` : journal propre au Domaine Réservé meta/ (ouvert 2026-08-09,
# nom préfixé pour ne jamais se confondre avec les annales.md des circuits).
NOMS_ANNALES = {"annales.md", "meta-annales.md"}

# Circuits et leurs racines relatives.
CIRCUITS = ["doctrinal", "atelier", "label", "meta"]

# Fichiers légitimement sans frontmatter YAML (protocole, README, prompts Hermes…).
# Ne pas leur appliquer B0.
FICHIERS_SANS_FM = {
    "CLAUDE.md", "README.md",
    "migration-2026-06-11.md",
    "echange-eleonore-g.md",
    "2026-06-18-entretien-integral.md",
    "10-briefing-infrastructure-hermes-agent-2026-07-03.md",
    "transcription-index-tilak-origine-polaire.md",
    "transcription-table-matieres-symboles-science-sacree.md",
}
PREFIXES_SANS_FM = (
    "meta/projet-unifie/hermes-prompts/",
)

# Fichiers dont les liens sortants ne sont PAS soumis au contrôle C3 d'étanchéité
# (les annales peuvent citer d'autres circuits pour situer les passes).
# `meta-index.md` : hub propre au Domaine Réservé meta/ (ouvert 2026-08-09).
FICHIERS_EXEMPTS_C3 = NOMS_ANNALES | {"index.md", "meta-index.md"}

# Patterns de liens considérés comme placeholders/exemples — ignorés en C1.
RE_LIEN_PLACEHOLDER = re.compile(
    r"^(\.\.\.|…|slug(-source)?|chemin(/relatif)?|autre-slug"
    r"|atelier/\.\.\.|doctrinal/\.\.\.|doctrinal/vigilance/\.\.\."
    r"|doctrinal/discernement/slug|doctrinal/deviations/slug"
    r"|doctrinal/symboles-ou-autorites/slug|doctrinal/sources/inexistante"
    r"|doctrinal/sources/\.\.\.|doctrinal/etudes/YYYY-MM-DD_synthese-si-existante"
    r"|symbole/autorite-x|deviation-y|symbole-ou-autorite|deviation"
    r"|[A-Z]{4}-MM-DD_.*|atelier/…|doctrinal/symboles/slug)$"
)

# Clés de frontmatter attendues par circuit (Sceau Recteur pour doctrinal).
CLES_REQUISES = {
    "doctrinal": ["title", "type", "status", "tradition_cadre", "created", "updated", "sources"],
    "atelier":   ["title", "type", "created", "updated"],
    "label":     ["title", "type", "created", "updated"],
    "meta":      ["title", "type"],
}

# Étanchéité des circuits : circuit source -> circuits interdits en cible.
# Règle du dépôt : doctrinal ne pointe JAMAIS vers atelier ni meta.
ETANCHEITE_INTERDITE = {
    "doctrinal": {"atelier", "meta", "label"},
}

# Le champ `sources:` du frontmatter doctrinal ne doit jamais viser meta/.
SOURCES_CIBLES_INTERDITES = {"meta"}

RE_ENTETE_ANNALES = re.compile(r"^##\s+\[(\d{4}-\d{2}-\d{2})\]\s*(.*)$")
RE_WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]*)?\]\]")
RE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# --------------------------------------------------------------------------
# Utilitaires
# --------------------------------------------------------------------------

class Rapport:
    def __init__(self):
        self.erreurs = []
        self.avertissements = []

    def erreur(self, fichier, code, message, ligne=None):
        self.erreurs.append({"fichier": fichier, "code": code,
                             "ligne": ligne, "message": message})

    def avertir(self, fichier, code, message, ligne=None):
        self.avertissements.append({"fichier": fichier, "code": code,
                                    "ligne": ligne, "message": message})

    def imprimer(self):
        if self.erreurs:
            print("ERREURS (bloquantes) :")
            for e in self.erreurs:
                loc = f":{e['ligne']}" if e["ligne"] else ""
                print(f"  [{e['code']}] {e['fichier']}{loc} — {e['message']}")
        if self.avertissements:
            print("\nAVERTISSEMENTS :")
            for a in self.avertissements:
                loc = f":{a['ligne']}" if a["ligne"] else ""
                print(f"  [{a['code']}] {a['fichier']}{loc} — {a['message']}")
        print(f"\n{len(self.erreurs)} erreur(s), "
              f"{len(self.avertissements)} avertissement(s).")


def lire(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


def separer_frontmatter(texte):
    """Retourne (dict_frontmatter, texte_corps, n_lignes_frontmatter).

    Parseur minimal volontairement : pas de dépendance PyYAML. Gère les
    scalaires, les listes en ligne [a, b] et les listes en blocs (- item).
    Renvoie (None, texte, 0) si aucun frontmatter délimité n'est présent.
    """
    lignes = texte.split("\n")
    if not lignes or lignes[0].strip() != "---":
        return None, texte, 0
    fin = None
    for i in range(1, len(lignes)):
        if lignes[i].strip() == "---":
            fin = i
            break
    if fin is None:
        return None, texte, 0

    fm = {}
    cle_courante = None
    for brute in lignes[1:fin]:
        if not brute.strip() or brute.lstrip().startswith("#"):
            continue
        if brute.lstrip().startswith("- ") and cle_courante:
            fm.setdefault(cle_courante, [])
            if isinstance(fm[cle_courante], list):
                fm[cle_courante].append(brute.lstrip()[2:].strip().strip("\"'"))
            continue
        if ":" not in brute:
            continue
        cle, _, valeur = brute.partition(":")
        cle = cle.strip()
        valeur = valeur.strip()
        cle_courante = cle
        if valeur == "":
            fm[cle] = []
        elif valeur.startswith("[") and valeur.endswith("]"):
            interieur = valeur[1:-1].strip()
            fm[cle] = ([x.strip().strip("\"'") for x in interieur.split(",") if x.strip()]
                       if interieur else [])
        else:
            fm[cle] = valeur.strip("\"'")
    return fm, "\n".join(lignes[fin + 1:]), fin + 1


def circuit_de(chemin_relatif):
    tete = chemin_relatif.split(os.sep)[0]
    return tete if tete in CIRCUITS else None


def parse_date(valeur):
    if not isinstance(valeur, str) or not RE_DATE.match(valeur.strip()):
        return None
    a, m, j = valeur.strip().split("-")
    try:
        return date(int(a), int(m), int(j))
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Contrôle A — invariants des annales
# --------------------------------------------------------------------------

def controler_annales(chemin_abs, chemin_rel, rap):
    texte = lire(chemin_abs)
    fm, corps, decalage = separer_frontmatter(texte)
    lignes = texte.split("\n")

    entetes = []
    for i, ligne in enumerate(lignes, start=1):
        m = RE_ENTETE_ANNALES.match(ligne)
        if m:
            d = parse_date(m.group(1))
            if d is None:
                rap.erreur(chemin_rel, "A0", f"date d'en-tête illisible : {ligne.strip()}", i)
            else:
                entetes.append((i, d, m.group(2).strip()))

    if not entetes:
        rap.avertir(chemin_rel, "A1", "aucune entrée `## [YYYY-MM-DD]` détectée")
        return

    # A2 — ordre chronologique inverse strict (dates non croissantes).
    for k in range(1, len(entetes)):
        ligne_prec, date_prec, _ = entetes[k - 1]
        ligne_cour, date_cour, titre_cour = entetes[k]
        if date_cour > date_prec:
            rap.erreur(
                chemin_rel, "A2",
                f"rupture d'ordre : {date_cour} apparaît après {date_prec} "
                f"(ligne {ligne_prec}). Convention : plus récent en haut.",
                ligne_cour)

    # A3 — frontmatter `updated` cohérent avec l'entrée la plus récente.
    date_max = max(d for _, d, _ in entetes)
    if fm and "updated" in fm:
        d_updated = parse_date(fm["updated"])
        if d_updated is None:
            rap.erreur(chemin_rel, "A3", f"`updated` illisible : {fm['updated']!r}")
        elif d_updated < date_max:
            rap.erreur(
                chemin_rel, "A3",
                f"`updated: {fm['updated']}` est antérieur à l'entrée la plus "
                f"récente ({date_max}).")
    else:
        rap.avertir(chemin_rel, "A3", "frontmatter sans champ `updated`")

    # A4 — doublons d'en-tête (même date + même titre).
    vus = {}
    for ligne_n, d, titre in entetes:
        cle = (d.isoformat(), titre)
        if cle in vus:
            rap.erreur(chemin_rel, "A4",
                       f"en-tête dupliqué (déjà ligne {vus[cle]}) : [{d}] {titre}",
                       ligne_n)
        else:
            vus[cle] = ligne_n

    # A5 — empreinte d'append mécanique : run de lignes vides anormal.
    # Le format du dépôt utilise UNE ligne vide avant un séparateur `---`.
    for i in range(2, len(lignes)):
        if lignes[i].strip() == "---" and lignes[i - 1].strip() == "" \
                and lignes[i - 2].strip() == "":
            rap.avertir(
                chemin_rel, "A5",
                "double ligne vide avant un séparateur — signature possible "
                "d'un ajout mécanique en fin de fichier plutôt qu'une insertion.",
                i + 1)


# --------------------------------------------------------------------------
# Contrôle B — hygiène du frontmatter
# --------------------------------------------------------------------------

def controler_frontmatter(chemin_rel, fm, rap):
    circ = circuit_de(chemin_rel)
    nom = os.path.basename(chemin_rel)
    rel_unix = chemin_rel.replace(os.sep, "/")
    # Exemption B0 : fichiers légitimement sans frontmatter.
    sans_fm_legitime = (
        nom in FICHIERS_SANS_FM
        or any(rel_unix.startswith(p) for p in PREFIXES_SANS_FM)
    )
    if fm is None:
        if not sans_fm_legitime:
            rap.erreur(chemin_rel, "B0", "aucun frontmatter délimité par `---`")
        return
    # Les fichiers de service (annales, index) sont `type: meta` quel que soit
    # leur circuit : ils ne relèvent pas du Sceau Recteur doctrinal.
    fichier_de_service = (os.path.basename(chemin_rel) in NOMS_ANNALES
                          or os.path.basename(chemin_rel) in ("index.md", "meta-index.md")
                          or str(fm.get("type", "")).strip() == "meta")
    if circ and not fichier_de_service:
        for cle in CLES_REQUISES.get(circ, []):
            if cle not in fm:
                rap.erreur(chemin_rel, "B1", f"clé de frontmatter manquante : `{cle}`")

    # B2 — sources_count cohérent avec sources.
    if "sources_count" in fm and "sources" in fm:
        try:
            attendu = int(str(fm["sources_count"]).strip())
        except ValueError:
            rap.erreur(chemin_rel, "B2", f"`sources_count` non entier : {fm['sources_count']!r}")
        else:
            reel = len(fm["sources"]) if isinstance(fm["sources"], list) else 0
            # "to-source" est un marqueur d'absence, pas une source.
            reel_hors_marqueur = sum(
                1 for s in (fm["sources"] if isinstance(fm["sources"], list) else [])
                if s.strip().lower() != "to-source")
            if attendu not in (reel, reel_hors_marqueur):
                rap.erreur(
                    chemin_rel, "B2",
                    f"`sources_count: {attendu}` ≠ nombre réel de sources "
                    f"({reel}, dont {reel_hors_marqueur} hors marqueur `to-source`)")

    # B3 — cohérence created / updated.
    d_c, d_u = parse_date(fm.get("created", "")), parse_date(fm.get("updated", ""))
    if d_c and d_u and d_u < d_c:
        rap.erreur(chemin_rel, "B3", f"`updated` ({d_u}) antérieur à `created` ({d_c})")

    # B4 — étanchéité du champ `sources:` (doctrinal ne source jamais meta/).
    if circ == "doctrinal" and isinstance(fm.get("sources"), list):
        for s in fm["sources"]:
            for interdit in SOURCES_CIBLES_INTERDITES:
                if s.strip().strip("[]").startswith(interdit + "/"):
                    rap.erreur(chemin_rel, "B4",
                               f"`sources:` doctrinal pointe vers `{interdit}/` : {s}")


# --------------------------------------------------------------------------
# Contrôle C — intégrité et étanchéité des liens
# --------------------------------------------------------------------------

def collecter_cibles(racine):
    """Index des cibles résolvables : chemins sans extension + slugs nus."""
    par_chemin, par_slug = set(), {}
    for base, _, fichiers in os.walk(racine):
        if ".git" in base.split(os.sep):
            continue
        for nom in fichiers:
            if not nom.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(base, nom), racine)
            sans_ext = rel[:-3].replace(os.sep, "/")
            par_chemin.add(sans_ext)
            par_slug.setdefault(os.path.basename(sans_ext), []).append(sans_ext)
    return par_chemin, par_slug


def controler_liens(chemin_rel, corps, par_chemin, par_slug, rap):
    circ = circuit_de(chemin_rel)
    nom = os.path.basename(chemin_rel)
    # Les annales et index sont exempts du contrôle C3 (liens contextuels légitimes).
    interdits = set() if nom in FICHIERS_EXEMPTS_C3 else ETANCHEITE_INTERDITE.get(circ, set())
    for brut in RE_WIKILINK.findall(corps):
        cible = brut.strip().replace("\\", "/")
        if cible.endswith(".md"):
            cible = cible[:-3]
        # Ignorer les placeholders/exemples.
        if RE_LIEN_PLACEHOLDER.match(cible):
            continue
        # C1 — résolution.
        if cible not in par_chemin:
            candidats = par_slug.get(os.path.basename(cible), [])
            if not candidats:
                rap.avertir(chemin_rel, "C1", f"lien non résolu : [[{brut}]]")
                continue
            if len(candidats) > 1:
                rap.avertir(chemin_rel, "C2",
                            f"slug ambigu [[{brut}]] → {len(candidats)} cibles possibles")
            cible = candidats[0]
        # C3 — étanchéité des circuits.
        tete = cible.split("/")[0]
        if tete in interdits:
            rap.erreur(chemin_rel, "C3",
                       f"étanchéité rompue : `{circ}` pointe vers `{tete}` — [[{brut}]]")


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".", help="racine du dépôt (défaut : .)")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--strict", action="store_true",
                    help="les avertissements deviennent bloquants")
    args = ap.parse_args()

    racine = os.path.abspath(args.racine)
    if not os.path.isdir(racine):
        print(f"Racine introuvable : {racine}", file=sys.stderr)
        return 2

    rap = Rapport()
    par_chemin, par_slug = collecter_cibles(racine)

    for base, dossiers, fichiers in os.walk(racine):
        dossiers[:] = [d for d in dossiers if d not in (".git", "node_modules", "_inbox")]
        for nom in sorted(fichiers):
            if not nom.endswith(".md"):
                continue
            chemin_abs = os.path.join(base, nom)
            chemin_rel = os.path.relpath(chemin_abs, racine)
            try:
                texte = lire(chemin_abs)
            except Exception as exc:                       # pragma: no cover
                rap.erreur(chemin_rel, "X0", f"lecture impossible : {exc}")
                continue

            fm, corps, _ = separer_frontmatter(texte)
            controler_frontmatter(chemin_rel, fm, rap)
            controler_liens(chemin_rel, corps, par_chemin, par_slug, rap)
            if nom in NOMS_ANNALES:
                controler_annales(chemin_abs, chemin_rel, rap)

    if args.json:
        print(json.dumps({"erreurs": rap.erreurs,
                          "avertissements": rap.avertissements},
                         ensure_ascii=False, indent=2))
    else:
        rap.imprimer()

    if rap.erreurs:
        return 1
    if args.strict and rap.avertissements:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:                               # pragma: no cover
        print(f"Erreur d'exécution : {exc}", file=sys.stderr)
        sys.exit(2)
