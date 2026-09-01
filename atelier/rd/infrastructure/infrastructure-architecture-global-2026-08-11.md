---
title: "Infrastructure — Architecture globale du système (2026-08-11)"
type: infrastructure
tags: [rd, infrastructure, architecture, systeme, hermes, omniroute, serveur]
created: 2026-08-11
updated: 2026-08-11
sources: []
links: []
---

# Architecture Infrastructure — Vue globale

Cartographie complète du système d'infrastructure (matériel, services, agents,
synchronisation). Constat pur sans recommandation (§VIII.2) ; optimisations et
diagnostics vivent ailleurs (registre des problèmes).

## 1. Topologie réseau et physique

```
┌─────────────────────────────────────────────────────────────────┐
│                         Internet / Réseau                        │
└──────────────┬──────────────────┬──────────────────┬─────────────┘
               │                  │                  │
        ┌──────▼────────┐  ┌──────▼────────┐  ┌────▼──────────────┐
        │ GitHub        │  │ Discord       │  │ Autres services   │
        │ Sidyvision/   │  │ (Hermes       │  │ (Qwen, API Anthropic)
        │ wiki.git      │  │  gateways)    │  │
        │ (SSH origin)  │  │               │  │
        └──────┬────────┘  └──────┬────────┘  └────┬──────────────┘
               │                  │               │
        ┌──────▼──────────────────▼───────────────▼─────────┐
        │  Hetzner Server (Ubuntu, /root/wiki)             │
        │  ├─ 2 vCPU AMD EPYC-Rome                        │
        │  ├─ 3.7 GB RAM, 38 GB Disk (51% libre)          │
        │  ├─ SSH key (git@github.com)                    │
        │  └─ 1 GB Swap utilisé                           │
        └─────┬──────────────────────────────────────────┘
              │
        ┌─────▼────────────────────────────────────────────────┐
        │              Postes de travail (iPad)                │
        │  ┌────────────────┐        ┌──────────────────┐     │
        │  │ Obsidian       │◄──────►│ Working Copy     │     │
        │  │ (Git plugin)   │        │ (Folder Sync)    │     │
        │  │ • Édition      │        │ • Fetch/Pull/Push│     │
        │  │ • Commits      │        │ • SSH au server  │     │
        │  │  locaux        │        └──────────────────┘     │
        │  └────────────────┘                                  │
        └──────────────────────────────────────────────────────┘
```

## 2. Couche applicative — Services sur Hetzner

### 2.1 Profils Hermes (12 agents Discord)

Chacun = une instance `hermes -p <nom> gateway run` en systemd service.

| Profil | Fonction | RAM | Statut | Notes |
|--------|----------|-----|--------|-------|
| **gardien** | Protocol Guardian (doctrine, conformité) | 167 MB | Actif | Accès `meta/`, moteur Qwen (test) |
| **marketing** | Sensibilisation, dépôt Discord | 125 MB | Actif | Free-response ON |
| **ar-music** | A&R | 35 MB | Actif | Productif |
| **visual-da** | Direction Artistique | 35 MB | Actif | Étendu photo/argentique 2026-08-07 |
| **production** | Production (scheduling, budget) | 35 MB | Actif | Productif |
| **admin-legal** | Administratif & Légal | 34 MB | Actif | Productif |
| **accounting** | Comptabilité (factures, budgets) | 32 MB | Actif | Productif |
| **distribution** | Distribution (ventes, canaux) | 35 MB | Actif | Productif |
| **publication** | Publication (site, archives) | 35 MB | Actif | Validation préversion requise |
| **studio** | Ingénierie son | 36 MB | Actif | Productif |
| **fanzine** | Fanzine & Communication | 34 MB | Actif | Productif |
| **commerce** | Commerce, profitabilité | 32 MB | Actif | Guardrails doctrine appliqués |
| **TOTAL** | — | **639.5 MB** | — | —  |

**Configuration commune** : chaque profil `/root/.hermes/profiles/<nom>/` contient
- `config.yaml` (connexion Discord + provider)
- `SOUL.md` (prompt du rôle, verbatim)
- `MEMORY.md` (mémoire agent, append-only)
- `skills/` (72 skills groupées)
- `.env` (clé API, tokens)

**Gateway Discord** : chaque profil connecté à Discord via un bot distinct,
dans des salons assignés (allowlist stricte de salons autorisés).

### 2.2 omniroute (Node.js)

| Composant | Valeur | Notes |
|-----------|--------|-------|
| Processus | 2 × node | Fork/cluster |
| Mémoire | **1 040 MB** (28 % RAM totale) | Ressource critique |
| Version | v16.2.12 | À vérifier si à jour |
| Port | ? | Non documenté ici |
| Fonction | ? | À déterminer |

