#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verifier-renvois-skills.py — un skill livre-t-il les fichiers qu'il déclare ?
(chantier OUT-17)

Déterministe : sans LLM, sans réseau, EN LECTURE SEULE. Il constate, ne corrige
rien, et sort en code non nul si un renvoi déclaré n'existe pas.

Motif (constaté le 2026-09-15) : un skill peut déclarer `references/…`,
`templates/…`, `scripts/…` ou `assets/…` et n'en livrer aucun — le fichier
déclaré vivait dans une AUTRE position de la file, écartée par ailleurs. Trois
renvois morts ont été trouvés ainsi sur vingt-deux skills créés, dont deux
invisibles autrement.

Ce qu'il ne fait pas — et c'est le point délicat : un chemin cité **au fil d'une
phrase d'exemple** ou dans un **bloc de code** n'est pas une déclaration. Un
contrôle qui crie à tort sera ignoré, donc il mentira par omission ensuite.
D'où deux classes distinctes :
    déclaré   — chemin porté par une ligne de liste, une ligne de tableau ou le
                cartouche (frontmatter) ;
    mentionné — chemin cité ailleurs (prose, bloc de code) : hors déclaration.

Par défaut, seuls les renvois DÉCLARÉS manquants sont bloquants ; les mentions
ne le sont qu'avec --strict.

Usage :
    python3 verifier-renvois-skills.py [--racine DIR]... [--json] [--strict]

Codes de sortie : 0 sain · 1 anomalie · 2 erreur du script
"""

import argparse
import glob
import json
import os
import re
import sys

MOTIF = re.compile(r'(?<![\w/.\-])((?:references|templates|scripts|assets)/[A-Za-z0-9._/\-]+)')
BLOC = re.compile(r'^\s*(```|~~~)')


def sections_declarees(texte):
    """Rend l'ensemble des lignes 'de déclaration', hors blocs de code."""
    lignes, dans_bloc, gardees = texte.split('\n'), False, set()
    for l in lignes:
        if BLOC.match(l):
            dans_bloc = not dans_bloc
            continue
        if dans_bloc:
            continue
        if re.match(r'^\s*[-*+]\s', l) or re.match(r'^\s*\|', l):
            gardees.add(l.strip())
    return gardees


def analyse_skill(chemin):
    texte = open(chemin, encoding='utf-8', errors='replace').read()
    front = ''
    if texte.lstrip().startswith('---'):
        blocs = texte.split('---')
        if len(blocs) >= 3:
            front = blocs[1]
    lignes_declarees = sections_declarees(texte)
    decl, ment = {}, {}
    for m in MOTIF.finditer(texte):
        p = m.group(1).rstrip('.,;:)')
        ligne = texte[:m.start()].count('\n')
        contenu_ligne = texte.split('\n')[ligne].strip()
        # déclaré si la ligne (ou le cartouche) le porte comme élément
        if p in front or contenu_ligne in lignes_declarees or re.match(r'^\s*[-*+]\s', contenu_ligne):
            decl.setdefault(p, contenu_ligne[:80])
        else:
            ment.setdefault(p, contenu_ligne[:80])
    base = os.path.dirname(chemin)
    manquants_decl = sorted(p for p in decl if not os.path.exists(os.path.join(base, p)))
    manquants_ment = sorted(p for p in ment if not os.path.exists(os.path.join(base, p)))
    return manquants_decl, manquants_ment, sorted(decl)


def racines_skills(demandees):
    if demandees:
        return [(os.path.abspath(d), os.path.basename(os.path.dirname(os.path.abspath(d))) or os.path.abspath(d))
                for d in demandees]
    base = os.environ.get('HERMES_HOME') or os.path.expanduser('~/.hermes')
    base = os.path.abspath(base)
    out = [(os.path.join(base, 'skills'), 'default')]
    for d in sorted(glob.glob(os.path.join(base, 'profiles', '*', 'skills'))):
        out.append((d, os.path.basename(os.path.dirname(d))))
    return out


def main():
    ap = argparse.ArgumentParser(description='Renvois déclarés par les skills vs fichiers livrés (OUT-17).')
    ap.add_argument('--racine', action='append', default=None,
                    help='racine des skills (répétable ; défaut : tous les profils du home Hermes)')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--strict', action='store_true', help='les mentions manquantes deviennent bloquantes')
    a = ap.parse_args()

    rapport = {'racines': [], 'skills': 0, 'declares_manquants': 0, 'mentions_manquantes': 0}
    lignes = []
    for racine, profil in racines_skills(a.racine):
        if not os.path.isdir(racine):
            lignes.append('%-10s racine absente : %s' % (profil, racine))
            continue
        fiches = sorted(glob.glob(os.path.join(racine, '**', 'SKILL.md'), recursive=True))
        n_decl = n_ment = 0
        detail = []
        for f in fiches:
            d, m, declares = analyse_skill(f)
            nom = os.path.basename(os.path.dirname(f))
            n_decl += len(d)
            n_ment += len(m)
            if d or m:
                detail.append({'skill': nom, 'chemin': f, 'declares_manquants': d,
                               'mentions_manquantes': m, 'declares': len(declares)})
                for p in d:
                    lignes.append('    RENVOI MORT  %-34s %s' % (nom, p))
                for p in m:
                    lignes.append('    mention (non déclarée) %-22s %s' % (nom, p))
        rapport['racines'].append({'profil': profil, 'racine': racine, 'skills': len(fiches),
                                   'declares_manquants': n_decl, 'mentions_manquantes': n_ment,
                                   'detail': detail})
        rapport['skills'] += len(fiches)
        rapport['declares_manquants'] += n_decl
        rapport['mentions_manquantes'] += n_ment
        lignes.append('%-10s %3d skill(s) examiné(s) | renvois morts %d | mentions manquantes %d'
                      % (profil, len(fiches), n_decl, n_ment))

    if a.json:
        print(json.dumps(rapport, ensure_ascii=False, indent=1))
    else:
        print('Renvois déclarés par les skills — contrôle du %s' % __import__('time').strftime('%Y-%m-%d %H:%M'))
        for l in lignes:
            print('  ' + l)
        print('  total : %d skill(s), %d renvoi(s) mort(s), %d mention(s) manquante(s)'
              % (rapport['skills'], rapport['declares_manquants'], rapport['mentions_manquantes']))
    if rapport['declares_manquants'] or (a.strict and rapport['mentions_manquantes']):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
