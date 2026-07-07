---
title: "Directive Sashimono — philosophie d'assemblage du dépôt"
type: meta
tags: [outillage, methode, protocole, sashimono, assemblage]
created: 2026-07-07
updated: 2026-07-07
---

# Directive Sashimono — philosophie d'assemblage du dépôt

## 1. Objet et statut de ce document

Ce document formalise l'usage du **sashimono** (指物) — l'art japonais de la menuiserie
fine assemblée sans clou ni vis, où les pièces tiennent par la seule justesse de leurs
joints — comme **interface conceptuelle et philosophie opératoire** de la démarche
globale (wiki doctrinal, Instrument, label, agents).

**Statut** : analogie d'outillage, au même titre que le vocabulaire du greffe ou du
sas. Elle sert la clarté formelle et la discipline de méthode ; elle **n'établit
aucune correspondance doctrinale**. La question distincte du sashimono comme métier
traditionnel au sens guénonien (support possible d'une initiation de métier, art
sacré au sens de Coomaraswamy) est renvoyée à la fiche
`doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md` — 🔍, verdict
réservé à l'utilisateur (Cmd 3, Cmd 12).

## 2. Le sashimono en bref

Menuiserie d'assemblage japonaise (mobilier fin, notamment traditions d'Edo et de
Kyōto `to-source`) : les pièces de bois sont jointes par tenons, mortaises et
assemblages taillés, **sans fixation métallique** ; la solidité vient de la précision
de la coupe et du respect du fil du bois ; les joints sont le plus souvent
invisibles de l'extérieur ; l'assemblage se monte d'abord **à blanc** (sans colle)
pour vérification avant tout collage définitif `to-source`. L'artisan ne force
jamais un joint : un assemblage forcé fend la pièce.

## 3. Revue : ce que le dépôt pratique déjà en sashimono

Constat de la présente formalisation : les mécanismes existants du dépôt incarnent
déjà ces principes. La correspondance est descriptive, pièce par pièce :

| Principe sashimono | Incarnation existante |
|---|---|
| **Aucun clou** : rien ne tient par fixateur étranger | Règle commune des manifestes : script déterministe à validations bloquantes, jamais écrit à la main, jamais par LLM. Le LLM est le clou — il traverse, force et fend. |
| **Justesse de coupe** : la pièce est taillée pour son joint | Sceau Recteur normalisé, schéma de nœud v0.2.1 figé, générateur à validations bloquantes (0 erreur exigé). |
| **Jamais de joint forcé** | Cmd 3 (non-syncrétisme) : toute superposition structurelle forcée est rejetée (cas *waswâs*/Qliphoth). Tension documentée plutôt que résolue de force (fiche `tension-hadarat-burckhardt-jurjani`). |
| **Respect du fil du bois** : chaque essence selon sa nature | Chaque tradition dans sa géométrie native, visible en transparence, jamais poncée vers l'uniformité (invariant de l'Arbre unique). |
| **Assemblage à blanc** avant collage | Liens suggérés pointillé + 🔍 ; bac à sable + script `compare` ; déploiement PRÉVERSION avant PRODUCTION. Rien n'est collé avant le regard du maître. |
| **Démontabilité** : l'assemblage s'inspecte et se défait sans casse | Bascule réversible des moteurs (§VIII.10), `deprecated` plutôt que suppression (Cmd 10), flux à sens unique, annales append-only. |
| **Le joint invisible, jamais secret** | L'Instrument cache le manifeste à l'usage ; git et annales documentent intégralement chaque jointure. |
| **L'apprenti taille au gabarit, ne conçoit pas le joint** | Agents Hermes : autorité de signalement, jamais de décision ; lots traités fiche par fiche selon `MASTER-UPDATE.md`. |
| **Le maître seul valide l'assemblage** | Porte humaine (Cmd 13) : verdicts, contrats, publications, discernements tranchés par l'humain. |
| **Le verdict est dans le jeu du joint, pas dans la parole de l'apprenti** | Fiabilité d'action ≠ fiabilité narrative (§VIII.2) : le script `compare` est le juge de paix, jamais l'auto-rapport du modèle. |

## 4. Articles normatifs

La formalisation proprement dite — six articles, applicables aux quatre circuits :

**Art. 1 — Aucune pièce ne tient par colle.** Toute correspondance, structure ou
affirmation dont la solidité repose sur une assertion de modèle (et non sur une
source primaire ou un script déterministe) est un joint collé : à démonter, ou à
marquer 🔍 / `to-source` jusqu'à vérification humaine.

**Art. 2 — La coupe avant l'assemblage.** On normalise (frontmatter, schéma, gabarit)
avant d'intégrer. Un lot mal taillé ne s'ajuste pas au marteau côté intégration : il
retourne au sas `_inbox/` pour être retaillé côté production.

