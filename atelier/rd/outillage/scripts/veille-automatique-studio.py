#!/usr/bin/env python3
"""
Veille automatique Studio — recherche GitHub + arXiv, extraction, analyse,
génération de fiches de veille dans atelier/rd/veille/.

Maître-mot : self-improvement.
Intègre tout élément qualitatif (outillage, théorique, base de code)
pouvant soutenir l'amélioration autonome.

Verdict Sidy 2026-08-31 (voir proposition-veille-automatique-studio-2026-08-31.md).
"""

import json
import os
import re
import sys
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERREUR: PyYAML requis. pip install pyyaml", file=sys.stderr)
    sys.exit(1)


# ===== Configuration =====

WIKI_ROOT = Path("/root/wiki")
CONFIG_PATH = WIKI_ROOT / "atelier/rd/outillage/config/veille-mots-cles.yaml"
VEILLE_DIR = WIKI_ROOT / "atelier/rd/veille"
ARCHIVE_DIR = VEILLE_DIR / "archive"

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
ARXIV_SEARCH_URL = "http://export.arxiv.org/api/query"


def load_config():
    """Charge la config YAML."""
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def slugify(text: str) -> str:
    """Convertit un texte en slug ASCII minuscules avec tirets."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    text = text[:80]  # limite longueur
    return text


# ===== Recherche GitHub =====

def search_github(query: str, config: dict) -> list:
    """Recherche GitHub pour un mot-clé."""
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": config["api"]["github_results_per_query"],
    }
    url = f"{GITHUB_SEARCH_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})

    try:
        with urllib.request.urlopen(req, timeout=config["api"]["timeout_seconds"]) as r:
            data = json.loads(r.read())
        return data.get("items", [])
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        print(f"  WARN GitHub '{query}': {e}", file=sys.stderr)
        return []


def filtre_github(repo: dict, config: dict) -> bool:
    """Filtre un repo selon les critères."""
    min_stars = config["filtrage"]["min_stars"]
    max_age_months = config["filtrage"]["max_age_months"]
    licences_permises = config["filtrage"]["licences_permises"]
    langues = config["filtrage"]["langues"]

    if repo.get("stargazers_count", 0) < min_stars:
        return False

    # Âge
    pushed_at = repo.get("pushed_at")
    if pushed_at:
        try:
            pushed_date = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            cutoff = datetime.now(pushed_date.tzinfo) - timedelta(days=max_age_months * 30)
            if pushed_date < cutoff:
                return False
        except ValueError:
            pass

    # Licence
    licence = repo.get("license")
    if licence:
        spdx = (licence.get("spdx_id") or "").upper()
        if spdx not in [l.upper() for l in licences_permises] and spdx != "NOASSERTION":
            return False
    else:
        return False  # pas de licence = écarté

    # Langage
    lang = repo.get("language") or ""
    if langues and lang not in langues:
        return False

    return True


# ===== Recherche arXiv =====

def search_arxiv(query: str, config: dict) -> list:
    """Recherche arXiv pour un mot-clé."""
    params = {
        "search_query": f"all:{urllib.parse.quote(query)}",
        "start": 0,
        "max_results": config["api"]["arxiv_results_per_query"],
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_SEARCH_URL}?{urllib.parse.urlencode(params)}"

    try:
        with urllib.request.urlopen(url, timeout=config["api"]["timeout_seconds"]) as r:
            xml_data = r.read()
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", ns)
        results = []
        for entry in entries:
            results.append({
                "title": entry.findtext("atom:title", "", ns).strip().replace("\n", " "),
                "summary": entry.findtext("atom:summary", "", ns).strip().replace("\n", " "),
                "published": entry.findtext("atom:published", "", ns),
                "link": next(
                    (lnk.get("href") for lnk in entry.findall("atom:link", ns)
                     if lnk.get("type") == "text/html"),
                    entry.findtext("atom:id", "", ns)
                ),
                "authors": [a.findtext("atom:name", "", ns) for a in entry.findall("atom:author", ns)][:5],
            })
        return results
    except (urllib.error.URLError, ET.ParseError) as e:
        print(f"  WARN arXiv '{query}': {e}", file=sys.stderr)
        return []


# ===== Analyse de résonance théorique =====

def detecte_resonance(texte: str, config: dict) -> list:
    """Détecte les indicateurs de résonance théorique dans un texte."""
    indicateurs = config.get("indicateurs_theoriques", [])
    found = []
    for indicateur in indicateurs:
        pattern = r"\b" + re.escape(indicateur) + r"\b"
        if re.search(pattern, texte, re.IGNORECASE):
            found.append(indicateur)
    return found


# ===== Génération de fiche =====

def genere_fiche_github(repo: dict, resonance: list, config: dict) -> tuple:
    """Génère une fiche de veille pour un repo GitHub."""
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(repo["name"])
    owner = repo.get("owner", {}).get("login", "?")

    description = repo.get("description") or "(pas de description)"
    stars = repo.get("stargazers_count", 0)
    forks = repo.get("forks_count", 0)
    language = repo.get("language") or "?"
    licence = repo.get("license", {}).get("spdx_id", "?")
    created = repo.get("created_at", "?")[:10]
    updated = repo.get("updated_at", "?")[:10]
    url = repo.get("html_url", "")
    topics = ", ".join(repo.get("topics", [])[:10]) or "(aucun)"

    # Format de la fiche
    fiche = f"""---
