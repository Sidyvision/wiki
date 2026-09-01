---
title: "INS-02 — mode « axe unifié » et champ echelle : spécification"
type: projet
chantier: INS-02
tags: [atelier, rd, instrument, chantier, spec]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/instrument/ins-02-axe-unifie/intent]]"
  - "[[atelier/rd/outillage/spec-generateur-manifeste]]"
---

# INS-02 — spécification

## Comportement observable

**A. Champ `echelle` sur les registres.** Chaque registre du manifeste porte un champ
`echelle` valant `macrocosmique`, `microcosmique`, `transcalaire`, ou **absent**.
L'absence est un état légitime et le défaut : elle signifie « non tranché par Sidy »,
jamais « inconnu du système ».

**B. Contrôle d'échelle à la génération.** Pour tout ancrage reliant deux registres
dont les échelles sont **toutes deux déclarées** et **franchement mono-échelle et
opposées** (`macrocosmique` × `microcosmique`), le générateur émet un
**avertissement** nommant l'ancrage et les deux registres. Il n'échoue pas, ne
supprime rien, ne requalifie aucun ancrage. Un registre `transcalaire` ou sans
échelle ne déclenche jamais rien.

**C. Mode de rendu commutable.** L'interface offre deux vues d'un même état :
*éclatée* (l'actuelle, défaut) et *axe unifié*, où les colonnes centrales de tous les
registres se rabattent sur l'axe vertical unique. La bascule est une transition
continue, non un rechargement, et **ne modifie aucune donnée** : mêmes nœuds, mêmes
ancrages, mêmes statuts établi/suggéré de part et d'autre.

## Données consommées / produites

| | Chemin |
|---|---|
| Source | `atelier/rd/instrument/instrument-donnees.yaml` (bloc `registres:`) |
| Producteur | `atelier/rd/outillage/generer-manifeste.py` (schéma v0.2.5 → v0.2.6) |
| Manifeste | `atelier/rd/instrument/wiki-manifest.json` |
| Consommateur | le rendu, dans le dépôt `Sidyvision/instrument` |

Sens unique `dépôt → manifeste → interface` (§VII). L'interface ne réécrit jamais le
dépôt : la bascule de vue est un état local d'affichage, rien n'en remonte.

## Critères d'acceptation

1. `instrument-donnees.yaml` accepte `echelle:` sur un registre ; une valeur hors
   des trois admises fait **échouer** la génération avec un message nommant le
   registre fautif (validation bloquante, §5 de la spec du générateur).
2. Le manifeste régénéré **sans aucune valeur `echelle` renseignée** est identique,
   au bit près hors `generated_at`/`source_commit`, au manifeste actuel — la
   rétrocompatibilité est prouvée, pas supposée.
3. Un ancrage `macrocosmique` × `microcosmique` fabriqué pour le test fait apparaître
   exactement un avertissement dans le rapport de génération, et le compteur
   d'avertissements passe de `0` à `1`.
4. Le même ancrage avec un registre `transcalaire` n'en produit aucun.
5. En vue *axe unifié*, la liste des ancrages affichés `etabli` est identique à celle
   de la vue *éclatée* — vérifiée par comparaison, non à l'œil.
6. La bascule aller-retour ramène l'affichage à son état initial.

## Cas limites

- **Registre sans `echelle`** : cas nominal, aucun avertissement, aucun style
  particulier. On ne signale pas visuellement une absence de verdict.
- **Ancrage `suggere` (🔍)** : soumis au même contrôle. Un ancrage suggéré qui viole
  l'échelle cumule les deux signalements, ils ne se substituent pas l'un à l'autre.
- **Registre vide de nœuds** en vue unifiée : ne laisse pas de colonne fantôme.

## Ce qui reste `to-source`

Rien de nouveau. Les trois marqueurs de la colonne *faṣṣ* relèvent de INS-12 et ne
sont pas touchés ici.
