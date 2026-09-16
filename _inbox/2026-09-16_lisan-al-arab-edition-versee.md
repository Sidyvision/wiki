---
title: "Lisān al-ʿArab — édition numérique versée dans raw/ (2026-09-16)"
type: note
statut: proposition au sas — non versé aux circuits
date: 2026-09-16
---

# *Lisān al-ʿArab* — édition numérique versée dans `raw/`

> **Pièce de sas.** Elle rapporte un versement **déjà fait** (sur ordre de Sidy, en
> session) et les propositions qui en découlent. **Aucune page de circuit n'a été
> écrite** : ni fiche `doctrinal/sources/`, ni ligne de registre, ni entrée d'annales,
> ni index. Rien de ce qui suit n'est appliqué (Cmd 6, Cmd 12).

## 1. Ce qui a été versé

`raw/lisan-al-arab/` — **41 fichiers de charge utile, 410,5 Mo** (43 avec la fiche de
provenance et le script d'empreintes), deux éditions de la même impression :

- **Édition A, texte né-numérique** : المكتبة الشاملة, *Lisān al-ʿArab*, **ط. دار صادر —
  بيروت، الثالثة 1414 هـ**, 15 volumes, حواشي اليازجي, `book_id` 1687. Extraite du jeu de
  données `MoMonir/shamela_books_text` (HuggingFace, apache-2.0) : **8 116 pages** (une
  ligne = une page imprimée), 25,0 M caractères, notes de bas de page en champ séparé.
  Livrée en TSV page par page, en texte continu à marqueurs `[ج<vol> ص<page>]`, et en
  quinze fichiers par volume, prêts pour la transcription.
- **Édition B, témoin visuel** : scan de **la même édition imprimée** (دار صادر, 15
  volumes, 8 197 pages PDF), `archive.org/details/1_20240125_20240125_0340`.
- Détail complet, éditions, empreintes MD5, mesures et réserves :
  `raw/lisan-al-arab/PROVENANCE.md`.

**Pourquoi ces deux-là ensemble** : elles **coïncident page pour page** (§2). Le texte
seul ne se vérifie pas ; le scan seul ne se transcrit pas (`OUT-08` : l'OCR arabe du dépôt
n'est pas citable, Cmd 5). Les deux ensemble donnent un texte transcrivible **et**
vérifiable sur l'image de la page même.

## 2. La vérification faite, et sa portée

Sur **cinq folios**, dans quatre volumes, le folio imprimé lu sur l'image de la page PDF
de même rang est **le même nombre** — décalage **nul** entre page PDF et page imprimée,
donc entre le texte clavé et l'imprimé :

| Volume | Page PDF | Folio imprimé lu |
|---|---|---|
| ج1 | 100 | **١٠٠ = 100** |
| ج3 | 500 | **٥٠٠ = 500** |
| ج8 | 200 | **٢٠٠ = 200** |
| ج11 | 400 | **٤٠٠ = 400** |
| ج15 | 382 | **٣٨٢ = 382** |

Et sur la page imprimée **382** du tome 15, la **colonne de droite** de l'image et le texte
extrait se lisent **mot pour mot** (« والوَحاء الوَحاء ! يعني البِدارَ البِدارَ… »), le titre
courant des colonnes étant **و ح ي**.

Pièces visuelles : `raw/lisan-al-arab/verification/` (5 folios, la colonne, la pleine page).

**Portée, bornée** : cinq folios pour la coïncidence des paginations, une entrée pour la
fidélité du texte à l'image. La **coïncidence des paginations** et l'exploitabilité de
l'ensemble sont établies ; **les 8 116 pages ne sont pas attestées une par une**. Aucune
citation n'est levée de son `to-source` par cette passe : la levée appartient à Sidy
(§VII.2).

## 3. Signalement — une référence de page à corriger

`doctrinal/symboles/formule-al-waha-al-ajal-al-saa.md`, §« Le sens des mots », cite le
*Lisān* : « article وحي (**tome 15, pp. 172-173**, texte consulté sur la bibliothèque
Islamweb le 2026-09-13) ».

Sur l'édition de référence versée aujourd'hui — texte **et** image — l'entrée se trouve au
**tome 15, pp. 379-382** ; le passage cité est **à cheval sur la fin de ص381 et le début
de ص382** :

- ص379 (fin) : « وحي: الوَحْيُ: الإِشارة وَالْكِتَابَةُ والرِّسالة… » — ouverture de l'entrée ;
- ص381 (fin) : « والوَحى: العَجَلةُ، يَقُولُونَ: الوَحى الوَحى » ;
- ص382 : suite et citations (*Tahdhīb*, *Ṣiḥāḥ*, vers d'Abū al-Najm, *tawaḥḥah*).

**Écart : 209 pages.** Ce n'est pas une coquille de saisie mais vraisemblablement une
**autre pagination** (celle d'Islamweb, ou d'une autre édition) reprise sans être déclarée
comme telle. Les quatre éléments que la fiche donnait pour « à vérifier sur une édition
imprimée » sont **tous présents** sur l'image, aux pages ci-dessus.

**Ce que la machine ne fait pas** : corriger la fiche (Cmd 12), ni lever les `to-source`
(§VII.2). Elle signale, et la correction proposée est exactement : porter la référence au
**tome 15, pp. 379-382**, en nommant l'édition (دار صادر, 3ᵉ éd. 1414 هـ) — et, si la
référence d'origine doit survivre, la marquer comme provenant d'une autre pagination.

## 4. Signalement — U+200C dans le texte clavé (Cmd 15)

**1 520 occurrences de U+200C (ZWNJ)**, toutes dans le champ `texte` (**aucune** dans les
notes), toutes en **tête de page** — artefact de la source, non de l'extraction, qui n'en
a ni créé ni retiré. Le texte est **fidèle** ; c'est précisément pourquoi les invisibles y
sont.

Conséquence : dès qu'une conversion vers `textes/` sera faite, **le contrôle d'hygiène
Unicode refusera le fichier** — à juste titre. Deux voies, réservées au verdict :

- **(a)** retrait par le script de conversion, dans la procédure même du §II (retrait
  démontré **non substantiel** par mesure — ce qui est le cas : invisibles de présentation
  en tête de page —, exécuté par script **déterministe** dont le garde-fou aura été **vu
  refuser** sur faute fabriquée, consigné à l'`index-conversion.md` de la conversion) ;
- **(b)** exception déclarée au registre `config/hygiene-unicode-exceptions.yaml`, comme
  les 22 résidus tranchés le 2026-08-31 — mais ce registre porte des verdicts **déjà
  rendus** ; y verser 1 520 invisibles **non tranchés** serait une qualification déguisée.

La voie (a) est celle qui laisse le commandement intact. Elle n'est pas engagée ici.

## 5. Propositions (aucune appliquée)

1. **Fiche `doctrinal/sources/lisan-al-arab.md`** — `type: source`, portant l'édition
   exacte, les deux témoins et leurs empreintes, et un `to-source` **unique et honnête**
   sur ce qui n'est pas vérifié (les 8 116 pages). Le champ `status` n'est **pas** proposé
   par la machine : il relève du verdict (Cmd 12) — le *Lisān* est une œuvre lexicographique
   classique, la qualification (traditionnel / academique) ne se déduit pas de son genre.
2. **Correction de la référence de page** dans
   `doctrinal/symboles/formule-al-waha-al-ajal-al-saa.md` (§3) — et, dans la même passe, la
   levée des `to-source` de cette fiche, **si et seulement si** Sidy vérifie lui-même les
   quatre passages sur l'image.
3. **Ligne de chantier `BIB-05`** au registre du pôle R&D : *« adressabilité par racine du
   *Lisān al-ʿArab* »*. Objet : le *Lisān* se range **par dernière radicale, puis par
   première, puis par seconde** (arrangement d'al-Ṣiḥāḥ) — retrouver une racine à la main
   dans 8 200 pages est le geste qui bloque `BIB-04`. Un index mécanique `racine →
   (volume, page)` se construit sur le texte versé ; sa valeur se **mesure** (combien des
   97 racines déjà moissonnées deviennent adressables). Aucun code avant visa : triptyque
   à rédiger (Cmd 6).
4. **Sort du script d'extraction.** `extraire-lisan-shamela.py` est déposé dans `raw/`
   (hors git). Sa place naturelle est `atelier/rd/outillage/` — un script qui produit une
   pièce du dépôt est de l'outillage, et il doit être versionné pour audit. Copie jointe au
   sas : `_inbox/2026-09-16_lisan-al-arab_extraire-shamela.py`.
5. **Entrée d'annales** (à passer après le commit, Cmd 9) :

   ```
   ## [2026-09-16] ingest | Lisān al-ʿArab — édition numérique versée dans raw/
   - Édition A (texte né-numérique) : Shamela book 1687, ط. دار صادر 1414 هـ, 15 vol.,
     8 116 pages ; édition B (scan-témoin de la même impression, 8 197 p. PDF).
   - Paginations vérifiées coïncidentes : folio ٣٨٢ lu sur l'image de la page 382 du
     tome 15, colonne de droite identique mot pour mot au texte extrait.
   - Signalement : `doctrinal/symboles/formule-al-waha-al-ajal-al-saa` cite le tome 15
     pp. 172-173 ; le passage est à pp. 379-382 (écart 209 p., autre pagination).
   - U+200C ×1 520 (tête de page, champ texte) dans le texte clavé — voie de retrait
     proposée, non engagée (Cmd 15).
   - **Commit** : <sha>
   ```

## 6. Ce qui n'a pas été fait

- Aucune écriture dans un circuit : `doctrinal/`, `atelier/`, `label/`, `hermeneutique/`,
  `meta/` sont **intacts**.
- Aucun `textes/` : la conversion n'est pas engagée (elle viendra « plus tard », sur la
  consigne de Sidy — le versement est précisément ce qui la prépare).
- Aucun `to-source` levé, aucune fiche créée, aucun index bâti, aucune annales écrite.
- Aucun OCR versé : mesuré inexploitable (§3 de `PROVENANCE.md`).
- Le CSV source (473 Mo) et les fichiers temporaires de travail n'ont pas été conservés ;
  `raw/lisan-al-arab/` ne porte que les deux éditions, leurs dérivés, le script et les
  pièces de vérification.
