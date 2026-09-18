---
title: "Registre des chantiers — carte vivante des travaux ouverts du dépôt"
type: registre
tags: [atelier, rd, registre, chantiers, pilotage]
created: 2026-09-01
updated: 2026-09-18
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
  - "[[atelier/rd/veille/registre]]"
  - "[[atelier/rd/cahiers/bilan-2026-08-15-pont-agents]]"
  - "[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]"
  - "[[atelier/rd/infrastructure/2026-08-20_pistes-developpement-infrastructure]]"
---

# Registre des chantiers du dépôt

> **Ce que cette pièce est.** La carte vivante de **tous** les chantiers ouverts du
> dépôt, tous domaines confondus, tenue au pôle R&D sur demande de Sidy (2026-09-01).
> Elle existe pour une raison précise : jusqu'ici les pistes vivaient éclatées entre six
> registres locaux tenus à jour de façon inégale, et **aucun n'avait de vue d'ensemble** —
> un agent reprenant le fil à froid ne pouvait pas savoir où en étaient les choses.
>
> **Ce qu'elle n'est pas.** Elle **recense, elle n'absorbe pas.** Aucun contenu ne migre
> ici : chaque chantier reste instruit dans sa fiche et dans son circuit. Le registre ne
> porte que le pointeur, le statut et la prochaine action. Il ne recopie jamais une entrée
> du registre des problèmes, une scrutation de veille, un discernement, ni une valeur
> qu'un script calcule — il pointe.
>
> **Ce qu'elle ne décide pas.** Aucun verdict, aucune priorité doctrinale (Cmd 12), aucune
> décision engageante (Cmd 13). Les priorités portées sur les lignes d'ingénierie sont
> **proposées**, jamais tranchées.

## Comment lire ce registre

- **Identifiants stables**, jamais réutilisés ni renumérotés : `INS-` Instrument ·
  `INF-` infrastructure & agents · `OUT-` outillage & scripts · `BIB-` bibliothèque ·
  `CAS-` études de cas · `PRO-` process & protocole · `DOC-` doctrinal. Cet ID est la
  poignée greppable : il survit à un changement de titre et se cite depuis une entrée
  d'annales, une file de tâches ou un message d'agent.
- **Statuts** (mêmes mots que le registre des problèmes) : `ouvert` · `en-cours` ·
  `bloque` (une dépendance externe empêche d'avancer) · `attente-verdict` (rien ne manque
  sauf la décision de Sidy) · `clos` · `caduc` (le chantier n'a plus d'objet).
- **Discipline** : ce registre est **révisable en place**, à la différence des cahiers
  append-only. Un chantier clos n'est jamais supprimé (Cmd 10) : il garde son ID et
  descend en §9 avec sa date. L'historique, c'est git et les annales.
- **Instruit ou seulement recensé** (2026-09-01) : un chantier d'ingénierie qui entre
  en instruction reçoit un **triptyque** `intent.md` / `spec.md` / `plan.md` dans un
  dossier de son domaine (`atelier/rd/<domaine>/<id>-<slug>/`, voir
  `atelier/CLAUDE.md` §Nomenclature et le gabarit
  [[atelier/rd/outillage/gabarit-triptyque-chantier]]). La colonne *Triptyque* porte
  le pointeur ; vide = chantier recensé, pas encore instruit — ce n'est pas un défaut,
  c'est un état. Le registre **pointe, il n'absorbe pas** : aucun contenu du triptyque
  n'est recopié ici.
- **Vérification avant inscription** : aucune ligne n'est inscrite sans avoir été
  confrontée au disque et à `git log`. Ce qui n'a pas pu l'être va en §8, **jamais
  asserté ouvert**.

## Entretien

Quiconque **ouvre, fait avancer ou clôt** un chantier met à jour sa ligne **dans la même
passe que son entrée d'annales** (Cmd 9). On ne crée pas une obligation nouvelle : on
greffe une ligne sur un rituel déjà respecté. La désignation d'un agent responsable d'une
revue périodique est une décision engageante (Cmd 13) — elle est en §Points ouverts.

---

## 0. Vue d'ensemble

**63 lignes de chantier** — **toutes dans les quatre statuts déclarés** depuis
l'alignement du 2026-09-13, l'écart `recense` ayant été **clos le 2026-09-17 sur
verdict de Sidy** (voir la note ci-dessous) —, plus
**11** versés en §9 (clos ou caducs) et 6 lignes en §8
(à vérifier, non assertées ouvertes). Décompte mécanique — si vous modifiez une
ligne, ce tableau se recompte, il ne s'estime pas.

> **Rectification du 2026-09-17 (Cmd 10), seconde passe.** Le remplacement opéré plus
> tôt ce jour dans ce paragraphe avait **cassé la phrase** : l'ancre avait absorbé le
> mot « depuis », laissant une parenthèse ouverte et un membre de phrase sans verbe.
> La phrase est reprise entière ci-dessus. Mes contrôles étant tous structurels
> (`verifier-invariants.py`, Cmd 15, recomptage), **aucun ne pouvait voir une prose
> cassée** : c'est la relecture qui l'a vue, et le fait est inscrit plutôt que réparé
> en silence.
>
> **Et le constat se durcit.** `recense`, porté par `BIB-05` depuis `dfae737`, n'est
> pas seulement **sans colonne** au tableau par pôle : il est **hors du vocabulaire
> déclaré** au § *Comment lire ce registre*, qui n'admet que `ouvert`, `en-cours`,
> `bloque` et `attente-verdict`. C'est la **même classe de défaut** que l'écart
> `DOC-06`/`DOC-07`/`DOC-08` clos le 2026-09-13, et il est de mon fait. La machine
> **ne le résout pas d'office** : élargir le vocabulaire ou ramener `BIB-05` à une
> valeur déclarée est un verdict (Cmd 12), soumis à Sidy sous
> `recomptage-tableau-registre`. En attendant, `BIB-05` **reste tel quel**, et le
> total des quatre colonnes ne peut pas le compter.
>
> **Verdict rendu le 2026-09-17.** Sidy tranche : « ramène `BIB-05` à `ouvert`, le
> statut `recense` n'existe pas ». Des deux issues soumises, c'est donc la seconde —
> **le vocabulaire ne s'élargit pas**, la valeur fautive est ramenée à une valeur
> déclarée. `BIB-05` porte `ouvert` depuis ce jour ; son contenu est inchangé, seul
> le statut l'est. Le tableau par pôle **n'a pas besoin de colonne nouvelle** et
> redevient exact pour `BIB` : `ouvert` 1 → 2, total 3 → 4 ; total général `ouvert`
> 32 → 33 et 56 → 57. L'écart relevé ci-dessus est **clos** ; reste seul en attente
> l'écart global de recomptage, sous `recomptage-tableau-registre`.

> **Note de clôture et de correction (2026-09-17, Cmd 10).** `BIB-03` quitte §1–§7
> pour §9 : le chantier était clos depuis le **2026-09-02** (versement vers
> `textes/` au commit `d5a52d0`), seul le verdict manquait — il est rendu ce jour.
> Les compteurs bougent de **ce seul déplacement** : §1–§7 **61 → 60**, §9
> **10 → 11**, et au tableau par pôle `BIB` perd un `attente-verdict` (2 → 1,
> total 4 → 3), le total général passant `attente-verdict` 13 → 12 et 57 → 56.
>
> **Deux défauts de la passe `dfae737` (2026-09-16) sont corrigés en même temps,
> et signalés plutôt que tus.** (1) `BIB-05` avait été inséré **dans §6 Process**
> au lieu de §4 Bibliothèque ; la ligne est remise à son pôle, sans rien changer
> à son contenu. (2) La phrase ci-dessus disait « toutes dans les quatre statuts
> déclarés » : c'est **faux depuis `BIB-05`**, qui porte `recense`, un cinquième
> statut. Le constat est inscrit, la phrase amendée.
>
> **Ce qui n'est pas corrigé ici, et pourquoi.** Le tableau par pôle **ne
> colonne pas `recense`** : `BIB-05` n'y est donc **compté nulle part**, et sa
> ligne `BIB` reste de ce fait inexacte d'une unité. Ajouter une colonne
> déciderait de la **forme** du tableau, et cette forme est précisément ce qui
> attend le verdict de Sidy (queue : `recomptage-tableau-registre`). La machine
> ne tranche pas (Cmd 12). De même, le recomptage mécanique du 2026-09-17 donne
> **62 lignes** en §1–§7 après cette passe, contre les 60 désormais déclarées, et quatre lignes de pôle
> (`INF`, `OUT`, `BIB`, `DOC`) divergent du réel quand `INS`, `CAS` et `PRO`
> tombent juste : **cet écart global n'est pas touché**, il est déjà en attente
> sous `recomptage-tableau-registre`.

