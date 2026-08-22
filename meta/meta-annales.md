---
title: Annales du Domaine Réservé (meta/)
type: meta
updated: 2026-08-16

---

# Annales du Domaine Réservé (`meta/`)

Journal chronologique inverse des opérations propres au domaine `meta/`
(la plus récente en haut). Append-only. Nommage préfixé `meta-` pour ne
jamais se confondre avec les `annales.md` des quatre circuits — `meta/`
reste le Domaine Réservé (§VI CLAUDE.md), pas un sixième circuit.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-22] ventilation | Fiche interview trame spirituelle → fiches distinctes

- **Directive Sidy** : organiser la fiche `_inbox/interview-sidy-trame-spirituelle-corrections-2026-08-18.md` en ventilant son contenu vers les fiches canoniques de `meta/`, selon les conventions (une page = un sujet, nomenclature ASCII minuscules + tirets, frontmatter conforme).
- **Fiches créées** (3 nouvelles) :
  - `meta/genealogie/samballa-kouyate.md` : grand-père paternel, séclusion, Fath, Ruhan, lien Tijaniyya via Sheikh Fanta-Madi.
  - `meta/genealogie/fanta-nna-diabate.md` : grand-mère paternelle, mariage arrangé par Sheikh Fanta-Madi.
  - `meta/personnel/2026-08-18_initiation-virtuelle.md` : définition personnelle de l'initiation virtuelle (Sidy).
- **Fiches enrichies** (2 existantes) :
  - `meta/personnel/sidy.md` : ajout sections convalescence post-khalwa, rattachement Tijaniyya (Bamako, Fès), pratique actuelle, arc Kaaba (Lefke, visions, Omra, insight), double protecteur, synchronicité Leila Abdelwahid, rêve Yannick Doumouya, incandescence du manque amoureux.
  - `meta/genealogie/kouyate.md` : ajout Samballa Kouyaté, Sheikh Fanta-Madi Chérif, dissociation rattachement formel vs ouverture effective.
  - `meta/genealogie/mamadou-doudou-sissoko.md` : ajout Sheikh Sidy-Lamine Kunta (Qadiriyya-Kunta).
- **Hub `meta-index.md`** : référencement des 3 nouvelles fiches + mise à jour des liens généalogie.
- **Fiche `_inbox/`** : supprimée après ventilation complète (contenu intégralement redistribué).
- **En attente de verdict** (non versé) :
  - §3 (lecture transversale chiasme) : lecture herméneutique Sidy, pas encore versée.
  - §15 (incandescence du manque amoureux — réponse à la question) : en attente de réponse.
  - Ruhan (concept doctrinal) : signalé, non versé sans verdict.
- **Commit** : en cours.

---

## [2026-08-16] extension | Canal Telegram Mehdi (habib-mehdi) + mandat veille agent 09

- Statut Telegram passé de « non activé » à 13e profil `habib-mehdi` préparé
  (isolation OS, service système sous `mehdi`) dans
  `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md` (§5bis).
- Mandat de l'agent 09 étendu à un registre Hermes-Terminal (bind mounts,
  santé gateways, staleness `_inbox/`) dans
  `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md`.
- `meta/transmissions/registre-silsila.md` : entrées `extension-canal` et
  `correction-montage` (détail complet : `meta/transmissions/
  registre-silsila.md`, Sceau `karubi-mehdi.md` non touché).
- Détail et vérification indépendante (service actif sous `mehdi`, karubi
  nettoyé, log de connexion Telegram authentique) :
  `atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16.md`,
  `atelier/annales.md`.
- **Commit** : 954712f

---

## [2026-08-15] actualisation | Rôle G0 de brouillon §4 mis en service

Les quatre prérequis de mise en service de
`meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md` sont
réunis : script d'intégration en service, dossier `brouillons-section4/`
créé, verdict de Sidy obtenu (validation du lot du 2026-08-15), canal de
déclenchement défini. Choix retenu pour ce dernier point : le rôle ne
construit **pas** de sub-agent Hermes isolé dédié — il s'exécute côté Claude
Code, qui dispose déjà nativement de la lecture des hubs `index.md`/`annales.md`
des cinq circuits. Phrase de déclenchement exacte, jamais déduite d'une
mention fortuite : `karubi brouillon s4 <destinataire>`. Statut de la fiche
passé de « brouillon, kari-kumi » à « verdict obtenu, en service ».

