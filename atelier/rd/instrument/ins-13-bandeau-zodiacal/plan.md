---
title: "INS-13 — bandeau zodiacal : plan"
type: projet
chantier: INS-13
tags: [atelier, rd, instrument, chantier, plan, zodiaque]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/instrument/ins-13-bandeau-zodiacal/spec]]"
---

# INS-13 — plan

> **Statut : `brouillon`.** Aucun code avant visa de Sidy (Cmd 6).

## Étapes

1. Relire `spec-anneau-zodiacal.md` §2 et suivants (géométrie) — la forme y est
   tranchée, ce plan ne la rediscute pas.
2. Vérifier dans `wiki-manifest.json` que le bloc zodiacal est complet et ordonné
   (le rapport de génération annonce déjà « zodiaque inclus, maisons incluses »).
3. Implémenter le rendu dans `src/index.html` du dépôt `Sidyvision/instrument`,
   alimenté par le seul manifeste.
4. Éprouver le critère 4 : renommer un *manzil* dans le bac à sable, régénérer,
   recharger, constater — puis **remettre la valeur d'origine**.
5. Revenir sur `spec-anneau-zodiacal.md` : ajouter un pointeur vers ce dossier de
   chantier (adoption par pointeur, §Nomenclature de `atelier/CLAUDE.md`).

## Fichiers touchés

| Fichier | Nature |
|---|---|
| `src/index.html` du dépôt `Sidyvision/instrument` | modification (le rendu) |
| `atelier/rd/instrument/spec-anneau-zodiacal.md` | modification (pointeur seul, contenu inchangé) |
| `atelier/rd/instrument/instrument-donnees.yaml` | **inchangé** — la donnée existe déjà |

## Vérification

- Critère 1 : `grep -iE 'belier|taureau|gemeaux|cancer|lion|vierge|balance|scorpion|sagittaire|capricorne|verseau|poissons' src/` → aucun résultat.
- Critères 3 et 6 : comptage programmatique sur le manifeste (28 *manāzil*, 23
  ancrages avant comme après).
- Critère 4 : la manipulation de l'étape 4, faite et rapportée, non asserée.
- `python3 verifier-invariants.py --racine /root/wiki` en clôture.

## Points de retour à l'humain (Cmd 13)

Le rendu produit est une proposition visuelle : Sidy le vise avant toute publication.
Précédent direct — INS-09 (rendu d'*al-Insān al-Kāmil*) est en `attente-verdict`
précisément pour ce motif.

## Journalisation

`atelier/annales.md` + ligne INS-13 du registre, même passe (Cmd 9).
