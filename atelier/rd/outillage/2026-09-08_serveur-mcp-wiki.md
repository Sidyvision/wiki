---
title: "Serveur MCP wiki — accès partageable aux outils déterministes"
type: outillage
tags: [rd, infrastructure, mcp, outils-deterministes, interop]
created: 2026-09-08
updated: 2026-09-08
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe]]"
  - "[[atelier/rd/infrastructure/cartographie-routing-infrastructure]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# Serveur MCP wiki

> **Nature** : outillage déterministe exposant les scripts du dépôt via le protocole
> Model Context Protocol (MCP), pour que Claude Code, Hermes et Qoder partagent
> les mêmes outils vérifiés sans divergence entre agents.
>
> **Principe directeur** : les scripts déterministes (sans LLM, sans réseau) sont la
> source de vérité. Ce serveur ne fait que les rendre appelables — il ne contient
> aucun jugement, aucun résumé, aucun LLM. C'est la transposition du §VIII du
> protocole racine au format MCP.

## Emplacement

```
/root/mcp-servers/wiki/
├── wiki_mcp_server.py    ← serveur (601 lignes, mcp SDK v2)
├── .venv/                ← venv isolé (mcp 2.2.0, pyyaml)
├── .mcp.json             ← config Claude Code (gitignored)
└── README.md             ← documentation complète
```

## 14 outils exposés

### VÉRIFICATION (scripts déterministes — source de vérité)

| Outil | Script | Rôle |
|---|---|---|
| `verifier_invariants` | `verifier-invariants.py --json` | Contrôle structurel complet. **Source de vérité mécanique.** |
| `verifier_coherence_infra` | `verifier-coherence-infrastructure.py --json` | **Anti-fabulation** : confronte `infra_verif` vs réalité Hermes. |
| `detecter_non_tracke` | `detecter-non-tracke.py --json` | Fichiers présents mais non suivis par git. |
| `verifier_rapports_traites` | `verifier-rapports-traites.py --json` | Rapports de monitoring bien traités/archivés. |
| `valider_index_livres` | `valider-index-livres.py` | Validation mécanique des fiches `type: index-livre`. |
| `generer_glossaire_unifie` | `generer-glossaire-unifie.py` | Lexique unifié dérivé — refuse si validateur bloque. |
| `carte_du_depot` | `carte-du-depot.py` | Cartographie mécanique. **Lecture seule** (écrit dans /tmp). |

### LECTURE DE REGISTRES (structurée, pas brute)

| Outil | Source |
|---|---|
| `lire_registre_chantiers` | `atelier/rd/registre-chantiers.md` → JSON structuré |
| `lire_registre_problemes` | `atelier/rd/cahiers/registre-problemes.md` → entrées récentes |
| `lire_etat_infra` | `atelier/rd/infrastructure/cartographie-routing-infrastructure.md` → métriques |

### MONITORING SERVEUR (état live, lecture seule)

| Outil | Mesures |
|---|---|
| `etat_serveur` | RAM (`free -h`), disque (`df -h /`), gateways (`systemctl --user`), processus, uptime. |

### OPÉRATIONS FICHIERS

| Outil | Règle |
|---|---|
| `chercher_fiche` | Recherche par nom/contenu dans *.md. |
| `lire_fiche` | Lecture markdown tronquée (15000 car.). |
| `ajouter_inbox` | **Écriture UNIQUEMENT dans `_inbox/`** — Cmd 7/8, aucun git. |

## Intégration multi-clients

| Client | Configuration | Statut |
|---|---|---|
| **Hermes** | `~/.hermes/config.yaml` → `mcp_servers.wiki` | Config ajoutée, redémarrage requis |
| **Claude Code** | `/root/wiki/.mcp.json` (gitignored) | Créé à la racine du wiki |
| **Qoder** | UI Settings → MCP ou `qoder-mcp.json` | À faire si besoin |

## Architecture : un-serveur-par-domaine

Ce serveur `wiki` est le premier d'un catalogue prévu. Chaque domaine aura son
propre serveur isolé, sans couplage :

```
mcp-servers/
├── wiki/              ← CE SERVEUR
├── musique/           ← À venir : label/musique
├── edition/           ← À venir : textes, bibliothèque
├── 3d/                ← À venir : Instrument, rendu
└── infrastructure/    ← À venir : provisioning, secrets
```

## Conventions techniques

- **MCP SDK v2** : `FastMCP` → `MCPServer`, `run()` → `run_stdio_async()`. Import
  compat géré.
- **PyYAML** requis dans le venv (installé).
- **Pas de hot-reload** : modification config = redémarrage client.
- **Jamais d'auto-accept** : `ajouter_inbox` dépose, ne intègre pas.
- **Self-report interdit** : les scripts déterministes sont la vérité.

## Tests (2026-09-08)

Serveur testé avec un vrai client MCP (mcp 2.x) :
- 14 outils listés et répondants
- `verifier_invariants` : 1411 fichiers, 0 erreur, 0 avertissement
- `etat_serveur` : RAM 136M/3.7G, disque 76%, gateways actifs
- `lire_registre_chantiers` : 56 lignes parsées
- `ajouter_inbox` : fichier créé dans _inbox/, aucun git touché

## Références

- Protocole MCP : https://modelcontextprotocol.io/
- Inventaire outillage déterministe : [[atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe]]
- Règle VIII (déterminisme) : `CLAUDE.md` racine, §VIII
- Règle Cmd 7/8 (étanchéité, _inbox/) : `CLAUDE.md` racine, §VII
