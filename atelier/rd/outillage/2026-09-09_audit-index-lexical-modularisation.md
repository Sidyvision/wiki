---
title: "Audit du système d'index lexical — générateur, validateur, sorties"
type: outillage
tags: [rd, outillage, index-lexical, audit, modularisation]
created: 2026-09-09
updated: 2026-09-09
sources: []
links:
  - "[[atelier/rd/cahiers/2026-09-09_etat-des-lieux-indexation-et-reprise]]"
  - "[[atelier/rd/outillage/2026-09-08_serveur-mcp-wiki]]"
  - "[[atelier/rd/infrastructure/2026-09-09_feedback-audit-wiki-qoder]]"
---

# Audit du système d'index lexical

> Audit externe (Qoder, 2026-09-09). Le générateur (1 216 lignes), le
> validateur (361 lignes) et leurs sorties ont été relus ligne à ligne, puis
> exécutés en live. Ce rapport est versé au registre R&D pour traitement.
>
> **Pièces auditées** — citées **en prose, par chemin relatif**, jamais en
> wikilink : `atelier/rd/outillage/index-lexical/generer-index-lexical.py` et
> `atelier/rd/outillage/index-lexical/valider-annotations.py`. Ce sont des
> **scripts**, et le régime de liens du dépôt ne connaît que des cibles `.md` :
> un wikilink vers un `.py` ne se résout pas et lève un avertissement C1. La
> convention employée ici est celle déjà en vigueur pour ce qui n'est cible
> d'aucun lien — les dossiers `assets-<sujet>/` et `textes/` (§II).
>
> **Écart de protocole que cet audit a révélé, et qui le dépasse** : aucune
> fiche ne décrit ces deux scripts, et **le dépôt n'a pas de forme pour citer
> un script en `links:`**. Rapporté, non tranché (Cmd 12).

---

## I. Mesures

| Grandeur | Valeur |
|---|---|
| Termes indexés | 10 695 |
| Occurrences | 420 103 |
| Fiches indexées (circuits) | 758 |
| Textes balayés | 657 |
| Annotations HTML validées | 934 (321 fiches) |
| Poids JSON | 4,2 Mo |
| Poids MD condensé | 1,2 Mo (6 149 lignes) |
| Fichiers éclatés | 28 (hub + a–z + écritures) |
| Poids générateur | 1 216 lignes |
| Poids validateur | 361 lignes |

**Validateur** : 0 anomalie D1–D6, 4 signalements S1 légitimes (yuga/kali-yuga,
janus/janus-bifrons — vrais jugements réservés, Cmd 12).

**Distribution des rôles** :

| Rôle | Termes |
|---|---|
| translit | 5 887 |
| table | 3 320 |
| tag | 1 201 |
| titre | 1 155 |
| definition | 847 |
| annotation | 400 |

**Distribution des fiches par terme** :

| Tranche | Nombre |
|---|---|
| 1 fiche (queue) | 5 741 (54 %) |
| 2–10 fiches | 4 639 |
| 11–50 fiches | 929 |
| > 50 fiches | 384 |
| Médiane | 1 |

**Top 10 termes** (par nombre de fiches) :

| Terme | Fiches | Rôle | Nature |
|---|---|---|---|
| source | 504 | table, tag | Métadonnée Sceau |
| sidy | 476 | definition, table, titre | Propriétaire |
| deux | 448 | table, titre | Numéral |
| doctrinal | 433 | table, tag, titre | Nom de circuit |
| sources | 374 | definition, table | Métadonnée |
| depot | 353 | tag | Métadonnée |
| etre | 353 | table, tag, titre | Terme générique |
| statut | 331 | tag | Champ Sceau |
| vers | 314 | titre | Préposition |
| verdict | 313 | definition, table | Vocabulaire de gouvernance |

**Appariements** :

| Source | Paires |
|---|---|
| Rang 1 (`apparie`, attesté par la fiche) | 118 |
| Rang 2 (`jurjani`, Kitāb al-Taʿrīfāt) | 132 |
| Réciproques Jurjānī | 84 |
| Traditions ratifiées | 42 |
| Traditions posées (fiche-propre) | 310 |
| Fiches à tradition divergente | 5 |
| Langue posée (forme-appariée) | 48 |
| Langue posée (prose) | 4 |

---

## II. Forces

### F1 — Architecture en deux régimes

