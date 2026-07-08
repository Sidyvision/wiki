---
title: "14 — Compte-rendu : Re-déploiement Qwen3.6-27B-FP8 sur RunPod (2026-07-08)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, qwen, vllm, gpu-cloud, runbook, compte-rendu]
created: 2026-07-08
updated: 2026-07-08
---

# 14 — Compte-rendu : Re-déploiement Qwen3.6-27B-FP8 sur RunPod (2026-07-08)

> Session menée dans la nuit du 7 au 8 juillet, en parallèle du pivot Haiku (`13-…md`) : l'objectif
> était de rejouer intégralement la procédure du briefing 09 (déploiement Pod, connexion Claude
> Code, tests de non-régression) afin de disposer d'un point de comparaison direct avec Haiku,
> évalué séparément. **Résultat : succès, verdicts identiques au 2026-07-03** (atelier 8✓/0✗,
> doctrinal 12✓/0✗), mais avec plusieurs incidents en cours de route qui enrichissent les règles
> RunPod consolidées de `09-…v3.md` §4.

---

## 1. Chronologie des incidents

### 1.1 A100 PCIe hors capacité
Au moment de redémarrer le Pod existant, l'A100 PCIe était indiqué **« out of capacity »** —
fluctuation normale de la disponibilité RunPod, sans lien avec la config. Décision prise de
basculer temporairement sur A6000 (48 Go), ce qui a eu le mérite de tester en pratique une
hypothèse jusque-là non vérifiée (voir §2).

### 1.2 Écran d'édition du Pod vide / « template not found »
En tentant de rééditer un Pod existant (arrêté) pour changer sa configuration, deux symptômes
successifs :
- Les champs de l'écran d'édition sont apparus **vides**, alors que le Pod avait été déployé avec
  une config Custom complète.
- Le clic sur Deploy a ensuite renvoyé **« Template not found »**.

**Diagnostic** : RunPod semble référencer en interne un objet « template » même pour un
déploiement Custom ; si le Pod édité est dans un état incohérent, cette référence casse.

**Règle retenue** : ne pas tenter de rééditer un Pod dans cet état. **Terminer le Pod cassé et
redéployer entièrement depuis « + Deploy »**, jamais depuis un écran d'édition/reprise lié à un
Pod existant douteux.

### 1.3 OOM sur A6000, à deux réglages différents
Avec `--max-model-len 65536` (déjà réduit depuis 131072) :
- `--gpu-memory-utilization 0.90` → `torch.OutOfMemoryError`, ~46,27 Go utilisés sur 47,43 Go.
- `--gpu-memory-utilization 0.85` → **échec au même point, à quelques Mo près** (46,27 Go).

**Interprétation** : si `gpu_memory_utilization` bornait réellement l'usage total, l'échec à 0,85
aurait dû survenir plus tôt (théoriquement ~40,3 Go). Le fait que les deux réglages échouent au
même niveau, très proche du plafond physique de la carte, indique que **les poids du modèle
(~31 Go FP8) + l'overhead fixe (contexte CUDA, profiling des activations) occupent déjà la quasi-
totalité des 48 Go**, quel que soit ce réglage — celui-ci n'agit que sur le dimensionnement du
cache KV calculé lors du profiling, pas sur un plafond dur réellement respecté à l'allocation.

**Conclusion empirique retenue** (met à jour §3.1 de `note-optimisation-hermes-2026-07-03.md`,
qui recommandait un retour à l'A6000 sans l'avoir testé) :

> **L'A6000 (48 Go) ne convient pas à Qwen3.6-27B-FP8 dans une configuration utilisable en
> production** (65536 tokens de contexte était déjà jugé insuffisant pour les tâches `_inbox/`
> réelles lors des tests Ornith du 29 juin — a fortiori sur un modèle 3× plus gros). **L'A100
> (80 Go) reste la seule carte validée pour ce modèle à `--max-model-len 131072`.**

Piste non testée ce soir, à garder en réserve si l'A6000 doit être retenté un jour : quantifier le
cache KV lui-même (`--kv-cache-dtype fp8`), ce qui réduirait son empreinte mémoire indépendamment
du contexte demandé — different levier que `gpu_memory_utilization`, qui s'est révélé peu fiable
ici.

### 1.4 Retour à l'A100 : succès
Nouveau déploiement Custom sur A100, capacité redevenue disponible à cette tentative. Démarrage
propre jusqu'à `Application startup complete`, sans avertissement mémoire.

