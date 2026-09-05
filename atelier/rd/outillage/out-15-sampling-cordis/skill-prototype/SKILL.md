---
title: "OUT-15 — Échantillon A : skill spatiotemporal-composability (sampling Cordis)"
type: outillage
chantier: OUT-15
created: 2026-09-05
updated: 2026-09-05
tags: [atelier, rd, outillage, sampling, cordis, skill, composabilite, reversible]
sources:
  - "to-source"   # eSaadster/spatiotemporal-composability-skill — SPDX None, réappropriation conceptuelle
  - "to-source"   # inso1337/cordis-wasm — SPDX None, réappropriation conceptuelle
  - atelier/rd/veille/cordis/methodes.md
  - atelier/rd/veille/cordis/equations.md
links:
  - "[[atelier/rd/outillage/2026-09-05_sampling-fonction-studio-cordis]]"
  - "[[atelier/rd/registre-chantiers]]"
name: spatiotemporal-composability
description: "Concevoir des systèmes et agents où chaque capacité est un composant isolé, montable à chaud, déclarant ses dépendances et ses services, dont le déchargement revert intégralement ses effets. Utiliser quand on construit un système plugin, un registre d'outils, un framework modulaire, un agent à composants interchangeables, ou qu'on veut rendre un composant existant hot-swappable."
---

# Composabilité spatio-temporelle

Construire des logiciels et des agents de sorte que **chaque capacité soit un composant de premier ordre qu'on peut monter, recomposer et démonter à l'exécution** — sans redémarrage, sans résidu, sans dépendance non déclarée. Cela inclut les adapteurs de modèle, les registres d'outils, les journaux de session, les sandboxes, les boucles d'orchestration, et l'interface utilisateur. On ne change jamais le code pour modifier ce qu'un système *est*. On édite sa configuration, et le système se rebranche en toute sécurité.

La discipline repose sur deux garanties. Tout le reste en découle :

- **Composabilité temporelle** : décharger un composant **revert intégralement** tout ce qu'il a modifié. Chaque effet retourne son propre inverse. Le runtime accumule ces inverses. Le déchargement est **dérivé du chargement**, jamais écrit en parallèle.
- **Composabilité spatiale** : un composant **déclare** les services dont il a besoin. Le runtime les résout et les **re-résout** réactivement. Un composant s'active quand ses services déclarés apparaissent, se désactive quand ils se retirent. Un fournisseur survit toujours à ses consommateurs.

Un système qui manque l'une de ces garanties est un système à redémarrage déguisé en plugin.

---

## Le contrat de composant

Un composant a trois déclarations. Chaque capacité qu'on construit doit se réduire à cette forme. (Terminologie : un **coeffet** est une dépendance déclarée. Un **effet réversible** est une mutation qui porte son propre inverse.)

| Champ | Rôle | Formalisme Cordis |
|-------|------|-------------------|
| `inject` | les services typés qu'il **exige** | spécification de coeffects |
| `provide` | les services typés qu'il **installe** | provision |
| `apply` | les effets qu'il exécute tant qu'il est actif, chacun accompagné de son inverse | fonction d'effet témoin |

Un **service** est une capacité typée, nommée, accédée via une clé. La clé porte son type (contrat entre fournisseur et consommateur), une équivalence d'observation, et des opérations réversibles.

Un **filament** est une instance en cours d'exécution d'un composant. Il porte un contexte dérivé et un état de cycle de vie. Un composant peut avoir de multiples filaments (par exemple plusieurs instances sandbox). Un composant qui fournit des services n'a qu'un filament à la fois dans chaque réalme.

---

## Les cinq règles qui font tout le travail

### Règle 1 : tout effet est réversible

Une mutation a le type `état → état × (état → état)`. Elle retourne le nouvel état **et la fonction qui annule le changement**. Le runtime accumule ces inverses. Décharger un composant les exécute en ordre LIFO.

Quatre conséquences sont des exigences de conception :

1. **L'appelant fournit l'inverse là où l'effet se produit.** L'appelant sait ce qu'il a changé. Le runtime ne le reconstruit jamais après coup. `ouvrir()` retourne `fermer`, `enregistrer()` retourne `désenregistrer`, `générer()` retourne `tuer`.
2. **Les inverses composites se composent en ordre inverse.** Si le chargement fait A puis B, le déchargement fait annuler-B puis annuler-A. Précéder chaque inverse d'un accumulateur. Ne jamais écrire un `décharger()` qui énumère les étapes de nettoyage à la main.
3. **La récupération est une garantie structurelle.** Un inverse oublié est une **défaillance d'interface**, parce que l'opération n'a pas d'inverse correspondant.
4. **Les effets peuvent être étagés.** Une activation est un **itérateur d'effets**. Chaque itération effectue un pas réversible et rend une continuation. C'est une continuation délimitée réifiée, la structure que les générateurs fournissent. Le runtime peut observer le monde et dévier entre les itérations. La granularité d'abandon est une frontière d'iteration, pas plus fin.

