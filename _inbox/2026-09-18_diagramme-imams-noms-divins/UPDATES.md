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
| 2 | `haqaiq-al-hadra-al-ilahiyya.jpg` | `doctrinal/symboles/assets-imams-noms-divins/` | **versement d'une pièce graphique** — verdict demandé au §7 |
| 3 | bloc du §6 ci-dessous | `doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md` | **enrichissement, ajout seul** — une entrée dans « À transcrire ultérieurement » |

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

**Conséquence** : la piste de Sidy est portée à la fiche **comme piste (🔍)**, jamais
comme source. Sa vérification appartient à l'exemplaire physique et à Sidy (§VII,
discipline des sources, point 2).

## 3. Ce qui a été lu sur la planche, et comment

La planche est lisible mais dense : une vingtaine d'intitulés sont inscrits en petit
corps, le long de segments obliques ou verticaux. Le relevé a été fait par **découpes et
rotations successives de l'image** (Pillow, script jetable en bac à sable hors dépôt),
chaque étiquette étant ramenée à l'horizontale avant lecture. Aucune forme n'a été
restituée de mémoire.

**Résultat** : 5 étages, 7 Imams numérotés, 3 cercles de *sadana* (22 Noms au total,
recoupements compris), 3 mondes, 2 Présences, **23 intitulés de *raqāʾiq***.

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

À insérer dans `doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md`,
section **« À transcrire ultérieurement »**, comme quatrième point — et `updated:` à
remonter au 2026-09-18 (Cmd 8) :

```
4. La **planche des Imams des Noms divins** (*حقائق الحضرة الإلهيّة — دوائر ورقائق
   أحكام أئمة الأسماء الإلهية*), dont Sidy indique (2026-09-18) qu'une traduction
   française figure dans le présent ouvrage. **Non vérifié** : la présente fiche n'en
   porte aucune trace, sa transcription couvrant les pp. 35–49 (28 degrés du
   *nafas al-raḥmān*). À relever sur l'exemplaire physique : **les pages**, et si la
   planche y est donnée en entier ou en partie. Le relevé arabe de la planche, fait
   sur l'iconographie de l'Ibn al-Arabi Foundation, vit en
   [[doctrinal/symboles/imams-noms-divins]] — deux intitulés de *raqīqa* y restent non
   levés, que la version française trancherait.
```

## 7. Deux verdicts demandés à Sidy

**(a) La planche est-elle versée au dépôt, et où ?** Deux options, et la règle de coupe
est le **format**, non le contenu (§II) :

- **`doctrinal/symboles/assets-imams-noms-divins/`** (proposé) — la planche est une
  **image de référence dépersonnalisée**, 287 Ko, versionnable, adjacente à la fiche
  qu'elle sert, citée **en prose par chemin relatif** et cible d'aucun wikilink. Elle
  est la **pièce justificative du relevé** : sans elle, la transcription n'est pas
  vérifiable par un tiers, ce qui est l'argument le plus fort pour la verser.
- **`raw/assets/`** (hors git) — si Sidy préfère ne pas versionner une planche éditée
  par un tiers. Le relevé reste alors invérifiable depuis Obsidian.

**Point à trancher par Sidy et par lui seul** : la planche porte la marque de l'**Ibn
al-Arabi Foundation**. Le dépôt est privé et l'usage est d'étude ; la machine n'a pas
qualité pour statuer sur ce qui engage (Cmd 13).

**(b) La réécriture de la fiche du 2026-06-20 est-elle acceptée ?** Elle **remplace** un
contenu, elle ne l'amende pas. Rien n'est perdu — git garde la version antérieure, et le
§4 ci-dessus en consigne la teneur écart par écart. Mais c'est une substitution, et elle
appelle un verdict (Cmd 10, Cmd 12).

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
   déplacer `haqaiq-al-hadra-al-ilahiyya.jpg`.
3. Si (b) = accepté : écrire `doctrinal/symboles/imams-noms-divins.md` (relecture du
   diff avant validation) ; ajuster le chemin relatif de la planche si (a) a retenu
   `raw/assets/`.
4. Appliquer l'ajout du §6 à la fiche source Gloton, `updated:` remonté.
5. `git add` des fiches **avant** régénération de l'index lexical et validation
   (ordre prescrit, `protocoles/annotations-html.md`).
6. `generer-index-lexical.py --sortie-md-eclate` puis `valider-annotations.py`.
7. `verifier-invariants.py` — attendu : **0 erreur**, avertissements ≤ 77 + n, chaque
   ligne nouvelle expliquée.
8. `carte-du-depot.py` — vérifier que la page conserve ses liens entrants.
9. Commit, puis **entrée d'annales** `## [2026-09-18] archivage | …` portant le SHA
   court en dernière ligne (Cmd 9 — l'entrée se rédige **après** le commit).
10. Vider le sas.
