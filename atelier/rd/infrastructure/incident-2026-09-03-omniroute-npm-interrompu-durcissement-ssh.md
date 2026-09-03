---
title: "Incident R&D — OmniRoute : mise à jour npm interrompue par un arrêt serveur, et durcissement SSH consécutif (2026-09-03)"
type: fiche-rd
date: 2026-09-03
created: 2026-09-03
updated: 2026-09-03
circuit: rd/infrastructure
statut: consignation
---

# Incident R&D — OmniRoute : mise à jour npm interrompue, et durcissement SSH consécutif

**Date :** 2026-09-03 (14:02–18:00 UTC)
**Composants concernés :** OmniRoute (routeur de modèles, port 20128), Hermes
(WebUI + deux passerelles), sshd, pare-feu hôte
**Rédigé par :** Claude (Opus 5), sur diagnostic direct des logs système et
vérification empirique de chaque correctif

## Contexte

L'opérateur a éteint puis rallumé le serveur (redémarrage à 15:15 UTC). Au
retour, OmniRoute était hors service, et Hermes avec lui — son
`ANTHROPIC_BASE_URL` pointant sur le port 20128 resté muet.

Une mise à jour `npm install -g omniroute` (3.8.49 → 3.8.50) avait été lancée
manuellement à 14:02, soit environ une heure avant l'arrêt.

## Symptômes

`omniroute.service` en boucle de redémarrage, **450 cycles** enregistrés :

```
omniroute.service: Main process exited, code=exited, status=203/EXEC
omniroute.service: Failed with result 'exit-code'
```

Rien n'écoutait sur le port 20128. Les trois services Hermes tournaient
normalement mais sans routeur.

## Diagnostic

`203/EXEC` signifie exécutable introuvable. L'inspection de l'arborescence npm
a révélé une installation figée à mi-parcours :

- `/usr/lib/node_modules/omniroute/` ne contenait plus que `node_modules/` —
  ni `bin/`, ni `dist/`, ni `src/` : le corps du paquet n'avait jamais été
  décompressé ;
- l'ancienne version **3.8.49 était intacte**, garée par npm sous
  `/usr/lib/node_modules/.omniroute-h797OOZa` ;
- le lien `/usr/bin/omniroute` avait disparu, ne subsistaient que les liens
  temporaires `.omniroute-V3Gyy8R0` et `.omniroute-reset-password-1G5uEdc6`.

## Cause

**`npm install -g` n'est pas atomique.** Il déplace d'abord l'ancien paquet
vers un dossier temporaire préfixé d'un point, puis décompresse le nouveau,
puis recrée les liens dans `/usr/bin`. L'extinction du serveur est tombée
**entre la première et la deuxième étape** : ancien paquet déjà retiré, nouveau
pas encore posé, liens détruits.

Le redémarrage automatique de systemd (`Restart=always`) ne pouvait rien y
faire — il relançait un binaire qui n'existait plus, 450 fois.

## Résolution

1. Arrêt du service pour rompre la boucle.
2. Mise de côté (et non suppression) de la 3.8.49 vers
   `/root/omniroute-3.8.49-backup` et de la coquille vers
   `/root/omniroute-install-casse`, afin de préserver un retour arrière.
