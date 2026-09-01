# 10 — Briefing : Infrastructure globale Hermes Agent

**Date :** 2026-07-03
**Statut :** Architecture cible — en attente du prérequis Qwen3.6-27B-FP8 (briefing 09)
**Périmètre :** Consolidation de l'infrastructure autour de Hermes Agent (Nous Research, open source MIT), incluant l'usage iPhone (WhatsApp prioritaire, Discord), l'automatisation `_inbox/`, l'extension potentielle à `raw/`, et l'ouverture d'une dimension personnelle/récréative.

---

## 1. Contexte et motivation

La séparation actuelle Claude.ai (assistance/décision) ↔ Claude Code sur Hetzner (exécution mécanique) s'est imposée **par contrainte économique**, pas par principe architectural. Hermes Agent permet de :

1. **Réduire les coûts** : le travail mécanique (`_inbox/`, potentiellement `raw/`) bascule sur Qwen3.6-27B-FP8 auto-hébergé (RunPod), zéro appel API payant.
2. **Unifier l'accès** : un seul agent joignable depuis iPhone (WhatsApp, Discord), iPad (CLI via Termius, webui via Hermex), et serveur.
3. **Capitaliser** : mémoire persistante (SQLite/FTS5 + `MEMORY.md`) et skills auto-générées — le protocole INGEST devient une skill invocable au lieu d'être réexpliqué à chaque session.
4. **Ouvrir une dimension personnelle/récréative** dans un espace isolé du corpus doctrinal.

**Principe conservé** : la frontière assistance/exécution ne disparaît pas — elle est recréée *à l'intérieur* de Hermes via l'isolation des contextes (voir §4).

---

## 2. Architecture cible

```
┌─────────────────────────────────────────────────────────┐
│                     iPhone 16 Pro Max                    │
│  WhatsApp ──┐   Discord ──┐   Hermex (client natif) ──┐  │
└─────────────┼─────────────┼────────────────────────────┼──┘
              │             │                            │
              ▼             ▼                            ▼
┌─────────────────────────────────────────────────────────┐
│              Hetzner (root@Wiki) — HÔTE HERMES           │
│                                                          │
│  hermes gateway (systemd) ── un seul processus :         │
│    • adaptateur WhatsApp (bridge Baileys, Node.js)       │
│    • adaptateur Discord (bot token)                      │
│    • cron scheduler (tick 60s)                           │
│    • hermes-webui (pour Hermex, via Tailscale)           │
│                                                          │
│  hermes agent :                                          │
│    • mémoire : SQLite FTS5 + MEMORY.md                   │
│    • skills : ~/.hermes/skills/ (dont skill INGEST)      │
│    • workspace wiki : clone Sidyvision/wiki.git          │
│                                                          │
│  Claude Code (conservé en Phase 1-2, retiré ensuite      │
│  si Hermes valide les tests de régression)               │
└──────────────────────┬───────────────────────────────────┘
                       │ tunnel SSH (pattern briefing 09)
                       ▼
┌─────────────────────────────────────────────────────────┐
│           RunPod — Qwen3.6-27B-FP8 via vLLM              │
│     endpoint OpenAI-compatible (v0.19.1 épinglé)         │
└──────────────────────────────────────────────────────────┘

     iPad (inchangé) : Obsidian + Working Copy + Termius
     Claude.ai (inchangé) : assistance, décisions, doctrine
```

**Répartition des rôles :**

| Surface | Rôle |
|---|---|
| **Claude.ai (Projet)** | Assistance, arbitrages, production doctrinale, architecture — inchangé |
| **Hermes @ Hetzner** | Exécution mécanique : intégration `_inbox/`, cron, automatisations, dimension personnelle |
| **Qwen @ RunPod** | Moteur d'inférence de Hermes (aucun accès direct) |
| **WhatsApp** | Canal conversationnel principal mobile (rapide, vocal, quotidien) |
| **Discord** | Canal structuré : canaux par domaine, boutons de validation, commandes slash |
| **Hermex (iOS)** | Cockpit : sessions multiples, fichiers, supervision fine |
| **iPad** | Rédaction Obsidian, revue des fiches — inchangé |

---

## 3. Composants et configuration

### 3.1 Hôte Hermes : serveur Hetzner

