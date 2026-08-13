---
title: "Signalement — Confrontation de 5 fiches doctrinal/discernement/ au corpus Guénon déposé (raw/)"
type: outillage
tags: [outillage, discernement, methode, confrontation, corpus, guenon, citation]
created: 2026-08-13
updated: 2026-08-13
sources: []
links: ["[[doctrinal/discernement/2026-08-04_qutb-manu-metatron-er-ruh-fonction-polaire-universelle]]", "[[doctrinal/discernement/2026-07-28_marques-de-la-contrefacon-grille-de-vigilance]]", "[[doctrinal/discernement/2026-07-28_sept-tours-sitra-ahra]]", "[[doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil]]", "[[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]]"]
---

# Signalement — Confrontation de 5 fiches `discernement/` au corpus Guénon déposé

> **Objet du présent rapport** : documenter la méthode et les résultats d'une
> confrontation entre 5 fiches `doctrinal/discernement/` et le corpus Guénon
> désormais présent en intégralité dans `raw/` (7 œuvres, 0 chapitre manquant
> — cf. § 5). Le rapport **signale** des écarts de fidélité de citation ; il
> ne tranche **aucune** question de fond doctrinal et ne modifie aucun champ
> `status`/`Statut` de fiche (Cmd 12). Sur le contexte ayant permis ce travail
> en session directe : [[wiki-contrainte-integration-levee]] (mémoire, hors
> dépôt).

## 1. Méthode

### 1.1 Vérification de complétude du corpus (préalable)

Chaque fichier `raw/` du corpus Guénon porte dans son frontmatter un champ
`source:` contenant les paramètres d'URL d'origine `Chapitre=NNN&sigle=XXXX`.
Ces identifiants sont **contigus par œuvre** et permettent une vérification
strictement mécanique de complétude (script Python, comparaison d'ensemble
d'entiers), sans lecture de fond :

| Œuvre | sigle | plage id | trous |
|---|---|---|---|
| Aperçus sur l'initiation | AI | 26–73 | 0 |
| Autorité Spirituelle et Pouvoir Temporel | ASPT | 134–142 | 0 |
| La Crise du Monde Moderne | CMM | 688–696 | 0 |
| Le Roi du Monde | RM | 766–777 | 0 |
| Le Règne de la Quantité et les Signes des Temps | RQST | 726–765 | 0 |
| Le Symbolisme de la Croix | SC | 779–808 | 0 |
| Les états multiples de l'être | EME | 877–894 | 0 |

Un chapitre manquant de RQST (id 746) a été identifié puis déposé par Sidy en
cours de session ; la plage est désormais sans trou pour les 7 œuvres.
Doublons d'id résiduels (AI 28/70, RQST 729/752, EME 881) et fichiers
possiblement mal classés : **hors périmètre du présent rapport**, renvoyés à
un signalement Volet B distinct (non rédigé à ce jour).

### 1.2 Scoping de la confrontation

`doctrinal/sources/` contient 25 fiches de citation Guénon, chacune rattachée
à une œuvre et un jeu de chapitres précis. Douze de ces fiches sont
**confrontables** (œuvre présente en intégralité dans `raw/`) ; treize ne le
sont pas, dont plusieurs à risque de confusion de titre avec une œuvre
déposée (ex. *Aperçus sur l'Ésotérisme islamique et le Taoïsme* ≠ *Aperçus
sur l'initiation* ; *L'Homme et son devenir selon le Vêdânta* absent de
`raw/`).

Croisement des wikilinks de `doctrinal/discernement/` vers ces 12 fiches
confrontables : 5 fiches du circuit `discernement/` citent au moins une
source confrontable. C'est le périmètre exact du présent rapport.

### 1.3 Vérification

Pour chaque citation directe (texte entre guillemets attribué à Guénon),
extraction Python (normalisation NFC) du passage correspondant dans le
fichier `raw/` identifié par son `Chapitre=`, comparaison caractère par
caractère. Pour les paraphrases non guillemetées de contenu doctrinal
(marques, chapitres, renvois), vérification de la présence et de la
substance du passage source, sans exigence de verbatim.

## 2. Résultats — citations vérifiées exactes

| Fiche | Source confrontée | Résultat |
|---|---|---|
| [[doctrinal/discernement/2026-08-04_qutb-manu-metatron-er-ruh-fonction-polaire-universelle]] | *Roi du Monde* ch. III, IV, VI (4 citations directes) | **Exactes**, verbatim. Referme le gap auto-signalé par la fiche (« pagination laissée to-source ») pour ces 4 citations. |
| [[doctrinal/discernement/2026-07-28_marques-de-la-contrefacon-grille-de-vigilance]] | *Règne de la Quantité* ch. XXVIII–XL (marques 9, 10, 11 notamment) | **Fidèles** en substance et en attribution de chapitre. Carte id→chapitre confirmée par le contenu réel (ch. XXX = « Le renversement des symboles », ch. XXXV = « La confusion du psychique et du spirituel », ch. XXXIX = « La grande parodie »). |
| [[doctrinal/discernement/2026-07-28_sept-tours-sitra-ahra]] | *Règne de la Quantité* ch. XXXIX, n. 7 (Metatron, Vulliaud, renvoi *Roi du Monde*) | **Confirmé verbatim** : « les deux faces lumineuse et obscure de *Metatron* », référence P. Vulliaud *La Kabbale juive* t. II p. 373, renvoi *Roi du Monde* pp. 34-35, nombre solaire 666. |
| [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]] | *Symbolisme de la Croix* ch. II, note 1 et note 5 | **Confirmées verbatim**, caractère pour caractère. La partie de la fiche portant sur *L'Homme et son devenir selon le Vêdânta* ch. XII/XIII reste **non confrontable** (œuvre absente de `raw/`). |

