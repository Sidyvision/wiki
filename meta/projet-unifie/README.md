---
title: "Dossier d'amorçage — Projet unifié « LLM-Wiki & Instrument de la Tradition Primordiale »"
type: meta
tags: [outillage, projet-claude-ai, amorcage, onboarding]
created: 2026-06-28
updated: 2026-09-01
---

# Dossier d'amorçage du projet unifié

> **Un seul projet, deux faces** — la base de connaissance doctrinale (le LLM-Wiki selon la
> Restauration Guénon V1) et son interface dynamique en 3D (l'Instrument de la Tradition
> Primordiale). La fusion a été actée le 2026-06-28 ; ce dossier en est la porte d'entrée
> et le poste de pilotage.
>
> **Où va le regard en premier :**
> - **Où en sont les travaux** → `01-contexte-demarche-etat.md` §3, synthèse actualisée.
> - **Quels chantiers sont ouverts** → [[atelier/rd/registre-chantiers]], la carte vivante
>   de tous les chantiers du dépôt, doctrine incluse.
> - **Quelles décisions attendent Sidy** → le §Points ouverts de ce même registre.

---

## Le dossier, dossier par dossier (réorganisé le 2026-09-01)

Jusqu'à cette date, quarante fichiers vivaient à plat, et rien ne distinguait au premier
regard une pièce vivante d'un compte-rendu vieux de deux mois. **C'est la confusion la plus
coûteuse de ce dossier : lire un jalon daté comme s'il décrivait l'état courant.** Les
régimes sont désormais portés par l'arborescence.

### À la racine — le noyau de pilotage

| Pièce | Régime | Ce qu'elle porte |
|---|---|---|
| `00-instructions-projet.md` | **stable** | le système de pilotage permanent, à coller dans les instructions personnalisées du projet Claude.ai |
| `01-contexte-demarche-etat.md` | **§1-2 stables · §3 vivant** | ce qu'est le projet, comment on y travaille, et **la synthèse d'état** |
| `02-instrument-feuille-de-route.md` | **stable** | phases, invariants et garde-fous de l'Instrument (l'avancement, lui, est au registre) |
| `03-transition-modele-open-source.md` | **stable, scénario dépassé** | l'objectif de souveraineté et ses contraintes dures ; le scénario nommé ne vaut plus |
| `04-sessions-par-fonction-et-backlogs.md` | **§A stable · §B-C vivants** | le mode de travail par fonction ; les questions de décision et la vigilance permanente |
| `queue-idees.md` | **vivant** | file d'attente d'idées à destination des agents (dispositif ouvert le 2026-08-27) |
| `directive-discernement-domaines.md` | **stable** | la doctrine de méthode du Cmd 12 : forme / principe |
| `framework-etude-de-cas.md` | **stable** | le cadre des études de maisons et de marques |

### Les sous-dossiers

| Dossier | Régime | Comment le lire |
|---|---|---|
| `archives/` | **jalons datés** | runbooks, comptes-rendus de tests, procédures d'installation, briefings, exports. **Chaque pièce ne décrit que son jour** — ne jamais en déduire l'état courant. Index : `archives/README.md` |
| `propositions/` | **dispositifs soumis au verdict** | les sept `proposition-*.md`. Chacune porte en tête l'état réel de son exécution, daté |
| `outillage/` | **opératoire** | les deux harnais de non-régression (`regression-test.sh`, `regression-test-doctrinal.sh`), à exécuter côté serveur, jamais à charger dans un projet Claude.ai |
| `choura/` | **vivant** | les cycles de Consultation (*shūrā*) entre les douze agents, un fichier par cycle |
| `hermes-prompts/` | **configuration** | les douze rôles d'agents : un `NN-principe.md` et un ou plusieurs mandats chacun. Matière opératoire, pas documentation de projet |
| `hermes-skills/` | **configuration** | spécifications des skills d'agent |

> **Chemins d'avant la réorganisation.** Les entrées d'annales et les cahiers append-only
> antérieurs au 2026-09-01 citent ces pièces à leur ancien chemin, à plat
> (`meta/projet-unifie/12-…`). Ces citations sont **exactes pour leur date** et ne sont pas
> réécrites : un journal ne se corrige pas après coup. Pour les suivre aujourd'hui, ajouter
> le sous-dossier — `archives/` pour les fiches numérotées et les briefings,
> `propositions/` pour les `proposition-*`, `outillage/` pour les `.sh`.

---

## Amorcer un projet Claude.ai à partir de ce dossier

1. **Créer le projet**, l'intituler par ex. *« Tradition Primordiale — Wiki & Instrument »*.
2. **Coller `00-instructions-projet.md`** dans les **instructions personnalisées** : c'est le
   pilotage permanent, il vaut pour toutes les sessions.
3. **Charger en connaissances du projet** :
   - `CLAUDE.md` de la racine du dépôt — le protocole intégral fait toujours foi, et les
     `CLAUDE.md` locaux du circuit sur lequel on travaille le complètent (§II bis) ;
   - `01-contexte-demarche-etat.md` (le §3 d'abord) ;
   - `02-instrument-feuille-de-route.md` et `04-sessions-par-fonction-et-backlogs.md` ;
   - `atelier/rd/registre-chantiers.md` — **l'état des chantiers** ;
   - la fiche d'architecture courante de l'Instrument
     (`atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`,
     courante depuis le 2026-08-25 ; les v0.1 et v0.2 restent des jalons) et
     `spec-technique-axe-38-degres.md` ;
   - `doctrinal/index.md` — le Catalogue Universel, inventaire vivant ;
   - quelques fiches exemplaires pour le style : un symbole, un discernement avec son
     bloc 🔍, une fiche d'atelier.
4. **Ouvrir une session par fonction** (voir `04-…`) plutôt qu'une grande session
   fourre-tout : c'est ce qui a fait dériver le projet précédent.

**Ne pas charger dans Claude.ai** : `outillage/` (harnais serveur), `hermes-prompts/` et
`hermes-skills/` (configuration d'agents), `archives/` sauf besoin précis.

---

## Hiérarchie d'autorité

1. `CLAUDE.md` de la racine — **protocole invariant**, prime sur tout le reste ; les
   `CLAUDE.md` locaux de circuit le complètent sans s'y substituer.
2. `00-instructions-projet.md` — pilotage du projet Claude.ai (résume et applique le protocole).
3. `01` à `04` — contexte, état, feuille de route, mode de travail.

En cas de contradiction, `CLAUDE.md` tranche. Si un document de ce dossier le contredit,
**le signaler plutôt que de le suivre** (Action VIGILANCE).

## Entretien de ce dossier

- **Stables** (`00`, `02`, `03`, `01` §1-2, ce README) : à réviser aux jalons majeurs.
- **Vivants** (`01` §3, `04` §B-C, `queue-idees.md`, `choura/`) : à réactualiser souvent —
  une pièce vivante qui n'a pas bougé depuis un mois est une pièce périmée qui s'ignore.
- **Jalons** (`archives/`) : ne se retouchent pas. On en ouvre un nouveau, on ne corrige pas
  l'ancien (Cmd 10).
- Le suivi des **chantiers** ne se tient plus ici : il est au registre du pôle R&D. Ce
  dossier garde ce qui est **sensible** — motifs des décisions, configuration d'agents,
  matière personnelle (§VI).
- Toute refonte passe par le sas `_inbox/` et une session d'intégration, comme une
  intégration normale — jamais d'écriture directe au dépôt depuis Claude.ai.
