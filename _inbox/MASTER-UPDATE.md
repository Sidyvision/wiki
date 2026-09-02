# MASTER-UPDATE — ingest des deux ouvrages de Tilak (chantier DOC-06)

> **Ce que cette pièce est.** Le plan d'ingest exigé par l'Action ARCHIVAGE avant
> toute écriture (§VII, point 2 : « Présenter le plan — titres, slugs, dossiers,
> statuts — AVANT toute écriture » ; Cmd 6). Le §I du protocole racine prévoit un
> `MASTER-UPDATE.md` pour les **lots volumineux**, « traités fiche par fiche dans
> l'ordre du manifeste » : c'est le cas ici, et c'est l'instrument prévu.
>
> **Ce qu'elle n'est pas.** Ni un ingest fait, ni une autorisation. Aucune fiche
> n'est écrite tant que Sidy n'a pas visé ce plan. Le chantier est **ouvert et
> instruit**, il n'est pas exécuté.
>
> Chantier : **DOC-06** (`atelier/rd/registre-chantiers.md`).
> Ouvert le 2026-09-02 sur verdict de Sidy.

## 1. Ce qui est au sas, et son état

| ouvrage | fichier | volume | état |
|---|---|---|---|
| *The Arctic Home in the Vedas* (1903, 544 p.) | `conversions/chapitres-arctic-home/` | 13 chapitres + index, **23 729 lignes** | OCR découpé, non intégré |
| *The Orion, or Researches into the Antiquity of the Vedas* (1893, 237 p.) | `conversions/chapitres-orion/` | 8 chapitres + appareil, **~9 500 lignes** | OCR découpé, non intégré |

Les deux sont l'**original anglais**. L'exemplaire physique de Sidy est la
traduction française d'*Arctic Home* (Jean et Claire Remy, Arché, Milano, 1979).
**Les paginations ne se correspondent pas** et aucune table de correspondance
n'est établie : aucune référence de page relevée sur l'un ne vaut pour l'autre.

