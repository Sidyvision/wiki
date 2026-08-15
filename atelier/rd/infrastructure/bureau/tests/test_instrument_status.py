import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
from modules.instrument_status import InstrumentState


def test_load_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "INSTRUMENT_DONNEES", tmp_path / "absent.yaml")
    state = InstrumentState()
    state.load()
    assert state.error == "instrument-donnees.yaml introuvable"


def test_load_parses_version_and_nodes(tmp_path, monkeypatch):
    path = tmp_path / "instrument-donnees.yaml"
    path.write_text(
        "# instrument-donnees.yaml — Déclaration applicative de l'Instrument (v1.4.2)\n"
        "noeuds:\n  - id: a\n  - id: b\n  - id: c\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(config, "INSTRUMENT_DONNEES", path)
    state = InstrumentState()
    state.load()
    assert state.error is None
    assert state.version == "1.4.2"
    assert state.node_count == 3


def test_load_handles_malformed_yaml(tmp_path, monkeypatch):
    path = tmp_path / "instrument-donnees.yaml"
    path.write_text("noeuds: [unclosed", encoding="utf-8")
    monkeypatch.setattr(config, "INSTRUMENT_DONNEES", path)
    state = InstrumentState()
    state.load()
    assert state.error is not None
