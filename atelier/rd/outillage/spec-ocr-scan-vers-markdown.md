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

## 1. Ce que la chaîne fait — et ce qu'elle ne fait pas

Elle produit un **texte de repérage**, jamais un texte critique. La sortie est
brute de machine : les translittérations diacritées et le devanāgarī sont mal
rendus. Elle sert à *savoir où chercher*, exactement comme l'instrument de
repérage de `rd/bibliotheque/` — la lecture du texte primaire reste humaine
(§VII). Toute sortie va au sas `_inbox/`, jamais directement dans un circuit.

## 2. Étape 1 — `ocr-scan-vers-markdown.sh`

```
bash atelier/rd/outillage/ocr-scan-vers-markdown.sh <source.pdf> <sortie.md> "<titre>"
```

Rend chaque page en image (`pdftoppm -r 300 -gray`), l'OCRise
(`tesseract 5`, `-l eng`, `--psm 1`), et concatène le tout avec un marqueur
`<!-- page N -->` par page. Deux pages en parallèle (`xargs -P 2`) : c'est le
nombre de cœurs de la machine, monter plus haut ne gagne rien et sature les
3,7 Gio de RAM. Les images intermédiaires sont détruites au fil de l'eau —
sinon 781 pages à 300 dpi remplissent le disque.

**Débit mesuré** : ~13 pages/minute sur le serveur (2 cœurs). 237 pages en
13 min, 544 pages en 29 min. Une conversion d'ouvrage se lance en tâche de fond,
elle ne se surveille pas en synchrone.

Le marqueur `<!-- page N -->` est **la pièce maîtresse** : c'est lui qui permet
de remonter du Markdown au scan, et c'est sur lui que repose tout le contrôle
d'intégrité de l'étape 2. Il ne doit jamais être retiré d'un fichier converti.

## 3. Étape 2 — `decouper-ouvrage-chapitres.py`

```
python3 atelier/rd/outillage/decouper-ouvrage-chapitres.py \
        <converti.md> <dossier-sortie> <prefixe> [page-de-debut]
```

Découpe en un fichier par chapitre, chacun avec son frontmatter
(`source`, `section`, `pages_pdf`) et ses marqueurs de page conservés.

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

## 7. Limites connues

- **Anglais imprimé uniquement** (`-l eng`). Pour le français, `-l fra` est
  installé ; l'arabe ne l'est pas et demanderait `tesseract-ocr-ara`.
- **Détection des chapitres calée sur `CHAPTER <romain>`.** Un ouvrage à
  chapitres numérotés en chiffres arabes, ou en français (`CHAPITRE PREMIER`),
  n'est pas découpé — le script rend alors un unique `front-matter`, ce qui est
  un comportement correct et visible, non une erreur silencieuse.
- Aucune extraction d'images ni de tableaux.
