---
title: "Rapport d'erreurs — session Hindouisme et Soufisme / réseau subtil (2026-08-29 → 30)"
type: experience
statut_experience: reproduit
tags: [rd, cahier, rapport, erreurs, vigilance, instrument, methode, verification-mecanique]
created: 2026-08-30
updated: 2026-08-30
sources: []
links: ["[[atelier/rd/cahiers/registre-problemes]]", "[[atelier/rd/instrument/2026-08-30_reseau-subtil-unification-axes-deux-echelles]]", "[[atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable]]", "[[doctrinal/sources/guenon-homme-devenir-vedanta-ch21-artere-coronale-rayon-solaire]]", "[[doctrinal/sources/avalon-serpent-power-nadis-reseau]]"]
---

# Rapport d'erreurs — session « Hindouisme et Soufisme / réseau subtil »

> Circuit **atelier**, pôle R&D, cahier de laboratoire. Document de méthode, non
> doctrinal. Liens vers `doctrinal/` en sens unique, signalés.
>
> **Commande** : Sidy, 2026-08-30 — « Instruit un rapport complet au R&D,
> surtout les diverses erreurs trouvées tout au long de la session. »
>
> **Périmètre** : la session du 2026-08-29 au 2026-08-30 (transcriptions
> Shayegan, Majmaʿ al-Bahrayn, Avalon, ch. XXI du Vêdânta, ancrages
> inter-registres). **Vingt défauts** recensés, classés par *qui les a produits*
> et surtout par **ce qui les a attrapés** — c'est cette seconde colonne qui
> porte l'enseignement.

## 0. Le tableau d'ensemble

| # | Défaut | Origine | **Attrapé par** |
|---|---|---|---|
| 1 | « Aucune correspondance » colonnes séphirothiques ↔ nâdîs | machine | **Sidy** |
| 2 | L'« interversion » de Guénon prise pour un doute | machine | **Sidy** |
| 3 | Deux registres rendus à l'envers depuis le 2026-08-20 | machine | **test mécanique** |
| 4 | Hélices courant sur toute la hauteur | machine | **lecture de la source** |
| 5 | 3,5 tours d'hélice empruntés à un autre symbolisme | machine | **lecture de la source** |
| 6 | `__xEclate` écrasé par une affectation ultérieure | machine | **test aller-retour** |
| 7 | Scan sur la clef `noeuds` au lieu de `nodes` | machine | auto-détection |
| 8 | Sahasrāra : 1000 pétales plafonnés à 24 **en silence** | machine | **relecture des planches** |
| 9 | Qualification des ancrages sur la longueur totale | machine | **relecture adversariale** |
| 10 | « Oblique ⇒ décalage-donnée » — faux, et grave | machine | **relecture adversariale** |
| 11 | Anneau notionnel restreint à `tasawwuf` | machine | **test mécanique** |
| 12 | Générateur : garde Cmd 3 annoncée mais absente sur les ancrages | outillage | **audit du code** |
| 13 | Générateur : comptage des ancrages faux | outillage | recoupement |
| 14 | `verifier-invariants` [A6] : faux positif sur deux SHA | outillage | investigation |
| 15 | Fiche ch. XV-XXI : attributions de chapitres fausses | dépôt | **texte primaire** |
| 16 | 26 entrées d'annales sans SHA (Cmd 9) | dépôt | balayage mécanique |
| 17 | 23 fiches doctrinales absentes de l'index | dépôt | balayage mécanique |
| 18 | Table des 38 degrés : **contradiction de numérotation interne** | dépôt | **collation en cours de session** |
| 19 | `merkavah-muraqaba` : mauvaise version d'un rapprochement que Sidy vient de rouvrir | dépôt | recherche préalable |
| 20 | Photos annoncées présentes et jamais commitées | process | **Sidy** |

**Ce que la troisième colonne dit.** Sur vingt défauts, **trois seulement** ont
été attrapés par relecture humaine de Sidy, et **aucun** par une relecture
narrative de la machine sur son propre travail. Tout le reste vient de trois
sources : un **test mécanique**, la **lecture de la source primaire**, ou une
**relecture adversariale** conduite en se demandant non pas « est-ce juste ? »
mais « qu'est-ce qui, ici, ferait échouer la vérification ? ». C'est la
confirmation la plus nette qu'ait reçue à ce jour la règle §VIII.2 du protocole
racine : *fiabilité d'action ≠ fiabilité narrative*.

---

## 1. Erreurs de la machine — le fond doctrinal

