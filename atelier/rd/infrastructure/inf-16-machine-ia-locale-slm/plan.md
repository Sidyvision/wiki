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

**~~Étape 3 bis~~ — sans objet depuis le 2026-09-04.** Le motif de la suspension
des containers GPU cloud est établi (verdict de Sidy, §*Verdict* du `spec.md`) :
configuration trop fastidieuse, facturation maintenue à l'arrêt, coût
disproportionné pour du matériel non possédé. L'étape est conservée barrée
plutôt que retirée (Cmd 10) — c'est la trace de ce qui a été cherché.

**Étape 4 — refondue le 2026-09-04.** La version initiale prévoyait de louer
quelques heures de GPU cloud comme **instrument de mesure** avant tout achat.
Elle tombe : le premier point du verdict — la configuration fastidieuse — vaut
identiquement pour un essai d'une heure et pour un usage durable, et le
troisième vaut a fortiori pour une dépense qui ne laisse aucun bien. Prétendre
maintenir l'étape en la disant « petite » reviendrait à contourner le verdict
plutôt qu'à en tenir compte.

Il n'existe donc **plus de moyen de mesurer avant d'acheter**. C'est un fait du
chantier, pas un échec : il faut le porter, non le masquer. Trois voies de
remplacement, à trancher par Sidy :

| Voie | Ce qu'elle donne | Ce qu'elle coûte |
|---|---|---|
| **4a — Décider sur données publiées** | débits et durées repris de mesures tierces, sourcées et datées | ce ne sont pas *nos* mesures sur *notre* charge : la matrice le porte en toutes lettres, jamais fondu avec du mesuré (§VII) |
| **4b — La machine la moins chère devient l'instrument de mesure** | on acquiert d'abord le plus petit matériel qu'on voudrait de toute façon (option B), on y mesure la charge de référence réelle, et l'on ne décide qu'ensuite d'un éventuel palier supérieur | une dépense engagée avant la comparaison complète — mais sur un bien possédé, revendable, et utile même si le verdict final va ailleurs |
| **4c — Renoncer à la mesure préalable** | on tranche sur la seule matrice documentaire | risque assumé de surdimensionner ou de sous-dimensionner, à couvrir par le critère 10 (réversibilité) |

**La voie 4b mérite d'être regardée en premier** : elle retourne la contrainte
en méthode. Le matériel devient lui-même le banc d'essai, la dépense reste
proportionnée, et la réversibilité (Cmd 10) y est réelle — un bien possédé se
revend ou se réaffecte, une heure de location ne laisse rien. C'est aussi, dans
l'esprit du dépôt, un montage à blanc au sens propre : on éprouve avant
d'engager le gros.

Garde maintenue quelle que soit la voie : **aucune matière de `meta/` ne quitte
le dépôt** (§VI), y compris pour un essai et y compris sous forme d'extrait.

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
3. **Le sort de l'option D** (serveur GPU dédié loué) — le critère qui a fermé E
   (« trop coûteux pour du matériel dont on n'est pas propriétaire ») semble
   l'emporter de la même façon, mais l'écarter serait une décision, pas un
   relevé (Cmd 13). Question posée à Sidy, non tranchée ici.
4. **Le choix de la voie de mesure** (étape 4 : 4a documentaire, 4b la petite
   machine comme banc d'essai, 4c sans mesure préalable) — la voie 4b engage une
   dépense avant la fin de la comparaison, donc elle relève de Sidy.
5. **La décision d'achat** (étape 6) — préparée par la machine, tranchée par
   Sidy. C'est l'objet même du chantier, et son seul terme.

> **Ce que le verdict du 2026-09-04 a déjà retiré du plan** : la location de
> calcul, qui figurait ici en point 3. Elle n'est pas reportée, elle est fermée
> (option E, §*Verdict* du `spec.md`).

## Journalisation

Circuit : `atelier/annales.md`, préfixe `## [YYYY-MM-DD] chantier | INF-16 — …`,
SHA court du commit en dernière ligne, entrée rédigée **après** le commit (Cmd 9).
Ligne de registre `INF-16` mise à jour **dans la même passe** (section *Entretien*
du registre des chantiers).

Si le chantier produit une optimisation mesurée, elle va au
[[atelier/rd/cahiers/journal-optimisations]] ; s'il bute, au
[[atelier/rd/cahiers/registre-problemes]]. L'un ou l'autre, jamais les deux.
