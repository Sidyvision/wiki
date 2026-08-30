---
title: "Conversion des chemins nus en wikilinks — 142 occurrences (2026-08-30)"
type: outillage
created: 2026-08-30
updated: 2026-08-30
auteur: agent
statut: cloture
---

# Conversion des chemins nus en wikilinks

## Contexte

Le registre des problèmes ([2026-08-18]) signalait 142 chemins nus dans les champs de liens (sources, cross_links, liens, links). Ces chemins violaient la règle §IV du protocole : tous les liens internes doivent être au format `[[chemin]]`.

## Méthode

Script Python parcourant tous les fichiers .md du dépôt (hors raw/, _inbox/, .git) :
1. Extraction du frontmatter YAML
2. Pour chaque champ de liens, détection des chemins nus (contenant `/` mais pas `[[...]]`)
3. Conversion en wikilink : `chemin/vers/fiche` → `[[chemin/vers/fiche]]`
4. Préservation des cas légitimes :
   - URLs externes (http/https)
   - Chemins raw/ (fichiers bruts)
   - `to-source` (marqueur de source manquante)
5. Validation YAML post-conversion
6. Rejet des fichiers avec erreurs de parsing

## Problèmes rencontrés

### Itération 1 — Triple crochet (abandonnée)
Premier script modifiait le texte brut du frontmatter :
```python
ancien = f"- {chemin}"
nouveau = f'- "[[{chemin}]]"'
```
Résultat : `[[[chemin]]]` au lieu de `"[[chemin]]"`. YAML interprétait `[[[` comme une liste imbriquée, cassant 62 fichiers.

**Leçon** : Ne jamais modifier le texte YAML brut. Toujours parser → modifier → sérialiser.

### Itération 2 — Double enveloppe (corrigée)
Deuxième script utilisait `yaml.dump()` mais générait `[["[[chemin]]"]]` :
```python
nouvelle_liste.append(f'"[[{chemin}]]"')  # Erreur : guillemets dans la chaîne
```
YAML sérialisait : `- '[["[[chemin]]"]]'` au lieu de `- '[[chemin]]'`.

**Correction** : supprimer les guillemets internes, laisser YAML gérer l'échappement.

### Itération 3 — Succès
Script final :
```python
nouvelle_liste.append(f'[[{chemin}}]]')  # Correct : chaîne pure
```
YAML sérialise avec les bons échappements : `- '[[chemin]]'`

## Résultats

- **62 fichiers modifiés**
- **142 chemins nus convertis en wikilinks**
- **0 erreur YAML**
- **Vérificateur invariants** : 3 erreurs B0 (raw/, immuables) + 1 avertissement A6 connu
- **Générateur de graphe** : 1475 arêtes (1266 établies, 209 suggérées), 65 "liens morts" (URLs externes dans sources:, normal)

## Fichiers impactés

Principaux groupes :
- **atelier/projets/** : 13 fiches (projets GEM, Instrument, anneau zodiacal)
- **atelier/rd/** : 28 fiches (infrastructure, instrumentation, cahiers)
- **label/** : 10 fiches (distribution, production, direction artistique)
- **doctrinal/** : 8 fiches (symboles, discernements, sources)
- **hermeneutique/** : 2 fiches (20th century boys, lost)
- **meta/** : 1 fiche (brief incident ZWJ)

## Vérifications post-conversion

```bash
# Aucun chemin nu restant
python3 -c "..."  # Vérification : 0 chemin nu

# Aucun erreur YAML
python3 -c "..."  # Vérification : 0 erreur

# Vérificateur invariants
python3 verifier-invariants.py --racine /root/wiki
# Résultat : 3 erreurs B0 (raw/), 1 avertissement A6

# Générateur de graphe
python3 Graphe/generer-cartographie.py
# Résultat : 1475 arêtes, 65 liens morts (URLs externes)
```

## Leçons tirées

1. **Toujours parser → modifier → sérialiser** pour le YAML, jamais de manipulation textuelle brute
2. **Laisser le sérialiseur YAML gérer les échappements** (guillemets, apostrophes)
3. **Validation post-conversion** : vérifier YAML + vérifier intégrité du dépôt
4. **Itérations courtes** : tester sur 1 fichier avant de lancer sur 62

## Résolution du point 3a du registre

Le registre des problèmes ([2026-08-18]) point 3a est **résolu** :
- Option C appliquée (conversion par batch)
- 142 chemins nus → 142 wikilinks
- 0 chemin nu restant
- 0 régression

## Liens

- Registre des problèmes : [2026-08-18] point 3a
- Script de conversion : non conservé (usage unique)
- PR GitHub : en cours (à créer)
