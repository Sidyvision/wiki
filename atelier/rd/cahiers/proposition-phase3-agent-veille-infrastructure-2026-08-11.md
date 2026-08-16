---
title: "Proposition — Phase 3 du pôle R&D : agent de veille infrastructure"
type: meta
statut: brouillon
cible: "atelier/rd/index.md — État de la phase 1 partielle, §« Non inclus »"
created: 2026-08-11
updated: 2026-08-16
tags: [atelier, rd, phase3, hermes, veille, infrastructure]
sources: []
links: ["[[atelier/rd/index]]"]
---

# Proposition — Phase 3 : agent de veille infrastructure

> **Statut** : `brouillon`, non visé. Le §V (canal, fréquence, heure, nature
> du rapport) est tranché par Sidy. Le §III.1 (qui porte la veille), tranché
> une première fois le 2026-08-11 pour le poste INTÉGRATION, a été **rouvert
> le même jour** : la veille est réattribuée au **Studio Sound Engineer**
> (agent H‍ermes, position 9 de la roue zodiacale) — voir §III.1
> « Réouverture ». Cette réattribution **rouvre à son tour** le mécanisme
> technique proposé au §VI (conçu pour l'ancien verdict), sans rouvrir le
> §III.3 (signalement Discord seul, jamais d'écriture directe — inchangé
> quel que soit l'exécutant). L'écriture elle-même (script, webhook,
> crontab, extension du prompt d'agent) reste hors périmètre de cette note
> (§VI) — un plan présenté avant toute écriture (Cmd 6), intégralement
> réversible. Le verdict d'ouverture définitive (passage à l'écriture)
> appartient à Sidy.
>
> **Note architecturale (2026-08-11)** : Cette note documente une transition 
> du flux alchimique/théurgique adopté 
> ([[doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire|trois 
> territoires]]). Le Discernement (fiches 16/17 sur extension zodiacale des 
> 12 agents) devient R&D/Laboratoire en attente d'exécution : un chantier 
> exploratoire (statut_experience: exploratoire) sous supervision de Sidy. 
> La transition ne sera complète — passage en Théorie adoptée ou Archivage — 
> que quand le Maître valide l'exécution effective et ses résultats.

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

1. **Qui** — ~~**routine côté poste INTÉGRATION** (session Claude Code
   périodique/planifiée sur le serveur), **pas un agent H‍ermes dédié**.
   Motif retenu : cohérent avec le statu quo du cloisonnement technique
   H‍ermes (accès FS restreint, retour d'expérience en cours — cf. mémoire
   « Cloisonnement technique H‍ermes ») ; réutilise un poste déjà cadré par le
   protocole plutôt que d'ouvrir une nouvelle couche à superviser.~~

   **Réouverture (2026-08-11, même jour)** : Sidy relie explicitement ce
   chantier à l'extension de rôle des 12 agents H‍ermes sur calibrage
   zodiacal (fiches `meta/projet-unifie/16-...` et `17-...`) et attribue la
   veille infrastructure à **l'agent le plus approprié** de la roue.
   Cartographie effectuée (les 12 positions et leur force de correspondance,
   cf. `doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`,
   clos 2026-07-14) : aucun des 12 rôles n'est dédié à l'infrastructure
   informatique — les deux correspondances solides (position 4 Cancer,
   Administration & Legal ; position 10 Capricorne, Protocol Guardian) sont
   des registres gouvernance/conformité, pas infrastructure matérielle ou
   logicielle. Le seul rôle de registre technique/matériel est la
   **position 9 (Sagittaire), Studio Sound Engineer**
   (`meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md`,
   correspondance « cohérente, non prouvée », archétype Faiseur) — c'est
   celui-ci que Sidy désigne. Motif retenu : extension d'un mandat déjà
   technique/pédagogique existant, plutôt que création d'une 13e position
   hors roue — cohérent avec la règle de gouvernance déjà posée (fiche 16 :
   « la roue zodiacale est l'étage principiel, les rôles en dérivent, jamais
   l'inverse ») puisqu'aucun nouveau rôle n'est créé, un rôle existant est
   étendu. **Ce que cette réouverture ne fait pas encore** : elle ne touche
   ni le prompt d'agent en production
   (`hermes-prompts/09-studio-sound-engineer.md`) ni le brouillon
   d'extension zodiacale hors dépôt
   (`/root/brouillons-prompts-zodiaque/09-studio-sagittarius.md`) —
   l'extension effective du mandat est un acte séparé, à confirmer
   explicitement (Cmd 6), et conditionnée par le chantier nommé ci-dessous.
   **Accès FS/exécution — tranché (2026-08-11)** : l'accès du Studio Sound
   Engineer aux scripts déterministes (`verifier-invariants.py`,
   `Graphe/generer-cartographie.py --verifier`, `detecter-non-tracke.py`,
   relevé serveur) est désormais accordé — le cloisonnement technique
   H‍ermes ne bloque plus ce chantier (statu quo levé). Gouvernance : par défaut
   régime strict (demande Discord → validation Sidy → exécution) ; auto-accept
   mode optionnel, activable ad hoc par Sidy pour une période donnée
   (similaire au mode auto-accept du plan de Claude Code), qui se désactive
   automatiquement après — cohérent avec Cmd 13 (porte humaine), traçabilité
   Discord intégrale.

   **Registre alchimique** (transition Discernement → R&D) : 
   Cette désignation du Studio Sound Engineer incarne le passage du Plan théurgique 
   (hypothèse : extension zodiacale du rôle) à la mise en œuvre concrète 
   (Laboratoire : exécution du prompt étendu). L'agent du Sagittaire reçoit 
   l'Intention (pédagogie + veille infrastructure) et y répond par l'Acte — 
   reste sous régime de non-finalité (exploratoire) jusqu'à verdict de Sidy 
   sur l'adéquation du résultat.
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

**Clause (2026-08-11, réouverture du §III.1)** : la réattribution de la
veille au Studio Sound Engineer (position 9) ne rouvre PAS ce risque tel
quel — elle ne rouvre pas non plus le §III.3, resté intact : le
signalement passe toujours et uniquement par Discord, jamais par une
écriture directe au registre, quel que soit l'exécutant (poste INTÉGRATION
ou agent H‍ermes). C'est cette règle inchangée, et non l'identité de
l'exécutant, qui continue de contenir le risque nommé ici.

## V. Désignation effective (tranchée, 2026-08-11)

Deux points instruits avec Sidy en séance, sur les deux volets laissés ouverts
par le §III :

1. **Déclencheur de la routine** — **planifiée par cron**, et non lancée à la
   demande. Choix assumé malgré le coût nommé lors de l'arbitrage (nouvelle
   surface : un job headless sur le serveur, hors session supervisée,
   précédent jusqu'ici réservé au gateway H‍ermes via `DISCORD_HOME_CHANNEL`).
   Le risque « qui relit si personne n'est en session au moment où le cron
   tourne » se referme de lui-même par construction du §III.3 : la routine ne
   touche jamais au dépôt, elle **signale sur Discord** — la lecture différée
   par Sidy (ou une session INTÉGRATION sur sa demande) est le mode de
   fonctionnement prévu, pas un angle mort.
2. **Canal Discord** — **nouveau canal dédié**, plutôt que de réutiliser
   `#gardien` (dont le mandat réel, vérifié dans son prompt
   `meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`, est la
   conformité doctrinale/éthique des actes commerciaux du label — doctrine du
   don, anti-accumulation — et non la veille technique). Garde l'étanchéité de
   sens entre vigie doctrinale et vigie infrastructure plutôt que de la
   dissoudre par économie d'un canal.

## VI. Ce que cette note ne fait pas encore (et ce qui reste à faire)

Le §III et le §V sont tranchés en principe, mais cette note ne code encore
aucun automatisme et ne modifie aucun fichier hors `_inbox/`. Restent à
instruire séparément, avant toute écriture (Cmd 6) :

- ~~le nom exact du nouveau canal~~ — **tranché (2026-08-11)** : canal
  `#infrastructure` créé par Sidy côté Discord. Reste à inscrire à
  l'allowlist (§VIII.8) au moment de l'écriture du mécanisme de post ;
  l'identifiant numérique du canal (snowflake Discord) n'est **pas** consigné
  ici, par cohérence avec `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`
  qui ne fixe que les noms lisibles — l'identifiant vit dans la configuration
  d'exécution locale (`.env`/`config.yaml`), jamais dans le dépôt versionné.
- ~~la fréquence exacte du cron~~ — **tranchée (2026-08-11)** : **quotidienne,
  12:00 (midi)**, par analogie assumée avec le « Rapport du matin » déjà
  envisagé côté H‍ermes/gardien (cf.
  `meta/projet-unifie/04-sessions-par-fonction-et-backlogs.md`).
- ~~le contenu exact du rapport~~ — **tranché en nature (2026-08-11)** : un
  rapport de **suggestion, révision, développement** — au-delà du simple
  constat brut des 3 scripts déterministes, la routine peut proposer des
  pistes (ce qui mérite révision, ce qui pourrait être développé). Ce
  caractère suggestif **renforce**, plutôt qu'il n'assouplit, la règle déjà
  tranchée au §III.3 : aucune suggestion n'est journalisée d'office — **toute
  entrée du registre passe par la validation de Sidy avant consignation**, le
  rapport Discord restant un projet soumis, jamais une écriture actée.
- ~~format précis et mécanisme technique de post~~ — **tranchés par
  délégation (2026-08-11)** : Sidy s'en remet à la proposition ci-dessous, à
  charge d'optimiser après une première expérience directe (`statut_experience:
  exploratoire`, régime propre à `rd/`, §V.a de CLAUDE.md) :
  - **Format** — en-tête (date, heure d'exécution) ; section 1 résumé
    `verifier-invariants.py` (erreurs/avertissements, delta vs baseline
    connue) ; section 2 résumé `Graphe/generer-cartographie.py --verifier`
    (anomalies bloquantes/avertissements, delta) ; section 3
    `detecter-non-tracke.py` (décompte par circuit, alerte si
    `hors-circuit-inconnu`) ; section 4 empreinte serveur (RAM/disque/swap,
    snapshot simple — la récurrence formelle de cette mesure reste le
    chantier ouvert ci-dessous) ; section 5 « Suggestions » (1 à 3 pistes de
    révision/développement en texte libre, explicitement marquées comme
    propositions non actées, jamais comme constats).
  - ~~**Mécanisme** — **webhook Discord simple** sur le canal
    `#infrastructure`, et non un agent H‍ermes ni un bot dédié : un webhook
    est spécifique au canal, ne nécessite ni token de bot ni gateway, et
    n'ouvre donc aucune surface côté H‍ermes (cohérent avec le §III.1). Un
    script Python dédié (`atelier/rd/outillage/`, à nommer) orchestre les 3
    scripts déterministes + le relevé serveur, compose le texte, et poste au
    webhook ; l'URL du webhook est un secret et vit en configuration locale
    hors dépôt (même régime que les identifiants Discord, §VIII.5), inscrite
    à l'allowlist du canal au moment de l'écriture (§VIII.8).~~

    **Mécanisme — tranché (2026-08-11)** : le webhook+script tiers proposé
    initialement pour le poste INTÉGRATION n'a plus lieu d'être — l'agent
    Studio Sound Engineer compose et poste le rapport lui-même via le canal
    `#infrastructure` (pas de tiers, traçabilité agent natives via les
    empreintes H‍ermes). Flux : l'agent orchestre les 3 scripts déterministes
    + relevé serveur, compose le texte selon le format en 5 sections
    ci-dessus, puis demande via Discord : « Rapport de veille — validez ? »
    (ou directe si auto-accept mode actif). Sidy valide (ou auto-accept
    exécute), l'agent poste au canal. Toute action est tracée Discord (audit
    trail intégrale, natif agent H‍ermes). Pas d'écriture au registre par
    l'agent (inchangé, §III.3) — le rapport Discord est le signalement ;
    Sidy (ou session INTÉGRATION) opère la consignation au registre si
    actionnable. Le format en 5 sections demeure la cible de contenu
    (indépendant du mécanisme).
  - **Ce que cette transition ne fait pas encore** : elle n'est qu'une
    documentation du changement — l'extension effective du prompt du Studio
    Sound Engineer (`hermes-prompts/09-studio-sound-engineer.md`) reste un
    acte séparé, non exécuté par cette note (Cmd 6), à confirmer explicitement
    avant toute modification du prompt d'agent en production.
- **le chantier laissé ouvert au §III.2** (récurrence de la mesure d'empreinte
  serveur : fréquence de prise, stockage des séries, seuils d'alerte) avant
  qu'il n'entre effectivement dans le périmètre de veille. **Point resté 
  dépendant** : après la réouverture du §III.1, ce chantier ne peut s'instruire
  que si le nouveau mécanisme (agent Studio Sound Engineer) a d'abord été mis
  en place — l'intégration de la mesure récurrente dépend de son exécutant.

---

## Récapitulatif — Chantiers ouverts après la réouverture (2026-08-11)

Le §III et le §V sont maintenant tranchés en principe (voir tableaux ci-dessous).
Restent à instruire séparément, avant toute écriture effective du mécanisme
(Cmd 6) :

| Chantier | Bloqage | Responsable | Statut |
|---|---|---|---|
| **Extension prompt agent 09** | Cmd 6 : plan avant modification | Sidy (validation) | ~~À instruire~~ **Fait (2026-08-16)**, voir §Mise à jour |
| **Accès FS/exécution agent 09** | Déf. du cloisonnement H‍ermes | Décision architecturale | Tranché (2026-08-11, §III.1) |
| **Nouveau mécanisme d'éxécution** | Dépend du cloisonnement ↑ | Conception R&D | Prompt étendu ; `hermes cron create` + canal Discord `#infrastructure` restent à créer (porte humaine) |
| **Récurrence empreinte serveur** | Dépend du mécanisme ↑ | R&D + choix opérationnel | À instruire (inchangé) |

## Mise à jour (2026-08-16)

Extension effective du prompt réalisée :
`meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md`, section
« Infrastructure veille mandate ». Le registre couvert s'élargit au-delà des
3 scripts + empreinte serveur prévus ici : ajout d'un registre H‍ermes-Terminal
(intégrité bind mounts Mehdi, santé des 12 gateways, staleness `_inbox/`),
motivé par une session distincte (canal Telegram pour Mehdi + mandat d'audit),
où un bind mount `karubi-mehdi.md` a été trouvé figé sur un inode périmé sans
détection systématique préexistante. Format, cadence, canal, gouvernance
Discord-Validation : inchangés par rapport aux §V/§VI ci-dessus. Reste hors
périmètre de ce geste (Cmd 13, porte humaine) : `hermes cron create` côté
profil `studio`, création du canal Discord `#infrastructure` et son
allowlisting, `hermes -p studio gateway install/restart`. Statut de cette note
laissé à `brouillon` (comme pour l'intégration du 2026-08-12) : le prompt est
étendu, le mécanisme d'exécution ne l'est pas encore.

Le risque nommé au §IV (surface d'écriture d'un agent H‍ermes) est désormais 
contenu par le §III.3 (signalement Discord uniquement, jamais d'écriture 
directe au registre), quel que soit l'exécutant. Ce n'est pas une dérogation 
à la porte humaine, c'est sa réaffirmation.

## Intégration (2026-08-12)

Archivée telle quelle dans `atelier/rd/cahiers/` sur consigne explicite de
Sidy (« intègre le reste »). Aucune écriture d'automatisme effectuée par ce
geste d'archivage — conformément au §VI ci-dessus, tout ce qui reste
« à instruire » ou « à trancher » dans le tableau récapitulatif demeure
non exécuté. Seul le renvoi depuis `atelier/rd/index.md` (§« Non inclus »)
est mis à jour pour pointer ici. Statut de la note laissé à `brouillon` :
son intégration au dépôt documente une décision déjà tranchée en principe,
elle n'achève pas les chantiers restants du tableau ci-dessus.
