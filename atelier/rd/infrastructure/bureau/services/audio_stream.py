"""Petit serveur HTTP de streaming audio.

Le tableau de bord pilote une playlist et ce serveur sert le fichier
sélectionné ; l'écoute réelle se fait côté client (ex. Safari iPad) via
tunnel SSH ou Tailscale vers ce port (bind 127.0.0.1 par défaut — jamais de
port ouvert publiquement, §VIII.8 du protocole).

Sert uniquement des fichiers audio situés sous `audio_root` (racine
configurée par l'appelant) — jamais en dehors, jamais d'écriture.
"""

from __future__ import annotations

import mimetypes
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

AUDIO_EXTENSIONS = {".mp3", ".flac", ".wav", ".ogg", ".m4a", ".opus"}


class PlaylistState:
    def __init__(self, audio_root: Path) -> None:
        self.audio_root = audio_root
        self._current: Path | None = None
        self._lock = threading.Lock()

    def list_tracks(self) -> list[Path]:
        if not self.audio_root.exists():
            return []
        return sorted(
            p for p in self.audio_root.rglob("*") if p.suffix.lower() in AUDIO_EXTENSIONS
        )

    def select(self, relative: str) -> Path | None:
        candidate = (self.audio_root / relative).resolve()
        try:
            candidate.relative_to(self.audio_root.resolve())
        except ValueError:
            return None
        if candidate.exists() and candidate.suffix.lower() in AUDIO_EXTENSIONS:
            with self._lock:
                self._current = candidate
            return candidate
        return None

    @property
    def current(self) -> Path | None:
        with self._lock:
            return self._current


def make_handler(state: PlaylistState) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args) -> None:  # silence stdout
            pass

        def do_GET(self) -> None:  # noqa: N802 (nom imposé par BaseHTTPRequestHandler)
            parsed = urlparse(self.path)

            if parsed.path == "/playlist":
                self._send_json(
                    [str(p.relative_to(state.audio_root)) for p in state.list_tracks()]
                )
                return

            if parsed.path == "/select":
                query = parse_qs(parsed.query)
                relative = unquote(query.get("file", [""])[0])
                track = state.select(relative)
                self._send_json({"selected": str(track) if track else None})
                return

            if parsed.path == "/current":
                self._stream_file(state.current)
                return

            self.send_error(404)

        def _send_json(self, payload) -> None:
            import json

            body = json.dumps(payload).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _stream_file(self, track: Path | None) -> None:
            if track is None or not track.exists():
                self.send_error(404, "Aucune piste sélectionnée")
                return
            mime, _ = mimetypes.guess_type(str(track))
            data = track.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", mime or "application/octet-stream")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Accept-Ranges", "bytes")
            self.end_headers()
            self.wfile.write(data)

    return Handler


def run(audio_root: Path, host: str, port: int) -> None:
    state = PlaylistState(audio_root)
    server = ThreadingHTTPServer((host, port), make_handler(state))
    print(f"Audio stream sur http://{host}:{port} (racine : {audio_root})")
    server.serve_forever()
