---
title: "Changelog du protocole CLAUDE.md (racine)"
type: meta
tags: [protocole, historique, changelog]
created: 2026-08-28
updated: 2026-08-29
---

# Changelog du protocole `CLAUDE.md` (racine)

Historique des révisions du protocole racine. Migré hors du préambule de
`CLAUDE.md` le 2026-08-28 pour alléger le contexte chargé à chaque session —
le protocole racine ne conserve qu'un en-tête de statut court avec pointeur
vers le présent fichier. Append-only, ordre chronologique inverse : toute
nouvelle révision du protocole y est consignée immédiatement après le marqueur
ci-dessous (convention d'insertion, amendement 2026-07-27).

<!-- INSERTION: EN-TÊTE -->

## [2026-08-29] clarification | Objet documentaire de la bibliothèque R&D (couvertures, sommaires, index, glossaires)

Demande explicite de Sidy : noter de façon nette, claire et définitive que les
photographies de couverture, sommaire, index et glossaire déposées dans
`atelier/rd/bibliotheque/` (section « Index et glossaires transcrits » de
`catalogue-bibliotheque.md`) sont **strictement documentaires et d'orientation**
— elles permettent de savoir *où chercher* dans un ouvrage physique possédé,
sans nécessiter la numérisation intégrale de la bibliothèque, impossible à
entreprendre en pratique. C'est l'objet même de ce pôle. §VII (Discipline des
sources), point 1 du `CLAUDE.md` racine amendé en conséquence : consultation de
`atelier/rd/bibliotheque/catalogue-bibliotheque.md` rendue **impérative et
prioritaire**, y compris avant tout signalement d'absence d'une œuvre (un agent
qui déclare une œuvre « absente du corpus » sans avoir vérifié ce pôle commet un
signalement prématuré — cas vécu le jour même avec *Hindouisme et Soufisme*,
Shayegan, dont la fiche `sommaire-hindouisme-soufisme.md` existait déjà côté
`atelier/rd/bibliotheque/` au moment où l'absence avait été signalée par excès
de prudence, avant `git pull`). Note renforcée en tête de
`atelier/rd/bibliotheque/catalogue-bibliotheque.md` dans la même passe. Aucun
autre contenu du protocole modifié.

## [2026-08-28] maintenance | Migration de l'historique hors du protocole racine

L'historique des révisions qui vivait en préambule de `CLAUDE.md` (environ
cent lignes, chargées à chaque session) est migré intégralement ci-dessous
(bloc « Historique migré »). Le protocole racine conserve un en-tête de statut
court (dernières révisions, pointeurs d'archive). Corrections de dérive
appliquées dans la même passe : ligne Wendel Nazaire/Hassan ajoutée à la table
Karūbī (`meta/CLAUDE.md`), arbre du §II complété, guide de déploiement
`verifier-invariants.py` déplacé de la racine vers `meta/` et renommé selon la
nomenclature (§III), `meta-index.md` complété (karubi-wendel, briefs/, fiches
de premier niveau manquantes), `README.md` racine actualisé (il décrivait la
structure pré-Restauration), en-tête de l'entrée du 2026-08-25 restauré dans
`meta-annales.md` (perdu au commit d09cc88). Détail complet dans l'entrée
`meta-annales.md` du même jour.

## Historique migré (préambule du protocole racine, 2026-06-11 → 2026-08-22)

Protocole issu de la **Restauration « Guénon V1 »** (2026-06-11, rév. 2026-06-12),
étendu en **V2** le 2026-07-05 (ouverture du quatrième circuit `label/`, postes de
travail rendus agnostiques au modèle, règles de supervision des moteurs locaux,
protocole de publication du site), **révisé le 2026-07-06** : réintégration in extenso
des protocoles d'exécution (le présent fichier doit être auto-suffisant pour tout
moteur), discipline des sources, règle commune des manifestes, supervision étendue des
agents (mémoire, skills, canaux, extension `raw/`), vigilance documentaire, et
**ancrage éthique des actes contractuels et commerciaux du label** (§V.c) et
**ouverture du pôle Fiqh** (préséance mālikite, bloc ⚖️, double face du Gardien —
§V.c.6 et §VII).
**Révisé le 2026-07-07** : adoption de la philosophie et de la convention
terminologique Sashimono (§VII, « Convention Sashimono » ; directive détaillée :
`meta/philosophie-sashimono.md`).
**Révisé le 2026-07-16** : double contrôle systématique (sashimono + confrontation
Gizeh) inscrit au §VII.
**Révisé le 2026-08-04** : ouverture du cinquième circuit `hermeneutique/`
(§II, §V.d, §VI) — navigation du domaine intermédiaire via les médiums de fiction
tenus pour interfaces, clés doctrinales suggérées, registres `analyse` et
`expression`, double fonction avec le bureau de Direction Artistique du label.
On ne
parle jamais de « réforme » : une réforme prétend corriger le principe, une
restauration rétablit l'ordre normal. Le mot « réforme » est banni du dépôt.
**Révisé le 2026-08-08** : taxonomie élargie du circuit `hermeneutique/`
(types `auteur`, `figure`, `dispositif` ; dossiers `hermeneutique/auteurs/`
et `atelier/etudes-de-cas/`) et introduction de l'axe de **portance**
(*jikugumi*/*zōsaku*) et de l'axe de **nature** (*restitution*/*homologie*)
des joints — §II, §III, §V.d, §VII (convention Sashimono). Visé par Sidy.
**Révisé le 2026-08-08 (second amendement)** : ouverture du pôle **R&D** de
l'atelier — `atelier/rd/`, pôle interne au circuit existant (verdict Sidy :
Option C, nom `rd/`, phase 1 partielle). Cinq circuits, inchangés. Le pôle
reçoit la finalité de **souveraineté** : consignation systématique de tout ce
qui relève de l'infrastructure globale hardware/software, en vue de son
entretien, développement qualitatif, optimisation à mesure, et de
l'émancipation progressive de tout intermédiaire de service tiers. Sceau
atelier étendu (§V.a), régime de liens de `projets/` hérité par `rd/` (§VI),
`liens_atelier` élargi (§V.d), annales de l'atelier inscrites au Cmd 9.
**Révisé le 2026-08-09** : ouverture d'un régime propre à la **couche agentique
opérative** (Hermes) au sein du Domaine Réservé — §VI, corollaire agentique.
L'étanchéité `meta/` continue de régir les cinq circuits du dépôt à l'identique ;
elle ne s'applique plus telle quelle aux agents Hermes, dont la fonction inclut
par construction l'usage du contexte personnel de Sidy. Contrepartie
non-négociable : toute donnée personnelle injectée dans un prompt d'agent porte
sa propre hiérarchie ontologique explicite (clause `## Ontological order`), pour
distinguer le principe (précédant, structurant) de la détermination individuelle
(contingente, ne portant rien — *zōsaku*, §VII). Point de méthode, non de
doctrine : ne rouvre aucune correspondance déjà tranchée. Voir fiche
`doctrinal/discernement/2026-08-09_hierarchie-principe-determination-individuelle.md`.
**Le 2026-08-08 (exécution)** : migration de `atelier/projets/` vers `rd/`
effectuée fiche par fiche (§IV de la proposition) : 16 fiches migrées (slugs
conservés), anciennes fiches conservées en stubs `deprecated` avec pointeur
(Cmd 10), assets et scripts déplacés avec les fiches. §II mis à jour
(`projets/` désormais résiduel). `album-personnel.md` déplacé le même jour
vers `label/production/` (verdict Sidy : relève de la création artistique,
non du pôle R&D) — stub `deprecated` conservé, liens entrants `materiel/`
coupés (§VI).
**Révisé le 2026-08-09** : ouverture du hub propre à `meta/` —
`meta/meta-index.md` et `meta/meta-annales.md` (verdict Sidy : nommage
préfixé `meta-` pour écarter tout risque de lecture comme sixième circuit ;
`meta/` reste le Domaine Réservé, non un circuit). Motif : le comptage
mécanique des liens entrants (`carte-du-depot.py`, bug de résolution
corrigé le même jour) faisait apparaître 66 fiches de `meta/`
(`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
`projet-unifie/`) sans aucun lien entrant, faute de hub interne au domaine
— les quatre circuits en ont un (`index.md`/`annales.md`), `meta/` n'en
avait aucun. §II, §VI et §X (Cmd 9) mis à jour.
**Révisé le 2026-08-12 : éclatement expérimental en protocoles locaux
(verdict Sidy — méthode à l'essai, non tranchée définitivement).** Le présent
fichier ne porte plus, seul, la lettre intégrale de toute règle : les Sceaux,
nomenclatures et actions d'exécution **propres à un seul circuit** vivent
désormais dans un `CLAUDE.md` local (`doctrinal/`, `atelier/`, `label/`,
`hermeneutique/`, `meta/` — carte au §II bis). Motif : réduire ce que doit lire
un agent travaillant dans un seul circuit, sans rien perdre pour un agent
travaillant depuis la racine (chargée par construction en toute circonstance).
Ce qui reste ici : tout ce qui est transversal (postes de travail, carte des
circuits, étanchéité inter-circuits, protocoles d'exécution communs,
supervision des agents, procédure d'intégration, commandements absolus). Le
**Corollaire d'auto-suffisance** (ancien Cmd 14) est amendé en conséquence — sa
nouvelle lettre figure au §X. **Archive intégrale** de la version
pré-éclatement, non modifiée, conservée pour rollback :
`meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md` (Cmd 10 : jamais
de suppression sèche). Réversible sur simple verdict de Sidy.
**Révisé le 2026-08-22** : ajout du **Commandement 15 (Hygiène Unicode)** suite
à l'incident de contamination par caractères Zero Width Joiner (U+200D). 31
fichiers nettoyés, 156 occurrences supprimées. Interdiction formelle d'insérer
des caractères Unicode invisibles dans le dépôt. Référence : rapport
`atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`.
