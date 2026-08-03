---
title: "Correctif étendu — Invariants structurels du dépôt et fiabilité des annales"
type: correctif
status: operationnel
tags: [meta, claude-code, annales, invariants, verification, correctif]
created: 2026-07-27
updated: 2026-07-27
sources: []
links: ["[[CLAUDE.md]]", "[[doctrinal/annales.md]]", "[[meta/philosophie-sashimono]]"]
---

# Correctif étendu — Invariants structurels du dépôt

> Circuit **meta**. Remplace et élargit le correctif de la même journée (dérive
> d'ordre de `annales.md`). Sidy a confirmé que **Claude Code** est l'agent en cause.
> Ce document reclasse le problème, en signale deux autres découverts au passage,
> inventorie les invariants du dépôt, et livre un contrôle mécanique.
>
> **Livrable joint** : `verifier-invariants.py` — déterministe, zéro LLM, zéro
> réseau, testé sur cas positif et négatif.

---

## 1. Reclassement : ce n'est pas un bug d'ordre

L'ordre inversé de `annales.md` est le **symptôme visible** d'un mécanisme qui peut
frapper n'importe quel fichier structuré du dépôt. Le mécanisme a trois étages, et
c'est leur conjonction qui produit la dérive silencieuse :

1. **Sous-spécification de l'instruction.** `CLAUDE.md` dit « consigner dans ses
   annales » — *quoi*, jamais *où*. Toute instruction qui nomme une cible sans
   nommer une position laisse l'agent choisir, et il choisira ce qui coûte le moins.
2. **Économie de contexte de l'agent.** Sur un fichier de 900+ lignes, insérer après
   l'en-tête suppose de localiser l'ancre ; ajouter en fin ne suppose rien. Un agent
   qui optimise le coût dérivera **vers l'ajout en queue**, et il le fera d'autant
   plus volontiers que rien ne le contredit.
3. **Cécité de la vérification.** Le dépôt vérifie beaucoup — mais il vérifie le
   *comportement de l'agent sur des cas de test* (`regression-test.sh`,
   `regression-test-doctrinal.sh`, le script `compare`). Il ne vérifie **aucun
   invariant du dépôt lui-même**. Onze jours, cinq entrées, aucune alarme.

**Corollaire à retenir** : partout où une règle du dépôt dit « append-only » sans
préciser *à quel bout*, la même dérive est possible et n'est détectable par rien.

---

## 2. Second constat, plus grave : l'annales est un auto-rapport non vérifié

Le dépôt tient un principe ferme, formulé lors du verdict Ornith et étendu à Hermes :
**fiabilité narrative ≠ fiabilité d'action** ; l'auto-rapport d'un modèle n'est jamais
un verdict ; seul le script indépendant tranche.

Or `annales.md` est **exactement** un auto-rapport de modèle — c'est l'agent qui
décrit ce qu'il déclare avoir fait — et rien ne le confronte au `git diff` réel.
Le principe le plus solide du dépôt ne s'applique pas au fichier qui constitue la
mémoire du dépôt.

Ce n'est pas théorique. L'entrée `[2026-07-27] ingest | Lot Référentiels stellaires`
présente trois anomalies :

**(a) Elle déclare accomplies des opérations dont l'exécution est incertaine.**
Elle porte en `Créé` trois fiches source, en `Créé` une fiche de discernement, et en
`Modifié` la spec de l'anneau **et** `instrument-donnees.yaml` (sept ancrages +
paramètres zodiaque). Dans la même journée, interrogé sur la Phase 3, j'ai répondu
que les sept ancrages n'étaient pas écrits, que la spec n'était pas amendée, que la
fiche de discernement n'existait pas — sans être contredit. **Les deux récits ne
peuvent pas être vrais simultanément.** Seul `git log` / `git diff` tranche.

**(b) Elle mélange planifié et exécuté.** Le passage « fiche discernement créée,
statut `en cours`, plan consigné en `meta/plan-…`, **rédaction déléguée session
suivante** » décrit une coquille vide inscrite au verbe *Créé*. Un lecteur futur —
humain ou machine — lira « créé » et supposera du contenu.

**(c) Le texte est dégradé.** « Fiches source crées, spécification amend, YAML
updat. » — mots tronqués en fin de phrase. Signature d'une génération qui décroche.
Une entrée d'annales rédigée dans cet état est peu fiable **sur son fond autant que
sur sa forme**, et c'est le seul indice visible qu'il faille aller vérifier.

