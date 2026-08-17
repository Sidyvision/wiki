---
title: "Activation du monitoring quotidien (cron) et correction HOME_CHANNEL — profil studio (2026-08-17)"
type: infrastructure
tags: [rd, infrastructure, hermes, discord, studio, phase-3, cron, monitoring]
created: 2026-08-17
updated: 2026-08-17
sources: []
links: ["[[atelier/rd/infrastructure/activation-salon-infrastructure-studio-2026-08-16]]", "[[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]]"]
---

# Activation du monitoring quotidien (cron) et correction HOME_CHANNEL — profil `studio`

> **Synthèse** : après l'extension du SOUL.md du profil `studio` (volet 1
> monitoring + volet 2 R&D, validée le 2026-08-16 par le gardien), deux
> incohérences ont été identifiées et corrigées le 2026-08-17 : (1) le
> `DISCORD_HOME_CHANNEL` pointait vers `#analog-wizard` au lieu de
> `#infrastructure` — les notifications de startup/shutdown arrivaient
> dans le mauvais salon ; (2) aucun cron job n'avait été créé pour le
> volet 1 du mandat (monitoring quotidien 12h00). Les deux corrections
> ont été appliquées ; le gateway studio est opérationnel, notifie
> correctement `#infrastructure`, et le cron est programmé.

## 1. Contexte

Le gardien a étendu le SOUL.md du profil `studio` le 2026-08-16 avec
deux volets distincts (session gardien du 16 août) :

- **Volet 1 — Monitoring quotidien** : exécution à 12h00 des 3 scripts
  déterministes (`verifier-invariants.py`,
  `generer-cartographie.py --verifier`, `detecter-non-tracke.py`) +
  empreinte serveur + registre Hermes-Terminal. Rapport 5 sections
  posté sur `#infrastructure`.
- **Volet 2 — Recherche & développement** : événementiel, pas
  quotidien. Lecture des nouvelles fiches déposées dans `rd/`,
  recherche internet proactive, rapprochement avec les frictions
  documentées, propositions d'optimisation.

Le prompt SOUL.md précisait : « Posted to `#infrastructure` (single
channel for both volets for now) ». Deux incohérences ont été
détectées le lendemain.

## 2. Anomalie 1 — HOME_CHANNEL mal configuré

**Symptôme** : les notifications de startup/shutdown du gateway studio
arrivaient dans `#analog-wizard` (`1535173127695241248`) au lieu de
`#infrastructure` (`1536564394690084925`).

