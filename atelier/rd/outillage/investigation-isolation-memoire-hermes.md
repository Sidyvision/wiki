---
title: Investigation — Isolation mémoire Hermes par sub-agent
type: meta
statut: investigué
tags:
  - hermes
  - memory
  - sub-agent
  - bloquant
  - karubi
created: 2026-08-23
updated: 2026-08-23
---

# Investigation — Isolation mémoire Hermes par sub-agent

## Problème initial

Le skill Karūbī-Hermes nécessite un sub-agent qui ne doit **pas** avoir accès à la mémoire principale de Hermes (MEMORY.md/USER.md du profil gardien). Actuellement, tous les sub-agents créés via `delegate_task` héritent de la mémoire du profil parent.

## Investigation technique

### Code source Hermes v0.20.5

**Fichier** : `/usr/local/lib/hermes-agent/agent/agent_init.py`

**Ligne 578** : Le paramètre `skip_memory` est défini dans la signature de `_create_agent()`.

**Lignes 1842-1871** : Logique d'initialisation mémoire :
```python
if not skip_memory or _memory_toolset_requested:
    # Charge MEMORY.md et USER.md
    agent._memory_enabled, agent._user_profile_enabled = get_builtin_memory_store_flags(...)
    if agent._memory_enabled or agent._user_profile_enabled:
        # Initialise MemoryManager
        memory_manager = MemoryManager(...)
```

**Conclusion** : `skip_memory` est un paramètre global de l'agent, pas une configuration par sub-agent.

### delegate_task

**Fichier** : `/usr/local/lib/hermes-agent/tools/async_delegation.py`

**Fonction** : `dispatch_async_delegation()` crée un sub-agent pour exécuter une tâche isolée.

**Observation** : Le sub-agent hérite de la configuration du profil parent, y compris `memory_enabled: true`. Il n'y a **pas de paramètre** pour désactiver la mémoire spécifiquement pour un sub-agent.

### Solution proposée : PR #34098

**URL** : https://github.com/NousResearch/hermes-agent/pull/34098

**Statut** : PR ouverte, pas encore mergée dans v0.20.5

**Contenu** : Ajoute un paramètre `memory_enabled` dans la configuration des cron jobs, qui peut être réutilisé pour les sub-agents.

**Limitation** : Même si mergée, cette solution nécessite une mise à jour de Hermes et une modification du code de `delegate_task` pour exposer ce paramètre.

## Solutions pratiques

### Solution A : Profil dédié pour Karūbī (recommandée)

**Concept** : Créer un profil Hermes dédié `karubi` qui n'a pas de MEMORY.md/USER.md.

**Implémentation** :
```bash
# Créer le profil
hermes profile create karubi

# Configurer sans mémoire
cat > /root/.hermes/profiles/karubi/config.yaml << EOF
model: qwen3.8-max
provider: qwen
memory:
  memory_enabled: false
  user_profile_enabled: false
EOF

# Ne pas créer MEMORY.md ni USER.md dans ce profil
```

**Avantages** :
- Isolation totale de la mémoire
- Pas besoin de modifier le code Hermes
- Solution immédiate et testable

**Inconvénients** :
- Nécessite un profil séparé (gestion supplémentaire)
- Le sub-agent Karūbī doit être invoqué via ce profil spécifique

### Solution B : Workaround via fichier temporaire

**Concept** : Avant d'invoquer le sub-agent Karūbī, déplacer temporairement MEMORY.md/USER.md hors du profil gardien.

**Implémentation** :
```bash
# Avant invocation sub-agent
mv /root/.hermes/profiles/gardien/MEMORY.md /tmp/MEMORY.md.bak
mv /root/.hermes/profiles/gardien/USER.md /tmp/USER.md.bak

# Invoquer sub-agent Karūbī
# ... (exécution)

# Après invocation, restaurer
mv /tmp/MEMORY.md.bak /root/.hermes/profiles/gardien/MEMORY.md
mv /tmp/USER.md.bak /root/.hermes/profiles/gardien/USER.md
```

**Avantages** :
- Pas de modification de configuration
- Solution temporaire rapide

**Inconvénients** :
- Fragile (risque d'oubli de restauration)
- Nécessite un wrapper script
- Pas une solution propre

### Solution C : Attendre PR #34098

**Concept** : Attendre que la PR soit mergée et mettre à jour Hermes.

**Timeline estimée** :
- PR review : 1-2 semaines (estimation)
- Merge : 1 semaine après review
- Mise à jour Hermes : immédiate après merge

**Avantages** :
- Solution propre et officielle
- Intégrée dans le code Hermes

**Inconvénients** :
- Délai d'attente (2-4 semaines)
- Dépend de l'équipe Hermes

### Solution D : Modification manuelle du code Hermes (NON RECOMMANDÉE)

**Concept** : Modifier directement `/usr/local/lib/hermes-agent/tools/async_delegation.py` pour ajouter un paramètre `skip_memory` dans `dispatch_async_delegation()`.

**Risque** :
- Perte de la modification à la prochaine mise à jour Hermes
- Potentielle instabilité
- Non supporté officiellement

**Statut** : ÉCARTÉ

## Recommandation

**Solution A (profil dédié) recommandée** pour les raisons suivantes :

1. **Immédiate** : peut être implémentée aujourd'hui
2. **Propre** : pas de workaround fragile
3. **Maintenable** : configuration standard Hermes
4. **Évolutive** : si PR #34098 est mergée, migration facile

**Implémentation** :
1. Créer profil `karubi` avec `memory_enabled: false`
2. Modifier le script d'invocation Karūbī pour utiliser ce profil
3. Tester avec un cas simple (navette retour)
4. Valider avec Sidy

## Prochaines étapes

1. **Créer profil karubi** : `hermes profile create karubi`
2. **Configurer** : `memory_enabled: false`, `user_profile_enabled: false`
3. **Tester** : invoquer sub-agent Karūbī via ce profil
4. **Valider** : vérifier que MEMORY.md/USER.md ne sont pas chargés
5. **Intégrer** : modifier les scripts d'invocation Karūbī

## Notes techniques

- Le profil `karubi` peut être créé même si Hermes v0.20.5 n'a pas de commande `hermes profile create`. Création manuelle du répertoire `/root/.hermes/profiles/karubi/` suffit.
- La configuration `memory_enabled: false` doit être explicitement définie dans `config.yaml` du profil.
- Les autres profils (gardien, studio, etc.) restent inchangés avec `memory_enabled: true`.

## Références

- PR #34098 : https://github.com/NousResearch/hermes-agent/pull/34098
- Documentation Hermes : https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Code source : `/usr/local/lib/hermes-agent/agent/agent_init.py` (lignes 578, 1842-1871)
- Skill Karūbī-Hermes : `/root/wiki/meta/projet-unifie/hermes-skills/spec-skill-karubi-hermes.md`
