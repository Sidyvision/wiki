#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer-cartographie.py — Générateur du manifeste de cartographie du dépôt.
Version 1.1 (2026-07-22) — sévérité à deux niveaux.

Flux (à sens unique, CLAUDE.md §VII, règle commune des manifestes) :

    dépôt (.md + frontmatter)  →  graphe-cartographie.json  →  widget de lecture

Le widget ne réécrit JAMAIS le dépôt. Ce script ne lit JAMAIS index.md (page
rédigée à la main, susceptible de dériver) : la source de vérité est le
frontmatter de chaque fiche, celui-là même qui fait foi pour le Sceau Recteur.
Aucun LLM n'intervient dans cette boucle.

--------------------------------------------------------------------------------
SÉVÉRITÉ À DEUX NIVEAUX (changement de la v1.1)
--------------------------------------------------------------------------------
La v1.0 bloquait sur toute anomalie. Effet observé sur le dépôt réel : une fiche
très référencée (ibn-arabi) écartée pour un compteur erroné faisait s'effondrer
par ricochet des dizaines de fiches saines, qui apparaissaient alors comme
porteuses de « liens morts ». Le rapport devenait illisible et la cause réelle
noyée dans sa propre cascade.

D'où deux niveaux :

  BLOQUANT — ce qui relève de la gouvernance du dépôt. Rien n'est écrit.
      · frontmatter absent, non refermé, ou YAML illisible
      · champ obligatoire manquant (title, type, status…)
      · violation d'étanchéité (CLAUDE.md §VI)

  AVERTISSEMENT — ce qui relève de l'état du chantier. La fiche RESTE dans le
  graphe, l'anomalie est reportée et visible.
      · sources_count incohérent avec la liste sources
      · lien mort, ambigu, ou mal formé
      · fiche isolée (aucun lien)

Ce partage suit l'esprit kari-kumi (Art. 4) : le montage à blanc montre les
joints non taillés, il ne condamne pas le chantier entier pour eux.

L'option --strict rétablit le comportement v1.0 (tout bloque) pour un audit.

--------------------------------------------------------------------------------
ÉTANCHÉITÉ (CLAUDE.md §VI)
--------------------------------------------------------------------------------
    meta/  →  label/  →  atelier/projets/ et atelier/rd/  →  doctrinal/ et atelier/  (neutres)

Les liens ne descendent que du sensible vers le neutre. Un lien remontant est
une violation BLOQUANTE.

Le circuit meta/ est EXCLU du manifeste par défaut (« ne jamais copier de contenu
meta/ ailleurs sans demande explicite »). Conséquence à connaître : les fiches
doctrinales qui sourcent une pièce de meta/ verront ce lien signalé comme mort.
L'option --inclure-meta lève l'exclusion ; c'est une décision de Sidy, pas du
script.

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
    python3 generer-cartographie.py --depot /root/wiki --verifier
    python3 generer-cartographie.py --depot /root/wiki --sortie ./graphe-cartographie.json
    python3 generer-cartographie.py --depot /root/wiki --rapport anomalies.txt
    python3 generer-cartographie.py --depot /root/wiki --strict     # audit v1.0