**Art. 3 — Jamais de joint forcé.** Toute résistance formelle (tension doctrinale,
échec au `compare`, divergence de structure) suspend l'assemblage : on documente
(fiche `discernement`, rapport brut) et l'on pose les pièces **côte à côte**. Deux
pièces séparées valent toujours mieux que deux pièces mal jointes.

**Art. 4 — Tout assemblage se présente à blanc.** Aucune écriture, publication ou
correspondance ne devient définitive sans passage par un état démontable et
inspectable (🔍, bac à sable, préversion) soumis à la validation humaine.

**Art. 5 — L'assemblage reste démontable.** Toute phase d'infrastructure, toute
intégration, toute bascule de moteur doit être indépendamment réversible ; on
déprécie, on ne supprime pas ; la traçabilité (annales, git) est la condition de la
démontabilité.

**Art. 6 — Le joint parfait est invisible, jamais secret.** Les interfaces de
présentation (Instrument, site) masquent la jointure à l'usage ; le dépôt la
documente intégralement. Aucune élégance de surface ne dispense de la traçabilité.

## 5. Application par circuit

- **doctrinal/** : Art. 1 et 3 priment — le Cmd 3 et la discipline des sources sont
  la taille du joint ; le 🔍 est l'assemblage à blanc du discernement.
- **Instrument** : Art. 2 et 6 — le manifeste est le joint invisible ; le générateur
  à validations bloquantes est le gabarit de coupe.
- **label/** : Art. 4 — préversion avant production ; les liens doctrine↔label
  restent 🔍 tant que non arbitrés.
- **Agents (Hermes)** : Art. 1, 4 et 5 — `clarify` non contournable, `compare` comme
  seul verdict, extension `raw/` conditionnelle (trois cycles à blanc sans anomalie
  avant collage).

## 6. Lexique conventionnel (validé par l'utilisateur, 2026-07-07)

Terminologie japonaise adoptée **par convention** là où elle trouve sa place dans
l'œuvre — usage opératoire, jamais doctrinal. Orthographes et usages techniques à
vérifier contre une source de référence sur la menuiserie japonaise (`to-source`
global sur ce lexique ; les termes restent valides comme convention interne même en
attendant cette vérification).

| Terme | Sens artisanal | Emploi dans l'œuvre |
|---|---|---|
| **Kigumi** (木組み) | L'assemblage bois sans fixateur | Nom générique de la présente philosophie ; « règle kigumi » = Art. 1 (aucune pièce ne tient par colle). |
| **Hozo** (ほぞ) | Tenon et mortaise — même forme en positif et en négatif | **Ancrage d'équivalence** : un même degré ontologique sous deux voiles — l'un est l'exact creux de l'autre. Trait plein rouge de l'Instrument. |
| **Kumiko** (組子) | Treillis fin assemblé en plan (claustras, *shōji*) | **Ancrage de complémentarité** : lien tressé horizontal, deux aspects articulés d'une même unité, sans fusion. Lien bleu de l'Instrument. |
| **Kari-kumi** (仮組み) | Montage à blanc, sans colle, pour vérification | Tout état **suggéré 🔍** : liens pointillés, bac à sable + `compare`, préversion. Rien n'est collé avant le regard du maître. |
| **Sumi-tsuke** (墨付け) | Traçage à l'encre avant toute coupe | La fiche **discernement** : le trait précède la coupe (Cmd 6). Aucune correspondance n'est taillée sans son trait ; le trait peut conclure qu'on ne coupe pas. |
| **Ki-dori** (木取り) | Choix de la pièce dans le bois brut, selon le fil | **VIGILANCE et travail sur `raw/`** : la recherche de la pièce manquante — sélectionner dans les sources brutes la pièce dont le fil convient au membre absent du chantier. |

**Vue kari-kumi** : l'onglet **Instrument de délimitation apophatique** est, dans ce
lexique, la *vue kari-kumi du chantier* — l'œuvre entière montée à blanc, où se
voient d'un coup d'œil les joints non taillés (discernements `en cours`), les pièces
manquantes (`to-source`), et les assemblages qui résistent (tensions 🌐).

**Exclusions** : les termes de l'esthétique japonaise porteurs d'une charge
doctrinale propre (*ma* 間, *wabi-sabi*, etc.) sont **exclus de la convention** tant
qu'aucune fiche `discernement` ne les a instruits — le risque serait précisément le
joint forcé que l'Art. 3 interdit (ex. : rapprocher *ma* du *barzakh* serait une
correspondance inter-traditionnelle relevant du Cmd 3, jamais d'une convention de
vocabulaire).

## 7. Limites et garde-fou

L'analogie est **opératoire, non doctrinale**. Elle ne fonde aucune équivalence
entre le sashimono et un concept du Tasawwuf, de la métaphysique guénonienne ou de
toute autre forme traditionnelle. Si un usage futur devait franchir ce seuil
(symbolisme de l'assemblage, initiation de métier, art sacré), il exigerait la
résolution préalable de la fiche discernement liée — verdict appartenant à
l'utilisateur, jamais à la machine (Cmd 12).
