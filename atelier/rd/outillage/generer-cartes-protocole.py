#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer-cartes-protocole.py — Extraction automatique de cartes SRS depuis CLAUDE.md

Ce script lit le protocole CLAUDE.md et extrait les éléments éligibles au SRS :
- Commandements absolus (Cmd 1-13)
- Interdits de liens étanchéité
- Lexique Sashimono (hozo, zōsaku, kari-kumi, kumiko, etc.)
- Table Karūbī ↔ destinataire
- Vocabulaire technique (navette, canonique, zones scellées, etc.)

Usage :
    python3 generer-cartes-protocole.py [--output srs-cards.yaml]

Résultat :
    Fichier YAML contenant toutes les cartes extraites, prêtes pour révision SRS.
"""

import argparse
import re
from datetime import date
from pathlib import Path


def extraire_commandements(claude_md: str) -> list[dict]:
    """Extrait les 13 commandements absolus."""
    cartes = []
    
    # Pattern : cherche les sections "## Commandements absolus" puis les items numérotés
    section_match = re.search(r'##\s+Commandements absolus.*?\n(.*?)(?=\n##\s+|\Z)', 
                              claude_md, re.DOTALL | re.IGNORECASE)
    if not section_match:
        return cartes
    
    section = section_match.group(1)
    
    # Pattern pour chaque commandement : "1. **Nom** : description" ou "1. **Nom** — description"
    cmd_pattern = re.compile(r'(\d+)\.\s+\*\*([^*]+)\*\*\s*[:\-—]\s*(.+?)(?=\n\d+\.|\Z)', 
                             re.DOTALL)
    
    for match in cmd_pattern.finditer(section):
        numero = match.group(1)
        nom = match.group(2).strip()
        description = match.group(3).strip()
        
        # Nettoyer la description (enlever saut de ligne multiple)
        description = re.sub(r'\n+', ' ', description)
        
        cartes.append({
            'id': f'cmd-{numero.zfill(2)}',
            'question': f'Quel est le commandement absolu n°{numero} ?',
            'reponse': f'**{nom}** : {description}',
            'categorie': 'commandement',
            'source': 'CLAUDE.md#commandements-absolus',
            'created': date.today().isoformat(),
            'last_reviewed': None,
            'next_review': date.today().isoformat(),
            'interval_days': 1,
            'ease_factor': 2.5,
            'repetitions': 0,
            'tags': ['fondamental', 'commandement']
        })
    
    return cartes


def extraire_etancheite(claude_md: str) -> list[dict]:
    """Extrait les règles d'étanchéité inter-circuits."""
    cartes = []
    
    # Pattern : "X ne lie JAMAIS vers Y" ou "X → Y interdit"
    patterns = [
        r'\*\*(\w+)/\*\*\s*(?:ne\s+)?lie(?:nt)?\s+(?:JAMAIS|jamais)\s+vers\s+\*\*(\w+)/\*\*',
        r'\*\*(\w+)/\*\*\s*→\s*\*\*(\w+)/\*\*\s*[:\-—]\s*\*\*JAMAIS\*\*',
        r'(?:Interdit|Interdits?|INTERDIT)\s*:\s*\*\*(\w+)/\*\*\s*(?:→|vers)\s*\*\*(\w+)/\*\*',
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, claude_md, re.IGNORECASE):
            source = match.group(1)
            cible = match.group(2)
            
            # Éviter les doublons
            carte_id = f'etancheite-{source}-{cible}'
            if any(c['id'] == carte_id for c in cartes):
                continue
            
            cartes.append({
                'id': carte_id,
                'question': f'Quel circuit ne peut jamais pointer vers {cible}/ ?',
                'reponse': f'**{source}/** ne lie jamais vers **{cible}/**',
                'categorie': 'etancheite',
                'source': 'CLAUDE.md#etancheite-inter-circuits',
                'created': date.today().isoformat(),
                'last_reviewed': None,
                'next_review': date.today().isoformat(),
                'interval_days': 1,
                'ease_factor': 2.5,
                'repetitions': 0,
                'tags': ['etancheite', 'architecture']
            })
    
    return cartes


