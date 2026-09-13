---
title: "Suite des points ouverts du rapport Studio — exécution du 2026-09-13 (seconde passe)"
type: infrastructure
tags: [rd, infrastructure, monitoring, hermes, correctifs, registre, sas]
created: 2026-09-13
updated: 2026-09-13
sources: []
links:
  - "[[atelier/rd/infrastructure/2026-09-13_correctifs-rapports-studio]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
  - "[[atelier/rd/cahiers/journal-optimisations]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/infrastructure/monitoring-archive-charte]]"
original: []
infra_verif:
  - profil: studio
    cron_job: monitoring-infrastructure-quotidien
  - profil: studio
    discord_home_channel: "1536564394690084925"
---

# Suite des points ouverts du rapport Studio — exécution du 2026-09-13 (seconde passe)

## 1. Motif et cadre

**Consigne de Sidy, `#infrastructure`, 2026-09-13** : « Oui vas-y », en réponse au
rapport de clôture de la passe du matin, qui laissait **sept points** ouverts
(§10 de [[atelier/rd/infrastructure/2026-09-13_correctifs-rapports-studio]]).

Ce « oui » n'était pas assez précis pour être exécuté tel quel — sept points, dont
plusieurs à deux branches. Il a donc été **mis en forme et soumis par formulaire**,
point par point, et les réponses de Sidy sont consignées au §2 **telles quelles**.
C'est la boucle Discord-Validation ordinaire : suggérer → valider → exécuter.

**Pourquoi cette fiche existe.** La règle de validation de Sidy est
**conditionnelle** : son accord sur un lot vaut à condition que la documentation
soit **en place avant l'exécution**. Cette fiche est le **contrat** entre la
session Hermes qui exécute et la revue Claude Code qui auditera après coup. Elle
est **écrite et commitée avant la première écriture d'exécution** — c'est l'objet
de son premier commit.

**Ce que cette passe n'est pas.** Aucun geste n'est ajouté « au passage » : les six
gestes exécutés sont ceux du lot validé, ni plus ni moins. Ce qui n'est pas exécuté
l'est pour un motif nommé (§4), jamais par omission.

**Une écriture hors dépôt.** Cinq des six gestes vivent au dépôt ; le sixième
(N5) est une édition du **prompt du job cron** `monitoring-infrastructure-quotidien`,
qui vit dans `~/.hermes/profiles/studio/cron/jobs.json`, donc **hors du dépôt**.
Le texte d'avant est reproduit au §8, sa restauration est une édition de champ.

## 2. Le lot validé — les réponses de Sidy, verbatim

Question posée : *« Lot des 5 points arbitrables : qu'est-ce que j'exécute ? »*

> **Réponse 1** : « Oui — applique mes recommandations (N5, INF-09, N2, N3,
> vocabulaire), fiche-contrat d'abord »

Question posée : *« N1 — ta réponse "Toi directement" me laisse un doute : qui écrit
concrètement l'entrée au registre des problèmes ? »*

> **Réponse 2** : « Moi (agent Hermes) : tu lèves l'interdiction de mandat pour
> cette entrée, et je la dépose en déclarant l'écart »

Question posée : *« N4 — les deux fiches du sas (dont une à 5 jours) : veux-tu que
je prépare le plan d'intégration (Cmd 6) ? »*

> **Réponse 3** : « Non — le sas reste en attente pour l'instant »

