---
title: "Cordis — notes de lecture"
type: fiche-veille
statut_experience: exploratoire
source: "raw/A Programming Paradigm for Spatiotemporal Composability.pdf"
auteurs: "Yifan Shi (Peking Univ), Wei Zhang, Tianyi Cui (DeepSeek-AI)"
created: 2026-08-18
updated: 2026-08-18
tags: [cordis, lecture, paradigme, sashimono, resonances]
sources: []
links:
  - "[[atelier/rd/veille/index]]"
  - "[[atelier/rd/veille/cordis/equations]]"
  - "[[atelier/rd/veille/cordis/methodes]]"
  - "[[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]"
---

# Cordis — notes de lecture

> **Note de lecture** : cette fiche porte les observations, résonances,
> questions ouvertes. Pas de paraphrase — ce qui est déjà dans les
> équations et méthodes. Ce qui suit est le discernement qualitatif du
> lecteur.

---

## I. Résonance avec Sashimono

Le paradigme Cordis résonne de forme avec la convention Sashimono du
dépôt :

| Cordis | Sashimono |
|---|---|
| Effet réversible (inverse explicite) | Démontage sans joint forcé |
| Composant qui se retire sans laisser de trace | Pièce qui se retire à blanc |
| Teardown dérivé du chargement | Montage à blanc, pas de colle |
| Indépendance par équivalence observationnelle | Indépendance par absence de dépendance implicite |

**Ce qui résonne** : l'idée qu'un composant puisse être retiré sans
endommager le système, sans laisser de résidu, sans dépendance cachée.
C'est la même intuition que Sashimono : le démontage est la condition du
montage.

**Ce qui diffère** : Cordis est un paradigme d'ingénierie logicielle
(temps, espace, types, runtime) ; Sashimono est une convention de
dépôt (fichiers, circuits, invariants). La résonance est structurelle,
pas opérationnelle.

---

## II. Applicabilité au dépôt

### Chantier 1 — HMR pour les 12 agents

Les 12 agents du dépôt (Hermes, Studio Sound Engineer, etc.) sont
actuellement chargés au démarrage, pas remplaçables à chaud. Le
paradigme Cordis pourrait permettre :
- Remplacement d'un agent sans redémarrage du système hôte (gateway
  Hermes).
- Revert automatique des effets cumulés (fichiers modifiés, mémoire
  écrite, cron jobs créés) si l'agent est retiré.
- Dépendances déclaratives entre agents (ex. Studio Sound Engineer
  dépend de Hermes pour l'accès au dépôt).

**Question ouverte** : comment modéliser les agents comme composants
Cordis ? Quelle est l'API d'effet d'un agent ? Quel est son inverse ?

### Chantier 2 — Gestion des dépendances inter-gateways

Plusieurs gateways Hermes peuvent coexister (profil default, profil
gardien, etc.). Le paradigme Cordis pourrait permettre :
- Dépendances déclaratives entre gateways (ex. profil gardien dépend de
  profil default pour l'accès à certaines fiches).
- Isolation par réalmes (chaque profil a son propre store de mémoire).
- Notification réactive quand un profil change d'état.

**Question ouverte** : comment modéliser les gateways comme composants
Cordis ? Quelle est l'API d'effet d'une gateway ?

### Chantier 3 — Veille R&D comme effet réversible

La veille R&D (présente extension) produit des fiches, des notes, des
liens. Ces effets pourraient être modélisés comme réversibles :
- Si une fiche de veille est invalidée, son retrait revert les liens,
  les notes, les références.
- Pas de résidu : la fiche invalidée ne laisse pas de trace dans les
  autres fiches.

**Question ouverte** : comment modéliser les fiches de veille comme
effets réversibles ? Quelle est l'API d'effet d'une fiche ?

---

## III. Limites et questions ouvertes

### Limite 1 — Effets non réversibles

Certains effets ne sont pas réversibles par nature :
- Envoi d'un email, d'un message, d'une notification.
- Écriture sur un disque externe (non contrôlé par le runtime).
- Action irréversible sur un service tiers (suppression de données).

**Question** : comment le paradigme Cordis traite-t-il ces effets ? Le
papier mentionne la "withholding and compensation" (§6.1) mais ne détaille
pas. À instruire.

### Limite 2 — Cycles de dépendance

Le papier mentionne que les cycles de dépendance laissent les composants
permanemment inactifs (pas de deadlock, mais pas d'activation non plus).
C'est prévisible dès le chargement.

**Question** : comment détecter les cycles dans le dépôt ? Les 12 agents
ont-ils des dépendances cycliques ? À instruire.

### Limite 3 — Overhead de l'effect tracking

Le papier ne donne pas de benchmarks. L'effect tracking (stockage des
inverses, composition, revert) a un coût en mémoire et en temps.

**Question** : quel est l'overhead pour un système de 12 agents ?
Acceptable ? À instruire.

---

## IV. Ce qui reste à lire

- [ ] Discussion complète (§6) : granularité des composants, cycles de
  dépendance, language-independence.
- [ ] Related work (§7) : comparaison avec les systèmes d'effets et
  coeffects statiques, paradigmes de programmation, composabilité
  temporelle et spatiale.
- [ ] Conclusion (§8) : synthèse des contributions, perspectives.

---

## Liens

- Équations clés : [[atelier/rd/veille/cordis/equations]]
- Méthodes d'implémentation : [[atelier/rd/veille/cordis/methodes]]
- Fiche d'instruction globale :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
