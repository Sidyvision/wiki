---
title: "Incident R&D — Saturation RAM critique et indisponibilité des agents (2026-08-28)"
type: fiche-rd
date: 2026-08-28
created: 2026-08-28
updated: 2026-08-28
circuit: rd/infrastructure
statut: resolu
resolution_date: 2026-08-28
---

# Incident R&D — Saturation RAM critique et indisponibilité des agents

**Date :** 2026-08-28
**Périmètre :** Infrastructure multi-gateways (14 instances actives), OmniRoute daemonisé, Discord.

## Symptôme
- **Saturation système** : RAM système à 3.7 Go, dont 3.5 Go utilisés (saturation critique). Usage intensif du SWAP (982 Mo sur 2 Go).
- **Indisponibilité** : Agents Discord silencieux, outils de diagnostic (`hermes doctor`) signalant une perte d'authentification (`logged out`), logs d'erreur signalant des échecs `503 Service Unavailable` sur les combos de routage modèle.
- **Blocage opérationnel** : Tentatives de redémarrage des services ou de gestion des processus bloquées par manque de mémoire vive.

## Diagnostic
1. **Saturation structurelle** : L'infrastructure de 14 gateways Hermes tournant en parallèle (chaque instance ~110-120 Mo de RAM) combinée à l'instance daemonisée d'OmniRoute (~1.6 Go de RAM) dépasse la capacité mémoire disponible de l'hôte (3.7 Go). Le système est entré en état de "famine" mémoire permanente (thrashing).
2. **Cause secondaire (sécurité)** : L'indisponibilité des agents Discord n'est pas une panne logicielle mais la conséquence directe de l'audit de sécurité du 27/08/2026. La rédaction (redaction) automatique des secrets dans `.env` et `.bash_history` (pour prévenir l'exposition en clair) a supprimé les tokens d'authentification, rendant les gateways incapables de se connecter aux API tiers (Discord, portail Hermes).
3. **Fragilité de la remédiation** : La daemonisation systemd (incident du 27/08) a permis la stabilité des processus, mais le passage à l'échelle (14 profils actifs) n'a pas été calibré pour la ressource mémoire totale.

## Résolution
*   **Effectuée (2026-08-28, session Sidy + agent WebUI)** :
    1. Redémarrage physique du serveur (via `sudo systemctl reboot`, opérateur — la commande est hardline-bloquée côté agent).
    2. Constat post-reboot : les 11 gateways métier gérés par `systemd --user` (root, PID 934) se relancent automatiquement, ré-saturant immédiatement la RAM (3.5/3.7 Go).
    3. Arrêt (`systemctl --user stop`) + désactivation (`systemctl --user disable`) des 8 gateways non essentiels (`accounting`, `admin-legal`, `ar-music`, `distribution`, `fanzine`, `marketing`, `production`, `visual-da`) — exécuté par Sidy depuis un shell extérieur au gateway (le filtre hermes bloque l'arrêt d'un gateway depuis un autre gateway, cf. registre-problèmes entrée `[2026-08-25] Discord Gateway Gardien`).
    4. État final : 3 gateways prioritaires actifs (`gardien`, `studio`, `publication`), RAM disponible ~900 Mo, agents Discord opérationnels confirmés par retour de Sidy en session.
*   **Non-résolution du diagnostic initial (auth)** : les jetons Discord et OAuth n'ont pas été touchés ; le diagnostic `hermes doctor` « logged out » sur Nous Portal/Codex/xAI/MiniMax est pré-existant et sans lien avec l'indisponibilité — ces auth n'étaient pas configurées avant l'incident, donc pas responsables du silence. **Erreur d'aiguillage initial du diagnostic** (première hypothèse : token Discord manquant / audit sécurité 27/08), corrigée après lecture des logs des gateways révélant les warnings `system memory pressure is critical` (~24h consécutives sur `gardien/errors.log`).

## Compréhension tirée
- **Pattern "Multi-Gateway"** : Le déploiement de 14 gateways Hermes est structurellement incompatible avec la RAM actuelle. Le paradigme "1 profil = 1 gateway active" doit être révisé : adopter une logique de *gateway à la demande* ou de regroupement de profils sur une même instance si le seuil mémoire est atteint.
- **Règle de sécurité vs opérationnalité** : La rédaction automatique des jetons de sécurité lors d'un audit est nécessaire, mais elle doit être immédiatement suivie d'une procédure de re-configuration sécurisée des jetons (via `hermes auth` et non `edit .env`) pour ne pas couper les services critiques.

## Liens
- [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]]
- [[atelier/rd/cahiers/registre-problemes]]
