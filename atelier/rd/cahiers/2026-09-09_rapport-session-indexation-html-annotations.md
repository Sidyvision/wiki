---
title: "Rapport de session — indexation HTML, langues originales et convention d'annotation (2026-09-08 → 09)"
type: experience
statut_experience: reproduit
tags: [rd, cahier, rapport, indexation, annotation, langues-originales, epreuve-des-controles, methode, verification-mecanique]
created: 2026-09-09
updated: 2026-09-09
sources: []
links: ["[[atelier/rd/cahiers/2026-09-09_etat-des-lieux-indexation-et-reprise]]", "[[atelier/rd/cahiers/registre-problemes]]", "[[atelier/rd/outillage/index-lexical/2026-09-08_passe-jurjani-orphelines]]"]
original: []
---

# Rapport de session — indexation HTML, langues originales et convention d'annotation

> Circuit **atelier**, pôle R&D, cahier de laboratoire. Document de méthode, non
> doctrinal. Ce qu'il rapporte est **mesuré ou observé** ; ce qui reste supposé le dit.
>
> **Ce rapport couvre la première moitié du chantier** (`274ddc6..a4c7d32`). L'état au
> soir du 2026-09-09, les verdicts en attente, le registre des voies écartées et les
> commandes de reprise vivent dans
> [[atelier/rd/cahiers/2026-09-09_etat-des-lieux-indexation-et-reprise]] — **c'est ce
> second document qu'il faut ouvrir pour reprendre le chantier.**

## 1. Ce que la session a produit

Vingt-huit commits, `274ddc6..a4c7d32`, sur deux jours. Trois chantiers enchaînés :

1. **Discipline des langues originales** (§VII) — amendement de rang égal à la
   discipline des sources, champ `original:` ouvert aux cinq Sceaux (§IV), garde
   mécanique B5/B6/B7.
2. **Index lexical** — correctif du tokeniseur (A), récolte des titres et appariement
   (B), champ `jurjani` pour le rang 2 des appariements.
3. **Convention d'annotation HTML** — règles de placement ratifiées (D4/D5),
   vocabulaire `data-genre` scopé par circuit (D6), et **936 annotations** posées sur
   **321 fiches** des cinq circuits.

État final mesuré : index à **10 675 termes**, `verifier-invariants.py` 1418 fichiers
0 erreur / 0 avertissement, `valider-annotations.py` v1.2 aucune anomalie.

## 2. La leçon principale : neuf défauts, et aucun trouvé par relecture

C'est le fait de méthode le plus net de la session. **Aucun des neuf défauts ci-dessous
n'a été trouvé en relisant du code.** Tous l'ont été soit par une **faute fabriquée**
(§VII, Épreuve des contrôles), soit par une **mesure sur l'artefact**, soit par le
**refus d'un contrôle existant**.

| # | Défaut | Trouvé par |
|---|---|---|
| 1 | `RE_MOT` éclatait devanagari et hébreu vocalisé (`\W` exclut Mn/Mc) | mesure : 469 clés arabes, **0** devanagari |
| 2 | `MIN_LONGUEUR = 3` écartait `巴` et `神道` avant tout autre examen | témoin sur cible diagnostiquée |
| 3 | B6 refusait la graphie **valide** `to-original` | faute fabriquée |
| 4 | Le refus du partage levait un `NameError` — cause masquée | faute fabriquée |
| 5 | Une convention **citée en prose** était lue comme une annotation | refus faux, en dépôt vivant |
| 6 | Une branche D4 « dans du code » était **inatteignable** | relecture *après* correction du n° 5 |
| 7 | Le proposeur ne balayait que la **racine** des dossiers (`glob`/`rglob`) | incohérence de compte : 2 fiches sur 377 |
| 8 | Il annotait les **fichiers de service**, que l'index ignore | **refus D3** |
| 9 | Il **sautait toute fiche déjà annotée** — l'extension ne pouvait rien atteindre | incohérence de compte après extension |

**La forme est toujours la même** : le dispositif est **muet**, non pas faux. Il ne se
plaint jamais, donc il paraît vert. Un tokeniseur qui rend 9687 termes paraît riche ; un
proposeur qui trouve 2 fiches annotables sur 377 paraît simplement avoir peu à faire.