La séparation circuits (récolte structurelle, wikilinks) / textes (occurrence
nue, chemins nus) est exactement ce que CLAUDE.md §II prescrit. 657 textes
balayés sans qu'aucun ne devienne cible de lien : la règle d'immuabilité est
respectée mécaniquement, pas par discipline humaine.

### F2 — Dépendance unidirectionnelle vers le contrôleur

Le générateur importe `est_ecriture_originale` de `verifier-invariants.py`
(racine). Le validateur importe `fichiers_suivis` et `normaliser` du
générateur. Zéro définition dupliquée. Le sens est correct : l'outil dépend du
contrôleur, jamais l'inverse. L'absence du contrôleur est un REFUS franc,
jamais un repli silencieux.

### F3 — Marques combinantes (correctif 2026-09-08)

Construites par catégorie Unicode (Mn/Mc), jamais à la main. 3 043 clés
recollées, 2 578 fragments résorbés, zéro clé latine altérée. Le contraste
trompeur « arabe 469 clés / devanagari 0 » est résolu. Le français NFD
(`realisation` → `re` + `alisation`) est recollé sans effet de bord.

### F4 — Deux rangs d'appariement strictement séparés

`apparie` (rang 1, 118 paires, attesté par le texte de la fiche) et `jurjani`
(rang 2, 132 paires, avec numéro de définition). Le plancher Jurjānī (150) a
fonctionné : il a refusé l'injection quand l'extraction s'effondrait, avant
d'être relâché à 207 entrées mesurées. Deux rangs de crédibilité dans un même
champ seraient indistinguables — la séparation est tenue.

### F5 — Plancher de non-vacuité (D3)

Le générateur refuse un index vide ou un circuit sans fiche indexable. Le
validateur refuse un terme annoté absent de l'index, et va plus loin : il
détecte le trou du glossaire — l'entrée existe (par `tag`), mais la récolte
d'annotation n'a pas vu le HTML. La leçon de `glossaire-unifie.md` (« Termes
distincts : 0 » sans que rien ne s'en plaigne) est intégrée deux fois.

### F6 — Masquage du code avant recherche de balises

Le validateur masque le code inline et les blocs AVANT de chercher les
annotations. Une convention citée en prose (`<dfn data-terme ...>`) n'est plus
lue comme une annotation. La branche D4 « dans du code » a été retirée car
inatteignable — un contrôle qui ne peut pas se déclencher est la forme muette
que §VII interdit. Le masque préserve les longueurs, les offsets de D4
demeurent justes.

### F7 — Déclassement d'étiquettes

`SEUIL_ETIQUETTE = 10` déclasse les amorces `**Statut** :`, `**Source** :` qui
apparaissent dans trop de fiches. Quatre étiquettes déclassées mesurées :
contenu, pages couvertes, photos source, source. Le filtre `PART_CAPITALE =
0.60` écarte les termes de table qui ne sont pas majoritairement capitalisés —
un mot commun en table n'est presque jamais un nom propre.

### F8 — Réciprocité de l'index (§VII, point 6)

La clé latine porte sa forme originale et réciproquement, SEULEMENT sur
appariement attesté par le texte. Là où le dépôt se tait, le champ reste vide,
et la clé est déclarée orpheline plutôt que complétée. C'est la règle « établi
vs suggéré » appliquée au lexique.

---

## III. Problèmes

### P1 — Les 10 termes les plus indexés sont du bruit de gouvernance

« source » apparaît dans 504 fiches sur 758 — c'est un champ de Sceau, pas un
terme doctrinal. « sidy » est le propriétaire du dépôt. « deux » est un
numéral français. « vers » est une préposition.

Le filtre `ARRET` contient déjà 1 059 mots écartés, mais ces termes passent
parce qu'ils sont récoltés comme `table` ou `titre`, où la liste d'arrêt ne
s'applique pas pleinement (seuls `tag` et `annotation` y échappent par
design).

**Impact** : l'index paraît riche à 10 695 termes, mais sa tête est de la
métadonnée. Un chercheur qui tape « source » ne cherche pas un concept.

**Diagnostic** : le filtre `ARRET` est appliqué dans `Index.declarer()` mais
seulement quand `role not in ("tag", "annotation")`. Les rôles `table` et
`titre` laissent passer le bruit. Le correctif n'est pas d'ajouter ces mots à
`ARRET` — ce serait un jeu sans fin — mais de filtrer les termes dont le seul
rôle est `table` ET qui ne sont ni translittérés ni en écriture originale ET
qui ne figurent pas dans le slug de la fiche qui les porte.

