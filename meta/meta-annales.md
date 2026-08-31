---
title: Annales du Domaine Réservé (meta/)
type: meta
updated: 2026-08-31

---

# Annales du Domaine Réservé (`meta/`)

Journal chronologique inverse des opérations propres au domaine `meta/`
(la plus récente en haut). Append-only. Nommage préfixé `meta-` pour ne
jamais se confondre avec les `annales.md` des quatre circuits — `meta/`
reste le Domaine Réservé (§VI CLAUDE.md), pas un sixième circuit.

<!-- INSERTION: EN-TÊTE -->

## [2026-08-31] déploiement | Les 11 principes portés au moteur — 12/12 synchronisés

Go explicite de Sidy (Cmd 13), après la passe documentaire du matin. C'est la
fermeture du constat le plus lourd de la journée : onze agents sur douze
tournaient sur un prompt antérieur aux calibrations zodicales et aux mandats votés.

- **Sauvegardes** : `SOUL.md.bak-20260831-142649` dans chaque profil, hors dépôt,
  prises avant écriture. Retour possible profil par profil.
- **Déployé** : `NN-principe.md` → `SOUL.md` ; chaque `mandats/X.md` →
  `skills/hermes/X/SKILL.md` avec frontmatter `name` + `description`, corps verbatim.
  13 mandats posés au total. `publication` non retouché — déjà synchronisé.
- **Vérification `--derive`, sortie brute** : **0 agent en écart sur 12**, contre 11
  avant la passe. Hygiène Unicode sur le moteur (`SOUL.md` + `SKILL.md`) : 0 résultat
  — les 3 U+200D résiduels de `studio/SOUL.md`, hors dépôt donc hors du nettoyage du
  2026-08-22, sont partis avec le déploiement.
- **Vérification côté moteur** (§VIII.2 — le disque ne prouve pas le chargement) :
  compte de skills annoncé par les passerelles, `84 → 86` sur gardien et studio (deux
  mandats chacun), `87 → 87` sur publication (aucun nouveau). Le hook Choura s'est
  réenregistré au redémarrage (`14:27:15`).
- **Redémarrages** : 4 passerelles vivantes (`gardien`, `publication`, `studio`,
  `visual-da`) par `systemctl --user restart`, une à une. `SOUL.md` est relu à chaque
  prompt et n'exigeait pas de redémarrage ; les **skills** passent par un cache dont
  la clé ne porte ni mtime ni manifeste, d'où la nécessité. Les 8 dormants n'ont pas
  été réveillés : ils prendront leur prompt à leur prochaine fenêtre, la RAM
  (~730 Mo disponibles) ne permettant pas de les lever ensemble.
- **Observation non traitée** : `visual-da` tournait à 14:26 alors que son tour est à
  16:00 et que l'orchestrateur ouvre la fenêtre à 15:00. Écart constaté, non
  diagnostiqué — à instruire.
- **Commit** : 5039b1e


## [2026-08-31] protocole | Approbation requise ramenée à 0 sur `main`

Consigne de Sidy, après le constat fait à la fusion de la PR #20.

- **Constat** : `main` exigeait `required_approving_review_count: 1`. Le dépôt n'a
  qu'un seul compte (`Sidyvision`), et GitHub interdit d'approuver sa propre PR :
  la condition était **inatteignable par construction**. Toute fusion passait donc
  par `--admin` — la PR #20 comprise. Une protection qu'on est structurellement
  obligé de contourner ne protège plus rien ; elle habitue seulement à passer outre.
- **Changement** : `required_approving_review_count` 1 → **0**, par
  `PATCH /repos/Sidyvision/wiki/branches/main/protection/required_pull_request_reviews`.
- **Ce qui reste en place** (relu après coup, sortie brute) :
  `checks_requis: ["lint"]`, `strict: true`, `force_push: false`,
  `suppression: false`. La PR demeure obligatoire et le lint demeure bloquant :
  c'est la garde qui a une prise réelle. Seule tombe l'approbation que personne ne
  pouvait donner.
- **`enforce_admins: false`** est inchangé et reste la porte de secours.
- **Sauvegarde** de l'état antérieur prise avant modification (hors dépôt,
  scratchpad de session) — le retour se fait par le même point d'API.
- **Portée** : réglage GitHub, hors dépôt. Consigné ici parce que rien dans le
  dépôt n'en porte trace — même classe de dérive que les `SOUL.md` et
  l'orchestrateur de fenêtres.

## [2026-08-31] choura | Hook « contribution de Sidy » versé au Domaine Réservé

Consigne de Sidy : « lorsque je poste dans le salon de la Choura, que ce soit
intégré au tour comme ma contribution sans avoir à mentionner les agents par `@` ».
Rapport de passe complet, points 1 et 2 :
[[atelier/rd/cahiers/2026-08-31_rapport-migration-11-agents-et-contribution-choura]].

- **Écrit** : `meta/projet-unifie/choura/hook-contribution-sidy/` — copie de
  référence du script `/root/.hermes/scripts/choura-contribution-sidy.py` et son
  `README.md` de contrat (événement, filtres, insertion, idempotence).
- **Diagnostic** : le moteur n'exigeait aucune `@mention` — la passerelle Discord
  reçoit tous les messages des salons de `discord.allowed_channels`. Le trou était
  l'**écriture** dans `cycle-AAAA-MM-JJ.md`, seul document que lit un dormant à son
  réveil. La contribution existait dans le salon et n'existait pas dans le tour.
