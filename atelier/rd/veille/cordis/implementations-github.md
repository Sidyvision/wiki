---
title: "Implémentations du paradigme Cordis — veille GitHub"
type: fiche-veille
statut_experience: exploratoire
source: "GitHub API (recherche 2026-08-18)"
auteurs: "Divers (communauté open-source)"
created: 2026-08-18
updated: 2026-08-18
tags: [cordis, implementations, github, rust, go, jvm, wasm, langage]
sources: []
links:
  - "[[atelier/rd/veille/index]]"
  - "[[atelier/rd/veille/cordis/equations]]"
  - "[[atelier/rd/veille/cordis/methodes]]"
---

# Implémentations du paradigme Cordis — veille GitHub

> **Scrutation du 2026-08-18** : recherche GitHub sur les mots-clés
> "spatiotemporal composability", "revertible effects", "reactive
> coeffects". 7 repos trouvés, tous implémentations du paradigme Cordis
> dans différents langages.

---

## I. Repos identifiés

| Repo | Langage | Étoiles | Description | Lien |
|---|---|---|---|---|
| **cordis4j** | JVM (Java/Kotlin) | 4 | Cordis meta-framework on the JVM : revertible effects, reactive coeffects, dynamic composition | https://github.com/1na-ko/cordis4j |
| **spatiotemporal** | Rust | 2 | 时空可组合性演算 (calcul de composabilité spatiotemporelle) : effets réversibles, coeffects réactifs, cycle de vie inertiel des fibres | https://github.com/curtiseng/spatiotemporal |
| **stc-go** | Go | 1 | Implémentation Go du paradigme — "the programming model behind Cordis and DeepSeek Harness" | https://github.com/0xdenny218/stc-go |
| **revl** | Langage de recherche | 0 | "A research language for spatiotemporal composability" — langage dédié au paradigme | https://github.com/inso1337/revl |
| **cordis-rs** | Rust + Lua | 0 | Spatiotemporal composability in Rust avec scripting Lua | https://github.com/y0usaf/cordis-rs |
| **cordis-wasm** | WebAssembly | 0 | "Coeffects as Wasm imports" — paradigme Cordis forcé par le sandbox WebAssembly | https://github.com/inso1337/cordis-wasm |
| **spatiotemporal-composability-skill** | Skill agent | 0 | "Agent skill for runtime-recomposable software & agents" — compétence agent pour logiciels/agents recomposables à l'exécution | https://github.com/eSaadster/spatiotemporal-composability-skill |

---

## II. Analyse qualitative

### Ce qui est pertinent

1. **cordis4j** (4★) : implémentation JVM, potentiellement la plus mature (le plus d'étoiles). À scruter en priorité pour comprendre l'API Java/Kotlin.

2. **spatiotemporal** (2★) : implémentation Rust, description en chinois (时空可组合性演算). Intéressant car Rust a une gestion mémoire stricte — comment le paradigme s'articule avec le borrow checker ?

3. **cordis-wasm** : "Coeffects as Wasm imports" — l'idée que le sandbox WebAssembly peut *forcer* le paradigme (pas juste l'implémenter). Résonance avec la sandbox isolée du dépôt.

4. **spatiotemporal-composability-skill** : "Agent skill for runtime-recomposable software & agents" — directement pertinent pour Hermes (comment modéliser les agents comme composants recomposables).

### Ce qui est moins pertinent (pour l'instant)

- **revl** : langage de recherche, pas d'usage pratique immédiat.
- **stc-go** : Go est moins pertinent pour le dépôt (qui est TypeScript/Python).
- **cordis-rs** : Rust + Lua, mais pas d'étoiles — à surveiller, pas à scruter maintenant.

### Questions ouvertes

- Quel est le dépôt source de Cordis lui-même (TypeScript original) ? Les 7 repos sont des réimplémentations.
- Qui est `inso1337` (auteur de 2 repos : revl et cordis-wasm) ? Contributeur clé ou solo ?
- Le repo `spatiotemporal-composability-skill` est-il une skill pour Hermes, Claude Code, ou autre agent ?

---

## III. Prochaines scrutations

- [ ] Scruter **cordis4j** en détail (code source, README, exemples)
- [ ] Scruter **spatiotemporal** (Rust, description en chinois — traduire, comprendre l'articulation avec le borrow checker)
- [ ] Scruter **cordis-wasm** (comment le sandbox Wasm force le paradigme)
- [ ] Scruter **spatiotemporal-composability-skill** (est-ce une skill Hermes ?)
- [ ] Trouver le dépôt source Cordis (TypeScript original)

---

## Liens

- Équations clés : [[atelier/rd/veille/cordis/equations]]
- Méthodes d'implémentation : [[atelier/rd/veille/cordis/methodes]]
- Notes de lecture : [[atelier/rd/veille/cordis/notes-lecture]]
