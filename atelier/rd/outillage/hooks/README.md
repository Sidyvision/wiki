---
title: "Hooks git du dépôt — garde-fous locaux"
type: outillage
tags: [rd, outillage, hooks, git, verification, protocole]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination]]"
---

# Hooks git du dépôt

```bash
bash atelier/rd/outillage/hooks/installer-hooks.sh
```

**À exécuter après tout clone du dépôt.** `.git/hooks/` n'est pas versionné :
sans cette commande, un clone frais repart sans aucun garde-fou, et rien ne le
signale.

| Hook | Quand | Ce qu'il refuse |
|---|---|---|
| `pre-commit` | à chaque commit | caractères Unicode invisibles dans les fichiers indexés (Cmd 15) |
| `pre-push` | à chaque push | dépôt en défaut aux invariants, ou caractère invisible dans toute fiche suivie |

## Pourquoi ils existent

**`pre-commit`** date du 2026-08-22, écrit après l'incident de contamination par
*zero-width joiner* — voir
[[atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination]]. Il vivait
depuis lors **uniquement dans `.git/hooks/` de la machine de travail** : un clone
du dépôt repartait sans lui. Il est versé ici le 2026-09-01, inchangé.

**`pre-push`** est ouvert le 2026-09-01 (chantier `PRO-01`, verdict de Sidy).
La branche `main` est protégée côté GitHub et exige le contrôle `lint`, mais
`enforce_admins` est à `false` — le propriétaire du dépôt, sous l'identité duquel
poussent aussi les douze agents Hermes, y échappe. Ce réglage est **acté**, non
subi : le durcir imposerait un flux par pull request à treize acteurs qui
poussent aujourd'hui en direct, depuis un terminal iPad ou depuis un cron.

La contrepartie de ce choix est ce hook. Il exécute **exactement** ce que le CI
exécute, dans le même ordre — `verifier-invariants.py`, puis l'hygiène Unicode —
de sorte qu'un push accepté ici soit vert là-bas. Un garde-fou qui diverge de la
porte qu'il double ne sert qu'à donner confiance à tort.

## Ce que ces hooks ne sont pas

Des serrures. `git commit --no-verify` et `git push --no-verify` les contournent,
**délibérément** : une réparation en deux temps ou une urgence assumée doit
rester possible. Ils empêchent l'inattention, pas la décision.

Ils ne remplacent pas non plus le contrôle serveur : le `lint` de GitHub reste
le juge de dernier ressort, et c'est lui qui verra ce qui aurait été poussé avec
`--no-verify`.

## Note de méthode

En écrivant le contrôle d'hygiène Unicode — deux fois, dans le workflow CI puis
dans ce hook — les caractères invisibles y ont d'abord été inscrits
**littéralement**, c'est-à-dire la faute même que le contrôle traque. Corrigé
dans les deux cas en points de code échappés — la chaîne `\u200d` écrite
caractère par caractère, jamais le caractère lui-même.

Cela s'est produit une troisième fois dans le présent fichier, à la phrase même
qui décrit la leçon — le hook l'a signalée avant le commit, ce qui est
exactement son office.

La leçon vaut d'être retenue : **l'outil qui fait respecter une règle est le
premier endroit où on l'enfreint**, parce qu'on y manipule précisément la chose
interdite. Tout script de détection doit désigner ce qu'il cherche, jamais le
contenir.
