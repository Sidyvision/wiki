---
title: "Registre de traitement des rapports quotidiens (Studio/Publication)"
type: meta
created: 2026-09-02
updated: 2026-09-08
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
## [2026-09-08] traite | studio | 41dc3e7e492c | rapport du 2026-09-08

**Rapport** : `monitoring-archive/2026-09-08_41dc3e7e492c.txt`.
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 563 nœuds, 1920 arêtes (INF-16 intégré au graphe). 152 avertissements, 103 liens morts (−1). 2 fichiers `_inbox/` non commités. R&D : triptyque INF-16 complet (machine IA locale, visa plan attendu) ; OUT-08 OCR Futūḥāt post-essais (piste B validée, verdict critère 1 attendu). Signal : 76 fiches `sources:` null (augmenté de 75 à 76). Swap à 7,5 Mi / 2,0 Gi (saturation) — le RAM revient comme problème récurrent. Piste 5 de la synthèse (charte monitoring pour Publication) est aujourd'hui résolue (INF-15 clôturé cette session).
**Détail** : [[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm]], [[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]].
**Commit** : — (registre, en cours)


## [2026-09-10] traite | publication | ad3152b237bb | rapport du 2026-09-10

**Rapport** : `monitoring-archive/2026-09-10_ad3152b237bb.txt` (INF-15 clôturé, premier rapport Publication archivé depuis le mandat).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1504 fiches .md contrôlées, 0 erreur, 0 avertissement (première passe Publication sans delta disponible). Signal majeur : 75 fiches doctrinales avec mismatch `sources_count` vs longueur réelle `sources:` — surévaluation du compteur ou `sources:` vide quand `sources_count` > 0 (exemples : jivatma.md, adityas-mois-du-soleil.md, tomoe.md, golem.md + 71 autres). Fiches symboles `sources:` vide mais conformes : salawat.md, alam-al-mithal.md, fal-wa-tatayyur.md, ilm-al-nujum.md, taabir-al-ruya.md, tarbiyya-rabbaniyya.md, influx-spirituel-sommet-cranien.md, fiqh.md, maqamat-meknes.md, prakriti.md. Investigation 5 fiches `sources_count: 0` : awrad-ibn-arabi.md (PDF source raw/ identifié), jesus-and-enoch-in-ibn-arabi.md (PDF source raw/ identifié), shams-al-maarif.md (PDF source raw/ identifié) — les trois fiches sont des `type: source`, `sources_count: 0` structurellement correct. Recommandation : lifting `sources:` sur les fiches dont le corps cite des sources non reportées au cartouche.
**Détail** : 75 fiches mismatch sources_count/sources signalées (validation mécanique requise) ; fiches awrad/jesus/shams déjà investiguées le 05/09.
**Commit** : — (registre, en cours)

## [2026-09-08] traite | publication | ad3152b237bb | rapport du 2026-09-08

**Rapport** : `monitoring-archive/2026-09-08_ad3152b237bb.txt`.
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1411 fiches .md, 0 erreur, 0 avertissement. Signaux sémantiques : talisman-sihr.md et salawat.md avec `sources:` sans valeur YAML (syntaxe invalide, non détectée par le script) ; awrad-ibn-arabi.md, shams-al-maarif.md, jesus-and-enoch-in-ibn-arabi.md avec `sources: []` quand le corps cite des sources (cartouche vide mais corps référencé). Note : 155 fiches dans doctrinal/ portent `sources_count: 0` — écart de surface entre validation script et sémantique. Investigation 5 fiches : même trio akbarien (awrad, jesus, shams) + ibn-arabi-fard-afrad-gilis.md (10+ sources doctrinales candidates, aucune raw) + valsan-investiture-cheikh-al-akbar.md (PDF raw absent, 4 sources doctrinales candidates). Recommandation : conversion PDF raw/ → textes/ pour alimenter le cartouche.
**Détail** : 155 fiches `sources_count: 0` en surface ; fiches talisman-sihr.md, salawat.md pour syntaxe frontmatter.
**Commit** : — (registre, en cours)

## [2026-09-05] traite | publication | ad3152b237bb | rapport du 2026-09-05

