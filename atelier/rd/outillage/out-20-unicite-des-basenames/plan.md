---
title: "OUT-20 — unicité des basenames, garde du wikilink court : plan"
type: outillage
chantier: OUT-20
tags: [atelier, rd, outillage, chantier, plan, wikilink, controle]
created: 2026-09-18
updated: 2026-09-18
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/out-20-unicite-des-basenames/spec]]"
---

# OUT-20 — unicité des basenames, garde du wikilink court : plan

> **Statut** : `vise` — visa de Sidy, 2026-09-18 : « Je valide l'ensemble, tu peux
> engager ». **Les six étapes sont exécutées** le jour même : mesure (étape 1), deux
> verdicts rendus sur cette mesure (étape 2), B9 écrit (3), éprouvé par l'échec (4),
> organe MCP vérifié (5), journalisé (6).

## Étapes

1. **Mesurer les deux questions laissées ouvertes**, avant toute ligne de code : (a)
   combien de collisions de basename existent aujourd'hui entre les cinq circuits, une
   fois les exemptions nommées retirées ; (b) combien entre un circuit et `textes/` ou
   `protocoles/`. Sortie brute rapportée à Sidy, sans conclusion.
2. **Rapporter à Sidy les deux verdicts attendus** : refus sec ou avertissement
   conditionné à l'existence d'un renvoi court ; périmètre avec ou sans `textes/` et
   `protocoles/`. Le code n'est pas écrit avant.
3. **Écrire B9** dans `verifier-invariants.py`, dans la famille des contrôles B, avec sa
   liste d'exemptions close et nommée.
4. **Éprouver par l'échec** (§VII), dans une copie jetable hors dépôt vivant : ligne de
   base au vert, faute fabriquée, **refus observé**, faute retirée, retour au vert.
5. **Vérifier l'organe MCP** : l'entrée `verifier_invariants` rend B9 dans son JSON.
6. **Journaliser** et mettre à jour la ligne de registre dans la même passe.

## Fichiers touchés

- `verifier-invariants.py` — **modifié** (ajout du contrôle B9).
- `atelier/rd/registre-chantiers.md` — ligne `OUT-20` mise à jour.
- `atelier/annales.md` — entrée de passe, SHA court en dernière ligne.
- Aucun fichier supprimé, aucun renommé : le contrôle constate, il ne range pas.

## Vérification

```bash
# critère 1 — ligne de base inchangée sur le dépôt vivant
python3 verifier-invariants.py --racine /root/wiki | tail -2
# attendu : 0 erreur(s), 71 avertissement(s)   (et aucun [B9])

# critères 2 et 3 — l'épreuve par l'échec, en copie jetable
cp -r /root/wiki /tmp/bac-b9 && cd /tmp/bac-b9
cp doctrinal/symboles/barzakh.md atelier/rd/barzakh.md && git add atelier/rd/barzakh.md
python3 verifier-invariants.py --racine /tmp/bac-b9 | grep B9
# attendu : [B9] barzakh — porté par 2 fichiers : atelier/rd/barzakh.md,
#           doctrinal/symboles/barzakh.md
git rm --cached atelier/rd/barzakh.md && rm atelier/rd/barzakh.md
python3 verifier-invariants.py --racine /tmp/bac-b9 | tail -2   # retour au vert

# critère 4 — les homonymes de convention ne déclenchent rien
python3 verifier-invariants.py --racine /root/wiki | grep -c "B9.*plan\b"   # attendu : 0
```

## Points de retour à l'humain

Deux, tous deux avant l'écriture du code (Cmd 13) : la **sévérité** du contrôle (erreur
ou avertissement) et son **périmètre** (`textes/` et `protocoles/` inclus ou non). Aucun
des deux ne se déduit d'une mesure — ils engagent la règle, pas le fait.

## Journalisation

`atelier/annales.md` (le pôle `rd/` y journalise, `atelier/CLAUDE.md`), ligne `OUT-20`
du registre des chantiers mise à jour dans la même passe, et entrée au registre des
problèmes si l'épreuve révèle un écart non prévu.