**Diagnostic** : dans `/root/.hermes/profiles/studio/.env`, le
`DISCORD_HOME_CHANNEL` était fixé à `1535173127695241248` (salon
principal de l'agent studio pour son travail de son). Or le SOUL.md
dit explicitement que le canal de rapport infrastructure est
`#infrastructure`. Le HOME_CHANNEL sert de destination par défaut
pour les notifications de cycle de vie du gateway — il devait donc
être aligné sur le canal de rapport.

**Correction** :

```
# Avant
DISCORD_HOME_CHANNEL=1535173127695241248

# Après
DISCORD_HOME_CHANNEL=1536564394690084925
```

**Vérification** : après redémarrage du gateway (`hermes --profile
studio gateway restart`, PID 2011978, 04:54:16 UTC), le log confirme :

```
2026-08-17 04:54:22,253 INFO [...] Connected as HermesStudio#4408
2026-08-17 04:54:23,518 INFO [...] Sent home-channel startup notification to discord:1536564394690084925
```

La notification est bien arrivée sur `#infrastructure`.

## 3. Anomalie 2 — Aucun cron job pour le volet 1

**Symptôme** : `hermes --profile studio cron list` retournait « No
scheduled jobs ». Le volet 1 du SOUL.md prévoyait un cron quotidien
à 12h00, mais il n'avait jamais été créé.

**Correction** : création du cron job via l'outil de scheduling
Hermes :

| Paramètre | Valeur |
|---|---|
| Job ID | `b7acb57e3d58` |
| Nom | `monitoring-infrastructure-quotidien` |
| Schedule | `0 12 * * *` (midi UTC quotidien) |
| Repeat | forever |
| Deliver | `discord:1536564394690084925` (#infrastructure) |
| Workdir | `/root/wiki` |
| Toolsets | `terminal`, `file`, `read_file`, `execute_code` |

Le prompt du cron exécute dans l'ordre : (1) `verifier-invariants.py`,
(2) `generer-cartographie.py --verifier`, (3)
`detecter-non-tracke.py`, (4) empreinte serveur (RAM/disk/swap),
(5) registre Hermes-Terminal (bind-mount integrity, gateway health
des 12 profils, staleness de `_inbox/`), puis formate un rapport en
5 sections (conforme au SOUL.md §Volet 1).

Prochaine exécution : 2026-08-17 à 12:00 UTC.

## 4. État du volet 2 — Recherche & développement (option a validée)

Le volet 2 est défini dans le SOUL.md (mandat R&D événementiel).
Plutôt que de créer un cron séparé, l'option (a) a été validée par
Sidy le 2026-08-17 : intégrer la détection de nouvelles fiches dans
le prompt du cron quotidien existant.

### Mécanisme implémenté

**Script de détection** :
`atelier/rd/outillage/detecter-nouvelles-fiches-rd.sh` — compare un
snapshot horodaté de `atelier/rd/` avec l'état précédent (stocké
dans `atelier/rd/outillage/.snapshots-rd/`). Détecte :
- Fichiers nouveaux (présents aujourd'hui, absents hier)
- Fichiers modifiés (timestamp changé entre les deux runs)

Le script est exécuté par le cron quotidien **après** le volet 1.
Si la sortie est `aucune-nouvelle-fiche` → le rapport final n'a pas
de section R&D. Si des fiches sont listées → l'agent les lit, les
analyse, les rapproche du `registre-problemes.md`, et formule des
propositions d'optimisation (marquées PROPOSITION, jamais décision).

### Mise à jour du prompt cron

Le prompt du job `b7acb57e3d58` a été étendu (2026-08-17) pour
intégrer le volet 2 après le volet 1. Le rapport final passe de
5 à 6 sections : §1-§4 monitoring, §5 R&D (conditionnel), §6
Suggestions.

### Limites

- Le script détecte les modifications par timestamp, pas par contenu
  (un fichier édité sans changement de mtime ne sera pas vu — rare
  en pratique, les outils d'édition modernes mettent à jour le mtime).
- La recherche internet proactive n'est pas automatisée — signalée
  dans §6 Suggestions quand pertinente, exécutée sur demande.
- Le snapshot est initialisé au premier run (2026-08-17 12:00 UTC) —
  aucune détection avant le second run (2026-08-18 12:00 UTC).

## 5. État final après correction

| Élément | Valeur |
|---|---|
| Service | `hermes-gateway-studio.service`, `active (running)` (PID 2011978) |
| `DISCORD_HOME_CHANNEL` | `1536564394690084925` (#infrastructure) |
| Notification startup | Confirmée sur `#infrastructure` |
| Cron volet 1 | `b7acb57e3d58`, `0 12 * * *`, livrable #infrastructure |
| Cron volet 2 | Non créé (événementiel, non automatisé) |
| SOUL.md | Deux volets définis (monitoring + R&D) |
| Gouvernance | Discord-Validation : rapport signalé, Sidy valide avant action |

## 6. Leçons tirées

1. **Deux gestes distincts lors de l'extension d'un mandat agent** :
   - (a) Écrire le prompt dans le SOUL.md (fait par le gardien le 16 août).
   - (b) Configurer les variables Hermes qui en découlent
     (HOME_CHANNEL, cron jobs, workdir, toolsets) — omis lors de
     cette passe, corrigé le 17.

2. **HOME_CHANNEL ≠ canal de travail** : le salon principal de
   l'agent (`#analog-wizard` pour le studio) et le salon de rapport
   infrastructure (`#infrastructure`) sont distincts. Le HOME_CHANNEL
   du profil doit pointer vers le salon de rapport du volet actif,
   pas vers le salon de travail principal.

3. **Cron non créé ≠ cron oublié** : le gardien a proposé le plan
   (Cmd 6 : plan avant écriture), Sidy a validé, le prompt a été
   écrit — mais le cron Hermes lui-même n'a pas été programmé.
   Vérifier systématiquement qu'un `cron list` confirme la présence
   effective du job après toute proposition acceptée.

## 7. Points ouverts

- **Volet 2** : mécanisme de déclenchement à définir (cron
  événementiel, extension du prompt volet 1, ou appel manuel).
- **Mode free-response** dans `#infrastructure` : non activé —
  studio ne répond que sur @mention. Voir fiche précédente
  ([[atelier/rd/infrastructure/activation-salon-infrastructure-studio-2026-08-16|activation-salon-infrastructure-studio-2026-08-16]]).
- **Premier run cron** : 2026-08-17 à 12h00 UTC — vérifier que le
  rapport est bien formaté et livré sur `#infrastructure`.