Dépendance : PyYAML  (apt install python3-yaml, ou pip3 install pyyaml)
"""

import argparse
import json
import os
import subprocess
import re
import sys
from collections import defaultdict

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "ERREUR : le module PyYAML est requis.\n"
        "         Installation : apt install python3-yaml\n"
        "                   ou : pip3 install pyyaml\n"
    )
    sys.exit(1)


VERSION = "1.1"
SCHEMA_VERSION = "cartographie-1.1"


# ==============================================================================
# 1. CONFIGURATION
# ==============================================================================

# Rang d'étanchéité : plus le nombre est ÉLEVÉ, plus le circuit est SENSIBLE.
# Un lien est licite si rang(source) >= rang(cible).
RANG_ETANCHEITE = {
    "meta": 3,
    "label": 2,
    "atelier/projets": 1,
    "atelier/rd": 1,       # rd/ hérite du régime de projets/ (CLAUDE.md §VI)
    "atelier": 0,
    "doctrinal": 0,
}

# Tous les champs de liens reconnus par le protocole racine §IV
# (« tout Sceau comportant sources / cross_links / liens* »). Le Sceau label
# déclare explicitement liens: et liens_atelier: (label/CLAUDE.md) ; plusieurs
# fiches atelier/meta portent cross_links:. Ne lire que sources+links/cross_links
# faisait passer ces liens valides pour inexistants → faux nœuds isolés.
# Un champ absent d'un fichier est silencieusement ignoré (get(champ) or []).
# Le contrôle d'étanchéité §VI (construire_aretes) s'applique à TOUT champ lu.
_CHAMPS_LIENS_TOUS = ["sources", "liens", "liens_atelier", "links", "cross_links"]
CHAMPS_LIENS = {
    "doctrinal": _CHAMPS_LIENS_TOUS,
    "atelier": _CHAMPS_LIENS_TOUS,
    "label": _CHAMPS_LIENS_TOUS,
    "meta": _CHAMPS_LIENS_TOUS,
}

CHAMPS_OBLIGATOIRES = {
    "doctrinal": ["title", "type", "status", "created", "updated"],
    "atelier": ["title", "type", "created", "updated"],
    "label": ["title", "type", "created", "updated"],
    "meta": ["title"],
}

CIRCUITS = ["doctrinal", "atelier", "label", "meta"]

FICHIERS_EXCLUS = {"index.md", "annales.md", "CLAUDE.md", "README.md"}
DOSSIERS_EXCLUS = {"_inbox", "raw", ".git", "node_modules", ".obsidian"}


def _chemins_ignores(racine):
    """Ce que `.gitignore` exclut n'appartient pas au dépôt, donc pas au graphe.

    Ajouté le 2026-09-01 (chantier OUT-C2). Sans ce filtre, le venv de l'essai
    Graphify et son dossier de sorties régénérables injectaient 112 anomalies de
    frontmatter étrangères au dépôt — le même bruit qui masquait les erreurs
    réelles de `verifier-invariants.py`. Déterministe, sans réseau ni LLM.
    Retourne un ensemble vide si git est indisponible (le filtre des dossiers
    cachés reste alors seul en vigueur)."""
    try:
        sortie = subprocess.run(
            ["git", "ls-files", "--others", "--ignored", "--exclude-standard",
             "--directory", "-z"],
            cwd=racine, capture_output=True, check=True, timeout=60,
        ).stdout.decode("utf-8", "replace")
    except (OSError, subprocess.SubprocessError):
        return set()
    return {c.rstrip("/") for c in sortie.split("\0") if c}

WIKILINK = re.compile(r"^\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]$")


class Journal:
    """Collecteur d'anomalies, séparées par sévérité."""

    def __init__(self):
        self.bloquants = []
        self.avertissements = []

    def bloquant(self, categorie, message):
        self.bloquants.append((categorie, message))

    def avertir(self, categorie, message):
        self.avertissements.append((categorie, message))

    def compter(self, liste):
        c = defaultdict(int)
        for categorie, _ in liste:
            c[categorie] += 1
        return c


# ==============================================================================
# 2. LECTURE DU FRONTMATTER
# ==============================================================================

