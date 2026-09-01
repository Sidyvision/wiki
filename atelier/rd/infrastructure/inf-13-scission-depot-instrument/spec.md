---
title: "INF-13 — scission du dépôt Instrument : spécification"
type: infrastructure
chantier: INF-13
tags: [atelier, rd, infrastructure, chantier, spec, instrument, git]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-13-scission-depot-instrument/intent]]"
---

# INF-13 — spécification

## Comportement observable

Deux dépôts, une seule source de vérité.

- **`Sidyvision/wiki`** — la source. Porte la donnée, le producteur, la doctrine, les
  chantiers. Inchangé dans sa nature.
- **`Sidyvision/instrument`** — l'interface. Privé. Porte le rendu et **une copie
  reçue** du manifeste. N'a aucun accès en écriture au wiki, et n'en a pas besoin.

Le manifeste circule dans un seul sens, **poussé depuis le wiki**, jamais tiré par
l'interface. Ce choix n'est pas cosmétique : un dépôt destiné à devenir public ne
doit à aucun moment détenir de droit de lecture sur un dépôt privé.

## La ligne de coupe

| Part vers `instrument` | Reste dans `wiki` |
|---|---|
| `instrument-prototype.html` → `src/index.html` | Architecture v0.1 / v0.2 / v0.3, jalons, mises en regard |
| Le code de rendu à venir | `instrument-donnees.yaml` — la donnée source |
| Une copie reçue de `wiki-manifest.json` | `generer-manifeste.py` — le producteur |
| Sa CI de build et de déploiement | `assets-instrument/` — copie canonique |
| | Les triptyques `ins-*/` et les lignes `INS-` du registre |

**Vérifiée, non supposée.** Le prototype ne porte aucun `src=` ni `href=` : zéro
référence à `assets-instrument/`. Ses deux seules dépendances externes sont Three.js
r128 via `cdnjs.cloudflare.com` (ligne 1865) et `fetch('wiki-manifest.json')`
(ligne 164), **chemin relatif frère**. D'où une contrainte dure sur la disposition du
nouveau dépôt : `src/index.html` et `src/wiki-manifest.json` sont **côte à côte**.
La migration déplace, elle ne modifie pas — pas de dossier `data/` séparé qui
obligerait à retoucher le code migré au moment même où on le déplace.

## Critères d'acceptation

1. `gh api repos/Sidyvision/instrument` renvoie `"private": true`.
2. ~~`gh api repos/Sidyvision/instrument/branches/main/protection` renvoie une
   protection active avec `enforce_admins.enabled: true`.~~ **Critère amendé le
   2026-09-01, à l'exécution.** GitHub réserve la protection de branche — et les
   *rulesets* — aux dépôts **publics** ou aux plans payants : l'API répond `403,
   Upgrade to GitHub Pro or make this repository public` sur les deux. Le critère
   était donc irréalisable **en même temps** que le choix « privé d'abord », et il
   est remplacé, non abandonné :
   **`hooks/pre-commit` est versionné dans le dépôt frère et installé.** Il refuse
   (a) les caractères Unicode invisibles (Cmd 15), (b) une modification de
   `src/wiki-manifest.json` non déclarée comme publication (`MANIFESTE_RECU=1`),
   (c) la séparation du rendu et de son manifeste frère.
   Ce n'est pas un pis-aller improvisé : **le wiki avait déjà tranché ce cas** au
   chantier PRO-01 le 2026-09-01 — `enforce_admins: false` acté, garde-fou local
   préféré à un flux par pull request imposé à Sidy et aux douze agents. La doctrine
   du dépôt est donc appliquée, non contournée. La bascule en public (Cmd 13,
   réservée à Sidy) rendrait la protection serveur disponible : c'est un argument
   pour cette bascule, ce n'en est pas la décision.
3. `src/index.html` servi localement charge, et son `fetch` du manifeste frère
   résout — la coupe tient en fait, pas seulement sur le papier.
4. Le wiki conserve `instrument-prototype.html` en stub `deprecated` pointant vers le
   nouveau dépôt ; rien n'est supprimé (Cmd 10).
5. `CLAUDE.md` racine et `atelier/CLAUDE.md` nomment le dépôt frère et la ligne de
   coupe : le wiki n'est muet nulle part (Cmd 14).
6. Le `CLAUDE.md` du nouveau dépôt énonce sa subordination doctrinale au wiki.
7. `publier-manifeste-instrument.sh` régénère, compare, et **n'écrit rien** quand le
   contenu n'a pas changé — les tampons `generated_at` et `source_commit` ne sont pas
   des changements de fond et ne doivent pas déclencher de publication.
8. Aucun jeton, aucun secret GitHub n'est créé dans cette passe (Cmd 13).

## Cas limites

- **Manifeste divergent au moment de la scission** : rapporté, pas régénéré d'office
  (Cmd 12). *Constat de la passe du 2026-09-01 : la divergence portait uniquement sur
  `generated_at` et `source_commit` — 46 nœuds, 23 ancrages, 0 avertissement,
  contenu identique. Le manifeste versionné était à jour sur le fond.*
- **Le dépôt frère devient public** : le stub du wiki pointe vers une URL qui doit
  rester valable ; c'est le seul lien à revérifier lors de la bascule.
- **Le dépôt frère bascule en public** : la protection serveur de `main` devient
  alors disponible et doit être posée, `enforce_admins` compris — le garde-fou local
  ne la remplace pas, il la précède.
- **Le prototype évolue au-dehors** : le wiki ne le suit pas et n'a pas à le suivre.
  Seule l'architecture, qui reste ici, fait foi sur le *quoi*.

## Ce qui reste `to-source`

Rien — chantier d'infrastructure, sans assertion doctrinale.
