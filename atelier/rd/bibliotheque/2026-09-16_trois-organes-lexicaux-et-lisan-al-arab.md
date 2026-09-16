---
title: "Les trois organes lexicaux du dépôt, et le versement du Lisān al-ʿArab"
type: outillage
tags: [bibliotheque, index-lexical, glossaire, grammaire, lisan-al-arab, jurjani, gloton, chantier]
created: 2026-09-16
updated: 2026-09-16
sources:
  - "atelier/rd/outillage/index-lexical/index-lexical.md"
  - "atelier/rd/bibliotheque/glossaire-unifie.md"
  - "atelier/rd/bibliotheque/catalogue-bibliotheque.md"
  - "atelier/rd/outillage/index-lexical/moisson-racines-gloton.tsv"
  - "raw/lisan-al-arab/PROVENANCE.md"
  - "raw/lisan-al-arab/rapport-extraction.txt"
links: []
original: []
---

# Les trois organes lexicaux du dépôt, et le versement du Lisān al-ʿArab

Fiche de consignation, ouverte le 2026-09-16 pour **arrêter la dispersion** : cesser de
produire des fonctions qui finissent oubliées, et poser par écrit ce qui a été établi
pendant la session, avec la mesure de chaque chose et la procédure de reprise.

Elle ne rend **aucun verdict** (Cmd 12). Les points qui en appellent un sont rassemblés
au §6 et déposés au registre.

---

## 1. Ce qui a déclenché la fiche

Constat de Sidy, mot pour mot : *« Je ne veux plus passer du temps à développer des
fonctions qui finissent dans l'oubli comme le Glossaire »*, puis *« Il faut STOPER la
dispersion et le gaspillage qui va avec »*.

Le cas du glossaire unifié n'était pas un accident d'entretien. Il a une cause, et la
cause est lexicale : **trois questions distinctes avaient été confiées à un seul objet.**

---

## 2. Les trois organes, et la question à laquelle chacun répond

| Organe | Question | Unité | Clé | Génératif ? |
|---|---|---|---|---|
| **Index** | **où** | l'occurrence | la chaîne de surface | non |
| **Glossaire** | **quoi, et selon qui** | le sens attribué | le terme technique | non |
| **Grammaire** | **comment** | la règle | la racine | **oui** |

Trois conséquences, qui ne sont pas des opinions mais la définition même des trois unités :

1. **Une adresse n'instruit pas, un sens instruit.** C'est le point qui fonde déjà le
   chantier Gloton (légende p. 232 : case 4 = *« traductions possibles des différents
   sens que la racine prend en français »*). Un index parfait ne répond jamais à *que
   veut dire ce mot*.
2. **Un glossaire se reçoit d'une autorité, il ne se génère pas d'un index.** Le `ḥadd`
   d'al-Jurjānī n'est pas la *définition* de Guénon : l'organe doit porter **selon qui**.
   Un agrégat d'adresses ne peut pas porter d'attribution, donc ne peut pas être un
   glossaire.
3. **La grammaire est le seul organe génératif.** De ك ت ب on tire *kitāb*, *kātib*,
   *maktūb*, *maktaba* — elle rend lisibles des mots **jamais rencontrés**. Ni l'index ni
   le glossaire ne peuvent faire cela, tous deux étant bornés à l'attesté.

**Fait de bibliothèque relevé ce jour** : les trois organes existent déjà au dépôt comme
**trois livres d'un seul traducteur, Maurice Gloton** (catalogue, lignes 84, 85, 88) —
l'*Approche du Coran par la grammaire et le lexique*, le *Livre des Définitions*
d'al-Jurjānī, et *De la mort à la résurrection*. Rester dans **une seule chaîne de
traduction** est ce qui rend les correspondances lisibles d'un ouvrage à l'autre sans
arbitrage supplémentaire.

---

## 3. État mesuré des trois organes (2026-09-16)

Mesures relevées sur disque, non reprises d'un registre.

**Index — vivant.**
`atelier/rd/outillage/index-lexical/index-lexical.md` : **6509 lignes**, dont **6191
lignes de tableau**, `updated: 2026-09-15`, `type: artefact-derive`, générateur
`generer-index-lexical.py`. Condensé par lettre en `condense/` (`a.md`–`z.md`, plus
`hub.md` et `ecritures-originales.md`).

**Glossaire unifié — vide.**
`atelier/rd/bibliotheque/glossaire-unifie.md` : **33 lignes, zéro terme**. `sources: []`,
`links: []`, `created` et `updated` tous deux au `2026-08-22`. Corps :
`| — | — | 0 |` pour les ouvrages, `| — | — | — | — | — |` pour le lexique, et la ligne
`Termes distincts : 0 — occurrences : 0 — ouvrages : 0`.

