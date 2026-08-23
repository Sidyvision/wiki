---
title: Spécification SRS Hermes-native — format et implémentation
type: meta
statut: brouillon
created: 2026-08-23
updated: 2026-08-23
sources: []
links:
- '[[atelier/rd/outillage/2026-08-15_piste-srs-assimilation-protocole]]'
---

# Spécification SRS Hermes-native — format et implémentation

## Contexte

Le verdict Sidy du 2026-08-15 a décidé l'intégration Hermes-native du SRS (pas d'outil tiers comme Mnemosyne ou Anki). Les cartes seront auto-générées depuis CLAUDE.md et stockées dans la mémoire Hermes.

Cette fiche spécifie le format des cartes, le mécanisme d'extraction, et l'algorithme d'espacement.

## Format de carte

### Structure YAML

Chaque carte est stockée comme une entrée dans MEMORY.md ou un fichier dédié `~/.hermes/profiles/<profile>/srs-cards.yaml`.

```yaml
- id: "cmd-01"
  question: "Quel est le commandement absolu numéro 1 ?"
  reponse: "Une session = une fonction. Pas de mélange de rôles dans une même session."
  categorie: "commandement"
  source: "CLAUDE.md#cmd1"
  created: "2026-08-23"
  last_reviewed: null
  next_review: "2026-08-24"
  interval_days: 1
  ease_factor: 2.5
  repetitions: 0
  tags: ["fondamental", "session"]
```

### Champs requis

- **id** : identifiant unique (ex: `cmd-01`, `sashimono-03`, `etancheite-07`)
- **question** : texte de la question (court, clair)
- **reponse** : texte de la réponse (précis, vérifiable)
- **categorie** : regroupement thématique (commandement, sashimono, etancheite, karubi, etc.)
- **source** : référence au fichier/section d'origine
- **created** : date de création de la carte
- **last_reviewed** : date de dernière révision (null si jamais révisée)
- **next_review** : date de prochaine révision (calculée par algorithme)
- **interval_days** : intervalle en jours avant prochaine révision
- **ease_factor** : facteur de facilité SM-2 (2.5 par défaut)
- **repetitions** : nombre de révisions réussies consécutives
- **tags** : étiquettes pour filtrage/recherche

## Mécanisme d'extraction

### Script generer-cartes-protocole.py

Le script lit CLAUDE.md et extrait automatiquement les éléments éligibles au SRS.

#### Règles d'extraction

1. **Commandements absolus (Cmd 1-13)** :
   - Pattern : lignes commençant par `- Cmd N :` ou `**Cmd N**`
   - Extraction : titre + description
   - Format question : "Quel est le commandement N ?"
   - Format réponse : texte complet du commandement

2. **Interdits de liens (étanchéité)** :
   - Pattern : sections mentionnant "jamais", "interdit", "sens unique"
   - Extraction : circuit source + circuit cible interdit
   - Format question : "Quel circuit ne peut jamais pointer vers quel circuit ?"
   - Format réponse : "doctrinal ne pointe jamais vers hermeneutique"

3. **Convention Sashimono (lexique)** :
   - Pattern : termes en italique ou gras avec définition
   - Extraction : terme + définition
   - Format question : "Que signifie le terme X ?"
   - Format réponse : définition complète

4. **Table Karūbī ↔ destinataire** :
   - Pattern : table markdown avec colonnes "destinataire" et "nom_karubi"
   - Extraction : chaque ligne de la table
   - Format question : "Quel est le nom Karūbī pour X ?"
   - Format réponse : nom_karubi correspondant

5. **Vocabulaire technique** :
   - Pattern : termes techniques définis dans le texte (navette, canonique, zones scellées, etc.)
   - Extraction : terme + définition contextuelle
   - Format question : "Que signifie X dans le contexte du dépôt ?"
   - Format réponse : définition

#### Pseudo-code

```python
def extraire_commandements(claude_md):
    cartes = []
    for i in range(1, 14):
        pattern = rf"Cmd\s+{i}\s*[:\-]\s*(.+)"
        match = re.search(pattern, claude_md)
        if match:
            cartes.append({
                "id": f"cmd-{i:02d}",
                "question": f"Quel est le commandement {i} ?",
                "reponse": match.group(1).strip(),
                "categorie": "commandement",
                "source": "CLAUDE.md"
            })
    return cartes

def extraire_interdits_liens(claude_md):
    cartes = []
    # Pattern : "doctrinal ne pointe jamais vers hermeneutique"
    pattern = r"(\w+)\s+(?:ne\s+)?point(?:e)?(?:\s+jamais)?\s+vers\s+(\w+)"
    for match in re.finditer(pattern, claude_md):
        source, cible = match.groups()
        cartes.append({
            "id": f"etancheite-{len(cartes)+1:02d}",
            "question": f"Quel circuit ne peut jamais pointer vers {cible} ?",
            "reponse": f"{source} ne pointe jamais vers {cible}",
            "categorie": "etancheite",
            "source": "CLAUDE.md"
        })
    return cartes

# Similar functions for sashimono, karubi, vocabulaire...
```

## Algorithme d'espacement

### SM-2 simplifié

L'algorithme SM-2 ajuste l'intervalle et le facteur de facilité en fonction de la performance de l'utilisateur.

#### Paramètres