- **Un hook, pas une consigne de prompt** : une consigne dépend de l'obéissance de
  l'agent à chaque tour ; un hook `pre_llm_call` s'exécute en amont du modèle
  (§VIII.2 — fiabilité d'action ≠ fiabilité narrative).
- **Branché sur le seul profil `gardien`** (permanent, il ouvre et clôt le cycle) :
  le brancher partout produirait une entrée par profil éveillé pour un même message.
- **Date de cycle basculant à 12:00 heure de Paris**, comme la rotation des tours —
  avant midi, le cycle courant est celui de la veille.
- **Hors dépôt, non versionnable** : le bloc `hooks:` de
  `/root/.hermes/profiles/gardien/config.yaml` et `hooks_auto_accept: true`
  (nécessaire à l'enregistrement hors TTY, gardien seul). Même classe de dérive que
  les `SOUL.md` — signalée, documentée ici, pas résolue.
- **Carte régénérée** après écriture (`carte-du-depot.py`, 683 fiches).
- **Commit** : 16da41e

## [2026-08-31] infrastructure | Bascule omniroute des 14 profils, réparation du cycle Choura

- **Consignes de Sidy** : « bascule-les tous sur omniroute » (plan Qwen épuisé jusqu'au
  5 septembre), puis « le cycle Choura n'est pas opérationnel, le fichier d'amorce n'a
  pas été réalisé — charge-toi-en à la place du Gardien et programme un nouveau cycle à
  partir de midi, heure de Paris ».

### Bascule omniroute

- ✅ **14 profils + le défaut global** passés à `auto/best-free` / `custom:omniroute`,
  chaque `config.yaml` sauvegardé avant écriture. Vérification : 0 profil hors omniroute.
- 🔧 **`karubi` était une panne muette** : son `custom:qwen` pointait sur un serveur
  **local** (`localhost:8000`) qui n'écoute plus. Sa bascule est une réparation, pas un
  déclassement — et il n'était pas concerné par le plan Qwen épuisé, contrairement à ce
  que son nom de provider laissait croire.
- 🔧 **Global** : `api_mode: anthropic_messages` retiré du bloc `model` — omniroute
  parle `chat_completions`.
- ⛔ **`distribution` avait été tué le matin même à 07:00** par le quota épuisé (le
  journal porte la date de reset, `09-05 12:33 UTC`, qui confirme le dire de Sidy).
- ⚠️ **Hors périmètre, signalé** : `habib-mehdi` et `habib-wendel` appartiennent à
  **d'autres utilisateurs** (`/home/mehdi`, `/home/wendel`), tournent en ce moment et
  sont encore sur le plan Qwen épuisé. Non touchés — ce ne sont pas les douze agents.
- ⚠️ **Réserve de vérification** : le routage effectif de `distribution` et `marketing`
  est **inféré de l'absence de 429**, pas confirmé par une ligne `model=` — leurs seules
  lignes de ce type précèdent la bascule. La prochaine exécution cron tranchera.

### Réparation du cycle Choura

- ⛔ **La panne était écrite dans le dispositif.** Le tour du Gardien portait en dur
  « ouverture/clôture du cycle, **00:00** » alors que son job avait été déplacé à
  **18:00 UTC**. Il ouvrait donc le fichier du jour où il tournait, et tout agent dont
  le créneau tombait après minuit ne trouvait aucun fichier — son prompt lui ordonnant
  alors de signaler et de s'arrêter. `cycle-2026-08-29.md` et `cycle-2026-08-31.md`
  n'ont jamais existé ; les tours du 31 se sont déposés dans le fichier du 30.
- ✅ **Reprogrammation** (`_reprogrammer-choura.py`, 12 profils, 0 erreur) : ouverture
  à **12:00 heure de Paris**, rotation toutes les 2h.
- 🔍 **Le piège évité, et il aurait été invisible** : les expressions cron sont évaluées
  contre `hermes_time.now()`, qui honore la clé `timezone:` — mais **un profil ne charge
  que sa propre `config.yaml`, le global n'est pas fusionné**. Vérifié plutôt que
  supposé : le profil `gardien` rendait `timezone=''` et tournait en UTC. Sans la clé
  posée dans **chacun** des douze, les horaires auraient été décalés de 2h.
  Bénéfice second : le changement d'heure du 25 octobre est absorbé sans retouche.
- 🔍 **Troisième défaut, conséquence de l'ouverture à midi** : le cycle enjambe deux
  jours calendaires, « le fichier du jour » redevient ambigu à minuit. Le cycle est donc
  désormais identifié par sa **date d'ouverture**, avec une règle mécanique inscrite
  dans le prompt (avant 12:00 → le cycle courant est celui ouvert la veille). Sans
  elle, la panne se serait reproduite dès la première nuit.
- ✅ **Amorce déposée** : `cycle-2026-08-31.md` créé, `cycle-2026-08-30.md` clôturé.
  L'entrée d'amorce **n'est pas signée « gardien »** : un tour signé d'un agent qui ne
  l'a pas écrit serait une contribution fabriquée dans un journal append-only. Le
  Gardien tient son propre tour à 12:00, dans ce fichier.
- ✅ Les deux entrées datées du 31 restées dans le fichier du 30 **ne sont pas
  déplacées** (Cmd 10) : sous la nouvelle règle elles sont à leur place — ce qui était
  une anomalie devient conforme.

### Deux constats qui débordent les consignes

- ⛔ **Huit gateways sur douze sont à terre** (`failed` ×7, `inactive` ×1). Le cron
  vivant dans le gateway, ces agents **ne peuvent pas prendre leur tour** : c'est la
  cause des cinq tours manquants du cycle précédent, davantage que le bug de datation.
  Or un gateway pèse **136 Mo** et il ne reste que **704 Mo** : il y a place pour cinq,
  il en faut huit — et sans marge pour le travail des agents (le journal signale déjà
  « system memory pressure is elevated »). **Le Choura à douze ne tient pas en gateways
  permanents sur cette machine.** Décision d'architecture à prendre par Sidy.
- ⚠️ **Erreur de méthode commise, consignée** : lancer `hermes --profile X -z` sur un
  profil dont le gateway tourne **arrête ce gateway** (« stopped by an unexpected
  signal »). C'est ainsi que `distribution` est retombé à 08:38 — de mon fait, en
  voulant vérifier son routage. Une vérification ne doit pas passer par la CLI sur un
  profil vivant.

- 🛑 **RECTIFICATION, le jour même, sur signalement de Sidy (« on a mis quelque chose
  en place pour ça, regarde le R&D »).** Deux erreurs dans ce qui précède :
  1. **Les huit gateways à terre ne sont pas une panne : c'est une décision.** Le
     2026-08-28, après saturation RAM critique et reboot,
     `atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite.md`
     acte l'arrêt et la désactivation délibérés de ces huit gateways exactement
     (`accounting`, `admin-legal`, `ar-music`, `distribution`, `fanzine`, `marketing`,
     `production`, `visual-da`), pour ne garder que `gardien`, `studio`, `publication`.
     Motif : 14 gateways à ~120 Mo plus OmniRoute daemonisé à ~1,6 Go dépassent les
     3,7 Go de l'hôte. **Ne pas les relancer.** J'avais lu un symptôme là où le dépôt
     portait la résolution — la consigne de routine (lire les annales et le R&D avant
     de conclure) aurait suffi à l'éviter.
  2. **Ma proposition d'un cron système en one-shot n'est pas une idée neuve** : la
     même fiche la porte déjà en « compréhension tirée » — « le paradigme *1 profil =
     1 gateway active* doit être révisé : adopter une logique de **gateway à la
     demande** ». Ce n'est donc pas à proposer, c'est à implémenter.
  3. **Régression de ma part, réparée** : j'avais retiré le bloc `providers.custom:qwen`
     de `karubi`, alors que la convention posée le 2026-08-26
     (`2026-08-26_migration-omniroute-quota-qwen.md`) est de **toujours conserver le
     bloc d'origine intact**, seul `model.default`/`model.provider` étant redirigé —
     c'est ce qui rend le retour en arrière gratuit après le reset du quota. Bloc
     restauré ; les 13 profils honorent désormais la convention.
- ✅ **Ce que la même fiche confirme** : les 9 profils métier avaient été laissés sur
  Qwen « dans l'attente du reset naturel du quota… aucune action requise **sauf
  nouvelle demande de Sidy** ». La bascule d'aujourd'hui est cette demande. Et
  `habib-mehdi`/`habib-wendel` y sont **explicitement hors périmètre** — mon
  abstention était la bonne.

- 🛑 **SECONDE RECTIFICATION — j'avais cassé un dispositif existant sans le voir.**
  Sidy : « il n'y a que 3 agents qui maintiennent la veille, les autres se réveillent
  pour leur contribution puis s'éteignent. » Ce dispositif **existe déjà** :
  `/etc/cron.d/choura-orchestrator` appelle chaque minute
  `/root/.hermes/scripts/choura-window-orchestrator.py`, qui démarre le gateway d'un
  profil dormant une heure avant son tour et l'arrête une heure après. Le « gateway à
  la demande » conclu par l'incident du 28/08 était donc **implémenté**, pas seulement
  souhaité — et ma proposition d'un cron système réinventait ce qui tournait déjà.
  - ⛔ **Ce que j'avais cassé** : la table `ORDRE` de l'orchestrateur portait les
    heures **UTC figées** de l'ancienne rotation. En reprogrammant les tours en heure
    de Paris sans connaître ce script, j'ai désynchronisé les neuf fenêtres de leurs
    tours — chaque dormant aurait été réveillé au mauvais moment et **endormi à l'heure
    de sa contribution**. La panne aurait été parfaitement silencieuse : pas d'erreur,
    juste des tours manquants. C'est exactement le symptôme que je venais de
    diagnostiquer, reproduit par ma propre correction.
  - ✅ **Corrigé** : `ORDRE` en heures de Paris, et l'orchestrateur raisonne désormais
    en `Europe/Paris` (`datetime.now(PARIS)`) au lieu d'UTC — ce qui absorbe au passage
    le changement d'heure du 25 octobre, que la version figée aurait décalé d'une heure.
  - ✅ **Versé au dépôt** : `meta/projet-unifie/choura/orchestrateur/` (script, entrée
    cron, README). L'orchestrateur pilotait les douze agents **sans aucune trace dans
    le dépôt** — même classe de dérive que les `SOUL.md` : un composant opératoire que
    personne ne pouvait relire ni corriger depuis le dépôt.
  - ✅ **Contrôle créé** : `orchestrateur/verifier-synchronisation.py` lit les heures
    réelles dans les `jobs.json` et les confronte à `ORDRE`. Sortie du jour :
    **9 dormants, 0 désynchronisé**, crête mémoire **3 permanents + 1 dormant ≈ 544 Mo
    sur 3 819**. Ce contrôle existe parce que le désaccord ne produit aucune erreur
    visible — il rend le silence bruyant.

- **Commits** : `9494520` (et bascule omniroute : configs hors dépôt, sauvegardées sur place)


## [2026-08-31] deploiement | Agent 08 déployé sur le moteur — et le routage était déjà fait

- **Consigne de Sidy** : « déploie l'agent 08 sur le routing omniroute auto/best-free,
  mon Qwen Token Plan est épuisé jusqu'au 5 septembre. »
- ✅ **Routage — rien à changer, c'était déjà en place.** Le profil `publication` porte
  `auto/best-free` sur `custom:omniroute` depuis le **2026-08-26**, et son process a
  redémarré le 2026-08-30 : la config était donc chargée. Le cycle Choura du 2026-08-30
  tournait déjà en `model=auto/best-free`. Les `HTTP 429 token-plan quota exhausted` du
  journal datent des **27-28 août**, avant la bascule. `auto/best-free` vérifié exposé
  par omniroute (511 modèles, `tool_calling: true`).
- ✅ **Prompt déployé** (le go attendu depuis la passe du matin, Cmd 13). Sauvegarde
  hors dépôt, principe → `SOUL.md` (3 628 o, 62 l.), 3 mandats → skills du moteur.
  `--derive` : **publication ✅ synchronisé — premier des douze agents à l'être.**
- **Vérification de bout en bout**, l'agent interrogé en direct :
  « *Sagittarius ; site-orchestration, bibliothecaire, veille-referencement.* »
  L'ancien `SOUL.md` ne portait **aucune** section « Zodiac principle » : la réponse
  prouve le chargement du nouveau principe, la liste prouve la reconstruction de
  l'index des skills.
- 🔍 **Pourquoi un redémarrage était nécessaire** — vérifié dans le code du moteur, pas
  supposé : `load_soul_md()` relit `SOUL.md` sans cache (le principe seul n'aurait rien
  exigé), mais `build_skills_system_prompt()` garde un cache LRU en process **dont la
  clé ne contient ni mtime ni manifeste** — les trois mandats seraient restés
  invisibles jusqu'à la fin de vie du process.
- 🔧 **Donnée fausse du dépôt corrigée** : `bureau/modules/hermes_status.py` affirmait
  en docstring que les agents « tournent en process de fond, pas en service systemd —
  vérifié le 2026-08-15 ». Ce sont des services **systemd user** (`hermes-gateway-<profil>.service`,
  `enabled`) ; `systemctl` ne renvoyait rien parce qu'il était interrogé en portée
  système, sans `--user`. Un redémarrage passe donc par `gateway restart`, supervisé,
  jamais par un kill — ce que la note fausse aurait pu faire croire nécessaire.
- ⛔ **Ce que l'épuisement du Qwen Token Plan laisse en souffrance, hors périmètre de
  cette consigne.** Seuls **3 profils sur 14** sont sur omniroute (`publication`,
  `studio`, `gardien`). Les **9 autres et le défaut global** pointent encore sur
  `qwen3.7-plus` / `custom:qwen`, c'est-à-dire sur le plan épuisé — dont `distribution`,
  qui **tourne en ce moment**, et `karubi` (`qwen3.8-max`). Constat signalé, non
  corrigé : la consigne portait sur l'agent 08.
- ⚠️ **Incident de session à traiter** : en cherchant la clé omniroute, une expansion
  shell mal quotée de ma part a **affiché `OMNIROUTE_API_KEY` en clair** dans la
  session. La clé n'a atteint ni le dépôt ni un tiers, mais elle est sortie de son
  fichier — **à révoquer et régénérer** (CLAUDE.md §VIII.8).
- **Commit** : `cc5c7c9`


## [2026-08-31] archivage | Éclatement modulaire de l'agent 08 — et découverte que le dépôt ne parle pas au moteur

- **Consigne de Sidy** : « intègre `_inbox/` et exécute le plan », en s'instruisant au
  pôle R&D et en lisant « Solve et Coagula » de Guénon pour optimiser le plan.
- ✅ **Éclatement exécuté.** `08-publication-site.md` (270 l., 14 Ko, 3 mandats
  cumulés) devient `08-publication-site/` : `08-principe.md` (invariant) +
  `mandats/{site-orchestration,bibliothecaire,veille-referencement}.md`.
  Découpe **verbatim**, prouvée par un contrôle de conservation :
  **0 ligne perdue · 14 ajoutées, toutes déclarées · 0 fuite de périmètre ·
  0 Unicode invisible.**
- 🛑 **Trois corrections apportées à la fiche `_inbox/` avant exécution** — elle a été
  suivie sur son intention, pas sur sa lettre :
  1. **Sa découpe était une réécriture non déclarée.** Le prompt source est en
     anglais ; le `principe.md` qu'elle donnait en exemple était en français et
     condensait le « Zodiac principle » de 12 lignes à 3. Un changement de fond
     déguisé en réorganisation, et invérifiable par construction. Verdict de Sidy
     avant écriture : iso-contenu.
  2. **Sa validation mécanique ne prouvait rien.** `grep -c "## Mission\|## Scope\|
     ## Guardrails" >= 3` est satisfait par trois titres vides. Remplacée par
     `atelier/rd/outillage/comparer-prompts-hermes.py` (§VIII.2, juge de paix).
  3. **Son routeur n'avait aucun exécutant.** Un `principe.md` disant « tâche X →
     charger `mandats/Y.md` » n'est lu par rien. Or le mécanisme existe nativement :
     les **skills du moteur** (`SKILL.md` à frontmatter, corps tiré à la demande).
     Le routeur n'était pas à écrire.
- ⛔ **Découverte majeure — le dépôt ne parle pas au moteur.** Le prompt réellement
  chargé par un agent est `~/.hermes/profiles/<profil>/SOUL.md`, **hors dépôt git**, et
  aucun chemin déterministe ne l'alimente. Mesure du jour (`--derive`) :
  **12 agents sur 12 en écart.** Publications tourne sur **1 575 o** quand le dépôt en
  documente **14 256** — 203 lignes jamais parvenues à l'agent, dont ses trois mandats
  votés le 2026-08-24 et son principe zodiacal. Studio est le seul synchronisé, à 3
  caractères ZWJ près. **La saturation diagnostiquée à 14 Ko était donc documentaire,
  pas opérationnelle.** Ce n'est pas une réfutation du signal de Sidy — la constriction
  est réelle, elle est simplement ailleurs : non dans le poids d'un fichier, mais dans
  l'absence de chemin entre ce qui est décidé et ce qui s'exécute.
- ⏸️ **Déploiement NON exécuté** (Cmd 13). Procédure, sauvegarde et retour arrière
  écrits dans `08-publication-site/deployer-prompt-agent.md`, présentés à blanc. Il y
  est signalé que le principe (50 l.) est **plus lourd** que le `SOUL.md` actuel
  (30 l.) : le gain est l'isolation de périmètre et la réversibilité, **pas** une
  décharge — ne pas annoncer une décharge qui n'existe pas.
- 🔧 **Références rattrapées** : `meta-index.md` (C1 aurait cassé),
  `bureau/modules/hermes_status.py` (la table `PROFILES` lit la fiche par nom exact —
  sans correctif le tableau de bord affichait « fiche introuvable »), pierre tombale
  `13-librarian-archivist.md`. `verifier-invariants.py` : **sortie strictement
  identique à la référence prise avant la passe**, aucune régression.
- ⚠️ **Signalement de conformité, non corrigé en douce.** `meta/CLAUDE.md` (corollaire
  agentique, art. 1) exige que toute donnée personnelle injectée dans un prompt porte
  sa hiérarchie ontologique **en clair**, qualification *zōsaku* explicite. Or
  `grep -rn "hiérarchie ontologique"` ne renvoie **aucun** des douze prompts : la
  section « Your sign in Sidy's natal chart » énonce une harmonisation en prose sans
  qualifier le joint. Écart **antérieur** à ce chantier. Le corriger à l'intérieur
  d'une migration iso-contenu aurait été la faute même qui a été reprochée à la fiche.
  Passe distincte proposée.
- **Lecture de Guénon — usage formel assumé.** « Solve et Coagula » (*La Grande
  Triade*, chapitre « Solve et Coagula ») : *« dissoudre ce qui était coagulé et, simultanément, coaguler ce
  qui était dissous… les deux aspects d'une seule et même opération »*. Le défaut que
  cela révélait dans la fiche : un *solve* fort, un *coagula* faible — un principe
  réduit à une table d'aiguillage fixe. D'où la décision de **hisser les guardrails et
  les interdits de périmètre au principe**, jamais distribués dans les mandats, pour
  qu'aucun mandat ne puisse les desserrer. Usage **structurel** du texte, relevant de
  la contribution exacte de la machine (Cmd 12) ; le rapprochement doctrinal avec
  qabḍ/basṭ est signalé et **non versé** (Cmd 3) — voir
  `atelier/annales.md`, même date.
- ⚠️ **Deux rectifications portées le jour même, après relecture.**
  1. **L'ACL du sas `_inbox/` est une reconstruction, pas une restauration.** Le
     retrait des dernières fiches a emporté le répertoire ; son ACL propre est perdue
     et irrécupérable. Celle qui a été reposée est déduite de l'ACL d'un *fichier*
     voisin (accès `mehdi` et `wendel`), pas du répertoire : elle est **group-writable
     là où l'originale ne l'était pas** — un fichier déposé y atterrit `-rw-rw-r--+`
     quand les précédents portaient `-rw-r--r--+`. Fonctionnellement suffisant pour le
     dépôt SFTP, mais plus permissif : **à confirmer par Sidy**.
  2. **« *La Grande Triade*, ch. XXII » était une inférence, pas une lecture** — tirée
     du pied de page annonçant le chapitre suivant, dans une autre pagination de la
     source. Le fichier consulté porte en propre « CHAPITRE VI ». Le chapitre est
     désormais cité **par son titre**, qui n'exige aucune inférence (Cmd 5).
- **Commits** : `7b33b7b`, `c7afbc7`, `9264302`, `55f6831`, `829f1c9`, `0e89c13`


## [2026-08-30] git | Fusion dans `main` — et découverte de deux lignées sans ancêtre commun

- **Ordre de Sidy** : « Fusionne les branches ». **Une seule a été fusionnée**, et
  trois ne l'ont pas été — pour les raisons ci-dessous.
- ✅ **Fusionnée** : `claude/passation-instrument-claude-ai-kono6l` → `main`, via la
  **PR #18**, fast-forward strict (14 commits d'avance, 0 de retard). `main` passe à
  `657d79a`. Le push direct sur `main` a été **bloqué** pour la session d'agent
  (comportement voulu) : voie PR + merge API, la même que le 2026-08-29.
- 🛑 **Découverte en préparant la fusion — le dépôt porte DEUX lignées sans ancêtre
  commun.** `git merge-base` renvoie « aucune base commune » entre `origin/main` et
  `claude/instrument-graphic-design-n5d0ic`, `claude/shayegan-transcription-archivage-qt2815`,
  ainsi que le `main` **local** de la session. Comparaison de **contenu** (à deux
  points) : **−26 172 lignes** pour la première, **−17 103** pour la seconde. Ces
  branches ne sont pas « en avance » malgré leurs compteurs (387 et 66 commits) :
  elles portent un **état ancien et plus petit** du dépôt, antérieur à une réécriture
  d'historique. **Les fusionner aurait retiré des dizaines de milliers de lignes.**
  ⛔ Non fusionnées.
- ⚠️ **Erreur de méthode commise, puis corrigée — consignée pour qu'elle serve** :
  un premier test avec `git diff origin/main...origin/<branche>` (**trois points**)
  a rendu un résultat **vide**, que j'ai d'abord interprété comme « contenu déjà
  intégré à `main` » — et rapporté comme tel à Sidy. **C'était faux** : le diff à
  trois points **échoue silencieusement** (`no merge base`) quand les histoires sont
  disjointes, et rend un résultat vide indiscernable d'une égalité. Rectifié avant
  toute opération, par comparaison à **deux points**. **Règle pour ce dépôt : tant
  que les deux lignées coexistent, comparer une branche à `main` toujours à deux
  points.**
- ⚠️ **`fix/corrections-rapports-2026-08-30` — NON fusionnée, décision renvoyée à
  Sidy.** Seule branche à porter du contenu réel dans la lignée de `main`. Mais
  *(a)* son **correctif de sécurité est déjà dans `main`** — le secret HMAC exposé
  en clair y est déjà caviardé, arrivé par une autre voie ; *(b)* ce qui reste est
  pour l'essentiel la **suppression de 39 marqueurs `to-source`**, ce qui est une
  décision **de doctrine et non de forme** (le `to-source` est le signal du Cmd 5,
  en retirer 39 efface 39 signalements en cours) ; *(c)* elle **conflicte** sur trois
  fichiers, dont `registre-problemes.md`, append-only inséré en tête par les deux
  lignées. Conforme à VIGILANCE (« rapporter sans corriger d'office ») et au Cmd 13.
- **Vérification** : `python3 verifier-invariants.py --racine /root/wiki` →
  `0 erreur(s), 0 avertissement(s)` sur le HEAD fusionné.
- **Commit** : (entrée versée après la fusion ; voir PR #18, merge `657d79a`)

## [2026-08-30] briefs | Passation retour — session claude.ai vers session terminal

- **Brief créé** : [[meta/briefs/2026-08-30_passation-claude-ai-vers-terminal]], à la
  demande de Sidy qui repasse côté Claude Code Terminal. L'ancien brief
  [[meta/briefs/2026-08-30_passation-instrument-vers-claude-ai]] est **clos** et
  porte un pointeur vers celui-ci ; les deux sont recensés au `meta-index.md`.
- **⚠️ Avertissement porté en tête du brief, avant tout le reste** : **tout le
  travail est sur la branche `claude/passation-instrument-claude-ai-kono6l`, rien
  n'est sur `main`.** Sept commits. **La fusion appartient à Sidy** — rien n'a été
  fusionné sans ordre.
- **Contenu du point de reprise** : les trois discernements en attente de verdict,
  classés par importance (thèse d'unification · gens d'al-Aʿrāf · couple
  *khafḍ*/*rafʿ*, ce dernier restant le **point bloquant** du rendu) ; l'état vérifié
  du prototype ; les deux rapprochements **refusés** à ne pas rouvrir sans texte ; et
  la règle de méthode dégagée par le dossier (quatre mots français recouvrant des
  réalités distinctes).
- **Collations classées par rendement, et l'ordre est mécanique, non au flair** :
  déterminé sur des index **déjà transcrits au dépôt**. En tête, la **page 104 des
  *Sept Étendards du Califat*** — *khafḍ* **et** *rafʿ* y figurent tous deux ; puis
  **244-245**, où *khafḍ* et *rijāl Allāh* sont adjacents. Avertissement joint : une
  adjacence d'index ne prouve aucun rapport doctrinal, le tableau dit où regarder.
- **Ce que le terminal débloque et que le web ne pouvait pas** : `raw/` (*gitignored*,
  donc invisible depuis claude.ai) — c'est là que se cherchent *Le Roi du Monde* et
  le Paradis terrestre au sommet de la montagne, **cœur du §3 de la thèse** et
  aujourd'hui sans aucun relevé au dépôt. Signalé aussi : les clichés de cette
  session (p. 35, p. 412, p. 857, Râzî ch. XVIII, couvertures) **n'ont pas pu être
  versés** dans `raw/assets/` et restent à déposer côté serveur pour la traçabilité.
- **Vérification structurelle** : `python3 verifier-invariants.py --racine /root/wiki`
  → `0 erreur(s), 0 avertissement(s).` Hygiène Unicode : OK.
- **Commit** : 436287b

## [2026-08-30] briefs | Passation de la session Instrument vers Claude Code (claude.ai)

- **Motif** : budget de session épuisé côté terminal, la matière doctrinale étant
  intégrée et commitée. Ce qui reste est un travail de **rendu sur le prototype**,
  non commencé.
- **Brief créé** : `meta/briefs/2026-08-30_passation-instrument-vers-claude-ai.md`
  (`status: transmis`). Porte : les trois commandes de reprise et l'état attendu
  (**`0 erreur(s), 0 avertissement(s)`** désormais, [A6] ayant été raffiné) ; la
  tâche unique décrite en entier — reporter **six trouvailles** au prototype de
  façon navigable, l'Instrument étant un instrument de *sulūk* ; les quatre
  contraintes de rendu, dont trois désormais **sourcées** ; les sept commits du
  jour ; les six verdicts rendus par Sidy, à ne pas rouvrir ; six points ouverts,
  dont un seul demande une action de Sidy (photographier les pages antérieures à
  la p. 36 de Gloton, pour les degrés 1-10) ; l'inventaire de ce qui reste
  disponible en `raw/` ; et cinq pièges connus.
- **Répercussion au hub** : `meta-index.md`, section « Briefs ».
- **Étanchéité** : liens `meta/` → `doctrinal/` et `meta/` → `atelier/`
  uniquement, sens autorisé (§VI).
- **Commit** : à la ligne suivante du présent lot.


## [2026-08-30] briefs | Passation de la session « réseau subtil » vers le terminal

- **Motif** : `raw/` est inaccessible depuis la session web — le dossier est
  *gitignored* par construction, et les ouvrages de Guénon s'y trouvent. Sidy
  reprend depuis le serveur (`/root/wiki`).
- **Brief créé** :
  `meta/briefs/2026-08-30_passation-session-reseau-subtil-vers-terminal.md`
  (`status: transmis`). Ce n'est pas un résumé de session — les annales de
  circuit le font — mais un **point de reprise** : où en est chaque chantier, et
  ce qui l'attend.
- **Contenu** : les trois commandes de reprise et l'état attendu du vérificateur ;
  **six objets en attente de verdict** de Sidy ; **deux collations sur exemplaire
  physique**, dont la contradiction de numérotation de la table des 38 degrés
  (pp. 91-92 de Gloton) qui **bloque le chantier de l'incommensurable** ; ce que
  l'accès à `raw/` débloque immédiatement (Janus solsticial, ch. II de Shayegan) ;
  l'état de l'outillage avec ses pièges connus (l'option `--repo` du générateur,
  le faux positif [A6], le CDN du prototype) ; les six chantiers ouverts ; et les
  deux documents à lire en premier.
- **Rappel de procédure porté au brief** (§VIII.9) : le traitement de `raw/`
  produit des **fiches candidates dans `_inbox/`**, jamais d'écriture directe
  dans les circuits.
- **Étanchéité** : liens `meta/` → `atelier/` et `meta/` → `doctrinal/`
  uniquement — du sensible vers le neutre, sens autorisé (§VI). Aucun contenu
  `meta/` copié ailleurs.
- **Répercussion au hub** : `meta-index.md`, section « Briefs ».
- **Validation mécanique** : `verifier-invariants.py --racine /home/user/wiki`
  → `0 erreur(s), 1 avertissement(s)` ([A6], faux positif documenté).
- **Commit** : à la ligne suivante du présent lot.

---

## [2026-08-29] personnel | mise à jour | Rêve géants/Paris — liens vers les discernements Axe du Monde et Octogone/Barzakh

`meta/personnel/2026-06-20_reve-geants-paris.md` complétée : l'octogone
(mosaïque/vitraux) et le *quṭb* du rêve, notés en 2026-06-20 comme
insuffisamment développés pour une page dédiée, ont depuis reçu leur
instruction doctrinale complète (`doctrinal/discernement/2026-08-29_axe-du-monde-doctrine-transversale.md`,
`doctrinal/discernement/2026-08-29_octogone-monde-intermediaire-barzakh.md`),
sans lien conscient avec le rêve au moment de la lecture qui les a produites.
Liens ajoutés en sens autorisé (`meta/` → `doctrinal/`), aucune modification
côté `doctrinal/`.

## [2026-08-28] maintenance | Suppression du wiki-manifest.json racine (doublon périmé)

- **Contexte** : suite de la session de corrections de dérive (entrée
  précédente, commit 88d3253) — signalement n°1 (« wiki-manifest.json à la
  racine est un doublon périmé ; à supprimer ou déprécier ») tranché par
  verdict explicite de Sidy : « Yes you can delete the stale file ».
- **Action** : `git rm wiki-manifest.json` (356 lignes). Le manifeste vivant
  vit en `atelier/rd/instrument/wiki-manifest.json` (schéma v0.2.5, régénéré
  le 2026-08-25) ; le fichier racine datait du 2026-08-03 (schéma v0.2.1) et
  aucun script ne le visait — `generer-manifeste.py` écrit en
  `atelier/rd/instrument/`, `bureau/config.py` (`INSTRUMENT_MANIFEST`) lit ce
  même chemin, `instrument_status.py` ne lit que `instrument-donnees.yaml`.
  Références vérifiées sur `.md`, `.py`, `.sh`, `.json` : aucune ne pointe le
  chemin racine.
- **Cmd 10** : suppression autorisée par verdict humain explicite ; le
  fichier reste récupérable dans l'historique git (dernier commit le
  touchant : 5c43d49).
- **Contrôle** : `python3 verifier-invariants.py --racine /root/wiki` →
  `0 erreur(s), 17 avertissement(s)` — identique à l'exécution de référence.
- **Commit** : 1588bb7

## [2026-08-28] maintenance | Corrections de dérive du protocole (table Karūbī, arbre §II, historique migré, meta-index, README)

- **Contexte** : première session du moteur Qoder en poste INTÉGRATION (Cmd 14) ;
  revue du protocole à la demande de Sidy, verdict « apply all suggested
  corrections ». Six corrections de dérive appliquées, aucune modification de
  fond du protocole.
- **meta/CLAUDE.md** : ligne `Wendel Nazaire | Hassan` ajoutée à la table de
  correspondance Karūbī (instance G1 générée le 2026-08-21, présente au
  registre et dans `transmissions/` mais absente de la table ; `date_remise`
  encore vide — remise en attente).
- **CLAUDE.md (racine)** : historique des révisions du préambule (environ
  90 lignes) migré vers `meta/protocole-archives/changelog-CLAUDE.md`
  (append-only, marqueur `<!-- INSERTION: EN-TÊTE -->`) ; le protocole
  conserve un en-tête de statut court (dernières révisions + pointeurs
  d'archive). Arbre du §II complété : `README.md`, `Graphe/`,
  `carte-du-depot.py`, `verifier-invariants.py`, `graphe-cartographie.json`,
  sous-dossiers `meta/` manquants (`personnel/`, `genealogie/`, `journal/`,
  `briefs/`). Rév. portée à 2026-08-28.
- **Guide de déploiement** `verifier-invariants.py` : déplacé de la racine
  (fichier orphelin hors circuit, nom à espaces contraire à la nomenclature
  §III) vers `meta/2026-07-27_guide-deploiement-verifier-invariants.md`.
- **meta-index.md** : `karubi-wendel` ajouté aux transmissions, section
  `briefs/` créée, fiches de premier niveau manquantes recensées
  (bibliotheque-physique TOMBSTONE, philosophie-sashimono,
  plan-fiche-discernement-septenaire-transversal), renvoi périmé §V.c
  corrigé vers `meta/CLAUDE.md`.
- **meta-annales.md** : en-tête de l'entrée du 2026-08-25 (Signalement lot
  bibliothèque Tilak vers Hermes) restauré — le corps était présent sans
  son en-tête greppable, perdu à l'insertion du 2026-08-27 (commit d09cc88).
- **README.md (racine)** : réécrit — il décrivait la structure
  pré-Restauration (`wiki/entities`, `wiki/concepts`, `schema/`), supprimée
  depuis le 2026-06-11.
- **Signalements (rapportés sans correction d'office, verdict Sidy attendu)** :
  (1) `wiki-manifest.json` à la racine est un doublon périmé — généré le
  2026-08-03 (schéma v0.2.1) alors que le manifeste vivant vit en
  `atelier/rd/instrument/wiki-manifest.json` (v0.2.5, 2026-08-25) et
  qu'aucun script ne vise la racine ; à supprimer ou déprécier.
  (2) `meta/protocole-archives/CLAUDE.md.bak-2026-08-22-pre-deplacement-
  bibliotheque` conservé tel quel — référencé nommément dans des entrées
  d'annales append-only (`atelier/annales.md` 2026-08-22/23), un renommage
  créerait des références pendantes.
  (3) Orthographe « Bouzouida » (meta-index) vs « Bouzouïda »
  (meta/CLAUDE.md) — variante sans enjeu, laissée en l'état.
- **Contrôle** : `python3 verifier-invariants.py --racine /root/wiki` →
  `0 erreur(s), 17 avertissement(s)` — identique à l'exécution de référence
  d'avant correction ; aucun avertissement nouveau introduit.
- **Commit** : 88d3253

## [2026-08-27] projet-unifie | Choura : premier cycle wiki + câblage cron réel (12 profils Hermes)

- **Contexte** : verdict Sidy du 2026-08-27 sur
  [[meta/projet-unifie/proposition-cycle-consultation-choura-2026-08-27]] —
  exécution effective complète (wiki + infrastructure vivante), portée
  précisée : intégration des jobs cron préexistants (« unifier le tout »),
  puis salon de livraison précisé par Sidy (« général »).
- **Wiki** : `meta/projet-unifie/choura/cycle-2026-08-28.md` créé (premier
  cycle, marqueur `QUEUE`, gabarit d'entrée, règle d'affinité et clause
  anti-remplissage rappelées). Script `_ajouter-jobs-choura.py` conservé
  pour traçabilité (Cmd 9), non destiné à être relancé.
- **Infrastructure vivante** (`/root/.hermes/profiles/<role>/cron/jobs.json`,
  hors wiki, hors dépôt git) : job `cycle-choura` ajouté aux 12 profils de
  rôle (gardien, ar-music, visual-da, production, admin-legal, accounting,
  distribution, marketing, publication, studio, fanzine, commerce), cadence
  2h, ordre zodiacal, tous les jobs préexistants préservés intacts. `deliver`
  câblé sur `discord:1534857297321394248` (salon « général », guilde
  Label-Agent). Les 12 gateways ont été redémarrés individuellement
  (`hermes gateway restart`) pour prendre en compte les nouveaux jobs — PID
  renouvelés, statut vérifié `gateway list`.
- **Incident mineur corrigé au passage** : le script de câblage avait
  réintroduit des caractères ZWJ (U+200D) dans les prompts injectés — nettoyé
  sur le script, le fichier de cycle, `UPDATES.md`, et rétroactivement sur
  les 12 `jobs.json` déjà déployés (Cmd 15, hygiène Unicode).
- **Commit** : 1213c04

## [2026-08-25] projet-unifie | Signalement lot bibliothèque Tilak vers Hermes (rôle 08, mandat 2)

- **Contexte** : nouveau lot photographié (17 vues, `raw/Origine Polaire de la
  tradition Védique/`) — couverture et table des matières déjà transcrites
  directement (voir `atelier/annales.md`, entrée du même jour). Reste l'index
  alphabétique p.367-380 (IMG_0081-IMG_0088), à traiter sous le mandat 2
  (Librarian-Archivist) porté par la position 08 depuis le 2026-08-24.
- **Action** : ajout du lot Tilak à la section « Ordre des lots » de
  `hermes-prompts/08-publication-site.md`, avec périmètre exact précisé
  (uniquement IMG_0081-0088 ; IMG_0071-0072 déjà traités hors mandat ;
  IMG_0073-0080 hors périmètre) et métadonnées d'ouvrage pour le frontmatter.
- **Commit** : a56b603

## [2026-08-24] realignement | Crons Publication (08), Gardien (10), Studio (09) — ordres exécutés

- **Ordre exécuté** : `_inbox/ordre-cron-frontmatter-veille-08.md` (déposé dans
  l'entrée précédente, commit a32b1a5). Trois actions.
- **Action 1 (exécutée)** : cron créé sur profil `publication`, job
  `veille-referencement-investigation-08` (id `ad3152b237bb`), schedule
  `0 11 * * *`, deliver `#infrastructure` (`discord:1536564394690084925`),
  workdir `/root/wiki`. Prompt unifié : frontmatter conformity (§A) +
  investigation documentaire (§B). Le profil `librarian-archivist` n'existait
  pas côté serveur (déjà fusionné) — pas d'écart.
- **Action 2 (écart trouvé, résolu)** : le cron Gardien
  (`investigation-doctrinale-gardien`, id `431fcacadca2`) exécutait une
  fonction C (investigation documentaire sur `sources_count: 0`) qui n'était
  pas prescrite par la fiche 10. La fiche 10 prescrit la fonction A (veille
  protocole / doctrine du don). Verdict Sidy : le prompt Gardien est
  réaligné sur A-only (veille protocole label), renommé
  `veille-protocole-gardien`. La fonction C est transférée à Publication (08)
  comme partie intégrante de son troisième mandat unifié. Veille spirituelle
  (B) : en suspens, aucun mandat cron attribué à ce stade.
- **Action 3 (exécutée)** : le §1 de Studio (`verifier-invariants.py`) retiré
  de `monitoring-infrastructure-quotidien` (id `41dc3e7e492c`, profil
  `studio`). Studio recentré sur la R&D engagée (volet R&D rendu
  inconditionnel, analyse des 5 entrées récentes du registre-problèmes,
  synthèse 3-5 pistes prioritaires). La fonction frontmatter/investigation
  est désormais propriété exclusive de Publication (08).
- **Fiches mises à jour** : `08-publication-site.md` (third mandate réécrit
  pour refléter l'unification §A+§B et le transfert de C depuis le Gardien),
  `10-protocol-guardian.md` (section « Cron mandate » réécrite : realignement
  documenté, prompt serveur pointé, fonction C cédée à 08).
- **État final des crons quotidiens** :
  - Publication (08) — `veille-referencement-investigation-08`, 11:00 UTC,
    frontmatter + investigation documentaire (dépôt entier)
  - Studio (09) — `monitoring-infrastructure-quotidien`, 12:00 UTC,
    cartographie + non-trackés + cohérence infrastructure + R&D engagée
  - Gardien (10) — `veille-protocole-gardien`, 12:30 UTC, veille doctrine
    du don / protocole label (fiches label/ modifiées)
- **Rappel** : la veille spirituelle (B — doctrinal/ au sens transmission
  spirituelle, Naqshbandiyya/Tijaniyya) reste sans mandat cron attribué.
  À trancher lors d'un prochain chantier.

## [2026-08-24] cron + revue | Mandat frontmatter veille (position 08) précisé, Gardien documenté, ordre déposé en sas

- **Contexte** : suite de la fusion du rôle 13 (entrée précédente). Verdict
  Sidy : cron quotidien 11:00 UTC, portée **l'ensemble des fichiers du
  dépôt** (pas seulement le périmètre propre à la position 08) ; demande de
  vérifier si les jobs Studio (09) et Gardien (10) appellent aussi une
  correction (notion ontologique ou autre).
- **Corrigé** : `08-publication-site.md`, section « Third mandate » — cadence
  11:00 UTC (au lieu de 12:45 proposé), portée élargie au dépôt entier,
  chevauchement avec le §1 du job Studio signalé explicitly (non résolu,
  laissé au verdict de Sidy) plutôt que corrigé silencieusement.
- **Revue « notion ontologique »** : les sections « Zodiac principle » +
  « Your sign in Sidy's natal chart (harmonization context) » des fiches 09 et
  10 portent déjà la hiérarchie principe/détermination individuelle exigée par
  le corollaire agentique (`meta/CLAUDE.md`) — aucune correction nécessaire de
  ce côté.
- **Écart trouvé et documenté** : `10-protocol-guardian.md` ne documentait pas
  son propre cron (`investigation-doctrinale-gardien`, actif depuis avant ce
  contrôle) alors que `09-studio-sound-engineer.md` documente le sien. Section
  « Cron mandate » ajoutée, sans reconstituer le prompt réel non retrouvé dans
  le dépôt (Cmd 12 — pas de fabrication).
- **Déposé en sas** : `_inbox/ordre-cron-frontmatter-veille-08.md` — ordre
  opérationnel à l'attention d'une session Hermes CLI avec accès serveur (Cmd
  13, geste hors périmètre d'une session git seule) : création du cron,
  réconciliation du cron Gardien, signalement de la redondance Studio pour
  verdict Sidy. `_inbox/UPDATES.md` créé en conséquence.
- **Vérification mécanique** : `verifier-invariants.py` → 0 erreur ; scan
  Unicode (Cmd 15) propre sur les 4 fiches touchées.
- **Commit** : a32b1a5

## [2026-08-24] fusion | Rôle Librarian-Archivist (13) fusionné dans la position 08

Sur verdict de Sidy, le rôle Librarian-Archivist (ouvert le 2026-08-22, jamais
activé — section natal chart restée en brouillon) est fusionné dans
`meta/projet-unifie/hermes-prompts/08-publication-site.md` (« Second mandate »)
plutôt qu'ouvert comme treizième position, pour préserver la structure des
douze rôles. Motif : aucune des douze fonctions n'a de recoupement de domaine
avec le catalogage de bibliothèque (toutes bâties autour des opérations du
label) ; le rapprochement se justifie par l'éthos (« zero editorial initiative
BY DESIGN », déterministe, validation humaine avant tout acte final) — même
précédent que le mandat de veille infrastructure logé sur la position 09
(2026-08-16). Un troisième mandat (cron de veille « frontmatter », dans la
dynamique des crons Studio/Gardien) est proposé dans le même geste — cadence
et canal à confirmer par Sidy, création effective du job hors périmètre de
cette session (Cmd 13, geste serveur).
`meta/projet-unifie/hermes-prompts/13-librarian-archivist.md` conservé en
tombstone `deprecated` (Cmd 10). `meta-index.md` mis à jour.

- **Commit** : 615ee0f

## [2026-08-22] sortie de domaine | `bibliotheque-physique.md` → `atelier/rd/bibliotheque/`

Sur verdict de Sidy, le catalogue de la bibliothèque physique quitte le Domaine
Réservé pour `atelier/rd/bibliotheque/catalogue-bibliotheque.md`. Tombstone
`deprecated` conservé sur place (Cmd 10). Motif : un catalogue d'ouvrages
disponibles au travail n'est pas un fait personnel ; maintenu en `meta/`, il
était de surcroît inatteignable, aucun circuit ne pouvant pointer vers le
Domaine Réservé. L'étanchéité n'est pas relâchée : `doctrinal/` ne lie toujours
pas vers `atelier/`, la consultation prévue par §VII reste humaine et sans
wikilink.

Écriture également de `meta/projet-unifie/hermes-prompts/13-librarian-archivist.md`
— rôle bibliothécaire-archiviste, absent des douze rôles existants. Points
d'arrêt `clarify` non contournables, contrôle Cmd 15 en amont (colonnes de
script séparées, pour supprimer la cause des marques bidi plutôt que les
nettoyer après coup), interdiction de transcrire les définitions d'un glossaire.

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