title: "{repo['name']} — veille R&D automatique"
type: experience
statut_experience: exploratoire
tags: [veille, self-improvement, {language.lower()}]
created: {today}
updated: {today}
sources: ["{url}"]
links: []
---

# {repo['name']} — veille R&D automatique

**Source** : repo GitHub détecté automatiquement par veille Studio (cron quotidien).
Recherche déclenchée par mots-clés self-improvement / infrastructure / optimisation.

## Métadonnées

| Champ | Valeur |
|---|---|
| Repo | [{owner}/{repo['name']}]({url}) |
| Description | {description} |
| Langage | {language} |
| ⭐ Stars | {stars} |
| 🍴 Forks | {forks} |
| Licence | {licence} |
| Créé | {created} |
| Mis à jour | {updated} |
| Topics | {topics} |

## Analyse de pertinence

**À compléter par Studio** lors du tour de Choura — évaluation de la résonance avec
l'infrastructure actuelle (Hetzner, providers cloud, multi-gateways Hermes).

## Concepts théoriques extraits

{'**Indicateurs détectés** : ' + ', '.join(resonance) if resonance else '**Aucun indicateur théorique détecté dans les métadonnées disponibles.**'}

**À compléter par Studio** : lire le README complet, extraire les concepts théoriques
pertinents (cf. modèle AngelSpec 2026-08-31 : 5 paradigmes extraits).

## Statut

- ⏳ Clonage sandbox : **en attente validation Sidy** (Cmd 13)
- 📊 Analyse complète : à compléter lors du tour de Choura
- 🏛️ Qualification doctrinale : en attente (Gardien, si résonance détectée)

---

*Fiche générée automatiquement — à enrichir manuellement avant versement.*
"""
    return slug, fiche


def genere_fiche_arxiv(paper: dict, resonance: list, config: dict) -> tuple:
    """Génère une fiche de veille pour un paper arXiv."""
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(paper["title"][:60])
    authors = ", ".join(paper["authors"][:3])
    if len(paper["authors"]) > 3:
        authors += " et al."
    published = paper.get("published", "?")[:10]

    fiche = f"""---
title: "{paper['title'][:80]} — veille R&D automatique"
type: experience
statut_experience: exploratoire
tags: [veille, self-improvement, arxiv, paper]
created: {today}
updated: {today}
sources: ["{paper['link']}"]
links: []
---

# {paper['title']} — veille R&D automatique

**Source** : paper arXiv détecté automatiquement par veille Studio (cron quotidien).
Recherche déclenchée par mots-clés self-improvement / infrastructure / optimisation.