def lire_frontmatter(chemin):
    """Retourne (dict_frontmatter, erreur_ou_None)."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            contenu = f.read()
    except OSError as e:
        return None, f"lecture impossible : {e}"

    if not contenu.startswith("---"):
        return None, "frontmatter absent (le fichier ne commence pas par '---')"

    parties = re.split(r"^---\s*$", contenu, maxsplit=2, flags=re.MULTILINE)
    if len(parties) < 3:
        return None, "frontmatter non refermé (deuxième '---' manquant)"

    try:
        donnees = yaml.safe_load(parties[1])
    except yaml.YAMLError as e:
        return None, f"YAML invalide : {str(e).splitlines()[0]}"

    if donnees is None:
        return None, "frontmatter vide"
    if not isinstance(donnees, dict):
        return None, "frontmatter mal formé (ce n'est pas un dictionnaire de clés)"

    return donnees, None


def rang_de(chemin_relatif):
    for prefixe in sorted(RANG_ETANCHEITE, key=len, reverse=True):
        if chemin_relatif.startswith(prefixe + "/"):
            return RANG_ETANCHEITE[prefixe]
    return 0


def sous_dossier_de(chemin_relatif):
    morceaux = chemin_relatif.split("/")
    return morceaux[1] if len(morceaux) > 2 else morceaux[0]


# ==============================================================================
# 3. COLLECTE DES FICHES
# ==============================================================================

def collecter(depot, circuits_retenus, journal):
    """Parcourt le dépôt. Retourne le dict des fiches retenues.

    Une fiche n'est écartée QUE sur anomalie bloquante. Les incohérences de
    compteur la laissent en place, signalée.
    """
    fiches = {}

    for circuit in circuits_retenus:
        racine = os.path.join(depot, circuit)
        if not os.path.isdir(racine):
            journal.bloquant("structure", f"circuit absent du dépôt : {circuit}/")
            continue

        ignores = _chemins_ignores(racine)
        for dossier, sous_dossiers, fichiers in os.walk(racine):
            # Les dossiers cachés sont hors dépôt par convention (venv de
            # dépendances tierces, caches, état runtime) — même règle que
            # carte-du-depot.py. Ajouté le 2026-09-01 : sans elle,
            # `.graphify-venv/` injectait 112 anomalies de frontmatter
            # étrangères au dépôt, du même bruit que celui qui masquait les
            # erreurs réelles de verifier-invariants.py (chantier OUT-C2).
            sous_dossiers[:] = [
                d for d in sous_dossiers
                if d not in DOSSIERS_EXCLUS
                and not d.startswith(".")
                and os.path.relpath(os.path.join(dossier, d), racine)
                    .replace(os.sep, "/") not in ignores
            ]

            for nom in sorted(fichiers):
                if not nom.endswith(".md") or nom in FICHIERS_EXCLUS:
                    continue

                chemin_abs = os.path.join(dossier, nom)
                chemin_rel = os.path.relpath(chemin_abs, depot).replace(os.sep, "/")
                identifiant = chemin_rel[:-3]

                fm, erreur = lire_frontmatter(chemin_abs)
                if erreur:
                    journal.bloquant("frontmatter", f"{chemin_rel} : {erreur}")
                    continue  # illisible : on ne peut rien en faire

                manquants = [
                    c for c in CHAMPS_OBLIGATOIRES.get(circuit, [])
                    if c not in fm or fm[c] in (None, "")
                ]
                if manquants:
                    journal.bloquant(
                        "frontmatter",
                        f"{chemin_rel} : champ(s) obligatoire(s) manquant(s) : "
                        f"{', '.join(manquants)}"
                    )
                    continue  # Sceau Recteur incomplet : gouvernance

                # --- Cohérence sources_count : AVERTISSEMENT, pas blocage ----
                if circuit == "doctrinal" and "sources_count" in fm:
                    sources = fm.get("sources")
                    if sources is None:
                        sources = []
                    if not isinstance(sources, list):
                        journal.avertir(
                            "compteur",
                            f"{chemin_rel} : 'sources' n'est pas une liste YAML."
                        )
                    elif fm["sources_count"] != len(sources):
                        sens = "supérieur" if fm["sources_count"] > len(sources) else "inférieur"
                        journal.avertir(
                            "compteur",
                            f"{chemin_rel} : sources_count = {fm['sources_count']} "
                            f"({sens}) mais 'sources' contient {len(sources)} entrée(s)."
                        )

                fiches[identifiant] = {
                    "id": identifiant,
                    "chemin": chemin_rel,
                    "slug": nom[:-3],
                    "circuit": circuit,
                    "sous_dossier": sous_dossier_de(chemin_rel),
                    "rang": rang_de(chemin_rel),
                    "frontmatter": fm,
                }

    return fiches


# ==============================================================================
# 4. RÉSOLUTION DES WIKILINKS
# ==============================================================================

def construire_index_slugs(fiches):
    index = defaultdict(list)
    for identifiant, fiche in fiches.items():
        index[fiche["slug"]].append(identifiant)
    return index


def resoudre(cible_brute, fiches, index_slugs):
    """Retourne (identifiant, statut) — 'ok' | 'to-source' | 'introuvable' | 'ambigu'."""
    cible = cible_brute.strip()

    if cible == "to-source":
        return None, "to-source"
    if cible in fiches:
        return cible, "ok"

    candidats = index_slugs.get(cible, [])
    if len(candidats) == 1:
        return candidats[0], "ok"
    if len(candidats) > 1:
        return None, "ambigu"
    return None, "introuvable"


def extraire_cible(valeur):
    """Extrait la cible d'un lien. Accepte [[chemin]] (wikilink) ou chemin (format brut YAML)."""
    if not isinstance(valeur, str):
        return None
    valeur = valeur.strip()
    if valeur == "to-source":
        return "to-source"
    # Format wikilink : [[chemin]]
    m = WIKILINK.match(valeur)
    if m:
        return m.group(1)
    # Format brut (YAML désérialise [[chemin]] en liste, puis en string)
    # Accepter si le chemin contient au moins un caractère et pas de caractères invalides
    if valeur and not valeur.startswith('[') and '/' in valeur:
        return valeur
    return None


