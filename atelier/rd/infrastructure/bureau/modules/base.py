"""Interface commune à tous les modules du bureau.

Ajouter un module futur = un fichier de plus ici, déclaré dans le registre
`MODULES` de `app.py`. Chaque module fournit un résumé court (tuile du menu)
et une vue agrandie (mode monocle).
"""

from __future__ import annotations

from textual.widget import Widget


class Module:
    """Contrat minimal qu'un module du bureau doit remplir."""

    key: str = "module"
    title: str = "Module"
    icon: str = "◆"

    def summary_widget(self) -> Widget:
        """Widget compact affiché sur la tuile du menu principal."""
        raise NotImplementedError

    def full_widget(self) -> Widget:
        """Widget affiché en plein panneau (mode monocle)."""
        raise NotImplementedError

    def refresh_interval(self) -> float | None:
        """Intervalle (secondes) de rafraîchissement automatique, ou None."""
        return None

    async def refresh(self) -> None:
        """Rafraîchit l'état interne du module (lecture seule, jamais d'écriture)."""
        return None