**Corollaire pratique** : le contrôle qui rapporte un **compte** vaut plus que celui qui
rapporte un état. Les n° 7 et 9 ont été trouvés parce qu'un chiffre était *invraisemblable*,
non parce qu'une erreur était levée.

## 3. Le cas n° 6 mérite d'être isolé

Après avoir corrigé le n° 5 (masquer le code **avant** de chercher les balises), la
branche D4 « annotation dans du code » est devenue **inatteignable** : le masquage amont
la rendait morte.

Elle a été **retirée**, et le motif est protocolaire : *un contrôle qui ne peut pas se
déclencher est la forme muette même que le §VII interdit, et le laisser en place est pire
que ne rien avoir — il donne l'apparence d'une garde.* Une correction peut donc **créer**
un contrôle mort. Corriger un dispositif oblige à revérifier ce que la correction rend
inutile.

## 4. Trois trous hérités, dont un de six semaines

- **`hermeneutique` n'était pas un circuit pour `verifier-invariants.py`.**
  `CIRCUITS = ["doctrinal", "atelier", "label", "meta"]` : `circuit_de()` renvoyait
  `None`, donc **B1** (clés de Sceau) et **C3** (étanchéité) n'ont contrôlé **aucune**
  des 28 fiches depuis l'ouverture du circuit. Forme exacte de PRO-01. Découvert
  **par accident** — le nouveau refus D6 avait besoin d'un résolveur de circuit.
- **`ETANCHEITE_INTERDITE` ne portait pas « doctrinal/ → hermeneutique/ : jamais »**,
  que `hermeneutique/CLAUDE.md` énonçait sans que rien ne le garde.
- **`to-original` est né sans garde**, la veille du jour où `liens_doctrinal` avait été
  câblé *avec* la sienne. La leçon avait été écrite et n'a pas tenu vingt-quatre heures.

**Ce que cela dit** : un trou de contrôle ne se trouve pas en le cherchant, mais en
construisant autre chose qui a besoin de la pièce manquante. Les trois l'ont été ainsi.

## 5. Deux mesures qui ne se confondent pas

