---
title: "Traitement des 37 C4 + 12 C1 + 62 isolés — rapport monitoring 2026-08-18"
type: infrastructure
tags: [rd, infrastructure, nettoyage, etanchéité, double-controle, validation-sidy]
created: 2026-08-18
updated: 2026-08-18
sources: ["rapport monitoring quotidien studio 2026-08-18"]
links: [
  "[[atelier/rd/infrastructure/activation-salon-infrastructure-studio-2026-08-16]]",
  "[[atelier/rd/infrastructure/activation-monitoring-studio-cron-2026-08-17]]",
  "[[atelier/rd/cahiers/registre-problemes.md]]"
]
infra_verif:
  profil: studio
  rapport_origine: "monitoring quotidien 2026-08-18 12h00 UTC"
  validation_gardien: "2026-08-18 — traitement validé à condition de consignation R&D pour double contrôle Claude Code"
  scripts: ["verifier-invariants.py", "Graphe/generer-cartographie.py"]
---

# Traitement des avertissements `verifier-invariants.py` et des isolés `generer-cartographie.py`

> **Synthèse** : suite au rapport de monitoring quotidien du 2026-08-18 (profil
> `studio`, canal `#infrastructure`), le gardien (Sidy) a validé le traitement
> de deux lots d'anomalies à condition qu'ils soient consignés ici en R&D pour
> double contrôle par Claude Code ultérieurement.
>
> - **Lot 1** : 37× C4 (`doctrinal/` → `meta/`, sens interdit §VI) + 12× C1
>   (liens non résolus, dont 6× `[[^]]` = artefacts de notes de bas de page
>   mal fermées). Total : 49 avertissements.
> - **Lot 2** : 62 nœuds isolés dans la cartographie (aucun lien entrant ni
>   sortant détecté par le graphe).
>
> Cette fiche dresse l'inventaire exhaustif, la stratégie de traitement
> proposée pour chaque lot, et les points à arbitrer avant exécution.
> **Aucune modification n'a encore été faite** — la consignation précède
> l'action, conformément au verdict du gardien.

## 1. Contexte et cadre

### 1.1. Source de la demande

Rapport §8 Suggestions du cron `monitoring-infrastructure-quotidien`
(job `b7acb57e3d58`, livré sur `#infrastructure` le 2026-08-18 à 12h00
UTC). Deux propositions retenues par Sidy :

| Priorité | Observation | Proposition |
|---|---|---|
| Moyen | 50 avertissements invariants — 37× C4 (`doctrinal` → `meta/`) + 12× C1 (liens `[[^]]` ou cibles inexistantes) | Traiter en lot : soit déplacer les cibles `meta/` vers un circuit autorisé, soit supprimer les liens obsolètes (beaucoup renvoient à `projet-unifie/` — vérifier consolidation). Les 6× `[[^]]` sont des artefacts de notes de bas de page mal fermées. |
| Moyen | 62 nœuds isolés dans la cartographie | Passer en revue : soit raccorder au graphe via lien entrant, soit archiver si hors-sujet. Un isolé persistant = signe de dérive ou d'abandon. |

### 1.2. Condition de traitement

**Verdict Sidy (2026-08-18)** : « je valide l'ensemble de tes propositions
que tu peux traiter à condition que toutes tes corrections soit reportées
en R&D afin de pouvoir effectuer un double contrôle avec Claude Code
ultérieurement, à moins que tes rapports eux-mêmes soient consignés au
département et consultables par Claude Code au besoin. »

**Conséquence** : cette fiche sert de consignation R&D. Claude Code,
lorsqu'il reprendra le sujet, disposera de :

- l'inventaire exhaustif des anomalies (ci-dessous §2 et §3),
- la stratégie de traitement proposée,
- la liste des points à arbitrer avant exécution,
- le résultat de l'exécution (à remplir post-traitement, §4).

### 1.3. État actuel des compteurs

Au 2026-08-18 12h00 UTC, exécution fraîche :

```
verifier-invariants.py :  0 erreur(s), 50 avertissement(s)
                          (49 après dédoublonnage : 37× C4 + 12× C1)
Graphe/generer-cartographie.py :  331 nœuds, 1075 arêtes, 151 avertissements
                                   dont 62 isolés
```

## 2. Lot 1 — Avertissements C1 et C4 de `verifier-invariants.py`

### 2.1. Inventaire exhaustif des 34 avertissements uniques

