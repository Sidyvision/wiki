---
title: "Proposition — Phase 3 du pôle R&D : agent de veille infrastructure"
type: proposition-structure
statut: brouillon
cible: "atelier/rd/index.md — État de la phase 1 partielle, §« Non inclus »"
created: 2026-08-11
updated: 2026-08-11
---

# Proposition — Phase 3 : agent de veille infrastructure

> **Statut** : `brouillon`, non visé. Les trois questions du §III sont
> tranchées (verdicts Sidy du 2026-08-11, ci-dessous) ; ouverture effective
> (désignation de l'agent, écriture du prompt/de la routine) non encore
> exécutée — c'est un plan présenté avant toute écriture (Cmd 6),
> intégralement réversible. Le verdict d'ouverture définitive appartient à
> Sidy (charte du pôle : « phase 3, sur désignation de Sidy »).

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

## III. Ce que « veiller » signifierait concrètement (tranché, 2026-08-11)

Trois questions distinctes, tranchées séparément — verdicts Sidy du
2026-08-11 :

1. **Qui** — **routine côté poste INTÉGRATION** (session Claude Code
   périodique/planifiée sur le serveur), **pas un agent H‍ermes dédié**.
   Motif retenu : cohérent avec le statu quo du cloisonnement technique
   H‍ermes (accès FS restreint, retour d'expérience en cours — cf. mémoire
   « Cloisonnement technique H‍ermes ») ; réutilise un poste déjà cadré par le
   protocole plutôt que d'ouvrir une nouvelle couche à superviser.
2. **Quoi** — les 3 scripts déterministes **et** la mesure d'empreinte
   serveur (cf.
   [[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]], instantané
   ponctuel actuellement). **Point resté ouvert** : rendre cette mesure
   récurrente est un chantier à part (fréquence de prise, stockage des
   séries, seuils d'alerte) — non instruit par cette note, à traiter avant
   que la veille ne l'inclue effectivement.
3. **Quand un signal devient-il une entrée du registre** — **signalement via
   Discord**, jamais d'écriture directe dans `registre-problemes.md`. La
   routine rapporte le signal sur un canal Discord existant (allowlist
   stricte, §VIII.8 de CLAUDE.md) ; c'est Sidy, ou une session INTÉGRATION
   sur sa demande, qui rédige et consigne l'entrée. Écarte du même geste la
   question du push non supervisé (une consignation automatique aurait
   obligé à trancher si la routine committe/pousse sans relecture — §IX.5,
   Cmd 13) : le signalement Discord ne touche jamais au dépôt lui-même,
   aucune dérogation à la porte humaine n'est nécessaire.

## IV. Risque à nommer si la veille est confiée à un agent H‍ermes

Un agent de veille qui a accès en écriture au dépôt (même seulement au
registre) élargit la surface de ce qu'un agent de fonction peut modifier sans
repasser par le poste INTÉGRATION — à mettre en regard du cloisonnement
technique H‍ermes actuellement en statu quo (accès FS restreint, retour
d'expérience en cours). Une veille en lecture seule + signalement (Discord,
ou fichier de sortie relu manuellement) évite cette extension de surface ;
une veille en écriture directe au registre la crée délibérément. Point à
trancher explicitement, pas par défaut.

## V. Ce que cette note ne fait pas (et ce qui reste à faire)

Le §III est tranché, mais cette note ne désigne encore aucun agent, ne code
aucun automatisme, ne modifie aucun fichier hors `_inbox/`. Restent à
instruire séparément, avant toute écriture (Cmd 6) :

- la formulation exacte de la routine INTÉGRATION (fréquence, déclencheur —
  planifiée ou lancée par Sidy, contenu du rapport) ;
- le canal Discord de signalement (lequel, allowlist — §VIII.8) ;
- le chantier laissé ouvert au §III.2 (récurrence de la mesure d'empreinte
  serveur) avant qu'il n'entre effectivement dans le périmètre de veille.

Le risque nommé au §IV (surface d'écriture d'un agent H‍ermes) reste sans
objet tant que le §III.1 (routine INTÉGRATION, pas d'agent H‍ermes dédié)
n'est pas rouvert.
