---
title: "Veille infrastructure quotidienne — script livré, automatisation non câblée (2026-08-23)"
type: infrastructure
statut_experience: exploratoire
tags: [rd, infrastructure, veille, cron, hermes, verification]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
---

# Veille infrastructure quotidienne — script livré, automatisation non câblée

> **Contrepartie neutre**, écrite le 2026-09-01, d'une fiche de session du 2026-08-23 qui
> a été versée le même jour au Domaine Réservé parce qu'elle mêlait à l'ingénierie du fait
> personnel (§VI). Ce qui suit ne retient que la face publiable : ce qui a été écrit, ce
> qui tourne, ce qui ne tourne pas.

## Ce qui existe réellement, vérifié au disque le 2026-09-01

| Pièce | État constaté |
|---|---|
| `atelier/rd/infrastructure/scripts/veille-infrastructure-quotidien.sh` | **existe**, exécutable (`-rwxr-xr-x`, 1745 octets, 2026-08-23) |
| Job cron `veille-infrastructure-quotidien` | **n'existe dans aucun profil Hermes** |
| Job cron `veille-rd-hebdomadaire` | **n'existe dans aucun profil Hermes** |
| Job cron `investigation-doctrinale-gardien` | **n'existe dans aucun profil Hermes** |

Méthode : lecture de `/root/.hermes/profiles/*/cron/jobs.json` sur les quatorze profils
présents (`accounting`, `admin-legal`, `ar-music`, `commerce`, `default`, `distribution`,
`fanzine`, `gardien`, `karubi`, `marketing`, `production`, `publication`, `studio`,
`visual-da`). Les jobs réellement déclarés sont : `cycle-choura` sur douze profils,
`veille-protocole-gardien` (gardien), `point-hebdo-marketing` (marketing),
`veille-referencement-investigation-08` (publication), et sur `studio`
`monitoring-infrastructure-quotidien`, `coherence-infrastructure-brute`,
`archiver-monitoring-quotidien`.

## L'écart, et ce qu'il apprend

La fiche de session du 2026-08-23 affirmait le cron **créé**, identifiant à l'appui
(`6bc182f45d2c`), avec sa cadence et son canal de livraison. Rien de tel n'est déclaré
aujourd'hui. Deux lectures sont possibles et **cette fiche ne tranche pas** entre elles :
le job a pu être créé puis perdu lors d'une reconfiguration ultérieure (la migration
OmniRoute du 2026-08-26, la migration des prompts du 2026-08-31), ou il n'a jamais existé.
Ce qui est établi, c'est l'état d'aujourd'hui.

C'est **le même motif que l'incident du 2026-08-17**, qui a fait naître le champ
`infra_verif` : une fiche avait affirmé la création d'un job cron qui n'avait jamais été
créé (registre des problèmes, entrée `[2026-08-17]`). La leçon n'a manifestement pas
suffi : elle vaut pour toute fiche qui déclare une configuration appliquée. La règle est
qu'une affirmation d'infrastructure se vérifie mécaniquement, jamais sur déclaration
narrative — c'est le principe même du §VIII.2 (*le résultat brut précède toujours
l'interprétation*) et du couple `verifier-coherence-infrastructure.py` / `infra_verif`.

**Aucun `infra_verif` n'est porté par la présente fiche**, et c'est délibéré : ce champ
atteste une configuration *appliquée*. Il n'y en a pas à attester. L'inscrire ici ferait
échouer le contrôle, ce qui serait la bonne conséquence d'une mauvaise écriture.

## Ce que fait le script

Quatre sections, produites sur `stdout` (mode `no_agent` : la sortie est délivrée telle
quelle, aucun argument n'est transmis par le job — c'est la contrainte relevée le
2026-08-18 pour `archiver-monitoring-quotidien`). Il appelle `verifier-invariants.py` sur
la racine du dépôt et n'échoue jamais (`|| true`), afin qu'un dépôt en défaut n'interrompe
pas le rapport.

> Depuis le 2026-09-01, `verifier-invariants.py` restreint son parcours au périmètre du
> dépôt (chantier `OUT-C2` du registre) : la section correspondante du rapport passe de
> 210 lignes d'erreurs, presque toutes du bruit de dépendances tierces, à une sortie
> lisible. Le rapport quotidien redevient exploitable si le cron est un jour câblé.

## Suite

Le chantier reste ouvert au registre sous `INF-03` — décisions entièrement tranchées
depuis le 2026-08-11, **aucun automatisme écrit**. Une proposition de reprise datée du
2026-08-31 attend le verdict de Sidy. Le présent constat ne change pas ce statut : il le
documente, et retire une affirmation contraire qui circulait depuis huit jours.
