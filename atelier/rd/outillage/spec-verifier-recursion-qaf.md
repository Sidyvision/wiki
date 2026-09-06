---
title: "Spécification — Contrôle du modèle récursif de Sabri B. Rommane (Sūrat Qāf)"
type: outillage
tags: [rd, outillage, coran, muqattaat, verification, deterministe]
created: 2026-09-04
updated: 2026-09-04
sources: []
links: ["[[doctrinal/sources/sabri-ben-rommane-modele-recursif-muqattaat]]"]
---

# Spécification — `verifier-recursion-qaf.py`

> Écrit à l'intégration du 2026-09-04 de `raw/The Sabri Ben Rommane's Theory`.
> Script déterministe, même famille que `verifier-invariants.py` : ni LLM, ni
> réseau, ne corrige rien, n'écrit rien. Lien vers `doctrinal/` à **sens
> unique**, signalé (protocole `doctrinal/`, § Règles de liens).

## 1. Problème traité

La fiche source consigne deux constats de nature arithmétique. Ni l'un ni
l'autre ne doit reposer sur l'affirmation d'un agent : « scripter le
déterministe, réserver le modèle au jugement » (CLAUDE.md racine).

1. **Les comptes publiés par l'auteur ne suivent pas la règle qu'il énonce.**
   Il déclare la hamza « nœud terminal » (IMG_0445, IMG_0479) ; ses chiffres
   (IMG_0480) exigent qu'elle ne soit jamais émise.
2. **Le motif de découpage publié se déduit exactement des règles corrigées.**

## 2. Ce que le script fait

Il déplie l'arbre sur cinq niveaux depuis la graine ق, sous **deux** jeux de
règles, et confronte les sorties aux chiffres publiés :

- **Variante A** — règle *énoncée* : la hamza est émise puis ne branche plus.
- **Variante B** — règle *opérante* : la hamza n'est pas émise ; les noms de
  *fāʾ* et *yāʾ* sont tronqués à deux lettres.

Puis il applique la règle de découpage d'IMG_0447 — les lettres du niveau 5
groupées par leur parent de niveau 4, la taille du groupe étant la longueur du
nom du parent — et compare les 17 premières tailles au motif publié.

Les noms de lettres sont ceux du tableau de l'alphabet de Gloton (repère
**Aa**), `textes/une-approche-du-coran-gloton/corps-du-texte.md`.

## 3. Sortie attendue

```
Variante A : L1..L5 = [3, 9, 25, 67, 179]   — concordance : NON
Variante B : L1..L5 = [3, 8, 21, 56, 151]   — concordance : OUI
Découpage (B) : dérivé identique au publié, somme 45 = versets de Sūrat Qāf
```

Code de sortie `0` si les deux constats tiennent, `1` sinon, avec la ligne
`ÉCART :` qui dit lequel a cédé.

## 4. Ce que le script ne fait pas

Il ne dit rien de la **valeur** du modèle, ni de la correspondance entre les
groupes et les ruptures thématiques de la sourate — laquelle relève d'une
lecture du texte primaire et d'un verdict humain (Cmd 12). Il établit
uniquement que l'arithmétique publiée est reproductible, et sous quelle règle.
