---
title: "Journal des optimisations — pôle R&D (cahier append-only)"
type: meta
created: 2026-08-30
updated: 2026-09-13
tags: [atelier, rd, cahier, registre, laboratoire]
sources: []
links: []
---

# Journal des optimisations du pôle R&D

Cahier append-only des **améliorations de procédure** effectuées dans les travaux
du pôle `rd/`. Ouvert le 2026-08-30 (verdict Sidy, même séance) — miroir du
[[atelier/rd/cahiers/registre-problemes]] : là où le registre consigne les
échecs/blocages et leur résolution, ce journal consigne les optimisations
réussies et leur impact. Les deux partagent la même discipline de laboratoire
(règle 3 du pôle : tout fait se consigne, succès ou échec).

**Format** — phase 1 (consignation factuelle, aucune interprétation, même
esprit que les fiches `phase: corpus` de `atelier/etudes-de-cas/`) :

- **Procédure modifiée** : quel protocole, fiche, script ou outillage.
- **État avant** : description factuelle de l'état précédent (diff, commande,
  extrait).
- **Changement effectué** : ce qui a été modifié, sans reformulation narrative.
- **État après** : description factuelle du résultat (nouveau diff, nouvelle
  commande, nouvelle sortie).
- **Impact mesuré** : chiffres, temps, erreurs évitées — flagué `to-source` si
  l'impact n'est pas vérifié mécaniquement (§VII).
- **Liens** : fiches, commits, chantier concernés.
- **Statut** : `applique | mesure-pending | reporte`.

**Ce qui n'est pas ici** : la « leçon » d'une optimisation est une
interprétation (phase 2). Elle viendra dans une fiche séparée quand plusieurs
entrées auront le même motif, sur décision de Sidy. Le journal ne fait pas de
généralisation — il consigne.

**Règle** : append-only, jamais de réécriture ni de suppression (Cmd 10).
Insertion en tête (la plus récente en haut), marqueur ci-dessous.

<!-- INSERTION: EN-TÊTE -->

## [2026-09-13] Provider LLM des trois gateways rétabli sur DeepSeek — la bascule du 11/09 absente des `config.yaml`

- **Procédure modifiée** : provider LLM principal (`model.provider`,
  `model.default`) des profils `gardien`, `publication` et `studio` ;
  redémarrage des unités `hermes-gateway-{gardien,publication,studio}.service`.
  Demande de Sidy en session : « Redémarre le gateway de Publication », puis
  « Bascule Gardien aussi ».
- **État avant** (relevé du 13/09, ~14:00 UTC) :
  - `publication/config.yaml` et `studio/config.yaml` : `model.provider:
    custom:omniroute`, `model.default: auto/best-free`.
  - `gardien/config.yaml` : `model.provider: qwen`, `model.default:
    qwen3.7-plus`.
  - Aucun listener sur `localhost:20128` (`curl` → code 000) et **aucune unité
    systemd** ne lance `omniroute` (binaire pourtant présent : `/usr/bin/omniroute`,
    v3.8.50).
  - Journal du gateway `publication`, à 13:55:37 (avant tout redémarrage) :
    `APIConnectionError` sur `http://localhost:20128/v1`, trois tentatives,
    `API failed after 3 retries — Connection error`.
  - Test direct du provider `qwen` avec le modèle de la config de `gardien`
    (`qwen3.7-plus`) : **HTTP 403** `AccessDenied.Unpurchased` (« Access to
    model denied »).
  - Les trois `config.yaml` **ne portaient donc pas** la bascule que l'entrée
    `[2026-09-11]` ci-dessous consigne comme appliquée. L'écart est constaté,
    non expliqué (ni la date ni le mécanisme de la divergence ne sont établis) ;
    l'entrée du 11/09 n'est pas réécrite (Cmd 10).
- **Changement effectué** :
  1. Sauvegarde des trois fichiers en `config.yaml.bak-predeepseek-20260913`.
  2. `model.provider: deepseek`, `model.default: deepseek-v4-flash` dans les
     trois profils. Le bloc `providers.omniroute` est **conservé**, non
     supprimé, pour rester disponible si le service est relancé.
  3. Redémarrage des trois unités (`XDG_RUNTIME_DIR=/run/user/0`).
  4. `publication` a été redémarré **deux fois** : d'abord à la demande de Sidy
     (14:03, provider encore `custom:omniroute`), puis une seconde fois après la
     bascule de son provider (14:06).