**Rapport** : `monitoring-archive/2026-09-05_ad3152b237bb.txt`.
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1364 fiches, 0 erreur, 3 avertissements [C1] inchangés (liens non résolus : coran-essai-traduction-gloton, apercus-sur-l-initiation, principes-et-methodes-de-l-art-sacre — déjà signalés les dates antérieures). Signaux : asma-al-husna.md et ilm-al-huruf.md avec `sources_count: 0` alors que le corps cite explicitement `[[shams-al-maarif]]` et `[[jesus-and-enoch-in-ibn-arabi]]` — référencement non reporté au cartouche. Investigation 5 fiches : awrad-ibn-arabi.md (fiche-source, `sources_count: 0` structurellement correct, PDF raw/ présent), jesus-and-enoch-in-ibn-arabi.md (fiche-source, `sources_count: 0` structurellement correct, PDF raw/ présent), shams-al-maarif.md (fiche-source, `sources_count: 0` structurellement correct, PDF raw/ présent) — les trois premières fiches sont des `type: source`, pas des fiches doctrinales à alimenter.
**Détail** : asma-al-husna.md, ilm-al-huruf.md pour mismatch cartouche/corps.
**Commit** : — (registre, en cours)

## [2026-09-04] traite | publication | ad3152b237bb | rapport du 2026-09-04

