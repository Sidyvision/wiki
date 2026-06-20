# `_inbox/` — Sas d'entrée des ingests (à classer)

Dépose ici **tous** les fichiers `.md` produits par l'app iPad (Claude.ai) en attente
d'intégration. C'est le quai de déchargement du contenu produit, comme `raw/` l'est
pour les PDF bruts.

## Workflow

1. **App iPad** : produit les pages `.md` (et, idéalement, un `UPDATES.md` décrivant le
   classement souhaité). Dépose le tout dans ce dossier, puis **commit + push** via
   Obsidian Git.
2. **Claude Code (serveur)** : `git pull`, puis range chaque page dans son circuit
   (`doctrinal/…`, `atelier/…`, `meta/…`, ou `doctrinal/discernement/…`), répare le
   frontmatter, applique l'`UPDATES.md`, met à jour `index.md` et `annales.md`, lance
   VIGILANCE, commit/push, puis **vide ce dossier**.

## Règles

- Ne classe rien à la main : laisse Claude Code router selon le `type:` du frontmatter
  et les règles de `meta/briefing-claude-ai.md`.
- S'il existe un `UPDATES.md`, dépose-le aussi — il fait foi pour le classement.
- Ce dossier doit rester **vide** entre deux ingests (seul ce `README.md` y demeure).
- Rien ici n'est canonique : tant qu'un fichier est dans `_inbox/`, il n'est pas intégré.