| Code | Geste validé | Portée | Nature |
|---|---|---|---|
| **N1** | Déposer l'entrée préparée au `registre-problemes.md` | dépôt — cahier append-only | **écart déclaré** (§4) : interdiction de mandat levée nominativement |
| **N5** | Réintroduire `verifier-invariants.py` au §1 du rapport Studio | **hors dépôt** — prompt du job cron | édition de champ, texte d'avant conservé (§8) |
| **INF-09** | Requalifier le statut `ouvert` → `attente-verdict` | dépôt — `registre-chantiers.md` §2 | alignement du statut sur son propre texte |
| **N2** | Ouvrir `INF-17` (migration de provider), statut `clos`, versée en §9 | dépôt — `registre-chantiers.md` §9 | inscription d'un fait daté |
| **N3** | Le sas `_inbox/` et Git : reconnaître la pratique, et la borner | dépôt — fiche §6 (+ texte prêt §5.2) | **règle amendée là où l'agent peut écrire** ; l'entrée du registre des problèmes est *signalée*, non écrite (hors du périmètre levé) |
| **vocabulaire** | Aligner les trois statuts `DOC` hors vocabulaire | dépôt — `registre-chantiers.md` §7 + §0 | alignement sur le vocabulaire **déclaré**, sans l'élargir |
| **N4** | *non exécuté* | — | refus explicite de Sidy : le sas reste en attente |

## 3. Ce que chaque geste change, exactement

### N1 — l'entrée au registre des problèmes

Le rapport du 2026-09-13 (§3.4, §4.3 piste 1, §5.3) a mesuré un **défaut de
preuve** : l'entrée `[2026-09-11]` du `journal-optimisations.md` déclarait les
`Connection error` de **trois** jobs cron résolues **au nom des trois**, sur la foi
d'un **seul** run réussi (profil `gardien`). Le fait est vrai — le rapport a
mesuré que le job Studio porte bien le pin attendu — mais la preuve ne le portait
pas. C'est la première **instance datée sur le rapport lui-même** d'un motif que
§VII (*Épreuve des contrôles*) et l'entrée `[2026-09-04]` du registre disent déjà.

Le texte déposé est celui qui était **prêt au §5** de la fiche précédente,
complété de deux champs que le format déclaré du registre exige
(**Compréhension tirée**, **Statut**) et qui manquaient au brouillon. Le texte
exact est reproduit au §5.1 ci-dessous, **verbatim**, tel qu'inséré.

### N5 — le contrôle structurel revient au §1 du rapport Studio

Retiré le 2026-08-24 au profit du job `veille-frontmatter-quotidien` du profil
`publication` (11:00 UTC), `verifier-invariants.py` ne tournait plus dans le
rapport Studio. Conséquence mesurée le matin même : le contrôle A **étendu aux
cahiers append-only** (correctif C3) mord désormais dans le rapport
**Publication**, pas dans celui du pôle qui *propose les correctifs*.

Le geste rétablit le script en tête du §1 et renumérote les étapes. **Redondance
assumée et déclarée** : le script tournera dans deux rapports quotidiens (Studio
12:00, Publication 11:00). Le motif du choix : le rapport du pôle Studio ne doit
pas dépendre de la santé d'un autre profil pour porter son propre contrôle
structurel — c'est le même principe d'autonomie que la règle 2 de §VIII
(fiabilité d'action ≠ fiabilité narrative : un contrôle se cite, il ne se
suppose pas exécuté ailleurs).

### INF-09 — `ouvert` → `attente-verdict`

La ligne porte, dans sa propre colonne *Prochaine action* : « verdict
`attente-verdict` **rendu** : pause, pas de hook pour l'instant », et dans son
texte : « cycle mis en pause par Sidy (2026-09-01, dit en session) ». Le
vocabulaire déclaré du registre définit `attente-verdict` comme « rien ne manque
sauf la décision de Sidy » : c'est exactement l'état de cette ligne. La
requalification **n'est pas un recompte** mais un alignement du statut sur le
texte que la ligne porte déjà — et c'est Sidy qui l'a validé (Cmd 12/13 respectés).

### N2 — `INF-17`, ouverte et close, versée en §9

`journal-optimisations.md` `[2026-09-11]` documente une migration de fournisseur
d'inférence effective ; aucune ligne de chantier ne la portait. Le rapport
proposait deux branches (ouvrir la ligne, **ou** acter qu'une optimisation
n'appelle pas de ligne) et les laissait au verdict de Sidy.

Le verdict rendu : **ouvrir la ligne, statut `clos`, versée en §9 avec sa date**.
Motif : la migration a produit **trois jours de panne du rapport Studio** — ce
n'est pas une optimisation ordinaire, et un fait d'infrastructure de cette portée
ne reste pas sans identifiant greppable. Le registre garde la trace **sans feindre
un chantier ouvert** : c'est la discipline qu'il s'est donnée lui-même (« un
chantier clos n'est jamais supprimé : il garde son ID et descend en §9 avec sa
date »). La ligne est **confrontée au disque et à `git log`** avant inscription,
comme le registre l'exige.

