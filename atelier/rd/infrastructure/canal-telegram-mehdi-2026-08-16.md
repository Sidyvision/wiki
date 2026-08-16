---
title: "Infrastructure — Canal Telegram pour Mehdi, second robinet vers _inbox/"
type: infrastructure
tags: [rd, infrastructure, karubi, transmissions, telegram, hermes]
created: 2026-08-16
updated: 2026-08-16
sources: []
links: [atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12.md, meta/transmissions/karubi-mehdi.md, meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md, meta/transmissions/registre-silsila.md]
statut_experience: reproduit
---

# Canal Telegram pour Mehdi, second robinet vers `_inbox/`

> Décision Sidy du 2026-08-16 : Mehdi demande un moyen de déposer une note ou
> un fichier **hors Terminal** (téléphone, note rapide). Habib doit pouvoir
> l'instruire sur l'ouverture de ce canal. La confluence reste `_inbox/` — ce
> n'est jamais un nouveau périmètre, seulement un second chemin vers le même
> sas déjà décrit dans `acces-scope-mehdi-habib-2026-08-12.md`.

## 1. Problème posé

Le compte `mehdi` (voir fiche liée ci-dessus) donne un accès Terminal scopé,
mais un dépôt depuis un téléphone (note vocale retranscrite, photo, remarque
courte) sans ouvrir de session SSH est un usage distinct, plus léger. Deux
options techniques ont été examinées :

- Activer Telegram sur le profil H‍ermes `karubi` existant (celui que Sidy
  utilise pour le G0 de la navette Karūbī) : **écartée**. Vérifié cette
  session : les 12 gateways H‍ermes en production tournent tous en
  `systemctl --user` **sous root** (confirmé par `systemctl --user list-units`
  exécuté en tant que root, sans bascule `-M`). Le profil `karubi` a
  `terminal.cwd: /root/wiki` — le dépôt entier. Y brancher l'allowlist
  Telegram de Mehdi aurait donné à ses messages accès à un agent scopé **par
  le prompt seulement**, pas par le bind mount `ro` qui est la frontière
  réelle du dispositif décrit dans la fiche liée (§1 : « la frontière réelle
  [est] le montage ro au niveau OS »). Un canal supplémentaire n'a pas à
  affaiblir une garantie déjà posée.
- Script déterministe (poller Telegram sans LLM) : option plus simple,
  candidate sérieuse, mais écartée par Sidy en faveur de la suivante pour
  garder un Habib capable de répondre, pas seulement de déposer.

## 2. Solution retenue

**Nouveau profil H‍ermes dédié, exécuté comme service système sous le compte
`mehdi`** (uid 1000) — pas sous root, contrairement aux 12 profils existants.

- `hermes gateway install --system --run-as-user mehdi` (option confirmée par
  `hermes gateway install --help`, distincte de `--force`/`--start-now`) :
  crée un service systemd **système** (pas `--user` de root) qui s'exécute
  sous l'identité `mehdi`. `HERMES_HOME` se résout par défaut à
  `Path.home() / ".hermes"` (confirmé dans `hermes_constants.py`,
  `get_hermes_home`) — donc **sous ce compte**, `HERMES_HOME` devient
  `/home/mehdi/.hermes`, distinct de `/root/.hermes`. La frontière OS n'est
  plus contournée : ce processus est soumis aux mêmes permissions Unix que
  toute session Mehdi/SSH.
- Nom de profil proposé : `habib-mehdi` (distinct de `karubi`, qui reste
  l'outil G0 de Sidy — aucune confusion de nom, aucun partage d'instance).
- `config.yaml` du nouveau profil, points clés :
  - `terminal.cwd: /home/mehdi/depot-lecture` — même périmètre de lecture que
    la session Terminal de Mehdi (déjà scopé par bind mounts `ro`), pas
    `/root/wiki`.
  - `platform_toolsets: {telegram: [hermes-telegram]}` uniquement — pas de
    Discord, pas d'autres plateformes sur ce profil.
  - Persona : copie verbatim de `/home/mehdi/CLAUDE.md` en `SOUL.md` du
    profil (même règle que pour les 12 profils, fiche 15 §1 : le prompt
    versionné vit dans le dépôt, `SOUL.md` en est une copie locale non
    versionnée).
