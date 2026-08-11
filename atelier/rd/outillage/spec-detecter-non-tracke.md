---
title: "Spécification — Détecteur de fichiers non trackés (par circuit)"
type: outillage
tags: [rd, outillage, git, vigilance]
created: 2026-08-11
updated: 2026-08-11
sources: []
links: ["[[atelier/rd/cahiers/registre-problemes]]"]
---

# Spécification — `detecter-non-tracke.py`

> Piste C des « 4 pistes outillage » instruites en session R&D du 2026-08-11
> (voir [[atelier/rd/cahiers/registre-problemes]]). Script déterministe,
> même famille que `verifier-invariants.py` : ni LLM, ni réseau, ne corrige
> rien.

## 1. Problème traité

Un fichier peut rester non tracké (jamais `git add`, ou modifié sans être
stagé) d'une session à l'autre sans que rien ne le signale explicitement —
faute d'un geste `git status` systématique. Un brouillon oublié, un asset
déposé avant sa fiche, ou un script fraîchement écrit (cas de ce script
lui-même, auto-détecté à son premier essai) restent invisibles entre deux
sessions d'intégration.

## 2. Fonctionnement

`atelier/rd/outillage/detecter-non-tracke.py [--racine /root/wiki] [--json]`

1. Exécute `git status --porcelain` à la racine du dépôt.
2. Classe chaque chemin par circuit (`doctrinal`, `atelier`, `label`,
   `hermeneutique`, `meta`), ou `hors-circuit` (dossiers de service :
   `raw/`, `_inbox/`, `Graphe/`, `.git/`), ou `hors-circuit-inconnu` (signal
   d'alerte : chemin racine non reconnu — nouveau dossier ? faute de frappe ?).
3. Affiche un décompte par circuit, ou un JSON structuré (`--json`).

**Codes de sortie** : `0` aucun fichier non tracké · `1` au moins un fichier
non tracké (constat, pas une erreur) · `2` erreur d'exécution (pas un dépôt
git, `git` introuvable).

## 3. Ce que le script ne fait pas

- Ne stage rien, ne commite rien, ne supprime rien.
- Ne juge pas si un fichier non tracké est une anomalie : un brouillon en
  cours est un état légitime. Le constat revient à l'humain (Cmd 13).
- Ne couvre pas les fichiers *trackés mais divergents* d'un remote (ce
  périmètre reste à `git status -sb` / `git rev-list`, cf.
  [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]] §6).

## 4. Écart volontaire avec `verifier-invariants.py`

`verifier-invariants.py` ne connaît que 4 circuits (`CIRCUITS = ["doctrinal",
"atelier", "label", "meta"]`) — `hermeneutique/` en est absent, angle mort
non corrigé à ce jour. Ce script traite les cinq circuits du protocole
(`CLAUDE.md` §II) pour ne pas reproduire cet angle mort. Si un fichier
`hermeneutique/` apparaît un jour classé `hors-circuit-inconnu` par erreur,
c'est un signal à consigner au registre, pas à corriger silencieusement ici.
