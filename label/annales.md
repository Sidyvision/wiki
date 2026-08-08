---
title: Annales du Circuit Label
type: meta
updated: 2026-08-08
---

# Annales du Circuit Label

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-08] arbitrage | album-personnel — tranché, intégration en `label/production/`

**Arbitrage `rd/` vs `label/` tranché** (verdict Sidy) : l'album personnel relève
de la **création artistique** — œuvre et production — et non du pôle R&D de
l'atelier.

**Opérations** :
- Fiche canonique : `label/production/album-personnel.md` (Sceau Recteur §V.b :
  `type: production`, `medium: musique`, `projet: label`, `statut: en-cours`) ;
  contenu transféré à l'identique depuis `atelier/projets/`, note de gouvernance
  ajoutée.
- Stub `deprecated` conservé en `atelier/projets/` avec pointeur (Cmd 10 — jamais
  de suppression sèche).
- 4 liens entrants `atelier/materiel/*` → album coupés (étanchéité §VI : le
  neutre ne pointe pas vers le plus sensible) ; les fiches materiel restent
  référencées depuis la fiche label via `liens_atelier` (§V.b, sens licite).
- Index mis à jour : `label/index.md` (§III Production, nouvelle sous-section
  « Œuvre »), `atelier/index.md`, `atelier/rd/index.md`, arborescence §II et
  journal CLAUDE.md.

**Statut** : fiche `en-cours` ; sources `chatgpt-export-2026-05-10` (meta/,
signalée lien mort au graphe par construction — exclusion meta/ du manifeste).

**Vérification mécanique** : `verifier-invariants.py --racine /root/wiki` →
**0 erreur(s), 0 avertissement(s)** ; `generer-cartographie.py --verifier` →
6 anomalies bloquantes préexistantes (4 doctrinal/sources → v0_3, 2 frontmatter
doctrinal/sources) — hors périmètre de cet arbitrage, registre à jour.

---

## [2026-07-05] grand-lot | Protocole du don, équipe 12 agents, économie, fanzine, merchandising

**Lot final d'infrastructure doctrinal + label opératif** : intégration de 11 fiches label + 1 discernement doctrinal + 12 hermes-prompts (agents de fonction).

**Fiches label intégrées** (11) :
- Discernement (doctrinal) : correspondances 5↔5 / 12↔duodénaire, verdict en cours
- Distribution : doctrine du don (principe unifié), stratégie 300 vinyles, protocole cercles-token, merchandising (4 fiches)
- Direction artistique : 2 amorçages conceptuels (imaginaire ludique, génération non-cumulative)
- Production : modèle économique, équipe 12 agents Hermes
- Marketing : fanzine *Dans l'Absolu*

**Agents (Hermes)** : 12 prompts intégrés (`meta/projet-unifie/hermes-prompts/`), prêts à déploiement Phase 1.

**Statut** : Toutes les correspondances doctrine ↔ label restent suggérées (🔍) ; verdicts en attente de Sidy (Cmd 13). Installation Hermes bloquée par contrainte budgétaire.

---
