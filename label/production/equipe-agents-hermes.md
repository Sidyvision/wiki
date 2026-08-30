---
title: Équipe d'agents Hermes — 12 fonctions, 5 archétypes
type: production
medium: transversal
projet: label
statut: en-cours
tags:
- hermes
- agents
- organigramme
- archetypes
- protocole
- initiatique
created: 2026-07-05
updated: 2026-07-05
sources: []
liens:
- '[[label/distribution/doctrine-du-don]]'
- '[[label/production/modele-economique]]'
- '[[label/direction-artistique/amorcage/generation-non-cumulative]]'
- '[[label/production/modele-economique]]'
liens_atelier: []
links:
- '[[label/production/modele-economique]]'
---

# Équipe d'agents Hermes — 12 fonctions, 5 archétypes

> Configuration des agents personnalisés Hermes (system prompts + skills dans
> `~/.hermes/`) pour le label. Rédigée **en anticipation** de l'installation d'Hermes
> (Phase 1 en attente, contrainte budgétaire) : rien ne se périme, ce sont des fichiers
> de config prêts à coller. Les 12 system prompts vivent en
> `meta/projet-unifie/hermes-prompts/` (anglais). **Aucun agent n'accède au contexte
> personnel `meta/` sensible.**

## I. Principe structurant : deux plans

- **Plan horizontal — 12 fonctions opératives** : les métiers du label (l'entreprise
  telle qu'elle tourne). Le nombre 12 a **émergé des fonctions réelles**, non déclaré
  a priori (même méthode que le tableau des traits de l'album).
- **Plan vertical — 5 archétypes** : les rôles initiatiques du protocole (Dépositaire,
  Transmetteur, Faiseur, Tisseur, Gardien), issus de la conversation fondatrice sur le
  Protocole du Don. Chaque agent **sert un archétype**.
- **Génération non-cumulative** : la valeur naît de l'**interaction** entre fonctions,
  jamais de l'accumulation d'une seule — cf.
  [[label/direction-artistique/amorcage/generation-non-cumulative]]. L'organigramme est
  lui-même une application de ce principe.

> ⚠️ La correspondance des deux plans avec la doctrine (5 archétypes ↔ Cinq Présences
> *hadarat khams* ; 12 fonctions ↔ duodénaire zodiacal) est **suggérée, non validée** :
> elle fait l'objet d'une fiche `discernement/` côté doctrinal
> (`2026-07-05_correspondances-fonctions-initiatiques-entreprise`), dont le verdict
> appartient à Sidy (Cmd 12). Tant qu'elle n'est pas validée, la traiter comme une
> piste (🔍), jamais comme un fait établi.

## II. Les 5 archétypes (plan vertical)

| Archétype | Fonction initiatique |
|---|---|
| **Dépositaire** | Garde l'intention vivante ; référence morale du projet |
| **Transmetteur** | Fait circuler le vecteur (l'œuvre, la valeur) sans l'altérer |
| **Faiseur** | Produit et transforme une forme située (musique, image, objet) |
| **Tisseur** | Relie les autres fonctions, facilite la co-présence |
| **Gardien** | Veille aux limites et à la clause de non-corruption de l'intention |

## III. Les 12 fonctions opératives (plan horizontal)

Chaque agent : mission · référence incarnée · archétype servi · périmètre (dossier).

| # | Agent | Référence | Archétype | Périmètre |
|---|---|---|---|---|
| 01 | A&R / Direction artistique musicale | Peanut Butter Wolf (Stones Throw) | Dépositaire | sélection titres, séquençage, tableau des traits |
| 02 | Direction artistique visuelle & éditoriale | Vaughan Oliver (4AD) | Faiseur | artworks, standards visuels, cohérence site/pochettes/expo |
| 03 | Chargé de production | archétype label manager indé | Tisseur | `production/`, rétroplanning, budget, pressage |
| 04 | Administration & juridique | Donald Passman (adapté droit FR) | Gardien | `administratif/`, Sacem/SDRM/SPPF, contrats |
| 05 | Comptabilité & gestion | corpus CNM / régimes FR | Gardien | comptes, royautés, TVA, régimes |
| 06 | Distribution | Rough Trade Distribution / Bandcamp-first | Transmetteur | `distribution/`, disquaires, agrégateur |
| 07 | Marketing & communication | NTS Radio | Transmetteur | `marketing-communication/`, radio, presse, Instagram |
| 08 | Publication / site | orchestrateur du protocole publication | Transmetteur | manifeste → préversion → prod → annales |
| 09 | Ingénieur du son studio | Russell Elevado + Bob Power | Faiseur | protocoles A/B, boucle canal 1, M/S, bande |
| 10 | Gardien du Protocole | archétype Gardien (conversation fondatrice) | Gardien | veille intention, clause de non-corruption, cohérence des cercles |
| 11 | Éditeur du fanzine *Dans l'Absolu* | Wax Poetics | Faiseur | `marketing-communication/fanzine`, print de collection |
| 12 | Commerce & rentabilité | Sacred Bones / boutique Stones Throw | Faiseur | `production/modele-economique`, merchandising, revenus |

## IV. Tensions voulues par design

- **Agent 10 (Gardien du Protocole) ↔ Agent 12 (Commerce)** : le Commerce cherche la
  rentabilité ; le Gardien signale quand elle menace l'intention. Cette tension n'est
  pas un défaut à résoudre — c'est l'interaction qui génère la justesse (génération
  non-cumulative). Le Gardien a autorité de signalement ; l'humain tranche.
- **Agent 12** porte une consigne comportementale explicite : *l'artiste sous-priorise
  structurellement la rentabilité ; remettre ce sujet à l'ordre du jour sans qu'on le
  demande.*

## V. Garde-fous transversaux (dans chaque system prompt)

1. Une session = un agent = une fonction (extension de la doctrine « une session = une
   fonction » du projet wiki).
2. Jamais d'auto-accept ; l'humain valide toute écriture engageante (dépense, contrat,
   publication, tracklist, envoi aux dépositaires).
3. Verdict par vérification mécanique, jamais par auto-rapport du modèle.
4. Étanchéité `meta/` absolue : aucun agent n'accède au contexte personnel ; les prompts
   ne citent que les règles de design publiques.
5. Sur tout ce qui touche un principe traditionnel : l'agent renvoie à la fiche
   `discernement/` concernée, ne tranche jamais un principe (Cmd 12 étendu au label).

## VI. État

`en-cours` : organigramme validé par Sidy (12 agents, création du Gardien du Protocole
et des agents Fanzine + Commerce actée le 2026-07-05). Les 12 system prompts sont à
rédiger (Fable 5) selon la spec `PLAN-REDACTION-fable5.md`. Installation Hermes différée
(budget) — sans impact sur la préparation des configs.
