---
title: Annales du Circuit Label
type: meta
updated: 2026-09-08
---

# Annales du Circuit Label

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

<!-- INSERTION: EN-TÊTE -->

## [2026-09-08] ouverture | Établi de conception du kamon personnel (`amorcage/`)

- **Action** — création de [[label/direction-artistique/amorcage/kamon-personnel]], `statut: en-gestation`. La fiche ne dessine rien et ne tranche rien : elle rassemble ce qui contraint la conception, expose une méthode en six étapes, pose quatre épreuves de validation éliminatoires (échelle 5 mm, négatif, tangence des arcs, soustraction), et **nomme six questions dont la réponse n'appartient qu'à Sidy** (Cmd 13).
- **La contrainte principale, posée avant toute idée** — et elle est contre-intuitive : **un mon ne se compose pas à partir d'un sens qu'on veut dire.** Les quatre voies historiquement attestées procèdent toutes d'un **fait** : le nom (rébus), la brisure d'un mon reçu, le lieu ou le culte, la charge ou le métier. Composer en cherchant le motif qui « signifie » ce qu'on veut exprimer est la seule voie que la tradition du mon n'emprunte pas — et c'est précisément la pente que le discernement doctrinal identifie comme la **parenté hétérodoxe** du dossier (le dictionnaire universel des symboles). Cette contrainte **vaut dès maintenant, sans attendre le verdict**.
- **Étanchéité (§VI)** — deux renvois `label/` → `doctrinal/`, en **sens unique**, **signalés**, et **marqués suggérés (🔍)** tant que le discernement afférent n'est pas tranché, conformément à `label/CLAUDE.md`. Aucun renvoi vers `meta/` ni vers `atelier/`. Les chemins d'assets (`doctrinal/etudes/assets-kamon/`) sont cités **en prose, jamais en wikilink**.
- **Ce que la machine s'est explicitement interdit**, et qui est porté dans la fiche : dessiner le mon à la place de Sidy ; proposer un motif « qui lui correspondrait » (ce serait franchir la contrainte principale et substituer son jugement au sien sur ce qui le définit) ; trancher un sens (Cmd 12).
- **Dossier documentaire** — hors circuit, au doctrinal, entrée propre à `doctrinal/annales.md` du même jour. Il est **intégralement `to-source`** : le dépôt ne possède aucun ouvrage japonais ni héraldique. La conception reste néanmoins possible, **la grammaire du tracé étant vérifiable par le tracé lui-même** ; c'est le sens et les attributions qui attendent.
- **Graphe** — la fiche remonte « isolée », par **limite du Sceau label** (aucun champ de cartouche ne prévoit le renvoi vers `doctrinal/`) et non par défaut de la fiche. Signalé, non corrigé d'office ; verdict à Sidy — détail dans l'entrée doctrinale du jour.
- **Vérification** — `verifier-invariants.py` : 1415 fichiers, 0 erreur, 0 avertissement.
- **Commit** : 8d4159c

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
