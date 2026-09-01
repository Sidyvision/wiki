---
title: "INS-02 — mode « axe unifié » et champ echelle : intention"
type: projet
chantier: INS-02
tags: [atelier, rd, instrument, chantier, intent]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/instrument/2026-08-30_reseau-subtil-unification-axes-deux-echelles]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
---

# INS-02 — mode « axe unifié » et champ `echelle` : intention

## Le besoin

Le rendu actuel dispose les registres en colonnes séparées. Cette disposition est
lisible, mais elle **donne à voir ce qu'elle ne devrait pas dire** : quatre verticales
distinctes là où l'invariant de l'Instrument pose *un seul arbre inversé*, dont les
registres ne sont que des partitions. Le décalage latéral est un artefact d'affichage
que rien, dans l'interface, ne signale comme tel.

Second manque, sur la donnée cette fois : la règle de comparaison « échelle contre
échelle » (§2.3 de la fiche du 2026-08-30) n'est portée **que par la prose**. Rien
dans `instrument-donnees.yaml` ne dit qu'un registre est macrocosmique,
microcosmique ou transcalaire, donc rien ne peut le contrôler mécaniquement.

Constat, non supposition : la fiche source formule les deux gestes en §4.2, et la
ligne INS-02 du registre porte littéralement « spécifier avant de coder ».

## Qui le porte

Sidy, à la suite de la session doctrinale du 2026-08-30. Bénéficiaire : tout lecteur
de l'Instrument, à qui l'interface doit cesser de suggérer une pluralité d'axes.

## Hors périmètre

- **L'appariement terme à terme des registres.** Le mode unifié rabat des colonnes ;
  il n'apparie aucun nœud. §5 de la fiche source est explicite : la déduction des
  deux échelles ne produit aucun appariement.
- **La comparaison *laṭāʾif* ↔ *chakra*.** Elle dépend de INS-01 (ch. II de Shayegan,
  non transcrit). Chantier distinct.
- **L'attribution définitive des échelles aux quatre registres.** La table de §4.2 est
  déclarée « à soumettre — c'est une lecture, pas un constat ». Voir ci-dessous.

## Contraintes doctrinales

- **Cmd 12 / Cmd 13.** L'attribution `transcalaire`/`microcosmique` aux quatre
  registres est un **verdict de Sidy**, pas une décision d'implémentation. Le champ
  est ouvert vide, et le générateur avertit sans trancher.
- **Cmd 3.** Rabattre visuellement deux registres sur un même axe **ne crée aucune
  correspondance**. Le mode unifié montre une partition, il n'établit pas d'ancrage :
  rien de ce qui s'affiche « établi » ne doit changer d'état en basculant de vue.
- **§VII, manifestes.** Le champ naît dans `instrument-donnees.yaml`, transite par
  `generer-manifeste.py`, arrive au rendu. Aucune valeur en dur dans le code, aucune
  écriture retour depuis l'interface.
- **Invariant d'architecture** : un seul arbre inversé. Le mode unifié sert cet
  invariant — c'est son unique justification.

## Le signe de réussite

Un lecteur bascule d'une vue à l'autre et **comprend, sans explication écrite, que
l'écartement des colonnes est un réglage**. Et : un ancrage déclaré entre deux
registres d'échelles incompatibles produit un avertissement à la génération, là où
aujourd'hui rien ne se voit.

## Ce qui reste ouvert

| Question | Destinataire |
|---|---|
| Table d'attribution des échelles (§4.2, quatre registres) | **Sidy** — verdict |
| Un ancrage macro↔micro doit-il avertir, ou bloquer ? | **Sidy** — verdict ; défaut proposé : avertir |
| Les *laṭāʾif* (7 centres de Semnânī) | INS-01, ch. II de Shayegan, non transcrit |
