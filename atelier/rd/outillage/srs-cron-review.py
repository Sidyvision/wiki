#!/usr/bin/env python3
"""
SRS Review — Script cron pour révision quotidienne
Génère un rapport des cartes dues et le formate pour Discord
"""

import yaml
from datetime import datetime, timedelta
from pathlib import Path
import sys

SRS_CARDS_FILE = Path.home() / ".hermes" / "srs" / "srs-cards.yaml"

def load_cards():
    """Charge les cartes SRS"""
    if not SRS_CARDS_FILE.exists():
        return []
    with open(SRS_CARDS_FILE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('cards', [])

def get_due_cards(cards):
    """Récupère les cartes dues pour révision"""
    now = datetime.now()
    due = []
    for card in cards:
        next_review = datetime.fromisoformat(card['next_review'])
        if next_review <= now:
            due.append(card)
    return sorted(due, key=lambda c: c['ease_factor'])

def format_discord_message(cards, due_cards):
    """Formate le message pour Discord"""
    if not due_cards:
        next_date = min((c['next_review'] for c in cards), default='N/A')
        return f"🎴 **Révision SRS** — Aucune carte due\nProchaine révision : {next_date[:10]}"
    
    limit = min(5, len(due_cards))
    cards_to_show = due_cards[:limit]
    
    lines = [
        f"🎴 **Révision SRS** — {len(due_cards)} carte(s) due(s)",
        f"📚 Total : {len(cards)} cartes | ⏰ Dues : {len(due_cards)}",
        "",
        f"**{limit} premières cartes à réviser :**",
        ""
    ]
    
    for i, card in enumerate(cards_to_show, 1):
        lines.append(f"**{i}. [{card['categorie']}]** {card['question']}")
        lines.append(f"   _ease: {card['ease_factor']:.2f} | reps: {card['repetitions']}_")
        lines.append("")
    
    if len(due_cards) > limit:
        lines.append(f"_... et {len(due_cards) - limit} autre(s) carte(s)_")
        lines.append("")
    
    lines.append("💡 Commande : `hermes-srs review --limit 5`")
    lines.append("📊 Stats : `hermes-srs stats`")
    
    return '\n'.join(lines)

def main():
    cards = load_cards()
    if not cards:
        print("Aucune carte SRS trouvée. Lance `hermes-srs regenerate` pour en créer.")
        return 0
    
    due_cards = get_due_cards(cards)
    message = format_discord_message(cards, due_cards)
    print(message)
    return 0

if __name__ == "__main__":
    sys.exit(main())
