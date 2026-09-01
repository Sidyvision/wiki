---
title: "Contexte, démarche et état des travaux (snapshot 2026-08-07)"
type: meta
tags: [outillage, projet-claude-ai, contexte, etat-des-travaux]
created: 2026-06-28
updated: 2026-09-01
---

# Contexte, démarche et état des travaux

> **Régime de lecture (ajouté 2026-09-01).** Les §1-2 (contexte et démarche) sont
> **stables**. La partie « état des travaux » est un **snapshot daté du 2026-08-07** :
> elle n'a pas été tenue à jour depuis, et plusieurs de ses constats sont dépassés
> (signalés en encart à l'endroit où ils figurent). Pour l'état **courant** des
> chantiers — Instrument, infrastructure, outillage, bibliothèque, études de cas,
> process, doctrinal — la source vivante est le registre du pôle R&D :
> [[atelier/rd/registre-chantiers]]. Pour les discernements, `doctrinal/index.md` §VII.

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

## 3. État des travaux — snapshot daté du 2026-07-01

> Source vivante et faisant autorité pour l'inventaire : **`doctrinal/index.md`** (le Catalogue
> Universel). Les ordres de grandeur ci-dessous datent de ce snapshot et dérivent par la suite —
> toujours vérifier l'index avant de s'y fier.

### Ce qui est fait

- **Architecture restaurée et stable** : trois circuits, Sceau Recteur, nomenclature, circuit
  Discernement, Commandement 12. `CLAUDE.md` à jour fait foi.
- **Corps doctrinal nourri** (ordres de grandeur au 2026-07-01) : ≈ 5 traditions, ≈ 78 symboles
  (dont les sciences traditionnelles : `ilm-al-huruf`, `ilm-al-awfaq`, `ilm-al-nujum`, logique…),
  ≈ 25 autorités, plusieurs déviations, études et sources, et **15 fiches de discernement**.
- **Triage de l'export ChatGPT (140 conversations) intégralement clos** : catégories A, A+C, B, C,
  B+C traitées ; D exclue. Dernier lot intégré le 2026-06-28 (voir `annales.md`).
- **Circuit Atelier ouvert** : 3 fiches matériel audio (Neve 1073SPX, Tascam Model 12, Technics
  SU-8080), la fiche projet **album-personnel**, et le dossier **Instrument de la Tradition
  Primordiale** — architecture **v0.1** puis **v0.2 (développée)**, feuille de route v2,
  **spécification technique de l'axe des 38 degrés**, et 4 échanges `soumission-gem-*`.
- **Infrastructure — test Ornith 1.0 clôturé (2026-06-29)** : cycle `prepare/compare` réussi sur
  cas atelier (8 ✓) et doctrinal (12 ✓) via GPU cloud RunPod ; Ornith jugé viable pour l'intégration
  **sous supervision stricte** et **par lots fiche par fiche**. Voir `06-`, `07-`, `08-`.
- **Grand ingest doctrinal 2026-06-29 → 07-01 (intégré par Claude Code, sas `_inbox/` apuré de
  144 fichiers dont ~112 doublons/exports pré-Restauration écartés)** :
  - **Lot al-Jurjānī** : autorité `al-jurjani` ; sources `kitab-al-tarifat-jurjani` +
    `kitab-tarifat-index-transcription` (transcription intégrale des annexes/index, 88 p.).
  - **Cluster Manvantara / Mahdi-Rouge / 28-degrés** : symboles `manvantara`, `atlantide`,
    `manazil-al-qamar`, `table-28-degres-nafas-rahman`, `hadarat-khams` (Cinq Présences) ; sources
    `platon…brisson-2011`, `meftah…albouraq`, `transcription-anneau-28-lettres`, `fin-des-temps…` ×3,
    `barzakh-nur-lh`, `introduction…burckhardt`.
  - **Enrichissement akbarien** : 4 symboles (`al-insan-al-kamil`, `wahdat-al-wujud`, `barzakh`,
    `walaya`) dotés d'une section sourcée du *Kitāb al-Taʿrīfāt*.
  - **Discernement** : `tension-hadarat-burckhardt-jurjani` (Cinq Présences Burckhardt vs Jurjānī —
    **tension considérée résolue par Sidy**, ce qui autorise le renvoi depuis `hadarat-khams`).
  - Autorités `aiman-attar`, `titus-burckhardt` ; amorces `nafas-rahmani`, `eschatologie`.
- **⭐ Correspondance doctrinale ÉTABLIE (validée par le Gem René Guénon, 2026-07-01)** : la
  **convergence quadruple des 28** — 28 fuçûç = 28 lettres = 28 degrés du *Nafas al-Raḥmān* =
  28 *Manāzil al-Qamar* — est posée par Ibn ʿArabī lui-même (*Futūhāt*, ch. 198). C'est le **premier
  ancrage sourcé reliant la couche ontologique (Phase 2) à la couche astrologique (Phase 5)** de
  l'Instrument (équivalence verticale de type essentiel).
- **Signalement sensible majeur archivé** : `discernement/2026-06-20_synthese-danger-dissolution-identitaire`
  documente un type de réponse d'IA à risque (validation sans garde-fou) — à ne jamais reproduire.

### Ce qui reste ouvert / à venir

