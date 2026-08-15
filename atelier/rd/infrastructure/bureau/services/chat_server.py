"""Serveur de chat minimal (asyncio + websockets), diffusion à tous les clients.

Portée v1 : humains ↔ humains uniquement. La passerelle vers les agents
Hermès (relais Discord) est volontairement non implémentée ici — voir
`bureau-tui-architecture.md`, section "Décision de portée". Le point
d'extension prévu est `ChatBridge` ci-dessous, non branché.

Bind par défaut sur 127.0.0.1 (config.CHAT_HOST) : accès distant via tunnel
SSH ou Tailscale, jamais de port ouvert publiquement (§VIII.8 du protocole).
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import websockets
from websockets.server import WebSocketServerProtocol

import config


class ChatBridge:
    """Point d'extension pour une future passerelle (ex. relais Discord).

    Non implémenté en v1 (cf. décision de portée). Une implémentation future
    appellerait `broadcast()` pour injecter des messages externes, et
    recevrait les messages humains via `on_local_message`.
    """

    async def on_local_message(self, author: str, text: str) -> None:  # pragma: no cover
        return None


class ChatServer:
    def __init__(self, host: str = config.CHAT_HOST, port: int = config.CHAT_PORT) -> None:
        self.host = host
        self.port = port
        self.clients: set[WebSocketServerProtocol] = set()
        self.bridge = ChatBridge()

    async def _handler(self, websocket: WebSocketServerProtocol) -> None:
        self.clients.add(websocket)
        try:
            async for raw in websocket:
                try:
                    payload = json.loads(raw)
                    author = str(payload.get("author", "anonyme"))[:64]
                    text = str(payload.get("text", ""))[:2000]
                except (json.JSONDecodeError, TypeError):
                    continue
                if not text.strip():
                    continue
                await self.bridge.on_local_message(author, text)
                await self.broadcast(author, text)
        finally:
            self.clients.discard(websocket)

    async def broadcast(self, author: str, text: str) -> None:
        if not self.clients:
            return
        message = json.dumps({"author": author, "text": text})
        await asyncio.gather(
            *(client.send(message) for client in list(self.clients)),
            return_exceptions=True,
        )

    async def run(self) -> None:
        async with websockets.serve(self._handler, self.host, self.port):
            await asyncio.Future()  # tourne indéfiniment


def main() -> None:
    server = ChatServer()
    print(f"Chat server sur ws://{server.host}:{server.port}")
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
