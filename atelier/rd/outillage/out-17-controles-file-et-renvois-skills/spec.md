---
title: "OUT-17 — Contrôles manquants de la file d'écritures de skills : spécification"
type: outillage
chantier: OUT-17
tags: [atelier, rd, outillage, chantier, spec, skills, controles]
created: 2026-09-15
updated: 2026-09-15
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/infrastructure/2026-09-15_file-attente-morte-ecritures-skills]]"
---

# OUT-17 — Contrôles manquants de la file d'écritures de skills : spécification

## Comportement observable

Trois pièces, déterministes — sans LLM, sans réseau, exécutables seules, sans effet de bord :

1. **`etat-file-skills.py`** — parcourt `<HERMES_HOME>/pending/skills/` de chaque profil
   présent sous `/root/.hermes/profiles/`, plus le profil par défaut. Rend, en texte lisible
   **et** en `--json` : le nombre de positions en file par profil, la plus ancienne, la plus
   récente, et pour chaque position sa **conformité au contrat du magasin** — description
   ≤ 60 caractères, frontmatter YAML lisible, champ `name:` présent — ainsi que la mention
   d'une **redite** (même couple (skill, action) déjà présent en file).
2. **`verifier-renvois-skills.py`** — pour chaque skill installé d'une racine donnée (défaut :
   toutes les racines de skill de la flotte), extrait les chemins **déclarés** de forme
   `references/…`, `templates/…`, `scripts/…`, `assets/…` et vérifie leur existence sur le
   disque. Signale les manquants en nommant le skill **et** le chemin.
3. **Une ligne de rapport** — la sortie condensée de la première pièce, destinée à être
   appelée par un job existant. Le chantier **écrit** cette ligne ; il **ne modifie pas** le
   job (point de retour à l'humain).

## Données consommées / produites

- **Entrées** : `<HERMES_HOME>/pending/skills/*.json` (lecture seule),
  `<HERMES_HOME>/skills/**/SKILL.md` (lecture seule).
- **Sorties** : texte sur la sortie standard ; `--json` optionnel ; codes de sortie non nuls
  en cas d'anomalie.
- **Aucune écriture** dans le dépôt, dans les stores de skills ni dans la file. Sens unique du
  §VII respecté : ces contrôles **lisent**, ils n'écrivent jamais.

## Critères d'acceptation

1. `python3 etat-file-skills.py` sur une flotte à file vide n'imprime **pas** un silence : il
   nomme « file vide » et le nombre de profils examinés.
2. Sur une **faute fabriquée** — une position dont la description fait 61 caractères — le
   script la **compte comme inapte** et la nomme (§VII : faute → cri).
3. `python3 verifier-renvois-skills.py` lancé sur la flotte retrouve les renvois morts
   constatés le 2026-09-15 **s'ils sont encore présents**, et **n'en invente aucun** sur un
   skill sain.
4. Un chemin cité comme **exemple pédagogique** dans une phrase n'est **pas** signalé comme
   renvoi mort (cas limite traité, cf. ci-dessous).
5. Les deux scripts sortent en code non nul **si et seulement si** une anomalie est détectée ;
   `--strict` étend le non-zéro aux inaptes non bloquants.
6. La ligne de rapport tient en **une ligne** et nomme profil, positions, plus ancienne,
   inaptes.

## Cas limites

- **Dossier absent** (profil sans écriture en attente) : ne pas confondre *file vide* et
  *dossier absent* — le dire, distinctement.
- **Position illisible** (JSON corrompu) : compter comme anomalie, jamais l'ignorer en
  silence.
- **Chemin cité dans une phrase** : dans un `SKILL.md`, `` `scripts/foo.py` `` au fil d'un
  exemple n'est pas une déclaration de fichier. Ne crier que sur les déclarations — listes des
  sections « Fichiers de la skill » / « Fichiers support » et cartouches. *Un contrôle qui
  crie à tort est ignoré ensuite, donc il ment par omission.*
- **Pièce détenue hors des quatre dossiers** : ne pas inventer de règle ; contrôler seulement
  les quatre formes déclarables.

## Ce qui reste `to-source`

Aucun. Ce chantier ne dépend d'aucune source primaire.