### N3 — le sas `_inbox/` et Git : la pratique reconnue, et bornée

**Le fait mesuré** (rapport §3.3, fiche précédente §3) : deux fiches candidates
du sas sont **suivies par git** — situation que l'entrée `[2026-08-09]` du
registre des problèmes consignait comme un **incident**, et dont la leçon tirée
portait : « Le sas est intouchable par Git tant que l'intégration n'est pas
faite. » Or `git log` établit une **pratique délibérée** — au moins quatre
sessions depuis le 2026-08-28 (`INBOX:`, `SAS:`, `Fiche _inbox/ :`) — et
`_inbox/.gitkeep` déclare lui-même son suivi **par dessein** depuis le
2026-08-31 (le retrait des dernières fiches avait emporté le répertoire et ses
ACL, celles des profils `mehdi` et `wendel`, reposées à la main).

**La coupe retenue** (§6 ci-dessous) : la faute de l'incident de l'été est
`git add -A` **à la racine**, qui ramasse tout — y compris une pièce nominative
(`karubi-mehdi.md`, `image.jpeg` dans l'incident) ; elle n'est pas « le sas
versionné ». Le régime amendé distingue donc **le ramassage aveugle**, qui reste
interdit, et **le commit nominatif d'une fiche candidate**, qui est la pratique
constante du dépôt.

**Limite de la levée, respectée à la lettre.** La levée consentie par Sidy porte
sur « **cette entrée** » — celle de N1. L'énoncé amendé du régime est donc écrit
**là où cette passe peut écrire** (fiche §6) ; l'entrée que le registre des
problèmes devrait recevoir pour que la doctrine cesse de se contredire est
**préparée au §5.2** et **signalée au §10**, pour son dépositaire. Le geste n'est
pas fait à moitié : il est fait **jusqu'où la permission va**, et le reste est
nommé.

### Vocabulaire — trois statuts hors vocabulaire ramenés au vocabulaire déclaré

La note de recomptage du 2026-09-07 (§0 du registre) avait laissé le point
explicitement soumis à Sidy, entre deux branches : **élargir** le vocabulaire
déclaré (`fait`, `partiel`, `recensé` deviennent déclarés), ou **ramener** ces
trois lignes au vocabulaire existant.

Verdict rendu : **ramener**. Motifs : (1) les six valeurs déclarées
(`ouvert` · `en-cours` · `bloque` · `attente-verdict` · `clos` · `caduc`) décrivent
la **position d'un chantier**, tandis que `fait` / `partiel` / `recensé` décrivent
l'**état d'un ingest** — deux axes différents, et mêler les deux dans une même
colonne serait de l'accumulation, pas de la précision ; (2) l'élargissement d'un
vocabulaire est une **réforme**, quand la maison pratique la **restauration**
(Cmd 11) ; (3) les trois lignes portent déjà, dans leur texte, de quoi choisir :

| Ligne | Statut | Devient | Motif lu dans la ligne elle-même |
|---|---|---|---|
| `DOC-06` | `fait` | `en-cours` | ingest fait le 2026-09-02 (5 fiches) **et rouvert le même jour** pour une 6ᵉ fiche sur le chapitre XIII |
| `DOC-07` | `partiel` | `en-cours` | Osman Yahia versé ; la Futūḥāt est **renvoyée à OUT-08** (nouvel essai d'OCR) |
| `DOC-08` | `recensé` | `attente-verdict` | matière réservée par Sidy, retour différé ; **prochaine action proposée, en attente de visa** |

**Conséquence mécanique, recomptée et non estimée** : plus aucune valeur hors
vocabulaire ; le §0 du registre est recompté depuis ses lignes, et ses totaux
bougent en colonnes (voir §3 bis ci-dessous) **sans que le nombre de lignes
change** (56 avant, 56 après).

### 3 bis. Le §0 du registre, recompté ligne à ligne

| Pôle | ouvert | en-cours | bloqué | attente-verdict | total | Mouvement |
|---|---|---|---|---|---|---|
| `INS` | 9 | 2 | 1 | 3 | 15 | — |
| `INF` | **7** | 3 | 1 | **3** | 14 | `INF-09` : ouvert → attente-verdict |
| `OUT` | 7 | — | 1 | — | 8 | — |
| `BIB` | 1 | — | 1 | 1 | 3 | — |
| `CAS` | 1 | — | 1 | — | 2 | — |
| `PRO` | 3 | — | — | 3 | 6 | — |
| `DOC` | 4 | **2** | — | **2** | **8** | trois statuts alignés (2 `en-cours`, 1 `attente-verdict`) |
| **Total** | **32** | **7** | **5** | **12** | **56** | 33/5/5/10 +3 hors vocabulaire → 32/7/5/12, plus rien hors vocabulaire |

Le total des quatre colonnes passe donc de **53** (faux par construction : il
laissait trois lignes dehors) à **56**, qui est le nombre réel de lignes — et le
nombre de lignes, lui, ne bouge pas. `INF-17` va en **§9**, qui comptait 7 lignes
et en compte **8**.

## 4. Écarts déclarés — jamais silencieux

> **⚠ Écart 1 (N1) — écriture d'un agent de veille au `registre-problemes.md`.**
> Le mandat `infrastructure-veille` porte : « *pas d'écriture directe à
> `atelier/rd/cahiers/registre-problemes.md`* — le rapport Discord est le signal,
> Sidy ou une session INTEGRATION consigne ». **Sidy a levé nominativement cette
> interdiction pour cette entrée**, par réponse explicite à une question qui
> nommait la levée et sa conséquence (« tu lèves l'interdiction de mandat pour
> cette entrée, et je la dépose en déclarant l'écart »).
> Trois précautions : (a) la levée est **scopée à cette entrée** — la seconde
> entrée, celle du §5.2, n'est **pas** déposée ; (b) l'écart est déclaré **ici**,
> **dans la fiche**, et **dans l'entrée elle-même** (dernier champ) ; (c) la
> réversibilité est totale — `git revert` d'un seul commit suffit.
> **Précédent du même jour** : la passe du matin a écrit quatre entrées au
> `registre-traitement.md` sous la même lecture (consigne explicite ouvrant la
> porte que la clause fermait), avec la même déclaration d'écart.

> **⚠ Écart 2 (N5) — modification hors dépôt.** Le prompt du job
> `monitoring-infrastructure-quotidien` ne vit pas au dépôt ; l'édition est faite
> par la CLI Hermes (`hermes cron edit`), jamais par réécriture directe du fichier
> `jobs.json`. Vérification exigée : **relecture du prompt persisté** après
> édition, et **exécution réelle** de la commande ajoutée — jamais la seule foi
> d'un `last_status: ok` (§VIII.2).

## 5. Textes

### 5.1 N1 — l'entrée déposée au `registre-problemes.md`

*Reproduite mot pour mot telle qu'insérée en tête du cahier, après le marqueur
`<!-- INSERTION: EN-TÊTE -->`.*

```markdown
## [2026-09-13] Une résolution déclarée au nom de trois jobs, prouvée sur un seul

- **Symptôme** : l'entrée `[2026-09-11]` du `journal-optimisations.md` déclarait
  les `Connection error` des trois jobs cron résolues **au nom des trois**, sur la
  foi d'un seul run réussi (celui du profil `gardien`). Le rapport Studio du
  2026-09-13 a mesuré que le job Studio portait bien le pin attendu
  (`model = deepseek-flash`, `provider = deepseek`, `reasoning_effort = high`,
  `failure_streak = 0`, deux exécutions réussies les 09-12 et 09-13) — **le fait
  est vrai, la preuve ne le portait pas**.
- **Diagnostic** : défaut de *preuve*, non de configuration. Même classe que
  l'entrée `[2026-09-04]` (« un contrôle vert n'attestait pas que les liens du
  cartouche aboutissent ») et que §VII, *Épreuve des contrôles* — instance datée
  sur le rapport lui-même.
- **Résolution** : (à trancher) — soit relecture des `jobs.json` des trois profils
  avec citation brute, soit entrée de correction au `journal-optimisations.md`.
- **Compréhension tirée** : une optimisation déclarée au nom de N jobs doit citer
  N preuves ; une preuve unique portée au nom de plusieurs objets n'est pas une
  preuve faible, c'est une preuve absente. Le registre des optimisations hérite de
  §VII comme les autres : ce dont on n'a pas vu l'échec n'est pas réputé tenir.
- **Liens** : `journal-optimisations.md` `[2026-09-11]` ; rapport Studio du
  2026-09-13 §3.4 ; [[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]].
- **Statut** : `ouvert`

- **Déposé par** : session Hermes `studio` (mandat `infrastructure-veille`), sur
  consigne explicite de Sidy du 2026-09-13 **levant nominativement l'interdiction
  de mandat pour cette entrée** — écart déclaré au §4 de la fiche de passe.
```

### 5.2 N3 — l'entrée préparée, **non déposée**

*La levée de Sidy porte sur l'entrée de N1 (« cette entrée ») : celle-ci est
préparée, signalée, et attend son dépositaire. Motif : le principe d'une
permission scopée se respecte à la lettre, même quand la tentation est d'aller
plus vite.*

```markdown
## [2026-09-13] Le sas `_inbox/` et Git — une doctrine et une pratique qui se contredisaient

- **Symptôme** : l'entrée `[2026-08-09]` porte, comme compréhension tirée : « Le
  sas est intouchable par Git tant que l'intégration n'est pas faite. » Or deux
  fiches candidates du sas sont **suivies par git**, et `git log` établit une
  pratique délibérée d'au moins quatre sessions depuis le 2026-08-28.
- **Diagnostic** : la doctrine a été écrite sur un incident précis — un
  `git add -A` **à la racine** ramassant `_inbox/karubi-mehdi.md` (pièce
  nominative) et `_inbox/image.jpeg` —, et généralisée en règle sur le sas
  entier. La règle a débordé son fait. À l'inverse, le suivi de `_inbox/.gitkeep`
  est **voulu** depuis le 2026-08-31 (le retrait des fiches avait emporté le
  répertoire et les ACL des profils `mehdi` et `wendel`).
- **Résolution** : régime amendé — le **ramassage aveugle** du sas (commandes
  larges à la racine) reste interdit ; le **commit nominatif** d'une fiche
  candidate par la session qui la dépose est reconnu comme pratique normale,
  sous réserve que la pièce soit mesurée (pas de pièce nominative). Énoncé
  complet au §6 de la fiche de passe.
- **Compréhension tirée** : une leçon tirée d'un incident doit nommer son
  périmètre — sinon elle interdit plus qu'elle n'a vu, et le dépôt se met
  silencieusement en infraction avec sa propre règle.
- **Liens** : entrée `[2026-08-09]` ; rapport Studio du 2026-09-13 §3.3 ;
  `_inbox/.gitkeep` ; [[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]].
- **Statut** : `ouvert`
```

## 6. Régime du sas `_inbox/` par rapport à Git — énoncé amendé (N3)

**Ce qui est interdit, et le reste.** Aucun commit de masse à la racine
(`git add -A`, `git add .`) : le sas est un lieu de **dépôt brut**, où une pièce
peut être nominative le temps d'une intégration. C'est cette faute — et elle
seule — que l'incident de l'été a établie.

**Ce qui est reconnu.** (1) `_inbox/.gitkeep` **est suivi par dessein** : un sas
vide n'est pas un sas absent, et sa disparition emporte les ACL des profils qui y
déposent. (2) Une **fiche candidate** — un `.md` mesuré, sans donnée personnelle —
peut être commitée **nominativement**, par un `git add <chemin exact>`, par la
session qui la dépose ou la déplace. C'est la pratique constante du dépôt depuis
le 2026-08-28, non une récidive.

**Ce que le régime n'autorise pas.** Commiter une pièce **nominative** (transmission
Karūbī, image, facture) qui aurait atterri au sas : la ligne de coupe reste celle
de `raw/` — le format, non le contenu. Une telle pièce se retire par
`git rm --cached` nommément, jamais par réécriture d'historique (l'historique du
remote conserve le blob ; dépôt privé).

## 7. Réversibilité

| Geste | Réversible par |
|---|---|
| N1 (entrée au registre des problèmes) | `git revert` d'un commit — l'entrée s'ajoute, rien n'est réécrit (Cmd 10) |
| INF-09, N2, vocabulaire (`registre-chantiers.md`) | `git revert` ; registre **révisable en place**, l'historique est dans git |
| N3 (énoncé du régime) | `git revert` |
| **N5** (prompt du job, **hors dépôt**) | édition de champ par `hermes cron edit` ; **texte d'avant reproduit au §8** |

Aucune suppression sèche, aucun renommage, aucune passe de masse (Cmd 10).

## 8. Annexe — prompt du job `monitoring-infrastructure-quotidien`

### 8.1 Avant (2537 caractères, persisté avant correction)

```
Rapport quotidien du pôle Studio (profil studio, canal #infrastructure). Depuis /root/wiki, exécute dans l'ordre et cite la sortie brute de chaque script (jamais un résumé) :

## §1 — Cartographie et cohérence structurelle

1. python3 atelier/rd/outillage/graphe/generer-cartographie.py --depot /root/wiki --verifier
2. python3 atelier/rd/outillage/detecter-non-tracke.py --racine /root/wiki
3. python3 atelier/rd/outillage/verifier-coherence-infrastructure.py --racine /root/wiki

(§1 était autrefois ouvert par verifier-invariants.py — retiré 2026-08-24, repris par le job veille-frontmatter-quotidien du profil publication, 11:00 UTC.)

## §2 — Empreinte serveur

4. df -h /, free -h

## §3 — Registre Hermes-Terminal

5. Intégrité des bind-mounts, santé des gateways — relevé par `systemctl --user list-unit-files 'hermes-*'` d'abord (13 unités pour 14 profils ; `list-units` seul ne montre que les unités chargées, leçon de l'entrée [2026-09-01] du registre des problèmes) puis `is-active`/`is-enabled` par profil —, staleness de _inbox/

## §4 — Volet R&D (prioritaire, non conditionnel)

6. ./atelier/rd/outillage/detecter-nouvelles-fiches-rd.sh
7. Lire TOUTES les fiches R&D nouvelles (pas de seuil « aucune-nouvelle-fiche » qui saute la section). Pour chaque fiche :
   a. La lire en entier.
   b. La rapprocher de atelier/rd/cahiers/registre-problemes.md : une entrée existante couvre-t-elle ce problème, ou est-ce un problème nouveau ?
   c. Formuler une PROPOSITION d'action concrète (jamais une décision).
   d. Identifier les dépendances entre fiches R&D : quelle fiche nourrit quelle autre, quel angle mort reste ouvert.
   e. Si la fiche implique un autre agent (Studio, Gardien, Publication, etc.), le nommer et proposer un handoff explicite.
8. Relire les 5 entrées les plus récentes de registre-problemes.md. Pour chacune : l'état a-t-il changé depuis la dernière exécution ? Une proposition antérieure a-t-elle été appliquée, rejetée, ou est-elle stagnante ?
9. Synthèse R&D : 3 à 5 pistes prioritaires pour la prochaine session, classées par urgence et faisabilité. Marquer chaque piste PROPOSITION.

## Format du rapport

§1 Cartographie et cohérence (sorties brutes des scripts 1-3)
§2 Empreinte serveur
§3 Registre Hermes-Terminal
§4 R&D — analyse engagée (fiches nouvelles, registre-problemes, pistes prioritaires)
§5 Suggestions transversales

Contrôle anti-fabulation : ne jamais reformuler la sortie des scripts, la coller telle quelle. Étape 3 est le même contrôle (registre-problemes.md, entrée 2026-08-17).
```

### 8.2 Après (le texte qui sera persisté, à confronter à la relecture)

Différences, ligne à ligne : **ajout** de `verifier-invariants.py` en étape 1 ;
**renumérotation** des étapes 1–9 → 2–10 (les sous-étapes `a`–`e` du §4 ne bougent
pas) ; **remplacement** de la note parentétique du §1 ; **mise à jour** du renvoi
d'étape (« Étape 3 » → « Étape 4 ») dans le contrôle anti-fabulation.

```
Rapport quotidien du pôle Studio (profil studio, canal #infrastructure). Depuis /root/wiki, exécute dans l'ordre et cite la sortie brute de chaque script (jamais un résumé) :

## §1 — Cartographie et cohérence structurelle

1. python3 verifier-invariants.py --racine /root/wiki
2. python3 atelier/rd/outillage/graphe/generer-cartographie.py --depot /root/wiki --verifier
3. python3 atelier/rd/outillage/detecter-non-tracke.py --racine /root/wiki
4. python3 atelier/rd/outillage/verifier-coherence-infrastructure.py --racine /root/wiki

(verifier-invariants.py réintroduit au §1 le 2026-09-13, sur verdict de Sidy : le contrôle A, étendu aux cahiers append-only, doit mordre dans le rapport du pôle qui propose les correctifs, et non dépendre de la santé d'un autre profil. Redondance assumée et déclarée avec le job veille-frontmatter-quotidien du profil publication, 11:00 UTC.)

## §2 — Empreinte serveur

5. df -h /, free -h

## §3 — Registre Hermes-Terminal

6. Intégrité des bind-mounts, santé des gateways — relevé par `systemctl --user list-unit-files 'hermes-*'` d'abord (13 unités pour 14 profils ; `list-units` seul ne montre que les unités chargées, leçon de l'entrée [2026-09-01] du registre des problèmes) puis `is-active`/`is-enabled` par profil —, staleness de _inbox/

## §4 — Volet R&D (prioritaire, non conditionnel)

7. ./atelier/rd/outillage/detecter-nouvelles-fiches-rd.sh
8. Lire TOUTES les fiches R&D nouvelles (pas de seuil « aucune-nouvelle-fiche » qui saute la section). Pour chaque fiche :
   a. La lire en entier.
   b. La rapprocher de atelier/rd/cahiers/registre-problemes.md : une entrée existante couvre-t-elle ce problème, ou est-ce un problème nouveau ?
   c. Formuler une PROPOSITION d'action concrète (jamais une décision).
   d. Identifier les dépendances entre fiches R&D : quelle fiche nourrit quelle autre, quel angle mort reste ouvert.
   e. Si la fiche implique un autre agent (Studio, Gardien, Publication, etc.), le nommer et proposer un handoff explicite.
9. Relire les 5 entrées les plus récentes de registre-problemes.md. Pour chacune : l'état a-t-il changé depuis la dernière exécution ? Une proposition antérieure a-t-elle été appliquée, rejetée, ou est-elle stagnante ?
10. Synthèse R&D : 3 à 5 pistes prioritaires pour la prochaine session, classées par urgence et faisabilité. Marquer chaque piste PROPOSITION.

## Format du rapport

§1 Cartographie et cohérence (sorties brutes des scripts 1-4)
§2 Empreinte serveur
§3 Registre Hermes-Terminal
§4 R&D — analyse engagée (fiches nouvelles, registre-problemes, pistes prioritaires)
§5 Suggestions transversales

Contrôle anti-fabulation : ne jamais reformuler la sortie des scripts, la coller telle quelle. Étape 4 est le même contrôle (registre-problemes.md, entrée 2026-08-17).
```
