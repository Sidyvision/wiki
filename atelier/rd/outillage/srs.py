#!/usr/bin/env python3
"""
SRS Hermes-Native — Système de Répétition Espacée pour révision du protocole

Implémentation complète :
- Stockage YAML des cartes (srs-cards.yaml)
- Algorithme SM-2 pour espacement optimal
- Mode interactif pour révision
- Mode stats pour consultation
- Mode regenerate pour régénération depuis CLAUDE.md
"""

import yaml
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path
import random

# Configuration
SRS_DIR = Path.home() / ".hermes" / "srs"
CARDS_FILE = SRS_DIR / "srs-cards.yaml"
HISTORY_FILE = SRS_DIR / "srs-history.yaml"


def ensure_srs_dir():
    """Crée le répertoire SRS si nécessaire."""
    SRS_DIR.mkdir(parents=True, exist_ok=True)


def load_cards():
    """Charge les cartes depuis le fichier YAML."""
    ensure_srs_dir()
    if not CARDS_FILE.exists():
        return []
    
    with open(CARDS_FILE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('cards', [])


def save_cards(cards):
    """Sauvegarde les cartes dans le fichier YAML."""
    ensure_srs_dir()
    with open(CARDS_FILE, 'w', encoding='utf-8') as f:
        yaml.dump({'cards': cards}, f, allow_unicode=True, default_flow_style=False)


def load_history():
    """Charge l'historique des révisions."""
    ensure_srs_dir()
    if not HISTORY_FILE.exists():
        return []
    
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('history', [])


def save_history(history):
    """Sauvegarde l'historique des révisions."""
    ensure_srs_dir()
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        yaml.dump({'history': history}, f, allow_unicode=True, default_flow_style=False)


def calculate_next_review(card, quality):
    """
    Calcule la prochaine date de révision selon l'algorithme SM-2.
    
    quality: 0-5
    - 0: blackout total
    - 1: presque correct
    - 2: difficile, mais correct
    - 3: correct avec effort
    - 4: correct, facile
    - 5: parfait, instantané
    """
    ease_factor = card.get('ease_factor', 2.5)
    interval_days = card.get('interval_days', 1)
    repetitions = card.get('repetitions', 0)
    
    if quality < 3:
        # Réponse incorrecte : reset
        repetitions = 0
        interval_days = 1
    else:
        # Réponse correcte
        repetitions += 1
        
        if repetitions == 1:
            interval_days = 1
        elif repetitions == 2:
            interval_days = 6
        else:
            interval_days = round(interval_days * ease_factor)
    
    # Mise à jour du facteur de facilité
    ease_factor = max(
        1.3,
        ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    )
    
    next_review = datetime.now() + timedelta(days=interval_days)
    
    return {
        'ease_factor': round(ease_factor, 2),
        'interval_days': interval_days,
        'repetitions': repetitions,
        'next_review': next_review.isoformat(),
        'last_reviewed': datetime.now().isoformat()
    }


def get_due_cards(cards, limit=None):
    """Récupère les cartes dues pour révision, triées par priorité."""
    now = datetime.now()
    due_cards = []
    
    for card in cards:
        next_review_str = card.get('next_review')
        if not next_review_str:
            # Carte jamais révisée : due immédiatement
            due_cards.append(card)
            continue
        
        next_review = datetime.fromisoformat(next_review_str)
        if next_review <= now:
            due_cards.append(card)
    
    # Tri par priorité : ease_factor ascendant (les plus difficiles d'abord)
    due_cards.sort(key=lambda c: c.get('ease_factor', 2.5))
    
    if limit:
        return due_cards[:limit]
    
    return due_cards


def cmd_review(args):
    """Mode interactif : révision de cartes dues."""
    cards = load_cards()
    history = load_history()
    
    # Nombre de cartes par session
    limit = 5
    if '--limit' in args:
        idx = args.index('--limit')
        if idx + 1 < len(args):
            limit = int(args[idx + 1])
    
    due_cards = get_due_cards(cards, limit)
    
    if not due_cards:
        print("✓ Aucune carte due pour révision.")
        print(f"  Prochaine révision : {min((c.get('next_review', '2099-12-31') for c in cards), default='N/A')}")
        return
    
    print(f"=== RÉVISION SRS — {len(due_cards)} carte(s) due(s) ===\n")
    
    reviewed = 0
    for card in due_cards:
        print(f"━━━ Carte {reviewed + 1}/{len(due_cards)} ━━━")
        print(f"Catégorie : {card.get('categorie', 'N/A')}")
        print(f"ID : {card.get('id', 'N/A')}")
        print(f"\nQuestion : {card.get('question', 'N/A')}\n")
        
        # Attente de la réponse de l'utilisateur
        input("Appuie sur Entrée pour voir la réponse...")
        print(f"\nRéponse : {card.get('reponse', 'N/A')}\n")
        print(f"Source : {card.get('source', 'N/A')}")
        
        # Auto-évaluation
        while True:
            try:
                print("\nAuto-évaluation (0-5) :")
                print("  0 : blackout total")
                print("  1 : presque correct")
                print("  2 : difficile, mais correct")
                print("  3 : correct avec effort")
                print("  4 : correct, facile")
                print("  5 : parfait, instantané")
                
                quality = int(input("\nNote (0-5) : "))
                if 0 <= quality <= 5:
                    break
                print("Note invalide, recommence.")
            except ValueError:
                print("Entrée invalide, recommence.")
        
        # Mise à jour de la carte
        updates = calculate_next_review(card, quality)
        card.update(updates)
        
        # Historique
        history.append({
            'card_id': card.get('id'),
            'timestamp': datetime.now().isoformat(),
            'quality': quality,
            'categorie': card.get('categorie')
        })
        
        reviewed += 1
        print(f"\n✓ Carte mise à jour. Prochaine révision : {card['next_review'][:10]}")
        print(f"  ease_factor : {card['ease_factor']}, interval : {card['interval_days']}j\n")
    
    # Sauvegarde
    save_cards(cards)
    save_history(history)
    
    print(f"=== RÉVISION TERMINÉE — {reviewed} carte(s) révisée(s) ===")


def cmd_stats(args):
    """Affiche les statistiques SRS."""
    cards = load_cards()
    history = load_history()
    
    if not cards:
        print("Aucune carte SRS. Lance 'srs regenerate' pour en créer.")
        return
    
    # Statistiques globales
    total = len(cards)
    due = len(get_due_cards(cards))
    
    print(f"=== STATISTIQUES SRS ===\n")
    print(f"Total cartes : {total}")
    print(f"Cartes dues : {due}")
    print(f"Cartes à jour : {total - due}")
    
    # Répartition par catégorie
    categories = {}
    for card in cards:
        cat = card.get('categorie', 'inconnu')
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\nRépartition par catégorie :")
    for cat, count in sorted(categories.items()):
        print(f"  {cat} : {count}")
    
    # Historique
    if history:
        print(f"\nHistorique révisions : {len(history)}")
        if len(history) >= 5:
            print("  5 dernières révisions :")
            for entry in history[-5:]:
                print(f"    {entry['timestamp'][:10]} : {entry['card_id']} (qualité {entry['quality']})")
    
    # Prochaine révision
    due_cards = get_due_cards(cards, limit=1)
    if due_cards:
        print(f"\nProchaine carte due : {due_cards[0].get('id')} ({due_cards[0].get('categorie')})")
    else:
        next_reviews = [datetime.fromisoformat(c['next_review']) for c in cards if c.get('next_review')]
        if next_reviews:
            next_date = min(next_reviews)
            print(f"\nProchaine révision : {next_date.strftime('%Y-%m-%d')}")


def cmd_regenerate(args):
    """Régénère les cartes depuis CLAUDE.md."""
    script_path = Path("/root/wiki/atelier/rd/outillage/generer-cartes-protocole.py")
    
    if not script_path.exists():
        print(f"Erreur : script de génération introuvable : {script_path}")
        return
    
    # Chargement des cartes existantes pour préserver l'historique
    old_cards = load_cards()
    old_cards_by_id = {c['id']: c for c in old_cards}
    
    # Exécution du script de génération
    import subprocess
    result = subprocess.run(
        ['python3', str(script_path), '--output', str(CARDS_FILE)],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Erreur lors de la génération :")
        print(result.stderr)
        return
    
    print(result.stdout)
    
    # Restauration de l'historique pour les cartes existantes
    new_cards = load_cards()
    restored = 0
    for card in new_cards:
        card_id = card.get('id')
        if card_id in old_cards_by_id:
            old_card = old_cards_by_id[card_id]
            # Conserver ease_factor, interval_days, repetitions, next_review, last_reviewed
            card['ease_factor'] = old_card.get('ease_factor', 2.5)
            card['interval_days'] = old_card.get('interval_days', 1)
            card['repetitions'] = old_card.get('repetitions', 0)
            card['next_review'] = old_card.get('next_review')
            card['last_reviewed'] = old_card.get('last_reviewed')
            restored += 1
    
    save_cards(new_cards)
    
    print(f"\n✓ {len(new_cards)} cartes régénérées")
    print(f"  {restored} cartes avec historique préservé")
    print(f"  {len(new_cards) - restored} nouvelles cartes")


def cmd_help(args):
    """Affiche l'aide."""
    print("""
SRS Hermes-Native — Système de Répétition Espacée

Usage : srs <commande> [options]

Commandes :
  review [--limit N]    Révision interactive de cartes dues (défaut : 5 cartes)
  stats                 Affiche les statistiques SRS
  regenerate            Régénère les cartes depuis CLAUDE.md (préserve historique)
  help                  Affiche cette aide

Exemples :
  srs review            Révise 5 cartes dues
  srs review --limit 10 Révise 10 cartes dues
  srs stats             Voir les statistiques
  srs regenerate        Mettre à jour les cartes depuis le protocole

Fichiers :
  ~/.hermes/srs/srs-cards.yaml      Cartes SRS
  ~/.hermes/srs/srs-history.yaml    Historique des révisions
""")


def main():
    if len(sys.argv) < 2:
        cmd_help([])
        return
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    commands = {
        'review': cmd_review,
        'stats': cmd_stats,
        'regenerate': cmd_regenerate,
        'help': cmd_help
    }
    
    if command in commands:
        commands[command](args)
    else:
        print(f"Commande inconnue : {command}")
        cmd_help([])


if __name__ == '__main__':
    main()
