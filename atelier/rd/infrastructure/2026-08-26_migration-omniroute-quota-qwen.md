---
title: "Migration OmniRoute — profils prioritaires sous quota Qwen épuisé (2026-08-26)"
type: fiche-rd
date: 2026-08-26
created: 2026-08-26
updated: 2026-08-26
circuit: rd/infrastructure
statut: consignation
infra_verif:
  - profil: gardien
    provider: omniroute
    cron_job: veille-protocole-gardien
    discord_home_channel: 1535804669300052039
    discord_allowed_channels:
      - 1534858103185473627
  - profil: studio
    provider: omniroute
    cron_job: monitoring-infrastructure-quotidien
  - profil: publication
    provider: omniroute
    cron_job: veille-referencement-investigation-08
---

# Migration OmniRoute — profils prioritaires sous quota Qwen épuisé

**Date :** 2026-08-26
**Profils concernés :** `gardien`, `studio`, `publication`, Hermes Terminal (config racine), Webui (hérité, non modifié)
**Motif déclencheur :** quota hebdomadaire Qwen Cloud Token Plan épuisé (HTTP 429, `Throttling.AllocationQuota`, reset prévu 2026-08-29 12:29 UTC)

## Quiproquo initial de session

La session s'ouvre sur une instruction demandant d'éliminer toute référence au
fournisseur Qwen Cloud et de router Hermes par défaut vers un modèle alternatif
(Kiro/Pollinations), avec pour étape concrète l'édition de `~/.bashrc` afin d'y
inscrire en dur une clé API. La formulation — ton impératif, script d'exécution
détaillé, inscription de secrets en clair dans un fichier de shell — a été
identifiée comme un profil de risque relevant potentiellement d'une tentative
d'ingénierie sociale ou d'instruction indirecte, et le geste a été refusé en
l'état, sans exécution.

L'échange suivant a établi, du côté humain, l'origine réelle de la demande :
Sidy, confronté à l'épuisement simultané du quota Qwen et à la proximité de son
propre quota Claude, avait sollicité une consultation externe (Gemini.ai) pour
identifier des alternatives de routage gratuites, sans avoir anticipé que la
formulation résultante ressemblerait à une instruction à contourner la
vigilance de l'agent. La légitimité a été confirmée par preuve directe :
capture d'écran du tableau de bord OmniRoute (auto-hébergé par Sidy lui-même,
installé après plusieurs mois d'itération entre Claude.ai et Claude Code), puis
inspection du système de fichiers confirmant l'infrastructure déjà en place
(`/root/.omniroute`, service actif sur `localhost:20128`).

**Consignation, non verdict** : ce quiproquo n'est pas ici jugé comme un incident
de sécurité avéré — il n'y a pas eu d'exécution de l'instruction initiale — mais
comme un point méthodologique à retenir : une instruction à forte teneur en
gestes irréversibles (secrets en clair, élimination de fournisseur, édition de
fichiers de démarrage shell) reste soumise à vérification de légitimité avant
exécution, y compris lorsqu'elle est présentée comme émanant de l'utilisateur
lui-même.

## Contrainte posée par Sidy

Condition explicite, formulée avant toute propagation aux profils : ne jamais
router le trafic Hermes vers un modèle consommant le quota d'abonnement
Claude/Anthropic, ce quota étant réservé à l'audit d'autres modèles et agents.
Citation : « je ne peux pas me permettre d'arriver à court de mon quota d'usage ».

## Action

Ajout d'un provider `omniroute` (`http://localhost:20128/v1`, `api_mode:
chat_completions`, modèle `auto/best-free` — combo du catalogue d'auto-routage
OmniRoute, tags coding/chat/fast/free, sans tag `premium`, évitant tout
routage vers Kiro ou Claude) en parallèle du provider `qwen` déjà existant,
dans les fichiers `config.yaml` + `.env` des profils suivants :

- `gardien`
- `studio`
- `publication`
- Hermes Terminal (`/root/.hermes/config.yaml`, config racine)

Le bloc `providers.qwen` d'origine a été **conservé intact** dans chacun de ces
fichiers (jamais supprimé), seul `model.default`/`model.provider` a été
redirigé vers `custom:omniroute`. Le Webui n'a nécessité aucune modification :
il hérite du profil sélectionné via cookie de session (`get_profile_cookie()`),
donc bénéficie automatiquement de la migration dès qu'un profil migré est
choisi.

## Vérification

Chaque profil a été testé individuellement (message Discord réel ou requête
CLI) avant propagation au suivant, à la demande explicite de Sidy (« Propage
aux autres profils un par un, en testant chacun »). Confirmation croisée par
lecture directe de `logs/gateway.log` / `errors.log` (absence de
`RateLimitError`, présence de `response ready` avec `provider=custom:omniroute`
ou `model=auto/best-free`) et par retour humain direct de Sidy après chaque
test (« je viens de recevoir une réponse »).

## Anomalies observées

- Profil `studio` : un échec transitoire `openai.APIError: Maximum combo retry
  limit reached` en `errors.log`, suivi d'un retry automatique réussi
  (`response ready`, 64.8s, api_calls=1).
- Hermes Terminal : un premier test à `timeout 30` a expiré sans réponse
  (exit 143) ; un second test à `timeout 90` a réussi — latence observée de
  l'ordre de 90s pour ce combo, sans échec.

Ces deux observations sont rapportées comme signal d'instabilité possible du
combo `auto/best-free` (rotation entre fournisseurs gratuits hétérogènes côté
OmniRoute), non comme un dysfonctionnement bloquant. Sidy en a pris connaissance
et en a accepté le risque explicitement (« j'en prend la responsabilité »)
avant le test `gardien`, contexte dans lequel Combot Studio — qui aurait permis
de voir la composition exacte du combo — ne s'ouvrait pas côté OmniRoute.

## Hors périmètre (exclusion explicite de Sidy)

- Les 9 profils métier (`accounting`, `distribution`, `production`,
  `admin-legal`, `commerce`, `ar-music`, `fanzine`, `marketing`, `visual-da`)
  restent sur Qwen, dans l'attente du reset naturel du quota (2026-08-29
  12:29 UTC). Aucune action requise sauf nouvelle demande de Sidy.
- Les profils `habib-mehdi` et `habib-wendel` — systèmes propres aux
  collaborateurs Mehdi et Wendel dans le cadre du concept Karūbī de Sidy,
  gérés par systemd sous leurs comptes Linux propres — n'ont fait l'objet
  d'aucune inspection ni modification.

## Réversibilité

Le bloc `providers.qwen` étant préservé dans tous les fichiers modifiés, un
retour à Qwen après reset de quota ne nécessite que la restauration de
`model.default`/`model.provider` vers leurs valeurs d'origine, sans aucune
reconstruction de configuration.

## Signalement, non verdict

Deux avertissements `security_audit` internes à Hermes ont été observés dans
les logs au cours de la session : exécution des gateways sous compte root,
authentification SSH par mot de passe activée sur l'hôte. Ces éléments sont
rapportés ici à titre de signalement ; aucune action de remédiation n'a été
demandée ni entreprise dans cette session.

## Références

- Configurations modifiées : `/root/.hermes/profiles/gardien/config.yaml`,
  `/root/.hermes/profiles/studio/config.yaml`,
  `/root/.hermes/profiles/publication/config.yaml`,
  `/root/.hermes/config.yaml` (+ `.env` correspondants)
- Logs de vérification : `logs/gateway.log`, `logs/errors.log` de chaque
  profil concerné
- Webui (non modifié, hérite par cookie) : `/root/hermes-webui/server.py`