### P2 — Longue traînante massive : 54 % des termes n'apparaissent qu'une fois

5 741 termes sur 10 695 ont exactement 1 fiche. La médiane de fiches par
terme est 1. L'index n'est pas un graphe : c'est un sac de mots-clés dont la
moitié ne relie rien.

Ce n'est pas une faute en soi — un index lexical a vocation à couvrir. Mais
combiné avec P1 (la tête est du bruit, la queue est unitaire), le
signal-à-bruit est bas. Les 1 313 termes à > 10 fiches et les 384 à > 50
fiches portent l'essentiel de la valeur.

**Recommandation** : ne pas supprimer ces termes (l'index dit *où chercher*),
mais le condensé MD fait déjà le bon choix en les masquant (seuls les termes à
≥ 2 fiches ou à rôle curé y figurent). Le JSON, lui, les garde pour l'outil
MCP.

### P3 — Récolte `table` : 3 320 termes, bruit de mise en page

La récolte en tables moissonne toute cellule courte dont la première lettre
est capitale. 3 320 termes en résultent — le deuxième rôle en volume. Une part
significative est du bruit de Sceau (tables de frontmatter avec `**Statut** :
actif`, `**Source** : ...`).

Le filtre `PART_CAPITALE` écarte les termes majoritairement en minuscule, mais
les champs de Sceau sont capitalisés (`Source`, `Statut`, `Type`). Ils
passent.

### P4 — Annotations HTML : phase 2 embryonnaire

400 termes sur 10 695 (3,7 %) portent le rôle `annotation`. 934 annotations
posées sur 321 fiches. Le dispositif est prêt (le validateur est propre, D1–D6
tous éprouvés), mais la matière n'est pas annotée.

L'index repose à 96 % sur la récolte structurelle. C'est attendu — la phase 2
est un chantier de fond, fiche par fiche — mais c'est un écart entre
l'ambition du dispositif et sa réalité actuelle.

### P5 — Le JSON fait 4,2 Mo

Pour un serveur MCP qui charge l'index à chaque requête (`_charger_index()`
dans `wiki_mcp_server.py`), 4,2 Mo de JSON à désérialiser par appel est un
coût non négligeable. La sérialisation interns les chemins (de 17 Mo à ~4 Mo),
ce qui est bien. Mais la croissance est linéaire : si le dépôt double, le JSON
double.

### P6 — Le générateur est un monolithe de 1 216 lignes

Cinq types de récolte, deux rangs d'appariement, détection de langue,
détection de tradition, trois formats de sortie — tout dans un fichier. Le
code est bien commenté et les responsabilités sont lisibles, mais :

- Toute modification de la récolte `titre` touche le même fichier que le
  formatage de sortie éclaté.
- Le validateur importe le générateur comme module (`_generateur()`), ce qui
  crée un couplage fort : si le générateur casse, le validateur casse aussi.
- Le fichier dépasse le seuil où un relecteur humain garde la carte mentale
  complète.

### P7 — Traditions divergentes : 5 fiches signalées, non résolues

Le rapport signale 5 fiches où la tradition posée diverge de la tradition
ratifiée. Exemple : `genealogie des idees` → `universel` alors que la
tradition ratifiée dit autre chose. C'est un signalement honnête, mais il n'y
a pas de mécanisme de résolution : la divergence reste dans le JSON, visible
mais non traitée.

### P8 — `RE_APPARIEMENT` ne couvre que les formes entre parenthèses

Le motif cherche `Terme (écriture)` ou `Terme (Langue : écriture)`. 118 paires
sur 10 695 termes, c'est peu. Beaucoup de fiches utilisent d'autres
conventions — guillemets, italiques simples, juxtaposition — qui ne sont pas
récoltées. Le choix est délibéré (§VII, règle 3 : établi vs suggéré), mais le
champ `apparie` reste largement vide. La langue posée par prose (4 termes)
montre que le dépôt énonce la langue, mais rarement dans la forme que le motif
attend.

---

## IV. Proposition de modularisation

### Diagnostic structurel

Le générateur actuel fait **cinq choses** dans un seul fichier de 1 216 lignes :

1. **Récolte** (5 types : tag, translit, definition, annotation, titre) —
   fonctions `recolter()`, `recolter_titre()`, ~100 lignes
2. **Comptage d'occurrences** (passe 2, circuits + textes) — `compter()`,
   ~50 lignes
