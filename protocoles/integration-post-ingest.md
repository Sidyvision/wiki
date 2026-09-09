# Procédure d'intégration post-ingest (pédagogique)

> **Rattachement** : `CLAUDE.md`, §IX, *Procédure d'intégration post-ingest*. Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

Trame de référence — chaque notion réexpliquée jusqu'à maîtrise confirmée :

1. **Télécharger** les fichiers produits côté PRODUCTION (pages + `UPDATES.md`).
2. **Transférer au sas `_inbox/`** (Working Copy/SFTP, ou dépôt Obsidian + push puis
   `git pull` côté serveur).
3. **Ouvrir la session d'intégration** (Termius → serveur → outil CLI).
4. **Donner la consigne** : « Intègre les fichiers de l'ingest selon UPDATES.md et
   CLAUDE.md » (ou consigne séquencée fiche par fiche selon `MASTER-UPDATE.md`).
5. **Relire chaque écriture proposée** (jamais d'auto-accept), puis `git diff --stat`
   avant commit.
6. **Commit & push** : `git add -A && git commit -m "ARCHIVAGE: <sujet>" && git push`.
7. **Vérification mécanique** (`compare`/VIGILANCE), puis contrôle dans Obsidian
   (auto-pull).
8. Le sas `_inbox/` est vidé après intégration validée.
