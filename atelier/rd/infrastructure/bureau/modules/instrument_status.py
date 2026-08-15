"""État de l'Instrument de la Tradition Primordiale — lecture seule.

Ne lit que des sources déterministes : `instrument-donnees.yaml` (le
manifeste applicatif) et, s'il existe, `wiki-manifest.json`. Jamais de
parsing interprétatif de la prose des fiches d'architecture — dans l'esprit
de la règle des manifestes (§VII du protocole racine : dépôt → manifeste →
interface, à sens unique).
"""

from __future__ import annotations

import re
from datetime import datetime

import yaml
from rich.text import Text
from textual.containers import Vertical
from textual.widgets import Static

import config
from modules.base import Module

_VERSION_RE = re.compile(
    r"instrument-donnees\.yaml — Déclaration applicative de l'Instrument \(v([\w.]+)\)"
)


class InstrumentState:
    def __init__(self) -> None:
        self.version: str | None = None
        self.node_count: int | None = None
        self.last_modified: str | None = None
        self.error: str | None = None

    def load(self) -> None:
        path = config.INSTRUMENT_DONNEES
        if not path.exists():
            self.error = "instrument-donnees.yaml introuvable"
            return
        try:
            text = path.read_text(encoding="utf-8")
            match = _VERSION_RE.search(text)
            self.version = match.group(1) if match else None
            data = yaml.safe_load(text) or {}
            noeuds = data.get("noeuds") or []
            self.node_count = len(noeuds)
            mtime = datetime.fromtimestamp(path.stat().st_mtime)
            self.last_modified = mtime.strftime("%Y-%m-%d")
            self.error = None
        except Exception as exc:  # lecture seule : ne jamais planter le bureau
            self.error = f"erreur de lecture : {exc}"


class InstrumentModule(Module):
    key = "instrument"
    title = "Instrument"
    icon = "🜛"

    def __init__(self) -> None:
        self.state = InstrumentState()
        self.state.load()

    def _summary_text(self) -> Text:
        if self.state.error:
            return Text(f"⚠ {self.state.error}", style="yellow")
        t = Text()
        t.append(f"v{self.state.version or '?'}\n", style="bold cyan")
        t.append(f"{self.state.node_count or 0} nœuds déclarés\n")
        t.append(f"MAJ {self.state.last_modified or '?'}", style="dim")
        return t

    def summary_widget(self) -> Static:
        return Static(self._summary_text(), classes="tile-body")

    def full_widget(self) -> Vertical:
        body = Text()
        body.append("Instrument de la Tradition Primordiale\n\n", style="bold")
        body.append(self._summary_text())
        body.append("\n\nSource : atelier/rd/instrument/instrument-donnees.yaml\n")
        body.append("(manifeste déterministe — jamais de parsing de prose)\n", style="dim")
        return Vertical(Static(body))

    def refresh_interval(self) -> float | None:
        return 60.0

    async def refresh(self) -> None:
        self.state.load()
