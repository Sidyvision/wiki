---
title: "Registre de traitement des rapports quotidiens (Studio/Publication)"
type: meta
created: 2026-09-02
updated: 2026-09-02
tags: [atelier, rd, infrastructure, monitoring, registre]
sources: []
links:
  - "[[atelier/rd/infrastructure/monitoring-archive-charte]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
---

# Registre de traitement des rapports quotidiens

## Motif

Ouvert le 2026-09-02 (demande Sidy), en réponse à un risque concret constaté
dans la session du jour : deux sessions distinctes (Sidy en direct, une
session Claude Code) ont pu retraiter les mêmes suggestions d'un rapport
Studio/Publication sans que ni l'une ni l'autre ne puisse savoir que
l'autre était déjà passée. Ce registre ne remplace aucun des cahiers
existants (`registre-problemes.md` porte le diagnostic et la résolution) : il
répond à une question strictement antérieure — *« ce rapport a-t-il déjà été
regardé par quelqu'un ? »* — avant même d'ouvrir son contenu.

## Ce que ce registre couvre, et depuis quand

**Ne couvre que les rapports à partir du 2026-09-02.** Les huit rapports
Studio déjà archivés avant cette date (`monitoring-archive/2026-08-{17,18,19,
27,28,29,30,31}_41dc3e7e492c.txt`) sont **hors périmètre par construction** —
ce registre n'existait pas encore. Leur traitement se retrouve, au cas par
cas, dans `registre-problemes.md` (entrées `[2026-08-17]`, `[2026-08-18]`,
etc.) : absence d'entrée ici pour eux n'est **pas** un signal de rapport non
traité, contrairement à ce qui vaut pour tout rapport postérieur au
2026-09-02 (§ Règle d'usage). Choix délibéré, plutôt que de reconstituer
rétroactivement huit entrées sur la seule foi d'une lecture a posteriori —
ce registre décrit ce qui a été vu au moment où ça a été vu, pas une
reconstitution.

## Règle d'usage

Avant de traiter un rapport (archivé ou collé en session) : **grepper ce
fichier** sur le triplet `(profil, job_id, date du rapport)`. Une entrée déjà
présente signifie que le rapport a déjà été regardé — vérifier son résumé et
son lien avant de retraiter quoi que ce soit en double. Absence d'entrée pour
un rapport postérieur au 2026-09-02 = rapport non encore traité.

Après traitement d'un rapport (qu'il ait produit une correction, une fausse
alerte close, ou rien à faire) : **ajouter une entrée**, quelle que soit
l'issue — un rapport qui n'appelait aucune action reste un rapport traité, au
même titre qu'un cycle Choura « rien de neuf à signaler » reste une
contribution légitime.

**Qui écrit ici** : Sidy directement, ou une session Claude Code sous
consigne explicite — même gouvernance que `queue-idees.md`. Les agents Hermes
eux-mêmes n'écrivent jamais ici (Discord-Validation, comme partout ailleurs :
signalement seulement).

**Format** — une entrée par rapport, jamais par lot (un lot de plusieurs
rapports traités dans la même passe reçoit une entrée par rapport, toutes
datées du jour de la passe et renvoyant au même détail) :

```markdown
## [YYYY-MM-DD] traite | <profil> | <job_id> | rapport du YYYY-MM-DD

**Rapport** : lien vers l'archive (`monitoring-archive/...txt`) si
  archivée, sinon "collé en session, non archivé — cf. INF-15".
**Traité par** : Sidy directement | session Claude Code.
**Résumé** : une ligne (ce que le rapport disait, ce qui en a été fait).
**Détail** : lien vers l'entrée `registre-problemes.md` et/ou l'annales
  correspondante.
**Commit** : sha (rempli après le commit qui clôt le traitement, jamais avant
  — même règle que Cmd 9).
```

<!-- INSERTION: EN-TÊTE -->

## [2026-09-02] traite | publication | ad3152b237bb | rapport du 2026-09-01

**Rapport** : collé en session par Sidy, non archivé — cf. `INF-15`
(`monitoring-archive-charte.md` n'archive que le job Studio). Rapport
partiellement corrompu au collage : ses items « 4 »/« 5 » sont un duplicata
exact du rapport de la veille — écartés, non traités comme des constats
nouveaux du 2026-09-01.
**Traité par** : session Claude Code.
**Résumé** : ses deux points substantiels (210 erreurs, `hermeneutique/annales.md`)
étaient déjà clos le jour même par d'autres passes (`OUT-C2`, `PRO-C1`) ; rien
à faire.
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]`
« Deux rapports Publication collés par Sidy depuis Discord », point 4.
**Commit** : 2910adf

## [2026-09-02] traite | publication | ad3152b237bb | rapport du 2026-08-31

**Rapport** : collé en session par Sidy, non archivé — cf. `INF-15`.
**Traité par** : session Claude Code.
**Résumé** : `sources:` nu corrigé en `[]` sur deux fiches (défaut réel) ;
« lien non résolu » sur `atma.md` écarté (fausse alerte, les deux fiches
existent) ; trois recommandations de sourcing `raw/` signalées mais non
vérifiables depuis cette session (`raw/` exclu de git).
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]`
« Deux rapports Publication collés par Sidy depuis Discord », points 1-3.
**Commit** : 2910adf

## [2026-09-02] traite | studio | 41dc3e7e492c | rapport du 2026-08-31

**Rapport** : `monitoring-archive/2026-08-31_41dc3e7e492c.txt`, lu dans la
même passe que les trois entrées suivantes (2026-08-28 à 30).
**Traité par** : session Claude Code.
**Résumé** : écart `DISCORD_HOME_CHANNEL` du profil `gardien` corrigé (six
jours de fausse alerte identique) ; fausse alerte « script détecteur
manquant » close ; deux suggestions déjà résolues reconfirmées (frontmatter
`generer-cartographie.py`, fichier non suivi) ; gateways en échec et angle
mort d'archivage Publication signalés, non actionnables depuis cette session.
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]`
« Reprise des rapports Studio/Publication des derniers jours ».
**Commit** : 79b253b

## [2026-09-02] traite | studio | 41dc3e7e492c | rapport du 2026-08-30

**Rapport** : `monitoring-archive/2026-08-30_41dc3e7e492c.txt`, même passe
que l'entrée du 2026-08-31 ci-dessus (même résumé et même détail).
**Traité par** : session Claude Code.
**Résumé** : idem entrée du 2026-08-31.
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]`
« Reprise des rapports Studio/Publication des derniers jours ».
**Commit** : 79b253b

## [2026-09-02] traite | studio | 41dc3e7e492c | rapport du 2026-08-29

**Rapport** : `monitoring-archive/2026-08-29_41dc3e7e492c.txt`, même passe
que l'entrée du 2026-08-31 ci-dessus (même résumé et même détail).
**Traité par** : session Claude Code.
**Résumé** : idem entrée du 2026-08-31.
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]`
« Reprise des rapports Studio/Publication des derniers jours ».
**Commit** : 79b253b

## [2026-09-02] traite | studio | 41dc3e7e492c | rapport du 2026-08-28

**Rapport** : `monitoring-archive/2026-08-28_41dc3e7e492c.txt`, même passe
que l'entrée du 2026-08-31 ci-dessus (même résumé et même détail).
**Traité par** : session Claude Code.
**Résumé** : idem entrée du 2026-08-31.
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]`
« Reprise des rapports Studio/Publication des derniers jours ».
**Commit** : 79b253b