> **Note de recomptage (2026-09-15, seconde passe).** `OUT-19` ouvert (P5 du rapport Studio du jour). Recompte mécanique des lignes §1–§7 **avant** ajout : 60 = `ouvert` 33 / `bloque` 5 / `en-cours` 9 / `attente-verdict` 13 (la note ci-dessous, à 58, précède l'ajout d'`OUT-18`). **Après** ajout : **61 = 34 / 5 / 9 / 13**.
>
> **Note de recomptage (2026-09-15).** `OUT-17` est ajouté ce jour (contrôles
> manquants autour de la file d'écritures de skills), en même temps que `OUT-16`,
> versé par la passe concurrente du même jour. Le tableau a donc été **recompté
> depuis les lignes**, statut par statut, comme la règle de cette section
> l'exige : **58 lignes** en §1–§7, réparties **`ouvert` 32 / `bloque` 5 /
> `en-cours` 9 / `attente-verdict` 12**. Aucune valeur hors vocabulaire : le
> nombre de lignes et la somme des quatre colonnes **coïncident** cette fois
> (58 = 58), l'écart de vocabulaire étant clos depuis le 2026-09-13. §9 porte
> 10 lignes ; le §8 n'est pas recompté ici (ses lignes ne sont pas assertées).
>
> Les totaux issus du recomptage du 2026-09-13 étaient `33 / 5 / 5 / 10 = 53`,
> pour **56 lignes**. L'écart (+2 lignes, et une répartition qui bouge) **n'est
> pas expliqué ligne à ligne par cette passe** : entre les deux recomptages,
> plusieurs passes ont ouvert, requalifié ou clos des chantiers. Il est
> **signalé, pas lissé** — une passe qui découvre un écart ne le corrige pas
> d'office (Cmd 12) ; mais une passe qui ajoute une ligne doit recompter, et
> c'est ce qui a été fait ici.

> **Note de recomptage (2026-09-15, seconde passe).** `DOC-09` est ouvert ce jour
> — chantier de réminiscence autour du kamon Kouyaté (cadre et dossier A au
> Domaine Réservé), dont le dossier C demeure **non ouvert**. Le tableau a été
> **recompté depuis les lignes**, statut par statut, **par script et non par
> estime** : **59 lignes** en §1–§7, réparties **`ouvert` 33 / `bloque` 5 /
> `en-cours` 9 / `attente-verdict` 12**. Le nombre de lignes et la somme des
> quatre colonnes **coïncident** (59 = 59) ; aucune valeur hors vocabulaire.
> §9 porte toujours 10 lignes ; le §8 n'est pas recompté (lignes non assertées).
> Le seul mouvement par rapport au recomptage de la première passe du jour est
> `ouvert` 32 → **33**, imputé intégralement à la ligne ajoutée.

> **Note de recomptage (2026-09-15, troisième passe).** `OUT-18` est ouvert ce
> jour — l'organe de vérification (serveur MCP, `CLAUDE.md` §VIII.11) était
> réputé éprouvé **en bloc** alors qu'une seule de ses entrées l'avait été ;
> l'outil `carte_du_depot` échoue sur une option que le script n'accepte pas.
> Le tableau a été **recompté depuis les lignes**, statut par statut, **par
> script et non par estime** : **60 lignes** en §1–§7, réparties **`ouvert` 34 /
> `bloque` 5 / `en-cours` 9 / `attente-verdict` 12**. Lignes et somme des quatre
> colonnes **coïncident** (60 = 60) ; aucune valeur hors vocabulaire. §9 porte
> toujours 10 lignes. Le seul mouvement par rapport à la seconde passe du jour
> est `ouvert` 33 → **34**, imputé à la ligne ajoutée.

> **Note de recomptage (2026-09-15, quatrième passe).** `INF-16` change de statut ce
> jour — `ouvert` → **`attente-verdict`** : son plan a été **visé** par Sidy en session,
> et les trois relevés qui ne dépendaient d'aucun verdict (étapes 2, 3b et 3c) sont
> exécutés et consignés au `spec.md`. Rien ne manque plus que des **décisions** : la
> charge de référence (U1–U5), le budget, le sort de l'option D, le lieu d'installation,
> et la voie de mesure de l'étape 4. Le tableau a été **recompté depuis les lignes**,
> statut par statut, **par script et non par estime** : **60 lignes** en §1–§7,
> réparties **`ouvert` 33 / `bloque` 5 / `en-cours` 9 / `attente-verdict` 13**. Lignes
> et somme des quatre colonnes **coïncident** (60 = 60) ; aucune valeur hors vocabulaire.
> Le seul mouvement par rapport à la troisième passe du jour est `ouvert` 34 → **33** et
> `attente-verdict` 12 → **13** : **une seule ligne a changé de colonne**, aucune ligne
> n'a été ajoutée ni retirée. *Le compteur employé porte sur §1–§7 ; il ne compte pas §9,
> et cette note ne se prononce donc pas sur son nombre de lignes.*
>
> **Addendum du même jour, après coup.** Une **passe concurrente** a, depuis ce relevé,
> ouvert `OUT-19` et **recompté le tableau à 61 lignes** (`ouvert` 34 / `bloque` 5 /
> `en-cours` 9 / `attente-verdict` 13) — sa note est en tête de section, et elle confirme
> elle-même le `60 = 33/5/9/13` d'avant l'ajout, ce que ce relevé donnait. Ce qui est
> **signalé et non corrigé** (Cmd 12) : les numéros d'ordre du jour (« seconde »,
> « troisième », « quatrième ») ont été attribués par des passes **indépendantes** et **ne
> suivent plus l'ordre chronologique** — c'est la **mesure datée** qui fait foi, jamais le
> numéro.

Le 2026-09-15 : ouverture de `DOC-09` et d'`OUT-18`, `INF-16` requalifié
`attente-verdict` (voir les notes de recomptage ci-dessus, seconde à quatrième passes
du jour).
Mis à jour le 2026-09-13 : `INF-09` requalifié `attente-verdict` (alignement sur
son propre texte), `INF-17` ouvert et versé en **§9** (migration de provider), et
les trois statuts `DOC` hors vocabulaire ramenés au vocabulaire déclaré —
seconde passe du 2026-09-13, cf.
[[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]].
Le 2026-09-07 : ouverture de `INF-16` (machine d'IA locale et
développement SLM, chantier de comparaison, triptyque posé, plan en `brouillon`).
Le 2026-09-06 : ouverture de `OUT-15` et `INS-01` passé `ouvert` → `en-cours`
(transcription du ch. II de Shayegan faite dans `textes/`, relecture OCR en attente).

> **Note de recomptage (2026-09-07).** Deux branches concurrentes ont été fusionnées
> ce jour : l'une portait `OUT-15` et `DOC-08`, l'autre `INF-16`. Ni l'un ni l'autre
> des deux totaux n'a été repris — le tableau a été **recompté depuis les lignes
> elles-mêmes**, ligne par ligne et statut par statut, comme la règle de cette section
> l'exige.
>
> Ce recomptage a mis au jour **quatre écarts antérieurs à la fusion**, tous
> signalés et **aucun corrigé d'office** (Cmd 12) — ils ne relèvent pas de la passe
> qui les découvre :
>
> 1. **`INS`** — `INS-01` est passé `en-cours` le 2026-09-06, mais la ligne du
>    tableau portait toujours 10 `ouvert` / 1 `en-cours`. Recomptée : 9 / 2.
> 2. **`OUT`** — 8 lignes réelles (`OUT-02` à `OUT-08`, plus `OUT-15`), quand le
>    tableau en portait 6 puis 7. L'écart précédait l'ajout d'`OUT-15`.
> 3. **`DOC`** — 8 lignes réelles pour 6 annoncées, et surtout **trois statuts hors
>    du vocabulaire déclaré** par la section *Comment lire ce registre* : `DOC-06`
>    porte `fait`, `DOC-07` porte `partiel`, `DOC-08` porte `recensé`. Aucune des
>    quatre colonnes ne peut les accueillir : ils sont comptés à part, jamais
>    répartis d'autorité dans une colonne qui ne les nomme pas.
> 4. **Forme** — les lignes `DOC-06` et `DOC-07` portent 7 colonnes dans un tableau
>    qui en déclare 4.
>
> **Point soumis à Sidy** : soit le vocabulaire des statuts s'élargit (`fait`,
> `partiel`, `recensé` deviennent déclarés), soit ces trois lignes se ramènent au
> vocabulaire existant. Tant que ce n'est pas tranché, le total des quatre colonnes
> (53) et le nombre de lignes (56) diffèrent — et c'est l'écart lui-même qui est
> l'information.
>
> **Tranché le 2026-09-13 (verdict Sidy)** : les trois lignes **se ramènent** au
> vocabulaire déclaré — `DOC-06` et `DOC-07` en `en-cours`, `DOC-08` en
> `attente-verdict`. L'écart est clos ; les nouveaux totaux sont portés par la
> note de recomptage du 2026-09-13 (seconde), ci-dessous. Motifs du verdict au §3
> de [[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]].

> **Note de recomptage (2026-09-02).** Deux sessions concurrentes ont porté deux
> totaux différents sur cette ligne — 31/3/5/9 d'un côté, 30/3/5/10 de l'autre, tous
> deux à 48. Ni l'un ni l'autre n'a été retenu : le tableau a été **recompté depuis
> les lignes elles-mêmes**, statut par statut, conformément à la règle que cette
> section énonce. Le compte exact est celui ci-dessous.

> **Note de recomptage (2026-09-13).** Le recompte mécanique des tableaux §1–§7
> depuis leurs propres lignes a montré **deux lignes de pôle fausses**, non une
> seule : `INF` annonçait **3** `attente-verdict` là où il y en a **2**
> (`INF-15` est clos depuis le 09-10), et `PRO` en annonçait **2** là où il y en a
> **3**. Le rapport de monitoring Studio du 2026-09-13 avait mesuré l'écart et
> l'imputait à `INF` seul — le total `attente-verdict`, lui, **tombait juste par
> compensation**. Recompté, il vaut bien **10**, et les totaux généraux
> (`33 / 5 / 5 / 10 = 53`, +3 hors vocabulaire = **56 lignes**) sont **inchangés** :
> seules les deux lignes ci-dessus bougent. `INF-15` quitte en outre le §2 pour
> descendre en **§9** avec sa date, comme la discipline de ce registre le prescrit.
> Recompte et versement : correctif **C4** de
> [[atelier/rd/infrastructure/2026-09-13_correctifs-rapports-studio]].

> **Note de recomptage (2026-09-13, seconde).** Les trois statuts hors vocabulaire
> ont été **ramenés au vocabulaire déclaré** sur verdict de Sidy — `DOC-06` et
> `DOC-07` en `en-cours` (un ingest rouvert le même jour pour une 6ᵉ fiche ; une
> pièce renvoyée à `OUT-08`), `DOC-08` en `attente-verdict` (matière réservée par
> Sidy, action proposée en attente de visa). `INF-09` est requalifié
> `attente-verdict` : son propre texte dit le verdict rendu. Le tableau est
> **recompté depuis ses lignes**, statut par statut — `INF` passe de 8/2 à **7/3**
> en `ouvert`/`attente-verdict`, `DOC` de 4/0/0/1 à **4/2/0/2**. Le nombre de
> lignes **ne bouge pas** : **56** avant, **56** après — mais le total des quatre
> colonnes passe de **53** (faux par construction : il laissait trois lignes
> dehors) à **56**. `INF-17` va en **§9**. **Écart relevé en recomptant** : le §0
> déclarait « 7 versés en **§9** » quand ce tableau en portait **9** — `INF-14` et
> `INF-15` y ont été versés sans que ce compteur suive (le recompte C4 du matin
> portait sur §1–§7, pas sur §9). Le compteur est corrigé à **10** lignes, après
> versement d'`INF-17`. Passe :
> [[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]].

