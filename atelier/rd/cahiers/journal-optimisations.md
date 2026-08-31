---
title: "Journal des optimisations — pôle R&D (cahier append-only)"
type: meta
created: 2026-08-30
updated: 2026-08-30
tags: [atelier, rd, cahier, registre, laboratoire]
sources: []
links: []
---

# Journal des optimisations du pôle R&D

Cahier append-only des **améliorations de procédure** effectuées dans les travaux
du pôle `rd/`. Ouvert le 2026-08-30 (verdict Sidy, même séance) — miroir du
[[atelier/rd/cahiers/registre-problemes]] : là où le registre consigne les
échecs/blocages et leur résolution, ce journal consigne les optimisations
réussies et leur impact. Les deux partagent la même discipline de laboratoire
(règle 3 du pôle : tout fait se consigne, succès ou échec).

**Format** — phase 1 (consignation factuelle, aucune interprétation, même
esprit que les fiches `phase: corpus` de `atelier/etudes-de-cas/`) :

- **Procédure modifiée** : quel protocole, fiche, script ou outillage.
- **État avant** : description factuelle de l'état précédent (diff, commande,
  extrait).
- **Changement effectué** : ce qui a été modifié, sans reformulation narrative.
- **État après** : description factuelle du résultat (nouveau diff, nouvelle
  commande, nouvelle sortie).
- **Impact mesuré** : chiffres, temps, erreurs évitées — flagué `to-source` si
  l'impact n'est pas vérifié mécaniquement (§VII).
- **Liens** : fiches, commits, chantier concernés.
- **Statut** : `applique | mesure-pending | reporte`.

**Ce qui n'est pas ici** : la « leçon » d'une optimisation est une
interprétation (phase 2). Elle viendra dans une fiche séparée quand plusieurs
entrées auront le même motif, sur décision de Sidy. Le journal ne fait pas de
généralisation — il consigne.

**Règle** : append-only, jamais de réécriture ni de suppression (Cmd 10).
Insertion en tête (la plus récente en haut), marqueur ci-dessous.

<!-- INSERTION: EN-TÊTE -->

## [2026-08-30] Ouverture du journal des optimisations

- **Procédure modifiée** : discipline de laboratoire du pôle R&D — ajout d'un
  quatrième cahier à `atelier/rd/cahiers/`, après `registre-problemes.md`
  (2026-08-08), le bilan-pont (2026-08-15) et les comptes-rendus de sessions.
- **État avant** : le registre-problèmes consignait les échecs/blocages et
  leur résolution, avec le champ « Compréhension tirée ». Les optimisations
  réussies (procédures améliorées, scripts corrigés, contrôles ajoutés) ne
  laissaient aucune trace propre — elles étaient dispersées dans les annales
  ou les comptes-rendus de sessions, sans format dédié.
- **Changement effectué** : création de `atelier/rd/cahiers/journal-optimisations.md`
  (le présent fichier), annonce insérée dans `atelier/annales.md` (entrée du
  jour, SHA à compléter).
- **État après** : quatre cahiers dans `atelier/rd/cahiers/` — le registre des
  problèmes (échecs), le présent journal (réussites), le bilan-pont (synthèse
  transverse), les comptes-rendus de sessions (chroniques). Chaque optimisation
  effectuée dans le pôle a désormais son lieu de consignation dédié.
- **Impact mesuré** : non mesuré à ce stade — le cahier vient d'ouvrir, aucune
  entrée factuelle d'optimisation n'y a encore été versée. `to-source`.
- **Liens** : [[atelier/rd/cahiers/registre-problemes]] (cahier miroir) ;
  [[atelier/rd/index.md]] §Arborescence (à compléter du nouveau cahier) ;
  séance WebUI 2026-08-30 (verdict Sidy d'ouverture). Commit `84dc4de`.
- **Statut** : `applique` — le cahier est ouvert, en attente de sa première
  entrée d'optimisation factuelle.

## [2026-08-30] Maillage doctrinal — exploitation du graphe existant, pas d'outil parallèle

- **Procédure modifiée** : `doctrinal/CLAUDE.md` — ajout de la section
  « Exploitation du graphe lors de l'intégration (signal d'orphelins) ».
- **État avant** : le graphe (`graphe-cartographie.json`, 1475 edges,
  438 nodes, `Graphe/generer-cartographie.py`) existait mais n'était pas
  exploité systématiquement lors de l'intégration d'une nouvelle fiche
  doctrinale. Aucun signalement d'orphelins n'était produit à ce moment.
- **Changement effectué** : procédure ajoutée dans `doctrinal/CLAUDE.md`
  — l'agent consulte le graphe à l'intégration, signale les orphelines
  (zéro lien entrant), propose des liens (filiations orthodoxes/hétérodoxes)
  sans les inscrire, Sidy tranche (Cmd 12), puis les `cross_links` sont
  ajoutés et le graphe régénéré.
- **État après** : chaque nouvelle fiche doctrinale est désormais vérifiée
  contre le graphe existant avant inscription définitive des liens.
- **Impact mesuré** : non mesuré à ce stade (la procédure vient d'être
  ajoutée, aucune fiche intégrée depuis). `to-source`.
- **Décision de méthode** : pas de script parallèle créé — le graphe
  existant suffit. Un script `detecter-orphelins-doctrinaux.py` avait été
  amorcé puis supprimé (redondance, 143/305 fiches remontaient — bruit, pas
  signal).
- **Liens** : `doctrinal/CLAUDE.md` (section ajoutée) ; `graphe-cartographie.json`
  (source de vérité du maillage) ; `Graphe/generer-cartographie.py`
  (générateur) ; `doctrinal/annales.md` (entrée du 2026-08-30).
- **Statut** : `applique` — procédure en vigueur, en attente de la première
  intégration doctrinale avec signal d'orpheline.
