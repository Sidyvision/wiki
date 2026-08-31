#!/usr/bin/env python3
"""Orchestrateur de fenêtres du Cycle de Consultation (Choura).

Lance chaque gateway de profil une heure avant son tour Choura, l'arrête une
heure après : trois agents tiennent la veille en permanence, les neuf autres se
réveillent pour leur contribution puis s'éteignent. Appelé en cron * * * * *.

Motif : 14 gateways à ~136 Mo plus OmniRoute daemonisé (~1,6 Go) ne tiennent pas
dans les 3,7 Go de l'hôte — cf. incident du 2026-08-28 (saturation RAM), dont la
« compréhension tirée » demandait précisément une logique de gateway à la demande.

Fenêtre = [T-1h, T+1h). Les tours étant espacés de 2h, au plus UN dormant est
éveillé à la fois : 3 permanents + 1 dormant ≈ 544 Mo.

HEURES EN EUROPE/PARIS (révision du 2026-08-31). Elles étaient auparavant figées
en UTC, ce qui (a) devenait faux dès que la rotation Choura était reprogrammée en
heure locale, et (b) aurait décalé toutes les fenêtres d'une heure au changement
d'heure du 25 octobre. Le fuseau est désormais résolu, pas supposé — même règle
que les jobs cron des profils, qui sont évalués en Europe/Paris.
"""
import os
import subprocess
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")

ORDRE = [
    # (profil, heure du tour EN HEURE DE PARIS)
    # Seuls les 9 profils dormants sont orchestrés ici ; gardien, publication et
    # studio tiennent la veille en permanence (voir PERMANENTS).
    # Doit rester synchrone avec les expressions cron `cycle-choura` des profils,
    # posées par meta/projet-unifie/choura/_reprogrammer-choura.py.
    ("ar-music",    14),
    ("visual-da",   16),
    ("production",  18),
    ("admin-legal", 20),
    ("accounting",  22),
    ("distribution", 0),
    ("marketing",    2),
    ("fanzine",      8),
    ("commerce",    10),
]

# Profils en gateway permanente (non orchestrés)
PERMANENTS = {"gardien", "publication", "studio"}

FENETRE_AVANT = 1  # heures avant le tour
FENETRE_APRES = 1  # heures après le tour

UNIT = "hermes-gateway-{profile}.service"
LOG_PREFIX = "[choura-orchestrator]"


def is_active(profile: str) -> bool:
    r = subprocess.run(
        ["systemctl", "--user", "is-active", UNIT.format(profile=profile)],
        capture_output=True, text=True, timeout=10,
    )
    return r.stdout.strip() == "active"


def do_start(profile: str) -> None:
    r = subprocess.run(
        ["systemctl", "--user", "start", UNIT.format(profile=profile)],
        capture_output=True, text=True, timeout=30,
    )
    if r.returncode == 0:
        print(f"{LOG_PREFIX} START {profile}")
    else:
        print(f"{LOG_PREFIX} START FAILED {profile}: {r.stderr.strip()}", file=sys.stderr)


def do_stop(profile: str) -> None:
    r = subprocess.run(
        ["systemctl", "--user", "stop", UNIT.format(profile=profile)],
        capture_output=True, text=True, timeout=30,
    )
    if r.returncode == 0:
        print(f"{LOG_PREFIX} STOP  {profile}")
    else:
        print(f"{LOG_PREFIX} STOP  FAILED {profile}: {r.stderr.strip()}", file=sys.stderr)


def run():
    now = datetime.now(PARIS)
    heure_locale = now.hour

    # Pour chaque profil orchestré, calculer si la fenêtre inclut l'heure courante
    # Fenêtre : [tour - FENETRE_AVANT, tour + FENETRE_APRES)
    for profile, tour in ORDRE:
        if profile in PERMANENTS:
            continue  # sécurité : ne jamais toucher aux permanents

        start_h = (tour - FENETRE_AVANT) % 24
        stop_h = (tour + FENETRE_APRES) % 24

        if start_h < stop_h:
            # Fenêtre ne franchit pas minuit
            should_run = start_h <= heure_locale < stop_h
        else:
            # Fenêtre franchit minuit
            should_run = heure_locale >= start_h or heure_locale < stop_h

        active = is_active(profile)
        if should_run and not active:
            do_start(profile)
        elif not should_run and active:
            do_stop(profile)
        # sinon pas de changement


if __name__ == "__main__":
    # Environnement systemd --user
    os.environ.setdefault("XDG_RUNTIME_DIR", "/run/user/0")
    os.environ.setdefault("DBUS_SESSION_BUS_ADDRESS", "unix:path=/run/user/0/bus")
    try:
        run()
    except Exception as e:
        print(f"{LOG_PREFIX} ERREUR: {e}", file=sys.stderr)
        sys.exit(1)