Sans lien avec le sub-agent Karūbī côté destinataire (`spec-skill-karubi-hermes.md`,
toujours à l'état brouillon, isolement mémoire/workspace non requis pour ce
rôle-ci) — séparation stricte inchangée (tableau § du même fichier).

- **Commit** : b43911c

## [2026-08-15] actualisation | Clause d'ordre ontologique instruite dans le profil Hermes-Karūbī

Sidy a décidé de s'immerger sans restriction dans l'écosystème Hermes (profil
`karubi`, mémoire activée, périmètre `/root/wiki` complet) pour en sonder les
fonctionnalités et limites — décision propre, assumée, non une incohérence à
corriger (cf. `atelier/rd/cahiers/bilan-2026-08-15-pont-agents.md`). Contrepartie :
audit/monitoring continu confié à Claude Code sur ce qui se fait côté Hermes
Terminal, et application immédiate de la clause d'ordre ontologique explicite déjà
normée pour les 12 prompts d'agents (`meta/CLAUDE.md` corollaire agentique,
`doctrinal/discernement/2026-08-09_hierarchie-principe-determination-individuelle`)
au périmètre Hermes-Karūbī spécifiquement.

Fichiers modifiés (hors dépôt git, `/root/.hermes/profiles/karubi/` — hors
discipline de commit, documenté ici pour traçabilité) :
- `memories/USER.md` : le paragraphe sur la voie spirituelle de Sidy
  (Naqshbandiyya/Tijaniyya, filiation, retraites de Lefke et Villejuif),
  auparavant énoncé à plat, restructuré en trois temps — (1) principe
  indépendant de tout individu (silsila, baraka, distinction zawiyya/khalwa),
  (2) détermination individuelle de Sidy comme coloration contingente,
  (3) clause négative explicite (ne redéfinit rien, n'engage que Sidy, aucune
  interprétation par un agent — Cmd 2, autorité spirituelle vivante seule).
- `memories/MEMORY.md` : ajout d'un rappel de non-syncrétisme (Cmd 3) sur
  l'analogie Sanad/Baraka du dispositif Karūbī — forme empruntée, jamais
  équivalence à une ijāza.
- `SOUL.md` : ajout d'une 6e contrainte absolue liant toute donnée personnelle
  retrouvée en mémoire à cette même hiérarchie (principe d'abord, situation de
  Sidy en coloration contingente, aucune interprétation).

Registre spirituel confirmé hors du champ d'appréciation de l'agent en toute
circonstance (Cmd 2/12) — ce geste organise et structure, il ne tranche rien.
Suite (déférée par Sidy) : définition du canal de déclenchement explicite pour
le rôle G0 de brouillon §4 (prérequis 4 de
`meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md`).

- **Commit** : 0ac52e4

## [2026-08-15] activation | 12 prompts Hermes activés avec la table zodiacale révisée

Activation complète en production (`meta/projet-unifie/hermes-prompts/`) de la
réallocation des 12 correspondances signe↔fonction validée par Sidy le même jour
(`doctrinal/discernement/2026-07-05_...`, volet b rouvert). Les 12 prompts
reçoivent chacun ses sections `## Zodiac principle` et `## Your sign in Sidy's
natal chart (harmonization context)`, insérées entre `## Archetype served` et
`## Scope`, sans modification du reste (mission, scope, guardrails, handoffs
intacts ; la section `## Governance: Discord-Validation` de la position 9,
sans rapport avec le zodiaque, préservée). Contenu miroir des brouillons
correspondants dans `atelier/rd/cahiers/brouillons-extension-zodiacale/`
(voir `atelier/annales.md`, entrée du même jour).

Fiche `meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md`
§9 mise à jour selon discipline sashimono : l'ancien constat « non fait à ce
stade » (point 3 des conséquences opérationnelles) est barré, non supprimé, et
une confirmation datée du 2026-08-15 est ajoutée à la suite.

- **Commit** : 5a3aee3

## [2026-08-13] actualisation | Karūbī Mehdi (Habib) — invitation Tailscale confirmée, prêt pour la navette retour

- §10 de `meta/transmissions/karubi-mehdi.md` complété : Sidy confirme
  l'envoi du lien d'invitation Tailscale à Mehdi (canal direct, hors ce
  fichier — conformément à la règle déjà écrite au §10 : « une invitation ne
  se transmet pas par navette »). Lien lui-même **non inscrit** dans le
  dépôt (secret à usage limité, jamais versionné).
