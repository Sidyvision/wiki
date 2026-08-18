---
title: Infrastructure — Accès serveur scopé pour Mehdi via Habib (Karūbī)
type: infrastructure
tags:
- rd
- infrastructure
- karubi
- transmissions
- permissions
created: 2026-08-12
updated: 2026-08-12
sources: []
links:
- meta/transmissions/karubi-mehdi.md
- meta/transmissions/registre-silsila.md
- atelier/rd/cahiers/registre-problemes
statut_experience: exploratoire
---

# Accès serveur scopé pour Mehdi, par l'intermédiaire d'Habib

> Décision Sidy du 2026-08-11/12 : plutôt qu'un accès serveur direct pour
> Mehdi, le Karūbī (Habib) devient son intermédiaire technique — une session
> Claude Code sous compte Linux dédié, cantonnée à un périmètre de lecture
> scopé du dépôt, avec écriture uniquement vers son propre domaine et vers le
> sas `_inbox/`.

## 1. Problème posé

Mehdi (destinataire du Karūbī « Habib », voir `meta/transmissions/karubi-mehdi.md`)
souhaite un accès direct au serveur pour collaborer plus étroitement (corpus
Isaghuji, chantier Instrument/Mother Base). Un accès SSH brut casserait
l'étanchéité des circuits (CLAUDE.md §II/§VI) et le principe de verdict humain
(Cmd 6) — tout le dépôt serait exposé d'un coup, sans le filtre qu'incarne le
dispositif Karūbī.

## 2. Solution retenue

Compte Linux dédié `mehdi` (uid 1000, home `/home/mehdi`), avec deux domaines :

- **`depot-lecture/`** — bind mounts en lecture seule (`mount -o bind,ro`) vers :
  - `meta/transmissions/karubi-mehdi.md` (son propre fichier)
  - `atelier/rd/instrument/`, `atelier/rd/outillage/`, `atelier/rd/cahiers/`
    (le pôle R&D ouvert — **`atelier/rd/infrastructure/` explicitement exclu**,
    détails serveur hors périmètre)
  - `doctrinal/` (circuit complet)
  - `hermeneutique/` (circuit complet — ajouté le 2026-08-12, après le
    déploiement initial, sur décision Sidy)
- **`depot-ecriture/inbox/`** — bind mount lecture/écriture vers `_inbox/` du
  dépôt canonique (ACL `rwx` pour `mehdi`), pour déposer ses retours
  directement (ex. corpus Isaghuji) sans repasser systématiquement par Sidy.

Persistance : entrées `bind` dans `/etc/fstab` (backup préalable :
`/etc/fstab.bak-mehdi-20260812`).

Claude Code : `/home/mehdi/CLAUDE.md` (persona Habib, hérité de §3/§3bis du
Karūbī scellé, complété du protocole d'accès technique) et
`/home/mehdi/.claude/settings.json` (deny écriture/édition sur
`depot-lecture/**`, allow sur `depot-ecriture/**` — défense en profondeur,
la frontière réelle étant déjà le montage `ro` au niveau OS).

## 3. Vérifications effectuées (2026-08-12)

- Lecture de `depot-lecture/karubi-mehdi.md` : OK.
- Écriture sur `depot-lecture/karubi-mehdi.md` : refusée (`Permission denied`).
- Traversée `/root/wiki` directement (hors montages) : refusée (`Permission denied`).
- Traversée via `..` depuis un point monté : ne s'échappe pas du point de
  montage (comportement bind mount standard).
- `depot-lecture/rd/infrastructure/` : absent (confirmé exclu du périmètre).
- Copie `depot-lecture/** → depot-ecriture/inbox/` : OK.
- `generer-karubi.py verifier meta/transmissions/karubi-mehdi.md` après coup :
  `SCEAU INTACT`, hash inchangé (`22782cf6...c9c`) — aucune manipulation
  n'a touché le fichier canonique pendant la mise en place.

## 4. Points ouverts

- Le bind mount `rw` de `_inbox/` donne à `mehdi` la lecture du contenu déjà
  présent dans le sas (dépôts d'autres personnes en attente d'intégration),
  pas seulement l'écriture — un "écriture pure" strict n'est pas trivial en
  ACL POSIX standard. Accepté tel quel pour l'instant (le sas est par nature
  transitoire, vidé après chaque intégration) ; à durcir si besoin (ex. un
  sous-dossier `_inbox/mehdi/` dédié plutôt que le sas partagé).
- Aucun sandboxing process-level (bubblewrap/Docker) — la frontière est
  purement filesystem (bind mount ro + ACL + permissions Unix standard).
  Jugé suffisant pour ce premier déploiement (cohérent avec le choix "statu
  quo léger" déjà fait pour H‍ermes, mais ici renforcé par un compte OS dédié
  vu la nature humaine/SSH de l'accès).
- Le circuit `label/` reste hors périmètre de lecture — à revoir si la
  collaboration s'étend dans cette direction.
- **`statut_experience: exploratoire`** (2026-08-12) : le compte `mehdi` reste
  verrouillé, aucune connexion effective n'a encore eu lieu — la clé SSH
  publique de Mehdi est attendue à sa prochaine navette (voir §10 de
  `karubi-mehdi.md`). Ce chantier passe à `reproduit` puis `adopte` une fois
  une session Habib réellement testée en conditions réelles depuis le compte
  de Mehdi.
