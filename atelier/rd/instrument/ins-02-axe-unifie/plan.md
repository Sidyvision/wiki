---
title: "INS-02 — mode « axe unifié » et champ echelle : plan"
type: projet
chantier: INS-02
tags: [atelier, rd, instrument, chantier, plan]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/instrument/ins-02-axe-unifie/spec]]"
---

# INS-02 — plan

> **Statut : `brouillon`.** Aucun code n'est écrit pour ce chantier tant que Sidy n'a
> pas visé ce plan (Cmd 6 — pour un chantier `rd/`, ce fichier *est* le plan du Cmd 6).

## Étapes

1. **Verdict d'abord.** Soumettre à Sidy la table d'attribution des échelles (§4.2 de
   la fiche du 2026-08-30) et la question avertir/bloquer. Sans verdict, seules les
   étapes 2 et 3 sont exécutables — le champ existe, il reste vide.
2. Ouvrir `echelle` dans `instrument-donnees.yaml` (bloc `registres:`), sans le
   renseigner.
3. `generer-manifeste.py` : lire le champ, valider l'énumération (échec bloquant sur
   valeur inconnue), le propager au manifeste, passer le schéma en v0.2.6.
4. Contrôle d'échelle sur les ancrages : avertissement seul, dans le compteur
   existant du rapport de génération.
5. Renseigner les valeurs **une fois le verdict rendu**, jamais avant.
6. Côté rendu (dépôt `instrument`) : mode commutable, transition continue, état
   d'affichage local.

## Fichiers touchés

| Fichier | Nature |
|---|---|
| `atelier/rd/instrument/instrument-donnees.yaml` | modification (champ ouvert) |
| `atelier/rd/outillage/generer-manifeste.py` | modification (lecture, validation, contrôle) |
| `atelier/rd/outillage/spec-generateur-manifeste.md` | modification (§5, validations) |
| `atelier/rd/instrument/wiki-manifest.json` | **régénéré**, jamais édité à la main |
| `src/index.html` du dépôt `Sidyvision/instrument` | modification (étape 6) |

## Vérification

- Critère 2 (rétrocompatibilité) : régénérer vers une sortie temporaire et
  `diff` contre le manifeste versionné, en ignorant `generated_at` et
  `source_commit` — les deux seuls champs qui bougent légitimement à chaque passe.
- Critères 3 et 4 : ancrage de test **dans un bac à sable**, jamais dans
  `instrument-donnees.yaml` (le générateur accepte `--repo` sur un bac à sable).
- Critère 5 : comparer les deux listes d'ancrages `etabli` programmatiquement.
- Puis `python3 verifier-invariants.py --racine /root/wiki`.

## Points de retour à l'humain (Cmd 13)

- La table d'attribution des échelles — **bloquant pour l'étape 5**.
- Avertir ou bloquer sur incompatibilité d'échelle.
- Le passage de schéma v0.2.5 → v0.2.6 (tout consommateur du manifeste en dépend).

## Journalisation

`atelier/annales.md` (Cmd 9, SHA court en dernière ligne) et la ligne INS-02 de
`atelier/rd/registre-chantiers.md`, **dans la même passe**.
