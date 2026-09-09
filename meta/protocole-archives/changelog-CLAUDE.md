---
title: "Changelog du protocole CLAUDE.md (racine)"
type: meta
tags: [protocole, historique, changelog]
created: 2026-08-28
updated: 2026-09-09
---

# Changelog du protocole `CLAUDE.md` (racine)

Historique des révisions du protocole racine. Migré hors du préambule de
`CLAUDE.md` le 2026-08-28 pour alléger le contexte chargé à chaque session —
le protocole racine ne conserve qu'un en-tête de statut court avec pointeur
vers le présent fichier. Append-only, ordre chronologique inverse : toute
nouvelle révision du protocole y est consignée immédiatement après le marqueur
ci-dessous (convention d'insertion, amendement 2026-07-27).

<!-- INSERTION: EN-TÊTE -->

## [2026-09-09] amendement | §VII — L'axe de la LANGUE, distinct de celui de la tradition ; ratification des 42 unanimes

**Deux verdicts de Sidy**, 2026-09-09 : « ratifie les 42 unanimes » et « une alternative
serait de classifier par langue plutôt que par tradition, puisque chaque tradition trouve
son véhicule en une langue ».

**Le second est un amendement de principe, et il explique un échec mesuré la veille.** La
tentative de dériver la tradition d'un terme du consensus des fiches qui le citent avait
donné 110 divergences sur 160 — `barzakh` sortant `islam 36 / universel 12 / kabbale 2`.
Le verdict de Sidy en donne la raison exacte : **la langue est une propriété du TERME, la
tradition une propriété du CADRE où on le cite.** Les fiches comparatives déclarent
`universel` comme cadre de *leur propos*, non comme origine des termes qu'elles
rassemblent. La méthode ne mesurait donc pas ce qu'on lui demandait — et l'axe proposé
n'est pas un contournement, c'est la correction de l'objet.

**Ce qui est institué** : l'index porte **deux champs distincts, jamais fondus** —
`tradition` (le cadre) et `langue` (la langue du terme). `langue` n'est posée que sur
trois sources, chacune **déclarée avec la valeur** : (1) le champ **`original:` du Sceau**
(§IV) de la fiche dont le slug est le terme, l'écriture y donnant la langue ; (2) la
langue **énoncée en prose** ; (3) l'écriture de la **forme appariée** (`apparie` ou
`jurjani`). **Aucune quatrième voie**, et en particulier aucune déduction depuis la
graphie de la translittération (`al-`, `ḥ`, `ṣ`) : ce serait une heuristique d'orthographe,
et une heuristique n'est pas une source (Cmd 5).

**Seules les écritures EXCLUSIVES donnent la langue.** Le **han** est écarté : il sert le
chinois *et* le japonais, et `巴` y avait été déclaré « chinois » alors que *tomoe* est
japonais — constaté à la première génération, retiré. *Une écriture partagée ne source pas
une langue : elle source une écriture, ce qui n'est pas la même chose.* Le devanagari est
retenu bien qu'il serve aussi le hindi, parce que dans ce dépôt il ne porte que du
sanskrit — mais c'est un fait de **corpus**, non d'écriture, d'où la provenance toujours
déclarée à côté de la valeur.

**Conséquence architecturale, et c'est le fait à retenir.** La couverture de l'axe est
aujourd'hui faible — **52 termes** — parce que le dépôt n'énonce presque jamais la langue.
Mais il a déjà l'endroit pour le faire : **le champ `original:`**, ouvert la veille.
**L'axe de la langue se renforce donc exactement au rythme de la discipline des langues
originales, sans travail propre** : chaque `original:` posé donne la langue de son terme.
Deux amendements écrits à un jour d'intervalle, et le second se nourrit du premier sans
qu'on l'ait prévu.

**Ratification des 42 unanimes.** Table `traditions-ratifiees.json`, lue par le générateur,
qui **prime toute dérivation** et marque le degré `ratifie-sidy` : **la source est le
verdict**, non le décompte qui l'a préparé. Les clés `<dfn>` portant une tradition sourcée
passent de **33 à 75 sur 160**.

**Neuf de ces ratifications sont signalées sous réserve** dans la table elle-même :
`bhutas`, `matras`, `sat-chit-ananda`, `avarna`, `ativarna`, `swastika`, `mahatma`,
`upaguru` portent `universel` alors que leur écriture d'origine est **sanskrite** ;
`hokhmah` alors qu'elle est **hébraïque**. C'est le biais structurel mesuré, sous une
autre forme : l'unanimité vient de fiches guénoniennes comparatives. **Signalées, non
modifiées** — une ratification est un verdict de Sidy, pas une mesure, et la corriger
d'office serait substituer la machine à lui. L'axe langue les tranchera de lui-même dès
que leur `original:` sera posé.

**Réversibilité (Cmd 10)** : la table de ratification est un fichier de données ; le champ
`langue` est additif et régénérable. Les deux se retirent sans toucher une seule fiche.

## [2026-09-09] amendement | §VII — `S1`, signalement de doublon de référent (et non refus)

**Motif** : l'angle mort le plus large qui restait à la clôture de la passe d'annotation,
identifié et rapporté la veille. **`D5` garantit l'unicité de la CLÉ, jamais celle du
RÉFÉRENT** : `guenon` et `rene-guenon` désignent la même personne sous deux clés
distinctes, et D5, qui compte par clé, ne le voit pas. Le cas avait dû être écarté **à la
main** lors de l'annotation de `autorites/`.

**Ce qui est institué** : `S1`, qui relève les paires coannotées dans une même fiche dont
l'une est **composant** de l'autre.

**Et c'est un SIGNALEMENT, non un refus — le point est le fond de l'amendement.** La
mesure préalable sur les 936 annotations du dépôt donne **6 paires**, et elles ne sont
pas de même nature :

| paire | lecture |
|---|---|
| `burckhardt` / `titus-burckhardt` | **même personne** — doublon vrai |
| `janus` / `janus-bifrons` | même figure sous deux formes — doublon probable |
| `rijal` / `rijal-allah` | *rijāl* et *rijāl Allāh* — termes voisins, distincts ? |
| `yuga` / `kali-yuga` (×2), `yuga` / `satya-yuga` | **genre et espèce** — parfaitement légitime |

**La moitié des cas relevés sont légitimes.** En faire un refus aurait interdit d'annoter
un genre à côté de son espèce — une contrainte que rien dans le protocole ne fonde, et
qui aurait été découverte seulement en butant dessus. Distinguer un doublon d'un rapport
générique est un **jugement**, réservé à Sidy (Cmd 12) : le contrôle **montre la paire, il
ne tranche pas**.

**Conséquence de forme** : `valider-annotations.py` (v1.3) sépare désormais deux canaux —
les **refus**, qui sortent en code 2, et les **signalements**, qui s'impriment sur la
sortie standard et laissent le code à 0. Les signalements s'impriment **toujours**, y
compris quand tout est vert : *un signalement tu est un signalement perdu*.

**Épreuve** — *vert et silencieux* : bac à sable ne contenant qu'une fiche à annotation
unique, **aucun signalement**. *Déclenchement* : bac à sable portant `guenon` et
`rene-guenon` coannotés — **le signalement paraît, nommant la paire**, et le code reste
**0**, ce qui est le comportement attendu d'un signalement. Sur le dépôt vivant : 6
signalements, 0 anomalie, code 0.

**Ce que S1 ne voit pas**, et qui est déclaré : deux clés désignant le même référent
**sans partager de composant** (`Ibn ʿArabī` et `al-Shaykh al-Akbar`, par exemple) lui
échappent entièrement. Le signal est la **containment lexicale**, pas l'identité — il
attrape une famille de cas, non toutes. Rapporté (Cmd 12).

**Réversibilité (Cmd 10)** : signalement additif, sans effet sur le code de sortie ni sur
aucune fiche ; se retire sans trace.

## [2026-09-09] amendement | §VII — `categorie-editoriale`, seul mot ajouté au vocabulaire d'annotation

**Verdict de Sidy**, 2026-09-09 : « ajoute un genre pour les catégories éditoriales ».
Complète l'amendement du même jour ci-dessous, qui avait laissé ce manque **rapporté et
non comblé** — le champ `type:` de `hermeneutique/CLAUDE.md` ne nommant pas cette
catégorie, l'inventer d'office aurait été un mot de la machine et non du protocole.