3. `npm install -g omniroute` → 3.8.50, 1162 paquets, 4 minutes.
4. Démarrage, puis relance des trois services Hermes.
5. Après validation, suppression des deux dossiers de secours : **3,5 Go
   récupérés** (disque de 90 % à 81 % d'occupation).

**Vérification bout en bout** (et non simple constat de processus vivant) :
`omniroute health` → `healthy` ; `omniroute providers test-all` → tous les
fournisseurs à clé passent ; complétion réelle via `auto/best-fast`, routée
vers `openai/gpt-oss-20b`, HTTP 200.

Aucun timer systemd ni cron ne pilote OmniRoute, et `update-notifier` se
contente de signaler les versions sans les installer : **rien ne relancera
seul une mise à jour pendant un arrêt.**

## Découvertes annexes, non liées à la panne

### Fichier d'environnement caviardé

`/root/.omniroute-env.sh` contenait littéralement
`export ANTHROPIC_AUTH_TOKEN= [REDACTED-REVOKE-IF-VALID]` — un outil de
sécurité avait remplacé le jeton, en laissant une espace après le `=`. Le
`source` échouait donc sur `not a valid identifier` et la variable se chargeait
**vide**. Le jeton d'origine est à considérer comme compromis.

**Résolu en fin d'intervention.** L'opérateur a fourni une clé API OmniRoute
(`sk-0125…`), validée contre `/v1/models` (HTTP 200, 878 modèles) puis posée
dans le fichier, désormais en `600` :

```bash
export ANTHROPIC_BASE_URL=http://localhost:20128
export ANTHROPIC_AUTH_TOKEN=sk-…
```

### L'authentification d'OmniRoute dépend de l'endpoint

Erreur de raisonnement commise puis corrigée en cours d'intervention :
`/v1/messages` accepte les requêtes **sans jeton valide** (il échoue plus loin,
sur le nom de modèle), ce qui avait conduit à conclure trop vite que
l'authentification n'était pas appliquée. Or `/v1/models` renvoie `401` sans
clé réelle.

Second point : la clé s'envoie en **`Authorization: Bearer`**, pas en
`x-api-key`. C'est précisément ce que produit `ANTHROPIC_AUTH_TOKEN` dans
Claude Code (`ANTHROPIC_API_KEY` produirait `x-api-key`, qui échoue ici).

Conséquence observable : sans clé, le catalogue live paraissait **vide** ; avec
la clé, il expose **773 modèles**. Le « catalogue vide » n'était qu'un artefact
d'authentification.

### Connexion Claude désactivée puis expirée

La connexion OAuth `claude` était marquée inactive. Sa réactivation
(`omniroute providers edit <id> --active`) a fait passer le catalogue de 773 à
**878 modèles**. Mais un appel réel retourne :

```
[claude] All 1 connection(s) authentication expired — please reconnect
```

Le jeton OAuth a expiré : une réautorisation interactive reste requise
(`/root/reconnecter-claude.sh`). Noter que `providers list` affichait pourtant
`testStatus: active` et `lastError: null` — **l'état déclaré ne vaut pas
preuve, seul l'appel réel tranche.**

Relevé au passage : le fournisseur `cerebras` s'est auto-désactivé sur
`credits_exhausted`.

**Résolu — et l'occasion d'une erreur instructive.** La réautorisation par
l'opérateur n'a pas rafraîchi la connexion existante : elle en a créé une
**seconde**, sous `sidyvision@gmail.com`, laissant l'ancienne
(`56xfmzr7kj@privaterelay.appleid.com`) active mais `expired` — « No refresh
token available ».

Voyant deux connexions actives sous le même fournisseur, j'ai supposé que la
nouvelle était l'intruse et je l'ai désactivée. **C'était l'inverse** :
`sidyvision@gmail.com` *est* le compte d'OmniRoute et de `claude-omni` ; la
connexion `privaterelay` est l'ancienne, périmée. L'opérateur a corrigé, la
connexion a été réactivée aussitôt.

Vérification après coup : `cc/claude-haiku-4-5-20251001` — le modèle exact du
profil `claude-omni` — répond **HTTP 200** avec une complétion réelle.

**Leçon** : deux comptes Claude coexistent sur cette machine. L'appartenance
d'une connexion ne se déduit **pas** de son ancienneté ni de son format
d'adresse. Le seul juge est l'opérateur — à lui demander avant toute
désactivation.

### Comment `claude-omni` s'articule

L'alias est défini dans `/root/.bashrc` :

```bash
alias claude-omni='CLAUDE_CONFIG_DIR=~/.claude/profiles/cc-claude-haiku-4-5-20251001 claude'
```

Il tire sa configuration du `settings.json` **de ce profil** (`ANTHROPIC_BASE_URL`
vers le port 20128, `ANTHROPIC_MODEL=cc/claude-haiku-4-5-20251001`), et **non**
de `/root/.omniroute-env.sh` — lequel ne sert qu'aux shells interactifs. Les
deux chemins sont indépendants : modifier l'un n'affecte pas l'autre.

## Volet sécurité — exposition découverte et refermée

Le diagnostic a mis au jour une exposition antérieure à l'incident :

- OmniRoute écoutait sur `0.0.0.0:20128` (toutes interfaces, IP publique
  `178.105.125.156`), `ufw` inactif, politique `iptables INPUT` en `ACCEPT` ;
- soit **neuf clés fournisseurs** (Gemini, Groq, Mistral, NVIDIA, Cerebras…)
  utilisables par quiconque atteignait le port, aux frais de l'opérateur ;
- en parallèle, **6 659 tentatives d'authentification SSH échouées en 24 h**,
  avec `PermitRootLogin yes`, `PasswordAuthentication yes` et **aucune clé
  publique** dans `authorized_keys` : connexion root par mot de passe face à un
  brute-force permanent.

**Correctifs appliqués :**

1. `ufw` configuré puis activé — `INPUT` en `DROP`, n'autorisant que `22/tcp`,
   tout le trafic sur `tailscale0`, et `41641/udp`. Règles posées **avant**
   activation pour écarter tout verrouillage. Actif au démarrage.
2. Clé publique ED25519 de l'opérateur installée, connexion par clé validée
   (`Accepted publickey ... SHA256:2Jke…jT68`).
3. Durcissement SSH via `/etc/ssh/sshd_config.d/00-hardening.conf` :
   `PasswordAuthentication no`, `KbdInteractiveAuthentication no`,
   `PermitRootLogin prohibit-password`.
4. `systemctl reload ssh` (jamais `restart`) : `NRestarts=0`, sessions
   préservées.

**Vérification empirique :** une connexion forçant le mot de passe reçoit
`Permission denied (publickey)` ; zéro `Failed password` après 17:33:15 ; les
bots tombent désormais en `[preauth]`. Le pare-feu a bloqué des scans de 12 IP
distinctes en 10 minutes.

## Enseignements pour la doctrine R&D

**1. Une mise à jour npm globale est une fenêtre de fragilité.** Pendant
quelques minutes, le paquet n'existe ni dans l'ancienne ni dans la nouvelle
version. N'éteindre le serveur qu'après s'être assuré qu'aucune installation
n'est en cours. Le symptôme à reconnaître : `status=203/EXEC` avec un compteur
de redémarrages qui s'envole.

**2. Déplacer plutôt que supprimer, tant que le correctif n'est pas validé.**
Les `mv` vers `/root/` ont conservé un retour arrière gratuit pendant toute
l'intervention ; les 3,5 Go n'ont été rendus qu'après vérification.

**3. L'ordre des `Include` de sshd est un piège.** `Include
/etc/ssh/sshd_config.d/*.conf` figure **ligne 12**, avant les directives du
fichier principal, et sshd applique la **première** occurrence rencontrée.
`50-cloud-init.conf` imposait `PasswordAuthentication yes` : toute modification
du fichier principal aurait été silencieusement sans effet. D'où le préfixe
`00-` du fichier de durcissement, qui trie avant — et qui résiste aussi à une
régénération de `50-cloud-init.conf` par cloud-init.

**4. Ne jamais conclure sur l'authentification depuis un seul endpoint.** Voir
§ « L'authentification d'OmniRoute dépend de l'endpoint ».

**5. Le repli d'affichage du terminal casse les commandes collées.** Sur iPad,
les commandes longues ont été reçues par bash **avec de vrais retours à la
ligne** aux points de repli (`cp: missing destination file operand`). Pour toute
opération à faire exécuter par l'opérateur : **écrire un script et ne lui faire
taper qu'une commande courte** (`bash /root/durcir.sh`). Corollaire : le
préfixe `!` ne vaut que dans l'invite de Claude Code, jamais dans un shell.

**6. Un script d'opération sensible doit se protéger lui-même.**
`/root/durcir.sh` teste la syntaxe, contrôle la configuration effective, et
**annule tout seul** avant rechargement si l'un des deux échoue. Un
`/root/annuler.sh` symétrique reste disponible.

## Reste à faire

- [x] Poser une clé API OmniRoute valide dans `/root/.omniroute-env.sh`
      *(fait — validée contre `/v1/models`, HTTP 200)*
- [x] Réautoriser la connexion OAuth Claude *(fait — `sidyvision@gmail.com`
      reconnecté, `cc/claude-haiku-4-5-20251001` valide à HTTP 200. Le `401`
      initial venait de l'absence de `--api-key` pour OmniRoute lui-même, non
      de Claude)*
- [ ] Décider du sort de la connexion `56xfmzr7kj@privaterelay.appleid.com`,
      active mais **expirée sans jeton de rafraîchissement** — à réautoriser
      si elle sert encore, à retirer sinon
- [ ] Décider du sort de `cerebras` (crédits épuisés)
- [ ] Vérifier le pare-feu **cloud Hetzner**, distinct du pare-feu hôte
- [ ] Le jeton caviardé étant à considérer comme compromis, envisager la
      rotation des clés fournisseurs exposées avant la pose du pare-feu

## Connexions

- [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]] —
  incident OmniRoute précédent, même composant, cause différente (conflit de port)
- [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] —
  mise en place d'OmniRoute en fallback
- [[atelier/rd/infrastructure/cartographie-routing-infrastructure]]
- [[meta/projet-unifie/03-transition-modele-open-source]] — usage de
  `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN` pour brancher un endpoint local
