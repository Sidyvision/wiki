#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Épreuve du §VII de `verifier-hygiene-unicode.py`.

« Un contrôle dont on n'a pas vu l'échec n'est pas un contrôle vérifié. »

Ce script ne contrôle rien : il fabrique les fautes exactes que l'instrument doit
attraper et vérifie qu'il les attrape. Sortie 1 si une seule épreuve échoue.

Comme l'instrument, il n'écrit AUCUN caractère invisible en littéral : toute
injection passe par `chr(0x…)`. Les deux fichiers doivent pouvoir se scanner
mutuellement sans se déclencher — c'est l'objet de E4.

Six épreuves :
  E1  VERT        — sur un fichier sain, 0 violation et code 0.
  E2  ÉCHEC VU    — chacun des six codepoints du Cmd 15 est injecté SÉPARÉMENT.
                    Éprouver le jeu en bloc laisserait passer un membre oublié
                    du dictionnaire : c'est précisément la faute qui rend un
                    contrôle muet. Chaque membre doit être vu, et faire sortir
                    en code 1.
  E3  FRONTIÈRE   — bidi et saut de page sont comptés HORS Cmd 15, laissent le
                    code à 0, et n'incrémentent PAS le compte Cmd 15. La
                    frontière du jeu nommé par le commandement ne se franchit
                    pas dans un instrument (précédent : E1d de
                    `eprouver-mesure-ocr-arabe.py`). Avec --strict, ils font
                    bien échouer — sans quoi l'option ne servirait à rien.
  E4  AUTOSCAN    — l'instrument et cette épreuve, scannés par l'instrument,
                    doivent être PROPRES. Vérifie la discipline d'écriture en
                    échappements : un instrument porteur de ce qu'il traque est
                    la faute du 2026-09-14.
  E5  BINAIRE     — un fichier à octets nuls est ignoré, non signalé à tort, et
                    ne fait pas planter l'instrument (code 2 interdit).
  E6  POSITION    — ligne et colonne rapportées sont exactes. Un contrôle qui
                    voit juste mais situe faux n'est pas réparable à la main.
  E7  EXCEPTION   — un résidu tranché, déclaré au compte exact, cesse d'être
                    rapporté : un contrôle bruyant cesse d'être lu (motif
                    OUT-C2).
  E8  EXCÉDENT    — clause portante du registre. Au-delà du compte déclaré,
                    l'excédent RESTE bloquant. Une exception qui couvrirait un
                    fichier en bloc absorberait en silence toute contamination
                    ultérieure : ce serait une qualification implicite rendue
                    sans être avouée, soit la faute même que consigne la fiche
                    d'incident du 2026-09-14.
  E9  CADUQUE     — une exception devenue sans objet est signalée, pour que le
                    registre ne pourrisse pas en couverture dormante.
  E10 ÉTAT BRUT   — `--sans-exceptions` restitue l'état non filtré. Un registre
                    qu'aucune commande ne lève est un point aveugle.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
INSTRUMENT = ICI / "verifier-hygiene-unicode.py"

CMD15 = (0x200B, 0x200C, 0x200D, 0xFEFF, 0x200E, 0x200F)
BIDI = (0x202A, 0x202B, 0x202C, 0x202E, 0x2066, 0x2069)
PAGE = (0x000C, 0x000B)

SAIN = "Ligne une, sans rien d'invisible.\nLigne deux.\nLigne trois.\n"


def lancer(chemins, strict=False, exceptions=None, sans_exceptions=True):
    """Retourne (code, dict JSON) de l'instrument sur des chemins explicites.

    `sans_exceptions=True` par défaut : les épreuves E1 à E6 portent sur la
    détection nue et ne doivent pas dépendre du registre réel du dépôt, qui
    change. Les épreuves E7 à E10 fournissent leur propre registre.
    """
    cmd = [sys.executable, str(INSTRUMENT), "--json", "--racine", str(ICI.parent.parent.parent)]
    if strict:
        cmd.append("--strict")
    if exceptions is not None:
        cmd += ["--exceptions", str(exceptions)]
    elif sans_exceptions:
        cmd.append("--sans-exceptions")
    cmd += [str(c) for c in chemins]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return r.returncode, json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.returncode, None