> **Note de recomptage (2026-09-16).** Ouverture de **`BIB-04`** — le dépouillement du
> lexique coranique de Gloton, sur ordre de Sidy. Le chantier tournait depuis le
> 2026-09-16 avec trois fichiers déposés et un journal de reprise, **sans aucune ligne
> ici** : un agent reprenant le fil à froid par le registre ne l'aurait pas vu, ce qui
> est le défaut même que cette carte existe pour corriger. Il relève de `BIB` et non de
> `OUT` : l'outil d'extraction n'en est que le moyen, l'objet est un ouvrage de la
> bibliothèque physique. Tableau recompté depuis ses lignes : `BIB` passe de 1 à **2**
> en `ouvert` et de 3 à **4** lignes ; le total général de 32 à **33** en `ouvert` et de
> 56 à **57** lignes. Commits `e6c4f1f` et `2b4b45a`.

| Pôle | ouvert | en-cours | bloqué | attente-verdict | total |
|---|---|---|---|---|---|
| `INS` Instrument | 9 | 2 | 1 | 3 | **15** |
| `INF` Infrastructure & agents | 7 | 3 | 1 | 3 | **14** |
| `OUT` Outillage & scripts | 7 | — | 1 | — | **8** |
| `BIB` Bibliothèque | 2 | — | 1 | 1 | **4** |
| `CAS` Études de cas | 1 | — | 1 | — | **2** |
| `PRO` Process & protocole | 3 | — | — | 3 | **6** |
| `DOC` Doctrinal | 4 | 2 | — | 2 | **8** |
| **Total** | **33** | **7** | **5** | **12** | **57** |

> **Note de passe (2026-09-16), clôture de `BIB-04` sur le matériau photographié.**
> La moisson du lexique de Gloton est close sur les 107 planches extraites des 28
> photographies : **169 racines** avec leur case 4 (`edccb13`). Treize discontinuités
> subsistent dans la numérotation ; le contrôle par la page bornant chaque écart les
> attribue toutes à des **pages non photographiées**, aucune à un bloc-racine omis
> (sortie brute au journal §2). **Sidy a tranché le même jour : le reste du lexique sera
> photographié plus tard, au gré des opportunités.** `BIB-04` passe donc d'`ouvert` à
> **`attente-verdict`** — non parce qu'il resterait du travail en attente d'ordre, mais
> parce que ce qui reste exécutable dépend de deux arbitrages (régénération de
> `glossaire-unifie.md`, périmètre divergent des deux scripts). `BIB` passe de 2 à **1**
> en `ouvert` et de 1 à **2** en `attente-verdict`, à total constant (**4**) ; le total
> général de 33 à **32** en `ouvert` et de 12 à **13** en `attente-verdict`, à **57**
> lignes inchangées.
>
> **Réserve à ne pas escamoter (Cmd 5).** Un recomptage mécanique des lignes de ce
> registre **ne reconcilie pas** avec le tableau ci-dessus pour les pôles `DOC`, `OUT` et
> `INF`. La cause est de forme, non de fond : les tableaux n'ont pas tous le même nombre
> de colonnes (les lignes déjà closes en portent six, les autres huit ou neuf), si bien
> qu'un comptage par position de colonne les écarte. Je n'ai **pas** touché à ces trois
> pôles : l'écart préexiste à cette passe et n'appartient pas au chantier Gloton. Il est
> signalé ici pour qu'un recomptage général soit fait sciemment, sur une forme de tableau
> d'abord unifiée — décision qui appartient à Sidy.

**Ce que ce tableau dit d'abord** : 12 chantiers n'attendent **que** la décision de
Sidy — rien d'autre ne leur manque. 5 sont bloqués par une dépendance qui n'est pas
entre nos mains (une PR amont, une prise de vue, un texte à localiser). C'est là, et non
dans le nombre total, que se lit ce qui peut avancer aujourd'hui.

Le `DOC-01` compte pour une ligne mais recouvre **37 fiches de discernement `speculatif`**
en attente de verdict : elles ne sont ni listées ni hiérarchisées ici (Cmd 12), voir §7.

> **Note de recomptage (2026-09-18).** `OUT-20` ouvert (verdict F de la passe
> Studio/Publication du jour). Recompte **mécanique** des lignes §1–§7 **avant** ajout :
> **62** — `ouvert` 35 / `bloque` 5 / `en-cours` 9 / `attente-verdict` 13. Le §0
> déclarait **60** : l'écart de deux lignes est **antérieur à cette passe** et la note
> du 2026-09-13 le constatait déjà (« 62 lignes en §1–§7 après cette passe, contre les
> 60 désormais déclarées ») sans que le chiffre de tête ait suivi. Il n'est pas
> reconstitué rétroactivement ici : le compte de tête est simplement remis sur la
> mesure. **Après** ajout : **63 = `ouvert` 35 / `bloque` 5 / `en-cours` 9 /
> `attente-verdict` 14.**

## 0 bis. Infrastructure — où lire l'état réel

Ce registre **ne recopie aucune valeur** qu'un script calcule ou qu'une archive porte :
une valeur recopiée est une valeur périmée. Il dit **où regarder**.

| Ce qu'on veut savoir | Où c'est établi mécaniquement |
|---|---|
| Invariants du dépôt (Sceaux, liens, étanchéité, annales) | `verifier-invariants.py --racine /root/wiki` |
| Cohérence Hermes/cron réellement appliquée (anti-fabulation) | `atelier/rd/outillage/verifier-coherence-infrastructure.py` + champ `infra_verif` des fiches |
| État du serveur au jour le jour | `atelier/rd/infrastructure/monitoring-archive/` (rétention 40 j) |
| Fichiers présents mais non suivis par git | `atelier/rd/outillage/detecter-non-tracke.py` |
| Architecture serveur et agents | [[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]] |
| Fournisseur d'inférence courant des profils | [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] |
| Échecs, blocages, anomalies et leur résolution | [[atelier/rd/cahiers/registre-problemes]] (append-only) |
| Réussites et optimisations | [[atelier/rd/cahiers/journal-optimisations]] (append-only) |
| Veille externe qualifiée | [[atelier/rd/veille/registre]] (append-only) |
| Incidents caractérisés | `atelier/rd/incidents/` |
| Graphe de cartographie du dépôt | `graphe-cartographie.json`, régénéré par `atelier/rd/outillage/graphe/generer-cartographie.py` |

---

