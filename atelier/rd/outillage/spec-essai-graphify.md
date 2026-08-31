---
title: "Essai — Graphify (knowledge graph de code, local/déterministe)"
type: experience
tags: [outillage, graphe, essai, graphify, tree-sitter]
created: 2026-08-31
updated: 2026-08-31
sources: []
links: []
statut_experience: exploratoire
---

# Essai — Graphify (knowledge graph de code)

## Contexte

Demande de Sidy (2026-08-31), à la suite d'une comparaison avec notre propre
`generer-cartographie.py` (`atelier/rd/outillage/graphe/`) : installer
[Graphify](https://github.com/Graphify-Labs/graphify) à l'essai, côté
`atelier/rd/outillage/` uniquement.

**Différence de nature avec notre graphe existant** : le nôtre cartographie
le *dépôt doctrinal* (fiches Markdown, wikilinks `[[slug]]`, frontmatter
Sceau) pour un contrôle de forme/étanchéité. Graphify cartographie du **code
source** (fonctions, classes, imports) via parsing AST (`tree-sitter`), pour
donner à un assistant IA une structure interrogeable au lieu de relire les
fichiers. Les deux ne se recouvrent pas ; ce n'est pas un remplacement.

## Installation

Venv isolé, jamais le Python système (`externally-managed-environment` sur
cette machine) :

```
python3 -m venv atelier/rd/outillage/.graphify-venv
.graphify-venv/bin/pip install graphifyy   # 0.9.53
```

`graphify install` (qui écrirait dans un fichier `CLAUDE.md`/`AGENTS.md` et
poserait un hook `PreToolUse`) **n'a volontairement pas été exécuté** — hors
périmètre de la demande (« côté `atelier/rd/outillage/` »), et modifier un
fichier de protocole ou poser un hook d'interception d'outil est une décision
distincte, à instruire séparément si l'essai est concluant.

## Exécution

```
.graphify-venv/bin/graphify extract . --code-only
.graphify-venv/bin/graphify cluster-only .
```

`--code-only` : saute l'extraction docs/PDF/images (qui, elle, passerait par
un backend LLM — Anthropic/OpenAI/Gemini/Ollama selon config). L'extraction
code elle-même est **100 % locale (tree-sitter), aucun appel réseau**. Le
`cluster-only` a tenté un nommage de communautés via backend `anthropic` (non
installé dans le venv) : échec propre, repli sur des noms `Community N` —
confirme qu'aucun appel n'a été tenté sans le paquet, donc aucune fuite de
contenu vers un tiers ici.

## Résultat

- 22 fichiers Python de `atelier/rd/outillage/` analysés (les scripts
  `.sh` et fichiers hors extension reconnue ignorés).
- Graphe : 163 nœuds, 230 arêtes, 21 communautés.
- Sortie dans `graphify-out/` (non versionné, régénérable — `.gitignore`) :
  `graph.json`, `graph.html`, `GRAPH_REPORT.md`.
- Rapport lisible et pertinent : hubs par fichier (`generer-cartographie.py`,
  `srs.py`, `generer-manifeste.py`...), nœuds les plus connectés
  (`generer()`, `cmd_review()`, `main()`...), nœuds isolés (les 4 scripts
  `.sh` de cron, faute de support shell approfondi côté extraction), aucune
  dépendance circulaire détectée.

## Vigilance

- **Aucun appel réseau constaté** durant l'essai (mode `--code-only`, backend
  de labellisation absent → repli local).
- **Aucune fiche `doctrinal/` ni contenu sensible `meta/` traité** — essai
  strictement cantonné à `atelier/rd/outillage/`, comme demandé.
- Le venv (196 Mo) et `graphify-out/` sont exclus du dépôt git (`.gitignore`) :
  artefacts régénérables/dépendances, pas du contenu du dépôt.
- **Non fait** : `graphify install` (intégration comme skill Claude Code,
  écriture dans un `CLAUDE.md`, hook `PreToolUse`) — verdict Sidy requis avant
  toute extension au-delà de l'essai CLI local.

## Verdict

En attente — essai posé pour évaluation, `statut_experience: exploratoire`
(Cmd 12 : la machine constate et documente, ne décide pas de l'adoption).
