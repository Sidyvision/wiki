"""État des 12 agents Hermès — statut process + mission déclarée.

Statut : présence d'un process `hermes_cli.main --profile <profil> gateway
run` (les agents tournent en process de fond, pas en service systemd —
vérifié le 2026-08-15, `systemctl` ne renvoie rien pour hermes). Mission :
extraite du bloc `## Mission` de la fiche `hermes-prompts/NN-*.md`
correspondante — lecture seule, aucune écriture, aucune donnée personnelle
recopiée (seul le rôle fonctionnel est affiché, jamais le contexte
d'harmonisation zodiacal des fiches).
"""

from __future__ import annotations

import re
import subprocess

from rich.text import Text
from textual.containers import Vertical
from textual.widgets import Static

import config
from modules.base import Module

# profil hermes -> fichier de mission (meta/projet-unifie/hermes-prompts/)
PROFILES = [
    ("ar-music", "01-ar-music-artistic-direction.md"),
    ("visual-da", "02-visual-editorial-artistic-direction.md"),
    ("production", "03-production-manager.md"),
    ("admin-legal", "04-administration-legal.md"),
    ("accounting", "05-accounting-management.md"),
    ("distribution", "06-distribution.md"),
    ("marketing", "07-marketing-communication.md"),
    ("publication", "08-publication-site/08-principe.md"),
    ("studio", "09-studio-sound-engineer.md"),
    ("gardien", "10-protocol-guardian.md"),
    ("fanzine", "11-fanzine-editor.md"),
    ("commerce", "12-commerce-profitability.md"),
]

_ROLE_RE = re.compile(r"^#\s*ROLE:\s*(.+)$", re.MULTILINE)
_MISSION_RE = re.compile(r"^##\s*Mission\s*\n(.+?)(?=\n##\s|\Z)", re.MULTILINE | re.DOTALL)


class AgentInfo:
    def __init__(self, profile: str) -> None:
        self.profile = profile
        self.running: bool = False
        self.role: str | None = None
        self.mission: str | None = None
        self.error: str | None = None


class HermesFleetState:
    def __init__(self) -> None:
        self.agents: list[AgentInfo] = []

    def _is_running(self, profile: str) -> bool:
        pattern = f"hermes_cli.main --profile {profile} gateway run"
        try:
            result = subprocess.run(
                ["pgrep", "-f", pattern], capture_output=True, timeout=3
            )
            return result.returncode == 0
        except Exception:
            return False

    def _read_mission(self, filename: str) -> tuple[str | None, str | None, str | None]:
        path = config.HERMES_PROMPTS_DIR / filename
        if not path.exists():
            return None, None, "fiche introuvable"
        try:
            text = path.read_text(encoding="utf-8")
            role_match = _ROLE_RE.search(text)
            mission_match = _MISSION_RE.search(text)
            role = role_match.group(1).strip() if role_match else None
            mission = mission_match.group(1).strip() if mission_match else None
            return role, mission, None
        except Exception as exc:
            return None, None, f"erreur de lecture : {exc}"

    def load(self) -> None:
        agents = []
        for profile, filename in PROFILES:
            info = AgentInfo(profile)
            info.running = self._is_running(profile)
            info.role, info.mission, info.error = self._read_mission(filename)
            agents.append(info)
        self.agents = agents

    @property
    def running_count(self) -> int:
        return sum(1 for a in self.agents if a.running)


class HermesModule(Module):
    key = "hermes"
    title = "Agents Hermès"
    icon = "🜂"

    def __init__(self) -> None:
        self.state = HermesFleetState()
        self.state.load()

    def _summary_text(self) -> Text:
        t = Text()
        t.append(f"{self.state.running_count}/12 actifs\n", style="bold cyan")
        for agent in self.state.agents:
            dot = "●" if agent.running else "○"
            style = "green" if agent.running else "dim red"
            t.append(f"{dot} ", style=style)
            t.append(f"{agent.profile}\n", style="dim" if not agent.running else "")
        return t

    def summary_widget(self) -> Static:
        return Static(self._summary_text(), classes="tile-body")

    def full_widget(self) -> Vertical:
        body = Text()
        body.append("Flotte d'agents Hermès\n\n", style="bold")
        body.append(f"{self.state.running_count}/12 process actifs\n\n", style="bold cyan")
        for agent in self.state.agents:
            dot = "●" if agent.running else "○"
            style = "green" if agent.running else "dim red"
            body.append(f"{dot} ", style=style)
            body.append(f"{agent.profile}\n", style="bold")
            if agent.role:
                body.append(f"    {agent.role}\n", style="dim")
            if agent.mission:
                first_line = agent.mission.splitlines()[0].strip()
                body.append(f"    {first_line}\n", style="italic dim")
            if agent.error:
                body.append(f"    ⚠ {agent.error}\n", style="yellow")
            body.append("\n")
        return Vertical(Static(body))

    def refresh_interval(self) -> float | None:
        return 30.0

    async def refresh(self) -> None:
        self.state.load()
