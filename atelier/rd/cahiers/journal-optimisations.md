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

## [2026-08-30] Validation formelle — reconnaissance, pas ajout (item 3 clos)

- **Procédure modifiée** : aucune — l'item 3 est clos par reconnaissance.
- **État avant** : l'aspiration SLM avait identifié un manque supposé :
  protocole de validation formelle pour les fiches doctrinales (entrée/sortie,
  critères mécaniquement vérifiables, scellement). Proposition initiale :
  créer un script `valider-fiche-doctrinale.py` et étendre Karūbī.
- **Décision** : Sidy renvoie au discernement adopté du 2026-08-11
  ([[doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire]])
  qui contient déjà toute la légitimation — l'Athanor = Laboratoire-Sandbox
  (rd/), le flux Discernement → Laboratoire → Doctrine/Archivage, la
  validation par le Maître (Cmd 6/12/13), la distinction Doctrine/Théorie.
  Le dispositif Karūbī (zones scellées, hash, navette, registre-silsila)
  fait déjà la validation mécanique pour les transmissions. Le Sceau Recteur
  (frontmatter doctrinal) fait déjà la validation structurelle pour le
  doctrinal.
- **Changement effectué** : aucun protocole/script ajouté. L'item 3 est clos
  par reconnaissance de ce qui est déjà en acte.
- **État après** : la validation formelle n'est pas à créer — elle est déjà
  là, incarnée dans le discernement adopté du 2026-08-11 et les dispositifs
  existants (Karūbī, Sceau Recteur). Ce qui manque n'est pas un protocole —
  c'est la source Burckhardt "Alchimie" pour approfondir le vocabulaire
  (`to-source`).
- **Impact mesuré** : aucun ajout, donc aucun impact à mesurer. La clôture
  par reconnaissance évite la redondance.
- **Liens** : [[doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire]]
  (légitimation alchimique du Laboratoire-Athanor) ; `meta/transmissions/karubi-gabarit.md`
  (dispositif Karūbī, validation mécanique) ; `doctrinal/CLAUDE.md` (Sceau Recteur,
  validation structurelle) ; séance WebUI 2026-08-30 (verdict Sidy, item 3 clos par
  reconnaissance).
- **Statut** : `applique` — item 3 clos, aucune procédure ajoutée, source
  Burckhardt "Alchimie" `to-source`.

## [2026-08-30] Application procédure exploitation graphe — Golem + Frankenstein

- **Procédure appliquée** : exploitation du graphe (2026-08-30) à l'intégration de trois nouvelles fiches
- **Fiches créées** :
  - `doctrinal/symboles/golem.md` (symbole, phase 1, corpus brut, to-source)
  - `hermeneutique/frankenstein/frankenstein.md` (œuvre, phase 1, corpus brut, to-source)
  - `hermeneutique/auteurs/mary-shelley.md` (auteur)
- **Signalement graphe** : les trois fiches sont orphelines (zéro lien entrant), cross_links vides
- **Action** : liens signalés comme pistes (discernement matrices-artificielles-barzakh, symbole golem) mais non inscrits — en attente de verdict Sidy (Cmd 12)
- **Décision de méthode** : la procédure d'exploitation du graphe est appliquée systématiquement à l'intégration, y compris pour les fiches herméneutiques liées au doctrinal
- **Liens** : [[doctrinal/discernement/2026-06-20_matrices-artificielles-barzakh]], [[doctrinal/symboles/golem]], [[hermeneutique/frankenstein/frankenstein]]
- **Commit** : 659808c
- **Statut** : `applique` — procédure appliquée, fiches en attente de verdict

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
  (générateur) ; `doctrinal/annales.md` (entrée du 2026-08-30). Commit `2ec5a20`.
- **Statut** : `applique` — procédure en vigueur, en attente de la première
  intégration doctrinale avec signal d'orpheline.

## [2026-09-01] Levée du `to-source` Burckhardt « Alchimie » — légitimation athanor/Laboratoire

- **État avant** : la légitimation alchimique du Laboratoire-Athanor
  (ligne 70 ci-dessus) reposait sur l'analogie athanor/Sandbox affirmée dans
  `doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md`
  sans texte primaire — `sources: [to-source]`.
- **Changement effectué** : Sidy a photographié le chapitre XIII
  (« L'athanor ») de Titus Burckhardt, *Alchimie : Science et Sagesse*, et
  demandé l'intégration. Transcription intégrale déposée dans
  `doctrinal/sources/burckhardt-alchimie-ch13-athanor-transcription.md`,
  fiche `doctrinal/autorites/titus-burckhardt.md` mise à jour (2e ouvrage).
- **État après** : `to-source` levé dans la fiche discernement, remplacé par
  le lien vers la transcription, avec signalement daté dans le corps.
- **Impact mesuré** : non mesuré (marqueur de sourçage, pas de métrique de
  performance).
- **Liens** : `doctrinal/sources/burckhardt-alchimie-ch13-athanor-transcription.md` ;
  `doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md` ;
  `doctrinal/autorites/titus-burckhardt.md`.
- **Statut** : `applique`.
