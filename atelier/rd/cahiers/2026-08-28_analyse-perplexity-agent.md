---
title: "Analyse technique : agents de recherche - perplexe vs cookbook"
type: experience
tags: ["agents", "research", "methodology", "soverainete"]
created: 2026-08-28
updated: 2026-08-28
sources: ["[[atelier/etudes-de-cas/2026-08-28_build-your-own-perplexity.md]]"]
links: []
---

# Analyse technique : agents de recherche — perplexe vs cookbook

## 1. Contexte
Analyse du corpus "Build Your Own Perplexity with Exa" (Sarah Chieng, 2025). Cette étude explore l'implémentation d'assistants de recherche profonde utilisant des modèles d'inférence rapide (Cerebras) et des moteurs de recherche sémantique (Exa).

## 2. Analyse comparative
La méthodologie décrite marque un saut qualitatif par rapport aux approches RAG standard :

- **Recherche à deux couches (Layered Research)** : Au lieu d'une recherche unique, le système analyse les résultats, identifie les angles morts et lance une recherche ciblée.
  - *Applicabilité Hermes* : Ce schéma est directement implémentable pour automatiser la "discipline des sources" (identification des lacunes).
- **Orchestration Multi-Agents (Approche Anthropic)** : La décomposition d'une tâche complexe en sous-agents spécialisés travaillant en parallèle.
  - *Comparaison* : Notre système actuel de délégation (agent "Lead" vs subagents) est une forme embryonnaire de ce modèle. L'industrialisation de cette approche permettrait de scaler la complexité des recherches sans allonger le temps d'exécution.

## 3. Implications pour la R&D et la Souveraineté
Le passage de l'usage d'outils "boîtes noires" (Perplexity) à des agents souverains (notre propre implémentation) est une nécessité pour l'émancipation des services tiers.

- **Avantages** :
    - Maîtrise totale de la chaîne (recherche -> inférence -> synthèse).
    - Adaptabilité aux besoins spécifiques du dépôt (connaissance des doctrines, structure du wiki).
- **Risques** :
    - Complexité d'orchestration (gestion des tokens, latence des subagents, gestion des erreurs).

## 4. Recommandations
1. **Intégration d'une fonction de recherche itérative** : Développer une fonction Hermes inspirée du "deeper_research_topic" pour améliorer la précision des recherches automatiques.
2. **Standardisation de la délégation** : Utiliser le modèle multi-agents décrit (Lead agent + subagents parallèles) pour traiter les demandes de recherche complexes dans le dépôt.

*Note : Cette analyse valide l'intérêt technique des concepts pour le pôle R&D. L'implémentation opérationnelle fera l'objet d'un ticket Infrastructure distinct.*
