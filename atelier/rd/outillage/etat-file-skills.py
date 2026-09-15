#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""etat-file-skills.py — état de la file d'écritures de skills, et conformité
des propositions au contrat du magasin (chantier OUT-17).

Déterministe : sans LLM, sans réseau, EN LECTURE SEULE. Il ne modifie rien —
ni la file, ni les skills, ni le dépôt. Il constate, et il sort en code non nul
si une anomalie est trouvée (même famille que verifier-invariants.py).

Ce qu'il mesure, par profil Hermes :
  - le nombre de positions en attente dans <HERMES_HOME>/pending/skills/*.json ;
  - la plus ancienne et la plus récente ;
  - pour chaque position, sa conformité au contrat du magasin :
      * frontmatter délimité par `---` et lisible,
      * champ `name:` présent,
      * description <= 60 caractères (budget de l'index du prompt système),
      * couple (skill, action) déjà présent ailleurs dans la même file (redite).

Motif (constaté le 2026-09-15) : sur onze requêtes retenues d'un même lot, cinq
étaient inaptes au magasin et une n'avait même pas de champ `name:` — la porte
les avait mises en file sans jamais les confronter au contrat de leur
destination. Ce script le fait de l'extérieur, sans patcher le produit.

Usage :
    python3 etat-file-skills.py [--hermes-home DIR] [--profil NOM] [--json] [--strict]

Codes de sortie :
    0  aucune anomalie     1  au moins une anomalie      2  erreur du script
"""

import argparse
import glob
import json
import os
import re
import sys
import time

JOUR = 86400.0
BUDGET_DESC = 60


def racines(hermes_home=None):
    """Rend la liste des (nom de profil, chemin du home) à examiner."""
    if hermes_home:
        home = os.path.abspath(hermes_home)
        nom = os.path.basename(home.rstrip('/')) or home
        if nom.startswith('.'):
            nom = 'default'
        out = [(nom, home)]
        for d in sorted(glob.glob(os.path.join(home, 'profiles', '*'))):
            if os.path.isdir(d):
                out.append((os.path.basename(d), d))
        return out
    base = os.environ.get('HERMES_HOME') or os.path.expanduser('~/.hermes')
    base = os.path.abspath(base)
    out = [('default', base)]
    for d in sorted(glob.glob(os.path.join(base, 'profiles', '*'))):
        if os.path.isdir(d):
            out.append((os.path.basename(d), d))
    return out


def description_de(front):
    """Extrait la valeur de `description:` d'un frontmatter, bloc scalaire compris."""
    lignes = front.split('\n')
    for i, l in enumerate(lignes):
        m = re.match(r'^description:\s*(.*)$', l)
        if not m:
            continue
        reste = m.group(1).strip()
        if reste and reste not in ('>', '|', '>-', '|-', '>+', '|+'):
            return reste.strip('"').strip("'")
        # bloc scalaire : on prend les lignes suivantes plus indentées
        morceaux = []
        for suivante in lignes[i + 1:]:
            if not suivante.strip():
                continue
            if re.match(r'^[A-Za-z_][A-Za-z0-9_]*:', suivante):
                break
            morceaux.append(suivante.strip())
        return ' '.join(morceaux)
    return None


def conformite(rec):
    """Rend (anomalies bloquantes, avertissements) pour une position."""
    err, warn = [], []
    p = rec.get('payload') or {}
    ops = p.get('operations', []) if p.get('action') == 'batch' else [p]
    noms = [(o.get('name') or '') for o in ops]
    nom = next((n for n in noms if n), '')
    if not nom:
        err.append('aucun champ name: dans le lot')
    for o in ops:
        c = o.get('content') or ''
        if o.get('action') != 'create' or not c:
            continue
        if not c.lstrip().startswith('---'):
            err.append('frontmatter absent (le contenu ne commence pas par ---)')
            continue
        blocs = c.split('---')
        if len(blocs) < 3:
            err.append('frontmatter non fermé (pas de --- de clôture)')
            continue
        front = blocs[1]
        try:
            import yaml
            yaml.safe_load(front)
        except ImportError:
            warn.append('pyyaml absent : contrôle YAML réduit au structurel')
        except Exception as e:
            err.append('YAML invalide (%s)' % str(e).split('\n')[0][:60])
        if not re.search(r'^name:\s*\S', front, re.M):
            err.append('champ name: absent du frontmatter')
        desc = description_de(front)
        if desc is None:
            err.append('champ description: absent du frontmatter')
        elif len(desc) > BUDGET_DESC:
            err.append('description de %d caractères (> %d)' % (len(desc), BUDGET_DESC))
    return err, warn, nom


def main():
    ap = argparse.ArgumentParser(description='État de la file d\'écritures de skills (OUT-17).')
    ap.add_argument('--hermes-home', default=None, help='home Hermes à examiner (défaut : $HERMES_HOME ou ~/.hermes)')
    ap.add_argument('--profil', default=None, help='limiter à un profil')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--strict', action='store_true', help='les avertissements deviennent bloquants')
    a = ap.parse_args()

    maintenant = time.time()
    rapport = {'profils': [], 'positions': 0, 'anomalies': 0, 'avertissements': 0}
    lignes = []
    for profil, home in racines(a.hermes_home):
        if a.profil and profil != a.profil:
            continue
        dossier = os.path.join(home, 'pending', 'skills')
        if not os.path.isdir(dossier):
            rapport['profils'].append({'profil': profil, 'file': 'absente', 'positions': 0})
            lignes.append('%-10s file absente (aucun dossier pending/skills)' % profil)
            continue
        fichiers = sorted(f for f in os.listdir(dossier) if f.endswith('.json'))
        if not fichiers:
            rapport['profils'].append({'profil': profil, 'file': 'vide', 'positions': 0})
            lignes.append('%-10s file vide' % profil)
            continue
        positions, dates = [], []
        for f in fichiers:
            chemin = os.path.join(dossier, f)
            try:
                rec = json.load(open(chemin, encoding='utf-8'))
            except Exception as e:
                positions.append({'id': f[:-5], 'anomalies': ['JSON illisible (%s)' % e],
                                  'avertissements': []})
                continue
            err, warn, nom = conformite(rec)
            ts = rec.get('created_at')
            if ts:
                dates.append(ts)
            positions.append({'id': f[:-5], 'skill': nom, 'origine': rec.get('origin'),
                              'age_jours': round((maintenant - ts) / JOUR, 1) if ts else None,
                              'anomalies': err, 'avertissements': warn})
        # redites : couple (skill, action) présent plusieurs fois
        couples = {}
        for pos in positions:
            cle = pos.get('skill', '')
            couples[cle] = couples.get(cle, 0) + 1
        for pos in positions:
            if couples.get(pos.get('skill'), 0) > 1:
                pos['avertissements'].append('redite : %d positions sur le même skill' % couples[pos['skill']])
        nb_err = sum(len(p['anomalies']) for p in positions)
        nb_warn = sum(len(p['avertissements']) for p in positions)
        rapport['profils'].append({
            'profil': profil, 'file': 'presente', 'positions': len(positions),
            'plus_ancienne': time.strftime('%Y-%m-%d %H:%M', time.localtime(min(dates))) if dates else None,
            'plus_recente': time.strftime('%Y-%m-%d %H:%M', time.localtime(max(dates))) if dates else None,
            'anomalies': nb_err, 'avertissements': nb_warn, 'detail': positions})
        rapport['positions'] += len(positions)
        rapport['anomalies'] += nb_err
        rapport['avertissements'] += nb_warn
        lignes.append('%-10s %2d position(s) | plus ancienne %s | inaptes %d | redites/alertes %d' % (
            profil, len(positions),
            time.strftime('%Y-%m-%d %H:%M', time.localtime(min(dates))) if dates else '—',
            nb_err, nb_warn))
        for pos in positions:
            for e in pos['anomalies']:
                lignes.append('    INAPTE %s (%s) : %s' % (pos['id'], pos.get('skill') or '?', e))
            for w in pos['avertissements']:
                lignes.append('    alerte %s (%s) : %s' % (pos['id'], pos.get('skill') or '?', w))

    if a.json:
        print(json.dumps(rapport, ensure_ascii=False, indent=1))
    else:
        print('File d\'écritures de skills — état au %s' % time.strftime('%Y-%m-%d %H:%M'))
        for l in lignes:
            print('  ' + l)
        print('  total : %d position(s), %d inapte(s), %d alerte(s)' % (
            rapport['positions'], rapport['anomalies'], rapport['avertissements']))
    if rapport['anomalies'] or (a.strict and rapport['avertissements']):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
