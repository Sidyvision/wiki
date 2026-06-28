---
title: "Transition vers un modèle open-source local (remplacer Opus dans Claude Code)"
type: meta
tags: [outillage, projet-claude-ai, modele-local, open-source, transition, infrastructure, claude-code]
created: 2026-06-28
updated: 2026-06-28
---

# Transition vers un modèle open-source local

> **But précisé par Sidy (2026-06-28)** : ne pas seulement créer un agent d'intégration séparé, mais
> **remplacer le modèle qui motorise Claude Code lui-même** — aujourd'hui Opus via l'API Anthropic
> (payante au token) — par un **modèle open-source hébergé localement** (« **Ornith** » = nom
> d'exemple, modèle exact à confirmer). On garde **exactement le même workflow** (« intègre
> `_inbox/` », commit/push) ; seul le moteur change. La lecture lourde et la production de contenu
> restent côté **Claude.ai (forfait)** ; c'est le poste **intégration** (Claude Code) qu'on
> débranche du coût au token.

> ✅ **Faisabilité vérifiée (2026-06-28, via l'assistant Claude Code)** : c'est possible et
> documenté. Claude Code supporte officiellement un **endpoint personnalisé** ; plusieurs serveurs
> d'inférence open-source exposent désormais nativement l'API Anthropic. Détails et sources ci-dessous.

## 1. Le mécanisme exact (officiellement supporté)

Claude Code parle l'**API Messages d'Anthropic** (`POST /v1/messages`). Il suffit de le pointer vers
un endpoint qui parle la même API mais qui est adossé à un modèle open-source local :

```bash
export ANTHROPIC_BASE_URL=http://localhost:11434   # l'endpoint local
export ANTHROPIC_AUTH_TOKEN=ollama                 # jeton (factice en local)
export ANTHROPIC_MODEL=<nom-du-modele-charge>       # ex. le modèle "Ornith"
claude
```

À rendre permanent dans `~/.claude/settings.json` (bloc `env`) pour ne pas le retaper à chaque
session. Note : les modèles **purement locaux ne sont pas « supportés » directement** par Anthropic —
ce qui est supporté, c'est l'**endpoint compatible** ; le reste (le modèle derrière) est de notre
ressort.

## 2. Serveurs d'inférence qui exposent nativement l'API Anthropic

Aucun proxy nécessaire avec (vérifié 2026) :

- **Ollama** (≥ v0.14) — le plus simple pour démarrer. `ANTHROPIC_BASE_URL=http://localhost:11434`.
- **LM Studio** (≥ v0.4.1) — gestion de modèles en interface graphique.
- **vLLM** — haute performance / multi-GPU. `ANTHROPIC_BASE_URL=http://localhost:8000`.

**llama.cpp** ne parle pas l'API Anthropic directement : le placer derrière un **proxy** (type
**LiteLLM**) qui traduit. Option de repli si besoin.

## 3. Ce que le modèle DOIT savoir faire (exigences dures)

Claude Code est un agent : il **n'écrit pas juste du texte, il appelle des outils**. Le modèle local
doit donc tenir :

