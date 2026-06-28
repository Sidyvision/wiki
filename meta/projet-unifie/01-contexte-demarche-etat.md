---
title: "Contexte, démarche et état des travaux (snapshot 2026-06-28)"
type: meta
tags: [outillage, projet-claude-ai, contexte, etat-des-travaux]
created: 2026-06-28
updated: 2026-06-28
---

# Contexte, démarche et état des travaux

## 1. Contexte et esprit du projet

Le projet a un double visage devenu un seul :

- une **base de connaissance doctrinale** (le LLM-Wiki) tenue dans l'esprit **guénonien** et
  **akbarien** (Ibn ʿArabī), respectant les formes traditionnelles sans syncrétisme, et destinée à
  l'étude et à la transmission ;
- une **interface 3D contemplative** (l'Instrument de la Tradition Primordiale) qui donne à voir
  l'unité de principe sous les formes multiples, sans jamais devenir une source de vérité autonome.

Le dépôt est né d'un long travail de lecture (≈ 28 PDF + un export ChatGPT de 140 conversations) et
d'échanges spéculatifs personnels de Sidy, progressivement mis en ordre. Le tournant fondateur est
la **Restauration « Guénon V1 »** (2026-06-11, révisée 2026-06-12) : abandon d'une organisation
antérieure plate (`domain:`, `type: entity|concept`) au profit de **trois circuits étanches**
(`doctrinal/`, `atelier/`, `meta/`), du **Sceau Recteur**, et d'un vocabulaire rigoureux. Le mot
« réforme » est banni : on **restaure** un ordre normal, on ne corrige pas un principe.

Deux ajouts structurants ont suivi (2026-06-20) : le **circuit Discernement** (spéculations
personnelles datées, examinées dans leur *forme* sans trancher leur *principe*) et le
**Commandement 12 (upakarana)** qui fixe la juste place de l'IA — instrument auxiliaire qui se
prononce sur la structure, jamais sur le principe métaphysique.

## 2. Démarche de travail (le « comment », stable)

- **Séparation des rôles par coût** : la lecture lourde et la production restent côté Claude.ai
  (forfait) ; l'intégration mécanique reste légère et se fait côté serveur (API au token), bientôt
  sur un **modèle local** pour sortir du coût au token (voir `03-…`).
- **Sas `_inbox/`** : tout ce qui est produit transite par ce quai de déchargement, puis Claude Code
  (ou le modèle local) range, répare, indexe, journalise, commit/push, et vide le sas.
- **Plan avant écriture** (Cmd 6) pour tout archivage ; **journalisation systématique** dans
  `annales.md` (Cmd 9) ; **VIGILANCE** régulière (frontmatter, liens morts, orphelins, étanchéité).
- **Pédagogie** : chaque manipulation technique est expliquée à Sidy, qui apprend en faisant.
- **Discernement** : les spéculations personnelles ne sont ni effacées ni validées par l'IA ; elles
  sont documentées, leur généalogie tracée, leurs tensions formelles signalées, et adossées à des
  **lectures suggérées** rattachées à leur généalogie propre.

## 3. État des travaux — snapshot daté du 2026-06-28

> Source vivante et faisant autorité pour l'inventaire : **`doctrinal/index.md`** (le Catalogue
> Universel). Les ordres de grandeur ci-dessous datent de ce snapshot et dérivent par la suite —
> toujours vérifier l'index avant de s'y fier.

### Ce qui est fait

- **Architecture restaurée et stable** : trois circuits, Sceau Recteur, nomenclature, circuit
  Discernement, Commandement 12. `CLAUDE.md` à jour fait foi.
- **Corps doctrinal nourri** (ordres de grandeur au 2026-06-28) : ≈ 5 traditions, ≈ 68 symboles
  (dont les sciences traditionnelles : `ilm-al-huruf`, `ilm-al-awfaq`, `ilm-al-nujum`, logique…),
  ≈ 22 autorités, plusieurs déviations, études et sources, et **14 fiches de discernement**, toutes
  au statut `en cours`.
- **Triage de l'export ChatGPT (140 conversations) intégralement clos** : catégories A, A+C, B, C,
  B+C traitées ; D exclue. Dernier lot intégré le 2026-06-28 (voir `annales.md`).
- **Circuit Atelier ouvert** (premier remplissage depuis la Restauration) : 3 fiches matériel audio
  (Neve 1073SPX, Tascam Model 12, Technics SU-8080), la fiche projet **album-personnel**, et la
  fiche projet **Instrument de la Tradition Primordiale — architecture (esquisse v0.1)**.
- **Lectures suggérées** ajoutées rétroactivement aux 14 fiches de discernement (régularisation du
  2026-06-28).
- **Signalement sensible majeur archivé** : `discernement/2026-06-20_synthese-danger-dissolution-identitaire`
  documente un type de réponse d'IA à risque (validation sans garde-fou) — à ne jamais reproduire.

### Ce qui reste ouvert / à venir

- **Instrument de la Tradition Primordiale** : seule l'**architecture v0.1** est fixée. Reste la
  pile technique, le format du manifeste, la modélisation des degrés du Tasawwuf (tradition pilote),
  le calcul astrologique multi-méthodes, l'échéancier. Voir `02-…`.
- **Transition vers un modèle open-source local** : à préparer et installer. Voir `03-…`.
- **Backlogs de discernement et de vigilance** : 14 fiches `en cours` à faire mûrir ; tensions
  formelles et non-syncrétismes signalés à suivre. Voir `04-…`.
- **Bibliothèque physique** : recensée et validée (`meta/bibliotheque-physique.md`) ; certains
  ouvrages restent candidats à `raw/` pour un futur ingest.
- **Sources à compléter** : citations marquées `to-source` ou « citation non vérifiée » à confronter
  aux textes réels (notamment des citations attribuées à Ibn ʿArabī / al-Ghazālī / au Cheikh).

## 4. Repères chronologiques

- **2026-06-11/12** — Restauration Guénon V1 (trois circuits, Sceau Recteur).
- **2026-06-20** — circuit Discernement + Commandement 12 ; gros du triage ChatGPT ; sas `_inbox/`.
- **2026-06-28** — clôture du triage des 140 conversations ; ouverture de l'Atelier ; esquisse v0.1
  de l'Instrument ; lectures suggérées rétroactives ; **fusion** des deux travaux en un projet unique
  et ouverture du présent dossier d'amorçage.