### 1.5 Clé API : confusion sur un placeholder
`sk-<POD_ID>` dans la documentation était un gabarit à remplacer, pas une valeur littérale — collé
tel quel une fois, résultat `{"error":"Unauthorized"}`. Corrigé en récupérant la vraie valeur via
`echo $VLLM_API_KEY`. **Point de documentation à retenir** : marquer plus explicitement les
placeholders dans les futures procédures (ex. `sk-‹POD_ID_RÉEL›` ou une note en tête de bloc).

### 1.6 Conflit d'authentification Claude Code (bénin)
Au lancement de `claude`, avertissement `Auth conflict: Both a token (ANTHROPIC_AUTH_TOKEN) and an
API key (/login managed key) are set`. N'a pas faussé le test (une vraie clé Anthropic aurait de
toute façon rejeté le nom de modèle `Qwen3.6-27B-FP8`, inexistant côté Anthropic), mais résolu par
`/logout` avant de relancer. **Règle à ajouter à la procédure** : lancer `/logout` en début de
session avant de brancher Claude Code sur un endpoint local, pour éviter cet avertissement.

### 1.7 Consigne de test incomplète
La première tentative d'intégration (« Intègre les fichiers de l'ingest selon UPDATES.md et
CLAUDE.md », sans chemin explicite) a échoué **non pas par une erreur du modèle**, mais parce que
Claude Code tournait dans `/root` alors que `regression-test.sh prepare` avait déposé les fixtures
dans `/root/regression-test/sandbox/_inbox/`. Qwen a correctement identifié que `_inbox/` (relatif
à `/root`) était vide et l'a signalé sans halluciner — comportement sain, pas un défaut du modèle.

**Correction apportée** : la consigne doit toujours inclure le chemin explicite du bac à sable,
comme le prévoyait déjà le briefing 09 (« intègre `_inbox/` dans `/root/regression-test/sandbox`
selon `UPDATES.md` et `CLAUDE.md` ») — l'erreur venait d'une reformulation raccourcie de ma part en
cours de session, à ne pas reproduire.

---

## 2. Verdicts finaux (identiques au 2026-07-03)

| Cycle | Verdict | Détail |
|---|---|---|
| Atelier (`regression-test.sh`) | **8 ✓ / 0 ✗** | Fiches identiques à la référence Opus, catalogue à jour, annales journalisées, aucun effet de bord inattendu |
| Doctrinal (`regression-test-doctrinal.sh`) | **12 ✓ / 0 ✗** | Sceau Recteur intact, réparation du frontmatter propre (délimiteurs, guillemets, `## title:`), corps de fiche fidèle, étanchéité respectée |

**Qwen3.6-27B-FP8 sur A100 est confirmé équivalent Opus sur ces deux lots**, procédure rejouée de
bout en bout avec succès malgré les incidents d'infrastructure.

---

## 3. Mise à jour des décisions ouvertes (`note-optimisation-hermes-2026-07-03.md` §3.1)

| Décision | Statut avant ce soir | Statut après |
|---|---|---|
| GPU cible (A100 vs A6000) | Recommandation non testée en faveur de l'A6000 | **A6000 empiriquement écarté** pour ce modèle ; A100 requis |
| Mode d'hébergement (Phase 3 Hermes) | Ouvert | Sans objet pour l'instant — Hermes tourne sur Haiku (doc 13), la question ne se repose que si un retour au self-hosted est décidé |

---

## 4. État à la clôture de session

- Pod A100 **à éteindre** si non réutilisé dans l'heure (~1,40 $/h).
- Deux voies parallèles restent documentées et opérationnelles pour motoriser Claude Code :
  - **Qwen3.6-27B-FP8 / RunPod A100** (briefing 09 + ce compte-rendu) — gratuit à l'usage hors
    GPU-heure, contrainte de déploiement de Pod.
  - **Claude Haiku / API Anthropic directe** (doc 13) — pas d'infrastructure GPU, facturé au
    token.
- **Comparaison prévue ultérieurement** entre les deux, à l'initiative de Sidy — aucune bascule
  définitive décidée ce soir.
- Rien n'a touché le vrai dépôt `/root/wiki` : toute la session s'est déroulée dans les deux bacs à
  sable isolés (`/root/regression-test/`, `/root/regression-test-doctrinal/`), conformément à la
  conception des scripts de test.

---

## 5. Sources

- `09-briefing-transition-qwen36-27B-v3-2026-07-03.md` — procédure d'origine rejouée ce soir.
- `note-optimisation-hermes-2026-07-03.md` — décisions ouvertes mises à jour au §3 ci-dessus.
- `13-pivot-haiku-installation-hermes-phase1-2026-07-07.md` — voie alternative en comparaison.
- `06-compte-rendu-test-ornith-gpu-cloud-2026-06-29.md` — précédent où le seuil de 65536 tokens
  avait déjà été jugé insuffisant pour les tâches réelles (référence pour §1.3).
