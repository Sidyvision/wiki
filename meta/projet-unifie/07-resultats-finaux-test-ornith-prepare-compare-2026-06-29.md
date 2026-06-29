---
title: "Résultats finaux — cycle prepare/compare avec Ornith-1.0-9B (2026-06-29)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, ornith, vllm, gpu-cloud, runbook, resultats]
created: 2026-06-29
updated: 2026-06-29
---

# Résultats finaux — cycle prepare/compare avec Ornith-1.0-9B (2026-06-29)

> Suite directe de `06-compte-rendu-test-ornith-gpu-cloud-2026-06-29.md`, qui s'arrêtait avant
> la conclusion du cycle `prepare → compare`. Ce document rapporte le résultat final, obtenu
> dans une **session Claude Code fraîche** (comme recommandé), et la nuance majeure qui en
> ressort sur la fiabilité d'Ornith.

## 1. Verdict final

```
VERDICT : 8 ✓ / 0 ✗
✅ Ornith équivaut à Opus sur ce lot — rôle d'intégration VIABLE.
```

Vérification mécanique du script `ornith-test.sh compare` (indépendante de tout ce que le
modèle a pu dire de son propre travail) :
- **A. Contenu des 4 fiches produites** : identique byte pour byte à la référence Opus
  (`golden/`), pour les 4 fichiers (`neve-1073spx.md`, `tascam-model-12.md`,
  `technics-su-8080.md`, `2026-06-20_taekwondo-hansu.md`).
- **B. Catalogue (`doctrinal/index.md` §VIII Matériel)** : les 3 liens attendus sont présents.
- **C. Annales** : entrée correctement ajoutée, mentionnant le lot.
- **D. Effets de bord** : aucun fichier modifié en dehors du périmètre attendu (4 fiches créées
  + `index.md` + `annales.md` + `_inbox/` vidé) — pas de pollution du reste du bac à sable.

## 2. Déroulé de la session (contexte du verdict)

1. **`prepare`** : exécuté sans accroc, résumé fidèle et précis de ses 5 étapes par Ornith.
2. **Intégration effective** (lecture des 4 fiches sources, écriture des 4 fiches destination,
   mise à jour de `index.md` et `annales.md`) : chaque opération d'écriture
   (`Write`/`Update`) a été **relue et validée manuellement avant exécution** — aucune
   validation automatique (« auto-accept ») n'a été utilisée.
3. Au fil de cette session longue (~40 minutes de raisonnement continu), le **discours**
   d'Ornith s'est progressivement dégradé : termes techniques inventés (« norm- prefix »,
   « Madsum »), une URL GitHub fictive, des fragments de tchèque/russe/chinois sans rapport,
   une fuite de balise `</think>` dans la sortie visible, et une **contradiction interne**
   (affirmer à la fois que l'intégration était terminée et que les fichiers étaient encore
   dans `_inbox/`).
4. Face à cette incohérence narrative croissante, **aucune confiance n'a été accordée à
   l'auto-rapport d'Ornith**. Le verdict a été obtenu en relançant `ornith-test.sh compare`
   directement en shell, indépendamment de toute déclaration du modèle sur son propre travail.
5. **Résultat : malgré la dégradation du discours, le travail réellement exécuté sur le
   système de fichiers était entièrement correct.**

## 3. La nuance centrale à retenir : fiabilité d'action ≠ fiabilité narrative

C'est l'enseignement principal de ce test, à garder en tête pour toute utilisation future
d'Ornith (ou de tout modèle local de cette taille) :

- **Les actions concrètes d'Ornith (écritures de fichiers, diffs appliqués) ont été fiables**,
  du moins dans ce test, où chaque action a été soumise à une **revue humaine avant
  exécution**.
- **Le discours d'Ornith sur ce qu'il fait ou a fait devient peu fiable** au-delà d'une
  certaine durée de raisonnement continu dans une même session — il peut halluciner des faits,
  se contredire, ou mélanger des langues sans rapport, *tout en continuant à produire des
  actions correctes en parallèle*.
- **Conséquence pratique** : on ne peut pas se contenter de demander à Ornith « as-tu bien
  intégré le lot ? » et lui faire confiance sur sa réponse. Le **seul juge fiable est une
  vérification mécanique indépendante** (ici, le script `compare`), jamais l'auto-évaluation du
  modèle.

## 4. Recommandations pour une utilisation en production

1. **Ne jamais activer l'acceptation automatique des modifications** (`auto-accept edits`)
   avec Ornith en l'état actuel. Chaque `Write`/`Update`/commande Bash doit être relue avant
   validation, au moins jusqu'à ce que la fiabilité narrative soit améliorée (modèle plus
   grand, fine-tuning, ou garde-fous supplémentaires côté scripts).
2. **Toujours clore un cycle d'intégration par une vérification mécanique indépendante**
   (script de comparaison, diff, ou équivalent) — ne jamais se fier au résumé que le modèle
   donne de son propre travail.
3. **Limiter la durée des sessions Ornith.** La dégradation observée est apparue après une
   trentaine de minutes de raisonnement continu sur une tâche complexe. Privilégier des
   sessions courtes, ciblées sur une seule tâche, plutôt que des sessions longues qui
   accumulent du contexte de conversation.
4. **Ce test ne couvre que le cas le plus simple** (frontmatter allégé `atelier/materiel` et
   `meta`, sans Sceau Recteur doctrinal). Une intégration touchant le circuit `doctrinal/`
   (frontmatter complet, blocs Discernement, étanchéité des circuits) représente un enjeu plus
   élevé en cas d'erreur — recommandé de retester spécifiquement ce cas avant d'y confier
   Ornith, avec la même vigilance de revue manuelle systématique.
5. **La stratégie hybride de `03-transition-modele-open-source.md` reste la bonne approche** :
   Ornith pour la mécanique régulière supervisée, Opus/API pour les cas délicats (jugement
   doctrinal, Discernement, rédaction sensible) où l'autonomie complète est requise.

## 5. État du dépôt et du Pod à l'issue du test

- **Aucune écriture n'a atteint le vrai dépôt `/root/wiki`** : tout s'est déroulé dans le bac
  à sable isolé `ornith-test/sandbox` (sans `.git` actif, sans remote), conformément à la
  conception du script de test.
- Le Pod GPU reste dans l'état où la session s'est terminée — **vérifier s'il est toujours
  actif et l'arrêter si aucun autre test n'est prévu dans l'immédiat**, pour stopper la
  facturation.
