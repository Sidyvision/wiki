"""Bureau TUI — tableau de bord modulaire (menu façon jeu vidéo).

Écran unique : grille de tuiles, une par module (`modules/base.Module`),
résumé visible en permanence. Flèches pour naviguer, Entrée pour agrandir une
tuile en plein panneau ("monocle"), Échap pour revenir à la grille. Ajouter un
module futur = un fichier de plus dans `modules/`, déclaré ci-dessous dans
`MODULES` — rien d'autre à toucher.

Lancement : `python3 app.py` (voir README.md pour le détail pédagogique).
"""

from __future__ import annotations

from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Grid, Vertical
from textual.screen import Screen
from textual.widgets import DirectoryTree, Footer, Header, Input, Static

from modules.audio_player import AudioModule
from modules.base import Module
from modules.chat import ChatModule
from modules.hermes_status import HermesModule
from modules.instrument_status import InstrumentModule
from modules.reader import ReaderModule
from modules.video_player import VideoModule

MODULES: list[Module] = [
    InstrumentModule(),
    HermesModule(),
    ReaderModule(),
    AudioModule(),
    VideoModule(),
    ChatModule(),
]

GRID_COLUMNS = 3

CSS = """
Screen {
    background: $surface;
}

#banner {
    height: 3;
    content-align: center middle;
    text-style: bold;
    color: $accent;
    border-bottom: heavy $accent;
}

#tile-grid {
    grid-size: 3;
    grid-gutter: 1 2;
    padding: 1 2;
}

.tile {
    border: round $primary;
    padding: 1 1;
    height: 100%;
}

.tile:focus {
    border: heavy $accent;
    background: $boost;
}

.tile-title {
    text-style: bold;
    color: $accent;
}

.tile-body {
    color: $text;
}

#monocle-title {
    height: 3;
    content-align: center middle;
    text-style: bold;
    color: $accent;
    border-bottom: heavy $accent;
}

#reader-tree-pane {
    width: 30%;
    border-right: solid $primary;
}

#chat-log {
    height: 1fr;
    border: solid $primary;
}
"""


class Tile(Static, can_focus=True):
    """Une tuile du menu principal — résumé d'un module, focusable."""

    def __init__(self, module: Module, index: int) -> None:
        super().__init__(classes="tile")
        self.module = module
        self.index = index

    def compose(self) -> ComposeResult:
        yield Static(f"{self.module.icon}  {self.module.title}", classes="tile-title")
        yield self.module.summary_widget()

    def refresh_summary(self) -> None:
        try:
            old = self.query(".tile-body").first()
            old.remove()
            self.mount(self.module.summary_widget())
        except Exception:
            pass


class MonocleScreen(Screen):
    """Vue plein panneau d'un module — Échap pour revenir à la grille."""

    BINDINGS = [Binding("escape", "app.pop_screen", "Retour")]

    def __init__(self, module: Module) -> None:
        super().__init__()
        self.module = module

    def compose(self) -> ComposeResult:
        yield Static(f"{self.module.icon}  {self.module.title}", id="monocle-title")
        yield self.module.full_widget()
        if isinstance(self.module, ChatModule):
            yield Input(placeholder="Message... (Entrée pour envoyer)", id="chat-input")
        yield Footer()

    def on_mount(self) -> None:
        if isinstance(self.module, ReaderModule):
            tree = self.query_one(DirectoryTree)
            tree.focus()
        if isinstance(self.module, ChatModule):
            self.module.start_client(self._on_chat_message)
            self.query_one("#chat-input", Input).focus()

    def _on_chat_message(self, author: str, text: str) -> None:
        self.app.call_from_thread(self._refresh_chat_body)

    def _refresh_chat_body(self) -> None:
        try:
            lines = "\n".join(f"{a}: {t}" for a, t in self.module.history) or "(aucun message)"
            self.query_one(Vertical).query_one(Static).update(lines)
        except Exception:
            pass

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if isinstance(self.module, ChatModule) and event.input.id == "chat-input":
            self.module.send(event.value)
            event.input.value = ""

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        if not isinstance(self.module, ReaderModule):
            return
        path = Path(event.path)
        suffix = path.suffix.lower()
        content_scroll = self.query_one("#reader-content-scroll")
        if suffix == ".md":
            content_scroll.query("*").remove()
            content_scroll.mount(self.module.markdown_widget(path))
        else:
            self.module.render_selected(path)


class BureauApp(App):
    """Tableau de bord — écran principal (grille) + écrans monocle."""

    CSS = CSS
    TITLE = "Bureau"

    BINDINGS = [
        Binding("left", "focus_previous", "◄", show=False),
        Binding("right", "focus_next", "►", show=False),
        Binding("up", "focus_previous", "▲", show=False),
        Binding("down", "focus_next", "▼", show=False),
        Binding("enter", "open_focused", "Ouvrir"),
        Binding("q", "quit", "Quitter"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("🜛  Bureau — Tableau de bord  🜛", id="banner")
        with Grid(id="tile-grid"):
            for index, module in enumerate(MODULES):
                yield Tile(module, index)
        yield Footer()

    def on_mount(self) -> None:
        self.query(Tile).first().focus()
        for module in MODULES:
            interval = module.refresh_interval()
            if interval:
                self.set_interval(interval, self._make_refresher(module))

    def _make_refresher(self, module: Module):
        async def _refresh() -> None:
            await module.refresh()
            for tile in self.query(Tile):
                if tile.module is module:
                    tile.refresh_summary()

        return _refresh

    def action_open_focused(self) -> None:
        focused = self.focused
        if isinstance(focused, Tile):
            self.push_screen(MonocleScreen(focused.module))


def main() -> None:
    BureauApp().run()


if __name__ == "__main__":
    main()
