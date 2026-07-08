---
title: "Note d'optimisation — préparation de l'intégration Hermes Agent (2026-07-03)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, hermes, qwen, decisions]
created: 2026-07-03
updated: 2026-07-08
---

# Note d'optimisation — vers l'intégration Hermes

> Complément au briefing `10-briefing-infrastructure-hermes-agent-2026-07-03.md`, à la lumière de
> la session de déploiement Qwen du 2026-07-03. La Phase 0 du briefing 10 est **terminée** (endpoint
> vLLM opérationnel + double test de régression réussi). Cette note consigne ce qui est acquis, un
> point structurel favorable à Hermes, et **trois décisions ouvertes** à trancher avant la Phase 1.

## 1. Phase 0 : critère de sortie atteint

Le briefing 10 conditionnait tout à « endpoint vLLM répond, test de régression OK ». C'est fait :
- Endpoint `Qwen/Qwen3.6-27B-FP8` opérationnel (A100 PCIe, vLLM 0.19.1).
- Régression atelier **8 ✓ / 0 ✗**, doctrinal **12 ✓ / 0 ✗** (détail : `11-…`).

La voie est ouverte pour la **Phase 1** (installation Hermes sur Hetzner, `hermes model` pointant
l'endpoint RunPod, validation en CLI pur).

## 2. Point structurel favorable : Hermes échappe au bug Claude Code

La session a buté sur la **régression Claude Code ≥ 2.1.154** (injection de `role:"system"` dans
`messages[]`, rejetée par l'endpoint Anthropic `/v1/messages` de vLLM ; cf. `11-…` §3.2). Corrigée
par un pin à 2.1.150.

**Hermes n'est pas concerné** : il dialogue avec vLLM via l'endpoint **OpenAI-compatible**
(`/v1/chat/completions`), nettement plus mature que l'endpoint Anthropic. Conséquences :
- Le pin Claude Code à 2.1.150 est un correctif **transitoire**, limité aux Phases 1-5 (double
  exécution Claude Code ∥ Hermes). Il disparaît à la bascule Phase 6.
- L'endpoint OpenAI étant le chemin nominal de Hermes, la compatibilité tool-use / streaming y est
  a priori plus robuste — à confirmer lors de la validation CLI de la Phase 1.

## 3. Trois décisions ouvertes avant la Phase 1

### 3.1 GPU cible : A100 (1,40 $/h) vs A6000 (0,50 $/h)

L'A100 a été choisi le 2026-07-03 pour **écarter l'hypothèse matérielle** pendant le diagnostic —
hypothèse qui s'est révélée fausse (le coupable était le template, cf. `11-…` / `09-v3`). Le FP8 de
31 Go **tient sur un A6000 48 Go** avec marge pour le cache KV à `--max-model-len 131072`.

- Pour un usage **ponctuel supervisé** (Claude Code aujourd'hui) : peu importe, on stoppe le Pod
  entre sessions.
- Pour Hermes en **gateway** : le choix du GPU pèse directement sur le coût récurrent (voir 3.2).

**RECOMMANDATION INFIRME** (2026-07-08) : le compte-rendu
`14-compte-rendu-redeploiement-qwen-2026-07-08.md` §1.3 a démontré que l'A6000 (48 Go)
ne convient pas à Qwen3.6-27B-FP8 dans une configuration utilisable en production
(OOM même à `--max-model-len 65536`). **L'A100 (80 Go) reste la seule carte validée.**
Piste de repli non testée : quantifier le cache KV (`--kv-cache-dtype fp8`) pour réduire
l'empreinte mémoire sur A6000.

### 3.2 Mode d'hébergement : Pod à la demande vs Pod permanent vs Serverless

C'est **la** question de coût de la Phase 3 (gateway systemd). Une gateway permanente n'appelle le
modèle que sur message/cron, **mais le Pod RunPod facture tant qu'il tourne** :
- A6000 permanent : ~0,50 $/h ≈ **360 $/mois**.
- A100 permanent : ~1,40 $/h ≈ **1 000 $/mois**.

Trois options :

| Option | Principe | Avantage | Limite |
|---|---|---|---|
| **Pod à la demande** | Script start/stop autour des sessions | Coût minimal | Latence de démarrage ; incompatible avec cron/gateway 24-7 |
| **Pod permanent** | Pod A6000 tournant en continu | Réactivité immédiate | ~360 $/mois même à faible usage |
| **Serverless** | Endpoint scale-to-zero, facturé à l'inférence | Pas de coût à vide ; **supprime le piège du port SSH volatil** (vigilance n°4 du briefing 10) | Cold start ; à re-tester (écarté en juin car sans SSH) |

**Point neuf** : le Serverless avait été écarté en juin **parce qu'il n'offre pas de tunnel SSH** —
or Claude Code en avait besoin. **Hermes, lui, n'a besoin que d'un endpoint HTTPS authentifié**, pas
d'un tunnel. Le Serverless redevient donc un **candidat sérieux pour la Phase 3**, avec un double
bénéfice : coût à vide nul + disparition de la reconfiguration du tunnel à chaque restart. À tester
spécifiquement avant de figer l'architecture de la gateway.

**Recommandation** : Phases 1-2 sur Pod à la demande (A6000) ; évaluer le Serverless dès la Phase 3.

### 3.3 Timing du lancement de la Phase 1

Rien ne bloque techniquement le démarrage de la Phase 1. Deux préalables de confort :
- Écrire le **script de tunnel paramétrable** demandé au §3.1 du briefing 10 (voir §4 ci-dessous) —
  utile tant que Claude Code reste dans le circuit (Phases 1-5).
- Décider 3.1 et 3.2 au moins provisoirement, pour ne pas installer Hermes sur une cible qui
  changera.

## 4. Optimisation concrète immédiate : script de tunnel

Le briefing 10 (§3.1) demande un script de reconnexion du tunnel paramétrable (le port RunPod
change à chaque restart). À écrire côté Hetzner, p. ex. `tunnel-runpod.sh <IP> <PORT>` qui tue
l'ancien tunnel `-L 8000` et remonte le nouveau. Utile immédiatement pour Claude Code, réutilisable
pour la connexion CLI de Hermes en Phase 1. (Spécification uniquement ici — l'écriture du script
relève de Claude Code, pas d'une écriture directe au dépôt.)

## 5. Ce qui ne change pas

- **Claude.ai** reste le canal d'assistance / arbitrage / production doctrinale.
- **Le script `compare` reste le juge de paix**, pour Hermes comme pour Claude Code.
- **L'arbitrage final appartient à Sidy** ; Hermes n'intègre rien sans validation `clarify`, ne
  touche `annales.md` qu'en append, ne prononce aucun verdict de discernement.
- **Règle d'or** (verdict Ornith, étendue à Hermes) : fiabilité narrative ≠ fiabilité d'action.
