---
title: "Déploiement profil karubi — Isolation mémoire sub-agent"
type: infrastructure
tags: [rd, hermes, memoire, isolation, karubi]
created: 2026-08-23
updated: 2026-08-23
sources: []
links: []
---

# Déploiement profil karubi — Isolation mémoire sub-agent

## Contexte

**Problème identifié** : Le skill Karūbī-Hermes nécessite un sub-agent qui ne doit pas avoir accès à la mémoire principale (MEMORY.md/USER.md du profil gardien).

**Investigation code source Hermes v0.20.5** :
- Fichier `agent/agent_init.py` ligne 578 : paramètre `skip_memory` dans signature `_create_agent()`
- Fichier `agent/agent_init.py` lignes 1842-1871 : logique initialisation mémoire
- Fichier `tools/async_delegation.py` : sub-agents héritent configuration profil parent
- **Conclusion** : Pas de `memory_enabled` par sub-agent dans Hermes v0.20.5

**Solution recommandée** : Créer un profil dédié `karubi` avec `memory_enabled: false`

## Déploiement effectué

### 1. Création profil karubi

**Répertoire créé** : `/root/.hermes/profiles/karubi/`

### 2. Configuration

**Fichier** : `/root/.hermes/profiles/karubi/config.yaml`

```yaml
model:
  default: qwen3.8-max
  provider: custom:qwen

providers:
  custom:qwen:
    base_url: "http://localhost:8000/v1"
    api_key: "local"

memory:
  enabled: false
  user_profile_enabled: false
  injection_prompt: ""

agent:
  max_turns: 150
  reasoning_effort: low
```

**Paramètres clés** :
- `memory.enabled: false` : désactive chargement MEMORY.md
- `user_profile_enabled: false` : désactive chargement USER.md
- `injection_prompt: ""` : désactive injection mémoire dans prompt système
- `reasoning_effort: low` : optimisé pour tâches documentaires (pas de raisonnement complexe)

### 3. Fichiers mémoire

**USER.md** : `/root/.hermes/profiles/karubi/USER.md`

Contenu :
- Identité Karūbī (médiateur documentaire)
- Contexte (dépôt, profil isolé, accès lecture seule)
- 5 destinataires (Mehdi, Mikael, Habiba-Nour, Jean-Marc, Wendel)
- Règles spécifiques (aucune mémoire persistante, lecture seule, neutralité, adab)
- Concepts clés (Karūbī, sanad, zones scellées, zones de croissance, navette)
- Préférences (français, ton affectueux, protocole Karūbī)

**MEMORY.md** : non créé (volontairement, car `memory.enabled: false`)

### 4. Vérification

**Commande** :
```bash
for profile in /root/.hermes/profiles/*/; do
  name=$(basename "$profile")
  echo "=== $name ==="
  [ -f "$profile/USER.md" ] && echo "  USER.md: $(wc -c < "$profile/USER.md") bytes" || echo "  USER.md: MANQUANT"
  [ -f "$profile/MEMORY.md" ] && echo "  MEMORY.md: $(wc -c < "$profile/MEMORY.md") bytes" || echo "  MEMORY.md: MANQUANT"
done
```

**Résultat** :
```
=== karubi ===
  USER.md: 1570 bytes
  MEMORY.md: MANQUANT
```

**Statut** : ✓ Profil karubi déployé avec isolation mémoire (USER.md présent, MEMORY.md absent volontairement)

## Fonctionnement

### Invocation sub-agent Karūbī

**Avant** (profil gardien avec mémoire) :
```bash
hermes --profile gardien chat --message "Invoquer sub-agent Karūbī pour Mehdi"
```
→ Sub-agent hérite mémoire gardien (MEMORY.md + USER.md)

**Après** (profil karubi isolé) :
```bash
hermes --profile karubi chat --message "Invoquer sub-agent Karūbī pour Mehdi"
```
→ Sub-agent sans mémoire (aucun chargement MEMORY.md/USER.md)

### Cas d'usage

**Scénario 1 : Navette retour Mehdi**
```bash
# Invoquer sub-agent Karūbī pour traiter navette Mehdi
hermes --profile karubi chat --message "Traiter navette Mehdi dans _inbox/"
```
→ Sub-agent lit `meta/transmissions/karubi-mehdi.md`
→ Sub-agent traite §8 (Mémoire vivante) et §9 (Questions)
→ Sub-agent ne conserve rien (profil isolé)
→ Sidy reprend la main pour §10 (Réponses)

