---
title: "INF-16 — Runbook : rafale d'entraînement sur RunPod (charge d'entraînement, pas d'inférence)"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, inf-16, runbook, runpod, entrainement, lora, securite]
created: 2026-09-16
updated: 2026-09-16
sources:
  - "https://docs.runpod.io/pods/pricing"
  - "https://docs.runpod.io/accounts-billing/billing"
links:
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/devis-rafale-runpod-2026-09-16]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/eval-jeu-de-taches-2026-09-16]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan]]"
  - "[[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]]"
---

# Runbook — la rafale d'entraînement

> **Statut : écrit, non exécuté.** Ce runbook est le troisième préalable du devis (§5). Il
> décrit une **charge d'entraînement** — pas l'inférence d'un modèle servi. L'antécédent de
> juin 2026 au dépôt portait sur l'inférence (vLLM) ; **ce runbook-ci ne l'étend pas, il
> traite l'autre charge**, et reprend seulement les enseignements opérationnels qui valent
> pour les deux (SSH, tunnel, port non exposé, destruction).
>
> **Mode pédagogique** : chaque étape dit *quoi faire*, *pourquoi*, et *ce qui se passe
> derrière* — pour n'avoir à le redemander à personne.
>
> **Rien ici n'autorise un lancement** : la dépense relève de la porte humaine (Cmd 13).

## 0. Ce qui doit être vrai avant de commencer

| Préalable | État au 2026-09-16 |
|---|---|
| Jeu de données constitué, empreinté | ✅ `/root/sandbox-rd/inf-16-dataset/corpus-souverain.jsonl` — 872 enregistrements, 11,5 Mo, `sha256:c776d5e213814c48…` |
| Jeu d'évaluation émis | ✅ `taches.jsonl` — 13 tâches, fiche source `sha256:e9a635ff10520…` |
| Modèle de base choisi | ⏳ proposé : **Qwen3-8B** (16,38 Go en bf16, 4,10 Go en 4 bits, 144 Kio de cache KV par jeton) |
| Compte RunPod + moyen de paiement | ❌ **inexistant** — c'est l'engagement lui-même. **Forme retenue** : l'agent gère l'installation ; la clé d'API est déposée par Sidy **sur le serveur** (§10) |
| Verdict de Sidy sur la dépense (Cmd 13) | ❌ non donné — l'engagement se matérialise par la création du compte et le dépôt de la clé |
| Charge de référence (U1–U5) | ❌ non arrêtée — elle décide de la **cible**, donc de la recette |

## 1. Choisir le pod

1. **RunPod → « Pods » → Deploy a Pod.** Jamais « Serverless » : le Serverless n'offre ni
   SSH ni tunnel (constat de juin 2026, payé une fois). *Derrière* : un Pod est une machine
   à vous pour la durée ; le Serverless est une file d'exécution sans accès système.
2. **GPU selon le scénario** du devis : A6000 48 Go (sobre) · A100 80 Go (recommandé) ·
   H100 80 Go (rapide). *Derrière* : à 8B en 4 bits, la mémoire n'est pas le facteur
   limitant — la vitesse l'est, et la H100 fait gagner des minutes, pas de la justesse.
3. **Disque conteneur : 50 Go.** **Volume : 50 Go**, monté sur `/workspace`. *Derrière* :
   le disque conteneur est **effacé à l'arrêt** ; seul le volume survit — et c'est lui qui
   continue d'être facturé à l'arrêt (0,20 $/Go/mois).
