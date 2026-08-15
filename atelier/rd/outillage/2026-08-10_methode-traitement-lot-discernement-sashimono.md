---
title: "Méthode — Traitement d'un lot de fiches discernement/ (qualification sashimono fiche par fiche)"
type: outillage
tags: [outillage, discernement, methode, sashimono, fiche-par-fiche]
created: 2026-08-10
updated: 2026-08-15
sources: []
links: ["[[atelier/rd/outillage/2026-08-10_methode-croisement-discernement]]", "[[doctrinal/index]]"]
---

# Méthode — Traitement du bloc `doctrinal/discernement/2026-06-20_*` (11 fiches)

> **Objet du présent rapport** : documenter le *moyen* utilisé pour traiter,
> à la demande de Sidy, un lot de 11 fiches `discernement/` issues d'une même
> séance de production des fiches (2026-06-20), explicitement écarté du croisement général
> ([[atelier/rd/outillage/2026-08-10_methode-croisement-discernement]]) parce
> qu'une co-occurrence de même séance n'est pas une corroboration. Ce document
> ne contient et ne reformule **aucun** contenu doctrinal ni verdict de fond —
> il documente une méthode d'ingénierie, transposable à tout futur lot
> similaire.

## 1. Constat de départ

Le croisement général (méthode déterministe, extraction frontmatter +
wikilinks) est **impuissant** sur un lot mono-séance : les 11 fiches se
co-citent naturellement (même expérience source), et un script de
co-citation y verrait à tort une convergence. Aucune action mécanique
honnête n'existait donc sur ce lot avant une lecture de fond.

## 2. Reconnaissance intégrale avant tout plan

Contrairement au croisement général (frontmatter suffisant), ce lot a
nécessité une **lecture complète des 11 corps de fiche**, pas seulement du
frontmatter — délégué à un agent Explore dédié. Motif : deux angles morts
déjà rencontrés dans la session précédente (croisement général) tenaient
précisément à une extraction qui s'arrêtait au frontmatter et manquait des
éléments logés en corps de texte (ex. une confrontation Gizeh déjà présente
mais non détectée). Leçon retenue : **toute reconnaissance sur du contenu
narratif/spéculatif doit lire le corps intégral, l'extraction déterministe
ne suffit que pour du contenu structuré (frontmatter, listes de liens)**.

## 3. Passage obligé par un plan validé avant écriture (Cmd 6)

Le constat de reconnaissance (aucune fiche du lot ne porte de qualification
sashimono explicite malgré 10/11 rapprochements inter-traditionnels ;
aucune matière polaire/axiale/septénaire/métrologique-28 au sens strict ;
4 liens à référent vide en prose ; un manquement de sourçage qualifié
« grave » par une fiche elle-même) a été présenté en Plan Mode avant toute
écriture. Le plan fixait explicitement ce qu'il **ne ferait pas** (aucune
fusion entre fiches, aucun `Statut`/`Conclusion` modifié, aucune
confrontation Gizeh fabriquée) — ces bornes négatives se sont révélées aussi
utiles à faire approuver que le geste positif lui-même.

## 4. Différenciation du geste selon l'état de la fiche

Le lot n'était pas homogène : 9 fiches ouvertes, 1 fiche close (verdict
Sidy 2026-07-14, antérieur à l'adoption du double contrôle du 2026-07-16), 1
fiche de nature différente (alerte, pas un rapprochement). Trois traitements
distincts en ont résulté :

- **fiches ouvertes** → qualification *kari-kumi* (geste normal du double
  contrôle, applicable rétroactivement à du contenu produit avant la règle) ;
- **fiche close antérieure à la règle** → **pas** de qualification
  kari-kumi (rouvrir la forme d'une fiche close pour y coller une
  qualification vivante aurait pu se lire comme une réouverture de fond) ;
  seule une **note factuelle de traçabilité**, explicitement non-rouvrante,
  a été ajoutée ;
- **fiche de nature différente** (alerte) → **aucune** modification, geste
  simplement inapplicable.

Enseignement généralisable : la règle « qualifier tout joint » ne doit
jamais s'appliquer mécaniquement à un lot — l'état de chaque pièce (ouverte /
close / hors-catégorie) commande un traitement propre, et le distinguo lui
seul suffit souvent à éviter un faux mouvement (ici : rouvrir une fiche déjà
tranchée par Sidy).

## 5. Vérification mécanique indépendante de l'outil d'édition

Sur une fiche du lot, deux appels d'édition ont rapporté un succès, suivis
d'une réponse ambiguë de l'outil de lecture (relecture bloquée, laissant
craindre une double insertion). Plutôt que de se fier au rapport de succès
de l'outil (§VIII.2 : fiabilité d'action ≠ fiabilité narrative), la
vérification a été faite par une commande indépendante :

```bash
grep -n "Qualification sashimono\|updated:" fichier.md
```

Un seul résultat par motif confirmait l'absence de duplication. Cette
vérification par un canal distinct de celui qui a produit l'écriture
(grep vs. outil d'édition) est reproductible pour tout futur lot de
modifications homogènes sur de multiples fichiers.

## 6. Discipline fiche par fiche tracée par tâches (§VIII.3)

Les 11 fiches ont été suivies comme 11 tâches distinctes (une par fiche),
jamais traitées par une instruction large sur le dossier. Ceci a permis un
contrôle final trivial : `git status --short` devait lister exactement les
fichiers correspondant aux tâches marquées terminées — ni plus, ni moins
(en particulier, confirmer qu'aucune modification involontaire n'avait
touché la fiche d'alerte exclue du geste).

## 7. Séquence de clôture en deux commits

1. commit substantif (les fiches modifiées) ;
2. **puis** entrée d'annales rédigée avec le SHA court du premier commit,
   committée séparément.

Cette séquence (jamais l'inverse) découle directement de Cmd 9 : une entrée
d'annales décrivant une opération encore non commitée serait un
enregistrement d'une opération planifiée mais non exécutée, interdit par la
règle. Le second commit ne modifie qu'`annales.md`.

## 8. Nature du livrable

Comme pour le croisement général, le résultat est un **signalement**, jamais
un verdict : la qualification sashimono documente une structure formelle
déjà présente dans le texte, elle ne juge à aucun moment la validité
spirituelle du contenu (Cmd 2, Cmd 12). Deux constats mécaniques (liens
morts, sourçage à vérifier) ont été rapportés à l'identique dans l'entrée
d'annales plutôt que corrigés d'office, conformément à Cmd 10 (pas de
correction/suppression sans confirmation) — la réparation d'un lien mort
n'est pas neutre si sa cible probable (un motif familial documenté ailleurs)
n'a jamais été confirmée comme devant exister en fiche autonome.

## 9. Limites et transposabilité

- Cette méthode suppose un lot **petit et homogène par provenance** (une
  séance). Pour un lot volumineux ou hétérogène, la reconnaissance intégrale
  en amont (§2) devient le goulot d'étranglement — à budgétiser en
  conséquence (agent dédié, hors du fil principal).
- Le distinguo ouverte/close/hors-catégorie (§4) est probablement le point
  le plus généralisable de cette méthode : tout futur traitement de lot sur
  `discernement/` devrait commencer par cette partition avant même de
  choisir le geste à appliquer.