# ==============================================================================
# 5. CONSTRUCTION DES ARÊTES
# ==============================================================================

def est_suggere(fiche_source, statut_lien):
    """Un lien est 'suggéré' (kari-kumi, pointillé 🔍) s'il n'est pas assis."""
    if statut_lien == "to-source":
        return True
    fm = fiche_source["frontmatter"]
    if fm.get("status") == "speculatif":
        return True
    if fm.get("type") == "discernement" and str(fm.get("statut", "")).lower() == "en cours":
        return True
    return False


def construire_aretes(fiches, index_slugs, journal):
    aretes = []
    vues = set()

    for identifiant in sorted(fiches):
        fiche = fiches[identifiant]
        circuit = fiche["circuit"]

        for champ in CHAMPS_LIENS.get(circuit, []):
            valeurs = fiche["frontmatter"].get(champ) or []

            if isinstance(valeurs, str):
                journal.avertir(
                    "lien",
                    f"{fiche['chemin']} : '{champ}' est une chaîne seule, "
                    f"une liste YAML est attendue."
                )
                continue
            if not isinstance(valeurs, list):
                journal.avertir("lien", f"{fiche['chemin']} : '{champ}' mal formé.")
                continue

            for valeur in valeurs:
                cible_brute = extraire_cible(valeur)

                if cible_brute is None:
                    apercu = str(valeur)
                    if len(apercu) > 70:
                        apercu = apercu[:67] + "…"
                    journal.avertir(
                        "lien",
                        f"{fiche['chemin']} : '{champ}' contient une entrée hors schéma : "
                        f"{apercu!r}"
                    )
                    continue

                cible_id, statut = resoudre(cible_brute, fiches, index_slugs)

                if statut == "introuvable":
                    journal.avertir(
                        "lien mort",
                        f"{fiche['chemin']} : '{champ}' → [[{cible_brute}]] (absent du dépôt)"
                    )
                    continue

                if statut == "ambigu":
                    journal.avertir(
                        "lien ambigu",
                        f"{fiche['chemin']} : '{champ}' → [[{cible_brute}]] correspond à "
                        f"{len(index_slugs[cible_brute])} fiches ; utiliser la forme longue."
                    )
                    continue

                if statut == "to-source":
                    fiche.setdefault("_lacunes", 0)
                    fiche["_lacunes"] += 1
                    continue

                # --- Étanchéité : BLOQUANT ------------------------------------
                cible = fiches[cible_id]
                if fiche["rang"] < cible["rang"]:
                    journal.bloquant(
                        "étanchéité",
                        f"{fiche['chemin']} (neutre) → {cible['chemin']} (plus sensible). "
                        f"Les liens ne vont que du sensible vers le neutre — CLAUDE.md §VI."
                    )
                    continue

                cle = (identifiant, cible_id, champ)
                if cle in vues:
                    continue
                vues.add(cle)

                aretes.append({
                    "source": identifiant,
                    "target": cible_id,
                    "champ": champ,
                    "nature": "source" if champ == "sources" else "lien",
                    "assise": "suggere" if est_suggere(fiche, statut) else "etabli",
                })

    relies = {a["source"] for a in aretes} | {a["target"] for a in aretes}
    for identifiant in sorted(fiches):
        if identifiant not in relies:
            journal.avertir("isolée", f"{fiches[identifiant]['chemin']} : aucun lien.")

    return aretes


