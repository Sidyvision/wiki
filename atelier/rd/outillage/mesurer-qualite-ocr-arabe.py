#!/usr/bin/env python3
"""
Mesure de qualité d'une sortie OCR arabe — chantier OUT-08.

Principe (§VIII) : DÉTERMINISTE, bibliothèque standard seule, sans LLM, sans
réseau. Il ne corrige rien et ne conclut rien. Il RAPPORTE des indices, et le
verdict sur la lisibilité appartient à l'utilisateur (Cmd 12).

Ce que le script NE dit PAS, et ne dira jamais : qu'un texte est « citable »,
« lisible » ou « bon ». Il classe des sorties pour désigner celles qu'un humain
lira. C'est tout.

Indices produits :
    I1  % de tokens à violation positionnelle (ة ou ى ailleurs qu'en finale)
        PRIMAIRE : ne peut pas devenir muet, n'a besoin d'aucune donnée externe.
    I2  % de tokens de 1-2 caractères (émiettement)
    I3  longueur moyenne des tokens arabes
    I4  % de caractères hors bloc arabe et ponctuation attendue
    I5  occurrences de 4-grammes coraniques + ancres formulaires
        CONFIRMATOIRE : preuve la plus forte, mais dépend des citations
        effectivement présentes sur la page mesurée.
    I6  invisibles interdits par le Cmd 15 (U+200B/C/D/E/F, U+FEFF)
        Ce n'est PAS un indice de qualité : c'est un contrôle d'hygiène.

Normalisation : appliquée DES DEUX CÔTÉS. Le texte coranique de référence est
fortement vocalisé, le scan ne l'est presque pas. Sans elle, I5 renverrait zéro
pour TOUTE piste — le « contrôle muet » que le §VII interdit.

Garde anti-mutisme : moins de 20 tokens arabes → refus (code 2), jamais
« 0 violation, parfait ».

Usage :
    python3 mesurer-qualite-ocr-arabe.py [--reference ref.txt] [--tsv] fichier...

Codes de sortie :
    0  mesure faite
    2  entrée inexploitable (garde anti-mutisme) ou erreur d'exécution
"""

import argparse
import sys
import unicodedata
from pathlib import Path

# --- Bloc arabe et sous-ensembles -------------------------------------------

# Toute marque combinante (unicodedata.combining != 0) plus le tatweel.
# Une table d'intervalles écrite à la main laissait passer U+0656/0657/065E —
# marques coraniques qui restaient collées au ة et le faisaient compter comme
# non final : I1 valait 1,71 % sur du Coran sain. Défaut attrapé par E1a le
# 2026-09-07 ; le test générique n'a pas ce trou.
TATWEEL = "\u0640"  # ـ


def est_diacritique(ch):
    return ch == TATWEEL or unicodedata.combining(ch) != 0

# Repli des variantes de la hamza : appliqué partout.
REPLIS_HAMZA = {
    "ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا",
    "ؤ": "و", "ئ": "ي",
}

# Repli de ة et ى : nécessaire pour APPARIER le scan au Coran (I5), mais il
# efface justement les deux lettres sur lesquelles I1 se fonde. I1 se mesure
# donc AVANT ce repli — sans quoi il vaudrait 0 sur n'importe quelle entrée,
# y compris la pire, et serait le « contrôle muet » que le §VII interdit.
# Ce défaut a été introduit puis attrapé par l'épreuve E1 le 2026-09-07.
REPLIS_APPARIEMENT = {"ى": "ي", "ة": "ه"}

# Interdits par le Commandement 15. Écrits en échappements, JAMAIS en
# littéral : un fichier qui contient les caractères qu'il prétend interdire
# fait échouer le contrôle d'hygiène sur lui-même. Constaté et corrigé le
# 2026-09-07, avant le premier commit de ce script.
INVISIBLES = {
    "\u200b": "ZWSP", "\u200c": "ZWNJ", "\u200d": "ZWJ",
    "\u200e": "LRM", "\u200f": "RLM", "\ufeff": "BOM",
}

PONCTUATION_ATTENDUE = set(" \t\n\r0123456789.,;:!?()[]{}«»\"'-–—/،؛؟٪-٭")

# Lettres dont la forme finale est distincte : leur présence en position non
# finale à l'intérieur d'un token est une faute de segmentation caractéristique.
FINALES_STRICTES = {"\u0629", "\u0649"}  # ة (ta marbuta), ى (alif maqsura)

ANCRES = [
    "بسم الله الرحمن الرحيم",
    "صلي الله عليه وسلم",
    "رضي الله عنه",
    "قال رسول الله",
    "سبحانه وتعالي",
]


def est_arabe(ch):
    return "؀" <= ch <= "ۿ" or "ݐ" <= ch <= "ݿ"


def normaliser(texte, pour_appariement=True):
    """Dévocalise et replie les variantes orthographiques.

    `pour_appariement=False` conserve ة et ى : c'est la forme sur laquelle I1
    se mesure. `True` les replie : c'est la forme sur laquelle I5 s'apparie.
    """
    texte = unicodedata.normalize("NFD", texte)
    sortie = []
    for ch in texte:
        if est_diacritique(ch):
            continue
        ch = REPLIS_HAMZA.get(ch, ch)
        if pour_appariement:
            ch = REPLIS_APPARIEMENT.get(ch, ch)
        sortie.append(ch)
    return "".join(sortie)


