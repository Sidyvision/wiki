---
title: "Incident R&D — Saturation RAM critique et indisponibilité des agents (2026-08-28)"
type: infrastructure
date: 2026-08-28
created: 2026-08-28
updated: 2026-09-08
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

## Addendum (2026-09-08) — récidive et arrêt temporaire d'OmniRoute

**Symptôme** : terminal extrêmement lent signalé par Sidy. Mesures prises côté serveur à
17:19-17:24 UTC : RAM à 90 % (3,5/3,7 Gi utilisés), **swap plein à 100 %** (2,0/2,0 Gi),
`kswapd0` (démon noyau de gestion du swap) cumulant 119h32 de CPU depuis le 3 septembre —
signe d'un état de thrashing (échange RAM/disque permanent) filé sur cinq jours, pas d'un
pic ponctuel.

**Diagnostic** : `omniroute.service`, actif en continu depuis le 2026-09-07 14:28:40 UTC
(~27h), consommait à ce moment **1,9 Gio de RSS + 1,6 Gio de swap** (pic mesuré 2,3 Gio /
pic swap 1,6 Gio) — au-dessus de la fourchette historique 1,0–1,6 Gio relevée le
2026-08-31 ([[atelier/rd/infrastructure/cartographie-routing-infrastructure]], §1). La
cause structurelle est **inchangée depuis cet incident** : 3,7 Gio de RAM physique,
plafond matériel fixe, insuffisant pour la charge combinée des gateways Hermes et
d'OmniRoute — la même contrainte que la cartographie nomme non résolue en §4-5
(« la pression est revenue »).

**Résolution (temporaire)** : `systemctl stop omniroute` exécuté par Sidy le 2026-09-08 à
17:35:39 UTC. Effet mesuré : RAM disponible passée de 207 Mio à **2,0 Gio**, swap de
2,0/2,0 Gio (plein) à **400 Mio**. Arrêt **non permanent** : le service reste `enabled` au
disque (pas de `disable` exécuté), il repartirait au prochain redémarrage du serveur. Le
service s'est arrêté en état `failed (Result: exit-code)`, code 143 — SIGTERM non
intercepté proprement par le process Node, plutôt que le `inactive (dead)` attendu d'un
arrêt propre. Écart de forme sans conséquence sur le résultat mesuré (la RAM a bien été
libérée) : à distinguer du motif de `failed` du 28 août, qui signalait alors de vraies
tentatives de démarrage avortées après reboot, pas un arrêt volontaire.

**Effet de bord assumé** : le routage LLM des profils `gardien`, `studio`, `publication`
et du Terminal est indisponible tant qu'OmniRoute reste arrêté.

**Compréhension tirée** : récidive de la fragilité structurelle du 28 août, jamais levée
depuis. Signal nouveau à surveiller dans la durée : l'empreinte mémoire d'OmniRoute ce
jour (1,9 Gio) dépasse la fourchette historique — reste à établir si c'est une charge de
routage simplement plus lourde ou une dérive mémoire progressive. La décision structurelle
(upgrade RAM, ou régime « gateway à la demande » déjà nommé comme piste le 28 août) reste
entière à Sidy (Cmd 13) ; cet arrêt est un geste conservatoire, pas une résolution.

## Liens
- [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]]
- [[atelier/rd/infrastructure/cartographie-routing-infrastructure]]
- [[atelier/rd/cahiers/registre-problemes]]
