#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer-karubi.py — outillage déterministe du dispositif Karubi.
Aucun LLM dans la boucle. Six commandes :

  sceller  <fichier.md>          Calcule le hash des zones scellées et l'écrit
                                 dans le frontmatter (hash_sceau), met à jour
                                 `updated` à la date du jour.
  verifier <fichier.md>          Recalcule le hash des zones scellées et le
                                 compare à hash_sceau. Sortie : SCEAU INTACT /
                                 SCEAU ROMPU. Code retour 0 / 1.
  empreinte <fichier.md>         Affiche le sha256 du fichier ENTIER (à inscrire
                                 comme hash_parent dans les instances filles).
  statut <fichier.md>            Résumé concis : état du sceau, version, portée,
                                 destinataire, date dernière modif., nb de zones.
  diff <fichier.md> <fichier.md> Compare deux versions d'un même Karūbī : zones
                                 scellées modifiées, entrées §8/§9 ajoutées.
  index <dossier>                Liste tous les fichiers Karūbī d'un dossier avec
                                 leur état de sceau (INTACT/ROMPU), version, hash.

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
    m = re.search(rf'^{champ}:\s*"?([^"\n]*)"?', texte, flags=re.M)
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


def cmd_statut(chemin: Path) -> None:
    texte = lire(chemin)
    titre = champ_frontmatter(texte, "title") or "(sans titre)"
    version = champ_frontmatter(texte, "version") or "?"
    portee = champ_frontmatter(texte, "portee") or "?"
    dest = champ_frontmatter(texte, "destinataire") or "?"
    updated = champ_frontmatter(texte, "updated") or "?"
    hash_inscrit = champ_frontmatter(texte, "hash_sceau") or "(non scellé)"
    calcule = hash_sceau(texte)
    etat = "INTACT" if hash_inscrit == calcule else "ROMPU"
    nb_zones = zones_scellees(texte).count("===") + 1

    print(f"Fichier : {chemin.name}")
    print(f"Titre : {titre}")
    print(f"Destinataire : {dest}")
    print(f"Version : {version}")
    print(f"Portée : {portee}")
    print(f"Dernière mise à jour : {updated}")
    print(f"État du sceau : {etat}")
    print(f"Hash inscrit : {hash_inscrit}")
    print(f"Hash calculé : {calcule}")
    print(f"Nombre de zones scellées : {nb_zones}")


def cmd_diff(ancien_path: Path, nouveau_path: Path) -> None:
    ancien_texte = lire(ancien_path)
    nouveau_texte = lire(nouveau_path)

    ancien_hash = champ_frontmatter(ancien_texte, "hash_sceau") or "(non scellé)"
    nouveau_hash = champ_frontmatter(nouveau_texte, "hash_sceau") or "(non scellé)"

    ancien_zones = zones_scellees(ancien_texte).split("\n===\n")
    nouveau_zones = zones_scellees(nouveau_texte).split("\n===\n")

    print(f"Comparaison : {ancien_path.name} → {nouveau_path.name}")
    print(f"Ancien hash : {ancien_hash}")
    print(f"Nouveau hash : {nouveau_hash}")
    print()

    if ancien_hash == nouveau_hash:
        print("✓ Zones scellées identiques (aucune modification).")
    else:
        print(f"✗ Zones scellées MODIFIÉES ({len(ancien_zones)} → {len(nouveau_zones)} zones)")
        for i, (a, n) in enumerate(zip(ancien_zones, nouveau_zones), 1):
            if a != n:
                print(f"  Zone {i} : contenu différent")

    # Comparer §8 et §9
    def extraire_section(texte: str, section: str) -> str:
        pattern = re.compile(rf"^## {section}[.\s](.*?)(?=^## |\Z)", re.M | re.S)
        m = pattern.search(texte)
        return m.group(1).strip() if m else ""

    for sec in ["8", "9"]:
        ancien_sec = extraire_section(ancien_texte, sec)
        nouveau_sec = extraire_section(nouveau_texte, sec)
        if ancien_sec == nouveau_sec:
            print(f"✓ §{sec} inchangé")
        else:
            ancien_lignes = set(ancien_sec.split("\n"))
            nouveau_lignes = set(nouveau_sec.split("\n"))
            ajoutees = nouveau_lignes - ancien_lignes
            retires = ancien_lignes - nouveau_lignes
            if retires:
                print(f"✗ §{sec} : {len(retires)} ligne(s) retirée(s) (violation append-only)")
            if ajoutees:
                print(f"+ §{sec} : {len(ajoutees)} entrée(s) ajoutée(s)")


def cmd_index(dossier: Path) -> None:
    if not dossier.is_dir():
        sys.exit(f"ERREUR : dossier introuvable : {dossier}")

    fichiers = sorted(dossier.glob("karubi-*.md"))
    if not fichiers:
        print(f"Aucun fichier Karūbī trouvé dans {dossier}")
        return

    print(f"Index des Karūbī dans {dossier} ({len(fichiers)} fichier(s))")
    print("-" * 60)

    for f in fichiers:
        texte = lire(f)
        titre = champ_frontmatter(texte, "title") or "(sans titre)"
        dest = champ_frontmatter(texte, "destinataire") or "?"
        version = champ_frontmatter(texte, "version") or "?"
        hash_inscrit = champ_frontmatter(texte, "hash_sceau") or "(non scellé)"
        calcule = hash_sceau(texte)
        etat = "INTACT" if hash_inscrit == calcule else "ROMPU"

        print(f"{f.name:40} v{version:2} {etat:6} {dest}")


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)

    cmd = sys.argv[1]
    if cmd in ("sceller", "verifier", "empreinte", "statut"):
        if len(sys.argv) != 3:
            sys.exit(__doc__)
        chemin = Path(sys.argv[2])
        if not chemin.is_file():
            sys.exit(f"ERREUR : fichier introuvable : {chemin}")
        {"sceller": cmd_sceller,
         "verifier": cmd_verifier,
         "empreinte": cmd_empreinte,
         "statut": cmd_statut}[cmd](chemin)

    elif cmd == "diff":
        if len(sys.argv) != 4:
            sys.exit(__doc__)
        cmd_diff(Path(sys.argv[2]), Path(sys.argv[3]))

    elif cmd == "index":
        if len(sys.argv) != 3:
            sys.exit(__doc__)
        cmd_index(Path(sys.argv[2]))

    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
