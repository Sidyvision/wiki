---
title: "Proposition — Cycle de Consultation (الشورى) entre les 12 agents"
type: meta
tags: [outillage, projet-claude-ai, choura, hermes, gardien, proposition]
created: 2026-08-27
updated: 2026-08-27
---

# Proposition — Cycle de Consultation (الشورى)

> **Statut : validée par Sidy le 2026-08-27, exécution effective complète
> (wiki + câblage cron réel).** Scaffolding wiki créé :
> `meta/projet-unifie/choura/cycle-2026-08-28.md` (premier cycle, ouverture au
> tour du Gardien à 00:00). Câblage infrastructure : un job cron ajouté à
> chacun des 12 profils `.hermes` (`/root/.hermes/profiles/<role>/cron/jobs.json`),
> cadence 2h, ordre calé sur la table zodiacale validée (§9,
> `17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md`), Gardien en
> position d'ouverture/clôture (00:00). Règle d'affinité (zodiaque/rôle) pour
> les matières hors-périmètre strict explicitement intégrée aux prompts.
> Aucun redémarrage de service ni push wiki effectué dans ce chantier (hors
> périmètre demandé).

## 1. Constat — un dispositif réellement nouveau

L'exploration du dépôt ne fait apparaître **aucun** mécanisme de délibération
tournante existant. Ce qui existe aujourd'hui :

- des **tensions structurelles pairées**, volontaires et non hiérarchiques
  (ex. Gardien (10) ↔ Commerce (12), documentées dans
  `meta/projet-unifie/proposition-pole-fiqh-2026-07-06.md`) ;
- le **Rapport du matin**, point de synchronisation quotidien mais **descendant
  vers Sidy**, pas un espace de délibération entre agents ;
- le **double contrôle systématique** (sashimono + confrontation Gizeh,
  `CLAUDE.md` racine §VII) — des contrôles de relevé appliqués à une
  production donnée, pas une consultation ouverte.

Le Cycle de Consultation proposé par Sidy est donc à traiter comme une
**pièce neuve du protocole**, pas un ajustement d'un mécanisme existant — et
signalé comme tel plutôt qu'artificiellement rattaché à un dispositif
antérieur.

## 2. Proposition — la boucle

- **Cadence** : 24 heures, boucle reprise indéfiniment (poursuite jusqu'à
  arrêt explicite de Sidy).
- **Point de départ et de clôture** : le Gardien (agent 10) — cohérent avec
  son rôle transversal de vigilance protocolaire.
- **Rotation** : les 12 rôles dans leur ordre déjà établi
  (`01-ar-music-artistic-direction` → … → `12-commerce-profitability`), puis
  retour au Gardien.
- **Contribution attendue à chaque tour** : l'agent s'exprime depuis son
  propre rôle sur trois axes — (a) ses tâches en cours, (b) l'état du dépôt
  tel qu'il le perçoit depuis son poste, (c) ses perspectives/objectifs — **en
  s'appuyant explicitement sur la contribution du précédent**, pas en
  parallèle isolé. C'est un relais, pas douze monologues.
- **Clôture** : au retour au Gardien, synthèse du tour complet — ce qui a
  émergé, ce qui reste en tension, ce qui mérite un signalement à Sidy.
- **Interjection de Sidy** : possible à tout moment, sur n'importe quel tour.
  Le cycle ne l'ignore pas : l'agent en cours (ou le Gardien si le cycle est
  entre deux tours) intègre l'interjection dans sa propre contribution ou
  provoque une synthèse anticipée si l'interjection le justifie.

## 3. Esquisse d'outillage

- **Support** : fichier append-only dédié par cycle,
  `meta/projet-unifie/choura/cycle-YYYY-MM-DD.md` (un fichier par jour,
  ouvert par le Gardien à son tour d'ouverture, clos par lui 24h plus tard) —
  évite qu'un unique fichier glissant grossisse indéfiniment ; l'archivage
  quotidien donne une trace nette par cycle (Cmd 9 — journalisation).
- **Cadence par agent** : 24h / 12 rôles ≈ 2h par agent. Chaque tour est une
  entrée datée-horodatée dans le fichier du jour :
  ```markdown
  ## [HH:MM] agent-slug (role)
  **S'appuyant sur** : [ce que le précédent a soulevé, en une phrase]
  **Tâches en cours** : …
  **État du dépôt perçu** : …
  **Perspective / objectif** : …
  ```
- **Mécanique de relais** : le job cron de chaque agent, à l'heure de son
  tour, lit la dernière entrée du fichier du jour, rédige la sienne, et
  déclenche (ou laisse le cron suivant démarrer normalement) le tour de
  l'agent suivant. Un canal Discord dédié « choura » (cohérent avec
  l'architecture Discord existante à allowlist stricte,
  `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`) peut
  miroiter le fichier pour que Sidy suive et interjecte en direct sans passer
  par le dépôt.
- **Le Gardien** : job cron à J, 00:00 (ouverture, éventuelle synthèse du
  cycle précédent) et à J+1, 00:00 (clôture/synthèse du cycle en cours) —
  ou toute autre heure de rotation fixe à trancher par Sidy.

## 4. Garde-fous (non négociables)

- **Autorité de signalement seulement** (§VIII.6, Cmd 13) : la consultation
  produit des perspectives et des signaux, jamais une décision exécutoire.
  Toute action qui engage (dépense, contrat, publication, verdict de
  discernement) issue d'un tour de choura repasse par Sidy comme n'importe
  quel autre canal.
- **Aucun verdict métaphysique** (Cmd 12) : un agent peut signaler une
  tension doctrinale perçue, jamais la trancher — renvoi vers
  `doctrinal/discernement/` ou vers Sidy comme d'habitude.
- **Anti-remplissage** : une contribution qui ne fait que paraphraser la
  précédente sans rien ajouter est un signal de dérive du dispositif, pas une
  vraie consultation — à surveiller particulièrement en cas de charge faible
  (agents sans tâche réelle ce jour-là). Prévoir une clause explicite : un
  agent peut légitimement contribuer « rien de neuf de mon côté aujourd'hui »
  plutôt que de meubler.
- **Étanchéité inter-circuits inchangée** (§VI racine) : un agent du pôle
  label ne fait pas remonter de fait personnel de `meta/` dans sa
  contribution, même dans cet espace de parole élargi.
- **Traçabilité** (Cmd 9) : chaque cycle clos est archivé, jamais perdu — le
  fichier quotidien fait office d'annale du dispositif.

## 5. Points ouverts

- Cadence exacte de rotation (2h fixe, ou variable selon charge réelle des
  agents) : à trancher par Sidy après un premier cycle d'essai.
- Faut-il un mode « cycle allégé » les jours sans matière (éviter la
  paraphrase forcée évoquée au §4) ?
- Articulation avec la Queue de tâches
  (`proposition-queue-taches-2026-08-27.md`) : le cycle pourrait devenir un
  lieu naturel où une idée émergente d'un agent est proposée pour la queue —
  à examiner si les deux propositions sont validées ensemble.
- Le Gardien portant à la fois l'ouverture/clôture de la choura et son rôle de
  vigilance protocolaire (§10 des prompts Hermes) : vérifier que la charge
  cumulée ne dilue pas sa fonction première de dire non.