Tout effet de bord doit passer par cette primitive. Le registrer un outil, ouvrir une connexion modèle, s'abonner à un bus, générer un sous-processus, monter une vitrine d'interface, démarrer un minuterie. Si une opération ne peut pas être exprimée comme `état-nouvel + inverse`, elle n'appartient pas à l'intérieur de la frontière.

### Règle 2 : toute dépendance est un service déclaré et typé

Un composant obtient ce dont il a besoin en **le déclarant dans `inject` et le lisant depuis le contexte**. Il ne fouille jamais dans un registre global, un singleton, ou les entrailles d'un parent.

- **L'accès non déclaré est une erreur.** Lire une clé non déclarée échoue au point d'utilisation. Le code qui localise un service retourne `undefined` plus un `if (!x) return`. Ce modèle signale que le composant n'a pas déclaré le service avant que quoi que ce soit ne s'exécute.
- **Identifier le fournisseur.** Deux fournisseurs qui installent des valeurs égales restent deux fournisseurs différents. La résolution enregistre *qui* fournit chaque clé. Remplacer un fournisseur par un identique re-résout quand même ses consommateurs.
- **L'activation attend la satisfaction.** Un composant ne s'active que quand chaque clé de son `inject` a un fournisseur actif. Une dépendance manquante laisse le composant inactif. Il ne s'active pas pour crasher à la première utilisation.

### Règle 3 : un contexte, une source de vérité

Tout état qu'un composant peut toucher vit dans un **contexte** à trois parties : l'état courant, l'accumulateur d'inverses, et la table de services typés. L'accumulateur définit ce que le déchargement doit exécuter. La table définit ce que `inject` et `provide` lisent et écrivent.

Chaque interaction entre un composant et le système passe par ce contexte. Un composant ne jamais écrit dans une variable globale, une carte au niveau module, ou le champ privé d'un autre composant. Il écrit dans son propre contexte, qui est l'environnement partagé.

Les contextes forment un arbre. Un composant dérive son contexte de son parent. La dérivation est bon marché et réversible par abandon. Les ajustements de l'enfant disparaissent quand l'enfant se décharge. Le chargement d'un composant branche son contexte dans l'arbre. Le déchargement le retire.

### Règle 4 : classifier chaque changement et laisser la classification piloter le cycle de vie

La vue cible pilote le cycle de vie d'un composant. Les appels impératifs `démarrer()` et `arrêter()` ne le pilotent pas. La vue cible tient deux faits : si le filament est réformé, et quel filament fournit chaque clé déclarée.

Chaque changement de table de services est classifié par rapport à la déclaration `inject` de chaque dépendant :

- **activation** : la dépendance est devenue satisfaite parce qu'une clé est apparue,
- **désactivation** : la dépendance est devenue non satisfaite parce qu'une clé s'est retirée,
- **neutre** : aucune dépendance déclarée n'a changé.

L'activation déclenche le chargement. La désactivation déclenche le déchargement. Le neutre ne déclenche rien. C'est le mécanisme de réactivité. On n'écrit pas à la main « quand le modèle change, fais X ». On déclare `inject: [modèle]`, et le runtime recharge quand le fournisseur du modèle change.

### Règle 5 : composer à la couche de configuration

La *composition* du système (quels composants existent, avec quelle configuration, dans quel ordre) est des **données**, pas du code. Une configuration est un arbre d'entrées. Chaque entrée contient `(identifiant/URL du composant, isolation, interception, configuration, désactivé)`.

Un changement de configuration réconcilie le système en cours :

- ajouter une entrée → instancier un filament,
- retirer une entrée → revertir ses effets et le retirer,
- changer la `configuration` → laisser le composant comparer les valeurs et recharger seulement après un changement matériel,
- basculer `désactivé` → décharger ou recharger.

Grâce à la **confluence**, l'état au repos est une fonction de la configuration *finale* seule. L'orchestrateur peut réconcilier avidement ou paresseusement, dans n'importe quel ordre. Il converge vers l'état d'un chargement from-scratch de la configuration finale.

