#!/usr/bin/env python3
"""Contrôle de synchronisation entre l'orchestrateur de fenêtres et les tours réels.

Un désaccord entre la table ORDRE de l'orchestrateur et les expressions cron
`cycle-choura` des profils ne produit AUCUNE erreur visible : l'agent est
simplement endormi à l'heure de son tour, et sa contribution manque au cycle
sans que rien ne le signale. C'est exactement ce qui est arrivé le 2026-08-31.

Ce script rend le silence bruyant. Déterministe, lecture seule, sans LLM.

Usage : python3 verifier-synchronisation.py
Sortie : 0 si tout concorde, 1 sinon.
"""
import importlib.util
import json
import pathlib
import sys

ORCHESTRATEUR = pathlib.Path("/root/.hermes/scripts/choura-window-orchestrator.py")
PROFILS = pathlib.Path("/root/.hermes/profiles")
RSS_GATEWAY_MO = 136  # mesuré le 2026-08-31
RAM_HOTE_MO = 3819


def charger_orchestrateur():
    if not ORCHESTRATEUR.exists():
        print(f"⛔ orchestrateur introuvable : {ORCHESTRATEUR}", file=sys.stderr)
        sys.exit(1)
    spec = importlib.util.spec_from_file_location("orch", ORCHESTRATEUR)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def heure_du_tour(profil):
    chemin = PROFILS / profil / "cron" / "jobs.json"
    if not chemin.exists():
        return None
    jobs = [j for j in json.loads(chemin.read_text())["jobs"]
            if j.get("name") == "cycle-choura"]
    if len(jobs) != 1:
        return None
    return int(jobs[0]["schedule"]["expr"].split()[1])


def main():
    m = charger_orchestrateur()
    ko = 0
    print(f"{'profil':<14} {'tour (cron)':>11}  {'ORDRE':>6}  fenêtre        état")
    for profil, tour_orch in m.ORDRE:
        tour_cron = heure_du_tour(profil)
        a = (tour_orch - m.FENETRE_AVANT) % 24
        b = (tour_orch + m.FENETRE_APRES) % 24
        couvert = (a <= tour_cron < b) if a < b else (tour_cron >= a or tour_cron < b)
        ok = tour_cron is not None and tour_orch == tour_cron and couvert
        if not ok:
            ko += 1
        etat = "✅" if ok else f"⛔ endormi à son tour ({tour_cron}h)"
        print(f"{profil:<14} {str(tour_cron)+'h':>11}  {str(tour_orch)+'h':>6}  "
              f"[{a:>2}h,{b:>2}h)      {etat}")

    for profil in sorted(m.PERMANENTS):
        t = heure_du_tour(profil)
        print(f"{profil:<14} {str(t)+'h':>11}  {'—':>6}  permanent      ✅")

    def dans_fenetre(tour, h):
        a = (tour - m.FENETRE_AVANT) % 24
        b = (tour + m.FENETRE_APRES) % 24
        return (a <= h < b) if a < b else (h >= a or h < b)

    pic = max(sum(1 for _, tour in m.ORDRE if dans_fenetre(tour, h))
              for h in range(24))
    crete = (len(m.PERMANENTS) + pic) * RSS_GATEWAY_MO
    print()
    print(f"dormants simultanés au pire : {pic}")
    print(f"empreinte crête : {len(m.PERMANENTS)} permanents + {pic} dormant "
          f"= ~{crete} Mo sur {RAM_HOTE_MO} Mo")
    print()
    print(f"{len(m.ORDRE)} dormants, {ko} désynchronisé(s).")
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
