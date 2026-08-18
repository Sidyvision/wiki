---
title: "Cordis — équations clés du paradigme"
type: fiche-veille
statut_experience: exploratoire
source: "raw/A Programming Paradigm for Spatiotemporal Composability.pdf"
auteurs: "Yifan Shi (Peking Univ), Wei Zhang, Tianyi Cui (DeepSeek-AI)"
created: 2026-08-18
updated: 2026-08-18
tags: [cordis, equations, effets-reversibles, coeffets-reactifs, paradigme]
sources: []
links:
  - "[[atelier/rd/veille/index]]"
  - "[[atelier/rd/veille/cordis/methodes]]"
  - "[[atelier/rd/veille/cordis/notes-lecture]]"
  - "[[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]"
---

# Cordis — équations clés du paradigme

> **Note de lecture** : cette fiche extrait les équations structurantes du
> papier, sans paraphrase. Chaque équation est donnée dans son contexte
> minimal (quel problème elle résout, quelle propriété elle garantit).

---

## I. Effets réversibles (§3.1)

### Équation 1 — Transformation pure d'une fonction impure

Toute fonction impure $f_{\text{impure}} : X \to Y$ est transformée en
fonction pure $f : \Gamma \times X \to \Gamma \times Y$ où $\Gamma$ est
le contexte partagé.

**Résolution** : séparation des effets de la logique pure ; le contexte
devient une donnée explicite.

### Équation 2 — Signature d'un effet réversible

Un effet est une fonction de type :

$$\text{eff} : \Gamma \to \Gamma \times (\Gamma \to \Gamma)$$

Appliquée au contexte courant, elle rend :
- le contexte modifié
- son **inverse explicite** $\Gamma \to \Gamma$

**Résolution** : l'inverse n'est pas implicite (comme dans un GC) ; il
est fourni par l'effet lui-même, donc traçable par le runtime.

### Équation 3 — Composition d'effets réversibles (opérateur ⋄)

Si $\text{eff}_1 = (\Gamma_1, g_1)$ et $\text{eff}_2 = (\Gamma_2, g_2)$,
alors :

$$\text{eff}_1 \diamond \text{eff}_2 = (\Gamma_2 \circ \Gamma_1,\; g_1 \circ g_2)$$

**Propriété** : l'inverse de la composée est la composée des inverses en
ordre inverse. C'est ce qui garantit la réversibilité structurelle.

### Théorème 7 — Récupération du contexte

> Pour toute séquence d'effets réversibles appliquée par un composant,
> l'accumulateur récupère le contexte initial. Reverter la séquence rend
> la main au contexte de départ.

**Garantie** : composabilité temporelle locale.

---

## II. Coeffects réactifs (§3.2)

### Équation 20 — Contexte de coeffect (type dépendant)

Étant donné une famille de types $\mathcal{V} : K \to \text{Type}$, le
contexte de coeffect est le type de fonction partielle dépendante :

$$\Sigma \triangleq (k : K) \rightharpoonup \mathcal{V}_k$$

**Résolution** : le contexte n'est plus une annotation statique ; c'est
un type qui porte l'information de dépendance à l'exécution.

### Équation — Coeffect à une clé (triple)

Un coeffect à une clé $k$ est un triple :

$$(\mathcal{V}_k,\; \simeq,\; \mathcal{A}_k)$$

où :
- $\mathcal{V}_k$ : type de la valeur
- $\simeq$ : équivalence observationnelle
- $\mathcal{A}_k$ : action de notification

**Résolution** : un coeffect n'est pas une donnée plate ; c'est un type
+ une équivalence + une action. L'équivalence est ce qui permet de
détecter un changement (notification).

### Équation — Résolution deux-couches (réalmes)

Pour `ctx.get(key)` :

$$k \to \rho(k) \to \sigma(\rho(k))$$

où :
- $\rho$ : table des réalmes (clé → symbole de réalme)
- $\sigma$ : store des valeurs (réalme → valeur)

**Résolution** : isolation spatiale — deux composants peuvent demander
la même clé $k$ mais être liés à des valeurs différentes selon leur
réalme $\rho(k)$.

---

## III. Unification — Paradigme du contexte (§3.3)

### Équation — Contexte unifié

Le contexte unifié porte à la fois les effets (transformation + inverse)
et les coeffects (dépendances réactives). C'est un **seul type** qui
réifie les deux dimensions.

### Équivalence observationnelle

Sur les coeffects, une relation d'équivalence observationnelle $\simeq$
fournit aux effets leur **indépendance** : deux effets sont indépendants
si leurs coeffects sont observationnellement équivalents.

**Résolution** : l'indépendance n'est plus une propriété syntaxique
(comme dans les systèmes d'effets statiques) ; elle est définie par
observation, donc applicable à des contextes qui évoluent à l'exécution.

---

## IV. Calcul de composition dynamique (§4)

### Composants et fibres

- **Composant** : unité de composition dynamique, porte un effet cumulatif
  et une specification de coeffects.
- **Fibre** : instance d'un composant en cours d'exécution.

### Machine à états du composant

Le composant passe par les états :
- Inactif → Actif (satisfaction des coeffects)
- Actif → Unloading (retrait demandé)
- Unloading → Inactif (tous les effets réversibles ont été reverted)

### Transitions en cours (§4.3)

Le calcul traite :
- **Retrait** (4.3.1) : revert des effets, résolution des dépendants
- **Itération** (4.3.2) : effet cumulatif sur plusieurs pas
- **Asynchronie** (4.3.3) : état inertiel `Unloading` pour laisser le
  teardown asynchrone se terminer
- **Échec** (4.3.4) : reprise après erreur, rollback des effets

### Métathéorie (§4.4)

- **Preservation** (4.4.1) : typage préservé par transition
- **Composabilité temporelle** (4.4.2) : garantie locale étendue au
  système global
- **Composabilité spatiale** (4.4.3) : idem pour les dépendances
- **Progress** (4.4.4) : pas de deadlock structurel (sauf cycle de
  dépendances, qui est prévisible dès le chargement)
- **Confluence** (4.4.5) : ordre d'application des effets sans importance

---

## V. Implémentation — Cordis (§5)

### Primitive unique

Toute mutation du contexte passe par un seul appel : `ctx.effect(...)`.
- Provision de coeffect : `ctx.provide(key, value, realm)`
- Récupération de coeffect : `ctx.get(key)` (deux-couches)
- Instantiation de composant : réduite à un `ctx.effect`
- Toute opération effectuée via le contexte est **automatiquement**
  tracée et revertée au déchargement.

### Cycle de vie

- **Activation** : déclenchée par la satisfaction des coeffects (§3.2)
- **Désactivation** : revert complet des effets cumulés
- **HMR** : remplacement à chaud d'un composant = chargement d'un
  nouveau + retrait de l'ancien, sans redémarrage du système hôte.

---

## VI. Ce qui reste à extraire

- [ ] Détails de l'indépendance des effets (preuve complète)
- [ ] Cas d'étude Koishi : métriques d'adoption (600+ plugins dans la
  nature, selon la fiche outillage)
- [ ] Discussion §6 : granularité des composants, cycles de dépendance,
  language-independence

---

## Liens

- Méthodes d'implémentation : [[atelier/rd/veille/cordis/methodes]]
- Notes de lecture : [[atelier/rd/veille/cordis/notes-lecture]]
- Fiche d'instruction globale :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
