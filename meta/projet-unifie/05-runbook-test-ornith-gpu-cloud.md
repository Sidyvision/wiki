---
title: "Runbook — Test d'Ornith 1.0 sur GPU cloud à l'heure (motoriser Claude Code)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, runbook, ornith, vllm, gpu-cloud]
created: 2026-06-28
updated: 2026-06-28
---

# Runbook — Tester Ornith 1.0 sur GPU cloud à l'heure

> **Objectif** : valider qu'Ornith 1.0 peut **motoriser Claude Code à la place d'Opus** pour
> l'intégration `_inbox/`, **sans engagement matériel**, en louant un GPU à l'heure le temps d'un
> test. Critère de réussite : Ornith intègre un lot témoin aussi proprement qu'Opus (frontmatter,
> index, annales, étanchéité, liens).
>
> **Mode pédagogique** : chaque étape dit *quoi faire, pourquoi, et ce qui se passe derrière*.
> Détaillé exprès pour ne pas avoir à le redemander.

> 🔧 **Corrections issues du 1er test réel (2026-06-29)** — voir le compte-rendu complet
> `06-compte-rendu-test-ornith-gpu-cloud-2026-06-29.md`. À retenir avant de recommencer :
> 1. **RunPod : choisir Pods → Deploy a Pod, PAS Serverless** (le Serverless n'offre pas d'accès
>    SSH/tunnel).
> 2. **Authentification** : Claude Code envoie `x-api-key`, mais vLLM n'accepte que
>    `Authorization: Bearer <clé>` → 401 systématique. **Correctif : `ANTHROPIC_CUSTOM_HEADERS`**
>    (cf. Phase 5).
> 3. **Contexte** : `32768` est **trop petit** (le prompt système de Claude Code ≈ 27K tokens, des
>    tours réels atteignent ~143K) → **utiliser `--max-model-len 131072`** (cf. Phase 3).
> 4. L'image `vllm/vllm-openai` **n'a pas de serveur SSH** : l'installer après chaque (re)démarrage ;
>    le **port SSH externe change à chaque restart** ; **ne jamais faire `pkill -f vllm`** (tue le
>    PID 1 → redémarre le conteneur). Détails dans le compte-rendu §3–4.

## Vue d'ensemble de l'architecture du test

```
[iPad/Termius] ──ssh──> [Serveur Hetzner]  ──tunnel SSH chiffré──>  [GPU cloud à l'heure]
                         · dépôt /root/wiki                         · vLLM sert Ornith-1.0-9B
                         · client `claude`                          · port 8000 (API Anthropic)
                         · scripts, git                             · JAMAIS exposé en public
```

**Séparation des rôles (importante pour la sécurité)** :
- Le **serveur Hetzner** garde le dépôt, git, et le client `claude`. Les **secrets** (clé SSH du
  dépôt) **restent ici**.
- Le **GPU cloud** ne fait *que* de l'inférence. Il est **éphémère et tiers** : on n'y met aucun
  secret du dépôt.
