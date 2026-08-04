#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer-karubi.py — outillage déterministe du dispositif Karubi.
Aucun LLM dans la boucle. Trois commandes :

  sceller  <fichier.md>          Calcule le hash des zones scellées et l'écrit
                                 dans le frontmatter (hash_sceau), met à jour
                                 `updated` à la date du jour.
  verifier <fichier.md>          Recalcule le hash des zones scellées et le
                                 compare à hash_sceau. Sortie : SCEAU INTACT /
                                 SCEAU ROMPU. Code retour 0 / 1.
  empreinte <fichier.md>         Affiche le sha256 du fichier ENTIER (à inscrire
                                 comme hash_parent dans les instances filles).

Zones scellées : tout ce qui se trouve entre les marqueurs
  <!-- SCEAU:DEBUT -->  et  <!-- SCEAU:FIN -->
(plusieurs paires possibles). Le hash est le sha256 de la concaténation
des zones, normalisées (fins de ligne \\n, espaces de fin de ligne retirés).

Usage type du cycle de navette (côté Sidy, G0) :
  1. python3 generer-karubi.py verifier karubi-<nom>.md   # au retour du fichier
  2. (édition humaine : §4, §10, silsila si besoin, version: n+1)
  3. python3 generer-karubi.py sceller  karubi-<nom>.md   # re-scellement
  4. journaliser dans registre-silsila.md, commit, rendre le fichier.
"""

import hashlib
import re
import sys
from datetime import date
from pathlib import Path

DEBUT = "<!-- SCEAU:DEBUT -->"
FIN = "<!-- SCEAU:FIN -->"


def lire(chemin: Path) -> str:
    return chemin.read_text(encoding="utf-8")


def zones_scellees(texte: str) -> str:
    """Concatène le contenu de toutes les paires SCEAU:DEBUT/FIN, normalisé."""
    morceaux = []
    pos = 0
    while True:
        d = texte.find(DEBUT, pos)
        if d == -1:
            break
        f = texte.find(FIN, d)
        if f == -1:
            sys.exit("ERREUR : marqueur SCEAU:DEBUT sans SCEAU:FIN — fichier corrompu.")
        bloc = texte[d + len(DEBUT):f]
        lignes = [l.rstrip() for l in bloc.replace("\r\n", "\n").split("\n")]
        morceaux.append("\n".join(lignes).strip())
        pos = f + len(FIN)
    if not morceaux:
        sys.exit("ERREUR : aucune zone scellée trouvée dans ce fichier.")
    return "\n===\n".join(morceaux)


def hash_sceau(texte: str) -> str:
    return hashlib.sha256(zones_scellees(texte).encode("utf-8")).hexdigest()


def champ_frontmatter(texte: str, champ: str) -> str | None:
    m = re.search(rf'^{champ}:\s*"?([^"\n]*)"?\s*$', texte, flags=re.M)
    return m.group(1).strip() if m else None


def remplacer_champ(texte: str, champ: str, valeur: str) -> str:
    motif = rf'^({champ}:\s*).*$'
    if not re.search(motif, texte, flags=re.M):
        sys.exit(f"ERREUR : champ `{champ}` absent du frontmatter.")
    return re.sub(motif, rf'\g<1>"{valeur}"', texte, count=1, flags=re.M)


def cmd_sceller(chemin: Path) -> None:
    texte = lire(chemin)
    empreinte = hash_sceau(texte)
    texte = remplacer_champ(texte, "hash_sceau", empreinte)
    texte = re.sub(r'^(updated:\s*).*$', rf'\g<1>{date.today().isoformat()}',
                   texte, count=1, flags=re.M)
    chemin.write_text(texte, encoding="utf-8")
    print(f"SCELLÉ : {chemin.name}")
    print(f"hash_sceau = {empreinte}")


def cmd_verifier(chemin: Path) -> None:
    texte = lire(chemin)
    inscrit = champ_frontmatter(texte, "hash_sceau")
    calcule = hash_sceau(texte)
    if inscrit == calcule:
        print(f"SCEAU INTACT : {chemin.name}")
        print(f"hash = {calcule}")
        sys.exit(0)
    print(f"SCEAU ROMPU : {chemin.name}")
    print(f"inscrit  = {inscrit}")
    print(f"calculé  = {calcule}")
    print("→ Une zone scellée a été modifiée depuis le dernier scellement G0.")
    sys.exit(1)


def cmd_empreinte(chemin: Path) -> None:
    print(hashlib.sha256(chemin.read_bytes()).hexdigest())


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in ("sceller", "verifier", "empreinte"):
        sys.exit(__doc__)
    chemin = Path(sys.argv[2])
    if not chemin.is_file():
        sys.exit(f"ERREUR : fichier introuvable : {chemin}")
    {"sceller": cmd_sceller,
     "verifier": cmd_verifier,
     "empreinte": cmd_empreinte}[sys.argv[1]](chemin)


if __name__ == "__main__":
    main()