# ==============================================================================
# 6. ASSEMBLAGE ET RAPPORT
# ==============================================================================

def construire_noeuds(fiches):
    noeuds = []
    for identifiant in sorted(fiches):
        f = fiches[identifiant]
        fm = f["frontmatter"]
        noeuds.append({
            "id": identifiant,
            "label": str(fm.get("title", f["slug"])),
            "circuit": f["circuit"],
            "sous_dossier": f["sous_dossier"],
            "type": fm.get("type"),
            "status": fm.get("status"),
            "tradition_cadre": fm.get("tradition_cadre"),
            "tags": fm.get("tags") or [],
            "updated": str(fm.get("updated", "")),
            "chemin": f["chemin"],
            "lacunes_to_source": f.get("_lacunes", 0),
        })
    return noeuds


def rapport(noeuds, aretes, journal):
    par_circuit = defaultdict(int)
    for n in noeuds:
        par_circuit[n["circuit"]] += 1

    par_assise = defaultdict(int)
    for a in aretes:
        par_assise[a["assise"]] += 1

    lignes = [
        "",
        f"  MANIFESTE DE CARTOGRAPHIE — script v{VERSION}",
        "",
        f"  Nœuds : {len(noeuds)}",
    ]
    for circuit in CIRCUITS:
        if par_circuit.get(circuit):
            lignes.append(f"      {circuit:<12} {par_circuit[circuit]}")
    lignes += [
        "",
        f"  Arêtes : {len(aretes)}",
        f"      établies    {par_assise.get('etabli', 0)}",
        f"      suggérées   {par_assise.get('suggere', 0)}",
        "",
        f"  Lacunes to-source : {sum(n['lacunes_to_source'] for n in noeuds)}",
        "",
    ]

    if journal.avertissements:
        compte = journal.compter(journal.avertissements)
        lignes.append(f"  Avertissements : {len(journal.avertissements)} (non bloquants)")
        for categorie in sorted(compte, key=lambda c: -compte[c]):
            lignes.append(f"      {categorie:<14} {compte[categorie]}")
        lignes.append("")

    return "\n".join(lignes)


def ecrire_rapport(chemin, journal):
    with open(chemin, "w", encoding="utf-8") as f:
        if journal.bloquants:
            f.write(f"ANOMALIES BLOQUANTES ({len(journal.bloquants)})\n")
            f.write("=" * 60 + "\n\n")
            for categorie, message in journal.bloquants:
                f.write(f"[{categorie}] {message}\n")
            f.write("\n\n")
        f.write(f"AVERTISSEMENTS ({len(journal.avertissements)})\n")
        f.write("=" * 60 + "\n\n")
        courant = None
        for categorie, message in sorted(journal.avertissements):
            if categorie != courant:
                f.write(f"\n--- {categorie} ---\n")
                courant = categorie
            f.write(f"{message}\n")


