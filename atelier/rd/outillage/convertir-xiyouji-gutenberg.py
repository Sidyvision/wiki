#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convertir-xiyouji-gutenberg.py — Conversion texte → Markdown du `Xī Yóu Jì`
(西遊記) de Wú Chéng'ēn, édition Project Gutenberg n° 23962, chinois traditionnel.

Convertit `raw/xi-you-ji-wu-chengen-traditionnel-gutenberg-23962.txt` (UTF-8,
domaine public) vers `textes/xi-you-ji-wu-chengen-traditionnel/`, à raison d'un
fichier par 回 (100 chapitres, verdict Sidy du 2026-09-15).

Principe (même famille que convertir-ghazali-ihya.py et
convertir-ibnsirin-dictionnaire-reves.py) : DÉTERMINISTE, sans LLM, sans réseau.
Il ne touche jamais à `raw/` (immuable, hors git) : il lit la source et écrit la
conversion dans `textes/`.

CHAÎNE — ce qui est retiré, et rien d'autre :

  1. L'en-tête et le pied de Project Gutenberg, délimités par les bornes
     `*** START OF THE PROJECT GUTENBERG EBOOK ... ***` et
     `*** END OF THE PROJECT GUTENBERG EBOOK ... ***`.
     Ce n'est PAS une correction du texte — que la règle d'immuabilité de
     `textes/` interdirait. C'est la couche de DIFFUSION : notice de licence,
     adresses du site, appel aux dons. Elle n'appartient pas à l'œuvre, au même
     titre que les contrôles bidi retirés de l'Ihyâ' arabe
     (`textes/ghazali-ihya-ulum-al-din-arabe/index-conversion.md`, étape 3).

  2. La ligne de crédit du transcripteur (`Produced by ...`), qui suit la borne
     d'ouverture. Même couche, même motif. Elle est REPORTÉE dans
     l'index-conversion : retirer n'est pas effacer.

Ce qui n'est PAS touché : le texte du roman, ses espaces idéographiques U+3000,
sa ponctuation, et jusqu'à l'espace initiale parasite du titre du 第八三回 —
une conversion reçoit, elle ne redresse pas.

GARDE-FOUS (épreuve des contrôles, CLAUDE.md racine §VII) — quatre refus, chacun
vu échouer sur un cas fabriqué avant emploi. Le script n'écrit RIEN si l'un cède :

  G1  bornes Gutenberg absentes ou en ordre inverse ;
  G2  nombre de 回 différent de 100, numérotation non strictement croissante
      de 1 à 100, ou doublon ;
  G3  caractère invisible du Cmd 15 (U+200B/C/D, U+FEFF, U+200E/F, U+000C)
      relevé en sortie ;
  G4  matière non reconnue entre la borne d'ouverture et le premier 回 (tout ce
      qui n'est ni blanc ni la ligne de crédit) — refus plutôt que perte
      silencieuse.

USAGE :
    convertir-xiyouji-gutenberg.py                 # rapport seul (défaut)
    convertir-xiyouji-gutenberg.py --appliquer     # écrit les 100 tranches
    convertir-xiyouji-gutenberg.py --source X --sortie Y   # bac à sable
"""
import argparse
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
SOURCE = RACINE / "raw" / "xi-you-ji-wu-chengen-traditionnel-gutenberg-23962.txt"
SORTIE = RACINE / "textes" / "xi-you-ji-wu-chengen-traditionnel"

BORNE_DEBUT = re.compile(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK.*?\*\*\*")
BORNE_FIN = re.compile(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK.*?\*\*\*")
TITRE = re.compile(r"^\s*第([一二三四五六七八九十百零○]+)回")
CREDIT = re.compile(r"^\s*Produced by .*$")
INVISIBLES = tuple(chr(c) for c in (0x200B, 0x200C, 0x200D, 0xFEFF,
                                    0x200E, 0x200F, 0x000C))
# Construits par chr() et NON écrits en clair : un littéral invisible dans ce
# fichier serait lui-même une violation du Cmd 15 (relevée le 2026-09-15).

CHIFFRES = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
            "六": 6, "七": 7, "八": 8, "九": 9, "○": 0, "零": 0}


class Refus(Exception):
    """Un garde-fou a cédé : aucune écriture n'a lieu."""


def numero(han: str) -> int:
    """`一` → 1, `八三` → 83, `一○○` → 100. Lève Refus sur une forme inconnue."""
    han = han.strip()
    try:
        if han in ("一○○", "一零零", "一百"):
            return 100
        if "十" in han:
            avant, _, apres = han.partition("十")
            dizaines = CHIFFRES[avant] if avant else 1
            unites = CHIFFRES[apres] if apres else 0
            return dizaines * 10 + unites
        if len(han) == 2:
            return CHIFFRES[han[0]] * 10 + CHIFFRES[han[1]]
        return CHIFFRES[han]
    except KeyError as exc:
        raise Refus(f"G2 — numéro de 回 non interprétable : {han!r}") from exc


