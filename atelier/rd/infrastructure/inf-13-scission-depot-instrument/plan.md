---
title: "INF-13 — scission du dépôt Instrument : plan"
type: infrastructure
chantier: INF-13
tags: [atelier, rd, infrastructure, chantier, plan, instrument, git]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-13-scission-depot-instrument/spec]]"
---

# INF-13 — plan

> **Statut : `vise`** — plan approuvé par Sidy le 2026-09-01, exécuté dans la même
> session. Les étapes marquées **différé** ne le sont pas et attendent un verdict
> distinct (Cmd 13).

## Étapes

**0. Pré-vol du manifeste** — régénérer vers une sortie temporaire et comparer au
manifeste versionné, *avant* toute écriture. Vérifier après coup qu'un script écrit
dans la même session sait exécuter son propre mode à blanc ne prouverait rien. Un
dépôt neuf ne se fonde pas sur un artefact qu'on n'a pas regardé.
→ *Fait le 2026-09-01 : divergence limitée aux deux tampons de provenance, contenu
identique.*

1. Branche `chantier/triptyque-sdlc-et-scission-instrument` (`main` est protégée).
2. **Commit A** — la convention du triptyque seule. Elle tient debout sans la
   scission : si celle-ci est refusée, rien n'est à défaire.
3. **Commit B** — les amendements de non-silence (protocole racine,
   `atelier/CLAUDE.md`, changelog), le stub `deprecated`, le script de publication.
   *Le wiki dit la scission avant que la chose pointée existe au-dehors* : ouvrir un
   dépôt tourné vers l'extérieur que l'histoire du wiki ne référence pas encore
   laisserait un artefact orphelin en cas de refus.
4. `gh repo create Sidyvision/instrument --private`, clone en `/root/instrument`.
   **Pas de sous-module** : écarté délibérément — coût quotidien élevé, et le sens
   unique n'a besoin d'aucun couplage git entre les deux dépôts.
5. Squelette, copie du prototype en `src/index.html`, manifeste frère, push.
6. Protection de `main` calquée sur PRO-01, puis **contrôle par appel d'API**.
7. **différé** — automatisation : workflow wiki poussant le manifeste vers le dépôt
   frère via secret PAT. Le jeton d'écriture croisée engage (Cmd 13) ; l'art. 4
   Sashimono veut le montage à blanc avant le définitif.

## Fichiers touchés

| Fichier | Nature |
|---|---|
| `CLAUDE.md` (racine), §II et §VII | modification — mention du dépôt frère |
| `atelier/CLAUDE.md`, *Structure du circuit* | modification — ligne de coupe |
| `meta/protocole-archives/changelog-CLAUDE.md` | ajout d'entrée (Cmd 10) |
| `atelier/rd/instrument/instrument-prototype.html` | **copié** puis remplacé par un stub `deprecated` (jamais supprimé) |
| `atelier/rd/outillage/publier-manifeste-instrument.sh` | création |
| `atelier/rd/registre-chantiers.md` | modification — INF-13 ouvert |

## Vérification

Les huit critères du `spec.md`, chacun par une commande nommée :
`gh api repos/Sidyvision/instrument` (1), `gh api .../branches/main/protection` (2),
serveur local + chargement de page (3), lecture du stub (4), `grep` sur les deux
protocoles (5, 6), double exécution du script sur un dépôt inchangé (7),
`gh api repos/Sidyvision/instrument/actions/secrets` renvoyant zéro secret (8).
Puis `python3 verifier-invariants.py --racine /root/wiki` en clôture (§VII).

## Points de retour à l'humain (Cmd 13)

- Le jeton PAT et l'automatisation — **différés**.
- Le passage en public.
- Le choix d'hébergement du rendu.

## Journalisation

`atelier/annales.md` (le chantier) et `meta/meta-annales.md` (l'amendement du
protocole racine et l'ouverture d'un dépôt frère relèvent aussi du Domaine Réservé),
plus la ligne INF-13 du registre — même passe (Cmd 9).
