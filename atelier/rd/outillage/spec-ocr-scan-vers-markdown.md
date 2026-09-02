---
title: "Spécification — Chaîne OCR scan vers Markdown découpé par chapitre"
type: outillage
tags: [rd, outillage, ocr, pdf, numerisation, bibliotheque]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe]]"
  - "[[atelier/rd/bibliotheque/catalogue-bibliotheque]]"
---

# Chaîne OCR — `ocr-scan-vers-markdown.sh` + `decouper-ouvrage-chapitres.py`

> Deux scripts, un seul usage : porter un **scan d'ouvrage** (PDF image, sans
> couche texte exploitable) vers du Markdown découpé par chapitre, exploitable
> au dépôt. Éprouvés le 2026-09-02 sur 781 pages (deux ouvrages de Tilak,
> `raw/orionortheantiqu021979mbp.pdf` et `raw/9566.pdf`).
>
> Comme tout l'outillage du pôle (§VIII) : **déterministes, sans LLM, sans
> réseau**. Le second constate et sort en code non nul quand son invariant est
> rompu ; il ne corrige rien.
>
> **Révision du 2026-09-02 (soir)** — éprouvés sur deux ouvrages
> supplémentaires, 1 475 pages : *al-Futūḥāt al-makkiyya* (arabe, 779 p.) et
> Osman Yahia, *Histoire et classification de l'œuvre d'Ibn 'Arabi*
> (français, 696 p.). La langue devient un paramètre, l'arabe cesse d'être
> une limite, et un jeu de motifs français est ajouté au découpage.

## 1. Ce que la chaîne fait — et ce qu'elle ne fait pas

Elle produit un **texte de repérage**, jamais un texte critique. La sortie est
brute de machine : les translittérations diacritées et le devanāgarī sont mal
rendus. Elle sert à *savoir où chercher*, exactement comme l'instrument de
repérage de `rd/bibliotheque/` — la lecture du texte primaire reste humaine
(§VII). Toute sortie va au sas `_inbox/`, jamais directement dans un circuit.

## 2. Étape 1 — `ocr-scan-vers-markdown.sh`

```
bash atelier/rd/outillage/ocr-scan-vers-markdown.sh \
     <source.pdf> <sortie.md> "<titre>" [langue]
```

Rend chaque page en image (`pdftoppm -r 300 -gray`), l'OCRise
(`tesseract 5`, `--psm 1`), et concatène le tout avec un marqueur
`<!-- page N -->` par page. Deux pages en parallèle (`xargs -P 2`) : c'est le
nombre de cœurs de la machine, monter plus haut ne gagne rien et sature les
3,7 Gio de RAM. Les images intermédiaires sont détruites au fil de l'eau —
sinon 781 pages à 300 dpi remplissent le disque.

**Langue** (4ᵉ argument, ouvert le 2026-09-02) : code `tesseract`, défaut
`eng`. Ex. `fra`, `ara`, `fra+ara`. Une langue non installée fait sortir le
script en **code 2** avec la liste des langues disponibles, sans produire de
fichier : avant cette garde, elle rendait un Markdown vide *sans erreur*, et
une tâche de fond échouait en silence (même famille de piège que le `chmod +x`
refusé, §6). Langues installées à ce jour : `ara`, `eng`, `fra`.

**Débit mesuré** sur le serveur (2 cœurs), à ne pas sous-estimer :

| Langue | Débit | Référence |
|---|---|---|
| `eng` | ~13 p/min | Tilak, 237 p. en 13 min ; 544 p. en 29 min |
| `fra` | ~24 p/min | Osman Yahia, 696 p. en 29 min |
| `ara` | ~10 p/min | Futūḥāt, 779 p. en 1 h 20 |

L'arabe coûte environ 25 % de plus que l'anglais. Une conversion d'ouvrage se
lance en tâche de fond, elle ne se surveille pas en synchrone.

Le marqueur `<!-- page N -->` est **la pièce maîtresse** : c'est lui qui permet
de remonter du Markdown au scan, et c'est sur lui que repose tout le contrôle
d'intégrité de l'étape 2. Il ne doit jamais être retiré d'un fichier converti.

## 3. Étape 2 — `decouper-ouvrage-chapitres.py`

```
python3 atelier/rd/outillage/decouper-ouvrage-chapitres.py \
        <converti.md> <dossier-sortie> <prefixe> [page-de-debut] [--langue=en|fr]
```

