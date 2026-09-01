---
title: "Proposition — Queue de tâches et déploiement aux agents"
type: meta
tags: [outillage, projet-claude-ai, queue, hermes, proposition]
created: 2026-08-27
updated: 2026-08-27
---

# Proposition — Queue de tâches et déploiement aux agents

> **Statut : validée par Sidy le 2026-08-27, exécution effective.** Fichier
> réel créé : `meta/projet-unifie/queue-idees.md`. Deux des points ouverts du
> §5 sont tranchés à la validation :
> 1. **Champ `priorite`** : adopté (`haute | normale | basse`), obligatoire à
>    la création de chaque entrée.
> 2. **Marqueur d'insertion** : `QUEUE` (chronologique direct), même
>    convention que `meta/transmissions/registre-silsila.md`.
>
> Présente fiche conservée comme fiche de conception (archive), au même titre
> que `proposition-pole-fiqh-2026-07-06.md`.

## 1. Constat

Aucun mécanisme de file d'attente n'existe actuellement dans le dépôt. Le seul
mécanisme de circulation de tâches est le sas `_inbox/` + `UPDATES.md`
(`CLAUDE.md` racine §IX), qui sert **l'intégration de contenu déjà rédigé**,
pas la **capture d'idées en vrac** en attente de traitement. Sidy formule le
besoin ainsi : « J'ai beaucoup d'idées sans avoir le temps de toutes les
exécuter. Cette option me permettra d'en garder une trace et qu'elles soient
déployées aux agents appropriés automatiquement. »

## 2. Proposition — le fichier de queue

Fichier réel : `meta/projet-unifie/queue-idees.md`, append-only (marqueur
`<!-- INSERTION: QUEUE -->`, cf. §VII racine — « Convention d'insertion »).

Format d'entrée (tel qu'implémenté, champ `priorite` inclus) :

```markdown
## [YYYY-MM-DD] slug-idee | agent_cible | statut | priorite

**Description** : formulation de l'idée, aussi brute que nécessaire.
**Contexte** : d'où vient l'idée (conversation, observation, besoin repéré).
**Agent(s) concerné(s)** : un ou plusieurs slugs parmi les 12 rôles
  (`01-ar-music-artistic-direction`, ..., `12-commerce-profitability`,
  `13-librarian-archivist`), ou `non-assigné` si le tri reste à faire.
**Priorité** : haute | normale | basse
**Statut** : `en attente | assignée | en cours | traitée | abandonnée`
**Traité le** : YYYY-MM-DD (rempli à la clôture)
**Résultat / lien** : fiche produite, décision prise, ou motif d'abandon.
```

Chaque entrée reste dans le fichier même une fois `traitée` (traçabilité
intégrale, Cmd 10 — jamais de suppression sèche). Une revue périodique peut
archiver les entrées closes anciennes vers un fichier `queue-idees-archives.md`
sur le même modèle que les navettes Karūbī, si le volume le justifie.

## 3. Esquisse de dispatch aux agents

Objectif : qu'une idée assignée à un agent lui « arrive » sans action manuelle
répétée de Sidy, tout en respectant la règle de signalement (§VIII.6) et la
porte humaine (Cmd 13).

- Chaque job cron d'agent (`~/.hermes/profiles/<agent>/cron/jobs.json`,
  architecture existante — cf. `meta/projet-unifie/
  15-architecture-discord-hermes-2026-08-07.md`) gagne une étape de lecture
  qui filtre `queue-idees.md` sur les entrées où `agent_cible` correspond à
  son propre rôle et `statut: en attente`.
- Ces entrées remontent dans le **Rapport du matin** du jour, sous une
  nouvelle section « Queue » — cohérent avec la fonction déjà établie du
  Rapport du matin comme signalement pur (verdicts en attente, tâches de
  l'humain, signaux, échéances, état des sas).
- L'agent peut lui-même faire progresser le statut `en attente → assignée →
  en cours` pour signaler qu'il s'en saisit — c'est un geste de
  **signalement**, pas une décision qui engage.
- Le passage à `traitée` reste réservé à Sidy pour toute idée dont l'issue
  engage (dépense, contrat, publication, verdict de discernement — Cmd 13).
  Pour une tâche non-engageante de pure recherche ou rédaction (ex. un
  brouillon d'étude, une compilation de sources), l'agent a l'autorité de
  clore lui-même en `traitée`, à charge pour lui de motiver ce choix dans le
  champ Résultat — cohérent avec l'autorité de signalement déjà reconnue aux
  agents (§VIII.6).

## 4. Gouvernance

- Seule Sidy, ou une session Claude Code opérant sous un plan validé, ajoute
  de **nouvelles** entrées à la queue (le dépôt d'idée elle-même engage la
  file, donc relève de Cmd 6/13).
- Les agents ne modifient que le `statut` et les champs `Traité le` /
  `Résultat` des entrées qui leur sont assignées — jamais le texte de la
  Description ou le Contexte d'origine (immuabilité de l'énoncé, à l'image de
  `created:` immuable, Cmd 8).
- Toute idée non-assignée (`agent_cible: non-assigné`) reste visible dans le
  Rapport du matin du Gardien (10), dont le rôle transversal de vigilance
  protocolaire en fait le point de tri naturel — à confirmer par Sidy plutôt
  qu'imposé par cette proposition.

## 5. Points ouverts

- ~~Marqueur d'insertion (`EN-TÊTE` vs `QUEUE`) pour `queue-idees.md`~~ —
  **tranché 2026-08-27 : `QUEUE`.**
- ~~Faut-il un champ `priorite` (haute/normale/basse) ?~~ — **tranché
  2026-08-27 : oui, adopté tel que formulé (haute/normale/basse),
  obligatoire dès la première entrée.**
- Articulation avec le Cycle de Consultation (voir
  `proposition-cycle-consultation-choura-2026-08-27.md`) : le cycle pourrait
  devenir un canal naturel où les agents remontent des idées vers la queue,
  plutôt que l'inverse — à examiner conjointement si les deux propositions
  sont validées.
