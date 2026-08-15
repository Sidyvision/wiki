#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
integrer-navette-karubi.py — intégration mécanique d'une navette Karūbī revenue
dans `_inbox/`. Aucun LLM dans la boucle. Réutilise `generer-karubi.py` (vérif.
de sceau) et `ajouter-memoire-karubi.py` (écriture append-only §8/§9) comme
primitives — ne réimplémente ni l'une ni l'autre.

Usage :
  python3 integrer-navette-karubi.py <navette.md> <canonique.md> [--appliquer]

Sans `--appliquer` : mode à blanc (kari-kumi), affiche le rapport, n'écrit rien.
Avec `--appliquer` : applique les ajouts §8/§9 au canonique, archive la navette,
ajoute une entrée dans `registre-silsila.md`.

Ce que ce script NE FAIT JAMAIS :
- Ne touche jamais à §4 (État des travaux) ni §10 (Réponses de Sidy) — ces
  zones sont réservées à Sidy (Cmd 13, porte humaine). Les nouvelles Questions
  §9 sont seulement signalées dans le rapport, jamais répondues.
- Ne recalcule ni ne modifie `hash_sceau` ou `version` — ces champs ne bougent
  que si les zones scellées elles-mêmes changent (jamais le cas en navette
  retour normale) ; laissé à `generer-karubi.py sceller` si besoin, sur décision
  humaine.
- Ne corrige jamais une zone scellée divergente : si la navette a une zone
  scellée différente du canonique, c'est un incident, pas une navette — le
  script s'arrête net, n'écrit rien, signale l'écart pour investigation.
- Ne supprime jamais une navette traitée : elle est déplacée (archivée), jamais
  effacée (Cmd 10).

Étapes :
  1. Vérifie le sceau du canonique (SCEAU INTACT requis).
  2. Compare les zones scellées navette vs canonique — doivent être identiques.
  3. Pour §8 puis §9 : vérifie que le texte du canonique est un PRÉFIXE du texte
     de la navette (garde-fou append-only — un contenu canonique absent de la
     navette est signalé comme incident, pas silencieusement ignoré). Le reste
     (suffixe) est le bloc à ajouter.
  4. Applique chaque bloc via `ajouter-memoire-karubi.py` (si --appliquer).
  5. Archive la navette vers `navettes-archivees/<destinataire>/<horodatage>.md`.
  6. Ajoute une entrée `retour` dans `registre-silsila.md`.
"""

import importlib.util
import re
import sys
import subprocess
from datetime import date, datetime
from pathlib import Path

ICI = Path(__file__).resolve().parent


def _charger_module(nom_fichier: str, nom_module: str):
    chemin = ICI / nom_fichier
    spec = importlib.util.spec_from_file_location(nom_module, chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


generer = _charger_module("generer-karubi.py", "generer_karubi")

SECTION_RE = {
    "8": re.compile(r"^## 8[.\s]", re.M),
    "9": re.compile(r"^## 9[.\s]", re.M),
}
PROCHAINE_SECTION_RE = re.compile(r"^## \d+[.\s]", re.M)


def extraire_section(texte: str, section: str) -> str:
    m = SECTION_RE[section].search(texte)
    if not m:
        sys.exit(f"ERREUR : section §{section} introuvable.")
    debut = texte.find("\n", m.end())
    if debut == -1:
        debut = len(texte)
    else:
        debut += 1
    m2 = PROCHAINE_SECTION_RE.search(texte, debut)
    fin = m2.start() if m2 else len(texte)
    return texte[debut:fin]


def normaliser(texte: str) -> str:
    return "\n".join(l.rstrip() for l in texte.replace("\r\n", "\n").split("\n"))


def calculer_ajout(canon_section: str, nav_section: str) -> str | None:
    """Retourne le bloc ajouté par la navette, ou None si rien de nouveau.
    Sort en erreur (sans rien écrire) si le canonique n'est pas un préfixe de
    la navette — indice d'une violation append-only côté destinataire."""
    c = normaliser(canon_section).rstrip()
    n = normaliser(nav_section).rstrip()
    if c == n:
        return None
    if not n.startswith(c):
        sys.exit(
            "ERREUR : violation append-only détectée — le contenu canonique de "
            "cette section n'est pas un préfixe du contenu de la navette. Cela "
            "signale un contenu canonique absent, modifié ou réordonné côté "
            "navette. Aucune écriture effectuée. Investigation humaine requise."
        )
    ajout = n[len(c):].strip("\n")
    return ajout if ajout.strip() else None


def rapport_zones_scellees(canon_texte: str, nav_texte: str) -> None:
    canon_hash = generer.hash_sceau(canon_texte)
    nav_hash = generer.hash_sceau(nav_texte)
    if canon_hash != nav_hash:
        sys.exit(
            "ERREUR : zones scellées de la navette différentes du canonique.\n"
            f"  hash canonique = {canon_hash}\n"
            f"  hash navette   = {nav_hash}\n"
            "Ceci n'est pas une navette normale — c'est un incident (une zone "
            "scellée ne se modifie jamais hors G0). Aucune écriture effectuée."
        )


def appliquer_ajout(canon_chemin: Path, section: str, bloc: str) -> None:
    subprocess.run(
        [sys.executable, str(ICI / "ajouter-memoire-karubi.py"),
         str(canon_chemin), section, bloc],
        check=True,
    )