Découpe en un fichier par chapitre, chacun avec son frontmatter
(`source`, `section`, `pages_pdf`) et ses marqueurs de page conservés.

`--langue=en` (défaut) : `CHAPTER <romain>`, `PREFACE`, `APPENDIX`, `INDEX`,
`CONTENTS`. `--langue=fr` : `CHAPITRE <romain|PREMIER>`, `<n>e PARTIE`,
`INTRODUCTION`, `CONCLUSION`, `RÉPERTOIRE GÉNÉRAL`, `ADDENDA «X»`, et les
tables récapitulatives nommées une à une.

Trois mécanismes, chacun né d'un échec constaté :

1. **Tolérance OCR sur les chiffres romains.** L'OCR lit `CHAPTER VIIL` pour
   VIII, `XIUL` pour XIII, `U1` pour II, `VY` pour V. Le script énumère les
   lectures plausibles de chaque romain (table `AMBIG`) au lieu de normaliser
   par substitution — une substitution simple ne peut pas rendre `U` → `III`
   et `U` → `V` selon le contexte.
2. **Contrainte de séquence.** Seul le chapitre *suivant* est accepté. Sans
   elle, la table des matières — qui liste « CHAPTER I, II, III… » à raison
   d'un par ligne — ouvre une fausse section à chaque ligne. C'est ce qui s'est
   produit au premier essai : 20 sections détectées pour 13 chapitres réels.
3. **Paramètre `page-de-debut`.** Complément du précédent : on ignore
   explicitement le liminaire. Pour `9566.pdf`, le corps commence p. 32.

**Fenêtre de détection** : les 14 premières lignes d'une page. Le premier
réglage (6 lignes) manquait le chapitre I, précédé sur sa page du titre de
l'ouvrage.

**Fusion des sections à titre courant.** `GENERAL INDEX` se répète en tête de
chaque page d'index : sans fusion, l'index produit 39 fichiers d'une page. Les
sections consécutives de même nature non numérotée sont recollées.

## 4. Le contrôle d'intégrité

En fin d'exécution, le script confronte les pages réparties dans les fichiers
produits aux pages lues dans la source : **aucune manquante, aucune dupliquée**.
Sortie en code 1 si l'invariant est rompu, avec la liste des pages perdues.

**Éprouvé par son échec** (§VII, épreuve des contrôles, 2026-09-02) : sur une
copie en bac à sable dont la fusion des index a été volontairement rendue
fautive, le contrôle a rapporté `540 pages reparties / 544 lues`, nommé les
quatre pages perdues (508, 510, 514, 526) et sorti en code 1. L'état sain
rend `544 / 544`, code 0. Le contrôle n'a pas été seulement vu vert.

## 5. Contrôle externe — la table des matières

Le contrôle d'intégrité prouve qu'aucune page n'est perdue ; il ne prouve pas
que le **découpage tombe aux bons endroits**. Cette seconde question se tranche
contre une source indépendante du scan.

Pour `9566.pdf`, le dépôt possédait déjà la table des matières de la traduction
française : `doctrinal/sources/transcription-index-tilak-origine-polaire.md`.
Les 13 chapitres détectés y correspondent un à un — et c'est cette
correspondance, non la sortie du script, qui autorise à nommer les fichiers par
leurs titres réels. **Règle de méthode** : quand une table des matières
indépendante existe, elle est le juge du découpage ; à défaut, les titres restent
numériques et le doute est signalé.

## 6. Pièges rencontrés, à ne pas re-découvrir

- **Une couche texte présente n'est pas une couche texte utilisable.**
  `orionortheantiqu021979mbp.pdf` portait un OCR LuraDocument de 2006 rendant
  « Prajapatit=Yaj Da », « Bevayana », « Yishuv&n ». Un OCR neuf est nettement
  plus fidèle. **Toujours comparer un échantillon** `pdftotext` contre
  `tesseract` sur la même page avant de choisir — le coût est de trois minutes.
- **Une page vide en sortie n'est pas un échec d'OCR.** Les 17 pages quasi vides
  des deux conversions ont été vérifiées visuellement : ce sont de vraies pages
  blanches. Contrôler avant de conclure à une perte.