**Ce qui est institué** : un sixième genre propre à `hermeneutique/`,
**`categorie-editoriale`** — la catégorie de publication ou de classement sous laquelle
une œuvre paraît ou se range : *shōnen*, *seinen*, *thriller*, *gothique*, *comédie*,
*roman*. **10 poses** dans le circuit.

**C'est le seul mot de tout ce vocabulaire qui ne vienne pas du protocole**, et il est
donc le seul à devoir **porter sa limite dans son nom**. Il la porte : *éditoriale* dit
que la catégorie est celle du **marché du livre et de l'édition**, jamais une catégorie
de connaissance. Un *shōnen* n'est pas une `ecole`, et les confondre serait exactement la
faute de catégorie que le Cmd 3 poursuit — d'autant que ce circuit y est soumis avec une
rigueur accrue.

**Deux noms voisins écartés pour collision**, et la raison mérite d'être consignée :
`registre` est **déjà un champ du Sceau herméneutique** (`registre: analyse | expression`)
et l'employer aurait créé deux sens pour un même mot dans un même circuit ; `genre` seul
se serait confondu avec `data-genre`, l'attribut qui le porte.

**Ce que le mot ne couvre pas, et qui reste sans genre** (Cmd 12) : un **métier**
(*mangaka*), une **structure de production** (studio, éditeur), et **`saga`**, que
`hermeneutique/CLAUDE.md` traite déjà comme une règle de fiche-hub. Le manque est
rapporté plutôt que comblé en étirant le mot — un genre qui s'étire cesse d'être clos.

**Épreuve des contrôles (§VII)** — *vert* : dépôt vivant, « 321 fiches annotées, 936
annotations. OK — aucune anomalie », code 0 ; bac à sable, `categorie-editoriale` dans une
fiche `hermeneutique/` ne lève **rien**. *Refus* : même genre posé dans
`doctrinal/symboles/` — « data-genre='categorie-editoriale' est valide, mais son circuit
(doctrinal) ne l'admet pas », **D6**, code 2.

**Réversibilité (Cmd 10)** : le genre se retire sur verdict ; ses 10 poses sont un
remplacement littéral, réversible de même.

## [2026-09-09] amendement | §VII — Vocabulaire de `data-genre` scopé par circuit ; `hermeneutique` reconnu comme circuit par le contrôleur

**Verdict de Sidy**, 2026-09-09 : « étends le vocabulaire clos pour hermeneutique/ ».

**Le motif, mesuré.** La passe d'annotation des circuits non doctrinaux avait buté : les
sept genres transversaux ne savent nommer ni une œuvre profane, ni un personnage, ni un
dispositif d'œuvre. Sur 90 poses proposées dans `hermeneutique/`, 53 avaient dû être
rejetées faute de mot — et forcer `entite`, réservé au métaphysique, sur un personnage de
fiction aurait été une **faute de catégorie** exactement là où le Cmd 3 s'applique avec
une rigueur accrue.

**Ce qui est institué — et ce ne sont pas des mots nouveaux.** `hermeneutique/` reçoit
cinq genres propres, admis **chez lui seul** : `oeuvre`, `auteur`, `figure`,
`dispositif`, `concept`. Ce sont, **terme pour terme, les valeurs du champ `type:` que
`hermeneutique/CLAUDE.md` déclare déjà**. L'annotation emprunte au circuit son propre
vocabulaire, et hérite du même coup de la garde Cmd 3 qui y est attachée : `auteur`
« emprunte la forme d'archivage de `doctrinal/autorites/` sans en partager la fonction —
aucun statut d'autorité conféré ni supposé » ; `oeuvre` ne se fond **jamais** dans
`ouvrage`, réservé au traité traditionnel. Ne pas fondre ces deux registres est le fond
même du non-syncrétisme.

**`entite` reste admis dans `hermeneutique/`**, à côté de `figure`. J'avais d'abord voulu
l'en exclure, en tirant argument de « le hozo y est exclu par défaut » — mais cette clause
régit les **joints entre traditions**, non la faculté de nommer une entité reçue. Une
fiche du circuit en cite légitimement une dans la même phrase qu'une figure de fiction :
c'est même son sujet. Distinguer les deux est un **jugement réservé** (Cmd 12) — la garde
ouvre les deux mots plutôt que de trancher à la place de Sidy.

**Ce qui reste sans genre, et le reste sciemment** : les catégories éditoriales (*shōnen*,
*seinen*, *thriller*, *gothique*) et les structures de production (studios, éditeurs). Le
vocabulaire `type:` du circuit ne les nomme pas ; leur inventer un genre aurait été un mot
**de la machine et non du protocole**. Le manque est rapporté, non comblé.

**Migration des annotations déjà posées.** Les 35 annotations versées la veille dans
`hermeneutique/` employaient `ouvrage` pour *Death Stranding*, *Metal Gear*,
*Frankenstein*, et `autorite` pour Kojima, Mary Shelley, Naoki Urasawa. Migrées dans le
**même commit** : 16 `oeuvre`, 5 `auteur`. Sans cela, deux conventions auraient coexisté
dans le circuit — et le validateur les aurait acceptées toutes deux, de sorte que rien
n'en aurait averti plus tard.

**Un trou hérité, trouvé en câblant et comblé — `hermeneutique` n'était pas un circuit
pour le contrôleur.** `verifier-invariants.py` portait
`CIRCUITS = ["doctrinal", "atelier", "label", "meta"]` : `circuit_de()` renvoyait `None`
pour toute fiche du circuit, de sorte que **B1** (clés de Sceau requises) et **C3**
(étanchéité) n'ont **jamais contrôlé aucune des 28 fiches** depuis l'ouverture du circuit.
Le contrôle ne se plaignait pas : il ne regardait rien. C'est la forme exacte de PRO-01,
découverte ici parce que le nouveau contrôle D6 avait besoin d'un résolveur de circuit.
**Mesuré avant de combler** : les 28 fiches passent B1 sans une seule erreur, la fermeture
est donc sans effet rétroactif. `CLES_REQUISES` reçoit
`["title", "type", "registre", "created", "updated", "sources"]` — `registre` y est requis
car il distingue `analyse` de `expression`, donc le régime de production de la fiche. Et
`ETANCHEITE_INTERDITE` inscrit enfin « doctrinal/ → hermeneutique/ : jamais », que le
protocole local énonçait sans que rien ne le garde.

**Définition canonique partagée, troisième application.** `valider-annotations.py`
**importe** `circuit_de()` du contrôleur racine au lieu d'écrire une seconde règle
chemin → circuit. Même motif que le partage de `est_ecriture_originale()` et de
`fichiers_suivis()` : deux résolveurs qui divergent, c'est le contrôle qui ment sans se
plaindre.

**Épreuve des contrôles (§VII) — vert sur X, refus sur Y.** Le refus **D6** ne porte pas
sur un genre inconnu — VOC le refusait déjà — mais sur un genre **valide posé dans le
mauvais circuit**, et c'est cette face-là qui a été éprouvée.
- *Vert* : dépôt vivant, « 316 fiches annotées, 913 annotations. OK — aucune anomalie »,
  code 0 ; `verifier-invariants.py` 1418 fichiers, **0 erreur, 0 avertissement**. Bac à
  sable : `oeuvre` dans une fiche `hermeneutique/` et `entite` dans une fiche
  `doctrinal/` ne lèvent **rien**.
- *Refus* : bac à sable, `data-genre="oeuvre"` dans `doctrinal/symboles/` et
  `data-genre="dispositif"` dans `atelier/rd/` — **deux refus D6**, chacun nommant son
  fichier et son circuit, code 2.

**Réversibilité (Cmd 10)** : les cinq genres se retirent sur verdict ; la migration
`ouvrage`→`oeuvre` / `autorite`→`auteur` est un remplacement littéral, réversible de
même. Le comblement du trou de `CIRCUITS` est sans effet rétroactif, mesuré comme tel.

## [2026-09-08] amendement | §VII — Ratification des règles de placement des annotations HTML

**Verdict de Sidy**, 2026-09-08 : « Ratifie les règles de placement au protocole ». Ces
règles étaient **appliquées depuis l'ouverture du chantier d'indexation mais non
ratifiées** — signalées comme telles à la validation des cinq fiches pilotes.

**Ce qui est institué**, au §VII, transversal aux cinq circuits : cinq règles de
placement, dont quatre outillées.
1. **Jamais dans un wikilink** — le texte d'un wikilink est l'étiquette du lien ; le
   graphe est le porteur légitime du renvoi. *Refus D4.*
