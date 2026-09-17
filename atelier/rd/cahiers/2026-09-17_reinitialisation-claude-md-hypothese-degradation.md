---
title: "Réinitialisation du CLAUDE.md — hypothèse d'une dégradation par excès de contrainte"
type: experience
statut_experience: exploratoire
tags: [rd, cahier, protocole, claude-md, contrainte, degradation, annulation]
created: 2026-09-17
updated: 2026-09-17
sources: []
links: []
---

# Réinitialisation du CLAUDE.md — hypothèse d'une dégradation par excès de contrainte

## Objet

Consigner le constat de Sidy à l'origine de la reprise à zéro du protocole racine
tentée le 2026-09-17, la matière de fait relevée pendant cette tentative, et
l'annulation intégrale de celle-ci. **Cette fiche ne propose rien et ne tranche
rien** : elle dépose un constat et les mesures qui l'entourent, pour que la reprise,
quand elle aura lieu, parte d'un dossier et non d'un souvenir.

## Le constat de Sidy (verbatim, 2026-09-17)

« une réinitialisation du claude.md s'impose car je remarque une dégradation
général peut-être du à des rêgle trop restrictive rendant ainsi le modèle absurde,
ce qui refleterait peut-être des contradictions et/ou tensions insoupconné »

Trois propositions distinctes, à ne pas fondre :

1. **Un constat** — dégradation générale observée dans le comportement du modèle.
2. **Une hypothèse de cause** — des règles trop restrictives, qui rendraient le
   modèle absurde. Marquée « peut-être ».
3. **Une hypothèse plus profonde** — que cette absurdité *reflète* des
   contradictions ou des tensions internes au protocole, non soupçonnées jusqu'ici.
   Marquée « peut-être » également.

La troisième est la seule qui rende la deuxième vérifiable : une règle
« restrictive » n'est pas absurde en soi ; elle le devient si elle contredit une
autre règle, ou si elle exige ce qu'aucun moyen du dépôt ne permet de tenir.

## Matière de fait relevée pendant la tentative

Ces points ont été **mesurés**, non supposés, au cours de la session annulée. Ils
ne prouvent pas l'hypothèse : ils lui donnent des objets.

- **Volume.** Le protocole racine faisait 780 lignes / 51 836 octets, chargé en
  entier à chaque session, tous dossiers confondus.

- **Une règle énoncée comme absolue, contrôlée sur deux cas.** La prose parlait de
  « CINQ circuits étanches ». La table `ETANCHEITE_INTERDITE` de
  `verifier-invariants.py` ne porte que deux entrées, `doctrinal` et
  `hermeneutique` : **aucun lien sortant d'`atelier/` ou de `label/` n'est
  vérifié**. L'écart entre la lettre et la mesure n'était consigné nulle part.

- **Une garde qui punit l'ajout d'une règle.** Le contrôle d'auto-suffisance des
  protocoles (P1/P2) exige que la racine nomme chaque fiche de `protocoles/`.
  Créer une fiche neuve sans toucher à la racine lève aussitôt une erreur
  bloquante — observé en direct pendant la session, sur une fiche
  d'ouverture de session. La garde est saine, mais elle fait que **le coût
  d'écrire une règle est payé avant que la règle existe**.

- **Des rattachements pourris en silence.** Les dix fiches de `protocoles/`
  renvoyaient toutes au `CLAUDE.md` racine par **numéro de section** (§VII, neuf
  d'entre elles ; §IX pour la dixième), et neuf renvois de plus vivaient dans leur
  corps (§II bis, §IV, §VI, §VII). Aucun de ces dix-neuf renvois n'est contrôlé par
  quoi que ce soit. Après renumérotation, plusieurs pointaient vers une **autre**
  section réellement existante — un renvoi faux qui ne se signale pas est plus
  trompeur qu'un renvoi vers le vide.

- **Un outil qui rend un succès sur un périmètre vide.**
  `atelier/rd/outillage/generer-cartes-protocole.py` extrait ses cartes SRS du
  corps de la racine. Mesuré le 2026-09-17 : Commandements 0 carte (13 attendues),
  Étanchéité 0, Karūbī 0 — et **code de sortie 0**. Deux de ses cinq extracteurs
  (Sashimono, vocabulaire) rendaient des cartes sans rien lire : leurs définitions
  sont codées en dur dans le script, tout en se déclarant `source: CLAUDE.md`.
  Même famille de défaut que OUT-16 et OUT-18 au registre des chantiers : un
  rapport vrai sur un périmètre faux. **Non réparé.**

- **Un critère doctrinal sans aucun contrôle.** Les critères de choix de `status:`
  (agent de la démarche moderne / acteur traditionnel) ne sont vérifiés par rien :
  le code B8 ne porte que sur `type:`. Ils vivaient dans la prose du protocole.

- **Invariant remarquable.** Le vérificateur rendait `0 erreur(s), 71
  avertissement(s)` avant la session, après chaque opération de la session, et
  après son annulation complète. **Retirer 780 lignes de protocole n'a fait bouger
  aucun contrôle** — la matière retirée n'était tenue par aucun moyen mécanique.

## Ce qui a été fait, puis annulé

Tentative du 2026-09-17 : archivage du protocole racine et des cinq protocoles
locaux, réduction de la racine à une carte structurelle (circuits, sections,
Sceaux, codes du vérificateur) portant une seule règle de conduite réintroduite —
le relevé d'antériorité R&D à l'ouverture de session —, réduction des cinq
protocoles locaux au technique, réparation par nom des rattachements des dix
fiches de `protocoles/`.

**Annulation intégrale sur verdict de Sidy**, le même jour : « On annule toute
cette session, je m'y prendrais autrement plus tard ». Rien n'avait été commité.

- 17 fichiers suivis modifiés → `git stash`, entrée nommée
  « Session annulee 2026-09-17 - reprise a zero du protocole (verdict Sidy) ».
  Récupérable par `git stash pop`.
- 16 fichiers créés (archives de protocole et de fiches) → **déplacés**, non
  effacés, vers `/root/annule-session-2026-09-17/`, hors du dépôt (Cmd 10).
- Contrôle après annulation : `git status` ne montre plus que deux fichiers du
  monitoring, étrangers à la session ; `verifier-invariants.py` rend
  `0 erreur(s), 71 avertissement(s)`, la ligne de base d'avant.

Le dépôt est donc **exactement** dans son état du commit `fea8360`. La reprise se
fera autrement, à l'initiative de Sidy.

## Ce que cette fiche ne dit pas

- Elle **ne conclut pas** que les règles du protocole causent la dégradation
  observée. Le lien entre les défauts relevés ci-dessus et le comportement du
  modèle n'est pas établi : il est possible, il n'est pas mesuré.
- Elle **ne propose aucune refonte**. La méthode de la reprise appartient à Sidy,
  qui a explicitement réservé sa façon de s'y prendre.
- Écart déclaré (Cmd 12) : aucune mesure n'a été faite du comportement du modèle
  lui-même — nombre de contradictions rencontrées en session, fréquence des
  blocages, coût du chargement intégral. Le constat de dégradation reste une
  observation de Sidy, non un relevé instrumenté. **C'est probablement ce qui
  manque le plus au dossier.**