## 3. Écart signalé — fiche du 2026-07-27

[[doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil]]
présente deux formulations **entre guillemets, attribuées à Guénon**, qui ne
sont pas verbatim :

1. « Dans la tradition hyperboréenne, le septénaire *sapta-ṛkṣa* (les sept
   *Ṛṣis* ou Patriarches) siègent à la Grande Ourse. Dans la tradition
   atlantéenne, ils sont remplacés dans ce rôle par les Pléiades. »
   (attribuée « *Roi du Monde* ch. X, note 2 »)

   Texte réel (`raw/`, id 775, note appelée par le signe [4]) : *« La Grande
   Ourse est, dans l'Inde, le sapta-riksha, c'est-à-dire la demeure
   symbolique des sept Rishis; ceci est naturellement conforme à la
   tradition hyperboréenne, tandis que, dans la tradition atlante, la
   Grande Ourse est remplacée dans ce rôle par les Pléiades. »* — le sens
   général est fidèle ; la formulation n'est pas celle de Guénon (« ou
   Patriarches » notamment est absent du texte source), et le style
   verbal (« siègent à ») diffère de celui du texte (« est la demeure
   symbolique de »).

2. « une même fonction septénaire, deux supports stellaires, deux courants
   traditionnels » (présentée entre guillemets, attribuée à Guénon,
   *Roi du Monde* ch. X)

   Recherche exhaustive des termes « même fonction », « deux supports »,
   « deux courants » dans le fichier `raw/` correspondant au chapitre X
   (id 775) : **absents**. Cette phrase est une synthèse de la fiche, pas
   une citation.

Le contenu doctrinal environnant (rapport Balance polaire/Balance
zodiacale, Grande Ourse dite « Balance de jade », lien à *Melki-Tsedeq*,
renvoi au *Siphra di-Tseniutha*) est en revanche **fidèle sur le fond**,
vérifié dans le même fichier `raw/`.

## 4. Nature du signalement

Ce constat porte exclusivement sur la **forme de la citation** — l'usage de
guillemets impliquant l'exactitude verbatim, ici non tenue — et non sur la
validité de l'hypothèse portée par la fiche (septénaire à trois états,
rapport des deux Balances), dont l'examen métaphysique reste readable dans
la fiche elle-même et réservé à Sidy. La question posée n'est pas « ceci est
faux », mais : *voici deux passages entre guillemets qui ne correspondent
pas mot pour mot au texte source déposé — souhaitez-vous les reformuler en
paraphrase (hors guillemets) ou les remplacer par la citation exacte ?*

Aucun `Statut` de fiche `discernement` n'a été modifié par ce rapport.

## 5. Limites

- Périmètre strictement borné aux 5 fiches citant une source `doctrinal/sources/`
  confrontable — 23 autres fiches `discernement/` n'ont pas été confrontées
  (soit parce qu'elles ne citent aucune des 12 sources confrontables via
  wikilink, soit parce qu'elles n'ont pas de source Guénon directe).
- Trois fiches `doctrinal/sources/` portant sur *Les états multiples de
  l'être* (EME) sont confrontables mais ne sont citées par aucune fiche
  `discernement/` actuelle — hors périmètre par construction du croisement
  wikilink, pas par choix de contenu.
- Le Volet B (doublons d'id, fichiers possiblement mal classés, script
  `organize_guenon.sh`) reste entièrement à instruire, non commencé.
- Seules les citations **directement guillemetées** ont fait l'objet d'une
  vérification verbatim stricte ; les paraphrases de contenu doctrinal sans
  guillemets ont été vérifiées quant à leur présence et leur substance, non
  caractère pour caractère.