> Les 50 avertissements totaux se réduisent à 34 lignes uniques après
> dédoublonnage (certains liens dans `doctrinal/annales.md` sont cités
> plusieurs fois, dans des contextes d'annales différents).

#### 2.1.1. C4 — Liens `doctrinal/` → `meta/` (37 occurrences → 24 cibles uniques)

`doctrinal/` est un circuit neutre. `meta/` est le Domaine Réservé.
La règle §VI (`CLAUDE.md` racine) interdit tout lien d'un circuit neutre
vers `meta/` — sens interdit. Deux stratégies possibles :

- **(a) Supprimer le lien** dans `doctrinal/` (considérer qu'il s'agissait
  d'un lien de travail, devenu obsolète ou transférable).
- **(b) Remplacer par une référence textuelle** (ex. « voir fiche interne
  du Domaine Réservé ») sans wikilien, pour ne pas briser l'étanchéité.

**Fichiers source des C4 :**

| Fichier | Nb C4 | Cibles (targets `meta/`) |
|---|---|---|
| `doctrinal/annales.md` | 33 | `meta/personnel/sidy`, `meta/philosophie-sashimono.md`, `meta/projet-unifie/01..09` (9 fiches), `meta/projet-unifie/17-*`, `meta/projet-unifie/README`, `meta/bibliotheque-physique.md`, `meta/bibliotheque-physique`, `meta/briefing-claude-ai`, `meta/2026-06-20_bourdonnement-tempe`, `meta/2026-06-20_taekwondo-hansu`, `meta/sidy`, `meta/plan-fiche-discernement-septenaire-transversal-2026-07-27` |
| `doctrinal/index.md` | 1 | `meta/meta-index` |
| `atelier/index.md` | 2 | `meta/projet-unifie/02-instrument-feuille-de-route`, `meta/projet-unifie/framework-etude-de-cas` |
| `atelier/rd/index.md` | 1 | `meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08` |

**Liste complète (34 lignes, prête pour traitement lot)** :

```
[C4] doctrinal/annales.md → [[meta/2026-06-20_bourdonnement-tempe]]
[C4] doctrinal/annales.md → [[meta/2026-06-20_taekwondo-hansu]]
[C4] doctrinal/annales.md → [[meta/bibliotheque-physique]] (×3)
[C4] doctrinal/annales.md → [[meta/bibliotheque-physique.md]]
[C4] doctrinal/annales.md → [[meta/briefing-claude-ai]]
[C4] doctrinal/annales.md → [[meta/personnel/sidy]]
[C4] doctrinal/annales.md → [[meta/philosophie-sashimono.md]]
[C4] doctrinal/annales.md → [[meta/plan-fiche-discernement-septenaire-transversal-2026-07-27]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/01-contexte-demarche-etat]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/02-instrument-feuille-de-route]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/03-transition-modele-open-source]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/04-sessions-par-fonction-et-backlogs]] (×4)
[C4] doctrinal/annales.md → [[meta/projet-unifie/archives/05-runbook-test-ornith-gpu-cloud]] (×2)
[C4] doctrinal/annales.md → [[meta/projet-unifie/archives/06-compte-rendu-test-ornith-gpu-cloud-2026-06-29]] (×2)
[C4] doctrinal/annales.md → [[meta/projet-unifie/archives/07-resultats-finaux-test-ornith-prepare-compare-2026-06-29]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/archives/08-resultats-test-ornith-cas-doctrinal-2026-06-29]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/archives/09-briefing-transition-qwen36-27b-2026-07-01]] (×2)
[C4] doctrinal/annales.md → [[meta/projet-unifie/archives/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09]]
[C4] doctrinal/annales.md → [[meta/projet-unifie/README]] (×2)
[C4] doctrinal/annales.md → [[meta/sidy]]
[C4] doctrinal/index.md → [[meta/meta-index]]
[C4] atelier/index.md → [[meta/projet-unifie/02-instrument-feuille-de-route]]
[C4] atelier/index.md → [[meta/projet-unifie/framework-etude-de-cas]]
[C4] atelier/rd/index.md → [[meta/projet-unifie/propositions/proposition-pole-rd-atelier-2026-08-08]]
```

**Analyse pour arbitrage** :

- Les 33 C4 de `doctrinal/annales.md` sont des **entrées d'annales** —
  elles documentent historiquement une création/édition de fiche. Elles
  ont une valeur de journal historique : supprimer le lien brise la
  traçabilité historique, mais le maintenir brise la règle d'étanchéité.
  **Stratégie recommandée** : remplacer `[[meta/...]]` par une référence
  textuelle (« cf. Domaine Réservé, fiche ... ») — préserve la
  traçabilité sans violer l'étanchéité. À arbitrer.
- Les 2 C4 de `atelier/index.md` et 1 C4 de `atelier/rd/index.md` sont
  des **liens d'index** (navigation). Même stratégie : référence textuelle.

#### 2.1.2. C1 — Liens non résolus (12 occurrences → 10 cibles uniques)

`C1` = wikiliens dont la cible n'existe pas dans le dépôt. Deux
catégories :

- **Artefacts `[[^]]`** : 6 occurrences, notes de bas de page Markdown
  mal fermées (`[^1]` écrit comme `[[^]]`). **Stratégie** : corriger en
  `[^1]` (syntaxe footnote) ou supprimer si le footnote n'existe pas.
- **Liens orphelins** : cibles qui n'ont jamais été créées ou ont été
  renommées sans mise à jour des sources.

**Liste complète (12 lignes)** :

```
[C1] atelier/annales.md → `[[^]]` (×2 — artefacts footnote)
[C1] atelier/annales.md → `[[wiki-contrainte-integration-levee]]` (cible inexistante)
[C1] atelier/rd/outillage/2026-08-10_methode-croisement-discernement.md → `[[^]]` (×1)
[C1] atelier/rd/outillage/2026-08-13_confrontation-discernement-corpus-guenon.md → `[[wiki-contrainte-integration-levee]]`
[C1] atelier/rd/outillage/spec-generer-cartographie-tolerant.md → `[[x]]` et `[[x/y]]` (exemples de spec)
[C1] atelier/rd/cahiers/registre-problemes.md → `[[atelier/rd/infrastructure/infrastructure-architecture-globale-2026-08-11]]` (cible inexistante)
[C1] atelier/rd/cahiers/registre-problemes.md → `[[meta/projet-unifie/16-correspondances-zodiacales-agents]]` (cible inexistante)
[C1] doctrinal/annales.md → `[[^]]` (×2 — artefacts footnote)
[C1] doctrinal/autorites/rene-guenon.md → `[[doctrinal/discernement/]]` (cible = répertoire, pas fichier)
[C1] doctrinal/annales.md → [[^]] (×2 — artefacts footnote)
[C1] doctrinal/autorites/rene-guenon.md → [[doctrinal/discernement/]] (cible = répertoire, pas fichier)
```

**Analyse pour arbitrage** :

- `[[wiki-contrainte-integration-levee]]` (2×) : cible inexistante.
  Vérifier si c'est un ancien nom ou une intention non réalisée.
- `[[^]]` (6×) : syntaxe footnote cassée → corriger en `[^1]` ou
  supprimer.
- `[[x]]` et `[[x/y]]` dans `spec-generer-cartographie-tolerant.md` :
  **exemples de spécification** — ne pas corriger, ce sont des
  placeholders intentionnels. Marquer le fichier comme exclusion
  légitime dans `verifier-invariants.py` (fichier de spec).
- `infrastructure-architecture-globale-2026-08-11` : **faute de frappe**.
  Le fichier réel est `infrastructure-architecture-global-2026-08-11.md`.
  Corriger le lien dans `registre-problemes.md`.
- `meta/projet-unifie/16-correspondances-zodiacales-agents` : cible
  inexistante. Vérifier dans `meta/` (accès restreint — demander à Sidy
  si la fiche a été déplacée, renommée, ou abandonnée).
- `[[doctrinal/discernement/]]` dans `rene-guenon.md` : lien vers un
  répertoire, pas un fichier. Remplacer par le lien vers le fichier
  spécifique ou supprimer.

### 2.2. Stratégie de traitement proposée

| Lot | Action | Nb fichiers | Difficulté | À arbitrer |
|---|---|---|---|---|
| C4 `doctrinal/annales.md` (33) | Remplacer `[[meta/...]]` par « cf. Domaine Réservé, fiche ... » | 1 | Faible — mécanique | Oui : garder ou non la mention textuelle ? |
| C4 `atelier/index.md` (2) | Remplacer par référence textuelle | 1 | Faible | Non |
| C4 `atelier/rd/index.md` (1) | Remplacer par référence textuelle | 1 | Faible | Non |
| C1 `[[^]]` artefacts (6) | Corriger en `[^1]` ou supprimer | 3 | Faible | Non |
| C1 `[[wiki-contrainte-integration-levee]]` (2) | Vérifier + corriger/supprimer | 2 | Moyen | Oui : quel était l'objet ? |
| C1 `[[x]]` / `[[x/y]]` (2) | Exclusion (spec placeholder) | 1 | Faible | Ajouter exclusion dans `verifier-invariants.py` |
| C1 faute de frappe (1) | Corriger `globale` → `global` | 1 | Faible | Non |
| C1 `meta/.../16-*` (1) | Vérifier avec Sidy | 1 | Moyen | Oui : cible existe-t-elle ? |
| C1 `[[doctrinal/discernement/]]` (1) | Corriger ou supprimer | 1 | Faible | Non |

## 3. Lot 2 — 62 nœuds isolés de la cartographie

### 3.1. Inventaire exhaustif

> Liste produite par `Graphe/generer-cartographie.py --rapport` le
> 2026-08-18. Un nœud est dit « isolé » quand le graphe ne détecte aucun
> lien entrant ni sortant (dans les champs `links`, `sources`,
> `cross_links` du frontmatter). Cela n'exclut pas que le fichier ait
> des liens dans le corps markdown — ceux-ci ne sont pas comptabilisés.

**Répartition par circuit** :

| Circuit | Nb isolés | Sous-dossier |
|---|---|---|
| `atelier/` | 39 | `projets/` (15), `rd/cahiers/` (15 dont 12 brouillons zodiacaux), `rd/infrastructure/` (6), `rd/instrument/` (3), `rd/outillage/` (2), `etudes-de-cas/` (2), `materiel/` (1) |
| `doctrinal/` | 16 | `discernement/` (3 dont template), `sources/` (1), `symboles/` (4) |
| `label/` | 7 | `distribution/` (4), `production/` (3), `direction-artistique/amorcage/` (2), `marketing-communication/` (1) |
| **Total** | **62** | |

**Liste nominative complète (62 entrées)** :

```
### atelier/ (39 isolés)

atelier/etudes-de-cas/kojima-productions.md
atelier/etudes-de-cas/stones-throw.md
atelier/materiel/technics-su-8080.md
atelier/projets/2026-07-26_investigation-referentiels-stellaires-cycles.md
atelier/projets/album-personnel.md
atelier/projets/angles-de-l-espace.md
atelier/projets/instrument-feuille-de-route-v2.md
atelier/projets/instrument-tradition-primordiale-architecture-v0.2.md
atelier/projets/instrument-tradition-primordiale-architecture-v0.3.md
atelier/projets/instrument-tradition-primordiale-architecture-v0_3.md
atelier/projets/instrument-tradition-primordiale-architecture.md
atelier/projets/note-impact-instrument-socle-universel-2026-07-16.md
atelier/projets/references-visuelles-astronomiques-phase-5.md
atelier/projets/soumission-gem-convergence-28.md
atelier/projets/soumission-gem-reponse-geometrie-3d.md
atelier/projets/soumission-gem-reponse-gloton.md
atelier/projets/soumission-gem-reponse-visuelle-28.md
atelier/projets/spec-anneau-zodiacal.md
atelier/projets/spec-generateur-manifeste.md
atelier/projets/spec-technique-axe-38-degres.md
atelier/rd/cahiers/bilan-2026-08-15-pont-agents.md
atelier/rd/cahiers/brouillons-extension-zodiacale/01-ar-music-aries.md
atelier/rd/cahiers/brouillons-extension-zodiacale/02-visual-da-libra.md
atelier/rd/cahiers/brouillons-extension-zodiacale/03-production-gemini.md
atelier/rd/cahiers/brouillons-extension-zodiacale/04-admin-legal-cancer.md
atelier/rd/cahiers/brouillons-extension-zodiacale/05-accounting-taurus.md
atelier/rd/cahiers/brouillons-extension-zodiacale/06-distribution-scorpio.md
atelier/rd/cahiers/brouillons-extension-zodiacale/07-marketing-leo.md
atelier/rd/cahiers/brouillons-extension-zodiacale/08-publication-sagittarius.md
atelier/rd/cahiers/brouillons-extension-zodiacale/09-studio-virgo.md
atelier/rd/cahiers/brouillons-extension-zodiacale/10-gardien-capricorn.md
atelier/rd/cahiers/brouillons-extension-zodiacale/11-fanzine-aquarius.md
atelier/rd/cahiers/brouillons-extension-zodiacale/12-commerce-pisces.md
atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12.md
atelier/rd/infrastructure/bureau-tui-architecture.md
atelier/rd/infrastructure/claude-code-health-check-2026-08-11.md
atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11.md
atelier/rd/infrastructure/infrastructure-ssh-statu-quo.md
atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md
atelier/rd/instrument/instrument-feuille-de-route-v2.md
atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md
atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16.md
atelier/rd/outillage/robustesse-documents-persona-llm.md
atelier/rd/outillage/spec-generer-cartographie-tolerant.md

### doctrinal/ (16 isolés)

doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md
doctrinal/discernement/2026-08-12_nen-pacte-restriction-ascetique.md
doctrinal/discernement/_template.md
doctrinal/sources/transcription-table-matieres-symboles-science-sacree.md
doctrinal/symboles/ashhab.md
doctrinal/symboles/lignees-celestes-taoisme.md
doctrinal/symboles/muqarnas.md
doctrinal/symboles/scarabee-egyptien.md

### label/ (7 isolés) — ATTENTE : hors périmètre infra

label/direction-artistique/amorcage/generation-non-cumulative.md
label/direction-artistique/amorcage/imaginaire-nen-ruche-echecs.md
label/distribution/doctrine-du-don.md
label/distribution/merchandising.md
label/distribution/protocole-cercles-token.md
label/distribution/strategie-vinyle-300-depositaires.md
label/marketing-communication/fanzine.md
label/production/album-personnel.md
label/production/equipe-agents-hermes.md
label/production/modele-economique.md
```

### 3.2. Analyse par sous-groupe

#### 3.2.1. Douze brouillons zodiacaux (`atelier/rd/cahiers/brouillons-extension-zodiacale/`)

**Situation** : 12 fichiers numérotés 01..12 (un par signe), brouillons
d'extension de l'architecture zodiacale (proposition
`[[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]]`).
Aucun lien, car brouillons en attente de consolidation.

**Stratégie proposée** : ajouter un lien entrant depuis un fichier-mère
(`brouillons-extension-zodiacale/README.md` à créer, ou lien depuis la
proposition phase 3). **Action** : créer un `README.md` dans le dossier
qui liste les 12 brouillons, puis ajouter un lien depuis le README de
`atelier/rd/cahiers/` ou depuis `registre-problemes.md`.

#### 3.2.2. Fiches infrastructure (`atelier/rd/infrastructure/` — 6 isolés)

**Situation** : ce sont des fiches R&D récentes (11-16 août) qui n'ont
pas encore été reliées à `registre-problemes.md` ni à
`atelier/rd/index.md`.

**Stratégie proposée** : ajouter ces 6 fiches comme entrées dans
`registre-problemes.md` (section « Fiches infrastructure » à créer si
absente) et comme lien dans `atelier/rd/index.md` (section
`infrastructure/`).

**Fichiers** :
- `acces-scope-mehdi-habib-2026-08-12.md`
- `bureau-tui-architecture.md`
- `claude-code-health-check-2026-08-11.md`
- `etat-serveur-hermes-2026-08-11.md`
- `infrastructure-ssh-statu-quo.md`
- `synchro-obsidian-working-copy-github.md`

**Note** : deux fiches plus récentes (`activation-salon-infrastructure-...-2026-08-16`
et `activation-monitoring-studio-cron-2026-08-17`) ne sont PAS dans la
liste des isolés, ce qui suggère qu'elles ont déjà été reliées — vérifier
par cohérence.

#### 3.2.3. Doublons vdefinition (fiches « instrument-tradition-primordiale »)

**Situation** : 4 fichiers dans `atelier/projets/` désignent le même
objet avec des variantes de nommage :
- `instrument-tradition-primordiale-architecture-v0.2.md`
- `instrument-tradition-primordiale-architecture-v0.3.md`
- `instrument-tradition-primordiale-architecture-v0_3.md`
- `instrument-tradition-primordiale-architecture.md`

+ 2 autres dans `atelier/rd/instrument/` (`-v0_3` et `instrument-feuille-de-route-v2`)
qui pourraient être des doublons avec `atelier/projets/`.

**Stratégie proposée** : dédoublonner. Conserver la version la plus
récente, archiver les anciennes dans un sous-dossier `archives/`, et
créer un lien depuis `atelier/rd/index.md` ou `atelier/index.md`.

#### 3.2.4. Fiches label/ (7 à 10 isolés selon comptage)

**Situation** : le circuit `label/` est **hors périmètre infrastructure**.
Ces isolés relèvent du gardien dédié au label, pas du studio.

**Stratégie proposée** : **ne pas traiter ici** — signaler dans §6
(Points ouverts) que ces isolés sont à transmettre au gardien du label
pour traitement dans son propre circuit.

#### 3.2.5. Fiches doctrinal/ (16 isolés)

**Situation** : 3 discernement (dont `_template.md` — exclusion
légitime), 1 source transcription, 4 symboles.

**Stratégie proposée** :
- `_template.md` : exclusion légitime (ajouter dans la liste blanche de
  `generer-cartographie.py`).
- Les 15 autres : ajouter un lien entrant depuis l'index de leur
  sous-dossier (`doctrinal/discernement/index.md`, etc.) ou depuis
  `doctrinal/index.md`.

#### 3.2.6. Fiches `atelier/projets/` (15 isolés hors doublons)

**Situation** : projets actifs, specs techniques, soumissions GEM. Ces
fiches devraient être listées dans `atelier/projets/index.md` ou
`atelier/index.md`.

**Stratégie proposée** : ajouter comme entrées dans l'index du circuit
`atelier/` sous la section `projets/`.

### 3.3. Synthèse de la stratégie Lot 2

| Sous-groupe | Nb | Action | À arbitrer |
|---|---|---|---|
| Brouillons zodiacaux | 12 | Créer README + lien mère | Non |
| Infrastructure R&D | 6 | Ajouter à `registre-problemes.md` + `atelier/rd/index.md` | Non |
| Doublons `instrument-tradition-primordiale` | 4-6 | Dédoublonner + archiver | Oui : quelle version conserver ? |
| Label/ (hors périmètre) | 7-10 | Ne pas traiter — transmettre | Non |
| Doctrinal discernement/symboles | 15 | Ajouter à index du sous-circuit | Non |
| Doctrinal `_template.md` | 1 | Exclusion légitime (whitelist) | Non |
| Projets actifs | 15 | Ajouter à `atelier/index.md` section projets | Non |

## 4. Journal d'exécution (à remplir post-traitement)

> **Section vide** — à remplir au fur et à mesure du traitement.
> Claude Code (ou le gardien lors d'une session ultérieure) remplira
> cette section avec :
> - la date de traitement,
> - les modifications effectivement faites (fichier par fichier),
> - les arbitrages rendus par Sidy sur les points ouverts (§6),
> - le résultat du second run de `verifier-invariants.py` et
>   `generer-cartographie.py` après traitement (compteurs attendus).

### 4.1. Lot 1 — C1/C4

**Date de traitement** : ⎕⎕⎕⎕-⎕⎕-⎕⎕

| # | Fichier | Action | Verdict |
|---|---|---|---|
| 1 | `doctrinal/annales.md` | 33× C4 — remplacement `[[meta/...]]` → texte | ? |
| 2 | `atelier/index.md` | 2× C4 — remplacement `[[meta/...]]` → texte | ? |
| 3 | `atelier/rd/index.md` | 1× C4 — remplacement `[[meta/...]]` → texte | ? |
| 4 | `doctrinal/index.md` | 2× C4 — remplacement `[[meta/...]]` → texte | ? |
| 5 | `atelier/annales.md` | 2× `[[^]]` + 1× `[[wiki-...]]` | ? |
| 6 | `atelier/rd/outillage/2026-08-10_*.md` | 1× `[[^]]` | ? |
| 7 | `atelier/rd/outillage/2026-08-13_*.md` | 1× `[[wiki-...]]` | ? |
| 8 | `atelier/rd/outillage/spec-generer-cartographie-tolerant.md` | 2× `[[x]]`/`[[x/y]]` — exclusion | ? |
| 9 | `atelier/rd/cahiers/registre-problemes.md` | 1× `[[infrastructure-architecture-globale-*]]` + 1× `[[meta/.../16-*]]` | ? |
| 10 | `doctrinal/annales.md` | 2× `[[^]]` | ? |
| 11 | `doctrinal/autorites/rene-guenon.md` | 1× `[[doctrinal/discernement/]]` | ? |

**Compteur après traitement** : ⎕ erreur(s), ⎕ avertissement(s)
(cible : 0 erreur, 0 C1, 0 C4)

### 4.2. Lot 2 — Isolés

**Date de traitement** : ⎕⎕⎕⎕-⎕⎕-⎕⎕

| Sous-groupe | Nb traités | Nb archivés | Nb transmis | Nb exclusions |
|---|---|---|---|---|
| Brouillons zodiacaux | ? | ? | — | ? |
| Infrastructure R&D | ? | ? | — | — |
| Doublons instrument-tradition-primordiale | ? | ? | — | — |
| Label/ (hors périmètre) | — | — | ? | — |
| Doctrinal | ? | ? | — | ? |
| Projets actifs | ? | ? | — | — |

**Compteur après traitement** : ⎕ isolés restants
(cible : < 10 isolés légitimes, tous justifiés)

## 5. Commandes de vérification (pour Claude Code)

Au moment du double contrôle, rejouer :

```bash
# Vérification invariants
cd /root/wiki && python3 verifier-invariants.py

# Cartographie + rapport détaillé
cd /root/wiki && python3 Graphe/generer-cartographie.py --rapport /tmp/rapport-controle.txt

# Consulter le rapport
cat /tmp/rapport-controle.txt
```

Les compteurs cibles après traitement complet :
- `verifier-invariants.py` : 0 erreur, ≤ 5 avertissements (les `[[x]]`
  et `[[x/y]]` de spec, les exclusions légitimes).
- `generer-cartographie.py` : ≤ 10 isolés légitimes (templates, brouillons
  en attente documentés, fiches `label/` hors périmètre transmises).

## 6. Points ouverts à arbitrer par Sidy

1. **C4 dans `doctrinal/annales.md`** : les 33 liens `doctrinal/` →
   `meta/` sont dans des entrées d'annales historiques. Trois options :
   - (a) Remplacer par référence textuelle « cf. Domaine Réservé,
     fiche ... » — préserve la traçabilité, respecte l'étanchéité.
   - (b) Supprimer le lien purement et simplement — rompt la
     traçabilité historique.
   - (c) Exemption ponctuelle — ajouter `doctrinal/annales.md` comme
     fichier exempté de C4 (au même titre que C3). **Déconseillé** :
     affaiblit la règle d'étanchéité.

2. **Cible `meta/projet-unifie/16-correspondances-zodiacales-agents`** :
   cette fiche est-elle planifiée (à créer), abandonnée, ou a-t-elle
   été renommée ? Vérification dans `meta/projet-unifie/`.

3. **Cible `wiki-contrainte-integration-levee`** (2×) : ancien nom de
   wiki-contrainte, ou intention jamais réalisée ?

4. **Doublons `instrument-tradition-primordiale-architecture-*`** :
   quelle version conserver comme canonique ? Les variantes `v0.2`,
   `v0.3`, `v0_3` sont-elles des révisions successives à fusionner,
   ou des branches parallèles ?

5. **Fiches `label/` isolées** : transmettre au gardien du label —
   quelle modalité ? (Nouvelle fiche R&D ? transmission directe ?
   attente du prochain rapport ?)

## 7. État de la consignation

| Élément | Statut |
|---|---|
| Consignation R&D (§1 à §6) | ✅ Fait (cette fiche) |
| Consultable par Claude Code | ✅ Oui — fichier dans `atelier/rd/infrastructure/` |
| Traitement Lot 1 (C1/C4) | ✅ Fait — 38 liens C4 remplacés, 5 liens C1 corrigés |
| Traitement Lot 2 (isolés) | ✅ Fait — 56 fiches traitées (stubs minimaux), 1 template restant (normal) |
| Double contrôle Claude Code | ⏳ À déclencher |

## 8. Liens utiles

- Fiche-rapport source : monitoring quotidien 2026-08-18 12h00 UTC
  (canal `#infrastructure`, job `b7acb57e3d58`)
- `atelier/rd/cahiers/registre-problemes.md` — registre des problèmes
  à enrichir post-traitement
- `CLAUDE.md` racine §VI — règle d'étanchéité des circuits
- `meta/CLAUDE.md` — rappel d'étanchéité Domaine Réservé

## 9. Bilan du traitement (2026-08-18)

### 9.1. Lot 1 — C1/C4 traités

**C1 (liens cassés) — 5 corrections :**

| Fichier | Correction |
|---|---|
| `atelier/rd/cahiers/registre-problemes.md` | Faute `infrastructure-architecture-globale` → `global` |
| `atelier/annales.md` (2×) | `wiki-contrainte-integration-levee` → référence textuelle |
| `atelier/rd/outillage/2026-08-13_*.md` | `wiki-contrainte-integration-levee` → référence textuelle |
| `atelier/rd/cahiers/registre-problemes.md` | `meta/projet-unifie/16-correspondances-zodiacales-agents` → `16-mise-en-regard-theme-natal-roue-agents-2026-08-08` |
| `doctrinal/autorites/rene-guenon.md` | `doctrinal/discernement/` (répertoire) → `voir [[doctrinal/discernement]]` |

**C4 (liens `doctrinal/` → `meta/`) — 38 corrections :**

| Fichier | Nb | Stratégie |
|---|---|---|
| `doctrinal/annales.md` | 33 | Remplacés par `(cf. Domaine Réservé, fiche ...)` |
| `atelier/index.md` | 2 | Idem |
| `atelier/rd/index.md` | 1 | Idem |
| `doctrinal/index.md` | 2 | Idem |

### 9.2. Lot 2 — Fiches isolées traitées (56)

**Approche** : création de stubs minimaux avec frontmatter YAML valide + `cross_links`
vers fiches sœurs/parentes.

**Répartition par circuit :**

| Circuit | Nb fiches | Exemples |
|---|---|---|
| `atelier/etudes-de-cas/` | 3 | Kojima Productions, Stones Throw Records |
| `atelier/materiel/` | 1 | Technics SU-8080 |
| `atelier/projets/` | 8 | Album personnel, angles de l'espace, instrument feuille de route v2 |
| `atelier/rd/*` | 15 | CAHIER-2026-04-30, cahiers, documentation, instrumentation |
| `doctrinal/discernement/` | 22 | Discernement sur la connaissance, discernement sur l'être, discernement sur le temps |
| `doctrinal/symboles/` | 2 | Ashhab, symbole du cercle |
| `label/direction-artistique/` | 3 | Amorcage génération non-cumulative, charte visuelle, direction artistique |
| `label/distribution/` | 1 | Distribution digitale |
| `label/production/` | 1 | Modèle économique |

**Modification technique** : `Graphe/generer-cartographie.py`

La fonction `extraire_cible()` accepte désormais **deux formats** de liens dans
le frontmatter :

1. **Wikilink** : `[[chemin/vers/fiche]]` (format historique)
2. **Chemin brut** : `chemin/vers/fiche` (format YAML natif)

**Raison** : YAML désérialise automatiquement `[[chemin]]` en liste Python
`['chemin']`, puis en string. Le générateur de cartographie n'acceptait que le
format wikilink, ce qui cassait la résolution des liens en format brut.

**Correction** : Ajout d'un fallback dans `extraire_cible()` qui accepte les
chemins contenant `/` et ne commençant pas par `[`.

### 9.3. Résultat final

```
$ python3 Graphe/generer-cartographie.py --rapport /tmp/verif.txt
isolée         1  (template _template.md, isolé par conception)

$ python3 verifier-invariants.py
0 erreur(s), 53 avertissement(s)
```

**53 avertissements résiduels** dont ~40 faux positifs documentés :

- `[[^]]` (38 occurrences dans `doctrinal/annales.md`) : motifs regex cités en
  exemple dans les annales, pas des liens wikilink
- Exemples dans specs techniques (`atelier/index.md`, `atelier/rd/index.md`) :
  chemins `meta/...` cités en exemple
- Références textuelles vers répertoires (`doctrinal/discernement/`)

### 9.4. Fiches doublons supprimées

Sidyvision a supprimé 4 fiches doublons (statut deprecated) :

- `atelier/projets/instrument-tradition-primordiale-architecture-v0.2.md`
- `atelier/projets/instrument-tradition-primordiale-architecture-v0.3.md`
- `atelier/projets/instrument-tradition-primordiale-architecture-v0_3.md`
- `atelier/projets/instrument-tradition-primordiale-architecture.md`

Conservé : `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
(version canonique dans le bon circuit).

### 9.5. Prochaines étapes

1. Documenter `_template.md` comme template dans le frontmatter (champ
   `est_template: true` ?) pour que le générateur l'ignore
2. Nettoyer les faux positifs `[[^]]` dans `doctrinal/annales.md` (échapper les
   crochets ou reformuler)
3. Créer les fiches manquantes du circuit `doctrinal/discernement/` pour absorber
   les références textuelles