# ==============================================================================
# 7. POINT D'ENTRÉE
# ==============================================================================

def main():
    p = argparse.ArgumentParser(
        description="Génère le manifeste de cartographie du dépôt (script déterministe)."
    )
    p.add_argument("--depot", default="/root/wiki", help="Racine du dépôt")
    p.add_argument("--sortie", default=None,
                   help="JSON produit (défaut : <depot>/graphe-cartographie.json)")
    p.add_argument("--rapport", default=None,
                   help="Écrit le détail complet des anomalies dans ce fichier")
    p.add_argument("--inclure-meta", action="store_true",
                   help="Inclut le circuit meta/ (exclu par défaut — CLAUDE.md §VI)")
    p.add_argument("--verifier", action="store_true",
                   help="Contrôle seul : valide et rapporte, n'écrit aucun manifeste")
    p.add_argument("--strict", action="store_true",
                   help="Tout avertissement redevient bloquant (audit)")
    args = p.parse_args()

    depot = os.path.abspath(args.depot)
    if not os.path.isdir(depot):
        sys.stderr.write(f"ERREUR : dépôt introuvable : {depot}\n")
        return 1

    sortie = args.sortie or os.path.join(depot, "graphe-cartographie.json")
    circuits_retenus = [c for c in CIRCUITS if c != "meta" or args.inclure_meta]

    journal = Journal()
    fiches = collecter(depot, circuits_retenus, journal)
    index_slugs = construire_index_slugs(fiches)
    aretes = construire_aretes(fiches, index_slugs, journal)
    noeuds = construire_noeuds(fiches)

    if args.strict:
        journal.bloquants.extend(journal.avertissements)
        journal.avertissements = []

    if args.rapport:
        try:
            ecrire_rapport(args.rapport, journal)
            sys.stdout.write(f"\n  Détail des anomalies écrit dans : {args.rapport}\n")
        except OSError as e:
            sys.stderr.write(f"ERREUR d'écriture du rapport : {e}\n")

    # --- Anomalies bloquantes -------------------------------------------------
    if journal.bloquants:
        compte = journal.compter(journal.bloquants)
        sys.stderr.write(
            f"\n  ÉCHEC — {len(journal.bloquants)} anomalie(s) bloquante(s). "
            f"Aucun manifeste écrit.\n\n"
        )
        for categorie in sorted(compte, key=lambda c: -compte[c]):
            sys.stderr.write(f"      {categorie:<14} {compte[categorie]}\n")
        sys.stderr.write("\n")
        limite = 40
        for categorie, message in journal.bloquants[:limite]:
            sys.stderr.write(f"    [{categorie}] {message}\n")
        if len(journal.bloquants) > limite:
            reste = len(journal.bloquants) - limite
            sys.stderr.write(f"    … et {reste} autre(s). Utiliser --rapport pour le détail.\n")
        sys.stderr.write("\n")
        return 1

    sys.stdout.write(rapport(noeuds, aretes, journal))

    if args.verifier:
        sys.stdout.write("  Mode --verifier : aucun manifeste écrit.\n\n")
        return 0

    manifeste = {
        "schema": SCHEMA_VERSION,
        "depot": os.path.basename(depot),
        "meta_inclus": args.inclure_meta,
        "avertissements": len(journal.avertissements),
        "nodes": noeuds,
        "edges": aretes,
    }

    temporaire = sortie + ".tmp"
    try:
        with open(temporaire, "w", encoding="utf-8") as f:
            json.dump(manifeste, f, ensure_ascii=False, indent=2)
            f.write("\n")
        os.replace(temporaire, sortie)
    except OSError as e:
        sys.stderr.write(f"ERREUR d'écriture : {e}\n")
        if os.path.exists(temporaire):
            os.remove(temporaire)
        return 1

    sys.stdout.write(f"  Écrit : {sortie}\n\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
