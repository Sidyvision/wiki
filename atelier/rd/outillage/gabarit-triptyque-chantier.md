---
title: "Gabarit du triptyque de chantier — intent / spec / plan"
type: outillage
tags: [atelier, rd, outillage, gabarit, chantiers, methode]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/index]]"
---

# Gabarit du triptyque de chantier

> **Ce que cette pièce est.** Le modèle unique des trois fiches que reçoit un chantier
> d'ingénierie du pôle R&D lorsqu'il passe de *recensé* à *instruit* : `intent.md`
> (pourquoi), `spec.md` (quoi), `plan.md` (comment). Convention ouverte le 2026-09-01
> sur demande de Sidy, à la lecture du *AI-Native SDLC Playbook*.
>
> **Ce qu'elle n'est pas.** Ni une doctrine, ni une analogie d'assemblage. Le triptyque
> est une **convention d'ingénierie** et n'emprunte **aucun terme du lexique Sashimono**
> (§VII du protocole racine) — ce lexique est clos aux termes nouveaux sans fiche
> `discernement` préalable (Cmd 3). En particulier, `intent.md` **n'est pas** un
> *sumi-tsuke* : le *sumi-tsuke* désigne la fiche `discernement`, instrument doctrinal
> relevant du Cmd 12. Un chantier d'ingénierie ne tranche rien de doctrinal.

## 1. Périmètre — où le triptyque s'applique, où il ne s'applique pas

**Il s'applique** aux chantiers du pôle `atelier/rd/` qui produisent du logiciel :
identifiants `INS-` (Instrument), `INF-` (infrastructure et agents), `OUT-`
(outillage et scripts).

**Il ne s'applique pas** aux circuits documentaires — `doctrinal/`,
`hermeneutique/`, `label/`, `meta/`. Ceux-ci disposent déjà des instruments qui
remplissent la même fonction : le Sceau porte l'intention et la nature de la fiche,
la fiche `discernement` instruit la question ouverte, les annales tiennent le
« comment cela s'est fait ». Y greffer un triptyque produirait le doublon que le
Cmd 14 interdit — *ce qui est propre à un circuit ne vit que là, jamais deux fois,
jamais nulle part*.

Un chantier `BIB-`, `CAS-`, `PRO-` ou `DOC-` n'en reçoit pas d'office : ce sont des
chantiers de contenu ou de process. S'il en vient à comporter une part logicielle
réelle, cette part seule est instruite ici.

## 2. Rapport au Cmd 6 — pas de règle nouvelle

Le Cmd 6 pose : **« pas d'écriture sans plan validé »**. Pour un chantier
d'ingénierie du pôle `rd/`, **le `plan.md` visé par Sidy *est* le plan du Cmd 6**.
Le triptyque ne crée aucune obligation supplémentaire : il donne sa forme à une
obligation qui existait déjà et qui, jusqu'ici, se satisfaisait d'un échange en
session — donc sans trace consultable à froid.

Corollaire : tant qu'un `plan.md` n'est pas visé, aucun code n'est écrit pour ce
chantier.

## 3. Emplacement et nomenclature

Le triptyque vit **dans le domaine du chantier**, jamais dans un arbre parallèle :

```
atelier/rd/<domaine>/<id-en-minuscules>-<slug>/
├── intent.md
├── spec.md
└── plan.md
```

Exemple : `atelier/rd/instrument/ins-02-axe-unifie/intent.md`.

- Le dossier porte l'**ID stable** du registre, en minuscules ASCII (`ins-02`,
  `inf-13`) — la poignée greppable survit à tout changement de titre.
- Les trois fichiers portent des noms nus (`intent.md`, `spec.md`, `plan.md`) : le
  dossier les désambiguïse, et la forme reste celle du Playbook.
- Un chantier peut n'avoir qu'une ou deux jambes posées. Un `intent.md` seul est un
  état valide et fréquent : l'intention est écrite, la spécification ne l'est pas
  encore. **Un `plan.md` sans `spec.md` ne l'est pas** — on ne planifie pas ce qu'on
  n'a pas spécifié.

Le pointeur vers ce dossier est porté par la ligne du chantier dans
`atelier/rd/registre-chantiers.md`. Le registre **pointe, il n'absorbe pas** : aucun
contenu du triptyque n'y est recopié.

## 4. Le Sceau

Les trois fiches portent le Sceau atelier ordinaire (`atelier/CLAUDE.md`), avec le
champ optionnel `chantier:` qui les relie à leur ligne de registre :

