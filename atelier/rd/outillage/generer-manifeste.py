#!/usr/bin/env python3
# =============================================================================
# generer-manifeste.py — Générateur déterministe du wiki-manifest (schéma v0.2.1)
#
#   Phase 1 de l'Instrument de la Tradition Primordiale.
#   Croise deux couches :
#     1. la vérité doctrinale : les fiches de doctrinal/ (labels, existence,
#        discernements « en cours ») — LECTURE SEULE ;
#     2. la déclaration applicative : atelier/rd/instrument/instrument-donnees.yaml
#        (nœuds, degrés verticaux, ancrages).
#   Produit : atelier/rd/instrument/wiki-manifest.json
#
#   AUCUN LLM dans la boucle. Parse mécanique uniquement.
#   Validations bloquantes : voir la spec (spec-generateur-manifeste.md §5).
#
#   Usage :
#     python3 generer-manifeste.py --repo /root/wiki
#     python3 generer-manifeste.py --repo /root/regression-test/sandbox   # bac à sable
# =============================================================================

import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # PyYAML : apt install python3-yaml
except ImportError:
    sys.exit("ERREUR : PyYAML manquant. Installer avec : apt install python3-yaml")

# --- Constantes du schéma v0.2.2 --------------------------------------------
#
#   v0.2.2 (2026-08-20) : le bloc `zodiaque:` d'instrument-donnees.yaml (degrés
#     du falak al-burūj/al-manāzil, obliquité, époque de référence, signes) est
#     désormais propagé dans le manifeste (clé "zodiaque"), avec validations
#     mécaniques dédiées (§ci-dessous). Auparavant déclaré en YAML mais jamais
#     émis : le prototype le transcrivait à la main sans passer par le
#     manifeste — écart signalé dans rd/instrument/2026-08-20_etat-avancement-
#     pistes-developpement.md §5, fermé ici sur demande de Sidy.

SCHEMA_VERSION = "0.2.2"
TYPES_ANCRAGE = {"equivalence", "complementarite", "subversion", "parodie"}
ETATS_ANCRAGE = {"etabli", "suggere", "identifie"}
DIRECTIONNALITES = {"none", "ascendant", "descendant"}

# Frontmatter : bloc YAML entre deux lignes `---` en tête de fichier.
RE_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
# Bloc 🔍 normalisé des discernements : ligne « **Statut** : en cours | validée | invalidée »
RE_STATUT_DISCERNEMENT = re.compile(
    r"\*\*Statut\*\*\s*:\s*(en cours|valid[ée]e|invalid[ée]e)", re.I
)
# Wikilink : [[chemin/ou/slug]] — on ne garde que le slug final pour comparer.
RE_WIKILINK = re.compile(r"\[\[([^\]|]+)")


# --- Petites fonctions utilitaires -------------------------------------------

def lire_frontmatter(chemin: Path):
    """Retourne (frontmatter dict, corps str) d'une fiche, ou (None, texte) si absent/invalide."""
    texte = chemin.read_text(encoding="utf-8", errors="replace")
    m = RE_FRONTMATTER.match(texte)
    if not m:
        return None, texte
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None, texte
    return (fm if isinstance(fm, dict) else None), texte[m.end():]


def slug_de(wikilink_ou_chemin: str) -> str:
    """« doctrinal/symboles/barzakh » ou « [[…/barzakh]] » → « barzakh »."""
    s = wikilink_ou_chemin.strip().strip("[]").split("|")[0]
    return s.rstrip("/").split("/")[-1].removesuffix(".md")


def sha_git(repo: Path) -> str:
    """SHA du commit courant du dépôt, ou « inconnu » hors dépôt git."""
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        return r.stdout.strip() if r.returncode == 0 else "inconnu"
    except Exception:
        return "inconnu"


# --- Cœur du générateur -------------------------------------------------------

def indexer_fiches_doctrinales(repo: Path) -> dict:
    """Index {slug: (chemin relatif, frontmatter)} de toutes les fiches doctrinal/."""
    index = {}
    for f in sorted((repo / "doctrinal").rglob("*.md")):
        fm, _ = lire_frontmatter(f)
        index[f.stem] = (f.relative_to(repo).as_posix(), fm or {})
    return index


def discernements_en_cours(repo: Path) -> list:
    """Liste [(chemin relatif sans .md, {slugs cibles des cross_links})] des
    discernements dont le bloc 🔍 porte « Statut : en cours »."""
    resultats = []
    dossier = repo / "doctrinal" / "discernement"
    if not dossier.is_dir():
        return resultats
    for f in sorted(dossier.glob("*.md")):
        fm, corps = lire_frontmatter(f)
        m = RE_STATUT_DISCERNEMENT.search(corps)
        if not m or "en cours" not in m.group(1).lower():
            continue
        cibles = set()
        for lien in (fm or {}).get("cross_links", []) or []:
            if isinstance(lien, str):
                cibles.add(slug_de(lien))
        chemin_sans_ext = f.relative_to(repo).as_posix().removesuffix(".md")
        resultats.append((chemin_sans_ext, cibles))
    return resultats


