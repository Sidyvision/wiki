---
title: Bureau TUI — architecture
type: infrastructure
tags:
- rd
- infrastructure
- tui
- textual
- bureau
- ansi
- chat
- hermes
- instrument
created: 2026-08-15
updated: 2026-08-15
sources: []
links:
- '[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]'
---

# Bureau TUI — architecture

> `statut_experience: exploratoire` — première version, verdict Sidy du
> 2026-08-15 (plan validé en session Claude Code). Objet : un tableau de bord
> unique exécutable en terminal, rassemblant lecteur vidéo, lecteur audio
> (streaming), lecteur de textes/images, chat, état de l'Instrument et état des
> 12 agents Hermès. Esthétique "menu de jeu vidéo" — inspiration relevée dans
> [[hermeneutique/metal-gear/mother-base]] §5bis/§5ter (un point d'entrée
> unique vers des sous-systèmes hétérogènes, l'interface qui ne suspend jamais
> le monde, l'observabilité en lecture seule séparée de l'action) et
> [[hermeneutique/metal-gear/idroid]] (interface comme membrane entre
> l'individu et l'infrastructure collective) — **transposition de forme
> uniquement**, aucune correspondance doctrinale invoquée (Cmd 3 : la
> fiche source elle-même le précise, aucune `cle_doctrinale` n'y est posée).

## Pourquoi (contexte)

Sidy veut consulter en un coup d'œil, depuis un terminal, l'état de son
infrastructure personnelle (Instrument, agents Hermès) et disposer d'outils
usuels (média, lecture, messagerie) sans quitter ce point d'entrée — sur un
serveur headless aux ressources limitées (Hetzner, 2 vCPU, 3.7 Go RAM,
2.2 Go déjà utilisés + swap actif au 2026-08-15).

## Contraintes vérifiées avant conception

- `ffmpeg` installé ; `mpv`/`chafa` absents → rendu vidéo/image ANSI fait main.
- Les 12 agents Hermès sont des process `hermes_cli.main --profile <nom>
  gateway run` (pas des services systemd) ; le CLI `hermes` expose une
  commande `status` utilisable pour un état déterministe.
- Aucun serveur de chat n'existait — écrit ici, léger (asyncio).
- `Pillow`, `websockets`, `textual`, `pypdf` : dépendances ajoutées (aucune
  n'était présente sur la machine).

## Architecture

Voir `bureau/README.md` pour le détail d'exécution. Résumé :

- `app.py` — App Textual, grille de tuiles façon menu de jeu vidéo ; chaque
  tuile résume un module, `Entrée` l'agrandit en plein panneau (mode
  monocle), `Échap` revient à la vue d'ensemble.
- `modules/` — six briques indépendantes (`base.Module` commun) :
  vidéo, audio, lecteur textes/images, chat, état Instrument, état agents.
- `services/` — `ansi_render.py` (rendu demi-bloc partagé vidéo+images),
  `chat_server.py` (asyncio websockets, process séparé), `audio_stream.py`
  (petit serveur HTTP de streaming).

## Conformité au protocole

- Flux à sens unique : le bureau **lit** le dépôt (`instrument-donnees.yaml`,
  `wiki-manifest.json`, `meta/projet-unifie/hermes-prompts/*.md`), n'y **écrit
  jamais**.
- État de l'Instrument lu depuis les manifestes déterministes uniquement
  (jamais de parsing interprétatif de prose) — esprit de la règle des
  manifestes (§VII racine).
- Chat et streaming audio bindés sur `127.0.0.1` par défaut ; accès distant
  via tunnel SSH ou Tailscale, jamais de port ouvert publiquement (§VIII.8).
- Aucun secret dans git : configuration sensible (ports si changés, tokens
  futurs) dans un `.env` local gitigoré.
- Rendu vidéo/image déclenché uniquement à la demande explicite, jamais en
  tâche de fond, compte tenu de la RAM/CPU disponibles.
- Passerelle chat ↔ agents Hermès (relais Discord) **non implémentée** dans
  cette version : reportée, touche l'infrastructure agentique existante
  (credentials, allowlist §VIII.8), demande session et verdict séparés.

## État d'avancement

- [x] Fiche d'architecture (présente fiche).
- [x] Squelette du projet (`bureau/`) et App Textual (grille, monocle,
      navigation clavier).
- [x] Modules : instrument, agents, lecteur, vidéo, audio, chat.
- [x] Tests unitaires (`tests/`, 10 tests, rendu ANSI + parsing manifestes/
      missions) et lint (`ruff`) : tous verts.
- [x] Fumée automatisée (`textual` `run_test`/pilot headless) : les six
      modules s'ouvrent en mode monocle sans erreur de montage.
- [ ] Vérification en conditions réelles (terminal SSH), mesure CPU/RAM
      pendant un rendu vidéo, écoute audio via tunnel, chat à deux clients —
      **reste à faire par Sidy en session réelle** (le pilote headless ne
      teste pas le rendu visuel ni l'accès réseau distant).
- [ ] Entrée `atelier/annales.md` avec SHA du commit (après revue et commit).
