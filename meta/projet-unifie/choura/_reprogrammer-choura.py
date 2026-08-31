#!/usr/bin/env python3
"""Reprogrammation du cycle Choura — ouverture à 12:00 heure de Paris.

Exécuté le 2026-08-31 sur verdict de Sidy (« programme un nouveau cycle à partir
de midi, heure de Paris »). Succède à `_ajouter-jobs-choura.py` (2026-08-27), qui
avait câblé les douze jobs à des heures UTC.

TROIS DÉFAUTS CORRIGÉS — c'est ce qui bloquait le cycle :

1. Le tour du Gardien portait en dur « ouverture/clôture du cycle, 00:00 » alors
   que son job avait été déplacé à 18:00 UTC. Il ouvrait donc le fichier du jour
   où il tournait, et tout agent dont le créneau tombait après minuit ne trouvait
   aucun fichier — son prompt lui ordonnant alors de signaler et s'arrêter.
   Constat : `cycle-2026-08-29.md` et `cycle-2026-08-31.md` n'ont jamais existé,
   et les tours du 31 se sont déposés dans le fichier du 30.

2. Aucun fuseau n'était déclaré. Les expressions cron sont évaluées contre
   `hermes_time.now()`, qui honore la clé `timezone:` de la config — mais un
   profil ne charge QUE sa propre config.yaml (le global n'est pas fusionné,
   vérifié le 2026-08-31). Sans la clé dans CHAQUE profil, les heures seraient
   restées en UTC, soit 2h d'écart avec l'intention.

3. Le cycle ouvrant désormais à midi, il enjambe deux jours calendaires. « Le
   fichier du jour » redevient ambigu à minuit. Le prompt définit donc le cycle
   par sa DATE D'OUVERTURE, avec une règle mécanique : avant midi, le cycle
   courant est celui ouvert la veille.

Usage : python3 _reprogrammer-choura.py [--dry-run]
"""
import argparse
import json
import pathlib
import shutil
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")
HEURE_OUVERTURE = 12

# profil: (position, signe, heure locale Paris)
PROFILES = {
    "gardien":      (10, "Capricorne", 12),
    "ar-music":     (1,  "Bélier",     14),
    "visual-da":    (2,  "Balance",    16),
    "production":   (3,  "Gémeaux",    18),
    "admin-legal":  (4,  "Cancer",     20),
    "accounting":   (5,  "Taureau",    22),
    "distribution": (6,  "Scorpion",   0),
    "marketing":    (7,  "Lion",       2),
    "publication":  (8,  "Sagittaire", 4),
    "studio":       (9,  "Vierge",     6),
    "fanzine":      (11, "Verseau",    8),
    "commerce":     (12, "Poissons",   10),
}

REGLE_CYCLE = f"""1. Depuis /root/wiki, identifie le fichier du cycle courant.

   **Le cycle s'ouvre à {HEURE_OUVERTURE}:00, heure de Paris**, et court sur 24h — il
   enjambe donc deux jours calendaires. Un cycle est identifié par sa **date
   d'ouverture**, jamais par la date du moment où tu tournes. Règle mécanique,
   à appliquer telle quelle :

   - il est {HEURE_OUVERTURE}:00 ou plus tard (heure de Paris) → date du cycle = **aujourd'hui**
   - il est avant {HEURE_OUVERTURE}:00 → date du cycle = **hier**

   Le fichier est `meta/projet-unifie/choura/cycle-<date du cycle>.md`.
   Vérifie l'heure de Paris avant de conclure (`TZ=Europe/Paris date`), ne
   suppose pas que l'horloge du serveur soit à l'heure locale.

   S'il n'existe pas, ce n'est pas ton rôle de le créer (ouverture réservée au
   tour du Gardien à {HEURE_OUVERTURE}:00) — signale-le simplement dans ta réponse et
   arrête-toi, n'improvise pas un fichier."""


