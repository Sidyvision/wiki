#!/usr/bin/env python3
# =============================================================================
# comparer-geometrie-rendu.py — le RENDU calcule-t-il la géométrie contrôlée ?
#
#   Chantier INS-15. Versé au dépôt le 2026-09-02 (étape 6 bis du plan visé).
#
#   `verifier-geometrie-polaire.py` contrôle des formules écrites EN PYTHON. Le
#   rendu, lui, tourne en JavaScript, dans un autre dépôt. Rien ne garantit que
#   les deux se rejoignent : le contrôle pourrait passer sur une implémentation
#   pendant que la scène en dessine une autre.
#
#   Ce script EXTRAIT les fonctions de géométrie du fichier de rendu — telles
#   quelles, sans les recopier — les exécute sous Node avec un Vector3 minimal,
#   et confronte leurs sorties à la référence Python sur une grille de cas.
#
#   Recopier les fonctions ici produirait un contrôle qui s'observe lui-même :
#   c'est le motif PRO-01, et c'est ce qu'on évite en les lisant dans le fichier
#   RÉELLEMENT SERVI.
#
#   Le sens unique est respecté : ce script LIT le dépôt frère, il n'y écrit
#   jamais (§VII, règle 5 des manifestes).
#
#   Usage :
#     python3 atelier/rd/outillage/comparer-geometrie-rendu.py
#     python3 …/comparer-geometrie-rendu.py --rendu /root/instrument/src/index.html
#     python3 …/comparer-geometrie-rendu.py --fausser     # DOIT détecter
# =============================================================================

import argparse
import importlib.util
import json
import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
NOMS = ["declinaison", "baseLocale", "directionSoleil", "hauteur", "azimut",
        "angleHoraire", "moisDeSoleil"]

SHIM = """
class Vector3 {
  constructor(x=0,y=0,z=0){ this.x=x; this.y=y; this.z=z; }
  addScaledVector(v,s){ this.x+=v.x*s; this.y+=v.y*s; this.z+=v.z*s; return this; }
}
const THREE = { Vector3 };
var d2r = function(d){ return d * Math.PI / 180; };
var r2d = function(r){ return r * 180 / Math.PI; };
var ANNEE = 365.24;
var etat = { obl: 23.44, lat: 90 };
"""


def extraire(source, nom):
    """Capture « function <nom>( … ) { … } » jusqu'à l'accolade de même niveau."""
    i = source.find("function " + nom + "(")
    if i < 0:
        raise SystemExit(f"ERREUR : fonction introuvable dans le rendu : {nom}")
    j = source.index("{", i)
    niveau = 0
    for k in range(j, len(source)):
        if source[k] == "{":
            niveau += 1
        elif source[k] == "}":
            niveau -= 1
            if niveau == 0:
                return source[i:k + 1]
    raise SystemExit(f"ERREUR : accolade non refermée : {nom}")


def sorties_du_rendu(chemin_rendu):
    html = Path(chemin_rendu).read_text(encoding="utf-8")
    corps = SHIM + "\n".join(extraire(html, n) for n in NOMS)
    pilote = corps + """
const cas = [];
for (const lat of [90, 89, 80, 70, 66.56, 60, 45]) {
  for (let jour = 0; jour < 365; jour += 37) {
    for (let H = 0; H < 360; H += 47) {
      etat.obl = 23.44; etat.lat = lat;
      const dec = declinaison(jour);
      const v = directionSoleil(lat, dec, H);
      cas.push({lat, jour, H, dec, h: hauteur(v), a: azimut(v), mois: moisDeSoleil(lat)});
    }
  }
}
process.stdout.write(JSON.stringify(cas));
"""
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(pilote)
        tmp = f.name
    try:
        r = subprocess.run(["node", tmp], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit("ERREUR Node :\n" + (r.stderr or ""))
        return json.loads(r.stdout)
    finally:
        os.unlink(tmp)


def charger_reference():
    spec = importlib.util.spec_from_file_location(
        "geo", ICI / "verifier-geometrie-polaire.py")
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass          # le module exécute ses propres contrôles ; on ne veut que ses fonctions
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rendu", default="/root/instrument/src/index.html")
    ap.add_argument("--fausser", action="store_true",
                    help="injecte 1° dans la référence — la comparaison DOIT le détecter")
    args = ap.parse_args()

    geo = charger_reference()
    cas = sorties_du_rendu(args.rendu)
    biais = 1.0 if args.fausser else 0.0
    TOL = 1e-9

    pire_d = pire_h = pire_a = pire_m = 0.0
    for c in cas:
        dec = geo.declinaison(c["jour"]) + biais
        pire_d = max(pire_d, abs(dec - c["dec"]))
        pire_h = max(pire_h, abs(geo.hauteur(c["lat"], dec, c["H"]) - c["h"]))
        da = abs(geo.azimut(c["lat"], dec, c["H"]) - c["a"]) % 360.0
        pire_a = max(pire_a, min(da, 360.0 - da))
        pire_m = max(pire_m, abs(geo.mois_de_soleil(c["lat"] + biais) - c["mois"]))

    print("=" * 92)
    print("Concordance RENDU ↔ contrôle sur {} cas{}".format(
        len(cas), "  [RÉFÉRENCE FAUSSÉE de 1°]" if args.fausser else ""))
    print("  rendu lu : {}".format(args.rendu))
    print("=" * 92)
    print("  déclinaison    : écart max {:.3e}°".format(pire_d))
    print("  hauteur        : écart max {:.3e}°".format(pire_h))
    print("  azimut         : écart max {:.3e}°".format(pire_a))
    print("  mois de soleil : écart max {:.3e}".format(pire_m))

    concordent = max(pire_d, pire_h, pire_a, pire_m) <= TOL
    if args.fausser:
        if concordent:
            print("\nÉCHEC : la comparaison n'a rien vu alors que la référence était")
            print("        faussée — elle ne compare donc rien.")
            return 1
        print("\nOK : la comparaison DÉTECTE la divergence introduite.")
        return 0
    if concordent:
        print("\nOK : le rendu et le contrôle calculent la MÊME géométrie "
              "(écart < {:.0e}°).".format(TOL))
        return 0
    print("\nÉCHEC : le rendu ne calcule pas ce que le contrôle valide.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
