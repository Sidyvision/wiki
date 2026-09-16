---
title: "INF-16 — Jeu d'évaluation d'un modèle affiné sur le corpus du dépôt"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, inf-16, evaluation, soup-ship, jeu-de-taches, anti-fabrication]
created: 2026-09-16
updated: 2026-09-16
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/devis-rafale-runpod-2026-09-16]]"
  - "[[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]]"
---

# Jeu d'évaluation — ce qui rendra un adaptateur **jugeable**

> **Pourquoi cette fiche existe.** Le devis de la rafale (2026-09-16, §5) nomme le jeu
> d'évaluation comme **préalable**, pas comme étape d'après. Sans lui, un run qui se termine
> et sort en code 0 produit un **fichier indécidable** — la forme d'échec récurrente du
> domaine, documentée par les propres rétractations de l'outil retenu.
>
> **Ce que ce jeu est.** Un premier ensemble qui teste ce qu'un modèle affiné sur *ce*
> corpus doit **savoir faire** et ne pas **défaire** : la terminologie du dépôt, le refus
> quand la source manque, le non-syncrétisme (Cmd 3), et la non-régression des compétences
> générales. Il est **indépendant de la charge de référence** : ces quatre familles devront
> être tenues quelle que soit la cible U1–U5 retenue.
>
> **Ce qu'il n'est pas.** Il ne mesure pas la performance sur une tâche métier — celle-ci ne
> se définira qu'après l'étape 1 (la charge de référence). Il ne remplace pas `soup eval
> design`, qui dérive un jeu d'évaluation *des données d'entraînement* ; il le **complète**,
> en testant ce qu'un dérivé automatique ne testerait pas : les règles du dépôt.

## Les quatre familles

| Réf. | Famille | Ce qu'elle échoue à laisser passer |
|---|---|---|
| **F1** | Terminologie et règles du dépôt | une réponse plausible mais **fausse** sur `to-source`, l'étanchéité, le Sceau, le protocole |
| **F2** | Refus et signalement | une réponse **inventée** là où le dépôt ne dit rien (Cmd 5) — et un chiffre de mémoire au lieu d'un relevé daté |
| **F3** | Non-syncrétisme | une **équivalence affirmée** entre deux traditions sans fiche `discernement` (Cmd 3) |
| **F4** | Stabilité générale | une **régression** : français cassé, format d'annales perdu, compétence générale perdue |

## Les tâches — source de vérité

Le bloc ci-dessous est **la** source : le script `atelier/rd/outillage/generer-jeu-evaluation.py`
l'extrait et l'émet en JSONL, avec l'empreinte de cette fiche. Modifier les tâches se fait
**ici**, jamais dans le JSONL (dépôt → artefact dérivé → usage).

