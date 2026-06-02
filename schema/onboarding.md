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
| Obsidian Git    | ✅ Configuré (auto-pull)   | Pull automatique activé — voir section ci-dessous       |

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

## Synchronisation Obsidian : ✅ résolue (auto-pull activé)

### Historique

Obsidian sur iPad ne recevait pas automatiquement les mises à jour quand Claude Code modifiait des fichiers et faisait un `git push` : il fallait déclencher un `Git: Pull` **manuellement** après chaque push.

### Résolution (2026-06-02)

La synchronisation automatique est désormais activée dans Obsidian Git :

- Paramètres → Obsidian Git → « Pull updates on startup » → **activé**
- Paramètres → Obsidian Git → « Auto pull interval » → **réglé**

Obsidian récupère donc seul les changements poussés par Claude Code, sans `Git: Pull` manuel.

### Workflow courant

1. Claude Code modifie les fichiers et fait `git push`
2. Obsidian (iPad) pull automatiquement (au démarrage + à intervalle régulier)
3. Les fichiers apparaissent sans action manuelle

> En cas de doute (changement attendu non visible), un `Git: Pull` manuel via la palette de commandes reste possible pour forcer la synchro.

---

## Comment démarrer une session Claude Code

Dans Termius, connectez-vous au serveur puis lancez simplement :

```bash
claude
```

✅ La clé API est désormais persistée dans `~/.bashrc` — plus besoin de la retaper à chaque session.

### Clé API persistée (2026-06-02)

La clé est définie en bas de `~/.bashrc` :

```bash
export ANTHROPIC_API_KEY='sk-ant-...'
```

Elle se charge automatiquement à chaque shell interactif (sessions Termius).

Historique : les tentatives précédentes avaient laissé **plusieurs lignes `export` cassées** dans `~/.bashrc` (espace après `=`, clé coupée sur plusieurs lignes, caractères `l`→`1` / `O`→`0` introduits par le clavier iPad). Les lignes fautives s'annulaient entre elles → la clé n'était jamais chargée. Nettoyé le 2026-06-02 pour ne conserver qu'une seule ligne correcte (entre quotes simples).

> Note clavier iPad : pour toute future édition de la clé, attention aux substitutions `l`↔`1` et `O`↔`0`, et toujours entourer la valeur de quotes simples sans espace après `=`.

---

## Coffre Obsidian

- Nom du coffre : **Wiki**
- Contenu : clone du repo GitHub
- Fichiers dupliqués à la racine (CLAUDE, index, log, overview) — importés manuellement au début, peuvent être supprimés

---

## Prochaines étapes suggérées

1. ~~Régler la sauvegarde permanente de la clé API~~ ✅ fait le 2026-06-02
2. ~~Activer le pull automatique dans Obsidian Git~~ ✅ fait le 2026-06-02
3. Alimenter `raw/` avec les premières sources
4. Lancer le premier INGEST

---

## Notes techniques

- SSH configuré : clé `~/.ssh/id_ed25519` liée au compte GitHub Sidyvision
- Git configuré : `user.name = sidyvision`, `user.email = 5q7spz6b8v@privaterelay.appleid.com`
- Branche : `main`
- Remote : `git@github.com:Sidyvision/wiki.git`
