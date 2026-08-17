#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier-coherence-infrastructure.py — Confronte les actions de configuration
H‍ermes/Discord affirmées par les fiches atelier/rd/infrastructure/ (bloc
frontmatter `infra_verif`) à l'état réel du serveur (`hermes cron list`,
fichiers `.env` des profils).

Motif (registre-problemes.md, [2026-08-17] ouvert) : une fiche a affirmé la
création d'un job cron avec un tableau de paramètres complet et une citation
de log — le job n'a jamais existé. Aucune vérification mécanique indépendante
n'a précédé la clôture de cette passe, malgré la consigne écrite dans la même
fiche. Ce script remplace la consigne rédactionnelle (déjà tentée, déjà
retombée) par un contrôle déterministe, même famille que
verifier-invariants.py et detecter-non-tracke.py : DÉTERMINISTE, sans LLM,
sans réseau. Il ne corrige rien — il constate, avec la fiche source citée pour
chaque écart.

Usage :
    python3 verifier-coherence-infrastructure.py [--racine /root/wiki] [--json]

Codes de sortie :
    0  toutes les affirmations infra_verif concordent avec l'état réel
    1  au moins un écart constaté
    2  erreur d'exécution du script lui-même (hermes introuvable, etc.)
"""

import argparse
import glob
import json
import os
import subprocess
import sys

import yaml


def lire_frontmatter(chemin):
    """Retourne le dict frontmatter d'une fiche, ou None si absent/invalide."""
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    lignes = texte.split("\n")
    if not lignes or lignes[0].strip() != "---":
        return None
    fin = None
    for i in range(1, len(lignes)):
        if lignes[i].strip() == "---":
            fin = i
            break
    if fin is None:
        return None
    bloc = "\n".join(lignes[1:fin])
    try:
        fm = yaml.safe_load(bloc)
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def collecter_affirmations(racine):
    """Parcourt atelier/rd/infrastructure/*.md, retourne une liste
    d'affirmations (dict) avec la fiche source attachée."""
    motif = os.path.join(racine, "atelier", "rd", "infrastructure", "*.md")
    affirmations = []
    for chemin in sorted(glob.glob(motif)):
        fm = lire_frontmatter(chemin)
        if not fm or not fm.get("infra_verif"):
            continue
        rel = os.path.relpath(chemin, racine)
        for item in fm["infra_verif"]:
            if isinstance(item, dict):
                affirmations.append({**item, "_fiche": rel})
    return affirmations


def cron_jobs_actifs(profil):
    """Retourne la liste des noms de jobs cron (--all, y compris désactivés)
    du profil H‍ermes donné. Lève RuntimeError si la commande échoue."""
    try:
        out = subprocess.run(
            ["hermes", "--profile", profil, "cron", "list", "--all"],
            capture_output=True, text=True, timeout=30,
        )
    except FileNotFoundError:
        raise RuntimeError("commande 'hermes' introuvable dans l'environnement")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"'hermes --profile {profil} cron list' a expiré (30s)")
    sortie = out.stdout + out.stderr
    if "No scheduled jobs" in sortie:
        return []
    # Format de sortie non garanti stable entre versions H‍ermes : on prend
    # toute ligne non vide comme candidat contenant potentiellement un nom de
    # job, et on cherche une inclusion de sous-chaîne à l'appel — volontairement
    # permissif plutôt que de sur-parser une sortie non documentée.
    return [l.strip() for l in sortie.splitlines() if l.strip()]


def lire_env(profil, racine_hermes="/root/.hermes/profiles"):
    """Retourne un dict des clés DISCORD_* du .env d'un profil, ou {} si le
    fichier n'existe pas."""
    chemin = os.path.join(racine_hermes, profil, ".env")
    valeurs = {}
    if not os.path.isfile(chemin):
        return valeurs
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or "=" not in ligne:
                continue
            cle, _, val = ligne.partition("=")
            valeurs[cle.strip()] = val.strip()
    return valeurs


def normaliser_liste(valeur):
    """Accepte une liste YAML ou une chaîne 'a,b,c' et retourne un set de
    chaînes nettoyées, pour comparaison insensible à l'ordre/aux espaces."""
    if valeur is None:
        return set()
    if isinstance(valeur, str):
        items = valeur.split(",")
    else:
        items = valeur
    return {str(i).strip() for i in items if str(i).strip()}


def verifier_affirmation(item, cache_cron, cache_env):
    """Retourne une liste de (statut, message) — statut 'OK' ou 'ECART'."""
    profil = item.get("profil")
    if not profil:
        return [("ECART", "bloc infra_verif sans champ 'profil'")]

    resultats = []

    if "cron_job" in item:
        if profil not in cache_cron:
            try:
                cache_cron[profil] = cron_jobs_actifs(profil)
            except RuntimeError as e:
                return [("ECART", f"impossible de vérifier le cron du profil {profil} : {e}")]
        jobs = cache_cron[profil]
        attendu = item["cron_job"]
        present = any(attendu in j for j in jobs)
        if present:
            resultats.append(("OK", f"cron '{attendu}' présent (profil {profil})"))
        else:
            resultats.append(("ECART", f"cron '{attendu}' ABSENT (profil {profil}) — "
                                        f"`hermes --profile {profil} cron list --all` ne le montre pas"))

    if profil not in cache_env:
        cache_env[profil] = lire_env(profil)
    env = cache_env[profil]

    if "discord_home_channel" in item:
        attendu = str(item["discord_home_channel"])
        reel = env.get("DISCORD_HOME_CHANNEL", "")
        if reel == attendu:
            resultats.append(("OK", f"DISCORD_HOME_CHANNEL = {attendu} (profil {profil})"))
        else:
            resultats.append(("ECART", f"DISCORD_HOME_CHANNEL attendu {attendu}, "
                                        f"réel '{reel}' (profil {profil})"))

    if "discord_allowed_channels" in item:
        attendu = normaliser_liste(item["discord_allowed_channels"])
        reel = normaliser_liste(env.get("DISCORD_ALLOWED_CHANNELS", ""))
        if attendu <= reel:
            resultats.append(("OK", f"DISCORD_ALLOWED_CHANNELS couvre les {len(attendu)} "
                                     f"salon(s) attendu(s) (profil {profil})"))
        else:
            manquants = attendu - reel
            resultats.append(("ECART", f"DISCORD_ALLOWED_CHANNELS ne contient pas "
                                        f"{sorted(manquants)} (profil {profil})"))

    if not resultats:
        resultats.append(("ECART", f"bloc infra_verif du profil {profil} ne contient aucun "
                                    f"champ reconnu (cron_job / discord_home_channel / "
                                    f"discord_allowed_channels)"))
    return resultats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    affirmations = collecter_affirmations(args.racine)

    cache_cron, cache_env = {}, {}
    lignes = []
    ecarts = 0
    for item in affirmations:
        for statut, message in verifier_affirmation(item, cache_cron, cache_env):
            if statut == "ECART":
                ecarts += 1
            lignes.append({"statut": statut, "message": message, "fiche": item["_fiche"]})

    if args.json:
        print(json.dumps(lignes, ensure_ascii=False, indent=2))
        return 1 if ecarts else 0

    if not affirmations:
        print("  Aucune affirmation infra_verif trouvée dans atelier/rd/infrastructure/.")
        return 0

    print(f"  {len(lignes)} affirmation(s) vérifiée(s), {ecarts} écart(s) :\n")
    for l in lignes:
        marque = "✅" if l["statut"] == "OK" else "❌"
        print(f"  {marque} [{l['fiche']}] {l['message']}")

    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main())
