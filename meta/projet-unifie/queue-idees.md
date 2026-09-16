---
title: "Queue de tâches — idées en attente de déploiement aux agents"
type: meta
created: 2026-08-27
updated: 2026-09-16
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
## [2026-09-16] statut-glossaire-unifie | non-assigné | en attente | normale

**Description** : trancher le statut de `atelier/rd/bibliotheque/glossaire-unifie.md`. Mesuré le
2026-09-16 : **33 lignes, ZÉRO terme** — l'inscription contraire du registre (BIB-04, « 1850 termes »)
a été corrigée au titre du Cmd 10. La question n'est pas d'entretien mais de nature : un glossaire
porte **le sens et son attribution** (« selon qui »), un index ne porte que **l'adresse** ; un agrégat
d'adresses ne peut donc pas être un glossaire. Le glossaire réel du vocabulaire technique est **déjà
un livre transcrit au dépôt** — al-Jurjānī, *Le Livre des Définitions* (trad. Gloton), **220
définitions, 0010 à 1864** (catalogue, ligne 85). Verdict attendu : le fichier est-il déclaré
`caduc` ? Rien n'est régénéré ni édité entre-temps (artefact dérivé).
**Contexte** : fiche `atelier/rd/bibliotheque/2026-09-16_trois-organes-lexicaux-et-lisan-al-arab.md`, §3 et §6.1.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** :

## [2026-09-16] perimetre-generateur-validateur-index | non-assigné | en attente | basse

**Description** : `generer-glossaire-unifie.py` sélectionne les fiches sur le **préfixe de nom de
fichier** (`index-`) quand `valider-index-livres.py` borne au **champ** `type: index-livre`. Mesuré :
des 6 fiches `index-*.md`, **5 portent `type: ressource`**, une seule (`index-origine-polaire-tilak.md`)
porte `type: index-livre`. Les deux instruments ne désignent donc pas le même ensemble, et toute
mesure prise sur l'un est à lire avec cette réserve. Aligner sur le **champ** (et non sur le nom)
paraît le sens juste, mais c'est un verdict, non un constat.
**Contexte** : même fiche, §3 et §6.2. Subordonné à l'entrée `statut-glossaire-unifie` : si le
glossaire est déclaré caduc, la moitié de la divergence tombe d'elle-même.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : basse
**Statut** : en attente
**Résultat / lien** :

## [2026-09-16] recomptage-tableau-registre | non-assigné | en attente | basse

**Description** : le tableau de synthèse de `atelier/rd/registre-chantiers.md` (§0) ne se réconcilie
pas pour les pôles **DOC**, **OUT** et **INF**. Réserve Cmd 5 déjà inscrite au registre. **Ces trois
pôles n'ont pas été touchés** par les passes récentes : la cause relevée est formelle — les tableaux
concernés ne portent pas le même nombre de colonnes, de sorte qu'un comptage mécanique uniforme les
lit mal. Recompter et, le cas échéant, uniformiser les colonnes.
**Contexte** : même fiche, §6.3.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : basse
**Statut** : en attente
**Résultat / lien** :


## [2026-09-15] reexamen-rubrique-erudition-academique | non-assigné | en attente | normale

**Description** : réexaminer au critère du type `reference` (adopté le 2026-09-15) les sept fiches
de la rubrique « Érudition académique » du Catalogue doctrinal — Ali Hussain, R. Raphael Afilalo,
Yaqub Chaudhary, Aiman Attar, Titus Burckhardt, Faraz Rabbani, Hamza Yusuf : autorité, ou
référence ? Rien à déplacer d'office ; verdict de Sidy fiche par fiche (Cmd 12).
**Contexte** : proposition `meta/projet-unifie/propositions/proposition-type-reference-2026-09-15.md`,
question 4 — « Plus tard, ajoute à Queue-idée » (Sidy, 2026-09-15). Relevé à trancher au passage :
la fiche Yaqub Chaudhary, rangée sous « Érudition académique », porte `status: traditionnel`.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** :

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