Le §VII a d'abord porté un chiffre mêlant deux unités sans le dire — 3043 clés recollées
(clés **brutes**, avant filtre) contre +154 termes (termes **retenus**, sur l'artefact) —
et affirmait « aucune clé latine altérée » quand trois disparaissaient.

Corrigé **avant commit**, sur le motif que le §VII se déclare lui-même « mesuré, non
allégué » : le Cmd 5 vaut pour le protocole comme pour les fiches. **Une mesure sans son
unité n'est pas une mesure.**

## 6. Ce que la mesure a empêché d'écrire

Trois règles ont été **écartées avant d'être inscrites**, chacune par un relevé préalable :

- **« Jamais d'annotation dans une citation »**, entendue comme « dans un blockquote ».
  Relevé sur `doctrinal/` : les blocs `>` y sont massivement **la voix propre du dépôt** —
  `> **Statut**` (53), `> **Généalogie des idées**` (53), `> **Examen formel**` (50),
  `> 🔍 **Discernement**` (49), plus les blocs `> 🌐 **Forme Traditionnelle Divergente**`
  et `> ⚠️ **Déviation Profane**` que le §VII prescrit lui-même. Ce sont **les blocs les
  plus denses en terminologie du circuit** : la règle inférée aurait fermé la porte
  principale, **en silence**. Resserrée sur le *texte reçu*.
- **Exclure `entite` de `hermeneutique/`**, tiré de « le *hozo* y est exclu par défaut ».
  Cette clause régit les **joints entre traditions**, non la faculté de nommer une entité
  reçue. La garde aurait bloqué une distinction légitime au lieu d'en imposer une.
- **Rendre `RE_CODE` tolérant au retour à la ligne**, pour masquer un incise coupé en
  deux. Mesuré : rendu glouton par les backticks orphelins, il avalerait **186 819
  caractères** de `doctrinal/annales.md`. **Le remède était pire que le mal.**

**Règle qui s'en dégage** : une prohibition dont la portée est *inférée* et non *mesurée*
est de la même famille que la porte sans garde. Elle paraît protéger et elle ferme.

## 7. Le régime apparié, vérifié huit fois

Le régime d'annotation appariée veut que l'HTML **type** ce que le graphe voit déjà, sans
jamais porter l'existence d'un lien. Ce n'était qu'une intention de conception.

Après **chacune** des huit passes d'annotation, le graphe a été régénéré et ses **arêtes
comparées terme à terme après tri** : **1937, rigoureusement identiques, à chaque fois**.
936 annotations, **zéro lien créé**. Les nœuds ne diffèrent que des `updated:` remontés.

**C'est la seule preuve qui vaille** : le régime n'est plus une discipline qu'on affirme,
c'est un fait qu'on remesure. Toute passe future doit refaire cette comparaison — non le
compte des arêtes, qui peut coïncider par hasard, mais leur **contenu trié**.

## 8. Le partage des définitions canoniques

Trois fonctions sont désormais détenues en un seul point et **importées** :

| définition | détenteur | importée par |
|---|---|---|
| `fichiers_suivis()` — la matière du dépôt | générateur d'index | validateur |
| `est_ecriture_originale()` | **`verifier-invariants.py`** | générateur |
| `circuit_de()` | **`verifier-invariants.py`** | validateur |

Le **sens** de la dépendance est délibéré : l'outil de R&D dépend du contrôleur racine,
jamais l'inverse — le contrôleur doit tourner même si le pôle `rd/` est absent. L'absence
du détenteur provoque un **refus franc et nommé**, jamais un repli silencieux sur une
copie locale : *un index construit sur une seconde définition paraîtrait juste sans
l'être.*

## 9. Ce qui relève du jugement, et qui n'a pas été scripté

La chaîne est déterministe de bout en bout **sauf un maillon** : la classification des
candidats en `<dfn>` (terme) ou `<span data-genre>` (nom, avec l'un des genres clos).
C'est la contribution propre de la machine au sens du **Cmd 12** — catégorisation
formelle, non perception de principe — et elle a été versée dans des **tables JSON
relisibles**, jamais dans le code.

Les rejets sont l'autre moitié de cette contribution, et ils sont massifs : sur les 5
circuits, **environ 1900 poses proposées pour 936 retenues**. Deux familles dominent :

- les **noms communs français** que le repli ASCII rend homographes d'un tag —
  `métaphysique`, `sainteté` (glose de *walāya*), `isthme` (glose de *barzakh*), `être`,
  `centre`, `nombre`, `soleil` ;
- le **vocabulaire de gouvernance du dépôt lui-même** — `chantier` (21 occurrences),
  `infrastructure` (12), `veille`, `registre`, `monitoring`, `spec`, `README`,
  `transcription`, `manifeste`, `scan`, `catalogue`.

**Le second est le plus insidieux** : ce sont de vrais termes, mais du dépôt et non de la
doctrine. Les laisser entrer aurait noyé les 936 annotations utiles sous le bruit de
l'outillage — un index qui s'indexe lui-même.

## 10. Le vocabulaire clos a joué son rôle en refusant

Trois fois, aucun genre du vocabulaire clos ne convenait : `califat` (institution),
*Éditions Le Turban Noir* (maison d'édition), *Nurasunna* / *SeekersGuidance*
(organisations contemporaines). Forcer `entite`, réservé au métaphysique, aurait été une
**faute de catégorie**.

Ils sont restés sans genre. **Un vocabulaire clos qui s'étire cesse d'être clos**, et
perd la seule propriété qui le rende contrôlable. Quand `hermeneutique/` a réellement eu
besoin de mots, la réponse n'a pas été d'étirer les sept existants mais d'**emprunter au
circuit son propre champ `type:`** — cinq genres qui portaient déjà leur garde Cmd 3.
`categorie-editoriale`, le seul mot véritablement ajouté de toute la session, porte sa
limite **dans son nom** : *éditoriale* dit marché du livre, jamais catégorie de
connaissance.

## 11. La règle non outillable, et sa gestion

La règle 5 des placements — *jamais dans un texte reçu* — **ne peut pas être outillée** :
rien ne distingue mécaniquement une citation transcrite d'un bloc de la voix propre du
dépôt (cf. §6).

Elle a donc été appliquée **à la main, deux fois, avec l'exclusion nommée** :

- les **7 fiches de transcription** de `doctrinal/sources/` (corps et index du *Kitāb
  al-Taʿrīfāt*, Meftah, annexes des *Révélations de la Mecque*, anneau des 28 lettres,
  index Tilak, table des matières de *L'Homme et son devenir*) ;
- `atelier/rd/bibliotheque/` (**21 fiches**) — transcriptions des sommaires, index et
  glossaires d'ouvrages physiques.

**Une règle non outillable se tient en la déclarant à chaque application**, jamais en la
laissant à la vigilance. Sa trace est dans les annales, pas dans un script.

## 12. Écarts ouverts à la clôture (Cmd 12 — rapportés, non corrigés)

- **`doctrinal/doctrines/`**, cité à l'arbre du §II, **est absent du disque**. Écart
  antérieur à cette session, toujours ouvert.
- **125 des 158 clés `<dfn>` n'ont pas de fiche doctrinale** portant `tradition_cadre` :
  elles restent intypables hors `doctrinal/`, où la fiche citante fournissait le cadre.
- **48 des 132 appariements Jurjānī sont à sens unique** — leur translittération
  n'apparaît nulle part dans le dépôt, et le vocabulaire du dictionnaire n'y a pas été
  injecté.
- **Les syntagmes ne sont pas appariables** : `chikai to seiyaku / 誓約と制約` est une
  paire de syntagmes, les clés de l'index sont des tokens. Limitation structurelle.
- **`D5` garantit l'unicité de la clé, jamais celle du référent** : `guenon` et
  `rene-guenon` désignent la même personne sous deux clés et coexisteraient sans refus.
  Écarté à la main cette fois ; le contrôle ne le verrait pas.
- **Un incise de code coupé sur deux lignes échappe au masquage** — correctif mesuré et
  écarté (§6).
- **`mangaka`, les studios et `saga`** restent sans genre dans `hermeneutique/`.
- **`label/` n'a produit aucune pose retenue** : son vocabulaire est entièrement de
  gouvernance.
- **Fiches sans candidat annotable**, l'appariement D1 interdisant de contourner
  l'absence de tag ou de lien : 41 en `symboles/`, 24 en `sources/`, 14 en
  `discernement/`, 11 en `autorites/`, 3 en `traditions/`, 3 en `deviations/`, 2 en
  `etudes/`.
- **Les artefacts dérivés `index-lexical.json` / `.md` restent hors dépôt** — le `.md`
  pèse plus de 1 Mo, poids à instruire avant de le verser sur un dépôt consulté depuis
  Obsidian iPad.

## 13. Un écart de forme de la session elle-même

L'entrée d'annales du 2026-09-09 sur `categorie-editoriale` a été versée **dans le commit
d'archivage lui-même**, avec un SHA en attente, alors que le **Cmd 9** veut qu'elle soit
rédigée *après* le commit. Corrigé par un commit de journal séparé, et consigné dans
l'entrée. Signalé ici parce que la faute est **structurelle et récurrente** : elle guette
chaque fois qu'un lot groupe protocole, outillage et annales.

## 14. Ce qu'une session suivante devrait reprendre

Par ordre de rendement décroissant, et sans qu'aucun de ces points ne soit tranché :

1. **Le référent, non la clé.** `D5` ne voit pas que `guenon` et `rene-guenon` sont la
   même personne. Une table de formes courtes, ou un contrôle sur le référent, fermerait
   l'angle mort le plus large restant.
2. **La tradition des 125 clés sans fiche.** Chacune attend soit sa fiche doctrinale,
   soit un champ portant sa tradition — sans quoi elles restent intypables hors du
   circuit doctrinal.
3. **Le poids du condensé.** 1 Mo de markdown est hostile à Obsidian sur iPad. Un
   découpage par initiale, ou un condensé restreint aux termes multi-fiches, est à
   instruire avant de verser l'artefact au dépôt.
4. **La réciprocité complète (§VII, point 6)** : 48 appariements à sens unique, et la
   question — non tranchée — de savoir si la forme latinisée d'une autorité textuelle a
   sa place dans un index qui est celui du **wiki**.
