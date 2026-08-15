import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.ansi_render import pixels_to_text


def test_pixels_to_text_even_rows():
    grid = [
        [(255, 0, 0), (0, 255, 0)],
        [(0, 0, 255), (255, 255, 255)],
    ]
    text = pixels_to_text(grid)
    assert text.plain == "▀▀\n"


def test_pixels_to_text_odd_row_padded_with_black():
    grid = [
        [(255, 0, 0)],
    ]
    text = pixels_to_text(grid)
    assert text.plain == "▀\n"


def test_pixels_to_text_empty():
    text = pixels_to_text([])
    assert text.plain == ""