- `.env` du nouveau profil (jamais commité — secrets) :
  - `TELEGRAM_BOT_TOKEN` — token du bot créé via `@BotFather`.
  - `TELEGRAM_ALLOWED_USERS` — le seul `user_id` numérique Telegram de Mehdi
    (allowlist fail-closed, confirmé dans `authz_mixin.py`,
    `platform_env_map`).
  - `TELEGRAM_HOME_CHANNEL` (+ `_NAME` optionnel) — non utilisé dans ce sens
    (pas de message système poussé vers Mehdi par cron), laissé vide.
  - `chmod 600` systématique (règle fiche 15 §4, appliquée à l'identique).
- Comportement attendu : tout message reçu de l'utilisateur Telegram
  allowlisté est traité par l'agent Habib (lecture `depot-lecture/`, écriture
  `depot-ecriture/inbox/` — mêmes droits que la session Terminal de Mehdi,
  car même compte Unix), qui dépose le contenu (texte, ou pièce jointe
  téléchargée) dans `depot-ecriture/inbox/telegram-<horodatage>.md` (ou
  extension d'origine pour un fichier joint) → bind mount rw → `_inbox/` du
  dépôt canonique. Aucune écriture ailleurs : ce périmètre est celui déjà
  vérifié pour la session Terminal (§3 de la fiche liée), inchangé ici — même
  compte, même droits, second point d'entrée seulement.

## 3. Vérifications à effectuer (avant de considérer le canal « en service »)

Rien n'est encore exécuté — cette fiche documente la procédure, pas un état
acquis. Étapes humaines requises avant toute vérification (Cmd 13, hors
exécution agent) :

- Sidy crée le bot via `@BotFather`, récupère le token.
- Mehdi envoie `/start` au bot une fois créé, ou communique son `user_id`
  Telegram par un canal séparé du dépôt (même pratique que pour sa clé SSH).
- Sidy (ou moi sur confirmation explicite du token) édite le `.env` du
  nouveau profil `habib-mehdi`.
- `hermes gateway install --system --run-as-user mehdi` puis
  `hermes -p habib-mehdi gateway restart`.

Une fois ces étapes faites :

- `grep "Connected as" /home/mehdi/.hermes/profiles/habib-mehdi/logs/gateway.log`
  — vérification obligatoire, ne jamais faire confiance à l'absence d'erreur
  seule (règle fiche 15 §4).
- Test réel : Mehdi envoie un message test, vérifier qu'il atterrit dans
  `_inbox/` (via `depot-ecriture/inbox/`) avec le bon horodatage/contenu.
- Test négatif : un utilisateur Telegram non allowlisté (second compte test,
  ou revue de code de la toolset `hermes-telegram` à défaut) ne reçoit aucune
  réponse.
- `ps -o user= -p <pid du service>` confirme que le processus tourne bien
  sous `mehdi`, pas sous `root` — vérification de la garantie même du §2
  ci-dessus (sans quoi cette fiche documenterait une frontière qui n'existe
  pas réellement).

## 4. Points ouverts

- **Mécanisme non encore éprouvé** : `--run-as-user` sur `gateway install
  --system` n'a jamais été utilisé pour aucun des 12 profils existants (tous
  en `--user` sous root). Premher usage réel de ce chemin — à traiter comme
  `statut_experience: exploratoire` jusqu'à un test en conditions réelles.
