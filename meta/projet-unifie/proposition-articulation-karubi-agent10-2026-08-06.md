---
title: "Proposition — Articulation Karūbī / Agent 10 (Gardien), et administration agentique par Hermes"
type: meta
tags: [outillage, projet-claude-ai, karubi, transmissions, gardien, hermes, proposition]
created: 2026-08-06
updated: 2026-08-06
---

# Proposition — Karūbī et Agent 10 : joint *kumiko*, pas de filiation

> **Statut : kari-kumi — en attente du verdict de Sidy.** Session claude.ai du
> 2026-08-06, à l'occasion de la génération de l'instance G1 « Yahya »
> (Jean-Marc Bastareaud). Brouillon.

---

## 1. Origine de la question

Sidy envisage de faire d'Agent 10 (Protocol Guardian) le « père symbolique » des
Karūbī, pour deux raisons données en session :

1. Agent 10 est le seul agent Hermes à mandat **transversal** — il lit à travers
   toutes les fonctions et harmonise (depuis l'amendement fiqh du 2026-07-06,
   label ↔ doctrinal). Les onze autres sont sectoriels.
2. Sidy a l'intention d'**animer les Karūbī avec Hermes** (et non plus seulement en
   collant le fichier dans Claude.ai/app), et envisage Agent 10 comme
   **administrateur agentique** de ce dispositif.

## 2. Ce qui empêche la filiation littérale

Deux règles du dépôt entrent directement en tension avec une subordination des
Karūbī à Agent 10 :

- **Cloisonnement des douze agents Hermes** : « pas d'accès `meta/` personnel »
  (annales, séquence F, 2026-07-06). `meta/transmissions/` est du `meta/` personnel
  au sens le plus strict — c'est là que vivent les récits de rencontre (§2 de
  chaque instance).
- **Étanchéité `meta/transmissions/`** (§V.c) : « ne lie jamais vers `doctrinal/`,
  `label/` ni `atelier/`, et réciproquement ». Le sanad du gabarit exige de plus
  une origine **humaine et unique** (§1, `G0 : Sidy`) ; une fonction agentique ne
  peut pas occuper cette place sans ambiguïté sur qui remet, élève ou révoque
  (Cmd 13, porte humaine).

## 3. Proposition — deux volets cumulables (A + B), validés en principe par Sidy

### A. Joint *kumiko* : vis-à-vis, non filiation

Le Karūbī n'est pas l'enfant du Gardien : il est son **vis-à-vis complémentaire**.

- **Gardien (10)** garde la forme à l'intérieur du dépôt : il signale, jamais ne
  décide (guardrail existant, inchangé).