def main():
    echecs = []
    tmp = Path(tempfile.mkdtemp(prefix="eprouve-unicode-"))

    # --- E1 : vert sur fichier sain ---------------------------------------
    f = tmp / "sain.txt"
    f.write_text(SAIN, encoding="utf-8")
    code, d = lancer([f])
    ok = code == 0 and d is not None and d["violations_cmd15"] == 0
    print(f"E1  VERT        code={code} violations={d['violations_cmd15'] if d else '?'}  "
          f"{'✅' if ok else '❌ attendu 0 violation et code 0'}")
    if not ok:
        echecs.append("E1 : l'instrument signale une faute sur un fichier sain")

    # --- E2 : chaque membre du Cmd 15, séparément -------------------------
    for point in CMD15:
        f = tmp / f"cmd15-{point:04X}.txt"
        f.write_text(f"avant{chr(point)}apres\n", encoding="utf-8")
        code, d = lancer([f])
        vu = d is not None and d["violations_cmd15"] == 1
        ok = vu and code == 1
        print(f"E2  ÉCHEC VU    U+{point:04X}  code={code} violations="
              f"{d['violations_cmd15'] if d else '?'}  "
              f"{'✅ vu' if ok else '❌ NON VU — contrôle muet sur ce codepoint'}")
        if not ok:
            echecs.append(f"E2 : U+{point:04X} non détecté, ou code de sortie erroné")

    # --- E3 : frontière du Cmd 15 -----------------------------------------
    corps = "".join(f"x{chr(p)}y\n" for p in BIDI + PAGE)
    f = tmp / "hors-cmd15.txt"
    f.write_text(corps, encoding="utf-8")
    code, d = lancer([f])
    attendu = len(BIDI) + len(PAGE)
    ok = (code == 0 and d is not None
          and d["violations_cmd15"] == 0
          and d["signalements_hors_cmd15"] == attendu)
    print(f"E3  FRONTIÈRE   code={code} cmd15={d['violations_cmd15'] if d else '?'} "
          f"hors={d['signalements_hors_cmd15'] if d else '?'} (attendu 0 / {attendu})  "
          f"{'✅' if ok else '❌ frontière franchie ou signalement manqué'}")
    if not ok:
        echecs.append("E3 : bidi/mise en page fondus dans le Cmd 15, ou non vus")

    code_s, _ = lancer([f], strict=True)
    ok_s = code_s == 1
    print(f"E3b STRICT      code={code_s}  "
          f"{'✅ --strict fait échouer' if ok_s else '❌ --strict sans effet'}")
    if not ok_s:
        echecs.append("E3b : --strict ne fait pas échouer sur un signalement")

    # --- E4 : l'instrument et l'épreuve se scannent sans se déclencher -----
    code, d = lancer([INSTRUMENT, Path(__file__).resolve()])
    ok = code == 0 and d is not None and d["violations_cmd15"] == 0
    print(f"E4  AUTOSCAN    code={code} violations={d['violations_cmd15'] if d else '?'}  "
          f"{'✅ écriture en échappements tenue' if ok else '❌ instrument porteur de ce qu il traque'}")
    if not ok:
        echecs.append("E4 : l'instrument ou son épreuve contient un invisible littéral")

    # --- E5 : binaire ignoré sans planter ---------------------------------
    f = tmp / "binaire.bin"
    f.write_bytes(bytes([0x00, 0xFF, 0xFE, 0x41, 0x00, 0x42]))
    code, d = lancer([f])
    ok = code == 0 and d is not None and d["fichiers_ignores"] == 1 and d["fichiers_lus"] == 0
    print(f"E5  BINAIRE     code={code} ignores={d['fichiers_ignores'] if d else '?'}  "
          f"{'✅ ignoré proprement' if ok else '❌ signalé à tort, ou plantage'}")
    if not ok:
        echecs.append("E5 : fichier binaire mal traité (code 2 ou faux positif)")

    # --- E6 : position exacte ---------------------------------------------
    # L'invisible est placé ligne 3, colonne 5 : "abcd" puis le caractère.
    f = tmp / "position.txt"
    f.write_text("premiere\ndeuxieme\nabcd" + chr(0x200B) + "efgh\n", encoding="utf-8")
    code, d = lancer([f])
    t = d["detail"]["cmd15"][0] if d and d["detail"]["cmd15"] else None
    ok = t is not None and t["ligne"] == 3 and t["colonne"] == 5
    print(f"E6  POSITION    ligne={t['ligne'] if t else '?'} colonne={t['colonne'] if t else '?'} "
          f"(attendu 3 / 5)  {'✅' if ok else '❌ situe faux'}")
    if not ok:
        echecs.append("E6 : position rapportée inexacte")

    # --- E7 à E10 : le registre d'exceptions déclarées -------------------
    # Ouvert le 2026-09-14 sur verdict de Sidy (OUT-16). Le garde-fou de
    # l'excédent est la clause portante : une exception couvre un compte exact,
    # jamais un fichier en bloc. Il est éprouvé PAR L'ÉCHEC.
    cible = tmp / "sous-exception.txt"
    cible.write_text("a" + chr(0x200D) + "b\nc" + chr(0x200D) + "d\n", encoding="utf-8")

    def registre(occurrences, fichier=None):
        r = tmp / f"exc-{occurrences}-{'x' if fichier else 'o'}.yaml"
        r.write_text(
            "exceptions:\n"
            f"  - fichier: \"{fichier or cible.as_posix()}\"\n"
            "    codepoint: \"U+200D\"\n"
            f"    occurrences: {occurrences}\n"
            "    motif: \"epreuve\"\n"
            "    fiche: \"epreuve\"\n", encoding="utf-8")
        return r

    # E7 : compte exact → honoré, plus rien de bloquant.
    code, d = lancer([cible], exceptions=registre(2))
    ok = code == 0 and d and d["violations_cmd15"] == 0 and d["exceptions_honorees"] == 2
    print(f"E7  EXCEPTION   code={code} bloquantes={d['violations_cmd15'] if d else '?'} "
          f"honorees={d['exceptions_honorees'] if d else '?'}  "
          f"{'✅ résidu tranché non rapporté' if ok else '❌ exception non honorée'}")
    if not ok:
        echecs.append("E7 : une exception au compte exact n'est pas honorée")

    # E8 : LA clause portante — 2 observées pour 1 déclarée, l'excédent bloque.
    code, d = lancer([cible], exceptions=registre(1))
    ok = (code == 1 and d and d["violations_cmd15"] == 1
          and d["exceptions_excedents"] == 1 and d["exceptions_honorees"] == 1)
    print(f"E8  EXCÉDENT    code={code} bloquantes={d['violations_cmd15'] if d else '?'} "
          f"excedents={d['exceptions_excedents'] if d else '?'} (attendu 1 / 1)  "
          f"{'✅ l exception n absorbe pas la suite' if ok else '❌ ABSORPTION SILENCIEUSE'}")
    if not ok:
        echecs.append("E8 : l'excédent au-delà du compte déclaré n'est pas bloquant "
                      "— une exception absorberait toute contamination ultérieure")

    # E9 : 5 déclarées pour 2 observées → caduque signalée, non bloquant.
    code, d = lancer([cible], exceptions=registre(5))
    ok = code == 0 and d and len(d["exceptions_caduques"]) == 1
    print(f"E9  CADUQUE     code={code} caduques={len(d['exceptions_caduques']) if d else '?'}  "
          f"{'✅ registre tenu à jour' if ok else '❌ exception périmée non signalée'}")
    if not ok:
        echecs.append("E9 : une exception devenue périmée n'est pas signalée")

    # E10 : --sans-exceptions restitue l'état brut. Sans quoi le registre
    # deviendrait un point aveugle qu'aucune commande ne permettrait de lever.
    code, d = lancer([cible], sans_exceptions=True)
    ok = code == 1 and d and d["violations_cmd15"] == 2 and d["registre_exceptions"] is None
    print(f"E10 ÉTAT BRUT   code={code} bloquantes={d['violations_cmd15'] if d else '?'} "
          f"(attendu 2)  {'✅ le registre est levable' if ok else '❌ état brut inaccessible'}")
    if not ok:
        echecs.append("E10 : --sans-exceptions ne restitue pas l'état brut")

    # --- E11 : le périmètre PAR DÉFAUT voit les fichiers non suivis -------
    # Motif, 2026-09-15 : `git ls-files` nu ne rend que le SUIVI. Le Cmd 15
    # porte « avant commit », et ce qui s'apprête à être commité est encore
    # non suivi — le périmètre nu manquait donc exactement les fichiers qu'il
    # devait lire, et rendait « PROPRE » sans les avoir ouverts. Les 36
    # fichiers du chantier Ghazâlî sont passés sous ce trou.
    #
    # L'épreuve est PAR L'ÉCHEC, en trois points indissociables : un fichier
    # non suivi contaminé doit être VU ; un fichier suivi et sain ne doit rien
    # lever ; un fichier ignoré par git doit rester HORS périmètre — sans quoi
    # l'instrument irait corriger `raw/`, immuable et jamais commité.
    bac = tmp / "bac-git"
    bac.mkdir()
    for arg in (["init", "-q"], ["config", "user.email", "e@e"],
                ["config", "user.name", "e"]):
        subprocess.run(["git"] + arg, cwd=str(bac), capture_output=True)
    (bac / ".gitignore").write_text("ignore/\n", encoding="utf-8")
    (bac / "suivi-sain.txt").write_text(SAIN, encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=str(bac), capture_output=True)
    subprocess.run(["git", "commit", "-qm", "socle"], cwd=str(bac),
                   capture_output=True)
    (bac / "non-suivi.txt").write_text(
        "avant" + chr(0x200B) + "apres\n", encoding="utf-8")
    (bac / "ignore").mkdir()
    (bac / "ignore" / "brut.txt").write_text(
        "avant" + chr(0x200B) + "apres\n", encoding="utf-8")

    r = subprocess.run(
        [sys.executable, str(INSTRUMENT), "--json", "--racine", str(bac),
         "--sans-exceptions"], capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        d = None
    fichiers = {v["fichier"] for v in (d["detail"]["cmd15"] if d else [])}
    vu_non_suivi = any("non-suivi.txt" in f for f in fichiers)
    hors_ignore = not any("ignore/brut.txt" in f for f in fichiers)
    ok = (r.returncode == 1 and d is not None and d["violations_cmd15"] == 1
          and vu_non_suivi and hors_ignore)
    print(f"E11 PÉRIMÈTRE   code={r.returncode} non-suivi vu={vu_non_suivi} "
          f"ignoré hors périmètre={hors_ignore}  "
          f"{'✅' if ok else '❌ le périmètre par défaut est aveugle'}")
    if not ok:
        echecs.append("E11 : le périmètre par défaut ne lit pas les fichiers "
                      "non suivis, ou déborde sur ce que git ignore")

    print()
    if echecs:
        print(f"ÉPREUVE ÉCHOUÉE — {len(echecs)} défaut(s) :")
        for e in echecs:
            print(f"  - {e}")
        return 1
    print("ÉPREUVE PASSÉE — vert sur le sain ; chacun des six codepoints du "
          "Cmd 15 vu séparément ; frontière hors-Cmd 15 tenue ; autoscan "
          "propre ; binaire ignoré ; position exacte ; exception honorée au "
          "compte exact, EXCÉDENT bloquant, exception caduque signalée, état "
          "brut restituable, périmètre par défaut ouvert au non-suivi et "
          "fermé sur ce que git ignore.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