2. **Jamais dans un titre** (H1..H6) — le `title:`/H1 est le site canonique de la forme
   originale (langues originales, point 3) et l'index l'y récolte déjà. *Refus D4.*
3. **Jamais dans du code** — une balise entre chevrons dans du code est un **exemple
   cité**. Tenu non par un refus mais par le **masquage amont** : le code est masqué
   avant la recherche des balises, donc une convention citée en prose n'est jamais lue
   comme une pose.
4. **Une seule occurrence par terme et par fiche** — l'annotation *type* le terme, elle
   ne le *compte* pas. *Refus D5.*
5. **Jamais dans un texte reçu** (transcription, citation mot pour mot). **Non
   outillée**, et l'écart est déclaré : rien ne distingue mécaniquement une citation
   transcrite d'un bloc de la voix propre du dépôt. Elle lie le rédacteur, non le script.

**Ce que la mesure a écarté — le point le plus important de cet amendement.** Une
première rédaction de la règle 5 disait « jamais dans une citation », entendue comme
« jamais dans un blockquote ». Relevé sur `doctrinal/` avant d'écrire : les blocs `>` y
sont **massivement la voix propre du dépôt** — `> **Statut**` (53),
`> **Généalogie des idées**` (53), `> **Examen formel**` (50), `> **Conclusion**` (50),
`> 🔍 **Discernement — Spéculation Personnelle**` (49), sans compter les blocs
`> 🌐 **Forme Traditionnelle Divergente**` et `> ⚠️ **Déviation Profane**` que le §VII
prescrit lui-même. Ce sont **les blocs les plus denses en terminologie de tout le
circuit**. La règle inférée aurait fermé la porte principale de l'annotation, et l'aurait
fermée **en silence** — personne ne remarque une annotation qui n'est pas posée. Elle a
été resserrée sur le **texte reçu**, qui est le motif réel. Une prohibition dont la
portée est inférée, et non mesurée, est une faute de la même famille que la porte sans
garde.

**Épreuve des contrôles (§VII) — vert sur X, refus sur Y.**
- *Vert* : dépôt vivant, « 5 fiches annotées, 21 annotations. OK — aucune anomalie »,
  code 0 ; bac à sable ne contenant qu'une fiche saine — dont une **citation de la
  convention en prose**, qui doit précisément ne PAS être lue — aucun refus.
- *Refus* : trois fautes fabriquées hors dépôt vivant — **D4** annotation dans un titre,
  **D4** annotation dans un wikilink, **D5** terme annoté une seconde fois (le refus
  nomme la ligne de la première pose). Trois refus, un par faute, code 2.
- Conformité préalable des 21 annotations existantes **vérifiée mécaniquement** avant de
  faire des règles des refus : aucun doublon, aucun placement interdit. Un contrôle ne se
  cable pas sans savoir s'il refuserait l'état sain.

**Deux défauts du validateur v1.0, trouvés en câblant les nouveaux et corrigés.**
- **Une convention citée en prose était lue comme une annotation.** Le code n'était masqué
  qu'après la recherche des balises : une entrée d'annales décrivant la convention entre
  chevrons a produit un refus faux. C'est le **piège structurel déjà rencontré** avec le
  marqueur d'insertion cité en prose dans un fichier append-only. Corrigé : le masquage
  passe avant la recherche, en préservant les longueurs pour que les positions de D4
  restent justes.
- **Une branche D4 « dans du code » était inatteignable** — le masquage amont la rendait
  morte. Retirée : un contrôle qui ne peut pas se déclencher est la forme muette même que
  le §VII interdit, et il est pire de la laisser en place, car elle donne l'apparence
  d'une garde.

**Une limite rapportée, non corrigée** (Cmd 12) : le motif de code inline n'admet pas de
retour à la ligne, de sorte qu'un incise de code **coupé sur deux lignes** échappe au
masquage. Constaté sur la présente section même, à sa rédaction. Le correctif évident —
tolérer le retour à la ligne — a été **mesuré et écarté** : rendu glouton par les
backticks orphelins du dépôt, il avalerait 186 819 caractères de `doctrinal/annales.md`.
La règle reste donc tenue par le rédacteur.

**Réversibilité (Cmd 10)** : les cinq règles se démontent sur verdict ; D4 et D5 se
retirent sans effet rétroactif, aucune fiche existante ne les enfreignant.

## [2026-09-08] amendement | §VII — Champ `jurjani` de l'index lexical : le rang 2 des appariements

**Verdict de Sidy**, 2026-09-08 : « donne un champ propre à Jurjani et intègre les 132 à
l'index ».

**Ce qui est institué.** L'index lexical porte désormais **deux** champs d'appariement,
qui ne se fondent jamais :
- **`apparie` — rang 1** : la paire que **la fiche énonce elle-même**, dans son `title:`
  ou son H1 (`Tomoe (巴)`) ou en tête de définition (`**Buddhi** (Sanskrit : बुद्धि)`).
  59 paires.
- **`jurjani` — rang 2** : la paire qu'une **autorité textuelle transcrite au dépôt**
  établit — le *Kitāb al-Taʿrīfāt* d'al-Jurjānī —, chacune portant son **numéro de
  définition**, qui est sa source et se vérifie au texte. 132 appariements.

**Pourquoi deux champs et non un.** Deux rangs de crédibilité versés dans un même champ
seraient **indistinguables** : c'est très exactement ce que la règle « établi vs
suggéré » interdit (§VII, manifestes, règle 3), et ce que l'onglet apophatique de
l'Instrument matérialise par ailleurs. **Le rang 1 prime** : une clé que la fiche
apparie d'elle-même ne reçoit aucun renvoi Jurjānī. Le condensé `index-lexical.md` les
distingue à l'œil — renvoi nu pour le rang 1, `— Jurjānī déf. NNNN` pour le rang 2 : un
lecteur n'a jamais à deviner d'où vient une paire.

**Réciprocité partielle, et dite comme telle** (§VII, point 6). Sur les 132, **84**
portent le renvoi dans les deux sens ; les **48** autres ne l'ont que dans un seul, leur
translittération n'apparaissant nulle part dans le dépôt. On **n'injecte pas** le
vocabulaire du dictionnaire dans un index qui est celui du wiki — ce serait indexer
Jurjānī, non le dépôt. L'écart est déclaré, non comblé.

**Ce que la passe a trouvé, et qui vaut plus que les 132.** Sur **1141** clés orphelines,
**1009 ne sont pas des termes** : ce sont les lettres de l'alphabet relevées des tableaux
de translittération, des particules, des fragments de corpus. Le résidu terminologique
réel est de **6 clés**, et **aucune n'a demandé une translittération de mon fait** —
chacune est résolue par une source déjà présente au dépôt. Le **rang 3** que Sidy avait
par avance autorisé (« sinon tu feras la traduction par tes propres moyens et on sourcera
plus tard ») s'est donc trouvé **vide** : aucun `to-source` de ce chef n'est à poser.

**Épreuve des contrôles (§VII) — vert sur X, refus sur Y.** Deux refus francs gardent le
rang 2, tous deux éprouvés **hors dépôt vivant** :
- *Source absente* — bac à sable sans les fiches de transcription : « REFUS : source
  Jurjānī absente … un index privé de son rang 2 sans le dire serait un index muet »,
  code 2, rien écrit.
- *Récolte sous le plancher* — bac à sable portant une transcription tronquée à 10
  entrées : « REFUS : récolte Jurjānī sous le plancher : 10 entrées pour 150 attendues au
  minimum — motif de lecture probablement caduc », code 2, rien écrit.
- *Vert* : dépôt vivant, 10 648 termes, 132 appariements, 84 réciproques ;
  `verifier-invariants.py` 0 erreur / 0 avertissement.

Le plancher existe parce qu'un dictionnaire vide **ne se plaint jamais de lui-même** : si
le motif de lecture devenait caduc (fiche renommée, transcription tronquée, forme
changée), l'index perdrait tout son rang 2 en affichant la même sortie verte. C'est la
forme de PRO-01 et INF-14 appliquée par avance à un dispositif neuf.

**Deux faux appariements du rang 1, trouvés par la mesure et corrigés le même jour** :
`systeme` ↔ `α` (les H2 étaient lus ; retirés — seuls `title:` et H1 y entrent, le site
que le point 3 déclare canonique) et `conversion` ↔ `δ`. **Une lettre grecque isolée est
un label dans ce dépôt** (α, δ, γ, π, φ, tous employés comme variables ou numéros de
système), jamais un terme ; un caractère han isolé, lui, est un terme plein (巴) — d'où
une exclusion **par écriture**, non par longueur. 61 → **59 paires, toutes vraies**.

