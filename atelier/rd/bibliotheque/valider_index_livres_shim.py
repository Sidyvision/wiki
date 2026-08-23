#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pont d'import : `valider-index-livres.py` porte un tiret, non importable
tel quel. Ce module le charge et re-expose les primitives partagees.
Aucune logique propre — toute regle vit dans le validateur."""

import importlib.util
import io
import os
import sys

_ICI = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_ICI, "valider-index-livres.py")
_spec = importlib.util.spec_from_file_location("_vil", _SRC)
_vil = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vil)

lire_frontmatter = _vil.lire_frontmatter
liste_yaml = _vil.liste_yaml


def valider(dossier, racine_raw=None):
    """Relance le validateur sur `dossier`, silencieusement, et rend son code.

    ATTENTION : la sortie detaillee est avalee — l'appelant ne recoit que le
    code de retour. « le generateur valide » ne veut pas dire « le generateur
    rapporte » : pour lire les anomalies, lancer le validateur directement.
    `racine_raw` doit etre transmis, sinon le validateur retombe sur son
    defaut ; ne jamais le forcer a None (le controle H1 se desarmerait)."""
    argv, stdout = sys.argv, sys.stdout
    try:
        sys.argv = ["valider-index-livres.py", "--dossier", dossier]
        if racine_raw:
            sys.argv += ["--raw", racine_raw]
        sys.stdout = io.StringIO()
        return _vil.main()
    finally:
        sys.argv, sys.stdout = argv, stdout
