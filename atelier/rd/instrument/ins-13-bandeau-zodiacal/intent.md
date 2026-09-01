---
title: "INS-13 — bandeau zodiacal : intention"
type: projet
chantier: INS-13
tags: [atelier, rd, instrument, chantier, intent, zodiaque]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/instrument/spec-anneau-zodiacal]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
---

# INS-13 — bandeau zodiacal : intention

## Le besoin

**Manque de rendu, non manque de donnée** — la formule est de la spécification
existante (`spec-anneau-zodiacal.md`, §0) et le constat tient toujours. Les colonnes
*Manzil* et *Signe (portion)* des degrés 11 à 38 sont sourcées (Gloton,
*De la mort à la résurrection*, pp. 45–48) et transitent déjà par le manifeste ; le
prototype ne les affiche pas. Le dépôt porte une matière tranchée que l'interface ne
montre pas.

C'est le chantier le plus proche de l'exécutable de tout le pôle `INS` : il ne dépend
d'aucun verdict doctrinal ouvert. Les chantiers voisins (INS-04, INS-05, INS-06,
INS-09) sont bloqués en amont du rendu ; celui-ci ne l'est pas.

## Qui le porte

Sidy. Ouvert le 2026-07-27, spécifié le 2026-07-26, jamais implémenté.

## Hors périmètre

- **Tout thème daté ou localisé.** La domification reste générique : ni époque ni
  lieu dans le manifeste (schéma v0.2.5). Aucune carte du ciel individuelle.
- **Toute correspondance nouvelle.** La spécification existante le pose : elle
  « n'établit aucun ancrage nouveau ». Ce chantier visualise, il n'instruit rien.
- **Les degrés 1 à 10**, hors de la portion zodiacale de la table.

## Contraintes doctrinales

- **Cmd 3.** L'affichage conjoint des degrés et des arcs de l'écliptique ne repose
  pas sur une assimilation nouvelle mais sur la **convergence des 28**, premier
  ancrage `etabli` du dépôt (*Futūḥāt* ch. 198) : un *manzil* **est** un arc de
  l'écliptique. Rien n'est ajouté ; ce qui est déjà tranché est montré.
- **§VII, manifestes.** Aucune valeur zodiacale en dur dans le code de rendu — la
  spécification existante en fait une règle explicite. L'anneau lit le manifeste.
- **Cmd 5.** Les trois marqueurs `to-source` de la colonne *faṣṣ* relèvent de INS-12
  et **ne bloquent pas** ce chantier ; ils ne sont simplement pas affichés comme
  établis.

## Le signe de réussite

Le bandeau s'affiche à partir du seul manifeste, et une modification d'un *manzil*
dans `instrument-donnees.yaml` se répercute à l'écran après une simple régénération —
sans qu'une ligne de rendu soit touchée. C'est la preuve que la chaîne tient.

## Ce qui reste ouvert

Rien qui bloque. La forme exacte du bandeau (anneau circulaire ou bande horizontale)
est une question de rendu tranchée par la spécification existante, à relire au moment
d'implémenter.
