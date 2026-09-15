#!/usr/bin/env python3
"""
Épreuve du §VII de `mesurer-qualite-ocr-arabe.py` — chantier OUT-08.

« Un contrôle dont on n'a pas vu l'échec n'est pas un contrôle vérifié. »
Ce script ne mesure rien : il fabrique les fautes exactes que l'instrument doit
attraper, et vérifie qu'il les attrape. Il sort en code 1 si une seule épreuve
échoue.

Quatre épreuves :
  E1a  VERT       — sur de l'arabe sain, I1 doit être proche de zéro.
  E1b  MONOTONIE  — chaque indice est éprouvé par la corruption QU'IL prétend
                    mesurer, et par elle seule :
                      · transpositions 5/10/20 %      → I1 doit croître
                      · fragmentation (espaces ajoutés) → I2 croît, I3 décroît
                    Éprouver I2 par la soudure était une faute de l'épreuve,
                    pas de l'indice : la soudure réduit l'émiettement, elle ne
                    l'augmente pas. Corrigé le 2026-09-07.
  E1c  REFUS      — sur un texte en formes de présentation (U+FB50-U+FDFF),
                    l'instrument doit REFUSER, et non imprimer « 0 violation ».
  E1d  BIDI/I7    — I7 doit compter les contrôles d'enrobage bidi, et I6 doit
                    rester inchangé : la frontière du jeu nommé par le Cmd 15
                    ne se franchit pas dans un instrument. Ajouté le
                    2026-09-14, après 1562 contrôles bidi passés inaperçus.

Usage : python3 eprouver-mesure-ocr-arabe.py <reference-arabe-saine.txt>
"""

import random
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
INSTRUMENT = ICI / "mesurer-qualite-ocr-arabe.py"