- **q** : qualité de la réponse (0-5)
  - 0 : blackout total
  - 1 : presque correct
  - 2 : difficile, mais correct
  - 3 : correct avec effort
  - 4 : correct, facile
  - 5 : parfait, instantané

#### Calcul

```python
def sm2(card, q):
    """
    Algorithme SM-2 simplifié.
    
    Args:
        card: dict avec interval_days, ease_factor, repetitions
        q: qualité de réponse (0-5)
    
    Returns:
        dict mis à jour avec nouveaux interval_days, ease_factor, repetitions
    """
    if q < 3:
        # Réponse incorrecte ou difficile : reset
        card["repetitions"] = 0
        card["interval_days"] = 1
    else:
        # Réponse correcte
        if card["repetitions"] == 0:
            card["interval_days"] = 1
        elif card["repetitions"] == 1:
            card["interval_days"] = 6
        else:
            card["interval_days"] = round(card["interval_days"] * card["ease_factor"])
        
        card["repetitions"] += 1
    
    # Mise à jour du facteur de facilité
    card["ease_factor"] = max(
        1.3,
        card["ease_factor"] + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    )
    
    # Calcul de next_review
    card["last_reviewed"] = date.today().isoformat()
    card["next_review"] = (date.today() + timedelta(days=card["interval_days"])).isoformat()
    
    return card
```

### Stratégie de révision

#### Sessions de révision

1. **Révision quotidienne** : cron Hermes à 09:00 UTC (11:00 Paris)
2. **Nombre de cartes par session** : 5-10 cartes (configurable)
3. **Sélection** : cartes dont `next_review <= today`, triées par `ease_factor` ascendant (les plus difficiles d'abord)

#### Mécanisme d'interaction

**Option A : Cron avec rapport**
- Cron génère un rapport des cartes à réviser
- Sidy répond dans Discord/Telegram avec les réponses
- Script parse les réponses et met à jour les cartes

**Option B : Commande interactive**
- Commande `hermes srs review` lance une session interactive
- L'agent pose les questions une par une
- Sidy répond, l'agent met à jour les cartes en temps réel

**Option C : Injection prompt**
- Au début de chaque session, l'agent injecte 2-3 cartes dans le prompt
- Sidy répond spontanément
- L'agent met à jour les cartes en fin de session

**Recommandation** : Option B (commande interactive) pour la flexibilité, avec Option C en complément pour la révision passive.

## Stockage

### Fichier srs-cards.yaml

```yaml
# ~/.hermes/profiles/default/srs-cards.yaml
cards:
  - id: "cmd-01"
    question: "Quel est le commandement absolu numéro 1 ?"
    reponse: "Une session = une fonction. Pas de mélange de rôles dans une même session."
    categorie: "commandement"
    source: "CLAUDE.md#cmd1"
    created: "2026-08-23"
    last_reviewed: "2026-08-23"
    next_review: "2026-08-24"
    interval_days: 1
    ease_factor: 2.5
    repetitions: 1
    tags: ["fondamental", "session"]
  
  - id: "cmd-02"
    # ...
```

### Intégration MEMORY.md

Les cartes peuvent aussi être injectées dans MEMORY.md pour rappel passif :

```markdown
## Révisions SRS en cours

- **cmd-01** (next: 2026-08-24) : Une session = une fonction
- **sashimono-03** (next: 2026-08-25) : hozo = tenon-mortaise, portance structurelle
```

## Plan d'implémentation

### Phase 1 : Extraction (1-2 heures)
1. Écrire `generer-cartes-protocole.py`
2. Tester sur CLAUDE.md
3. Valider les cartes extraites avec Sidy

### Phase 2 : Stockage (30 min)
1. Créer structure `srs-cards.yaml`
2. Écrire fonctions de lecture/écriture YAML

### Phase 3 : Algorithme (1 heure)
1. Implémenter SM-2
2. Tester avec des réponses simulées
3. Valider les calculs d'intervalle

### Phase 4 : Interface (2-3 heures)
1. Écrire commande `hermes srs review`
2. Implémenter interaction questions/réponses
3. Intégrer mise à jour cartes

### Phase 5 : Cron (30 min)
1. Créer cron quotidien 09:00 UTC
2. Générer rapport des cartes à réviser
3. Optionnel : parse réponses Discord/Telegram

## Verdicts Sidy requis

1. **Format carte** : YAML dans `srs-cards.yaml` ou injection dans MEMORY.md ?
2. **Algorithme** : SM-2 simplifié ou variante ?
3. **Interface** : commande interactive, cron avec rapport, ou injection prompt ?
4. **Fréquence** : quotidienne, hebdomadaire, ou adaptative ?
5. **Nombre de cartes par session** : 5, 10, ou variable ?

## Estimation

- **Nombre total de cartes** : ~80-120 (estimation fiche piste)
- **Temps de révision quotidien** : 5-10 minutes (5-10 cartes)
- **Temps d'implémentation** : 5-7 heures (Phases 1-5)

## Risques

1. **Surcharge cognitive** : trop de cartes par session → frustration
2. **Perte de contexte** : cartes trop isolées → manque de cohérence
3. **Maintenance** : cartes obsolètes si CLAUDE.md évolue sans régénération

## Mitigations

1. **Limiter à 5-10 cartes par session**
2. **Regrouper par catégorie** (commandements, sashimono, etc.)
3. **Régénérer cartes après chaque modification CLAUDE.md**
4. **Archiver cartes obsolètes plutôt que supprimer**
