---
title: "INF-14 — hébergement du rendu sur sidyvision.com : spécification"
type: infrastructure
chantier: INF-14
tags: [atelier, rd, infrastructure, chantier, spec, instrument, hebergement, netlify]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-14-hebergement-rendu-sidyvision/intent]]"
---

# INF-14 — spécification

## Les deux verdicts de Sidy (2026-09-01)

1. **Adresse : `sidyvision.com/instrument`** — un chemin, non un sous-domaine.
2. **INS-09 diffusé tel quel**, avec le marquage des correspondances suggérées.

Les deux ont été rendus contre la recommandation de la machine ; ils sont exécutés tels
quels (Cmd 13 — la porte humaine tranche, la machine prépare). Ce que la recommandation
visait est consigné ci-dessous en contraintes, non en objections.

## Ce que le second verdict engage réellement — vérifié après coup

La recommandation supposait qu'INS-09 laissait en suspens une **correspondance
doctrinale**. Vérification faite dans le rendu : c'est inexact, et le verdict de Sidy
s'en trouve mieux fondé qu'il n'y paraissait.

- Le code porte `// -- Filament : al-Insān al-Kāmil (validé 2026-07-01) --` et
  `// avec le filament al-Insān al-Kāmil, verdict Sidy 2026-07-26`.
- Le nœud renvoie à une fiche `discernement` datée :
  `doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara`.
- L'équivalence est déclarée **établie**, avec sa source.

**Ce qu'INS-09 laisse ouvert est donc le rendu *graphique* du filament — une proposition
visuelle —, non la correspondance qu'il figure.** Diffuser ne publie aucune affirmation
doctrinale non visée : cela publie une mise en forme que Sidy pourra réviser. Le risque
que le Cmd 13 vise n'est pas engagé ici.

Le rendu implémente par ailleurs déjà la distinction du §VII : 17 occurrences d'« établi »,
libellés `SUGGÉRÉ`, styles pointillés, 10 marqueurs 🔍. Le manifeste porte 21 mentions
`etabli` contre 2 `suggere`. La machinerie existe et fonctionne — elle n'est pas à
construire.

## Le fait qui commande le dispositif

**`sidyvision.com` n'a pas de source versionnée.** Le compte GitHub ne porte que deux
dépôts, `wiki` et `instrument` : le site est un **déploiement manuel** Netlify (« drop »).
Ses déploiements ne sont donc reproductibles par personne, et son contenu n'existe qu'à
un seul endroit — le CDN de Netlify.

C'est la contrainte réelle du verdict « chemin plutôt que sous-domaine » : servir
`/instrument` **oblige à toucher au déploiement du site**, là où un sous-domaine ne
l'aurait pas fait. Le travail inclut donc de mettre ce déploiement sous contrôle, ce qui
est un gain en soi — un site qu'on ne sait pas redéployer est un site qu'on ne possède
qu'à moitié, ce qui contredit frontalement la finalité de souveraineté du pôle.

## Comportement observable

```
   dépôt wiki                dépôt instrument            sidyvision.com
   ──────────                ────────────────            ──────────────
   instrument-donnees.yaml
        └─ generer-manifeste.py
                └─ wiki-manifest.json ──poussé──▶ src/wiki-manifest.json
                                                 src/index.html
                                                       │
                                                  Netlify build
                                                       │
                                                       ▼
                                          sidyvision.com/instrument/
```

- `sidyvision.com/` continue de servir la page actuelle, **inchangée à l'œil**.
- `sidyvision.com/instrument/` sert le rendu.
- Le sens unique n'est pas rompu : le site est un consommateur de plus. Rien ne remonte.
- **Aucun identifiant Netlify ne vit côté wiki** : c'est Netlify qui tire depuis GitHub,
  le wiki ne pousse que vers le dépôt frère.

## Critères d'acceptation

1. `curl -sI https://sidyvision.com/` renvoie `200` et la page actuelle, **octet pour
   octet identique** à la capture de référence prise avant toute intervention.
2. `curl -sI https://sidyvision.com/instrument/` renvoie `200`.
3. `curl -s https://sidyvision.com/instrument/wiki-manifest.json | python3 -m json.tool`
   est du JSON valide et annonce 46 nœuds.
4. Une poussée sur `main` du dépôt `instrument` déclenche un redéploiement, et la
   modification est visible en ligne — sans intervention manuelle.
5. Le déploiement du site est **reproductible depuis le serveur**, sans clic dans une
   interface web que personne n'aurait documentée.
6. La page racine et le rendu ne partagent aucun état : le rendu ne peut pas casser la
   page d'accueil.

## Cas limites

- **Perte de la page actuelle.** Elle n'existe qu'en un exemplaire, sur le CDN. Une
  capture de référence est prise et versionnée **avant** toute manipulation : sans cela,
  une erreur de déploiement effacerait un contenu dont il n'existe aucune sauvegarde.
  C'est le risque principal de ce chantier, et il naît du choix « chemin ».
- **Anomalie de forme de la page actuelle** : deux `<!DOCTYPE html>` et deux `<html>`
  imbriqués (un document collé dans un autre). Elle est **conservée telle quelle** — la
  reproduire à l'identique est la seule garantie que rien n'a bougé (Cmd 12 : on
  rapporte, on ne répare pas d'office ; la réparation sera un chantier distinct si Sidy
  la veut).
- **Chemin relatif du manifeste** : `fetch('wiki-manifest.json')` est relatif. Servi
  sous `/instrument/`, il résout en `/instrument/wiki-manifest.json`. La contrainte de
  fraternité de dossier (INF-13) tient donc, à condition que l'URL se termine par `/`.

## Ce qui reste `to-source`

Rien. Chantier d'infrastructure.
