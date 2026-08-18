---
title: "Cordis — méthodes d'implémentation"
type: fiche-veille
statut_experience: exploratoire
source: "raw/A Programming Paradigm for Spatiotemporal Composability.pdf"
auteurs: "Yifan Shi (Peking Univ), Wei Zhang, Tianyi Cui (DeepSeek-AI)"
created: 2026-08-18
updated: 2026-08-18
tags: [cordis, implementation, typescript, koishi, hmr, ctx-effect]
sources: []
links:
  - "[[atelier/rd/veille/index]]"
  - "[[atelier/rd/veille/cordis/equations]]"
  - "[[atelier/rd/veille/cordis/notes-lecture]]"
  - "[[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]"
---

# Cordis — méthodes d'implémentation

> **Note de lecture** : cette fiche extrait les choix de méthode
> (architecture, API, patterns) du papier, sans paraphrase. Chaque
> méthode est donnée dans son contexte minimal (quel problème elle
> résout, quelle propriété elle garantit).

---

## I. Bibliothèque centrale (§5.1)

### Primitive unique — `ctx.effect(...)`

**Tout** `ctx.provide(key, value, realm)`, `ctx.get(key)`, instantiation
de composant, et toute autre opération mutante passe par `ctx.effect`.

**Méthode** : toute mutation est automatiquement tracée (inverse stocké)
et revertée au déchargement. Pas de teardown manuel.

**Avantage** : le développeur fournit l'inverse de chaque opération
atomique ; l'inverse de toute composée suit par composition (§3.1). Le
teardown d'un composant est **dérivé de son chargement**, pas écrit en
parallèle.

### Algorithmes clés (§5.1.1)

- **Effect tracking** : accumulateur des inverses dans l'ordre inverse
  d'application.
- **Coeffect operations** : résolution deux-couches (`k → ρ(k) → σ(ρ(k))`)
  avec isolation par réalmes.
- **Component lifecycle** : machine à états (Inactif → Actif → Unloading
  → Inactif) ; transitions déclenchées par satisfaction/insatisfaction
  des coeffects.
- **Context access** : `ctx.get(key)` et `ctx.provide(key, value, realm)`
  comme seules API publiques.

---

## II. Chargeur de composants (§5.2)

### Configuration déclarative (§5.2.1)

Les composants sont décrits par une configuration (fichier ou objet) :
- Nom du composant
- Dépendances (coeffects requis)
- Réalmes (isolation spatiale)
- Hooks de lifecycle (optionnels, pour logique spécifique)

**Méthode** : pas de code de chargement ; le chargeur lit la config,
résout les dépendances, et déclenche l'activation quand tous les
coeffects sont satisfaits.

### Hot Module Replacement (§5.2.2)

**HMR** : remplacement à chaud d'un composant = chargement d'un nouveau
+ retrait de l'ancien, **sans redémarrage** du système hôte.

**Méthode** :
1. Nouveau composant chargé comme fibre additionnelle
2. Nouveau composant atteint l'état `ACTIVE`
3. Trafic basculé progressivement (poids ajustables)
4. Ancien composant retiré (revert de ses effets)

**Garantie** : continuité de service, pas de temps d'arrêt, pas de perte
d'état accumulé (caches, connexions, calculs partiels).

---

## III. Cas d'étude — Koishi (§5.3)

### Framework hôte

**Koishi** : framework de chatbots TypeScript, 600+ plugins dans la
nature (au moment de l'écriture du papier).

### Migration

Le paradigme Cordis a été rétro-appliqué à Koishi :
- **Avant** : plugins chargés manuellement, pas de HMR, pas de revert
  automatique, dépendances non déclaratives.
- **Après** : plugins comme composants Cordis, HMR, revert automatique,
  dépendances déclaratives et résolues réactivement.

### Métriques d'adoption

- **600+ plugins** migrés vers le paradigme Cordis (adoption
  communautaire).
- **Pas de breaking change** pour les plugins existants (rétro-compat).
- **Réduction du code de teardown** : la plupart des plugins n'ont plus
  besoin de méthode `deactivate()` manuelle.

---

## IV. Patterns d'ingénierie extraits

### Pattern 1 — Inversion explicite

Chaque opération atomique fournit son inverse. Exemple :
- `register(event, handler)` → inverse : `unregister(event, handler)`
- `set(key, value)` → inverse : `restore(key, oldValue)`

**Avantage** : le teardown est dérivé, pas écrit. Moins de bugs, moins
de code.

### Pattern 2 — Isolation par réalmes

Deux composants peuvent demander la même clé `k` mais être liés à des
valeurs différentes selon leur réalme `ρ(k)`. Exemple :
- Plugin A demande `k = "logger"` dans réalme `ρ_A`
- Plugin B demande `k = "logger"` dans réalme `ρ_B`
- Chaque plugin reçoit son propre logger isolé.

**Avantage** : pas de conflit de noms, pas de dépendance accidentelle.

### Pattern 3 — Notification réactive

Quand un coeffect change (nouveau provider, retrait, remplacement), le
runtime notifie tous les composants dépendants. Exemple :
- `ctx.provide("db", newDb, "realm1")` → tous les composants qui
  dépendent de `"db"` dans `"realm1"` sont notifiés.
- Si un composant perd son provider (retrait), il passe en état
  `INACTIF` (dépendance non satisfaite).

**Avantage** : pas de polling, pas de stale references, pas de crash
silencieux.

### Pattern 4 — HMR sans redémarrage

Remplacement d'un composant = chargement du nouveau + retrait de
l'ancien. Le système hôte ne redémarre jamais. Exemple :
- Chatbot en production, plugin de modération à mettre à jour.
- Nouveau plugin chargé, ancien retiré, trafic basculé.
- Pas de temps d'arrêt, pas de perte de sessions utilisateur.

**Avantage** : continuité de service, pas de perte d'état accumulé.

---

## V. Ce qui reste à instruire

- [ ] Détails de l'API TypeScript (signatures exactes, exemples)
- [ ] Code source de Cordis (dépôt GitHub ?)
- [ ] Benchmarks : overhead de l'effect tracking, latence du HMR
- [ ] Limites : cas où le pattern ne s'applique pas (effets non
  réversibles, dépendances cycliques non détectables statiquement)

---

## Liens

- Équations clés : [[atelier/rd/veille/cordis/equations]]
- Notes de lecture : [[atelier/rd/veille/cordis/notes-lecture]]
- Fiche d'instruction globale :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
