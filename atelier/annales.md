---
title: Annales de l'Atelier (Projets et Matériels)
type: meta
updated: 2026-08-16
---

# Annales de l'Atelier

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

<!-- INSERTION: EN-TÊTE -->

## [2026-08-16] correction | Canal Telegram Mehdi — architecture initiale en service

- **Écart initial** : session Hermes terminal a d'abord configuré Telegram sur
  le profil `karubi` (sous root, sans isolation OS). Verdict Sidy : reprendre
  l'architecture R&D initiale (profil dédié, isolation OS).
- **Correction** :
  - Module `hermes-agent[telegram]` installé dans le venv système
  - Token et allowlist retirés de `/root/.hermes/profiles/karubi/.env`
  - Service `hermes-gateway-karubi.service` arrêté et désactivé
  - Service `hermes-gateway-habib-mehdi.service` relancé — tourne sous
    l'utilisateur `mehdi` (uid 1000), isolation OS vérifiée
- **État final** : opérationnel, bot `@HabibKarubi_bot` connecté, Mehdi
  allowlisté (817763036), cwd `/home/mehdi/depot-lecture` (bind mount ro),
  message test envoyé via `sudo -u mehdi hermes --profile habib-mehdi send`
- **Fiche R&D** : `atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16.md`
  mise à jour (§5 : architecture corrigée et en service)
- **Configuration H‍ermes** (`.env`, `config.yaml`, services systemd) : hors dépôt,
  jamais commitée — le présent commit ne porte que la documentation wiki
  (fiches + annales + registre), vérifiée exempte de tout secret avant staging.
- **Commit** : 954712f

---

## [2026-08-16] archivage | Cordis — paradigme de composabilité spatiotemporelle

- Ingest de `raw/A Programming Paradigm for Spatiotemporal Composability.pdf`
  (Shi, Zhang, Cui — Peking University / DeepSeek-AI, accompagne la sortie du
  DeepSeek Harness).
- Fiche créée : `atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle.md`
  (`outillage`, `exploratoire`, `brouillon`).
- Qualification sashimono (§VII, double contrôle) : homologie de forme
  constatée avec plusieurs articles de la convention (art. 1, 3, 4, 5, 6),
  portance zōsaku, non tranchée.
- Hypothèse plus large de Sidy (filiation orientale/chinoise explicite,
  au-delà de la simple homologie) renvoyée en discernement doctrinal, lien
  signalé sens unique : `doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md`
  (enrichi ce jour, statut `speculatif`, verdict réservé).
- Pistes H‍ermes (§8 de la fiche) posées comme jalon, aucune décision
  d'implémentation.
- Passage par `_inbox/cordis-composabilite-spatiotemporelle/` avant intégration
  (validation Sidy des deux tours de plan, 2026-08-16).
- SHA : `ade0da6`

## [2026-08-15] archivage | Bilan R&D — pont inter-agents

Fiche `atelier/rd/cahiers/bilan-2026-08-15-pont-agents.md` créée : synthèse de la
période 2026-08-08 → 2026-08-15 destinée à tout agent (H‍ermes terminal, Claude
Code, ou autre) reprenant le fil des travaux R&D sans avoir participé aux sessions
antérieures. Couvre : ouverture et structure du pôle R&D, outillage déterministe
du dépôt, outillage Karūbī (append-only + admin Agent 10, verdict Sidy 2026-08-15),
spec rôle G0 de brouillon §4, Bureau TUI, infrastructure Hetzner, phase 3 veille,
extension zodiacale, SRS H‍ermes-native ; chantiers ouverts par priorité (dont le
blocage A — isolation mémoire H‍ermes par sub-agent : décision propre de Sidy,
assumée le même jour, pas une incohérence à corriger) ; leçons transversales
opérationnelles. Aucun contenu doctrinal. Lien entrant ajouté dans
`atelier/rd/index.md`. Committé dans le même lot que l'outillage de navette
Karūbī (`integrer-navette-karubi.py`, `spec-skill-karubi-actualisation-g0.md`,
note `meta/CLAUDE.md`, entrée `registre-silsila.md`) — verdict Sidy obtenu pour
l'ensemble.
- **Commit** : 2657421

## [2026-08-15] archivage | Intégration registre problèmes + fiche outillage R&D

Deux fichiers du sas `_inbox/` intégrés :

