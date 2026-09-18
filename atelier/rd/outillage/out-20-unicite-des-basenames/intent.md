---
title: "OUT-20 — unicité des basenames, garde du wikilink court : intention"
type: outillage
chantier: OUT-20
tags: [atelier, rd, outillage, chantier, intent, wikilink, controle]
created: 2026-09-18
updated: 2026-09-18
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/infrastructure/2026-09-18_correctifs-rapports-studio-publication]]"
---

# OUT-20 — unicité des basenames, garde du wikilink court : intention

## Le besoin

Mesuré le 2026-09-18, pas supposé : **589 wikilinks courts** (`[[barzakh]]` plutôt que
`[[doctrinal/symboles/barzakh]]`) vivent dans **156 fiches** — 85 en `doctrinal/`, 44 en
`meta/`, 25 en `atelier/`, 1 en `label/`, 1 en `hermeneutique/`. Aucun n'est ambigu
aujourd'hui : chacun se résout vers un basename unique.

Cette forme est admise par le §IV racine depuis le verdict du 2026-09-18, et elle repose
tout entière sur une condition qui n'est **contrôlée par rien** : que deux fichiers du
dépôt ne portent jamais le même nom. Le jour où cela arrive — un dépôt qui a gagné 150
fiches en une journée le 2026-09-16 —, le renvoi change de cible **sans que rien ne
bouge dans la fiche qui le porte**. C'est la signature du défaut le plus coûteux : celui
qui se produit dans un fichier que personne n'éditait, et qu'aucun diff ne montre.

Origine : rapport Publication du 2026-09-16, signalement F (`barzakh-nur-lh.md`, quatre
`cross_links` en forme courte), élargi à tout le dépôt par la mesure du 2026-09-18.

## Qui le porte

Sidy (verdict du 2026-09-18 : « entériner, et outiller le seul vrai risque »). Pour tout
rédacteur du dépôt — humain ou moteur — et pour le générateur de cartographie, qui
résout déjà par basename et signale `ambigu` sans que rien n'empêche l'ambiguïté de
naître.

## Hors périmètre

- **Réécrire les 589 renvois courts en chemin complet** — la passe de masse a été
  explicitement écartée au verdict : le dépôt restaure, il ne réforme pas (Cmd 11).
- **Interdire la forme courte** — elle est admise ; c'est l'unicité qui est gardée, pas
  la forme.
- **Les basenames hors circuits** (`raw/`, `_inbox/`) — hors périmètre de git ou de
  passage, ils ne sont la cible d'aucun wikilink.
- **Le cas des fichiers de service homonymes par construction** (`intent.md`, `spec.md`,
  `plan.md` d'un dossier de chantier ; `index.md`, `annales.md`, `CLAUDE.md`,
  `README.md`, `SKILL.md`) — ils sont homonymes **par convention nommée** et ne sont
  cible d'aucun renvoi court : ils sont exemptés, et l'exemption est déclarée dans la
  spec, jamais implicite.

## Contraintes doctrinales

- **Cmd 12** : le contrôle constate une collision de noms, il ne renomme rien et ne
  choisit pas quel fichier doit céder. Il refuse et nomme les deux chemins ; l'arbitrage
  revient à Sidy.
- **Cmd 14** : le principe (« la forme courte tient à l'unicité du basename ») est
  énoncé au §IV racine ; ce chantier n'en porte que la procédure.
- **§VII, épreuve des contrôles** : B9 devra avoir été **vu refuser** sur une collision
  fabriquée dans un bac à sable, et le double résultat consigné — « vert sur X, refus
  sur Y ». Un contrôle qui n'a affiché que du vert est réputé non éprouvé.
- **Cmd 11** : restauration, jamais réforme — le contrôle empêche une dégradation
  future, il ne corrige pas le passé.

## Le signe de réussite

Deux observations, pas une : (1) `verifier-invariants.py` sur le dépôt vivant rend
exactement la ligne de base du jour — **0 erreur, 71 avertissements** — sans nouvelle
classe ; (2) dans une copie jetable, la création d'un second fichier portant un basename
déjà pris produit un **refus B9 nommant les deux chemins**.

## Ce qui reste ouvert

- **Erreur ou avertissement ?** Une collision ne casse rien tant qu'aucun renvoi court
  ne vise ce basename. Refus sec, ou avertissement qui devient refus lorsqu'un renvoi
  court existe ? — **verdict de Sidy** (porté à la spec comme question, non tranché).
- **Périmètre exact** : les cinq circuits seuls, ou aussi `protocoles/` et les artefacts
  dérivés d'`index-lexical/` ? — mesure à faire avant de trancher.
