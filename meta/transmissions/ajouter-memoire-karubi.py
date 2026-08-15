#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ajouter-memoire-karubi.py — append-only déterministe pour §8 et §9 des
fichiers Karūbī. Aucun LLM dans la boucle.

Usage :
  python3 ajouter-memoire-karubi.py <fichier.md> 8 "<texte à ajouter>"
  python3 ajouter-memoire-karubi.py <fichier.md> 9 "<texte à ajouter>"

Règles :
- N'écrit QUE sous les marqueurs `## 8.` (ou `## 9.`) respectifs.
- Refuse si un marqueur `<!-- SCEAU:` se trouve après le point d'insertion
  prévu (garde-fou anti-erreur de parsing).
- Ne recalcule ni ne modifie `hash_sceau` (les zones de croissance sont
  hors du périmètre de `zones_scellees()` dans `generer-karubi.py`).
- Chaque entrée doit être datée et signée (convention Karūbī :
  "- [YYYY-MM-DD] — le Karūbī : …" ou "- [YYYY-MM-DD] — <prenom> : …").
  Le texte passé en argument est inséré tel quel.
"""

import sys
import re
from pathlib import Path

DEBUT = "<!-- SCEAU:DEBUT -->"
FIN = "<!-- SCEAU:FIN -->"

SECTIONS = {
    "8": re.compile(r"^## 8[.\s]", re.M),
    "9": re.compile(r"^## 9[.\s]", re.M),
}


def localiser_section(texte: str, section: str) -> int:
    """Retourne l'index de la ligne suivant le titre de section (point d'insertion)."""
    m = SECTIONS[section].search(texte)
    if not m:
        sys.exit(f"ERREUR : section {section} introuvable dans le fichier.")
    # point d'insertion : juste après la ligne du titre
    debut_ligne = texte.rfind("\n", 0, m.start()) + 1
    fin_ligne = texte.find("\n", m.end())
    if fin_ligne == -1:
        fin_ligne = len(texte)
    return fin_ligne + 1  # après le \n du titre


def verifier_pas_de_sceau_apres(texte: str, pos_insertion: int) -> None:
    """Refuse si un marqueur SCEAU apparaît après le point d'insertion."""
    reste = texte[pos_insertion:]
    if DEBUT in reste or FIN in reste:
        sys.exit(
            "ERREUR : marqueur SCEAU détecté après le point d'insertion prévu.\n"
            "Cela indique un problème de structure du fichier. Abandon sans écriture."
        )


def trouver_fin_section(texte: str, section: str, pos_insertion: int) -> int:
    """Retourne la position de fin de la section (début de la section suivante
    ou EOF), pour insérer à la fin de la zone de croissance concernée."""
    # Cherche la prochaine section (## N.) après le point d'insertion
    pattern = re.compile(r"^## \d+[.\s]", re.M)
    m = pattern.search(texte, pos_insertion)
    if m:
        return m.start()
    return len(texte)


def cmd_ajouter(chemin: Path, section: str, texte_a_ajouter: str) -> None:
    if section not in SECTIONS:
        sys.exit(f"ERREUR : section invalide '{section}'. Attendu : 8 ou 9.")

    texte = chemin.read_text(encoding="utf-8")
    pos_insertion = localiser_section(texte, section)
    verifier_pas_de_sceau_apres(texte, pos_insertion)

    # Insérer à la fin de la section (avant la prochaine ## ou EOF)
    fin_section = trouver_fin_section(texte, section, pos_insertion)

    # Préparer l'entrée : préfixer d'un saut de ligne si la section n'est pas vide
    prefixe = ""
    if fin_section > pos_insertion and texte[pos_insertion:fin_section].strip():
        prefixe = "\n"
    suffixe = "\n" if not texte.endswith("\n") else ""

    nouvelle_entree = prefixe + texte_a_ajouter.rstrip() + "\n" + suffixe
    nouveau_texte = texte[:fin_section] + nouvelle_entree + texte[fin_section:]

    chemin.write_text(nouveau_texte, encoding="utf-8")
    print(f"AJOUTÉ §{section} : {chemin.name}")
    print(f"Entrée ({len(texte_a_ajouter)} caractères) insérée en position {fin_section}.")


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    chemin = Path(sys.argv[1])
    section = sys.argv[2]
    texte_a_ajouter = sys.argv[3]

    if not chemin.is_file():
        sys.exit(f"ERREUR : fichier introuvable : {chemin}")
    cmd_ajouter(chemin, section, texte_a_ajouter)


if __name__ == "__main__":
    main()
