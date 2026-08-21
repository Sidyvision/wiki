---
title: "Pistes de développement — infrastructure et outillage R&D (2026-08-20)"
type: infrastructure
statut_experience: exploratoire
tags: [rd, infrastructure, bilan, pistes-developpement]
created: 2026-08-20
updated: 2026-08-20
sources: []
links: ["[[atelier/rd/index]]", "[[atelier/rd/cahiers/bilan-2026-08-15-pont-agents]]", "[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]", "[[atelier/rd/infrastructure/bureau-tui-architecture]]", "[[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]]", "[[atelier/rd/veille/cordis/notes-lecture]]", "[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]"]
---

# Pistes de développement — infrastructure et outillage R&D

## Contexte

Reprise, à la demande de Sidy, du rapport conjoint Studio–Gardien du 2026-08-20
qui devait porter sur les pistes de développement du dépôt/infrastructure en
général (le Gardien s'étant enlisé techniquement — voir
[[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]] —
son rapport final a dérivé vers un simple audit de vigilance). Le pendant
spécifique au chantier de l'Instrument est consigné dans
[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]].

**Méthode** : lecture intégrale de l'état de l'infrastructure serveur, du Bureau
TUI, du bilan pont inter-agents du 2026-08-15, des propositions Phase 3 (veille
infrastructure) et de son extension du 2026-08-18, de la veille externe Cordis,
et de l'incident de robustesse persona-LLM.

**Posture** : signalement et pistes, aucun verdict (Cmd 12/13).

---

## 1. Infrastructure serveur — état et points ouverts

D'après `infrastructure-architecture-global-2026-08-11.md` (constat factuel,
« sans recommandation ») : serveur Hetzner (2 vCPU, 3.7 GB RAM, 38 GB disque,
51% libre), 12 profils Hermes actifs (639.5 MB RAM cumulés, 17%), charge quasi
nulle mais **swap déjà sollicité (1/2 GB)**.

**Anomalie non résolue la plus notable** : le processus `omniroute` (passerelle
Discord↔Hermes) consomme **1040 MB RAM — 28% du total, plus que les 12 agents
réunis** — et sa fonction précise n'est toujours pas documentée à ce jour
(« investigation ouverte » depuis le 2026-08-11).

**Points de fragilité identifiés** (SPoF) : clé API Anthropic partagée par les
11 agents (perte = paralysie collective) ; fonction d'omniroute inconnue ; clé
SSH Hetzner unique ; absence de sauvegarde hors-site ; aucun monitoring de
charge en série temporelle (seul un rapport quotidien ponctuel existe via le
cron `monitoring-infrastructure-quotidien`, archivé mais non agrégé en série).

## 2. Chantiers déjà tranchés côté décision, non exécutés

