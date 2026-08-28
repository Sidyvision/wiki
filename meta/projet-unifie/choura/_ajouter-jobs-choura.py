#!/usr/bin/env python3
"""Script d'exécution unique — ajout du job cron Choura aux 12 profils Hermes.
Conservé pour traçabilité (Cmd 9) ; non destiné à être relancé (idempotence
non garantie — vérifier l'absence du job 'cycle-choura' avant relance).
Exécuté le 2026-08-27 sous plan validé (verdict Sidy, câblage cron réel Choura).
"""
import json
import secrets
from datetime import datetime, timedelta, timezone

PROFILES = {
    # profil: (position, signe, heure_UTC, est_gardien)
    "gardien":     (10, "Capricorne", 0, True),
    "ar-music":    (1,  "Bélier",     2, False),
    "visual-da":   (2,  "Balance",    4, False),
    "production":  (3,  "Gémeaux",    6, False),
    "admin-legal": (4,  "Cancer",     8, False),
    "accounting":  (5,  "Taureau",    10, False),
    "distribution":(6,  "Scorpion",   12, False),
    "marketing":   (7,  "Lion",       14, False),
    "publication": (8,  "Sagittaire", 16, False),
    "studio":      (9,  "Vierge",     18, False),
    "fanzine":     (11, "Verseau",    20, False),
    "commerce":    (12, "Poissons",   22, False),
}

def prompt_for(profile, position, signe, est_gardien):
    base = f"""Tu es l'agent Hermes `{profile}` (rôle {position} des douze, signe {signe} — cf. la table zodiacale validée le 2026-08-15, `meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md` §9). Ce tour s'inscrit dans le **Cycle de Consultation (Choura)** — dispositif validé par Sidy le 2026-08-27, voir `meta/projet-unifie/proposition-cycle-consultation-choura-2026-08-27.md`.

## Ce que tu fais

1. Depuis /root/wiki, identifie le fichier de cycle du jour : `meta/projet-unifie/choura/cycle-<AAAA-MM-JJ>.md` (date du jour). S'il n'existe pas encore, ce n'est normalement pas ton rôle de le créer (ouverture réservée au tour du Gardien à 00:00) — si tu le trouves absent hors de ce cas, signale-le simplement dans ta réponse et arrête-toi, n'improvise pas un fichier.
2. Lis la dernière entrée du fichier (ou celle du fichier de la veille si le tien vient d'ouvrir).
3. Rédige ta propre entrée en t'appuyant explicitement dessus, sur trois axes : tes tâches en cours (côté rôle {profile}), l'état du dépôt tel que tu le perçois depuis ta fonction, une perspective ou un objectif que tu proposes de regarder.
4. Rappelle ton rôle et ton signe zodiacal en tête de ton entrée (cohérence avec la section « Zodiac principle » de ton prompt de production, `meta/projet-unifie/hermes-prompts/`).

## Règle d'affinité (verdict Sidy, 2026-08-27)

Si une matière abordée dans le cycle déborde la définition stricte de ton rôle, tu te prononces quand même — par l'**affinité la plus proche** (signe zodiacal voisin dans la table, ou rôle adjacent dans la rotation). Ne jamais t'abstenir au seul motif du hors-périmètre : l'attribution par affinité prime le rejet par défaut.

## Clause anti-remplissage

« Rien de neuf à signaler » est une contribution légitime — ne force pas un contenu artificiel pour occuper le tour.

## Ce que tu ne fais jamais

Aucun verdict métaphysique, aucune décision engageante (dépense, contrat, publication, tracklist, arbitrage de discernement) — cela reste réservé à Sidy (Cmd 12/13). Ce tour est un signalement de perspective, rien de plus.

## Écriture

Ajoute ton entrée en fin du fichier de cycle du jour (respecte le marqueur `<!-- INSERTION: QUEUE -->`, jamais d'édition d'une entrée existante). Commit local avec un message clair (`git add meta/projet-unifie/choura/ && git commit -m "CHOURA: tour {profile}"`). **Ne push jamais** — la synchronisation reste un geste humain."""

    if est_gardien:
        base += """

## Tour spécifique au Gardien (ouverture/clôture du cycle, 00:00)

En plus de ton propre tour ci-dessus : (a) clôture le fichier de cycle de la veille par une brève synthèse en fin de fichier (pas un verdict — un résumé factuel des tours passés) ; (b) si le fichier de cycle du jour n'existe pas encore, crée-le sur le modèle du fichier de la veille (même Sceau, même gabarit d'entrée en tête, marqueur `<!-- INSERTION: QUEUE -->`, `created`/`updated` à la date du jour)."""

    return base

def make_job(profile, position, signe, heure, est_gardien):
    now = datetime.now(timezone.utc)
    next_run = now.replace(hour=heure, minute=0, second=0, microsecond=0)
    if next_run <= now:
        next_run += timedelta(days=1)
    return {
        "id": secrets.token_hex(6),
        "name": "cycle-choura",
        "prompt": prompt_for(profile, position, signe, est_gardien),
        "skills": [],
        "skill": None,
        "model": "auto/best-free",
        "provider": "custom:omniroute",
        "provider_snapshot": None,
        "model_snapshot": None,
        "base_url": None,
        "script": None,
        "no_agent": False,
        "monitor_script": None,
        "monitor_url": None,
        "monitor_state": None,
        "context_from": None,
        "schedule": {
            "kind": "cron",
            "expr": f"0 {heure} * * *",
            "display": f"0 {heure} * * *",
        },
        "schedule_display": f"0 {heure} * * *",
        "repeat": {"times": None},
        "enabled": True,
        "state": "scheduled",
        "paused_at": None,
        "paused_reason": None,
        "created_at": now.isoformat(),
        "next_run_at": next_run.isoformat(),
        "last_run_at": None,
        "last_status": None,
        "last_error": None,
        "last_delivery_error": None,
        "failure_streak": 0,
        "deliver": None,
        "origin": None,
        "enabled_toolsets": None,
        "workdir": "/root/wiki",
        "fire_claim": None,
    }

def main():
    for profile, (position, signe, heure, est_gardien) in PROFILES.items():
        path = f"/root/.hermes/profiles/{profile}/cron/jobs.json"
        try:
            with open(path) as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"jobs": [], "updated_at": None}
        if any(j.get("name") == "cycle-choura" for j in data["jobs"]):
            print(f"{profile}: SKIP (déjà présent)")
            continue
        job = make_job(profile, position, signe, heure, est_gardien)
        data["jobs"].append(job)
        data["updated_at"] = datetime.now(timezone.utc).isoformat()
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"{profile}: OK ({job['id']}, {job['schedule']['expr']})")

if __name__ == "__main__":
    main()