1. **Entrée registre-problemes** (`atelier/rd/cahiers/registre-problemes.md`) :
   ajout de l'entrée `[2026-07-20] Lecture défensive d'un document-persona par un LLM neuf`,
   relatant le cas Karūbī et le signal du classificateur de sécurité sur collage à froid.
   Chaîne d'observation complète → `atelier/rd/outillage/robustesse-documents-persona-llm`.

2. **Nouvelle fiche outillage** (`atelier/rd/outillage/robustesse-documents-persona-llm.md`,
   type `outillage`, statut `exploratoire`) : instrumentation complète du problème
   (forme / contenu, catégorisation du signal, résolution appliquée, pistes à vérifier).
   Étanchéité neutre, liens vers `meta/transmissions/registre-silsila.md` (faits personnels,
   hors circuit).

- **Commit** : c67275b

## [2026-08-15] outillage | Piste — SRS pour l'assimilation du protocole (CLAUDE.md)

Fiche d'instruction ouverte (`atelier/rd/outillage/2026-08-15_piste-srs-assimilation-protocole.md`)
en réponse à un double constat : (1) optimisation infrastructure Hermes —
lacunes observées entre sessions sur des règles protocolales denses (Cmd 9,
Cmd 12, nommage Karūbī — cf. registre 2026-08-13 §2 et §3) ; (2)
assimilation côté utilisateur CLI — le protocole (~10 000 mots) demande une
révision espacée pour passer de la conscience à l'automatisme.

La fiche instruit à frais égaux Mnemosyne (SRS local Maastricht, SM-2+,
équipe de recherche cognitive) et Anki (sync mobile native, écosystème
large), puis propose une troisième voie : intégration Hermes-native. Le
verdict Sidy (2026-08-15) tranche en faveur de cette dernière option :
sous-système de cartes auto-générées depuis CLAUDE.md, vivant dans la
mémoire Hermes (`MEMORY.md` ou extension), sans SRS tiers. §VIII (non
inclus) : format de carte, script d'extraction, mécanisme de révision
(cron Hermes, commande `hermes drill`, ou injection systématique dans le
prompt d'ouverture), algorithme d'espacement — font l'objet d'une fiche
ultérieure).

**Commit** : 5a83157

## [2026-08-15] infrastructure | Bureau TUI — première version

Tableau de bord terminal unique (`atelier/rd/infrastructure/bureau/`, Python +
Textual, esthétique "menu de jeu vidéo" — inspiration de forme relevée dans
`hermeneutique/metal-gear/mother-base` et `idroid`, aucune correspondance
doctrinale invoquée). Six modules indépendants (`modules/base.Module`) : état
de l'Instrument (lecture déterministe d'`instrument-donnees.yaml`), état des
12 agents Hermès (process `pgrep`, missions lues depuis
`meta/projet-unifie/hermes-prompts/`), lecteur textes/pdf/images (façon
Internet Archive, restreint aux quatre circuits publics), lecteur vidéo
(rendu ANSI demi-bloc via ffmpeg, déclenché à la demande uniquement — RAM
serveur limitée), streaming audio (serveur HTTP local, écoute côté client via
tunnel SSH/Tailscale), chat local (v1 humains uniquement, passerelle
Hermès/Discord explicitement différée). 10 tests unitaires verts, `ruff`
propre, fumée headless Textual (pilote) OK sur les 6 modules,
`verifier-invariants.py` : 0 erreur. Testé et validé par Sidy en terminal SSH
réel avant commit.

**Commit** : 5c688b4

## [2026-08-15] mise-a-jour | Brouillons zodiacaux alignés sur la table révisée des 12 fonctions

Suite à la réallocation complète des 12 correspondances signe↔fonction validée
par Sidy le même jour (`doctrinal/discernement/2026-07-05_...`, volet b rouvert),
les brouillons de `atelier/rd/cahiers/brouillons-extension-zodiacale/` sont mis
en cohérence avec la nouvelle table : positions 2 (Taureau→Balance), 6
(Vierge→Scorpion), 7 (Balance→Lion), 9 (Sagittaire→Vierge) renommées via `git mv`
(historique préservé) et réécrites ; positions 5 (Taureau), 8 (Sagittaire), 12
(Poissons) — absentes jusqu'ici — nouvellement rédigées. Positions 1, 3, 4, 10, 11
(signes inchangés) laissées en l'état. Chaque brouillon conserve son
`statut_experience: exploratoire` et sa clause d'étanchéité. Détail complet :
`meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md`
§9.

- **Commit** : 5a3aee3

## [2026-08-13] signalement | Fiches biographiques (2026-06-20) confrontées à AI et IRS

Demande de Sidy : mettre les fiches biographiques en relation avec le corpus, et
en particulier avec *Aperçus sur l'initiation* et *Initiation et Réalisation
spirituelle* (déposée ce jour).

- Créé `atelier/rd/outillage/2026-08-13_fiches-biographiques-confrontation-ai-irs.md`
  (`type: outillage`) — traitement fiche par fiche des douze `discernement/2026-06-20_*`.
- Règle d'appariement posée : un chapitre répond à la **question déclarée ouverte**
  par la fiche, jamais à son récit. Dix chapitres lus intégralement avant citation :
  AI V (`30`), AI VII (`32`), AI VIII (`33`), IRS V (`555`), IRS VI (`556`),
  IRS XVI (`566`), IRS XXI (`571`), IRS XXII (`572`), IRS XXIV (`574`),
  IRS XXVII (`577`).
- Question centrale de neuf fiches (« qui est habilité à reconnaître un *Fard* ? »)
  sourcée : AI V (rattachement « idéal » vain ; « juge et partie dans sa propre
  cause »), AI VIII (la chaîne), IRS V (virtuel/effectif), avec le contrepoint
  IRS XXIV (formes normales sans *Guru* individuel).
- `mythe-personnel-unifie` : AI VII, qui admet le cas *ativarna* tout en posant
  son critère — appariement bilatéral, non restrictif.
- `matrices-artificielles-barzakh` : IRS VI, où Guénon récuse le terme
  « égrégore » lui-même comme non traditionnel.
- `synthese-danger-dissolution-identitaire` : IRS XXVII, qui distingue trois cas
  (quiétistes / « fous en Christ » / *majdhûb*) — troisième catégorie doctrinale
  neuve pour le dépôt, sans critère de reconnaissance externe et sans application
  à un cas particulier.
- `origine-jumeau-spirituel` : IRS XXII, lu et instruit en complément le même jour
  (§ 5.3) — catégorie doctrinale de l'antériorité hors du temps humain
  (« réminiscence platonicienne »), assortie de l'avertissement de Guénon sur les
  « lueurs » pré-initiatiques, « d'ordre probablement plus psychique que
  spirituel ». Appariement bilatéral.
- Quatre fiches restent sans source guénonienne, signalées comme telles.
- Aucun `status`/`Statut` modifié. Création des fiches `doctrinal/sources/` et
  ajout des wikilinks : **proposés, non exécutés** — en attente d'accord.
- Signalement `raw/` : IRS ch. XXX (id 580) toujours absent — le fichier déposé
  est la page de sommaire de l'œuvre, non le chapitre.
- **Suite donnée le même jour** (accord de Sidy, « oui, crée les fiches ») : le § 7
  passe de *proposé* à **exécuté** — sept fiches `doctrinal/sources/` créées et
  huit rattachements posés dans le champ `sources:` des fiches biographiques.
  Opération consignée côté doctrinal (`doctrinal/annales.md`, entrée du même jour).
- Le présent document amendé en conséquence : § 5.2 corrigé (IRS XXVII ne distingue
  pas trois cas mais une **série** — au moins six positions sous une même apparence,
  dont les faux *majâdhîb* de deux sortes contraires et les jongleurs-initiés) ;
  § 7 marqué exécuté.
- **Double contrôle (§ VII) consigné après coup** au § 7 bis, avec mention de son
  retard : joint qualifié ***zōsaku* × *kari-kumi*** (une extrémité contingente,
  montage à blanc) ; Gizeh : **confronté, aucun ancrage**.
- **IRS ch. XXX (id 580) déposé par Sidy le même jour** — signalement de complétude
  levé, corpus IRS complet (34 fichiers, aucun identifiant manquant sur 551–583).
  Chapitre lu et instruit au § 6 bis ; huitième fiche source créée et rattachée à
  `matrices-artificielles-barzakh` et `visions-centre-nocturne` (consigné côté
  doctrinal). Double contrôle posé cette fois **au moment de la production**
  (§ 7 ter) : *zōsaku* × *kari-kumi*, nature **homologie** ; Gizeh due et instruite
  (matière axiale) — **aucun ancrage**, conflation polaire/solaire écartée.
- Commit: `0c3a7ba` ; complément IRS XXII : `96ab694` ; exécution du § 7 et
  correction du § 5.2 : `4795d2d` ; IRS ch. XXX : `e3a9ce6`.


## [2026-08-13] signalement | Tour d'horizon : déblocages ouverts par le corpus Guénon déposé

Dépôt de *La Grande Triade* dans `raw/` par Sidy. Confrontation de fond (et non
plus de forme) entre le corpus désormais intégral et les marqueurs d'inachèvement
des fiches `doctrinal/discernement/`.

- Créé `atelier/rd/outillage/2026-08-13_tour-horizon-corpus-guenon-deblocages.md`
  (`type: outillage`) — distinct du rapport de fidélité de citation du même jour.
- Quatre déblocages signalés : GT ch. XVII (`Chapitre=714`) sur la restriction de
  degré de `adam-qadmon-insan-kamil-wang-vaishvanara` ; GT ch. XXVI n. 11
  (`Chapitre=722`) sur le chantier de la Balance de `septenaire-transversal` ;
  GT ch. XV (`Chapitre=712`) candidat au sourçage d'un `to-source` sashimono ;
  lisibilité partielle de `sept-tours-sitra-ahra` (blocage kabbalistique intact).
- Candidat Cmd 3 signalé : équivalence *Es-Sakînah* / *Shekinah* posée par Guénon
  lui-même (GT ch. XXVI), portée par aucune fiche `discernement/`.
- Carte des identifiants `Chapitre=NNN` établie pour AI, IRS, GT, RM, SC, RQST.
- Signalement de complétude : *Initiation et Réalisation Spirituelle* id 580
  (ch. XXX) manquant dans `raw/`.
- Précision sur l'Instrument : yaml = 36 nœuds `tasawwuf` + 7 `universel`
  uniquement ; GT est matériau de fondation pour `universel/`, non ouverture
  d'un espace extrême-oriental.
- Cmd 12 respecté : aucun `status`/`Statut` de fiche `discernement/` modifié.
- Volet B (hygiène `raw/`) relevé, non instruit — Cmd 10.
- Commit: `37bf44d`.


---

## [2026-08-13] signalement | Confrontation de 5 fiches discernement/ au corpus Guénon (raw/)

- **Contexte** : contrainte production/intégration temporairement levée
  ([[wiki-contrainte-integration-levee]], mémoire) ; corpus Guénon complété en
  `raw/` (dépôt du chapitre RQST manquant, id 746, par Sidy).
- **Opération** : vérification mécanique de complétude des 7 œuvres Guénon
  déposées (0 trou après dépôt) via les champs `Chapitre=`/`sigle=` du
  frontmatter `source:`, puis confrontation verbatim de 5 fiches
  `doctrinal/discernement/` (celles citant, via wikilink, une des 12 fiches
  `doctrinal/sources/` confrontables) contre le texte brut correspondant.
- **Résultat** : 4 fiches confirmées exactes (citations et attributions de
  chapitre fidèles). 1 fiche —
  [[doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil]]
  — porte deux formulations entre guillemets attribuées à Guénon qui sont en
  réalité des paraphrases/synthèses, non du texte verbatim. Signalement remis
  à Sidy, aucun `Statut` modifié (Cmd 12).
- **Livrable** :
  [[atelier/rd/outillage/2026-08-13_confrontation-discernement-corpus-guenon]].
- **Non traité** : Volet B (doublons d'id AI 28/70, RQST 729/752, EME 881 ;
  fichiers possiblement mal classés ; `organize_guenon.sh`) — reporté, non
  commencé.
- Commit : `023a31c`.

---

## [2026-08-13] vigilance | Rapport R&D — défauts observés, intégration retour Karūbī Mehdi (Habib)

- Sur demande explicite de Sidy, consignation dans
  `atelier/rd/cahiers/registre-problemes.md` de trois observations tirées de
  l'intégration du retour `_inbox/karubi-mehdi-navette-20260812.md` : (1)
  écart d'append silencieux — une entrée §8 de la navette absente du fichier
  canonique, sceau intact n'ayant rien signalé (piste d'outillage : mode
  `diff` pour `generer-karubi.py`, ouvert) ; (2) confusion nom du Karūbī /
  nom du destinataire, déjà résolue par l'ajout d'une table à `meta/CLAUDE.md`
  (commit `6b4871e`) ; (3) friction récurrente du Cmd 9 (SHA après commit
  imposant un second commit de forme), confirmée comme comportement normal du
  protocole tel qu'écrit, non un défaut isolé (reporté).
- **Commit** : 76d08b0

---

## [2026-08-13] vigilance | Retour d'expérience R&D — première intégration sous CLAUDE.md éclaté

- Sur demande explicite de Sidy (« toute information instructive au R&D pour
  monitoring »), consignation dans `atelier/rd/cahiers/registre-problemes.md`
  des observations tirées de la première intégration `_inbox/` réalisée sous
  la convention CLAUDE.md éclatée (racine + cinq `CLAUDE.md` locaux,
  2026-08-12) : chargement confirmé fonctionnel des protocoles locaux,
  traitement du reliquat `Protocole.md` (doublon non nettoyé du commit
  d42c954, supprimé le 2026-08-12/13 — voir `meta/meta-annales.md`
  [2026-08-12]), confirmation de l'intégrité de l'archive canonique, et
  validation du principe d'auto-signalement du sas via la fiche
  `hermeneutique/metal-gear/idroid.md`.
- Aucune écriture de contenu hors du cahier R&D ; simple journalisation
  transversale de cette entrée pour Cmd 9 (opération conduite depuis
  l'atelier, sur un objet propre au pôle `rd/`).
- `verifier-invariants.py --racine /root/wiki` : `0 erreur(s), 45
  avertissement(s)` (inchangé, pré-existants, phase de calibrage).
- **Commit** : bddece0

## [2026-08-12] archivage | Audit de santé Claude Code (`/doctor`) versé dans rd/infrastructure

- **Fiche créée** : `atelier/rd/infrastructure/claude-code-health-check-2026-08-11.md`
  — `type: infrastructure`, `statut_experience: exploratoire`. Rapport brut
  (anglais d'origine) produit par Sidy le 2026-08-11 via `/doctor`,
  conservé tel quel — diagnostic mécanique de l'installation, non un
  jugement sur le contenu doctrinal.
- **Non exécuté** : les recommandations du rapport (notamment « trimmer
  `CLAUDE.md` », devenue sans objet après l'éclatement en protocoles
  locaux du 2026-08-12) restent hors périmètre, aucun plan validé ne les
  couvre (Cmd 6).
- **Commit** : 036635b

## [2026-08-12] archivage | Proposition phase 3 (agent de veille infrastructure) archivée dans rd/cahiers

- **Fiche créée** : `atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  — `type: meta` (précédent : `registre-problemes.md`, même dossier), statut
  `brouillon` conservé tel quel (contenu non ré-écrit, seule une section
  « Intégration (2026-08-12) » ajoutée en queue de fiche).