Plusieurs pistes de développement ne sont **pas des idées nouvelles** : elles
ont déjà reçu un verdict de principe et n'attendent que l'exécution technique
(rappel Cmd 6 : l'exécution reste une étape distincte de la décision).

- **Phase 3 — veille infrastructure** (`proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  toujours `brouillon` bien que les décisions listées soient tranchées) :
  agent désigné (Studio Sound Engineer), canal `#infrastructure`, cron
  quotidien 12:00, accès FS accordé. Reste à exécuter : `hermes cron create`
  côté profil studio, création + allowlisting effectif du canal Discord,
  redémarrage du gateway.
- **Extension veille externe R&D + sandbox** (`proposition-extension-veille-rd-2026-08-18.md`,
  statut `effectif` depuis le 2026-08-18) : reste à instruire — extension
  effective du prompt agent côté veille externe, mécanisme de cron
  hebdomadaire, mise en place réelle de `/root/sandbox-rd/` (le dossier existe
  mais est vide selon le rapport conjoint du 2026-08-20), format du rapport
  hebdomadaire.
- **Bureau TUI** (`bureau-tui-architecture.md`, verdict Sidy 2026-08-15) :
  squelette, 6 modules, tests unitaires et fumée automatisée tous verts —
  mais **jamais vérifié en conditions réelles** (SSH, CPU/RAM pendant un rendu
  vidéo, tunnel audio, chat multi-client). Reste hors périmètre : la
  passerelle chat ↔ agents Hermès (touche credentials/allowlist, session
  séparée requise).
- **SRS Hermes-native** (bilan pont-agents §III.C) : principe décidé
  (intégration native, pas d'outil SRS tiers), mais format de carte, script
  d'extraction, mécanisme de révision et algorithme d'espacement restent
  entièrement à définir.
- **Isolation mémoire Hermes par sub-agent** (bilan pont-agents §III.A) :
  bloquant technique identifié pour le déploiement du skill Karūbī — aucun
  toggle `memory_enabled` trouvé à ce jour, non résolu.

## 3. Veille externe Cordis — piste d'applicabilité à instruire

Le paradigme Cordis (effets réversibles, coeffects réactifs, HMR sans
redémarrage — cas d'étude Koishi, 600+ plugins) a été rapproché **par forme**,
non doctrinalement, de la convention Sashimono (`veille/cordis/notes-lecture.md`) :
effet réversible ↔ démontage sans joint forcé, retrait sans trace ↔ montage à
blanc. Trois chantiers d'applicabilité sont posés comme **questions ouvertes,
non instruites** :
1. HMR pour les 12 agents Hermes (remplacement à chaud sans redémarrage,
   revert automatique des effets cumulés).
2. Gestion des dépendances inter-gateways.
3. Modélisation des fiches de veille R&D elles-mêmes comme effets réversibles.

Aucun rapprochement n'est en revanche fait, dans les documents actuels, entre
Cordis et l'architecture de l'Instrument elle-même (flux `wiki → manifeste →
app` à sens unique) — un air de famille est repérable (irréversibilité
contrôlée) mais n'a jamais été formulé nulle part. Signalé comme piste
possible, non comme lien établi.

Reste également ouvert côté registre de veille : identifier le dépôt source
Cordis (TypeScript original), l'identité du contributeur `inso1337`, et la
nature exacte du repo `spatiotemporal-composability-skill`
(`atelier/rd/veille/registre.md`).

## 4. Outillage — points restants

- `verifier-invariants.py` : angle mort C3 sur annales/index, en attente
  d'arbitrage (bilan pont-agents §III.E).
- `Graphe/generer-cartographie.json` jamais régénéré — 4 anomalies bloquantes
  de frontmatter recensées le 2026-08-20 (voir rapport conjoint en `_inbox/`,
  déjà en cours de traitement séparément).
- Incident de robustesse documents-persona-LLM (`robustesse-documents-persona-llm.md`,
  2026-07-20) : statut final « en cours » — la résolution appliquée n'est
  vérifiée qu'au niveau de l'intégrité cryptographique (hash inchangé), **pas
  encore confirmée au niveau comportemental**. Reproduction contrôlée non
  encore effectuée (relève de la discipline de laboratoire complète, phase 2
  du pôle R&D, non ouverte).

## 5. Hygiène signalée en marge

Le `README.md` de `atelier/rd/cahiers/brouillons-extension-zodiacale/` ne
correspond pas exactement aux 12 fichiers réellement présents dans le dossier
(signes divergents pour les positions 02/06/07/09 entre le tableau du README
et les noms de fichiers réels ; les positions 5/8/12 sont dites « hors
périmètre, en attente de verdict » dans le texte du README alors que les
fichiers `05-accounting-taurus.md`, `08-publication-sagittarius.md` et
`12-commerce-pisces.md` existent déjà sur disque). Point non résolu par cette
passe (nécessiterait l'ouverture des 12 fichiers), signalé pour vérification.

---

## 6. Pistes classées (aucune tranchée)

**P1 — investigation courte, faible risque**
1. Identifier la fonction réelle d'omniroute (1040 MB RAM, non documentée).
2. Mettre en place un monitoring de charge en série temporelle (actuellement
   absent, seul un instantané quotidien existe).

**P2 — exécution de décisions déjà rendues**
3. Finaliser l'exécution technique de la Phase 3 veille infrastructure (cron,
   canal Discord, gateway).
4. Finaliser l'exécution de l'extension veille externe + sandbox du
   2026-08-18 (prompt, cron hebdomadaire, peuplement effectif de
   `/root/sandbox-rd/`).
5. Vérifier le Bureau TUI en conditions réelles (SSH, charge, audio, multi-client).

**P3 — chantiers de fond**
6. Lever le bloquant `memory_enabled` pour l'isolation mémoire par sub-agent
   (condition du déploiement Karūbī).
7. Définir le SRS Hermes-native (format, extraction, révision, espacement).
8. Instruire les 3 questions d'applicabilité Cordis, en commençant par HMR
   agents Hermes (le chantier le plus concret et le mieux documenté des trois).

**P4 — hygiène**
9. Clarifier l'incohérence README/dossier des brouillons d'extension zodiacale.
10. Confirmer comportementalement la résolution de l'incident robustesse
    persona-LLM (reproduction contrôlée), au-delà de la seule vérification du
    hash.

---

## Rappel de méthode

Consignation et signalement uniquement — aucune exécution, aucun accès
credentials, aucune modification d'infrastructure effectuée dans cette passe
(Cmd 6, Cmd 12, Cmd 13).
