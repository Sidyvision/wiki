#!/usr/bin/env python3
"""Hook Choura — inscrit un message de Sidy dans le cycle comme sa contribution.

Branché sur `pre_llm_call`. Quand Sidy écrit dans le salon Choura (#général),
son message est déposé dans le fichier de cycle courant sous une entrée signée
`sidy`, **sans qu'il ait à mentionner un agent par @**. Les tours suivants s'y
appuient en priorité (clause inscrite dans le prompt des douze).

Pourquoi un hook et non une consigne d'agent : le moteur ne demande aucun
@mention pour traiter un message — le filtrage se fait par salon autorisé. Ce
qui manquait n'était donc pas un réglage de mention, mais le geste qui inscrit
le message dans le journal du cycle.

Enregistré sur le SEUL profil `gardien` (config.yaml, bloc hooks). Le Gardien
tient la veille en permanence et c'est lui qui ouvre et clôt le cycle : le
brancher ailleurs produirait une entrée par profil éveillé.

Wire protocol : JSON sur stdin, JSON optionnel sur stdout (voir
agent/shell_hooks.py). Ce hook n'émet qu'un `context` informatif et ne bloque
jamais rien — une défaillance ici ne doit pas empêcher un agent de répondre.
"""
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")
HEURE_OUVERTURE = 12
CHOURA = pathlib.Path("/root/wiki/meta/projet-unifie/choura")
SALON_CHOURA = "1534857297321394248"  # #général
ETAT = pathlib.Path("/root/.hermes/scripts/.choura-contributions-vues.json")
MARQUEUR_FIN = "## Gabarit d'entrée"


def fichier_de_cycle(maintenant):
    """Le cycle est identifié par sa DATE D'OUVERTURE (12:00 Paris)."""
    jour = maintenant.date()
    if maintenant.hour < HEURE_OUVERTURE:
        jour -= timedelta(days=1)
    return CHOURA / f"cycle-{jour.isoformat()}.md"


def contient(payload, aiguille):
    """Cherche récursivement une valeur dans le payload (le champ salon n'est
    pas garanti stable entre versions du moteur — on ne suppose pas sa place)."""
    if isinstance(payload, dict):
        return any(contient(v, aiguille) for v in payload.values())
    if isinstance(payload, list):
        return any(contient(v, aiguille) for v in payload)
    return aiguille in str(payload)


def deja_vu(empreinte):
    try:
        vues = set(json.loads(ETAT.read_text()))
    except Exception:
        vues = set()
    if empreinte in vues:
        return True
    vues.add(empreinte)
    # borne : on ne garde que les 500 dernières empreintes
    ETAT.write_text(json.dumps(sorted(vues)[-500:]), encoding="utf-8")
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    if payload.get("hook_event_name") != "pre_llm_call":
        return

    extra = payload.get("extra") or {}
    message = (extra.get("user_message") or payload.get("user_message") or "").strip()
    plateforme = (extra.get("platform") or payload.get("platform") or "").lower()

    if not message or plateforme != "discord":
        return
    # Le salon : si l'identifiant apparaît quelque part dans le payload on exige
    # qu'il s'agisse bien du salon Choura ; s'il n'y figure nulle part, on
    # accepte (le profil gardien n'est autorisé que sur trois salons).
    if contient(payload, "15348") and not contient(payload, SALON_CHOURA):
        return

    maintenant = datetime.now(PARIS)
    cycle = fichier_de_cycle(maintenant)
    if not cycle.exists():
        return  # cycle non ouvert — ne jamais improviser un fichier

    empreinte = hashlib.sha256(
        f"{payload.get('session_id','')}|{message}".encode()).hexdigest()[:16]
    if deja_vu(empreinte):
        return

    corps = "\n".join("> " + l if l.strip() else ">" for l in message.splitlines())
    entree = (
        f"\n## [{maintenant.strftime('%Y-%m-%d %H:%M')}] sidy "
        f"(contribution humaine, salon Choura)\n\n"
        f"{corps}\n\n"
        f"**Nature** : parole de Sidy, déposée telle quelle depuis Discord. "
        f"Elle prime dans le cycle (Cmd 12/13) et n'est ni résumée ni interprétée "
        f"ici. Les tours suivants s'appuient dessus.\n\n"
        f"**S'appuyant sur** : —\n\n"
    )

    texte = cycle.read_text(encoding="utf-8")
    if MARQUEUR_FIN in texte:
        i = texte.index(MARQUEUR_FIN)
        texte = texte[:i] + entree.lstrip("\n") + "\n" + texte[i:]
    else:
        texte += entree
    texte = re.sub(r"^updated: .*$", f"updated: {maintenant.date().isoformat()}",
                   texte, count=1, flags=re.M)
    cycle.write_text(texte, encoding="utf-8")

    print(json.dumps({"context":
        f"[Choura] Le message de Sidy vient d'être inscrit dans {cycle.name} "
        f"comme sa contribution au cycle. Tu n'as pas à l'y recopier."}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # un hook ne doit jamais empêcher un agent de répondre