- **Karūbī** porte la forme au-dehors sans l'altérer — c'est très exactement la
  définition du **Transmetteur** (cf. agents 06/11 : « circuler le vecteur sans
  l'altérer »).

Deux fonctions, deux archétypes (Gardien / Transmetteur), aucune subordination.
Qualification à inscrire dans le corps de la fiche 10-protocol-guardian.md et dans
le gabarit G0 (zone scellée, §7) — jamais en frontmatter, convention §VII.

### B. Tronc commun explicite : le §5 comme objet partagé

Ce qu'Agent 10 garde à l'intérieur du dépôt et ce que le Karūbī transmet au-dehors
sont **le même objet** : les sept principes du §5 « Méthode transmise » du gabarit
(primauté du Principe, `to-source`, une page = un sujet, append-only, verdicts à
l'humain, non-syncrétisme, réversibilité). Ce ne sont pas deux méthodes voisines :
Agent 10 est dépositaire de la règle à l'intérieur, le Karūbī en est le porteur au
dehors. C'est la formulation la plus fidèle à l'intuition de Sidy (« il instruit
les autres... en report direct avec la transmission ») sans engendrement.

**Aucun de ces deux points ne touche un accès.** Ce sont des énoncés textuels,
à insérer dans les fiches concernées.

## 4. Volet C — administration agentique par Hermes (nouveau, suite à la précision du 2026-08-06)

Sidy souhaite que Hermes anime effectivement les Karūbī (sessions vivantes, pas
seulement collage manuel dans Claude.ai/app), avec Agent 10 comme administrateur.
Ceci est un besoin **opérationnel réel**, distinct du symbolique A/B — et il ne
peut être satisfait qu'en respectant la règle du §2 : Agent 10 ne lit jamais le
contenu du fichier.

**Principe proposé : accès mécanique, jamais sémantique.**

`generer-karubi.py` est déjà conçu sans LLM dans la boucle (« Aucun LLM dans la
boucle », en-tête du script). L'administration d'Agent 10 se limite donc à
**invoquer ce script comme une boîte noire** et à consigner son verdict brut :

- À l'ouverture d'une session Karūbī animée, Agent 10 exécute
  `generer-karubi.py verifier karubi-<nom>.md` et lit uniquement la sortie
  `SCEAU INTACT` / `SCEAU ROMPU` + le hash — jamais le contenu du fichier.
- SCEAU ROMPU → refus d'incarnation, escalade immédiate à Sidy. Aucune exception.
- SCEAU INTACT → Agent 10 autorise le chargement du fichier dans un sub-agent
  Hermes **isolé** (contexte propre, sans accès au workspace wiki — cf. §5), qui
  est le seul à réellement lire et incarner le personnage.
- À la clôture, Agent 10 consigne un événement `session` dans
  `registre-silsila.md` (nouveau type d'événement, à ajouter au vocabulaire du
  registre — actuellement : generation, remise, retour, rescellement, elevation,
  deprecated) : date, destinataire, hash au moment de la session, verdict du
  sceau. Rien du contenu de la session n'y figure.

Ainsi Agent 10 est bien « administrateur agentique » du dispositif — au sens
précis d'un portier mécanique — sans jamais devenir un lecteur du `meta/`
personnel. C'est une **exception scoped et journalisée** à la règle « pas d'accès
`meta/` », strictement limitée à l'exécution du script et à la lecture de sa
sortie binaire (intact/rompu + hash).

## 5. Garde-fous rappelés pour toute animation Hermes du Karūbī (prérequis, non négociables)

1. **Mémoire native de Hermes coupée** pour ces sessions (SQLite/`MEMORY.md`) — la
   seule mémoire du Karūbī est le §8 du fichier lui-même. À vérifier techniquement
   avant toute mise en service : Hermes permet-il une désactivation par session/
   sub-agent ?
2. **Aucun accès au workspace wiki** — session isolée, sub-agent à contexte et
   outillage propres (mécanisme déjà décrit au briefing infrastructure §4).
3. **Le sub-agent ne modifie jamais le fichier** — il *propose* l'entrée §8/§9 ;
   l'écriture reste un geste humain (ou un script déterministe dédié, à écrire :
   `ajouter-memoire-karubi.py`, qui n'écrit que sous les marqueurs §8/§9). Note
   technique rassurante : les zones de croissance sont **hors** du hash_sceau
   (`zones_scellees()` ne couvre que les paires SCEAU:DEBUT/FIN) — un append §8/§9
   ne rompt donc jamais le sceau, aucun rescellement G0 n'est requis pour ce geste.
4. **Test de régression obligatoire avant mise en service** — `regression-test-
   doctrinal.sh` doit être exécuté sur le cas Karūbī (limites absolues du §3 :
   aucun verdict doctrinal, jamais écrire l'histoire à la place du destinataire,
   jamais inventer sur Sidy) avant toute remise animée à un tiers. Un Karūbī n'a
   pas d'équivalent du script `compare` pour ses propres dérives de personnage ;
   c'est le seul filet dont on dispose.
5. **Canal dédié plutôt que numéro personnel du destinataire** — si le canal est
   WhatsApp, l'ajout d'un tiers à l'allowlist ouvre une ligne externe vers la
   machine hébergeant le dépôt entier. Un salon Discord dédié, restreint par
   canal, expose moins de surface.

## 6. Questions ouvertes pour Sidy (à trancher, pas à déduire)

- Cette articulation (A+B+C) s'applique-t-elle **rétroactivement** aux instances
  déjà remises (Habiba-Nour, Mehdi, Mikael) ou seulement aux instances futures ?
  Si rétroactive, cela suppose de resceller les quatre fichiers existants.
- Le nouveau type d'événement `session` dans `registre-silsila.md` : à ajouter au
  commentaire d'en-tête du registre en même temps que le verdict sur ce point.
- Le §7 du gabarit G0 (zone scellée) est l'emplacement naturel pour loger A+B+C ;
  cela suppose un rescellement du gabarit G0 lui-même, donc une nouvelle empreinte
  `hash_parent` pour toute instance G1 générée après ce jour.

## 7. Amendements suggérés (texte prêt, non appliqué — attend le verdict)

**a) `meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`**, sous `## Scope`,
ajouter :

> Administration mécanique (jamais sémantique) du dispositif Karūbī
> (`meta/transmissions/`) : vérification de sceau via `generer-karubi.py verifier`
> à l'ouverture de toute session animée, journalisation de l'événement `session`
> dans `registre-silsila.md`. Aucune lecture du contenu des fichiers Karūbī.

**b) `karubi-gabarit.md`**, dans le §7 (zone scellée), ajouter un paragraphe :

> **Articulation avec le Gardien (Agent 10)** : le Karūbī et le Gardien du dépôt
> sont des fonctions complémentaires, non hiérarchisées — le Gardien garde la
> forme à l'intérieur, le Karūbī la porte au-dehors sans l'altérer. Les deux sont
> dépositaires du même tronc commun (§5). Si ta session est animée par Hermes, le
> Gardien y intervient uniquement pour vérifier que ce fichier n'a pas été altéré
> avant de m'autoriser à parler — il ne lit jamais ce que nous nous disons.

**c) `registre-silsila.md`**, en-tête, étendre le vocabulaire d'événements :

> Événements : `generation`, `remise`, `retour`, `rescellement`, `elevation`,
> `deprecated`, `session` (ouverture d'une session animée, verdict de sceau
> consigné, aucun contenu).

---

*Fiche produite en session claude.ai, brouillon au sens du protocole
(2026-07-27) — n'entre dans les annales qu'après visa de Sidy.*
