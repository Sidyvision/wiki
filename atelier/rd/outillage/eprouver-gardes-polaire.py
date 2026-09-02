#!/usr/bin/env python3
# =============================================================================
# eprouver-gardes-polaire.py — les huit gardes du bloc `polaire:` refusent-elles ?
#
#   Chantier INS-15. Outillage versé au dépôt (étape 6 bis du plan visé).
#
#   « Un contrôle dont on n'a pas vu l'échec n'est pas un contrôle vérifié »
#   (§VII du protocole racine, Épreuve des contrôles — motifs PRO-01 et INF-14).
#
#   Ce script fabrique, une par une, la faute exacte que chaque garde doit
#   attraper, la présente au générateur DANS UNE COPIE JETABLE du dépôt, et
#   vérifie qu'il REFUSE en nommant la bonne garde. Il ne touche jamais le dépôt
#   vivant : la copie est faite dans un répertoire temporaire, détruit à la fin.
#
#   Il vérifie aussi le cas sain — condition nécessaire, jamais suffisante.
#
#   Usage :  python3 atelier/rd/outillage/eprouver-gardes-polaire.py
#            python3 …/eprouver-gardes-polaire.py --repo /root/wiki
# =============================================================================

import argparse
import copy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERREUR : PyYAML manquant. Installer avec : apt install python3-yaml")


# --- Les fautes. Une par garde. Chacune dit ce qu'elle casse et ce qu'on attend. --

def f_g1(d):
    """G1 — le cercle arctique n'est pas une valeur libre : il EST 90 - obliquité."""
    d["polaire"]["latitude_min_deg"] = 60.0

def f_g2(d):
    """G2 — la station par défaut doit rester dans le domaine du module."""
    d["polaire"]["latitude_deg"] = 45.0

def f_g3(d):
    """G3 — redéclarer ce qui vit dans `zodiaque:` est un doublon (Cmd 14)."""
    d["polaire"]["obliquite_deg"] = 23.44          # même valeur : le doublon reste un doublon

def f_g4(d):
    """G4 — un statut hors énumération ne commande aucun style de rendu."""
    d["polaire"]["cycles"]["statut"] = "certain"

def f_g5(d):
    """G5 — les quatre Yugas hors proportion 4:3:2:1 : la roue serait fausse."""
    d["polaire"]["cycles"]["yugas"][3]["ans"] = 6500

def f_g6(d):
    """G6 — les deux jeux de Tilak sont complets ou absents, jamais à moitié."""
    d["polaire"]["caracteristiques"].pop()

def f_g7(d):
    """G7 — rien n'est asserté sans source, QUEL QUE SOIT le statut.
    La faute est enfouie à dessein : c'est exactement celle qui était passée
    inaperçue (un seuil crépusculaire conventionnel, sans source)."""
    d["polaire"]["seuils_crepusculaires"].pop("source")

def f_g8(d):
    """G8 — un scalaire nu à la racine du bloc fait passer une convention pour
    un fait. C'est la faute prise à sa racine, non dans son occurrence."""
    d["polaire"]["crepuscule_deg"] = -18.0


GARDES = [
    ("G1", "cercle arctique ≠ 90 - obliquité",        f_g1, "latitude_min_deg"),
    ("G2", "station par défaut hors domaine",          f_g2, "latitude_deg"),
    ("G3", "redéclaration d'une clé de `zodiaque:`",   f_g3, "redéclaration interdite"),
    ("G4", "statut hors énumération",                  f_g4, "statut invalide"),
    ("G5", "Yugas hors proportion 4:3:2:1",            f_g5, "proportions"),
    ("G6", "un jeu de caractères incomplet",           f_g6, "les deux jeux de"),
    ("G7", "statut sans source (enfoui)",              f_g7, "sans « source »"),
    ("G8", "scalaire conventionnel nu",                f_g8, "scalaire nu"),
]