def corps_entre_bornes(texte: str) -> str:
    """G1 — isole le corps entre les deux bornes Gutenberg."""
    debut = BORNE_DEBUT.search(texte)
    fin = BORNE_FIN.search(texte)
    if not debut or not fin:
        manquantes = []
        if not debut:
            manquantes.append("START")
        if not fin:
            manquantes.append("END")
        raise Refus(f"G1 — borne(s) Gutenberg absente(s) : {', '.join(manquantes)}")
    if fin.start() <= debut.end():
        raise Refus("G1 — bornes Gutenberg en ordre inverse")
    return texte[debut.end():fin.start()]


def decouper(corps: str):
    """G2/G4 — rend la liste [(numero, titre, contenu)] des 100 回."""
    lignes = corps.split("\n")
    debuts = [i for i, ligne in enumerate(lignes) if TITRE.match(ligne)]
    if not debuts:
        raise Refus("G2 — aucun titre de 回 trouvé")

    prelude = [l for l in lignes[:debuts[0]] if l.strip()]
    inconnu = [l for l in prelude if not CREDIT.match(l)]
    if inconnu:
        raise Refus(
            "G4 — matière non reconnue avant le premier 回 : "
            + "; ".join(repr(l[:60]) for l in inconnu[:3])
        )

    chapitres = []
    for rang, debut in enumerate(debuts):
        fin = debuts[rang + 1] if rang + 1 < len(debuts) else len(lignes)
        titre = lignes[debut].strip()
        num = numero(TITRE.match(lignes[debut]).group(1))
        chapitres.append((num, titre, "\n".join(lignes[debut:fin]).strip("\n")))

    numeros = [c[0] for c in chapitres]
    if len(chapitres) != 100:
        raise Refus(f"G2 — {len(chapitres)} 回 trouvés, 100 attendus")
    if numeros != list(range(1, 101)):
        attendus = set(range(1, 101))
        manquants = sorted(attendus - set(numeros))
        doublons = sorted({n for n in numeros if numeros.count(n) > 1})
        raise Refus(
            f"G2 — numérotation non conforme (manquants={manquants}, "
            f"doublons={doublons}, croissante={numeros == sorted(numeros)})"
        )
    return chapitres, prelude


def controler_invisibles(chapitres):
    """G3 — aucun invisible du Cmd 15 en sortie."""
    releve = {}
    for num, _, contenu in chapitres:
        for car in INVISIBLES:
            if car in contenu:
                releve.setdefault(f"U+{ord(car):04X}", []).append(num)
    if releve:
        detail = "; ".join(f"{k} dans les 回 {v[:5]}" for k, v in releve.items())
        raise Refus(f"G3 — caractère(s) invisible(s) du Cmd 15 en sortie : {detail}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--appliquer", action="store_true",
                    help="écrit les tranches (sans ce drapeau : rapport seul)")
    ap.add_argument("--source", type=Path, default=SOURCE)
    ap.add_argument("--sortie", type=Path, default=SORTIE)
    args = ap.parse_args()

    if not args.source.exists():
        print(f"REFUS — source introuvable : {args.source}", file=sys.stderr)
        return 2

    texte = args.source.read_text(encoding="utf-8")
    try:
        corps = corps_entre_bornes(texte)
        chapitres, prelude = decouper(corps)
        controler_invisibles(chapitres)
    except Refus as refus:
        print(f"REFUS — {refus}", file=sys.stderr)
        return 1

    retire = len(texte) - len(corps)
    print(f"Source        : {args.source}")
    print(f"Corps         : {len(corps)} caractères "
          f"({retire} retirés — en-tête et pied Gutenberg)")
    print(f"Crédit reporté: {prelude or 'aucun'}")
    print(f"回 trouvés     : {len(chapitres)} (1 à {chapitres[-1][0]})")
    print(f"Garde-fous    : G1 bornes OK · G2 numérotation OK · "
          f"G3 invisibles OK · G4 prélude reconnu")
    print(f"Sortie        : {args.sortie}")

    if not args.appliquer:
        print("\nRapport seul — aucune écriture. Relancer avec --appliquer.")
        return 0

    args.sortie.mkdir(parents=True, exist_ok=True)
    for num, titre, contenu in chapitres:
        cible = args.sortie / f"xiyouji-hui-{num:03d}.md"
        cible.write_text(contenu + "\n", encoding="utf-8")
    print(f"\nÉcrit : {len(chapitres)} fichiers dans {args.sortie}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
