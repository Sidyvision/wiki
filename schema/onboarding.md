---
title: Onboarding — État du Wiki
type: meta
updated: 2026-06-02
---

# Onboarding — État du Wiki au 2026-06-02

## Contexte

Wiki personnel en français, maintenu par Claude Code sur un serveur Hetzner.
Accès via Termius (iPad). Navigation via Obsidian (iPad).

---

## Infrastructure en place

| Composant       | État                      | Détails                                                 |
|-----------------|---------------------------|---------------------------------------------------------|
| Serveur Hetzner | ✅ Opérationnel           | IP : 178.105.125.156                                    |
| Claude Code     | ✅ Installé               | v2.1.150, dossier `~/wiki`                              |
| GitHub          | ✅ Connecté               | `git@github.com:Sidyvision/wiki.git` (SSH)              |
| Obsidian Git    | ⚠️ Partiellement configuré | Voir problème ci-dessous                                |

---

## Structure du wiki sur le serveur

```
~/wiki/
├── CLAUDE.md              ← schéma opérationnel (à lire en premier)
├── README.md
├── raw/                   ← sources brutes (vide pour l'instant)
│   └── assets/
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── overview.md
│   ├── sources/
│   ├── entities/
│   ├── concepts/
│   ├── analyses/
│   └── logs/
└── schema/
    └── onboarding.md      ← ce fichier
```

---

## Problème en cours : Obsidian pas dans la boucle

### Symptôme

Obsidian sur iPad ne reçoit pas automatiquement les mises à jour quand Claude Code modifie des fichiers et fait un `git push`.

### Ce qui a été fait

- Obsidian Git (plugin) installé dans Obsidian
- Token GitHub configuré dans Obsidian Git
- Nom et email auteur configurés (Sidyvision)
- Clone du repo effectué via `Git: Clone an existing remote repo`
- Un `Git: Pull` manuel a fonctionné une fois (« Everything is up-to-date »)

### Ce qui manque probablement

Le `Git: Pull` dans Obsidian doit être déclenché **manuellement** après chaque `git push` de Claude Code. Il n'y a pas de synchronisation automatique.

### Solution immédiate (workflow manuel)

1. Claude Code modifie les fichiers et fait `git push`
2. Dans Obsidian → Palette de commandes → `Git: Pull`
3. Les fichiers apparaissent dans Obsidian

### Solution idéale (à configurer)

Activer la synchronisation automatique dans Obsidian Git :

- Paramètres → Obsidian Git → « Pull updates on startup » → activer
- Paramètres → Obsidian Git → « Auto pull interval » → régler à 5 minutes

---

## Comment démarrer une session Claude Code

Dans Termius, connectez-vous au serveur puis tapez :

```bash
ANTHROPIC_API_KEY=votre-clé-api claude
```

⚠️ La clé API doit être entrée à chaque session (pas encore sauvegardée de façon permanente).

### Sauvegarder la clé API définitivement

Pour ne plus avoir à la retaper, exécuter dans le terminal Linux (pas dans Claude Code) :

```bash
echo 'export ANTHROPIC_API_KEY=votre-clé' >> ~/.bashrc && source ~/.bashrc
```

Note : les tentatives précédentes ont échoué à cause du clavier iPad qui ajoutait des caractères invalides. Essayer depuis le clavier physique ou via SSH depuis un autre appareil si possible.

---

## Coffre Obsidian

- Nom du coffre : **Wiki**
- Contenu : clone du repo GitHub
- Fichiers dupliqués à la racine (CLAUDE, index, log, overview) — importés manuellement au début, peuvent être supprimés

---

## Prochaines étapes suggérées

1. Régler la sauvegarde permanente de la clé API
2. Activer le pull automatique dans Obsidian Git
3. Alimenter `raw/` avec les premières sources
4. Lancer le premier INGEST

---

## Notes techniques

- SSH configuré : clé `~/.ssh/id_ed25519` liée au compte GitHub Sidyvision
- Git configuré : `user.name = sidyvision`, `user.email = 5q7spz6b8v@privaterelay.appleid.com`
- Branche : `main`
- Remote : `git@github.com:Sidyvision/wiki.git`