def extraire_sashimono(claude_md: str) -> list[dict]:
    """Extrait le lexique Sashimono."""
    cartes = []
    
    # Termes Sashimono avec leurs définitions
    termes = {
        'hozo': 'Tenon-mortaise : ancrage d\'équivalence établi entre deux traditions',
        'zōsaku': 'Portance nulle : élément contingent qui ne porte rien doctrinalement',
        'kari-kumi': 'Assemblage à blanc : montage provisoire en attente de validation',
        'kumiko': 'Assemblage validé : joint doctrinal confirmé après vérification',
        'sumi-tsuke': 'Traçage : marquage des points d\'ancrage avant assemblage',
        'ki-dori': 'Choix du bois : sélection des sources et traditions pertinentes',
    }
    
    for terme, definition in termes.items():
        cartes.append({
            'id': f'sashimono-{terme}',
            'question': f'Que signifie le terme Sashimono "{terme}" ?',
            'reponse': definition,
            'categorie': 'sashimono',
            'source': 'CLAUDE.md#convention-sashimono',
            'created': date.today().isoformat(),
            'last_reviewed': None,
            'next_review': date.today().isoformat(),
            'interval_days': 1,
            'ease_factor': 2.5,
            'repetitions': 0,
            'tags': ['sashimono', 'vocabulaire']
        })
    
    return cartes


def extraire_karubi(claude_md: str) -> list[dict]:
    """Extrait la table Karūbī ↔ destinataire."""
    cartes = []
    
    # Pattern : table markdown avec colonnes "destinataire" et "nom_karubi"
    table_pattern = re.compile(
        r'\|\s*destinataire\s*\|\s*nom_karubi\s*\|.*?\n'
        r'\|[-\s|]+\|\n'
        r'(.*?)(?=\n\n|\Z)',
        re.DOTALL | re.IGNORECASE
    )
    
    match = table_pattern.search(claude_md)
    if not match:
        return cartes
    
    table_content = match.group(1)
    
    # Pattern pour chaque ligne de table
    row_pattern = re.compile(r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|')
    
    for row_match in row_pattern.finditer(table_content):
        destinataire = row_match.group(1).strip()
        nom_karubi = row_match.group(2).strip()
        
        # Nettoyer les noms
        destinataire = destinataire.replace('**', '').strip()
        nom_karubi = nom_karubi.replace('**', '').strip()
        
        if destinataire and nom_karubi and destinataire != 'destinataire':
            cartes.append({
                'id': f'karubi-{destinataire.lower().replace(" ", "-")}',
                'question': f'Quel est le nom Karūbī pour {destinataire} ?',
                'reponse': f'**{nom_karubi}**',
                'categorie': 'karubi',
                'source': 'CLAUDE.md#transmissions-karubi',
                'created': date.today().isoformat(),
                'last_reviewed': None,
                'next_review': date.today().isoformat(),
                'interval_days': 1,
                'ease_factor': 2.5,
                'repetitions': 0,
                'tags': ['karubi', 'transmission']
            })
    
    return cartes


def extraire_vocabulaire_technique(claude_md: str) -> list[dict]:
    """Extrait le vocabulaire technique du protocole."""
    cartes = []
    
    # Termes techniques avec leurs définitions
    termes = {
        'navette': 'Cycle de transmission d\'un fichier Karūbī entre Sidy et le destinataire',
        'canonique': 'Fichier Karūbī officiel, maintenu par Sidy (G0)',
        'zones scellées': 'Sections Karūbī protégées par hash, modifiables uniquement par Sidy',
        'zones de croissance': 'Sections Karūbī append-only (§8 Mémoire vivante, §9 Questions)',
        'G0': 'Génération 0 : Sidy, créateur et gardien du protocole Karūbī',
        'G1': 'Génération 1 : destinataires directs du Karūbī',
        'to-source': 'Marqueur indiquant qu\'une source doit être vérifiée dans le texte primaire',
        'append-only': 'Mode d\'écriture : on n\'efface jamais, on ajoute seulement',
        'kari-kumi (statut)': 'Brouillon en attente de validation, montage à blanc',
        'discernement': 'Circuit doctrinal pour les correspondances non encore tranchées',
        'VIGILANCE': 'Contrôle de conformité au protocole (Cmd 11)',
        'Sceau Recteur': 'Frontmatter doctrinal avec tous les champs obligatoires',
    }
    
    for terme, definition in termes.items():
        # Nettoyer le terme pour l'ID
        terme_id = terme.lower().replace(' ', '-').replace('(', '').replace(')', '')
        
        cartes.append({
            'id': f'vocab-{terme_id}',
            'question': f'Que signifie "{terme}" dans le contexte du dépôt ?',
            'reponse': definition,
            'categorie': 'vocabulaire',
            'source': 'CLAUDE.md',
            'created': date.today().isoformat(),
            'last_reviewed': None,
            'next_review': date.today().isoformat(),
            'interval_days': 1,
            'ease_factor': 2.5,
            'repetitions': 0,
            'tags': ['vocabulaire', 'protocole']
        })
    
    return cartes


def generer_yaml(cards: list[dict]) -> str:
    """Génère le contenu YAML pour les cartes."""
    import yaml
    
    data = {
        'cards': cards,
        'metadata': {
            'generated': date.today().isoformat(),
            'total': len(cards),
            'source': 'CLAUDE.md'
        }
    }
    
    return yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)