def _charger_instrument():
    """Importe l'instrument pour réutiliser sa dévocalisation, sans la redire."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("instrument", INSTRUMENT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def devocaliser(texte):
    return _charger_instrument().normaliser(texte, pour_appariement=False)


def mesurer(chemin, reference):
    """Lance l'instrument et retourne (code, dict d'indices)."""
    r = subprocess.run(
        [sys.executable, str(INSTRUMENT), "--tsv", "--reference", str(reference),
         str(chemin)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return r.returncode, None
    lignes = [l for l in r.stdout.strip().split("\n") if l]
    if len(lignes) < 2:
        return r.returncode, None
    c = lignes[1].split("\t")
    # Colonnes TSV : fichier, tokens, I1, I2, I3, I4, I5_ng, I5_anc, I6, I7.
    return 0, {"I1": float(c[2]), "I2": float(c[3]), "I3": float(c[4]),
               "I6": int(c[8]), "I7": int(c[9])}


def corrompre(texte, taux, germe=42):
    """Transpose deux caractères adjacents dans `taux` des mots. Déterministe."""
    rng = random.Random(germe)
    mots = texte.split(" ")
    for i, m in enumerate(mots):
        if len(m) >= 3 and rng.random() < taux:
            j = rng.randrange(len(m) - 1)
            mots[i] = m[:j] + m[j + 1] + m[j] + m[j + 2:]
    return " ".join(mots)


def fragmenter(texte, taux, germe=7):
    """Insère une espace au milieu de `taux` des mots — imite l'émiettement."""
    rng = random.Random(germe)
    mots = texte.split(" ")
    for i, m in enumerate(mots):
        if len(m) >= 4 and rng.random() < taux:
            j = rng.randrange(1, len(m) - 1)
            mots[i] = m[:j] + " " + m[j:]
    return " ".join(mots)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    ref = Path(sys.argv[1])

    # Les corruptions portent sur le texte DÉVOCALISÉ. Appliquées au texte
    # vocalisé, elles permutent surtout des diacritiques — que l'instrument
    # efface ensuite : la faute devenait invisible et I1 restait plat à 0,44 %
    # quel que soit le taux. Défaut attrapé par E1b le 2026-09-07.
    sain = devocaliser(ref.read_text(encoding="utf-8"))
    echecs = []
    tmp = Path(tempfile.mkdtemp(prefix="eprouve-ocr-"))

    # --- E1a : vert sur l'arabe sain -------------------------------------
    code, m = mesurer(ref, ref)
    if code != 0 or m is None:
        echecs.append("E1a : l'instrument a refusé une référence saine")
        print("E1a  VERT       ÉCHEC (refus sur entrée saine)")
    else:
        ok = m["I1"] < 1.0
        print(f"E1a  VERT       I1 = {m['I1']:.2f} %  "
              f"{'✅ proche de zéro' if ok else '❌ attendu < 1 %'}")
        if not ok:
            echecs.append(f"E1a : I1 = {m['I1']:.2f} % sur de l'arabe sain")

    # --- E1b : monotonie sous corruption croissante -----------------------
    serie_t, serie_f = [], []
    for taux in (0.0, 0.05, 0.10, 0.20):
        f = tmp / f"transpose-{int(taux*100):02d}.txt"
        f.write_text(corrompre(sain, taux), encoding="utf-8")
        code, m = mesurer(f, ref)
        if code != 0 or m is None:
            echecs.append(f"E1b : refus inattendu (transposition {taux:.0%})")
            break
        serie_t.append(m["I1"])
        print(f"E1b  transposition {taux:>5.0%}  I1 = {m['I1']:>6.2f} %")

        g = tmp / f"fragmente-{int(taux*100):02d}.txt"
        g.write_text(fragmenter(sain, taux), encoding="utf-8")
        code, m = mesurer(g, ref)
        if code != 0 or m is None:
            echecs.append(f"E1b : refus inattendu (fragmentation {taux:.0%})")
            break
        serie_f.append((m["I2"], m["I3"]))
        print(f"E1b  fragmentation {taux:>5.0%}  I2 = {m['I2']:>6.2f} %   "
              f"I3 = {m['I3']:>5.2f}")

    if len(serie_t) == 4 and len(serie_f) == 4:
        i1_ok = all(serie_t[i] < serie_t[i + 1] for i in range(3))
        i2_ok = all(serie_f[i][0] < serie_f[i + 1][0] for i in range(3))
        i3_ok = all(serie_f[i][1] > serie_f[i + 1][1] for i in range(3))
        print(f"E1b  MONOTONIE  I1 {'✅' if i1_ok else '❌'} croît sous transposition | "
              f"I2 {'✅' if i2_ok else '❌'} croît et I3 {'✅' if i3_ok else '❌'} "
              f"décroît sous fragmentation")
        for ok, msg in ((i1_ok, "I1 ne croît pas sous transposition"),
                        (i2_ok, "I2 ne croît pas sous fragmentation"),
                        (i3_ok, "I3 ne décroît pas sous fragmentation")):
            if not ok:
                echecs.append(f"E1b : {msg} — l'indice ne mesure rien")

    # --- E1c : refus sur formes de présentation ---------------------------
    # U+FB50-U+FDFF : de l'arabe pour un œil humain, invisible au motif
    # U+0600-U+06FF. C'est la forme exacte du contrôle muet.
    f = tmp / "formes-presentation.txt"
    f.write_text("ﺎﻠﺴﻟﺎﻣ ﻊﻠﻴﻜﻣ " * 200, encoding="utf-8")
    code, _ = mesurer(f, ref)
    ok = code != 0
    print(f"E1c  REFUS      code {code}  "
          f"{'✅ refus obtenu' if ok else '❌ a rapporté au lieu de refuser'}")
    if not ok:
        echecs.append("E1c : rapport silencieux sur un texte à zéro token arabe")

    # --- E1d : I7 voit les contrôles bidi, et I6 ne les avale pas ---------
    # Motif : I6 couvre le jeu nommé par le Cmd 15 et lui seul ; les contrôles
    # d'enrobage (U+202A-U+202E, U+2066-U+2069) en sont absents. Avant l'ajout
    # de I7 le 2026-09-14, un PDF arabe natif passait le contrôle en silence
    # alors qu'il en portait 1562 pour 55 000 caractères.
    # Le contrôle est éprouvé PAR L'ÉCHEC : un texte sain doit donner I7 = 0,
    # le même texte enrobé doit donner exactement le nombre injecté, et I6
    # doit rester inchangé dans les deux cas.
    f = tmp / "bidi-absent.txt"
    f.write_text(sain, encoding="utf-8")
    code_a, d_a = mesurer(f, ref)

    lre, rle, pdf_c = chr(0x202A), chr(0x202B), chr(0x202C)
    lignes_b = [lre + l + pdf_c for l in sain.split("\n")]
    injecte = 2 * len(lignes_b)
    f = tmp / "bidi-present.txt"
    f.write_text("\n".join(lignes_b), encoding="utf-8")
    code_b, d_b = mesurer(f, ref)

    ok = (code_a == 0 and code_b == 0
          and d_a["I7"] == 0 and d_b["I7"] == injecte
          and d_a["I6"] == d_b["I6"])
    print(f"E1d  BIDI/I7    I7 sain={d_a['I7'] if code_a == 0 else '?'} "
          f"I7 enrobé={d_b['I7'] if code_b == 0 else '?'} (attendu {injecte})  "
          f"I6 inchangé={d_a['I6'] == d_b['I6'] if code_b == 0 else '?'}  "
          f"{'✅' if ok else '❌ I7 aveugle, ou I6 contaminé'}")
    if not ok:
        echecs.append("E1d : I7 ne compte pas les contrôles bidi, "
                      "ou I6 les absorbe (frontière du Cmd 15 franchie)")

    print()
    if echecs:
        print(f"ÉPREUVE ÉCHOUÉE — {len(echecs)} défaut(s) :")
        for e in echecs:
            print(f"  - {e}")
        return 1
    print("ÉPREUVE PASSÉE — vert sur l'arabe sain, dégradation monotone sous "
          "corruption, refus sur entrée muette, bidi vu par I7 sans "
          "contaminer I6.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