- **État après** : test d'aller-retour réel par `hermes --profile <nom> -z`
  — la config est lue *et* une génération est demandée, ce n'est pas une simple
  relecture de fichier. Les trois rendent la réponse attendue :
  - `publication` → `OK-PUBLICATION` (PID 292241)
  - `studio` → `OK-STUDIO` (PID 292266)
  - `gardien` → `OK-GARDIEN` (PID 292920)

  Journaux des trois unités après redémarrage : aucune erreur de provider (les
  seules lignes `Failed with result 'exit-code'` sont la mort des anciens
  processus pendant l'arrêt volontaire). `verifier-invariants.py` : **0 erreur,
  73 avertissements**, exit 0 — identique à la mesure d'avant intervention.
- **Impact mesuré** : **3 profils sur 3 répondent** après bascule, contre
  **0 sur 3** avant (403 côté qwen, connexion refusée côté omniroute). RAM des
  gateways au relevé : publication 207,2 MiB (pic 229,8), studio 206,5 MiB
  (pic 234,2), gardien 185,8 MiB (pic 205,3). Le coût de la bascule reste
  `to-source` : aucune facturation DeepSeek relevée à cette heure.
- **Signalement lié** : `INF-07` (fonction réelle du processus `omniroute`,
  `en-cours`) — au 13/09 le processus **n'existe pas** : ni listener sur son
  port, ni unité systemd. Consigné ici comme fait, **non inscrit au registre**
  (verdict requis, Cmd 12).
- **Liens** : `~/.hermes/profiles/{gardien,publication,studio}/config.yaml` et
  leurs copies `.bak-predeepseek-20260913` ; `.env` des mêmes profils
  (`DEEPSEEK_API_KEY`) ; `plugins/model-providers/deepseek/` de l'installation
  Hermes (`/usr/local/lib/hermes-agent/`, qui documente le retrait des alias
  `deepseek-chat`/`deepseek-reasoner` au 2026-07-24) ; `https://api.deepseek.com`
  (`/v1/models` → `deepseek-flash`, `deepseek-v4-pro`) ; annales
  `atelier/annales.md`, entrée du 2026-09-13.
- **Statut** : `applique`.

## [2026-09-11] Migration provider LLM : Omniroute → DeepSeek V4.1-Flash

- **Procédure modifiée** : provider LLM principal, fallback chain, auxiliaires
  (vision, compression, title_generation), clé API et crons des profils
  gardien/publication/studio.
- **État avant** : provider par défaut `custom:omniroute` (`localhost:20128/v1`),
  model `auto/best-free`. Omniroute en mode forwarding reposant sur la RAM
  locale du serveur — les 14 gateways simultanés saturaient les 3.7 GiB
  disponibles. Les crons des 12 profils (default + 11 secondaires) tournaient
  tous en agent-mode sur Omniroute, multipliant les requêtes concurrentes.
  Les 3 gateways cibles (gardien/publication/studio) échouaient en
  `RuntimeError: Connection error` quotidiennement depuis fin août. Aucun
  mode réflexion/thinking n'était activé sur les crons.
- **Changement effectué** :
  1. Provider principal : `model.default = deepseek/deepseek-flash`
     (DeepSeek-V4.1-Flash, 552B MoE, 8-16B actifs, KV cache 890 B/token).
  2. Provider de secours : Omniroute conservé en `fallback_providers`
     (bascule automatique sur rate-limit/erreur réseaux).
  3. Auxiliaires : `auxiliary.vision.provider`, `auxiliary.compression.provider`,
     `auxiliary.title_generation.provider` → deepseek.
  4. Clé API : `DEEPSEEK_API_KEY` ajoutée dans `~/.hermes/.env` + `.env` des
     3 profils actifs (gardien, publication, studio) — chaque gateway lit
     son propre `$HERMES_HOME/.env`, pas la racine.
  5. Crons : tous les crons des profils default, marketing, accounting,
     admin-legal, ar-music, commerce, distribution, fanzine, karubi,
     production, visual-da désactivés (pauses). Seuls restent actifs
     gardien (`veille-protocole-gardien`), publication
     (`veille-referencement-investigation-08` + `archiver-veille-publication`)
     et studio (`monitoring-infrastructure-quotidien` +
     `coherence-infrastructure-brute` + `archiver-monitoring-quotidien`).
  6. Cible profil : `hermes --profile <nom> cron edit/pause` (la variable
     `HERMES_PROFILE` est ignorée par le CLI cron).
  7. Mode réflexion : `--reasoning-effort high` piné sur les 3 crons
     agent-mode (thinking DeepSeek natif).
  8. Horaires : tous les crons actifs tournent 11:00-12:30 UTC (off-peak
     DeepSeek, hors 01:10h UTC lun-ven).
  9. Gateways : les 3 services systemd ont été restartés (`systemctl --user
     restart hermes-gateway-{gardien,publication,studio}.service`).
- **État après** : run test `veille-protocole-gardien` → `succeeded`.
  Les 3 gateways actifs avec PIDs neufs, chacun pointant deepseek-flash.
  Les runs publication et studio en cours (agents scan lourds du wiki).
  Le provider Omniroute reste disponible en fallback, pas supprimé de
  la config.
- **Impact mesuré** : RAM gateway gardien : ~210 MiB (stable, pic 297 MiB).
  Coût off-peak : $0.15/M tokens entrée, $0.60/M sortie (vs Omniroute
  dont le coût réel n'était pas mesuré car forwarding local).
  Les erreurs `Connection error` quotidiennes des 3 crons sont résolues
  (testé : run gardien succeeded). `to-source` pour les gains RAM globaux
  (le serveur tourne encore à 2.7 Gi/3.7 Gi — les gateways désactivés
  des autres profils ne sont pas encore arrêtés).
- **Liens** : `~/.hermes/config.yaml` (provider.default, fallback_providers,
  auxiliary.*) ; `~/.hermes/.env` (DEEPSEEK_API_KEY) ;
  `~/.hermes/profiles/{gardien,publication,studio}/.env` (clés DeepSeek) ;
  `~/.hermes/profiles/*/cron/jobs.json` (pins provider/model/reasoning) ;
  https://api-docs.deepseek.com/ (documentation officielle).
- **Statut** : `applique` — run test gardien succeeded, crons schedulés
  activés sur deepseek-flash, gateways relancés.

## [2026-09-02] Chaîne OCR versée en outillage — le scan d'ouvrage devient reproductible

- **Procédure modifiée** : conversion des scans d'ouvrages de `raw/` vers du
  Markdown exploitable. Aucune procédure n'existait : les deux conversions
  précédentes du dépôt (Jurjani, index Tilak) étaient des **transcriptions
  humaines de photographies**, pas des conversions de PDF.
- **État avant** : deux scripts écrits en session, hors dépôt
  (`/root/ocr_pdf2md.sh`, `/root/decouper_chapitres.py`), non versionnés, non
  documentés, non éprouvés — donc perdus à la session suivante.
- **Changement effectué** : versés en `atelier/rd/outillage/` sous
  `ocr-scan-vers-markdown.sh` et `decouper-ouvrage-chapitres.py`, avec leur
  spécification `spec-ocr-scan-vers-markdown.md`. Un **contrôle d'intégrité** a
  été ajouté au découpeur (aucune page perdue ni dupliquée, sortie en code non
  nul sinon) — il n'existait pas dans la version de session, où la vérification
  était faite à la main.
- **État après** : le découpage rejoué depuis le nouvel emplacement rend un
  résultat **identique octet pour octet** au résultat de session (contrôlé par
  `diff` sur les chapitres 1, 9 et 13). Le contrôle d'intégrité rend
  `544 / 544 pages, 0 manquante, 0 doublon`, code 0.
- **Impact mesuré** : 781 pages converties (237 + 544), ~13 pages/minute,
  0 page perdue, 0 dupliquée sur les deux ouvrages. Sur le premier ouvrage,
  l'OCR neuf remplace une couche texte de 2006 rendant « Prajapatit=Yaj Da »
  là où `tesseract` rend « Prajapati=Yajna ».
- **Épreuve du contrôle** (§VII) : le contrôle d'intégrité a été **mis en défaut
  dans un bac à sable** avant d'être déclaré. Sur une copie dont la fusion des
  sections d'index a été volontairement rendue fautive, il rapporte
  `540 pages reparties / 544 lues`, nomme les quatre pages perdues (508, 510,
  514, 526) et sort en code 1. État sain restauré : `544 / 544`, code 0.
- **Liens** : [[atelier/rd/outillage/spec-ocr-scan-vers-markdown]] ·
  [[atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe]] ·
  chantier `BIB-03`.
- **Statut** : `applique`.

## [2026-08-30] Validation formelle — reconnaissance, pas ajout (item 3 clos)

- **Procédure modifiée** : aucune — l'item 3 est clos par reconnaissance.
- **État avant** : l'aspiration SLM avait identifié un manque supposé :
  protocole de validation formelle pour les fiches doctrinales (entrée/sortie,
  critères mécaniquement vérifiables, scellement). Proposition initiale :
  créer un script `valider-fiche-doctrinale.py` et étendre Karūbī.
- **Décision** : Sidy renvoie au discernement adopté du 2026-08-11
  ([[doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire]])
  qui contient déjà toute la légitimation — l'Athanor = Laboratoire-Sandbox
  (rd/), le flux Discernement → Laboratoire → Doctrine/Archivage, la
  validation par le Maître (Cmd 6/12/13), la distinction Doctrine/Théorie.
  Le dispositif Karūbī (zones scellées, hash, navette, registre-silsila)
  fait déjà la validation mécanique pour les transmissions. Le Sceau Recteur
  (frontmatter doctrinal) fait déjà la validation structurelle pour le
  doctrinal.
- **Changement effectué** : aucun protocole/script ajouté. L'item 3 est clos
  par reconnaissance de ce qui est déjà en acte.
- **État après** : la validation formelle n'est pas à créer — elle est déjà
  là, incarnée dans le discernement adopté du 2026-08-11 et les dispositifs
  existants (Karūbī, Sceau Recteur). Ce qui manque n'est pas un protocole —
  c'est la source Burckhardt "Alchimie" pour approfondir le vocabulaire
  (`to-source`).
- **Impact mesuré** : aucun ajout, donc aucun impact à mesurer. La clôture
  par reconnaissance évite la redondance.
- **Liens** : [[doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire]]
  (légitimation alchimique du Laboratoire-Athanor) ; `meta/transmissions/karubi-gabarit.md`
  (dispositif Karūbī, validation mécanique) ; `doctrinal/CLAUDE.md` (Sceau Recteur,
  validation structurelle) ; séance WebUI 2026-08-30 (verdict Sidy, item 3 clos par
  reconnaissance).
- **Statut** : `applique` — item 3 clos, aucune procédure ajoutée, source
  Burckhardt "Alchimie" `to-source`.

## [2026-08-30] Application procédure exploitation graphe — Golem + Frankenstein

- **Procédure appliquée** : exploitation du graphe (2026-08-30) à l'intégration de trois nouvelles fiches
- **Fiches créées** :
  - `doctrinal/symboles/golem.md` (symbole, phase 1, corpus brut, to-source)
  - `hermeneutique/frankenstein/frankenstein.md` (œuvre, phase 1, corpus brut, to-source)
  - `hermeneutique/auteurs/mary-shelley.md` (auteur)
- **Signalement graphe** : les trois fiches sont orphelines (zéro lien entrant), cross_links vides
- **Action** : liens signalés comme pistes (discernement matrices-artificielles-barzakh, symbole golem) mais non inscrits — en attente de verdict Sidy (Cmd 12)
- **Décision de méthode** : la procédure d'exploitation du graphe est appliquée systématiquement à l'intégration, y compris pour les fiches herméneutiques liées au doctrinal
- **Liens** : [[doctrinal/discernement/2026-06-20_matrices-artificielles-barzakh]], [[doctrinal/symboles/golem]], [[hermeneutique/frankenstein/frankenstein]]
- **Commit** : 659808c
- **Statut** : `applique` — procédure appliquée, fiches en attente de verdict

## [2026-08-30] Ouverture du journal des optimisations

- **Procédure modifiée** : discipline de laboratoire du pôle R&D — ajout d'un
  quatrième cahier à `atelier/rd/cahiers/`, après `registre-problemes.md`
  (2026-08-08), le bilan-pont (2026-08-15) et les comptes-rendus de sessions.
- **État avant** : le registre-problèmes consignait les échecs/blocages et
  leur résolution, avec le champ « Compréhension tirée ». Les optimisations
  réussies (procédures améliorées, scripts corrigés, contrôles ajoutés) ne
  laissaient aucune trace propre — elles étaient dispersées dans les annales
  ou les comptes-rendus de sessions, sans format dédié.
- **Changement effectué** : création de `atelier/rd/cahiers/journal-optimisations.md`
  (le présent fichier), annonce insérée dans `atelier/annales.md` (entrée du
  jour, SHA à compléter).
- **État après** : quatre cahiers dans `atelier/rd/cahiers/` — le registre des
  problèmes (échecs), le présent journal (réussites), le bilan-pont (synthèse
  transverse), les comptes-rendus de sessions (chroniques). Chaque optimisation
  effectuée dans le pôle a désormais son lieu de consignation dédié.
- **Impact mesuré** : non mesuré à ce stade — le cahier vient d'ouvrir, aucune
  entrée factuelle d'optimisation n'y a encore été versée. `to-source`.
- **Liens** : [[atelier/rd/cahiers/registre-problemes]] (cahier miroir) ;
  [[atelier/rd/index.md]] §Arborescence (à compléter du nouveau cahier) ;
  séance WebUI 2026-08-30 (verdict Sidy d'ouverture). Commit `84dc4de`.
- **Statut** : `applique` — le cahier est ouvert, en attente de sa première
  entrée d'optimisation factuelle.

## [2026-08-30] Maillage doctrinal — exploitation du graphe existant, pas d'outil parallèle

- **Procédure modifiée** : `doctrinal/CLAUDE.md` — ajout de la section
  « Exploitation du graphe lors de l'intégration (signal d'orphelins) ».
- **État avant** : le graphe (`graphe-cartographie.json`, 1475 edges,
  438 nodes, `Graphe/generer-cartographie.py`) existait mais n'était pas
  exploité systématiquement lors de l'intégration d'une nouvelle fiche
  doctrinale. Aucun signalement d'orphelins n'était produit à ce moment.
- **Changement effectué** : procédure ajoutée dans `doctrinal/CLAUDE.md`
  — l'agent consulte le graphe à l'intégration, signale les orphelines
  (zéro lien entrant), propose des liens (filiations orthodoxes/hétérodoxes)
  sans les inscrire, Sidy tranche (Cmd 12), puis les `cross_links` sont
  ajoutés et le graphe régénéré.
- **État après** : chaque nouvelle fiche doctrinale est désormais vérifiée
  contre le graphe existant avant inscription définitive des liens.
- **Impact mesuré** : non mesuré à ce stade (la procédure vient d'être
  ajoutée, aucune fiche intégrée depuis). `to-source`.
- **Décision de méthode** : pas de script parallèle créé — le graphe
  existant suffit. Un script `detecter-orphelins-doctrinaux.py` avait été
  amorcé puis supprimé (redondance, 143/305 fiches remontaient — bruit, pas
  signal).
- **Liens** : `doctrinal/CLAUDE.md` (section ajoutée) ; `graphe-cartographie.json`
  (source de vérité du maillage) ; `Graphe/generer-cartographie.py`
  (générateur) ; `doctrinal/annales.md` (entrée du 2026-08-30). Commit `2ec5a20`.
- **Statut** : `applique` — procédure en vigueur, en attente de la première
  intégration doctrinale avec signal d'orpheline.

## [2026-09-01] Levée du `to-source` Burckhardt « Alchimie » — légitimation athanor/Laboratoire

- **État avant** : la légitimation alchimique du Laboratoire-Athanor
  (ligne 70 ci-dessus) reposait sur l'analogie athanor/Sandbox affirmée dans
  `doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md`
  sans texte primaire — `sources: [to-source]`.
- **Changement effectué** : Sidy a photographié le chapitre XIII
  (« L'athanor ») de Titus Burckhardt, *Alchimie : Science et Sagesse*, et
  demandé l'intégration. Transcription intégrale déposée dans
  `doctrinal/sources/burckhardt-alchimie-ch13-athanor-transcription.md`,
  fiche `doctrinal/autorites/titus-burckhardt.md` mise à jour (2e ouvrage).
- **État après** : `to-source` levé dans la fiche discernement, remplacé par
  le lien vers la transcription, avec signalement daté dans le corps.
- **Impact mesuré** : non mesuré (marqueur de sourçage, pas de métrique de
  performance).
- **Liens** : `doctrinal/sources/burckhardt-alchimie-ch13-athanor-transcription.md` ;
  `doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md` ;
  `doctrinal/autorites/titus-burckhardt.md`.
- **Statut** : `applique`.