Observation brute : omniroute seul consomme plus de RAM que les 12 profils
Hermes réunis.

### 2.3 Autres services

| Service | RAM | Fonction | Statut |
|---------|-----|----------|--------|
| `hermes-webui/server.py` | 9.8 MB | Interface web | Actif |

## 3. Couche dépôt — Workflow CONSULTATION → INTÉGRATION

```
CONSULTATION (iPad)              INTÉGRATION (Hetzner)
───────────────────────          ────────────────────

Obsidian (lecture/édition)
  ↓ commit local
  ├─ [si push] → Working Copy
  │            ↓ Fetch/Pull/Push
  │            ↓ via SSH
  │            ├─→ GitHub origin
  │                   ↓ (WebHook ou poll)
  │                   ↓
  │               Hetzner server
  │               $ git pull
  │               $ verifier-invariants.py
  │               $ generer-cartographie.py
  │               $ atelier/rd/outillage/detecter-non-tracke.py
  │               ↓
  │               Sac d'intégration (_inbox/) → circuits
  │               ↓
  │               annales + registre

Obsidian auto-pull (périodique)
  ← reads latest from GitHub
```

## 4. Empreinte mémoire détaillée

| Composant | RSS | % de 3.7 GB | Notes |
|-----------|-----|------------|-------|
| Hermes 12 agents | 639.5 MB | 17 % | Incluant gardien (Qwen) |
| omniroute | 1 040 MB | 28 % | Critique, investigation ouverte |
| hermes-webui | 9.8 MB | <1 % | Faible |
| Autres (kernel, syst.) | ~2 GB | 54 % | Estimation grossière |
| **Total utilisé** | ~3.7 GB | 100 % | = RAM totale |
| **RAM libre** | 822 MB | 22 % | Selon mesure du moment |
| **RAM disponible (kernel)** | 1.6 GB | 43 % | Inclut page cache récupérable |
| **Swap utilisé** | 1 GB / 2 GB | 50 % | Pression mémoire visible |

**Signal d'alerte** : utilisation du swap (1 GB) indique une pression mémoire
au moment de la mesure. Pas de crise immédiate mais à surveiller.

## 5. Ressources stockage

| Ressource | Utilisé | Libre | % utilisé |
|-----------|---------|-------|-----------|
| `/` | 19 GB | 18 GB | 51 % |

Aucune saturation imminente.

## 6. Uptime et charge

| Métrique | Valeur | Notes |
|----------|--------|-------|
| Uptime | 78j 18h | Serveur stable |
| Load avg 1 min | 0.01 | Très faible |
| Load avg 5 min | 0.06 | Très faible |
| Load avg 15 min | 0.04 | Très faible |

Pas de surcharge CPU.

## 7. Circuits informatiques et protocoles

| Circuit | Protocole | Données | Direction | Fréquence |
|---------|-----------|---------|-----------|-----------|
| Git | SSH | Commits code | iPad ↔ Hetzner | Manuelle |
| Discord | HTTPS | Messages texte | Hermes ↔ Discord | Temps réel |
| API | HTTPS | Requêtes LLM | Hermes ↔ Anthropic/Qwen | À la demande |
| Wiki (interne) | Filesystem | Markdown | Hetzner (commit) | À l'intégration |

## 8. Points de défaillance uniques (SPoF)

| SPoF | Impact | Mitigation actuelle | Remédiation suggérée |
|-----|--------|--------------------|--------------------|
| **Clé API Anthropic** | 11 agents paralysés | Partagée sur tous les profils | Clé personnelle Sidy (pending) |
| **omniroute** | Fonction inconnue | — | À clarifier |
| **Hetzner SSH key** | Écriture dépôt bloquée | Clé déjà en place | Key rotation périodique ? |
| **Uptime Hetzner** | Tous les services | SLA Hetzner 99.9% | Pas de backup hors-site |

## 9. Points ouverts (pas instruits ici)

1. **omniroute** : fonction exacte, dépendances, optimisation RAM ?
2. **Clé API Anthropic** : impasse à Sidy, en attente résolution budget
3. **Qwen sur gardien** : clause « No API automation » à respecter (risque révocation)
4. **Hermes accès `meta/`** : cloisonnement technique statu quo temporaire (retour d'expérience en cours)
5. **Historique de charge** : aucune série temporelle disponible (monitoring à venir)

## 10. Références et documentation connexe

- [[etat-serveur-hermes-2026-08-11]] — mesures brutes et détails techniques
- [[synchro-obsidian-working-copy-github]] — procédure Obsidian/Working Copy
- [[infrastructure-ssh-statu-quo]] — décision statu quo SSH
- `meta/projet-unifie/archives/15-architecture-discord-hermes-2026-08-07.md` — détails profils Hermes
- `atelier/rd/cahiers/registre-problemes.md` — diagnostics ouverts
