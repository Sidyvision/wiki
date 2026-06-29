---
title: "Compte-rendu — Premier test GPU cloud d'Ornith-1.0-9B (RunPod, 2026-06-29)"
type: meta
tags: [outillage, projet-claude-ai, infrastructure, ornith, vllm, gpu-cloud, runbook, resultats]
created: 2026-06-29
updated: 2026-06-29
---

# Compte-rendu — Premier test GPU cloud d'Ornith-1.0-9B (RunPod, 2026-06-29)

> Session menée en suivant `05-runbook-test-ornith-gpu-cloud.md`. Le test a globalement
> **réussi** (mécanisme de comparaison validé, selftest PASS), mais s'est arrêté avant la
> conclusion du cycle complet `prepare → compare` sur une anomalie de cohérence observée
> chez Ornith, à reproduire et investiguer. Document à lire avant de reprendre le test.

## 1. Résumé exécutif

- **Pod GPU loué et configuré avec succès** : RTX A6000 (48 Go VRAM) sur RunPod, image
  `vllm/vllm-openai:latest`, Ornith-1.0-9B chargé et fonctionnel.
- **Tunnel SSH Hetzner ↔ GPU monté et validé** : Claude Code sur le serveur Hetzner peut
  parler à vLLM sur le GPU distant comme s'il était en local.
- **Claude Code branché sur Ornith avec succès**, après résolution de deux blocages non
  anticipés par le runbook initial (authentification, taille de contexte — détails §4).
- **Ornith a démontré une boucle agentique fonctionnelle** : lecture de fichiers, recherche
  de motifs, exécution de commandes shell, compréhension fidèle de documents longs
  (`CLAUDE.md`, `ornith-test.sh`).
- **`ornith-test.sh selftest` : PASS (8 ✓ / 0 ✗)** — le mécanisme de comparaison golden/sandbox
  lui-même est validé.
- **Anomalie observée pendant `prepare`** : une réponse d'Ornith a mêlé du texte incohérent
  (fragments en russe sans rapport, fuite d'une balise `</think>` dans la sortie visible,
  syntaxe cassée en fin de message). Le test a été interrompu par prudence avant `compare`,
  sans tirer de conclusion sur la fiabilité d'Ornith à partir d'un seul incident.

## 2. Architecture finale validée

| Composant | Valeur |
|---|---|
| Fournisseur | RunPod — **Pods** (pas Serverless ; le mode Serverless ne convient pas, voir §4.1) |
| GPU | 1× RTX A6000, 48 Go VRAM, 50 Go RAM, 8 vCPU |
| Image | `vllm/vllm-openai:latest` |
| Container disk | 50 Go |
| Volume persistant | 50 Go, monté sur `/workspace` |
| Coût observé | ≈ 0,50 $/h |
| Modèle | `deepreinforce-ai/Ornith-1.0-9B` |
| Contexte final retenu | **`--max-model-len 131072`** (131072 — voir §4.3 pour la justification) |

### Commande de démarrage finale (Container start command, overrides RunPod)

```
deepreinforce-ai/Ornith-1.0-9B --served-model-name Ornith-1.0-9B --host 127.0.0.1 --port 8000 --max-model-len 131072 --gpu-memory-utilization 0.90 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser qwen3_xml --reasoning-parser qwen3 --trust-remote-code
```

### Variables d'environnement du conteneur (gérées par RunPod)

- `VLLM_API_KEY` = `sk-<ID-du-pod>` (auto-généré par RunPod)
- `HF_HOME` = `/workspace/huggingface` (cache HF sur le volume persistant, pour ne pas
  retélécharger les ~19 Go du modèle à chaque test)

### Ports

- **TCP exposé : `22` uniquement.** Le port `8000` (vLLM) n'est **jamais** exposé
  publiquement — accès uniquement via tunnel SSH depuis le Hetzner, conformément au
  principe de sécurité du runbook.
- ⚠️ **Le port externe associé au `22` change à chaque redémarrage du Pod.** Toujours
  vérifier l'onglet **Connect → Direct TCP ports** après un restart avant de relancer un
  tunnel.

## 3. Procédure de connexion (à refaire après chaque redémarrage du Pod)