- Les deux prérequis de connexion (clé SSH installée, invitation envoyée)
  sont désormais réunis. Sceau vérifié (`generer-karubi.py verifier`) :
  INTACT avant et après édition, hash inchangé.
- `updated` déjà à 2026-08-13 (session précédente du jour), aucune
  incrémentation supplémentaire nécessaire.
- Fichier prêt à être renvoyé à Mehdi (portée `khassa`, version inchangée à
  2 — le contenu scellé n'a pas bougé, seule la zone d'actualisation §10 a
  grandi).
- **Commit** : 35c8fd9

---

## [2026-08-13] archivage | Intégration du retour de Mehdi (Karūbī Habib)

- Fichier `_inbox/karubi-mehdi-navette-20260812.md` intégré au fichier
  canonique `meta/transmissions/karubi-mehdi.md`. Sceau vérifié
  (`generer-karubi.py verifier`) : INTACT avant et après écriture.
- Écart d'append corrigé : entrée §8 du 2026-08-12 (installation Tailscale +
  transmission de la clé SSH publique de Mehdi) reportée dans le fichier
  canonique — le fait était déjà acté (canal direct, entrée `activation-acces`
  du registre) mais pas la parole du Karūbī elle-même.
- `updated` du fichier canonique → 2026-08-13. Entrée `retour` journalisée
  dans `meta/transmissions/registre-silsila.md`. Sas `_inbox/` vidé.
- **Clarté ajoutée au protocole** (sur signalement de Sidy) : `meta/CLAUDE.md`
  complété d'un tableau de correspondance destinataire ↔ nom du Karūbī, la
  distinction (nom propre du personnage, pas le nom du destinataire) n'étant
  documentée nulle part hors des fichiers individuels et du registre.
- **Commit** : 6b4871e

---

## [2026-08-12] vigilance | Suppression du reliquat `Protocole.md` (racine)

- **Anomalie** : `verifier-invariants.py` signalait `[B0] Protocole.md — aucun
  frontmatter délimité par \`---\`` — seule erreur bloquante restante du dépôt.
- **Origine** : reliquat non nettoyé du commit `d42c954` (« ARCHIVAGE :
  éclatement expérimental du protocole en CLAUDE.md par circuit »,
  2026-08-12) — copie du corps de l'ancien `CLAUDE.md` monolithique déposée
  à la racine du dépôt, hors de toute arborescence de circuit, sans
  frontmatter.
- **Constat** : comparaison ligne à ligne (`diff`) avec
  `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md` — identité
  exacte du corps (912 lignes), l'archive canonique ajoutant seulement le
  frontmatter (`type: meta`, `status: deprecated`) et la note d'avertissement
  de tête déjà prévue par le CLAUDE.md racine (révision 2026-08-12).
  L'archive demandée par Sidy existait donc déjà, correctement scellée ;
  `Protocole.md` n'était qu'un doublon orphelin, sans fonction propre.
- **Traitement** : suppression (`git rm`), sur confirmation explicite de
  Sidy — aucune information perdue, le contenu intégral reste conservé dans
  l'archive canonique (Cmd 10 respecté : rien n'est perdu, tout est déjà
  ailleurs).
- `verifier-invariants.py --racine /root/wiki` : `0 erreur(s), 45
  avertissement(s)` (pré-existants, non bloquants, phase de calibrage).
- **Commit** : 27671d1

## [2026-08-12] amendement | éclatement expérimental du CLAUDE.md en protocoles locaux

- **Directive Sidy** : `CLAUDE.md` racine (912 lignes) devenu lourd à naviguer ;
  demande d'éclatement en un `CLAUDE.md` par circuit, de sorte qu'un agent
  travaillant dans un seul dossier n'ait sous les yeux que le protocole qui le
  concerne (Claude Code charge le `CLAUDE.md` racine en toute circonstance, et
  charge en plus celui d'un sous-dossier quand un agent y travaille).
- **Tension résolue** : l'ancien Cmd 14 (Corollaire d'auto-suffisance) imposait la
  lettre intégrale de toute règle dans le fichier unique, sans aucun renvoi.
  Verdict Sidy (verbatim) : *« on change la règle mais on note dans le fichier
  même que nous testons une méthode alternative le temps d'être fixé sur son
  efficacité, tout en archivant l'original impérativement »* — amendement
  explicite, qualifié de méthode à l'essai (réversible, non tranchée
  définitivement), pas une doctrine d'organisation figée.
