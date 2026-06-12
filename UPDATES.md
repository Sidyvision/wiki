# UPDATES — Restauration du protocole (CLAUDE.md révisé), 2026-06-12

> Consignes pour la session Claude Code (`/root/wiki`). Applique dans l’ordre.

## 1. Remplacement du protocole

- Écrase `/root/wiki/CLAUDE.md` par le nouveau fichier `CLAUDE.md` fourni dans ce lot.

## 2. Création de l’arborescence atelier

```bash
mkdir -p atelier/materiel atelier/entretiens atelier/projets doctrinal/sources
```

## 3. Bannissement du mot « réforme » (vocabulaire de la Restauration)

Remplacer dans les fichiers suivants (sans toucher au reste du contenu) :

- `doctrinal/annales.md` : « Réforme structurelle complète » → « Restauration structurelle complète » ; toute autre occurrence de « réforme/Réforme » → « restauration/Restauration ».
- `doctrinal/index.md` : vérifier et corriger toute occurrence.
- `meta/protocole-archivage-claude-ai.md` : « réformé le 2026-06-11 (réforme “Guénon V1”) » → « restauré le 2026-06-11 (Restauration “Guénon V1”) » ; idem partout.
- `meta/ingest-brief.md` : « refondue le 2026-06-11 après la réforme doctrinale » → « …après la Restauration doctrinale » ; idem partout.
- `MIGRATION.md` (s’il subsiste) : déplacer vers `meta/migration-2026-06-11.md` et renommer le titre en « Protocole de Restauration Traditionnelle du Wiki » (document d’archive, ne plus exécuter).

## 4. Mise à jour du Catalogue (`doctrinal/index.md`)

- Ajouter une section **VI. L’Atelier (hors doctrine)** avec trois sous-listes vides : Matériel, Entretiens, Projets (à renseigner au fil des archivages).
- Vérifier que la section Domaine Réservé pointe vers `meta/` et non `doctrinal/autorites/sidy` : si `sidy.md` est encore dans `doctrinal/autorites/`, le déplacer vers `meta/sidy.md` (fiche personnelle, étanchéité §VI du nouveau CLAUDE.md) et corriger l’index. Signaler si des pages doctrinales le référencent.

## 5. Entrée pour les Annales (`doctrinal/annales.md`, en tête)

```markdown
## [2026-06-12] restauration | Révision du protocole CLAUDE.md
- **Opération** : RESTAURATION (protocole)
- **Modifié** : CLAUDE.md (workflow iPad/serveur documenté, circuit atelier + projets,
  doctrinal/sources/ ajouté, meta/ clarifié, Sceau Recteur enrichi du champ sources,
  procédure post-ingest pédagogique, vocabulaire « restauration »)
- **Créé** : atelier/{materiel,entretiens,projets}/, doctrinal/sources/
- **Notes** : le mot « réforme » est banni du dépôt ; MIGRATION.md archivé en meta/.
```

## 6. VIGILANCE puis commit

- Lancer une passe VIGILANCE rapide (liens morts, occurrences restantes de « réforme » : `grep -ri "réforme" --include="*.md" .`).
- Puis :

```bash
git add -A && git commit -m "RESTAURATION: protocole CLAUDE.md révisé (atelier, meta, workflow iPad)" && git push
```

## 7. À NE PAS faire maintenant

- Ne pas normaliser le frontmatter des anciennes pages (passe RESTAURATION dédiée, sur demande ultérieure).
- Ne pas toucher à `raw/`.