## Métadonnées

| Champ | Valeur |
|---|---|
| Titre | {paper['title']} |
| Auteurs | {authors} |
| Publié | {published} |
| Lien | [{paper['link']}]({paper['link']}) |

## Résumé

{paper['summary'][:1500]}

## Concepts théoriques extraits

{'**Indicateurs détectés** : ' + ', '.join(resonance) if resonance else '**Aucun indicateur théorique détecté dans le résumé.**'}

**À compléter par Studio** : lire le paper complet, extraire les concepts théoriques
pertinents (cf. modèle AngelSpec 2026-08-31 : 5 paradigmes extraits).

## Statut

- 📊 Analyse complète : à compléter lors du tour de Choura
- 🏛️ Qualification doctrinale : en attente (Gardien, si résonance détectée)

---

*Fiche générée automatiquement — à enrichir manuellement avant versement.*
"""
    return slug, fiche


# ===== Point d'entrée =====

def main():
    config = load_config()
    today = datetime.now().strftime("%Y-%m-%d")
    max_fiches = config["api"]["max_fiches_per_run"]

    print(f"[{datetime.now().isoformat()}] Démarrage veille automatique Studio")
    print(f"  Maître-mot : self-improvement")
    print(f"  Max fiches par run : {max_fiches}")

    fiches_generees = 0
    fiches_avec_resonance = 0
    slugs_deja_vus = set()

    # Parcourt les mots-clés
    for mot_cle in config["mots_cles"]:
        print(f"\n--- Mot-clé : {mot_cle} ---")

        # GitHub
        repos = search_github(mot_cle, config)
        for repo in repos:
            if fiches_generees >= max_fiches:
                break

            slug = slugify(repo["name"])
            if slug in slugs_deja_vus:
                continue

            # Évite les doublons avec fiches existantes
            fiche_path = VEILLE_DIR / f"{today}_{slug}.md"
            if fiche_path.exists():
                continue

            if not filtre_github(repo, config):
                continue

            slugs_deja_vus.add(slug)
            texte = f"{repo.get('description', '')} {' '.join(repo.get('topics', []))}"
            resonance = detecte_resonance(texte, config)

            slug_fiche, contenu = genere_fiche_github(repo, resonance, config)
            chemin = VEILLE_DIR / f"{today}_{slug_fiche}.md"
            chemin.write_text(contenu)
            print(f"  ✅ GitHub : {chemin.name}")
            fiches_generees += 1
            if resonance:
                fiches_avec_resonance += 1
                print(f"     🏛️ Résonance : {resonance}")

        # arXiv
        papers = search_arxiv(mot_cle, config)
        for paper in papers:
            if fiches_generees >= max_fiches:
                break

            slug = slugify(paper["title"][:60])
            if slug in slugs_deja_vus:
                continue

            fiche_path = VEILLE_DIR / f"{today}_{slug}.md"
            if fiche_path.exists():
                continue

            slugs_deja_vus.add(slug)
            resonance = detecte_resonance(paper["summary"], config)

            slug_fiche, contenu = genere_fiche_arxiv(paper, resonance, config)
            chemin = VEILLE_DIR / f"{today}_{slug_fiche}.md"
            chemin.write_text(contenu)
            print(f"  ✅ arXiv : {chemin.name}")
            fiches_generees += 1
            if resonance:
                fiches_avec_resonance += 1
                print(f"     🏛️ Résonance : {resonance}")

        if fiches_generees >= max_fiches:
            print(f"\n⏸️  Limite de {max_fiches} fiches atteinte, arrêt.")
            break

    # Résumé pour le cron
    print(f"\n{'=' * 60}")
    print(f"RÉSUMÉ : {fiches_generees} fiche(s) générée(s)")
    print(f"         {fiches_avec_resonance} avec résonance théorique")

    if fiches_avec_resonance > 0:
        print("RESONANCE_DETECTEE")
        return 2  # code de retour = signal pour le cron

    return 0


if __name__ == "__main__":
    sys.exit(main())
