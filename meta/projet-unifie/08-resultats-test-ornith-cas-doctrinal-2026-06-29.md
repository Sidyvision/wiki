---
title: "Résultats — test d'Ornith-1.0-9B sur le cas doctrinal (Sceau Recteur, 2026-06-29)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, ornith, vllm, gpu-cloud, runbook, resultats, doctrinal]
created: 2026-06-29
updated: 2026-06-29
---

# Résultats — test d'Ornith-1.0-9B sur le cas doctrinal (2026-06-29)

> Suite directe de `07-resultats-finaux-test-ornith-prepare-compare-2026-06-29.md`, qui concluait
> le test sur le cas **atelier/meta** (frontmatter allégé, sans Sceau Recteur). Ce document couvre
> le test, annoncé comme restant à faire, sur le cas **doctrinal** — Sceau Recteur complet,
> frontmatter corrompu à réparer, vérification de `cross_links`, étanchéité des circuits.
>
> Bac à sable : `/root/ornith-test-doctrinal/` (`golden/` = référence Opus, `sandbox/` = travail
> d'Ornith). Script de vérification mécanique : `meta/projet-unifie/ornith-test-doctrinal.sh compare`.

## 1. Verdict final

```
VERDICT : 12 ✓ / 0 ✗
✅ Ornith gère le cas DOCTRINAL (Sceau Recteur + réparation) — équivalent Opus sur ce lot.
```

Obtenu au **second run**, après un premier run en échec total. Les deux runs sont décrits ci-dessous
car leur comparaison est l'enseignement principal de ce test.

## 2. Premier run — échec total (discours et action)

**Consigne donnée** : la formule standard, large — *« intègre `_inbox/` selon `UPDATES.md` et
`CLAUDE.md` »* — identique à celle ayant réussi sur le cas atelier (`07-…`).

**Résultat** :
- Discours **massivement halluciné dès la première réponse** : mélange de caractères chinois sans
  rapport, fausses citations coraniques (verset inventé « Quran 4:83bis »), réponses attribuées à un
  « constructeur (Sentry) » fictif, tableaux incohérents, formulations syntaxiquement cassées.
- **Aucune action réelle exécutée** : vérification mécanique (`ls _inbox/`, `git status`) après coup
  → les 3 fichiers source (`UPDATES.md`, `nafs-qalb-irritation.md`, `README.md`) étaient inchangés,
  *working tree clean, nothing to commit*.

**Différence notable avec le test atelier (`07-…`)** : sur le cas atelier, la dégradation narrative
était apparue après ~30-40 minutes et n'avait **pas** empêché des écritures correctes (*fiabilité
d'action ≠ fiabilité narrative*). Ici, sur le cas doctrinal — plus complexe (Sceau Recteur,
`cross_links`, étanchéité) — les deux dimensions ont échoué **ensemble et dès le départ** : aucune
action n'a été produite derrière le discours incohérent.

## 3. Second run — succès complet, avec consigne resserrée

**Changement de méthode** : nouvelle session Claude Code fraîche, et **consigne courte et bornée à
une seule fiche** plutôt que la formule large habituelle :

> *« Lis `_inbox/UPDATES.md` et `_inbox/nafs-qalb-irritation.md`, puis applique exactement les
> consignes d'`UPDATES.md` pour cette seule fiche. Ne touche à rien d'autre. »*

**Déroulé** :
1. Plan annoncé avant écriture (vérification de l'existence des cibles `cross_links` —
   `al-ghazali`, `ibn-arabi` — avant toute écriture).
2. `Write` de la fiche réparée dans `doctrinal/symboles/nafs-qalb-irritation.md` — frontmatter
   Sceau Recteur valide, corps **identique à la référence Opus**, citation non vérifiée signalée
   comme telle (conforme au Commandement 5) plutôt que présentée comme un fait établi.
3. `Update` ciblé de `doctrinal/index.md` (1 ligne ajoutée, bon emplacement).
4. **Incident corrigé en cours de route** : à l'étape des annales, un premier essai d'`Update` a
   échoué (« File must be read first »), et Ornith a basculé sur un `Write` qui **réécrivait tout
   `annales.md` depuis la ligne 1**, avec un nouveau frontmatter inventé — violation frontale du
   Commandement 9 (annales append-only). **Refusé manuellement** (option « No »). Après consigne
   corrective explicite rappelant le caractère append-only, Ornith a relu le fichier intégralement
   puis proposé un **edit ciblé** (insertion d'une entrée au bon endroit, rien d'autre touché) —
   validé.