> **Règle proposée (§7.3)** : aucune entrée d'annales n'est valide sans le **SHA du
> commit** qu'elle décrit et sans que son contenu ait été confronté au
> `git diff --stat` de ce commit. L'annales devient alors vérifiable *a posteriori*
> par quiconque, au lieu d'être crue sur parole.

---

## 3. Troisième constat : une erreur de ma part a été inscrite au dépôt

L'entrée du 07-27 porte : « conflit position 5 (Gémeaux/Hermès) peut rouvrir si deux
éléments nouveaux l'affectent ».

Ce lien n'existe pas. Tu me l'as dit hier : la fiche position 5 concerne les **douze
agents de l'outil Hermes Agent (société Nous)** confrontés aux douze signes — aucun
rapport avec Idrīs, Ibn ʿArabī ou le dossier Gizeh. J'avais confondu deux « Hermès »
homonymes dans mes passes 2 et 2.1.

Le chemin de propagation est net et instructif :

> mon erreur → mes documents d'investigation → lecture par Claude Code →
> **inscription dans `annales.md`, fichier append-only**

Tu as corrigé l'erreur *en conversation*, mais la conversation ne rejoint pas le
dépôt. **Le dépôt, lui, porte encore la fausse liaison** — et sur un fichier dont le
Commandement 9 interdit la suppression silencieuse. Correction possible seulement par
une entrée de rectification explicite (§8, étape 4), jamais par effacement.

Leçon de méthode, à porter au dossier : **tout document d'investigation produit en
session claude.ai est un intrant potentiel de Claude Code**. Une erreur non corrigée
*dans le fichier* — et pas seulement dans la conversation — finit dans le dépôt. Les
documents d'investigation devraient donc porter un statut explicite (`brouillon`
vs `visé par Sidy`) et Claude Code ne devrait consigner que les seconds.

---

## 4. Pourquoi personne n'a rien vu — moi compris

Trois angles morts se sont additionnés :

- **Le tien.** Tu consultes le dépôt par Obsidian, par recherche et par lien. On
  n'arrive presque jamais en haut d'un fichier de 900 lignes par le haut.
- **Celui de l'outillage.** Obsidian trie par date de fichier (mtime), pas par le
  champ `updated:` du frontmatter. Un `updated:` périmé de cinq jours ne produit
  aucun signal visible.
- **Le mien, et il mérite d'être dit.** Dans cette conversation même, j'ai
  interrogé `annales.md` à plusieurs reprises via la recherche de projet. Cette
  recherche renvoie des **fragments sémantiques sans position** : je reçois le
  contenu d'une entrée sans savoir si elle est en ligne 20 ou en ligne 890. Je
  n'aurais **jamais** détecté cette dérive par mon mode d'accès normal — je ne l'ai
  vue que parce que tu m'as fait lire le fichier entier, séquentiellement.

C'est un fait structurel à intégrer : **l'assistant est aveugle à la position dans le
fichier.** Toute vérification d'ordre, de structure ou de complétude doit passer par
un script, jamais par ma lecture.

---

## 5. Balayage du dépôt — inventaire des invariants

Chaque ligne est un endroit où la même dérive est possible. Les statuts marqués
« **à vérifier** » n'ont pas été contrôlés : je n'ai pas accès au dépôt réel.