**Une limitation structurelle rapportée, non contournée** : `chikai to seiyaku /
誓約と制約` est un appariement de **syntagmes** ; les clés de cet index sont des
**tokens**, il ne peut pas le porter. Une extension à la barre oblique a été essayée puis
**retirée** — aucune paire vraie, et une fausse.

**Relevé complet de la passe** :
`atelier/rd/outillage/index-lexical/2026-09-08_passe-jurjani-orphelines.md`
(`type: artefact-derive` — l'index ne s'indexe pas lui-même).

**Réversibilité (Cmd 10)** : le champ `jurjani` est additif et régénérable ; le retirer ne
touche ni `apparie` ni aucune fiche du dépôt.

## [2026-09-08] amendement | §IV — Champ `original:` du Sceau (transversal) et sa garde mécanique

**Verdict de Sidy**, 2026-09-08, en réponse à la question du domicile du marqueur :
le champ **`original:` du Sceau**, miroir exact de `sources:`.

**Ce qui a rendu la question nécessaire.** L'amendement du même jour (§VII, discipline
des langues originales) instituait le marqueur `to-original` « sur le modèle exact de
`to-source` » — mais `to-source` a un domicile précis (`sources: ["to-source"]`,
contrôlé en B2) là où `to-original` n'en avait aucun. Une garde ne peut pas couvrir un
champ que nul texte ne nomme : sa portée serait inconnaissable, ce qui est la faute de
la porte-sans-garde retournée. La question a donc été posée plutôt que tranchée par la
machine (Cmd 13).

**Ce qui est institué.** §IV, règle transversale : tout Sceau des cinq circuits admet un
champ **facultatif** `original:`, liste YAML de chaînes entre guillemets droits, portant
la ou les formes du sujet dans son écriture d'origine (`original: ["巴"]`), ou le
marqueur `original: ["to-original"]`. Liste vide = le sujet n'appelle aucune écriture
d'origine. Le champ est **facultatif** : son absence n'est pas une faute, et aucune passe
de masse ne l'ajoute (§VII, point 5). Inscrit aux cartouches de `doctrinal/`, `atelier/`,
`label/` et `hermeneutique/` ; pour `meta/`, admis sur les fiches de contenu du domaine
mais **jamais dans le cartouche scellé d'une instance Karūbī**, que `generer-karubi.py`
fige et dont toute clé ajoutée à la main romprait l'empreinte.

**Garde mécanique, câblée le même jour — le champ ne naît pas sans elle.** C'est le
manque que l'ouverture de `liens_doctrinal` (2026-09-08, entrée précédente) avait su
éviter et que le marqueur `to-original` avait, lui, reproduit pendant une passe.
`verifier-invariants.py` porte trois codes nouveaux :
- **B5** — contradiction : `original: ["to-original"]` déclare l'absence d'une forme que
  le `title:` ou le H1 porte déjà.
- **B6** — graphie fautive du marqueur (`to_original`, `tooriginal`, `to-originel`...).
  Un marqueur mal orthographié est **invisible** : il paraît posé et n'est vu de
  personne.
- **B7** — forme du champ : liste YAML de chaînes ; marqueur et formes jamais mêlés ;
  une translittération refusée comme forme originale.

**Ce que la garde NE FAIT PAS**, et ne peut pas faire : exiger le champ. Savoir si le
sujet d'une fiche *appelle* une écriture d'origine demande la perception du sujet, non
la lecture de sa forme — jugement réservé (Cmd 12), et interdit d'office par le point 5.
La garde contrôle la **cohérence**, jamais la complétude.

**Définition canonique partagée.** `est_ecriture_originale()` vit désormais dans
`verifier-invariants.py` — le contrôleur racine, toujours présent — et
`generer-index-lexical.py` l'en **importe**. Le sens de la dépendance est délibéré :
l'outil de R&D dépend du contrôleur, jamais l'inverse. Son absence provoque un **refus
franc et nommé**, jamais un repli silencieux sur une copie locale : un index construit
sur une seconde définition paraîtrait juste sans l'être.

**Épreuve des contrôles (§VII) — vert sur X, refus sur Y.**
- *Vert* : dépôt vivant, 1417 fichiers, **0 erreur, 0 avertissement**. Bac à sable ne
  contenant que la fiche saine (`original: ["巴"]` avec `巴` au titre) : **0 erreur**.
- *Refus* : bac à sable de quatre fautes fabriquées, hors dépôt vivant — **B5** sur
  `to-original` contre un titre portant `巴` ; **B6** sur `to_original` ; **B7** sur
  `original: ["bindu"]` (translittération) ; **B7** sur `["नाद", "to-original"]`
  (marqueur mêlé à une forme). Quatre refus, un par faute, chacun nommant son fichier,
  code de sortie **1**.
- *Refus du partage* : générateur exécuté depuis une arborescence privée du contrôleur
  racine — « REFUS — définition canonique de l'écriture originale introuvable », code 1.

**Deux défauts de mes propres contrôles, trouvés par la faute fabriquée et non par la
relecture** — c'est très exactement ce que l'Épreuve existe pour trouver :
- **B6 refusait la graphie VALIDE.** L'alternative `to-originals?` de la première
  rédaction matchait `to-original` lui-même : le contrôle n'était pas muet mais
  **bavard à tort**, et aurait rendu le champ inutilisable dès sa première pose.
- **Le refus du partage était illisible.** `refus()` étant défini plus bas dans le
  fichier, l'appeler à l'import levait un `NameError` : refus obtenu, cause masquée. Un
  refus doit **nommer** sa cause ; remplacé par un `sys.exit` explicite.

**Réversibilité (Cmd 10)** : champ facultatif, aucune fiche existante n'en porte, aucune
migration n'est due ; les trois codes se retirent sans effet rétroactif.

## [2026-09-08] amendement | §VII — Discipline des langues originales (rang égal à la discipline des sources)

**Verdicts de Sidy**, 2026-09-08, en session : « il faut impérativement que le
protocole intègre les termes dans leurs langues originelles, pas juste la forme
latinisée », puis « c'est aussi important que la discipline des sources », puis, sur la
question de portée : « Toutes les écritures, toutes les fiches ».