> **Cmd 10 — correction d'une inscription antérieure.** Le registre affirmait en BIB-04
> que `glossaire-unifie.md` est *« périmé et non vide (le générateur rend 1850 termes,
> 6 ouvrages) »*. **C'est faux quant à ce qui existe sur disque** : 1850 décrit ce que le
> générateur *rendrait*, pas ce qui est là. La correction est portée au registre ; la
> ligne fautive n'est pas effacée.

Cause mesurée de la vacuité : `generer-glossaire-unifie.py` sélectionne sur le **préfixe
de nom de fichier** `index-`, alors que `valider-index-livres.py` sélectionne sur le
**champ `type: index-livre`**. Des 6 fiches `index-*.md`, **5 portent `type: ressource`**
et une seule, `index-origine-polaire-tilak.md`, porte `type: index-livre`. Les deux
instruments ne désignent pas le même ensemble.

**Glossaire réel — un livre, déjà transcrit.**
Catalogue, ligne 85 : al-Jurjānī, *Le Livre des Définitions* (trad. Gloton, Albouraq) —
**220 définitions, de 0010 à 1864**, dont 205 tirées des 54 clichés de
`raw/Transcription Jurjani/` (52 pages non contiguës) et 15 hors clichés. Matériel au
dépôt : `doctrinal/sources/kitab-al-tarifat-jurjani.md`,
`doctrinal/autorites/al-jurjani.md`, `textes/divers/jurjani-definitions.md`,
`raw/Jurjani (définitions).md`, `atelier/rd/outillage/verifier-transcription-jurjani.py`,
`atelier/rd/outillage/index-lexical/2026-09-08_passe-jurjani-orphelines.md`.

**Grammaire — partielle, et dormante côté Gloton.**
`moisson-racines-gloton.tsv` : **169 racines** avec leur case 4, tirées de 107 planches
lues sur 107. Chantier **dormant, ni clos ni bloqué** (verdict Sidy du 2026-09-16 : le
reste sera photographié *« au gré des opportunités »*). Treize discontinuités de
numérotation, toutes vérifiées comme plages non photographiées par le contrôle de la
**page bornant chaque écart** ; la plus serrée est `0521 (p.391) -> 0527 (p.394)`, soit
3 pages. La règle **un trou de photo n'est pas un trou de source** reste confirmée.

---

## 4. Le versement du Lisān al-ʿArab — état réel, et où est l'autorité

**L'analyse du versement existe déjà et n'est pas la mienne.** Elle est au sas :
`_inbox/2026-09-16_lisan-al-arab-edition-versee.md`, `statut: proposition au sas — non
versé aux circuits`, accompagnée de `_inbox/2026-09-16_lisan-al-arab_extraire-shamela.py`.
**C'est elle qui fait foi sur le Lisān**, non la présente fiche ; ce qui suit n'en est que
le report utile au chantier lexical, et **rien de ce qu'elle propose n'est appliqué ici** :
un document en attente de visa ne s'applique pas.

Versé le **2026-09-16** sur ordre de Sidy, `raw/lisan-al-arab/`, **392 Mo, 37 fichiers**.
`raw/` est hors git (`/raw/*` ignoré) : ce dossier n'entre dans aucun circuit ; la chaîne
reste `raw/` → analyse → `_inbox/` → validation humaine → intégration (§VIII.9). Les cinq
circuits sont **intacts** : aucune écriture, aucun `to-source` levé, aucun index bâti.

**Édition A — texte né-numérique.** المكتبة الشاملة, لسان العرب, **دار صادر — بيروت**,
**الثالثة 1414 هـ**, ḥawāshī al-Yāzijī ; Ibn Manẓūr (ت. 711 هـ) ; **15 volumes** ;
`[ترقيم الكتاب موافق للمطبوع]` — **la pagination suit l'imprimé**. Source :
`shamela.ws/book/1687` via le jeu de données `MoMonir/shamela_books_text` (HuggingFace,
apache-2.0), `category_30.csv`, `book_id = 1687`. Fichiers : `..._juz-01.txt` à
`..._juz-15.txt`, le consolidé `..._texte.txt` (**46 Mo**), et `..._pages.tsv`
(**8117 lignes** : en-tête + 8116 pages ; colonnes `volume / page / texte /
note_bas_de_page`). Rapport d'extraction : **24 953 771** caractères de texte,
**537 575** de notes ; trous de pagination déclarés par volume — v6 : 1 ; v10 : 1 ;
v11 : 5 ; v12 : 3 ; v13 : 2 ; v15 : 6 ; **18 au total**, contrôlables contre l'édition B.

