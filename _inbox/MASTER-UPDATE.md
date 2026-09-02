---
chantier: DOC-07
ouvert: 2026-09-02
---
# Plan d'ingest — DOC-07 : Osman Yahia (classification Ibn ʿArabī) et Al-Futūḥāt al-Makkiyya (Maymaniyya, t. 1)

## Ce que cette pièce est, et ce qu'elle n'est pas

Un **plan**, comme `MASTER-UPDATE.md` l'a été pour DOC-06. Ni un ingest fait, ni
une autorisation. **Aucune fiche n'est écrite tant que Sidy n'a pas visé ce
plan.** Deux sources très différentes, traitées séparément parce que leur risque
l'est.

## 1. Osman Yahia — *Histoire et classification de l'œuvre d'Ibn ʿArabī* (1964)

### 1.1 Ce que c'est

Thèse de l'Institut Français de Damas (Osman Yahia, 1964) : le catalogue
critique de référence de l'œuvre d'Ibn ʿArabī — 851 ouvrages numérotés
(« numéros OY », cités dans toute l'orientalisme akbarien depuis), avec
répertoire, tables de correspondance manuscrits/imprimés, table des noms
propres. **Ce n'est pas un texte d'Ibn ʿArabī** : c'est un instrument d'érudit
pour authentifier, dater et situer ce qu'on lit *sous son nom*.

### 1.2 État de la conversion (déjà faite, au sas)

`_inbox/conversions/chapitres-osman-yahya/` — 17 fichiers, 40 007 lignes,
chaîne `pdftoppm 300dpi + tesseract 5 (fra)`, français uniquement (`-l fra`
assumé — les passages en graphie arabe ne sont pas OCRisés). Qualité
**contrôlée et documentée en tête de la conversion elle-même** (chose que Tilak
n'avait pas) :
> « Les translittérations diacritées sont approximatives... Ne jamais citer une
> translittération d'après cette sortie sans retour au scan. »

Un fichier reste volontairement d'un seul tenant : `osman-yahya-08-repertoire.md`
(18 111 lignes, numéros d'ouvrage 1 à 851) — non découpé par chapitre, découpable
par tranches si besoin s'en fait sentir.

### 1.3 Ce que l'ingest produirait

| # | objet | destination | statut |
|---|---|---|---|
| 1 | Le texte converti (17 fichiers) | `textes/osman-yahya-histoire-classification-oeuvre-ibn-arabi/` | cabinet de lecture, pas de Sceau |
| 2 | Une notice de source | `doctrinal/sources/osman-yahia-histoire-classification-1964.md` | `academique` |

**Une notice, pas dix-sept fiches** — même principe qu'à DOC-06 : le sujet
d'une notice de source est l'ouvrage, non le chapitre.

**Pourquoi la notice est justifiée** (test DOC-06 : besoin déjà exprimé, pas
volume de source) : le dépôt porte déjà plusieurs fiches Ibn ʿArabī avec des
marqueurs `to-source` sur l'attribution ou la datation d'un texte cité « sous
son nom » — la notice donne l'instrument pour vérifier, elle ne lève aucun
`to-source` par elle-même (aucune levée sans retour au scan/à l'édition
primaire, discipline des sources §VII).

**Ce qui n'est pas proposé** : aucune fiche sur le contenu du répertoire
(851 entrées) — il reste ce qu'il est, un instrument consulté à la demande
depuis `textes/`, pas transformé en page doctrinale.

### 1.4 Signalement doctrinal à porter dans la notice

Osman Yahia est un travail d'orientalisme scientifique, **statut `academique`**
comme Tilak — mais l'analogie s'arrête là : il ne prétend à aucune thèse
disputée sur la Tradition, c'est un travail de catalogage. Aucune réserve de
fond équivalente aux trois posées sur Tilak n'est nécessaire ; une seule
prudence à écrire : les numéros OY identifient un texte, ils ne garantissent
pas son authenticité intrinsèque — question qui reste, comme toujours, du
ressort de l'examen humain.

## 2. Al-Futūḥāt al-Makkiyya — édition Maymaniyya, tome 1

### 2.1 Ce que c'est, et pourquoi c'est d'une autre nature

Le texte arabe original de l'œuvre maîtresse d'Ibn ʿArabī — `traditionnel`,
rang le plus élevé du dépôt sur ce tradition_cadre. **Un seul tome sur les
quatre de l'édition Maymaniyya.** Rien de comparable, en gravité, à Tilak ou
même à Osman Yahia : ce n'est pas un commentaire, c'est la source elle-même.

### 2.2 État de la conversion — ⚠ non exploitable en l'état

779 pages, `pdftoppm 300dpi + tesseract 5 (ara)`, **jamais découpé par
chapitre**, un seul fichier de 34 998 lignes. Échantillon relevé au hasard
(ligne 5000) :

```
ان ظل يهذى لوهم » رأشسه يتش دق
وكل من قال فولا » فالذ كر من ذاك أصدق
```

Comparer au relevé Tilak (« CHAPTER ITIL » pour III) : ici, la dégradation
n'est pas ponctuelle, elle est **structurelle**. Le texte arabe non vocalisé,
en ligature, sort de Tesseract 5 largement corrompu — mots recomposés au
hasard, ordre des lettres parfois inversé. Ce n'est pas un texte relisible
caractère par caractère comme pour l'anglais de Tilak : sur cet échantillon, la
proportion de suites illisibles est trop haute pour qu'une relecture partielle
suffise à en garantir la fidélité globale.

**Aucune citation n'en est envisageable** — la discipline de fiabilité qui a
permis d'utiliser l'OCR anglais de Tilak (relecture caractère par caractère
avant toute citation) ne peut pas s'appliquer à un volume de cette taille avec
cette densité de corruption : la charge de vérification dépasserait ce qu'un
usage ponctuel justifie.

### 2.3 Ce que ce plan propose — trois options, tranchées par Sidy, pas par la machine

Le dépôt n'a, à ce stade, **aucun besoin déjà exprimé** qui appellerait un
ingest du texte arabe de la Futūḥāt (contrairement à Osman Yahia, où les
`to-source` existants motivent la notice) : toutes les citations actuelles du
dépôt passent par des traductions publiées et vérifiées (Penot). Trois voies,
sans recommandation de la machine sur ce qui touche à la fiabilité d'une source
de premier rang (Cmd 12) :

- **(a) Rien ne bouge** : le PDF reste en `raw/`, la conversion `.md` actuelle
  est retirée du sas sans être versée nulle part — elle ne répond à aucun
  besoin et son état ne permet la vérification de rien.
- **(b) Versée à `textes/` avec avertissement bloquant en tête** : le cabinet
  de lecture accepte des originaux non relus (LISEZ-MOI.md le prévoit pour
  Tilak/Orion) ; ce serait le premier texte arabe du cabinet, avec un
  avertissement plus sévère qu'ailleurs — « non citable en l'état, aide au
  repérage de page uniquement ».
- **(c) Nouvelle tentative d'OCR** avant toute décision de versement —
  hors du périmètre de ce plan (question d'outillage, pas d'ingest ; à ouvrir
  comme chantier `atelier/rd/outillage` séparé si retenue).

Dans les trois cas : **aucune fiche doctrinale n'est proposée** sur ce tome —
ni notice de source, ni matière. Une notice sur un texte qu'on ne peut pas
lire fiablement serait une affirmation sans le contrôle qui la justifie
(Cmd 5).

## 3. Ordre de traitement proposé

1. Osman Yahia : notice écrite, texte versé à `textes/`, sas vidé de cette part.
2. Futūḥāt Maymaniyya : **attente du choix (a)/(b)/(c)** — rien n'est écrit
   avant ; le fichier reste au sas ou est retiré selon la réponse.

## 4. Ce que ce plan attend de Sidy

| # | question | pourquoi |
|---|---|---|
| 1 | Le plan est-il visé pour sa partie Osman Yahia (notice + versement `textes/`) ? | Cmd 6 |
| 2 | Une seule notice de source est-elle le bon découpage pour Osman Yahia, ou faut-il plus ? | proportion, comme DOC-06 |
| 3 | Futūḥāt Maymaniyya t. 1 : (a) rien ne bouge, (b) versé à `textes/` avec avertissement sévère, ou (c) nouvelle tentative d'OCR d'abord ? | la machine ne tranche pas la fiabilité d'une source de premier rang |
| 4 | Si (a) ou en attendant (c) : le fichier `.md` actuel au sas est-il supprimé (le PDF source reste intact en `raw/`, Cmd 10) ? | rien ne doit traîner au sas sans destination |
