---
title: "Proposition — Type neutre « référence » (Sceau Recteur et annotations)"
type: meta
tags: [protocole, sceau-recteur, annotations-html, reference, proposition]
created: 2026-09-15
updated: 2026-09-15
---

# Proposition — le type neutre « référence »

> **Statut : validée par Sidy le 2026-09-15, exécution effective.** Réponses aux questions du
> § 6 : « 1. Confirmé 2. Oui 3. Oui 4. Plus tard, ajoute à Queue-idée ». Exécuté le même jour :
> protocoles (§ 4, points 1-4), outils (points 5-7, dont le contrôle B8 de la proposition
> annexe), reprises des points 8 et 9 ; le point 10 est versé à
> `meta/projet-unifie/queue-idees.md`. Idée de Sidy : « un nouveau type : "référence" comme
> catégorie neutre ».

## 1. Constat — deux trous, révélés le même jour

**Au Sceau.** Le champ `type:` du Sceau Recteur n'offre, pour une personne, que
`autorite`. Une personne citée **sans être une autorité** n'a pas de place : Curt Jaimungal,
élément antagoniste de l'étude du 2026-09-15, a d'abord été placé en `autorites/`, puis — sur
verdict de Sidy (« il ne me semble pas que l'on puisse placer Curt Jaimungal en autorité ») —
replié dans la fiche **source** de sa conférence, un talon `deprecated` restant en
`autorites/curt-jaimungal.md`. Le repli fonctionne pour une personne connue par **une**
source ; il ne vaut plus pour une personne citée à travers plusieurs textes, ou sans texte
versé.

**Aux annotations.** Le vocabulaire `data-genre` est clos à sept valeurs (`autorite`, `lieu`,
`ouvrage`, `entite`, `ecole`, `cycle`, `principe`). Aucune n'est neutre pour une personne :
l'annotation du nom de Jaimungal a dû être **retirée** de l'étude.

**Un troisième cas, moins visible.** Muhammad ʿAbduh, Rashīd Riḍā et Jamāl al-Dīn
al-Afghānī, cités par Sidy comme figures de la déviation réformiste, ont été placés en
`autorites/` avec un `status: profane` **proposé** ; leur placement est déclaré provisoire
dans chaque fiche. Le mot « autorité » y porte une valeur que le statut contredit.

## 2. Proposition

### 2.1 Au Sceau Recteur — `type: reference`

Ajouter `reference` aux valeurs de `type:` dans `doctrinal/CLAUDE.md` :

> `reference` : personne ou figure **citée** par le dépôt — pour être discutée, réfutée ou
> documentée — **sans autorité** reconnue dans l'ordre traditionnel. Le type dit ce qu'est la
> fiche dans le dépôt ; il ne confère rien.

**Le type reste neutre ; le statut porte le jugement.** Une référence reçoit son `status`
comme toute fiche : `academique` (Jaimungal), `profane` (proposé pour ʿAbduh, Riḍā,
al-Afghānī), `contre-traditionnel` le cas échéant. La distinction devient lisible : `type`
répond à « qu'est-ce ? », `status` à « que vaut ce qui y est reproduit ? ».

**Frontières, à inscrire au protocole avec la définition** :

| Type | Porte sur | Exemple |
|---|---|---|
| `autorite` | une personne dont l'enseignement **fait autorité** dans l'ordre traditionnel | Ibn ʿArabī, Guénon |
| `reference` | une personne **citée**, sans cette autorité | Jaimungal, ʿAbduh |
| `source` | un **texte**, un document, une conférence | la conférence de Jaimungal |

Une même personne peut avoir une fiche `reference` et plusieurs fiches `source` (ses
textes) ; la fiche `reference` pointe vers les sources, jamais l'inverse obligatoire.

### 2.2 Aux annotations — `data-genre="reference"`

Ajouter `reference` au vocabulaire **clos et transversal** (valable dans les cinq circuits),
qui passe de sept à huit valeurs : l'annotation *type* le nom, sans conférer d'autorité — la
même garde que `auteur` en `hermeneutique/`. Le mot « figure » est écarté : il appartient déjà
au vocabulaire propre d'`hermeneutique/` (D6 le refuserait ailleurs).

### 2.3 Arborescence

Nouveau dossier `doctrinal/references/<slug>.md`, nommé comme `autorites/` (slug de la
personne, sans date). Nouvelle rubrique au Catalogue, § III bis « Les Références ».

## 3. Deux points de vigilance

- **Homonymie avec l'atelier.** Dans `atelier/`, « (RÉFÉRENCE) » qualifie `materiel/` et
  `entretiens/` au sens de *documentation de consultation*. Autre circuit, autre sens : la
  définition du type le signalera en une ligne, pour qu'aucun agent ne confonde.
- **Pas de glissement vers « source ».** Une référence est une **personne** ; un texte reste
  une `source`, même s'il est de la même personne.

## 4. Ce que l'exécution toucherait

**Protocoles**

1. `doctrinal/CLAUDE.md` — valeurs de `type:` au Sceau, définition, tableau des frontières.
2. `CLAUDE.md` racine, §VII — « `data-genre` restreint à un vocabulaire clos de sept
   valeurs » devient huit (le principe y est énoncé : Cmd 14).
3. `protocoles/annotations-html.md` — vocabulaire, et la garde « aucune autorité conférée ».
4. `meta/protocole-archives/changelog-CLAUDE.md` — entrée d'amendement ; version du protocole
   archivée avant modification (Cmd 10).

**Outils**

5. `valider-annotations.py` — `reference` ajouté à `GENRES_CLOS` ; **épreuve** : un genre
   `reference` accepté, un genre inventé toujours refusé.
6. `verifier-invariants.py` — **constat du 2026-09-15** : il exige la *présence* de `type:`
   mais n'en contrôle pas la *valeur*. Aucun changement n'est donc nécessaire pour accepter
   `reference`. **Proposition annexe, à viser séparément** : lui faire contrôler la valeur de
   `type:` contre la liste du Sceau (refus d'un type inconnu), avec épreuve — ce trou existe
   indépendamment de la présente proposition.
7. `generer-index-lexical.py`, `graphe/generer-cartographie.py`, `carte-du-depot.py` — aucun
   n'énumère les types ni les dossiers de `doctrinal/` (relevé du 2026-09-15) : régénération
   seulement, puis contrôle que les fiches de `references/` y figurent.

**Reprises de fiches** — chacune sur verdict, jamais d'office (Cmd 12)

8. **Jaimungal** : créer `doctrinal/references/curt-jaimungal.md` (la personne) ; la fiche
   source de la conférence reste ; le talon `autorites/curt-jaimungal.md` est redirigé vers la
   référence ; l'annotation de son nom dans l'étude est rétablie en `data-genre="reference"`.
9. **ʿAbduh, Riḍā, al-Afghānī** : déplacement `autorites/` → `references/` par `git mv`,
   talons `deprecated` aux anciens emplacements, annotations `autorite` → `reference` dans
   les fiches qui les citent. **Verdict attendu**, fiche par fiche.
10. **Rubrique « Érudition académique »** du Catalogue (sept fiches : Ali Hussain,
    R. Raphael Afilalo, Yaqub Chaudhary, Aiman Attar, Titus Burckhardt, Faraz Rabbani,
    Hamza Yusuf) : **à réexaminer** au même critère, sans rien déplacer d'office. Relevé
    utile : la fiche Yaqub Chaudhary, rangée sous « Érudition académique », porte
    `status: traditionnel` — incohérence à trancher quelle que soit l'issue de la présente
    proposition.

**Clôture** : index lexical et graphe régénérés (fiches ajoutées à git **avant** — règle du
2026-09-15), validateur, `verifier-invariants.py`, annales (doctrinal, atelier, meta),
commit, envoi.

## 5. Réversibilité

Chaque déplacement laisse un talon ; le type et le genre peuvent être retirés sur simple
verdict, les fiches revenant à leur emplacement antérieur (Cmd 10).

## 6. Questions pour Sidy

1. Le nom : `reference` (ASCII, sans accent, comme `autorite`) — confirmé ?
2. La reprise de ʿAbduh, Riḍā et al-Afghānī : en `references/` ?
3. La proposition annexe (contrôle de la valeur de `type:`) : à ouvrir ?
4. L'examen de la rubrique « Érudition académique » : maintenant, ou plus tard ?
