---
title: "Passation — session claude.ai (Instrument + dossier khafḍ/rafʿ) vers session terminal"
date: 2026-08-30
type: brief
status: transmis
destinataires: [sidy, session-terminal]
created: 2026-08-30
updated: 2026-08-30
references:
  - doctrinal/discernement/2026-08-30_chute-realisation-deux-aspects-de-qaf.md
  - doctrinal/discernement/2026-08-30_gens-de-al-araf-et-les-inities.md
  - doctrinal/discernement/2026-08-30_khafd-raf-couple-operatoire-des-degres.md
  - doctrinal/sources/razi-noms-divins-ch18-khafid-rafi.md
  - doctrinal/sources/gloton-approche-coran-grammaire-lexique.md
  - doctrinal/symboles/table-28-degres-nafas-rahman.md
  - atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable.md
  - atelier/rd/instrument/instrument-prototype.html
---

# Passation — de la session claude.ai à la session terminal

> **Ce document est le point de reprise.** Il ne résume pas la session — les annales
> le font — il dit **où en est chaque chantier, ce qui l'attend, et par quoi
> commencer**.

## 0. ⚠️ État des branches — à lire avant tout

### ✅ Fusion faite le 2026-08-30, sur ordre de Sidy (« Fusionne les branches »)

`claude/passation-instrument-claude-ai-kono6l` → **`main`**, via la PR **#18**
(fast-forward strict : 14 commits d'avance, 0 de retard). `main` est désormais à
**`657d79a`**. Le push direct sur `main` étant bloqué pour les sessions d'agent
(comportement voulu, cf. `registre-problemes` [2026-08-29]), la voie PR + merge API
a été employée — la même que le 2026-08-29.

```bash
cd /root/wiki
git fetch origin
git checkout main && git pull origin main
python3 verifier-invariants.py --racine /root/wiki    # attendu : 0 erreur(s), 0 avertissement(s)
```

### 🛑 PIÈGE — le dépôt porte DEUX lignées sans ancêtre commun

Découvert en préparant la fusion. **`git merge-base` renvoie « aucune base
commune »** entre `origin/main` et trois références :

| Référence | Diff **de contenu** avec `main` | Verdict |
|---|---|---|
| `claude/instrument-graphic-design-n5d0ic` | 265 fichiers, **−26 172 lignes** | ⛔ **NE PAS FUSIONNER** |
| `claude/shayegan-transcription-archivage-qt2815` | 185 fichiers, **−17 103 lignes** | ⛔ **NE PAS FUSIONNER** |
| le `main` **local** de la session web | idem (même lignée) | artefact |

Ces branches ne sont pas « en avance » : elles portent un **état ancien et plus
petit** du dépôt, antérieur à une réécriture d'historique. Les compteurs de commits
(387 et 66 « d'avance ») **mentent** — ils comparent des lignées disjointes. Les
fusionner **retirerait des dizaines de milliers de lignes** du wiki actuel.

> ⚠️ **Erreur de méthode commise puis corrigée, à connaître** : un premier test
> avec `git diff origin/main...origin/<branche>` (**trois points**) a rendu un
> résultat **vide**, que j'ai d'abord lu comme « contenu déjà intégré ». C'était
> faux : le diff à trois points **échoue silencieusement** (`no merge base`) quand
> les histoires sont disjointes. **Sur ce dépôt, toujours comparer à deux points**
> (`git diff origin/main origin/<branche>`).

**À vérifier côté serveur** : si `/root/wiki` porte lui aussi un `main` local de
l'ancienne lignée, `git pull origin main` échouera (« refusing to merge unrelated
histories »). Le remède est local et sans perte, l'ancienne lignée restant sur
`origin/claude/shayegan-transcription-archivage-qt2815` :

```bash
git fetch origin && git checkout -B main origin/main
```

### ⚠️ `fix/corrections-rapports-2026-08-30` — NON fusionnée, décision à Sidy

Seule branche à porter du contenu réel dans la lignée de `main` (1 commit). **Mais** :

- **son correctif de sécurité est déjà dans `main`** — le secret HMAC exposé en
  clair y est déjà caviardé, arrivé par une autre voie ;
- **ce qui reste est, pour l'essentiel, la suppression de 39 marqueurs
  `to-source`** (39 lignes `- to-source` retirées, plus deux `sources: []`). C'est
  une **décision de doctrine, pas de forme** : le `to-source` est le signal du
  Cmd 5. En retirer 39 d'un coup efface 39 signalements en cours ;
- elle **conflicte** sur trois fichiers (`registre-problemes.md` — append-only, les
  deux lignées ayant inséré en tête —, `doctrinal/autorites/ibn-sina.md`,
  `doctrinal/etudes/2026-06-04_islam-et-ia.md`).

**Non fusionnée délibérément** (VIGILANCE : « rapporter sans corriger d'office » ;
Cmd 13). L'intention probable de la branche était de réparer une incohérence
`sources: ["to-source"]` / `sources_count: 0` — mais il y a **deux réparations
possibles** (vider la liste, ou porter le compte à 1) et elles n'ont pas le même
sens. **Verdict à Sidy.**

## 1. Ce qui a été fait (résumé de contrôle, non de narration)

| Chantier | État |
|---|---|
| **Report des six trouvailles au prototype** (tâche du brief précédent) | ✅ **fait** — sept stations de navigation, `instrument-prototype.html`, vérifié au navigateur |
| **Degrés 1-10 du *Nafas*** (`to-source` depuis juillet) | ✅ **levé** — collation de la p. 35 de Gloton |
| **Apparat éditorial des deux ouvrages Albouraq** | ✅ **établi** sur clichés de couverture |
| **Dossier *khafḍ* / *rafʿ*** | 🔍 **ouvert**, 3 fiches de discernement, aucun verdict |

## 2. ⚡ Ce qui attend un verdict de Sidy — par ordre d'importance

### (1) La thèse d'unification — c'est le sommet du dossier

`doctrinal/discernement/2026-08-30_chute-realisation-deux-aspects-de-qaf.md`

Intuition de Sidy : le thème du dossier est **la chute hors du Paradis, la
réalisation spirituelle, et les deux aspects de Qâf (muraille / apex) rapportés à
l'état primordial**. Son pivot est **déjà sourcé au dépôt** : Guénon donne la
restauration de l'état primordial comme « **première étape essentielle** de la
réalisation » (*Aperçus sur l'Initiation*).

**Ce qu'elle ajoute à l'acquis** : la fiche close de juillet établit la **double
nature** de Qâf, jamais le **sens de parcours** entre ses deux aspects. C'est
l'apport net, et il est non tranché.

**Trois questions posées à Sidy.** La première d'abord : *« chute » est-il le terme
retenu, malgré la charge chrétienne (péché originel) que le mot importe et que le
* hubūṭ* coranique ne porte pas ?*

### (2) Les gens d'al-Aʿrāf sont-ils les initiés ?

`doctrinal/discernement/2026-08-30_gens-de-al-araf-et-les-inities.md`

Intuition **ancienne** de Sidy, antérieure au dossier et indépendante de lui —
consigné comme tel. Appui le plus fort : leur acte propre, *yaʿrifūna kullan
bi-sīmāhum*, est **mot pour mot** la définition de la *firāsa* portée par le dépôt.
Objection assumée : *« ils n'y sont pas entrés, et ils espèrent »* (VII, 46).

**Reformulation soumise, à accepter ou refuser** : initiés **au seuil** — Petits
Mystères accomplis, Grands non encore. C'est une modification de l'hypothèse ; elle
n'est pas acquise.

### (3) Le couple *khafḍ* / *rafʿ*

`doctrinal/discernement/2026-08-30_khafd-raf-couple-operatoire-des-degres.md`

✅ **Le point bloquant est levé** (collation des pp. 104-105 et 244-245, le
2026-08-30 même). La question était : le « il abaisse » du Calife est-il
l'*isqāṭ*-châtiment d'ar-Râzî ou la « réalisation descendante » de Vâlsan ?
**Réponse du texte : ni l'un ni l'autre.** Le registre dominant est **ontologique** —
*rafʿ* et *khafḍ* sont « deux degrés existenciels fondamentaux » : *rafʿ* = la
manifestation informelle (Anges, purs esprits, Esprit muhammadien) ; *khafḍ* =
« l'expansion et la différenciation du Souffle **au degré individuel** ». **Aucune
charge morale.** Et p. 245, Dieu Lui-même « revêt les attributs de "descente"
(*nuzūl*) » : la descente n'est pas en soi une déchéance.

**Deux acquis de plus, et ils comptent :**

- **Le joint avec les guṇas n'est plus pressenti, il est posé** (note 33, p. 105) :
  *ḍamma* → *sattwa*, *kasra* → *tamas*, *fatḥa* → *rajas*, avec renvoi à la figure
  de Guénon dans *La Théorie hindoue des cinq éléments*. Combiné à la note 30
  (*rafʿ* = *ḍamma*, *khafḍ* = *kasra*) : **rafʿ ↔ sattwa, khafḍ ↔ tamas.**
  L'état *kari-kumi* est caduc pour ce joint.
- ⚠️ **Distinction à ne jamais perdre** : à la p. 104, *rafʿ* et *khafḍ* sont les
  termes de l'***iʿrāb*** (la vocalisation) employés comme symboles ontologiques —
  **ce ne sont pas les Noms divins**. Gilis renvoie le Nom *al-Khāfiḍ* ailleurs :
  *Futūḥāt*, **chap. 558**. Le dossier porte désormais **deux objets distincts**
  qu'il serait fatal de fondre.

**Ce qui reste à trancher** : la qualification du joint (*kumiko* proposé pour le
couple vocalique-ontologique ↔ guṇas, sur autorité de **Gilis et non d'Ibn ʿArabī** ;
*kari-kumi* maintenu pour toute extension aux Noms divins).

## 3. 📷 Collations sur exemplaire physique — par ordre de rendement

C'est ici que le terminal ne change rien : il faut les livres. Mais l'ordre a été
**déterminé mécaniquement**, sur des index déjà transcrits au dépôt — pas au flair.

> ✅ **Les deux premières entrées ont été faites le 2026-08-30 même** (Sidy a
> photographié pp. 104-105 et 244-245). **L'index disait vrai** — la méthode de
> désignation mécanique est validée par le résultat. Transcription :
> `doctrinal/sources/sept-etendards-califat.md`, § « Chapitres XIII et XXXII ».
> **Le point bloquant (3) est levé** : voir §2 ci-dessus, réécrit.

| # | Ouvrage | Pages | Ce que ça débloque |
|---|---|---|---|
| ~~1~~ | ~~*Les Sept Étendards*~~ | ~~**104**~~ | ✅ **fait** — *khafḍ* et *rafʿ* y sont bien traités ensemble, comme **degrés d'existence** et via la vocalisation ; **et la note 33 pose la correspondance avec les guṇas** |
| ~~2~~ | ~~*idem*~~ | ~~**244-245**~~ | ✅ **fait** — les *rijāl Allāh* y sont définis **par leur abaissement** ; renvoi au Nom *al-Khāfiḍ* : *Futūḥāt* **chap. 558** |
| **1** | *Les Sept Étendards* | **193-202** | **chap. XXVI, « Opposition des Anges et *chute de l'Homme* »** — le titre même de la moitié « chute » de la thèse (1). Aucun relevé au dépôt |
| **2** | *idem* | **169-174** | **chap. XXIII, « *La Montagne du Califat* »** — l'autre moitié de la thèse. Aucun relevé |
| **3** | *idem* | **109-114** | chap. XIV, « Les Califes-Pôles » — les occurrences de *quṭb* (109, 111, 166) |
| 4 | *idem* | **29** | *Rafʿ ad-darajāt* — le Nom du degré 38 |
| 5 | *idem* | 81-86 et 265-272 | chap. X « L'Arbre et la Balance » ; chap. XXXV « La Balance et l'Épée » |
| 6 | Ibn ʿArabī, *Futūḥāt* | **chap. 558** | la section sur le Nom divin *al-Khāfiḍ*, **nommément désignée par Gilis** (note 16, p. 244). C'est le **seul** endroit qui traiterait le Nom lui-même |
| 7 | Vâlsan, *Les états des initiés au moment de leur mort* | — | *Futūḥāt* ch. 176. **Le pont** entre « initié » et état posthume. **Non possédé** — à obtenir |
| 8 | Ar-Râzî, *Traité sur les Noms divins* | ch. **XVIII** (n° de page) + ch. *al-Muʿizz*/*al-Mudhill* | pagination manquante ; le chapitre voisin complète la série de quatre Noms |
| 9 | Un *tafsīr* classique | VII, 46-49 | les deux lectures reçues des Aʿrāf sont aujourd'hui affirmées **de mémoire** → `to-source` intégral |

> **Avertissement sur les entrées 1-3** : ce sont des **indices de pagination**.
> Une adjacence dans un index ne prouve aucun rapport doctrinal. Le tableau dit
> **où regarder**, jamais ce qu'on y trouvera.

## 4. 🔑 La règle de méthode dégagée par ce dossier — à tenir

En trois jours, **quatre mots français** ont recouvert des réalités distinctes :

| Mot | Recouvre |
|---|---|
| « **degrés** » | *darajāt* de rang (40:15, 58:11) / degrés cosmologiques du ch. 198 |
| « **descente** » | *isqāṭ*-châtiment / « réalisation descendante » |
| « **Balance** » | *mīzān* eschatologique (VII, 8-9) / signe zodiacal |
| « **chute** » | *hubūṭ* / chute cyclique guénonienne / *isqāṭ* |

**À chaque fois la confusion venait de la langue de travail, jamais des sources.**
Aggravant : **Maurice Gloton signe quatre piliers du dépôt** (Râzî, *De la mort à
la résurrection*, le lexique coranique, le Coran de travail) — le vocabulaire
français de tout le dossier relève d'une seule main.

> **Règle** : dans ce dossier, tout terme porteur se vérifie **à la racine arabe ou
> au terme guénonien exact** avant d'être employé comme argument. Le lexique
> coranique de Gloton (p. 412 transcrite) est justement l'outil qui y donne accès.

**Vérification la plus économique du dossier, et elle n'est pas faite** : quel terme
arabe Ibn ʿArabī emploie-t-il pour les degrés du chapitre 198 ? Si c'est *darajāt*,
l'univocité validée le 2026-07-14 gagne un appui réel ; sinon elle se réduit à une
constance de traduction.

## 5. ✋ Deux rapprochements refusés — ne pas les rouvrir sans texte

1. **ق** — la lettre *qāf* est le degré 17 (le Trône, « qui enveloppe le Cosmos ») ;
   *Jabal Qāf* est la montagne qui entoure, = Meru chez Guénon. **Même nom, même
   description, aucun texte ne pose l'identité.** Coïncidence nominale, refusée
   comme la gématrie de `merkavah-muraqaba`. Seule la convergence *fonctionnelle*
   est instructible, **sur texte**.
2. **Les deux « Balances »** — le *mīzān* de VII, 8-9 n'est pas le signe zodiacal du
   *Mahdi Rouge*. Homonymie française.

Également signalé pour qu'on ne le commette pas par inadvertance : l'*aʿrāf*
coranique (*barzakh* eschatologique) **n'est pas** le « Barzakh supérieur » de l'axe
(degrés 19-20, transition cosmologique). Deux barzakhs, deux plans.

## 6. 🖥️ L'Instrument — état du rendu

`atelier/rd/instrument/instrument-prototype.html` — **sept stations de navigation**
(0 à 6), une seule active à la fois, chacune disant une chose et affichant sa
**garde** (ce qu'elle ne prouve pas). Tout est **touchable** (iPad) ; touches 0-6 et
flèches en doublon.

Deux corrections apportées au rendu existant :
- le **halo du sommet** était un cône se rétrécissant vers le haut — une
  convergence, donc l'erreur que la contrainte 2 interdit. Remplacé par une bande de
  section constante ;
- son étiquette passe de « Hāhūt (1–10) » à « **1–10 · Le Degré divin** » : « Hāhūt »
  était une attribution du Gem, jamais de Gloton.

**Une erreur commise et consignée** (§9.2 du chantier) : la station 3 avait d'abord
été tracée dans la scène 3D, égale **en coordonnées de monde** — et le rendu la
montrait **convergeant en entonnoir**, la perspective étant par définition une
mesure de distance à un point de vue. Marques sorties de la scène, tracées en
pixels.

**Ce qui n'est pas fait, et volontairement** : aucune donnée modifiée
(`instrument-donnees.yaml` inchangé) ; l'**Option A** du chantier reste bloquée ;
Coran LVI, 3 ajoute une **quatrième** description de la discontinuité (simultanée
dans les deux sens) qui n'est **pas rendue** — elle attend le verdict (3).

## 7. Ce que le terminal débloque, et que claude.ai ne pouvait pas

- **`raw/`** — *gitignored*, donc invisible depuis le web. Les ouvrages de Guénon
  s'y trouvent : c'est là que se cherchent *Le Roi du Monde* (montagne polaire) et
  *L'Ésotérisme de Dante* / *Le Symbolisme de la Croix* (le Paradis terrestre au
  sommet et son enceinte) — **le cœur du §3 de la fiche (1)**, aujourd'hui sans
  aucun relevé au dépôt.
- **`raw/assets/`** — les clichés déposés (`IMG_0362`…) ; ceux de cette session
  (p. 35, p. 412, p. 857, Râzî ch. XVIII, couvertures) n'y ont **pas** été versés,
  la session web n'y ayant pas accès. **À déposer côté serveur** pour la traçabilité.

## 8. En une phrase

Le rendu est fait et vérifié ; la matière doctrinale est intégrée, sourcée et
indexée ; **trois fiches attendent un verdict**, dont une thèse d'unification qui
est celle de Sidy ; le point bloquant a été levé le soir même par la collation des
pp. 104-105 et 244-245 ; et le point de reprise le plus rentable est désormais le
**chapitre XXVI, « Opposition des Anges et chute de l'Homme »** — suivi du
**chapitre XXIII, « La Montagne du Califat »** : les deux moitiés de la thèse,
chacune titre d'un chapitre du même livre déjà en bibliothèque.