def valider_zodiaque(zodiaque: dict, decl_noeuds: list, erreurs: list, avertissements: list):
    """Valide le bloc `zodiaque:` (peut être absent) et retourne la valeur à
    inscrire dans le manifeste, ou None si absente/invalide au point de ne
    rien produire. Erreurs bloquantes limitées aux malformations structurelles
    (types) ; le reste (12 signes attendus, degrés cohérents avec un nœud
    déclaré) reste un avertissement — ce ne sont pas des invariants du schéma,
    seulement des indices de dérive possible."""
    if not zodiaque:
        return None
    if not isinstance(zodiaque, dict):
        erreurs.append("zodiaque : doit être un mapping (dict)")
        return None

    degres_declares = {d.get("degre_vertical") for d in decl_noeuds
                        if d.get("degre_vertical") is not None}

    for cle in ("degre_falak_al_buruj", "degre_falak_al_manazil"):
        v = zodiaque.get(cle)
        if v is not None and not isinstance(v, int):
            erreurs.append(f"zodiaque.{cle} : doit être un entier ou null (reçu {v!r})")
        elif isinstance(v, int) and v not in degres_declares:
            avertissements.append(
                f"zodiaque.{cle} = {v} : aucun nœud déclaré ne porte ce degre_vertical"
            )

    obliquite = zodiaque.get("obliquite_deg")
    if obliquite is not None and not isinstance(obliquite, (int, float)):
        erreurs.append(f"zodiaque.obliquite_deg : doit être numérique (reçu {obliquite!r})")

    signes = zodiaque.get("signes")
    if signes is not None:
        if not isinstance(signes, list):
            erreurs.append("zodiaque.signes : doit être une liste")
        else:
            if len(signes) != 12:
                avertissements.append(
                    f"zodiaque.signes : {len(signes)} entrée(s) déclarée(s), 12 attendues"
                )
            for i, s in enumerate(signes):
                if not isinstance(s, dict) or not str(s.get("label", "")).strip():
                    erreurs.append(f"zodiaque.signes[{i}] : doit porter un « label » non vide")

    return zodiaque