- **Provenance** : déposée en `_inbox/` le 2026-08-11 ; le document
  s'auto-déclarait sans écriture hors `_inbox/` (« cette note ne code encore
  aucun automatisme »). Archivage décidé le 2026-08-12 sur consigne explicite
  de Sidy (« intègre le reste »), question de placement posée et tranchée :
  destination `atelier/rd/index.md` telle qu'indiquée par le `cible:` du
  document lui-même.
- **Portée de l'archivage** : documente des décisions de principe déjà
  tranchées par Sidy le 2026-08-11 (agent désigné : Studio Sound Engineer,
  poste 9 ; canal `#infrastructure` ; cron quotidien midi ; rapport en 5
  sections). **N'exécute aucun automatisme** — le tableau récapitulatif de la
  fiche (extension du prompt d'agent, accès FS/exécution, mécanisme
  technique, récurrence de l'empreinte serveur) reste explicitement « à
  instruire »/« à trancher », conformément au Cmd 6.
- **Mise à jour de renvoi** : `atelier/rd/index.md`, §« État de la phase 1
  partielle » → « Non inclus », pointeur ajouté vers la fiche archivée.
- `python3 verifier-invariants.py --racine /root/wiki` : 1 erreur bloquante
  pré-existante (`Protocole.md`, sans rapport avec cette intégration), 44
  avertissements pré-existants — aucun nouveau signal introduit.
- **Commit** : 3e846e9

## [2026-08-11] infrastructure | Cartographie architecture infrastructure serveur/Hermes/omniroute

- **Opération** : création de document cartographique global unifiant mesures brutes, topologie 
  réseau, description des services (12 profils Hermes + omniroute), empreinte mémoire consolidée, 
  et identification des points de défaillance critiques pour diagnostic et audit. Document 
  d'architecture destiné à l'onboarding et à la base de comparaison historique.
- **Fichiers créés** :
  - `atelier/rd/infrastructure/infrastructure-architecture-globale-2026-08-11.md` : cartographie 
    complète (topologie, services, mémoire, uptime, circuits réseau, SPoF, points ouverts)
- **Fichiers modifiés** :
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la cartographie 
    comme résolution du point ouvert « infrastructure documentation globale »
- **Mesures et observations** :
  - Topologie : GitHub (SSH origin) ↔ Hetzner (2 vCPU, 3.7 GB RAM, 38 GB disk 51% libre) 
    ↔ iPad (Obsidian via Working Copy)
  - Services : 12 profils Hermes (639.5 MB total), omniroute 1040 MB (28% RAM, critique), 
    hermes-webui 9.8 MB
  - Uptime : 78j 18h ; load avg < 0.1
  - Swap utilisé : 1 GB / 2 GB (signal d'alerte mémoire au moment de la mesure)
  - SPoF identifiés : clé API Anthropic (11 agents paralysés), omniroute (fonction inconnue), 
    Hetzner SSH key (écriture dépôt), uptime Hetzner (tous les services)
- **Points ouverts à instruire** :
  1. omniroute : fonction exacte, dépendances, optimisation RAM ?
  2. Clé API Anthropic : impasse à Sidy (budget), en attente résolution
  3. Qwen sur gardien : clause « No API automation » — risque révocation à respecter
  4. Hermes accès meta/ : cloisonnement technique statu quo (retour d'expérience en cours)
  5. Historique de charge : aucune série temporelle (monitoring à installer)
- **Vérification** :
  - `verifier-invariants.py --racine /root/wiki` : 5 erreurs, 45 avertissements (baseline 
    stable +2 pour nouvelle fiche avec liens meta)
  - Aucune anomalie de structure ou de liens dans la cartographie créée
- **État** : cartographie complète, observation brute sans recommandations d'optimisation 
  (distinction §VIII.2 maintenue) ; base solide pour diagnostics et onboarding futurs
- **Commit** : (à venir)

---

## [2026-08-11] outillage | Implémentation des 4 pistes outillage instruites (pistes A, B, C, D) — documentation fiches et verification

- **Opération** : finalisation de la documentation et vérification des quatre pistes 
  d'outillage du pôle R&D (session 2026-08-11). Pistes A (C4 verifier-invariants) et C 
  (detecter-non-tracke.py) déjà implémentées en code et en spec, pistes B et D manquaient 
  de fiches dédiées.
- **Fichiers créés** :
  - `atelier/rd/outillage/spec-generer-cartographie-tolerant.md` : documentation de la 
    sévérité à deux niveaux du script v1.1 (BLOQUANT gouvernance, AVERTISSEMENT chantier) 
    — distinct d'un « mode tolérant », c'est une hiérarchisation des anomalies
  - `atelier/rd/infrastructure/infrastructure-ssh-statu-quo.md` : documentation du verdict 
    (statu quo SSH, pas de migration HTTPS+PAT), rationale (gestion de secret + coût 
    détour Working Copy) et clause de réouverture
- **Fichiers modifiés** :
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la complétude 
    de l'implémentation des quatre pistes (A, B, C, D tous en statut resolu) et les 
    résultats de vérification (baseline stable)
- **Vérification** : 
  - `verifier-invariants.py --racine /root/wiki` : 5 erreur(s), 43 avertissement(s) — 
    baseline stable (+2 warnings attendus pour les 2 nouvelles fiches avec liens meta)
  - `generer-cartographie.py --depot /root/wiki --verifier` : 2 anomalies BLOQUANT 
    (frontmatter absent) — inchangées
  - `detecter-non-tracke.py --racine /root/wiki` : identifie 2 fichiers non-trackés 
    (les 2 nouvelles fiches), aucune anomalie
- **État** : pistes B et D documentées. Piste A (C4 verifier-invariants) reste sans fiche 
  dédiée à ce stade (implémentation active en code, arbitrage verbal de Sidy en session 
  jugé suffisant pour cette passe). Piste C (spec existante et script testé) complète.
- **Commit** : 3650ed8

---

## [2026-08-11] agents-h‍ermes | Extension du prompt agent 09 (Studio Sound Engineer, pos. 9 Sagittaire) — zodiacal + governance

- **Opération** : intégration au prompt en production des sections zodiacales 
  (principle + harmonisation thème natal) et de la clause de gouvernance Discord-validation 
  requise par le chantier phase 3. Trois sections insérées entre « ## Archetype served » 
  et « ## Scope » : (1) Zodiac principle (Sagittaire feu mutable jupitérien pédagogique), 
  (2) Your sign in Sidy's natal chart (contexte natal : Ascendant 2°51 Saturn conjonction 
  4°32, pédagogie disciplinée de Saturn), (3) Governance: Discord-Validation (stricte par 
  défaut, auto-accept ad hoc, traçabilité Discord, jamais d'actes silencieux).
- **Fichiers modifiés** : 
  - `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md` : trois sections 
    insérées (Zodiac principle copié du brouillon `/root/brouillons-prompts-zodiaque/09-studio-sagittarius.md` 
    tel quel, Your sign du brouillon tel quel, Governance rédigé pour l'occasion)
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant le symptôme 
    (brouillon en attente), le diagnostic (dépendance phase 3), la résolution (trois 
    sections intégrées), la compréhension (extension ≠ réforme structurelle)
- **Validation** : `verifier-invariants.py --racine /root/wiki` : baseline inchangée
  (5 erreur(s) pré-existantes, 40 avertissement(s))
- **État** : prompt agent 09 étendu, reste en régime exploratoire (statut_experience non 
  formalisé en frontmatter, déjà documenté par le registre) ; accès FS/gouvernance résolus 
  séparément ; déploiement effectif de la veille infrastructure reste un acte distinct (Cmd 6).
- **Commit** : 29cb5cc

---

## [2026-08-11] phase-3 | Explicitation du flux alchimique Discernement → R&D (théorie des trois territoires adoptée)

- **Opération** : enrichissement conceptuel de la proposition phase 3 pour nommer 
  explicitement sa position dans le flux adopté le même jour (trois territoires de 
  l'inachevé). La note documente une transition de la spéculation zodiacale 
  (Discernement) vers la mise en œuvre concrète (R&D exploratoire) ; cette transition 
  était implicite et doit être nommée par référence à la théorie.
- **Fichiers modifiés** : 
  - `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` : blockquote 
    architecturale ajoutée après l'en-tête (explicitant la transition Discernement → R&D 
    et la finalité non-achevée jusqu'à verdict de Sidy) ; §III.1 enrichi d'une 
    sous-section « Registre alchimique » décrivant l'incarnation du passage du Plan 
    théurgique à l'Acte
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la 
    transition alchimique, sa non-transparence antérieure, et son ancrage à la théorie 
    adoptée
- **Validation** : `verifier-invariants.py --racine /root/wiki` : baseline inchangée
  (5 erreur(s) pré-existantes, 40 avertissement(s))
- **État** : note phase 3 reste `brouillon`, enrichie de la dimension architecturale. 
  Aucun changement aux chantiers énumérés (accès FS, mécanisme technique, extension 
  du prompt) — leurs exécutions restent des actes séparés. Transition conceptuelle 
  maintenant explicite.
- **Commit** : 29cb5cc

---

## [2026-08-11] phase-3 | Réouverture §III.1 : réattribution veille infrastructure au Studio Sound Engineer (position 9)

- **Opération** : documentation de la réouverture du §III.1 de la proposition phase 3. 
  L'ancien verdict (poste INTÉGRATION) tranché en séance a été rouvert le même jour 
  (2026-08-11) ; réattribution à l'agent Studio Sound Engineer (position 9 Sagittaire).
- **Fichiers modifiés** : 
  - `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` : bloc de tête 
    mis à jour, §III.1 documentant l'ancien et nouveau verdict (discipline sashimono), 
    §IV confirmant que la réouverture ne rouvre PAS le §III.3, §VI récapitulatif des 
    chantiers ouverts après la réouverture
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la réouverture, 
    le diagnostic (cartographie des 12 rôles), la résolution (accès FS accordé), la 
    compréhension tirée (traçabilité des décisions qui se chevauchent)
- **Validation** : `verifier-invariants.py --racine /root/wiki` : baseline inchangée
  (5 erreur(s) pré-existantes, 40 avertissement(s))
- **État** : `_inbox/` reste à traiter selon flux normal (INTÉGRATION, Cmd 8). 
  Registre-problemes consigné et tracé. Phase 3 ouverte en principe, chantiers 
  spécifiques (accès FS, mécanisme technique, récurrence empreinte) restent à 
  instruire avant écriture effective (Cmd 6).

---

## [2026-08-11] structure | Hypothèse méthodologique : Sandbox comme dépendance structurelle du R&D

- **Contexte** : réflexion sur la relation entre Discernement (spéculation personnelle),
  R&D (exploration exploratoire), et le Sandbox (espace de travail). Fiche de
  discernement rédigée (voir annales doctrinal du même jour).
- **Proposition** : expliciter que le Sandbox (`atelier/rd/cahiers/`) est la **poche
  de travail du R&D**, c'est-à-dire l'espace de non-finalité programmée — tout
  chantier en phase `exploratoire` y vit par défaut, demeure réversible jusqu'à
  validation explicite (Cmd 6, Cmd 13), et sort du Sandbox soit vers doctrine
  adoptée, soit vers archivage.
- **Impact sur rd/** : aucun changement immédiat au structure ni aux scripts. Change
  seulement la **clarté architecturale** et le régime de navigation entre chantiers.
- **Statut** : en attente de verdict (Cmd 12) sur l'opportunité de formaliser cette
  explicitation en CLAUDE.md.
- **Aucune écriture au registre rd/** : reste une hypothèse documentée ailleurs
  (discernement), non encore actionnable.

---

## [2026-08-11] archivage | Chantier 12 agents (zodiacal) — brouillons d'extension principielle versionnés en atelier/rd/

- **Opération** : déplacement de `/root/brouillons-prompts-zodiaque/` vers
  `atelier/rd/cahiers/brouillons-extension-zodiacale/` — 9 brouillons (pos.
  1, 2, 3, 4, 6, 7, 9, 10, 11) + README, avec frontmatter + clause
  d'étanchéité explicite (CLAUDE.md §VI). Positions 5, 8, 12 marquées en
  attente. Reste hors écriture : application en production, reste
  exploratoire (statut_experience). Détail au registre rd/:
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** : 9 fichiers créés/modifiés en
  `atelier/rd/cahiers/brouillons-extension-zodiacale/` (all with frontmatter +
  clause), README inclus.
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : c156226

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — accès FS accordé, gouvernance Discord-validation tranché, mécanisme de post tranché

- **Opération** : suite de la réouverture du §III.1 : Sidy accorde l'accès FS
  du Studio Sound Engineer aux scripts déterministes, définit la gouvernance
  (strict par défaut + auto-accept ad hoc), et fixe le mécanisme de post
  (l'agent compose et poste le rapport lui-même via Discord, plus de webhook
  tiers). Format des 5 sections conservé. Note mise à jour, blockquote de
  tête et §III.1 complétés, §VI mécanisme réécrit (pas de webhook, pas de
  crontab — c'est l'agent). Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md`
  (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : f94d0e1

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — §III.1 rouvert, veille réattribuée au Studio Sound Engineer

- **Opération** : Sidy rouvre le §III.1 (déjà tranché : routine poste
  INTÉGRATION) en le reliant explicitement au chantier de l'extension de
  rôle des 12 agents H‍ermes sur calibrage zodiacal (fiches
  `meta/projet-unifie/16-...`, `17-...`) et attribue la veille
  infrastructure à la **position 9 (Sagittaire), Studio Sound Engineer** —
  seul rôle des 12 de registre technique/matériel, après cartographie
  complète des 12 positions confirmant l'absence d'autre candidat naturel.
  Ancien verdict conservé barré (sashimono, réversibilité), cascade
  documentée sur le mécanisme du §VI (rouvert à son tour), §III.3 et §IV
  inchangés. Chantier FS/accès H‍ermes nommé, non résolu, hors périmètre.
  Détail au registre : [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (blockquote de tête, §III.1, §IV, §VI, toujours `brouillon`),
  `atelier/rd/cahiers/registre-problemes.md` (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : bd64d60

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — format et mécanisme proposés par délégation

- **Opération** : Sidy délègue explicitement le format précis du rapport et
  le mécanisme technique de post (« je me fie à ta suggestion le temps d'en
  faire l'expérience directe et j'optimiserai au besoin »). Proposition
  consignée au §VI de la note : format en 5 sections, mécanisme = webhook
  Discord simple (canal `#infrastructure`) + script Python dédié
  (`atelier/rd/outillage/`, à écrire), régime `statut_experience:
  exploratoire` (§V.a) invoqué explicitement. Écriture effective toujours
  hors périmètre (Cmd 6). Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (blockquote de tête + §VI, toujours `brouillon`),
  `atelier/rd/cahiers/registre-problemes.md` (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : c92401e

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — heure et nature du rapport tranchées

- **Opération** : Sidy fixe l'heure du cron (12:00, midi) et la nature du
  rapport (suggestion, révision, développement — au-delà du simple constat
  brut). Tension identifiée et refermée dans le même énoncé : le caractère
  suggestif du rapport ne crée aucune dérogation à la porte humaine (§III.3,
  Cmd 13) — toute suggestion est validée par Sidy avant journalisation.
  Détail au registre : [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` (§VI,
  toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée).
- **Commit** : beee81f

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — fréquence quotidienne tranchée

- **Opération** : Sidy confirme la fréquence du cron proposée au §VI —
  **quotidienne**, cohérente avec le « Rapport du matin » déjà envisagé côté
  H‍ermes/gardien. Note mise à jour. Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` (§VI,
  toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée).
- **Commit** : c5acb2c

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — canal Discord `#infrastructure` créé

- **Opération** : Sidy communique en session le nom et l'identifiant du canal
  Discord dédié tranché au §V (`#infrastructure`). Note mise à jour (§VI) :
  nom consigné, identifiant numérique volontairement **non** consigné dans le
  dépôt (même régime que les secrets de configuration — cf.
  `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`). Détail
  au registre : [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` (§VI,
  toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée). Vérifié qu'aucun identifiant
  numérique Discord n'a été écrit dans le dépôt (`grep` négatif sur la
  totalité de `/root/wiki`).
- **Commit** : 59e0e78

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — désignation effective (§V) instruite

- **Opération** : instruction des deux volets laissés ouverts par le §III
  (déclencheur de la routine, canal Discord de signalement). Recherche menée
  sur l'architecture Discord H‍ermes (`meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`)
  et le prompt réel du profil `gardien`
  (`meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`), révélant que
  ce dernier a un mandat doctrinal/éthique et non technique malgré son
  étiquette « Vigie transversale ». Détail complet au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Verdicts Sidy (2026-08-11)** : (1) déclencheur = **planifié par cron**
  (nouvelle surface assumée, refermée par construction puisque la routine ne
  fait que signaler sur Discord, jamais écrire au dépôt) ; (2) canal =
  **nouveau canal dédié**, pas de réutilisation de `#gardien`.
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (nouveau §V « Désignation effective » et §VI « reste à faire », toujours
  `brouillon` — nom du canal, fréquence exacte, contenu du rapport et
  mécanisme de post restent à instruire, Cmd 6),
  `atelier/rd/cahiers/registre-problemes.md` (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée, après correction d'un lien mal
  formé — ZWJ intempestif dans deux chemins `meta/projet-unifie/`).
  `Graphe/generer-cartographie.py --verifier` : 2 anomalies bloquantes
  (les 2 `frontmatter` pré-existantes, hors périmètre — inchangé).
- **Commit** : 34bc9a2

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — §III tranché

- **Opération** : discussion des trois questions du §III de
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (qui, quoi, comment consigner). Détail complet, y compris le retour en
  arrière sur la question 3, au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Verdicts Sidy (2026-08-11)** : (1) routine côté poste INTÉGRATION, pas
  d'agent H‍ermes dédié ; (2) périmètre = 3 scripts déterministes + mesure
  d'empreinte serveur (récurrence de la mesure laissée en chantier séparé) ;
  (3) signalement via un canal Discord existant, aucune écriture
  automatique dans `registre-problemes.md`.
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (§III et §V mis à jour, toujours `brouillon` — désignation effective non
  exécutée, Cmd 6), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée).
- **Commit** : 380595a

---

## [2026-08-11] outillage/proposition | Session R&D (suite) — détecteur non-trackés, statu quo SSH, proposition phase 3

- **Opération** : suite de la session R&D du jour (voir entrée précédente pour
  la première passe C4/cartographie/fourche Instrument). Trois volets restants
  du plan validé, traités ici.
- **Piste outillage C** : création de
  `atelier/rd/outillage/detecter-non-tracke.py` (+ fiche
  [[atelier/rd/outillage/spec-detecter-non-tracke]]) — constat déterministe des
  fichiers non trackés par git, classé par circuit. Lié depuis
  [[atelier/rd/index]]. Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Piste outillage D** : décision statu quo SSH (question posée le
  2026-08-09) consignée — verdict Sidy, aucune migration HTTPS+PAT du remote
  `origin`. `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`
  §5 réécrite. Détail au registre.
- **Phase 3 (agent de veille infrastructure)** : note d'instruction déposée en
  sas — `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  statut `brouillon`, non visée. Ne désigne aucun agent ; pose trois questions
  (qui, quoi, quand un signal devient une entrée du registre) et un risque
  (surface d'écriture si confiée à un agent H‍ermes) pour verdict de Sidy.
  Aucune écriture hors `_inbox/` pour ce volet (Cmd 6).
- **Fichiers modifiés** : `atelier/rd/index.md`,
  `atelier/rd/cahiers/registre-problemes.md` (2 nouvelles entrées),
  `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`.
- **Fichiers créés** : `atelier/rd/outillage/detecter-non-tracke.py`,
  `atelier/rd/outillage/spec-detecter-non-tracke.md`,
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`.
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée). `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes (les 2 `frontmatter` pré-existantes,
  hors périmètre — inchangé).
- **Commit** : 37e6023

---

## [2026-08-11] outillage/correction | Session R&D — C4 (verifier-invariants.py), cartographie serveur, fourche Instrument v0_3/v0.3

- **Opération** : session R&D instruite sur les 3 priorités validées (outillage,
  cartographie infra, phase 3) — voir [[atelier/rd/index]] et
  [[atelier/rd/cahiers/registre-problemes]] pour le détail des entrées.
- **`verifier-invariants.py`** : ajout du contrôle C4 (non bloquant) — signale
  un `annales.md`/`index.md` de circuit neutre pointant vers `meta/`, angle mort
  de l'exemption C3 consigné au registre le 2026-08-09. Non bloquant, cohérent
  avec la phase de calibrage en cours (CLAUDE.md, amendement 2026-07-27).
- **Créé** : `atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11.md` —
  relevé factuel matériel + empreinte mémoire (12 profils H‍ermes, `omniroute`),
  sans interprétation ni recommandation. Lié depuis [[atelier/rd/index]].
- **Piste outillage « générateur tolérant »** : constat que
  `Graphe/generer-cartographie.py` est déjà en v1.1 (2026-07-22, antérieure au
  diagnostic du registre) avec deux niveaux de sévérité — aucun correctif
  nécessaire. En instruisant les 4 anomalies d'étanchéité résiduelles, découverte
  d'une fourche non documentée :
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
  (tiret bas) et `...v0.3.md` (point) coexistaient comme deux fiches
  indépendantes depuis la migration `projets/ → rd/` du 2026-08-08 (les deux
  fourches existaient déjà séparément côté `projets/`). Comparaison confirmant
  `v0.3` (point) à jour et strict superset de `v0_3` (tiret bas, figée au
  2026-07-01) : `v0_3.md` repassée `deprecated` (Cmd 10, fusion sans perte) ;
  les 4 liens `doctrinal/sources/guenon-*` (sens interdit §VI vers `v0_3`)
  retirés côté `doctrinal/` et reportés en sens licite dans `v0.3.md` ;
  `atelier/index.md` repointé.
- **Fichiers modifiés** : `verifier-invariants.py`, `atelier/index.md`,
  `atelier/rd/index.md`, `atelier/rd/cahiers/registre-problemes.md` (2 entrées
  mises à jour en place + 1 nouvelle entrée `resolu`),
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`,
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`,
  4 fiches `doctrinal/sources/guenon-*`.
- **Validation** : `Graphe/generer-cartographie.py --verifier` : 6 → 2 anomalies
  bloquantes (restent 2 `frontmatter` pré-existantes, hors périmètre — contenu
  doctrinal, cf. registre). `verifier-invariants.py --racine /root/wiki` :
  `0 erreur(s), 40 avertissement(s)` (avertissements C4 attendus).
- **Commit** : 48cfaa6
- **Reste de la session validée** : piste outillage C (détection de fichiers non
  trackés), consignation du statu quo SSH
  (`atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md` §5),
  ouverture phase 3 (agent de veille infrastructure) — à traiter à la suite.

---

## [2026-08-10] outillage | Registre des problèmes R&D — near-miss étanchéité + récidive du piège de chiffre

- Consignation R&D (demande explicite de Sidy : « instruit le R&D s'il a
  quoi que ce soit de pertinent ») à la suite de la réparation des liens à
  référent vide du bloc `discernement/2026-06-20_*` (voir
  `doctrinal/annales.md` et `meta/meta-annales.md`, même jour) : une
  tentative de lien `doctrinal/ -> meta/` a été insérée puis interceptée et
  annulée **avant tout commit** (aucune trace dans l'historique git), et le
  chiffre de consigne (« 4 liens ») s'est révélé erroné à la revérification
  directe (5 réels) — troisième occurrence du même motif déjà consigné à
  deux reprises le 2026-08-09 dans ce registre. Entrée complète :
  [[atelier/rd/cahiers/registre-problemes]].
- **Commit** : 8e7dc07 (annales substantives de l'opération elle-même) — la
  présente entrée journalise séparément la mise à jour du cahier R&D.

---

## [2026-08-10] outillage | Méthode de traitement d'un lot mono-séance `discernement/` (qualification sashimono)

- Consignation R&D (demande explicite de Sidy : « rapporte tout ce que tu
  considères instructif au R&D ») du traitement du bloc
  `doctrinal/discernement/2026-06-20_*` (11 fiches) —
  [[atelier/rd/outillage/2026-08-10_methode-traitement-lot-discernement-sashimono]].
  Aucun contenu doctrinal reproduit ; méthode d'ingénierie uniquement
  (reconnaissance intégrale avant plan, distinguo ouverte/close/hors-catégorie,
  vérification mécanique indépendante de l'outil d'édition, séquence en deux
  commits substantif→annales). Complète
  [[atelier/rd/outillage/2026-08-10_methode-croisement-discernement]] pour le
  cas d'un lot mono-séance, hors périmètre de la méthode de croisement
  général.

---

## [2026-08-10] outillage | Méthode de croisement des fiches `discernement/`

- **Directive Sidy** : instruire le pôle R&D d'un rapport des moyens et méthode
  utilisés pour croiser les 33 fiches `doctrinal/discernement/` entre elles et
  avec le reste du circuit doctrinal (demande formulée sans accès serveur
  possible côté Claude.ai — angle mort visé par la présence d'un agent côté
  dépôt).
- **Créé** : [[atelier/rd/outillage/2026-08-10_methode-croisement-discernement]]
  — documente le passage déterministe (script bash d'extraction frontmatter/
  wikilinks/`to-source`/termes sashimono, exécuté avant toute lecture par le
  modèle) et la logique de clustering (partition par statut, graphe de
  co-citation, contrôle de complétude du double contrôle Gizeh, détection
  d'artefacts, isolement des blocs mono-session). Rapport d'ingénierie pur —
  aucun contenu doctrinal.
- **Vérification** : `verifier-invariants.py` → 0 erreur, 1 avertissement
  (`[C1] lien non résolu : [[^]]` — faux positif : le motif regex bash cité en
  exemple dans le corps de la fiche contient la séquence `[[^]]`, lue à tort
  comme un wikilink par le scanner mécanique ; aucun lien réellement cassé).
- **Commit** : `3e2f6c7` — OUTILLAGE: Méthode de croisement des fiches discernement (rapport R&D)

---

## [2026-08-09] integration | fiche Obsidian/Working Copy/GitHub du sas → `rd/infrastructure/`

- **Directive Sidy** : tout ce qui relève de l'infrastructure se consigne au
  pôle R&D (« tu n'oublieras pas de tout rapporter au R&D »).
- **Fiche intégrée** : `_inbox/fiche-setup-obsidian-git-sync.md` (rédigée
  2026-06-29, dépannage de la synchro iPad) →
  `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`
  (`type: infrastructure`, dates conservées/bumpées, contenu repris avec
  l'avis technique Hermes du 2026-08-09 sur la décision SSH/PAT — verdict
  Sidy toujours attendu).
- **Sas vidé** : la fiche originale est retirée de `_inbox/` après
  intégration ; `karubi-mehdi.md` et `image.jpeg` restent au sas.
- **Rappel connexe** : entrée registre des problèmes [2026-08-09]
  (vault désynchronisé = 6 commits serveur non poussés, `resolu`).

---

## [2026-08-08] arbitrage | `album-personnel.md` déplacé vers `label/production/` (verdict Sidy)

- **Verdict Sidy** : l'album personnel relève de la **création artistique**
  (œuvre et production) — circuit `label/`, non le pôle R&D. Arbitrage
  `rd/` vs `label/` (proposition §IV) tranché en faveur de `label/`.
- **Déplacement** : `atelier/projets/album-personnel.md` →
  `label/production/album-personnel.md` ; contenu transféré à l'identique,
  Sceau Recteur §V.b appliqué (`type: production`, `medium: musique`,
  `projet: label`, `statut: en-cours`), note de gouvernance ajoutée.
- **Cmd 10 respecté** : stub `deprecated` avec pointeur conservé en `projets/`.
- **4 liens entrants coupés** (étanchéité §VI) :
  `materiel/{neve-1073spx, studio-principal, tascam-model-12, technics-su-8080}`
  pointaient vers la fiche (neutre → plus sensible, interdit) ; frontmatter et
  corps purgés, `updated` bumped. La référence légitime vit désormais côté
  label (`liens_atelier`, §V.b, sens licite label → materiel).
- **Index mis à jour** : `label/index.md` (§III, nouvelle sous-section
  « Œuvre »), `atelier/index.md`, `rd/index.md`, `doctrinal/index.md` §VIII
  (repointé), arborescence §II et journal CLAUDE.md.
- **Registre des problèmes** : nouvelle entrée consignée ; entrée
  « 10 anomalies » → `partiellement-resolu` (4/10 levées).
- **Vérification mécanique** : `verifier-invariants.py --racine /root/wiki` →
  **0 erreur(s), 0 avertissement(s)** ; graphe → 6 anomalies préexistantes
  hors périmètre (consignées au registre).

---

## [2026-08-08] restauration | Ouverture du registre des problèmes du pôle `rd/` (phase 2 — discipline de laboratoire)

- **Verdict Sidy** : mécanisme approuvé, avec amorçage rétroactif depuis la
  session de migration (3 entrées).
- **Fichier créé** : `atelier/rd/cahiers/registre-problemes.md` — cahier
  append-only, premier cahier ouvert du pôle ; format miroir du bloc 🧪
  Expérience appliqué à l'erreur (Symptôme brut / Diagnostic / Résolution /
  Compréhension tirée / Liens / Statut).
- **Amorçage rétroactif (3 entrées)** :
  1. `graphe-cartographie.json` jamais régénéré (bloqué par les anomalies du
     graphe) — ouvert ;
  2. 10 anomalies bloquantes du graphe (8 étanchéité + 2 frontmatter),
     pré-existantes, vérifiées contre la baseline HEAD — ouvert ;
  3. lien mort `manvantara → v0_2` (version inexistante), corrigé vers `v0.3`
     lors de la migration — résolu.
- **Index** : `rd/index.md` mis à jour (le registre entre dans l'arborescence).
- **Rien d'autre** : pas de modification de CLAUDE.md (Sceau et type `meta`
  suffisent), aucun nouveau circuit, aucune règle de lien nouvelle.

---

## [2026-08-08] migration | `atelier/projets/` → `rd/` — 16 fiches migrées (proposition §IV exécutée)

- **Opération** : migration fiche par fiche du dossier `projets/` vers le pôle
  `rd/` (verdict Sidy 2026-08-08, proposition §IV : « le dossier devient rd/
  par migration fiche à fiche ; chaque fiche migrée garde son slug, l'ancienne
  reçoit deprecated avec pointeur »).
- **Migrées vers `rd/instrument/` (15 fiches)** : architecture v0.1, v0.2,
  v0.3, v0_3 ; feuille-de-route-v2 ; spec-technique-axe-38-degres ;
  spec-anneau-zodiacal ; angles-de-l-espace ;
  references-visuelles-astronomiques-phase-5 ; soumission-gem-convergence-28 ;
  soumission-gem-reponse-geometrie-3d ; soumission-gem-reponse-gloton ;
  soumission-gem-reponse-visuelle-28 ;
  2026-07-26_investigation-referentiels-stellaires-cycles ;
  note-impact-instrument-socle-universel-2026-07-16.
- **Migrée vers `rd/outillage/` (1 fiche)** : spec-generateur-manifeste.
- **Cmd 10 respecté** : aucune suppression — chaque ancienne fiche reste en
  `projets/` comme stub `type: deprecated` avec pointeur vers la fiche
  canonique ; contenu des fiches inchangé, dates conservées, bandeau de
  migration inséré.
- **Assets et outillage déplacés avec les fiches** (git mv) :
  `assets-instrument/` (4 images), `instrument-donnees.yaml`,
  `wiki-manifest.json`, `instrument-prototype.html`, `generer-manifeste.py`
  (chemins par défaut du script mis à jour).
- **Scripts mis à jour** : `generer-manifeste.py` (chemins données/sortie →
  `rd/instrument/`) ; `Graphe/generer-cartographie.py` (rang d'étanchéité
  `atelier/rd` = 1, hérité de projets/, CLAUDE.md §VI).
- **Liens repointés** : 15 wikilinks entrants (atelier/index, doctrinal/index,
  4 fiches doctrinal/sources) + références textuelles (meta/projet-unifie/02,
  README, doctrinal/symboles/manvantara — pointait une version `v0_2`
  inexistante, corrigé vers v0.3 ; doctrinal/discernement/zodiaque-barzakh).
  Les annales et les cartes générées ne sont pas repointées (documents
  historiques / artefacts dérivés).
- **Non migré** : `album-personnel.md` — arbitrage `rd/` vs `label/` requis
  (proposition §IV : « à trancher fiche par fiche » ; verdict Sidy en attente).
- **Vérifications** : invariants (0 erreur), cartographie (0 nouvelle anomalie
  vs baseline : 9 anomalies d'étanchéité pré-existantes, identiques avant/après),
  manifeste régénéré (43 nœuds, 9 ancrages).

---

## [2026-08-08] restauration | Ouverture du pôle R&D `atelier/rd/` (verdict Sidy : Option C, phase 1 partielle)

- **Verdict consigné** : « Option C, nom `rd/`, phase 1 partielle. Tout ce qui
  en relève doit systématiquement y être consigné avec comme but l'entretien,
  le développement qualitatif, l'optimisation à mesure de l'infrastructure
  globale hardware/software, l'émancipation progressive de tout intermédiaire
  de service tiers par souveraineté des moyens de production/déploiement/
  information. Un des agents sera chargé de veiller à cette tâche spécifique. »
  Cinq circuits, inchangés (pas de sixième circuit).
- **Créé** : `atelier/rd/index.md` (charte du lieu, mission verbatim,
  frontières, état de phase) ; arborescence `rd/{instrument,infrastructure,
  audio,outillage,cahiers}/` (.gitkeep).
- **Amendements CLAUDE.md** : note de révision (second amendement 2026-08-08) ;
  §II arborescence atelier ; §V.a Sceau atelier étendu (types
  `experience | infrastructure | outillage`, `statut_experience` optionnel,
  `projets/` et `rd/` même régime de lien) ; §V.d `liens_atelier` élargi à
  `atelier/etudes-de-cas/` et `atelier/rd/` ; §VI hiérarchie d'étanchéité
  (rd/ hérite du régime de projets/, frontière meta/rd précisée) ; Cmd 9
  (annales de l'atelier inscrites à la liste).
- **Amendé** : `atelier/index.md` — régimes référence/recherche, section R&D,
  destination de migration de `projets/` signalée.
- **Déposé** : `meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08.md`
  (proposition d'origine, brouillon, commitée avec l'opération qu'elle a fondée).
- **Non inclus dans la phase 1 partielle** : migration de `atelier/projets/`
  (fiche par fiche, Cmd 10), discipline de laboratoire (phase 2), agent de
  veille infrastructure (phase 3, sur désignation de Sidy).
- **Vérification** : `python3 verifier-invariants.py --racine /root/wiki` →
  `0 erreur(s), 0 avertissement(s).` (exécuté avant le commit).
- **Commit** : 3c1b3d8

## [2026-08-08] archivage | Studio Principal — fiche-hub de l'espace d'atelier

- **Créé** : `atelier/materiel/studio-principal.md` (depuis `_inbox/studio-principal.md`) —
  fiche-hub de l'espace audio (trois pôles : synthèse/composition, enregistrement
  analogique, monitoring). `sources: ["to-source"]`, plusieurs points marqués
  incertains dans le corps (placement Yamaha H5, sync Tascam/Logic, configuration
  rack, acoustique).
- **Chevauchement traité** : deux appareils décrits dans la source
  (Neve 1073SPX, Tascam Model 12) avaient déjà leur fiche propre, sourcée
  (`chatgpt-export-2026-05-10`) — `atelier/materiel/neve-1073spx.md` et
  `atelier/materiel/tascam-model-12.md`. Décision (Sidy) : fiche-hub sans
  duplication — les deux fiches existantes sont référencées par wikilink et non
  redécrites ; seuls les éléments nouveaux (Moog Voyager, Fender Rhodes, Revox A77,
  micros, Yamaha H5, Distressor EL8x, chaîne de capture) sont documentés en propre.
- **Deux fichiers déjà déposés à l'appui, non encore confrontés au texte** :
  `raw/assets/studio-principal-vue-generale.jpeg`, `raw/assets/routing-schema.html`
  — signalés en §« Sources à déposer » de la fiche.
- **`atelier/index.md`** : ajout d'une entrée sous « Matériels & Techniques ».
- `verifier-invariants.py --racine /root/wiki` : à exécuter avant commit.

## [2026-07-27] spec-anneau + instrument-donnees.yaml | Dédoublement 19/20, 7 prophètes planétaires

- **Opération** : ARCHIVAGE ET CORRECTION — intégration spec anneau zodiacal et mise à jour YAML avec 7 ancrages établis + paramètres zodiaque.
- **Créé** : `atelier/projets/spec-anneau-zodiacal.md` (copié de _inbox/, quatre amendements appliqués)
- **Modifié** : `atelier/projets/instrument-donnees.yaml` (v0.3.1 → v0.3.2 *draft*)
- **Contenu des amendements à spec-anneau** :
  * **§3.1** : dédoublement confirmé (19/20, Toit/Terre du Jardin), avec justification doctrinale Gloton pp. 39-40. Two constantes `degre_falak_al_buruj: 19` + `degre_falak_al_manazil: 20` (12 signes vs 28 manāzil).
  * **§3.3** : paramètre époque validé (`epoque_reference`), avec justification ad-dahr (le Temps pur siège au degré 19).
  * **§3.1 (addendum)** : confirmation degré 19 par trois voies (Gloton, hiérarchie islamique, table 28 degrés) — point ouvert 5 clos.
  * **§3.4** : non-alignement renforcé, deux divisions cessent d'être superposées sur support unique.
- **Contenu YAML (v0.3.2)** :
  * 7 ancrages prophètes planétaires ajoutés (degrés 21-27) : Abraham/Saturne/samedi → Adam/Lune/lundi, source Gloton pp. 39-40 + Mahdi Rouge articles I-II, statut `etabli`.
  * Section `zodiaque:` ajoutée : `degre_falak_al_buruj: 19`, `degre_falak_al_manazil: 20`, `obliquite_deg: 23.44`, `epoque_reference: null` (à paramétrer Phase 5).
  * Nœuds/ancrages structurants inchangés ; version YAML remise à jour sans validation de manifeste (crédit API insuffisant en fin de session).
- **Validation** : spec-anneau relue (4 amendements grammaticaux + jusifications doctrinales), YAML syntaxe valide (grep/inspection manuelle).
- **Points de vigilance** :
  * Dédoublement 19/20 : correction ergonomique *et* doctrinale. Deux anneaux concentriques à deux hauteurs distinct (rendu à décider : deux couronnes ou deux niveaux différents selon Phase 5 UI).
  * Paramètre époque : validé comme concept, valeur concrète (JD ou UTC) à fixer en Phase 5 (calcul astrologique multi-méthodes) — actuellement `null`.
  * Prophètes planétaires : ancrage établi sur identité prophète↔ciel↔degré (données akbariennes primaires), distinct de l'ancrage Aqtâb guénonien (Phase 3). Aucun élément dans instrument-donnees.yaml tant que fiche discernement septénaire transversal n'est pas close.
  * Aucune génération manifeste en fin de session (crédit API insufficient) — à valider en prochaine session après rédaction fiche discernement.
- **Prochaine étape** : rédaction fiche discernement [[doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil]] (plan consigné), fermeture du lot B, validation manifeste + commit final du v0.3.2.
- **Note de méthode** : le dédoublement 19/20 rend visible une articulation doctrinale explicitée par la source (Gloton) — pas de « correction pour le confort visuel » mais exécution d'une structure sourcée que la table implicite. Aucun ancrage dans YAML tant que la fiche discernement n'est pas validée (Cmd 13).

---

## [2026-07-17] archivage | instrument-donnees.yaml v0.3.1 + ancrage Aqtâb (Phase 2)

- **Opération** : ARCHIVAGE — intégration d'une version mise à jour du YAML applicatif.
- **Remplacé** : `atelier/projets/instrument-donnees.yaml` (v0.3 du 2026-07-01) → v0.3.1
  du 2026-07-17.
- **Contenu** :
  * 36 nœuds déclarés (8 notionnels structurants/traversants + 28 nœuds-degrés 11-38).
  * 3 ancrages `établi` :
    - (a) table-28 ↔ manazil-al-qamar (convergence des 28, inchangé depuis v0.3)
    - (b) table-28 ↔ nafas-rahmani (convergence des 28, inchangé depuis v0.3)
    - (c) **NOUVEAU** : table-28 ↔ sept-Pôles/Aqtâb guénoniens, **cible: null**, sourcé par
      `doctrinal/discernement/2026-07-16_sept-poles-aqtab-malakut-planetaire`. Identité
      doctrinale (non-syncrétisme), confirmée par convergences textuelles guénoniennes
      (3 sources indépendantes) + source akbarienne antérieure (1911).
- **Validation** : exécuté `python3 generer-manifeste.py --repo /root/wiki` → ✓ 0 erreur,
  36 nœuds, 3 ancrages, 0 avertissements, commit 996ee452c13d.
- **Point de vigilance** :
  * Ancrage (c) sans nœud cible : l'Instrument ne modélise actuellement que la tradition
    `tasawwuf` (Phase 2, multi-traditions, Phase 3 non ouverte). L'ancrage est porté sur
    le nœud structurant `table-28-degres-nafas-rahman` en attente de déclaration d'un
    nœud `aqtab` formel. Placement confirmé par Sidy avant intégration.
  * Réserve résiduelle (fiche doctrinal) : lien explicite wirātha↔aqtāb non localisé dans
    extrait transmis du Futūḥāt ch. 36 — à rechercher pour ancrage (c) plus complet.
- **Génération manifeste** : `wiki-manifest.json` produit sans anomalie.

---
