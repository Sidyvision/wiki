# UPDATES — 2026-09-18 — Lot « Planche des Imams des Noms divins »

> Lot d'**ingest d'une pièce déposée en session** (planche iconographique transmise par
> Sidy le 2026-09-18). **Aucune écriture directe dans un circuit n'a été faite.**
> Le sas est une **proposition** : intégration fiche par fiche, chaque écriture relue
> (jamais d'auto-accept, §VIII.1), sur verdict de Sidy (Cmd 6, Cmd 13).

---

## 1. Objet — une fiche réécrite, une planche versée, un ajout proposé

| # | Pièce du sas | Cible proposée | Nature |
|---|---|---|---|
| 1 | `imams-noms-divins.md` | `doctrinal/symboles/imams-noms-divins.md` | **réécriture** d'une fiche existante (`created: 2026-06-20` préservé) |
| 2 | `haqaiq-al-hadra-al-ilahiyya.jpg` | `doctrinal/symboles/assets-imams-noms-divins/` | ✅ **VERSÉE** (287 Ko) — verdict de Sidy du 2026-09-18 |
| 3 | `gloton-figure-7-p97.jpg` | `doctrinal/symboles/assets-imams-noms-divins/` | ✅ **VERSÉE** (1,0 Mo) — photographie fournie par Sidy le 2026-09-18, §2 bis |
| 4 | bloc du §6 ci-dessous | `doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md` | **enrichissement, ajout seul** — une entrée dans « À transcrire ultérieurement » |

Origine : consigne de Sidy du 2026-09-18 — « fais l'ingest de ce diagramme », avec deux
indications à vérifier : (a) un commentaire de ChatGPT sur cette planche se trouverait
dans l'export versé en `meta/` ; (b) Gloton donne une traduction française de la même
planche dans *De la mort à la résurrection*, ouvrage qui devrait se trouver au dépôt.

## 2. Ce que la recherche préalable a établi (avant toute écriture)

**(a) Le commentaire ChatGPT est déjà au dépôt — sous forme de fiche, pas d'export.**
`raw/` est vide en session (l'archive ZIP de l'export vit sur le serveur, `/raw/*` étant
exclu de git) et le triage `meta/projet-unifie/archives/triage-chatgpt-export.md` ne
recense aucune conversation dont le titre porte sur les Noms divins. En revanche
`doctrinal/symboles/imams-noms-divins.md` existe depuis le **2026-06-20**, et son propre
texte se déclare « commenté à partir d'un diagramme intitulé *Les réalités de la Présence
divine — Cercles et feuilles des jugements des Imams des Noms divins* » : c'est **ce
commentaire-là**, déjà ingéré. Le lot ne l'ajoute donc pas : il le **confronte à la
planche**.

**(b) La traduction Gloton n'est PAS au dépôt.** La fiche
`doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md` (44,7 Ko,
`created: 2026-07-01`) transcrit les pp. 35–49 de l'ouvrage, consacrées aux **28 degrés
du *nafas al-raḥmān*** et aux 28 *manāzil al-qamar* — matière entièrement distincte.
Contrôle mécanique : `grep -cE "raqiq|raqā|imam|imâm|jawad|muqsit|sadana|سدنة|رقيقة|أئمة"`
sur cette fiche rend **0**. La planche n'y a laissé aucune trace. L'ouvrage est par
ailleurs bien recensé au catalogue physique (`atelier/rd/bibliotheque/catalogue-bibliotheque.md`,
l. 90, statut CONFIRMÉ 2026-07-01), mais le catalogue **n'établit ni ne lève rien** par
lui-même (§VII.1).

**Conséquence, à l'heure de ce constat** : la piste de Sidy a d'abord été portée à la
fiche **comme piste (🔍)**, sa vérification appartenant à l'exemplaire physique. Sidy a
produit cette vérification le jour même. **Voir le §2 bis : elle corrige ce que le
présent paragraphe laissait supposer.**

## 2 bis. La vérification de Sidy — et ce qu'elle corrige

Sidy a photographié la pièce : **Figure 7, p. 97**, légendée « *L'aspect de la présence
des Noms divins, ce bas monde, le monde ultime et l'Isthme (barzakh)* ». Elle est versée
au sas (`gloton-figure-7-p97.jpg`).

**Ce que j'avais laissé entendre, et qui est faux.** Le §2 (b) établissait — et
établit toujours — que la traduction de cette planche n'est pas au dépôt. J'en ai
implicitement conclu qu'elle était **ailleurs dans le même ouvrage**, et que la
collation consisterait à la retrouver. La photographie montre autre chose : la figure
de Gloton porte la **même doctrine**, les **sept mêmes Imams**, et **n'est pas la même
figure**.

**Quatre différences, vérifiées sur les deux pièces :**

1. **Neuf Noms au lieu de sept.** Les sept Imams numérotés de la planche arabe se
   retrouvent **un à un** (الحي/Vivant, العالم/Savant, المريد/Volontaire,
   القائل/Parlant, القادر/Puissant, الجواد/Libéral, المقسط/Répartiteur). La Figure 7
   en ajoute **deux : Organisateur et Séparateur**, tous deux **sur l'axe** — c'est-à-dire
   à la place exacte que la planche arabe laisse vide, n'y inscrivant que des *raqāʾiq*.
2. **Aucune *raqīqa*, aucune liaison tracée.** La Figure 7 ne dessine **aucun segment**
   entre ses cercles, là où la planche arabe trace chaque liaison **et la nomme** — les
   23 intitulés du §3. Le terme technique de la planche arabe est absent de la figure
   française.
3. **Aucun cercle de *sadana*.** Les 22 Noms des trois cercles de gardiens n'ont aucune
   contrepartie.
4. **Registre terminal différent.** La planche arabe : العالم المطلق, les deux mondes
   conditionnés, حضرة الجنة والإيمان / حضرة النار والكفر. La Figure 7 : un anneau
   **Intermonde / Barzakh** (le même cercle nommé deux fois, en français au-dessus et en
   arabe en dessous) autour du disque **Ce bas monde**, puis **La terre du
   Rassemblement**, **Le Jardin**, **Le Feu**.

**Les deux titres diffèrent aussi**, et c'est un indice de plus : حقائق الحضرة الإلهية —
دوائر ورقائق أحكام أئمة الأسماء الإلهية d'un côté ; « L'aspect de la présence des Noms
divins, ce bas monde, le monde ultime et l'Isthme (*barzakh*) » de l'autre.

**Ce qui reste ouvert, et qui n'est pas rien** : l'ouvrage porte une **série numérotée
de figures** — celle-ci est la **septième** — et le dépôt n'en transcrit que les
pp. 35–49. **Rien n'exclut qu'une autre figure du même ouvrage corresponde à la planche
arabe.** Cela se tranche en photographiant les autres figures, pas en raisonnant. À quoi
s'ajoute une question de situation : le texte transcrit au dépôt couvre les pp. 35–48
(ch. 198, sections 11–38) ; **de quelle partie du livre la p. 97 relève-t-elle ?**

**Un écart déclaré, non comblé** (Cmd 12) : la forme originale d'**Organisateur** et de
**Séparateur** n'est pas établie. Elle ne se conjecture pas depuis le français — un Nom
divin restitué à l'estime serait une faute plus grave que le blanc. Elle se prend sur la
page arabe en regard dans l'ouvrage, ou sur le texte primaire.

**Une latéralité relevée, non interprétée.** Sur les deux figures, الجواد/Libéral est à
droite et المقسط/Répartiteur à gauche — ce rang concorde. En pied, elles s'inversent :
la planche arabe met النار à gauche et الجنة à droite, la Figure 7 met **Le Jardin à
gauche et Le Feu à droite**. Deux raisons interdisent d'en conclure quoi que ce soit :
la Figure 7 **ne trace aucun segment**, de sorte que sa disposition peut n'être que
typographique ; et aucun examen du dépôt n'a superposé ces latéralités.

⚠️ **Rectification (même jour, §2 ter).** J'avais invoqué à l'appui la vigilance des
annales du 2026-08-04 (« Imâms akbariens avec inversion »). **Elle ne porte pas sur
cette planche** — elle vise le ternaire de la Khuṭba, *Qutb* + Imâm de droite + Imâm de
gauche, où Vâlsan note que l'Imâm de gauche est le plus élevé. Deux structures que seul
le mot *Imâm* rapproche. La citation est retirée de la fiche et remplacée par cette
distinction, qui vaut mieux que l'appui qu'elle prétendait donner.

## 3. Ce qui a été lu sur la planche, et comment

La planche est lisible mais dense : une vingtaine d'intitulés sont inscrits en petit
corps, le long de segments obliques ou verticaux. Le relevé a été fait par **découpes et
rotations successives de l'image** (Pillow, script jetable en bac à sable hors dépôt),
chaque étiquette étant ramenée à l'horizontale avant lecture. Aucune forme n'a été
restituée de mémoire.

**Résultat** : 5 étages, 7 Imams numérotés, 3 cercles de *sadana* (22 Noms au total,
recoupements compris), 3 mondes, 2 Présences, **23 intitulés de *raqāʾiq***.

La **Figure 7 de Gloton**, arrivée ensuite (§2 bis), est en typographie d'imprimerie et
se lit sans traitement : deux agrandissements ont suffi à vérifier les hauteurs de rang
(quatre cercles alignés au premier rang latéral, deux au second, deux Noms sur l'axe) et
l'absence de tout segment de liaison.

**Deux intitulés sont déclarés non levés**, et le restent :

- `رقيقة إيجاد المعابر (?)` — le mot final se lit **المعابر** ou **المعايير**, la
  résolution de la planche ne tranche pas.
- `رقيقة الحكم (?)` — deux occurrences symétriques (versant gauche et versant droit),
  dont seul le second mot est pleinement lisible.

C'est la règle qui commande ici, pas la gêne du blanc : *une forme originale ne se
restitue ni de mémoire ni par un modèle ; elle se prend au texte, ou elle se déclare
absente* (§VII, discipline des langues originales, point 4). **Une écriture originale
ajoutée sans source est une faute plus grave que son absence.**

**Un piège de typographie signalé, parce qu'il a failli produire une faute.** Dans la
graphie de la planche, la hamza de **إيجاد** se réduit à une marque fine au-dessus de
l'alif : à faible résolution, `رقيقة إيجاد النعيم` se lit **أعياد النعيم** (« les fêtes
de la félicité »), qui est un contresens et qui se serait transmis comme s'il était
juste. Le cas a été tranché par un agrandissement dédié.

## 4. Confrontation — six écarts entre la planche et la rédaction du 2026-06-20

La rédaction antérieure procède d'un **commentaire de modèle conversationnel**, réputé
**reconstruction plausible et non source** (§VII, discipline des sources, point 3). Elle
portait d'ailleurs elle-même ses réserves : `sources: ["to-source"]`, tag
`citations-a-verifier`, deux « citation non vérifiée » au corps. La confrontation
**confirme ces réserves et les précise**.

| # | Rédaction du 2026-06-20 | Ce que la planche porte |
|---|---|---|
| 1 | « les cinq grands Imams (pentarchie) », dont un cinquième **al-Muḥkim/al-Mukhaṣṣiṣ** | **Sept Imams numérotés** (الأول … السابع). **المحكم** et **المخصص** ne sont pas des Noms : ce sont les **titres fonctionnels** inscrits au-dessus de *al-ʿĀlim* (2ᵉ) et de *al-Murīd* (3ᵉ) |
| 2 | *al-Jawād* et *al-Muqsiṭ* = « Noms opératifs intermédiaires », hors des Imams | Ils sont les **6ᵉ et 7ᵉ Imams**, sous les titres **الإمام المنعم** et **الإمام العادل** |
| 3 | « Sphère de Rigueur (al-ʿAdl, al-Ḥikma, al-Qudra) » | Ce cercle n'existe pas. Le cercle de gauche est **سدنة الغضب** : المذل، المحصي، الشديد العقاب، الحسيب، الضار، المعذب — **aucun des trois Noms cités** |
| 4 | Sphère de Miséricorde : 5 Noms | **سدنة الرضى** en porte **7** : les 5 cités, plus **المنعم** et **الستار** |
| 5 | Sphère centrale mixte : 7 Noms | Le cercle central en porte **9** : les 7 cités, plus **المذل** et **الضار** |
| 6 | **rien** sur un cinquième étage | La planche porte **trois mondes** (العالم المطلق, العالم المقيد بالسعادة, العالم المقيد بالشقاوة) et **deux Présences** (حضرة الجنة والإيمان, حضرة النار والكفر) — c'est-à-dire précisément la charnière eschatologique, absente du commentaire |

**Deux formulations données entre guillemets par la rédaction antérieure ne figurent pas
sur la planche** : *tashābuk al-aḥkām* (« entrelacement des jugements ») et la sentence
« le châtiment n'est jamais sans science ni sagesse ». Elle les marquait « citation non
vérifiée » ; la confrontation permet d'être plus net : **elles ne viennent pas de là**.

**Et un écart de traduction, qui est le plus instructif.** La rédaction antérieure
traduit le titre de la planche par « Cercles et **feuilles** des jugements ». Le titre
porte **دوائر ورقائق** : **رقائق** est le pluriel de **رقيقة**, la *liaison subtile*, et
non de **ورقة**, la feuille. Ce n'est pas un détail de lexique : la planche emploie ce
mot une vingtaine de fois pour nommer chacun de ses segments — **c'est son terme
technique propre**, et il était intégralement absent du commentaire. La page réécrite
le restitue comme colonne vertébrale du relevé.

## 5. Ce que la fiche réécrite fait, et ne fait pas

**Fait** : elle relève ce que la planche porte, forme par forme, dans son écriture
d'origine, avec les numéros d'ordre, les titres fonctionnels et les 23 *raqāʾiq*. Elle
porte le double contrôle du §VII (qualification sashimono : **kari-kumi** intégral,
aucun joint *hozo* posé ; confrontation Gizeh : **due, car la matière est septénaire** —
résultat 🔍 *aucun ancrage sourcé*, consigné y compris négatif).

**Ne fait pas** : elle ne tranche rien. Elle ne rapproche pas les sept Imams du
septénaire transversal pourtant **tranché** au dépôt (Balance, degré du Soleil,
Ourse/Pléiades, verdict du 2026-08-03) — ce rapprochement serait un lien
inter-traditionnel non instruit, que le **Cmd 3** interdit de supposer. Elle ne
qualifie pas la latéralité droite/gauche de la planche, les annales du 2026-08-04
ayant déjà déclaré les latéralités du dépôt **non superposables**, « Imâms akbariens
avec inversion » nommément compris.

**Cartouche** : `created: 2026-06-20` **préservé** (Cmd 8), `updated: 2026-09-18`,
`sources: ["to-source"]` maintenu (référence primaire non établie — le seul des trois
cas que le cartouche prend en charge, `doctrinal/CLAUDE.md`), tag `citations-a-verifier`
**maintenu** puisque l'attribution même de la planche reste à établir, ajout de
`original: ["أئمة الأسماء الإلهية"]` — syntagme déclaré **entier** (§VII, discipline des
langues originales, point 7), pris sur le titre de la planche.

**Aucune annotation HTML n'a été posée**, et c'est délibéré : la fiche est
majoritairement du **texte relevé**, que la règle 5 du §VII interdit d'annoter ; et le
validateur `valider-annotations.py` **ignore `_inbox/`**, de sorte qu'une annotation
posée dans le sas serait une pièce non éprouvée. Elles se poseront, s'il y a lieu, à
l'intégration — après `git add`, dans l'ordre prescrit.

## 6. Ajout proposé à la fiche source Gloton (ajout seul, rien de retiré)

La fiche source décrit un ouvrage dont elle ne transcrit que les pp. 35–49. La
photographie de Sidy y ajoute un fait daté : **il existe une Figure 7, p. 97**, et
l'ouvrage porte donc une série numérotée de figures dont le dépôt ne connaît rien.
Deux gestes, tous deux en **ajout seul**, et `updated:` à remonter au 2026-09-18 (Cmd 8).

**(a)** Dans la section **« À transcrire ultérieurement »**, comme quatrième point :

```
4. La **série des figures de l'ouvrage**, dont le dépôt ne connaît aujourd'hui qu'un
   membre. **Figure 7, p. 97** — « L'aspect de la présence des Noms divins, ce bas
   monde, le monde ultime et l'Isthme (barzakh) » — photographiée par Sidy le
   2026-09-18 et relevée en [[doctrinal/symboles/imams-noms-divins]], section « Mise
   en regard ». Restent à relever sur l'exemplaire : **les figures 1 à 6 et
   au-delà** (l'une d'elles correspond-elle à la planche arabe des Imams ?) ; **la
   partie du livre dont relève la p. 97**, le texte transcrit ici couvrant les
   pp. 35-48 (ch. 198, sections 11-38) ; et **la page arabe en regard de la Figure 7**,
   seule à pouvoir donner la forme originale des deux Noms « Organisateur » et
   « Séparateur », sans contrepartie sur la planche arabe.
```

**(b)** Dans la section **« Concepts liés »**, une entrée :

```
- [[doctrinal/symboles/imams-noms-divins]] — les sept Imams des Noms divins ; la
  Figure 7 de cet ouvrage (p. 97) y est mise en regard d'une planche arabe de l'Ibn
  al-Arabi Foundation. Les deux figures portent la même hiérarchie et ne sont pas la
  même figure.
```

⚠️ **Ce que cet ajout ne fait pas** : il n'ajoute rien au champ `sources:` de la fiche
source et ne touche à aucune de ses transcriptions. La Figure 7 **ne lève pas** le
`to-source` de la planche arabe (§7 c ci-dessous).

## 6 bis. Rapprochement kabbalistique — ce que la recherche a rendu

Consigne de Sidy (2026-09-18) : chercher une relation avec les **sentiers de la Kabbale**,
« notamment ce que nous avions vu au sujet des sentiers de Tiferet ». La pièce visée
existe : 🔍 [[doctrinal/discernement/2026-08-30_nadis-du-coeur-sentiers-sephirothiques-tiferet]]
(`speculatif`, **(P1) tranché le 2026-08-30** — sentiers séphirothiques et *nâdîs* sont
deux projections complémentaires d'un même réseau, *kumiko* ; **(P2) non rendu**).

Le relevé complet est porté à la fiche, section « Rapprochement avec l'Arbre
séphirothique ». Résumé de ce qui s'y trouve, et surtout de ce qui **ne** s'y trouve pas.

**Ce qui se relève (🔍, *kari-kumi*)** :

1. **La planche est nativement une structure de stations et de voies** — *دوائر ورقائق*
   dans son titre même —, c'est-à-dire du même genre formel que l'Arbre, sur le versant
   où le discernement de Tiferet fait porter toute sa distinction.
2. **La latéralité qualitative concorde sur ses trois termes** : droite = Miséricorde /
   **سدنة الرضى** ; gauche = Rigueur / **سدنة الغضب** ; milieu = Équilibre / le cercle
   central, qui porte des Noms **des deux** côtés (المنعم avec la droite, المذل et الضار
   avec la gauche) et dont la liaison se nomme **رقيقة الجمع بين النفع والضرر**, *le lien
   de la réunion du profit et du dommage*. C'est la fonction que l'Arbre donne à sa
   colonne du milieu et à **Tiferet** en son centre.

**Ce qui est refusé, et dit avant d'y penser** : la planche porte 23 intitulés relevés,
l'Arbre 22 sentiers. **Le rapprochement n'est pas fait.** La recherche de concordances
chiffrées est écartée **par construction** au dépôt, et le discernement de Tiferet
nomme cette pente « celle qu'il ne faut pas prendre ». Deux raisons propres s'y ajoutent :
deux de mes 23 lectures sont **réservées**, et *رقائق الإمداد* est un **pluriel** — 23
n'est pas même un nombre ferme.

**Ce qui ne concorde pas, posé avec la même netteté** : les sentiers portent des
**lettres**, les *raqāʾiq* des **أحكام** (jugements) — différence de nature ; et **il n'y
a pas de station centrale cardiaque sur l'axe** de la planche, le 6ᵉ Imam (**الجواد**)
étant à droite et non au milieu. Chercher un « Tiferet » en comptant jusqu'à six ne
donne rien.

**Un signalement assorti de son avertissement** : que les voies portent des lettres d'un
côté et des jugements de l'autre a la forme d'une **inversion du lettrique**. Le
discernement de Tiferet a posé une inversion de ce genre, puis l'a **retirée le jour
même** — « un artefact de mon propre découpage ». Le précédent est daté ; l'observation
est donc consignée comme signalement, jamais comme appui. Et l'autre structure islamique
du dépôt, les **28 degrés du *nafas al-raḥmān*** (même ouvrage de Gloton), met les
lettres sur les **stations** : de quoi interdire toute généralisation sur « le côté
islamique ».

**Blocage de fond, inchangé** : le dépôt **ne documente pas les 22 sentiers** —
[[doctrinal/sources/kabbale-10-sefirot-structure]] le dit d'elle-même — et la tradition
en connaît plusieurs arrangements incompatibles. **Aucune mise en correspondance des
voies n'est possible aujourd'hui.**

**Une erreur de ma part, rectifiée en chemin** (§2 ter) : j'avais invoqué la vigilance
des annales du 2026-08-04, « Imâms akbariens avec inversion », comme si elle portait sur
cette planche. Elle vise le **ternaire de la Khuṭba** (*Qutb* + Imâm de droite + Imâm de
gauche), une autre structure que seul le mot *Imâm* rapproche des sept Imams des Noms.
La citation est retirée des deux pièces et remplacée par la distinction.

**Ce que je ne fais pas** : ouvrir une fiche `discernement`. Un lien structurel entre
traditions l'exige (Cmd 3), mais il exige aussi un verdict, et deux préalables manquent —
l'arrangement des sentiers et le rattachement primaire de la planche. La proposition
qu'un examen aurait à instruire est formulée en fin de section : *le cercle central des
sadana et la colonne du milieu remplissent une même fonction de réunion des deux
versants* — testable, et réfutable si le rattachement primaire donne à la planche une
autre économie.

## 7. Trois verdicts demandés à Sidy

**(a) Les deux pièces sont-elles versées au dépôt, et où ?** La règle de coupe est le
**format**, non le contenu (§II) :

- **`doctrinal/symboles/assets-imams-noms-divins/`** (proposé) — ce sont des **images
  de référence dépersonnalisées**, versionnables, adjacentes à la fiche qu'elles
  servent, citées **en prose par chemin relatif** et cibles d'aucun wikilink. Elles
  sont la **pièce justificative du relevé et de la mise en regard** : sans elles, ni la
  transcription arabe ni la comparaison ne sont vérifiables par un tiers. C'est
  l'argument le plus fort pour les verser.
- **`raw/assets/`** (hors git) — si Sidy préfère ne pas versionner des pièces éditées
  par des tiers. Le relevé reste alors invérifiable depuis Obsidian.

Deux réserves de forme, s'il y a versement : la photographie de la Figure 7 pèse
**1,0 Mo** et gagnerait à être recompressée (le texte y reste lisible bien en deçà) ;
et elle **montre l'environnement de la prise de vue** (main, étagère) — un recadrage sur
la seule page serait plus juste pour une pièce d'étude.

**Point à trancher par Sidy et par lui seul** : la planche arabe porte la marque de
l'**Ibn al-Arabi Foundation**, et la Figure 7 est une page d'un ouvrage sous droits
(Albouraq). Le dépôt est privé et l'usage est d'étude ; la machine n'a pas qualité pour
statuer sur ce qui engage (Cmd 13).

**(b) La réécriture de la fiche du 2026-06-20 est-elle acceptée ?** Elle **remplace** un
contenu, elle ne l'amende pas. Rien n'est perdu — git garde la version antérieure, et le
§4 ci-dessus en consigne la teneur écart par écart. Mais c'est une substitution, et elle
appelle un verdict (Cmd 10, Cmd 12).

**(c) La Figure 7 lève-t-elle quelque chose ?** Ma réponse est **non**, et je la donne
comme proposition, non comme verdict. Elle établit qu'un texte traduit par Gloton porte
la **même hiérarchie de sept Noms** — ce qui est un appui réel. Elle n'établit **pas**
que la planche arabe procède de ce texte : les deux figures diffèrent sur quatre points
(§2 bis), et la planche arabe reste sans référence textuelle. Le `to-source` du
cartouche est donc **maintenu**. Si Sidy juge au contraire que la concordance un à un
des sept Imams suffit à rattacher la planche, c'est un verdict qui lui revient (§VII,
discipline des sources, point 2 : la levée du marqueur n'appartient jamais à la
machine).

## 7 bis. Les deux pièces sont versées — verdict rendu

**Verdict de Sidy, 2026-09-18** : « Tu peux verser aux assets doctrinal, pas raw. »
Le §7 (a) est donc **tranché**, et exécuté : `doctrinal/symboles/assets-imams-noms-divins/`
contient désormais `haqaiq-al-hadra-al-ilahiyya.jpg` (287 Ko) et
`gloton-figure-7-p97.jpg` (1,0 Mo).

**Ce que le versement rend vrai** : les chemins relatifs cités en prose dans la fiche
résolvent **une fois la fiche à sa place** (`doctrinal/symboles/`). Tant qu'elle attend
au sas, les deux pièces sont en place et la fiche ne l'est pas — état transitoire, à
refermer par le verdict (b).

**Rappel du refus antérieur, pour mémoire et non comme obstacle** : une première
tentative de pousser la photographie de la p. 97 avait été refusée par le garde-fou du
poste d'intégration (publication d'une page d'ouvrage sous droits). Le refus n'avait pas
été contourné — la pièce avait été retirée du commit et l'écart déclaré. **Le verdict de
Sidy lève la question** : le dépôt est privé, l'usage est d'étude, et la décision
appartenait à l'humain (Cmd 13), non à la machine.

**Deux réserves de forme maintenues, sans effet bloquant** : la photographie de la p. 97
pèse 1,0 Mo et montre l'environnement de la prise de vue (main, étagère). Elle est versée
**telle que reçue** — recadrer ou recompresser une pièce reçue sans qu'on l'ait demandé
serait altérer un document, et le gain de poids ne le justifie pas. Le recadrage reste
disponible sur un mot de Sidy.

## 8. Signalement annexe (Cmd 9, non corrigé)

`doctrinal/symboles/imams-noms-divins.md` est recensée à `doctrinal/index.md` (l. 68)
mais **aucune entrée d'annales ne la nomme** — ni sa création du 2026-06-20, ni depuis.
Écart relevé, **non corrigé d'office** : une entrée d'annales se rédige après le commit
qu'elle décrit, et une entrée décrivant une opération passée non journalisée en son
temps ne se fabrique pas après coup. L'intégration du présent lot fournira l'occasion
de journaliser la page pour la première fois.

## 9. Contrôle mécanique

`verifier-invariants.py` avant le lot : **0 erreur, 77 avertissements**. Le sas
`_inbox/` n'est pas dans le périmètre des contrôles de cartouche ; le chiffre est
rapporté comme **base de comparaison** pour l'intégration, non comme validation des
pièces du sas.

**Hygiène Unicode (Cmd 15) — contrôle éprouvé par l'échec** (§VII, épreuve des
contrôles). Le balayage des invisibles (U+200B/C/D, U+FEFF, U+200E/F) sur les deux
`.md` du sas rend **0**. Le même balayage, relancé sur une **copie jetable** en bac à
sable où un ZWSP avait été inséré exprès dans le titre H1, rend **`REFUS UPDATES.md:
ZWSP x1`**. Vert sur l'état sain, refus sur la faute fabriquée : le contrôle est
éprouvé, non supposé.

