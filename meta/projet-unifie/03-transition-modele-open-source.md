---
title: "Transition vers un modèle IA open-source local (sortir du coût au token)"
type: meta
tags: [outillage, projet-claude-ai, modele-local, open-source, transition, infrastructure]
created: 2026-06-28
updated: 2026-06-28
---

# Transition vers un modèle IA open-source local

> **But** : décharger le **rôle mécanique d'intégration** (aujourd'hui tenu par Claude Code via
> l'API payante au token) sur un **modèle open-source hébergé localement**, pour ne plus payer au
> token les opérations répétitives. La lecture lourde et la production de contenu **restent côté
> Claude.ai** (forfait). Ce document prépare la décision, l'installation et le workflow.

> ⚠️ **Point de vigilance — nom du modèle** : le nom « **Ornithpar** » avancé en exemple n'est pas
> reconnu comme un modèle existant à la date de rédaction. Il est traité ici comme un *placeholder*
> « modèle open-source à confirmer ». **À faire** : confirmer le nom exact, sa source (Hugging Face
> ou autre), sa licence et ses capacités réelles avant tout engagement. Les familles citées plus bas
> sont des repères de méthode, pas une recommandation figée.

## 1. Ce que le poste « intégration » doit réellement savoir faire

Le rôle à reprendre est **mécanique et contraint**, pas créatif. Il exige :

1. **Suivi d'instructions rigoureux** et discipline de format (YAML du Sceau Recteur, wikilinks,
   nommage ASCII).
2. **Usage d'outils / agentique** : lire/écrire des fichiers, exécuter des commandes shell et `git`,
   appliquer des `UPDATES.md`. C'est **le vrai goulot** : beaucoup de petits modèles savent générer
   du texte mais tiennent mal une boucle d'outils fiable.
3. **Compréhension du français** (le dépôt et les consignes sont en français).
4. **Fenêtre de contexte** suffisante pour lire plusieurs fiches + l'`UPDATES.md` + des bouts d'index.
5. **Déterminisme** : pour l'intégration, on préfère la régularité à la créativité (température basse).

Corollaire : une grande partie du rôle peut être rendue **encore plus déterministe par des scripts**
(parser le frontmatter, réparer `-----`→`---`, mettre à jour l'index, générer le manifeste). Plus on
scripte, moins le modèle local a besoin d'être puissant. **Stratégie recommandée : scripts d'abord,
modèle local ensuite pour ce qui exige du jugement (classement, maillage, rédaction de la ligne
d'annales).**

## 2. Critères de choix d'un modèle open-source

- **Capacité agentique / tool-use** réelle et fiable (priorité n°1).
- **Qualité en français** et en raisonnement structuré.
- **Taille vs matériel disponible** : un modèle qui tient sur le matériel cible, quantifié si besoin.
- **Licence** réellement ouverte et compatible avec l'usage.
- **Écosystème de service** (facilité à l'exposer via une API locale type OpenAI-compatible).

Familles open-source à évaluer (repères de méthode, à vérifier au moment du choix, car le paysage
évolue vite) : **Qwen**, **Llama**, **Mistral/Mixtral**, **DeepSeek**, **Gemma**, **Command-R**.
Le critère décisif restera la **fiabilité agentique** sur *ce* workflow précis, à tester sur un lot
réel d'`_inbox/`, pas les benchmarks génériques.

## 3. Où l'héberger (matériel)

L'iPad ne peut pas faire tourner le modèle. Trois pistes :

- **(a) Sur le serveur Hetzner actuel** s'il a les ressources (RAM/VRAM) — sinon migrer vers une
  instance plus capable (CPU à forte RAM pour de petits modèles quantifiés, ou GPU pour de plus gros).
- **(b) Un serveur dédié séparé** (GPU) qui n'héberge que le modèle, exposant une API locale que
  Claude Code (ou un agent maison) appelle.
- **(c) Un appareil dédié futur** (déjà évoqué dans la fiche v0.1 de l'instrument comme hypothèse
  assumée non figée) — horizon plus lointain.

**Recommandation de méthode** : commencer petit (un modèle quantifié sur le serveur existant ou une
instance modeste) pour valider le workflow de bout en bout avant d'investir dans du GPU.

## 4. Comment le brancher dans le workflow (deux options)

- **Option A — Agent maison léger** : un script orchestrateur (Python) qui lit `_inbox/`, appelle le
  modèle local via une API locale (p. ex. Ollama / llama.cpp / vLLM, exposant une API
  OpenAI-compatible), et applique les éditions de fichiers + `git`. Maximum de contrôle, maximum de
  scripts déterministes autour du modèle. **Recommandé** pour ce rôle contraint.
- **Option B — Réutiliser le harnais Claude Code en le pointant vers un endpoint local** si la
  configuration le permet. Plus simple à prendre en main, mais dépend de la compatibilité de l'outil
  avec un backend non-Anthropic — **à vérifier**.

Dans les deux cas, le **contrat de travail ne change pas** : « intègre `_inbox/` » selon
`UPDATES.md` et `CLAUDE.md`, puis commit/push, puis vider le sas.

## 5. Plan d'installation par étapes (pédagogique, à dérouler en session « infrastructure »)

> Détaillé exprès pour éviter d'avoir à se répéter. Chaque commande sera ré-expliquée en direct au
> moment de l'exécution ; ici, c'est la **carte d'ensemble**.

1. **Confirmer le modèle** (nom exact, licence, taille, capacités tool-use) — lever l'ambiguïté
   « Ornithpar ».
2. **Évaluer le matériel** : `nproc`, `free -h`, présence GPU (`nvidia-smi`), espace disque
   (`df -h`). En déduire la taille de modèle réaliste.
3. **Installer un serveur d'inférence local** (p. ex. Ollama pour démarrer vite, vLLM pour plus de
   débit) exposant une API locale.
4. **Télécharger le modèle** (quantifié si nécessaire) et vérifier qu'il répond.
5. **Écrire l'orchestrateur** (Option A) : lecture `_inbox/`, prompt système = règles d'intégration
   condensées + `CLAUDE.md`, application des éditions, `git`.
6. **Tester sur un lot réel** déjà intégré par Claude Code, et **comparer le résultat** (frontmatter,
   index, annales, étanchéité) — c'est le critère de réussite.
7. **Définir la répartition cible** : ce que fait le modèle local (mécanique régulière) vs ce qui
   reste sur l'API Claude (cas ambigus, jugement doctrinal délicat, rédaction sensible).
8. **Documenter** la procédure dans `meta/` et basculer progressivement.

## 6. Points de vigilance de la transition

- **Ne pas dégrader la qualité d'intégration** : un modèle local moins fiable peut introduire des
  erreurs de frontmatter ou des liens morts. D'où : scripts déterministes au maximum + tests de
  non-régression + VIGILANCE systématique après chaque lot.
- **Garder l'humain dans la boucle** pour le classement ambigu et tout ce qui touche au Discernement
  (Cmd 12 inchangé, quel que soit le modèle).
- **Sécurité / secrets** : la clé API et l'accès `git` (clé SSH du dépôt) restent sensibles ; le
  modèle local ne doit pas les exfiltrer dans des fichiers du dépôt.
- **Coût réel** : un GPU loué peut coûter plus qu'un usage API modéré — comparer honnêtement avant de
  migrer le matériel.
- **Étanchéité du rôle** : le modèle local **applique**, ne **rédige pas** de doctrine (même règle
  économique qu'aujourd'hui).
