---
title: "Incident R&D — Saturation RAM critique et indisponibilité des agents (2026-08-28)"
type: fiche-rd
date: 2026-08-28
created: 2026-08-28
updated: 2026-08-28
circuit: rd/infrastructure
statut: ouvert
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
*   **Immédiate** : Aucune intervention système (reboot/kill) n'est possible via l'agent (protection hardline). **Redémarrage physique de l'hôte requis par l'opérateur.**
*   **Court terme (post-reboot) :** 
    1. Ré-authentification ciblée : lancer `hermes auth` uniquement pour les profils critiques (`gardien`, `studio`, `publication`).
    2. Rationnement des gateways : arrêter les gateways des profils non utilisés (`fanzine`, `commerce`, `visual-da`, etc.) pour maintenir le système sous le seuil de saturation mémoire.

## Compréhension tirée
- **Pattern "Multi-Gateway"** : Le déploiement de 14 gateways Hermes est structurellement incompatible avec la RAM actuelle. Le paradigme "1 profil = 1 gateway active" doit être révisé : adopter une logique de *gateway à la demande* ou de regroupement de profils sur une même instance si le seuil mémoire est atteint.
- **Règle de sécurité vs opérationnalité** : La rédaction automatique des jetons de sécurité lors d'un audit est nécessaire, mais elle doit être immédiatement suivie d'une procédure de re-configuration sécurisée des jetons (via `hermes auth` et non `edit .env`) pour ne pas couper les services critiques.

## Liens
- [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]]
- [[atelier/rd/cahiers/registre-problemes]]
