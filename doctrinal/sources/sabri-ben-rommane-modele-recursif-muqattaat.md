---
title: "Sabri B. Rommane — modèle récursif des muqaṭṭaʿāt (Sūrat Qāf)"
type: source
status: academique
tradition_cadre: "islam"
tags: [muqattaat, coran, sourate-qaf, recursion, structure, iltifat, ijaz, blogging-theology]
created: 2026-09-04
updated: 2026-09-09
sources: ["[[doctrinal/sources/gloton-approche-coran-grammaire-lexique]]"]
sources_count: 1
cross_links: ["[[doctrinal/symboles/ilm-al-huruf]]", "[[doctrinal/sources/gloton-approche-coran-grammaire-lexique]]"]
---

# Sabri B. Rommane — modèle récursif des *muqaṭṭaʿāt*

## Identification

- **Auteur de la thèse** : **Sabri B. Rommane** (graphie de la diapositive ;
  le dossier `raw/` porte « Sabri Ben Rommane »).
- **Support** : entretien vidéo de la chaîne **<span data-nom="blogging-theology" data-genre="ouvrage">Blogging Theology</span>** (hôte : Paul
  Williams), diaporama projeté par l'auteur.
- **Titre de la vidéo** : *Did the Qur'an Hide a Secret Algorithm for 1400 Years?*
- **Chaîne** : **Blogging Theology**. **Mise en ligne** : **2 mai 2026**.
- **Lien** : `https://youtu.be/-8P-D_agsdc` (communiqué par Sidy le 2026-09-04).
  ✅ **Apparat établi par Sidy le 2026-09-04** — titre, chaîne et date relevés par
  consultation humaine, la consultation automatique ayant été refusée (page
  anti-robot). La vidéo elle-même n'a pas été visionnée par la machine : la
  présente fiche repose sur les captures d'écran, non sur la bande. Le lien reste
  un *repère de provenance* ; il ne lève aucun `to-source`.
- **Base de la présente fiche** : les **42 captures d'écran** versées dans
  `raw/The Sabri Ben Rommane's Theory/` (IMG_0443 → IMG_0486). `raw/` est
  *gitignored* — les fichiers ne sont pas versionnés, mais leur nom rend la
  collation reproductible.
- **Nature** : exposé d'une hypothèse structurelle **en cours de rédaction** et
  **non publiée en revue**. L'auteur le dit lui-même (IMG_0485) : « Only three
  surahs tested […] Need peer-review ».
- **Statut** : `academique`. C'est un travail d'analyse structurelle, argumenté et
  falsifiable, non un texte d'autorité doctrinale. Il établit — si confirmé — un
  **fait de structure** sur le texte ; il ne dit rien de son sens au plan des
  principes.

> ⚠️ **Ce que cette fiche n'est pas.** Elle ne valide ni n'invalide la thèse. Elle
> consigne ce que l'auteur avance, ce que la vérification déterministe reproduit,
> et les tensions formelles relevées. La portée métaphysique de l'*iʿjāz* invoqué
> en IMG_0483 n'est pas du ressort de la machine (Cmd 12).

## La thèse en propre

Chaque lettre isolée en tête de sourate est traitée comme une **graine**. On
remplace récursivement chaque lettre par les lettres de son **nom arabe** (ق →
ق ا ف). L'auteur nomme le procédé *« linguistic fractal »*. Au niveau 4 la
population de lettres se **stabilise** (aucune lettre nouvelle) ; le **niveau 5**
sert de « Control Level and encryption key ».

Le découpage de la sourate s'obtient en groupant les lettres du niveau 5 **par leur
parent de niveau 4**, la taille de chaque groupe valant la longueur du nom du
parent (IMG_0447). Appliqué à **Sūrat Qāf** (45 āyāt), cela donne 17 groupes, eux-mêmes
emboîtés en *Subsections* et *Major Sections*. La prétention centrale est
**prédictive** : les frontières ainsi engendrées doivent coïncider avec les
ruptures thématiques et les ***<dfn data-terme="iltifat" data-translit="iltifāt" data-tradition="islam">iltifāt</dfn>*** du texte.

## Collation du lot photographique

| Fait | Constat |
|---|---|
| Fichiers présents | 42 (IMG_0443 → IMG_0486) |
| **IMG_0456** | **absent** — lacune non comblée |
| **IMG_0471** | **absent** — lacune non comblée |
| IMG_0474 / IMG_0475 | **deux captures d'une même diapositive** (Groupe 17) |
| Diapositives distinctes | **41** (42 fichiers − 1 doublon ; les absents ne sont pas décomptés) |

