#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verifier-recursion-qaf.py — contrôle déterministe du modèle récursif de
Sabri B. Rommane sur Sūrat Qāf (raw/The Sabri Ben Rommane's Theory, 2026-09-04).

Objet : rejouer les deux règles de branchement possibles et confronter leurs
sorties aux chiffres publiés par l'auteur. Le script ne juge rien : il compte.

Noms de lettres pris du tableau de l'alphabet de Gloton (repère Aa),
`textes/une-approche-du-coran-gloton/corps-du-texte.md`.

Usage : python3 atelier/rd/outillage/verifier-recursion-qaf.py
Sortie : rapport texte sur stdout ; code 0 si les deux contrôles concordent
avec les chiffres publiés, 1 sinon.
"""

# Chiffres publiés par l'auteur, à confronter.
NIVEAUX_PUBLIES = [3, 8, 21, 56, 151]          # IMG_0480 : L1..L5
MOTIF_PUBLIE = [3, 3, 2, 3, 3, 2, 2, 3, 3, 3,  # IMG_0447 : tailles des 17 groupes
                2, 3, 3, 3, 2, 3, 2]
VERSETS_QAF = 45                               # Sūrat Qāf, 45 āyāt

# Variante A — règle ÉNONCÉE par l'auteur : « Hamza = terminal node »
# (IMG_0445, IMG_0479). La hamza est émise, mais ne se branche plus.
NOMS_A = {
    'ق': ['ق', 'ا', 'ف'],   # qâf
    'ا': ['ا', 'ل', 'ف'],   # 'alif
    'ف': ['ف', 'ا', 'ء'],   # fâ'
    'ل': ['ل', 'ا', 'م'],   # lâm
    'م': ['م', 'ي', 'م'],   # mîm
    'ي': ['ي', 'ا', 'ء'],   # yâ'
    'ء': ['ء'],             # hamza : noeud terminal, se reproduit telle quelle
}

# Variante B — règle OPÉRANTE, déduite des chiffres publiés : la hamza n'est
# pas émise du tout. Les noms de fâ' et yâ' sont tronqués à deux lettres.
NOMS_B = {
    'ق': ['ق', 'ا', 'ف'],
    'ا': ['ا', 'ل', 'ف'],
    'ف': ['ف', 'ا'],
    'ل': ['ل', 'ا', 'م'],
    'م': ['م', 'ي', 'م'],
    'ي': ['ي', 'ا'],
}


def deplier(noms, graine='ق', niveaux=5):
    """Rend la liste des niveaux 1..n obtenus en remplaçant chaque lettre par
    les lettres de son nom."""
    seq, sortie = [graine], []
    for _ in range(niveaux):
        suivant = []
        for lettre in seq:
            suivant.extend(noms[lettre])
        seq = suivant
        sortie.append(seq[:])
    return sortie


def motif_depuis_parents(noms, niveau4):
    """Règle de découpage (IMG_0447) : les lettres du niveau 5 sont groupées par
    leur parent de niveau 4 ; la taille du groupe est la longueur du nom du
    parent."""
    return [len(noms[lettre]) for lettre in niveau4]


def rapport():
    ecarts = []

    for etiquette, noms, attendu in (
        ('A — hamza émise puis terminale (règle énoncée)', NOMS_A, False),
        ('B — hamza jamais émise (règle opérante)',        NOMS_B, True),
    ):
        print(f'\n=== Variante {etiquette} ===')
        niveaux = deplier(noms)
        comptes = [len(n) for n in niveaux]
        print(f'  L1..L5 (lettres)  : {comptes}')
        print(f'  publié par l\'auteur : {NIVEAUX_PUBLIES}')
        concorde = comptes == NIVEAUX_PUBLIES
        print(f'  concordance        : {"OUI" if concorde else "NON"}')
        if attendu and not concorde:
            ecarts.append(f'variante B ne reproduit plus {NIVEAUX_PUBLIES}')
        if not attendu and concorde:
            ecarts.append('variante A reproduit les chiffres : le constat s\'effondre')

    # Le motif de groupes ne se dérive que sous la variante B.
    print('\n=== Découpage en groupes (variante B) ===')
    niveaux = deplier(NOMS_B)
    motif = motif_depuis_parents(NOMS_B, niveaux[3])
    tete = motif[:len(MOTIF_PUBLIE)]
    print(f'  dérivé  : {tete}')
    print(f'  publié  : {MOTIF_PUBLIE}')
    print(f'  identique : {"OUI" if tete == MOTIF_PUBLIE else "NON"}')
    print(f'  somme dérivée : {sum(tete)} — versets de Sūrat Qāf : {VERSETS_QAF}')
    if tete != MOTIF_PUBLIE:
        ecarts.append('le motif dérivé ne reproduit plus le motif publié')
    if sum(tete) != VERSETS_QAF:
        ecarts.append(f'la somme dérivée n\'est plus {VERSETS_QAF}')

    # Ensemble stable : le point où plus aucune lettre nouvelle n'apparaît.
    print('\n=== Ensemble stable (variante B) ===')
    for i, n in enumerate(niveaux, start=1):
        print(f'  L{i} : {len(n):>3} lettres, {len(set(n))} distinctes')

    print()
    if ecarts:
        for e in ecarts:
            print(f'ÉCART : {e}')
        return 1
    print('Contrôle vert : les deux constats consignés à la fiche sont reproduits.')
    return 0


if __name__ == '__main__':
    raise SystemExit(rapport())
