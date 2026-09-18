---
title: "OUT-20 — unicité des basenames, garde du wikilink court : spécification"
type: outillage
chantier: OUT-20
tags: [atelier, rd, outillage, chantier, spec, wikilink, controle]
created: 2026-09-18
updated: 2026-09-18
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/out-20-unicite-des-basenames/intent]]"
---

# OUT-20 — unicité des basenames, garde du wikilink court : spécification

## Comportement observable

Un contrôle **B9** s'ajoute à `verifier-invariants.py`. Il balaie les fichiers `.md`
suivis par git dans le périmètre retenu, groupe par **basename sans extension**, et
signale tout basename porté par **plus d'un chemin**. Le message nomme les chemins en
cause, tous, dans l'ordre alphabétique — jamais « 2 fichiers en conflit » sans dire
lesquels.

Sont **exemptés par nom**, parce qu'ils sont homonymes par convention et cibles d'aucun
renvoi court : `index.md`, `annales.md`, `meta-index.md`, `meta-annales.md`, `CLAUDE.md`,
`README.md`, `LISEZ-MOI.md`, `SKILL.md`, `intent.md`, `spec.md`, `plan.md`. La liste est
**close et nommée dans le code**, jamais devinée par motif.

Le contrôle **ne renomme rien** et ne propose aucun gagnant (Cmd 12).

## Données consommées / produites

- **Entrée** : `git ls-files '*.md'` — la même vue que le reste du vérificateur, qui
  ne contrôle que ce que git suit.
- **Sortie** : des lignes sur la sortie standard, au format des autres codes
  (`[B9] <basename> — porté par N fichiers : <chemin1>, <chemin2>`), et l'entrée
  correspondante dans le JSON de `verifier_invariants` (organe MCP, §VIII.11).
- **Aucun fichier écrit.**

## Critères d'acceptation

1. `python3 verifier-invariants.py --racine /root/wiki` rend **0 erreur, 71
   avertissements** — la ligne de base du 2026-09-18 — et **aucune ligne `[B9]`**.
2. Dans une copie jetable hors dépôt vivant, `cp doctrinal/symboles/barzakh.md
   atelier/rd/barzakh.md` puis `git add` de la copie : le contrôle **refuse**, et la
   ligne nomme **les deux chemins**.
3. Le fichier piégé retiré, le contrôle revient au vert sans intervention.
4. La collision entre deux `plan.md` de deux dossiers de chantier distincts **ne
   déclenche rien** (exemption nommée).
5. La sortie JSON de l'entrée MCP `verifier_invariants` porte B9 au même titre que les
   autres codes — un contrôle que l'organe de vérification ne rend pas n'est pas
   vérifiable à distance.

## Cas limites

- **Deux fichiers de même basename dont aucun n'est cible d'un renvoi court** : le
  défaut est latent, pas actif. C'est la question ouverte de l'intent — refus sec ou
  avertissement conditionnel —, **soumise à Sidy**, non tranchée ici. **Chiffrée le
  2026-09-18** (étape 1 du plan) : **17 collisions entre circuits existent déjà**, dont
  12 sont la trace voulue de la migration du 2026-08-08 ; **aucune n'est visée par un
  renvoi court**. Un refus sec échouerait donc 17 fois dès la première exécution, sur des
  doublons voulus.
- **Basename identique entre un circuit et `textes/` ou `protocoles/`** : ces deux
  dossiers ne sont cible d'aucun wikilink (§II). Périmètre à trancher : les exclure,
  ou les inclure pour prévenir une future ouverture. **Mesure à faire d'abord** : combien
  de collisions existent aujourd'hui entre un circuit et ces deux dossiers.
- **Renommage en cours de session** : le contrôle lit `git ls-files`, donc l'index —
  un fichier créé et non `git add` est invisible, exactement comme pour les autres
  codes. L'écart est connu, il n'est pas propre à B9.

## Ce qui reste `to-source`

Rien : ce chantier ne porte aucune affirmation factuelle sur une source externe. Les
deux seules valeurs citées — 589 occurrences, 156 fiches — sont une mesure du dépôt,
reproductible par le script joint au `plan.md`.
