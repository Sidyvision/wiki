---
title: "Sampling comme fonction de Studio — premier échantillon Cordis (spatiotemporal-composability + cordis-wasm)"
type: outillage
statut_experience: en-cours
tags: [atelier, rd, outillage, sampling, cordis, infrastructure-veille, skill, sandbox]
created: 2026-09-05
updated: 2026-09-05
sources:
  - "to-source"   # eSaadster/spatiotemporal-composability-skill — pas de license déclarée (SPDX None)
  - "to-source"   # inso1337/cordis-wasm — pas de license déclarée (SPDX None)
  - atelier/rd/veille/cordis/implementations-github.md
  - atelier/rd/veille/cordis/methodes.md
  - atelier/rd/veille/cordis/equations.md
  - .hermes/profiles/studio/skills/hermes/infrastructure-veille/SKILL.md
  - atelier/rd/registre-chantiers.md
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
---

# Sampling comme fonction de Studio — premier échantillon Cordis

> **Objet de cette fiche** : (1) Positionner le *sampling* (réappropriation technique d'éléments de code externes) comme fonction explicite de l'agent Studio via son mandat `infrastructure-veille` Volet 2. (2) Documenter la rupture identifiée : la veille Cordis a repéré 7 repos externes (août 2026) mais n'a jamais produit le rapport événementiel Discord requis pour validation et consignation. (3) Proposer un premier échantillon *concret, fondé, licencé* : la skill `spatiotemporal-composability` pour Hermes + le pattern sandbox `cordis-wasm` pour l'isolation OS.

---

## I. Le mandat existe déjà — et il est précis

La skill `infrastructure-veille` (profil Studio, mandat 2026-08-16) définit au **Volet 2 — Recherche & développement** :

> **Cadence** : événementielle. Deux déclencheurs :
> 1. **Dépôt de nouvelle source** dans `atelier/rd/` — lire, analyser, rapprocher.
> 2. **Recherche internet proactive** sur technologies émergentes : *frameworks, outils de dev, paradigmes d'orchestration, self-improvement d'agents, hot-reload, composabilité dynamique, évolutions des outils utilisés (Hermes Agent, Qwen, Discord API, systemd, bind mounts, etc.)*.
>
> **Missions** :
> - **Analyse et rapprochement** : confronter les sources (déposées ou trouvées) aux besoins/frictions documentés. Exemple cité : l'étude Cordis (§8) — lire le type de rapprochement attendu avec l'infrastructure Hermes (rechargement à chaud des gateways, dépendances entre agents, etc.).
> - **Propositions d'optimisation** : suggérer des améliorations incrémentales — explicitement marquées comme propositions.
> - **Veille technologique** : suivre les évolutions, signaler ce qui mérite attention ou test.
> - **Démarche self-improvement** : identifier ce qui peut être amélioré par développement incrémental.
>
> **Format de sortie** : **rapport événementiel** (pas de cron quotidien). Même gouvernance Discord-Validation que le Volet 1 : signalement sur `#infrastructure`, **Sidy valide avant toute action**. **Pas d'écriture directe au dépôt** — le rapport Discord est le signal, Sidy ou une session INTEGRATION consigne si validé.

**Conclusion** : le sampling *est* la traduction opérationnelle de ce mandat. Chaque "source trouvée" = un breakbeat repéré. Chaque "rapprochement" = le moment où on décide de le sampler. Chaque "proposition d'optimisation" = le flip produit. Le **rapport Discord validé par Sidy** = le *clearance* (autorisation d'échantillonnage). La **session INTEGRATION** = le consignement en fiche triptyque.

---

## II. La rupture identifiée — où le sampling s'est arrêté

| Étape | État | Preuve |
|-------|------|--------|
| 1. Repérage veille GitHub (2026-08-18) | ✅ **Fait** | `atelier/rd/veille/cordis/implementations-github.md` : 7 repos identifiés, 4 marqués "à scruter en priorité" |
| 2. Extraction équations/méthodes (2026-08-18) | ✅ **Fait** | `equations.md`, `methodes.md`, `notes-lecture.md` |
| 3. **Rapport événementiel Discord (Volet 2)** | ❌ **Jamais émis** | Aucun log Discord `#infrastructure` ne porte d'analyse Cordis → rapprochement infra Hermes |
| 4. Validation Sidy | ❌ **Jamais demandée** | Pas de signal, pas de verdict |
| 5. Consignation triptyque (intent/spec/plan) | ❌ **Jamais ouverte** | `registre-chantiers.md` : aucun chantier `OUT-` ou `INF-` sur Cordis |
| 6. Échantillon prélevé + adapté | ❌ **Jamais fait** | Aucun code/sample dans `atelier/rd/outillage/` issu de l'externe |

**Diagnostic** : la veille a fait le travail de *crate-digging* (fouiller les bacs), mais **le producteur n'a jamais appuyé sur "record"** — le geste de sampler (transformer la piste repérée en proposition validée puis en code adapté) n'a pas été exécuté. La gouvernance Discord-Validation n'a pas été activée pour ce dossier.

---

## III. Premier échantillon : deux pièces, une même philosophie

La veille a identifié 7 repos Cordis. Deux sont **directement pertinents** pour l'infra Hermes et n'ont **aucune license déclarée** (SPDX: None) — ce qui impose une **réappropriation conceptuelle** (paraphrase technique, pas copier-coller), fidèle à l'éthique du sampling : *on prend l'idée, pas l'enregistrement*.

### Échantillon A — `spatiotemporal-composability-skill` (eSaadster)
- **Cible** : une **skill Hermes** native (`~/.hermes/skills/spatiotemporal-composability/SKILL.md`).
- **Ce qu'elle apporte** : un contrat de composant à 3 champs (`inject` / `provide` / `apply`), effets réversibles (chaque mutation retourne son inverse), dépendances typées résolues réactivement, HMR transactionnel, isolation par réalmes, confluence.
- **Résonance Hermes** : tes 12 agents Sashimono sont *exactement* des composants Cordis — chacun déclare ce qu'il injecte (discord, cron, skills, mémoire), ce qu'il fournit (sa fonction), et ses effets (écriture fichiers, appels API) devraient être réversibles. Le hot-reload des gateways sans redémarrage = HMR Cordis.
- **License** : **aucune déclarée** (GitHub API SPDX: None). → **Réappropriation conceptuelle seulement** : on réécrit le contrat à notre façon, en français, selon le vocabulaire Sashimono, sans copier le SKILL.md.

### Échantillon B — `cordis-wasm` (inso1337)
- **Cible** : un **pattern d'isolation OS** pour les agents Hermes — chaque agent comme un composant Wasm dont les coeffects (dépendances) sont des *imports Wasm*, physiquement inatteignables s'ils ne sont pas déclarés.
- **Ce qu'il apporte** : confinement *physique* (pas convention), `INACTIVE_ACCESS` impossible (link error à l'instanciation), mémoire linéaire par composant = revert gratuit au drop, async inertia layer (activation par étapes `activate_step` avec rollback partiel), host-mediated effects (acquisitions tracées, émissions compensées), fs.coeffect comme frontière système réelle.
- **Résonance Hermes** : ton isolation bind-mount + user!=root (Mehdi) = exactement le §6.1 du papier Cordis ("OS co-designed with the paradigm bounds a component to its declared dependencies"). Le gateway Hermes = hôte Wasm ; chaque agent = module Wasm ; les compétences (skills, cron, discord) = coeffects importés.
- **License** : **aucune déclarée** (GitHub API SPDX: None). → **Réappropriation conceptuelle** : on adapte l'architecture à ton stack (Python, systemd, bind mounts) sans copier le code Rust/Python du repo.

> **Rappel légal (sampling éthique)** : sans license, "tous droits réservés" s'applique par défaut. Le sampling légal = **clearance** (permission) OU **transformation substantielle** (nouvelle œuvre). Ici : pas de clearance → on fait de la *réappropriation conceptuelle* documentée (cette fiche = la traçabilité du isnad). Si une license est ajoutée ultérieurement (MIT, Apache-2.0), un échantillon direct devient possible.

---

## IV. Triptyque du premier chantier de sampling

Le chantier reçoit l'identifiant **`OUT-15`** (Outillage & scripts — sampling externe). Il suit le gabarit `atelier/rd/outillage/gabarit-triptyque-chantier.md`.

### OUT-15 — intent.md (pourquoi)

**Le besoin** : l'agent Studio a un mandat explicite de veille proactive et de rapprochement (`infrastructure-veille` Volet 2) mais n'a jamais produit le rapport événementiel Discord qui transforme une piste repérée en échantillon validé. Le dépôt contient des études Cordis approfondies (équations, méthodes, implémentations GitHub) qui n'ont jamais été *samplées* — ni transformées en propositions concrètes pour l'infra Hermes (skills, sandbox, HMR, isolation).

**Qui le porte** : Studio (agent de fonction, rôle 9), mandaté par Sidy pour le sampling via infrastructure-veille.

**Hors périmètre** :
- Copier-coller du code des repos externes (license absente → interdit).
- Refonte globale de l'architecture Hermes (gain incrémental seulement).
- Décision doctrinale (Cmd 12) : le sampling est une technique d'ingénierie, pas un discernement.

**Contraintes doctrinales** :
- Cmd 5 (source primaire) : chaque élément samplé doit avoir sa `to-source` tracée (repo, commit, fichier, ligne).
- Cmd 6 (plan validé) : aucun code d'échantillon n'est écrit sans `plan.md` visé par Sidy.
- Cmd 8 (created immuable) : la fiche de sampling porte sa date d'origine.
- Cmd 10 (pas de suppression) : un échantillon rejeté devient `deprecated`, jamais effacé.
- §VII (sens unique) : le sampling va `extérieur → atelier/rd/` ; jamais l'inverse.

**Signe de réussite** : un premier échantillon (skill `spatiotemporal-composability` OU pattern sandbox `cordis-wasm`) consigné en `atelier/rd/outillage/out-15-<slug>/` avec son triptyque complet, sa provenance (`sources: ["to-source: ..."]`), sa réappropriation paraphrasée, et son plan d'intégration incrémental validé par Sidy.

**Ce qui reste ouvert** :
- Choix du premier échantillon (A skill, B sandbox, ou les deux en parallèle) → verdict Sidy.
- Clarification license : contacter les auteurs pour demander une license (MIT/Apache-2.0) → si obtenue, échantillon direct possible.

---

### OUT-15 — spec.md (quoi)

**Comportement observable** : Studio émet un rapport événementiel Discord `#infrastructure` proposant un échantillon Cordis (A ou B) avec : (1) description technique paraphrasée, (2) rapprochement concret avec une friction infra Hermes documentée, (3) proposition d'intégration incrémentale, (4) analyse de license, (5) demande de verdict Sidy. Si verdict favorable → session INTEGRATION ouvre le triptyque et consigne l'échantillon.

**Données consommées / produites** :
- Entrée : `atelier/rd/veille/cordis/implementations-github.md`, `equations.md`, `methodes.md` ; repos GitHub `eSaadster/spatiotemporal-composability-skill` (commit `8108cce`) et `inso1337/cordis-wasm` (commit `f5c0562`).
- Sortie : `atelier/rd/outillage/out-15-sampling-cordis/intent.md`, `spec.md`, `plan.md` + rapport Discord événementiel.

**Critères d'acceptation** :
1. Rapport Discord émis sur `#infrastructure` avec les 5 éléments ci-dessus.
2. Sidy émet un verdict explicite (✅ valider / ❌ rejeter / 🔄 revoir) sur le message Discord.
3. Si ✅ : triptyque créé dans `atelier/rd/outillage/out-15-sampling-cordis/` avec Sceau atelier, `chantier: OUT-15`.
4. `verifier-invariants.py --racine /root/wiki` passe sans erreur sur les nouvelles fiches.
5. Entrée d'annales `atelier/annales.md` avec SHA court du commit d'ajout.

**Cas limites** :
- Si license ajoutée ultérieurement sur le repo source → mise à jour `sources:` de `to-source` vers `MIT`/`Apache-2.0` + échantillon direct possible (nouveau plan).
- Si Sidy rejette → fiche marquée `caduc` dans `registre-chantiers.md`, raison consignée.

**Ce qui reste `to-source`** :
- License des deux repos (à clarifier auprès des auteurs).
- Commit exact du SKILL.md `spatiotemporal-composability` (le raw 404 suggère un chemin différent).
- Confirmation que `cordis-wasm` DESIGN.md reflète l'implémentation courante (7 commits, dernier août 2026).

---

### OUT-15 — plan.md (comment)

> **Statut** : `brouillon` — seul un plan `vise` autorise l'écriture (Cmd 6).

**Étapes** :
1. **Rapport Discord** : rédiger le rapport événementiel Volet 2 (format skill infrastructure-veille) proposant l'échantillon A (skill) avec rapprochement concret : "remplacer la configuration statique des 12 agents Sashimono par un contrat `inject/provide/apply` à effets réversibles, permettant HMR des gateways sans redémarrage".
2. **Attendre verdict Sidy** : sur Discord `#infrastructure`. Si 🔄 → réviser rapport. Si ❌ → marquer `caduc`, consigner raison, arrêter.
3. **Si ✅** : créer dossier `atelier/rd/outillage/out-15-sampling-cordis/` + triptyque (intent/spec/plan = cette fiche) + fiche d'échantillon `echantillon-A-skill.md` (réappropriation conceptuelle du contrat Cordis en skill Hermes, vocabulaire Sashimono, sans copier le code).
4. **Vérification** : `python3 verifier-invariants.py --racine /root/wiki` → 0 erreur.
5. **Annales** : entrée `atelier/annales.md` avec SHA court, type `integration`, tags `[atelier, rd, outillage, sampling, cordis]`.
6. **Registre** : mettre à jour ligne `OUT-15` dans `atelier/rd/registre-chantiers.md` (statut `en-cours` → `clos` ou `caduc`).

**Fichiers touchés** :
- Création : `atelier/rd/outillage/out-15-sampling-cordis/{intent,spec,plan,echantillon-A-skill}.md`
- Modification : `atelier/rd/registre-chantiers.md` (ligne OUT-15), `atelier/annales.md` (append-only).
- Rien ne se supprime, rien ne se déplace (Cmd 10).

**Vérification** :
- `grep -r "OUT-15" atelier/rd/registre-chantiers.md` → ligne présente.
- `python3 verifier-invariants.py --racine /root/wiki` → exit code 0.
- `git log --oneline -1` → SHA court correspondant à l'annale.

**Points de retour à l'humain** (Cmd 13) :
- Verdict sur le rapport Discord (étape 2).
- Choix A vs B vs A+B (étape 1).
- Autorisation de contacter les auteurs pour license (si souhait d'échantillon direct).

**Journalisation** :
- Circuit d'annales : `atelier/annales.md`.
- Registre : `atelier/rd/registre-chantiers.md` (ligne OUT-15, même passe).

---

## V. Prochaine action immédiate

**Émettre le rapport événementiel Discord** (Volet 2 infrastructure-veille) proposant l'**échantillon A — skill `spatiotemporal-composability`** comme premier sampling, avec :
- Résumé technique paraphrasé (contrat inject/provide/apply, effets réversibles, HMR, réalmes).
- Rapprochement : "les 12 agents Sashimono = 12 composants Cordis ; hot-reload gateways = HMR ; isolation Mehdi = réalmes".
- Proposition : réécrire le contrat en skill Hermes `spatiotemporal-composability` (français, vocabulaire Sashimono) pour valider l'approche sur un agent pilote.
- License : `to-source` (aucune déclarée) → réappropriation conceptuelle seulement.
- Demande de verdict Sidy : ✅ valider le sampling / 🔄 revoir le rapprochement / ❌ rejeter.

**Dès verdict ✅** : cette fiche devient le triptyque `OUT-15` officiel, le dossier `out-15-sampling-cordis/` est créé, et l'échantillon A est consigné.

---

## VI. Références croisées (isnad du sampling)

| Élément | Rôle dans le isnad | Lien |
|---------|-------------------|------|
| `atelier/rd/veille/cordis/implementations-github.md` | Crate-digging (repérage) | source primaire veille |
| `atelier/rd/veille/cordis/methodes.md` | Extraction technique | méthodes Cordis |
| `atelier/rd/veille/cordis/equations.md` | Fondement formel | équations §3-4 |
| `.hermes/profiles/studio/skills/hermes/infrastructure-veille/SKILL.md` | Mandat opératoire | Volet 2 §Missions |
| `atelier/rd/registre-chantiers.md` | Pilotage | ligne `OUT-15` |
| `eSaadster/spatiotemporal-composability-skill` (commit `8108cce`) | Source externe A | `to-source` |
| `inso1337/cordis-wasm` (commit `f5c0562`) | Source externe B | `to-source` |

---

## VII. Marqueur d'insertion

<!-- INSERTION: EN-TÊTE -->

*Fiche créée le 2026-09-05. Prochaine étape : rapport Discord Volet 2 infrastructure-veille pour verdict Sidy sur l'échantillon A.*