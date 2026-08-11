---
title: "Proposition — Phase 3 du pôle R&D : agent de veille infrastructure"
type: proposition-structure
statut: brouillon
cible: "atelier/rd/index.md — État de la phase 1 partielle, §« Non inclus »"
created: 2026-08-11
updated: 2026-08-11
---

# Proposition — Phase 3 : agent de veille infrastructure

> **Statut** : `brouillon`, non visé. Rien de ce qui suit n'est exécuté ; c'est
> un plan présenté avant toute écriture (Cmd 6), intégralement réversible.
> Le verdict d'ouverture et de désignation appartient à Sidy (Cmd 13, et la
> charte du pôle elle-même : « phase 3, sur désignation de Sidy »).

---

## I. Rappel du mandat (verdict d'ouverture du pôle, 2026-08-08)

> « Un des agents sera chargé de veiller à cette tâche spécifique »
> (entretien, développement qualitatif, optimisation de l'infrastructure
> globale hardware/software, émancipation progressive de tout intermédiaire
> de service tiers).

`atelier/rd/index.md` classe explicitement cette désignation hors du
périmètre de la phase 1 partielle, à instruire séparément. Cette note
instruit — elle ne désigne rien.

## II. Ce qui existe déjà et que la veille consoliderait, sans le dupliquer

| Outil | Rôle actuel | Cadence actuelle |
|---|---|---|
| `verifier-invariants.py` | contrôle structurel (frontmatter, annales, liens, étanchéité) | manuel, à la clôture de chaque session (CLAUDE.md, amendement 2026-07-27) |
| `Graphe/generer-cartographie.py --verifier` | anomalies bloquantes/avertissements du graphe de liens | manuel, sur demande |
| `atelier/rd/outillage/detecter-non-tracke.py` (créé 2026-08-11, cette session) | fichiers non trackés par git, classés par circuit | manuel |
| `atelier/rd/cahiers/registre-problemes.md` | journal append-only des symptômes/diagnostics/résolutions | écriture manuelle, au fil de l'eau |

**Constat** : trois scripts déterministes existent déjà et se recoupent
(structure, liens, staging git) mais aucun n'est exécuté automatiquement ni
consolidé en un seul rapport de veille. La phase 3 n'a donc pas à *créer* de
nouveaux capteurs — elle a à décider **qui** relit leurs sorties, **quand**,
et **comment** un signal devient une entrée du registre plutôt qu'un
avertissement silencieux perdu entre deux sessions.

## III. Ce que « veiller » signifierait concrètement (à trancher)

Trois questions distinctes, à ne pas confondre dans un seul verdict :

1. **Qui** — un agent H‍ermes existant (profil dédié ?) ou une routine
   Claude Code côté poste INTÉGRATION (session périodique, pas un agent
   Discord) ? Les deux natures sont très différentes : un agent H‍ermes tourne
   en continu et peut réagir à un événement (ex. commit) ; une routine
   INTÉGRATION suppose une session lancée par Sidy ou planifiée.
2. **Quoi** — périmètre exact de la veille : uniquement les 3 scripts
   déterministes ci-dessus (structure/liens/staging), ou aussi la mesure
   d'empreinte serveur (cf.
   [[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]], instantané
   ponctuel actuellement, jamais répété) ?
3. **Quand un signal devient-il une entrée du registre** — automatique
   (l'agent écrit lui-même dans `registre-problemes.md`) ou l'agent
   *signale*, un humain ou une session INTÉGRATION *consigne* ? La deuxième
   option est plus conforme à Cmd 13 (porte humaine) et à la nature actuelle
   du registre (écriture manuelle réfléchie, pas un flux de logs bruts) —
   mais c'est un arbitrage, pas une évidence.

## IV. Risque à nommer si la veille est confiée à un agent H‍ermes

Un agent de veille qui a accès en écriture au dépôt (même seulement au
registre) élargit la surface de ce qu'un agent de fonction peut modifier sans
repasser par le poste INTÉGRATION — à mettre en regard du cloisonnement
technique H‍ermes actuellement en statu quo (accès FS restreint, retour
d'expérience en cours). Une veille en lecture seule + signalement (Discord,
ou fichier de sortie relu manuellement) évite cette extension de surface ;
une veille en écriture directe au registre la crée délibérément. Point à
trancher explicitement, pas par défaut.

## V. Ce que cette note ne fait pas

Elle ne désigne aucun agent, ne code aucun automatisme, ne modifie aucun
fichier hors `_inbox/`. Elle pose les trois questions (§III) et le risque
(§IV) pour que le verdict de Sidy porte sur des options nommées plutôt que
sur une intention encore vague.