def generer(repo: Path, chemin_donnees: Path, chemin_sortie: Path) -> int:
    erreurs, avertissements = [], []

    # 1. Charger la déclaration applicative.
    if not chemin_donnees.is_file():
        sys.exit(f"ERREUR : fichier déclaratif introuvable : {chemin_donnees}")
    donnees = yaml.safe_load(chemin_donnees.read_text(encoding="utf-8")) or {}
    decl_noeuds = donnees.get("noeuds", []) or []
    decl_ancrages = donnees.get("ancrages", []) or []
    decl_zodiaque = donnees.get("zodiaque") or {}

    # 2. Indexer la vérité doctrinale.
    fiches = indexer_fiches_doctrinales(repo)
    en_cours = discernements_en_cours(repo)

    # 3. Construire les nœuds.
    noeuds, ids = [], set()
    for d in decl_noeuds:
        tradition = d.get("tradition", "").strip()
        fiche = d.get("fiche", "").strip()          # ex. doctrinal/symboles/barzakh
        slug = slug_de(fiche)
        # id : déclaré si fourni (cas des nœuds-degrés partageant une même fiche
        # source), sinon <tradition>/<slug de la fiche>.
        node_id = d.get("id") or f"{tradition}/{slug}"

        if not tradition or not fiche:
            erreurs.append(f"nœud incomplet (tradition/fiche requis) : {d}")
            continue
        if node_id in ids:
            erreurs.append(f"id de nœud dupliqué : {node_id}")
            continue
        if slug not in fiches:
            erreurs.append(f"fiche doctrinale introuvable pour le nœud {node_id} : {fiche}")
            continue

        chemin_rel, fm = fiches[slug]
        # Libellé : déclaré si fourni (idem), sinon le title de la fiche
        # (jamais retapé à la main).
        label = d.get("label") or fm.get("title") or slug

        # question_ouverte : premier discernement « en cours » qui pointe ce slug.
        question = False
        for chemin_disc, cibles in en_cours:
            if slug in cibles:
                question = f"[[{chemin_disc}]]"
                break

        ids.add(node_id)
        noeuds.append({
            "id": node_id,
            "tradition": tradition,
            "label": label,
            "source": f"[[{chemin_rel.removesuffix('.md')}]]",
            "degre_vertical": d.get("degre_vertical", None),
            "question_ouverte": question,
            "ancrages": [],
        })
    par_id = {n["id"]: n for n in noeuds}

    # 4. Valider et rattacher les ancrages (stockage à sens unique sur le nœud source).
    for a in decl_ancrages:
        src, typ = a.get("noeud", ""), a.get("type", "")
        etat = a.get("etat", "")
        cible = a.get("cible", None)
        direction = a.get("directionnalite", "none")
        source_doc = a.get("source", None)
        contexte = f"ancrage {src} → {cible} ({typ}/{etat})"

        if src not in par_id:
            erreurs.append(f"{contexte} : nœud source non déclaré"); continue
        if typ not in TYPES_ANCRAGE:
            erreurs.append(f"{contexte} : type invalide"); continue
        if etat not in ETATS_ANCRAGE:
            erreurs.append(f"{contexte} : etat invalide"); continue
        if direction not in DIRECTIONNALITES:
            erreurs.append(f"{contexte} : directionnalite invalide"); continue
        if cible is not None and cible not in par_id:
            erreurs.append(f"{contexte} : cible non déclarée"); continue
        if etat == "etabli" and not source_doc:
            erreurs.append(f"{contexte} : un ancrage etabli DOIT être sourcé (Cmd 5)"); continue
        if typ in ("subversion", "parodie") and cible is not None:
            # Correctif waswâs/Qliphoth (architecture v0.2 §2/§6) : jamais de pont
            # inter-traditions structurel — cible non nulle SEULEMENT si un
            # discernement l'a spécifiquement établi.
            if not (source_doc and "discernement" in str(source_doc)):
                erreurs.append(
                    f"{contexte} : subversion/parodie avec cible exige une fiche "
                    f"doctrinal/discernement/ en source (correctif v0.2 §2)"
                ); continue
        if direction != "none" and typ != "complementarite":
            avertissements.append(f"{contexte} : directionnalite sur un type non-complementarite")
        if source_doc and slug_de(str(source_doc)) not in fiches:
            avertissements.append(f"{contexte} : fiche source introuvable au dépôt : {source_doc}")

        par_id[src]["ancrages"].append({
            "type": typ,
            "etat": etat,
            "directionnalite": direction,
            "cible": cible,
            "source": source_doc,
            "note": a.get("note", ""),
        })

    # 5. Valider et intégrer le bloc zodiaque (indépendant des nœuds/ancrages).
    zodiaque_valide = valider_zodiaque(decl_zodiaque, decl_noeuds, erreurs, avertissements)

    # 6. Rapport et sortie.
    for w in avertissements:
        print(f"⚠ AVERTISSEMENT : {w}")
    if erreurs:
        for e in erreurs:
            print(f"✗ ERREUR : {e}")
        print(f"\nVERDICT : {len(erreurs)} erreur(s) — manifeste NON produit.")
        return 1

    manifeste = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.datetime.now(datetime.timezone.utc)
                        .isoformat(timespec="seconds"),
        "source_commit": sha_git(repo),
        "nodes": noeuds,
    }
    if zodiaque_valide is not None:
        manifeste["zodiaque"] = zodiaque_valide
    chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
    chemin_sortie.write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    nb_ancrages = sum(len(n["ancrages"]) for n in noeuds)
    print(f"✓ Manifeste produit : {chemin_sortie}")
    print(f"  {len(noeuds)} nœud(s), {nb_ancrages} ancrage(s), "
          f"zodiaque {'inclus' if zodiaque_valide is not None else 'absent'}, "
          f"{len(avertissements)} avertissement(s), commit {manifeste['source_commit'][:12]}")
    return 0


# --- Point d'entrée -----------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Générateur du wiki-manifest (v0.2.1), déterministe.")
    p.add_argument("--repo", default="/root/wiki", help="racine du dépôt wiki")
    p.add_argument("--donnees", default=None,
                   help="fichier déclaratif (défaut : <repo>/atelier/rd/instrument/instrument-donnees.yaml)")
    p.add_argument("--sortie", default=None,
                   help="manifeste produit (défaut : <repo>/atelier/rd/instrument/wiki-manifest.json)")
    args = p.parse_args()

    repo = Path(args.repo).resolve()
    if not (repo / "doctrinal").is_dir():
        sys.exit(f"ERREUR : {repo} ne ressemble pas au dépôt (doctrinal/ absent).")
    donnees = Path(args.donnees) if args.donnees else repo / "atelier/rd/instrument/instrument-donnees.yaml"
    sortie = Path(args.sortie) if args.sortie else repo / "atelier/rd/instrument/wiki-manifest.json"

    sys.exit(generer(repo, donnees, sortie))


if __name__ == "__main__":
    main()