- ~~**Dépendance non résolue, plus prioritaire que ce chantier**~~ — **résolue
  le 2026-08-16** : le point de montage `depot-lecture/karubi-mehdi.md`
  n'était en réalité pas monté du tout (fichier vide à la place, malgré une
  entrée `fstab` correcte). `mount -o bind,ro` seul (sans `umount` préalable,
  puisque rien n'était monté) a suffi. Inode et contenu identiques des deux
  côtés désormais, écriture toujours refusée — voir
  `meta/transmissions/registre-silsila.md`, entrée `correction-montage`.
- **Écriture du contenu joint (photo, audio)** : le comportement exact de
  téléchargement de pièces jointes par la toolset `hermes-telegram` n'a pas
  été vérifié dans le code source à la rédaction de cette fiche — à confirmer
  avant le test réel (peut nécessiter une conversion, ex. note vocale → texte
  ou dépôt brut du fichier audio).
- **Persona dupliquée entre deux points d'entrée** : Habib existe maintenant
  sous deux formes indépendantes pour Mehdi — la session Claude Code Terminal
  (`/home/mehdi/CLAUDE.md`, invoquée manuellement) et ce nouveau profil
  H‍ermes Telegram (`habib-mehdi`, toujours actif en tâche de fond). Elles
  partagent le même périmètre de lecture/écriture (même compte Unix) mais
  sont deux instances distinctes, sans mémoire partagée entre elles — à
  signaler à Mehdi pour éviter toute confusion (« ce que je te dis sur
  Telegram, la session Terminal ne le sait pas automatiquement »).
- **Registre spirituel hors champ** (corollaire agentique, `meta/CLAUDE.md`
  point 4) : ce canal, comme la session Terminal, documente et organise —
  il n'interprète ni ne conseille sur un plan spirituel.

## 5. Réalisé le 2026-08-16 (architecture initiale corrigée et en service)

**Écart initial puis correction** : une session Hermes terminal a d'abord
configuré Telegram sur le profil `karubi` existant (sous root, sans isolation
OS). Verdict Sidy : reprendre l'architecture initiale de la fiche R&D.

**Architecture finale en service** :
- **Profil** : `habib-mehdi` créé sous `/home/mehdi/.hermes/profiles/habib-mehdi/`
- **Service** : `hermes-gateway-habib-mehdi.service` (systemd système), tourne
  sous l'utilisateur `mehdi` (uid 1000) — isolation OS respectée
- **Token** : stocké dans `.env` du profil `habib-mehdi`, non reproduit ici
  (secret — jamais en clair dans une fiche versionnée) — bot `@HabibKarubi_bot`
  (réutilisé depuis karubi)
- **Allowlist** : `TELEGRAM_ALLOWED_USERS=817763036` (Mehdi) dans
  `/home/mehdi/.hermes/profiles/habib-mehdi/.env`
- **Cwd** : `/home/mehdi/depot-lecture` (bind mount ro sur `/root/wiki/doctrinal`,
  `/root/wiki/hermeneutique`, `/root/wiki/rd`, `/root/wiki/karubi-mehdi.md`)
- **Module Telegram** : `hermes-agent[telegram]` installé dans le venv système
- **Test réel** : message envoyé via `sudo -u mehdi hermes --profile habib-mehdi
  send --to telegram:817763036` — reçu côté Mehdi ✅
- **État** : opérationnel, isolation OS vérifiée (`ps -o user=` → `mehdi`)

**Nettoyage karubi** :
- Token et allowlist retirés de `/root/.hermes/profiles/karubi/.env`
- Service `hermes-gateway-karubi.service` arrêté et désactivé
- Mehdi ne parle plus à la créature ailée via Telegram

**Points ouverts restants** :
- Écriture de pièces jointes (photo, audio) : comportement de téléchargement
  par la toolset `hermes-telegram` non encore vérifié — à confirmer si Mehdi
  envoie des fichiers
- Mémoire partagée : aucune entre ce canal Telegram et la session Terminal de
  Mehdi (deux instances Hermes distinctes, même compte Unix)
- Registre spirituel hors champ (corollaire agentique, `meta/CLAUDE.md` point 4)