def main():
    parser = argparse.ArgumentParser(
        description='Extraction automatique de cartes SRS depuis CLAUDE.md'
    )
    parser.add_argument(
        '--output', '-o',
        default='srs-cards.yaml',
        help='Fichier de sortie (défaut : srs-cards.yaml)'
    )
    parser.add_argument(
        '--claude-md',
        default='/root/wiki/CLAUDE.md',
        help='Chemin vers CLAUDE.md (défaut : /root/wiki/CLAUDE.md)'
    )
    
    args = parser.parse_args()
    
    # Lire CLAUDE.md
    claude_path = Path(args.claude_md)
    if not claude_path.exists():
        print(f'Erreur : {claude_path} n\'existe pas')
        return 1
    
    claude_md = claude_path.read_text(encoding='utf-8')
    
    # Extraire les cartes
    print(f'Extraction depuis {claude_path}...')
    
    cartes_commandements = extraire_commandements(claude_md)
    print(f'  Commandements : {len(cartes_commandements)} cartes')
    
    cartes_etancheite = extraire_etancheite(claude_md)
    print(f'  Étanchéité : {len(cartes_etancheite)} cartes')
    
    cartes_sashimono = extraire_sashimono(claude_md)
    print(f'  Sashimono : {len(cartes_sashimono)} cartes')
    
    cartes_karubi = extraire_karubi(claude_md)
    print(f'  Karūbī : {len(cartes_karubi)} cartes')
    
    cartes_vocabulaire = extraire_vocabulaire_technique(claude_md)
    print(f'  Vocabulaire : {len(cartes_vocabulaire)} cartes')
    
    # Combiner toutes les cartes
    toutes_cartes = (
        cartes_commandements +
        cartes_etancheite +
        cartes_sashimono +
        cartes_karubi +
        cartes_vocabulaire
    )
    
    print(f'\nTotal : {len(toutes_cartes)} cartes extraites')
    
    # Générer YAML
    yaml_content = generer_yaml(toutes_cartes)
    
    # Écrire le fichier
    output_path = Path(args.output)
    output_path.write_text(yaml_content, encoding='utf-8')
    
    print(f'\nFichier généré : {output_path}')
    
    return 0


if __name__ == '__main__':
    exit(main())