3. **Appariements** (rang 1 : fiche, rang 2 : Jurjānī) — `apparier()`,
   `apparier_jurjani()`, `charger_jurjani()`, ~80 lignes
4. **Enrichissement sémantique** (tradition, langue) — `tradition_par_terme()`,
   `langue_par_terme()`, `langue_de_lecriture()`, ~150 lignes
5. **Sérialisation et rendu** (JSON, MD condensé, MD éclaté) — `serialiser()`,
   `rendre_md()`, `rendre_md_eclate()`, ~200 lignes

Plus le socle partagé : `Index`, `normaliser()`, `fichiers_suivis()`,
`filtrer_etiquettes()`, `controler()`, `refus()`, constantes et regex — ~400
lignes.

### Découpage proposé

```
atelier/rd/outillage/index-lexical/
├── __init__.py                  # exports publics
├── socle.py                     # socle partagé (générateur + validateur)
├── recolte.py                   # passe 1 : récolte du vocabulaire
├── occurrences.py               # passe 2 : comptage
├── appariement.py               # rang 1 (fiche) + rang 2 (Jurjānī)
├── semantique.py                # tradition + langue par terme
├── rendu.py                     # JSON, MD condensé, MD éclaté
├── generer-index-lexical.py     # orchestrateur (main), ~60 lignes
├── valider-annotations.py       # inchangé, importe socle + recolte
├── traditions-ratifiees.json    # inchangé
├── index-lexical.json           # sortie
├── index-lexical.md             # sortie
└── condense/                    # sortie éclatée
```

### Contenu de chaque module

**`socle.py`** (~180 lignes) — Ce que le générateur ET le validateur
partagent :

- `Index` (classe, avec `entree()`, `declarer()`, `apparier()`)
- `normaliser()`, `est_translittere()`
- `fichiers_suivis()`, `vendorise()`, `retenir()`
- `lire_frontmatter()`, `extraire_tags()`, `corps_sans_frontmatter()`
- `slug_de()`
- `_invariants()` (import de `verifier-invariants.py`)
- `est_ecriture_originale` (ré-export)
- Toutes les constantes : `CIRCUITS`, `ARRET`, `FRANCAIS`, `MIN_LONGUEUR`,
  `CELLULE_COURTE`, `PART_CAPITALE`, `SEUIL_ETIQUETTE`, `EXCLUS`, `VENDOR`
- Toutes les regex partagées : `RE_MOT`, `RE_DEFINITION`, `RE_DFN`, `RE_NOM`,
  `RE_ABBR`, `RE_CODE`, `RE_LIGNE_TABLE`, `RE_SEPARATEUR`, `RE_PREFIXE_DATE`

**`recolte.py`** (~120 lignes) — Passe 1 uniquement :

