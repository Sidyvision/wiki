---
title: "Incident R&D — OmniRoute EADDRINUSE et daemonisation systemd (2026-08-27)"
type: fiche-rd
date: 2026-08-27
created: 2026-08-27
updated: 2026-08-27
circuit: rd/infrastructure
statut: consignation
---

# Incident R&D — OmniRoute EADDRINUSE et daemonisation systemd

**Date :** 2026-08-27 (07:29–07:31 UTC)
**Composant concerné :** OmniRoute (proxy de routage de modèle, port 20128)
**Rédigé par :** Claude (Sonnet 5), sur relecture croisée d'un rapport Gemini + vérification directe des logs système + confirmation de l'opérateur (Sidy)

## Contexte amont

Depuis le 2026-08-26, OmniRoute tourne en fallback suite à l'atteinte du quota
hebdomadaire du plan Qwen (voir
[[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]]). Ce
fallback n'avait pas été anticipé comme dépendant d'une connexion terminal
active en permanence pour que le routing de modèle persiste (notamment pour
les cron jobs des agents Hermes).

Le 2026-08-27 au matin : configuration de Termius sur iPhone 16 Pro Max →
lancement manuel d'OmniRoute → relance via Hermes WebUI des tâches agents
interrompues la veille (interruption due au quota Qwen atteint). La connexion
Termius s'est coupée peu après cette relance — comportement connu de l'app sur
iOS (coupure au changement d'app ou à la mise en veille) — tuant l'instance
OmniRoute manuelle et entraînant le conflit de port décrit ci-dessous.

## Symptômes

À la tentative de reprise en main (création d'un service systemd pour
OmniRoute), trois cycles de démarrage successifs échouent :

```
Error: listen EADDRINUSE: address already in use 0.0.0.0:20128
```

## Diagnostic (confirmé par `journalctl -u omniroute`)

- 07:29:25 → 07:30:34 : trois instances lancées par systemd (PID 2274440,
  2274524, 2274590) échouent chacune deux fois avec `EADDRINUSE`, avant que
  systemd n'abandonne (`Failed with result 'exit-code'`) et ne retente.
- 07:30:39 : arrêt manuel enregistré (`Stopping omniroute.service`).
- 07:31:27 → 07:31:55 : démarrage réussi après 26,9s (contre ~0,1s pour les
  tentatives précédentes), signe qu'un obstacle a été levé entre les deux.
- Aucun processus résiduel présent après coup.

## Cause

**Confirmée par l'opérateur** : la déconnexion du terminal Termius pendant
l'exécution d'un agent a laissé le processus `omniroute` manuel (lancé hors
daemon) tourner sans supervision, occupant le port 20128 — ce qui a fait
échouer les trois premières tentatives de démarrage du service systemd.

Le mécanisme exact (sockets `CLOSE_WAIT` résiduels vs process encore
réellement vivant — hypothèse avancée par un rapport Gemini consulté en cours
d'intervention) n'est **pas tranché** par les logs disponibles (`journalctl`,
`.bash_history`) : les PID cités par ce rapport (2184165, 2259924, 2260369,
2272600) et l'usage revendiqué de `kill -9`/`fuser -k` n'y sont pas retrouvés
— probablement de simples commandes tapées à la main dans une session dont
l'historique n'avait pas encore été flushé sur disque au moment de la
vérification. Sans incidence sur le diagnostic ni la remédiation.

## Résolution

Daemonisation d'OmniRoute via un service systemd :

```
/etc/systemd/system/omniroute.service
[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart=/usr/bin/omniroute
Restart=always
RestartSec=3
```

`systemctl enable --now omniroute`. État vérifié : `active (running)`,
`enabled` (survit au reboot), stable depuis 07:31:27 sans redémarrage depuis.

## Enseignement pour la doctrine R&D

Le vrai point de fragilité n'était pas OmniRoute lui-même mais le
**couplage implicite entre routing de modèle et session terminal mobile** —
un mode de connexion par nature instable sur iOS (changement d'app, veille).
La daemonisation systemd supprime structurellement cette dépendance : les
cron jobs et agents Hermes n'ont plus besoin d'un onglet Termius ouvert pour
que le routing persiste.

**Point de vigilance pour l'avenir :** avant toute future daemonisation d'un
process jusque-là lancé à la main, tuer explicitement toute instance
manuelle résiduelle avant le premier `systemctl start`
(`ss -tlnp | grep <port>`), pour éviter la course au port observée ici.

## Note de sécurité annexe (sans lien direct avec l'incident)

En cours de vérification, un `ANTHROPIC_AUTH_TOKEN` en clair a été repéré
dans `/root/.bash_history` et `/root/.omniroute-env.sh` (fichier non chargé
par aucun service actif — OmniRoute charge désormais son propre `.env` via
`/root/.omniroute/.env`). Le token a été redacté des deux fichiers sur disque
le 2026-08-27. **Ceci n'a pas révoqué le token côté fournisseur** — à faire
séparément si ce token est encore valide.

## Connexions

- Lié à : [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]]