- **`chmod +x` refusé passe inaperçu.** Un premier lancement en tâche de fond a
  échoué en `Permission denied` parce que la commande de `chmod` avait été
  rejetée en amont. Une tâche de fond dont on ne relit pas le code de sortie est
  une tâche dont on ne sait rien — même leçon que `infra_verif`.
- **Ne pas installer `marker-pdf`** (~5 Gio, PyTorch) : le disque n'a que 8 Gio
  libres et `tesseract` suffit pour de l'anglais imprimé.
- **`markitdown` (Microsoft) ne remplace pas cette chaîne.** Éprouvé le
  2026-09-02 sur nos deux PDF : sur un scan pur (Futūḥāt) il rend **0 octet**
  — il s'appuie sur `pdfminer`/`pdfplumber`, qui ne lisent que du texte déjà
  encodé, et n'embarque aucun OCR local ; sur Osman Yahia il lit la couche
  ClearScan, donc *reproduit* les défauts qu'on avait écartés, et invente en
  prime de faux tableaux Markdown à partir des colonnes de chiffres du
  répertoire. Son plugin OCR passe par une API LLM Vision (clé OpenAI) ou
  Azure Document Intelligence : réseau + tiers, contraire au §VIII. **En
  revanche il est le bon outil pour les formats nativement structurés**
  (`.docx`, `.pptx`, `.xlsx`, `.epub`, `.html`), où il préserve titres, listes
  et vraies tables — usage à retenir le jour où de tels fichiers arrivent.
- **La langue de l'étiquette n'est pas la langue de la commande.** Le
  frontmatter portait `(eng)` en dur : patcher la commande `tesseract` à la
  main sans toucher l'étiquette produisait un fichier qui **mentait sur sa
  propre fabrication**. Corrigé par le paramètre ; retenir le principe — un
  libellé codé en dur à côté d'un comportement paramétrable finit toujours
  par diverger.

## 7. Limites connues

- **Langues installées : `eng`, `fra`, `ara`.** Toute autre demande son paquet
  `tesseract-ocr-<code>` ; à défaut le script sort en code 2 (§2).
- **Découpage : jeux `en` et `fr` seulement.** Un ouvrage à chapitres numérotés
  en chiffres arabes n'est pas découpé — le script rend alors un unique
  `front-matter`, comportement correct et visible, non une erreur silencieuse.
- **Pas de découpage pour l'arabe manuscrit ou calligraphié** — voir §8.
- Aucune extraction d'images ni de tableaux.

## 8. Le cas des *Futūḥāt* : pourquoi le découpage a été refusé

Constat du 2026-09-02, à ne pas re-tenter sans élément neuf. Les 560 bâbs des
*Futūḥāt* sont annoncés par des en-têtes **calligraphiés et ornementés** que
l'OCR rend en bouillie : `عوالبابالخامس والعشيرون ث*#` pour « le vingt-cinquième
bâb ». Trois obstacles, chacun mesuré :

1. **Les ordinaux sont écrits en toutes lettres**, non en chiffres : il faut un
   analyseur d'ordinaux arabes, pas une regex. Écrit et éprouvé
   (`atelier/rd/outillage/essais-non-retenus/ordinaux-arabes.py`, hors service) :
   97 % des lignes de l'index reconnues.
2. **L'appariement glouton ne suffit pas.** Quand l'OCR perd la dizaine,
   « الثامن والعشرون » donne `{18, 28}` et le glouton prend toujours 18. Il faut
   un appariement **global** (programmation dynamique sur la plus longue suite
   croissante). Piège rencontré : avec des back-pointers vers une table mutable,
   la chaîne reconstruite réutilise une même ligne pour deux rangs — il faut
   chaîner des nœuds immuables.
3. **Le corps reste trop bruité.** Sur l'index, 253 rangs cohérents sont
   retrouvés ; sur le corps, ~50 bâbs seulement, avec des fautes vérifiables
   (bâbs 75 et 81 assignés à la même page 617 ; « الحادى والسبعون » lu 81 au lieu
   de 71).

**Décision : pas de découpage.** Un découpage à ce taux d'erreur produirait de
*fausses références*, ce qui est pire qu'un fichier entier. Le Markdown reste
d'un tenant, exploitable par recherche plein-texte, avec ses 779 marqueurs de
page intacts pour remonter au scan. Règle générale qui s'en dégage : **quand le
contrôle externe ne peut pas trancher, on ne découpe pas** — le §5 vaut aussi
par son refus.
