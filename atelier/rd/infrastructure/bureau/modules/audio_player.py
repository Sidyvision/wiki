"""Contrôle de la playlist audio — le rendu sonore se fait côté client.

Ce module pilote `services/audio_stream.py` (serveur HTTP local, bind
127.0.0.1) : il choisit la piste courante, le serveur la sert. Aucune lecture
audio locale sur ce serveur headless — l'écoute réelle se fait depuis
l'appareil de Sidy via tunnel SSH ou Tailscale vers ce port (§VIII.8).
"""

from __future__ import annotations

import threading
from pathlib import Path

from rich.text import Text
from textual.containers import Vertical
from textual.widgets import Static

import config
from modules.base import Module
from services.audio_stream import PlaylistState
from services.audio_stream import run as run_audio_server

AUDIO_ROOT = config.WIKI_ROOT / "label" / "musique"


class AudioModule(Module):
    key = "audio"
    title = "Audio"
    icon = "🜁"

    def __init__(self) -> None:
        self.state = PlaylistState(AUDIO_ROOT)
        self._server_started = False

    def ensure_server(self) -> None:
        if self._server_started:
            return
        thread = threading.Thread(
            target=run_audio_server,
            args=(AUDIO_ROOT, config.AUDIO_HOST, config.AUDIO_PORT),
            daemon=True,
        )
        thread.start()
        self._server_started = True

    def select_track(self, relative: str) -> Path | None:
        self.ensure_server()
        return self.state.select(relative)

    def _summary_text(self) -> Text:
        t = Text()
        current = self.state.current
        if not self._server_started:
            t.append("serveur arrêté\n", style="dim")
        else:
            t.append(f"http://{config.AUDIO_HOST}:{config.AUDIO_PORT}\n", style="dim cyan")
        if current:
            t.append(f"♪ {current.name}\n", style="bold")
        else:
            t.append("aucune piste sélectionnée\n", style="dim")
        tracks = self.state.list_tracks()
        t.append(f"{len(tracks)} piste(s) disponible(s)", style="dim")
        return t

    def summary_widget(self) -> Static:
        return Static(self._summary_text(), classes="tile-body")

    def full_widget(self) -> Vertical:
        body = Text()
        body.append("Playlist audio (streaming)\n\n", style="bold")
        body.append(self._summary_text())
        body.append("\n\n")
        for track in self.state.list_tracks():
            rel = track.relative_to(AUDIO_ROOT)
            marker = "▶ " if track == self.state.current else "  "
            body.append(f"{marker}{rel}\n")
        return Vertical(Static(body))

    def refresh_interval(self) -> float | None:
        return None

    async def refresh(self) -> None:
        return None