Installation en une commande (`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`) — installe uv, Python 3.11, et le dépôt sous `~/.hermes/`. Node.js v18+ requis pour le bridge WhatsApp (géré par l'installeur).

Configuration modèle : pointer sur l'endpoint vLLM RunPod (OpenAI-compatible) via `hermes model` → « your own endpoint ». Le tunnel SSH Hetzner→RunPod du briefing 09 reste le pattern de connexion. **Attention** : le port SSH externe RunPod change à chaque redémarrage — le script de reconnexion du tunnel doit être paramétrable ou régénéré.

Gateway en service système : `sudo hermes gateway install --system` (survit aux reboots, indépendant de toute session utilisateur).

Diagnostic : `hermes doctor`, logs sous `~/.hermes/logs/gateway.log`, commande `/platform list` pour l'état des adaptateurs (circuit breaker par plateforme en cas de panne amont).

### 3.2 WhatsApp (canal principal)

**Mécanisme** : bridge Baileys intégré — émule une session WhatsApp Web, appairage par QR code (`hermes gateway setup` → WhatsApp, ou `hermes whatsapp`). Pas de compte Meta Business, pas de frais API. Session persistante sous `~/.hermes/platforms/whatsapp/session` (survit aux redémarrages, pas de re-scan).

**⚠️ Décision requise — deux modes :**

| Mode | Fonctionnement | Risque |
|---|---|---|
| **Numéro dédié (recommandé)** | Un second numéro (eSIM data-only, SIM prépayée) porte le bot ; vous lui écrivez comme à un contact | Isole votre compte personnel |
| **Numéro personnel** | Vous vous écrivez à vous-même | ⚠️ Baileys est un client non officiel ; Meta peut restreindre les comptes en cas d'usage automatisé intensif |

La documentation est explicite : utiliser un numéro dédié, garder un usage conversationnel, jamais d'envoi sortant automatisé vers des contacts qui n'ont pas écrit d'abord. **L'iPhone 16 Pro Max supporte la double eSIM** — une eSIM data/numéro secondaire résout ce point proprement.

**Verrouillage de sécurité (obligatoire avant mise en service) :**

```bash
# ~/.hermes/.env
WHATSAPP_ALLOWED_USERS=336XXXXXXXXX   # votre numéro, indicatif pays, sans le +
```

```yaml
# ~/.hermes/config.yaml
whatsapp:
  unauthorized_dm_behavior: ignore    # silence total pour les inconnus
  reply_prefix: ""                    # supprime le préfixe "⚕ Hermes Agent"
```

```bash
chmod 700 ~/.hermes/platforms/whatsapp/session   # credentials = mot de passe
```

Sans allowlist, la gateway refuse tout message entrant par défaut (comportement sain).

**Capacités** : messages vocaux entrants transcrits automatiquement (faster-whisper local possible — cohérent avec l'éthique auto-hébergée, aucune clé API), réponses en streaming (édition du message en temps réel), envoi/réception de fichiers et d'images. Les protocoles WhatsApp Web changent périodiquement et peuvent casser le bridge — le réflexe est alors `hermes update` + re-pairing.

### 3.3 Discord (canal structuré)

**Mécanisme** : bot classique via le Discord Developer Portal — créer l'application, activer **Message Content Intent** (Privileged Gateway Intents — cause n°1 de bot muet si oublié), copier le token, inviter le bot sur un serveur privé.

**Intérêt spécifique pour votre usage :**

1. **Canaux par domaine** : un serveur Discord privé avec `#wiki-ingest`, `#infra`, `#instrument-3d`, `#personnel` — chaque canal est une session distincte. C'est la matérialisation visible de la séparation des domaines.
2. **`DISCORD_FREE_RESPONSE_CHANNELS`** : dans les canaux listés, Hermes répond sans être mentionné — conversation fluide dans les canaux dédiés.
3. **Boutons de clarification** : quand l'agent appelle l'outil `clarify` (choix d'approche, validation avant décision non triviale), Discord affiche un bouton par option. **C'est le mécanisme qui implémente votre règle « jamais d'acceptation automatique »** : la skill INGEST sera écrite pour appeler `clarify` avant tout `git push`, et vous validez d'un tap depuis l'iPhone.
4. **Commandes slash automatiques** : toute skill installée devient une commande `/` Discord au redémarrage de la gateway — `/ingest` invocable directement.
5. **Uploads natifs** : l'agent peut envoyer les fiches produites directement dans le canal pour relecture avant intégration.
6. **Canaux vocaux** : conversation vocale temps réel avec transcription — la dimension récréative peut passer par là.

### 3.4 Clients iOS

| App | Coût | Usage |
|---|---|---|
| **WhatsApp / Discord natifs** | — | Interaction quotidienne (via gateway) |
| **Hermex** (MIT, open source) | Gratuit | Cockpit : sessions multiples, streaming, fichiers ; se connecte à `hermes-webui` via **Tailscale** (réseau WireGuard privé, aucun port ouvert) ou Cloudflare Tunnel ; URL serveur dans le Keychain iOS ; aucun tracking |
| **HermesPilot** | 9,99 $ à vie | Option ultérieure si besoin : approbations en app, Live Activity, sync desktop |

**Recommandation** : WhatsApp + Discord pour le quotidien, Hermex pour la supervision. Tailscale à installer sur Hetzner + iPhone (déjà pertinent aussi pour sécuriser l'accès Termius).

---

## 4. Isolation des domaines (transposition de la séparation des canaux)

La séparation Claude.ai/Claude Code empêchait la contamination entre assistance et exécution. À l'intérieur de Hermes, cette frontière est recréée par trois mécanismes cumulés :

1. **Sessions par plateforme/canal** : les sessions ne se partagent pas entre canaux Discord ni entre plateformes — `#wiki-ingest` et `#personnel` sont des contextes distincts par construction.
2. **Sub-agents isolés** : pour les pipelines (ex. traitement `raw/`), Hermes lance des sub-agents à contexte et outillage propres, sans pollution du contexte principal.
3. **Discipline de la mémoire** : `MEMORY.md` est agent-curé mais lisible et éditable — revue périodique pour vérifier qu'aucune inférence doctrinale non validée ne s'y glisse. La mémoire de Hermes est **opérationnelle** (préférences, procédures, état des projets), jamais **doctrinale**. Le wiki reste l'unique dépositaire du doctrinal ; Commandement 3 et vigilance apophatique s'appliquent au contenu que Hermes *écrit*, pas seulement à ce qu'il retient.

**Règle d'or inchangée (verdict Ornith, étendue à Hermes)** : fiabilité narrative ≠ fiabilité d'action. Tout cycle d'intégration se conclut par le script `compare` indépendant, jamais par l'auto-évaluation de l'agent. La skill INGEST doit inclure l'exécution de `compare` comme étape terminale obligatoire, avec rapport du résultat brut.

---

## 5. Skill INGEST (spécification cible)

La skill encode le protocole existant :

```
1. Lire UPDATES.md dans _inbox/
2. Pour chaque fichier listé : vérifier frontmatter YAML
   (statut, type de fiche), destination selon CLAUDE.md
3. clarify → présenter le plan d'intégration (boutons Discord) → ATTENDRE validation
4. Déplacer les fichiers, mettre à jour index.md et annales.md (append-only)
5. Exécuter le script compare → rapporter le résultat BRUT
6. clarify → validation finale avant git commit + push
```

Étapes 3 et 6 = points de validation humaine non contournables. La skill s'améliore à l'usage (mécanisme natif Hermes), mais **toute modification de la skill elle-même est relue avant d'être acceptée** — les skills sont des fichiers Markdown sous `~/.hermes/skills/`, versionnables dans un dépôt Git dédié pour audit.

**Extension `raw/` (Phase 6, conditionnelle)** : uniquement après validation de la skill INGEST sur au moins 3 cycles sans anomalie au `compare`. Le traitement de `raw/` produit des fiches candidates dans `_inbox/` (jamais d'écriture directe dans le wiki), qui repassent ensuite par le circuit INGEST standard. La chaîne reste : `raw/` → analyse Hermes → `_inbox/` + `UPDATES.md` → validation → intégration.

---

## 6. Dimension personnelle et récréative

Espace dédié, hermétique au corpus doctrinal :

- **Canal** : `#personnel` sur Discord et/ou conversation WhatsApp — sessions distinctes des canaux wiki.
- **Cron en langage naturel** : briefing matinal (météo, actualités choisies), rappels, résumés hebdomadaires livrés sur WhatsApp.
- **Vocal** : messages vocaux WhatsApp transcrits/répondus ; canal vocal Discord pour conversation temps réel.
- **Outils créatifs** : génération d'images et TTS disponibles via le Tool Gateway (Nous Portal, optionnel/payant) ou des alternatives auto-hébergées à évaluer — décision non bloquante, à prendre à l'usage.
- **Mémoire personnelle** : Hermes construit un modèle de vos préférences au fil de l'eau — c'est ici que le « grows with you » prend son sens sans toucher au wiki.

---

## 7. Ordre des opérations

| Phase | Contenu | Critère de sortie |
|---|---|---|
| **0** (en cours) | Déploiement Qwen3.6-27B-FP8 sur RunPod (briefing 09, étapes A–J) | Endpoint vLLM répond, test de régression OK |
| **1** | Installation Hermes sur Hetzner, `hermes model` → endpoint RunPod, validation en CLI pur (pas de gateway) | Conversations CLI stables, `hermes doctor` propre |
| **2** | Tailscale (Hetzner + iPhone), `hermes-webui`, Hermex | Accès mobile supervisé fonctionnel |
| **3** | WhatsApp : obtenir numéro dédié (eSIM), pairing QR, allowlist, `unauthorized_dm_behavior: ignore`, gateway en systemd | Conversation WhatsApp stable sur 48h |
| **4** | Discord : bot, Message Content Intent, serveur privé, canaux par domaine, `DISCORD_FREE_RESPONSE_CHANNELS` | Boutons `clarify` fonctionnels |
| **5** | Skill INGEST : écriture, test sur un `_inbox/` réel **en parallèle de Claude Code** (double exécution, comparaison des résultats) | 3 cycles sans divergence au `compare` |
| **6** | Bascule : Claude Code retiré du circuit INGEST ; pilote `raw/` | `compare` propre sur `raw/` → `_inbox/` |
| **7** | Dimension personnelle : cron, briefings, vocal, mémoire personnelle | À l'usage |

Chaque phase est indépendamment réversible. La Phase 5 en double exécution est le test de régression décisif — même méthodologie que pour Ornith.

---

## 8. Points de vigilance consolidés

1. **WhatsApp/Baileys est non officiel** : numéro dédié obligatoire, usage conversationnel, jamais de sortant automatisé non sollicité. Les mises à jour du protocole WhatsApp peuvent casser le bridge → `hermes update` + re-pairing.
2. **Session WhatsApp = credentials complets** : `chmod 700`, jamais dans Git, jamais partagée.
3. **Message Content Intent Discord** : à activer dans le Developer Portal, sinon bot muet.
4. **Port SSH RunPod volatil** : le tunnel Hetzner→RunPod doit être reconfiguré à chaque restart du Pod (règle briefing 09 inchangée).
5. **Mémoire et skills de Hermes sont des surfaces d'audit** : revue périodique de `MEMORY.md` et diff des skills avant acceptation des auto-améliorations.
6. **Le script `compare` reste le juge de paix** — pour Hermes comme pour tout agent.
7. **Coût RunPod** : Hermes en gateway permanente n'appelle le modèle que sur message/cron — mais le Pod RunPod, lui, facture tant qu'il tourne. Évaluer à l'usage : Pod à la demande vs. permanent vs. migration ultérieure vers du serverless (le modèle 27B tient sur une carte modeste).
8. **Vigilance documentaire** (protocole habituel) : à la clôture de la mise en place, mettre à jour `03-transition-modele-open-source.md`, `04-sessions-par-fonction-et-backlogs.md` et `briefing-claude-ai.md` pour refléter la nouvelle architecture.

---

## 9. Ce qui ne change pas

- **Claude.ai** reste le canal d'assistance, d'arbitrage et de production doctrinale (ce projet).
- **Le wiki** reste l'unique source de vérité doctrinale ; Commandement 3, vigilance apophatique, discipline `to-source`, consultation de la bibliothèque physique : intégralement en vigueur.
- **L'arbitrage final appartient à Sidy** — Hermes ne prononce aucun verdict de discernement, n'intègre rien sans validation `clarify`, et ne touche jamais à `annales.md` autrement qu'en append.
- **iPad + Obsidian + Working Copy** : flux de rédaction et de synchronisation inchangé.
