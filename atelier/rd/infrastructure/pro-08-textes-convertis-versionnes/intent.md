---
title: "PRO-08 — un dossier versionné pour les textes convertis : intention"
type: infrastructure
chantier: PRO-08
tags: [atelier, rd, infrastructure, chantier, intent, raw, obsidian, synchronisation]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
---

# PRO-08 — un dossier versionné pour les textes convertis : intention

## Le besoin

**Constat de Sidy**, 2026-09-02 :

> « Aucun fichier Markdown n'a d'intérêt à rester en `raw/` sachant qu'en y étant
> ils restent masqués et je ne peux pas travailler avec ces ressources en dehors
> du terminal. »

Vérifié au disque, et non supposé :

| mesure | valeur |
|---|---|
| fichiers `.md` sous `raw/` | **708** |
| dont suivis par git | **0** — `/raw/*` est dans `.gitignore` |
| distincts par contenu | **561** (donc **147 doublons exacts**) |
| poids total des `.md` | **14 Mo** |
| poids total de `raw/` | **2,6 Go** |

Le corpus concerné n'est pas marginal : *Symboles de la Science sacrée* (92
fiches), *Le Théosophisme* (68), *Aperçus sur l'initiation* (52), *Le Règne de la
Quantité* (44), *Études sur l'Hindouisme* (39), *Formes traditionnelles et Cycles
cosmiques* (32), *Le Symbolisme de la Croix* (31), *La Grande Triade* (28),
*L'Homme et son devenir* (27), *Les états multiples* (20), *Le Roi du Monde*
(12) — plus Jurjani, Avalon, Shayegan, Vâlsan.

**Ce qui en découle, et qui est le vrai défaut** : ces textes sont cités en
source par des dizaines de fiches doctrinales, mais **Sidy ne peut pas les
ouvrir** depuis Obsidian pour vérifier une citation. Le poste CONSULTATION est
aveugle sur la matière même que le poste doctrinal invoque.

## Qui le porte

Sidy. Bénéficiaire : le poste CONSULTATION (Obsidian sur iPad, §I du protocole
racine), aujourd'hui privé de la moitié utile du dépôt.

## Les deux motifs de l'exclusion, éprouvés

Le `.gitignore` ne cache pas ses raisons — « peuvent contenir des données
personnelles + fichiers volumineux ». **Les deux ont été vérifiés, séparément,
et aucun ne tient pour les Markdown.**

### 1. Le poids — le motif vise les binaires, pas le texte

**14 Mo** de Markdown contre **2,6 Go** pour `raw/` entier. Le volume est
constitué des PDF, images et exports ; le texte converti en est 0,5 %.

### 2. Les données personnelles — mesuré, pas présumé

Balayage des 708 fichiers :

| motif cherché | trouvé |
|---|---|
| adresses e-mail | **aucune** |
| IBAN (motif strict) | **aucun** |
| numéros de téléphone | **aucun** |

⚠️ **Un faux positif rencontré, et il vaut d'être consigné** : un premier
balayage a signalé « IBAN » dans *Le Roi du Monde*. C'était **« Liban »** — la
recherche insensible à la casse trouvait la sous-chaîne. Le motif a été resserré
sur des bornes de mot avant de conclure. Un contrôle qui n'est pas éprouvé sur ce
qu'il prétend attraper ne vaut rien (§VII).

**En revanche, le motif tient pleinement pour les binaires** : `raw/` contient
des factures nominatives (`facture-woodbrass-*.pdf`), un export `ChatGPT
historique`, un dossier `Downloads`. Ceux-là restent hors git, et c'est le sens
de l'exclusion d'origine.

## Hors périmètre

- **Lever l'exclusion de `raw/` en bloc.** *Raison* : versionnerait aussi 2,6 Go
  de binaires dont des pièces nominatives. C'est la **première voie**, celle que
  Sidy a écartée.
- **Verser les textes dans un circuit existant.** *Raison* : `doctrinal/` porte
  des fiches au Sceau Recteur ; un texte brut n'en a pas et n'en veut pas. L'y
  loger casserait l'invariant plutôt que de l'honorer.
- **Nettoyer, corriger ou annoter les textes convertis.** *Raison* : ce sont des
  **sources**, immuables par nature. Ce chantier les déplace, il ne les touche
  pas.
- **Statuer sur les 147 doublons.** *Raison* : dédoublonner est une décision de
  contenu, pas de plomberie ; elle est signalée, non prise. Voir `spec.md` §4.

## Contraintes doctrinales

| Commandement | Ce qu'il impose ici |
|---|---|
| **§II** — architecture du dépôt | Un dossier de premier niveau **n'est pas un circuit**. Il faudra le dire explicitement, comme le protocole le fait déjà pour `meta/` (« pas un sixième circuit »), sans quoi la prochaine lecture à froid le prendra pour tel. |
| **Cmd 10** — pas de suppression sèche | Aucun fichier n'est supprimé de `raw/` : la migration **copie**, et l'original demeure jusqu'à verdict de suppression. |
| **Cmd 13** — porte humaine | Versionner 14 Mo et 561 fichiers change la nature du dépôt : c'est une décision, pas une réparation. |
| **§VII** — épreuve des contrôles | Le vérificateur d'invariants **doit avoir été vu échouer puis passer** sur la nouvelle arborescence, avant qu'on la déclare tenue. |
| **§VI** — étanchéité | Le nouveau dossier ne pointe vers aucun circuit et aucun circuit ne le cite en wikilink : ce sont des textes, pas des fiches. |

## Le signe de réussite

1. Sidy ouvre Obsidian sur son iPad et **lit un chapitre de Guénon** sans passer
   par le terminal.
2. `verifier-invariants.py` rend **0 erreur, 0 avertissement** sur un dépôt qui
   porte 561 fichiers sans frontmatter.
3. `raw/` conserve intacts ses binaires, ses factures et son export — **rien de
   nominatif n'entre dans git**.
4. La règle est **écrite** au protocole : quiconque lit `§II` à froid sait ce
   qu'est ce dossier et ce qu'il n'est pas.

## Ce qui reste ouvert

| question | destinataire |
|---|---|
| Le **nom** du dossier et sa place dans `§II` | Sidy — voir `spec.md` §1, trois candidats pesés |
| Les **147 doublons** : versés tels quels, ou résolus avant migration ? | Sidy |
| Les originaux de `raw/` : **conservés** après copie, ou retirés une fois la migration éprouvée ? | Sidy (Cmd 10) |
| Le régime des **futurs** textes convertis : passent-ils encore par `raw/` ? | Sidy — c'est la question de fond, celle qui évite que le problème se reforme |
