---
title: "La traduction anglaise de l'Ihyâ' par Fazl-ul-Karim (Dacca, 1971) — méthode déclarée et mesure de l'abrègement"
type: source
status: academique
tradition_cadre: "islam"
tags: [ghazali, ihya, traduction, abregement, fazl-ul-karim, sources-primaires, a-trancher]
created: 2026-09-14
updated: 2026-09-14
sources: ["raw/Ihya Ulum Al Din Vol 4.pdf"]
sources_count: 1
cross_links:
  - "[[doctrinal/discernement/2026-08-09_wahhabisme-effondrement-califat-grande-subversion]]"
  - "[[doctrinal/sources/histoire-wahhabis-corancez-redissi]]"
  - "[[doctrinal/sources/guenon-crise-monde-moderne-ch5-individualisme]]"
---

# La traduction anglaise de l'Ihyâ' par Fazl-ul-Karim — méthode déclarée et mesure

## Objet

Cette fiche consigne **deux faits** touchant la traduction anglaise de l'`Ihyâ'
'ulûm al-dîn` déposée en `raw/` : la méthode que le traducteur déclare lui-même
en préface, et la mesure de l'écart entre cette traduction et l'original arabe.

Elle **ne rend pas de verdict** sur la qualification de la démarche. Cette
qualification appartient à Sidy ; la fiche lui en fournit la matière et l'énonce
comme pendante (`a-trancher`). Le silence sur le verdict est ici explicite, non
un amortissement : voir `atelier/rd/incidents/2026-09-14_amortissement-constat-doctrinal-traduction-ihya.md`.

## Description matérielle

Quatre volumes en `raw/`, producteur ABBYY FineReader 11 (océrisés).

| Fichier | Pages | Contenu |
|---|---|---|
| `Ihya Ulum Al Din Vol 1.pdf` | 262 | BOOK OF WORSHIP (`'ibâdât`), ch. I–X |
| `Ihya Ulum Al Din Vol 2.pdf` | 222 | BOOK OF WORLDLY USAGES (`'âdât`), ch. I–XI |
| `Ihya Ulum Al Din Vol 3.pdf` | 295 | BOOK OF DESTRUCTIVE EVILS (`muhlikât`), ch. I–X |
| `Ihya Ulum Al Din Vol 4.pdf` | 732 | **mal étiqueté** — page de titre : `VOL. Ill` |

**Avertissement de manipulation** : le fichier « Vol 4 » porte en page de titre
`VOL. Ill` et ses pages 1 à 298 **dupliquent le volume 3**. Le quatrième livre
(`munjiyât`) commence à la page PDF 299. Toute exploitation doit partir de la
page 299, sous peine de convertir deux fois le livre III et d'ignorer le livre
IV.

## Fait n° 1 — la méthode, déclarée par le traducteur

Préface, page PDF 301, signée « Dacca October, 1971 Fazlul Karim » :

> This work is an attempt to translate the fourth part of the Ihya **not too
> literally but in substance** from the original written in Arabic. [...] A
> litteral translation is avoided in order to **omit the unnecessary arguments
> of sects and sub-sects** then prevailing in the world and also to **omit the
> sayings of the sages of less importance**. But it should be noted that **no
> verse of the Holy Quran or the Hadis of the Holy Prophet has been ommitted**.

L'énoncé est primaire : le traducteur déclare ce qu'il retranche, ce qu'il
conserve, et à quel titre. Rien n'est inféré.

### La hiérarchie que cette déclaration dessine

| Conservé sans exception | Retranché |
|---|---|
| le verset coranique | les arguments des écoles (*sects and sub-sects*) |
| le hadîth | les paroles des sages « of less importance » |

Sont conservées intégralement les deux sources scripturaires. Sont retranchés le
tissu dialectique des écoles et la chaîne des maîtres que Ghazâlî cite — c'est-
à-dire, dans un ouvrage de la nature de l'Ihyâ', l'appareil de la
**transmission**, déclaré de moindre importance par le traducteur.

On note en outre que le retranchement est **offert comme gage de fidélité** :
« no verse [...] has been ommitted » occupe la place de la garantie d'intégrité
de l'ouvrage.

## Fait n° 2 — la mesure

Sondage déterministe, comptage de mots. Les deux côtés ne suivent pas la même
chaîne, et cela se dit :

