---
title: "Queue de tâches — idées en attente de déploiement aux agents"
type: meta
created: 2026-08-27
updated: 2026-09-17
---

# Queue de tâches

> Dispositif validé par Sidy le 2026-08-27 — voir
> `meta/projet-unifie/propositions/proposition-queue-taches-2026-08-27.md` (fiche de
> conception, archivée). File d'attente d'idées en vrac, en attente de
> traitement par les agents Hermes concernés.
>
> Journal append-only. Une entrée par idée, jamais supprimée (Cmd 10) — le
> statut évolue en place jusqu'à `traitée`/`abandonnée`.
> Format : `## [YYYY-MM-DD] slug-idee | agent_cible | statut | priorite`
> Priorité tranchée par Sidy le 2026-08-27 (point ouvert §5 de la fiche de
> conception, résolu) : `haute | normale | basse`, obligatoire à la création
> de l'entrée.

<!-- INSERTION: QUEUE -->

## [2026-09-17] recolte-discernement-verdicts | non-assigné | en attente | normale

La **récolte du Registre du Discernement** est versée en
[[atelier/rd/cahiers/2026-09-10_recolte-discernement-etat-maturite]]. Ce n'est pas un
rapport à archiver : c'est une **liste de travail classée par maturité formelle**, et
elle n'attend qu'une chose — **des verdicts de Sidy**, que la machine ne rend jamais
(Cmd 12).

**Ce qui est mesuré, et qui donne l'urgence** : `17 traditionnel` et
`1 contre-traditionnel` sont **inchangés depuis le 2026-09-10**, alors que l'assiette
est passée de 58 à **59 fiches** dont **42 `speculatif`**. Aucun verdict de
discernement n'a été rendu en une semaine : la récolte grossit, elle ne se cueille
pas.

**Les rangs les plus mûrs, tels que la pièce les classe** — A1, le dossier
kabbalistique (quatre fiches, une séance) ; A2, le dossier Qâf du 2026-08-30 (trois
fiches, une séance) ; A3, les verdicts d'un mot. La section E ne demande **pas** un
verdict mais une **thèse** (deux fiches ouvertes sans conclusion) : ne pas la traiter
comme les autres.

**Anomalie de forme non corrigée, à trancher** (§F.2, vérifiée le 2026-09-17) :
`2026-08-20_traite-emanation-gauche-isaac-ha-kohen.md` et
`2026-08-20_etat-lieux-kabbale-depot.md` portent `type: discernement` mais **zéro**
bloc 🔍, alors qu'il est impératif. Deux issues possibles, aucune n'est mienne :
rédiger le bloc, ou changer le type.
## [2026-09-17] visa-versement-lisan-al-arab | machine | traité | normale