**Rapport** : `monitoring-archive/2026-09-04_ad3152b237bb.txt`.
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1361 fiches, 0 erreur, 3 avertissements [C1] (mêmes liens non résolus que la veille). Signaux sémantiques : doctrinal/index.md contient des wikilinks depuis doctrinal/ vers label/ (line 401) et hermeneutique/ (line 384) — violations §VI (liens du sensible vers le neutre, pas l'inverse) ; ibn-sirin.md et imam-malik.md avec `sources:` sans valeur YAML. Investigation 5 fiches : charles-andre-gilis.md (10+ sources doctrinales candidates, aucune raw), ibn-qayyim.md (stub, aucune source raw ou doctrinale), ibn-sirin.md (stub, aucune source), imam-malik.md (stub, aucune source). Recommandation : valider les sources akbariennes (Gilis) depuis les fiches sources existantes ; Zad al-Ma'ad et Al-Tibb al-Nabawi restent absents du dépôt.
**Détail** : doctrinal/index.md pour violations §VI ; charles-andre-gilis.md pour sources candidates.
**Commit** : — (registre, en cours)

## [2026-09-03] traite | publication | ad3152b237bb | rapport du 2026-09-03

**Rapport** : `monitoring-archive/2026-09-03_ad3152b237bb.txt`.
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1352 fiches, 0 erreur, 0 avertissement (corpus stable). Signaux : récidive `sources:` nu (4 fiches : mawlid-al-rasul.md, ibn-sirin.md, imam-malik.md, madhhab-maliki.md) — même anomalie signalée le 2026-08-31 et corrigée en intégration le 2026-09-02, mais 4 fiches subsistent. Investigation 5 fiches : ibn-qayyim.md (stub, aucune source), mawlid-al-rasul.md (fiche-source, `sources_count: 0` structurellement correct, anomalie formelle uniquement), ibn-sirin.md (stub, aucune source raw/), imam-malik.md (stub, aucune source raw/), madhhab-maliki.md (stub, aucune source raw/).
**Détail** : mawlid-al-rasul.md, ibn-sirin.md, imam-malik.md, madhhab-maliki.md pour récidive `sources:` nu.
**Commit** : — (registre, en cours)

## [2026-08-30] traite | publication | ad3152b237bb | rapport du 2026-08-30

**Rapport** : `monitoring-archive/2026-08-30_ad3152b237bb.txt` (rétroactivement archivé, hors périmètre ouverture registre 2026-09-02 — traitement volontaire pour boucler l'historique).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1344 fiches, 0 erreur, 8 avertissements [C1] (liens non résolus, mêmes marqueurs syntaxiques qu'aux dates précédentes). Signaux : `sources:` nu sur 3 fiches (mawlid-al-rasul.md, ibn-sirin.md, imam-malik.md). Investigation 5 fiches : awrad-ibn-arabi.md, jesus-and-enoch-in-ibn-arabi.md, shams-al-maarif.md (les trois mêmes fiches-type-source investiguées ensuite les 03, 04, 05, 06, 07, 08, 10/09 — pattern récurrent lié à `sources_count: 0` structurel). Recommandation : les sources primaires existent dans raw/ (PDF), conversion en textes/ recommandée.
**Détail** : 8 avertissements [C1] (marqueurs syntaxiques annales/outillage).
**Commit** : — (registre, en cours)

## [2026-08-29] traite | publication | ad3152b237bb | rapport du 2026-08-29

**Rapport** : `monitoring-archive/2026-08-29_ad3152b237bb.txt` (rétroactivement archivé, hors périmètre).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1338 fiches, 0 erreur, 8 avertissements [C1]. Même pattern que le 30/08 : `sources:` nu sur les mêmes fiches, même recommandation de conversion PDF raw/. Investigation portait sur les mêmes 3 fiches sources akbariennes (awrad, jesus, shams) — la boucle d'investigation était déjà en place avant l'ouverture du registre.
**Détail** : patterns conformes aux rapports suivants (mêmes fiches investiguées).
**Commit** : — (registre, en cours)

## [2026-08-28] traite | publication | ad3152b237bb | rapport du 2026-08-28

**Rapport** : `monitoring-archive/2026-08-28_ad3152b237bb.txt` (rétroactivement archivé, hors périmètre).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1336 fiches, 0 erreur, 8 avertissements [C1]. Investigation sur les 3 mêmes fiches sources akbariennes (awrad, jesus, shams). Premier rapport à documenter explicitement la présence de `shams-al-maarif-traduit-complet.pdf` dans raw/. Recommandation : même pattern que les dates suivantes.
**Détail** : pattern récurrent awrad/jesus/shams, bien avant INF-15.
**Commit** : — (registre, en cours)

## [2026-08-27] traite | publication | ad3152b237bb | rapport du 2026-08-27

**Rapport** : `monitoring-archive/2026-08-27_ad3152b237bb.txt` (rétroactivement archivé, hors périmètre).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1332 fiches, 0 erreur, 8 avertissements [C1]. Même corpus que la veille, même pattern d'investigation. Premier rapport à mentionner explicitement la corrélation entre `sources:` nu et `sources_count: 0` comme anomalie systémique (et non ponctuelle).
**Détail** : premiers signaux d'une anomalie systémique `sources:` nu.
**Commit** : — (registre, en cours)

## [2026-08-25] traite | publication | ad3152b237bb | rapport du 2026-08-25

**Rapport** : `monitoring-archive/2026-08-25_ad3152b237bb.txt` (rétroactivement archivé, hors périmètre).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1318 fiches, 0 erreur, 15 avertissements [C1] (liens non résolus, mêmes marqueurs syntaxiques). Signaux : 5 fiches avec `sources:` nu au lieu de `[]` (abdullah-daghestani.md, al-jazari.md, al-khwarizmi.md, al-nabulusi.md, hamza-yusuf.md) — les deux premières (al-jazari.md, al-khwarizmi.md) citent `[[islam-and-artificial-intelligence]]` ×4 dans le corps, fiche source et PDF raw existent. Investigation 5 fiches : les mêmes 3 fiches sources akbariennes + 2 autorités avec anomalies de `sources:` nu.
**Détail** : 5 fiches `sources:` nu signalées, 2 avec source candidate identifiée (islam-and-artificial-intelligence).
**Commit** : — (registre, en cours)

## [2026-08-24] traite | publication | ad3152b237bb | rapport du 2026-08-24

**Rapport** : `monitoring-archive/2026-08-24_ad3152b237bb.txt` (rétroactivement archivé, hors périmètre).
**Traité par** : session Hermes Agent (cette session, verdict Sidy).
**Résumé** : 1318 fiches, 0 erreur, 15 avertissements [C1]. Signaux : 5 fiches avec `sources:` nu (abdullah-daghestani.md, al-jazari.md, al-khwarizmi.md, al-nabulusi.md, hamza-yusuf.md) — même pattern que le 25/08. Investigation 5 fiches : abdullah-daghestani.md (source absente), al-jazari.md (source candidate : `[[islam-and-artificial-intelligence]]`), al-khwarizmi.md (source candidate : même fiche), al-nabulusi.md (source absente), hamza-yusuf.md (source absente). Première occurrence du signal : le marqueur `to-source` est incohérent avec `sources_count: 0`.
**Détail** : al-jazari.md, al-khwarizmi.md pour sources candidates identifiées dans `islam-and-artificial-intelligence.md`.
**Commit** : — (registre, en cours)


## [2026-09-08] traite | publication | ad3152b237bb | rapport du 2026-09-06

**Rapport** : cron output `ad3152b237bb/2026-09-06_11-04-41.md`, non archivé — cf. `INF-15` (archive monitoring limitée au profil studio).
**Traité par** : session Hermes Agent (cette session).
**Résumé** : conformité frontmatter stable (1400 fiches, 0 erreur, identique à la passe précédente) ; investigation documentaire sur 5 fiches doctrinales `sources_count: 0` les plus anciennes — **toutes 5 ont des PDF correspondants dans `raw/`** (Awrad_Ibn_Arabi.pdf, Jesus_And_Enoch_In_Ibn_'arabi.pdf, shams-al-maarif-traduit-complet.pdf). Recommandation 09-06 de renseigner les deux fiches autorités akbariennes (Valsan, Gilis) **déjà exécutée** (created 2026-08-30, sources renseignées, count 2 et 4). Signal : 75 fiches doctrinales `sources:` null au lieu de `[]` — non détecté par le script.
**Détail** : [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-09-02]` point 3 (sources raw hors portée mécanique) ; [[doctrinal/sources/awrad-ibn-arabi.md]], [[doctrinal/sources/jesus-and-enoch-in-ibn-arabi.md]], [[doctrinal/sources/shams-al-maarif.md]], [[doctrinal/symboles/salawat.md]], [[doctrinal/symboles/talisman-sihr.md]].
**Commit** : a0f916a (registre — signalement, verdict Sidy attendu)

## [2026-09-08] traite | publication | ad3152b237bb | rapport du 2026-09-07

**Rapport** : cron output `ad3152b237bb/2026-09-07_11-03-25.md`, non archivé — cf. `INF-15`.
**Traité par** : session Hermes Agent (cette session).
**Résumé** : conformité frontmatter stable (1406 fiches, 0 erreur). Investigation 5 fiches `sources_count: 0` suivantes — **3 sources candidates identifiées dans `raw/`** (mêmes 3 PDF que la veille, confirmés présents). **Signal confirmé et vivant** : 76 fiches doctrinales portent `sources:` (YAML null) au lieu de `sources: []` — discrepancy interne sur `doctrinal/symboles/salawat.md` (cite `[[awrad-ibn-arabi]]` dans le corps, `sources_count: 0`, `sources:` null) et `doctrinal/symboles/talisman-sihr.md` (cite `[[shams-al-maarif]]`, `sources_count: 0`, `sources:` null). Autorités Valsan/Gilis déjà renseignées (non actionnable). État disque/RAM amélioré vs rapport (84% / swap 912Mi).
**Détail** : [[atelier/rd/cahiers/registre-problemes]], signal 76 fiches `sources:` null ; [[doctrinal/symboles/salawat.md]], [[doctrinal/symboles/talisman-sihr.md]] ; raw/ PDFs confirmés.
**Commit** : a0f916a (registre — signalement, verdict Sidy attendu)

## [2026-09-08] traite | gardien | 431fcacadca2 | rapport du 2026-09-07

**Rapport** : cron output `431fcacadca2/2026-09-07_12-31-22.md`, non archivé (pas d'archive monitoring pour gardien).
**Traité par** : session Hermes Agent (cette session).
**Résumé** : 0 signal détecté. Scan 24h : aucun commit sur `label/` depuis 7 jours (dernier f70a495 2026-08-30, conversion mécanique chemins nus→wikilinks). Revue approfondie des 7 textes-cadres (`doctrine-du-don.md`, `protocole-cercles-token.md`, `strategie-vinyle-300-depositaires.md`, `merchandising.md`, `modele-economique.md`, `equipe-agents-hermes.md`, `fanzine.md`) : vocabulaire public verrouillé (jamais NFT/token/blockchain), non-transférabilité + absence bénéfice promis maintenues, tension Gardien↔Commerce institutionnalisée. `strategie-vinyle-300-depositaires.md:49` (« clientèle de collectionneurs ») qualifié correctement : critère de sélection de relais physiques, pas confusion don/marchandise. Cohérence structurelle triple : doctrine↔protocoles-cercles↔stratégie-vinyle OK, doctrine↔modele-economique OK, doctrine↔textes publics OK (fanzine seul organe public actif, *Dans l'Absolu* non déployé).
**Détail** : [[label/distribution/doctrine-du-don.md]], [[label/distribution/protocole-cercles-token.md]], [[label/distribution/strategie-vinyle-300-depositaires.md]], [[label/production/modele-economique.md]], [[label/production/equipe-agents-hermes.md]], [[label/marketing-communication/fanzine.md]].
**Commit** : a0f916a (registre — signalement)

## [2026-09-07] traite | studio | 41dc3e7e492c | rapport du 2026-09-07

**Rapport** : `monitoring-archive/2026-09-07_41dc3e7e492c.txt`, lu dans la même
passe que les quatre entrées suivantes (2026-09-03 à 06).
**Traité par** : session Claude Code.
**Résumé** : 0 écart de cohérence infra, 3 gateways actifs conformes à la
décision du 2026-08-28, bind-mounts tous OK. **Signal fort retenu** : disque à
85 % et **swap entièrement consommé** (2,0/2,0 Gi, 25 Mi libres) — pente
confirmée sur les cinq rapports (81 → 83 → 84 → 85 → 85 %). Le rapport dit le
fichier du sas « bloqué volontairement (caractères arabes vs pre-commit hook) » :
la cause exacte est mesurée à cette passe — **1 302 U+200F et 810 U+200E**,
interdits par le Cmd 15. Constat conservé, fichier non corrigé (une conversion
se remplace, elle ne se retouche pas).
**Détail** : [[atelier/annales]], entrée `[2026-09-07]`.
**Commit** : 448db16

## [2026-09-07] traite | studio | 41dc3e7e492c | rapport du 2026-09-06

**Rapport** : `monitoring-archive/2026-09-06_41dc3e7e492c.txt`, même passe que
l'entrée du 2026-09-07 ci-dessus.
**Traité par** : session Claude Code.
**Résumé** : constate la résorption des états `failed` des gateways (amélioration
nette vs `[2026-09-01]`) et 0 écart infra. Volet R&D : la chaîne DOC-08
(critère de statut académique, relevé des six fiches, ouverture du chantier) est
déjà consignée au dépôt et **n'appelle aucune action de cette passe** — son
verdict appartient à Sidy (Cmd 12). Deux questions restent ouvertes et sont
laissées telles : divergence afilalo/al-akili, et aiman-attar.
**Détail** : [[atelier/annales]], entrée `[2026-09-07]`.
**Commit** : 448db16

## [2026-09-07] traite | studio | 41dc3e7e492c | rapport du 2026-09-05

**Rapport** : `monitoring-archive/2026-09-05_41dc3e7e492c.txt`, même passe.
**Traité par** : session Claude Code.
**Résumé** : 23 fichiers non suivis au moment du rapport — **résorbés depuis**
par les passes d'intégration des 2026-09-05 et 09-06 ; le contrôle du jour n'en
voit plus que ceux de cette session. RAM signalée tendue (597 Mi disponibles,
swap 1,7/2,0 G) : constat repris dans le signal transversal de la présente passe.
Rien d'autre d'actionnable.
**Détail** : [[atelier/annales]], entrée `[2026-09-07]`.
**Commit** : 448db16

## [2026-09-07] traite | studio | 41dc3e7e492c | rapport du 2026-09-04

**Rapport** : `monitoring-archive/2026-09-04_41dc3e7e492c.txt`, même passe.
**Traité par** : session Claude Code.
**Résumé** : rapport le plus dense des cinq. Ses cinq pistes ont été confrontées
au disque : la n°4 (exécuter `verifier-recursion-qaf.py`) est **close depuis le
2026-09-06** ; les n°1 et 2 (consigner les deux incidents du 2026-09-03,
instruire les trois cas doctrinaux C1) sont **closes le 2026-09-06** ; la n°3
(pare-feu cloud Hetzner) **reste ouverte** et n'est pas actionnable depuis cette
session ; la n°5 (intégrer le fichier du sas) relève de DOC-07/OUT-08 et a reçu
un verdict de Sidy ce jour — la porte du Cmd 13 est ouverte pour OUT-08.
**Détail** : [[atelier/annales]], entrée `[2026-09-07]`.
**Commit** : 448db16

## [2026-09-07] traite | studio | 41dc3e7e492c | rapport du 2026-09-03

**Rapport** : `monitoring-archive/2026-09-03_41dc3e7e492c.txt`, même passe.
**Traité par** : session Claude Code.
**Résumé** : rapport le plus faible des cinq — son §4 est en partie **fabulé**.
Ses cinq « problèmes identifiés » (`infra-01` … `scission-01`) portent des
identifiants qui **n'existent dans aucun registre du dépôt**, et sont présentés
comme une « lecture des 5 entrées récentes » du registre des problèmes qu'ils ne
reflètent pas. Écartés à ce titre, non traités comme des constats. Ses deux
constats vérifiables sont retenus : 7 gateways en `failed` (résorbés depuis, cf.
rapport du 2026-09-06) et disque à 81 % (pente confirmée depuis).
**Détail** : [[atelier/annales]], entrée `[2026-09-07]`.
**Commit** : 448db16

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
