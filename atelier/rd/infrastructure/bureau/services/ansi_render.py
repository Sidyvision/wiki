"""Rendu ANSI "demi-bloc", partagé entre le lecteur vidéo et le lecteur d'images.

Technique : chaque caractère `▀` (demi-bloc haut) porte une couleur de premier
plan (pixel du haut) et une couleur de fond (pixel du bas) — deux pixels par
caractère de terminal, sans dépendance externe lourde (pas de mpv/chafa,
disponible nulle part sur ce serveur). Résolution bornée par
`config.ANSI_MAX_COLS`/`ANSI_MAX_ROWS` pour rester léger.
"""

from __future__ import annotations

import subprocess
from collections.abc import Iterator
from pathlib import Path

from PIL import Image
from rich.text import Text

HALF_BLOCK = "▀"


def pixels_to_text(pixels: list[list[tuple[int, int, int]]]) -> Text:
    """Convertit une grille RGB (lignes x colonnes) en Rich Text demi-bloc."""
    height = len(pixels)
    width = len(pixels[0]) if height else 0
    out = Text()
    for y in range(0, height, 2):
        top_row = pixels[y]
        bottom_row = pixels[y + 1] if y + 1 < height else [(0, 0, 0)] * width
        for x in range(width):
            r1, g1, b1 = top_row[x]
            r2, g2, b2 = bottom_row[x]
            out.append(HALF_BLOCK, style=f"rgb({r1},{g1},{b1}) on rgb({r2},{g2},{b2})")
        out.append("\n")
    return out


def _image_to_pixel_grid(
    image: Image.Image, cols: int, rows: int
) -> list[list[tuple[int, int, int]]]:
    image = image.convert("RGB").resize((cols, rows * 2))
    width, height = image.size
    data = image.load()
    return [[data[x, y] for x in range(width)] for y in range(height)]


def image_to_ansi(path: Path, cols: int, rows: int) -> Text:
    with Image.open(path) as image:
        grid = _image_to_pixel_grid(image, cols, rows)
    return pixels_to_text(grid)


def ffmpeg_frame_grids(
    path: Path, cols: int, rows: int, fps: int = 10
) -> Iterator[list[list[tuple[int, int, int]]]]:
    """Décode `path` via ffmpeg, un frame RGB brut à la fois.

    Lancé uniquement sur action explicite (lecture demandée par l'utilisateur),
    jamais en tâche de fond — coût CPU assumé pour cet usage ponctuel.
    """
    height = rows * 2
    frame_size = cols * height * 3
    cmd = [
        "ffmpeg",
        "-i", str(path),
        "-vf", f"fps={fps},scale={cols}:{height}",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-loglevel", "error",
        "-",
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    assert proc.stdout is not None
    try:
        while True:
            raw = proc.stdout.read(frame_size)
            if len(raw) < frame_size:
                break
            grid = [
                [
                    (raw[i], raw[i + 1], raw[i + 2])
                    for i in range(row * cols * 3, (row + 1) * cols * 3, 3)
                ]
                for row in range(height)
            ]
            yield grid
    finally:
        proc.terminate()
        proc.wait(timeout=5)
