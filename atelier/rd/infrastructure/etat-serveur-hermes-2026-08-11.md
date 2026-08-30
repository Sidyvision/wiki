---
title: État mesuré du serveur (matériel + empreinte Hermes/omniroute) — 2026-08-11
type: infrastructure
tags:
- atelier
- rd
- infrastructure
- serveur
- hermes
- mesure
created: 2026-08-11
updated: 2026-08-11
sources: []
links:
- '[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]'
---

# État mesuré du serveur — 2026-08-11

Fiche de constat pur, sans interprétation ni recommandation (§VIII.2 : le résultat
brut précède toujours l'interprétation). Relevé exécuté depuis le poste
INTÉGRATION, sur demande du pôle R&D. Toute lecture d'optimisation s'appuie sur
ce constat mais vit ailleurs (registre des problèmes, ou fiche dédiée).

## 1. Matériel (Hetzner)

| Ressource | Mesure |
|---|---|
| CPU | 2 vCPU, AMD EPYC-Rome @ 2,0 GHz, 1 thread/cœur |
| RAM totale | 3,7 Gio |
| RAM utilisée | 2,2 Gio |
| RAM libre | 822 Mio |
| RAM disponible (estimation noyau) | 1,6 Gio |
| Swap | 2,0 Gio alloué, **1,0 Gio utilisé** |
| Disque (`/`) | 38 Gio total, 19 Gio utilisés, 18 Gio libres (51 %) |
| GPU | Aucun (contrôleur affiché : Virtio GPU virtuel, pas de GPU physique) |
| Uptime | 78 jours, 18h ; load average 0,01 / 0,06 / 0,04 (1/5/15 min) |

Commandes : `nproc`, `lscpu`, `free -h`, `df -h /`, `lspci \| grep -i vga`,
`nvidia-smi` (absent), `uptime`.

## 2. Empreinte mémoire des processus applicatifs actifs

### 12 profils Hermes (`hermes_cli.main --profile <nom> gateway run`)

| Profil | RSS (Mio) |
|---|---|
| gardien | 167,4 |
| marketing | 125,0 |
| ar-music | 35,5 |
| visual-da | 35,5 |
| production | 35,0 |
| admin-legal | 34,8 |
| accounting | 32,0 |
| distribution | 35,3 |
| publication | 35,5 |
| studio | 36,9 |
| fanzine | 34,7 |
| commerce | 32,0 |
| **Total 12 profils** | **639,5 Mio** |

`gardien` et `marketing` ressortent nettement au-dessus des dix autres profils
(167,4 et 125,0 Mio contre ~32-37 Mio) — fait consigné, cause non investiguée
à ce stade.

### Autres processus mesurés

| Processus | RSS (Mio) |
|---|---|
| `hermes-webui/server.py` (1 instance) | 9,8 |
| `omniroute` (node, v16.2.12, 2 processus) | 1 040,1 |

Commande : `ps -eo pid,rss,args` filtré par processus, somme des RSS par groupe.

## 3. Observation factuelle

`omniroute` seul (1 040,1 Mio) consomme plus de RAM que l'ensemble des 12
profils Hermes réunis (639,5 Mio), soit environ 28 % de la RAM totale du
serveur (3,7 Gio) pour un seul outil. Le swap est utilisé à 1,0 Gio sur 2,0
Gio alloués au moment du relevé. Fait brut consigné sans diagnostic ni
recommandation — à instruire séparément si jugé pertinent (registre des
problèmes ou fiche dédiée).

## 4. Portée et limites de ce relevé

- Instantané à une date et une heure données (2026-08-11) ; aucune valeur
  garantie stable dans le temps (charge Hermes variable selon l'activité
  Discord, par exemple).
- Ne couvre pas : latence réseau, I/O disque, historique de charge, présence
  d'autres processus non listés ici.
- Ce relevé est la base factuelle demandée pour la cartographie infra du pôle
  R&D ([[atelier/rd/index]]) — aucune décision d'optimisation n'est prise sur
  cette seule fiche (Cmd 13, porte humaine).

## 5. Liens

- [[atelier/rd/index]] — charte du pôle, arborescence `rd/infrastructure/`.
- [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]] — autre
  fiche du même dossier, infrastructure de synchronisation.