**Édition B — scan-témoin de la même impression**, `..._j01.pdf` à `j15.pdf`, 8 197 p.
Concordance des paginations **vérifiée par le sas** : folio ٣٨٢ lu sur l'image de la
page 382 du tome 15, colonne de droite identique mot pour mot au texte extrait.

**Deux obstacles déjà mesurés par le sas, et qui ne sont pas miens à trancher :**

1. **U+200C × 1 520** dans le champ texte (têtes de page). Le Cmd 15 **refusera** le
   fichier tant qu'il n'est pas traité — à juste titre. Deux voies de retrait sont
   proposées au sas ; **aucune n'est engagée**.
2. **Signalement porté par le sas** : `doctrinal/symboles/formule-al-waha-al-ajal-al-saa.md`
   cite le tome 15 pp. 172-173 ; le passage est à pp. 379-382 (écart de 209 pages, donc
   une autre pagination). Correction **réservée au verdict**, et subordonnée par le sas à
   la vérification des quatre passages sur l'image par Sidy lui-même.

**Le fait qui commande tout le chantier lexical**, et que je n'avais pas : **le *Lisān* se
range par dernière radicale, puis par première, puis par seconde** (arrangement d'al-Ṣiḥāḥ).
Retrouver une racine à la main dans 8 200 pages est donc le geste coûteux — c'est lui, et
non le manque de matière, qui borne l'exploitation. D'où la proposition **`BIB-05`** du sas :
un index mécanique `racine → (volume, page)`, construit sur le texte versé, dont la valeur
se **mesure** au nombre de racines déjà moissonnées qui deviennent adressables. **Aucun code
avant visa ; triptyque à rédiger (Cmd 6).**

> **Écart relevé ce jour, à porter à l'attention du sas.** La fiche du sas chiffre la
> moisson Gloton à **97 racines** ; le TSV en porte **169** au 2026-09-16 (passe close le
> jour même, commits `edccb13` / `741806a`). Le critère de mesure de `BIB-05` est donc à
> établir sur **169**, non 97. Je ne modifie pas la fiche du sas : elle attend visa.

**Ce que le versement déplace** : le pivot par **racine** — celui qui ramène *dhikr*,
*dhākir*, *madhkūr*, *tadhkira*, *dhakar* à ذ ك ر — devient mécanisable **sans aucune
photographie supplémentaire**. Le chantier Gloton n'en est **pas** remplacé et reste
dormant : Gloton donne le **français** de la racine, ce que le *Lisān* ne donne pas. Les
deux ne répondent pas à la même question.

**Ce que le versement ne fait pas** : le *Lisān* est un dictionnaire de langue, non un
glossaire technique. Il ne remplace ni al-Jurjānī (le `ḥadd` du vocabulaire du Taṣawwuf)
ni le jugement sur la **notion** (le pôle de Tilak, le *quṭb* coranique) — la
correspondance par notion relève du verdict, jamais de la machine.

## 5. Les deux lois lues cette session, et où elles sont déjà inscrites

**Guénon — loi de la correspondance.** Le langage scolastique est *« le moins inadéquat
de tous ceux que l'Occident met à notre disposition »*, mais *« il ne s'applique plus
au-delà d'un certain point où s'arrêtent les correspondances qu'on peut légitimement
établir »*. Sur *Mâyâ* : rendre par « illusion » plutôt que par « art » ne produit pas
une nuance mais **une autre doctrine**, en prenant pour néant ce qui n'est que
*« degrés différents dans la réalité »*. Guénon **ne définit pas** : il déploie l'éventail
des traductions et nomme l'erreur que chacune induit. **Une correspondance sans sa limite
énoncée est une annexion.**

**Ghazālī — loi de la limite** (*Munqidh*, trad. Jabre 1959). *« L'ivrogne ne connaît pas
la définition de l'ivresse… un médecin malade connaît bien la définition de la santé : il
est pourtant malade »* ; et *« Ce qui pouvait s'apprendre, je l'avais acquis »* — les
livres d'abord épuisés, **puis** su où ils s'arrêtent.

**Les deux énoncent une seule loi : un instrument vaut jusqu'à une limite, et la faute
n'est pas de s'en servir, mais de ne pas marquer où il cesse.** Elle est **déjà** au
dépôt, sous deux formes : **Cmd 5** (marquer l'inconnu plutôt que deviner) et le marqueur
**`to-source`**. Rien à construire — de quoi rendre explicite que les en-têtes
*« Instrument de repérage : il dit *où chercher*, jamais *quoi conclure* »* portés à
l'identique par `index-lexical.md` et `glossaire-unifie.md` sont l'application de cette
loi, et non une formule d'usage.

**Corollaire tenu cette session** : une **figure** tient ses relations *simultanément*,
une **liste** les tient *successivement*. L'organe des correspondances est donc
l'**Instrument** (`atelier/rd/instrument/`, table des 28 degrés,
**8 Lāhūt / 4 Jabarūt / 7 Malakūt / 9 Nāsūt**, colonnes *Lettre / Nom Divin / Faṣṣ /
Manzil*, degré 16 = Ciel du Soleil / Idrīs à la médiane du Malakūt), **non un glossaire**.

---

## 6. Points soumis au verdict de Sidy (Cmd 12 — la machine ne tranche pas)

1. **`glossaire-unifie.md` est-il déclaré caduc ?** Mesuré vide (33 lignes, 0 terme) ; le
   glossaire réel est un livre déjà transcrit (al-Jurjānī, 220 définitions). Le
   régénérer produirait un agrégat d'adresses sous un nom qui promet des sens.
2. **Divergence de périmètre générateur/validateur** (préfixe `index-` contre champ
   `type: index-livre`, 5 fiches sur 6 hors du champ). Priorité basse, mais toute mesure
   faite sur l'un des deux instruments est à lire avec cette réserve.
3. **Recomptage du tableau de synthèse du registre** : non-réconciliation pour `DOC`,
   `OUT` et `INF`. Réserve Cmd 5 déjà inscrite ; **ces trois pôles n'ont pas été
   touchés**, la cause est formelle (tableaux à nombres de colonnes différents).

**Aucune fonction nouvelle n'est proposée par cette fiche.** Un contrôle de fraîcheur des
artefacts dérivés avait été envisagé en séance : il a été **retiré**, son seul office à la
naissance étant d'exiger à chaque commit la régénération d'un objet dont l'existence même
est en question — il serait devenu la prochaine fonction oubliée.

---

## 7. Procédure de reprise après coupure

À lire en premier si la session s'est interrompue. Aucune étape ne suppose de mémoire de
la session précédente.

**a. Se situer.** Lire cette fiche, puis la ligne du chantier au registre
(`atelier/rd/registre-chantiers.md`, section `## 4. Bibliothèque (BIB)`), puis la
dernière entrée de `atelier/annales.md`.

**b. Ne rien régénérer.** `glossaire-unifie.md` est un `type: artefact-derive` **en
attente de verdict** (§6.1). Tant que le verdict n'est pas rendu, il ne se régénère ni ne
s'édite à la main. Un document en attente ne s'applique pas.

**c. Vérifier avant d'écrire, toujours mesurer plutôt que citer.** Les chiffres de cette
fiche sont des mesures datées du 2026-09-16 ; les recontrôler sur disque avant de les
réemployer, jamais les reprendre d'un registre.

**d. Contrôles mécaniques, résultat rapporté brut.**
`atelier/rd/outillage/verifier-hygiene-unicode.py` (instrument unique du Cmd 15, appelé
par le hook `pre-commit`) et `verifier-invariants.py`. Note d'état au 2026-09-16 : les
**71 avertissements** de `verifier-invariants.py` **préexistent** dans
`doctrinal/autorites/rene-guenon.md` (étanchéité C5/C6 inversée) et ne sont pas imputables
aux passes récentes.

**e. Ne jamais `git add -A`.** Deux fichiers de sortie cron sont non suivis et doivent
rester hors de tout commit :
`atelier/rd/infrastructure/monitoring-archive/2026-09-16_41dc3e7e492c.txt` et
`..._ad3152b237bb.txt`. **Stager les chemins un par un.**

**f0. Le sas d abord.** Lire `_inbox/2026-09-16_lisan-al-arab-edition-versee.md` : c est la piece qui fait foi sur le Lisan, et elle attend le visa de Sidy. Rien de ce qu elle propose (BIB-05, retrait des U+200C, correction de page, deplacement du script vers l outillage) ne s applique avant ce visa.

**f. Si le Lisān doit être exploité.** Il n'y a **rien à ingérer** : le versement est
complet, provenancé et vérifié. Le point d'entrée est `..._pages.tsv` (adressage
`volume/page`, pagination fidèle à l'imprimé, donc citable). Tout instrument qui le lira
va dans `atelier/rd/outillage/`, en **étendant l'existant** plutôt qu'en dupliquant, et
n'écrit rien dans `raw/`.

**g. Bornes de la reprise.** Le chantier Gloton reste **dormant** : il ne reprend qu'à
l'arrivée de nouvelles photographies, par passes d'**ajout strict** (`git diff --numstat`
doit rendre `N 0`), **sans campagne à programmer**.
