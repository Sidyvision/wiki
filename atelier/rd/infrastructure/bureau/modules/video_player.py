"""Lecteur vidéo ANSI — rendu à la demande uniquement.

Le décodage `ffmpeg` (`services/ansi_render.ffmpeg_frame_grids`) n'est
déclenché que sur action explicite (`play`) : jamais en tâche de fond,
contrainte RAM/CPU du serveur (3.7 Go, swap actif — voir
`bureau-tui-architecture.md`). Navigue `config.READER_ROOTS` pour trouver un
fichier vidéo, comme le lecteur de textes/images.
"""

from __future__ import annotations

from pathlib import Path

from rich.text import Text
from textual.containers import Vertical
from textual.widgets import Static

import config
from modules.base import Module
from services.ansi_render import ffmpeg_frame_grids, pixels_to_text

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".mov", ".webm", ".avi"}


def _is_allowed(path: Path) -> bool:
    resolved = path.resolve()
    for root in config.READER_ROOTS:
        try:
            resolved.relative_to(root.resolve())
            return True
        except ValueError:
            continue
    return False


class VideoModule(Module):
    key = "video"
    title = "Vidéo"
    icon = "🜃"

    def __init__(self) -> None:
        self.current_path: Path | None = None
        self.playing: bool = False
        self._content_pane: Static | None = None

    def open(self, path: Path) -> bool:
        if not _is_allowed(path) or path.suffix.lower() not in VIDEO_EXTENSIONS:
            return False
        self.current_path = path
        self.playing = False
        return True

    def _summary_text(self) -> Text:
        t = Text()
        if self.current_path:
            t.append(f"🎬 {self.current_path.name}\n", style="bold")
            t.append("en lecture" if self.playing else "en pause", style="dim")
        else:
            t.append("aucune vidéo ouverte", style="dim")
        return t

    def summary_widget(self) -> Static:
        return Static(self._summary_text(), classes="tile-body")

    def full_widget(self) -> Vertical:
        self._content_pane = Static(self._summary_text())
        return Vertical(self._content_pane)

    def play_frames(self):
        """Générateur d'objets Text ANSI, un par frame — consommé par app.py.

        Rendu uniquement sur appel explicite (touche de lecture) : jamais
        pré-calculé, jamais en tâche de fond.
        """
        if self.current_path is None:
            return
        self.playing = True
        try:
            for grid in ffmpeg_frame_grids(
                self.current_path, config.ANSI_MAX_COLS, config.ANSI_MAX_ROWS
            ):
                yield pixels_to_text(grid)
        finally:
            self.playing = False

    def refresh_interval(self) -> float | None:
        return None

    async def refresh(self) -> None:
        return None