-----

## Étape 1 — exécutée le 2026-09-18 : la mesure, et ce qu'elle renverse

Périmètre : `git ls-files '*.md'` — **1760 fichiers suivis, 1667 basenames distincts**.

### (a) Collisions entre circuits, hors exemptions nommées : **17**

**L'unicité du basename n'est donc pas un état à préserver : c'est un état qui n'existe
déjà plus.** La mesure du matin (« 589 renvois courts, 0 ambiguïté ») portait sur les
*renvois* et reste exacte — aucun d'eux ne vise un basename doublé. Elle ne disait rien
des **fichiers**, et c'est là que se trouvent les 17.

| Classe | Nombre | Détail |
|---|---|---|
| `atelier/projets/` ↔ `atelier/rd/` (instrument et outillage) | **12** | stubs `deprecated` laissés en place à la migration du 2026-08-08 (Cmd 10) face à la fiche vivante de même nom : `spec-anneau-zodiacal`, `angles-de-l-espace`, `soumission-gem-*` (4), `spec-technique-axe-38-degres`, `spec-generateur-manifeste`, `instrument-feuille-de-route-v2`, `references-visuelles-astronomiques-phase-5`, `note-impact-instrument-socle-universel-2026-07-16`, `2026-07-26_investigation-referentiels-stellaires-cycles` |
| `doctrinal/autorites/` ↔ `doctrinal/references/` | **4** | `al-afghani`, `muhammad-abduh`, `rashid-rida`, `curt-jaimungal` — une même personne fichée dans les deux dossiers |
| `atelier/projets/` ↔ `label/production/` | **1** | `album-personnel` (migration du 2026-08-08 vers `label/`) |

Les 12 premières sont donc la **trace voulue** d'une migration réversible, et les 4
suivantes une distinction de rôle (autorité / référence) qui mérite d'être regardée pour
elle-même — ni l'une ni l'autre n'est un défaut à corriger par ce chantier.

### (b) Collisions impliquant `textes/`, `protocoles/` ou la racine : **18**

- **`textes/` contre lui-même : 15**, homonymie **par construction** des conversions —
  `index-conversion` × 10, `corps-du-texte` × 3, `00-front-matter` / `01-a` … `11-k` × 2
  (deux dictionnaires découpés par lettre).
- **`textes/` contre `doctrinal/sources/` : 3** — `sefer-yetsira-ramban`,
  `traite-emanation-gauche-isaac-ha-kohen`, `koly-cherif-keita-djinns-aident-humains` :
  la fiche qui dit, et le texte reçu qui est dit, portent le même nom.
- **`_inbox/` contre `doctrinal/symboles/` : 1** — `tariqa`. **C'est le seul cas vivant
  du risque que ce chantier vise** : cinq fiches doctrinales portent le renvoi court
  `[[tariqa]]`, et le sas a déposé un homonyme le 2026-09-17 (`a3e9d7a`). Le graphe
  exclut `_inbox/` de ses nœuds, donc rien n'a cassé — mais la démonstration est faite
  sur pièce, et non en théorie : **un lot entrant peut doubler un basename visé par des
  renvois courts, sans que rien ne le signale.**

### Ce que la mesure impose aux deux verdicts de l'étape 2

1. **Sévérité** : un refus sec ferait échouer le dépôt **17 fois dès la première
   exécution**, sur des doublons voulus. Le contrôle doit donc soit avertir, soit ne
   refuser **que** sur un basename réellement visé par un renvoi court — auquel cas il
   refuserait aujourd'hui sur le seul `tariqa`, et pour une raison juste.
2. **Périmètre** : inclure `textes/` ajouterait 15 collisions par construction ; c'est
   `_inbox/` — non prévu au périmètre initial — qui a produit le seul cas vivant.


-----

## Étapes 2 à 6 — exécutées le 2026-09-18

### Étape 2 — les deux verdicts, rendus sur la mesure