Le remplacement de module à chaud (HMR) est un cas particulier : remplacer le code d'un composant = disposer l'ancien filament + instancier un nouveau filament depuis le module rechargé. La disposition revert les effets de l'ancien filament. Aucune frontière d'acceptation rédigée à la main n'est requise.

---

## Commutativité et indépendance : l'obligation du fournisseur

La règle 1 rend chaque effet réversible. L'indépendance rend les composants entrelacés sûrs. D'autres composants peuvent déplacer l'état entre le moment où un composant enregistre un inverse et le moment où cet inverse s'exécute. La commutation détermine si l'inverse annule toujours son propre effet à l'état déplacé.

Un fournisseur qui ne peut pas garantir la commutativité doit **déclarer l'ordre**. Un composant qui déclare `inject: [clé-X]` accepte que la valeur de `clé-X` puisse changer entre ses itérations. Le runtime notifie ; le composant se recharge. C'est la réactivité.

---

## L'isolation par réalmes

Deux composants peuvent demander la même clé mais être liés à des valeurs différentes selon leur réalme. La résolution deux-couches `clé → ρ(clé) → σ(ρ(clé))` assure l'isolation spatiale.

**Avantage** : pas de conflit de noms, pas de dépendance accidentelle. Chaque composant vit dans son propre espace de services, même quand les clés sont identiques.

---

## Le cycle de vie — état inertiel et HMR

Le composant passe par les états :

    INACTIF --L-Begin--> RECHARGEMENT --L-Finish--> ACTIF
        ^                      | L-Divert / L-Raise       | L-Leave
        +---- L-Unload --- DÉCHARGEMENT <----------------+

- **Inertie** (§4.3.3 du papier) : une itération en vol toujours atterrit. Le gap async entre les itérations est le moment où le monde peut changer et L-Divert se déclenche, annulant exactement les étapes complétées (rollback partiel aux frontières d'itération).
- **Provisions étagées** : les exports `provide:` sont collectés à l'instanciation mais publiés dans Σ seulement à L-Finish — un filament en transition ne fournit rien, donc aucun dépendant ne peut s'activer contre un fournisseur à moitié installé.
- **L-Raise = trappe** (§4.3.4) : le filament récupère avant d'enregistrer, arrivant à Inactif(ξ) sans rien installé. Les fibres échouées sont **retenues** de L-Begin jusqu'à un `réessayer` explicite de l'orchestrateur.
- **Garde sur L-Unload** (Thm 63) : un fournisseur qui quitte cesse de résoudre immédiatement, mais reste appelable par les vues engagées de ses dépendants ; ses propres inverses — potentiellement async — ne s'exécutent qu'après que chaque dépendant a épuisé les siens.

---

## Quand cet outil est le mauvais

- Un script, un job one-shot, ou un système sans reconfiguration à l'exécution. La composition statique suffit.
- Des composants qui partagent un état mutable en dehors d'un service déclaré. Cet état est hors du modèle et de ses garanties.
- Des dépendances dont les interfaces dérivent entre versions indépendantes. L'identité de clé seule les lie. Ajouter de l'espace de noms, des dépendances de peer, ou des vérifications structurelles. Le versionnement reste un problème ouvert.
- Des systèmes temps-réel ou à mémoire fixe où le coût de suivi d'inverses est trop élevé. Mesurer d'abord. L'overhead est faible dans la plupart des systèmes, mais il n'est pas nul.

---

## La règle empirique

> Si vous ne pouvez pas le démonter et récupérer votre état, ce n'est pas un composant. C'est une charge avec une API plugin. Faire déclarer à chaque capacité ce dont elle a besoin, revertir ce qu'elle fait, et vivre ou mourir par la configuration. Monter, recomposer, et étendre à la couche de configuration.

---

*Provenance : cet échantillon réapproprie les concepts de « A Programming Paradigm for Spatiotemporal Composability » (Shi, Zhang, Cui — Peking Univ / DeepSeek-AI), à travers la skill `spatiotemporal-composability` de eSaadster et le runtime `cordis-wasm` de inso1337. Les garanties invoquées (récupération exacte, ordonnancement, progression, confluence, indépendance) sont des résumés informels. Les définitions et preuves vivent dans le papier original.*

*Statut license : les deux repos source n'ont aucune license déclarée (SPDX None). Cette fiche est une réappropriation conceptuelle documentée, pas une copie du code. La traçabilité du isnad est portée par cette fiche elle-même et par `atelier/rd/outillage/2026-09-05_sampling-fonction-studio-cordis.md`.*
