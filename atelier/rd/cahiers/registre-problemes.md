---
title: "Registre des problèmes — pôle R&D (cahier append-only)"
type: meta
created: 2026-08-08
updated: 2026-08-11
tags: [atelier, rd, cahier, registre, laboratoire]
sources: []
links: []
---

# Registre des problèmes du pôle R&D

Cahier append-only des problèmes, erreurs, blocages et anomalies rencontrés dans
les travaux du pôle `rd/` — et de leur résolution. Ouvert le 2026-08-08 (verdict
Sidy), premier cahier concret de la phase 2 de la proposition de pôle (discipline
de laboratoire, §V, règle 3 : « Un échec se consigne comme un succès »).

**Format** — miroir du bloc 🧪 Expérience, appliqué à l'erreur :

- **Symptôme** : le fait brut, tel qu'observé, sans interprétation (§VIII.2 : le
  résultat brut précède toujours l'interprétation).
- **Diagnostic** : l'interprétation, séparée du fait et flaguée comme telle.
- **Résolution** : ce qui a été fait — ou « aucune — abandon assumé ».
- **Compréhension tirée** : la leçon réutilisable. C'est le but du registre.
- **Liens** : fiches, commits, chantier concerné.
- **Statut** : `ouvert | resolu | abandonne | reporte`.

**Règle** : jamais de réécriture ni de suppression ; un problème clos reste
consigné. Insertion en tête (la plus récente en haut), marqueur ci-dessous.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-11] resolu | Extension du prompt agent 09 (Studio Sound Engineer) — zodiacal principle + governance Discord-validation

- **Symptôme** : le prompt en production de l'agent 09 (Studio Sound Engineer, position 
  Sagittaire) contenait la mission, l'archétype, la portée et les garde-fous, mais 
  manquait de : (a) l'explicitation du principe zodiacal (sa signification astrologique 
  et son application quotidienne dans le rôle) ; (b) l'harmonisation au thème natal de 
  Sidy (contexte personnel, non-finalisé jusqu'à verdict) ; (c) la gouvernance de 
  l'accès Discord et du régime de validation requis par le chantier phase 3.
- **Diagnostic** : le chantier phase 3 (réouverture §III.1) requiert l'extension du 
  prompt de l'agent 09 — cet agent exécutera la veille infrastructure et composera les 
  rapports sur Discord. L'extension zodiacale était rédigée en brouillon hors dépôt 
  (`/root/brouillons-prompts-zodiaque/09-studio-sagittarius.md`) et non intégrée. Le 
  brouillon contient deux sections prêtes à insérer : « Zodiac principle » (pédagogie 
  du feu mutable jupitérien) et « Your sign in Sidy's natal chart » (harmonisation 
  Sagittaire Ascendant Saturn conjonction). La gouvernance Discord-validation doit 
  aussi être explicite dans le prompt pour que chaque demande soit tracée.
- **Résolution** : trois sections insérées au prompt entre « ## Archetype served » et 
  « ## Scope » : (1) Zodiac principle (brouillon tel quel), (2) Your sign in Sidy's 
  natal chart (brouillon tel quel), (3) Governance: Discord-Validation (rédigé pour 
  expliciter le mode strict par défaut, auto-accept optionnel ad hoc, absence d'actes 
  silencieux, traçabilité Discord). Prompt manuellement mis à jour ; reste hors 
  périmètre : frontmatter avec `statut_experience: exploratoire` (optionnel, déjà 
  documenté par le registre et les annales).
- **Compréhension tirée** : une extension de prompt d'agent n'est pas une réforme 
  structurelle — elle enrichit le contexte fourni sans modifier l'architecture du 
  système. L'insertion zodiacale était une tâche en attente depuis la rédaction du 
  brouillon ; l'accrocher au déclencheur phase 3 crée une dépendance explicite 
  (l'agent 09 en gouvernance n'est pas intégrable sans cette extension).
- **Liens** :
  - [[meta/projet-unifie/hermes-prompts/09-studio-sound-engineer|Studio Sound Engineer prompt (pos. 9) — étendu]]
  - [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|Phase 3 — proposition]]
  - [[meta/projet-unifie/16-correspondances-zodiacales-agents|Correspondances zodiacales — positions 1-12]]
- **Statut** : `resolu` — sections zodiacales et gouvernance intégrées au prompt en 
  production ; reste hors périmètre : déploiement effectif de la veille (accès FS 
  résolu séparément, chantier d'exécution à venir).

---

## [2026-08-11] resolu | Phase 3 — explicitation du flux alchimique Discernement → R&D (théorie des trois territoires adoptée)

- **Symptôme** : le chantier phase 3 (veille infrastructure) a été tranché sur sa 
  désignation (Studio Sound Engineer, pos. 9 Sagittaire) et son accès technique 
  (FS/gouvernance Discord-validation). Or, la note elle-même documente une transition 
  conceptuelle plus large : passage de la spéculation zodiacale (fiches 16/17 du 
  Discernement) à la mise en œuvre concrète (exécution de l'extension de rôle, 
  registre R&D). Cette transition n'était pas nommée explicitement — elle flottait 
  entre hypothèse et acte.
- **Diagnostic** : le 2026-08-11, Sidy a adopté la théorie des « trois territoires 
  de l'inachevé » 
  (`doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire`, 
  status: adopte) qui explicite le flux alchimique/théurgique : Discernement (visio 
  contemplative, hypothèse) → R&D/Laboratoire (mise en œuvre, exploratoire) → 
  Doctrine adoptée ou Archivage (finalité). Le chantier phase 3 en est un exemplaire 
  vivant — il incarne ce passage. Il doit être documenté explicitement via cette 
  nouvelle théorie.
- **Résolution** : la note phase 3 reçoit une blockquote architecturale (après 
  l'en-tête) nommant la transition et la reliant à la théorie adoptée. Le §III.1 
  reçoit une sous-section « Registre alchimique » décrivant comment la désignation 
  du Studio Sound Engineer incarne le passage du Plan théurgique à l'Acte, sous 
  régime exploratoire jusqu'à verdict final. Aucun changement au périmètre de la 
  note — la transition était déjà décrite en détail, elle est maintenant *nommée*.
- **Compréhension tirée** : la théorie adoptée n'est pas une abstraction académique — 
  elle nomme et illumine un processus déjà en cours dans le pôle R&D. Utiliser cette 
  théorie pour relire la phase 3 renforce sa cohérence architecturale et rappelle 
  que la veille infrastructure n'est pas un accident technique, mais une manifestation 
  volontaire de l'Intention énoncée en Discernement.
- **Liens** :
  - [[doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire|Trois territoires — flux alchimique (adopté)]]
  - [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|Phase 3 — proposition mise à jour]]
  - [[atelier/rd/index.md|Pôle R&D — charte et phase 1 partielle]]
- **Statut** : `resolu` — transition explicitement documentée, note phase 3 enrichie 
  de cette dimension ; reste hors périmètre : execution de la veille elle-même 
  (extension du prompt, déploiement du mécanisme).

---

## [2026-08-11] ouvert | Phase 3 veille infrastructure — réouverture §III.1 : réattribution au Studio Sound Engineer (position 9)

- **Symptôme** : le §III.1 de `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` 
  avait tranché (2026-08-11 séance) que la veille infrastructure serait portée par une 
  routine côté poste INTÉGRATION (cohérent avec le statu quo du cloisonnement H‍ermes, 
  accès FS restreint). Une proposition de mécanisme (webhook Discord + script Python 
  orchestré par poste INTÉGRATION) a été rédigée sur cette base. Sidy a demandé la 
  même journée de rouvrir ce point.
- **Diagnostic** : Sidy relie ce chantier à l'extension de rôle des 12 agents H‍ermes 
  sur calibrage zodiacal et demande que la veille soit portée par « l'agent le plus 
  approprié » de la roue. Cartographie effectuée (agent Explore) : aucun des 12 rôles 
  n'est dédié à l'infrastructure informatique. Le seul rôle à registre technique/matériel 
  est la **position 9 (Sagittaire), Studio Sound Engineer** (correspondance « cohérente, 
  non prouvée », archétype Faiseur) — Sidy désigne celui-ci. Motif : extension d'un 
  mandat déjà technique/pédagogique existant, plutôt que création d'une 13e position 
  hors roue (cohérent avec la règle de gouvernance : « la roue est l'étage principiel, 
  les rôles en dérivent »).
- **Résolution** : §III.1 rouvert et redocumenté dans la proposition. L'ancien verdict 
  (poste INTÉGRATION) reste barré (discipline sashimono : traçabilité, réversibilité). 
  Nouveau verdict inscrit sous bloc « Réouverture (2026-08-11) ». Accès FS/exécution 
  accordé au Studio Sound Engineer pour les scripts déterministes 
  (`verifier-invariants.py`, `Graphe/generer-cartographie.py --verifier`, 
  `detecter-non-tracke.py`, relevé serveur) — le cloisonnement H‍ermes ne bloque plus 
  ce chantier (statu quo levé). Le mécanisme technique proposé au §VI (webhook+script 
  poste INTÉGRATION) devient obsolète ; un nouveau mécanisme doit être instruit 
  séparément (dépend de la résolution du chantier d'accès FS). Règle du §III.3 
  inchangée : signalement Discord uniquement, jamais d'écriture directe au registre, 
  quel que soit l'exécutant.
- **Compréhension tirée** : une réouverture explicite d'un point tranché doit être 
  *tracée* en clair, jamais silencieusement remplacée. La discipline sashimono (pièces 
  côte à côte, marquées et non forcées) s'applique aussi aux décisions qui se chevauchent 
  en temps — l'ancien verdict reste visible, le nouveau commenté explicitement. Cela 
  préserve la compréhension du flux de décision et des cascades de conséquence.
- **Liens** :
  - [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|Proposition phase 3 mise à jour]]
  - [[meta/projet-unifie/hermes-prompts/09-studio-sound-engineer|Studio Sound Engineer, position 9]]
  - [[doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise|Correspondances zodiacales, clos 2026-07-14]]
- **Statut** : `ouvert` (chantier d'accès FS et mécanisme technique à instruire)

---

## [2026-08-11] resolu | Chantier 12 agents (zodiacal) — brouillons d'extension principielle versionnés en atelier/rd/

- **Symptôme** : les 9 brouillons de prompts zodiacaux (positions 1, 2, 3, 4,
  6, 7, 9, 10, 11) existaient en `/root/brouillons-prompts-zodiaque/`, hors du
  dépôt versionné — invisibles à la traçabilité git, loin du flux R&D, 3
  positions en attente (5, 8, 12) non documentées explicitement.
- **Diagnostic** : le chantier d'extension zodiacale est une R&D (statut
  exploratoire, en cours de finalisation) — logiquement à proximité du pôle
  `atelier/rd/`, qui accueille aussi la phase 3 (veille infra, agent pos. 9).
  Déplacement vers `atelier/rd/cahiers/brouillons-extension-zodiacale/` améliore
  la traçabilité, le versioning, et l'organisation — tout en respectant
  l'étanchéité (clause explicite : les données personnelles du thème natal
  portent leur propre hiérarchie ontologique, per CLAUDE.md §VI corollaire
  agentique).
