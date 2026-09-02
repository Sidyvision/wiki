---
title: "Queue de tâches — idées en attente de déploiement aux agents"
type: meta
created: 2026-08-27
updated: 2026-09-02
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

## [2026-09-02] etendre-archive-rapports-publication | non-assigné | en attente | haute

**Description** : étendre `atelier/rd/infrastructure/monitoring-archive-charte.md`
au job Publication `veille-referencement-investigation-08` (profil
`publication`), sur le modèle exact de l'archivage déjà en place pour Studio
(`archiver-monitoring-quotidien.py`, cron dédié `10 12 * * *`) — copier ce que
Hermes persiste déjà sur disque
(`/root/.hermes/profiles/publication/cron/output/`) vers un dossier
équivalent, avec la même rétention de 40 jours.
**Contexte** : session d'INTÉGRATION du 2026-09-02. Sidy a dû coller
lui-même deux rapports Publication dans la conversation, faute d'archive
mécanique — geste qu'il ne devrait pas avoir à refaire. Consigné `INF-15`
dans `atelier/rd/registre-chantiers.md`. Nécessite un accès au serveur Hermes
(création de job cron) : hors de portée d'une session Claude Code distante
comme celle qui consigne cette idée.
**Agent(s) concerné(s)** : non-assigné (accès serveur requis — Sidy ou
session avec terminal Hermes).
**Priorité** : haute
**Statut** : en attente
**Traité le** :
**Résultat / lien** : `atelier/rd/registre-chantiers.md`, ligne `INF-15` ;
`atelier/rd/infrastructure/monitoring-archive-charte.md`.

## [2026-09-02] verifier-redemarrer-gateways-hermes-en-echec | non-assigné | en attente | normale

**Description** : vérifier si les six services `hermes-gateway-*` constatés
en échec dans chaque rapport Studio du 2026-08-28 au 31 (`accounting`,
`admin-legal`, `distribution`, `marketing`, `production`, `visual-da`) sont
censés tourner ou sont dormants par construction (les 9 profils métier étaient
volontairement laissés sur Qwen en attente de reset de quota, cf.
`atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen.md`,
§Hors périmètre) ; le cas échéant, redémarrer via
`systemctl --user restart hermes-gateway-<profil>.service`. Inclut, dans le
même geste, le socket Discord Gardien resté fermé depuis le 2026-08-25
(`registre-problemes.md`, entrée `[2026-08-25]` — bloqué par le filtre de
sécurité Hermes qui refuse tout restart émis depuis un terminal enfant d'un
gateway, requiert un shell extérieur, SSH ou terminal local).
**Contexte** : signalé de façon répétée dans les rapports Studio archivés,
jamais actionné. Nécessite un accès `systemctl`/SSH au serveur : hors de
portée de cette session distante (dépôt git seul).
**Agent(s) concerné(s)** : non-assigné (accès serveur requis).
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** : `atelier/rd/cahiers/registre-problemes.md`, entrées
`[2026-09-02]` et `[2026-08-25]` (« Discord Gateway Gardien »).

## [2026-09-02] verification-humaine-sources-raw-trois-fiches | 08-publication-site | en attente | normale

**Description** : vérifier sur le serveur (`raw/` y est présent, exclu de
git) la présence effective de `Awrad_Ibn_Arabi.pdf`,
`Jesus_And_Enoch_In_Ibn_'arabi.pdf` et `shams-al-maarif-traduit-complet.pdf`,
puis — condition posée par le protocole (§VII racine, discipline des sources,
point 2), non par cette entrée — vérification du **texte primaire** par Sidy
lui-même avant toute levée de `to-source` : `doctrinal/sources/awrad-ibn-arabi.md`,
`doctrinal/sources/jesus-and-enoch-in-ibn-arabi.md`,
`doctrinal/sources/shams-al-maarif.md` (`sources: [], sources_count: 0`
actuellement sur les trois).
**Contexte** : recommandation du rapport Publication du 2026-08-31 (§2,
investigation documentaire), traitée en session le 2026-09-02 mais non
actionnable : `raw/` est intégralement exclu de git, une session distante ne
peut ni confirmer ni infirmer la présence des PDF, et la levée du
`to-source` reste de toute façon un geste humain exclusif.
**Agent(s) concerné(s)** : 08-publication-site (constat de présence) ;
levée du `to-source` réservée à Sidy (Cmd 5, non délégable).
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** : `atelier/rd/cahiers/registre-problemes.md`, entrée
`[2026-09-02]` « Deux rapports Publication collés par Sidy depuis Discord »,
point 3.