> ⚠️ **Anomalie d'ordre, signalée et non résolue.** IMG_0457 (« Subsections 1-2
> reflective break ») récapitule la clôture du **Groupe 6**, alors que la
> diapositive du Groupe 6 apparaît **après**, en IMG_0458 ; la lacune IMG_0456
> tombe dans cet intervalle. L'ordre des captures n'est donc pas certainement
> celui des diapositives à cet endroit.

## Vérification déterministe (2026-09-04)

Le calcul est déterministe : il a été **scripté**, non délégué au jugement du
modèle. Script et spécification :
`atelier/rd/outillage/verifier-recursion-qaf.py` et
`atelier/rd/outillage/spec-verifier-recursion-qaf.md`. Les noms de lettres sont
pris du **tableau de l'alphabet de Gloton**
([[doctrinal/sources/gloton-approche-coran-grammaire-lexique]], repère **Aa**,
`textes/une-approche-du-coran-gloton/corps-du-texte.md`).

### Constat 1 — la règle énoncée ne produit pas les chiffres publiés

L'auteur énonce en IMG_0445 et IMG_0479 : **« Hamza = terminal node »**, ce qui
suppose que la hamza est **émise** puis cesse de se brancher — le nom de *fāʾ*
étant alors ف ا ء.

| Variante | Règle | Série L1→L5 | Concorde avec IMG_0480 ? |
|---|---|---|---|
| **A** | hamza **émise**, terminale (*fāʾ* → ف ا ء) | 3, 9, 25, 67, **179** | ❌ non |
| **B** | hamza **jamais émise** (*fāʾ* → ف ا) | 3, 8, 21, 56, **151** | ✅ oui |

La série publiée (IMG_0480 : « L₀=1, L₁=3, L₂=8, L₃=21, L₄=56, L₅=151 ») exige la
variante **B**. La règle **opérante** n'est donc pas la règle **énoncée**.

> **La contradiction est interne au diaporama, et non un désaccord de lecture.**
> La diapositive IMG_0446 donne elle-même son niveau 2 développé : **ق ا ف ا ل ف ف ا**
> — huit lettres, **aucune hamza**. L'exemple travaillé par l'auteur suit la
> variante B ; sa formulation en prose suit la variante A.

**Incertitude de lecture consignée** : la vignette d'IMG_0446 se lit « 131 » à la
résolution disponible, là où IMG_0480 et IMG_0481 donnent **151** et où le calcul
donne **151**. Les trois observations sont enregistrées ; **aucune coquille n'est
affirmée** sur une image non relisible.

### Constat 2 — le découpage publié, lui, est exactement reproduit

En variante B, les tailles des **17 premiers parents de niveau 4** donnent :

```
dérivé  : [3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2]
IMG_0447: [3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2]   → identiques
somme   : 45 = nombre exact d'āyāt de Sūrat Qāf, sans troncature
```

**Confirmation indépendante, plus forte que les seules tailles** : chaque
diapositive de groupe est étiquetée de sa **lettre-parent**. La suite relevée sur
les diapositives — G1 ق, G2 ا, G3 ف, G4 ا, G5 ل, G6 ف, G7 ف, G8 ا, G9 ا, G10 ل,
G11 ف, G12 ل, G13 ا, G14 م, G15 ف, G16 ا, G17 ف — **est mot pour mot le niveau 4
dérivé** ق ا ف ا ل ف ف ا ا ل ف ل ا م ف ا ف. La reproduction porte donc sur les
lettres elles-mêmes, pas seulement sur leur compte.

> **Résultat reproduit.** Sous la règle opérante (B), le motif publié suit
> effectivement du procédé publié. Le constat 1 porte sur l'énoncé de la règle,
> **pas** sur la validité arithmétique du découpage.

### Constat 3 — une troisième incohérence, sur la diapositive IMG_0447

Elle énonce : « 3-letter names (Qāf, Alif, **Fā**) → 3-verse groups ; 2-letter
names (**Fāʾ, Alif**) → 2-verse groups ». *Alif* et *Fā* figurent chacun dans les
**deux** colonnes. Les listes correctes sont Qāf / Alif / Lām / Mīm → 3 et
Fāʾ / Yāʾ → 2. Le motif publié sur la **même** diapositive est néanmoins juste :
l'erreur est dans la légende, pas dans le résultat.

## Contrôle lexical par Gloton — ce qu'il borne

L'auteur appuie son traitement de la hamza sur *« school of thought of arabic
grammar »*, sans nommer d'école. Le lexique de Gloton donne à cette formule vague
un **référent réel**, et rien de plus :

- Le tableau de l'alphabet (repère **Aa**) donne هَمْزَة *hamza* avec valeur
  numérique « — » et ألِف *'alif* avec valeur 1 ; le *relevé* de la même section
  énonce que l'alphabet compte **28 consonnes portant valeur numérique, la hamza
  n'en portant aucune**.