**Ce qui est institué.** Une nouvelle discipline transversale au §VII, insérée
immédiatement à la suite de la discipline des sources et **de même rang** qu'elle. Six
points : (1) la forme latinisée ne suffit jamais seule — la forme d'origine se porte
*à côté* d'elle, jamais à sa place ; (2) portée universelle, aucune écriture
privilégiée ni exclue, aucun circuit exempté (`textes/` en est hors par sa règle
d'immuabilité propre, non par exemption, et reste indexé) ; (3) le `title:` du Sceau et
le H1 sont le site canonique de la forme originale ; (4) marqueur d'absence
**`to-original`**, calqué sur `to-source` — une forme originale ne se restitue ni de
mémoire ni par un modèle, et son ajout sans source est une faute *plus grave* que son
absence ; (5) **aucune passe de masse** — les fiches se complètent au fil des sessions
qui les touchent, restauration et non réforme (Cmd 11) ; (6) réciprocité de l'index,
dans les deux sens.

**Ce qui a motivé l'amendement** (mesuré, non allégué). Le tokeniseur de
`atelier/rd/outillage/index-lexical/generer-index-lexical.py` employait `[^\W\d_]+` ;
or `\w` de Python exclut les marques combinantes (catégories Unicode Mn/Mc). Les
écritures qui en emploient étaient donc éclatées en débris — devanagari, hébreu vocalisé
— tandis que l'arabe non vocalisé et le han, qui n'en emploient pas, passaient intacts.
D'où un index affichant 469 clés arabes et **zéro** devanagari : l'abondance apparente
masquait exactement l'angle mort qu'il aurait dû lever. C'est la forme de faute que le
dépôt a déjà payée deux fois (PRO-01, INF-14) : le dispositif n'était pas faux, il était
**muet**.

**Correctif appliqué le jour même** (« correctif A », verdict Sidy) : `RE_MOT` construit
sa classe de lettres par **catégorie Unicode** (Mn/Mc admises) plutôt qu'à la main. Deux
mesures, deux unités, consignées telles quelles au §VII — avant correction, en balayage
à blanc sur les 2131 fichiers du dépôt et au niveau des clés brutes : 3043 clés en
écriture originale recollées, 2578 fragments résorbés, 3 clés latines disparues
(`alisation`, `pendance`, `tudes`), elles-mêmes des débris NFD que le correctif recolle ;
après correction, sur l'artefact d'index et au niveau des termes retenus : 9687 → 9841
(+154), arabe 469 → 532, hébreu 97 → 183, devanagari 0 → 5, grec / han / kana inchangés.

**Épreuve des contrôles — ce qui est dû et ce qui ne l'est pas.** `RE_MOT` est une règle
d'**extraction**, non une garde : aucun refus ne lui est dû, et le geste éprouvant est
ici la table de tokenisation avant/après sur les six écritures (`बिंदु`, `बुद्धि`,
`जीवात्मन्`, `巴`, `مقرنص`, `תּוֹרָה`), observée éclatée puis entière.

**Ce qui reste ouvert et n'est PAS réputé fait** (Cmd 12 — rapporté, non corrigé
d'office) :
- **`to-original` naît sans garde mécanique.** Ni `verifier-invariants.py` ni
  `valider-annotations.py` ne connaissent ce marqueur : une fiche qui l'omet, ou qui le
  porte à tort, passe en silence. C'est exactement le manque que l'ouverture de
  `liens_doctrinal`, la veille, avait su éviter en câblant le champ *avec* sa
  couverture C1/C2. L'écart est déclaré ici plutôt que comblé d'office : le câblage
  demande son propre verdict.
- **Point 6 non tenu par l'outillage** : les clés en écriture originale que l'index
  porte sont des orphelines — aucun champ ne les relie à leur forme latinisée.
- **Point 3 non tenu par l'outillage** : le `title:` du Sceau et les H1/H2 ne sont pas
  récoltés par le générateur, alors que le point 3 en fait le site canonique. C'est la
  cause pour laquelle `tomoe` et `巴` restent absents de l'index malgré une fiche
  entière qui leur est consacrée. Correctif non appliqué, en attente de verdict.
- **Le dépôt ne satisfait pas aujourd'hui à la règle**, et le point 5 interdit de l'y
  mettre en conformité d'office.

**Réversibilité (Cmd 10)** : l'amendement est un texte de §VII, démontable sur simple
verdict de Sidy ; le correctif du tokeniseur l'est également — la version antérieure du
générateur est conservée hors dépôt et l'ancienne classe est documentée en commentaire
dans le fichier.

## [2026-09-08] amendement | §II — Convention des dossiers `assets-<sujet>/` ; `label/CLAUDE.md` — ouverture du champ `liens_doctrinal`

**Deux verdicts de Sidy**, 2026-09-08, en réponse à deux signalements portés à la
clôture de la session d'ouverture du dossier kamon : « Ajoute un lien
label/ → doctrinal/ » et « Oui, ajoute assets-instrument/ à Claude.md ».

### A — §II, les dossiers d'assets

**Ce qui a motivé l'amendement.** La session du 2026-09-08 a produit deux planches
SVG (`doctrinal/etudes/assets-kamon/`) en reprenant une convention qui existait
**en fait** depuis 2026-08 — `atelier/rd/instrument/assets-instrument/` — mais qui
ne figurait **nulle part** au protocole. Le §II ne mentionnait aucun dossier
d'assets, alors que le dépôt en versionnait déjà six fichiers. L'écart a été
signalé plutôt que corrigé d'office (Cmd 12) ; le verdict le referme.

**Ce que l'amendement inscrit.** Un `assets-<sujet>/` peut s'ouvrir à côté des
fiches qu'il sert, dans n'importe quel circuit. **Ce n'est pas un circuit** : pas
de Sceau, hors régime de liens (§VI), cible d'aucun wikilink, ignoré du graphe —
**même statut que `textes/`**, et pour la même raison. La **ligne de coupe est
identique à celle de `textes/` : le format, non le contenu.** `raw/assets/` garde
les binaires lourds et toute pièce nominative, et le motif de confidentialité du
`.gitignore` y porte pleinement ; `assets-<sujet>/` ne reçoit que le versionnable
et le mesuré.

Trois règles portées : préfixe `assets-` + nom du sujet, au plus près des fiches ;
citation **en prose par chemin relatif**, jamais en wikilink ; contenu **produit ou
vérifié, jamais approximé**. La troisième vient d'une décision de la session qui a
motivé l'amendement : les motifs organiques du répertoire kamon (*kiri*, *aoi*,
*fuji*, *kiku*) ont été **délibérément non figurés**, un dessin approximatif dans
un dépôt de transmission se transmettant comme s'il était juste.

**La convention est constatée, non instituée** : `assets-instrument/` la précède
de plusieurs semaines. Le protocole enregistre un usage, il n'en crée pas un.

### B — `label/CLAUDE.md`, le champ `liens_doctrinal`

**Ce qui a motivé l'amendement.** `label/CLAUDE.md` autorise depuis toujours le
renvoi `label/ → doctrinal/` (sens unique, signalé, 🔍 tant que non tranché), mais
**aucun champ du Sceau label ne permettait de le déclarer** : `liens:` est réservé
aux liens internes au circuit, `liens_atelier:` aux renvois vers
`atelier/materiel/`. Conséquence mécanique constatée le 2026-09-08 : une fiche
label dont les seuls renvois sortants sont doctrinaux remonte « isolée » au graphe.
La règle permettait le lien, la forme interdisait de l'inscrire.

**Ce que l'amendement ouvre.** Le champ `liens_doctrinal: []` au Sceau label, sur
le modèle exact de `liens_atelier`. Il **ne relâche aucune étanchéité** : il rend
déclarable ce qui était déjà permis, sous les mêmes contraintes (sens unique,
signalé, 🔍), et ne doit jamais porter de cible `atelier/`, `hermeneutique/` ou
`meta/`.

**Deux contrôles ont été étendus en conséquence, et le second est le point qui
compte.**

1. `atelier/rd/outillage/graphe/generer-cartographie.py` — `liens_doctrinal` ajouté
   à `_CHAMPS_LIENS_TOUS`. **Sans cette ligne, le champ aurait été écrit et jamais
   lu** : la fiche serait restée isolée et le dépôt aurait cru le problème résolu.
   C'est la forme exacte de PRO-01 et INF-14 — le contrôle muet.
2. `verifier-invariants.py` — `liens_doctrinal` ajouté à `CHAMPS_LIENS_CARTOUCHE`,
   **en même temps que son ouverture**, pour qu'un champ de liens nouveau ne
   naisse pas hors de la couverture C1/C2. Ajout **sans effet rétroactif** :
   aucune fiche du dépôt ne portait ce champ auparavant.

**Manque hérité, signalé et NON corrigé** (il demande son propre verdict) : `liens:`
et `liens_atelier:` du Sceau label restent hors de `CHAMPS_LIENS_CARTOUCHE` — une
cible morte y passe en silence. Le commentaire du code le porte désormais en clair.
Le même besoin existe pour `atelier/rd/` et `atelier/projets/`, qui peuvent aussi
pointer vers `doctrinal/` : **hors périmètre du présent verdict**, non traité.

### Épreuve des contrôles (§VII) — les deux refus ont été observés

Les deux scripts ayant été modifiés, l'épreuve était due. Conduite en **copie
jetable**, jamais dans le dépôt vivant :

- **Vert sur l'état sain** : `verifier-invariants.py` — 1415 fichiers, 0 erreur,
  0 avertissement ; graphe — 1932 arêtes (**+2**, exactement les deux liens
  déclarés), isolées **43 → 42**, la fiche label ayant quitté la liste.
- **Refus sur la faute fabriquée** (cible morte dans `liens_doctrinal`) : le
  vérificateur lève `[C1] … lien non résolu au cartouche (\`liens_doctrinal:\`)`,
  et le graphe lève `'liens_doctrinal' → [[…]] (absent du dépôt)`. **Chacun nomme
  le champ**, ce qui atteste qu'il le lit réellement.
- **Contre-épreuve du muet** : l'ancienne liste de champs remise dans la copie
  jetable, le graphe retombe à 1930 arêtes et 43 isolées, la fiche redevenant
  isolée alors que son cartouche déclare les deux liens. La nécessité de la
  modification n° 1 est ainsi **démontrée, non affirmée**.

### Réversibilité (Cmd 10)