1. **Tool use / function calling fiable** — *l'exigence n°1 et le vrai goulot*. Le modèle doit
   accepter le tableau `tools` et renvoyer des blocs `tool_use` bien formés. Un tool-use bancal
   **casse la boucle agentique** (l'intégration échoue ou tourne en rond).
2. **Contexte long** — 32K **minimum**, 64K+ **recommandé** (lire plusieurs fiches + `UPDATES.md` +
   bouts d'index sans saturer).
3. **Streaming**, **gestion du system prompt**, **suivi d'instructions multi-étapes**.

Ordre de grandeur de taille : **≥ 13B** pour un tool-use raisonnablement fiable ; en dessous de ~7B,
taux d'échec élevé. Le critère décisif n'est pas le benchmark générique mais la **fiabilité
agentique sur _notre_ workflow** — à tester sur un vrai lot `_inbox/`.

## 4. Matériel (le poste réellement contraignant)

L'iPad ne fait pas tourner le modèle ; il tourne sur le serveur. Ordres de grandeur (vérifiés) :

- **Modèle ~70B** : ≈ **44 Go de VRAM quantifié**, ≈ **80 Go en FP16** → une **instance GPU** dédiée.
- **Modèle 8–14B** : matériel plus modeste, **mais fiabilité agentique moindre** — acceptable pour
  démarrer/tester, risqué pour l'intégration sans garde-fous.
- **CPU seul** : fonctionne mais **très lent** (latence de plusieurs secondes par étape) → bon pour
  l'expérimentation, pas pour l'usage courant.

Pistes : (a) instance GPU chez Hetzner ; (b) serveur dédié GPU séparé exposant l'endpoint ; (c)
appareil dédié futur (hypothèse déjà notée dans la fiche v0.1 de l'instrument). **Recommandation :
commencer petit** (un 8–14B quantifié) pour valider la chaîne de bout en bout **avant** de louer du
GPU coûteux.

## 5. Plan d'installation par étapes (session « Infrastructure », pédagogique)

> Carte d'ensemble ; chaque commande sera ré-expliquée en direct au moment de l'exécution.

1. **Confirmer le modèle** : nom exact (« Ornith » → ?), source (Hugging Face…), licence, fenêtre de
   contexte, qualité tool-use. Lever l'ambiguïté avant tout.
2. **Relevé matériel** : `nproc`, `free -h`, `nvidia-smi` (GPU ?), `df -h` (disque). En déduire la
   taille de modèle réaliste.
3. **Installer le serveur d'inférence** : Ollama pour démarrer vite (`curl -fsSL https://ollama.com/install.sh | sh`),
   ou vLLM pour le débit. Vérifier qu'il répond.
4. **Télécharger le modèle** (quantifié si besoin) et le tester hors Claude Code (un appel simple).
5. **Brancher Claude Code** : poser `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_MODEL`
   dans `~/.claude/settings.json`, lancer `claude`, faire un essai trivial (lire un fichier, éditer,
   `git status`).
6. **Test de non-régression** : lui faire intégrer un lot `_inbox/` **déjà** intégré par Opus, puis
   **comparer** (frontmatter, `index.md`, `annales.md`, étanchéité, liens). C'est le **critère de
   réussite objectif**.
7. **Définir la répartition cible** (voir §7) et basculer progressivement.
8. **Documenter** la procédure finale dans `meta/`.

## 6. Pièges concrets propres à Claude Code sur endpoint non-Anthropic (vérifiés)

- **Recherche d'outils MCP désactivée** quand `ANTHROPIC_BASE_URL` pointe un hôte non-Anthropic →
  réactiver avec `ENABLE_TOOL_SEARCH=true`, **mais** le proxy/serveur doit savoir transmettre les
  blocs `tool_reference` (sinon, ne pas l'activer).
- **Prompt caching imprévisible** sur endpoint custom → si erreurs de cache, poser
  `DISABLE_PROMPT_CACHING=1`.
- **WebSearch** peut ne pas être disponible (dépend du serveur) — sans incidence pour l'intégration.
- **Tool-call fragile** sur petits modèles : appels malformés, outils hallucinés, dérive en cours de
  tâche. D'où l'importance de scripter le déterministe (ci-dessous) et de la VIGILANCE post-lot.
- **Latence** : 5–10 s/étape sur petit matériel — gênant en interactif, pas faux pour autant.

## 7. Stratégie recommandée : scripter d'abord, hybride ensuite

- **Scripter le déterministe** : parser/réparer le frontmatter (`-----`→`---`, `## title:`,
  guillemets), mettre à jour l'index, générer le manifeste de l'app, lancer les contrôles VIGILANCE.
  Plus on scripte, **moins le modèle local a besoin d'être puissant** — il ne porte que le jugement
  (classement ambigu, maillage, rédaction de la ligne d'annales).
- **Hybride** : modèle **local** pour la mécanique régulière (lots bien formatés au Sceau Recteur,
  comme les zips d'ingest) ; **Opus/API** réservé aux cas difficiles (classement ambigu, jugement
  doctrinal délicat, rédaction sensible, Discernement). Cmd 12 inchangé quel que soit le moteur.
- **Garder l'humain dans la boucle** pour tout ce qui touche au Discernement et à l'étanchéité.

## 8. Points de vigilance de la transition

- **Ne pas dégrader la qualité d'intégration** : tests de non-régression + VIGILANCE après chaque
  lot ; un modèle local moins fiable introduit vite des liens morts / frontmatter cassé.
- **Coût réel** : un GPU loué peut coûter **plus** qu'un usage API modéré — comparer honnêtement
  avant de migrer le matériel. La bascule se justifie surtout si le volume d'intégration est élevé.
- **Sécurité / secrets** : clé API et clé SSH du dépôt restent sensibles ; le modèle local ne doit
  jamais les recopier dans des fichiers du dépôt.
- **Étanchéité du rôle** : le moteur local **applique, ne rédige pas** de doctrine (même règle
  économique qu'aujourd'hui).

## 9. Sources (vérifiées le 2026-06-28)

- Claude Code — Settings (`ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_MODEL`,
  `ENABLE_TOOL_SEARCH`, `DISABLE_PROMPT_CACHING`) : https://code.claude.com/docs/en/settings.md
- Claude Code sur Amazon Bedrock / Google Vertex (fournisseurs officiels) :
  https://code.claude.com/docs/en/amazon-bedrock · https://code.claude.com/docs/en/google-vertex-ai
- Ollama — compatibilité API Anthropic : https://docs.ollama.com/api/anthropic-compatibility
- Claude Code avec LLM locaux (Ollama, LM Studio, llama.cpp, vLLM) :
  https://renezander.com/guides/claude-code-local-llm-anthropic-base-url/
- vLLM — intégration Claude Code : https://docs.vllm.ai/en/stable/serving/integrations/claude_code/