def executer(repo_bac):
    """Lance le générateur sur le bac à sable. Rend (code, sortie complète)."""
    r = subprocess.run(
        [sys.executable, str(repo_bac / "atelier/rd/outillage/generer-manifeste.py"),
         "--repo", str(repo_bac)],
        capture_output=True, text=True,
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/root/wiki")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()

    rel_yaml = "atelier/rd/instrument/instrument-donnees.yaml"
    sain = yaml.safe_load((repo / rel_yaml).read_text(encoding="utf-8"))
    if not sain.get("polaire"):
        sys.exit("ERREUR : aucun bloc `polaire:` dans " + rel_yaml)

    print("=" * 92)
    print("INS-15 — épreuve des huit gardes du bloc `polaire:`")
    print("Bac à sable jetable ; le dépôt vivant n'est jamais modifié.")
    print("=" * 92)

    resultats = []
    with tempfile.TemporaryDirectory(prefix="eprouve-polaire-") as tmp:
        bac = Path(tmp) / "wiki"
        # On ne copie que ce dont le générateur a besoin : la donnée et l'outil.
        for sous in ("atelier/rd/instrument", "atelier/rd/outillage", "doctrinal"):
            shutil.copytree(repo / sous, bac / sous, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))

        # --- Passe 1 : l'état sain doit PASSER. Nécessaire, jamais suffisant.
        code, sortie = executer(bac)
        sain_ok = (code == 0)
        print("\nPASSE 1 — état sain : le générateur doit ACCEPTER")
        print("-" * 92)
        print("  {}  état sain".format("OK  " if sain_ok else "ÉCHEC"))
        if not sain_ok:
            print("      " + sortie.strip().replace("\n", "\n      "))
        # Le rapport doit ANNONCER le bloc : un rapport muet peut masquer une absence.
        annonce = "polaire inclus" in sortie
        print("  {}  le rapport annonce « polaire inclus »".format("OK  " if annonce else "ÉCHEC"))

        # --- Passe 2 : chaque faute doit être REFUSÉE, et par la bonne garde.
        print("\nPASSE 2 — chaque garde doit REFUSER sa faute (§VII, motif PRO-01)")
        print("-" * 92)
        for nom, titre, faute, attendu in GARDES:
            casse = copy.deepcopy(sain)
            faute(casse)
            (bac / rel_yaml).write_text(
                yaml.safe_dump(casse, allow_unicode=True, sort_keys=False), encoding="utf-8")
            code, sortie = executer(bac)
            refuse = (code != 0)
            bonne = attendu in sortie
            ok = refuse and bonne
            resultats.append(ok)
            detail = ("refus, garde nommée" if ok
                      else "REFUS SANS LE BON MOTIF" if refuse
                      else "ACCEPTÉ — la garde ne voit rien")
            print("  {}  {} — {:<38} {}".format(
                "OK  " if ok else "ÉCHEC", nom, titre, detail))
            if not ok:
                lignes = [l for l in sortie.splitlines() if "ERREUR" in l or "VERDICT" in l]
                for l in lignes[:3]:
                    print("        " + l.strip())
            # Remettre l'état sain avant la faute suivante.
            (bac / rel_yaml).write_text(
                yaml.safe_dump(sain, allow_unicode=True, sort_keys=False), encoding="utf-8")

    print("\n" + "=" * 92)
    tout = sain_ok and annonce and all(resultats)
    if tout:
        print("VERDICT : l'état sain passe, et les {} gardes refusent chacune SA faute.".format(
            len(resultats)))
        print("          Les gardes observent donc quelque chose de réel.")
    else:
        if not sain_ok:
            print("VERDICT : l'état sain est REFUSÉ — la donnée ou l'outil est en faute.")
        if not annonce:
            print("VERDICT : le rapport n'annonce pas le bloc polaire — il pourrait taire son absence.")
        if not all(resultats):
            print("VERDICT : {} garde(s) INOPÉRANTE(S) — elles n'attrapent pas ce "
                  "qu'elles prétendent garder.".format(resultats.count(False)))
    print("=" * 92)
    return 0 if tout else 1


if __name__ == "__main__":
    sys.exit(main())
