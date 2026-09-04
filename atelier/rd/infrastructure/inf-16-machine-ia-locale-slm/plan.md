---
title: "INF-16 — Machine d'IA locale et développement SLM : plan"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, plan, slm, materiel]
created: 2026-09-04
updated: 2026-09-04
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# INF-16 — Machine d'IA locale et développement SLM : plan

> **Statut** : `brouillon` — seul un plan `vise` autorise l'écriture (Cmd 6).
> Ce chantier ne produit pas de code ; ce que le visa autorise ici, ce sont les
> **dépenses de mesure** de l'étape 4 et l'ordre des étapes.

## Étapes

**Étape 1 — Arrêter la charge de référence.** Sidy retient, parmi les cinq usages
candidats du `spec.md` (U1 tri des tâches Hermes, U2 filtre d'étanchéité, U3
recherche sémantique, U4 fine-tuning, U5 distillation depuis un modèle large),
ceux qui comptent. C'est la seule étape qui ne peut pas être préparée par la
machine : elle décide de la taille de modèle, donc de la machine, donc du prix.
La ligne de verdict est consignée ici même sous la forme exacte
`charge de reference arretee : <usages> — <date>`, que le critère d'acceptation 1
va chercher.

**Étape 2 — Relever les prix, datés et sourcés.** Pour chaque option A à G : prix
d'acquisition de la configuration réellement visée (pas l'entrée de gamme, qui
n'est presque jamais la configuration utile), et coût récurrent. Aucun prix écrit
de mémoire (Cmd 5). Ce relevé inclut les paliers Apple au-dessus de l'entrée de
gamme, les cartes NVIDIA neuves **et** d'occasion, et les tarifs d'hébergeurs
GPU.

**Étape 3 — Mesurer ce qui est mesurable sans rien acheter.** Trois mesures :
(a) le **coût récurrent réel actuel** de la couche modèle — relevé, jamais
estimé, en nommant sa provenance ; (b) le volume et la forme du corpus qui
servirait à U3/U4 (`textes/` : 560 fichiers versés le 2026-09-02 ; `doctrinal/`
et les autres circuits) ; (c) la taille mémoire des modèles candidats, d'après
leurs fiches publiées. Cette étape retire à elle seule plusieurs cellules du
« non relevé ».

**Étape 3 bis — Retrouver le motif de la suspension des containers GPU cloud.**
Il conditionne l'honnêteté de l'option E et n'est consigné nulle part
(`to-source` du `spec.md`). Si le motif reste introuvable, l'écrire tel quel :
« motif non retrouvé », plutôt que de trancher l'option sans lui.

**Étape 4 — Montage à blanc avant tout achat.** Louer quelques heures de GPU
cloud (option E utilisée comme **instrument de mesure**, pas comme solution) et y
éprouver la charge de référence retenue sur un SLM candidat : débit réel,
qualité de sortie sur les tâches U1/U2, durée d'un fine-tuning de référence pour
U4. C'est la seule façon de remplir les critères 4, 5 et 6 par une mesure plutôt
que par une réputation — et le premier montage réel de la sandbox `/root/sandbox-rd/`,
ouverte le 2026-08-18 et **encore vide** (`INF-02`).

Deux gardes non négociables sur cette étape :
- **Aucune matière de `meta/` ne quitte le dépôt**, ni pour un essai, ni sous
  forme d'extrait (§VI). L'essai se fait sur du corpus neutre — `doctrinal/`,
  `textes/` — ou sur des données fabriquées pour l'occasion.
- **La dépense, si modeste soit-elle, est un point de retour à l'humain**
  (Cmd 13, ci-dessous).

**Étape 5 — Remplir la matrice.** Les 7 options × 12 critères, chaque cellule
mesurée, sourcée+datée, ou explicitement « non relevé ». L'option F (statu quo)
est renseignée comme les autres.

**Étape 6 — Rendre la recommandation à Sidy.** Proposée, argumentée, jamais
tranchée (Cmd 13). Elle nomme l'option retenue **et** ce qu'elle coûte en
souveraineté : une option qui laisse la couche LLM chez un tiers est présentée
comme telle, en toutes lettres.

**Étape 7 — Clore.** Entrée d'annales avec le SHA (Cmd 9), ligne de registre mise
à jour dans la même passe, et **réouverture d'`OUT-07`** (speculative decoding)
si — et seulement si — l'option retenue apporte un GPU local.

## Fichiers touchés

| Fichier | Nature |
|---|---|
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent.md` | créé (2026-09-04) |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec.md` | créé (2026-09-04) |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan.md` | créé (2026-09-04), le présent fichier |
| `atelier/rd/registre-chantiers.md` | modifié — ligne `INF-16` + recomptage du §0 |
| `atelier/annales.md` | modifié — entrée append-only en tête (Cmd 9) |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/matrice.md` | **à créer** à l'étape 5, pas avant |

Rien n'est déplacé, rien n'est supprimé. Aucun fichier existant du pôle n'est
réécrit hormis le registre et les annales, chacun selon sa discipline propre
(révisable en place pour le registre, append-only en tête pour les annales).

## Vérification

| Ce qu'on vérifie | Commande exacte |
|---|---|
| Invariants du dépôt, fiches du chantier comprises | `python3 verifier-invariants.py --racine /root/wiki` |
| La ligne de registre existe et pointe ici | `grep -n "INF-16" atelier/rd/registre-chantiers.md` |
| Les trois fiches portent bien le champ `chantier:` | `grep -c "^chantier: INF-16" atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/*.md` → `1` par fichier |
| Hygiène Unicode (Cmd 15) | contrôle du hook `pre-push` versionné (`atelier/rd/outillage/hooks/`) |
| La charge de référence a bien été arrêtée (critère 1) | `grep -n "charge de reference arretee" atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan.md` |

**Ce que ces contrôles ne prouvent pas** : ils portent sur la forme des fiches,
jamais sur la justesse d'un prix ou d'une mesure. Aucun script ne peut vérifier
qu'un tarif relevé est le bon — c'est la source datée qui en répond, et elle se
re-relève avant d'engager. Le dire ici évite de prendre un vert de forme pour
une validation de fond (§VII, épreuve des contrôles).

Si l'étape 4 produit un contrôle mécanique (par exemple un garde-fou de filtrage
pour U2), son **refus devra avoir été observé** sur une faute fabriquée exprès,
en bac à sable, et les deux résultats consignés — vert sur l'état sain, refus sur
la faute (§VII).

## Points de retour à l'humain

Quatre, dont deux avant toute action :

1. **Le visa de ce plan** (Cmd 6) — rien ne démarre sans lui.
2. **L'arrêt de la charge de référence** (étape 1) — Sidy seul.
3. **La location de calcul de l'étape 4** — dépense, si petite soit-elle
   (Cmd 13), et sortie de matière du dépôt vers un tiers (§VI) : le corpus
   exact envoyé est soumis avant l'essai.
4. **La décision d'achat** (étape 6) — préparée par la machine, tranchée par
   Sidy. C'est l'objet même du chantier, et son seul terme.

## Journalisation

Circuit : `atelier/annales.md`, préfixe `## [YYYY-MM-DD] chantier | INF-16 — …`,
SHA court du commit en dernière ligne, entrée rédigée **après** le commit (Cmd 9).
Ligne de registre `INF-16` mise à jour **dans la même passe** (section *Entretien*
du registre des chantiers).

Si le chantier produit une optimisation mesurée, elle va au
[[atelier/rd/cahiers/journal-optimisations]] ; s'il bute, au
[[atelier/rd/cahiers/registre-problemes]]. L'un ou l'autre, jamais les deux.