4. **Image** : une image PyTorch/CUDA récente, **Python 3.10 à 3.12** (contrainte dure de
   `soup-cli` : au-delà de 3.12, pip résout des roues PyTorch non testées qui plantent avant
   même l'exécution).
5. **Ports** : seul le `22` (SSH) est exposé. Aucune API d'inférence n'est publiée ici, et
   aucune ne doit l'être. *Derrière* : un port ouvert sur l'Internet est une porte ; le
   tunnel SSH la remplace par une serrure.

## 2. Sécurité — quatre règles non négociables

1. **Aucun secret du dépôt sur le pod.** Le pod est **éphémère et tiers**. La clé SSH du
   dépôt, les jetons, les `.env` restent sur le serveur. On monte **la donnée
   d'entraînement**, rien d'autre.
2. **`meta/` n'y monte jamais** — ni entier, ni en extrait (§VI). Le garde-fou du jeu de
   données le refuse par conception, et son refus a été **observé** : `--circuits meta` rend
   un code 2 *avant toute lecture*.
3. **Le port d'écoute reste `22`.** Rien d'inférence, rien de public.
4. **Ce qui sort, c'est l'artefact** — pas les données, pas les journaux bruts.

## 3. Monter la donnée

```bash
# depuis le serveur, vers le pod (le port SSH externe change à chaque redémarrage :
# le relire dans l'onglet Connect → Direct TCP ports avant de relancer un tunnel)
scp -P <port> /root/sandbox-rd/inf-16-dataset/corpus-souverain.jsonl root@<hote>:/workspace/
scp -P <port> /root/sandbox-rd/inf-16-dataset/taches.jsonl           root@<hote>:/workspace/
```

*Pourquoi `/workspace` et pas ailleurs* : c'est le volume persistant. Le reste est effacé.

## 4. Installer l'outil et lancer l'entraînement

```bash
# sur le pod
pipx install "soup-cli[train]"        # ou : uv tool install "soup-cli[train]"
soup doctor                            # GPU, dépendances, versions : à consigner
soup --version                         # à consigner aussi

# 1) laisser l'outil écrire la configuration, puis LA LIRE
soup autopilot --model Qwen/Qwen3-8B --data corpus-souverain.jsonl --goal chat --dry-run

# 2) entraîner — premier run de faisabilité : SFT, LoRA r=16, 4 bits
soup train --config soup.yaml
```

*Ce qui se passe derrière* : `autopilot` choisit méthode, quantisation, LR et époques
d'après des règles, puis écrit un `soup.yaml` ; `train` télécharge la base (16,38 Go au
premier run), entraîne **l'adaptateur seul** (la base reste gelée) et écrit des points de
contrôle. La configuration retenue est **à consigner telle quelle** : sans elle, le run
n'est pas reproductible, et un adaptateur non reproductible n'est pas un livrable.

**La recette définitive n'est pas arrêtée** : elle dépend de la charge de référence
(étape 1). Ce runbook décrit le premier run de **faisabilité**, pas le run utile.

## 5. Évaluer — l'étape qui rend l'artefact jugeable

```bash
soup eval custom --model ./output --tasks taches.jsonl     # mise en forme au schéma attendu
soup ship                                                  # verdict SHIP / DON'T SHIP + preuve
```

*Pourquoi c'est une étape, et non une vérification de courtoisie* : la forme d'échec
documentée de ce domaine est **un run qui se termine, sort en code 0, affiche une perte
normale, et est faux**. L'outil retenu en a publié quatre exemples. **Sans verdict
d'évaluation, l'adaptateur ne quitte pas le pod.**

## 6. Rapatrier, puis détruire

```bash
# rapatrier : l'adaptateur, le rapport d'évaluation, la configuration exacte, les versions
scp -P <port> -r root@<hote>:/workspace/output            ./artefact/
scp -P <port>    root@<hote>:/workspace/soup.yaml        ./artefact/
scp -P <port>    root@<hote>:/workspace/rapport-eval.json ./artefact/
```

Puis, **sur l'interface RunPod : `Terminate`** — jamais `Stop`.
*Derrière* : un pod arrêté facture son volume **au double** (0,20 $/Go/mois) ; 50 Go
arrêtés = **10 $/mois** à ne rien calculer. Vérifier ensuite que le pod a disparu de la
liste **et** que le solde est retombé au niveau d'avant.

## 7. Où va l'artefact

- **`raw/`** (hors git), comme toute pièce binaire du dépôt, **avec une fiche de
  provenance** : empreinte de l'artefact, modèle de base, empreinte du jeu de données,
  configuration, versions, et le verdict d'évaluation.
- **Ce qu'il est** : un fichier qui **porte** ce sur quoi il a été entraîné — donc un objet
  à traiter comme tel, sans diffusion et sans publication, tant que le dépôt n'a pas de
  régime pour cet objet (critère 11 de la `spec.md`).

## 8. Ce à quoi il faut s'attendre

- **Les défauts silencieux.** L'outil a publié : un adaptateur sauvegardé inerte (clés
  malformées — il se recharge comme la base non affinée), des gradients faux sous une perte
  saine, une clé de configuration ignorée. **Contrôle minimum après rapatriement** :
  recharger l'adaptateur et vérifier que les tenseurs portent bien leurs clés, puis lui
  poser une question de la famille F1 — s'il répond comme la base, le run est à refaire.
- **Le collage depuis un iPad.** Une commande **collée** arrive **abîmée** : espaces
  insérés (« `read - rs k` » au lieu de `read -rs k`) et ligne **coupée au milieu d'un
  chemin** (`> /` puis `root/. runpod-api-key`) — **observé le 2026-09-16**, avec les
  messages d'erreur de bash pour seule trace. Les `-options` et les chemins sont les
  premières victimes, et l'échec est **silencieux sur le fond** : rien ne s'écrit, mais on
  croit avoir agi. *Règle* : **taper court, ne coller qu'un seul jeton** (une clé, une
  adresse) ; jamais une commande entière collée depuis un écran de téléphone.