```yaml
---
title: "INS-02 — mode « axe unifié » : intention"
type: projet          # projet (INS-) | infrastructure (INF-) | outillage (OUT-)
chantier: INS-02
tags: [atelier, rd, instrument, chantier, intent]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
---
```

Rappel du Cmd 8 : `created` est immuable, `updated` remonte à chaque édition de fond.
Rappel du Sceau atelier : `rd/` peut pointer vers `doctrinal/` **en sens unique** et
tout lien de ce type est signalé ; l'inverse reste interdit — aucune page doctrinale
ne mentionne jamais un chantier, l'Instrument inclus.

-----

## 5. Modèle — `intent.md` (pourquoi)

```markdown
# <ID> — <titre du chantier> : intention

## Le besoin
Ce qui manque aujourd'hui, constaté et non supposé. Un fait vérifiable, pas une
ambition. Si le constat vient d'un incident, d'un cahier ou d'une scrutation de
veille, le pointer.

## Qui le porte
Sidy, un agent de fonction, un dépositaire extérieur. Et pour qui l'on construit.

## Hors périmètre
Ce que ce chantier ne fera pas — la moitié la plus utile de la fiche. Chaque exclusion
avec sa raison en une ligne.

## Contraintes doctrinales
Les Commandements que ce chantier touche et ce qu'ils imposent concrètement ici.
Toute question qui relève du Cmd 12 est **nommée et renvoyée**, jamais tranchée
au passage par une décision technique.

## Le signe de réussite
À quoi l'on reconnaîtra que c'est fait. Observable, sinon ce n'est pas un signe.

## Ce qui reste ouvert
Les inconnues assumées à ce stade, chacune avec son destinataire : Sidy (verdict),
une source à trouver (`to-source`), ou une mesure à faire.
```

## 6. Modèle — `spec.md` (quoi)

```markdown
# <ID> — <titre du chantier> : spécification

## Comportement observable
Ce que la chose fait, vue du dehors. Pas d'implémentation ici : si une phrase nomme
une bibliothèque ou une fonction, elle appartient au `plan.md`.

## Données consommées / produites
Fichiers en entrée, artefacts en sortie, avec leurs chemins réels. Pour tout ce qui
touche l'Instrument ou le site : rappeler le sens unique `dépôt → manifeste →
interface` (§VII) — l'interface ne réécrit jamais le dépôt.

## Critères d'acceptation
Une liste numérotée, chaque ligne **vérifiable par une commande ou une observation
nommée**. « Le rendu est correct » n'est pas un critère ; « la page charge et le
`fetch` du manifeste frère résout » en est un.

## Cas limites
Donnée absente, valeur nulle, correspondance non établie. Rappel du §VII : ce qui
n'est pas sourcé s'affiche **suggéré** (pointillé + 🔍), jamais fondu avec l'établi.

## Ce qui reste `to-source`
Les marqueurs restants, avec la source primaire à atteindre pour les lever (Cmd 5).
```

## 7. Modèle — `plan.md` (comment)

```markdown
# <ID> — <titre du chantier> : plan

> **Statut** : `brouillon` | `vise` — seul un plan `vise` autorise l'écriture (Cmd 6).

## Étapes
Ordonnées, chacune assez petite pour être vérifiée seule. La ligne dit ce qui est
fait, pas ce qui est espéré.

## Fichiers touchés
Chemins réels, création ou modification. Ce qui est **copié** et ce qui est
**déplacé** est distingué : rien ne se supprime, un original devient `deprecated`
(Cmd 10).

## Vérification
Les commandes exactes qui prouvent chaque critère d'acceptation du `spec.md`. Un
contrôle qui n'observe rien de réel n'est pas une vérification — le contrôle qui
gardait `main` sans rien regarder (PRO-01, 2026-08-31) est le contre-exemple de
référence.

## Points de retour à l'humain
Ce qui, dans ce plan, engage (Cmd 13) : dépense, jeton d'accès, publication en
production, verdict doctrinal. Préparé par la machine, tranché par Sidy.

## Journalisation
Le circuit d'annales concerné et la ligne de registre à mettre à jour dans la même
passe (Cmd 9, et section *Entretien* du registre des chantiers).
```

-----

## 8. Ce que le triptyque ne dispense pas de faire

Il ne remplace ni la vérification structurelle de clôture
(`python3 verifier-invariants.py --racine /root/wiki`, §VII), ni l'entrée d'annales
avec son SHA court (Cmd 9), ni la mise à jour de la ligne de registre dans la même
passe. Il s'y greffe.