- **Sévérité** : « refus seulement si un renvoi court vise ». B9 ne refuse que lorsqu'un
  basename doublé est **effectivement la cible** d'un renvoi court. Les 17 collisions
  voulues restent muettes — le contrôle garde ce qui casse un lien, non ce qui déplaît à
  l'œil.
- **Périmètre** : « les cinq circuits **plus `_inbox/`** ». `textes/` et `protocoles/`
  restent dehors (cibles d'aucun wikilink, §II ; et `textes/` porte 15 collisions par
  construction).

### Étape 3 — B9 écrit, et ce qu'il n'est pas

Deux pièces, délibérément séparées : `collecter_collisions()` compte des **noms de
fichiers** dans le périmètre B9 ; `controler_unicite_basenames()` croise ce compte avec
les **renvois courts réellement écrits**, récoltés au passage par les deux contrôleurs de
liens (corps et cartouche).

**Deux pièges évités, l'un et l'autre mesurés :**

1. **B9 n'est pas un doublon de `C2`.** `C2` avertit quand un lien court est ambigu *dans
   l'index de résolution* — d'où `_inbox/` est absent. Or le sas est exactement la porte
   par laquelle une collision entre. `C2` regarde les liens, B9 regarde les fichiers.
2. **`_inbox/` figure dans `DOSSIERS_EXCLUS`**, et `hors_perimetre()` l'écarte pour tous
   les autres contrôles — à juste titre : le sas n'est pas le dépôt. Réutiliser cette
   fonction ici aurait **annulé le verdict par un détail d'implémentation** ; B9 porte
   donc son propre filtre, qui reprend la clause git et laisse tomber la clause des
   dossiers exclus. Le motif est écrit dans le code, à l'endroit où l'on serait tenté de
   « simplifier ».

B9 émet **une** ligne par basename fautif, portée par `<dépôt>` et non par une fiche : le
défaut n'est pas dans la fiche qui renvoie, il est dans la paire de fichiers qui rend son
renvoi équivoque.

### Étape 4 — épreuve par l'échec (§VII), quatre temps, en copie jetable

Bac à sable hors dépôt vivant (`git archive HEAD | tar -x`), **jamais le dépôt lui-même** :

| Temps | État | Attendu | Obtenu |
|---|---|---|---|
| 1 | sain (collision du sas retirée) | 0 erreur | **0 erreur**, 77 avertissements ✅ |
| 2 | homonyme fabriqué **dans un circuit** (`atelier/rd/barzakh.md`) | refus | **31 erreurs** — B9 tire, et il est **le seul à nommer la cause** ; les 30 autres (`C3`, `C1`) sont l'effet de bord de la résolution par slug ✅ |
| 3 | homonyme fabriqué **dans le sas** (`_inbox/lot-epreuve/barzakh.md`) — *le cas visé par le verdict* | refus, et lui seul | **exactement 1 erreur**, B9 seul, les autres contrôles muets ✅ |
| 4 | faute retirée | retour au vert | **0 erreur** ✅ |

Le temps 3 est celui qui justifie le chantier : quand la collision naît dans le sas, **B9
est le seul contrôle du dépôt qui la voit**.

### Étape 5 — le dépôt vivant, et le remède appliqué

Au premier passage sur le dépôt vivant : **1 erreur** — `tariqa`, porté par
`doctrinal/symboles/tariqa.md` et par le lot du sas du 2026-09-17, et visé en forme courte
par cinq fiches. Le contrôle nomme lui-même les deux issues (« nommer le chemin complet,
ou lever la collision ») : la première est mécanique et n'engage rien, elle est appliquée
— **8 occurrences dans 5 fiches** passent à `[[doctrinal/symboles/tariqa]]`. Le lot du sas
reste intact : son intégration est une passe à part entière, et B9 a précisément servi à
la signaler **avant** qu'elle ait lieu.

**Ligne de base après** : `0 erreur, 71 avertissements` — inchangée. B9 est en place et
vert, sans avoir rien coûté au dépôt.

### Étape 6 — journalisation

`atelier/annales.md`, ligne `OUT-20` du registre des chantiers, et cette fiche.
