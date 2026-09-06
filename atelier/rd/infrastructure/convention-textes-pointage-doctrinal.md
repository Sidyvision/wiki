---
title: "Convention — Pointage des textes convertis depuis doctrinal/sources/"
type: infrastructure
status: adopte
created: 2026-09-06
updated: 2026-09-06
sources: []
tags: [textes, convention, pointage, doctrinal, sources]
---

# Convention — Pointage des textes convertis depuis doctrinal/sources/

## Contexte

`textes/` est un dossier de premier niveau (§II) qui contient des **sources primaires converties** en Markdown. Il n'est **pas un circuit** : il ne porte aucun Sceau, n'entre dans aucun régime de liens (§VI), et les fichiers qu'il contient n'ont pas de frontmatter doctrinal.

Les fiches `doctrinal/sources/` décrivent ces sources primaires et portent le Sceau Recteur. Elles peuvent vouloir référencer le texte converti correspondant dans `textes/`.

## Le problème

§VI interdit les liens depuis `doctrinal/` vers des dossiers hors circuit. Pourtant, les fiches doctrinales ont besoin de pointer vers les textes convertis pour :
- Permettre la vérification des citations
- Faciliter la consultation depuis Obsidian
- Maintenir la traçabilité entre la fiche doctrinale et sa source primaire

## La convention

### 1. Le champ `texte_converti` dans le frontmatter

Une fiche `doctrinal/sources/` qui correspond à un texte dans `textes/` **peut** inclure un champ optionnel `texte_converti:` dans son frontmatter :

```yaml
---
title: "Le Symbolisme de la Croix"
type: source
status: traditionnel
tradition_cadre: "universel"
sources: []
sources_count: 0
texte_converti: "[[textes/le-symbolisme-de-la-croix]]"
---
```

Ce champ :
- N'est **pas** un wikilink au sens de §VI (il n'est pas dans `sources:` ni `cross_links:`)
- Est un **pointeur documentaire** vers un fichier dans `textes/`
- N'est **pas** contrôlé par `verifier-invariants.py` (pas de validation de résolution)
- Ne crée **pas** d'arête dans le graphe de cartographie

### 2. Syntaxe du pointeur

Le pointeur utilise la syntaxe wikilink standard `[[chemin/vers/dossier]]` où :
- Le chemin est relatif à la racine du dépôt
- Il pointe vers un **dossier** dans `textes/`, pas vers un fichier individuel
- Exemple : `[[textes/le-symbolisme-de-la-croix]]` pointe vers le dossier `textes/le-symbolisme-de-la-croix/`

### 3. Pas de pointeur inverse

Les fichiers dans `textes/` **ne doivent jamais** contenir de lien vers `doctrinal/`. La règle d'immuabilité de `textes/` s'applique : un texte converti ne s'enrichit pas de liens doctrinaux.

### 4. Le corps de la fiche peut référencer le texte

Le corps d'une fiche `doctrinal/sources/` peut contenir des mentions du texte converti, par exemple :

```markdown
## Accès au texte

Le texte converti est disponible dans `[[textes/le-symbolisme-de-la-croix]]`.
Chapitre pertinent : `chapitre-03-la-croix-dans-les-traditions-anciennes.md`.
```

Ces mentions dans le corps :
- Sont des **aides à la navigation** pour le lecteur
- Ne créent **pas** d'arête dans le graphe (le graphe ne parse que le frontmatter)
- Ne violent **pas** §VI car elles sont dans le corps, pas dans le frontmatter

### 5. Pas de validation mécanique

Contrairement aux champs `sources:` et `cross_links:`, le champ `texte_converti:` n'est **pas** validé par `verifier-invariants.py` :
- Pas de contrôle de résolution (le fichier cible peut exister ou non)
- Pas de contrôle de format (la syntaxe est libre)
- Pas de contrôle d'étanchéité (§VI ne s'applique pas à ce champ)

La responsabilité de maintenir des pointeurs valides incombe à l'agent qui crée ou modifie la fiche.

### 6. Pas de compteur

Le champ `texte_converti:` n'a **pas** de compteur associé. Il est unique par fiche (un texte primaire = une fiche source).

## Exemples

### Exemple 1 : Fiche avec texte converti

Fiche : `doctrinal/sources/guenon-symbolisme-croix.md`
```yaml
---
title: "Le Symbolisme de la Croix"
type: source
status: traditionnel
tradition_cadre: "universel"
sources: []
sources_count: 0
texte_converti: "[[textes/le-symbolisme-de-la-croix]]"
---

# Le Symbolisme de la Croix

## Accès au texte

Le texte converti est disponible dans `[[textes/le-symbolisme-de-la-croix]]`.

## Résumé

...
```

### Exemple 2 : Fiche sans texte converti

Fiche : `doctrinal/sources/ibn-arabi-futuhat-ch36.md`
```yaml
---
title: "Futūḥāt al-Makkiyya — Chapitre 36"
type: source
status: traditionnel
tradition_cadre: "islam"
sources: []
sources_count: 0
---

# Futūḥāt al-Makkiyya — Chapitre 36

## Résumé

...
```

Pas de champ `texte_converti:` car le texte n'est pas converti dans `textes/`.

### Exemple 3 : Fiche avec texte converti partiel

Fiche : `doctrinal/sources/guenon-regne-quantite.md`
```yaml
---
title: "Le Règne de la Quantité et les Signes des Temps"
type: source
status: traditionnel
tradition_cadre: "universel"
sources: []
sources_count: 0
texte_converti: "[[textes/le-regne-de-la-quantite]]"
---

# Le Règne de la Quantité et les Signes des Temps

## Accès au texte

Le texte converti est disponible dans `[[textes/le-regne-de-la-quantite]]`.
Chapitres pertinents :
- `chapitre-01-aspects-divers-tradition-orthodoxie.md`
- `chapitre-07-la-descente-qualitative-ou-l-obscurcissement.md`

## Résumé

...
```

## Justification

Cette convention respecte :
- **§II** : `textes/` reste un dossier de premier niveau, pas un circuit
- **§VI** : le pointeur n'est pas dans `sources:` ni `cross_links:`, donc pas soumis à l'étanchéité
- **§VII** : la validation est manuelle, pas mécanique (pas de faux positifs)
- **Cmd 10** : pas de suppression de fichiers, pas de modification de `textes/`
- **Cmd 13** : la convention est réversible (supprimer le champ `texte_converti:` suffit)

## Ce qui n'est pas couvert

- Les fichiers individuels dans `textes/` : le pointeur vise un **dossier**, pas un fichier
- Les textes dans `raw/` : cette convention ne s'applique qu'à `textes/`
- Les liens depuis d'autres circuits que `doctrinal/sources/` : seul ce type de fiche peut utiliser `texte_converti:`

## Évolution

Cette convention peut évoluer si :
- Un besoin de pointage depuis d'autres circuits émerge (à discuter)
- La validation mécanique devient nécessaire (ajouter un contrôle dans `verifier-invariants.py`)
- La syntaxe doit être étendue (ex. pointer vers un fichier individuel)

Pour l'instant, elle couvre le cas d'usage immédiat : permettre aux fiches doctrinales de référencer leurs textes convertis sans violer l'architecture du dépôt.