- Gloton documente que la hamza est considérée **par certains grammairiens** —
  il nomme **al-Khalîl**, et **Régis Blachère** côté français — tantôt comme
  « attaque vocalique », tantôt comme « explosive glottale », c'est-à-dire comme
  un **fait de prononciation** plus que comme une lettre de plein exercice.
- Il distingue la *hamzat al-qaṭʿ* (هَمْزَة القَطْع, stable) de la *hamzat al-waṣl*
  (هَمْزَة الوَصْل, instable), cette dernière **« ne s'écrit ni ne se prononce quand
  elle est en liaison avec un autre mot »** ; et il note que l'*alif* est d'abord
  **le support de la hamza**.

> **Portée exacte.** Ces relevés rendent **plausible** qu'une tradition
> grammaticale ne compte pas la hamza comme lettre à part entière — ce qui est la
> variante **B**, celle qui produit les chiffres publiés. Ils **ne démontrent pas**
> que c'est l'école visée par l'auteur, qui ne la nomme pas. Conformément à
> l'emploi assigné à cet ouvrage : *il borne ce que le lexique autorise à dire*,
> il ne tranche pas.

## Ce que l'auteur concède lui-même

- **IMG_0460** : la cohésion du Groupe 8 « would have been possible to note […]
  **even without our model** (Farrin connection) » — l'apport revendiqué n'est pas
  la détection de l'unité mais son **encadrement prédictif**.
- **IMG_0461** : « This is to have time to also talk about the repercussion and
  the relevance of this finding, **if confirmed**. »
- **IMG_0485** : « But confirmation is not certain : Only three surahs tested
  (single-letter Muqatta'at) · Compound initials (e.g. Alif-Lām-Mīm) not yet
  analyzed · **Need peer-review**. »

La charge argumentative des diapositives IMG_0478 à IMG_0484 (récursion, automate
fini, ensembles stables, anachronisme de 1300 ans, *hiddenness problem*, *<dfn data-terme="ijaz" data-translit="iʿjāz" data-tradition="islam">iʿjāz</dfn>*)
repose **entièrement** sur cette condition non encore remplie.

## Texte converti

`textes/sabri-ben-rommane-theory/corps-du-texte.md` — transcription des 39
diapositives distinctes par lecture directe des captures (2026-09-04), lacunes et
anomalie d'ordre signalées sur place plutôt que reconstituées.

> Comme toute pièce de `textes/` (PRO-08), cette transcription **ne porte aucun
> Sceau**, n'est la cible d'aucun wikilink, et **ne lève par elle-même aucun
> `to-source`** : le contrôle de la source primaire — ici la vidéo et le futur
> article — par Sidy demeure requis (§VII.2, Cmd 5).

## Emploi de cette source dans le dépôt

Instrument de **repérage structurel**, à convoquer là où une thèse porte sur
l'architecture formelle du texte coranique et sur les *<dfn data-terme="muqattaat" data-translit="muqaṭṭaʿāt" data-tradition="islam">muqaṭṭaʿāt</dfn>*. Elle ne
constitue **pas** une autorité sur le sens des lettres isolées : sur ce terrain,
[[doctrinal/symboles/ilm-al-huruf]] tient la doctrine reçue, et le rapport entre
les deux relève d'un examen ouvert, non d'une assimilation.

⚠️ **Piège d'homonymie signalé.** La sourate **Qāf** (<span data-nom="coran" data-genre="ouvrage">Coran</span> L) n'a aucun rapport
établi ici avec le **Mont Qāf** cosmologique (voir
`doctrinal/discernement/2026-07-02_mont-qaf-meru-topologie-apex.md`) :
le rapprochement serait fondé sur le seul nom. **Non-lien délibéré.**

---

## Exécution déterministe confirmée (2026-09-06)

Le script `atelier/rd/outillage/verifier-recursion-qaf.py` a été exécuté le
2026-09-06 et confirme **les deux constats consignés ci-dessus** :

- **Variante A** (règle énoncée par l'auteur, hamza émise puis terminale) :
  produit L1..L5 = `[3, 9, 25, 67, 179]` — **ne concorde pas** avec IMG_0480
  `[3, 8, 21, 56, 151]`.

- **Variante B** (règle opérante déduite des chiffres, hamza jamais émise) :
  produit L1..L5 = `[3, 8, 21, 56, 151]` — **concorde exactement** avec IMG_0480.

- **Découpage en 17 groupes** (variante B) : suite dérivée `[3, 3, 2, 3, 3, 2,
  2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2]` **identique** à IMG_0447 ; somme = 45
  āyāt de Sūrat Qāf.

**Code de sortie : 0** (les deux contrôles concordent avec les chiffres publiés).
La concordance arithmétique de la variante B est un **fait vérifié**, non une
interprétation.