1. **L'image `vllm/vllm-openai` ne contient pas de serveur SSH.** Après chaque démarrage
   ou redémarrage du conteneur, il faut le réinstaller à la main :
   ```bash
   # Se connecter via le proxy RunPod (fonctionne même sans sshd dans le conteneur) :
   ssh <pod-id>-<hash>@ssh.runpod.io -i ~/.ssh/id_ed25519

   # Puis, dans le conteneur :
   apt update && apt install -y openssh-server
   mkdir -p ~/.ssh && chmod 700 ~/.ssh
   echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMRYQBrXxC3g09bKvLwdWWdZacaQR+k+UPjelSaTR7vy sidyvision-wiki" >> ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/authorized_keys
   service ssh start
   ```
2. **Vérifier le port externe actuel** (Connect → Direct TCP ports, format `IP:PORT → :22`).
3. **Monter le tunnel depuis le serveur Hetzner** (port à adapter à chaque fois) :
   ```bash
   ssh -N -f -L 8000:127.0.0.1:8000 root@<IP> -p <PORT> -i ~/.ssh/id_ed25519
   ```
4. **Vérifier le tunnel** :
   ```bash
   export VLLM_API_KEY="sk-<ID-du-pod>"   # à récupérer via : cat /proc/1/environ | tr '\0' '\n' | grep VLLM_API_KEY, depuis le conteneur
   curl -s http://localhost:8000/v1/models -H "Authorization: Bearer $VLLM_API_KEY"
   ```
5. **Configurer et lancer Claude Code** (dans le même shell, pour que les variables
   persistent) :
   ```bash
   export ANTHROPIC_BASE_URL=http://localhost:8000
   export ANTHROPIC_API_KEY=$VLLM_API_KEY
   export ANTHROPIC_MODEL=Ornith-1.0-9B
   export ANTHROPIC_SMALL_FAST_MODEL=Ornith-1.0-9B
   export ANTHROPIC_DEFAULT_HAIKU_MODEL=Ornith-1.0-9B
   export DISABLE_PROMPT_CACHING=1
   export ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"
   claude
   ```

> ⚠️ Ces variables ne survivent pas à l'ouverture d'un nouvel onglet/terminal — elles
> doivent être réexportées dans **chaque** nouveau shell utilisé pour lancer `claude`.

## 4. Écarts par rapport au runbook initial (`05-…`) — à corriger pour la prochaine fois

### 4.1 Serverless vs Pod

Le premier réflexe sur RunPod a été d'utiliser le template **Serverless vLLM** — qui ne
convient pas : pas d'accès SSH direct, architecture différente (endpoint RunPod authentifié,
pas de tunnel local). Il faut bien choisir **Pods → Deploy a Pod**, pas Serverless.

### 4.2 Authentification Claude Code ↔ vLLM (blocage majeur, non documenté dans le runbook)

vLLM (même en exposant une API « compatible Anthropic ») n'authentifie qu'via le header
`Authorization: Bearer <clé>`. **Claude Code envoie nativement `x-api-key`**, jamais
`Authorization`, ce qui produit un `401 Unauthorized` systématique, quelle que soit la
validité de la clé.

**Solution trouvée** : forcer Claude Code à ajouter le bon header via la variable
`ANTHROPIC_CUSTOM_HEADERS` :
```bash
export ANTHROPIC_CUSTOM_HEADERS="Authorization: Bearer ${VLLM_API_KEY}"
```
Confirmé efficace via les logs de debug Claude Code (`has Authorization header: true` après
correction, contre `false` avant). **À ajouter explicitement dans `05-runbook-…md`.**

### 4.3 Taille de contexte insuffisante (blocage majeur, sous-estimé dans le runbook)

Le runbook recommandait `--max-model-len 32768`, jugé « largement suffisant ». En pratique :
- Le seul **prompt système** de Claude Code (outils, instructions) pèse déjà
  **~107 000 caractères (~27 000 tokens)**.
- Avec des tâches de lecture de fichiers réels du dépôt, certains tours ont atteint
  **142 800 tokens en entrée** sur un seul appel.
- `32768` → erreur 500 immédiate. `65536` → toujours insuffisant sur les tâches réelles.
- **`131072` (128K) a fonctionné** pour les tests menés (lecture de fichiers, scripts).

