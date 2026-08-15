---
title: "Spécification — rôle G0 de brouillon §4 (actualisation Karūbī)"
type: meta
tags: [outillage, hermes, skill, karubi, transmissions, proposition]
created: 2026-08-15
updated: 2026-08-15
---

# Spécification — rôle G0 « brouillon §4 » (actualisation Karūbī)

> **Statut : brouillon, kari-kumi.** Documente un rôle **distinct** du sub-agent
> Karūbī côté destinataire (`spec-skill-karubi-hermes.md`) — ce dernier reste
> isolé du wiki (aucun accès `index.md`/`annales.md`, mémoire native désactivée,
> périmètre limité au fichier `karubi-<nom>.md` chargé). Le rôle décrit ici
> s'exécute **côté G0 uniquement**, jamais dans une session avec un destinataire.

## Ce que ce rôle résout

Le cycle de navette (§7 du gabarit) prévoyait jusqu'ici que Sidy rédige §4
(État des travaux) **de mémoire**, à chaque retour de fichier. Ce rôle
constitue un **brouillon** de §4 en s'enquérant des hubs du wiki
(`doctrinal/index.md`/`annales.md`, `hermeneutique/index.md`/`annales.md`,
`atelier/index.md`/`annales.md`, `label/index.md`/`annales.md`), au même niveau
d'abstraction que ce que Sidy écrirait lui-même. L'autonomie porte sur la
**collecte**, jamais sur l'**écriture finale** : §4 reste une zone réservée à
Sidy (Cmd 13, porte humaine) au gabarit — ce rôle ne fait qu'éviter à Sidy de
partir d'une page blanche.

## Déclencheur

Explicite, par Sidy, **après** une intégration de navette réussie via
`meta/transmissions/integrer-navette-karubi.py`. Jamais automatique, jamais
enchaîné à l'intégration elle-même, jamais pendant une session avec un
destinataire (Cmd 13 : rien qui engage ne se déclenche seul).

## Séparation stricte d'avec le sub-agent Karūbī (destinataire)

| | Sub-agent Karūbī (`spec-skill-karubi-hermes.md`) | Rôle G0 (ce fichier) |
|---|---|---|
| Interlocuteur | Le destinataire (Mehdi, etc.) | Sidy seul |
| Accès wiki | Le fichier `karubi-<nom>.md` chargé, rien d'autre | `index.md`/`annales.md` des quatre circuits + `hermeneutique/`, `atelier/rd/` |
| Mémoire native | Désactivée | Sans objet (session G0 ponctuelle, pas de session persistante avec un tiers) |
| Sortie | Proposition §8/§9, validée par le destinataire ou script déterministe | Fichier de brouillon séparé, jamais écrit dans le canonique |
| Verdict final | Le destinataire relit sa propre proposition | Sidy seul relit et colle dans §4 |

Ces deux rôles ne partagent ni contexte, ni session, ni sub-agent. Un agent
qui aurait vu le contenu d'`index.md`/`annales.md` ne doit **jamais** être
réutilisé comme sub-agent Karūbī côté destinataire — contamination du
périmètre, violation de l'isolement documenté dans l'autre spec.

## Étape 1 — lecture

- Lecture des hubs (`index.md`/`annales.md`) des circuits pertinents au
  destinataire concerné (le périmètre déjà lisible par le destinataire
  lui-même sert de repère : pour Mehdi, `doctrinal/`, `hermeneutique/`,
  `atelier/rd/{instrument,outillage,cahiers}` — jamais `label/` ni
  `atelier/rd/infrastructure/`, hors de son périmètre de lecture propre).
- Lecture du §4 **actuel** du `karubi-<destinataire>.md` canonique, comme
  gabarit de ton et de granularité (même niveau d'abstraction, jamais plus
  détaillé que l'existant).
- **Jamais** de lecture de `meta/` au-delà du fichier canonique lui-même —
  étanchéité du Domaine Réservé inchangée (`meta/CLAUDE.md`).

## Étape 2 — rédaction du brouillon

- Même niveau d'abstraction que l'exemple gabarit : « le pôle X existe et
  s'appelle Y », jamais de détail cru d'une fiche `label/` ou `meta/`.
- Aucune correspondance doctrinale nouvelle affirmée comme établie — si le
  brouillon mentionne un ancrage discuté, il porte la même prudence
  (🔍/kari-kumi) que toute fiche du dépôt (§VII racine, double contrôle
  sashimono/Gizeh — s'applique identiquement ici).
- Sortie : fichier séparé,
  `meta/transmissions/brouillons-section4/<destinataire>-<YYYY-MM-DD>.md`,
  texte brut, prêt à être collé mais **jamais** écrit directement dans le
  canonique.

## Étape 3 — remise à Sidy

- Le rôle s'arrête à l'écriture du brouillon. Aucune écriture dans
  `karubi-<destinataire>.md`, aucun rescellement, aucune journalisation dans
  `registre-silsila.md` — ces trois actes restent réservés à Sidy seul :
  1. Sidy relit et édite le brouillon à sa guise.
  2. Sidy colle le texte final dans §4 du canonique.
  3. Sidy incrémente `version`, appelle `generer-karubi.py sceller`.
  4. Sidy journalise (`registre-silsila.md`), commit, rend le fichier.

## Ce que ce rôle ne fait jamais

- N'écrit jamais dans le fichier canonique `karubi-<destinataire>.md`.
- Ne répond jamais aux Questions §9 (§9→§10 reste une réponse directe de
  Sidy, mot pour mot — hors périmètre de tout automatisme, cf.
  `meta/CLAUDE.md`).
- Ne modifie jamais `hash_sceau` ni `version`.
- Ne s'exécute jamais pendant, ni juste avant, une session avec le
  destinataire — sessions disjointes dans le temps comme dans le contexte.
- Ne lit jamais `label/` ni `atelier/rd/infrastructure/` pour un destinataire
  dont le périmètre de lecture propre les exclut (cohérence avec le bind
  mount déjà en place, cf. `atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12.md`).

## Prérequis de mise en service

1. `meta/transmissions/integrer-navette-karubi.py` en service (fait,
   2026-08-15).
2. Dossier `meta/transmissions/brouillons-section4/` créé (fait).
3. Verdict de Sidy sur le présent brouillon de spec.
4. Canal de déclenchement explicite défini (commande dédiée, non détectée
   implicitement — même exigence que pour la skill Karūbī côté destinataire).
