---
title: "Piste — SRS (Mnemosyne / Anki) pour l'assimilation du protocole"
type: outillage
statut: brouillon
tags: [rd, outillage, protocole, memoire, assimilation, hermes, srs]
created: 2026-08-15
updated: 2026-08-15
sources: []
links: ["[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]", "[[atelier/rd/cahiers/registre-problemes]]"]
---

# Piste — SRS pour l'assimilation du protocole (CLAUDE.md)

> **Statut** : `brouillon`, non visé pour les sections d'implémentation
> (§VI, §VII). Le §I–V est constat + instruction. Le §VII porte un verdict
> Sidy du 2026-08-15 : **intégration Hermes-native** (sous-système de cartes
> auto-générées depuis CLAUDE.md dans la mémoire Hermes), à la place d'un
> SRS tiers (Mnemosyne, Anki). Ce verdict ne clôt pas la fiche : l'écriture
> du script et du format de carte font l'objet d'une fiche ultérieure
> (§VIII).

---

## I. Objet de la fiche

Cette instruction est ouverte pour répondre à un double constat :

1. **Optimisation infrastructure Hermes** : la mémoire des agents Hermes
   (`memory` tool) est injectée automatiquement dans chaque session — mais
   certains éléments protocolaux ne sont pas systématiquement respectés
   malgré cette injection : violations, redemandes, frictions sur Cmd 9 /
   Cmd 12 / nommage Karūbī (cf. registre 2026-08-13, symptômes 2 et 3).
   Le problème n'est pas l'injection, c'est la rétention et l'application
   cohérente des règles denses (~10 000 mots de protocole).

2. **Assimilation côté utilisateur (Sidy, CLI iPad)** : le protocole
   (CLAUDE.md racine + 5 CLAUDE.md de circuits) est dense (~10 000 mots)
   et sa lettre (Cmd 1 à 13, interdits de liens, nomenclature sashimono,
   table Karūbī ↔ destinataire, zones scellées vs croissance) demande une
   révision régulière pour être tenue sans friction.

Sidy vient d'entendre parler de **Mnemosyne** (SRS local, équipe de
Maastricht, SM-2 amélioré) ; jamais d'Anki. La fiche instruit les deux à
frais égaux, puis propose une alternative Hermes-native.

---

## II. État du protocole actuellement

### II.1 Ce qui existe

| Artefact | Chargé à chaque session | Persistance |
|---|---|---|
| CLAUDE.md racine | oui (toujours, protocole) | disque (injecté en début de session) |
| CLAUDE.md `doctrinal/` | oui (circuit actif) | disque (injecté si circuit actif) |
| CLAUDE.md `atelier/`, `label/`, `hermeneutique/`, `meta/` | oui (circuit actif) | disque (injecté si circuit actif) |
| `meta/transmissions/registre-silsila.md` | non (consultable sur demande) | disque |
| `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md` | non (archive) | disque |

### II.2 Lacunes observées (registre 2026-08-13)

- **Symptôme 2** : confusion nom du Karūbī / nom du destinataire — la
  table existait en `meta/transmissions/` mais aucun agent ni Sidy ne la
  retenait entre sessions. Résolution : ajout à `meta/CLAUDE.md` (commit
  `6b4871e`).
- **Symptôme 3** : friction sur Cmd 9 (SHA après commit) — la règle est
  dans CLAUDE.md mais n'est pas appliquée mécaniquement.

### II.3 Constat brut

