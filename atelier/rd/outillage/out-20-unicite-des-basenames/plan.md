---
title: "OUT-20 — unicité des basenames, garde du wikilink court : plan"
type: outillage
chantier: OUT-20
tags: [atelier, rd, outillage, chantier, plan, wikilink, controle]
created: 2026-09-18
updated: 2026-09-18
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/out-20-unicite-des-basenames/spec]]"
---

# OUT-20 — unicité des basenames, garde du wikilink court : plan

> **Statut** : `brouillon` — seul un plan `vise` autorise l'écriture (Cmd 6). Rien de ce
> qui suit n'a été exécuté.

## Étapes

1. **Mesurer les deux questions laissées ouvertes**, avant toute ligne de code : (a)
   combien de collisions de basename existent aujourd'hui entre les cinq circuits, une
   fois les exemptions nommées retirées ; (b) combien entre un circuit et `textes/` ou
   `protocoles/`. Sortie brute rapportée à Sidy, sans conclusion.
2. **Rapporter à Sidy les deux verdicts attendus** : refus sec ou avertissement
   conditionné à l'existence d'un renvoi court ; périmètre avec ou sans `textes/` et
   `protocoles/`. Le code n'est pas écrit avant.
3. **Écrire B9** dans `verifier-invariants.py`, dans la famille des contrôles B, avec sa
   liste d'exemptions close et nommée.
4. **Éprouver par l'échec** (§VII), dans une copie jetable hors dépôt vivant : ligne de
   base au vert, faute fabriquée, **refus observé**, faute retirée, retour au vert.
5. **Vérifier l'organe MCP** : l'entrée `verifier_invariants` rend B9 dans son JSON.
6. **Journaliser** et mettre à jour la ligne de registre dans la même passe.

## Fichiers touchés

- `verifier-invariants.py` — **modifié** (ajout du contrôle B9).
- `atelier/rd/registre-chantiers.md` — ligne `OUT-20` mise à jour.
- `atelier/annales.md` — entrée de passe, SHA court en dernière ligne.
- Aucun fichier supprimé, aucun renommé : le contrôle constate, il ne range pas.

## Vérification

```bash
# critère 1 — ligne de base inchangée sur le dépôt vivant
python3 verifier-invariants.py --racine /root/wiki | tail -2
# attendu : 0 erreur(s), 71 avertissement(s)   (et aucun [B9])

# critères 2 et 3 — l'épreuve par l'échec, en copie jetable
cp -r /root/wiki /tmp/bac-b9 && cd /tmp/bac-b9
cp doctrinal/symboles/barzakh.md atelier/rd/barzakh.md && git add atelier/rd/barzakh.md
python3 verifier-invariants.py --racine /tmp/bac-b9 | grep B9
# attendu : [B9] barzakh — porté par 2 fichiers : atelier/rd/barzakh.md,
#           doctrinal/symboles/barzakh.md
git rm --cached atelier/rd/barzakh.md && rm atelier/rd/barzakh.md
python3 verifier-invariants.py --racine /tmp/bac-b9 | tail -2   # retour au vert

# critère 4 — les homonymes de convention ne déclenchent rien
python3 verifier-invariants.py --racine /root/wiki | grep -c "B9.*plan\b"   # attendu : 0
```

## Points de retour à l'humain

Deux, tous deux avant l'écriture du code (Cmd 13) : la **sévérité** du contrôle (erreur
ou avertissement) et son **périmètre** (`textes/` et `protocoles/` inclus ou non). Aucun
des deux ne se déduit d'une mesure — ils engagent la règle, pas le fait.

## Journalisation

`atelier/annales.md` (le pôle `rd/` y journalise, `atelier/CLAUDE.md`), ligne `OUT-20`
du registre des chantiers mise à jour dans la même passe, et entrée au registre des
problèmes si l'épreuve révèle un écart non prévu.
