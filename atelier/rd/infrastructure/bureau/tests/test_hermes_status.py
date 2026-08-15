import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules.hermes_status import PROFILES, HermesFleetState


def test_all_profiles_have_mission_files():
    import config

    for _profile, filename in PROFILES:
        path = config.HERMES_PROMPTS_DIR / filename
        assert path.exists(), f"fiche manquante : {filename}"


def test_read_mission_extracts_role_and_mission():
    state = HermesFleetState()
    role, mission, error = state._read_mission("09-studio-sound-engineer.md")
    assert error is None
    assert "Sound Engineer" in role
    assert "reamping" in mission or "recording" in mission


def test_read_mission_missing_file():
    state = HermesFleetState()
    role, mission, error = state._read_mission("00-does-not-exist.md")
    assert role is None
    assert mission is None
    assert error == "fiche introuvable"


def test_twelve_profiles_declared():
    assert len(PROFILES) == 12