### 1.1 « Aucune correspondance » entre colonnes séphirothiques et nâdîs

- **Symptôme** : j'ai affirmé que Guénon n'établissait aucune correspondance
  entre les trois colonnes de l'arbre séphirothique et les trois *nâdîs*.
- **Fait** : il l'établit dans une seule phrase — la colonne du milieu
  « correspond à *sushumnâ* », les latérales sont « en relation avec *idâ* et
  *pingalâ* ».
- **Diagnostic** : affirmation négative produite **de mémoire**, sans relire la
  page. Une négation (« il ne dit pas ») coûte aussi cher à établir qu'une
  affirmation, et je l'ai traitée comme gratuite.
- **Résolution** : rectifiée dans la fiche, le YAML et les annales.
- **Compréhension tirée** : ⚠️ **une affirmation négative sur une source exige la
  même vérification qu'une affirmation positive.** C'est même la plus dangereuse,
  parce qu'elle ferme une piste au lieu d'en ouvrir une fausse — et qu'elle ne
  laisse aucune trace à vérifier plus tard.

### 1.2 L'« interversion » de Guénon prise pour un doute

- **Symptôme** : j'ai présenté la remarque de Guénon sur l'interversion
  Yesod/Malkhut ↔ Mūlādhāra/Swādhishthāna comme une hésitation de sa part.
- **Fait** : c'est sa **conclusion**. L'appariement que j'avais déclaré était
  bon ; seule ma justification était fausse.
- **Diagnostic** : le résultat étant juste, rien ne signalait le défaut. C'est le
  cas le plus difficile à détecter — **une bonne réponse pour un mauvais motif**
  passe tous les contrôles de sortie.
- **Compréhension tirée** : les contrôles mécaniques valident des **sorties**,
  jamais des **raisons**. Seule la relecture de la source par un humain attrape
  cette classe-là. C'est un argument fort pour que la levée d'un `to-source`
  reste, comme le veut le protocole, un acte humain.

## 2. Erreurs de la machine — le rendu

### 2.1 Deux registres à l'envers pendant dix jours

- **Symptôme** : les registres `hindouisme-tantra` et `vedanta` étaient rendus
  **tête en bas** depuis le 2026-08-20 — Mūlādhāra à la couronne, Sahasrāra à la
  base.
- **Diagnostic** : le rendu supposait « rang 1 = sommet » pour tous les
  registres. Or `rang` enregistre l'ordre **propre à chaque tradition** : la
  Kabbale énumère du haut, le Kundalinī-yoga et le Vêdânta du bas.
- **Résolution** : champ `sens_rang` — le sens est désormais **lu dans la
  donnée**, jamais supposé.
- **Compréhension tirée** : ⚠️ **une convention tacite partagée par les premières
  données devient un bug silencieux dès la troisième.** Le premier registre versé
  était kabbalistique ; sa convention est devenue la règle sans jamais avoir été
  déclarée. Toute convention doit être **portée par la donnée** dès qu'un second
  cas existe — et le moment de l'écrire est celui où l'on en ajoute un second,
  pas celui où l'erreur se voit.
- **Aggravant** : dix jours de rendu faux, et **aucune relecture ne l'avait vu**.
  C'est un test mécanique qui l'a trouvé.

### 2.2 Hélices sur toute la hauteur, et 3,5 tours empruntés

- **Symptôme** : les deux canaux latéraux couraient sur toute la colonne, avec
  **3,5 tours** codés en dur.
- **Fait** : Avalon écrit qu'ils entrent dans *suṣumnā* à *Ājñā* ; et les 3,5
  tours étaient ceux des **enroulements de Kuṇḍalinī autour du liṅga** — un tout
  autre symbolisme, emprunté par ressemblance de forme.
- **Résolution** : `canal_debut`/`canal_fin` versés ; nombre de tours **dérivé**
  du nombre de centres enlacés (deux hélices contra-rotatives se croisent deux
  fois par tour ⇒ *n*/2 tours), confirmé par la Planche I.
- **Compréhension tirée** : ⚠️ **un nombre codé en dur dans un rendu symbolique
  est une assertion doctrinale non sourcée.** Elle a l'air d'un choix graphique ;
  elle n'en est pas un. Un paramètre visuel doit être *dérivé* d'une donnée ou
  *déclaré* avec sa source — jamais posé « parce que ça rend bien ».

### 2.3 Le plafond de Sahasrāra, silencieux

