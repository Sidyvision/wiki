---
title: "Incident d'édition : un `index()` non ancré détruit 1 600 lignes d'une pièce en cours"
type: outillage
statut_experience: reproduit
created: 2026-09-03
updated: 2026-09-03
status: resolu
severity: eleve
affected_systems: [wiki, outillage, transcription]
---

# Incident d'édition : un `index()` non ancré détruit 1 600 lignes d'une pièce en cours

## Résumé

**Date** : 2026-09-03
**Nature** : suppression silencieuse de contenu par un script d'édition mal ancré
**Étendue** : 1 618 lignes (17 blocs de page) d'un fichier de 2 355 lignes, **avant tout commit**
**Impact** : nul au final — récupération intégrale
**Statut** : résolu

## Description

Au cours de la transcription de *Une approche du Coran par la grammaire et le
lexique* (Gloton), une correction du tableau de la page 64 a été appliquée par un
script Python de la forme :

```python
old_start = s.index("| Nom de la lettre | Transcription | ...")
old_end   = s.index("*Encadré de la colonne « valeur numérique »", old_start)
s = s[:old_start] + new + s[old_end:]
```

Le tableau de l'alphabet arabe **figure deux fois** dans l'ouvrage : page 18 et
page 64, à l'identique — fait que la pièce elle-même signalait explicitement.
`s.index()` a donc trouvé le tableau de la **p. 18**, tandis que le point d'arrivée
se trouvait dans la **p. 64**. Le découpage a emporté tout l'intervalle : les blocs
des pages 31 à 62.

Le fichier est passé de 2 355 à 737 lignes. **Aucune erreur n'a été levée** : le
script s'est terminé normalement et a affiché `ok`.

## Ce qui a permis de le voir

Le contrôle mécanique qui suivait immédiatement l'écriture — `wc -l`,
`grep -c '^## '` — a renvoyé 737 lignes et 13 blocs contre 2 355 et 44 attendus.
Sans ce contrôle systématique après chaque passe (§VIII.2 : la fiabilité d'action ne
se déduit pas de la fiabilité narrative), la perte serait passée inaperçue jusqu'au
commit, voire au-delà.

## Récupération

Le fichier n'était pas suivi par git : aucun `checkout` possible. La récupération
s'est faite depuis le **journal de session** (`~/.claude/.../<session>.jsonl`), qui
conserve l'entrée de chaque appel d'outil, donc le corps de chaque heredoc d'ajout.

1. Extraction des 28 commandes contenant `corps-du-texte.md <<'EOF'`.
2. Découpage des heredocs, sélection des 17 blocs perdus (p. 31 à p. 62).
3. Récupération séparée de la dernière version du bloc p. 18 depuis le script de
   remplacement qui l'avait produit.
4. Recomposition, puis contrôle : 44 blocs, volume cohérent avec l'ajout attendu.

Copie de l'état tronqué conservée avant reconstruction.

## Enseignements

1. **`index()` sur un motif non unique n'est pas un outil d'édition.** Sur un
   document à sections répétées — et une transcription de livre en est un par
   nature — tout ancrage doit être vérifié unique (`s.count(motif) == 1`) ou porté
   par un repère de section (`## p. 64`) plutôt que par le contenu.
2. **Un script de découpage doit affirmer son invariant.** `assert` sur le nombre
   d'occurrences, et sur la variation de taille attendue, transforment une
   destruction silencieuse en échec bruyant.
3. **Le contrôle mécanique après écriture n'est pas une formalité.** C'est lui, et
   lui seul, qui a rendu l'incident visible dans la minute.
4. **Une pièce longue non commitée est sans filet.** Un commit intermédiaire, même
   provisoire, aurait rendu la récupération triviale ; ici elle a dépendu de la
   conservation du journal de session, qui n'est pas une garantie du dépôt.

## Suites

Aucune correction d'outillage automatisée n'est proposée à ce stade : la règle est
une discipline d'écriture de script, pas un défaut d'un programme du dépôt. Point
soumis à Sidy : faut-il porter les points 1 et 2 en consigne dans `CLAUDE.md`,
ou les laisser en retour d'expérience ici ?