**Description** : le versement du *Lisān al-ʿArab* dans `raw/lisan-al-arab/` (2026-09-16, sur ordre
de Sidy — 392 Mo, 15 volumes, 8117 pages adressables, pagination conforme à l'imprimé) est
**complet, provenancé et vérifié**. Son analyse est déposée au sas :
`_inbox/2026-09-16_lisan-al-arab-edition-versee.md`, `statut: proposition au sas — non versé aux
circuits`, accompagnée de `_inbox/2026-09-16_lisan-al-arab_extraire-shamela.py`. **Elle attend le
visa de Sidy, et rien d'autre ne manque** (même forme que `BIB-03`). Tant que le visa n'est pas
donné, **rien de ce qu'elle propose ne s'applique** — un document en attente ne s'applique pas.

**Ce que le visa débloque, et qui ne doit surtout pas être engagé d'avance** :
1. l'ouverture de **`BIB-05`** — index mécanique `racine → (volume, page)`, dont le motif est que le
   *Lisān* se range **par dernière radicale** (arrangement d'al-Ṣiḥāḥ) : retrouver une racine à la
   main dans 8 200 pages est le geste coûteux, et c'est lui, non le manque de matière, qui borne le
   chantier lexical. Triptyque `intent`/`spec`/`plan` à viser **avant tout code** (Cmd 6) ;
2. le traitement des **1 520 U+200C** du champ texte — le Cmd 15 refusera le fichier tant qu'ils
   sont là, **à juste titre** ; deux voies sont proposées au sas, aucune n'est engagée ;
3. le **signalement de pagination** porté par le sas sur
   `doctrinal/symboles/formule-al-waha-al-ajal-al-saa.md` (cite le t. 15 pp. 172-173 ; le passage est
   à pp. 379-382, écart de 209 pages). Le sas subordonne la correction à la vérification des quatre
   passages **sur l'image, par Sidy lui-même** ;
4. le déplacement du script d'extraction vers `atelier/rd/outillage/`.

**À réconcilier au passage** : la pièce du sas chiffre la moisson Gloton à **97 racines** ; le TSV en
porte **169** au 2026-09-16 (passe close le jour même). Le critère de mesure de `BIB-05` — combien de
racines déjà moissonnées deviennent adressables — est donc à établir sur **169**, non 97. La pièce du
sas n'a **pas** été modifiée : elle attend visa.

**CLÔTURE DU 2026-09-17 — visa rendu, entrée traitée.** Sidy a visé le versement le
2026-09-17. Les quatre points ci-dessus sont réglés ainsi : **(1)** `BIB-05` est
**ouverte au registre en recensement seul** — aucun code, triptyque à rédiger et à
viser ; **(2)** les 1 520 U+200C sont **laissés en place**, aucune des deux voies
n'est engagée, la conversion vers `textes/` n'étant pas ouverte ; **(3)** la
correction de pagination est **faite** (t. 15 pp. 379-382) et le `to-source` du seul
article وحي levé — les deux autres marqueurs de la fiche subsistent, ils ne relèvent
pas du *Lisān* ; **(4)** le script est versé en
`atelier/rd/outillage/extraire-lisan-shamela.py`. S'y ajoute la fiche
[[doctrinal/sources/lisan-al-arab]], `status: traditionnel` **sur verdict exprès de
Sidy du 2026-09-17** — la machine ne l'a pas déduit. La réconciliation 97/169 est
tranchée au profit de **169** (mesure au TSV), et inscrite comme telle à `BIB-05`.
Le sas `_inbox/` a été vidé après intégration (§II, pas 8) : le signalement de
conservation porté par cette entrée est **éteint**, la matière étant désormais dans
les circuits.

**Point de vigilance sur la conservation** : la pièce est bien **suivie par git** (vérifié :
`git ls-files _inbox/` la liste, elle n'est pas ignorée), mais `_inbox/` est par définition **vidé
après chaque intégration** (§II du protocole racine). Si le sas est vidé avant que le visa soit donné,
l'analyse ne subsistera que dans l'historique — et la procédure de reprise de
`atelier/rd/bibliotheque/2026-09-16_trois-organes-lexicaux-et-lisan-al-arab.md` (§7), qui la désigne
comme sa première étape, perdrait sa cible en clone frais. **Rien n'est déplacé d'office** : c'est un
signalement, le geste appartient au verdict (Cmd 12).

**Contexte** : fiche `atelier/rd/bibliotheque/2026-09-16_trois-organes-lexicaux-et-lisan-al-arab.md`,
§4 ; annales de l'atelier, entrée `[2026-09-16] consignation` (commit `4852e98`).
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** :

## [2026-09-16] statut-glossaire-unifie | non-assigné | en attente | normale

**Description** : trancher le statut de `atelier/rd/bibliotheque/glossaire-unifie.md`. Mesuré le
2026-09-16 : **33 lignes, ZÉRO terme** — l'inscription contraire du registre (BIB-04, « 1850 termes »)
a été corrigée au titre du Cmd 10. La question n'est pas d'entretien mais de nature : un glossaire
porte **le sens et son attribution** (« selon qui »), un index ne porte que **l'adresse** ; un agrégat
d'adresses ne peut donc pas être un glossaire. Le glossaire réel du vocabulaire technique est **déjà
un livre transcrit au dépôt** — al-Jurjānī, *Le Livre des Définitions* (trad. Gloton), **220
définitions, 0010 à 1864** (catalogue, ligne 85). Verdict attendu : le fichier est-il déclaré
`caduc` ? Rien n'est régénéré ni édité entre-temps (artefact dérivé).
**Contexte** : fiche `atelier/rd/bibliotheque/2026-09-16_trois-organes-lexicaux-et-lisan-al-arab.md`, §3 et §6.1.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** :

## [2026-09-16] perimetre-generateur-validateur-index | non-assigné | en attente | basse

**Description** : `generer-glossaire-unifie.py` sélectionne les fiches sur le **préfixe de nom de
fichier** (`index-`) quand `valider-index-livres.py` borne au **champ** `type: index-livre`. Mesuré :
des 6 fiches `index-*.md`, **5 portent `type: ressource`**, une seule (`index-origine-polaire-tilak.md`)
porte `type: index-livre`. Les deux instruments ne désignent donc pas le même ensemble, et toute
mesure prise sur l'un est à lire avec cette réserve. Aligner sur le **champ** (et non sur le nom)
paraît le sens juste, mais c'est un verdict, non un constat.
**Contexte** : même fiche, §3 et §6.2. Subordonné à l'entrée `statut-glossaire-unifie` : si le
glossaire est déclaré caduc, la moitié de la divergence tombe d'elle-même.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : basse
**Statut** : en attente
**Résultat / lien** :

## [2026-09-16] recomptage-tableau-registre | non-assigné | en attente | basse

**Description** : le tableau de synthèse de `atelier/rd/registre-chantiers.md` (§0) ne se réconcilie
pas pour les pôles **DOC**, **OUT** et **INF**. Réserve Cmd 5 déjà inscrite au registre. **Ces trois
pôles n'ont pas été touchés** par les passes récentes : la cause relevée est formelle — les tableaux
concernés ne portent pas le même nombre de colonnes, de sorte qu'un comptage mécanique uniforme les
lit mal. Recompter et, le cas échéant, uniformiser les colonnes.

**Ajout du 2026-09-17 (Cmd 10) — un cinquième statut sans colonne.** Le tableau
par pôle ne porte **que quatre colonnes de statut** (`ouvert`, `en-cours`,
`bloque`, `attente-verdict`). Or `BIB-05`, ouvert le 2026-09-16, porte
**`recense`** : il n'est donc **compté dans aucune colonne**, et la ligne `BIB`
reste inexacte d'une unité même après la clôture de `BIB-03` ce jour. La machine
n'ajoute pas la colonne : la **forme** du tableau relève du verdict (Cmd 12), et
c'est l'objet même de cette entrée.

**Rectification du même jour, seconde passe : le défaut est plus grave que « pas de
colonne ».** Vérification faite au § *Comment lire ce registre*, le vocabulaire
déclaré des statuts n'admet que **quatre** valeurs — `ouvert`, `en-cours`, `bloque`,
`attente-verdict`. `recense` **n'y figure pas**. `BIB-05` porte donc une **valeur hors
vocabulaire**, exactement la classe d'écart relevée sur `DOC-06`/`DOC-07`/`DOC-08` et
close le 2026-09-13 — et celui-ci est de mon fait (`dfae737`). Deux issues à trancher,
comme alors : soit le vocabulaire **s'élargit** à `recense` (et le tableau gagne une
colonne), soit `BIB-05` est **ramené à une valeur déclarée**. La machine ne choisit
pas ; `BIB-05` reste tel quel jusqu'au verdict.

**VERDICT DU 2026-09-17 — ce point est clos.** Sidy tranche : « ramène `BIB-05` à
`ouvert`, le statut `recense` n'existe pas ». Des deux issues, c'est la **seconde** :
le vocabulaire **ne s'élargit pas**, il reste à quatre valeurs, et la valeur fautive
est ramenée à une valeur déclarée. Appliqué le jour même — `BIB-05` porte `ouvert`,
contenu inchangé ; plus aucune ligne du registre ne porte `recense` (vérifié : 0
occurrence). Le tableau par pôle **n'a pas besoin de colonne nouvelle** : `BIB` passe
à `ouvert` 2, total 4, et redevient **exact** ; le total général à `ouvert` 33, 57.

**Ce qui reste en attente sous cette entrée**, et elle n'est donc pas close : l'écart
global de recomptage. Après clôture de `BIB-03` et application du verdict,
**62 lignes** réelles en §1–§7 contre **60** déclarées ; `BIB`, `INS`, `CAS` et `PRO`
tombent juste, **`INF`, `OUT` et `DOC` divergent** — soit exactement les trois pôles
nommés au premier paragraphe de cette entrée.
Recomptage mécanique du 2026-09-17 après clôture de `BIB-03` : **62 lignes** en
§1–§7 contre **60** déclarées ; `INS`, `CAS` et `PRO` tombent juste, `INF`,
`OUT`, `BIB` et `DOC` divergent.
**Contexte** : même fiche, §6.3.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : basse
**Statut** : en attente
**Résultat / lien** :


## [2026-09-15] reexamen-rubrique-erudition-academique | non-assigné | en attente | normale

**Description** : réexaminer au critère du type `reference` (adopté le 2026-09-15) les sept fiches
de la rubrique « Érudition académique » du Catalogue doctrinal — Ali Hussain, R. Raphael Afilalo,
Yaqub Chaudhary, Aiman Attar, Titus Burckhardt, Faraz Rabbani, Hamza Yusuf : autorité, ou
référence ? Rien à déplacer d'office ; verdict de Sidy fiche par fiche (Cmd 12).
**Contexte** : proposition `meta/projet-unifie/propositions/proposition-type-reference-2026-09-15.md`,
question 4 — « Plus tard, ajoute à Queue-idée » (Sidy, 2026-09-15). Relevé à trancher au passage :
la fiche Yaqub Chaudhary, rangée sous « Érudition académique », porte `status: traditionnel`.
**Agent(s) concerné(s)** : `non-assigné`
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** :

## Gabarit d'entrée (à copier pour chaque nouvelle idée)

```markdown
## [YYYY-MM-DD] slug-idee | agent_cible | statut | priorite

**Description** : formulation de l'idée, aussi brute que nécessaire.
**Contexte** : d'où vient l'idée (conversation, observation, besoin repéré).
**Agent(s) concerné(s)** : un ou plusieurs slugs parmi les 12 rôles
  (`01-ar-music-artistic-direction`, ..., `12-commerce-profitability`,
  `13-librarian-archivist`), ou `non-assigné` si le tri reste à faire.
**Priorité** : haute | normale | basse
**Statut** : en attente | assignée | en cours | traitée | abandonnée
**Traité le** : YYYY-MM-DD (rempli à la clôture)
**Résultat / lien** : fiche produite, décision prise, ou motif d'abandon.
```

Règles de gouvernance (rappel, cf. fiche de conception §4) :
- Seule Sidy, ou une session Claude Code sous plan validé, ajoute de
  **nouvelles** entrées.
- Les agents ne modifient que `statut`, `Traité le` et `Résultat / lien` des
  entrées qui leur sont assignées — jamais `Description`/`Contexte`/`Priorité`
  d'origine.
- Passage à `traitée` réservé à Sidy pour tout ce qui engage (Cmd 13) ; les
  agents ont autorité de clôture directe uniquement pour une tâche
  non-engageante de recherche/rédaction, motivée dans `Résultat`.

## [2026-09-02] etendre-archive-rapports-publication | non-assigné | en attente | haute

**Description** : étendre `atelier/rd/infrastructure/monitoring-archive-charte.md`
au job Publication `veille-referencement-investigation-08` (profil
`publication`), sur le modèle exact de l'archivage déjà en place pour Studio
(`archiver-monitoring-quotidien.py`, cron dédié `10 12 * * *`) — copier ce que
Hermes persiste déjà sur disque
(`/root/.hermes/profiles/publication/cron/output/`) vers un dossier
équivalent, avec la même rétention de 40 jours.
**Contexte** : session d'INTÉGRATION du 2026-09-02. Sidy a dû coller
lui-même deux rapports Publication dans la conversation, faute d'archive
mécanique — geste qu'il ne devrait pas avoir à refaire. Consigné `INF-15`
dans `atelier/rd/registre-chantiers.md`. Nécessite un accès au serveur Hermes
(création de job cron) : hors de portée d'une session Claude Code distante
comme celle qui consigne cette idée.
**Agent(s) concerné(s)** : non-assigné (accès serveur requis — Sidy ou
session avec terminal Hermes).
**Priorité** : haute
**Statut** : en attente
**Traité le** :
**Résultat / lien** : `atelier/rd/registre-chantiers.md`, ligne `INF-15` ;
`atelier/rd/infrastructure/monitoring-archive-charte.md`.

## [2026-09-02] verifier-redemarrer-gateways-hermes-en-echec | non-assigné | en attente | normale

**Description** : vérifier si les six services `hermes-gateway-*` constatés
en échec dans chaque rapport Studio du 2026-08-28 au 31 (`accounting`,
`admin-legal`, `distribution`, `marketing`, `production`, `visual-da`) sont
censés tourner ou sont dormants par construction (les 9 profils métier étaient
volontairement laissés sur Qwen en attente de reset de quota, cf.
`atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen.md`,
§Hors périmètre) ; le cas échéant, redémarrer via
`systemctl --user restart hermes-gateway-<profil>.service`. Inclut, dans le
même geste, le socket Discord Gardien resté fermé depuis le 2026-08-25
(`registre-problemes.md`, entrée `[2026-08-25]` — bloqué par le filtre de
sécurité Hermes qui refuse tout restart émis depuis un terminal enfant d'un
gateway, requiert un shell extérieur, SSH ou terminal local).
**Contexte** : signalé de façon répétée dans les rapports Studio archivés,
jamais actionné. Nécessite un accès `systemctl`/SSH au serveur : hors de
portée de cette session distante (dépôt git seul).
**Agent(s) concerné(s)** : non-assigné (accès serveur requis).
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** : `atelier/rd/cahiers/registre-problemes.md`, entrées
`[2026-09-02]` et `[2026-08-25]` (« Discord Gateway Gardien »).

## [2026-09-02] verification-humaine-sources-raw-trois-fiches | 08-publication-site | en attente | normale

**Description** : vérifier sur le serveur (`raw/` y est présent, exclu de
git) la présence effective de `Awrad_Ibn_Arabi.pdf`,
`Jesus_And_Enoch_In_Ibn_'arabi.pdf` et `shams-al-maarif-traduit-complet.pdf`,
puis — condition posée par le protocole (§VII racine, discipline des sources,
point 2), non par cette entrée — vérification du **texte primaire** par Sidy
lui-même avant toute levée de `to-source` : `doctrinal/sources/awrad-ibn-arabi.md`,
`doctrinal/sources/jesus-and-enoch-in-ibn-arabi.md`,
`doctrinal/sources/shams-al-maarif.md` (`sources: [], sources_count: 0`
actuellement sur les trois).
**Contexte** : recommandation du rapport Publication du 2026-08-31 (§2,
investigation documentaire), traitée en session le 2026-09-02 mais non
actionnable : `raw/` est intégralement exclu de git, une session distante ne
peut ni confirmer ni infirmer la présence des PDF, et la levée du
`to-source` reste de toute façon un geste humain exclusif.
**Agent(s) concerné(s)** : 08-publication-site (constat de présence) ;
levée du `to-source` réservée à Sidy (Cmd 5, non délégable).
**Priorité** : normale
**Statut** : en attente
**Traité le** :
**Résultat / lien** : `atelier/rd/cahiers/registre-problemes.md`, entrée
`[2026-09-02]` « Deux rapports Publication collés par Sidy depuis Discord »,
point 3.
