---
title: "Queue de tâches — idées en attente de déploiement aux agents"
type: meta
created: 2026-08-27
updated: 2026-08-27
---

# Queue de tâches

> Dispositif validé par Sidy le 2026-08-27 — voir
> `meta/projet-unifie/propositions/proposition-queue-taches-2026-08-27.md` (fiche de
> conception, archivée). File d'attente d'idées en vrac, en attente de
> traitement par les agents Hermes concernés.
>
> Journal append-only. Une entrée par idée, jamais supprimée (Cmd 10) — le
> statut évolue en place jusqu'à `traitée`/`abandonnée`.
> Format : `## [YYYY-MM-DD] slug-idee | agent_cible | statut | priorite`
> Priorité tranchée par Sidy le 2026-08-27 (point ouvert §5 de la fiche de
> conception, résolu) : `haute | normale | basse`, obligatoire à la création
> de l'entrée.

<!-- INSERTION: QUEUE -->

## Gabarit d'entrée (à copier pour chaque nouvelle idée)

```markdown
## [YYYY-MM-DD] slug-idee | agent_cible | statut | priorite

**Description** : formulation de l'idée, aussi brute que nécessaire.
**Contexte** : d'où vient l'idée (conversation, observation, besoin repéré).
**Agent(s) concerné(s)** : un ou plusieurs slugs parmi les 12 rôles
  (`01-ar-music-artistic-direction`, ..., `12-commerce-profitability`,
  `13-librarian-archivist`), ou `non-assigné` si le tri reste à faire.
**Priorité** : haute | normale | basse
**Statut** : en attente | assignée | en cours | traitée | abandonnée
**Traité le** : YYYY-MM-DD (rempli à la clôture)
**Résultat / lien** : fiche produite, décision prise, ou motif d'abandon.
```

Règles de gouvernance (rappel, cf. fiche de conception §4) :
- Seule Sidy, ou une session Claude Code sous plan validé, ajoute de
  **nouvelles** entrées.
- Les agents ne modifient que `statut`, `Traité le` et `Résultat / lien` des
  entrées qui leur sont assignées — jamais `Description`/`Contexte`/`Priorité`
  d'origine.
- Passage à `traitée` réservé à Sidy pour tout ce qui engage (Cmd 13) ; les
  agents ont autorité de clôture directe uniquement pour une tâche
  non-engageante de recherche/rédaction, motivée dans `Résultat`.

Aucune idée n'est encore en file — dispositif prêt à recevoir sa première
entrée.