- **Symptôme** : *Sahasrāra* déclare **1000** pétales ; la couronne était
  plafonnée à 24 sans que rien ne le dise. Or 24 n'est le compte d'aucun autre
  centre : la couronne se lisait comme un **compte exact**.
- **Diagnostic** : c'est la définition même d'un **décalage-artefact non
  résorbable** — une convention de dessin devenue indiscernable d'une donnée.
- **Résolution** : au-delà du seuil, la couronne devient **double**, en deux
  anneaux décalés — forme qu'aucun compte exact ne produit — et l'info-bulle
  porte le nombre réel.
- **Compréhension tirée** : ⚠️ **tout plafonnement, arrondi ou simplification de
  rendu doit être visible dans la forme même, pas seulement dans un commentaire
  de code ou une info-bulle.** Le lecteur regarde l'image ; s'il faut survoler
  pour savoir que ce qu'on voit est conventionnel, la convention ment.

### 2.4 La qualification des ancrages — deux fautes en une

- **Symptôme** : j'avais qualifié les ancrages inter-registres sur leur
  **longueur totale**, et écrit qu'un ancrage resté oblique en mode unifié
  signalait un **décalage-donnée**.
- **Fait, premier étage** : la longueur mêlait deux grandeurs de sens différent —
  la **hauteur** (le niveau, qui signifie) et le **report latéral** (la colonne,
  qui signifie autre chose). Hokhma↔Ājñā ressortait « oblique » alors que ses
  deux extrémités sont **à la même hauteur**.
- **Fait, second étage — le grave** : la hauteur d'un domaine de registre
  parallèle est une **répartition proportionnelle** sur l'étendue de l'axe, donc
  de la **présentation** ; une bande de Présence, elle, est posée à ses **degrés
  déclarés**, donc de la **donnée**. Un ancrage entre les deux a une extrémité de
  chaque sorte : son obliquité est un **artefact de convention**, et rien
  d'autre.
- **Portée** : en faire un indice de décalage-donnée aurait installé **au cœur du
  rendu la confusion exacte que la spec interdit** — et l'aurait installée sous
  la forme la plus difficile à déloger, celle d'une aide à la lecture.
- **Résolution** : la qualification se lit sur **Y** (le niveau) et **X** (la
  colonne), **jamais sur Z**. Elle est donc identique dans les deux modes — ce
  qui est la vérité : la correspondance de niveau ne dépend pas de l'angle de vue.
- **Compréhension tirée** : ⚠️ **la distinction donnée / présentation doit être
  tenue par extrémité, pas par objet.** Un même segment peut être moitié donnée,
  moitié convention. Et : **une fonctionnalité qui *interprète* pour le lecteur
  est plus dangereuse qu'une qui affiche** — l'erreur d'affichage se voit,
  l'erreur d'interprétation s'installe.

### 2.5 L'anneau notionnel restreint à `tasawwuf`

- **Symptôme** : le joint ternaire latéral ↔ Janus, une fois verdicté, ne se
  traçait pas : le filtre de l'anneau des nœuds notionnels ne retenait que
  `tradition === "tasawwuf"`.
- **Diagnostic** : la **provenance** d'un nœud servait de critère à sa
  **fonction**. Or l'anneau accueille les nœuds *transversaux*, et un joint
  transversal peut parfaitement joindre deux symboles dont aucun n'est akbarien.
- **Résolution** : filtre élargi aux nœuds `universel` sans degré.
- **Compréhension tirée** : ⚠️ **un filtre écrit quand une seule tradition
  existait devient une exclusion doctrinale dès la deuxième** — même famille que
  §2.1. La donnée était juste, le verdict rendu, et le rendu la taisait pour une
  raison qui n'en était pas une.

## 3. Erreurs d'outillage

### 3.1 Une garde annoncée mais absente

- **Symptôme** : le générateur documentait l'application du Cmd 3 (tout ancrage
  inter-registres exige une fiche `discernement/` en source) — et **ne
  l'appliquait pas** aux ancrages.
- **Compréhension tirée** : ⚠️ **un commentaire décrivant une garde n'est pas une
  garde.** La classe d'erreur est celle déjà consignée au registre le 2026-08-17
  (une fiche affirmant un job cron jamais créé) : l'écart entre ce qu'un document
  affirme et ce que le code fait. Le remède est le même — **un test qui échoue
  quand la garde manque**, pas une relecture.

### 3.2 Le faux positif [A6]