Les deux volets sont additifs — **rien n'est supprimé**, ce pourquoi aucune archive
complète du protocole n'est déposée (mêmes précédents que les amendements des
2026-09-01 et 2026-09-02). Retrait sur simple verdict : ôter la section du §II ;
ôter `liens_doctrinal` du Sceau label, des deux scripts, et du cartouche de
`label/direction-artistique/amorcage/kamon-personnel.md` — la fiche redeviendrait
« isolée », état antérieur exact.


## [2026-09-02] amendement | §II — Ouverture de `textes/`, le cabinet de lecture

**Verdict de Sidy**, 2026-09-02, cité *verbatim* : « `textes/` validé,
dédoublonne avant migration, et amende le §II ». Chantier PRO-08
(`atelier/rd/infrastructure/pro-08-textes-convertis-versionnes/`).

### Ce qui a motivé l'amendement

Constat de Sidy : « Aucun fichier Markdown n'a d'intérêt à rester en `raw/`
sachant qu'en y étant ils restent masqués et je ne peux pas travailler avec ces
ressources en dehors du terminal. »

Vérifié au disque : `/raw/*` est dans `.gitignore`, et `raw/` contenait **708
fichiers `.md`, zéro suivi par git**. Tout le corpus converti — Guénon (*Symboles
de la Science sacrée*, *Le Théosophisme*, *Aperçus sur l'initiation*, *Le Règne
de la Quantité*, *Le Symbolisme de la Croix*, *La Grande Triade*, *L'Homme et son
devenir*, *Les états multiples*, *Le Roi du Monde*…), Jurjani, Avalon, Shayegan,
Vâlsan — ne se synchronisait **jamais** vers Obsidian. Le poste CONSULTATION
(§I) était aveugle sur la matière même que les fiches doctrinales citent en
source.

### Les deux motifs de l'exclusion, MESURÉS avant d'être écartés

Le `.gitignore` porte ses raisons — « peuvent contenir des données personnelles +
fichiers volumineux » — et aucune n'avait jamais été vérifiée.

| motif | mesure |
|---|---|
| fichiers volumineux | **14 Mo** de Markdown contre **2,6 Go** pour `raw/` entier : le texte en est 0,5 % |
| données personnelles | **0** adresse e-mail, **0** IBAN, **0** téléphone sur 708 fichiers |

Le motif de confidentialité **tient pleinement pour les binaires** : `raw/` porte
des factures nominatives, un export ChatGPT, un dossier `Downloads`. D'où la
ligne de coupe retenue : **le format, non le contenu**.

⚠️ **Un faux positif consigné.** Le premier balayage avait signalé « IBAN » dans
*Le Roi du Monde* : c'était **« Liban »**, la recherche insensible à la casse
trouvant la sous-chaîne. Le motif a été resserré sur bornes de mot **avant** de
conclure — sans quoi le corpus aurait porté un soupçon faux.

### Ce que le §II dit désormais

- Entrée `textes/` dans l'arbre, et `raw/` explicité comme **hors git**.
- Une section de statut : `textes/` **n'est pas un sixième circuit**, pas plus
  que `meta/` n'en est un. Aucun Sceau, aucun régime de liens (§VI), cible
  d'aucun wikilink, ignoré du graphe.
- La **règle d'immuabilité** : un texte de `textes/` ne se corrige pas ; une
  conversion meilleure le remplace, datée. Ce qui se dit d'un texte se dit dans
  une fiche `doctrinal/sources/`, qui porte le Sceau et le statut.

### Conséquence outillée, et son épreuve

`verifier-invariants.py` exempte `textes/` du contrôle B0, par une ligne nommée
dans `PREFIXES_SANS_FM` — mécanisme **qui existait déjà** pour « les fichiers
légitimement sans frontmatter ». Sans elle, la migration aurait produit **560
erreurs**, c'est-à-dire le bruit même qui avait masqué la seule erreur vraie du
2026-09-01 (chantier OUT-C2).

**L'exemption est CIBLÉE, et les deux faces ont été éprouvées** (§VII) :

- un `.md` nu **dans** `textes/` → accepté, 0 erreur ;
- un `.md` nu **hors** `textes/` → **`B0` levé**.

Sans la seconde face, rien ne distinguerait un amendement ciblé d'un
désarmement général du contrôle.

### Réversibilité (Cmd 10)

La migration **copie**, elle ne déplace pas : les 708 originaux demeurent dans
`raw/`. Retirer `textes/` et la ligne d'exemption rétablit l'état antérieur sans
perte. Le retrait des originaux serait une **seconde décision**, non préparée
ici.

### Ce qui reste ouvert

Le **régime des futurs** textes convertis — passent-ils encore par `raw/`, ou
directement du sas vers `textes/` ? Posé à Sidy, **non tranché**. C'est la
question qui décide si le problème peut se reformer.

---


## [2026-09-01] amendement | §I — Levée de la clôture économique PRODUCTION/INTÉGRATION

**Verdict Sidy**, en session, sur signalement fait à la clôture de la session
précédente (fiche `atelier/rd/infrastructure/cartographie-routing-infrastructure.md`,
produite côté INTÉGRATION alors même que §I l'interdisait en principe).

**Fait déclencheur.** L'architecture des « postes de travail » (§I) distinguait
PRODUCTION (lecture lourde, rédaction — app conversationnelle au forfait) et
INTÉGRATION (mécanique seule — outil CLI serveur) sur la base d'une **prémisse
économique unique** : Sidy ne parvenait plus à authentifier Claude Code (Terminal)
avec son compte Claude Pro, et tenait pour acquis qu'Anthropic avait fait basculer
l'accès à Claude Code du OAuth (forfait) vers l'API seule (facturation à l'usage,
jugée trop coûteuse pour absorber de la rédaction côté intégration). Sidy a pu de
nouveau s'authentifier avec son compte Pro — la prémisse ne tient plus.

**Verdict, mot pour mot** : à la question de savoir si la distinction
PRODUCTION/INTÉGRATION gardait une raison d'être indépendante du coût (discipline de
workflow, app iPad seule, mode pédagogique), Sidy a tranché : **« coût seul
justifiait la clôture »** — pas de raison résiduelle invoquée. La clôture tombe donc
avec sa seule prémisse, pas seulement assouplie.

**Changement effectué (§I)** :
- Table des postes : colonne « Règle de coût » renommée « Régime » — son contenu
  n'oppose plus PRODUCTION/INTÉGRATION sur une base de coût. La ligne INTÉGRATION
  porte désormais explicitement : lecture lourde et production de contenu
  autorisées, **sur consigne directe de Sidy en session** (pas d'initiative autonome
  au long cours sans validation).
- « Règle économique et fonctionnelle absolue » retirée en tant que telle, remplacée
  par un paragraphe qui nomme le fait déclencheur, cite le verdict, et pointe vers la
  présente entrée pour la lettre complète.
- Ce qui ne change **pas**, énuméré explicitement pour éviter toute sur-lecture du
  verdict : le principe « scripter le déterministe, réserver le modèle au jugement »
  (indépendant du coût) ; le sas `_inbox/`/`UPDATES.md` comme voie normale des lots
  PRODUCTION (la levée ajoute une voie, n'en retire aucune) ; Cmd 6 (pas d'écriture
  sans plan présenté) et Cmd 13 (porte humaine sur ce qui engage) pleins et entiers —
  la levée porte sur la **capacité** de rédiger côté intégration, pas sur la
  **dispense** de validation humaine.

**Ce qui reste inchangé ailleurs** : « Mode pédagogique obligatoire » (§I, fin), le
statut de CONSULTATION et des AGENTS DE FONCTION, et toute règle des `CLAUDE.md`
locaux de circuit qui ne dérive pas de cette clôture.

**Portée** : transversale (§I vit à la racine, Cmd 14). Aucun `CLAUDE.md` local ne
cite la clôture de coût nommément — aucune modification requise ailleurs.

**Réversibilité (Cmd 10)** : la clôture se rétablit d'elle-même si le fait qui la
lève cesse d'être vrai (accès Pro/OAuth de nouveau indisponible, ou de nouveau
facturé à l'usage) — la règle a toujours été fondée sur un fait vérifiable, pas sur
un principe fixe. Pas de snapshot `CLAUDE.md.bak-*` créé pour cet amendement
(pratique réservée aux restructurations majeures, cf. `CLAUDE-v2-monolithique_2026-08-12.md`
et le `.bak-2026-08-22-pre-deplacement-bibliotheque`) — l'historique git du fichier
suffit à la réversibilité d'un amendement de cette taille, comme pour les deux
amendements précédents du 2026-09-01.

- **Commit** : 89f5b51

