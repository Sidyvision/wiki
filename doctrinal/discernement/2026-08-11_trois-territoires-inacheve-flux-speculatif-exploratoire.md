---
title: "Trois territoires de l'inachevé — flux spéculatif → exploratoire → finalisé"
type: discernement
status: speculatif
description: >
  Hypothèse méthodologique sur la parenté entre Discernement, R&D et Herméneutique (registre expression),
  leur nature commune (non-finalité, portance zōsaku, validation humanelle), et le flux programmé
  qui les relie : spéculation personnelle → chantier exploratoire → doctrine adoptée ou archivée.
  Sandbox comme dépendance structurelle du R&D.
created: 2026-08-11
updated: 2026-08-11
refs:
  - "CLAUDE.md (§II, §V, §VI, §VII — circuits et régimes)"
  - "meta/philosophie-sashimono.md (Art. 3, 5 — démontabilité, réversibilité)"
  - "_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md (cascade doctrinale)"
  - "atelier/rd/index.md (phase 1 partielle, statut_experience)"
status_experience: exploratoire
---

# Trois territoires de l'inachevé — flux spéculatif → exploratoire → finalisé

## Observation structurelle

Le dépôt accueille trois domaines qui partagent une caractéristique : **ils ne sont jamais finalisés d'office**. Chacun suit un régime propre d'exploration, d'attente, d'hypothèse — et chacun peut *générer* un acte finalisé, mais jamais seul.

| Domaine | Localisation | Nature | Statut | Portance | Validation requise |
|---|---|---|---|---|---|
| **Discernement** | `doctrinal/discernement/` | Spéculation personnelle, hypothèse doctrinale | `status: speculatif` | *zōsaku* — ne porte rien, contingent | Cmd 12 : verdict humain requis avant acte |
| **R&D** | `atelier/rd/` | Exploration expérimentale, chantier en cours | `statut_experience: exploratoire \| reproduit \| adopte \| abandonne` | *zōsaku* — expérimentation réversible tant que non adoptée | Cmd 6 : plan validé avant écriture ; Cmd 13 : porte humaine |
| **Herméneutique (registre: expression)** | `hermeneutique/expression/` | Formulation d'intuitions, exploration d'idées propres | `registre: expression` | *zōsaku* — idée qui existe, reste ouverte | Cmd 12/13 : pas de clôture de discernement, validation avant acte |

**Nature commune** :
- **Non-finalité** : aucun de ces trois n'énonce un acte, une certitude, un état définitif
- **Portance *zōsaku*** (philosophie sashimono) : une extrémité contingente, ne portant rien — réversible, démontable, jamais figé
- **Validation humanelle requise** avant toute transformation en acte (Cmd 13 : porte humaine)
- **Gouvernance transparente** : chacun porte ses propres marqueurs de statut (`speculatif`, `exploratoire`, `expression`)

## Le flux programmé : spéculation → exploration → finalisation

Ce que l'architecture rend possible (et que cette note propose de documenter explicitement) :

### Phase 1 : **Discernement** (spéculation personnelle)
Une hypothèse intéressante naît dans le Discernement. Elle porte :
- Une vigilance doctrinale (références explicites, non-syncrétisme Cmd 3)
- Un statut : `status: speculatif` (en attente de verdict)
- Une portance *zōsaku* : elle ne prétend rien actuer

**Exemple** : fiche sur une correspondance zodiacale hypothétique entre une position astrologique et une fonction d'agent.

### Phase 2 (optionnel) : **Transformation en chantier R&D**
Si une piste du Discernement semble **testable et intéressante**, elle peut migrer vers un chantier du R&D **sans attendre un verdict doctrinal d'abord**. Cette migration :
- Requiert une validation explicite (Cmd 6 : plan avant écriture)
- Change de régime : `status: speculatif` → `statut_experience: exploratoire`
- Entre dans le Sandbox (espace des tests, dépendance structurelle du R&D)
- Reste réversible : peut être reproduit, adopté, ou **abandonné** sans conséquence doctrinale
- N'écrit aucune doctrine tant qu'elle n'est pas finalisée

**Exemple** : le brouillon de l'extension zodiacale des 12 agents H‍ermes est un chantier R&D — spéculation testée, en cours de reproduction et d'optimisation, sans engagement doctrinal avant validation.

### Phase 3 : **Deux destinations**

Un chantier R&D peut déboucher sur deux issues :