## 10. Ordre d'intégration proposé

1. Verdict sur le §7 (a) et (b).
2. Si (a) = versement : créer `doctrinal/symboles/assets-imams-noms-divins/` et y
   déplacer **les deux** pièces — `haqaiq-al-hadra-al-ilahiyya.jpg` et
   `gloton-figure-7-p97.jpg`, cette dernière recadrée et recompressée si Sidy le juge
   bon (§7 a).
3. Si (b) = accepté : écrire `doctrinal/symboles/imams-noms-divins.md` (relecture du
   diff avant validation) ; ajuster le chemin relatif de la planche si (a) a retenu
   `raw/assets/`.
4. Appliquer les **deux** ajouts du §6 à la fiche source Gloton (« À transcrire
   ultérieurement » et « Concepts liés »), `updated:` remonté. Rien n'est retiré, et le
   champ `sources:` n'est pas touché.
5. `git add` des fiches **avant** régénération de l'index lexical et validation
   (ordre prescrit, `protocoles/annotations-html.md`).
6. `generer-index-lexical.py --sortie-md-eclate` puis `valider-annotations.py`.
7. `verifier-invariants.py` — attendu : **0 erreur**, avertissements ≤ 77 + n, chaque
   ligne nouvelle expliquée.
8. `carte-du-depot.py` — vérifier que la page conserve ses liens entrants.
9. Commit, puis **entrée d'annales** `## [2026-09-18] archivage | …` portant le SHA
   court en dernière ligne (Cmd 9 — l'entrée se rédige **après** le commit).
10. Vider le sas.