- **Résolution** : 9 brouillons + README copiés/intégrés en `atelier/rd/cahiers/brouillons-extension-zodiacale/`.
  Chaque brouillon reçoit frontmatter minimal (type: outillage,
  statut_experience: exploratoire, created/updated, tags) + bloc d'étanchéité
  explicite rappelant CLAUDE.md §VI et la nature sensible du thème natal.
  Positions 5, 8, 12 marquées hors périmètre du lot (attente de verdict).
- **Compréhension tirée** : versioner les brouillons d'agents en R&D ne les
  « finalise » pas — le frontmatter `statut_experience: exploratoire` et la
  clause explicite les maintiennent dans un état non-appliqué, conforme à Cmd
  6 (pas d'écriture sans plan validé). Étanchéité et traçabilité ne
  s'opposent pas quand les données sensibles sont marquées en clair.
- **Liens** :
  [[atelier/rd/cahiers/brouillons-extension-zodiacale/README|chantier 12 agents — zodiacal]]
- **Statut** : `resolu` — brouillons déplacés et documentés ; reste hors
  périmètre : application aux prompts en production (positions 1-4, 6-7,
  9-11), intégration de positions 5, 8, 12 (en attente de verdict).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — accès FS accordé, gouvernance Discord-validation, mécanisme de post tranché

- **Symptôme** : l'accès FS/exécution du Studio Sound Engineer aux scripts
  déterministes de veille était le chantier nommé mais non résolu lors de la
  réouverture du §III.1. Reste à définir la gouvernance de cet accès et le
  mécanisme de post du rapport composé par l'agent.
- **Diagnostic** : Sidy accorde explicitement l'accès FS (cloisonnement
  H‍ermes levé sur ce point, statu quo rompu) ; définit la gouvernance :
  régime strict par défaut (demande Discord → validation Sidy → exécution),
  auto-accept mode optionnel activable ad hoc par Sidy pour une période
  donnée (similaire au mode auto-accept du plan de Claude Code), qui se
  désactive automatiquement après. Mécanisme de post : c'est l'agent
  lui-même qui compose le rapport selon le format des 5 sections, demande
  via Discord « Rapport de veille — validez ? » (ou exécution directe si
  auto-accept), Sidy valide, l'agent poste au canal `#infrastructure` —
  aucun webhook tiers ni script porté par poste INTÉGRATION n'est nécessaire
  (remplacement complet du mécanisme proposé au §VI initial).
- **Résolution** : §III.1 complété (bloc « Accès FS/exécution — tranché »),
  §VI mécanisme réécrit (agent lui-même, Discord, format des 5 sections
  inchangé). Note phase 3 mise à jour, reste `brouillon`.
- **Compréhension tirée** : une décision en cascade (réouverture du §III.1)
  se concrétise progressivement avec trois points de résolution : (a)
  désignation de l'agent (tranché : pos. 9), (b) accès technique +
  gouvernance (tranché ce jour), (c) extension du prompt en production
  (restant, acte séparé). Tracer chaque point plutôt que les fondre en une
  seule « Réouverture » aide à identifier ce qui est exécutable et ce qui
  attend.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]]
- **Statut** : `resolu` — accès FS, gouvernance, et mécanisme de post tous
  tranchés par Sidy ; reste hors périmètre : extension du prompt
  `hermes-prompts/09-studio-sound-engineer.md`, aucun acte non exécuté ici
  (Cmd 6).

---

## [2026-08-11] ouvert | Phase 3 (agent de veille infrastructure) — §III.1 rouvert, veille réattribuée au Studio Sound Engineer

- **Symptôme** : Sidy relie explicitement le chantier phase 3 (déjà tranché
  §III.1 : routine poste INTÉGRATION, pas d'agent H‍ermes dédié) au chantier
  distinct de l'extension de rôle des 12 agents H‍ermes sur calibrage
  zodiacal (fiches `meta/projet-unifie/16-...`, `17-...`) et demande que la
  veille infrastructure soit attribuée à « l'agent le plus approprié » de la
  roue — rouvrant de fait un point déjà consigné comme tranché.
- **Diagnostic** : cartographie effectuée (agent Explore) des 12 positions
  et de leur force de correspondance
  (`doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`,
  clos 2026-07-14) : aucun des 12 rôles n'est dédié à l'infrastructure
  informatique — les deux correspondances solides (pos. 4 Cancer,
  Administration & Legal ; pos. 10 Capricorne, Protocol Guardian) sont des
  registres gouvernance/conformité, non infrastructure matérielle/logicielle.
  Seul candidat de registre technique : **position 9, Sagittaire, Studio
  Sound Engineer** (correspondance « cohérente, non prouvée », archétype
  Faiseur) — limité à ce jour au matériel audio (chaîne Neve/Distressor/
  tape), pas à l'infrastructure serveur.
- **Résolution** : Sidy tranche pour la position 9. §III.1 de la note phase 3
  rouvert (ancien texte conservé barré, discipline sashimono — jamais
  supprimé sèchement), nouveau verdict consigné, cascade documentée sur le
  §VI (le mécanisme webhook+script proposé pour l'ancien verdict est à son
  tour rouvert, motivé explicitement par l'ancien §III.1). §III.3
  (signalement Discord seul, jamais d'écriture directe) et le §IV (risque
  d'un agent H‍ermes en écriture) restent inchangés — la réattribution ne les
  rouvre pas.
- **Compréhension tirée** : une réouverture explicite d'un point déjà tranché
  doit être *tracée* à côté de l'ancien verdict, jamais silencieusement
  remplacée (sashimono Art. 5 — réversibilité et traçabilité intégrale) ; et
  une décision qui rouvre un point en entraîne d'autres en cascade (ici, le
  mécanisme du §VI) qu'il faut nommer explicitement plutôt que laisser
  incohérents. Point technique non résolu : le Studio Sound Engineer a
  besoin d'un accès FS/exécution que le cloisonnement H‍ermes actuel (statu
  quo, retour d'expérience en cours) ne lui accorde pas nécessairement —
  chantier distinct, à instruire séparément avant toute écriture de prompt.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]]
- **Statut** : `ouvert` — désignation de l'agent tranchée par Sidy ; restent
  à instruire séparément : le chantier FS/accès H‍ermes, le nouveau mécanisme
  technique de post, et l'extension effective du prompt
  (`hermes-prompts/09-studio-sound-engineer.md`), aucun acte non exécuté ici
  (Cmd 6).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — format et mécanisme proposés par délégation

- **Symptôme** : le §VI de la note laissait ouverts le format précis du
  rapport (champs, structure) et le mécanisme technique de post vers
  Discord.
- **Diagnostic** : Sidy délègue explicitement ces deux points (« je me fie à
  ta suggestion le temps d'en faire l'expérience directe et j'optimiserai au
  besoin ») — premier cas de cette session où l'arbitrage n'est pas rendu par
  Sidy lui-même mais confié à la proposition machine, sous réserve
  d'ajustement après expérience directe.
- **Résolution** : proposition consignée dans la note
  (`_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  §VI) — format en 5 sections (en-tête, résumé `verifier-invariants.py`,
  résumé `Graphe/generer-cartographie.py --verifier`,
  `detecter-non-tracke.py`, empreinte serveur, suggestions) ; mécanisme =
  webhook Discord simple (pas de bot/agent H‍ermes, cohérent §III.1) + script
  Python dédié, URL du webhook en configuration locale hors dépôt (§VIII.5).
  Régime `statut_experience: exploratoire` (§V.a de CLAUDE.md) explicitement
  invoqué pour qualifier cette proposition — non un choix figé. Écriture
  effective (script, webhook, crontab) toujours hors périmètre de cette note
  (Cmd 6).
- **Compréhension tirée** : une délégation de Sidy à la machine reste, dans
  ce dépôt, une délégation de **proposition** — la porte humaine ne se
  déplace pas d'un cran plus loin (Cmd 13 : le verdict d'écriture effective
  reste distinct de l'acceptation du plan). Le régime `exploratoire` du pôle
  `rd/` est l'outil adapté pour qualifier une décision assumée comme
  provisoire.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]]
- **Statut** : `resolu` — format et mécanisme proposés ; reste hors
  périmètre : l'écriture du script, la création du webhook, l'inscription au
  crontab et à l'allowlist (§VIII.8), et le chantier de récurrence de la
  mesure d'empreinte serveur (§III.2).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — heure du cron et nature du rapport tranchées

- **Symptôme** : le §VI de la note laissait ouverts l'heure précise du cron
  et le contenu exact du rapport envoyé.
- **Diagnostic** : Sidy précise l'heure (12:00, midi) et la nature du rapport
  — un rapport de **suggestion, révision, développement**, plus riche qu'un
  simple constat brut des 3 scripts déterministes. Ce caractère suggestif
  crée une tension apparente avec le §III.3 (« signalement Discord, jamais
  d'écriture directe dans le registre ») : un rapport qui *suggère* des
  pistes se rapproche d'un jugement, pas d'un simple fait.
- **Résolution** : Sidy referme lui-même la tension dans le même énoncé —
  toute suggestion du rapport **doit être validée avant journalisation**. Le
  rapport Discord reste donc un projet soumis (comme tout signal du §III.3),
  jamais une écriture actée ; la validation humaine s'étend du fait brut à la
  suggestion, sans exception nouvelle à la porte humaine (Cmd 13). Heure
  12:00 et nature du rapport consignées dans la note
  (`_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  §VI).