- On relie les deux par un **tunnel SSH** : Claude Code parle à `http://localhost:8000`, qui est en
  réalité le GPU distant via le tunnel. Le port d'inférence n'est **jamais** ouvert sur Internet
  (vLLM n'a pas d'authentification par défaut — l'exposer serait dangereux).

---

## Phase 0 — Choisir le fournisseur et le GPU

**Fournisseurs « à l'heure », facturés à la seconde/minute, sans engagement** :
- **RunPod** — le plus simple (images prêtes, accès SSH, volumes persistants). Recommandé pour un
  premier test. **Choisir « Pods → Deploy a Pod », PAS « Serverless »** (le Serverless n'offre pas
  l'accès SSH/tunnel ; vérifié 2026-06-29). Setup validé : 1× RTX A6000 48 Go, image
  `vllm/vllm-openai:latest`, volume 50 Go sur `/workspace`, ≈ 0,50 $/h.
- **Vast.ai** — souvent le moins cher (marché d'instances), un peu plus brut.
- **Lambda Cloud** — propre, parfois en rupture de stock.

**Quel GPU ?** Ornith-1.0-9B en **bf16 pèse ≈ 19 Go**. Pour un test confortable :
- **Recommandé : un GPU 48 Go** (RTX A6000 / L40S) — ≈ 0,5–0,9 $/h. Large marge pour le cache KV.
- Possible : 80 Go (A100/H100) — plus cher, inutile pour le 9B.
- À éviter pour ce test : 24 Go (les 19 Go de poids laissent trop peu pour le contexte ; faisable
  seulement en réduisant fortement le contexte ou via une variante GGUF Q4 sur Ollama — voir Annexe).

**Coût d'un test** : 1 à 2 h → **quelques dollars**. On éteint après → la facturation s'arrête.

> 💡 **Astuce coût** : crée un **volume réseau persistant** (~50 Go) sur le fournisseur et fais-y
> télécharger Ornith. Aux tests suivants, tu rattaches le volume et tu **ne re-télécharges pas** les
> 19 Go.

---

## Phase 1 — Lancer l'instance GPU

1. Créer un compte chez le fournisseur, ajouter un peu de crédit.
2. Lancer une instance :
   - **GPU** : 48 Go (cf. ci-dessus).
   - **Image** : une image **vLLM** ou **PyTorch CUDA** récente (RunPod en propose des prêtes).
   - **Disque/volume** : ≥ 50 Go (poids + cache HF).
   - **Accès SSH activé** (note l'hôte, le port et l'utilisateur fournis).
3. Se connecter en SSH à l'instance (depuis le serveur Hetzner ou Termius) :
   ```bash
   ssh <user>@<hote-gpu> -p <port>
   ```
   *Pourquoi* : on prépare le serveur d'inférence sur la machine GPU.

---

## Phase 2 — Installer vLLM et télécharger Ornith (sur le GPU)

1. Vérifier le GPU :
   ```bash
   nvidia-smi
   ```
   *Derrière* : confirme que CUDA voit bien la carte et sa VRAM.
2. Installer vLLM si l'image ne l'a pas déjà :
   ```bash
   pip install -U vllm huggingface_hub
   ```
3. (Optionnel mais conseillé) pré-télécharger le modèle sur le volume persistant :
   ```bash
   huggingface-cli download deepreinforce-ai/Ornith-1.0-9B --local-dir ./Ornith-1.0-9B
   ```
   *Pourquoi* : sépare le téléchargement (long, ~19 Go) du démarrage du serveur.

---

## Phase 3 — Démarrer le serveur d'inférence vLLM (sur le GPU)

Commande de service **recommandée par l'auteur du modèle** (adaptée pour le test) :

```bash
vllm serve deepreinforce-ai/Ornith-1.0-9B \
  --served-model-name Ornith-1.0-9B \
  --host 127.0.0.1 --port 8000 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_xml \
  --reasoning-parser qwen3 \
  --trust-remote-code
```

Explication des options clés :
- `--served-model-name Ornith-1.0-9B` : le nom que Claude Code devra utiliser (`ANTHROPIC_MODEL`).
- `--host 127.0.0.1` : **n'écoute qu'en local** sur le GPU → on y accède **uniquement** par le
  tunnel SSH (sécurité). (L'auteur met `0.0.0.0` ; on reste plus prudent.)
- `--max-model-len 131072` : **corrigé après le test du 2026-06-29.** 32K et 64K sont
  **insuffisants** — le seul prompt système de Claude Code pèse ≈ 27K tokens, et des tours réels ont
  atteint ~143K tokens en entrée (→ erreur 500). **128K est le plancher réaliste** ; à 0.90 de
  `gpu-memory-utilization`, ça tient sur un GPU 48 Go avec le 9B. (Le modèle accepte jusqu'à 262 144.)
- `--enable-auto-tool-choice --tool-call-parser qwen3_xml` : **le point critique** — active et
  parse correctement les appels d'outils d'Ornith (sans ça, la boucle agentique de Claude Code casse).
- `--reasoning-parser qwen3` : gère le bloc de raisonnement `<think>` du modèle.

Attendre le message de démarrage complet (« Application startup complete » / modèle chargé).
**Vérifier l'API Anthropic** (depuis le GPU, autre terminal) :
```bash
curl -s http://127.0.0.1:8000/v1/messages \
  -H "content-type: application/json" \
  -d '{"model":"Ornith-1.0-9B","max_tokens":64,"messages":[{"role":"user","content":"dis bonjour"}]}'
```
*Pourquoi* : vLLM **implémente nativement l'API Anthropic** (`/v1/messages`) — c'est exactement ce
que parle Claude Code. Une réponse JSON = le serveur est bon.

---

## Phase 4 — Ouvrir le tunnel SSH (depuis le serveur Hetzner)

Sur le **serveur Hetzner** (pas le GPU), ouvrir un tunnel qui mappe le port local 8000 vers le GPU :
```bash
ssh -N -L 8000:127.0.0.1:8000 <user>@<hote-gpu> -p <port>
```
*Derrière* : tout ce qui frappe `localhost:8000` sur le Hetzner est chiffré et renvoyé au vLLM du
GPU. Laisser ce terminal ouvert pendant le test (ou ajouter `-f` pour le passer en arrière-plan).

---

## Phase 5 — Brancher Claude Code sur Ornith (sur le serveur Hetzner)

Dans le shell où tu lanceras `claude` :
```bash
export ANTHROPIC_BASE_URL=http://localhost:8000
export ANTHROPIC_MODEL=Ornith-1.0-9B
export ANTHROPIC_SMALL_FAST_MODEL=Ornith-1.0-9B    # sinon les tâches de fond appellent un Haiku inexistant
export ANTHROPIC_DEFAULT_HAIKU_MODEL=Ornith-1.0-9B
export DISABLE_PROMPT_CACHING=1                     # le cache de prompt est imprévisible hors Anthropic
# --- Authentification (CORRIGÉ après le test du 2026-06-29) ---
# vLLM n'authentifie QUE via le header "Authorization: Bearer <clé>".
# Or Claude Code envoie nativement "x-api-key" → 401 systématique.
# Correctif : injecter le bon header via ANTHROPIC_CUSTOM_HEADERS.
export VLLM_API_KEY="sk-..."                        # clé fournie par le serveur (auto-générée par RunPod)
export ANTHROPIC_API_KEY="$VLLM_API_KEY"
export ANTHROPIC_AUTH_TOKEN="$VLLM_API_KEY"
export ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"   # ← LE point qui débloque le 401
# NE PAS activer ENABLE_TOOL_SEARCH (recherche d'outils MCP) pour ce test
```
Puis :
```bash
claude
```
Test trivial d'abord : lui demander de lire un fichier, faire une petite édition, lancer
`git status`. *Pourquoi* : on valide la **boucle d'outils** avant l'intégration réelle.

> ⚠️ Ne pas mettre ces `export` dans `~/.bashrc` tant que le test n'est pas concluant : sinon **toutes**
> tes sessions `claude` basculeraient sur Ornith. Les garder dans un shell dédié pour le test.

---

## Phase 6 — Test de non-régression (le vrai juge)

1. Choisir un **lot témoin** déjà intégré proprement par Opus (p. ex. recréer un petit `_inbox/`
   à partir d'un zip d'ingest passé).
2. Lancer la consigne habituelle : **« intègre `_inbox/` selon UPDATES.md et CLAUDE.md »**.
3. **Comparer** le résultat à l'intégration Opus :
   - frontmatter (Sceau Recteur valide, guillemets droits) ;
   - `index.md` et `annales.md` corrects ;
   - étanchéité des circuits respectée, pas de liens morts ;
   - classement et maillage pertinents.
4. **Verdict** :
   - ✅ équivalent → Ornith est viable pour le rôle d'intégration ; envisager la suite (volume,
     coût, voie d'hébergement b/c).
   - ⚠️ approximatif (frontmatter cassé, liens manqués, dérive) → renforcer les **scripts
     déterministes** autour du modèle et garder la **stratégie hybride** (Opus pour les cas
     délicats). Re-tester.

---

## Phase 7 — Éteindre (arrêter la facturation)

1. Fermer le tunnel SSH (Ctrl-C sur le terminal du tunnel).
2. Arrêter / supprimer l'instance GPU **dans l'interface du fournisseur** (sinon elle continue d'être
   facturée). Conserver le **volume persistant** si tu prévois d'autres tests.
3. Sur le Hetzner, ouvrir un nouveau shell (sans les `export`) pour revenir à Opus.

---

## Annexe — Variante économique (GPU 24 Go via Ollama + GGUF)

Si tu veux tester sur une carte 24 Go moins chère : utiliser le build **`deepreinforce-ai/Ornith-1.0-9B-GGUF`**
(quantifié, ~6 Go) servi par **Ollama** (qui expose nativement l'API Anthropic ≥ v0.14). C'est moins
cher mais **plus fragile pour le tool-use** (le gabarit d'appel d'outils GGUF doit bien mapper le
format `qwen3_xml`). À réserver si le coût prime ; sinon, la voie vLLM ci-dessus (bf16, 48 Go) est
**plus fiable** car c'est le chemin recommandé par l'auteur du modèle.

---

## Récapitulatif des pièges (déjà rencontrés / vérifiés)

- **RunPod** : **Pods**, pas Serverless (sinon pas de SSH/tunnel). *(test 2026-06-29)*
- **Authentification** : Claude Code envoie `x-api-key`, vLLM exige `Authorization: Bearer` →
  injecter `ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer <clé>"`. *(test 2026-06-29)*
- **Contexte** : `--max-model-len 131072` (128K) est le plancher réaliste pour Claude Code ; 32K/64K
  échouent (erreur 500). *(test 2026-06-29)*
- **SSH sur l'image vLLM** : pas de `sshd` par défaut → l'installer après chaque (re)démarrage ; le
  port SSH externe **change à chaque restart** ; **ne jamais `pkill -f vllm`** (tue le PID 1 →
  redémarre le conteneur). Clé SSH dans **Settings → SSH public keys** (compte, pas le Pod). *(test 2026-06-29)*
- **Sécurité** : `--host 127.0.0.1` + tunnel SSH ; ne jamais exposer le port 8000 publiquement.
- **Modèle de fond** : fixer `ANTHROPIC_SMALL_FAST_MODEL` (et `ANTHROPIC_DEFAULT_HAIKU_MODEL`) sur
  Ornith, sinon erreurs sur un modèle Haiku absent.
- **Tool-use** : `--enable-auto-tool-choice --tool-call-parser qwen3_xml` obligatoires.
- **Cache** : `DISABLE_PROMPT_CACHING=1`.
- **Secrets** : rien de sensible sur le GPU tiers.
- **Coût** : éteindre l'instance ; volume persistant pour ne pas re-télécharger.
- **Variables non persistantes** : réexporter les `ANTHROPIC_*` dans chaque nouveau shell.
- **Fiabilité narrative (test 2026-06-29, conclu : VERDICT 8 ✓ / 0 ✗)** : en session longue, le
  *discours* d'Ornith se dégrade (langues mêlées, fuite `</think>`, contradictions) **mais ses
  écritures restent correctes** — *fiabilité d'action ≠ fiabilité narrative*. Donc, règles fermes :
  - **JAMAIS d'auto-accept** des modifications avec Ornith (relire chaque `Write`/`Update`/Bash).
  - **Toujours clore par `ornith-test.sh compare`** (juge mécanique indépendant), **jamais** par
    l'auto-évaluation du modèle (« as-tu bien intégré ? » n'est pas fiable).
  - **Limiter la durée des sessions** (dégradation observée après ~30-40 min de raisonnement continu).
  - Cas **doctrinal** (Sceau Recteur, Discernement, étanchéité) **pas encore testé** → enjeu plus
    élevé, à valider spécifiquement avant d'y confier Ornith.

## Sources (vérifiées le 2026-06-28)

- vLLM ↔ Claude Code (API Anthropic native, flags tool-call) :
  https://docs.vllm.ai/en/stable/serving/integrations/claude_code/
- Ornith-1.0-9B (carte modèle, commande vLLM, parser `qwen3_xml`) :
  https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B
- Ornith-1.0-9B-GGUF (variante quantifiée) :
  https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF
- Claude Code — variables d'environnement (`ANTHROPIC_BASE_URL`, modèles, cache) :
  https://code.claude.com/docs/en/settings.md