def archiver_navette(nav_chemin: Path, destinataire: str) -> Path:
    dossier = ICI / "navettes-archivees" / _slug(destinataire)
    dossier.mkdir(parents=True, exist_ok=True)
    horodatage = datetime_now_str()
    cible = dossier / f"{horodatage}_{nav_chemin.name}"
    nav_chemin.rename(cible)
    return cible


def datetime_now_str() -> str:
    return date.today().isoformat()


def _slug(texte: str) -> str:
    texte = texte.lower()
    remplacements = {"é": "e", "è": "e", "ê": "e", "à": "a", "ï": "i", "ù": "u",
                      "ô": "o", "ç": "c", "ā": "a", "ī": "i", "ū": "u"}
    for a, b in remplacements.items():
        texte = texte.replace(a, b)
    texte = re.sub(r"[^a-z0-9]+", "-", texte).strip("-")
    return texte or "destinataire"


def journaliser_registre(canon_texte: str, ajouts: dict, nav_nom: str) -> str:
    dest = generer.champ_frontmatter(canon_texte, "destinataire") or "?"
    gen = generer.champ_frontmatter(canon_texte, "generation") or "?"
    portee = generer.champ_frontmatter(canon_texte, "portee") or "?"
    version = generer.champ_frontmatter(canon_texte, "version") or "?"
    hash_sceau = generer.champ_frontmatter(canon_texte, "hash_sceau") or "?"

    n8 = 1 if ajouts.get("8") else 0
    n9 = 1 if ajouts.get("9") else 0
    parties = []
    if n8:
        parties.append("un ajout en §8 (Mémoire vivante)")
    if n9:
        parties.append("un ajout en §9 (Questions pour Sidy — réponse en §10 en attente)")
    resume = " et ".join(parties) if parties else "aucun ajout détecté"

    entree = (
        f"## [{date.today().isoformat()}] retour | {dest} | G{gen} | {portee} | "
        f"v{version} | {hash_sceau}\n"
        f"Fichier revenu via `_inbox/` (`{nav_nom}`) — intégré par "
        f"`integrer-navette-karubi.py`. Sceau vérifié : INTACT, zones scellées "
        f"identiques au canonique. {resume.capitalize()}. Archivé sous "
        f"`navettes-archivees/{_slug(dest)}/`.\n"
    )
    return entree


def inserer_dans_registre(entree: str) -> None:
    chemin = ICI / "registre-silsila.md"
    texte = chemin.read_text(encoding="utf-8")
    marqueur = "<!-- INSERTION: QUEUE -->"
    if marqueur not in texte:
        sys.exit("ERREUR : marqueur d'insertion introuvable dans registre-silsila.md.")
    pos = texte.find(marqueur) + len(marqueur)
    fin_ligne = texte.find("\n", pos) + 1
    nouveau_texte = texte[:fin_ligne] + "\n" + entree + texte[fin_ligne:]
    chemin.write_text(nouveau_texte, encoding="utf-8")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--appliquer"]
    appliquer = "--appliquer" in sys.argv
    if len(args) != 2:
        sys.exit(__doc__)

    nav_chemin, canon_chemin = Path(args[0]), Path(args[1])
    if not nav_chemin.is_file():
        sys.exit(f"ERREUR : navette introuvable : {nav_chemin}")
    if not canon_chemin.is_file():
        sys.exit(f"ERREUR : canonique introuvable : {canon_chemin}")

    canon_texte = canon_chemin.read_text(encoding="utf-8")
    nav_texte = nav_chemin.read_text(encoding="utf-8")

    inscrit = generer.champ_frontmatter(canon_texte, "hash_sceau")
    calcule = generer.hash_sceau(canon_texte)
    if inscrit != calcule:
        sys.exit(f"ERREUR : SCEAU ROMPU sur le canonique {canon_chemin.name} — abandon.")
    print(f"Sceau canonique : INTACT ({calcule[:12]}…)")

    rapport_zones_scellees(canon_texte, nav_texte)
    print("Zones scellées navette = canonique : OK")

    ajouts = {}
    for section in ("8", "9"):
        bloc = calculer_ajout(
            extraire_section(canon_texte, section),
            extraire_section(nav_texte, section),
        )
        if bloc:
            ajouts[section] = bloc
            print(f"\n--- Ajout détecté en §{section} ---\n{bloc}\n")
        else:
            print(f"§{section} : rien de nouveau.")

    if not ajouts:
        print("\nAucun ajout à intégrer. Rien à faire.")
        return

    print("\nRappel : §4 (État des travaux) et §10 (Réponses de Sidy) ne sont "
          "jamais touchés par ce script — à traiter séparément (relecture "
          "humaine, éventuel brouillon §4 via le rôle G0 dédié).")

    if not appliquer:
        print("\n[mode à blanc — relancer avec --appliquer pour écrire]")
        return

    for section, bloc in ajouts.items():
        appliquer_ajout(canon_chemin, section, bloc)

    dest = generer.champ_frontmatter(canon_texte, "destinataire") or "destinataire"
    archive = archiver_navette(nav_chemin, dest)
    print(f"\nNavette archivée : {archive}")

    entree = journaliser_registre(canon_texte, ajouts, nav_chemin.name)
    inserer_dans_registre(entree)
    print("Entrée ajoutée dans registre-silsila.md :")
    print(entree)


if __name__ == "__main__":
    main()