def prompt_for(profile, position, signe, est_gardien):
    base = f"""Tu es l'agent Hermes `{profile}` (rôle {position} des douze, signe {signe} — cf. la table zodiacale validée le 2026-08-15, `meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md` §9). Ce tour s'inscrit dans le **Cycle de Consultation (Choura)** — dispositif validé par Sidy le 2026-08-27, voir `meta/projet-unifie/proposition-cycle-consultation-choura-2026-08-27.md`.

## Ce que tu fais

{REGLE_CYCLE}
2. Lis la dernière entrée du fichier (ou celle du cycle précédent si le tien vient d'ouvrir).
3. Rédige ta propre entrée en t'appuyant explicitement dessus, sur trois axes : tes tâches en cours (côté rôle {profile}), l'état du dépôt tel que tu le perçois depuis ta fonction, une perspective ou un objectif que tu proposes de regarder.
4. Rappelle ton rôle et ton signe zodiacal en tête de ton entrée (cohérence avec la section « Zodiac principle » de ton prompt de production, `meta/projet-unifie/hermes-prompts/`).
5. **Contribution de Sidy** : si le fichier de cycle porte, depuis le tour précédent, une entrée signée `sidy`, tu t'appuies dessus en priorité — c'est la voix qui prime dans le cycle (Cmd 12/13). Tu n'y réponds pas par un verdict : tu en tiens compte dans ta perspective.

## Règle d'affinité (verdict Sidy, 2026-08-27)

Si une matière abordée dans le cycle déborde la définition stricte de ton rôle, tu te prononces quand même — par l'**affinité la plus proche** (signe zodiacal voisin dans la table, ou rôle adjacent dans la rotation). Ne jamais t'abstenir au seul motif du hors-périmètre : l'attribution par affinité prime le rejet par défaut.

## Clause anti-remplissage

« Rien de neuf à signaler » est une contribution légitime — ne force pas un contenu artificiel pour occuper le tour.

## Ce que tu ne fais jamais

Aucun verdict métaphysique, aucune décision engageante (dépense, contrat, publication, tracklist, arbitrage de discernement) — cela reste réservé à Sidy (Cmd 12/13). Ce tour est un signalement de perspective, rien de plus.

## Écriture

Ajoute ton entrée en fin du fichier de cycle courant (respecte le marqueur `<!-- INSERTION: QUEUE -->`, jamais d'édition d'une entrée existante). Horodate ton entrée en **heure de Paris**. Commit local avec un message clair (`git add meta/projet-unifie/choura/ && git commit -m "CHOURA: tour {profile}"`). **Ne push jamais** — la synchronisation reste un geste humain."""

    if est_gardien:
        base += f"""

## Tour spécifique au Gardien (ouverture/clôture du cycle, {HEURE_OUVERTURE}:00 heure de Paris)

En plus de ton propre tour ci-dessus :

(a) **Clôture le cycle précédent** (le fichier ouvert la veille à {HEURE_OUVERTURE}:00) par une brève synthèse en fin de fichier — un résumé factuel des tours passés, jamais un verdict.

(b) **Ouvre le cycle du jour** : crée `cycle-<date du jour>.md` sur le modèle du fichier précédent (même frontmatter, même en-tête de Sceau, gabarit d'entrée, marqueur `<!-- INSERTION: QUEUE -->`, `created`/`updated` à la date du jour). C'est le **fichier d'amorce** : sans lui, les onze tours suivants trouvent porte close et s'arrêtent. Cette création est la partie non négociable de ton tour — si tu ne fais rien d'autre, fais cela."""

    return base


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    maintenant = datetime.now(PARIS)
    erreurs = 0

    for profile, (position, signe, heure) in PROFILES.items():
        base_dir = pathlib.Path(f"/root/.hermes/profiles/{profile}")
        cfg = base_dir / "config.yaml"
        jobs_path = base_dir / "cron" / "jobs.json"

        # ── 1. Fuseau dans la config DU PROFIL (le global n'est pas fusionné)
        txt = cfg.read_text(encoding="utf-8")
        if "timezone:" not in txt:
            if not args.dry_run:
                shutil.copy2(cfg, cfg.with_suffix(f".yaml.bak-choura-{ts}"))
                cfg.write_text(
                    "# Fuseau de référence : les expressions cron sont évaluées contre\n"
                    "# hermes_time.now(), qui honore cette clé. Sans elle le profil\n"
                    "# tourne en UTC — 2h d'écart avec l'intention (posé le 2026-08-31).\n"
                    "timezone: Europe/Paris\n" + txt, encoding="utf-8")
            tz_note = "fuseau posé"
        else:
            tz_note = "fuseau déjà là"

        # ── 2. Job cycle-choura : horaire + prompt
        data = json.loads(jobs_path.read_text(encoding="utf-8"))
        jobs = [j for j in data.get("jobs", []) if j.get("name") == "cycle-choura"]
        if len(jobs) != 1:
            print(f"  ⛔ {profile:<13} {len(jobs)} job(s) cycle-choura — NON MODIFIÉ")
            erreurs += 1
            continue
        job = jobs[0]

        expr = f"0 {heure} * * *"
        prochain = maintenant.replace(hour=heure, minute=0, second=0, microsecond=0)
        if prochain <= maintenant:
            prochain += timedelta(days=1)

        job["schedule"] = {"kind": "cron", "expr": expr, "display": expr}
        job["schedule_display"] = expr
        job["prompt"] = prompt_for(profile, position, signe, profile == "gardien")
        job["next_run_at"] = prochain.isoformat()
        job["model"] = "auto/best-free"
        job["provider"] = "custom:omniroute"
        job["enabled"] = True
        job["state"] = "scheduled"
        job["failure_streak"] = 0
        job["last_error"] = None
        job["workdir"] = "/root/wiki"

        if not args.dry_run:
            shutil.copy2(jobs_path, jobs_path.with_suffix(f".json.bak-choura-{ts}"))
            data["updated_at"] = datetime.now().isoformat()
            jobs_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                                 encoding="utf-8")
        print(f"  {'○' if args.dry_run else '✅'} {profile:<13} rôle {position:>2} {signe:<11} "
              f"{expr:<12} → {prochain.strftime('%m-%d %H:%M %Z')}  ({tz_note})")

    print()
    print(f"{'(dry-run) ' if args.dry_run else ''}12 profils, {erreurs} erreur(s).")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