## 1. Instrument (`INS`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Triptyque | Ouvert par |
|---|---|---|---|---|---|---|
| INS-01 | Transcription du ch. II de Shayegan (*Les Disciplines Spirituelles*) — **faite** dans `textes/les-disciplines-spirituelles-daryush-shayegan/` | `en-cours` | relecture de la transcription OCR (artefacts de ligne signalés) | [[atelier/rd/instrument/2026-08-30_reseau-subtil-unification-axes-deux-echelles]] §6 | — | fiche du 2026-08-30, transcription 2026-08-30 |
| INS-02 | Mode « axe unifié » + champ `echelle` dans le générateur et le prototype | `ouvert` | spécifier avant de coder | même fiche, §4.2 | [[atelier/rd/instrument/ins-02-axe-unifie/intent]] | 2026-08-30 |
| INS-03 | Cieux planétaires ↔ *lokas* — comparaison licite jamais tentée | `ouvert` | ouvrir une fiche `discernement` dédiée (Cmd 3) | même fiche, §6 | — | 2026-08-30 |
| INS-04 | 22 sentiers séphirothiques comme réseau de canaux rayonnant de Tiferet | `bloque` | l'arrangement des sentiers n'est pas fixé au dépôt — instruire en amont | même fiche §3.3 ; `doctrinal/discernement/2026-08-30_nadis-du-coeur-sentiers-sephirothiques-tiferet` (`speculatif`) | — | 2026-08-30 |
| INS-05 | Bifurcation des centres surnuméraires — trois options posées, aucune implémentée | `attente-verdict` | Sidy tranche l'option | même fiche, §7.3 | — | 2026-08-30 |
| INS-06 | Divergences table/planches — deux cellules vides d'*Ājñā* | `attente-verdict` | combler ou laisser : relevé explicitement remis à Sidy | même fiche, §7.5 | — | 2026-08-30 |
| INS-07 | Figuration de la discontinuité — la réserve doctrinale la plus lourde que le rendu actuel ne porte pas | `ouvert` | instruire §7 « dans l'ordre, avant d'écrire une ligne de rendu » | [[atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable]] §8.6 | — | 2026-08-30 |
| INS-08 | Parallèle islamique sur la couronne de la tête (Guénon ch. XX, note 3) — texte non nommé | `ouvert` | localiser la source primaire | fiche du 2026-08-30, §6 | — | 2026-08-30 |
| INS-09 | Rendu d'al-Insān al-Kāmil — proposition non validée dans le prototype | `attente-verdict` | Sidy valide ou révise le rendu | [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]] P2.4 | — | jalon du 2026-08-20 |
| INS-10 | Détail optique de la lentille barzakh (degrés 19-20) | `ouvert` | spécifier | même jalon, P2.5 | — | 2026-08-20 |
| INS-11 | Fondation équivalente aux `hadarat-khams` pour la branche séphirothique (10 Sephiroth, 3 colonnes) — préalable à tout ancrage Kabbale complet | `ouvert` | fiche de fondation, sur source primaire | même jalon, P6.13 ; [[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3]] | — | 2026-08-20 |
| INS-12 | Colonne *faṣṣ* (Fuṣūṣ) de la table des 28 degrés — `to-source` (3 marqueurs restants) | `ouvert` | non bloquant : `instrument-donnees.yaml` ne l'utilise pas | `doctrinal/symboles/table-28-degres-nafas-rahman` | — | 2026-07-01 |
| INS-13 | Bandeau zodiacal horizontal — données déjà sourcées, **rendu manquant** | `ouvert` | implémenter le rendu | [[atelier/index]] §Instrument ; [[atelier/rd/instrument/spec-anneau-zodiacal]] | [[atelier/rd/instrument/ins-13-bandeau-zodiacal/intent]] | 2026-07-27 |
| INS-14 | Versant Sanātana Dharma — la fondation védantique est disponible (ch. X, XV, XVI de *L'Homme et son devenir*), la structure à 4 états n'est **pas encore ancrée** | `ouvert` | ancrer le registre `vedanta` | [[atelier/index]] §Instrument ; [[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16]] | — | 2026-07-16 |
| INS-15 | Situation polaire — **mode cosmologique** de l'Instrument : horizon, sphère céleste, révolution ascendante et descendante du soleil, roue du Manvantara ; bascule cosmologique/métaphysique sur le plan de base | `en-cours` | plan **visé** le 2026-09-02 ; phases 2 et 3 faites (donnée, générateur v0.2.6, rendu) — reste la mise en production (Cmd 13) | demande de Sidy du 2026-09-02 ; [[doctrinal/sources/tilak-origine-polaire-tradition-vedique]] ; [[atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable]] §6bis.5 | [[atelier/rd/instrument/ins-15-situation-polaire/intent]] | 2026-09-02 |

*Suites de [[atelier/rd/instrument/2026-08-29_mise-en-regard-majma-al-bahrayn-registres]] §7 :
non dépouillées dans cette passe → §8.*

## 2. Infrastructure & agents Hermes (`INF`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Triptyque | Ouvert par |
|---|---|---|---|---|---|---|
| INF-01 | Isolation mémoire Hermes par sub-agent (`memory_enabled`) — condition du déploiement du skill Karūbī | `bloque` | dépendance amont : PR #34098 de `hermes-agent` (hors de notre main) | [[atelier/rd/synthese-deploiement-memoire]] §187-189 ; [[atelier/rd/outillage/investigation-isolation-memoire-hermes]] | — | jalon du 2026-08-20, P3.6 |
| INF-02 | Sandbox R&D `/root/sandbox-rd/` — ouverte le 2026-08-18, **encore vide** : aucun montage de veille n'y a été éprouvé | `ouvert` | y éprouver un premier montage issu de la veille | [[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]] | — | 2026-08-18 |
| INF-03 | Phase 3 — automatisation de la veille infrastructure : décisions entièrement tranchées, **aucun automatisme écrit** — confirmé mécaniquement le 2026-09-01 : le script existe et est exécutable, mais **aucun des trois jobs cron qu'une fiche du 2026-08-23 déclarait créés n'est déclaré dans les quatorze profils Hermes** | `attente-verdict` | la proposition de reprise du 2026-08-31 est en `brouillon`, soumise à Sidy | [[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]] ; [[atelier/rd/cahiers/proposition-veille-automatique-studio-2026-08-31]] ; [[atelier/rd/infrastructure/2026-08-23_deploiement-veille-infrastructure-quotidienne]] | — | 2026-08-11, rouvert 2026-08-31 |
| INF-04 | Bureau TUI — vérification en conditions réelles jamais faite | `ouvert` | éprouver, puis consigner | [[atelier/rd/infrastructure/bureau-tui-architecture]] ; [[atelier/rd/cahiers/2026-08-31_rapport-investigation-architecture-modulaire-agents]] | — | jalon du 2026-08-15 |
| INF-05 | Migration des prompts Hermes vers la nomenclature modulaire — **1 rôle aligné sur 12** (`publication`) | `en-cours` | aligner les onze autres | [[atelier/rd/cahiers/2026-08-31_rapport-migration-11-agents-et-contribution-choura]] | — | 2026-08-31 |
| INF-06 | Monitoring de charge en série temporelle — seul un instantané quotidien existe | `ouvert` | spécifier la série | jalon du 2026-08-20, P1.2 | — | 2026-08-20 |
| INF-07 | Fonction réelle du processus `omniroute` (1040 Mo de RAM) | `en-cours` | partiellement documenté depuis (migration 2026-08-26, incident 2026-08-27) — reste à décrire le rôle nominal | [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] ; [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]] | — | jalon du 2026-08-20, P1.1 |
| INF-08 | Reproduction contrôlée de l'incident de robustesse persona-LLM | `ouvert` | reproduire, ou consigner l'abandon | [[atelier/rd/outillage/robustesse-documents-persona-llm]] | — | jalon du 2026-08-20, P4.10 |
| INF-09 | Levier d'action du cycle Choura : le dispositif produit des perspectives, mais sans contribution de Sidy le cycle reste consultatif — **cycle mis en pause par Sidy (2026-09-01, dit en session)** | `attente-verdict` | reprise sur nouvelle décision de Sidy (hook de contribution, ou abandon) — verdict `attente-verdict` rendu : pause, pas de hook pour l'instant | signalé par le Gardien dans le cycle du 2026-09-01 (cf. Domaine Réservé, dossier `choura/`) | — | 2026-09-01 |
| INF-10 | Contrôle anti-fabulation `coherence-infrastructure-brute` — second job cron en échec, non documenté | `ouvert` | diagnostiquer | [[atelier/rd/cahiers/registre-problemes]], entrée `[2026-08-18]` | — | 2026-08-18 |
| INF-11 | Continuité des tâches et de l'information entre Claude Code, Hermes Terminal et Discord — angle mort structurel (un cron « créé » le 2026-08-17 n'existait pas) | `ouvert` | c'est le motif d'existence du champ `infra_verif` ; reste à couvrir le passage d'information | registre des problèmes, entrée `[2026-08-17]` | — | 2026-08-17 |
| INF-12 | Positions zodiacales 5, 8 et 12 des agents : les douze brouillons existent sur disque (2026-08-15), mais le compte-rendu de chantier les donne « non traitées, en attente de verdict » — contradiction non levée | `attente-verdict` | confronter brouillons et verdict | `atelier/rd/cahiers/brouillons-extension-zodiacale/` ; jalon du 2026-08-20, P4.9 | — | 2026-08-11 |
| INF-13 | Scission du dépôt : le rendu de l'Instrument passe au dépôt frère `Sidyvision/instrument` (privé) — le §VII, *Règle commune des MANIFESTES*, exprimé en infrastructure plutôt qu'en discipline | `en-cours` | **clos pour l'essentiel** : dépôt frère créé, **passé public** le 2026-09-01 (verdict Sidy), `main` protégée avec `enforce_admins` actif et **épreuve réelle du refus faite**. Reste différée (Cmd 13) : l'automatisation du manifeste (PAT + workflow) — l'étage manuel fonctionne | [[atelier/rd/infrastructure/inf-13-scission-depot-instrument/intent]] | [[atelier/rd/infrastructure/inf-13-scission-depot-instrument/intent]] | 2026-09-01 |
| INF-16 | Machine d'IA locale et développement SLM — aucune capacité d'inférence locale n'existe (le serveur n'a pas de GPU), alors que la charte du pôle vise l'émancipation des intermédiaires tiers. Ouvert **comme comparaison**, sur consigne de Sidy : explorer les options (Mac Studio, Mac mini + LLM cloud, poste NVIDIA, GPU loué, GPU à l'heure, statu quo, montages étagés) jusqu'à la meilleure | `attente-verdict` | **étape 1** : Sidy arrête la charge de référence (lesquels des cinq usages U1–U5 comptent) — rien ne peut être comparé avant. Plan en `brouillon`, visa attendu (Cmd 6). **2026-09-07** : option E (GPU à l'heure) écartée puis **rouverte sous condition** le même jour — justifiable en complément d'un Mac Mini pour les rafales d'entraînement, jamais seule ni comme capacité permanente ; le critère de propriété né du premier verdict pèse toujours sur D, non tranché. Chantier mené **par reprises successives** (demande de Sidy) : l'état vivant et le prochain pas tiennent dans le §*Point de reprise* du `plan.md`. **2026-09-15** : plan **visé** (Sidy, en session) — étapes 2, 3b et 3c exécutées et consignées au `spec.md` ; il ne reste que des **décisions** (charge de référence, budget, sort de D, lieu, voie 4a/4b/4c). **Un devis d'une rafale d'entraînement RunPod attend d'être lu** — `devis-rafale-runpod-2026-09-16.md`, ≈ 4 à 28 $, rien lancé. **2026-09-16** : **troisième verdict — E est rouverte sans condition** (« On ouvre à nouveau l'option E. ») ; la rafale n'est plus subordonnée à une machine possédée, les préalables du run restent à faire, la dépense reste sous porte humaine. **Puis les trois préalables sont faits** : jeu de données constitué par script (872 enregistrements, 11,5 Mo, **hors dépôt**, deux gardes éprouvées), jeu d'évaluation (13 tâches, 4 familles), runbook d'entraînement. **Restent le modèle de base et le compte RunPod** — l'engagement lui-même. **Le soir du 2026-09-16 : pause** — la rafale n'a pas démarré (blocage de **manipulation** sur l'accès au compte, non technique) ; aucun pod, aucune dépense, rien sorti du dépôt ; reprise par la **voie A** (console, sans clé) ou la **voie B** (clé déposée) du §*Point de reprise* | demande de Sidy du 2026-09-07 ; [[atelier/rd/infrastructure/cartographie-routing-infrastructure]] §1 et §4.2 ; [[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]] (OUT-07, `bloque` sur cette absence même) ; [[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]] (relevé d'outillage de post-entraînement — critères 5, 6 et 11 ; rien engagé, 2026-09-15) | [[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]] | 2026-09-07 |

## 3. Outillage & scripts (`OUT`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| OUT-02 | Angle mort C3 : `ETANCHEITE_INTERDITE` ne porte que les clés `doctrinal` et `hermeneutique` — un lien `atelier/rd/` → `meta/` n'est **jamais bloquant**, il ne remonte qu'en avertissement C4. **Mesure du 2026-09-18** (signalement H du rapport Publication du 09-16, versé ici sur verdict de Sidy) : **45 fiches sous `atelier/` pointent vers un circuit plus sensible** — **29** artefacts dérivés `index-lexical/` (déjà exemptés du sens des liens par le verdict du 2026-09-15, `atelier/CLAUDE.md`), **1** registre (`monitoring-archive/registre-traitement.md` → `label`), et **15 fiches rédigées ordinaires → `meta/`** (canaux Telegram, accès scope, comptes rendus). Ce sont ces 15 qui sont le sujet, non l'artefact ni le registre | `ouvert` | étendre les clés, ou acter le comportement — **puis seulement** décider des exemptions, sur les 15 fiches mesurées : une dispense écrite avant le contrôle dispenserait de rien et se graverait sans qu'on ait vu ce qu'elle laisse passer | registre des problèmes, entrée `[2026-08-15]` (`reporte`) ; [[atelier/rd/infrastructure/2026-09-18_correctifs-rapports-studio-publication]] | 2026-08-15 |
| OUT-03 | SRS Hermes-native — format, extraction, révision, espacement non définis | `ouvert` | spécifier | [[atelier/rd/outillage/spec-srs-hermes-native]] ; [[atelier/rd/outillage/2026-08-15_piste-srs-assimilation-protocole]] | verdict Sidy du 2026-08-15 |
| OUT-04 | Trois questions d'applicabilité Cordis, non instruites (HMR des agents Hermes en priorité) | `ouvert` | instruire la première | [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]] ; [[atelier/rd/veille/cordis/notes-lecture]] | 2026-08-16 |
| OUT-05 | Contrôle A6 « corps d'entrée orphelin » du vérificateur — proposé, non implémenté ; l'incident append-only du 2026-08-28 (en-tête d'entrée mangé à l'insertion) n'a été vu par aucun contrôle | `ouvert` | implémenter | [[atelier/rd/cahiers/2026-08-28_compte-rendu-premiere-session-integration-qoder]] | 2026-08-28 |
| OUT-06 | Restes de veille Cordis : dépôt source (TS d'origine), identité du contributeur `inso1337`, nature du repo `spatiotemporal-composability-skill` | `ouvert` | scrutation complémentaire | [[atelier/rd/veille/registre]], entrée `[2026-08-18]` | 2026-08-18 |
| OUT-07 | Speculative decoding (Tencent/AngelSpec) — matériau qualifié, **non exploitable sans GPU local** | `bloque` | rouvrir si un chantier d'inférence GPU locale est ouvert ; re-vérifier l'état du repo avant tout engagement | [[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]] | 2026-08-31 |
| OUT-08 | OCR arabe — `tesseract 5 (ara)` sur *Al-Futūḥāt al-Makkiyya* (Maymaniyya) donne un texte structurellement corrompu (DOC-07). À qualifier : autre moteur, prétraitement du scan, ou correction manuelle assistée | `ouvert` | **Critère 1 tranché par Sidy le 2026-09-07 : NON franchi** — « il y a des fautes sur les deux échantillons […] il faudrait systématiquement que je réalise une vérification sur pdf ». Le gain est réel (I1 de 4,72-8,67 % à 1,56-2,97 % selon la page, chaîne `x2 + Otsu`, `--psm 6`) et **insuffisant** : le texte n'est pas citable (Cmd 5). Fait acquis au passage : le modèle en service était `tessdata_fast`, le moins précis des trois, et toute la qualification antérieure avait été menée dessus. Écartés sur mesure : `tessdata_best` (moins bon que le standard), `script/Arabic` (pire, + 89-95 invisibles Cmd 15), redressement (angle nul), 400 dpi. **Ce que le verdict ouvre** : « vérification systématique sur PDF » est la définition d'un *texte de repérage* — usage distinct, relevant de DOC-07, non tranché. **Pistes restantes** : C (ImageMagick) et D (OpenCV) couvertes par le Cmd 13 mais peu prometteuses — elles jouent sur la binarisation quand la corruption tient aux formes de lettres de la lithographie ; le seul candidat crédible serait un moteur entraîné sur la lithographie arabe (Kraken), bloqué par le disque | [[atelier/rd/outillage/out-08-ocr-arabe-futuhat/intent]] ; [[atelier/rd/outillage/out-08-ocr-arabe-futuhat/spec]] ; [[atelier/rd/outillage/out-08-ocr-arabe-futuhat/plan]] | 2026-09-02 |
| OUT-15 | Sampling externe — mandat already present in infrastructure-veille Volet 2, never activated. Premier échantillon : skill `spatiotemporal-composability` (eSaadster) + sandbox pattern `cordis-wasm` (inso1337), réappropriation conceptuelle (license absente SPDX None). Lié à OUT-04 (applicabilité Cordis) et OUT-06 (restes veille). | `ouvert` | rapport Discord Volet 2 → verdict Sidy → session INTEGRATION | [[atelier/rd/outillage/2026-09-05_sampling-fonction-studio-cordis]] ; [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]] | 2026-09-05 |
| OUT-16 | **Cmd 15 sans contrôle** — le commandement d'hygiène Unicode était le seul sans vérification mécanique : `verifier-invariants.py` n'en portait aucune trace, et trois récidives ont suivi en trois semaines (2026-08-22 ZWJ, 2026-09-07 commentaire de code, 2026-09-14 deux fois en une session, dont une par bornes d'intervalle écrites en caractères littéraux). Instrument livré et éprouvé : `verifier-hygiene-unicode.py` balaye la **vue git commitable** — suivis ET non-suivis non-ignorés (pas les seuls `.md` — la troisième récidive était dans un `.py`), codepoints en échappements seuls, autoscan propre. Trois classes rapportées séparément : violations Cmd 15 (bloquantes), enrobage bidi et mise en page (hors Cmd 15, non bloquants) — la frontière du jeu nommé par le commandement ne se franchit pas dans un instrument. Premier balayage sur 1685 fichiers : **22 violations, toutes U+200D**, dans exactement les trois fichiers que le post-scriptum manuel du 2026-08-31 avait déjà relevés et sciemment laissés (2 sauvegardes figées, 1 export de bibliothèque) — l'instrument reproduit mécaniquement cet audit et confirme le résidu inchangé. Plus 220 sauts de page `pdftotext`, tous dans une même conversion. | `en-cours` | **Registre d'exceptions déclarées ouvert le 2026-09-14 sur verdict de Sidy** : `config/hygiene-unicode-exceptions.yaml` porte les 22 résidus tranchés le 2026-08-31, chacun avec motif et renvoi à sa fiche — l'instrument porte un verdict déjà rendu sans en rendre aucun (Cmd 12). Garde-fou éprouvé par l'échec (E7-E10) : une exception couvre un compte **exact**, l'excédent reste bloquant, une exception sans objet est signalée caduque, et `--sans-exceptions` restitue l'état brut — sans quoi une exception absorberait en silence toute contamination ultérieure, qui serait une qualification implicite soustraite au verdict. Le dépôt passe à **0 violation non couverte**. **Les deux points pendants sont tranchés par Sidy le 2026-09-14.** `.bak` : quatre sauvegardes `index`/`annales` prouvées octet pour octet identiques à `git show da8e9b5^:<original>`, donc sans utilité, supprimées par `git rm` (réversible, Cmd 10) ; la cinquième, en `meta/protocole-archives/`, est **conservée et signalée** — elle siège dans l'archive prescrite par le Cmd 10, dont l'utilité est d'être lisible au repos, non d'être irrécupérable. Sauts de page : 220 retirés dans les 23 fichiers du corpus Shinto, 0 accolé — consigné dans l'`index-conversion.md` de la conversion. **Défaut de périmètre relevé et réparé le 2026-09-15** : le périmètre par défaut passait par `git ls-files` nu, qui ne rend que le **suivi** — or le Cmd 15 porte « avant commit », et ce qui s'apprête à être commité est encore non suivi. L'instrument rendait donc « PROPRE » sans avoir ouvert les 36 fichiers du chantier Ghazâlî : un rapport vrai sur un périmètre faux. Corrigé en `--cached --others --exclude-standard`, et **éprouvé par l'échec (E11)** — un non-suivi contaminé doit être vu, un suivi sain ne lève rien, et ce que git ignore (`raw/`, immuable) reste hors périmètre. E11 a été vue refuser sur l'ancien périmètre avant restauration. Balayage après réparation, sur 1730 fichiers : **0 violation non couverte, 0 signalement hors Cmd 15**. **2026-09-15 (soir) — l'instrument devient la porte** : le hook `pre-push` et le CI portaient leur propre copie du contrôle, limitée aux `.md`, et ont laissé passer trois `.py` piégés (12 violations) ; tous deux appellent désormais `verifier-hygiene-unicode.py` (`8fc5165`), éprouvé par l'échec (un `.py` porteur d'U+200B : ancien hook vert, nouveau refusé). Le hook `pre-commit` est aligné le même soir (`b200d95`), éprouvé de même : **les trois portes — commit, push, CI — appellent le même instrument**. | [[atelier/rd/incidents/2026-09-14_amortissement-constat-doctrinal-traduction-ihya]] ; [[atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination]] | 2026-09-14 |

| OUT-17 | **Trois contrôles manquants autour de la file d'écritures de skills** (établis le 2026-09-15). (1) **À l'entrée** : rien ne confronte une proposition au contrat du magasin — sur onze requêtes retenues d'un même lot, cinq étaient inaptes (description > 60 caractères), deux avaient un YAML invalide, une pas de champ `name:`. (2) **En file** : rien ne publie ce qui est retenu — 215 positions ont dormi 38 jours sans qu'aucun rapport le dise. (3) **À la sortie** : rien ne confronte les fichiers qu'un skill déclare à ceux réellement livrés — **six fichiers déclarés jamais livrés sur cinq skills** (quatre réparés par greffe depuis l'archive, deux par retrait de la déclaration, tous trouvés et traités le 2026-09-15). Deux pièces déterministes livrées et **éprouvées par l'échec** (§VII) : `etat-file-skills.py` (état de la file + compte des inaptes) et `verifier-renvois-skills.py` (renvois déclarés vs disque, qui distingue une déclaration d'une citation en exemple). | `en-cours` | introduire la ligne de rapport dans un job périodique : **faite le 2026-09-15** — étape 6 du §2 du job `monitoring-infrastructure-quotidien` (profil `studio`, id `41dc3e7e492c`) ; **suivre** désormais le taux d'inaptes et de renvois morts sur les rapports quotidiens | [[atelier/rd/outillage/out-17-controles-file-et-renvois-skills/intent]] ; [[atelier/rd/outillage/out-17-controles-file-et-renvois-skills/spec]] ; [[atelier/rd/outillage/out-17-controles-file-et-renvois-skills/plan]] | 2026-09-15 |

| OUT-18 | **L'organe de vérification était réputé éprouvé en bloc, alors qu'une seule de ses entrées l'avait été** — l'outil MCP `carte_du_depot` construit ses arguments avec `--json` (`wiki_mcp_server.py` l. 246-248) que `carte-du-depot.py` n'a jamais accepté : l'outil ne peut pas fonctionner, quel que soit l'appel, quand `verifier_invariants` rend son JSON sans défaut | `ouvert` | éprouver **une par une** les entrées du serveur MCP (chacune appelée pour de vrai, avec son refus observé sur faute fabriquée, §VII) ; le correctif de `carte_du_depot` (retrait de `--json`) **appliqué le 2026-09-15** sur consigne de Sidy — refus reproduit avant (`unrecognized arguments: --json`, code 2), appel réel après (`ok`, code 0) ; état d'avant conservé hors dépôt, trace dans [[atelier/rd/infrastructure/2026-09-15_execution-propositions-rapport-studio]]. Reste l'épreuve de refus entrée par entrée — le serveur vit hors dépôt et n'est pas versionné | registre des problèmes, entrée `[2026-09-15]` | 2026-09-15 |

| OUT-19 | **`infra_verif` ne sait pas vérifier une entrée `mcp_servers`** — l'affirmation « trois profils portent le serveur Ansari » (fiche `2026-09-15_integration-mcp-ansari`) n'est vérifiable qu'à la main, exactement le défaut que le champ `infra_verif` a été ouvert pour combler (§VII). Étendre `verifier-coherence-infrastructure.py` à une clé `mcp_servers` (profil → nom de serveur attendu dans `config.yaml`) | `ouvert` | triptyque à rédiger et viser (Cmd 6) ; aucun code avant visa ; épreuve par l'échec exigée (§VII) | rapport Studio du 2026-09-15, P5 (i) ; [[atelier/rd/infrastructure/2026-09-15_integration-mcp-ansari]] ; [[atelier/rd/infrastructure/2026-09-15_execution-propositions-rapport-studio]] | 2026-09-15 |
| OUT-20 | **Le wikilink court n'est gardé par rien** — la forme `[[slug]]` est admise par le §IV racine depuis le verdict du 2026-09-18 et repose tout entière sur l'unicité du basename dans le dépôt, qu'aucun contrôle ne vérifie ; mesure du jour : **589 occurrences dans 156 fiches, 0 ambiguïté** — mais une collision future changerait la cible d'un renvoi **silencieusement**, dans une fiche que personne n'édite | `attente-verdict` | deux verdicts avant tout code (sévérité : refus sec ou avertissement conditionnel ; périmètre : `textes/` et `protocoles/` inclus ou non), puis écriture de **B9** et épreuve par l'échec (§VII) — triptyque rédigé, `plan.md` en `brouillon` | [[atelier/rd/outillage/out-20-unicite-des-basenames/intent]] ; [[atelier/rd/outillage/out-20-unicite-des-basenames/spec]] ; [[atelier/rd/outillage/out-20-unicite-des-basenames/plan]] | 2026-09-18 |

## 4. Bibliothèque (`BIB`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| BIB-01 | Appendices non photographiés — aucune fiche possible en l'état | `bloque` | nouvelle prise de vue (geste humain) | [[atelier/rd/bibliotheque/catalogue-bibliotheque]] | 2026-08-22 |
| BIB-02 | *Symboles de la Science sacrée* : couverture d'index à 100 %, mais chapitres non traités en fiches au-delà des XVIII et XXXVII | `ouvert` | choisir les chapitres suivants | même catalogue | 2026-08-22 |
| BIB-04 | **Dépouillement du lexique coranique de Gloton** (*Une approche du Coran par la grammaire et le lexique*, section A, pp. 233-782) à partir des photographies de l'exemplaire physique. La moisson retient pour chaque bloc-racine la **case 4 — les traductions de la racine** : une adresse de lexique n'instruit rien, un sens instruit (verdict Sidy du 2026-09-16). **Moisson close le 2026-09-16 sur le matériau photographié : 169 racines, 107 planches lues sur 107** (`edccb13`). **Treize discontinuités** subsistent dans la numérotation ; chacune est vérifiée correspondre à des pages **non photographiées** (contrôle par la page bornant chaque écart, sortie brute au journal §2), aucune à un bloc-racine omis. **Verdict Sidy du 2026-09-16 : le reste du lexique sera photographié plus tard, au gré des opportunités.** Le chantier n'est donc ni clos ni bloqué — il reprend à chaque nouvelle prise de vue, par passes d'ajout strict, sans qu'aucune campagne soit à programmer. **Deux points restent réservés au verdict** : (1) `glossaire-unifie.md` est **périmé et non vide** (le générateur rend 1850 termes, 6 ouvrages) et n'a jamais été régénéré depuis le 2026-08-22 — **[Cmd 10, correction du 2026-09-16 : cette inscription est FAUSSE quant à ce qui existe sur disque. Mesuré ce jour : `glossaire-unifie.md` fait **33 lignes et porte ZÉRO terme** ; « 1850 termes, 6 ouvrages » décrit ce que le générateur *rendrait*, non ce qui est là. Cause mesurée : le générateur sélectionne sur le préfixe de nom `index-`, le validateur sur le champ `type: index-livre` — 5 des 6 fiches `index-*` portent `type: ressource`. La ligne fautive est maintenue et non effacée ; le verdict sur la caducité reste entier.]** ; (2) `generer-glossaire-unifie.py` sélectionne sur le **préfixe de nom de fichier** (`index-`) quand `valider-index-livres.py` borne au **champ** `type: index-livre` — 6 fiches `index-*`, 1 seule de ce type | `attente-verdict` | à l'arrivée de nouvelles photographies : `extraire-bandeaux-racines-gloton.py` puis passe d'ajout strict au TSV (procédure complète au journal §3, mode `--recadrer` compris). Sans photographies nouvelles, rien à exécuter : la dépose en fiche `type: index-livre`, la régénération de l'artefact dérivé et l'alignement des deux scripts attendent les deux arbitrages ci-dessus | [[atelier/rd/outillage/index-lexical/2026-09-16_gloton-moisson-racines-journal]] ; `moisson-racines-gloton.tsv` ; [[atelier/rd/bibliotheque/catalogue-bibliotheque]] ; [[atelier/rd/bibliotheque/2026-09-16_trois-organes-lexicaux-et-lisan-al-arab]] | 2026-09-16 |
| BIB-05 | **Adressabilité par racine du *Lisān al-ʿArab*.** Le *Lisān* se range **par dernière radicale, puis première, puis seconde** (arrangement d'al-Ṣiḥāḥ) : retrouver une racine à la main dans 8 116 pages est le geste coûteux qui borne le chantier lexical — ce n'est pas le matériau qui manque, c'est l'accès. Objet : un index mécanique `racine → (volume, page)` construit sur le texte versé (`raw/lisan-al-arab/`, témoin A, 8 116 pages, empreintes à `PROVENANCE.md`). **Sa valeur se mesure** : combien des racines déjà moissonnées deviennent adressables. **Assiette mesurée le 2026-09-17 : 169 racines** au TSV Gloton (`edccb13`, 107/107 planches) — **la pièce de sas annonçait 97, chiffre non retenu** : l'écart n'a pas été instruit, la mesure au fichier fait foi (Cmd 10, même faute que celle corrigée à BIB-04 le 2026-09-16). Ligne **ouverte en recensement seulement** : **aucun code n'est écrit**, le triptyque `intent`/`spec`/`plan` reste à rédiger et le `plan.md` visé *sera* le plan du Cmd 6 | `ouvert` | rédiger le triptyque `atelier/rd/bibliotheque/bib-05-adressabilite-racine-lisan/` et le soumettre au visa. Rien à exécuter avant | [[atelier/rd/bibliotheque/2026-09-16_trois-organes-lexicaux-et-lisan-al-arab]] ; [[doctrinal/sources/lisan-al-arab]] ; `atelier/rd/outillage/extraire-lisan-shamela.py` | 2026-09-17 |

## 5. Études de cas (`CAS`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| CAS-01 | Zellige de la Grande Mosquée — aucune donnée de proportion mesurée : la photographie de terrain n'est pas redressée | `bloque` | reprise du terrain dans de meilleures conditions | [[atelier/etudes-de-cas/zellige-grande-mosquee-paris]] §0 | 2026-08-24 |
| CAS-02 | Quadrivium et Épître 6 des Ikhwān al-Ṣafāʾ (proportions arithmétique/géométrique/harmonique) — point d'entrée signalé, chantier non ouvert | `ouvert` | ouvrir, ou classer | même fiche | 2026-08-24 |

## 6. Process & protocole (`PRO`)

| ID | Chantier | Statut | Prochaine action | Fiche d'origine | Ouvert par |
|---|---|---|---|---|---|
| PRO-03 | Types de fiche en usage mais absents du Sceau de `atelier/CLAUDE.md` : `registre` (`rd/veille/registre.md`, le présent fichier), `fiche-rd`, `session` | `ouvert` | régulariser le Sceau, ou aligner les fiches | relevé de la passe du 2026-09-01 | 2026-09-01 |
| PRO-04 | Quatre fichiers `.bak-2026-08-18-pre-C4` suivis par git, référencés nulle part (`atelier/`, `atelier/rd/`, `doctrinal/` ×2) | `attente-verdict` | `deprecated` avec pointeur, ou retrait assumé (Cmd 10) | relevé de la passe du 2026-09-01 | 2026-09-01 |
| PRO-05 | Rétroportage du champ `maturite` sur les fiches `discernement/` — **9 sur 56** le portent ; différé assumé, non borné | `ouvert` | les agents le renseignent au fil de leurs éditions de fond ; le différé n'a pas d'échéance | proposition du 2026-08-27 (cf. Domaine Réservé) | 2026-08-27 |
| PRO-06 | File d'idées pour les agents : dispositif validé le 2026-08-27, **encore vide** — jamais éprouvé en usage réel | `ouvert` | y verser une première idée | `queue-idees.md` (cf. Domaine Réservé) | 2026-08-27 |
| PRO-07 | Nature de `04-sessions-par-fonction-et-backlogs` : cesser d'être un backlog vivant pour devenir mode de travail + aiguillage | `attente-verdict` | refonte documentaire — décision de Sidy | relevé de la passe du 2026-09-01 | 2026-09-01 |
| PRO-09 | **Étanchéité et matériau expérientiel** — les règles §VI, §VII.2 et §VII.3 supposent toutes une origine **extérieure au déposant** (texte reçu, ouvrage, conversation). Le cas où la source est **Sidy lui-même** n'a pas de forme prévue : son vécu est soit exilé en `meta/` hors du champ du discernement, soit obligé de se dire en langue doctrinale. Mesuré sur le lot du **2026-06-20** (45 fiches à provenance conversationnelle, 32 `sources:` vides, 2 `to-source` sur 45) et sur deux fiches portant des éléments personnels nommés en circuit neutre (S4/S5, pointées non reproduites). **Cinq propositions journalisées — aucune appliquée** : P1 fiche de provenance du corpus ; P2 champ `materiau:` au Sceau ; P3 éclatement érigé en défaut ; P4 registre de l'**attestation** (trois sols : sourcé / sans source / attesté) ; P5 recevoir la contrainte comme qabḍ, non comme khawf | `attente-verdict` | reprise quand Sidy aura le temps — arbitrer les questions Q1-Q5 de la fiche. **En attendant, l'a priori du 2026-09-13 tient** : « d'a priori et instruire les fiches » ; S4/S5 non touchées | [[atelier/rd/cahiers/2026-09-13_etancheite-materiau-experientiel]] | 2026-09-13 |

## 7. Doctrinal (`DOC`)

> **Ce tableau recense, il n'instruit ni ne hiérarchise.** Aucune priorité n'est proposée
> sur les lignes doctrinales : l'ordre d'instruction et le verdict appartiennent au
> circuit `doctrinal/` et à Sidy (Cmd 12/13). **Source vivante : `doctrinal/index.md`,
> §VII — Le Registre du Discernement.** Le renvoi ci-dessous est un lien
> `atelier/rd/` → `doctrinal/`, **sens unique, signalé** (§VI du protocole racine) ;
> aucune page doctrinale ne mentionne jamais le présent registre.

| ID | Chantier | Statut | Où il est instruit |
|---|---|---|---|
| DOC-01 | **37 fiches de discernement au statut `speculatif`** sur 56 — verdict en attente. Le décompte est mécanique (`grep '^status:' doctrinal/discernement/*.md`, 2026-09-01) et n'est pas recopié en liste ici : il périmerait aussitôt | `attente-verdict` | [[doctrinal/index]] §VII |
| DOC-02 | Ingests annoncés et non faits : amorce `modes-du-souffle` (items 39-50, Gloton p. 41) ; récit eschatologique complet du ch. 198 ; fiche symbole `lune-noire` ; enrichissement de `ilm-al-nujum` (tables signes/planètes/dignités/maisons) | `ouvert` | poste INGEST ; liste tenue au Domaine Réservé (`04-…`, §E) |
| DOC-03 | Sources primaires à localiser : *ʿUqlat al-mustawfiz*, *Kitāb al-Inshāʾ al-Dawāʾir*, Meftah *Arma Artis* | `ouvert` | discipline des sources, §VII du protocole racine |
| DOC-04 | Citations attribuées non vérifiées (Ibn ʿArabī, al-Ghazālī, le Cheikh) marquées `to-source` — cas le plus net signalé : `symboles/chercheur-manifestant-akbarien` | `ouvert` | levée par vérification primaire humaine, jamais par le modèle |
| DOC-05 | Réserve résiduelle : lien explicite *wirātha* ↔ *aqtāb* non localisé dans le *Futūḥāt* ch. 36 — l'ancrage (c) de l'Instrument en dépend | `ouvert` | [[doctrinal/index]] §VII ; conséquence instrumentale en INS-11 |
| DOC-06 | **Ingest des deux Tilak** — *The Arctic Home in the Vedas* (1903) et *The Orion* (1893). La matière était déjà CONSOMMÉE par la donnée de l'Instrument (états du soleil, aurores) sans qu'aucune page doctrinale ne la porte — c'est le défaut corrigé | `en-cours` | ingest fait le 2026-09-02 (5 fiches, commit `47b03c5`), **rouvert le même jour** pour une 6ᵉ fiche sur le chapitre XIII (verdict Sidy, exclusion pure remplacée par catalogage averti) ; sas vidé des reliquats (plan exécuté + doublons OCR bruts) | [[doctrinal/sources/tilak-origine-polaire-tradition-vedique]] ; [[doctrinal/sources/tilak-culture-aryenne-primitive-ch13]] ; [[doctrinal/sources/guenon-atlantide-hyperboree]] (note 3) | — | 2026-09-02 |
| DOC-07 | **Osman Yahia, catalogue critique de l'œuvre d'Ibn ʿArabī (1964)** — versé. La **Futūḥāt al-Makkiyya, éd. Maymaniyya t. 1** (texte arabe original, `traditionnel`) est ajournée : OCR jugé structurellement corrompu, pas seulement dégradé — aucune fiche, aucune citation possible en l'état (Cmd 5) | `en-cours` | Osman Yahia notice + `textes/` faits le 2026-09-02 ; Futūḥāt renvoyée à **OUT-08** (nouvel essai d'OCR avant toute décision de versement), fichier au sas conservé sur demande de Sidy | [[doctrinal/sources/osman-yahia-histoire-classification-1964]] | — | 2026-09-02 |
| DOC-08 | **Exotérisme et ésotérisme dans l'attribution de `status`** — le verdict du 2026-09-06 sur quatre autorités a mis au jour un défaut de catégorie : `academique` était traité comme le résiduel de `traditionnel`, alors qu'il nomme une allégeance hors de la tradition. Sidy indique que la matière est « encore plus subtil que ça » et réserve le retour | `attente-verdict` | `[[atelier/rd/cahiers/2026-09-06_doc-08-exoterique-esoterique-statut]]` — trois registres tenus séparés (établi / lecture provisoire de la machine / réservé). Prochaine action proposée, **non faite, en attente de visa** : fiche `doctrinal/discernement/` |

| DOC-09 | **Chantier de réminiscence autour du kamon Kouyaté** — *retrouver avant de créer* : chercher une forme héraldique plausible plutôt que d'en inventer une. Dossier A (**mémoire familiale**, traditions rapportées) recueilli au **Domaine Réservé** ; dossier B (grammaire des *mon*) déjà porté par le glossaire ; **dossier C (confrontation) NON ouvert** — aucune piste de motif n'est privilégiée tant que le dossier A n'est pas constitué, et toute correspondance inter-traditions exigerait une fiche `discernement` (Cmd 3) | `ouvert` | [[doctrinal/etudes/2026-09-08_kamon-glossaire-systematique]] — dossier B, matériel factuel `to-source` (aucun ouvrage japonais ni héraldique au dépôt) ; [[doctrinal/discernement/2026-09-08_kamon-symbolisme-traditionnel-ou-convention-heraldique]] (`speculatif`, verdict réservé) ; cadre, mémoire et méthode au Domaine Réservé (non lié depuis ce circuit — sens interdit) |

## 8. À vérifier — non asserté ouvert

Ce qui n'a pas pu être confronté au disque dans la passe du 2026-09-01. **Rien ici n'est
présenté comme un chantier ouvert** ; l'inscription au registre attend la vérification.

- Suites proposées de [[atelier/rd/instrument/2026-08-29_mise-en-regard-majma-al-bahrayn-registres]] §7
  (« par ordre de maturité ») — non dépouillées.
- [[atelier/rd/outillage/2026-08-13_tour-horizon-corpus-guenon-deblocages]] — tour d'horizon de
  déblocages, statut de chacun non confronté.
- [[atelier/rd/outillage/2026-08-29_mise-en-regard-tenon-mortaise-axe-instrument]] — piste
  probablement liée à INS-02, articulation non établie.
- [[atelier/rd/outillage/spec-generer-cartographie-tolerant]] — le mode tolérant est-il implémenté
  depuis la régénération du 2026-08-31 ?
- Réserves méthodologiques des quatre fiches de phase corpus des études de cas
  (forteresses, dougong, refroidissement passif, Xuankong) — mentions non dépouillées.
- Deux entrées du registre des problèmes rouvrant le même point (Phase 3 veille, deux entrées
  `ouvert` le même jour) : bouclage possible, non confirmé.

## 9. Chantiers clos ou caducs (jamais supprimés — Cmd 10)

| ID | Chantier | Issue | Établi par |
|---|---|---|---|
| OUT-C1 | `graphe-cartographie.json` jamais régénéré, et 10 anomalies bloquantes | **caduc au 2026-08-31** : le graphe a été régénéré (commit `a25e482`) et le pôle intégré au protocole racine §VII. L'entrée du registre des problèmes qui l'affiche encore `ouvert` n'a jamais reçu d'entrée de clôture — c'est le comportement normal d'un cahier append-only, pas une anomalie | vérifié au disque et par `git log`, 2026-09-01 |
| INF-C1 | Crise de crédit API du 2026-08-07 — « tous les agents restent inactifs jusqu'à résolution » | **caduc au 2026-09-01** : sortie de crise par changement de fournisseur d'inférence (bascule OmniRoute du 2026-08-26), non par nouvelle clé. Les agents tournent en continu | [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] ; commits `CHOURA: tour <agent>` du 2026-08-28 au 2026-09-01 |
| PRO-C1 | `hermeneutique/annales.md` — `updated:` antérieur à sa dernière entrée | **clos le 2026-09-01** : corrigé dans la passe d'organisation. Seule erreur réelle que le vérificateur signalait, noyée dans 209 lignes de bruit (motif de OUT-01) | passe du 2026-09-01 |
| OUT-C2 | Périmètre de `verifier-invariants.py` : le script parcourait le disque sans consulter `.gitignore` — 209 des 210 erreurs étaient du bruit de venv tiers, de sorties régénérables et du sas `raw/`, et ce bruit avait masqué la seule erreur vraie du jour | **clos le 2026-09-01** sur verdict de Sidy. Le script interroge désormais git (`ls-files --others --ignored --exclude-standard`) et ne contrôle que ce qui appartient au dépôt ; le périmètre appliqué est annoncé en tête de sortie, jamais silencieux ; `--tout` restitue le comportement antérieur, donc rien n'est hors de portée. Repli sur l'exclusion des dossiers cachés hors dépôt git (bacs à sable). Le dépôt passe de 210 erreurs à **0 erreur, 0 avertissement** sur 709 fiches. `generer-cartographie.py` portait le même défaut (112 anomalies venues du même venv, refus d'écrire le manifeste) — corrigé de même, le graphe se régénère | `verifier-invariants.py` ; guide de déploiement (cf. Domaine Réservé) ; entrée `[2026-09-01]` du registre des problèmes |
| PRO-C2 | Cinq fiches à la racine de `atelier/rd/`, hors arborescence et sans lien entrant ; trois portaient du fait personnel en page neutre (§VI) | **clos le 2026-09-01** sur verdict de Sidy. Les trois fiches versées au Domaine Réservé avec leur historique git ; les deux neutres classées par leur nature (`infrastructure/`, `cahiers/`) ; la racine du pôle ne porte plus que `index.md` et le présent registre. Deux fiches restées côté `rd/` portaient le même défaut **dans leur corps** — blocs retirés, matière conservée au Domaine Réservé. Contreparties neutres écrites et indexées : déploiement de la veille quotidienne, inventaire de l'outillage ; pour la troisième, la contrepartie existait déjà (Cmd 4, pas de quatrième fiche) | passe du 2026-09-01 ; [[atelier/rd/index]] §Assainissement |
| PRO-C3 | Protection de la branche `main` contournable sans review | **clos le 2026-09-01** sur verdict de Sidy. Le fait s'est révélé plus net que la ligne ne le disait : la protection exigeait un contrôle `lint` qui **ne validait rien** — il parcourait un dossier `wiki/` et des sous-dossiers de l'arborescence plate abandonnée le 2026-06-11, tous inexistants, et imprimait « Frontmatter OK » sur zéro fichier. Le workflow exécute désormais `verifier-invariants.py` et l'hygiène Unicode, en bloquant ; vérifié qu'il **peut échouer** (clé de Sceau absente, ZWJ), le CI inspecte 709 fiches. `enforce_admins` reste à `false`, **acté et non subi** : le durcir imposerait un flux par pull request aux treize acteurs qui poussent en direct. Contrepartie : hook `pre-push` versionné qui exécute les mêmes contrôles avant que la faute quitte la machine | `.github/workflows/lint-and-validate.yml` ; [[atelier/rd/outillage/hooks/README]] ; entrée `[2026-09-01]` du registre des problèmes |
| PRO-08 | 708 fichiers Markdown invisibles dans `raw/` — le poste CONSULTATION aveugle sur la matière que les fiches citent en source | **clos le 2026-09-02** sur les trois verdicts de Sidy — « `textes/` validé, dédoublonne avant migration, et amende le §II ». Les deux motifs de l'exclusion de `raw/` avaient **n'avaient jamais été vérifiés** : mesurés, ils tombent pour le texte (14 Mo contre 2,6 Go ; **zéro** adresse, IBAN ou téléphone sur 708 fichiers) et tiennent pleinement pour les binaires (factures nominatives, export ChatGPT). D'où la ligne de coupe : **le format, non le contenu**. 560 fichiers migrés, 147 doublons écartés, 1 hors corpus, 0 refus. `raw/` **intact** — copie, jamais déplacement (Cmd 10). Un faux positif consigné en chemin : « IBAN » détecté dans *Le Roi du Monde* était **« Liban »**, motif resserré sur bornes de mot avant de conclure. Exemption B0 **ciblée** et éprouvée dans les deux sens : acceptée dans `textes/`, toujours levée ailleurs. ⚠ Reste ouvert, non tranché : le **régime des futurs** textes convertis | `atelier/rd/outillage/migrer-textes-convertis.py` (6 gardes éprouvées) ; `verifier-invariants.py` 0 erreur sur 560 fichiers sans Sceau ; `CLAUDE.md` §II + `meta/protocole-archives/changelog-CLAUDE.md` ; [[atelier/rd/infrastructure/pro-08-textes-convertis-versionnes/plan]] |
| INF-14 | Hébergement du rendu de l'Instrument sur `sidyvision.com` — un dépôt n'est pas une diffusion | **clos le 2026-09-01**, mis en production après validation explicite de Sidy dans la session (Action PUBLICATION, point 4). Le rendu est servi sur `https://sidyvision.com/instrument/`. Trois obstacles levés en chemin, chacun établi par mesure et non déduit : le site n'avait **aucune source versionnée** (déploiement manuel, capture de sauvegarde prise avant tout accès) ; le premier jeton ouvrait un compte **créé le jour même et vide** — le site était détenu par un autre compte ; le montage par proxy est tombé sur le **401 *edge-access*** dont Netlify frappe les `*.netlify.app` des comptes gratuits récents. Montage final : déploiement direct par l'API, page d'accueil et rendu dans le même site — ni proxy, ni build, ni liaison GitHub, ni secret chez un tiers. Les six critères contrôlés en ligne, le premier d'abord : page d'accueil **octet pour octet identique** à la capture. **Second temps le même jour** — Sidy demande la mise à jour automatique : elle est en place, non par liaison Netlify (qui aurait publié la racine du dépôt et **écrasé la page d'accueil**, outre l'OAuth par navigateur) mais par **GitHub Action** dans le dépôt frère, rejouant la même API et le même garde-fou d'empreinte. Éprouvée de bout en bout par `workflow_dispatch` : garde-fou vert, publication faite, et triple contrôle en ligne — page d'accueil intacte, rendu identique au dépôt, manifeste servi à 46 nœuds. **Troisième temps** : `enforce_admins` aligné sur la doctrine du wiki (`false` + garde-fou local, PRO-01), la **porte humaine déplacée dans le `pre-push`** (`PUBLIER=1` exigé pour toute poussée de `src/` sur `main`, puisqu'elle publie en production) — et, au passage, découverte que les deux hooks portaient un motif `grep` qui **ne correspondait jamais** : la faute même de PRO-01, reproduite dans du code neuf, corrigée et éprouvée dans les deux sens | [[atelier/rd/infrastructure/inf-14-hebergement-rendu-sidyvision/plan]] ; `atelier/rd/outillage/publier-instrument-netlify.sh` ; `.github/workflows/publier.yml` du dépôt frère (PR #1) ; capture de référence SHA-1 `6814d7f4…3334` |
| INF-15 | `monitoring-archive-charte.md` n'archivait que le job Studio (`41dc3e7e492c`) — le rapport quotidien Publication (`veille-referencement-investigation-08`) n'avait aucune trace au dépôt | **clos le 2026-09-10** : étendu au profil `publication` — job `archiver-veille-publication` (id `d3176b389ed8`, cron `10 11 * * *`), mêmes script et rétention (40 j), 13 sorties historiques rétroactivement archivées, charte mise à jour. **Versé en §9 le 2026-09-13** : la ligne portait en §2 un statut `**clos 2026-09-10**` hors vocabulaire (correctif C4) | [[atelier/rd/cahiers/registre-problemes]] entrée `[2026-09-02]` §3 ; [[atelier/rd/infrastructure/monitoring-archive-charte]] |
| INF-17 | Migration du fournisseur d'inférence des jobs cron — bascule vers DeepSeek et pose du pin (`model`, `provider`, `reasoning_effort`) ; documentée au journal des optimisations, sans ligne de chantier jusqu'ici | **clos le 2026-09-11** : migration effective, vérifiée le 2026-09-13 — `model = deepseek-flash`, `provider = deepseek`, `reasoning_effort = high`, `failure_streak = 0`, deux exécutions réussies (09-12 et 09-13). La migration a produit **trois jours de panne du rapport Studio** (09-10 → 09-12) : ce n'est pas une optimisation ordinaire, et un fait d'infrastructure de cette portée ne reste pas sans identifiant. **Ouverte le 2026-09-13 sur verdict de Sidy** — le rapport proposait la ligne ou la convention inverse ; elle est versée ici, close, sans feindre un chantier ouvert | [[atelier/rd/cahiers/journal-optimisations]] entrée `[2026-09-11]` ; rapport Studio du 2026-09-13 §3.4 ; [[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]] |
| BIB-03 | Deux ouvrages de Tilak scannés (`raw/`) convertis en Markdown par OCR : *The Orion* (1893, 237 p.) et *The Arctic Home in the Vedas* (1903, 544 p.) | **Clos.** Le versement a eu lieu le **2026-09-02** au commit `d5a52d0` (« PRO-08 clos : `textes/` ouvert ») : les deux conversions sont dans `textes/tilak-the-orion-1893/` et `textes/tilak-the-arctic-home-in-the-vedas-1903/`, chacune portant son `index-conversion.md`. **Pointeur mort corrigé le 2026-09-17 (Cmd 10)** : la ligne pointait encore vers le sas `_inbox/conversions/`, chemin **jamais suivi par git** (`git log --all` vide) et vidé depuis. La mention d'origine est conservée ici, non effacée. Le « non relue » n'est pas un reste de chantier : c'est une **propriété permanente de l'artefact**, déclarée par les `index-conversion.md` eux-mêmes. Pointeurs restants vérifiés résolvants : [[atelier/rd/outillage/spec-ocr-scan-vers-markdown]], [[doctrinal/sources/transcription-index-tilak-origine-polaire]] | **Verdict de Sidy du 2026-09-17** — « le chantier a été fermé il y a bien longtemps maintenant ». La clôture **date du 2026-09-02** (le versement) ; le 2026-09-17 est la date du verdict qui la constate, non celle du fait. |

---

## Points ouverts soumis à Sidy

Aucun n'est tranché par la machine (Cmd 12/13).

1. **Revue périodique** — désigner l'agent qui tient ce registre à jour hors des passes
   d'intégration. Candidat naturel : le Studio Sound Engineer, qui porte déjà le cron de
   monitoring et le mandat de veille infrastructure. C'est une décision engageante.
2. **OUT-01** — périmètre du vérificateur d'invariants. Priorité haute : le bruit masque
   les erreurs réelles, le cas s'est déjà produit.
3. **PRO-02** — sort des trois fiches à fait personnel logées en page neutre.
4. **PRO-04** — sort des quatre `.bak` suivis par git.
5. **PRO-07** — refonte de la nature du document de backlogs du Domaine Réservé.
6. **Vocabulaire du champ `statut:`** des propositions : aucun n'est établi au dépôt, et
   la seule occurrence existante est précisément celle qui était fausse. L'arrêter relève
   de Sidy ; en attendant, l'état réel de chaque proposition est porté en encart daté dans
   son corps.
7. **Régime d'un artefact dérivé porteur de corpus** (rapport Studio du 2026-09-15, P5 (ii)) —
   un adaptateur de poids entraîné sur le corpus du dépôt *contient* du corpus, vit hors du
   dépôt et n'entre dans aucune des cinq cloisons (§VI). À nommer avant qu'une machine
   existe (INF-16), sinon l'usage tranchera à la place du verdict.