5. Léger retour de discours confus en toute fin de session (~1m40 de raisonnement cumulé sur cette
   tâche) — caractères thaïs isolés, formulation étrange (« lycée de l'élite ») dans le résumé final
   auto-produit par Ornith. **Sans impact sur les actions déjà validées une à une.**

**Vérification mécanique indépendante** (`ornith-test-doctrinal.sh compare`) :

```
A. Présence et routage de la fiche doctrinale       — ✓
B. Sceau Recteur (frontmatter)                       — ✓ (7 sous-contrôles)
C. Corps de la fiche inchangé (vs référence Opus)    — ✓
D. Étanchéité (symbole → discernement non tranché)   — ✓ (absent, conforme)
E. Catalogue (doctrinal/index.md §II)                — ✓
F. Annales (nouvelle entrée mentionnant le lot)       — ✓
G. Effets de bord (git status)                       — fiche créée + index.md + annales.md modifiés
VERDICT : 12 ✓ / 0 ✗
```

Seul point relevé en §G, sans incidence sur le verdict : `_inbox/` n'a pas été vidé — conséquence
logique de la consigne explicitement restreinte à « ne toucher à rien d'autre » que la fiche
traitée, et non un défaut d'exécution.

## 4. La leçon centrale de ce test

Contrairement au test atelier (`07-…`), où l'enseignement portait sur la **dégradation narrative en
session longue malgré des actions fiables**, ce test sur le cas doctrinal révèle un second facteur,
au moins aussi déterminant : **la largeur de la consigne**.

- Une consigne **large et ouverte** (« intègre tout `_inbox/` ») sur une tâche **structurellement
  complexe** (Sceau Recteur, vérification croisée des liens, étanchéité) peut faire échouer à la
  fois le discours **et** l'action, dès le début de la session — pas seulement après une longue
  accumulation de contexte.
- Une consigne **courte, explicite et bornée à un seul livrable** ramène Ornith à un comportement
  cohérent et mécaniquement irréprochable sur ce même type de tâche, y compris quand un incident de
  méthode survient en cours de route (tentative de `Write` global sur un fichier append-only) — à
  condition qu'un humain refuse l'écriture incorrecte et reformule la consigne.

**Conséquence pratique** : le cas doctrinal n'est pas hors de portée d'Ornith, mais il exige un
**découpage de tâche plus fin** qu'un simple « intègre `_inbox/` » — fiche par fiche plutôt que lot
complet — au moins jusqu'à ce qu'un test sur un lot doctrinal multi-fiches soit mené avec la même
rigueur de relecture.

## 5. Recommandations mises à jour pour le cas doctrinal

1. **Ne jamais soumettre un lot doctrinal complet à Ornith avec la formule large standard.**
   Découper en consignes unitaires, une fiche à la fois, jusqu'à validation d'un volume plus
   important.
2. **Surveiller spécifiquement les opérations sur fichiers append-only** (`annales.md`) : un
   `Update` qui échoue ne doit jamais être suivi d'un `Write` global accepté sans relecture — c'est
   le point de rupture le plus probable observé sur ce cas.
3. **Règles déjà actées (`07-…`) toujours en vigueur** : jamais d'auto-accept, toujours clore par
   une vérification mécanique indépendante (`ornith-test-doctrinal.sh compare`), jamais se fier à
   l'auto-rapport d'Ornith (le tableau récapitulatif produit en fin de second run, bien que correct
   ici, ne remplace pas le script).
4. **Prochain test suggéré** : un lot doctrinal de 2-3 fiches simultanées, toujours avec une
   consigne resserrée fiche par fiche (ou en boucle), pour évaluer si la méthode tient à plus grande
   échelle sans retomber dans l'échec du premier run.

## 6. État du dépôt et du Pod à l'issue du test

- Travail mené exclusivement dans le bac à sable isolé `/root/ornith-test-doctrinal/sandbox`
  (référence `golden/` séparée) — **aucune écriture n'a atteint le vrai dépôt `/root/wiki`**.
- Migration du Pod GPU effectuée en cours de session (Volume Disk préservé, modèle non
  retéléchargé) suite à une indisponibilité matérielle côté fournisseur — sans impact sur le
  résultat du test une fois la nouvelle instance opérationnelle.
- Penser à vérifier l'état de facturation du Pod et l'éteindre si aucun autre test n'est prévu dans
  l'immédiat.
