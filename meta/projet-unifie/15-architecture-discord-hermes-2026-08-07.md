---
title: "15 — Architecture Discord des 12 agents H‍ermes (2026-08-07)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, hermes, discord, runbook]
created: 2026-08-07
updated: 2026-08-07
---

# 15 — Architecture Discord des 12 agents H‍ermes (2026-08-07)

> **Pourquoi cette fiche existe** : toute la configuration Discord (tokens, salons,
> services système) vit **hors du dépôt git**, dans `/root/.hermes/profiles/*/` et dans
> des services systemd — donc **invisible** à toute session qui ne consulte le dépôt
> que via GitHub (ex. une session Claude.ai Code séparée). Sans cette fiche, aucune
> traçabilité de cette infrastructure en cas de souci technique. Cette fiche documente
> l'**architecture et les procédures**, jamais les secrets eux-mêmes.

---

## 1. Ce qui est versionné vs. ce qui ne l'est pas

| Élément | Emplacement | Versionné dans `wiki` ? |
|---|---|---|
| Prompts de rôle (doctrine) | `meta/projet-unifie/hermes-prompts/01-…12-…md` | ✅ Oui |
| `SOUL.md` de chaque profil | `/root/.hermes/profiles/<profil>/SOUL.md` | ❌ Non (copie verbatim locale du prompt versionné, §VIII.7) |
| `config.yaml` de chaque profil | `/root/.hermes/profiles/<profil>/config.yaml` | ❌ Non |
| `.env` (tokens Discord, clé API Anthropic) | `/root/.hermes/profiles/<profil>/.env` | ❌ Non — **jamais**, secrets |
| Services gateway | `systemd --user` : `hermes-gateway-<profil>.service` | ❌ Non (état machine) |
| Logs | `/root/.hermes/profiles/<profil>/logs/gateway.log` | ❌ Non |

**Règle de fond** : les prompts (contenu doctrinal, éditable et versionnable) vivent dans
le dépôt. La configuration d'exécution (secrets, état de service) vit sur la machine
locale et ne doit **jamais** être commitée (risque de fuite de tokens dans l'historique
Git, y compris après suppression du fichier).

---

## 2. Les 12 profils et leur salon Discord

Un serveur Discord privé unique héberge tous les agents. Chaque agent = une application
Discord distincte (bot séparé, token séparé — pas de token partagé entre profils).

| # | Profil H‍ermes | Rôle (prompt source) | Salon(s) Discord |
|---|---|---|---|
| 01 | `ar-music` | Direction artistique musicale | `#marketing` |
| 02 | `visual-da` | Direction artistique visuelle (+ technique image, cf. commit `0d96231`) | `#analog-wizard` |
| 03 | `production` | Gestion de production | `#marketing` |
| 04 | `admin-legal` | Administratif / juridique | `#administratif` |
| 05 | `accounting` | Comptabilité | `#administratif` |
| 06 | `distribution` | Distribution | `#marketing` |
| 07 | `marketing` | Marketing / communication | `#marketing` + `#inspiration` |
| 08 | `publication` | Publication / site | `#marketing` |
| 09 | `studio` | Ingénieur son / studio | `#analog-wizard` |
| 10 | `gardien` | Vigie transversale (accès `meta/`) | `#gardien` |
| 11 | `fanzine` | Édition fanzine | `#marketing` |
| 12 | `commerce` | Commerce / rentabilité | `#administratif` |

**Free-response activé pour les 12 agents** (2026-08-07) : chaque agent répond sans
nécessiter de `@mention` dans son/ses salon(s) désigné(s) (`DISCORD_FREE_RESPONSE_CHANNELS`).

**Étanchéité** : allowlist stricte par utilisateur (`DISCORD_ALLOWED_USERS`) et par salon
(`DISCORD_ALLOWED_CHANNELS`) — silence total pour DM ou salon non listé, conformément à
CLAUDE.md §VIII.8.

---

## 3. Salon `#inspiration` — mécanisme de dépôt vers `raw/`

Le salon `#inspiration` est surveillé par le profil `marketing` uniquement. Deux modes
observés en usage réel (2026-08-07/08) :

- **Dépôt passif prévu à l'origine** (skill `raw-deposit`) : contenu déposé tel quel dans
  `raw/`, sans analyse ni éditorialisation — verrouillé tant que la condition des 3 cycles
  `_inbox/` sans anomalie (§VIII.9) n'est pas remplie.
- **Écart accepté en pratique (« Option A », validé par Sidy le 2026-08-07/08)** : l'agent
  `marketing` peut produire directement une fiche structurée dans `_inbox/` (avec
  frontmatter, questions ouvertes) à partir d'une description verbale, **à condition** que
  la pièce source immuable (photo, fichier) soit déposée séparément dans `raw/assets/`
  après validation humaine. Cette dérogation est documentée, délibérée, et ne doit pas être
  « corrigée » sans nouvelle décision explicite de Sidy.

---

## 4. Procédure de configuration (pour toute reprise/dépannage futur)

1. **Ne jamais utiliser `hermes gateway setup`** pour un déploiement multi-profils — bug
   connu de croisement de tokens entre profils (observé 2 fois). Toujours éditer le `.env`
   à la main.
2. Éditer `/root/.hermes/profiles/<profil>/.env` avec :
   - `DISCORD_BOT_TOKEN` (jamais dans `config.yaml`)
   - `DISCORD_ALLOWED_USERS` (IDs numériques, fail-closed)
   - `DISCORD_ALLOWED_CHANNELS`
   - `DISCORD_FREE_RESPONSE_CHANNELS` (réponse sans mention)
   - `DISCORD_HOME_CHANNEL` (cible des messages cron)
3. `chmod 600` systématique sur chaque `.env`.
4. `hermes -p <profil> gateway install` puis `gateway restart`.
5. **Vérification obligatoire** avant de considérer un profil « connecté » :
   `grep "Connected as" /root/.hermes/profiles/<profil>/logs/gateway.log`
   — ne jamais faire confiance à l'absence d'erreur seule.
6. Erreur fréquente : `PrivilegedIntentsRequired` — signifie que « Message Content Intent »
   n'est pas activé/sauvegardé dans le Developer Portal Discord pour cette application.
   Fix : réactiver + sauvegarder le toggle côté Discord, puis `gateway restart`.

---

## 5. État connu au 2026-08-07 (pour référence, peut devenir obsolète)

- **Clé API Anthropic partagée** entre les 12 profils (`sk-ant-api03-…`) — a atteint son
  plafond de crédit le 2026-08-07 (`HTTP 400: Your credit balance is too low`). Non résolu :
  Sidy prévoit de créer une clé liée à son plan personnel (console.anthropic.com) pour
  remplacer la clé partagée. **Vérifier `logs/errors.log` de chaque profil en cas de
  panne apparente d'un agent — c'est la première cause à exclure.**
- **Cloisonnement filesystem** : aucun mécanisme de sandboxing actif (voir levier natifs
  possibles côté H‍ermes — non documentés ici, décision de durcissement différée
  volontairement par Sidy après retour d'expérience réel sur Discord).
- **Canaux non encore activés** : Telegram, WhatsApp (Discord seul est en production).

---

## 6. À mettre à jour

Cette fiche doit être révisée à chaque changement structurel : nouveau profil, nouveau
salon, changement de clé API, activation d'un nouveau canal (Telegram/WhatsApp), ou
changement de politique de cloisonnement. Elle est la référence canonique pour toute
session (y compris Claude.ai Code via GitHub) qui a besoin de comprendre l'infrastructure
d'exécution des agents sans avoir accès à `/root/.hermes/`.
