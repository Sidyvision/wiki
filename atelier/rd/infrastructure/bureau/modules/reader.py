"""Lecteur de textes/images façon Internet Archive — lecture seule.

Navigue les racines autorisées de `config.READER_ROOTS` (les quatre circuits
publics du dépôt ; `meta/` et `_inbox/` ne sont jamais exposés ici). Rendu :
`.md` via le widget `Markdown` de Textual, `.pdf` via extraction de texte
paginée (`pypdf`), images via le rendu ANSI demi-bloc partagé
(`services/ansi_render`). Aucune écriture, jamais de sortie des racines
autorisées (vérifié par `_is_allowed`).
"""

from __future__ import annotations

from pathlib import Path

from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import DirectoryTree, Markdown, Static

import config
from modules.base import Module
from services.ansi_render import image_to_ansi

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}


def _is_allowed(path: Path) -> bool:
    resolved = path.resolve()
    for root in config.READER_ROOTS:
        try:
            resolved.relative_to(root.resolve())
            return True
        except ValueError:
            continue
    return False


class ReaderRootTree(DirectoryTree):
    """Arbre de fichiers restreint aux racines autorisées du dépôt."""

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".") and _is_allowed(p)]


class PdfPager:
    """Pagination simple d'un PDF déjà extrait en texte, une page = un écran."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.pages: list[str] = []
        self.index = 0
        self.error: str | None = None
        self._load()

    def _load(self) -> None:
        try:
            from pypdf import PdfReader

            reader = PdfReader(str(self.path))
            self.pages = [page.extract_text() or "(page vide)" for page in reader.pages]
        except Exception as exc:
            self.error = f"erreur de lecture PDF : {exc}"

    def current(self) -> str:
        if self.error:
            return self.error
        if not self.pages:
            return "(aucun texte extractible)"
        return self.pages[self.index]

    def next(self) -> None:
        if self.pages and self.index < len(self.pages) - 1:
            self.index += 1

    def previous(self) -> None:
        if self.pages and self.index > 0:
            self.index -= 1


class ReaderModule(Module):
    key = "reader"
    title = "Lecteur"
    icon = "📜"

    def __init__(self) -> None:
        self.current_path: Path | None = None
        self._content_pane: Static | None = None
        self._pdf_pager: PdfPager | None = None

    def _open(self, path: Path) -> None:
        if not _is_allowed(path):
            return
        self.current_path = path
        self._pdf_pager = None
        if path.suffix.lower() == ".pdf":
            self._pdf_pager = PdfPager(path)

    def summary_widget(self) -> Static:
        if self.current_path:
            label = str(self.current_path.relative_to(config.WIKI_ROOT))
        else:
            label = "aucun fichier ouvert"
        return Static(f"📜 {label}", classes="tile-body")

    def full_widget(self) -> Horizontal:
        roots = config.READER_ROOTS
        tree_root = roots[0] if roots else config.WIKI_ROOT
        tree = ReaderRootTree(tree_root, id="reader-tree")

        self._content_pane = Static("Sélectionnez un fichier dans l'arbre.", id="reader-content")
        content = VerticalScroll(self._content_pane, id="reader-content-scroll")

        return Horizontal(Vertical(tree, id="reader-tree-pane"), content)

    def render_selected(self, path: Path) -> None:
        """Appelé par app.py sur sélection d'un nœud du DirectoryTree.

        Cas `.md` : app.py monte `markdown_widget()` à la place de ce pane
        directement (widget de type différent, hors compétence de cette
        méthode qui ne fait que mettre à jour un `Static` existant).
        """
        if not _is_allowed(path) or path.is_dir() or path.suffix.lower() == ".md":
            return
        self._open(path)
        if self._content_pane is None:
            return

        suffix = path.suffix.lower()
        try:
            if suffix == ".pdf" and self._pdf_pager is not None:
                self._content_pane.update(self._pdf_pager.current())
            elif suffix in IMAGE_EXTENSIONS:
                text = image_to_ansi(path, config.ANSI_MAX_COLS, config.ANSI_MAX_ROWS)
                self._content_pane.update(text)
            else:
                self._content_pane.update(path.read_text(encoding="utf-8", errors="replace"))
        except Exception as exc:
            self._content_pane.update(f"⚠ erreur de lecture : {exc}")

    def markdown_widget(self, path: Path) -> Markdown:
        return Markdown(path.read_text(encoding="utf-8"))

    def pdf_next_page(self) -> None:
        if self._pdf_pager and self._content_pane:
            self._pdf_pager.next()
            self._content_pane.update(self._pdf_pager.current())

    def pdf_previous_page(self) -> None:
        if self._pdf_pager and self._content_pane:
            self._pdf_pager.previous()
            self._content_pane.update(self._pdf_pager.current())

    def refresh_interval(self) -> float | None:
        return None

    async def refresh(self) -> None:
        return None