⚠️ **Qualité d'OCR médiocre et inégale.** Relevé sur pièces : « CHAPTER ITIL »
pour III, « AGRAHAY ANA » pour Agrahāyaṇa, « Marthnda »/« Mirtinda » pour
Mārtāṇḍa, « Big-Veda » pour Rig-Veda, « sm » pour sun. Les passages en
devanāgarī translittéré sont **illisibles** par endroits. Conséquence de méthode,
non négociable : **aucune citation n'est reprise sans avoir été relue caractère
par caractère**, et tout mot sanskrit est rétabli dans sa forme translittérée
correcte, la forme OCR étant écartée sans être conservée (ce n'est pas une
variante, c'est un défaut de machine).

## 2. Le statut, arrêté d'avance

**`academique` pour tout.** Tilak est un travail de philologie comparée du
XIXe-XXe siècle. Sa fiche existante le pose déjà : « à ne pas confondre avec une
source doctrinale de rang égal aux textes akbariens ou guénoniens du dépôt ».

**Et l'estime de Guénon n'y change rien.** « Atlantide et Hyperborée » appelle
*The Arctic Home* un « remarquable ouvrage » — c'est une recommandation de
lecture, non un adoubement traditionnel. Le point est tranché d'avance pour que
l'ingest ne le rouvre pas fiche par fiche.

**Ce qui, en revanche, est `traditionnel`** : les textes que Tilak *cite* —
Ṛg-Veda, Taittirīya Saṃhitā/Brāhmaṇa/Āraṇyaka, Śatapatha, Avesta. Mais ils ne
sont pas ingérés *par* Tilak : une citation védique relevée chez lui reste
`to-source` tant qu'elle n'est pas vue sur une édition du texte. **Tilak est un
index, pas une source primaire.**

## 3. Ce que l'ingest produirait — proposition, fiche par fiche

### 3.1 Notices de source (circuit `doctrinal/sources/`)

| # | slug proposé | objet | statut |
|---|---|---|---|
| 1 | `tilak-origine-polaire-tradition-vedique` | **existe déjà** — enrichie, non recréée : passage de la notice de catalogue à la notice d'ouvrage lu | `academique` |
| 2 | `tilak-orion-antiquite-vedas-1893` | *The Orion* — le premier ouvrage, absent du dépôt | `academique` |

**Deux notices, pas quinze.** Une page = un sujet (Cmd 4), et le sujet d'une
notice de source est **l'ouvrage**, non le chapitre. Découper Tilak en treize
fiches fabriquerait une importance que le dépôt ne lui accorde pas.

### 3.2 Fiches de matière (circuit `doctrinal/`)

Trois seulement, et chacune justifiée par un **besoin déjà exprimé au dépôt**,
non par le fait que la matière existe :

| # | slug proposé | dossier | pourquoi elle est justifiée |
|---|---|---|---|
| 3 | `adityas-mois-du-soleil` | `symboles/` | Les états du soleil sont déjà **consommés** par la donnée de l'Instrument (bloc `polaire:`), qui les cite sans qu'aucune page doctrinale ne les porte. La matière est utilisée avant d'être fichée : c'est le défaut à corriger. |
| 4 | `ushas-les-trente-aurores` | `symboles/` | Même motif : les trente sœurs sont rendues, non fichées. |
| 5 | `devayana-pitriyana` | `symboles/` | Le couple est **déjà nommé par Guénon au dépôt** (SSS ch. XXXVII, les deux voies, les deux clefs) mais n'a pas de page propre. Tilak en donne la matière védique. La fiche serait tenue **sur Guénon** (`traditionnel`) et **complétée** par Tilak (`academique`), les deux registres distingués dans le corps. |

### 3.3 Ce qui n'est PAS proposé, et pourquoi

- **Aucune fiche `discernement`.** L'ingest verse de la matière ; il ne pose
  aucune question spéculative. Les questions ouvertes existent déjà et ont leurs
  fiches (chute/état primordial, Balance polaire/zodiacale).
- **Aucun ancrage inter-registres.** Cmd 3 : rien ne naît d'un ingest.
- **Aucune fiche sur la thèse historique** (origine arctique des Veda,
  datation par précession). Motif : c'est **la** thèse académique de Tilak, elle
  est disputée, et le dépôt n'a aucun usage qui l'exige. Elle est **résumée dans
  les deux notices**, où son statut se lit d'un coup d'œil, plutôt qu'installée
  dans le corps doctrinal.
- **Aucune reprise du chapitre XIII** (« Bearing on Primitive Aryan Culture ») :
  matière d'histoire raciale de l'époque, sans emploi au dépôt, et de celles dont
  la reprise sans usage serait un choix, non un archivage.

## 4. Signalements doctrinaux à porter dans les fiches

À écrire **dans** les fiches, non en annexe :

1. **Tilak est un index, pas une source.** Toute citation védique relevée chez
   lui reste `to-source` jusqu'à vérification sur édition du texte.
2. **Divergence 8 / 12 Ādityas** (🌐) : l'Āraṇyaka pose « aṣṭau te vyavasitāḥ »
   — le nombre huit est fixé par l'Écriture ; le Śatapatha, les Upaniṣads et la
   littérature post-védique en donnent douze, identifiés aux douze mois. **Les
   deux comptes sont portés séparément, jamais fondus.**
3. **Lacune du texte** : le Taittirīya Āraṇyaka donne les huit noms mais **ne dit
   pas lequel est Mārtāṇḍa**. À conserver comme lacune, non à combler.
4. **Kaśyapa au Mahāmeru** — soleil qui ne quitte jamais la montagne polaire et
   communique sa lumière aux sept visibles. 🔍 Touche de très près le hozo
   Meru = Qâf clos au dépôt. **Signalé, non déclaré** : exigerait sa propre fiche
   de discernement (Cmd 3).
5. **Trois septénaires distincts** : sept Ādityas (solaire), sept Ṛṣis de la
   Grande Ourse (stellaire, Roi du Monde ch. X), sept Aqtāb/Malakūt planétaire
   (hozo clos 2026-07-16). Les rapprocher serait un troisième septénaire jeté sur
   deux autres. **Interdit d'office à l'ingest.**
6. **Vigilance polaire/solaire** (§VII, double contrôle) : la matière est
   massivement polaire ; confrontation au pôle Gizeh à consigner **même si le
   résultat est négatif**.

## 5. Ordre de traitement, et point d'arrêt

1. Notice *Orion* (fiche 2) — l'ouvrage absent d'abord.
2. Enrichissement de la notice *Arctic Home* (fiche 1).
3. **ARRÊT — retour à Sidy.** Les deux notices sont lues avant que la moindre
   fiche de matière soit écrite : si le régime de citation ou le traitement de
   l'OCR ne convient pas, il vaut mieux le voir sur deux fiches que sur cinq.
4. Fiches 3, 4, 5, dans cet ordre.
5. Index de circuit, annales, graphe régénéré, `_inbox/` vidé.

## 6. Ce que ce plan attend de Sidy

| # | question | pourquoi elle ne m'appartient pas |
|---|---|---|
| 1 | **Le plan lui-même est-il visé ?** | Cmd 6 — rien n'est écrit avant |
| 2 | Cinq fiches est-il le bon découpage, ou faut-il **moins** ? | Le volume de la source ne commande pas le volume au dépôt ; c'est un jugement de proportion |
| 3 | Le chapitre XIII (culture aryenne primitive) est écarté — **confirmez-vous** ? | Écarter une part d'une source est une décision, pas une omission technique |
| 4 | Les conversions du sas doivent-elles être **versées à `raw/`** ou rester hors git ? | 33 000 lignes d'OCR au dépôt engagent son poids et sa lisibilité ; elles sont aujourd'hui **non suivies** |