- **Le SSH.** L'image de base ne contient pas toujours de serveur SSH ; le port externe
  **change à chaque redémarrage**.
- **Ne jamais tuer le processus 1** du conteneur (leçon de juin : un `pkill` trop large
  redémarre le pod).
- **La facturation à l'arrêt** (§6) et le **seuil de solde** (au moins 1 h de calcul en
  compte pour pouvoir louer ; plafond de dépense par défaut 80 $/h).
- **Le premier run coûte plus que le calcul** : téléchargement de la base, mise au point,
  et souvent un second essai. Le devis le prévoit (2 h de calcul + 2 h de mise au point).

## 9. Consigner, quoi qu'il arrive

Un run raté se consigne : commandes exactes, versions, code de sortie, message brut, coût
réel observé. C'est ce qui distingue une rafale d'une dépense.

## 10. Pilotage par API — la forme retenue (2026-09-16)

Sidy a retenu la forme où **l'agent gère toute l'installation** : la clé d'API devient donc
nécessaire — et elle est **déposée par lui sur le serveur**, jamais transmise par un canal
conversationnel. Ce que l'API permet, vérifié dans la documentation RunPod le 2026-09-16 :

| Geste | Appel |
|---|---|
| **Vérifier la clé sans rien créer** | `GET https://rest.runpod.io/v1/pods` |
| Créer le pod | `POST https://rest.runpod.io/v1/pods` |
| Suivre l'état | `GET https://rest.runpod.io/v1/pods/{podId}` |
| **Détruire** — jamais « arrêter » | `DELETE https://rest.runpod.io/v1/pods/{podId}` (équivalent de `Terminate`) |

**Clé SSH du pod.** Deux voies existent ; la seconde est retenue : la clé publique déclarée
au niveau du compte, ou l'**écrasement par pod** via la variable d'environnement
**`SSH_PUBLIC_KEY`**. Le pod naît ainsi avec **notre** clé publique dédiée
(`~/.ssh/id_ed25519_runpod_inf16.pub`, empreinte `SHA256:C3Ea6hs8flikIcJOSoqDY58DGDKzFWe1HuRxRJfSoO0`),
et la clé **privée ne quitte pas le serveur** — elle est dédiée à la rafale, donc retirable
sans toucher à l'identité SSH de la machine.

**Transfert de fichiers.** Le SSH « basic » (proxifié par RunPod) **ne supporte ni `scp` ni
SFTP** : il faut un **IP public**. C'est pourquoi la configuration retenue porte
`supportPublicIp: true` et le seul port `22/tcp` — **aucun autre port n'est exposé**, et
aucune API d'inférence n'est publiée.

**Charge utile de création** — à consigner telle quelle *avant* l'appel, pour que le pod soit
reproductible : `name`, `imageName` (PyTorch, **Python 3.10-3.12**), `gpuTypeIds`,
`gpuCount: 1`, `containerDiskInGb: 50`, `volumeInGb: 50`, `volumeMountPath: /workspace`,
`ports: "22/tcp"`, `supportPublicIp: true`, `env.SSH_PUBLIC_KEY`, `cloudType: "SECURE"`.

**Discipline de la clé d'API** — elle a tous les pouvoirs sur le compte, et la documentation
RunPod dit elle-même de la traiter comme un mot de passe :

1. **Jamais dans un canal conversationnel**, **jamais dans le dépôt** (`meta/` compris : il est
   suivi par git et poussé sur GitHub), **jamais sur le pod**.
2. Déposée par Sidy **sur le serveur**, hors dépôt, en mode `600` ; l'agent n'en lit que le
   **fichier**, ne l'affiche jamais, ne la journalise jamais.
3. **Premier appel en lecture seule** (`GET /pods` : ne crée rien, ne coûte rien) — une clé
   invalide se découvre là, pas au milieu d'un run.
4. **Révocation à la fin de la rafale.** Une clé qui a servi ne survit pas à son usage.

## 11. Ce que ce runbook ne fait pas

- Il ne **choisit pas la recette** : elle appartient à la charge de référence (étape 1).
- Il ne **règle pas les droits** sur `textes/` — le jeu de données actuel n'en contient
  aucun (corpus souverain), et c'est délibéré : une fois la cible connue, l'élargissement
  à `textes/` passera par cette question, pas par un ajout discret.
- Il n'**autorise rien** : lancer, c'est décider une dépense (Cmd 13).
