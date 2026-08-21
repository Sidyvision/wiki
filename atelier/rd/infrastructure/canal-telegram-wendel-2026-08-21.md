---
title: "Infrastructure — Canal Telegram pour Wendel Nazaire, second robinet vers _inbox/"
type: infrastructure
tags: [rd, infrastructure, karubi, transmissions, telegram, hermes]
created: 2026-08-21
updated: 2026-08-21
sources: []
links: [atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16.md, atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12.md, meta/transmissions/karubi-wendel.md, meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md]
statut_experience: exploratoire
---

# Canal Telegram pour Wendel Nazaire, réplique du dispositif Mehdi

> Décision Sidy du 2026-08-21 : après génération du Karūbī « Hassan »
> (`meta/transmissions/karubi-wendel.md`, sceau `f5d808eb…`), configurer pour
> Wendel un canal Telegram identique à celui de Mehdi — un second robinet vers
> `_inbox/`, jamais un nouveau périmètre. La présente fiche réplique
> `canal-telegram-mehdi-2026-08-16.md` ; seuls les écarts sont documentés ici.

## 1. Ce qui est identique au dispositif Mehdi

- Architecture : profil Hermes dédié, service systemd **système** sous le
  compte Unix du destinataire (pas sous root) — la frontière réelle est le
  compte OS + les montages `ro`, pas le prompt.
- Confluence : tout ce que Wendel dépose aboutit dans `_inbox/` du dépôt
  canonique via `depot-ecriture/inbox/` (bind mount rw + ACL).
- `.env` jamais commité, `chmod 600`, allowlist fail-closed.
- Vérification obligatoire `grep "Connected as"` dans le log gateway avant de
  dire le canal « en service » (règle fiche 15 §4).

## 2. Écarts par rapport au dispositif Mehdi

- **Périmètre de lecture** (verdict Sidy 2026-08-21, option A — minimal) :
  - `meta/transmissions/karubi-wendel.md` (son propre fichier)
  - `doctrinal/` (circuit complet)
  - `hermeneutique/` (circuit complet)
  - `label/direction-artistique/` (le pôle où se dessine sa place, annoncé en
    §4 de son Karūbī)
  - **Exclus** : le reste de `label/` (doctrine-du-don, cercles-token, etc.),
    tout `atelier/` y compris R&D. Révisable par verdict si la collaboration
    s'étend.
- **Persona** : Hassan (Hassan-Derwish), pas Habib. Le Telegram est le
  PREMIER point d'entrée de Wendel (pas de session Terminal préalable,
  contrairement à Mehdi) : `SOUL.md` est la persona d'origine, dérivée des
  §3/§3bis scellés de `karubi-wendel.md`. Un `/home/wendel/CLAUDE.md`
  versionné local en est la source (même règle que Mehdi : le prompt vit côté
  compte, `SOUL.md` en est la copie). Si un accès Terminal vient plus tard,
  il héritera du même fichier.
- **Bot** : un bot distinct est requis (ex. `@HassanKarubi_bot`) — le bot
  `@HabibKarubi_bot` appartient au canal de Mehdi ; le profil `karubi`
  (anciennement porteur du token) a été nettoyé le 2026-08-16.

## 3. Étapes exécutées par le gardien (2026-08-21)

1. Compte Unix `wendel` créé (`useradd -m -s /bin/bash`), domaines
   `depot-lecture/` et `depot-ecriture/inbox/` créés.
2. Entrées `bind` ajoutées à `/etc/fstab` (backup préalable
   `/etc/fstab.bak-wendel-<date>`) : quatre montages `ro` (karubi-wendel.md,
   doctrinal, hermeneutique, label/direction-artistique) + un `rw`
   (`_inbox/` → `depot-ecriture/inbox/`), ACL `rwx` pour `wendel` sur
   `_inbox/` (mêmes ACL que pour mehdi, sas partagé accepté tel quel — point
   ouvert §5).
3. Frontière vérifiée : lecture OK, écriture refusée en `ro`, traversée
   `/root/wiki` refusée, sceau de `karubi-wendel.md` contrôlé INTACT après
   toutes les manipulations (`generer-karubi.py verifier`).
4. Profil Hermes `habib-wendel` créé sous `/home/wendel/.hermes/profiles/`,
   `config.yaml` (cwd `/home/wendel/depot-lecture`, toolset telegram seule,
   même provider que les autres profils), `SOUL.md` + `CLAUDE.md` (persona
   Hassan), `.env` initialisé avec la clé modèle uniquement (pas de token
   Telegram encore), `chmod 600`.

## 4. Gestes humains restants (Cmd 13) — état 2026-08-21

- ✅ 1. Sidy a créé le bot via `@BotFather` : **@HassanKarubi_bot**
  (id `8960349824`), vérifié via l'API Telegram (`getMe`).
- ✅ 2. `user_id` de Wendel fourni par Sidy : `1244601251`.
- ✅ 3. `TELEGRAM_BOT_TOKEN` + `TELEGRAM_ALLOWED_USERS` écrits dans le `.env`
  du profil après consentement explicite (chemin terminal direct : le fichier
  `.env` est protégé en lecture par l'outillage, à juste titre).
- ✅ 4. Gateway installée — non via `gateway install` mais par réplication
  directe de l'unité systemd de Mehdi (`hermes-gateway-habib-wendel.service`,
  User/Group `wendel`, HERMES_HOME pointé sur le profil), activée et démarrée
  le 2026-08-21. Vérifié : service `active (running)`, `NRestarts=0`,
  `getWebhookInfo` sans webhook avec polling long actif (`allowed_updates`
  enregistrés). Le log « Connected as » n'est pas apparu explicitement au
  démarrage (le canal Mehdi avait eu le même comportement initial) — la
  vérification définitive reste le test réel.
- ⏳ 5. **Test réel** : message de Wendel → atterrit dans `_inbox/`.
  **Test négatif** : utilisateur non allowlisté sans réponse.
  `ps -o user=` doit confirmer `wendel`.

## 5. Points ouverts

- **Sas partagé** : le bind rw de `_inbox/` donne à `wendel` la lecture des
  dépôts en attente d'autres personnes (même point ouvert que pour Mehdi,
  accepté tel quel ; durcissement possible via sous-dossier dédié).
- **Pièces jointes** : comportement de téléchargement de la toolset
  `hermes-telegram` (photo, note vocale) non vérifié — same as Mehdi, à
  confirmer au premier envoi réel.
- **Deux futures instances** : si un accès Terminal est ouvert plus tard à
  Wendel, il faudra signaler comme pour Mehdi que les deux instances ne
  partagent pas de mémoire.
- **`statut_experience: exploratoire`** jusqu'au test réel (message reçu
  dans `_inbox/`), puis `reproduit` (le mécanisme `--run-as-user` ayant déjà
  été éprouvé par le canal Mehdi, ce chantier pourrait passer directement à
  `adopte` après test — verdict réservé à Sidy).
