---
title: "INF-13 — scission du dépôt Instrument : intention"
type: infrastructure
chantier: INF-13
tags: [atelier, rd, infrastructure, chantier, intent, instrument, git]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
  - "[[meta/projet-unifie/02-instrument-feuille-de-route]]"
---

# INF-13 — scission du dépôt Instrument : intention

## Le besoin

L'Instrument est le premier objet **logiciel** au sens strict que produit ce dépôt :
un prototype de 99 871 octets qui charge Three.js et consomme un manifeste. Il vit
aujourd'hui au milieu de fiches doctrinales, dans un dépôt dont la vocation est la
transmission et l'étude — deux régimes de travail qui n'ont ni le même rythme, ni les
mêmes contrôles, ni la même unité de révision.

Le motif n'est pas une préférence d'organisation : **le protocole l'écrit déjà.** Le
§VII, *Règle commune des MANIFESTES*, impose le flux `dépôt → manifeste → interface`,
à sens unique, et pose que « l'interface ne réécrit jamais le dépôt ». Un dépôt
séparé pour l'interface est cette règle exprimée en infrastructure plutôt qu'en
discipline. Tant que les deux cohabitent dans un même arbre git, le sens unique ne
tient que par la vigilance ; séparés, il tient par construction.

Précédent de méthode : l'éclatement de `CLAUDE.md` en protocoles locaux du
2026-08-12 — même geste, un cran plus haut.

## Qui le porte

Sidy, décision du 2026-09-01 à la lecture du *AI-Native SDLC Playbook*.

## Hors périmètre

- **Le contenu doctrinal de l'Instrument ne bouge pas.** Fiches d'architecture
  (v0.1, v0.2, v0.3), jalons, mises en regard (*Majma' al-Baḥrayn*, réseau subtil),
  `instrument-donnees.yaml`, `assets-instrument/`, les triptyques `ins-*/` : tout
  reste dans le wiki. Le déplacer serait une infraction au Cmd 7 — c'est du contenu
  de circuit, pas de l'interface.
- **Le producteur du manifeste ne bouge pas.** `generer-manifeste.py` lit
  `doctrinal/` : il est en amont, il reste en amont.
- **L'automatisation de la publication du manifeste** — spécifiée ici, non activée.
- **La mise en public du dépôt.**

## Contraintes doctrinales

- **§VII, sens unique.** Rien ne remonte de l'interface vers le dépôt. Le nouveau
  dépôt n'a aucun droit d'écriture sur le wiki, et ce n'est pas une politesse : c'est
  la raison d'être de la scission.
- **Cmd 3 et Cmd 12.** Aucune correspondance ne naît dans le dépôt de rendu. Un
  rapprochement visuel n'est pas un ancrage ; le verdict appartient à Sidy.
- **Cmd 7, étanchéité.** La ligne de coupe est *producteur/consommateur*, pas
  *Instrument/reste*. Elle doit être écrite des deux côtés.
- **Cmd 10.** Rien n'est supprimé côté wiki : le prototype migré laisse un stub
  `deprecated` avec pointeur, comme les 16 fiches d'`atelier/projets/` le 2026-08-08.
- **Cmd 14.** Le wiki ne doit pas devenir muet sur ce qui l'a quitté : le protocole
  racine et `atelier/CLAUDE.md` disent où vit le rendu et à quelles conditions.
- **Cmd 13.** Le jeton d'écriture croisée et la mise en public sont des décisions
  engageantes, réservées à Sidy.

## Le signe de réussite

Un lecteur du seul wiki sait qu'un dépôt frère existe, ce qu'il contient, ce qu'il ne
contient pas, et par quel canal le manifeste y parvient — sans avoir à ouvrir GitHub.
Et : `main` du nouveau dépôt est protégée, **contrôlée par appel d'API**, pas
supposée. PRO-01 a établi le 2026-08-31 qu'un contrôle peut exister sans rien
regarder ; on ne rejoue pas cela sur du neuf.

## Ce qui reste ouvert

| Question | Destinataire |
|---|---|
| Jeton PAT et automatisation GitHub Actions du manifeste | **Sidy** (Cmd 13) |
| Passage du dépôt en public | **Sidy** (Cmd 13) |
| Hébergement du rendu (GitHub Pages ou serveur propre — la souveraineté du pôle `rd/` plaide pour le second) | **Sidy** |
