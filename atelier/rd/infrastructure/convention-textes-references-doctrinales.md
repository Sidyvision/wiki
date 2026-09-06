---
title: "Convention — Référence aux textes convertis depuis les fiches doctrinales"
type: infrastructure
created: 2026-09-06
updated: 2026-09-06
sources: []
tags: [textes, convention, references, doctrinal, protocole]
---

# Convention — Référence aux textes convertis depuis les fiches doctrinales

## Contexte

Le dossier `textes/` contient des sources primaires converties en Markdown (chantier PRO-08). Il n'est **pas un circuit** et n'entre pas dans le régime des liens wikilinks (§VI du protocole racine).

Cependant, les fiches `doctrinal/sources/` ont besoin de référencer ces textes pour :
- Indiquer l'emplacement de la source convertie
- Permettre la consultation depuis Obsidian
- Maintenir la traçabilité entre la fiche doctrinale et sa source

## Règle générale

**Pas de wikilink `[[textes/...]]`** depuis les fiches doctrinales. `textes/` n'est pas un circuit, il ne fait pas partie du graphe de navigation.

## Convention de référence

### Dans le frontmatter

Utiliser le champ `texte_converti:` (optionnel) pour indiquer le chemin relatif :

```yaml
---
title: "Exemple de fiche source"
type: source
status: traditionnel
tradition_cadre: "islam"
sources: []
sources_count: 0
texte_converti: "textes/mon-texte/mon-texte.md"
cross_links: []
---
```

### Dans le corps de la fiche

Mentionner le texte converti en texte clair avec le chemin entre backticks :

```markdown
## Accès au texte

Le texte converti est disponible dans `textes/mon-texte/mon-texte.md`.
Consultation : Obsidian (post CONSULTATION) ou terminal.
```

### Exemple concret

Fiche `doctrinal/sources/shayegan-disciplines-spirituelles.md` :

```yaml
---
title: "Shayegan — Les Disciplines Spirituelles (ch. II de Hindouisme et Soufisme)"
type: source
status: academique
tradition_cadre: "islam"
sources: []
sources_count: 0
texte_converti: "textes/les-disciplines-spirituelles-daryush-shayegan/les-disciplines-spirituelles.md"
cross_links: []
---

# Shayegan — Les Disciplines Spirituelles

## Accès au texte

Le texte converti est disponible dans `textes/les-disciplines-spirituelles-daryush-shayegan/les-disciplines-spirituelles.md`.
Consultation : Obsidian (post CONSULTATION) ou terminal.

## Résumé

...
```

## Pourquoi cette convention

1. **Respect du protocole** : pas de wikilinks vers `textes/` (pas un circuit)
2. **Traçabilité** : le chemin est indiqué, consultable manuellement
3. **Consultation Obsidian** : le chemin relatif permet d'ouvrir le fichier depuis Obsidian (copier-coller ou navigation manuelle)
4. **Graphe propre** : le graphe de cartographie ne mélange pas circuits et dossiers techniques

## Cas particuliers

### Texte brut dans `raw/`

Si la source n'est pas convertie (PDF, scan), indiquer dans `sources:` :

```yaml
sources:
  - "raw/mon-document.pdf"
```

### Texte dans `_inbox/`

Si la source est en attente d'intégration, indiquer :

```yaml
sources:
  - "_inbox/mon-texte.md (en attente d'intégration)"
```

## Vérification

Le script `verifier-invariants.py` ne contrôle pas les champs `texte_converti:` ni les chemins dans le corps. La vérification est manuelle (cohérence entre la fiche et l'emplacement réel).

## Historique

- **2026-09-06** : Convention créée pour traiter les suggestions Publication (4 derniers jours). Résout le problème des fiches doctrinales devant référencer des textes dans `textes/` sans violer §VI.