- **Instrument de la Tradition Primordiale** : **architecture v0.2** fixée dans ses principes ;
  première correspondance Phase 2 ↔ Phase 5 **établie et sourcée** (convergence des 28) ; **spec
  technique de l'axe des 38 degrés** rédigée (géométrie 3D dictée par le Gem). Reste : le format du
  manifeste (`wiki-manifest`, prérequis), la modélisation des degrés du Tasawwuf, le calcul
  astrologique multi-méthodes, l'échéancier, et l'arbitrage de la question §8.2 (directions
  horizontales : Noms Divins abstraits vs quatre angles AS/DS/MC/FC). Voir `02-…`.
- **Transition vers un modèle open-source local** : Ornith 1.0 testé et jugé viable (2026-06-29) ;
  reste à trancher hébergement GPU (cloud à l'heure vs dédié) et à valider un lot multi-fiches. Voir `03-…`.
- **Backlogs de discernement et de vigilance** : 15 fiches à faire mûrir ; tensions formelles et
  non-syncrétismes signalés à suivre. Voir `04-…`.
- **Bibliothèque physique** : recensée et validée ; enrichie le 2026-07-01 (Georgel, Platon/Brisson,
  Burckhardt, Meftah/Albouraq, Ibn ʿArabī *De la mort à la résurrection*).
- **Sources primaires à acquérir / déposer** : Ibn ʿArabī *De la mort à la résurrection* (Gloton,
  possédé — à déposer dans `raw/` ; source de `table-28-degres`, actuellement `to-source`) ;
  *ʿUqlat al-mustawfiz* et *Kitāb al-Inshāʾ al-Dawāʾir* (Ibn ʿArabī, non possédés) ; Meftah *Arma
  Artis 2011* (non possédé — pagination des citations à confirmer).
- **Sources à compléter** : citations `to-source` ou « non vérifiée » à confronter aux textes réels
  (notamment attribuées à Ibn ʿArabī / al-Ghazālī / au Cheikh).

## 4. Repères chronologiques

- **2026-06-11/12** — Restauration Guénon V1 (trois circuits, Sceau Recteur).
- **2026-06-20** — circuit Discernement + Commandement 12 ; gros du triage ChatGPT ; sas `_inbox/`.
- **2026-06-28** — clôture du triage des 140 conversations ; ouverture de l'Atelier ; esquisse v0.1
  de l'Instrument ; lectures suggérées rétroactives ; **fusion** des deux travaux en un projet unique
  et ouverture du présent dossier d'amorçage.
- **2026-06-29** — test GPU cloud d'Ornith-1.0-9B clôturé (cas atelier + doctrinal réussis) ;
  début du grand ingest doctrinal (Jurjānī, hadarat-khams, barzakh-nur-lh).
- **2026-06-30** — lots al-Jurjānī et Manvantara/Atlantide ; enrichissement Jurjānī des 4 symboles akbariens.
- **2026-07-01** — lots Demeures lunaires / ʿIlm al-Nujūm / Meftah / table des 28-38 degrés ;
  **convergence des 28 validée par le Gem** (correspondance établie) ; ménage du sas `_inbox/`
  (144 fichiers) et intégration par Claude Code ; architecture Instrument v0.2 + spec technique de l'axe.
- **2026-07-03 → 2026-07-08** — Infrastructure Hermes Agent : briefing (10-), procédure installation
  phase 1 (12-), re-déploiement Qwen3.6-27B-FP8 (14-), pivot Haiku (13-). 12 profils Hermes
  configurés et testés sur modèle Haiku 4.5 direct (API Anthropic).
- **2026-08-06/07** — Extension du rôle 02 (Direction Artistique) pour couvrir technique
  image/film/argentique (commit `0d96231`, intégré). Discord activé pour les 12 agents (fiches 13-14-15) :
  salons `#marketing`, `#analog-wizard`, `#administratif`, `#gardien`, `#inspiration` (dépôt vers
  `raw/`). Free-response activé (pas de @mention requis). Test réel effectué : l'agent marketing
  a produit une fiche structurée en `_inbox/` (studio-principal.md) à partir d'une description
  verbale dans `#inspiration` — **déviation acceptée « Option A »** (enrichissement en `_inbox/`
  autorisé si la pièce source brute reste dépositée séparément en `raw/assets/` après validation
  humaine). Voir `15-architecture-discord-hermes-2026-08-07.md` pour traçabilité complète.
- **⚠️ 2026-08-07 crise API** : la clé Anthropic partagée par les 12 profils Hermes a atteint son
  plafond de crédit (`HTTP 400: Your credit balance is too low`). Attente d'une clé nouvelle liée
  au plan personnel Sidy (non encore créée). Tous les agents restent inactifs jusqu'à résolution.
  Vérifier `errors.log` en première analyse lors de panne d'agent.
  > **Dépassé — état au 2026-09-01.** Les agents ne sont plus inactifs : ils tournent en continu,
  > le fait est vérifiable au dépôt (dizaines de commits `CHOURA: tour <agent>` du 2026-08-28 au
  > 2026-09-01, cycles quotidiens sous `choura/`, cron de monitoring et de veille actifs). La
  > sortie de crise n'est pas passée par une nouvelle clé Anthropic mais par un **changement de
  > fournisseur d'inférence** : bascule des profils prioritaires (`gardien`, `studio`,
  > `publication`) sur OmniRoute le 2026-08-26, sous quota Qwen épuisé — voir la fiche R&D
  > `atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen.md`. Le paragraphe
  > ci-dessus est conservé comme jalon du 2026-08-07 (Cmd 10) ; il ne décrit plus l'état courant.