`verifier-invariants.py` signale « corps d'entrée orphelin possible » dès qu'une
entrée d'annales porte deux `- **Commit** :`. Or une entrée couvrant deux
livrables en porte légitimement deux. **Faux positif**, signalé deux jours de
suite, **non corrigé** (contrôle d'un fichier append-only — VIGILANCE :
rapporter, ne pas corriger d'office). Arbitrage à Sidy : raffiner le contrôle,
ou l'accepter tel quel.

## 4. Défauts trouvés dans le dépôt

### 4.1 Une fiche établie sur paraphrase, aux attributions fausses

`guenon-homme-devenir-vedanta-ch15-21` attribuait au **ch. XXI** « le rejet ou la
résorption finale » et plaçait les *nâdîs* au **ch. XIX**. Le texte primaire,
déposé par Sidy, montre que le ch. XXI est celui de **l'artère coronale et du
Rayon solaire**, et que c'est là que les *nâdîs* sont exposés.

- **Diagnostic** : la fiche portait déjà son propre avertissement
  (« ⚠️ Pagination `to-source` — transcription via index-rene-guenon.org »). Le
  `to-source` visait la **pagination** ; le défaut portait sur la **structure**.
- **Résolution** : sections XIX-XXI **conservées** (Cmd 10) et marquées **NON
  VÉRIFIÉES**, à collationner sur l'exemplaire physique.
- **Compréhension tirée** : ⚠️ **un `to-source` partiel donne une fausse
  assurance sur tout ce qu'il ne couvre pas.** Marquer la pagination incertaine a
  fait paraître le reste certain. Un marqueur de doute doit énoncer **son
  périmètre**, sans quoi il fonctionne comme un label de garantie sur le
  complément.

### 4.2 ⚠️ ~~Une contradiction de numérotation~~ → **RÉSOLU le 2026-08-30 : il n'y avait pas de contradiction**

> ## ✅ Résolution — et le diagnostic ci-dessous était lui-même en défaut
>
> Collation faite le 2026-08-30 sur clichés déposés par Sidy (`raw/assets/`).
> **Les deux « systèmes incompatibles » identifiés ci-dessous n'en étaient pas
> deux** : le système (a) n'a **aucune existence textuelle**. Les Figures 1 et 2
> (pp. 91-92) sont des diagrammes **concentriques sans numérotation** ; le rang
> de leurs anneaux avait été lu comme une suite de numéros de degrés.
>
> Le texte primaire (Gloton pp. 36-38, table courante) donne sans ambiguïté :
> **ʿArsh = degré 17** (qâf), **Kursī = degré 18** (kâf), **Sphère sans étoiles =
> degré 19** (jîm). Et la Figure 4 (p. 94) numérote les lettres **1-28** là où la
> table courante les numérote **11-38** : décalage constant de 10, vérifié terme à
> terme. Même ordre, deux origines.
>
> **Ce que ce défaut ajoute au présent rapport.** Il appartient à la même famille
> que le §2.3 (le plafond silencieux de *Sahasrāra*) et le §2.1 (la convention
> tacite de `sens_rang`) : **une convention de lecture non déclarée devient
> indiscernable d'une donnée.** Ici, un rang de dessin s'est fait passer pour un
> numéro de degré, et a tenu deux jours en bloquant un chantier entier.
>
> Il ajoute aussi une aggravation propre : **la demande de collation elle-même
> visait la mauvaise page.** J'ai demandé les pp. 91-92 (les Figures), alors que
> la réponse était aux pp. 36-38 (la table courante). Les Figures ne pouvaient pas
> trancher — c'est justement leur absence de numérotation qui avait créé l'erreur.
> J'ai donc demandé à l'humain de vérifier, sur la pièce même qui m'avait égaré,
> une question qu'elle ne pouvait pas résoudre.
>
> **Corrigé dans** `doctrinal/symboles/table-28-degres-nafas-rahman.md` (bloc
> normatif de convention de numérotation ajouté en tête, sections fautives
> conservées et marquées — Cmd 10) et
> [[atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable]] §5.
> **Aucune donnée de l'Instrument n'était fausse** : `instrument-donnees.yaml`
> portait déjà 17 = ʿArsh et 18 = Kursī.
>
> **Section conservée ci-dessous telle qu'écrite** (Cmd 10), comme trace.

### ~~4.2 Une contradiction de numérotation dans la table des 38 degrés~~ *(état antérieur, conservé)*

**Défaut nouveau, trouvé en fin de session, et il bloque le chantier que Sidy
vient d'ouvrir.** `doctrinal/symboles/table-28-degres-nafas-rahman.md` porte deux
numérotations incompatibles :

| Système | Ce qu'il pose | Conséquence pour le Kursī |
|---|---|---|
| **(a)** « Jabarūt — degrés 9-12 (Figure 2, p. 92) » | 9 = Corps universel · **10 = Trône (ʿArsh)** · **11 = Piédestal (Kursī)** · 12 = Sphère sans étoiles | le Kursī est le **degré 11** |
| **(b)** « degrés 1-10 pré-lettrés + degrés 11-38 = les 28 lettres » | le degré 11 est **hamza** (première des 28 lettres) | le degré 11 est **une lettre**, pas le Kursī |

Les deux ne peuvent tenir ensemble : le degré 11 ne peut être à la fois le
Piédestal et la *hamza*. Le comptage de la Figure 1 (8 termes) suivi de la
Figure 2 (4 termes) donne d'ailleurs **12** pré-lettrés, non 10.

- **Portée immédiate** : le rendu de l'Instrument suit le système **(b)** —
  degrés 11-38 sur l'axe, degrés 1-10 en halo « Hāhūt, non manifesté ». Sous le
  système **(a)**, le Kursī tomberait **à l'intérieur** de la zone rendue. La
  frontière conditionné / inconditionné du rendu dépend donc entièrement de
  laquelle des deux numérotations est la bonne.
- **Résolution** : **aucune.** Elle exige les pages 91-92 de Gloton, que seul
  Sidy peut collationner. **Rien n'a été modifié.**
- **Ce qui a failli arriver** : j'ai commencé à construire sur « Kursī = degré 11
  = base de l'axe rendu » une conclusion de design pour le chantier de
  l'incommensurabilité — avant de collationner et de voir la contradiction. Le
  raisonnement était séduisant et **entièrement faux dans un des deux systèmes**.
- **Compréhension tirée** : ⚠️ **deux numérotations d'origines différentes dans
  une même fiche sont un piège actif**, et la fiche le sait pour un autre cas
  (elle avertit déjà, à propos du tableau Meftah : « aucune correspondance
  chapitre ↔ degré n'est établie ici »). Elle ne le fait pas pour celui-ci. La
  règle « une page = un sujet » (Cmd 4) devrait s'étendre à **une page = un
  système de numérotation**, ou bien chaque table doit porter en tête, de façon
  non contournable, l'origine dont elle relève.

### 4.3 Un rapprochement que Sidy rouvre, et dont le dépôt garde une mauvaise version

Sidy indique, pour le chantier de l'incommensurabilité, que le Kursī puis le
ʿArsh sont « d'ailleurs un autre ancrage avec la Kabbale ». Le dépôt porte déjà
`doctrinal/symboles/merkavah-muraqaba.md`, où le rapprochement **ʿArsh / Kissé
ha-Kavod** figure — mais comme **exemple de ce qu'il ne faut pas faire** :
construit sur une gématrie sans assise textuelle (« Merkavah = 267 → 6 ;
Muraqaba = 349 → 7 »), puis érigé en « archétype primordial commun ».

- **Ce que cela ne dit pas** : que le rapprochement soit faux. Il n'est pas jugé.
- **Ce que cela dit** : que **la mauvaise manière de l'établir est déjà
  documentée**, et qu'un ancrage sur ce terrain devra montrer explicitement qu'il
  ne procède pas ainsi.
- **Compréhension tirée** : avant d'ouvrir un chantier de rapprochement, **chercher
  d'abord si le dépôt en garde une version déviée**. Les fiches `deviations/` et
  les blocs ⚠️ sont une **carte des pièges déjà repérés** — les consulter en
  amont coûte une recherche et évite de refaire un chemin déjà balisé comme
  mauvais.

### 4.4 Deux manques de discipline, signalés et non corrigés

- **26 entrées d'annales** des 29-30 août **sans SHA de commit** (Cmd 9), 9 côté
  doctrinal, 17 côté atelier. Chaque SHA est retrouvable mécaniquement
  (`git log -S` sur le titre de l'entrée). **Non corrigé** : fichiers
  append-only, VIGILANCE impose de rapporter et de demander.
- **23 fiches doctrinales** absentes de `doctrinal/index.md` (21 `sources/`,
  2 `discernement/`), toutes antérieures à la session. Seules les fiches de la
  session ont été portées, au titre de l'Action ARCHIVAGE point 4.

## 5. Un défaut de process

**Les photos annoncées et jamais commitées.** Sidy a indiqué que des photos
étaient dans `_inbox/` ; je ne les voyais pas et l'ai dit ; il a répondu « tu n'as
même pas regardé ». Vérification faite : elles étaient **`git add`ées mais jamais
commitées** — donc réellement absentes de mon côté, et réellement présentes du
sien.

- **Compréhension tirée** : dans un flux à deux machines, `git add` sans commit
  crée un état où **les deux parties ont raison** et se contredisent. Le premier
  réflexe utile n'est pas « je ne les vois pas » mais **« voici ce que je vois,
  exactement »** — l'état `git status` brut, qui aurait montré les fichiers
  *staged* et tranché en une ligne.
- **Second point, sur la friction** : j'ai soulevé une réserve de protocole sur la
  permanence des photos dans l'historique git ; Sidy a tranché (« il n'y a rien de
  sensible, arrêtons de perdre du temps »). La réserve était légitime à énoncer
  **une fois** ; l'insister aurait été une faute. Le verdict rendu, il s'applique.

## 6. Ce qui a été évité — et qui compte autant

Trois erreurs n'ont **pas** été commises, chacune parce qu'une règle du dépôt a
tenu au moment exact où elle était coûteuse :

1. **Combler les cellules vides d'*Ājñā*** d'après la Planche VII. La table ne
   donne ni couleur de *tattva* ni forme de *maṇḍala* ; la planche montre un
   triangle inversé. Les combler aurait été **trancher que la planche prime la
   table** — un verdict, non un relevé. Cellules laissées vides, divergence
   consignée.
2. **Lire l'obliquité des ancrages comme un décalage-donnée** (§2.4).
3. **Conclure sur « Kursī = degré 11 »** avant collation (§4.2).

Les trois ont en commun d'avoir été **des raisonnements séduisants** — cohérents,
utiles, presque élégants. C'est le signal : un rapprochement qui « tombe juste »
sans coûter d'effort mérite une vérification de plus, pas une de moins.

## 7. Les cinq règles que cette session ajoute au métier

1. **Une affirmation négative sur une source se vérifie comme une positive.**
2. **Toute convention tacite devient un bug au deuxième cas** — l'écrire dans la
   donnée au moment où l'on ajoute le second, pas quand l'erreur se voit.
3. **Un plafonnement, un arrondi, une simplification de rendu doit être visible
   dans la forme.** Un commentaire de code n'est pas une signalisation.
4. **Donnée et présentation se distinguent par extrémité, pas par objet** — et
   une fonction qui *interprète* pour le lecteur est plus dangereuse qu'une qui
   affiche.
5. **Un marqueur de doute doit énoncer son périmètre**, faute de quoi il certifie
   tout ce qu'il ne couvre pas.

**Ajoutée le 2026-08-30, après la collation Gloton (§4.2, résolution) :**

6. **Un nombre lu sur une figure doit déclarer ce qu'il est** — rang de dessin,
   indice dans une série, ou numéro de degré. À défaut, un rang d'anneau se fait
   passer pour un degré et la fiche se contredit elle-même sans que rien ne le
   signale. Corollaire de méthode, plus coûteux encore : **avant de demander une
   collation à l'humain, vérifier que la page demandée porte bien l'information
   cherchée.** J'ai fait collationner les Figures — qui ne portaient pas de
   numérotation, et qui étaient la cause de l'erreur — quand la réponse était dans
   la table courante, trois pages plus tôt.

## 8. Ce qui reste ouvert

| Point | Attend |
|---|---|
| ~~Contradiction de numérotation de la table des 38 degrés (§4.2)~~ | ✅ **RÉSOLU 2026-08-30** — la contradiction n'existait pas dans la source ; ʿArsh = 17, Kursī = 18 ; chantier débloqué, données de l'Instrument déjà justes |
| ~~Attributions de chapitres XIX-XXI (§4.1)~~ | ✅ **RÉSOLU 2026-08-30** — table des matières collationnée : deux **éditions** coexistent (l'index web reproduit la 1ʳᵉ éd., 26 ch. ; l'exemplaire de Sidy en a 24). L'artère coronale est au **ch. XX** de l'exemplaire (= XXI en 1ʳᵉ éd.). La correction du 2026-08-30 matin, qui la plaçait en XXI, était juste dans le repère web et fausse dans celui de l'exemplaire |
| 26 entrées d'annales sans SHA (§4.4) | autorisation de réparer |
| 23 fiches absentes de l'index (§4.4) | autorisation de compléter |
| Faux positif [A6] (§3.2) | raffiner ou accepter |
| Cellules vides d'*Ājñā* (§6.1) | verdict planche vs table |
