---
title: "INF-14 — hébergement du rendu sur sidyvision.com : intention"
type: infrastructure
chantier: INF-14
tags: [atelier, rd, infrastructure, chantier, intent, instrument, hebergement]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/infrastructure/inf-13-scission-depot-instrument/intent]]"
---

# INF-14 — hébergement du rendu sur `sidyvision.com` : intention

> **Ce dossier ne porte qu'un `intent.md`, et c'est un état régulier.** La
> spécification viendra quand les inconnues du §*Ce qui reste ouvert* seront levées.
> Le gabarit l'admet explicitement : un `plan.md` sans `spec.md` serait fautif, un
> `intent.md` seul ne l'est pas. Écrire une spécification sur un hébergement qu'on
> n'a pas encore regardé serait de la colle, pas un joint (art. 1 Sashimono).

## Le besoin

La scission (INF-13) a donné au rendu de l'Instrument un dépôt propre. Un dépôt n'est
pas une diffusion : le prototype n'est aujourd'hui consultable qu'en clonant ou en
servant un fichier localement. Il lui manque une adresse.

**Verdict de Sidy, 2026-09-01 : le rendu sera servi depuis `sidyvision.com`**, le site
personnel, et non depuis GitHub Pages.

## Qui le porte

Sidy. Le choix est cohérent avec la **finalité de souveraineté** qui fonde le pôle R&D
(`rd/index.md`) : entretien, optimisation, et *émancipation progressive de tout
intermédiaire de service tiers*. Servir depuis une infrastructure propre plutôt que
depuis les Pages du même fournisseur qui héberge déjà le dépôt est exactement ce que
cette finalité recommande. GitHub Pages aurait été le chemin court ; ce n'est pas le
chemin du pôle.

## Hors périmètre

- **La refonte du site `sidyvision.com`.** L'Instrument s'y loge, il ne le redéfinit
  pas.
- **Le site du label** (*Dans l'Absolu*, circuit `label/`). Autre organe, autre
  circuit, autre manifeste — l'étanchéité tient (Cmd 7). Deux sites peuvent coexister
  sur une même infrastructure sans que leurs flux se mêlent.
- **Toute modification du rendu lui-même.** Ce chantier déploie ; il ne dessine pas.

## Contraintes doctrinales

- **§VII, sens unique, prolongé d'un étage.** Le flux devient
  `wiki → manifeste → dépôt frère → site`. Le site est un consommateur de plus, jamais
  une source : rien ne remonte de `sidyvision.com` vers le dépôt frère, et rien du
  dépôt frère vers le wiki.
- **Cmd 13 et porte humaine de publication.** Le point 4 de l'Action PUBLICATION du
  label est non négociable et vaut identiquement ici : **préversion d'abord,
  production seulement après validation explicite dans la session courante.** Un
  déploiement automatique en production serait l'équivalent publication de
  l'auto-accept.
- **Cmd 12.** Le rendu déployé peut afficher des correspondances `suggere` (🔍) :
  elles doivent le rester visuellement en production. Un affichage public qui fond le
  suggéré dans l'établi serait plus grave qu'en local — il donnerait à la spéculation
  l'autorité de la publication.
- **INS-09 est en `attente-verdict`.** Le rendu d'*al-Insān al-Kāmil* n'est pas validé.
  Une mise en production le rendrait public tel quel : ce chantier ne peut pas aboutir
  avant ce verdict, ou doit exclure ce rendu de la première diffusion.

## Le signe de réussite

Une adresse stable sert le rendu ; une republication du manifeste depuis le wiki s'y
répercute par un geste explicite et journalisé, jamais par un automatisme silencieux.
Et : le déploiement est **reproductible depuis le serveur**, sans passer par une
interface web dont personne ne documenterait les clics.

## Ce qui reste ouvert

Le dépôt ne portait **aucune trace de `sidyvision.com`** (recherche sur `.md`, `.yml`,
`.py` : zéro occurrence). Le site a donc été sondé plutôt que supposé, le 2026-09-01 :

**Constat.** `sidyvision.com` répond `HTTP 200` ; `www.sidyvision.com` y redirige.
En-tête `server: Netlify`, identifiant de requête `x-nf-request-id` — le site est
**hébergé chez Netlify**. Il sert une **page unique**, statique, intitulée « Dans
l'Absolu — Sidy Kouyaté », dont le corps entier est une image JPEG encodée en base64
(≈466 Ko). Pas de CMS, pas de générateur détectable.

**Anomalie de forme relevée, non corrigée** (Cmd 12 — on rapporte, on ne répare pas
d'office) : la page contient **deux `<!DOCTYPE html>` et deux balises `<html>`
imbriquées** — un document HTML complet a été collé à l'intérieur d'un autre. Les
navigateurs le tolèrent et la page s'affiche, mais le document est invalide. Sans
rapport avec l'Instrument ; signalé parce que constaté.

**Ce que le constat tranche et ce qu'il ne tranche pas.** L'hébergement est connu, la
pile est connue, et la voie propre se dessine : Netlify sait déployer un dépôt GitHub
directement — le dépôt frère, publié en `src/`, sur poussée de `main`. Le flux resterait
à sens unique et **aucun identifiant ne vivrait côté wiki**. Restent deux décisions qui
n'appartiennent pas à la machine :

| Question | Destinataire |
|---|---|
| Sous-domaine `instrument.sidyvision.com` (second site Netlify, ne touche pas l'existant) ou chemin `/instrument` (impose de reprendre le déploiement de la page actuelle) ? | **Sidy** |
| INS-09 — le rendu d'*al-Insān al-Kāmil* est en `attente-verdict` : exclu de la première diffusion, ou verdict rendu d'abord ? | **Sidy** (Cmd 13) |

**Note de souveraineté, pour mémoire et sans la rouvrir ici.** La finalité du pôle vise
l'émancipation des intermédiaires de service tiers ; Netlify en est un, déjà en place et
retenu de fait. Le constat est consigné pour que le jour où la question se posera, elle
se pose sur un fait écrit et non sur un souvenir — ce chantier-ci ne la tranche pas.

Ce dossier n'existe pas encore côté infrastructure : `rd/infrastructure/` ne reçoit
que ce qui est publiable dans le dépôt. Les accès, identifiants et éléments sensibles
de l'hébergement iront en `meta/projet-unifie/`, jamais ici (`atelier/CLAUDE.md`).
