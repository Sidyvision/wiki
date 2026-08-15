"""Configuration du Bureau TUI.

Lit un fichier `.env` local (jamais commité) pour les valeurs qui pourraient
un jour devenir sensibles (ports non standards, tokens futurs). Aucune valeur
par défaut ci-dessous n'est un secret.
"""

from __future__ import annotations

import os
from pathlib import Path

BUREAU_DIR = Path(__file__).resolve().parent
WIKI_ROOT = BUREAU_DIR.parent.parent.parent.parent  # atelier/rd/infrastructure/bureau -> wiki/


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


_load_dotenv(BUREAU_DIR / ".env")

# Bind local par défaut — accès distant via tunnel SSH ou Tailscale (§VIII.8
# du protocole du dépôt), jamais de port ouvert publiquement par ce projet.
CHAT_HOST = os.environ.get("BUREAU_CHAT_HOST", "127.0.0.1")
CHAT_PORT = int(os.environ.get("BUREAU_CHAT_PORT", "8765"))

AUDIO_HOST = os.environ.get("BUREAU_AUDIO_HOST", "127.0.0.1")
AUDIO_PORT = int(os.environ.get("BUREAU_AUDIO_PORT", "8766"))

# Racines de lecture autorisées pour le lecteur texte/image/pdf — jamais
# d'écriture, jamais de sortie de ces racines.
READER_ROOTS = [
    WIKI_ROOT / "atelier",
    WIKI_ROOT / "doctrinal",
    WIKI_ROOT / "hermeneutique",
    WIKI_ROOT / "label",
]

# Rendu ANSI demi-bloc : résolution bornée pour rester léger sur un serveur
# à 3.7 Go de RAM.
ANSI_MAX_COLS = int(os.environ.get("BUREAU_ANSI_MAX_COLS", "80"))
ANSI_MAX_ROWS = int(os.environ.get("BUREAU_ANSI_MAX_ROWS", "40"))

HERMES_PROMPTS_DIR = WIKI_ROOT / "meta" / "projet-unifie" / "hermes-prompts"
INSTRUMENT_DONNEES = WIKI_ROOT / "atelier" / "rd" / "instrument" / "instrument-donnees.yaml"
INSTRUMENT_MANIFEST = WIKI_ROOT / "atelier" / "rd" / "instrument" / "wiki-manifest.json"
