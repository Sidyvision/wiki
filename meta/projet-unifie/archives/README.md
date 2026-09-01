---
title: "Archives du projet unifié — jalons datés"
type: meta
tags: [outillage, projet-claude-ai, archives, jalons]
created: 2026-09-01
updated: 2026-09-01
---

# Archives du projet unifié

> **Régime de lecture : chaque pièce ici ne décrit que son jour.** Ce sont des
> photographies — runbooks tels qu'on les a suivis, résultats tels qu'on les a mesurés,
> procédures telles qu'on les a exécutées. Elles gardent leur valeur de trace et de mesure ;
> **aucune ne dit l'état courant**, et plusieurs le contredisent aujourd'hui.
>
> Pour l'état courant : `01-contexte-demarche-etat.md` §3, et
> [[atelier/rd/registre-chantiers]] pour les chantiers.
>
> **On ne retouche pas un jalon** (Cmd 10). On en ouvre un nouveau.

Dossier constitué le 2026-09-01 en réorganisant le dossier d'amorçage : ces pièces vivaient
jusque-là à plat, mêlées aux documents de pilotage, ce qui les faisait lire comme s'ils
étaient courants.

## Transition du moteur — tests Ornith puis Qwen (2026-06-28 → 07-08)

| Pièce | Ce qu'elle établit |
|---|---|
| `05-runbook-test-ornith-gpu-cloud.md` | la procédure pas à pas du premier test sur GPU loué à l'heure |
| `06-compte-rendu-test-ornith-gpu-cloud-2026-06-29.md` | premier test réel : résultats, correctifs, une anomalie à reproduire |
| `07-resultats-finaux-test-ornith-prepare-compare-2026-06-29.md` | cycle complet, verdict 8 ✓ / 0 ✗, et la nuance **fiabilité d'action ≠ fiabilité narrative** |
| `08-resultats-test-ornith-cas-doctrinal-2026-06-29.md` | cas doctrinal, 12 ✓ / 0 ✗ au 2ᵉ run ; leçon : **découper les lots doctrinaux fiche par fiche** |
| `09-briefing-transition-qwen36-27b-*.md` (v1, v2, v3) | transition Ornith → Qwen3.6-27B-FP8 : bilan, diagnostic de cause racine, puis procédure validée en production |
| `11-resultats-qwen36-27b-2026-07-03.md` | déploiement Qwen opérationnel, double verdict |
| `14-compte-rendu-redeploiement-qwen-2026-07-08.md` | re-déploiement sur RunPod |

**Ce qui en reste vrai** : les leçons de méthode (jamais d'auto-accept ; toujours clore par
une vérification mécanique indépendante ; limiter la durée des sessions ; découper les lots
doctrinaux). **Ce qui est caduc** : les modèles nommés et le dimensionnement — l'inférence
passe aujourd'hui par des fournisseurs tiers (bascule OmniRoute du 2026-08-26).

## Infrastructure et agents Hermes (2026-07-03 → 08-09)

| Pièce | Ce qu'elle établit |
|---|---|
| `10-briefing-infrastructure-hermes-agent-2026-07-03.md` | l'infrastructure agentique visée |
| `12-procedure-installation-hermes-phase1-2026-07-03.md` | procédure d'installation, **dépréciée** par la suivante |
| `13-pivot-haiku-installation-hermes-phase1-2026-07-07.md` | pivot du moteur et procédure révisée |
| `15-architecture-discord-hermes-2026-08-07.md` | les douze agents sur Discord : salons, identifiants, traçabilité |
| `16-mise-en-regard-theme-natal-roue-agents-2026-08-08.md` | mise en regard du thème natal vérifié et de la roue zodiacale des rôles |
| `17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md` | le chantier des douze agents et sa calibration |

## Session du 2026-08-23 — mémoire persistante et ressources

| Pièce | Ce qu'elle établit |
|---|---|
| `rapport-rd-memoire-persistante.md` | l'incident de mémoire persistante Hermes, son diagnostic et sa résolution |
| `synthese-ressources-deployees.md` | l'inventaire des ressources déployées ce jour-là |
| `plan-action-soutien-sidy.md` | le plan d'action personnel et professionnel |

Ces trois pièces ont été **versées au Domaine Réservé le 2026-09-01** depuis
`atelier/rd/`, où elles vivaient dans une page neutre alors qu'elles portent du fait
personnel (§VI). Leur versant publiable est écrit en propre côté `atelier/rd/` et indexé
là-bas. ⚠️ Elles déclarent des jobs cron créés — **vérification faite le 2026-09-01, aucun
des trois n'existe** dans les quatorze profils Hermes ; voir l'entrée `[2026-09-01]` de
[[atelier/rd/cahiers/registre-problemes]].

## Amont du projet (2026-05 → 06)

| Pièce | Ce qu'elle établit |
|---|---|
| `chatgpt-export-2026-05-10.md` | la notice de l'export de données ChatGPT, matière première du dépôt |
| `triage-chatgpt-export.md` | le classement proposé des 140 conversations |
| `briefing-claude-ai.md` | le briefing de passation serveur → iPad, d'avant la fusion des deux projets |
