---
title: "Tencent AngelSpec — framework unifié de speculative decoding"
type: experience
statut_experience: exploratoire
tags: [veille, inference, llm, speculative-decoding, vllm, qwen, tencent]
created: 2026-08-31
updated: 2026-08-31
sources: ["https://github.com/Tencent/AngelSpec", "https://arxiv.org/abs/2607.25852"]
links: []
---

# Tencent AngelSpec — framework unifié de speculative decoding

**Source** : vidéo YouTube « China Just Open-Sourced 6 Ways to Speed Up AI Inference (Tencent AngelSpec) » ([youtu.be/68kXJQCMBEg](https://youtu.be/68kXJQCMBEg)), investigation GitHub approfondie (API, paper arXiv, audit code, couverture médiatique).

## Contexte

AngelSpec est un framework de training **torch-native** pour le *speculative decoding* — technique d'accélération de l'inférence LLM où un modèle léger (drafter) propose plusieurs tokens d'avance, vérifiés en un seul passage par le modèle cible. Projet issu de l'équipe **Hunyuan AI Infra** de Tencent, open-sourcé le 29 juillet 2026.

## Innovations techniques

AngelSpec unifie **6 architectures de drafter** sous un même pipeline de training :

| Architecture | Méthode | Idée clé |
|---|---|---|
| **DFly** | Block-parallel | Conditionnement cible hybride + tête AR prédecesseur-conditionnée |
| **DFlash** | Block-parallel | Anchor sampling + génération de blocs parallèles |
| **DFlare** | Block-parallel | DFlash + fusion cible apprenante par couche |
| **Eagle3** | AR TTT | Test-time training avec input fusion |
| **DSpark** | Hybride | Backbone DFlash + tête AR style EAGLE |
| **MTP** | Single-head TTT | Couche MoE complète comme draft (natif Hy3) |

**Concept central** : aucun drafter unique n'optimise toutes les charges. AngelSpec spécialise structure et données d'entraînement :
- **MTP** : entraîné sur données conversationnelles riches → haute entropie, chat ouvert
- **Block-parallel (DFly/DFlash)** : entraîné sur code/maths → structure prédictible, spans longs

**D-cut** (innovation DFly) : la vérification devient une ressource partagée au niveau batch, réallocation dynamique du compute vers les préfixes haute-confiance, adaptation de la profondeur de vérification selon la charge serveur.

## Benchmarks (Hy3-A21B, TP=8, 8×H20)

### Throughput (Table 7 du paper)

| Concurrency | AR baseline | DFly | Speedup |
|---|---|---|---|
| 4 | 287.9 tok/s | 635.4 tok/s | **2.21×** |
| 8 | 426.3 tok/s | 964.8 tok/s | **2.26×** |
| 16 | 650.7 tok/s | 1623.8 tok/s | **2.50×** |
| 32 | — | — | 1.98–2.40× |
| 64 | — | — | 1.98–2.40× |

**vs DFlash** : DFly +10.5–11.8% throughput à concurrence égale.

### MTP + TTT — amélioration acceptance rate

| Benchmark | Base → TTT+Rollout | Δ |
|---|---|---|
| GSM8K | 56.8% → 80.6% | **+23.8 pp** |
| Math500 | 58.2% → 71.7% | +13.5 pp |
| HumanEval | 68.1% → 85.1% | +17.0 pp |
| MBPP | 58.4% → 71.3% | +12.9 pp |
| LiveCodeBench | 54.0% → 63.1% | +9.1 pp |
| **Moyenne** | 52.8% → 66.4% | **+13.6 pp** |

**TTT (Training-Time Test)** : résout le mismatch train/inference en exposant le module MTP à ses propres prédictions pendant l'entraînement (principe EAGLE-3).

### Ablation des pertes (Table 1)

Performance croissante : **CE ≈ KL < LK < TV Loss < e2e TV Loss (avec cold-start LK)**. AngelSpec offre 5 objectifs composable via config.

## État du projet GitHub

| Métrique | Valeur |
|---|---|
| Repo | [`Tencent/AngelSpec`](https://github.com/Tencent/AngelSpec) |
| ⭐ Stars | 231 |
| 🍴 Forks | 24 |
| Issues ouvertes | 5 (+ 1 PR ouverte) |
| Créé | 23 juillet 2026 |
| Dernier push | 31 juillet 2026 |
| Licence | **Apache-2.0** ✅ (+ 3 deps MIT : specforge, deepspec, torchspec) |
| Langage | Python (18 498 lignes) |

**Activité** : 3 commits seulement (release initiale 29-31 juil.), maintenance faible — aucune réponse aux contributions externes depuis 32 jours.

## Audit de qualité (PR #2 non mergée)

Reviewer externe `xy200303` a identifié **12 bugs de correctness** dans la PR #2 (ouverte 30 juil., non mergée) :

- **Bug critique** : RoPE `linear`/`dynamic` branches dans `llama3_eagle.py` oublient `base=` → default 10000 au lieu de `rope_theta` (ex: Llama-3 = 500000). Tout modèle entraîné avec `rope_theta ≠ 10000` utilise les **mauvaises fréquences de rotation**.
- `split_usp_batch` : variable locale shadowing fonction module → `UnboundLocalError` systématique
- Cache dataset omet `prompt_key` → réutilisation silencieuse de cache périmé
- Templates chat (`deepseek-r1-distill`) : `re.escape(None)` → `TypeError`
- Scripts exemples : `training.num_nodes` au lieu de `training.training_num_nodes` → `ConfigKeyError`

→ **Aucune réponse de Tencent** — PR non mergée, issues fermées par le reporter lui-même.

## Modèles pré-entraînés (HuggingFace AngelSlim)

| Modèle | Downloads | Usage |
|---|---|---|
| `Hy3-GGUF` | 309 682 | GGUF grand public (cartonne) |
| `Qwen3-1.7B_eagle3` | 37 973 | Drafter Eagle3 pour Qwen3-1.7B |
| `Hy4-preview-GGUF` | 26 215 | GGUF Hy4 |
| `Qwen3-8B_eagle3` | 7 470 | Drafter Eagle3 pour Qwen3-8B |
| `Qwen3-8B-DFly-Block8` | 51 | Drafter DFly pour Qwen3-8B |
| `Hy3-DFly-Block8` | 19 | Drafter DFly pour Hy3 |

→ Les drafter models spécifiques (DFly, MTP) ont très peu de downloads — adoption limitée à la recherche.

## Couverture médiatique

- MarkTechPost (30 juil.) — review technique positif
- HappyRock Cloud (31 juil.) — deep dive avec code Python reproductible
- Annonce officielle [@TencentHunyuan sur X](https://x.com/TencentHunyuan/status/2082447023626944936)
- Woosuk Kwon (co-créateur vLLM) a retweeté → validation implicite côté serving

## Pertinence pour l'infrastructure

### État actuel (2026-08-31)

Votre infrastructure (Hetzner, 3.7 Go RAM, pas de GPU, pas de containers — cf. [[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]]) ne permet pas d'exploiter AngelSpec dans l'immédiat :
- Les drafter models pré-entraînés (AngelSlim) nécessitent un GPU pour l'inférence (vLLM + drafter = plusieurs Go de VRAM)
- L'inférence actuelle se fait via providers cloud (Qwen token-plan, Anthropic API), pas en local sur GPU
- Les containers GPU cloud (RunPod) ont été suspendus

### Matériau à instruire pour développement futur

**La présente fiche est une référence technique constituée en attente d'un chantier d'inférence locale GPU.** Si un développement futur ouvre un chantier d'inférence locale sur GPU (retour aux containers, serveur dédié GPU, ou autre), AngelSpec offre :

| Élément | Valeur pour développement futur |
|---|---|
| **6 architectures de drafter** | DFly, DFlash, DFlare, Eagle3, DSpark, MTP — toutes unifiées sous un même pipeline. Permet de benchmarker plusieurs approches sans réécrire le code. |
| **Benchmarks Hy3-A21B** | 1.98–2.40× speedup (concurrence 4-64), +30% accepted length vs baseline — baseline à dépasser pour toute optimisation future. |
| **MTP + TTT** | +13.6 pp acceptance rate moyenne — méthode éprouvée pour améliorer les drafter models existants. |
| **D-cut** | Allocation dynamique de la vérification au niveau batch — pertinente pour serving à haute concurrence. |
| **Modèle `AngelSlim/Qwen3-8B_eagle3`** | 7 470 downloads, directement utilisable sur vLLM si Qwen3-8B déployé sur GPU — point d'entrée immédiat sans training. |
| **Licence Apache-2.0** | Production-safe, usage commercial ou souverain autorisé. |

### Points de vigilance (à re-consulter au moment de l'instruction)

- **Maintenance faible** : 32 jours sans réponse à la PR #2 (12 bugs de correctness non corrigés) au 2026-08-31. Re-vérifier l'état du repo avant engagement.
- **Bug RoPE critique** : tout entraînement custom avec `rope_theta ≠ 10000` utilise les mauvaises fréquences de rotation — à corriger manuellement avant usage.
- **Exigences matérielles** : 8 GPU minimum pour le training (4 inference + 4 training), 1 GPU suffit pour l'inférence avec drafter pré-entraîné.
- **Adoption limitée** : <100 downloads des drafter models spécifiques — la communauté n'a pas encore validé en production à grande échelle.

## Liens

- Repo : <https://github.com/Tencent/AngelSpec>
- Paper : <https://arxiv.org/abs/2607.25852>
- Modèles HuggingFace : <https://huggingface.co/collections/AngelSlim/angelspec>
- Documentation : <https://angelspec.readthedocs.io>

---

**Verdict** : AngelSpec est une référence scientifique sérieuse pour le speculative decoding, mais un projet de code fragile (maintenance faible, bugs critiques non corrigés). Les drafter models pré-entraînés (AngelSlim) sont consommables directement sans le framework. Pertinence pour votre stack : testable sur Qwen3-8B si vous dépassez les limites de coût/latence actuelles, mais pas urgent — votre note d'optimisation Hermes (2026-07-03) priorise d'autres chantiers (Serverless, A100 vs A6000).
