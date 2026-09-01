---
title: "Infrastructure — Cartographie de routing (hardware, software, canaux d'entrée/sortie)"
type: infrastructure
tags: [rd, infrastructure, routing, hardware, software, cartographie, points-fragiles]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]"
  - "[[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]]"
  - "[[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]]"
  - "[[atelier/rd/infrastructure/infrastructure-ssh-statu-quo]]"
  - "[[atelier/rd/infrastructure/configuration-hermex-webui-2026-08-23]]"
  - "[[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]]"
  - "[[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]]"
  - "[[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]]"
  - "[[atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16]]"
  - "[[atelier/rd/infrastructure/canal-telegram-wendel-2026-08-21]]"
  - "[[atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12]]"
  - "[[atelier/rd/infrastructure/monitoring-archive-charte]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
---

# Infrastructure — Cartographie de routing

> ⚠️ **Fiche de synthèse, pas de mesure nouvelle.** Chaque donnée ci-dessous est
> reprise d'une fiche déjà consignée dans le dépôt (lien en regard) ou d'une
> lecture directe des archives de monitoring déjà persistées
> (`atelier/rd/infrastructure/monitoring-archive/`) — aucune commande n'a été
> exécutée sur le serveur pour produire cette page. Ce n'est ni un
> `to-source` (rien n'est affirmé sans pointeur), ni un constat brut au sens
> de [[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]
> (qui s'interdisait toute lecture de force/fragilité, §VIII.2) : cette fiche
> assume au contraire la lecture diagnostique demandée par Sidy — c'est son
> **objet exact** (§ci-dessous). Le verdict de toute action de remédiation
> reste entier à Sidy (Cmd 13) ; rien ici n'est exécuté.

## 0. Vue d'ensemble en un coup d'œil

Pour un agent qui atterrit ici sans contexte — le détail argumenté est dans les
sections qui suivent, cette table ne fait que le résumer :

| | |
|---|---|
| **Hardware** | 1 serveur Hetzner — 2 vCPU AMD EPYC-Rome, 3,7 Gio RAM, 38 Gio disque |
| **Software** | 14 profils Hermes (12 métier + 2 Karūbī `habib-*`) · `omniroute` (routing LLM, `:20128`) · `hermes-webui` (`:8787`) · Tailscale Funnel |
| **Canaux (6)** | Git/SSH · Discord · Telegram ×2 (Mehdi, Wendel) · Terminal scopé (`mehdi`, `wendel`) · Webui/Tailscale · API LLM — tous convergent vers le sas `_inbox/` |
| **État mesuré au 2026-08-31** | RAM libre 136 Mio (critique) · disque 76 % utilisé · 4/12 gateways métier actifs |
| **Fragilités dominantes** | RAM structurellement sous-dimensionnée (§4.2) · `omniroute` SPoF · quota Qwen récurrent · secrets historiques non révoqués · comptes de service sous root |
| **Points ouverts non résolus** | [[atelier/rd/cahiers/registre-problemes]], entrées `[2026-09-01]` — gateways en `failed` divergents de la décision du 2026-08-28, profil `commerce` absent |
| **Aller plus loin** | §1 hardware · §2 software · §3 routing · §4 forts/fragiles · §5 lecture globale · §6 points ouverts |

## Nature et objet de la fiche

Pendant du [[atelier/materiel/studio-principal|routing du studio (musique)]]
mais pour l'infrastructure informatique globale : hardware, software, et
**routing** — comment un signal (message, commit, requête modèle) entre dans
le système, par quel chemin il transite, où il aboutit. Le studio a sa fiche
matériel + son schéma de routage ; l'infrastructure Hetzner/Hermes n'avait
jusqu'ici que des fiches de constat ponctuel
([[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11|architecture
globale, 2026-08-11]]) ou des fiches d'incident isolées. Cette page les relie
et ajoute ce qu'aucune ne portait encore : une lecture explicite
**fort/stable vs fragile**, pour aller du particulier (tel service, tel
canal) au global (où porter l'effort d'optimisation en premier).

**Ce que cette fiche n'est pas** : un remplacement des fiches sources — elle
pointe, elle n'absorbe pas (même discipline que
[[atelier/rd/registre-chantiers]]). Une mesure datée ci-dessous reste une
photographie ; à revérifier avant toute décision qui s'appuierait dessus.

## 1. Hardware — le serveur

Un seul poste physique porte toute l'infrastructure : le serveur Hetzner qui
héberge le dépôt (`/root/wiki`) et l'ensemble des services décrits plus bas.
Aucun autre poste physique n'entre dans le routing applicatif — les iPad
(PRODUCTION/CONSULTATION, §I du protocole racine) sont des clients, jamais
un maillon du routing serveur.

| Ressource | Mesure du 2026-08-11 | Mesure du 2026-08-31 | Écart |
|---|---|---|---|
| CPU | 2 vCPU AMD EPYC-Rome @ 2,0 GHz | — (non remesuré) | — |
| RAM totale | 3,7 Gio | 3,7 Gio | inchangée (plafond structurel) |
| RAM utilisée | 2,2 Gio | 3,3 Gio | **+1,1 Gio** |
| RAM libre | 822 Mio | 136 Mio | **−686 Mio** |
| Swap utilisé | 1,0 / 2,0 Gio | 1,4 / 2,0 Gio | **+0,4 Gio** |
| Disque (`/`) | 19 Gio utilisés / 38 Gio (51 %) | 28 Gio utilisés / 38 Gio (**76 %**) | **+9 Gio, +25 pts** |
| GPU | aucun (Virtio GPU virtuel) | — | — |
| Uptime | 78 j 18 h, load 0,01/0,06/0,04 | — (non remesuré) | — |

Sources : [[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]] (relevé
du 11) ; `atelier/rd/infrastructure/monitoring-archive/2026-08-31_41dc3e7e492c.txt`
(relevé du 31, `df -h` + `free -h` en tête de rapport). Vingt jours séparent
les deux mesures ; aucune mesure intermédiaire agrégée n'existe (le dossier
`monitoring-archive/` la porte jour par jour mais rien ne la synthétise avant
cette fiche).

## 2. Software — inventaire des services

### 2.1 Profils Hermes (agents Discord/Telegram)

14 instances au total : 12 profils « métier » (compte `root`) + 2 profils
Karūbī (`habib-mehdi`, `habib-wendel`, chacun sous son propre compte Unix
non-root — voir §3.3). État des 12 profils métier, relevé le 2026-08-31
(`systemctl --user list-units 'hermes-*'`, exécuté en root) :

| Profil | Fonction | RAM mesurée (2026-08-11) | État systemd (2026-08-31) |
|---|---|---|---|
| gardien | Protocol Guardian | 167 Mio | ✅ `active running` |
| ar-music | A&R | 35 Mio | ✅ `active running` |
| publication | Publication | 35 Mio | ✅ `active running` |
| studio | Ingénierie son | 37 Mio | ✅ `active running` |
| accounting | Comptabilité | 32 Mio | ❌ `failed` |
| admin-legal | Administratif & Légal | 35 Mio | ❌ `failed` |
| distribution | Distribution | 35 Mio | ❌ `failed` |
| fanzine | Fanzine & Communication | 35 Mio | ❌ `failed` |
| marketing | Sensibilisation | 125 Mio | ❌ `failed` |
| production | Production | 35 Mio | ❌ `failed` |
| visual-da | Direction Artistique | 35 Mio | ❌ `failed` |
| commerce | Commerce | 32 Mio | ⚠️ absent de la liste systemd (voir §5) |

Chaque profil vit sous `/root/.hermes/profiles/<nom>/` (`config.yaml`,
`SOUL.md`, `MEMORY.md`, `skills/`, `.env`).

### 2.2 Services de plateforme

| Service | Rôle | Port | Daemonisation | RAM (dernière mesure) |
|---|---|---|---|---|
| `omniroute` | Proxy de routage de modèle LLM (auto-routage vers fournisseurs gratuits) | `20128` (localhost) | systemd, `Restart=always` depuis le 2026-08-27 | ~1,0–1,6 Gio (2 process node) — **le plus gros consommateur du serveur** |
| `hermes-webui` | Interface web des sessions Hermes/Claude Code | `8787` (localhost, exposé via Tailscale Funnel) | systemd, même gabarit qu'omniroute, depuis le 2026-08-27 | ~10 Mio |
| Tailscale Funnel | Proxy HTTPS public → `127.0.0.1:8787` | `https://wiki.tail7ce5ca.ts.net` | service Tailscale natif | — |

### 2.3 Fournisseurs de modèle (LLM)

| Fournisseur | Consommé par | Régime | Fragilité connue |
|---|---|---|---|
| Anthropic (Claude) | Sessions Claude Code (terminal, intégration) | Quota d'abonnement Sidy, réservé — jamais routé aux agents Hermes (contrainte explicite, 2026-08-26) | Quota personnel, à ménager |
| Qwen (Cloud Token Plan) | 9 profils métier restés sur Qwen | Quota hebdomadaire, épuisable | Épuisement déjà survenu le 2026-08-26 (reset 2026-08-29) |
| OmniRoute (`custom:omniroute`, `auto/best-free`) | `gardien`, `studio`, `publication`, Hermes Terminal | Auto-routage gratuit multi-fournisseurs | Combo instable observé (retries, latences ~90s) ; SPoF (§4) |

## 3. Routing — canaux d'entrée/sortie

Six canaux distincts convergent vers le dépôt ou en repartent. Tous les
canaux d'écriture humaine convergent structurellement sur le même point :
le sas `_inbox/`.

| Canal | Protocole | Sens | Confluence / destination |
|---|---|---|---|
| **Git** (Obsidian + Working Copy ↔ GitHub ↔ Hetzner) | SSH (`git@github.com:Sidyvision/wiki.git`) | Sidy (iPad) ↔ dépôt | commits directs dans les circuits |
| **Discord** (12 gateways Hermes) | HTTPS (bot Discord par profil) | bidirectionnel, par salon alloué | agents métier, réponses en salon |
| **Telegram — Mehdi** (`habib-mehdi`) | HTTPS (bot `@HabibKarubi_bot`) | Mehdi → dépôt | `_inbox/` via `depot-ecriture/inbox/` |
| **Telegram — Wendel** (`habib-wendel`) | HTTPS (bot `@HassanKarubi_bot`) | Wendel → dépôt | `_inbox/` via `depot-ecriture/inbox/` |
| **Terminal SSH scopé** (comptes `mehdi`, `wendel`) | SSH + bind mounts `ro`/`rw` | lecture scopée ↔ `_inbox/` | `_inbox/` via `depot-ecriture/inbox/` |
| **Webui/Tailscale** | HTTPS (Tailscale Funnel) | Sidy (iPhone/iPad) ↔ sessions Hermes/Claude Code | reprise de session, pas d'écriture dépôt directe |
| **API LLM** | HTTPS | Hermes/Claude Code → Anthropic / Qwen / OmniRoute | réponses agent (texte) |

### Schéma de flux

```
Sidy (iPad)                    Mehdi / Wendel (SSH, Telegram)
   │ commit (Obsidian)              │ dépôt scopé
   ▼                                 ▼
Working Copy ──SSH──► GitHub ◄──git pull── Hetzner (/root/wiki)
                                          │
                                          ├── _inbox/ ◄── Telegram (habib-mehdi, habib-wendel)
                                          ├── _inbox/ ◄── Terminal scopé (mehdi, wendel)
                                          │
                                          ├── 12 profils Hermes ──HTTPS──► Discord
                                          │        │
                                          │        └──HTTPS──► Anthropic / Qwen / OmniRoute(:20128)
                                          │
                                          └── hermes-webui(:8787) ──Tailscale Funnel──► Sidy (iPhone/iPad)
```

Le sas `_inbox/` est donc le **point de convergence unique** de tout dépôt
externe (Sidy, Mehdi, Wendel, quel que soit le canal) avant intégration
humaine dans les circuits — cohérent avec §IX du protocole racine.

## 4. Points forts / stables — points fragiles

C'est l'objet demandé : une lecture croisée, pour savoir où l'infrastructure
tient d'elle-même et où elle ne tient que par une vigilance manuelle
répétée.

### 4.1 Points forts / stables

| Point | Pourquoi il tient |
|---|---|
| Git/SSH (`origin`) | Statu quo assumé, clé stable depuis des mois, zéro secret à renouveler ([[atelier/rd/infrastructure/infrastructure-ssh-statu-quo]]) |
| `omniroute` (daemonisation) | Éprouvé stable depuis le 2026-08-27 (`Restart=always`, aucun redémarrage depuis) — le vrai point de fragilité (couplage à une session terminal mobile) a été supprimé structurellement, pas contourné |
| `hermes-webui` (daemonisation) | Même remède, même stabilité depuis le 2026-08-27 |
| Canal Telegram Mehdi | Isolation OS vérifiée (`ps -o user=` → `mehdi`, pas `root`), test réel confirmé, `statut_experience: reproduit` |
| CPU / charge processeur | Load average historiquement quasi nul (0,01–0,06) ; jamais identifié comme facteur de panne dans aucun incident consigné |
| `monitoring-archive/` + `coherence-infrastructure-brute` | Jobs réparés et tracés par `infra_verif` (vérification mécanique indépendante de l'affirmation narrative de l'agent) |
| Sas `_inbox/` | Point de convergence unique, discipline d'étanchéité respectée à ce jour |

### 4.2 Points fragiles

| Point | Nature de la fragilité | Signal déjà observé |
|---|---|---|
| **RAM (3,7 Gio, plafond matériel)** | Structurellement insuffisante pour 14 gateways + `omniroute` simultanés | Saturation critique et indisponibilité des agents le 2026-08-28 ([[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]]) ; RAM libre retombée à 136 Mio le 2026-08-31, swap à 1,4/2,0 Gio |
| **`omniroute` (SPoF)** | Un seul process porte le routage modèle de `gardien`/`studio`/`publication`/Terminal, et consomme à lui seul jusqu'à 28 % de la RAM totale | Incident EADDRINUSE du 2026-08-27 ; « fonction inconnue » restée non documentée du 2026-08-11 au 2026-08-26 |
| **Gateways Discord — état divergent de la décision consignée** | Le 2026-08-28, 3 gateways devaient rester actifs (`gardien`, `studio`, `publication`) et 8 désactivés. Le relevé du 2026-08-31 montre `ar-music` **actif** (hors liste des 3) et 7 gateways en état `failed` — pas `inactive`/`disabled` propre, ce qui signale une tentative de démarrage avortée, pas un arrêt volontaire propre | Écart non instruit à ce jour — **point ouvert**, §5 |
| **Quota Qwen** | Épuisement hebdomadaire récurrent, 9 profils métier dépendants | Épuisement du 2026-08-26, reset attendu 2026-08-29 |
| **Combo `auto/best-free` (OmniRoute)** | Rotation entre fournisseurs gratuits hétérogènes, latence et échecs transitoires observés | Retry `Maximum combo retry limit reached` (profil studio) ; latence ~90s (Terminal), 2026-08-26 |
| **Disque (`/`, 76 % utilisé au 2026-08-31)** | Progression de +25 points en 20 jours (51 % → 76 %), aucun seuil d'alerte automatisé connu | Constat brut, aucune saturation encore atteinte |
| **Secrets en clair, historique** | `ANTHROPIC_AUTH_TOKEN` trouvé en clair dans `.bash_history` et `.omniroute-env.sh` ; rédigé sur disque le 2026-08-27 mais **jamais révoqué côté fournisseur** | [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]], note de sécurité annexe |
| **Comptes de service sous root** | Les 12 gateways Hermes métier tournent en `systemctl --user` **sous root**, pas sous compte dédié (contrairement aux profils Karūbī `habib-mehdi`/`habib-wendel`) | Avertissement `security_audit` interne observé, signalé sans remédiation (2026-08-26) |
| **SSH par mot de passe activé sur l'hôte** | Surface d'attaque en plus de la clé SSH | Même avertissement `security_audit`, signalé sans remédiation |
| **Aucun backup hors-site** | SLA Hetzner (99,9 %) est la seule garantie de disponibilité ; git reste la seule copie distribuée réelle (GitHub) | [[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]] §8 (SPoF) |
| **Hermex (app native mobile)** | WebSocket non supporté par le webui actuel — inutilisable, contournement PWA seulement | [[atelier/rd/infrastructure/configuration-hermex-webui-2026-08-23]] |
| **Profil `commerce`** | N'apparaît pas du tout dans `systemctl --user list-units 'hermes-*'` du 2026-08-31 — ni actif ni `failed`, absent | Écart non instruit — **point ouvert**, §5 |