- **Anglais** — `pdftotext` appliqué aux quatre PDF de `raw/`, le quatrième
  restreint aux pages 299-732 (les pages 1-298 redoublent le livre III, voir
  *Description matérielle*).
- **Arabe** — concaténation des 36 fichiers de
  `textes/ghazali-ihya-ulum-al-din-arabe/` (eux-mêmes issus de `pdftotext` sur
  `raw/9472.pdf`), marqueurs de pagination `<!-- pdf … -->` retirés.

L'échafaudage markdown restant (frontmatter, titres) a été mesuré, non supposé :
le retirer fait passer le compte arabe de 1 056 204 à 1 055 988, soit **216 mots,
0,02 %**. Le chiffre rapporté est le premier ; l'écart est sans effet sur le
rapport.

| | Arabe | Anglais |
|---|---|---|
| Unités de chapitre | 40 kitâb | **41 en-têtes `CHAPTER`** (10 / 11 / 10 / 10) |
| Mots | 1 056 204 | **544 347** |

**L'appareil des chapitres est complet ; le corps du texte est à 52 %.**

Le rapport de 52 % est un **plancher**, non une estimation : il compte un mot
arabe pour un mot anglais, ce qui sous-estime l'écart. L'arabe agglutine dans le
mot ce que l'anglais dissocie (prépositions, pronoms affixés, article) ; une
traduction complète vers l'anglais s'allonge en nombre de mots. L'écart réel est
donc supérieur à la moitié.

### Réserves sur la mesure (Cmd 12 — l'indice se rapporte avec ses limites)

- Le PDF arabe peut porter un appareil éditorial (index, notes) gonflant son
  compte ; l'OCR anglais peut en perdre. Aucun de ces deux effets ne rend compte
  d'un facteur 2.
- Le comptage de mots n'est pas un comptage de contenu : c'est un indice de
  volume, et il est rapporté comme tel.
- Le décompte des chapitres (41 contre 40) n'établit pas une correspondance
  chapitre à chapitre, seulement que l'appareil visible est du même ordre.

### Ce que la conjonction des deux mesures fait voir

Ce qui est complet est ce qui se vérifie d'un coup d'œil — la table des
matières. Ce qui manque est ce qui ne se vérifie que par collation. Un lecteur
qui contrôle la complétude d'une traduction par son sommaire — le contrôle le
plus naturel — ne voit rien.

## Conséquence versée au chantier

La traduction n'a **pas** été convertie en `textes/` : verdict de Sidy du
2026-09-14. Le texte arabe intégral est le texte de référence du chantier, et il
l'est seul. Voir `textes/ghazali-ihya-ulum-al-din-arabe/index-conversion.md`.

## Rattachements — inscrits au cartouche sur verdict de Sidy du 2026-09-14

La machine avait proposé ces trois liens sans les inscrire ; Sidy les a
validés le 2026-09-14, et ils sont portés au cartouche à cette date.

1. `doctrinal/discernement/2026-08-09_wahhabisme-effondrement-califat-grande-subversion`
   — rattachement pressenti par Sidy lors de l'ouverture du chantier. Fiche de
   statut `speculatif`. La réserve C5 formulée avant verdict ne tenait pas :
   C5 porte sur les pages `traditionnel`, et celle-ci est `academique` —
   l'inscription laisse le vérificateur à 71 avertissements, inchangé. Même
   configuration que `histoire-wahhabis-corancez-redissi`, qui porte ce même
   lien sous le même statut.
2. `doctrinal/sources/histoire-wahhabis-corancez-redissi` — précédent de fiche
   `source` sur un objet de même famille.
3. `doctrinal/sources/guenon-crise-monde-moderne-ch5-individualisme` — le
   rapprochement avec le protestantisme et le libre examen a été avancé par
   Sidy ; il est rapporté ici comme sa position, et n'est pas argumenté par
   cette fiche.

## Réserve de méthode

Le fait qu'une démarche se qualifie d'après ses énoncés et sa direction, et non
d'après l'intention de son agent, est une règle du dépôt et non une conclusion
de cette fiche. Qualifier une méthode éditoriale n'est pas attribuer une
appartenance à qui l'emploie. La fiche s'en tient à ce que le document déclare
et à ce que la mesure donne.
