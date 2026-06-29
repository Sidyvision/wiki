---
title: "Dossier d'amorçage — Projet unifié « LLM-Wiki & Instrument de la Tradition Primordiale »"
type: meta
tags: [outillage, projet-claude-ai, amorcage, onboarding]
created: 2026-06-28
updated: 2026-06-28
---

# Dossier d'amorçage du projet unifié

> Ce dossier rassemble les documents à charger dans le **nouveau projet Claude.ai** qui
> remplace l'ancien projet « LLM Wiki » (devenu trop chargé de sessions disparates). Il
> acte la **fusion** en un seul projet de deux travaux jusque-là menés en parallèle :
>
> 1. **le LLM-Wiki** selon la Restauration Guénon V1 (la base de connaissance doctrinale) ;
> 2. **l'Instrument de la Tradition Primordiale** (son interface dynamique et symbolique en 3D).
>
> Désormais : **un seul projet, deux faces** — la base de connaissance et son interface.

---

## Comment amorcer le nouveau projet Claude.ai

1. **Créer le projet** sur claude.ai, l'intituler par ex. *« Tradition Primordiale — Wiki & Instrument »*.
2. **Coller `00-instructions-projet.md`** dans le champ **« Instructions personnalisées »** du projet
   (c'est le système de pilotage permanent ; il vaut pour toutes les sessions du projet).
3. **Charger en connaissances du projet** (boutons « Ajouter du contenu / fichiers ») :
   - `CLAUDE.md` (la racine du dépôt — le protocole intégral fait toujours foi) ;
   - `01-contexte-demarche-etat.md` (contexte + état des travaux) ;
   - `02-instrument-feuille-de-route.md` (l'app) ;
   - `03-transition-modele-open-source.md` (la bascule hors-token) ;
   - `04-sessions-par-fonction-et-backlogs.md` (le mode de travail + les listes à traiter) ;
   - `05-runbook-test-ornith-gpu-cloud.md` (procédure de test du modèle local Ornith) ;
   - la fiche `atelier/projets/instrument-tradition-primordiale-architecture.md` (architecture détaillée) ;
   - `doctrinal/index.md` (le Catalogue Universel — inventaire vivant) ;
   - quelques fiches exemplaires pour le style (1 symbole, 1 discernement avec bloc 🔍, 1 fiche atelier).
4. **Ouvrir une session par fonction** (voir `04-…`) plutôt qu'une grande session fourre-tout :
   c'est ce qui a fait dériver l'ancien projet.

## Outils opérationnels (à NE PAS charger dans Claude.ai)

- `05-runbook-test-ornith-gpu-cloud.md` — procédure pas à pas du test du modèle local.
- `06-compte-rendu-test-ornith-gpu-cloud-2026-06-29.md` — compte-rendu du 1er test réel (résultats,
  correctifs, anomalie à reproduire).
- `07-resultats-finaux-test-ornith-prepare-compare-2026-06-29.md` — résultat final du cycle complet
  (VERDICT 8 ✓ / 0 ✗) et la nuance *fiabilité d'action ≠ fiabilité narrative*.
- `ornith-test.sh` — harnais de **test de non-régression** (bac à sable isolé sous
  `/root/ornith-test`, jamais le vrai dépôt). Sous-commandes : `prepare` (avant le test) ·
  `compare` (après l'intégration par Ornith) · `selftest` (validation du harnais) · `clean`.
- `ornith-test-doctrinal.sh` — harnais jumeau pour le **cas doctrinal** (Sceau Recteur +
  **réparation du frontmatter corrompu** `-----`/`## title:`/guillemets courbes + étanchéité +
  index §II + annales). Mêmes sous-commandes. Bac à sable : `/root/ornith-test-doctrinal`.
  Ces fichiers servent côté serveur (Claude Code), pas dans le projet Claude.ai.

## Hiérarchie d'autorité des documents

1. `CLAUDE.md` (dépôt) — **protocole invariant**, prime sur tout le reste.
2. `00-instructions-projet.md` — pilotage du projet Claude.ai (résume et applique le protocole).
3. `01` à `04` — contexte, état, feuille de route, mode de travail (s'inclinent devant `CLAUDE.md`).

En cas de contradiction : `CLAUDE.md` tranche. Si un de ces documents le contredit, le signaler
plutôt que de le suivre (Action VIGILANCE).

## Entretien de ce dossier

- `00`, `01` (partie « démarche »), `02`, `03` : **stables**, à réviser à chaque jalon majeur.
- `01` (partie « état des travaux ») et `04` (backlogs) : **vivants**, à réactualiser souvent.
- Toute refonte de ce dossier passe par le sas `_inbox/` et Claude Code, comme une intégration
  normale (jamais d'écriture directe au dépôt depuis Claude.ai).