## [2026-09-01] amendement | §VII — Épreuve des contrôles

**Verdict Sidy**, en clôture de la session du 2026-09-01, sur signalement de la machine.

**La règle** : *un contrôle dont on n'a pas vu l'échec n'est pas un contrôle vérifié.*
Tout dispositif mécanique de vérification — hook git, tâche de CI, validateur, garde-fou
de script, champ `infra_verif` — doit avoir été **vu refuser**, sur une faute fabriquée
exprès dans un bac à sable, avant qu'on lui fasse confiance. Passer au vert est une
condition nécessaire et jamais suffisante.

**Pourquoi elle entre au protocole.** Le dépôt a payé deux fois la même erreur à un jour
d'intervalle : le contrôle `lint` qui gardait `main` sans rien inspecter (PRO-01,
2026-08-31), et les hooks du dépôt de rendu dont le motif `grep` ne correspondait à rien
(INF-14, 2026-09-01) — ce second cas écrit le jour même par la machine qui venait de
consigner le premier. La forme de la faute est invariable : le contrôle est **muet**, non
pas faux, donc il paraît vert. Un motif qui ne correspond à rien, une liste de fichiers
vide, une dépendance absente, un chemin périmé.

**Le geste exigé** : vert sur l'état sain, puis refus observé sur la faute fabriquée,
puis retour à l'état sain — les deux résultats consignés aux annales. Un contrôle dont
l'entrée ne rapporte que le vert est réputé non éprouvé. Corollaire : un dispositif
hérité jamais vu échouer n'est pas réputé fonctionner ; le doute se rapporte et ne se
corrige pas d'office (Cmd 12).

**Placement** : §VII, après *Double contrôle systématique*, dont il partage la nature —
un contrôle de relevé, qui ne tranche rien. Un pointeur, sans duplication de la lettre,
est posé dans la *Vigilance documentaire (clôture de session)*. Transversal, donc racine
seule (Cmd 14).

**Réversibilité (Cmd 10)** : retirer la sous-section du §VII et le pointeur de clôture
rend au protocole son état antérieur.

- **Commit** : e02f519

## [2026-09-01] amendement | Scission du rendu de l'Instrument + triptyque de chantier au pôle rd/

**Verdict Sidy**, session du 2026-09-01, à la lecture du *AI-Native SDLC Playbook*
(Claude Academy).

**Racine — §VII, Règle commune des MANIFESTES, règle 5 ajoutée.** Le rendu de
l'Instrument est scindé vers un dépôt frère, `Sidyvision/instrument` (privé). Motif :
la règle du sens unique `dépôt → manifeste → interface` existait déjà et tenait par la
seule vigilance tant que la source et l'interface partageaient un arbre git ; elle
tient désormais par construction. **Ligne de coupe : producteur/consommateur, jamais
Instrument/reste** — la donnée (`instrument-donnees.yaml`), le producteur
(`generer-manifeste.py`), les fiches d'architecture, les mises en regard doctrinales,
`assets-instrument/` et les chantiers `INS-` restent au wiki ; seule l'interface part.
Le manifeste est poussé depuis le wiki, jamais tiré par l'interface. Rien n'a été
supprimé : `instrument-prototype.html` subsiste en stub `deprecated` (Cmd 10).

**Racine — §II.** L'arbre annote `rd/` de la ligne de coupe, pour qu'un lecteur du
seul protocole sache ce qui a quitté le dépôt et à quelles conditions (Cmd 14).

**`atelier/CLAUDE.md`.** Reprise de la ligne de coupe sous *Structure du circuit*.
Ajout — signalé comme **règle nouvelle**, non comme clarification — de la nomenclature
des dossiers de chantier `atelier/rd/<domaine>/<id>-<slug>/` portant le triptyque
`intent.md` / `spec.md` / `plan.md` ; la nomenclature antérieure était de forme plate
et muette sur les dossiers imbriqués, la version monolithique archivée du 2026-08-12
ne peut donc pas en rendre compte. Ajout du champ de Sceau optionnel `chantier:`
(même précédent que `statut_experience` et `infra_verif`).

**Périmètre du triptyque : le pôle `rd/` seul** (`INS-`, `INF-`, `OUT-`). Les circuits
documentaires conservent leurs instruments propres — Sceau, fiche `discernement`,
annales : y greffer un triptyque produirait le doublon que le Cmd 14 interdit. Pour un
chantier `rd/`, le `plan.md` visé par Sidy **est** le plan du Cmd 6 — aucune obligation
nouvelle, une obligation existante qui reçoit une forme consultable à froid.

**Clause de non-emprunt.** Le triptyque est une convention d'ingénierie et n'emprunte
aucun terme au lexique Sashimono, clos aux termes nouveaux sans fiche `discernement`
(Cmd 3). En particulier `intent.md` n'est pas un *sumi-tsuke* — celui-ci désigne la
fiche `discernement`, instrument doctrinal relevant du Cmd 12.

**Réversibilité (Cmd 10).** L'amendement est démontable sur simple verdict de Sidy :
supprimer la règle 5 du §VII et l'annotation du §II rend au dépôt son état antérieur ;
le dépôt frère redevient alors un miroir sans autorité, le wiki n'ayant jamais cessé
de porter la donnée et le producteur.

**Lettre complète du triptyque** : `atelier/rd/outillage/gabarit-triptyque-chantier.md`.
**Chantier** : `atelier/rd/infrastructure/inf-13-scission-depot-instrument/`.

## [2026-08-31] deplacement | Graphe/ → atelier/rd/outillage/graphe/ + usage explicite dans la vérification générale

Demande explicite de Sidy : renommer `Graphe/` (majuscule, racine) en minuscule
et le déplacer en outillage R&D, sous condition que cela n'endommage pas son
fonctionnement. Vérification préalable : `generer-cartographie.py` n'a aucune
dépendance de chemin relatif à sa propre localisation (`--depot` par défaut est
un chemin absolu, `/root/wiki` ; aucun usage de `__file__`/`os.path.dirname`) —
déplacement sans risque fonctionnel confirmé. Sortie inchangée :
`graphe-cartographie.json` reste écrit à la racine du dépôt.