#### Option A : **Adoption en Doctrine**
- L'expérimentation a ét≤ suffisamment reproductible, testée, optimisée
- Verdict humain positif (Cmd 12)
- La fiche **migre de R&D vers doctrinal** (ou génère une nouvelle fiche doctrinale qui la reprend)
- Statut final : `status: adopte` (ou intégrée en principe doctrinal stable)

#### Option B : **Archivage**
- L'expérimentation révèle des limites, des incohérences, ou perd de pertinence
- Verdict humain : abandon justifié
- Statut final : `statut_experience: abandonne` (avec motif documenté)
- La fiche reste en R&D comme enregistrement de l'apprentissage, jamais effacée (sashimono Art. 5 : réversibilité tracée)

### Cas spécial : **Herméneutique (expression) ↔ Discernement**
L'herméneutique registre: expression n'est pas destinée à finir en doctrine — c'est une **exploration permanente d'intuitions**. Elle peut :
- **Nourrir** le Discernement (une intuition d'expression intéresse et devient hypothèse doctrinale à explorer)
- **Nourrir** le R&D (une idée d'expression devient un chantier à tester)
- **Rester expression** (exploration ouverte, jamais clôturée, jamais acte final)

Chaque trajet reste volontaire, jamais imposé par la structure.

---

## Le Sandbox comme dépendance structurelle du R&D

**Actuellement** : le Sandbox (`atelier/rd/cahiers/`) existe mais son rôle reste implicite — c'est l'espace des expériences, des brouillons, des reproductions en cours.

**Proposition** : expliciter que le Sandbox est **la poche de travail du R&D**, c'est-à-dire :
- Tout chantier R&D en phase `exploratoire` y vit par défaut (brouillons, cahiers, tests)
- C'est l'espace de **non-finalité programmée** — l'expérimentation y demeure réversible
- Un chantier sort du Sandbox en migrant soit vers :
  - **Doctrine adoptée** (versification définitive, sortie du statut `exploratoire`)
  - **Archivage** (statut `abandonne`, reste en R&D comme enregistrement pédagogique)
- **Rien ne sort du Sandbox sans validation humaine** (Cmd 6, Cmd 13)

Cette explicitation renforce la cohérence plutôt que de la changer : elle nomme une structure qui existe déjà en practice, et la dote d'une clarté architecturale.

---

## Comment cette hypothèse se teste (régime exploratoire)

**Critique interne** :
- Aucune des trois domaines ne devient contraignant par cette documentation — elle décrit seulement comment ils *peuvent* dialoguer
- Chaque transition (Discernement → R&D, R&D → Doctrine) requiert toujours une validation explicite (Cmd 6, Cmd 12)
- Le Sandbox n'acquiert aucun pouvoir d'écriture autonome — il reste un espace de travail supervisé

**Test proposé** :
1. Ajouter cette section à `CLAUDE.md` (§II, sous la description des cinq circuits, ou en appendice §XI « flux intra-repositorium »)
2. Observer si l'**attribution d'un chantier Discernement → R&D** suit ce schéma de manière plus naturelle (ex. : extension zodiacale du brouillon 2026-08-09)
3. Valider auprès de Sidy que cette documentation rend plus claire ou plus cohérente la navigation entre les trois régimes
4. Affiner si certaines transitions sont plus fréquentes/utiles que d'autres

**Abandon possible** : si cette hypothèse s'avère redondante ou complique la lecture de CLAUDE.md, elle peut être intégralement archivée (jamais effacée).

---

## Complémentarité avec le contexte existant

Cette hypothèse enrichit :
- **Protocole du dépôt wiki** (mémoire utilisateur) — gouvernance générale du dépôt
- **Cloisonnement technique H‍ermes** (mémoire utilisateur) — accès FS des agents, hors champ mais connexe à la phase 2 d'une spéculation d'extension
- [[meta/philosophie-sashimono.md]] (art. 3 et 5 : démontabilité, réversibilité)
- [[atelier/rd/index.md]] (charte du pôle R&D, phase 1 partielle)

---

## Verdict attendu

Cmd 12 — jugement humain requis. Sidy détermine si :
1. Cette documentation aide ou complique la navigation du dépôt
2. Le flux proposé (Discernement → R&D → Doctrine/Archivage) est pertinent et opérationnel
3. Une formalisation dans CLAUDE.md (ou son abandon) est justifiée

Tant que le verdict n'est pas rendu, ce texte reste `status: speculatif` — hypothèse architecturale en attente de validation.
