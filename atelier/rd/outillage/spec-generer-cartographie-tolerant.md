---
title: Spécification — Générateur de cartographie avec sévérité à deux niveaux (v1.1)
type: outillage
tags:
- rd
- outillage
- cartographie
- gouvernance
created: 2026-08-11
updated: 2026-08-11
sources: []
links:
- '[[atelier/rd/cahiers/registre-problemes]]'
---

# Spécification — `generer-cartographie.py` v1.1 (mode "tolérant")

> Piste B des « 4 pistes outillage » instruites en session R&D du 2026-08-11
> (voir [[atelier/rd/cahiers/registre-problemes]]). Version 1.1 déployée depuis 
> 2026-07-22, déjà dotée d'une sévérité à deux niveaux sans qu'un mode 
> supplémentaire soit nécessaire.

## 1. Problème traité (historique)

`generer-cartographie.py` v1.0 refusait d'écrire le manifeste dès qu'une anomalie 
était détectée. En pratique sur le dépôt réel : une fiche très référencée portant 
une seule anomalie (ex. `sources_count` erroné) faisait s'effondrer toute la 
cartographie — des dizaines de fiches saines apparaissaient comme porteuses de 
« liens morts » vers cette fiche, générant un rapport illisible.

## 2. Solution : deux niveaux de sévérité (v1.1)

Plutôt qu'un mode « tolérant » suppressif, v1.1 distingue deux catégories d'anomalies :

### BLOQUANT — gouvernance du dépôt

Ces anomalies relèvent des invariants structurels (`CLAUDE.md` §I, Cmd 6) :
- Frontmatter absent, non refermé, ou YAML illisible
- Champ obligatoire manquant (`title`, `type`, `status`, `created`, `updated`)
- Violation d'étanchéité (`meta/ → neutre`, sens interdit par §VI)
- Fiche non dans son circuit déclaré

**Conséquence** : le manifeste n'est PAS écrit (`json` reste absent). C'est 
le comportement voulu : une anomalie de gouvernance ne doit jamais être 
contournée par le script.

### AVERTISSEMENT — état du chantier

Ces anomalies relèvent de l'inachevé ordinaire :
- `sources_count` incohérent avec la liste `sources` actuelle
- Lien mort, ambigu, mal formé (`[[x]]` au lieu de `[[x/y]]`)
- Fiche isolée (aucun lien entrant depuis d'autres circuits)

**Conséquence** : la fiche RESTE dans le graphe, l'anomalie est reportée 
dans le rapport de sortie (`--rapport anomalies.txt`), et visible à l'opérateur. 
Cohérent avec la philosophie kari-kumi (Art. 4 du sashimono) : le montage à 
blanc montre les joints non taillés, il ne condamne pas le chantier.

## 3. Options du script

| Option | Effet | Usage |
|--------|-------|-------|
| `--verifier` | Scan en mode rapport (pas de JSON écrit) | Vérification routine |
| `--rapport <fichier>` | Lister les anomalies dans un fichier | Audit |
| `--sortie <json>` | Écrire le manifeste (si BLOQUANT = zéro) | Production |
| `--strict` | Rétablir v1.0 : tout bloque | Audit critique, désormais rare |
| `--inclure-meta` | Lever l'exclusion de `meta/` du manifeste | Rare (décision Sidy) |

## 4. Distinction de cette approche

Ce n'est **pas** un « mode tolérant » au sens d'ignorer des anomalies. 
C'est une **hiérarchisation** : les anomalies sérieuses (gouvernance) sont 
bloquantes ; les anomalies opérationnelles (état du chantier) sont visibles 
mais non paralysantes.

En pratique : quand `generer-cartographie.py` refuse d'écrire le JSON, c'est 
qu'une fiche porte une violation BLOQUANTE, jamais une anomalie d'AVERTISSEMENT 
(même 100 fiches en avertissement ne suffiront pas à refuser l'écriture).

## 5. Exemple

```bash
# Scan et rapport d'anomalies
python3 generer-cartographie.py --racine /root/wiki --verifier --rapport anomalies.txt

# Résultat possible
# 📊 Total : 247 fiches
# 🛑 Bloquant : 2 (écriture refusée)
# ⚠️ Avertissement : 15 (fiches en chantier, gardées dans le graphe)

# Audit v1.0 (tout bloque)
python3 generer-cartographie.py --strict --racine /root/wiki --rapport audit-strict.txt
# Résultat : beaucoup plus d'anomalies, car stricte = v1.0
```

## 6. Écart volontaire avec l'exemption C3

L'exemption C3 de `verifier-invariants.py` (tous les `annales.md`/`index.md` 
de tous les circuits) ne s'applique PAS ici — `generer-cartographie.py` 
calcule l'étanchéité directement et signalera toujours un lien 
neutre → sensible, même dans `annales.md`.

## Références

- [[atelier/rd/cahiers/registre-problemes]] — entries [2026-08-08], [2026-08-11]
- `Graphe/generer-cartographie.py` — docstring v1.1 (lignes 5-65)
- `CLAUDE.md` §VII — rule commune des manifestes
