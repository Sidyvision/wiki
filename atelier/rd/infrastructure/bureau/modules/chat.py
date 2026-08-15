"""Client TUI du salon de chat — se connecte à `services/chat_server.py`.

v1 humains ↔ humains uniquement (décision de portée du plan). Le serveur
tourne en process séparé, lancé par `app.py` au démarrage (voir `ensure_server`
dans `audio_player.py` pour le même patron) ; bind 127.0.0.1 par défaut, accès
distant via tunnel SSH ou Tailscale (§VIII.8).
"""

from __future__ import annotations

import asyncio
import json
import threading
from collections import deque

import websockets
from rich.text import Text
from textual.containers import Vertical
from textual.widgets import Static

import config
from modules.base import Module
from services.chat_server import ChatServer

MAX_HISTORY = 200


class ChatModule(Module):
    key = "chat"
    title = "Chat"
    icon = "🜄"

    def __init__(self, author: str = "sidy") -> None:
        self.author = author
        self.history: deque[tuple[str, str]] = deque(maxlen=MAX_HISTORY)
        self._server_started = False
        self._ws = None
        self._loop: asyncio.AbstractEventLoop | None = None
        self._client_thread: threading.Thread | None = None

    def ensure_server(self) -> None:
        if self._server_started:
            return
        server = ChatServer(host=config.CHAT_HOST, port=config.CHAT_PORT)

        def _run() -> None:
            asyncio.run(server.run())

        threading.Thread(target=_run, daemon=True).start()
        self._server_started = True

    def start_client(self, on_message) -> None:
        """Ouvre une connexion websocket persistante dans un thread dédié.

        `on_message(author, text)` est appelé pour chaque message reçu
        (y compris les propres messages émis, diffusés par le serveur).
        """
        self.ensure_server()

        def _run() -> None:
            asyncio.run(self._client_loop(on_message))

        self._client_thread = threading.Thread(target=_run, daemon=True)
        self._client_thread.start()

    async def _client_loop(self, on_message) -> None:
        uri = f"ws://{config.CHAT_HOST}:{config.CHAT_PORT}"
        async with websockets.connect(uri) as ws:
            self._ws = ws
            self._loop = asyncio.get_running_loop()
            async for raw in ws:
                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                author = payload.get("author", "?")
                text = payload.get("text", "")
                self.history.append((author, text))
                on_message(author, text)

    def send(self, text: str) -> None:
        if self._ws is None or self._loop is None or not text.strip():
            return
        payload = json.dumps({"author": self.author, "text": text})
        asyncio.run_coroutine_threadsafe(self._ws.send(payload), self._loop)

    def _summary_text(self) -> Text:
        t = Text()
        status = "connecté" if self._ws is not None else "hors ligne"
        t.append(f"salon local — {status}\n", style="dim")
        for author, text in list(self.history)[-3:]:
            t.append(f"{author}: ", style="bold")
            t.append(f"{text}\n")
        if not self.history:
            t.append("(aucun message)", style="dim")
        return t

    def summary_widget(self) -> Static:
        return Static(self._summary_text(), classes="tile-body")

    def full_widget(self) -> Vertical:
        body = Text()
        for author, text in self.history:
            body.append(f"{author}: ", style="bold")
            body.append(f"{text}\n")
        if not self.history:
            body.append("(aucun message)", style="dim")
        return Vertical(Static(body))

    def refresh_interval(self) -> float | None:
        return None

    async def refresh(self) -> None:
        return None
