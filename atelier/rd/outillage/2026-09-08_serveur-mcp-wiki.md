---
title: "Serveur MCP wiki — accès partageable aux outils déterministes"
type: outillage
tags: [rd, infrastructure, mcp, outils-deterministes, interop]
created: 2026-09-08
updated: 2026-09-09
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
├── wiki_mcp_server.py    ← serveur (~800 lignes, mcp SDK v2)
├── .venv/                ← venv isolé (mcp 2.2.0, pyyaml)
├── .mcp.json             ← config Claude Code (gitignored)
└── README.md             ← documentation complète
```

## 16 outils exposés

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

### INDEX LEXICAL (ajouté 2026-09-09 — phase 3 du chantier d'indexation)

| Outil | Rôle |
|---|---|
| `chercher_terme` | Recherche déterministe dans `index-lexical.json`, **dans les deux sens** : `tomoe` trouve `巴`, `巴` trouve `tomoe`, et `al-ittifâqiyya` trouve `الاتفاقية` (§VII, point 6). |
| `etat_index_lexical` | Totaux, rangs d'appariement, et **fraîcheur déclarée** de l'index. |

**Quatre passes, de la plus stricte à la plus large, et la passe qui a répondu est
toujours nommée** dans le résultat : clé exacte, clé normalisée (diacritiques repliés —
`al-ṭarīqa` trouve `al-tariqa`), forme attestée, sous-chaîne. Cette dernière est
**signalée comme approximative** ; le client n'a jamais à deviner la qualité de sa
correspondance.

**Les deux rangs d'appariement ne sont jamais fondus** : `apparie` porte ce que la fiche
énonce elle-même (rang 1), `jurjani` ce qu'une autorité textuelle transcrite au dépôt
établit, **avec son numéro de définition** (rang 2). C'est la règle « établi vs suggéré »
(§VII, manifestes, règle 3) portée jusqu'au consommateur.

**Trois refus francs, tous éprouvés sur faute fabriquée** (§VII, Épreuve des contrôles) :
index absent (le remède, commande complète, est renvoyé avec le refus), index vide
(« jamais un index vert » — reprise du refus D3 du générateur), et **fraîcheur** : la
date de génération et le nombre de fiches plus récentes sont renvoyés à **chaque**
requête. *Un index périmé ne se plaint jamais de lui-même : il répond, et il répond faux.*

Un silence n'est jamais rendu tel quel : une recherche sans correspondance renvoie les
**clés proches** et rappelle de vérifier `index_perime`, plutôt que de laisser croire que
le terme n'existe pas.

**Les deux axes, rendus avec leur provenance** (2026-09-09). `chercher_terme` renvoie
`tradition` **et** `langue`, jamais fondus : la tradition est le **cadre** où le terme est
cité, la langue une propriété **du terme**. Chacun porte sa provenance — `fiche-propre`,
`definition` ou `ratifie-sidy` pour la tradition ; `sceau-original`, `prose` ou
`forme-appariee` pour la langue. **Un verdict et une mesure n'ont pas la même force, et
le client doit pouvoir le voir sans ouvrir le JSON.** `etat_index_lexical` en donne la
répartition.

**Réciprocité tenue chez le consommateur** (2026-09-09). La translittération que
Jurjānī donne d'une forme arabe **n'est pas une clé de l'index** — on n'injecte pas le
vocabulaire du dictionnaire dans un index qui est celui du wiki. Elle restait donc
introuvable par la recherche directe, et le point 6 du §VII n'était tenu qu'à moitié :
**48 des 132 appariements** étaient à sens unique. Une cinquième passe,
`translitteration-jurjani`, cherche dans les formes latines du champ `jurjani` — et
**les 132 sont désormais atteintes dans les deux sens**, sans qu'une seule clé de
dictionnaire soit entrée dans l'index. La réciprocité est tenue là où elle coûte le
moins : **chez le consommateur, non dans l'artefact.**

**Une divergence déclarée** : le serveur vit **hors du dépôt** (`/root/mcp-servers/`) et
doit rester exécutable si le pôle `rd/` est absent. Il réimplémente donc la
normalisation du générateur au lieu de l'importer — contrairement aux trois définitions
canoniques partagées à l'intérieur du dépôt. La divergence possible est **déclarée en
commentaire** plutôt que niée, et rattrapée par la remontée des clés proches.

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

## Tests (2026-09-09 — outils d'index lexical)

Épreuve des contrôles (§VII), dans le venv du serveur :
- **Vert** — `etat_index_lexical` : 10 688 termes, 756 fiches, 641 textes ; 118 clés
  appariées rang 1, 214 rang 2, 401 portant une annotation ; `perime: False`.
  `chercher_terme` : `tomoe` → `巴` (clé exacte) ; `巴` → `tomoe` ; `البرزخ` → jurjānī
  déf. 0295 ; `al-ṭarīqa` → `al-tariqa` par clé normalisée.
- **Refus** — index absent : refus nommé, **avec la commande de régénération** ; index
  vide : « jamais un index vert » ; index périmé : `perime: True` nommant la fiche plus
  récente.
- **Un faux positif trouvé par l'épreuve et corrigé** : le générateur écrit le condensé
  `.md` **après** le `.json`, de sorte que l'index se déclarait périmé **par lui-même** à
  chaque génération. Les artefacts dérivés sont exclus de la comparaison. *Un contrôle
  qui crie toujours vaut celui qui se tait.*

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