## 5. Lecture du particulier au global

La fragilité la plus citée fiche par fiche (RAM, `omniroute`, gateways
Discord, Qwen) n'est pas quatre problèmes indépendants : c'est **une seule
contrainte structurelle** — 3,7 Gio de RAM sur un plafond matériel fixe —
qui se manifeste à chaque fois qu'un service supplémentaire y est ajouté
sans retrait équivalent ailleurs. Chaque remédiation ponctuelle documentée
(daemonisation d'`omniroute`, arrêt de 8 gateways le 2026-08-28) a résolu son
incident local sans lever la contrainte globale — le relevé du 2026-08-31
(136 Mio de RAM libre, gateways en `failed` plutôt qu'en arrêt propre)
suggère que la pression est revenue. C'est une lecture, pas un verdict : la
décision d'ajouter de la RAM, de réduire le nombre de gateways simultanés,
ou d'adopter un régime « gateway à la demande » (piste déjà nommée dans
l'incident du 2026-08-28) reste entière à Sidy (Cmd 13).

## 6. Points ouverts (non instruits par cette fiche)

1. **Écart gateways du 2026-08-31** (§4.2) : pourquoi `ar-music` est actif
   hors de la liste des 3 prioritaires, et pourquoi 7 profils sont en
   `failed` plutôt qu'`inactive`/`disabled` — versé au registre des problèmes
   pour suivi, pas seulement signalé ici :
   [[atelier/rd/cahiers/registre-problemes]], entrée
   `[2026-09-01] ouvert | Gateways Discord en failed plutôt qu'inactive`.
2. **Profil `commerce`** absent de `systemctl --user list-units` — même
   traitement : [[atelier/rd/cahiers/registre-problemes]], entrée
   `[2026-09-01] ouvert | Profil Hermes commerce absent du relevé systemd`.
3. **`ANTHROPIC_AUTH_TOKEN`** redacté sur disque le 2026-08-27 : révocation
   côté fournisseur non confirmée à ce jour.
4. **CPU / uptime** non remesurés depuis le 2026-08-11 — cette fiche ne
   comble pas cet écart, elle le signale.
5. **Comptes de service sous root** et **SSH par mot de passe** : signalés
   par l'audit de sécurité du 2026-08-26, aucune remédiation entreprise à ce
   jour — portés ici pour visibilité, décision entière à Sidy.

## 7. Références

- [[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]] — topologie complète, constat pur du 2026-08-11
- [[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]] — mesures matérielles détaillées du 2026-08-11
- [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]] — détail du canal Git/Obsidian/Working Copy
- [[atelier/rd/infrastructure/infrastructure-ssh-statu-quo]] — décision SSH vs HTTPS+PAT
- [[atelier/rd/infrastructure/configuration-hermex-webui-2026-08-23]] — détail du canal webui/Tailscale
- [[atelier/rd/infrastructure/2026-08-26_migration-omniroute-quota-qwen]] — bascule des fournisseurs modèle
- [[atelier/rd/infrastructure/incident-2026-08-27-omniroute-eaddrinuse-daemonisation]] — daemonisation omniroute + hermes-webui
- [[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]] — crise RAM, arrêt de 8 gateways
- [[atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16]] · [[atelier/rd/infrastructure/canal-telegram-wendel-2026-08-21]] — canaux Telegram
- [[atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12]] — accès Terminal scopé
- [[atelier/rd/infrastructure/monitoring-archive-charte]] — dispositif de mesure quotidien, source du relevé du 2026-08-31
- `atelier/rd/infrastructure/monitoring-archive/2026-08-31_41dc3e7e492c.txt` — relevé brut cité §1/§2
- [[atelier/materiel/studio-principal]] — pendant côté studio audio (routing matériel musique)