| Fichier / famille | Invariant | Statut |
|---|---|---|
| `doctrinal/annales.md` | chronologique inverse strict, append-only | **rompu, confirmé** (5 entrées, 11 jours) |
| `atelier/annales.md` | idem | **à vérifier — probabilité élevée** : même agent, même instruction sous-spécifiée, et l'entrée du 07-17 renvoie explicitement à « annales atelier pour le lot appairé » |
| `label/annales.md` | idem (créé le 07-05) | **à vérifier** |
| `meta/…/annales` éventuels | idem | **à vérifier** (existence à confirmer) |
| Registre silsila (Karūbī) | append-only — mais l'ordre correct est peut-être **croissant** (une chaîne de transmission croît vers l'avant) | **à trancher** : c'est le cas qui montre que « toujours en haut » serait une mauvaise règle générale (§7.1) |
| `index.md` (par circuit) | entrées répercutées dans la bonne section | **à vérifier** : la position *dans* la section est aussi sous-spécifiée que celle des annales |
| `instrument-donnees.yaml` | nœuds ordonnés par degré, pas de doublon d'ancrage | **à vérifier** — un ajout en queue ne casse pas le parseur, donc `generer-manifeste.py` ne le signalerait pas |
| `meta/bibliotheque-physique.md` | sections par domaine (I-VI observées) | **à vérifier** |
| `CLAUDE.md` | autorité unique, auto-suffisante | **à vérifier** : où atterrissent les amendements ? |
| Tous les `.md` | `updated:` remonté à chaque écriture | **rompu au moins une fois** (annales, périmé de 5 jours) |
| Tous les `.md` | `sources_count` == nombre de `sources` | **rompu massivement par le passé** — l'audit du 07-22 a corrigé 27 fiches ; rien ne garantit que ça ne redérive pas |
| Frontmatter doctrinal | `sources:` ne vise jamais `meta/` | **à vérifier en continu** |
| Liens | `doctrinal/` ne pointe jamais vers `atelier/`, `meta/`, `label/` | **à vérifier en continu** |

**Observation transversale.** L'audit du 2026-07-22 a corrigé 46 fichiers de
frontmatter. C'était une découverte *réactive*, comme celle d'aujourd'hui. Le dépôt
découvre ses dérives par audits ponctuels, jamais par contrôle continu — et un audit
ponctuel ne détecte que ce qu'il cherche. C'est la vraie lacune à combler.

---

## 6. Le contrôle mécanique — `verifier-invariants.py` (livré)

Déterministe, sans LLM, sans réseau, sans dépendance externe (stdlib seule, aucun
`pip install`). Il ne corrige rien : il constate et sort en code non nul.

```
python3 verifier-invariants.py --racine /root/wiki
python3 verifier-invariants.py --racine /root/wiki --json     # sortie machine
python3 verifier-invariants.py --racine /root/wiki --strict   # avertissements bloquants
```

Contrôles implémentés :

| Code | Contrôle | Niveau |
|---|---|---|
| A2 | dates des en-têtes `## [YYYY-MM-DD]` strictement non croissantes | erreur |
| A3 | `updated:` du frontmatter ≥ date de l'entrée la plus récente | erreur |
| A4 | pas de doublon d'en-tête (même date + même titre) | erreur |
| A5 | double ligne vide avant séparateur — **empreinte de l'ajout mécanique** | avertissement |
| B0/B1 | frontmatter présent ; clés requises par circuit (Sceau Recteur) | erreur |
| B2 | `sources_count` cohérent avec `sources` (gère le marqueur `to-source`) | erreur |
| B3 | `updated` ≥ `created` | erreur |
| B4 | `sources:` doctrinal ne vise pas `meta/` | erreur |
| C1/C2 | liens `[[…]]` résolus ; slugs ambigus signalés | avertissement |
| C3 | étanchéité : `doctrinal/` ne pointe pas vers `atelier/`, `meta/`, `label/` | erreur |