Exécuté par `git mv Graphe atelier/rd/outillage/graphe`. Références mises à
jour dans les documents opératoires (protocole, pas les annales/rapports
datés qui restent des constats d'époque, non réécrits — Cmd 10) :
- `CLAUDE.md` racine : arbre §II (ligne ~121-124), en-tête de révisions,
  §VII (Vérification structurelle obligatoire + Action VIGILANCE).
- `doctrinal/CLAUDE.md` : références de chemin au script (§ Exploitation du
  graphe lors de l'intégration).
- `README.md` : entrée d'inventaire.
- `atelier/rd/outillage/detecter-non-tracke.py` : `"Graphe"` retiré de
  `DOSSIERS_HORS_CIRCUIT` — le dossier rejoint désormais le circuit `atelier`,
  il n'est plus un dossier de service hors-circuit comme `raw/`/`_inbox/`.
- `atelier/rd/outillage/spec-generer-cartographie-tolerant.md` : référence de
  chemin corrigée.

Deuxième demande groupée du même message : rendre explicite l'usage du graphe
dans la routine de vérification générale de clôture de session (il n'y était
pas nommément associé jusqu'ici, seule la procédure d'intégration d'une
nouvelle fiche doctrinale le mentionnait, dans `doctrinal/CLAUDE.md`). Ajouté
en §VII (racine) : régénération/consultation du graphe pour notions
orphelines et liens morts, avec le même principe de non-correction d'office
que le reste de l'Action VIGILANCE (Cmd 12).

Regénération et `verifier-invariants.py` relancés après déplacement pour
confirmer l'absence de régression (voir annales du jour).

## [2026-08-29] clarification | Objet documentaire de la bibliothèque R&D (couvertures, sommaires, index, glossaires)

Demande explicite de Sidy : noter de façon nette, claire et définitive que les
photographies de couverture, sommaire, index et glossaire déposées dans
`atelier/rd/bibliotheque/` (section « Index et glossaires transcrits » de
`catalogue-bibliotheque.md`) sont **strictement documentaires et d'orientation**
— elles permettent de savoir *où chercher* dans un ouvrage physique possédé,
sans nécessiter la numérisation intégrale de la bibliothèque, impossible à
entreprendre en pratique. C'est l'objet même de ce pôle. §VII (Discipline des
sources), point 1 du `CLAUDE.md` racine amendé en conséquence : consultation de
`atelier/rd/bibliotheque/catalogue-bibliotheque.md` rendue **impérative et
prioritaire**, y compris avant tout signalement d'absence d'une œuvre (un agent
qui déclare une œuvre « absente du corpus » sans avoir vérifié ce pôle commet un
signalement prématuré — cas vécu le jour même avec *Hindouisme et Soufisme*,
Shayegan, dont la fiche `sommaire-hindouisme-soufisme.md` existait déjà côté
`atelier/rd/bibliotheque/` au moment où l'absence avait été signalée par excès
de prudence, avant `git pull`). Note renforcée en tête de
`atelier/rd/bibliotheque/catalogue-bibliotheque.md` dans la même passe. Aucun
autre contenu du protocole modifié.

## [2026-08-28] maintenance | Migration de l'historique hors du protocole racine

L'historique des révisions qui vivait en préambule de `CLAUDE.md` (environ
cent lignes, chargées à chaque session) est migré intégralement ci-dessous
(bloc « Historique migré »). Le protocole racine conserve un en-tête de statut
court (dernières révisions, pointeurs d'archive). Corrections de dérive
appliquées dans la même passe : ligne Wendel Nazaire/Hassan ajoutée à la table
Karūbī (`meta/CLAUDE.md`), arbre du §II complété, guide de déploiement
`verifier-invariants.py` déplacé de la racine vers `meta/` et renommé selon la
nomenclature (§III), `meta-index.md` complété (karubi-wendel, briefs/, fiches
de premier niveau manquantes), `README.md` racine actualisé (il décrivait la
structure pré-Restauration), en-tête de l'entrée du 2026-08-25 restauré dans
`meta-annales.md` (perdu au commit d09cc88). Détail complet dans l'entrée
`meta-annales.md` du même jour.

## Historique migré (préambule du protocole racine, 2026-06-11 → 2026-08-22)

Protocole issu de la **Restauration « Guénon V1 »** (2026-06-11, rév. 2026-06-12),
étendu en **V2** le 2026-07-05 (ouverture du quatrième circuit `label/`, postes de
travail rendus agnostiques au modèle, règles de supervision des moteurs locaux,
protocole de publication du site), **révisé le 2026-07-06** : réintégration in extenso
des protocoles d'exécution (le présent fichier doit être auto-suffisant pour tout
moteur), discipline des sources, règle commune des manifestes, supervision étendue des
agents (mémoire, skills, canaux, extension `raw/`), vigilance documentaire, et
**ancrage éthique des actes contractuels et commerciaux du label** (§V.c) et
**ouverture du pôle Fiqh** (préséance mālikite, bloc ⚖️, double face du Gardien —
§V.c.6 et §VII).
**Révisé le 2026-07-07** : adoption de la philosophie et de la convention
terminologique Sashimono (§VII, « Convention Sashimono » ; directive détaillée :
`meta/philosophie-sashimono.md`).
**Révisé le 2026-07-16** : double contrôle systématique (sashimono + confrontation
Gizeh) inscrit au §VII.
**Révisé le 2026-08-04** : ouverture du cinquième circuit `hermeneutique/`
(§II, §V.d, §VI) — navigation du domaine intermédiaire via les médiums de fiction
tenus pour interfaces, clés doctrinales suggérées, registres `analyse` et
`expression`, double fonction avec le bureau de Direction Artistique du label.
On ne
parle jamais de « réforme » : une réforme prétend corriger le principe, une
restauration rétablit l'ordre normal. Le mot « réforme » est banni du dépôt.
**Révisé le 2026-08-08** : taxonomie élargie du circuit `hermeneutique/`
(types `auteur`, `figure`, `dispositif` ; dossiers `hermeneutique/auteurs/`
et `atelier/etudes-de-cas/`) et introduction de l'axe de **portance**
(*jikugumi*/*zōsaku*) et de l'axe de **nature** (*restitution*/*homologie*)
des joints — §II, §III, §V.d, §VII (convention Sashimono). Visé par Sidy.
**Révisé le 2026-08-08 (second amendement)** : ouverture du pôle **R&D** de
l'atelier — `atelier/rd/`, pôle interne au circuit existant (verdict Sidy :
Option C, nom `rd/`, phase 1 partielle). Cinq circuits, inchangés. Le pôle
reçoit la finalité de **souveraineté** : consignation systématique de tout ce
qui relève de l'infrastructure globale hardware/software, en vue de son
entretien, développement qualitatif, optimisation à mesure, et de
l'émancipation progressive de tout intermédiaire de service tiers. Sceau
atelier étendu (§V.a), régime de liens de `projets/` hérité par `rd/` (§VI),
`liens_atelier` élargi (§V.d), annales de l'atelier inscrites au Cmd 9.
**Révisé le 2026-08-09** : ouverture d'un régime propre à la **couche agentique
opérative** (Hermes) au sein du Domaine Réservé — §VI, corollaire agentique.
L'étanchéité `meta/` continue de régir les cinq circuits du dépôt à l'identique ;
elle ne s'applique plus telle quelle aux agents Hermes, dont la fonction inclut
par construction l'usage du contexte personnel de Sidy. Contrepartie
non-négociable : toute donnée personnelle injectée dans un prompt d'agent porte
sa propre hiérarchie ontologique explicite (clause `## Ontological order`), pour
distinguer le principe (précédant, structurant) de la détermination individuelle
(contingente, ne portant rien — *zōsaku*, §VII). Point de méthode, non de
doctrine : ne rouvre aucune correspondance déjà tranchée. Voir fiche
`doctrinal/discernement/2026-08-09_hierarchie-principe-determination-individuelle.md`.
**Le 2026-08-08 (exécution)** : migration de `atelier/projets/` vers `rd/`
effectuée fiche par fiche (§IV de la proposition) : 16 fiches migrées (slugs
conservés), anciennes fiches conservées en stubs `deprecated` avec pointeur
(Cmd 10), assets et scripts déplacés avec les fiches. §II mis à jour
(`projets/` désormais résiduel). `album-personnel.md` déplacé le même jour
vers `label/production/` (verdict Sidy : relève de la création artistique,
non du pôle R&D) — stub `deprecated` conservé, liens entrants `materiel/`
coupés (§VI).
**Révisé le 2026-08-09** : ouverture du hub propre à `meta/` —
`meta/meta-index.md` et `meta/meta-annales.md` (verdict Sidy : nommage
préfixé `meta-` pour écarter tout risque de lecture comme sixième circuit ;
`meta/` reste le Domaine Réservé, non un circuit). Motif : le comptage
mécanique des liens entrants (`carte-du-depot.py`, bug de résolution
corrigé le même jour) faisait apparaître 66 fiches de `meta/`
(`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
`projet-unifie/`) sans aucun lien entrant, faute de hub interne au domaine
— les quatre circuits en ont un (`index.md`/`annales.md`), `meta/` n'en
avait aucun. §II, §VI et §X (Cmd 9) mis à jour.
**Révisé le 2026-08-12 : éclatement expérimental en protocoles locaux
(verdict Sidy — méthode à l'essai, non tranchée définitivement).** Le présent
fichier ne porte plus, seul, la lettre intégrale de toute règle : les Sceaux,
nomenclatures et actions d'exécution **propres à un seul circuit** vivent
désormais dans un `CLAUDE.md` local (`doctrinal/`, `atelier/`, `label/`,
`hermeneutique/`, `meta/` — carte au §II bis). Motif : réduire ce que doit lire
un agent travaillant dans un seul circuit, sans rien perdre pour un agent
travaillant depuis la racine (chargée par construction en toute circonstance).
Ce qui reste ici : tout ce qui est transversal (postes de travail, carte des
circuits, étanchéité inter-circuits, protocoles d'exécution communs,
supervision des agents, procédure d'intégration, commandements absolus). Le
**Corollaire d'auto-suffisance** (ancien Cmd 14) est amendé en conséquence — sa
nouvelle lettre figure au §X. **Archive intégrale** de la version
pré-éclatement, non modifiée, conservée pour rollback :
`meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md` (Cmd 10 : jamais
de suppression sèche). Réversible sur simple verdict de Sidy.
**Révisé le 2026-08-22** : ajout du **Commandement 15 (Hygiène Unicode)** suite
à l'incident de contamination par caractères Zero Width Joiner (U+200D). 31
fichiers nettoyés, 156 occurrences supprimées. Interdiction formelle d'insérer
des caractères Unicode invisibles dans le dépôt. Référence : rapport
`atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`.