**Recommandation** : fixer `--max-model-len 131072` comme valeur de départ pour tout test
futur impliquant Claude Code, et surveiller la consommation VRAM réelle (`gpu-memory-utilization`
à 0.90 a suffi sur un GPU 48 Go avec ce contexte, mais à revérifier si on monte encore).

### 4.4 Fragilité de l'infrastructure entre redémarrages

- `pkill -f vllm` est **dangereux** : il cible le PID 1 du conteneur (le process de lancement
  vLLM lui-même), ce qui redémarre tout le conteneur (perte du `sshd` installé manuellement,
  retour à la configuration d'overrides sauvegardée). **Ne plus utiliser cette commande** —
  passer par les overrides + bouton « Restart Pod » de RunPod pour tout changement de
  configuration vLLM.
- Chaque redémarrage change le port TCP externe SSH — toujours revérifier avant de relancer
  un tunnel.
- La clé SSH doit être enregistrée dans **Settings → SSH public keys** (réglages de
  *compte*, pas dans la fiche du Pod) pour que le proxy `ssh.runpod.io` fonctionne.

## 5. Résultats des tests fonctionnels

| Test | Résultat |
|---|---|
| Lecture + résumé fidèle de `CLAUDE.md` | ✅ Réussi (recherche, lecture, commande shell, réponse correcte) |
| Lecture + résumé fidèle de `meta/projet-unifie/ornith-test.sh` (script long) | ✅ Réussi, résumé technique précis (but, sandbox isolé, 3 modes) |
| Diagnostic d'une erreur de chemin (`No such file or directory`) | ✅ Diagnostic correct et autonome après reformulation de la demande |
| `bash meta/projet-unifie/ornith-test.sh selftest` | ✅ **PASS — 8 ✓ / 0 ✗** |
| `prepare` (préparation du bac à sable + chargement `_inbox/`) | ⚠️ Exécuté sans erreur technique, mais réponse finale du modèle **incohérente** (cf. §6) |
| `compare` | **Non exécuté** — test interrompu par prudence après l'anomalie en `prepare` |

## 6. Anomalie observée (à signaler, sans surinterpréter)

Lors de l'étape `prepare`, après plusieurs tours de conversation cumulés dans la même
session Claude Code, la réponse finale d'Ornith a mêlé :
- des fragments de texte en russe, sans rapport apparent avec le contexte
  (« длине препаратизации/приемущество ») ;
- une fuite visible de balise `</think>` (normalement interne au raisonnement caché du
  modèle) dans le texte de réponse affiché ;
- une faute de frappe (« Sanbox » au lieu de « Sandbox ») et une phrase finale
  syntaxiquement incohérente.

**Aucune conclusion n'a été tirée sur la fiabilité générale d'Ornith à partir de cet
incident isolé.** Deux hypothèses à départager lors d'une prochaine session :
1. Dérive liée à l'**accumulation de contexte** sur une session longue (plusieurs tours
   successifs, contexte de conversation chargé) plutôt qu'une limite structurelle du modèle.
2. Limite réelle du modèle 9B sur une tâche agentique complexe et longue.

## 7. Recommandations pour la suite

1. **Relancer le cycle `prepare → compare` dans une session Claude Code toute neuve**
   (pas de reprise d'une session déjà longue), pour isoler si l'anomalie du §6 est liée à
   l'accumulation de contexte.
2. **Mettre à jour `05-runbook-test-ornith-gpu-cloud.md`** pour intégrer les correctifs
   des §4.2, 4.3 et 4.4 (header d'authentification, contexte minimal réaliste, mise en garde
   sur `pkill`).
3. Envisager un **script d'installation automatique** (réinstallation `sshd` + clé + service)
   à exécuter en une seule commande après chaque redémarrage du Pod, pour réduire le risque
   d'erreur humaine répétée sur cette étape manuelle.
4. **Vérifier l'état de facturation du Pod** après cette session — si le test n'est pas
   repris immédiatement, arrêter ou supprimer l'instance RunPod pour stopper les coûts.
5. Aucune écriture n'a atteint le vrai dépôt `/root/wiki` au cours de cette session : tout
   s'est déroulé sur le Pod GPU distant et dans le bac à sable isolé du script de test
   (conformément à sa conception). **Rien à committer côté dépôt suite à cette session.**