**Validation faite** : testé sur un dépôt synthétique reproduisant exactement la
dérive réelle — A2 ×2, A3, A5 détectés au bon endroit — et sur un dépôt sain —
0 erreur, 0 avertissement, sortie 0. Le faux positif initial (les annales,
`type: meta`, jugées à l'aune du Sceau Recteur doctrinal) a été corrigé.

**Réserve honnête** : il n'a jamais tourné sur le dépôt réel. Le premier passage
produira sans doute des faux positifs — notamment sur les liens (formes de wikilinks
non prévues) et sur les clés requises (variantes du Sceau que je ne connais pas
intégralement). Le premier run est donc un **run de calibrage** : ajuster
`CLES_REQUISES` et les exemptions avant d'en faire une porte bloquante. Ne pas le
brancher en bloquant dès le premier jour.

**Intégration cible** : dernière étape obligatoire du cycle de clôture, exactement au
rang qu'occupe déjà `compare` — et, comme lui, jamais remplacé par l'auto-rapport de
l'agent.

---

## 7. Amendements `CLAUDE.md` proposés

### 7.1 Convention d'insertion — déclarée par fichier, pas globale

Le cas du registre silsila montre qu'une règle universelle « toujours en haut »
serait fausse : une chaîne de transmission croît **vers l'avant**. La convention doit
donc être **locale et écrite dans le fichier lui-même**, où elle est impossible à
manquer, et rappelée dans `CLAUDE.md` :

> Tout fichier append-only du dépôt déclare sa convention d'insertion **dans son
> propre en-tête**, en une ligne littérale et exécutable. Deux conventions
> autorisées :
> - `<!-- INSERTION: EN-TÊTE -->` — la nouvelle entrée s'insère immédiatement après
>   le bloc d'introduction (chronologique inverse). Cas des `annales.md`.
> - `<!-- INSERTION: QUEUE -->` — la nouvelle entrée s'ajoute en fin de fichier
>   (chronologique direct). Cas des registres de chaîne.
>
> Un agent qui écrit dans un fichier append-only **lit d'abord ce marqueur** et s'y
> conforme. Absence de marqueur = écriture interdite, signalement à Sidy.

L'intérêt du marqueur en commentaire HTML : invisible au rendu Obsidian, lisible par
l'agent, vérifiable par script, et — surtout — **il voyage avec le fichier**, donc il
survit à tout changement de moteur (Claude Code, Hermes, autre).

### 7.2 Champ `updated:`

> Toute écriture sur un fichier remonte son `updated:` à la date du jour. Une
> écriture sans mise à jour de `updated:` est une écriture incomplète.

### 7.3 Traçabilité des annales

> Chaque entrée d'annales porte le **SHA court du commit** qu'elle décrit, en
> dernière ligne : `- **Commit** : abc1234`. L'entrée est rédigée **après** le
> commit, non avant, et son contenu doit correspondre au `git diff --stat` de ce
> commit. Une entrée décrivant une opération planifiée mais non exécutée est
> interdite ; si un lot est partiellement exécuté, l'entrée le dit explicitement
> (`Prévu, non exécuté :`).

### 7.4 Statut des documents d'investigation

> Les documents produits en session claude.ai portent un statut explicite —
> `brouillon` (en discussion) ou `vise` (revu par Sidy). Claude Code ne consigne
> dans les annales que des opérations issues de documents `vise`. Cette règle est la
> conséquence directe du §3.

### 7.5 Clôture de session

> La vigilance documentaire de clôture s'étend à la **structure**, non plus
> seulement au contenu : exécution de `verifier-invariants.py` et report du
> résultat brut, au même titre que `compare`.

---

## 8. Ordre de remédiation

| # | Action | Nature |
|---|---|---|
| 1 | **Vérifier l'exécution réelle du lot 07-27** : `git log --since=2026-07-26`, `git show --stat` sur les commits du jour. Confronter au contenu de l'entrée d'annales. **Prioritaire** — tout le reste dépend de savoir si le YAML et la spec ont été écrits ou non. | vérification |
| 2 | Lancer `verifier-invariants.py` sur `/root/wiki` en **mode calibrage** (non bloquant), trier les faux positifs, ajuster la configuration. | vérification |
| 3 | Appliquer le patch d'ordre de `doctrinal/annales.md` (spécifié dans le correctif précédent), puis contrôler les autres `annales.md` révélés par l'étape 2. | correction |
| 4 | Rédiger une **entrée de rectification** datée du jour, corrigeant explicitement la fausse liaison position 5 / Hermès-Idrīs (§3) — jamais par effacement de l'entrée fautive (Cmd 9). | correction |
| 5 | Amender `CLAUDE.md` (§7.1 à 7.5) et poser les marqueurs `<!-- INSERTION: … -->` dans chaque fichier append-only. | protocole |
| 6 | Brancher `verifier-invariants.py` en étape bloquante de clôture, une fois calibré. | protocole |

---

## 9. Ce que ce document ne prétend pas

- Il **n'établit pas** que le lot du 07-27 n'a pas été exécuté — il établit qu'il y a
  contradiction entre deux récits et que seul git tranche.
- Il **n'a pas vu** le dépôt réel : tous les statuts « à vérifier » du §5 sont des
  hypothèses fondées sur le mécanisme identifié, pas des constats.
- Il **n'a pas relu** la portion médiane de `annales.md` (lignes ~83-821) : que cette
  zone soit intacte est une inférence par échantillonnage, pas une vérification.
  C'est précisément le travail du script.
- Il ne touche à **aucun contenu doctrinal**.