- **Action** : contenu transversal (postes de travail, carte des circuits,
  étanchéité, protocoles d'exécution communs, supervision des agents, procédure
  d'intégration, commandements absolus) conservé à la racine, révisé avec une
  nouvelle entrée de révision et une section « II bis. Carte des protocoles
  locaux ». Contenu propre à un seul circuit (Sceau, nomenclature, actions
  d'exécution locales) migré vers `doctrinal/CLAUDE.md`, `atelier/CLAUDE.md`,
  `label/CLAUDE.md`, `hermeneutique/CLAUDE.md`, `meta/CLAUDE.md` — lettre
  complète, pas de résumé. Archive intégrale et non modifiée de la version
  pré-éclatement conservée (Cmd 10) :
  `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md`.
- **Complément (même jour)** : sur nouvelle directive Sidy, `Protocole.md`
  créé à la racine du dépôt comme copie fidèle et non modifiée du protocole
  intégral d'avant découpage (même contenu que l'archive, replacé au niveau
  racine pour consultation directe) ; `CLAUDE.md` (racine + cinq locaux) reste
  la version en vigueur, effectivement chargée par l'outil d'intégration.
- **Vérification** : `verifier-invariants.py --racine /root/wiki` exécuté —
  aucune des erreurs/avertissements relevés ne concerne un fichier touché par
  cet éclatement (toutes préexistantes, traitées ailleurs).
- **Commit** : d42c954

---

## [2026-08-10] archivage | création lignée Kouyaté et fiche Sidy-Lamine Kouyaté

- **Directive Sidy** : demande explicite de créer des fiches cibles pour
  combler des liens à référent vide relevés dans le bloc
  `doctrinal/discernement/2026-06-20_*`, dont au minimum une fiche
  « Kouyaté » et une fiche sur Sidy sous son nom complet.
- **`meta/genealogie/kouyate.md`** — hub généalogique du côté paternel
  (nom mandingue, lignée de griots, tradition orale du « frère-serpent »
  déjà documentée dans `2026-06-20_oiseau-serpent-jumeau.md`), en miroir
  de `arbre-genealogique-sissoko.md`. Absence d'ascendants nommés côté
  Kouyaté signalée comme lacune, non comblée artificiellement.
- **`meta/genealogie/sidy-lamine-kouyate.md`** — nœud de convergence des
  deux lignées (Kouyaté paternel, Sissoko maternel) sous le nom complet ;
  strictement généalogique, aucun contenu spirituel ou biographique
  au-delà de la position dans l'arbre (Cmd 4 : ce registre reste dans
  `meta/personnel/sidy.md`, une page = un sujet).
- **Lien effectif vers `doctrinal/`** porté par `kouyate.md` (sens
  autorisé, §VI) vers `mythe-personnel-unifie` et `origine-jumeau-spirituel`
  — voir l'entrée correspondante du même jour dans `doctrinal/annales.md`
  pour le détail de la correction côté fiches discernement.
- **Commit** : 211d8e9

## [2026-08-09] archivage | reclassement du compte rendu 12-agents hors circuit doctrinal

- **Constat** : au contrôle `verifier-invariants.py` déclenché par l'intégration du
  sas (voir `doctrinal/annales.md`), un fichier
  `doctrinal/discernement/compte-rendu-12-agents-2026-08-09.md` a été trouvé sur le
  disque — non tracké git, jamais passé par `_inbox/`, frontmatter incomplet.
  Écrit directement dans le circuit doctrinal par un agent Hermes en session
  terminal, hors protocole (Cmd 6 : pas d'écriture sans plan validé).
- **Nature réelle** : un compte rendu opérationnel destiné à un avis extérieur (état
  de l'infrastructure des 12 agents, chronologie de la calibration zodiacale,
  points ouverts), non une fiche de discernement — pas de statut de vérité
  traditionnelle en jeu.
- **Action** (verdict Sidy) : déplacé vers
  [[meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09]],
  Sceau `meta` conforme (`type: meta`), contenu intact, note de provenance ajoutée
  en tête. Fichier d'origine supprimé (jamais tracké git, aucune perte d'historique).
- **Commit** : d16189b

---

## [2026-08-09] archivage | intégration de l'image du thème natal depuis le sas

- **Constat** : `_inbox/image.jpeg` (carte natale Astrodienst, déposée par
  Sidy le 2026-08-08) était déjà **citée** comme source par deux fiches
  (`meta/personnel/2026-06-20_theme-astrologique.md`,
  `meta/projet-unifie/16-mise-en-regard-theme-natal-roue-agents-2026-08-08.md`)
  sans jamais avoir quitté le sas — intégration restée incomplète.