**Scénario 2 : Accompagnement destinataire**
```bash
# Invoquer sub-agent Karūbī pour accompagner Mikael
hermes --profile karubi chat --message "Accompagner Mikael dans appropriation protocole"
```
→ Sub-agent présente état travaux Sidy (§4)
→ Sub-agent accompagne Mikael dans construction protocole (§6)
→ Sub-agent recueille souvenirs Mikael (§8)
→ Sub-agent ne conserve rien (profil isolé)

**Scénario 3 : Intégration navette automatisée**
```bash
# Script déterministe (aucun LLM)
python3 /root/wiki/meta/transmissions/integrer-navette-karubi.py
```
→ Vérifie sceau
→ Compare zones scellées
→ Extrait ajouts §8/§9
→ Archive navette
→ Journalise dans registre-silsila.md
→ Aucun sub-agent Karūbī nécessaire (script déterministe)

## Avantages

1. **Isolation totale** : sub-agent Karūbī ne peut pas accéder mémoire profil gardien
2. **Propre** : configuration standard Hermes, pas de workaround fragile
3. **Maintenable** : profil dédié, configuration explicite
4. **Évolutif** : si PR #34098 Hermes mergée, migration facile

## Inconvénients

1. **Gestion supplémentaire** : profil séparé à maintenir
2. **Invocation explicite** : doit utiliser `--profile karubi` pour sub-agent Karūbī
3. **Pas de mémoire** : sub-agent ne conserve rien entre sessions (volontaire, mais limite continuité)

## Migration depuis profil gardien

**Avant** :
```bash
# Sub-agent Karūbī invoqué depuis profil gardien
hermes --profile gardien chat --message "Invoquer sub-agent Karūbī"
```

**Après** :
```bash
# Sub-agent Karūbī invoqué depuis profil karubi
hermes --profile karubi chat --message "Invoquer sub-agent Karūbī"
```

**Documentation à mettre à jour** :
- `meta/CLAUDE.md` : section Karūbī, préciser invocation profil karubi
- `meta/transmissions/karubi-gabarit.md` : section invocation sub-agent
- `atelier/rd/infrastructure/2026-08-23_memoire-persistante-deploiement.md` : section isolation mémoire

## Tests à effectuer

1. **Test invocation** :
   ```bash
   hermes --profile karubi chat --message "Test invocation sub-agent Karūbī"
   ```
   → Vérifier que sub-agent démarre sans erreur
   → Vérifier que sub-agent ne charge pas MEMORY.md/USER.md

2. **Test isolation** :
   ```bash
   hermes --profile karubi chat --message "Peux-tu accéder à la mémoire du profil gardien ?"
   ```
   → Sub-agent doit répondre "Non, je suis isolé"

3. **Test navette** :
   ```bash
   # Placer navette test dans _inbox/
   # Invoquer sub-agent Karūbī
   hermes --profile karubi chat --message "Traiter navette test dans _inbox/"
   ```
   → Sub-agent doit traiter navette sans erreur
   → Vérifier que sub-agent ne conserve rien

## Prochaines étapes

1. **Documenter** : mettre à jour `meta/CLAUDE.md` et `karubi-gabarit.md`
2. **Tester** : effectuer les 3 tests ci-dessus
3. **Valider** : confirmer isolation mémoire avec Sidy
4. **Déployer** : utiliser profil karubi pour invocations sub-agent Karūbī

## Références

- Investigation isolation mémoire : `atelier/rd/outillage/investigation-isolation-memoire-hermes.md`
- PR #34098 Hermes : https://github.com/NousResearch/hermes-agent/pull/34098
- Code source Hermes : `/usr/local/lib/hermes-agent/agent/agent_init.py` (lignes 578, 1842-1871)
- Skill Karūbī-Hermes : `meta/projet-unifie/hermes-skills/spec-skill-karubi-hermes.md`

---

**Statut** : ✓ Profil karubi déployé, en attente tests et validation Sidy

**Date** : 2026-08-23

**Auteur** : Hermes Agent (profil default)