La mémoire Hermes est injectée systématiquement dans chaque session
(visible au début de cette conversation : "MEMORY (your personal notes)
[1,977/2,200 chars]"). Pourtant, certains éléments protocolaux denses
(Cmd 1 à 13, interdits de liens, nomenclature sashimono, table Karūbī ↔
destinataire, zones scellées vs croissance) ne sont pas systématiquement
respectés malgré cette injection. L'injection statique ne garantit pas
l'application cohérente — une révision espacée (SRS) pourrait compléter
l'injection en maintenant les règles en mémoire active, au-delà du simple
effet de présence textuelle.

---

## III. Qu'est-ce qu'un SRS (spaced repetition system)

### III.1 Définition neutre

Un SRS est un système qui présente des items (cartes) à intervalles
croissants, en fonction de la facilité de rappel mesurée à chaque
révision. Le principe sous-jacent (Ebbinghaus, 1885 ; révisé par Wozniak,
1985) : un item correctement rappelé est revu plus tard ; un item oublié
est revu plus tôt.

### III.2 Algorithme SM-2

SM-2 (SuperMemo 2, Wozniak 1987) : chaque carte porte un facteur de
facilité `EF` (initialisé à 2.5) et un intervalle `I`. Après chaque
révision, l'utilisateur note la difficulté (0–5) ; l'algorithme ajuste
`EF` et `I`. C'est l'algorithme historique ; Mnemosyne utilise une
variante affinée (SM-2+), Anki utilise SM-17 (plus récent, moins
documenté publiquement).

### III.3 Pourquoi ça marche pour des textes longs

- Transmission orale traditionnelle (hifz coranique, sanad, poésie) :
  l'espacement régule l'effort sans sacrifier la consolidation.
- Pas de compréhension à réapprendre à chaque session : le SRS maintient
  l'accès à ce qui est déjà compris.

---

## IV. Comparaison Mnemosyne / Anki / alternatives

| Critère | Mnemosyne | Anki | Org-drill (Emacs) | RemNote | SuperMemo |
|---|---|---|---|---|---|
| Licence | GPL 3 | AGPL 3 (core) + add-ons propriétaires | GPL 3 | Propriétaire | Propriétaire (gratuit) |
| Stockage local | SQLite | SQLite | Org-mode | Cloud-first | Windows, local |
| Sync mobile | non (web wrapper) | AnkiWeb (natif) | Syncthorg | native | non |
| Algorithme | SM-2+ | FSRS (1.2+) | SM-2 | SM-2 | SM-17/18 |
| API / script | Python, CLI | Python, CLI, AnkiConnect | Elisp | REST (limité) | COM/CLI |
| Équipe de recherche | Maastricht (actif, publications) | Damien Elmes (solo) | Org-mode community | solo | Wozniak (solo) |
| Force | rigueur cognitive, données locales | écosystème large, sync mobile | intégré Emacs | prise de note + SRS unifiés | algorithme le plus avancé |
| Faiblesse | pas de mobile natif | AGPL, addons payants | Emacs-only | cloud, moins de contrôle | Windows, ancien UI |

**Recommandation comparée** :
- Mnemosyne : choix naturel si usage strictement local/serveur, pas de
  sync mobile nécessaire.
- Anki : choix naturel si sync iPad nécessaire.
- Ni l'un ni l'autre ne résout le cas spécifique Hermes : les cartes
  seraient un artefact extérieur au système, à maintenir en parallèle du
  protocole.

---

## V. Application au protocole Hermes — ce qui pourrait devenir cartes

Catalogue des éléments protocolaux éligibles à la mémorisation par SRS :

### V.1 Les 13 commandements absolus (Cmd 1 à 13)

13 cartes minimum, une par commandement. Possiblement éclatées si un Cmd
comporte plusieurs règles distinctes.

### V.2 Interdits de liens (sens uniques entre circuits)

~15 règles : `doctrinal/ → hermeneutique/` interdit, `label/ → meta/`
interdit, `atelier/ → label/` interdit, etc.

### V.3 Nomenclature sashimono

4 termes : zōsaku (portance nulle), hozo (tenon, portance structurelle),
kari-kumi (assemblage à blanc), kumiko (assemblage validé). 4 cartes, ou
une carte comparative.

### V.4 Frontmatter Sceau (circuits × types)

5 circuits × ~8 types = ~40 combinaisons possibles. Pas toutes éligibles :
la fiche peut cibler les cas ambigus (ex. `type: source` en
`hermeneutique/` vs `doctrinal/`).

### V.5 Table Karūbī ↔ destinataire

4 Karūbī (Mehdi, Mikael, Jean-Marc, Habib/Nour). 4 cartes.

### V.6 Vocabulaire technique

~20 termes : navette, canonique, zones scellées, zones de croissance,
INSERTION (EN-TÊTE/QUEUE), sashimono, Gizeh, VIGILANCE, etc.

**Estimation brute** : ~80–120 cartes pour couvrir le protocole entier.

---

## VI. Deux usages distincts — problème posé avant le verdict

### VI.1 Usage A : agents Hermes

La mémoire Hermes (`memory` tool) est injectée automatiquement dans
chaque session. Le problème n'est pas la disponibilité : c'est que, malgré
l'injection, certains éléments protocolaux ne sont pas respectés
cohéremment — violations, redemandes, frictions (cf. registre 2026-08-13,
symptômes 2 et 3). Hypothèse : l'injection statique ne suffit pas à
garantir l'application active ; une révision espacée (SRS) pourrait
compléter l'injection en maintenant les règles protocolales en mémoire
active, par-delà l'effet de simple présence textuelle.

### VI.2 Usage B : Sidy en CLI

Révision personnelle du protocole. Deux formes possibles :

- **Cron Hermes** : un job planifié (hebdomadaire ?) génère une session de
  cartes (fiche CLI imprimable) à partir du protocole, à réviser avant
  ouverture de session wiki.
- **Drill interactif** : une commande Hermes qui, avant chaque session
  wiki, pose 5 cartes aléatoires du protocole et attend la réponse avant
  de charger le prompt.

Forme à trancher.

---

## VII. Recommandation (verdict Sidy, 2026-08-15)

**Verdict tranché** : intégration Hermes-native. Pas de SRS tiers
(Mnemosyne, Anki) — le sous-système de cartes est généré automatiquement
depuis CLAUDE.md et vit dans la mémoire Hermes (`MEMORY.md` ou extension).

### VII.1 Ce que le verdict implique

- Le protocole (CLAUDE.md) est la source unique ; les cartes sont
  extraites automatiquement, jamais saisies à la main dans un SRS tiers.
- Le stockage est dans la mémoire Hermes (fichier markdown, pas SQLite,
  pas cloud).
- La révision peut être déclenchée manuellement (commande Hermes) ou
  automatiquement (cron Hermes avant session).

### VII.2 Ce que le verdict ne clôt pas

- Le format de carte (question / réponse, frontmatter dédié, ou simple
  entrée `MEMORY.md` ?).
- Le script d'extraction (depuis CLAUDE.md → cartes).
- Le mécanisme de révision (cron, commande, ou injection systématique
  dans le prompt ?).
- L'algorithme d'espacement (SM-2, simplifié, ou aucun — présentation
  aléatoire ?).

Ces questions font l'objet d'une fiche ultérieure (§VIII).

---

## VIII. Non inclus

Ce qui n'est pas instruit ici, et fait l'objet d'une fiche ultérieure
(conditionnelle au verdict ci-dessus) :

- **Format de carte** : structure exacte d'une carte (question/réponse,
  frontmatter, tags).
- **Script d'extraction** : `generer-cartes-protocole.py` (ou extension
  Hermes-native) lisant CLAUDE.md et produisant les cartes.
- **Mécanisme de révision** : commande Hermes (`hermes drill`), cron
  hebdomadaire, ou injection systématique dans le prompt d'ouverture.
- **Algorithme d'espacement** : SM-2 simplifié, ou présentation aléatoire
  sans espacement (la mémoire Hermes n'étant pas injectée systématiquement,
  l'espacement reste pertinent pour les sessions de révision ciblées).

---

## IX. Liens

- Registre des problèmes : `atelier/rd/cahiers/registre-problemes.md`
  (symptômes 2 et 3 de 2026-08-13).
- Infrastructure globale : `atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11.md`
  (architecture Hermes, profils, mémoire).