- **Action** : fichier déplacé vers son domicile naturel
  `raw/assets/theme-natal-sidy-astrodienst-2026-08-08.jpeg` (§II) ; les deux
  références corrigées vers ce chemin ; `updated:` remonté à 2026-08-09 sur
  les deux fiches.
- **Sas** : `_inbox/` ne contient plus désormais que `karubi-mehdi.md`
  (cycle Karūbī ouvert, préservé intentionnellement — voir
  `meta/transmissions/registre-silsila.md`).
- **Commit** : ef57ba4

---

## [2026-08-09] tranché | signalement `doctrinal/ → meta/personnel/` (sens interdit) résolu

- **Rappel** : entrée précédente signalait 4 fiches `meta/personnel/`
  (dont `gout-sucre-priere`) et `meta/projet-unifie/briefing-claude-ai`
  reçevant leur seul lien entrant depuis `doctrinal/annales.md`, sens
  interdit par §VI.
- **Correction factuelle** : vérification directe par grep — `gout-sucre-priere`
  n'a **aucun** lien depuis `doctrinal/annales.md` ; son unique lien entrant
  vient de `meta/genealogie/2026-06-20_oiseau-serpent-jumeau.md` (intra-`meta/`,
  conforme). L'ensemble réel est de **3 fiches** :
  `meta/personnel/2026-06-20_bourdonnement-tempe`,
  `meta/personnel/2026-06-20_taekwondo-hansu`,
  `meta/projet-unifie/briefing-claude-ai`.
- **Verdict** : les 3 liens vivent dans des entrées d'annales déjà publiées,
  datées (2026-06-20), append-only — non repris (Cmd 9/Cmd 10). Le hub
  `meta-index.md` leur donne désormais un lien entrant alternatif,
  intra-`meta/`, conforme. `doctrinal/index.md` (§IX), fichier non
  append-only, corrigé directement : lien `meta/sidy` retiré, remplacé par
  renvoi générique vers `meta-index.md`.
- **Détail complet** : voir `atelier/rd/cahiers/registre-problemes.md`,
  entrée `[2026-08-09] resolu | Tranché — signalement doctrinal/ →
  meta/personnel/`.
- **Commit** : fc0e1c6

---

## [2026-08-09] ouverture | création du hub `meta-index.md` / `meta-annales.md`

- **Constat** : le comptage mécanique des liens entrants (`carte-du-depot.py`,
  bug de résolution corrigé le même jour) faisait apparaître 80 fiches sans
  aucun lien entrant, dont 66 vivant dans `meta/` — faute de hub interne au
  domaine, contrairement aux quatre circuits qui disposent chacun d'un
  `index.md`/`annales.md`.
- **Verdict Sidy** : autorisation de traiter toutes les fiches orphelines, y
  compris personnelles ; nommage du hub propre à `meta/` avec préfixe `meta-`
  (`meta-index.md`, `meta-annales.md`) pour écarter tout risque de lecture
  comme sixième circuit.
- **Action** : création de `meta/meta-index.md`, recensant par sous-dossier
  (`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
  `projet-unifie/` y compris `hermes-prompts/`/`hermes-skills/`, fiches de
  premier niveau) les fiches du domaine — chacune reçoit ainsi un lien
  entrant légitime, intra-`meta/` exclusivement. Résout l'orphelinage des 66
  fiches `meta/`.
- **Scripts adaptés** : `verifier-invariants.py` (`NOMS_ANNALES`,
  `FICHIERS_EXEMPTS_C3`, détection `fichier_de_service` étendus aux nouveaux
  noms) et `carte-du-depot.py` (filtre d'orphelines étendu). `CLAUDE.md` §II,
  §VI et §X (Cmd 9) mis à jour en conséquence.
- **Hors périmètre, signalé séparément** (Cmd 7, non traité ici) : 4 fiches
  `meta/personnel/` et 1 fiche `meta/projet-unifie/` reçoivent leur seul lien
  entrant depuis `doctrinal/annales.md`, en sens interdit (§VI, sensible →
  neutre uniquement). Verdict humain toujours attendu — voir
  `atelier/rd/cahiers/registre-problemes.md`.
- **14 fiches restant orphelines hors `meta/`** (13 stubs `deprecated` de
  `atelier/projets/` + `doctrinal/discernement/_template.md`) : acceptées par
  conception, non traitées par lien artificiel — voir registre.
- **Commit** : fc0e1c6