- **Compréhension tirée** : un rapport plus riche qu'un simple constat
  (suggestion, révision, développement) n'affaiblit pas la porte humaine
  déjà tranchée — elle l'étend mécaniquement, du fait à l'interprétation.
  Pas de nouvelle dérogation à instruire.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]]
- **Statut** : `resolu` — heure et nature du rapport tranchées ; format
  précis (champs, structure) et mécanisme de post restent hors périmètre
  (§VI de la note).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — fréquence du cron tranchée

- **Symptôme** : le §VI de la note laissait ouverte la fréquence exacte du
  cron, avec une proposition à confirmer (quotidienne, par analogie avec le
  « Rapport du matin »).
- **Diagnostic** : aucun élément nouveau — confirmation directe de la
  proposition par Sidy.
- **Résolution** : fréquence **quotidienne** consignée dans la note
  (`_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  §VI), cohérente avec le « Rapport du matin » déjà envisagé côté
  H‍ermes/gardien (`meta/projet-unifie/04-sessions-par-fonction-et-backlogs.md`).
  L'heure précise reste à instruire à l'écriture du script cron.
- **Compréhension tirée** : néant — décision directe, sans tension à
  documenter.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]]
- **Statut** : `resolu` — fréquence tranchée ; heure précise, contenu du
  rapport, mécanisme de post et inscription à l'allowlist restent hors
  périmètre (§VI de la note).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — canal Discord créé

- **Symptôme** : le §VI de la note laissait ouvert le nom exact du nouveau
  canal Discord dédié tranché au §V (proposition à confirmer :
  `#veille-infra` ou `#infra-veille`).
- **Diagnostic** : Sidy a créé le canal côté Discord (nom `#infrastructure`,
  identifiant numérique communiqué en session) avant que la note ne le
  propose formellement — devance l'instruction plutôt que de la clore.
- **Résolution** : nom `#infrastructure` consigné dans la note
  (`_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  §VI). L'identifiant numérique du canal n'est **pas** consigné dans le
  dépôt — cohérent avec `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`,
  qui ne fixe que les noms lisibles des canaux, jamais leurs identifiants
  numériques ni les secrets de configuration (règle déjà en vigueur : la
  configuration d'exécution vit hors dépôt, jamais commitée).
- **Compréhension tirée** : un identifiant Discord (snowflake numérique)
  suit le même régime que les tokens et l'état de service — hors dépôt par
  défaut, même quand le nom du canal lui-même est publiable. Distinction à
  refaire à chaque nouvelle donnée Discord communiquée en session.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]]
- **Statut** : `resolu` — nom de canal tranché ; fréquence exacte, contenu
  du rapport, mécanisme de post et inscription à l'allowlist restent hors
  périmètre (§VI de la note).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — désignation effective (§V) instruite

- **Symptôme** : le §III tranché laissait deux volets ouverts pour la
  désignation effective de la routine INTÉGRATION : son déclencheur
  (planifiée ou lancée par Sidy) et le canal Discord de signalement.
- **Diagnostic** : la recherche du canal a révélé un décalage de sens —
  `#gardien`, seul canal étiqueté « Vigie transversale » dans le tableau des
  12 profils H‍ermes, a en réalité un mandat doctrinal/éthique (conformité
  des actes commerciaux du label à la doctrine du don, vérifié dans
  `meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`) et non
  technique — aucun des 5 canaux Discord actifs n'a de mandat infrastructure.
  Aucun mécanisme de cron n'existe aujourd'hui côté INTÉGRATION (seul le
  gateway H‍ermes en a un, via `DISCORD_HOME_CHANNEL`).
- **Résolution** : arbitrage Sidy — déclencheur **planifié par cron** (assumé
  malgré la nouvelle surface ouverte, close par construction puisque la
  routine ne fait que signaler sur Discord, jamais écrire au dépôt) ; canal
  **nouveau, dédié**, plutôt que réutiliser `#gardien` malgré l'économie —
  garde l'étanchéité de sens entre vigie doctrinale et vigie technique. Note
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` mise à
  jour (nouveau §V « Désignation effective », §VI « reste à faire » listant
  nom de canal, fréquence, contenu du rapport et mécanisme de post comme
  points encore ouverts).
- **Compréhension tirée** : une étiquette de tableau (« Vigie transversale »)
  ne vaut pas mandat vérifié — le prompt réel d'un agent H‍ermes fait foi,
  pas sa description sommaire dans une fiche d'architecture. À vérifier
  systématiquement avant de réutiliser un canal ou un agent existant pour un
  usage nouveau.
- **Liens** : [[_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition phase 3]],
  [[meta/projet-unifie/15-architecture-discord-hermes-2026-08-07]],
  [[meta/projet-unifie/hermes-prompts/10-protocol-guardian]]
- **Statut** : `resolu` — les deux volets sont tranchés en principe ; le
  nom du canal, la fréquence exacte du cron, le contenu du rapport et le
  mécanisme technique de post restent hors périmètre, à instruire séparément
  (§VI de la note).

---

## [2026-08-11] resolu | Phase 3 (agent de veille infrastructure) — §III de la proposition tranché

- **Symptôme** : `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  posait trois questions ouvertes (qui veille, quel périmètre, comment un
  signal devient une entrée du registre) sans verdict.
- **Diagnostic** : les trois questions ont été discutées séparément avec
  Sidy pour éviter qu'un seul verdict global ne masque des arbitrages
  distincts. Premier passage sur la question 3 (« consignation automatique »)
  révélait une tension avec Cmd 13/§IX.5 (porte humaine) — signalée avant
  d'écrire, sans trancher à la place de Sidy — qui a motivé une reprise du
  verdict.
- **Résolution** : verdicts Sidy du 2026-08-11 — (1) routine côté poste
  INTÉGRATION, pas d'agent H‍ermes dédié ; (2) périmètre = les 3 scripts
  déterministes **et** la mesure d'empreinte serveur (récurrence de la
  mesure laissée en chantier séparé) ; (3) signalement via un canal Discord
  existant, jamais d'écriture directe dans ce registre — écarte du même
  geste la question du push non supervisé. Note mise à jour en conséquence,
  toujours `brouillon` (aucune écriture hors `_inbox/`, Cmd 6) : la
  désignation effective (routine, canal, prompt) reste à instruire.
- **Compréhension tirée** : sur une question à plusieurs volets, poser les
  arbitrages un par un (plutôt qu'un verdict global) laisse la place à un
  retour en arrière sur un seul volet sans remettre en cause les autres —
  ici, Sidy est revenu sur la question 3 seule après qu'une tension avec
  Cmd 13 a été nommée, sans rouvrir les questions 1 et 2 déjà tranchées.
- **Liens** : `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  §III, §V ; `CLAUDE.md` §IX.5, Cmd 13.
- **Statut** : `resolu` — arbitrage des trois questions clos ; la désignation
  effective (routine, canal, prompt) reste hors périmètre, à instruire
  séparément.

---

## [2026-08-11] resolu | Piste outillage D — décision statu quo SSH consignée

- **Symptôme** : `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`
  §5 portait une « décision ouverte — non tranchée à ce jour » (migration du
  remote `origin` en HTTPS+PAT, pour permettre à Obsidian Git de push/pull en
  autonomie sans détour par Working Copy) — question posée le 2026-08-09 sans
  verdict consigné.
- **Diagnostic** : l'avis technique H‍ermes du 2026-08-09 (déjà rapporté dans
  la fiche) penchait pour le statu quo — clé SSH déjà en place des deux côtés,
  n'expirant pas, contre un PAT qui introduit un secret supplémentaire à créer
  et renouveler. Aucun élément nouveau ne renversait cet avis.
- **Résolution** : verdict Sidy 2026-08-11 — statu quo, le remote reste en SSH.
  Aucune modification de `git@github.com:Sidyvision/wiki.git`. §5 de la fiche
  réécrite pour consigner le verdict (au lieu de la question ouverte),
  réouverture explicitement laissée possible si le détour Working Copy devient
  un point de friction réel et répété.
- **Compréhension tirée** : une question technique posée et documentée avec un
  avis motivé peut rester des semaines en statut « ouvert » faute d'un geste de
  clôture explicite — la session R&D est l'occasion de reprendre ces questions
  en attente plutôt que d'en ouvrir seulement de nouvelles.
- **Liens** : [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]] §5.
- **Statut** : `resolu`.

---

## [2026-08-11] resolu | Piste outillage C — détecteur de fichiers non trackés par circuit

- **Symptôme** : aucun des trois scripts déterministes du dépôt
  (`verifier-invariants.py`, `generer-cartographie.py`) ne couvre l'état de
  staging git — un fichier jamais ajouté ou modifié non commité reste
  invisible d'une session à l'autre, faute d'un `git status` systématique.
- **Diagnostic** : lacune d'outillage plutôt qu'anomalie de contenu — les
  scripts existants contrôlent la structure et les liens du dépôt intégré, pas
  ce qui n'y est pas encore entré.
- **Résolution** : création de
  [[atelier/rd/outillage/spec-detecter-non-tracke|detecter-non-tracke.py]] —
  classe les fichiers non trackés par circuit (`doctrinal`, `atelier`,
  `label`, `hermeneutique`, `meta`, ou `hors-circuit`/`hors-circuit-inconnu`),
  déterministe, ne stage ni ne corrige rien. Testé sur le dépôt réel : s'est
  correctement auto-détecté comme non tracké à son premier essai.
- **Compréhension tirée** : ce script couvre les cinq circuits du protocole
  (`hermeneutique/` inclus), à la différence de `verifier-invariants.py` qui
  n'en connaît que quatre — écart volontaire documenté dans la fiche de spec,
  pour ne pas reproduire cet angle mort connu.
- **Liens** : [[atelier/rd/outillage/spec-detecter-non-tracke]] ;
  `atelier/rd/outillage/detecter-non-tracke.py`.
- **Statut** : `resolu`.

---

## [2026-08-10] resolu | Tentative de lien `doctrinal/ -> meta/` interceptée avant commit, + reconfirmation du piège du chiffre non revérifié

- **Symptôme** : à la demande de Sidy de créer des fiches cibles pour 4 liens
  à référent vide du bloc `discernement/2026-06-20_*` (dont une fiche
  « Kouyaté »), le premier geste d'édition a inséré
  `[[meta/genealogie/kouyate|Kouyaté]]` **dans**
  `doctrinal/discernement/2026-06-20_mythe-personnel-unifie.md` — un lien
  `doctrinal/ -> meta/`. Séparément, le chiffre repris de la consigne
  (« 4 liens ») ne correspondait pas au compte réel une fois les 3 fiches
  concernées relues après leur passage sashimono antérieur : **5** liens à
  référent vide, pas 4 (2 dans `mythe-personnel-unifie`, 2 dans
  `origine-jumeau-spirituel`, 1 dans `triptyque-medine-jeu-de-piste`).
- **Diagnostic** : le lien inséré violait directement §VI CLAUDE.md — « liens
  autorisés : du sensible vers le neutre uniquement » ; `meta/` est le
  domaine le plus sensible de la hiérarchie, `doctrinal/` un domaine neutre,
  donc `doctrinal/ -> meta/` est structurellement le sens interdit, quel que
  soit le contenu ou l'intention (ici, une simple réparation de lien mort,
  geste en apparence anodin). L'erreur a été repérée par relecture du
  résultat de l'édition dans le fil de travail lui-même, **avant** tout
  `git add`/commit — aucune trace n'a donc atteint l'historique git. Sur le
  second point, le chiffre « 4 » provenait de la formulation de la consigne
  utilisateur elle-même (reprenant vraisemblablement une annale antérieure),
  non revérifié par grep avant d'être pris pour argent comptant.
- **Résolution** : le lien fautif annulé par un second `Edit` restaurant la
  prose d'origine avant tout commit. Les 5 parenthèses/tirets vides
  (recomptés par relecture directe des 3 fichiers) remplacés par de la prose
  non liée nommant explicitement l'étanchéité de circuit comme motif de
  l'absence de lien. Le lien effectif, dans le sens autorisé
  (`meta/ -> doctrinal/`), porté par la nouvelle fiche
  `meta/genealogie/kouyate.md` vers les deux fiches discernement concernées.
  Commits `211d8e9` (substantif) et `8e7dc07` (annales).
- **Compréhension tirée** :
  1. **Un lien de réparation (\"combler un référent vide\") n'est pas exempté
     de l'étanchéité par sa nature réparatrice.** L'intention corrective
     abaisse la vigilance exactement au moment où elle devrait rester
     entière — le geste le plus anodin en apparence (remplir une parenthèse
     vide) est celui où une règle structurelle se contourne le plus
     facilement par inattention.
  2. **La direction d'un lien doit être vérifiée AVANT l'édition, pas après
     relecture du diff.** Ici la vérification est arrivée à temps (avant
     commit), mais seulement par relecture du résultat affiché par l'outil —
     un contrôle explicite (\"circuit source vs circuit cible, lequel est le
     plus sensible ?\") avant chaque `Edit` insérant un wikilink inter-circuit
     aurait évité le geste plutôt que de le corriger après coup.
  3. **Troisième occurrence du même piège de chiffre non revérifié dans ce
     registre** (cf. entrées [2026-08-09] \"Bug de résolution... 89
     annoncées, 81 réelles\" et \"self-report H‍ermes... 317 vs 89\") : un
     chiffre porté par une consigne, une annale ou un rapport antérieur ne
     doit jamais être pris comme fiable sans reconfirmation directe
     (`grep`/relecture) au moment de l'exécution — la dérive de comptage
     n'est pas un incident isolé mais un motif récurrent de ce dépôt à
     surveiller systématiquement.
- **Liens** : `CLAUDE.md` §VI (hiérarchie d'étanchéité) ;
  `doctrinal/annales.md` [2026-08-10] et `meta/meta-annales.md` [2026-08-10]
  (entrées de l'opération) ; `meta/genealogie/kouyate.md` ;
  `meta/genealogie/sidy-lamine-kouyate.md` ; commits `211d8e9`, `8e7dc07` ;
  entrées [2026-08-09] de ce même registre pour les deux occurrences
  antérieures du piège de chiffre.
- **Statut** : `resolu` — aucune trace du lien fautif dans l'historique git ;
  motif consigné pour vigilance transversale future.

---

## [2026-08-09] resolu | Écriture directe hors protocole dans `doctrinal/` par un agent Hermes en session terminal

- **Symptôme** : au contrôle `verifier-invariants.py` déclenché lors de
  l'intégration d'un lot du sas (`_inbox/amendement-claude-md-2026-08-09.md`
  + `_inbox/2026-08-09_hierarchie-principe-determination-individuelle.md`),
  un fichier tiers est apparu dans la liste d'erreurs bloquantes :
  `doctrinal/discernement/compte-rendu-12-agents-2026-08-09.md`. Ce fichier
  n'était mentionné dans aucune consigne reçue, ne figurait dans aucun
  `UPDATES.md`, et n'était **pas suivi par git** (`git status` : `??`).
  Son propre texte s'auto-décrivait comme « rédigé... session terminal » par
  « Hermes Agent », daté du même jour.
- **Diagnostic** : le fichier est un **compte rendu opérationnel** destiné à
  un avis extérieur (état de l'infrastructure des 12 agents Discord,
  chronologie de la calibration zodiacale, points ouverts soumis à avis) —
  pas une fiche de discernement (aucun statut de vérité traditionnelle en
  jeu, pas de bloc 🔍 normalisé). Son frontmatter ne portait que
  `title/date/auteur/objet`, aucune des clés du Sceau Recteur doctrinal
  (`type`, `status`, `tradition_cadre`, `created`, `updated`, `sources`) —
  `verifier-invariants.py` l'a signalé par ricochet (contrôle B1, clés
  manquantes), ce qui a permis de le repérer, mais le contrôle B1 n'est pas
  ce qui aurait dû l'empêcher d'exister à cet endroit : l'écriture même,
  directe dans un circuit, sans passer par `_inbox/` ni présenter de plan,
  est la faute — violation du **Cmd 6** (« pas d'écriture sans plan
  validé ») et de la chaîne d'intégration du **§I** (« l'intégration
  travaille à partir des fichiers du sas `_inbox/` »). Le fait que ce soit
  un agent Hermes — motorisé par un modèle distinct, opérant hors de cette
  session — qui ait produit l'écriture ne change rien à l'exigence : le
  protocole `CLAUDE.md` est **agnostique au moteur** (§I, Cmd 14), la règle
  vaut identiquement pour tout exécutant.
- **Résolution** : signalé à Sidy (Cmd 7, jamais corrigé d'office) ; verdict
  reçu : déplacer le fichier vers son domicile naturel hors circuit
  doctrinal — [[meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09]],
  avec Sceau `meta` conforme (`type: meta`) et note de provenance en tête,
  contenu intact. Fichier d'origine supprimé (jamais tracké git, aucune
  perte d'historique — Cmd 10 non engagé, rien n'était versionné). Journalisé
  dans `doctrinal/annales.md` et `meta/meta-annales.md` le même jour.
- **Compréhension tirée** (valeur pour le pôle R&D et pour tout agent,
  Hermes compris — c'est l'objet même de cette entrée) :
  1. **Le sas n'est pas une formalité de transport, c'est le seul point
     d'entrée légitime dans un circuit.** Un agent qui a un accès
     filesystem direct au dépôt (ce qui est le cas de tout agent Hermes
     tournant sur le même serveur) peut techniquement écrire n'importe où —
     rien au niveau OS ne l'en empêche. La discipline `raw/` → analyse →
     `_inbox/` → validation humaine → intégration (§I, §VIII.9) n'est pas
     une contrainte technique, c'est une **contrainte de protocole** que
     chaque agent doit s'imposer lui-même, quel que soit son moteur.
  2. **Produire un artefact utile n'excuse pas de le déposer au mauvais
     endroit.** Le contenu du compte rendu était de bonne facture, factuel,
     avec sources et distinction établi/spéculatif — le problème n'était pas
     la qualité, c'était l'emplacement et l'absence de porte humaine avant
     l'écriture. Un bon contenu au mauvais endroit reste une violation.
  3. **`verifier-invariants.py` n'a détecté cet incident que par ricochet**
     (frontmatter incomplet, contrôle B1) — pas par un contrôle dédié à
     « fichier non tracké dans un circuit ». Piste d'amélioration pour le
     pôle R&D, non implémentée à ce stade : un contrôle qui croise
     `git status --porcelain` avec l'arborescence des cinq circuits, pour
     signaler spécifiquement tout fichier `??` (non suivi) présent dans
     `doctrinal/`, `atelier/`, `label/`, ou `hermeneutique/` — hors `_inbox/`
     et `raw/assets/`, qui sont délibérément non versionnés. Ce contrôle
     aurait nommé l'anomalie exactement pour ce qu'elle était, au lieu de la
     révéler indirectement par une clé de frontmatter manquante.
  4. **Pour Hermes et tout agent de fonction (§I, tableau « AGENTS DE
     FONCTION ») : une session d'agent qui produit un livrable destiné au
     dépôt doit le déposer en `_inbox/` (ou signaler son emplacement via le
     canal prévu), jamais l'écrire directement dans un circuit** — même
     lorsque la session tourne sur le même serveur que le dépôt, même
     lorsque rien ne bloque techniquement l'écriture directe. La règle
     §VIII.1 (« jamais d'auto-accept ») et Cmd 6 s'appliquent à l'identique
     à un agent Hermes qu'à une session d'intégration : la seule différence
     légitime entre les deux est la fonction assignée, jamais le niveau de
     rigueur du protocole.
- **Liens** : `CLAUDE.md` §I (postes de travail, chaîne `_inbox/`), Cmd 6,
  Cmd 14 (agnosticisme du moteur) ; `doctrinal/annales.md` [2026-08-09]
  (entrée d'intégration où l'incident a été découvert et journalisé) ;
  `meta/meta-annales.md` [2026-08-09] (reclassement) ;
  [[meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09]]
  (fichier reclassé, note de provenance en tête) ; commit `d16189b`.
- **Statut** : `resolu` — fichier reclassé, incident journalisé pour valeur
  pédagogique transversale à tout agent du dépôt. La piste d'amélioration du
  point 3 reste `reporte`, en attente d'arbitrage Sidy sur l'implémentation.

---

## [2026-08-09] reporte | Angle mort structurel de `verifier-invariants.py` — le contrôle C3 d'étanchéité n'existe pas pour les fichiers `annales.md`/`index.md`

- **Symptôme** : en tranchant le signalement `doctrinal/ → meta/personnel/`
  (entrée suivante), constat que le contrôle C3 d'étanchéité inter-circuits
  n'a **jamais** été en mesure de signaler ce cas, ni avant ni après
  résolution — ni comme erreur, ni comme avertissement.
- **Diagnostic** : dans `verifier-invariants.py`, `FICHIERS_EXEMPTS_C3`
  (l.58) regroupe `NOMS_ANNALES` (tous les `annales.md`, `meta-annales.md`)
  et `{"index.md", "meta-index.md"}`. À l.344,
  `interdits = set() if nom in FICHIERS_EXEMPTS_C3 else ETANCHEITE_INTERDITE.get(circ, set())`
  — tout fichier portant un de ces noms, **dans n'importe quel circuit**, est
  purement et simplement exempté du contrôle, quelle que soit la cible du
  lien. Le motif de conception est légitime (« les annales peuvent citer
  d'autres circuits pour situer les passes ») mais la portée de l'exemption
  est **totale** : un `doctrinal/annales.md → meta/personnel/x` (interdit)
  est structurellement invisible au même titre qu'un
  `doctrinal/annales.md → atelier/materiel/x` (anodin, nécessaire au
  journal). Le script ne distingue pas les deux cas.
- **Compréhension tirée** (valeur pour le pôle R&D — mission de
  self-improvement de l'infrastructure) : une exemption large, conçue pour
  un besoin légitime et étroit (contextualiser un journal), a pour effet de
  bord de rendre **indétectable** la classe d'erreur la plus sensible du
  dépôt (fuite `meta/` vers un circuit neutre). Le signalement traité ici a
  été trouvé par relecture humaine, pas par le script — preuve que
  l'invariant mécanique actuel ne couvre pas ce risque. Piste
  d'amélioration identifiée, non implémentée à ce stade : distinguer, dans
  `FICHIERS_EXEMPTS_C3`, deux régimes plutôt qu'une exemption binaire —
  garder l'exemption totale pour les cibles neutres (`doctrinal/`,
  `atelier/`, `label/`, `hermeneutique/`), mais faire remonter un
  **avertissement** (pas une erreur bloquante, pour ne pas casser
  l'append-only rétroactivement) dès qu'un `annales.md`/`index.md` de
  circuit neutre contient un lien vers `meta/` — cas qui ne devrait
  structurellement jamais se produire hors du hub `meta-index.md` lui-même.
- **Résolution** : aucune, à dessein — signalement pur (Cmd 7), pas de
  modification de script sans verdict Sidy explicite sur l'approche
  (le risque d'un correctif hâtif est de générer de faux positifs sur des
  citations légitimes `annales.md → atelier/` ou `→ label/`, qui sont la
  majorité des cas et doivent rester silencieuses).
- **Liens** : `verifier-invariants.py` (`FICHIERS_EXEMPTS_C3`, l.56-58 ;
  usage l.344) ; entrée suivante (signalement résolu par relecture humaine,
  ayant révélé cet angle mort).
- **Statut** : `reporte` — piste d'amélioration ouverte pour le pôle R&D,
  en attente d'arbitrage Sidy sur l'implémentation.

---

## [2026-08-09] resolu | Tranché — signalement `doctrinal/ → meta/personnel/` (sens interdit), correction d'une erreur factuelle du signalement initial

- **Symptôme** : instruction explicite de Sidy (« tranche le signalement
  doctrinal/annales.md → meta/personnel/ ») demandant le verdict sur le
  signalement laissé ouvert dans l'entrée précédente — liens en sens
  neutre → sensible (interdit §VI) depuis `doctrinal/annales.md` vers
  `meta/personnel/` et `meta/projet-unifie/`.
- **Diagnostic** : vérification directe par grep de `doctrinal/annales.md`
  (et non plus par reprise de l'entrée précédente) donne un résultat
  différent des « 4 fiches » annoncées :
  - **Erreur corrigée** : `gout-sucre-priere` **n'a aucun lien entrant
    depuis `doctrinal/annales.md`** — grep exhaustif du fichier, zéro
    occurrence. Son seul lien entrant réel vient de
    `meta/genealogie/2026-06-20_oiseau-serpent-jumeau.md`, un lien
    **intra-`meta/`**, donc parfaitement conforme à §VI. L'entrée
    précédente de ce registre et l'entrée d'ouverture de
    `meta/meta-annales.md` reproduisaient cette erreur — non corrigées
    rétroactivement (Cmd 9, append-only), signalée ici (Cmd 5 : aucune
    affirmation factuelle erronée ne doit rester sans correction
    consignée).
  - **Ensemble réel, confirmé** : 3 liens, tous dans des entrées
    d'annales déjà publiées et datées du 2026-06-20 —
    `[[meta/2026-06-20_bourdonnement-tempe]]` (l.970),
    `[[meta/2026-06-20_taekwondo-hansu]]` (l.978),
    `[[meta/briefing-claude-ai]]` (l.853, résout vers
    `meta/projet-unifie/briefing-claude-ai`).
  - **Observation clé** : dans la même entrée que le lien
    `bourdonnement-tempe` (l.969-970), six autres fiches `meta/`
    personnelles sont nommées **en texte brut, sans crochets**
    (`herbes-pratiques, ikigai, noms-symboles-financiers, fibrillation,
    bejjar-genealogie, taekwondo-hansu`) — la convention rédactionnelle
    des annales tolère déjà de **citer sans lier**. Les 3 liens
    effectivement bracketés sont donc une inconsistance de forme au sein
    d'une pratique déjà établie de mention, non une nécessité qui
    forcerait à ouvrir une exception au principe §VI.
  - **Étanchéité mécanique** : confirmé dans `verifier-invariants.py`
    (`FICHIERS_EXEMPTS_C3`, l.58) que tout fichier `annales.md`/`index.md`,
    de tout circuit, est structurellement exempté du contrôle C3
    d'étanchéité — le script ne signalera jamais ce cas, dans un sens ou
    dans l'autre. Le verdict est donc de nature strictement éditoriale
    (Cmd 12), non mécanique.
  - **Découverte hors périmètre du signalement initial** : `doctrinal/index.md`
    (§IX) portait aussi `[[meta/sidy|Profil : Sidy]]` — même violation de
    sens, mais sur un fichier **non append-only** (à la différence des
    annales), donc directement corrigible sans tension avec Cmd 9/Cmd 10.
- **Résolution** :
  - `doctrinal/annales.md` : **aucune modification**. Les 3 liens vivent
    dans des entrées déjà publiées, datées, append-only (Cmd 9) — les
    rétracter serait une réécriture de l'historique (Cmd 10,
    non-révisionnisme), le remède serait pire que le mal pour un journal
    qui documente fidèlement l'état du dépôt au jour de sa rédaction. Le
    hub `meta-index.md` (ouvert la veille, entrée précédente) donne
    désormais à chacune des 3 fiches visées un lien entrant légitime,
    intra-`meta/`, qui existe indépendamment de ces liens historiques —
    l'étanchéité n'est donc plus la seule voie d'accès vers ces fiches
    depuis un contexte publié.
  - `doctrinal/index.md` (§IX) : lien `[[meta/sidy|Profil : Sidy]]`
    **retiré**, remplacé par un renvoi générique vers
    `[[meta/meta-index|meta-index]]` (le hub du domaine réservé lui-même
    porte déjà `[[meta/personnel/sidy|Sidy]]`, l.21 — aucun orphelinage
    introduit). Ce fichier n'étant pas append-only, la correction directe
    ne pose aucune tension avec Cmd 9/Cmd 10. `updated:` remonté à
    2026-08-09.
  - **Verdict de principe retenu pour le futur** : une entrée d'annales
    déjà publiée qui contrevient à §VI par un lien isolé n'est **pas**
    reprise après coup ; mais tout fichier non append-only du corps
    doctrinal (`index.md` notamment) qui contreviendrait de la même façon
    **est** corrigé sans délai, l'étanchéité y primant sur toute autre
    considération puisqu'aucune discipline d'immutabilité ne s'y oppose.
- **Vérification** : `python3 verifier-invariants.py --racine /root/wiki`
  → 0 erreur(s), 0 avertissement(s), avant et après les deux édits
  (`doctrinal/index.md`, `meta/meta-annales.md`). `carte-du-depot.py`
  régénéré, aucune orpheline nouvelle introduite.
- **Compréhension tirée** : un signalement de sens interdit sur un fichier
  append-only ne se résout pas comme sur un fichier ordinaire — la
  discipline d'immutabilité de Cmd 9/Cmd 10 prime sur §VI *a posteriori*,
  alors qu'elle ne le protège jamais *a priori* (rien n'empêchait de ne
  pas écrire ce lien en 2026-06-20). Le hub `meta-index.md`, en offrant un
  point d'entrée alternatif et conforme, absorbe la tension sans qu'il
  soit nécessaire de toucher au journal historique. Second enseignement :
  vérifier un signalement par grep direct avant de le trancher, plutôt que
  de faire confiance à sa reformulation dans une entrée antérieure — une
  erreur de recopie (`gout-sucre-priere`) avait survécu sans être
  requestionnée.
- **Liens** : [[meta/meta-index|meta-index]] ; [[meta/meta-annales|meta-annales]] ;
  entrée précédente (ouverture du hub, signalement initial, partiellement
  erronée sur `gout-sucre-priere`).
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Ouverture du hub `meta-index.md`/`meta-annales.md` — traitement des 66 orphelines de `meta/`, acceptation documentée des 14 restantes

- **Symptôme** : suite à l'entrée précédente (bug de résolution corrigé, 80
  orphelines réelles au comptage final), instruction explicite de Sidy : « Je
  t'autorise à traité toutes les fiches, même personnel ». Sur les 80, 66
  vivaient dans `meta/` (`personnel/`, `genealogie/`, `journal/`,
  `transmissions/`, `projet-unifie/` y compris `hermes-prompts/`) — matières
  couvertes par l'étanchéité §VI, non traitables par simple lien depuis un
  circuit.
- **Diagnostic** : blocage structurel — `meta/` n'a ni `index.md` ni
  `annales.md`, contrairement aux quatre circuits qui en ont chacun un ; il
  n'existait donc aucun hub interne légitime depuis lequel créer des liens
  vers ces 66 fiches. Créer des fichiers nommés `index.md`/`annales.md` dans
  `meta/` aurait fait lire le domaine comme un sixième circuit, ce que
  CLAUDE.md dément explicitement (« Domaine Réservé », pas un circuit).
- **Signalement séparé, à part** (Cmd 7, non traité par cette entrée) : 4
  fiches `meta/personnel/` (`bourdonnement-tempe`, `gout-sucre-priere`,
  `taekwondo-hansu`) et `meta/projet-unifie/briefing-claude-ai` reçoivent leur
  seul lien entrant depuis `doctrinal/annales.md` — sens neutre → sensible,
  interdit par §VI. Consigné ici comme signalement ouvert ; aucune action
  corrective (hors périmètre de l'autorisation donnée, qui porte sur le
  traitement des orphelines, pas sur cette violation de sens inverse).
  Verdict humain toujours attendu.
- **Résolution** : verdict Sidy — donner à `meta/` son propre hub, nommé avec
  le préfixe `meta-` pour écarter tout risque de confusion avec les
  `index.md`/`annales.md` des circuits (proposition initiale de Sidy :
  « meta/ gets it's own referenced link with the same exact names, index and
  annales as the others circuits exept it will bare the prefix » ; nommage
  exact tranché par question : `meta-index.md` / `meta-annales.md`).
  - `CLAUDE.md` amendé (§II arborescence, §VI Domaine Réservé, §X Cmd 9) pour
    documenter le hub et son statut distinct d'un circuit.
  - `verifier-invariants.py` adapté : `meta-annales.md` ajouté à
    `NOMS_ANNALES` (contrôles A0-A5 d'append-only) ; `meta-index.md` ajouté à
    `FICHIERS_EXEMPTS_C3` et à la détection `fichier_de_service` (exemption
    Sceau Recteur, `type: meta`).
  - `carte-du-depot.py` adapté : `meta/meta-index` et `meta/meta-annales`
    exclus du décompte des orphelines dans `rendre_liens()`, au même titre
    que tout `*/index` et `*/annales`.
  - `meta/meta-index.md` créé : hub recensant par sous-dossier
    (`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
    `projet-unifie/` y compris `hermes-prompts/`/`hermes-skills/`, fiches de
    premier niveau) l'ensemble des fiches du domaine, chacune avec un
    wikilink de la forme `meta/<chemin>` accompagné du titre exact, fidèle à
    son titre ou en-tête réel — aucun
    contenu des 66 fiches n'a été modifié, seul un lien entrant a été créé.
    Résout d'un coup l'orphelinage des 66 fiches `meta/`.
  - `meta/meta-annales.md` créé : squelette minimal, append-only, première
    entrée `[2026-08-09] ouverture` documentant la création du hub.
  - Les 14 fiches restant orphelines hors `meta/` (13 stubs `deprecated` de
    `atelier/projets/`, pointant déjà vers leur fiche canonique en `rd/`, +
    `doctrinal/discernement/_template.md`, gabarit jamais destiné à être lié)
    ne reçoivent **aucun** lien artificiel — acceptées par conception, même
    régime que les fichiers de service. Consigné explicitement pour ne pas
    laisser un chiffre non expliqué.
- **Vérification** : `verifier-invariants.py --racine /root/wiki` → 0
  erreur(s), 0 avertissement(s), avant et après chaque étape. Régénération de
  `meta/carte-du-depot.md` → orphelines réelles : 80 → **14**, toutes
  documentées ci-dessus, aucune résiduelle non expliquée.
- **Compréhension tirée** : un domaine « réservé » qui n'est pas un circuit a
  quand même besoin d'un mécanisme de maillage interne — sinon toute fiche
  qu'on y range est structurellement condamnée à l'isolement, indépendamment
  de son contenu. Le nommage préfixé (`meta-` plutôt que nu) permet de doter
  un domaine réservé d'un hub sans lui faire perdre son statut distinct d'un
  circuit — la distinction se lit dans le nom du fichier, pas seulement dans
  la prose de CLAUDE.md.
- **Liens** : `CLAUDE.md` §II/§VI/§X ; `verifier-invariants.py` ;
  `carte-du-depot.py` ; [[meta/meta-index|meta-index]] ;
  [[meta/meta-annales|meta-annales]] ; entrée précédente (bug de résolution).
- **Statut** : `resolu` — 66/66 orphelines `meta/` traitées ; `ouvert` pour le
  signalement séparé (sens interdit `doctrinal/annales.md → meta/personnel/`,
  verdict humain attendu).

---

## [2026-08-09] resolu | Bug de résolution des liens entrants dans carte-du-depot.py (89 orphelines annoncées, 81 réelles) + traitement du lot non sensible

- **Symptôme** : suite à la clôture de l'épisode H‍ermes (entrée précédente),
  instruction de traiter les 89 fiches sans lien entrant listées en §VI de
  `meta/carte-du-depot.md`. Avant tout traitement, vérification individuelle
  d'un échantillon des 89 : `meta/genealogie/2026-06-20_signature-kouyate` est
  citée dans la liste, alors que `meta/genealogie/2026-06-20_oiseau-serpent-jumeau.md`
  contient un wikilink pointant vers elle (`[[meta/2026-06-20_signature-kouyate]]`),
  et `verifier-invariants.py` ne signale aucun lien mort sur cette cible.
- **Diagnostic** : lecture du code de `rendre_liens()` dans `carte-du-depot.py`.
  Le script résout les wikilinks par correspondance exacte de chemin, avec un
  repli par nom court (`par_nom`) — mais ce repli n'agit que si le lien est
  écrit **sans aucun préfixe de répertoire**. Un lien écrit avec un préfixe de
  répertoire partiel mais devenu obsolète (ex. `[[meta/2026-06-20_signature-kouyate]]`,
  rédigé avant que la fiche soit rangée sous `meta/genealogie/`) n'est reconnu
  ni comme résolu ni comme mort : il est silencieusement ignoré, et sa cible
  réelle est comptée à tort comme sans lien entrant. Vérification systématique
  par script (résolution étendue au nom de fichier final, quel que soit le
  préfixe présent) : sur les 89 annoncées, **7 ont en réalité un lien entrant**
  (`atelier/etudes-de-cas/stones-throw`,
  `meta/genealogie/2026-06-20_oiseau-serpent-jumeau`,
  `meta/genealogie/2026-06-20_signature-kouyate`,
  `meta/personnel/2026-06-20_bourdonnement-tempe`,
  `meta/personnel/2026-06-20_gout-sucre-priere`,
  `meta/personnel/2026-06-20_taekwondo-hansu`,
  `meta/projet-unifie/briefing-claude-ai`). Total réel : **81** orphelines, pas
  89. Classification des 81 par lot :
  - 12 stubs `deprecated` (`atelier/projets/*`, Cmd 10) — terminus par design ;
  - 1 gabarit (`doctrinal/discernement/_template`) — non-cible par nature ;
  - 2 fiches `rd/` référencées seulement en prose par `atelier/rd/index.md`
    (`cahiers/registre-problemes`, `infrastructure/synchro-obsidian-working-copy-github`) —
    seul défaut structurel réellement corrigible sans toucher à un circuit
    sensible ;
  - 7 fiches `meta/` déjà `status: deprecated` ou notes opérationnelles closes —
    isolement cohérent avec leur statut, aucune action ;
  - reste (~59) : `meta/genealogie/`, `meta/personnel/`, `meta/journal/`,
    `meta/transmissions/karubi-*`, `meta/projet-unifie/*` (dont plusieurs sans
    frontmatter, qui recoupent l'anomalie déjà ouverte le 2026-08-08) — tous
    dans des matières couvertes par l'étanchéité §VI ou déjà signalées
    ailleurs ; aucun lien ajouté sans verdict Sidy au cas par cas.
- **Résolution** : lot des 2 fiches `rd/` traité — `atelier/rd/index.md`
  converti en wikilinks réels (`[[atelier/rd/cahiers/registre-problemes]]` et
  ajout de `[[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]]`
  dans la table des frontières, absente jusqu'ici même en prose).
  `verifier-invariants.py` → 0 erreur, 0 avertissement. `carte-du-depot.py`
  régénéré → 87 fiches sans lien entrant (89 → 87, conforme). Les lots
  sensibles (généalogie, personnel, journal, transmissions, projet-unifié)
  restent en l'état, en attente de verdict Sidy fiche par fiche ou lot par
  lot.

  **Complément (même jour)** : correctif appliqué à `carte-du-depot.py` sur
  autorisation explicite. Dans `rendre_liens()`, ajout d'un second repli de
  résolution : quand une cible de lien n'est ni un chemin exact ni un nom
  court sans préfixe, tentative de correspondance sur le seul nom de fichier
  final (`c.rsplit("/", 1)[-1]`), retenue si un unique candidat du dépôt y
  correspond — même logique que le repli `par_nom` existant, étendue aux
  préfixes de répertoire partiels/obsolètes. `carte-du-depot.py` régénéré →
  87 → **80** fiches sans lien entrant ; les 7 faux positifs identifiés
  n'apparaissent plus dans la liste. `verifier-invariants.py` → 0 erreur, 0
  avertissement (inchangé, le correctif ne touche que la carte dérivée,
  jamais les invariants structurels). Chiffre définitif retenu : **80**
  orphelines réelles.
- **Compréhension tirée** : le même piège que le self-report H‍ermes s'applique
  à un artefact du dépôt lui-même — un chiffre produit par un script n'est
  fiable qu'après lecture de son mécanisme de calcul, pas seulement de sa
  sortie. Avant tout traitement de masse sur un signalement chiffré (« N
  fiches orphelines », « N liens morts »), vérifier individuellement un
  échantillon contre le dépôt réel et, en cas d'écart, lire le code du script
  générateur plutôt que de corriger les fiches pour faire correspondre le
  chiffre. Second enseignement : sur un dépôt à étanchéité stricte (§VI),
  « traiter des orphelines » ne veut pas dire « ajouter des liens partout » —
  la majorité des orphelines réelles sont orphelines *par construction*
  (stubs terminaux, gabarits, circuits sensibles isolés à dessein) et
  n'appellent aucune action.
- **Liens** : `carte-du-depot.py` (fonction `rendre_liens()`, résolution
  `par_nom` + repli nom de fichier final) ; `meta/carte-du-depot.md`
  (régénéré 2026-08-09, §VI, 80 orphelines) ; `atelier/rd/index.md` (2
  wikilinks ajoutés) ; entrée précédente du présent registre (self-report
  H‍ermes) pour le fil de l'investigation ; anomalie frontmatter du
  2026-08-08 pour le recoupement `hermes-prompts/*`.
- **Statut** : `resolu` pour le lot C traité, le bug de script diagnostiqué
  et corrigé ; `ouvert` implicitement pour les lots sensibles restants (80
  fiches), en attente de verdict — suivi à réouvrir en entrée dédiée si Sidy
  tranche sur un de ces lots.

---

## [2026-08-09] resolu | Self-report H‍ermes Agent erroné sur le maillage wikilinks (317/403 annoncés vs 89/390 réels)

- **Symptôme** : constat visuel sur la Vue graphique Obsidian (iPad, 2026-08-09) —
  un large anneau de points quasi sans liens, dont cinq fiches-sources
  doctrinales identifiées nommément :
  `guenon-etats-multiples-ch13-hierarchies-spirituelles`,
  `guenon-symbolisme-croix-ch4-directions-espace`,
  `guenon-kundalini-yoga-etudes-hindouisme`,
  `ibn-arabi-de-la-mort-a-la-resurrection-gloton`, `sept-etendards-califat`.
  Interrogé côté serveur sur ce constat, H‍ermes Agent a répondu par un
  self-report : « 317 fiches sur 403 sans lien entrant », répartition par
  circuit (doctrinal 151, meta 95, atelier 44, label 12, hermeneutique 9),
  et une explication selon laquelle le protocole relierait les fiches par
  « références textuelles » plutôt que par wikilinks (double crochets).
- **Diagnostic** : vérification mécanique intégrale des deux affirmations.
  `verifier-invariants.py --racine /root/wiki` → 0 erreur, 0 avertissement.
  `carte-du-depot.py` → 390 fiches parcourues, **89** sans lien entrant (pas
  317). Aucun script du dépôt ne reproduit ni le total de 403 fiches valides
  (403 = compte brut de fichiers `.md`, avant exclusion de `raw/` et des
  fichiers sans frontmatter YAML — `CLAUDE.md`, `README.md`, plusieurs
  `hermes-prompts/*.md`, etc. ; 390 est le chiffre correct), ni la
  répartition par circuit annoncée. Vérification individuelle des 5 fiches
  citées comme motif : **aucune n'est orpheline**. Toutes ont
  `cross_links`/`sources` renseignés conformément au Sceau Recteur (§IV) et
  des liens entrants réels et multiples (`doctrinal/index.md`,
  `doctrinal/annales.md`, et jusqu'à 15 fichiers citants pour la fiche
  Ibn ʿArabī/Gloton). L'explication d'H‍ermes (maillage hors wikilinks) est donc
  réfutée par les faits sur le cas précis qui l'a motivée : le mécanisme
  `sources`/`cross_links` en wikilinks, tel que défini par le protocole,
  fonctionne correctement pour ces cinq fiches.
- **Résolution** : aucune correction de maillage nécessaire — il n'y avait
  pas de défaut réel sur les fiches à l'origine du constat. Le déficit
  mécanique véritable (89/390 fiches sans lien entrant) reste réel mais d'un
  ordre de grandeur très différent de l'annonce d'H‍ermes, concentré
  principalement dans `meta/personnel/`, `meta/projet-unifie/`,
  `meta/genealogie/`, `meta/transmissions/` et les stubs `deprecated` de la
  migration `rd/` (orphelinage volontaire, non anormal) — traitement séparé,
  hors objet de cette entrée.
- **Compréhension tirée** : un self-report d'agent conversationnel — même
  chiffré avec précision et accompagné d'une explication plausible et
  conforme en apparence à la lettre du protocole — n'est pas une source
  fiable sur l'état structurel du dépôt. Ici, l'agent a produit un chiffre
  erroné (317 au lieu de 89, plus de 3× l'écart), une répartition par
  circuit sans fondement, et une explication qui contredit le Sceau Recteur
  tel qu'écrit. Avant tout signalement fondé sur un constat visuel Obsidian
  ou un rapport d'agent, exécuter systématiquement `verifier-invariants.py`
  et `carte-du-depot.py`, et vérifier individuellement toute fiche citée
  nommément comme preuve — jamais de self-report en position de source.
- **Liens** : `meta/carte-du-depot.md` (généré 2026-08-09 03:48 UTC, §VI
  « Fiches sans lien entrant (89) », §VII statistiques) ;
  `doctrinal/sources/guenon-etats-multiples-ch13-hierarchies-spirituelles.md` ;
  `doctrinal/sources/guenon-symbolisme-croix-ch4-directions-espace.md` ;
  `doctrinal/sources/guenon-kundalini-yoga-etudes-hindouisme.md` ;
  `doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md` ;
  `doctrinal/sources/sept-etendards-califat.md`.
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Contenu du sas `_inbox/` poussé par erreur sur le dépôt

- **Symptôme** : le commit `d73cdb6` (intégration de la fiche synchro
  Obsidian) contient les fichiers `_inbox/karubi-mehdi.md` et
  `_inbox/image.jpeg`, ajoutés par un `git add -A` trop large.
- **Diagnostic** : faute d'opérateur — le sas `_inbox/` est par définition
  non versionné tant que l'intégration n'a pas eu lieu (cf. entrée
  [2026-08-09] ci-dessous, vault désynchronisé : « laissé non versionné — ne
  doit pas partir sur le dépôt sans passage par le circuit d'intégration »).
  `git add -A` à la racine ramasse tout, sas compris.
- **Résolution** : commit correctif immédiat `87ca442`
  (`git rm --cached` sur les deux fichiers + push). Les fichiers ne sont plus
  suivis ; l'historique du remote conserve toutefois le blob du commit fautif
  (dépôt privé — pas de réécriture d'historique sans verdict Sidy).
- **Compréhension tirée** : dans ce dépôt, ne jamais committer par
  `git add -A` depuis la racine ; ajouter nommément les fichiers intégrés
  (ou utiliser `git add -A -- <chemins>` hors `_inbox/`). Le sas est
  intouchable par Git tant que l'intégration n'est pas faite.
- **Liens** : commits `d73cdb6`, `87ca442` ; entrée ci-dessous
  (vault désynchronisé).
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Vault Obsidian (iPad) désynchronisé — 6 commits serveur jamais poussés

- **Symptôme** : le vault Obsidian sur l'iPad de Sidy n'est « plus du tout à
  jour » depuis un certain temps. Le vault = le dépôt wiki lui-même, consulté
  sur iPad via Obsidian en auto-pull depuis GitHub (`Sidyvision/wiki`,
  `CLAUDE.md` §postes : CONSULTATION).
- **Diagnostic** : aucun problème de configuration Obsidian côté serveur —
  l'auto-pull de l'iPad tire `origin/main`, or le serveur était en avance de
  6 commits non poussés (ouverture du pôle rd/, migration `projets/ → rd/`,
  arbitrage `album-personnel`, annales) plus 3 fichiers de travail non
  commités (registre des problèmes, thème natal corrigé, mise en regard
  roue/thème). La « connexion cassée » était simplement une chaîne de push
  interrompue côté serveur.
- **Résolution** : commit des 3 fichiers en attente puis `git push origin main`
  (7 commits au total). L'auto-pull de l'iPad récupérera l'état complet au
  prochain cycle. `_inbox/` (sas en attente d'intégration, contient des PDF
  bancaires) laissé non versionné — ne doit pas partir sur le dépôt sans
  passage par le circuit d'intégration.
- **Compréhension tirée** : un vault « cassé » peut n'être qu'un dépôt local en
  avance sur son remote. Avant d'incriminer l'outil de consultation (Obsidian,
  ses plugins, sa synchro), vérifier l'état git (`git status -sb`,
  `rev-list --left-right --count origin/main...HEAD`) : c'est le maillon serveur
  qui portait le retard.
- **Liens** : `CLAUDE.md` §postes (CONSULTATION = Obsidian iPad auto-pull) ;
  remote `git@github.com:Sidyvision/wiki.git`.
- **Statut** : `resolu`.

---

## [2026-08-08] resolu | Vision Hermes en 404 sur l'endpoint Qwen (auto-détection auxiliaire mal routée)

- **Symptôme** : l'outil `vision_analyze` échoue systématiquement avec
  `Error code: 404` ; mêmes échecs consignés pour les tâches auxiliaires
  `compression` et `title_generation` dans `~/.hermes/logs/agent.log` et
  `errors.log`. La conversation principale fonctionne normalement par ailleurs.
- **Diagnostic** : les tâches auxiliaires sont par défaut en `provider: auto`.
  L'auto-détection réécrit l'URL de base
  `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic` →
  `.../apps/v1` (règle générique pour les endpoints « anthropic-compatibles »),
  puis le SDK Anthropic ajoute `/v1/messages` : l'appel arrive sur
  `.../apps/v1/v1/messages`, qui n'existe pas. L'endpoint Qwen n'expose que la
  surface `anthropic_messages` sur `/apps/anthropic/v1/messages` (vérifié :
  le fil OpenAI `/apps/v1/chat/completions` renvoie lui aussi 404). Test
  discriminant : le même appel épinglé sur `custom:qwen` réussit (réponse
  correcte à l'analyse d'image), l'appel auto-détecté échoue en 404.
- **Résolution** : épinglage
  `auxiliary.{vision,compression,title_generation,web_extract}.provider: custom:qwen`
  via `hermes config set` sur le profil principal ET les 12 profils Discord
  (ar-music, visual-da, production, admin-legal, accounting, distribution,
  marketing, publication, studio, gardien, fanzine, commerce). Vérification en
  direct après coup : `vision_analyze` répond correctement (test carré rouge →
  « Red »).
- **Compréhension tirée** : quand le provider principal est un endpoint
  Anthropic-compatible qui n'expose QUE cette surface, l'auto-détection
  auxiliaire (`auto`) est trompeuse — elle présuppose que l'endpoint parle aussi
  OpenAI. Il faut épingler explicitement toutes les tâches auxiliaires sur le
  provider nommé. Un échec « vision » peut donc être un problème de routage
  auxiliaire, pas du modèle.
- **Liens** : `~/.hermes/config.yaml` (profil `default` + 12 profils) ;
  `~/.hermes/logs/agent.log` ; code Hermes `agent/auxiliary_client.py`
  (`_to_openai_base_url`, `resolve_vision_provider_client`) ;
  [[meta/projet-unifie/15-architecture-discord-hermes-2026-08-07]].
- **Statut** : `resolu`.

---

## [2026-08-08] resolu-partiel | 4 anomalies d'étanchéité `materiel → album-personnel` coupées

- **Symptôme** : 4 des 10 anomalies bloquantes du graphe (entrée ci-dessous) :
  `atelier/materiel/{neve-1073spx, studio-principal, tascam-model-12,
  technics-su-8080}.md` (neutre, rang 0) → `atelier/projets/album-personnel.md`
  (rang 1) — liens remontants, interdits (§VI).
- **Diagnostic** : liens historiques hérités de la création des fiches materiel
  (2026-06-20), antérieurs à la formalisation de l'étanchéité. Devenus sans
  objet légal après le déplacement d'`album-personnel` vers `label/` (rang 2) :
  le sens licite est label → materiel, porté par `liens_atelier` (§V.b) de la
  fiche canonique.
- **Résolution** : les 4 liens coupés le 2026-08-08 — frontmatter (`links`) et
  corps de texte — lors de l'exécution du verdict d'arbitrage. Aucune fiche
  supprimée ; l'information de contexte (« projet dans lequel cet appareil est
  utilisé ») subsiste côté label.
- **Compréhension tirée** : un arbitrage de circuit est l'occasion naturelle de
  purger les violations d'étanchéité qui pointaient vers la fiche arbitrée —
  le déplacement change le rang de la cible et rend caducs les liens entrants
  du neutre.
- **Liens** : entrée ci-dessous (10 anomalies) ; [[label/production/album-personnel]] ;
  [[atelier/projets/album-personnel]] (stub) ; `CLAUDE.md` §VI.
- **Statut** : `resolu` pour les 4 liens ; l'entrée « 10 anomalies » passe à
  6 anomalies restantes (4 doctrinal → v0_3 + 2 frontmatter).

---

## [2026-08-08] ouvert | `graphe-cartographie.json` jamais régénéré (bloqué par les anomalies du graphe)

- **Symptôme** : `generer-cartographie.py` refuse d'écrire
  `graphe-cartographie.json` en présence d'anomalie bloquante ; le JSON de
  cartographie est absent du dépôt (jamais régénéré depuis son introduction).
- **Diagnostic** : conséquence directe de l'entrée suivante. **Correction du
  2026-08-11** : le diagnostic initial (« strict par conception ») était déjà
  obsolète au moment où il a été écrit — `generer-cartographie.py` est en v1.1
  depuis le 2026-07-22 (antérieure à cette entrée) et distingue déjà BLOQUANT
  (frontmatter absent, étanchéité — gouvernance du dépôt, non contournable par
  design) et AVERTISSEMENT (lien mort/ambigu, `sources_count` incohérent — la
  fiche reste dans le graphe). Le script n'a jamais eu besoin d'un mode tolérant :
  il l'a déjà. Ce qui bloque encore l'écriture du JSON n'est pas un défaut
  d'outillage mais des anomalies de contenu réelles, volontairement classées
  BLOQUANT par le script (voir entrée suivante).
- **Résolution** : 4/6 anomalies bloquantes restantes levées le 2026-08-11
  (fourche `v0_3`/`v0.3` + liens `doctrinal → v0_3`, entrée dédiée ci-dessous) ;
  restent 2 `frontmatter`. Le JSON reste donc non régénéré tant que ces 2
  dernières anomalies (contenu doctrinal, hors périmètre de cette session) ne
  sont pas traitées — comportement voulu du script, pas un blocage à lever côté
  outillage.
- **Compréhension tirée** : vérifier l'état réel du code avant de reconduire un
  diagnostic d'une entrée antérieure — un script peut évoluer plus vite que le
  registre qui le décrit. Un générateur à deux niveaux de sévérité (BLOQUANT vs
  AVERTISSEMENT) répond structurellement à la question « faut-il un mode
  tolérant ? » sans qu'il soit besoin de rouvrir l'arbitrage à chaque anomalie
  bloquante résiduelle — ces dernières relèvent du contenu, pas du script.
- **Liens** : entrée suivante ; `Graphe/generer-cartographie.py` (docstring v1.1,
  2026-07-22) ; entrée fourche `v0_3`/`v0.3` ci-dessous ;
  [[meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08|proposition de pôle]].
- **Statut** : `partiellement-resolu` — le générateur n'a jamais nécessité de
  correctif ; 4/6 anomalies de contenu restantes levées, 2 `frontmatter` ouvertes
  (hors périmètre R&D/outillage).

---

## [2026-08-08] ouvert | 10 anomalies bloquantes du graphe (8 étanchéité + 2 frontmatter), pré-existantes

- **Symptôme** : `generer-cartographie.py` remonte 10 anomalies :
  - 2 `frontmatter` — frontmatter absent (le fichier ne commence pas par `---`) :
    `doctrinal/sources/transcription-index-tilak-origine-polaire.md`,
    `doctrinal/sources/transcription-table-matieres-symboles-science-sacree.md` ;
  - 4 `étanchéité` — `atelier/materiel/*` (neutre) →
    `atelier/projets/album-personnel.md` (plus sensible) ;
  - 4 `étanchéité` — `doctrinal/sources/guenon-*` (neutre) →
    `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
    (plus sensible).
- **Diagnostic** : toutes pré-existantes à la migration `projets/ → rd/` — vérifié
  point par point contre un export `git archive` de HEAD (mêmes 10 anomalies avant
  et après). La migration n'en introduit aucune.
- **Résolution** : les 4 liens `materiel → album-personnel` dépendaient du verdict
  d'arbitrage `album-personnel` (`rd/` vs `label/`), rendu le 2026-08-08 (`label/`).
  Les 4 liens `doctrinal/sources → v0_3` : traités fiche par fiche le 2026-08-11 —
  retirés côté `doctrinal/` (sens interdit par §VI) et reportés en sens licite dans
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`
  (voir entrée dédiée ci-dessous, fourche `v0_3`/`v0.3`).
- **Compréhension tirée** : avant d'attribuer une régression à une opération,
  comparer contre la baseline (HEAD) — ici la comparaison a innocenté la migration
  et isolé un passif ancien. Le registre doit consigner les anomalies dès leur
  découverte, pas seulement celles qu'on introduit.
- **Liens** : `Graphe/generer-cartographie.py` ; arbitrage `album-personnel.md`
  (verdict Sidy rendu le 2026-08-08 : `label/`) ; `CLAUDE.md` §VI ; entrée
  fourche `v0_3`/`v0.3` ci-dessous.
- **Statut** : `partiellement-resolu` — 8/10 levées (4 `materiel → album-personnel`
  le 2026-08-08, 4 `doctrinal → v0_3` le 2026-08-11) ; restent 2 `frontmatter`
  (`transcription-index-tilak-origine-polaire.md`,
  `transcription-table-matieres-symboles-science-sacree.md`), non traités cette
  session (hors périmètre outillage/rd — contenu doctrinal).

---

## [2026-08-08] resolu | Lien mort `manvantara → v0_2` (version inexistante)

- **Symptôme** : `doctrinal/symboles/manvantara.md` pointait vers une version
  `v0_2` (underscore) de l'architecture de l'Instrument, inexistante dans le dépôt.
- **Diagnostic** : coquille de slug — la cible `v0_2` n'existe pas ; le lien a été
  repointé vers `v0.3` conformément aux annales de la migration.
- **Résolution** : lien repointé vers `v0.3` lors de la migration (repérage des
  liens entrants).
- **Compréhension tirée** : les slugs de versions sont proches (`v0.3` / `v0_3`)
  et faciles à confondre ; un lien mort de ce type est silencieux tant qu'un
  générateur ou une relecture ne le remonte pas. À terme, un contrôle des liens
  entrants (ou le manifeste) devrait signaler toute cible inexistante.
- **Liens** : `doctrinal/symboles/manvantara.md` ;
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`.
- **Statut** : `resolu`.

---

## [2026-08-11] resolu | Fourche `v0_3`/`v0.3` de l'Instrument + 4 liens `doctrinal → v0_3` en sens interdit

- **Symptôme** : en instruisant les 4 anomalies d'étanchéité `doctrinal/sources →
  v0_3` (entrée « 10 anomalies » ci-dessus), découverte que
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
  (tiret bas) et `...v0.3.md` (point) coexistaient comme deux fiches indépendantes
  — même exact avertissement déjà consigné dans l'entrée `manvantara → v0_2`
  ci-dessus (« slugs de versions proches, faciles à confondre »), non appliqué à
  cette paire au moment de la migration `projets/ → rd/` du 2026-08-08 (les deux
  fourches existaient déjà côté `projets/`, migrées chacune séparément).
- **Diagnostic** : comparaison ligne à ligne des deux fiches — contenu identique
  jusqu'au §3.4 ; `v0.3` (point) porte en plus le §3.5 (nœud universel, verdict
  Sidy 2026-08-04) et une date `updated` plus récente. `v0_3` (tiret bas) est une
  version figée du 2026-07-01, jamais mise à jour depuis. Les 4 liens
  `doctrinal/sources/guenon-*` pointaient tous vers la fourche obsolète, en plus
  d'être dans le sens interdit par §VI (`doctrinal` neutre → `rd/` plus sensible).
- **Résolution** : `v0_3.md` repassée `deprecated` avec pointeur vers `v0.3.md`
  (Cmd 10, fusion sans perte confirmée) ; `atelier/index.md` repointé vers
  `v0.3.md` ; les 4 `cross_links` illicites retirés des fiches
  `doctrinal/sources/guenon-*` ; liens reportés en sens licite dans le champ
  `links` de `v0.3.md`.
- **Compréhension tirée** : une migration fiche-par-fiche (Cmd 10) qui déplace
  deux fourches d'un même document sans les comparer d'abord propage la
  confusion au lieu de la résoudre — le repérage `v0.3`/`v0_3` aurait dû se faire
  une fois pour toutes lors de la migration du 2026-08-08, pas fiche par fiche à
  chaque anomalie découverte ensuite. Un contrôle de similarité de slugs (au-delà
  du seul contrôle de liens morts) serait pertinent en amont d'une prochaine
  migration.
- **Liens** : entrée « 10 anomalies » ci-dessus ; entrée `manvantara → v0_2` ;
  [[atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3]] ;
  `CLAUDE.md` §VI, Cmd 10.
- **Statut** : `resolu`.