def tokeniser(texte_normalise):
    """Découpe sur tout ce qui n'est pas une lettre arabe."""
    tokens, courant = [], []
    for ch in texte_normalise:
        if est_arabe(ch):
            courant.append(ch)
        else:
            if courant:
                tokens.append("".join(courant))
                courant = []
    if courant:
        tokens.append("".join(courant))
    return tokens


def ngrammes(tokens, n=4):
    return {" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def charger_reference(chemin):
    """Retourne l'ensemble des 4-grammes normalisés du texte de référence."""
    brut = Path(chemin).read_text(encoding="utf-8")
    return ngrammes(tokeniser(normaliser(brut)), 4)


def mesurer(chemin, ref_ngrammes):
    brut = Path(chemin).read_text(encoding="utf-8", errors="replace")

    # I6 se mesure sur le texte BRUT : la normalisation ne doit pas masquer
    # ce que le Cmd 15 interdit.
    i6 = {nom: brut.count(c) for c, nom in INVISIBLES.items()
          if brut.count(c)}
    i6_total = sum(i6.values())

    texte = normaliser(brut, pour_appariement=True)
    tokens = tokeniser(texte)
    # Forme conservant ة et ى, seule sur laquelle I1 a un sens.
    tokens_i1 = tokeniser(normaliser(brut, pour_appariement=False))

    if len(tokens) < 20:
        raise ValueError(
            f"{chemin} : {len(tokens)} tokens arabes seulement (< 20). "
            "Entrée inexploitable — refus plutôt qu'un rapport trompeur. "
            "Cause probable : texte vide, ou écrit en formes de présentation "
            "(U+FB50-U+FDFF) que le motif U+0600-U+06FF ne reconnaît pas."
        )

    # I1 — violation positionnelle
    violations = 0
    for t in tokens_i1:
        if any(c in FINALES_STRICTES for c in t[:-1]):
            violations += 1
    i1 = 100.0 * violations / len(tokens_i1) if tokens_i1 else 0.0

    # I2 — émiettement
    i2 = 100.0 * sum(1 for t in tokens if len(t) <= 2) / len(tokens)

    # I3 — longueur moyenne
    i3 = sum(len(t) for t in tokens) / len(tokens)

    # I4 — caractères parasites
    total_car = sum(1 for c in texte if not c.isspace())
    parasites = sum(
        1 for c in texte
        if not c.isspace() and not est_arabe(c) and c not in PONCTUATION_ATTENDUE
    )
    i4 = 100.0 * parasites / total_car if total_car else 0.0

    # I5 — ancrage externe
    i5_ng = 0
    if ref_ngrammes:
        for i in range(len(tokens) - 3):
            if " ".join(tokens[i:i + 4]) in ref_ngrammes:
                i5_ng += 1
    plat = " ".join(tokens)
    i5_ancres = sum(plat.count(normaliser(a)) for a in ANCRES)

    return {
        "fichier": Path(chemin).name,
        "tokens": len(tokens),
        "I1": i1, "I2": i2, "I3": i3, "I4": i4,
        "I5_ngrammes": i5_ng, "I5_ancres": i5_ancres,
        "I6": i6_total, "I6_detail": i6,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichiers", nargs="+")
    ap.add_argument("--reference", help="texte arabe sain, pour I5")
    ap.add_argument("--tsv", action="store_true", help="sortie machine")
    args = ap.parse_args()

    ref = charger_reference(args.reference) if args.reference else set()
    if args.reference and not ref:
        print(f"REFUS : référence {args.reference} sans 4-gramme exploitable.",
              file=sys.stderr)
        return 2

    lignes, refus = [], []
    for f in args.fichiers:
        try:
            lignes.append(mesurer(f, ref))
        except ValueError as e:
            refus.append(str(e))

    if not lignes:
        for r in refus:
            print(f"REFUS : {r}", file=sys.stderr)
        return 2

    lignes.sort(key=lambda d: d["I1"])

    if args.tsv:
        print("fichier\ttokens\tI1\tI2\tI3\tI4\tI5_ng\tI5_anc\tI6")
        for d in lignes:
            print(f"{d['fichier']}\t{d['tokens']}\t{d['I1']:.2f}\t{d['I2']:.2f}\t"
                  f"{d['I3']:.2f}\t{d['I4']:.2f}\t{d['I5_ngrammes']}\t"
                  f"{d['I5_ancres']}\t{d['I6']}")
    else:
        print(f"{'fichier':<28} {'tok':>6} {'I1%':>7} {'I2%':>7} {'I3':>6} "
              f"{'I4%':>6} {'I5ng':>5} {'I5an':>5} {'I6':>5}")
        print("-" * 82)
        for d in lignes:
            print(f"{d['fichier']:<28} {d['tokens']:>6} {d['I1']:>7.2f} "
                  f"{d['I2']:>7.2f} {d['I3']:>6.2f} {d['I4']:>6.2f} "
                  f"{d['I5_ngrammes']:>5} {d['I5_ancres']:>5} {d['I6']:>5}")
        print("\nI1 primaire (violation positionnelle) — trié dessus, croissant.")
        print("I6 n'est pas un indice de qualité : c'est le contrôle Cmd 15.")
        print("Aucun de ces chiffres ne dit qu'un texte est lisible. "
              "Ce verdict appartient à l'utilisateur (Cmd 12).")

    for r in refus:
        print(f"\nREFUS : {r}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