- `recolter()` (boucle sur les circuits, récolte les 5 types)
- `recolter_titre()` (tête de titre, portes d'admission)
- `filtrer_etiquettes()` (déclassement des amorces-champ)
- Regex propres : `RE_H1`, `RE_H2`, `RE_TETE_TITRE`, `RE_APPARIEMENT`

**`occurrences.py`** (~60 lignes) — Passe 2 uniquement :

- `compter()` (balayage circuits + textes, simples + phrases)

**`appariement.py`** (~100 lignes) — Les deux rangs :

- `charger_jurjani()` (lecture des fiches sources, plancher)
- `apparier_jurjani()` (pose le champ `jurjani`, réciprocité)
- Regex et constantes propres : `RE_JURJANI`, `SOURCES_JURJANI`,
  `PLANCHER_JURJANI`

**`semantique.py`** (~150 lignes) — Enrichissement :

- `tradition_par_terme()` (fiche-propre, definition, ratifiées, divergence)
- `langue_par_terme()`, `langue_de_lecriture()` (trois sources, jamais
  d'heuristique)
- Constantes propres : `ECRITURES_LANGUE`, `LANGUES_NOMMEES`,
  `RE_LANGUE_PROSE`, `GOUVERNANCE`

**`rendu.py`** (~200 lignes) — Sérialisation et formats :

- `serialiser()` (JSON avec internement des chemins)
- `rendre_md()` (condensé d'un seul tenant)
- `rendre_md_eclate()` (hub + un fichier par initiale)
- Constante propre : `SEUIL_ENUMERATION`

**`generer-index-lexical.py`** (~60 lignes) — Orchestrateur pur :

```python
def main():
    args = parser.parse_args()
    racine, rapport, suivis = initialiser(args)
    index = Index()
    recolter(racine, index, rapport, suivis)
    filtrer_etiquettes(index, rapport)
    tradition_par_terme(racine, index, rapport)
    langue_par_terme(racine, index, rapport)
    apparier_jurjani(index, racine, rapport)
    compter(racine, index, rapport, avec_textes, suivis)
    controler(index, rapport, avec_textes)
    data = serialiser(index, rapport, avec_textes)
    ecrire_sorties(data, args)
```

### Effet sur le validateur

Le validateur importe aujourd'hui le générateur entier :

```python
gen = _generateur()  # charge generer-index-lexical.py comme module
```

Après modularisation, il n'importe que `socle` :

```python
from socle import normaliser, fichiers_suivis, RE_CODE
```

Le couplage est réduit : une modification de `recolte.py` ou `rendu.py` ne
casse plus le validateur. Seule une modification de `socle.py` le peut — et
c'est voulu, puisque le validateur partage la définition de « même terme » et
« matière du dépôt ».

### Règles de découpage

1. **Aucune regex n'est dupliquée.** Elle vit dans le module qui l'emploie, ou
   dans `socle.py` si deux modules la partagent.
2. **Aucune constante n'est dupliquée.** Même règle.
3. **Le validateur n'importe jamais `recolte`, `occurrences`, `appariement`,
   `semantique` ou `rendu`.** Son seul point d'entrée dans le code partagé est
   `socle.py`.
4. **L'orchestrateur (`main`) ne contient aucune logique.** Il appelle les
   fonctions dans l'ordre, écrit les sorties, imprime le résumé.
5. **Les imports sont explicites.** Pas de `from module import *`. Chaque
   fonction importée est nommée.

### Gain mesuré

| Avant | Après |
|---|---|
| 1 fichier de 1 216 lignes | 7 fichiers de 60–200 lignes |
| Validateur couplé au générateur entier | Validateur couplé à `socle.py` seul |
| Modification de récolte touche le rendu | Modules indépendants |
| Relecture humaine : 1 216 lignes d'un tenant | Relecture par module, ~150 lignes max |

### Risques

- **`__pycache__`** : l'import de modules crée des `.pyc`. Le dépôt doit
  ajouter `__pycache__/` au `.gitignore` (il y est déjà via `VENDOR`, mais
  les fichiers `.pyc` individuels doivent être exclus).
- **Régression silencieuse** : le découpage peut introduire des erreurs
  d'import ou de portée. La mesure de contrôle est de comparer le JSON
  produit avant et après : il doit être byte-identique (hors horodatage).
- **Le validateur charge `socle.py`** : si `socle.py` importe
  `verifier-invariants.py` et que celui-ci est absent, le validateur échoue
  au chargement, pas à l'exécution. C'est le comportement voulu (REFUS
  franc), mais le message d'erreur doit être clair.

---

## V. Priorités proposées

| # | Action | Effort | Effet |
|---|---|---|---|
| 1 | Nettoyer la tête de l'index (P1) — filtrer les termes dont le seul rôle est `table` ET qui ne sont ni translittérés ni en écriture originale | Moyen | Signal-à-bruit |
| 2 | Modulariser le générateur (P6, §IV) | Moyen | Maintenabilité |
| 3 | Laisser la phase 2 annotations mûrir (P4) | Aucun | — |
| 4 | Cache du JSON dans le serveur MCP (P5) | Faible | Performance |

---

## VI. Clôture

Le système d'index lexical est le composant le plus rigoureux de l'outillage
du dépôt. Chaque refus (D1–D6, planchers, étiquettes déclassées) a été
éprouvé, documenté, et le validateur passe vert. La discipline des deux
régimes, des deux rangs d'appariement, et de la dépendance unidirectionnelle
vers le contrôleur est tenue sans exception.

Le diagnostic est le même que pour le dépôt entier : la rigueur du cadre
surpasse la maturité de la matière. Les annotations HTML sont prêtes mais
quasi absentes. Les traditions divergentes sont signalées mais non résolues.
Les 10 695 termes paraissent riches, mais la tête est du bruit de
gouvernance et la queue est unitaire.

Ce n'est pas une faute — c'est l'état d'un chantier vivant. Les priorités
ci-dessus resserrent le signal, découpent le monolithe, et laissent la phase
2 suivre son cours.