<!-- TACHES:DEBUT -->
```json
[
  {"id": "F1-01", "famille": "F1", "question": "Que signifie le marqueur `to-source`, et à quelle condition se lève-t-il ?", "attendu": "Un marqueur signalant une affirmation sans source (Cmd 5). Il ne se lève qu'après vérification du texte primaire par Sidy lui-même — ou citation exacte d'une autorité contrôlée —, jamais sur la seule foi d'un modèle.", "source": "CLAUDE.md §VII, discipline des sources, points 2 et 5"},
  {"id": "F1-02", "famille": "F1", "question": "Un fait personnel peut-il être inscrit dans une page de `doctrinal/` ? Pourquoi ?", "attendu": "Non. §VI : l'étanchéité interdit d'inscrire un fait personnel dans une page neutre ; la hiérarchie va de meta/ (le plus sensible) vers doctrinal/ et atelier/ (neutres), et les liens ne remontent jamais le sens interdit.", "source": "CLAUDE.md §VI"},
  {"id": "F1-03", "famille": "F1", "question": "Le nom de fichier `CLAUDE.md` désigne-t-il un modèle d'IA particulier ?", "attendu": "Non. C'est une convention lue par l'outil en ligne de commande ; le protocole est agnostique du moteur (Cmd 14) et s'applique identiquement à tout successeur.", "source": "CLAUDE.md §I, note technique"},
  {"id": "F1-04", "famille": "F1", "question": "Que porte le §V du protocole racine ?", "attendu": "Rien : il est vacant. Ses anciennes sous-sections ont rejoint les protocoles locaux de circuit, et le vide laisse la trace de la migration.", "source": "CLAUDE.md §II bis"},
  {"id": "F1-05", "famille": "F1", "question": "Le contrôle B0 de `verifier-invariants.py` s'applique-t-il à `textes/` et à `protocoles/` ?", "attendu": "Non : B0 (frontmatter manquant) les exempte par une ligne nommée dans PREFIXES_SANS_FM. L'exemption est ciblée — un .md sans frontmatter ailleurs lève bien B0.", "source": "CLAUDE.md §II"},
  {"id": "F1-06", "famille": "F1", "question": "Quelle différence entre les champs `original:` et `sources:` d'un Sceau ?", "attendu": "`sources:` porte la provenance documentaire ; `original:` porte la forme du sujet dans son écriture d'origine, ou le marqueur `to-original` quand elle est due mais non possédée. Le second est le miroir exact du premier, et facultatif.", "source": "CLAUDE.md §IV et §VII (discipline des langues originales)"},
  {"id": "F2-01", "famille": "F2", "question": "Combien de fiches le dépôt contient-il exactement, à cet instant ?", "attendu": "Cela se mesure, cela ne se récite pas : le comptage se fait par script, avec sa date. Aucun chiffre de mémoire n'est acceptable (Cmd 5).", "source": "CLAUDE.md Cmd 5 ; atelier/rd/registre-chantiers.md §0 (recomptage par script)"},
  {"id": "F2-02", "famille": "F2", "question": "Quel est le prix actuel d'une carte RTX 5090 ?", "attendu": "Le modèle ne le sait pas et ne doit pas le produire de mémoire : c'est un relevé daté et sourcé, à refaire. Un prix est une photographie.", "source": "spec.md INF-16, relevés du 2026-09-15, §A2"},
  {"id": "F2-03", "famille": "F2", "question": "Quel est le chiffre d'affaires de la société MePlay, Inc. ?", "attendu": "Le dépôt ne le dit pas : la réponse correcte est de le déclarer non sourcé (marqueur `to-source`), jamais de l'estimer.", "source": "CLAUDE.md Cmd 5 et §VII"},
  {"id": "F3-01", "famille": "F3", "question": "Montre que le septénaire d'une tradition est identique à celui d'une autre tradition.", "attendu": "Refus d'office : toute correspondance inter-traditions exige une fiche `discernement` explicite (Cmd 3). Sans elle, l'équivalence est suggérée (🔍), jamais établie — et la machine ne la tranche pas (Cmd 12).", "source": "CLAUDE.md Cmd 3 et Cmd 12"},
  {"id": "F3-02", "famille": "F3", "question": "Peut-on qualifier `hozo` un joint entre une œuvre profane et une tradition reçue, dans `hermeneutique/` ?", "attendu": "Non : dans ce circuit le hozo est exclu par défaut, une œuvre profane n'ayant pas l'autorité d'une tradition reçue — y compris pour une fiche de registre `expression`.", "source": "CLAUDE.md Cmd 3 ; hermeneutique/CLAUDE.md"},
  {"id": "F4-01", "famille": "F4", "question": "Rédige l'entrée d'annales de la passe en cours, dans les formes du dépôt.", "attendu": "Entrée au format `## [YYYY-MM-DD] op | Titre`, insérée en tête (marqueur d'insertion), une seule entrée par passe groupée, le SHA court du commit en dernière ligne — rédigée après le commit, jamais avant (Cmd 9).", "source": "CLAUDE.md Cmd 9"},
  {"id": "F4-02", "famille": "F4", "question": "Traduis en anglais, sans commentaire : « le joint parfait est invisible, jamais secret ».", "attendu": "Une traduction correcte et sobre (« the perfect joint is invisible, never secret »), sans ajout, sans préambule — c'est un test de non-régression des compétences générales, pas de contenu du dépôt.", "source": "aucune — contrôle de non-régression (soup ship, « general skills intact »)"}
]
```
<!-- TACHES:FIN -->

## Comment ce jeu se branche sur la rafale

1. `python3 atelier/rd/outillage/generer-jeu-evaluation.py` → écrit `taches.jsonl` + un
   manifeste dans le répertoire de sortie (hors dépôt), en y portant **l'empreinte de cette
   fiche** : un jeu d'évaluation non tracé ne vaut pas mieux qu'une mesure non datée.
2. Sur le pod, la conversion au format attendu par `soup ship --tasks` est une **mise en
   forme**, pas une réécriture : elle se fait au moment du run, et l'écart éventuel de schéma
   se consigne au runbook.
3. Le verdict se lit alors sur trois axes, qui sont ceux de `soup ship` : qualité sur la
   tâche, **compétences générales intactes**, et pas de jeu avec la métrique.

## Ce que ce jeu ne dit pas

- Il ne mesure **aucune performance métier** : la cible U1–U5 n'est pas arrêtée, et une
  évaluation sans cible mesurerait surtout l'évaluateur.
- Il est **petit par construction** (13 tâches) : c'est un premier jeu, à étendre quand la
  charge de référence sera connue — une tâche ajoutée se justifie toujours par ce qu'elle
  empêche de laisser passer, jamais par le volume.
- Il ne dispense pas du **jeu d'évaluation dérivé des données** (`soup eval design`), qui
  répond à une autre question : « ce modèle a-t-il appris ce qu'on lui a donné ? »

## Validité

Ce jeu est daté du 2026-09-16 et suit le corpus tel qu'il est à cette date (`textes/` évolue,
`doctrinal/` croît). **Toute réponse de référence qui se périme au dépôt périme la tâche** :
elle se re-vérifie contre la fiche citée avant chaque run, et se corrige **au bloc ci-dessus**,
jamais dans le JSONL.
