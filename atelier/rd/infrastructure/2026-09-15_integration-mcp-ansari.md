---
title: "Intégration du serveur MCP Ansari — une dépendance tierce déclarée"
type: infrastructure
tags: [rd, infrastructure, mcp, agents, interop, dependance-tiers]
created: 2026-09-15
updated: 2026-09-15
sources:
  - "https://mcp.ansari.chat/mcp"
  - "https://github.com/ansari-project/ansari-mcp"
  - "https://github.com/ansari-project/ansari-skill"
  - "https://arxiv.org/abs/2608.20390"
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/2026-09-08_serveur-mcp-wiki]]"
  - "[[atelier/rd/infrastructure/cartographie-routing-infrastructure]]"
---

# Intégration du serveur MCP Ansari

> **Nature** : seconde entrée du catalogue MCP du dépôt, et **première entrée qui
> n'est pas maison**. Le premier serveur du catalogue —
> [[atelier/rd/outillage/2026-09-08_serveur-mcp-wiki]] — expose vers les agents les
> scripts déterministes du dépôt ; celui-ci expose vers les agents la réponse d'un
> **service tiers hébergé**, hors de notre contrôle et hors de nos sources.
>
> **Ce que cette fiche consigne** : ce qui a été branché, ce qui est **prouvé par
> sortie réelle**, ce qui ne l'est **pas**, et la réserve de régime que la
> consignation doit porter. Elle ne propose aucun usage doctrinal : c'est un état
> d'infrastructure.

## 1. Ce qui a été branché — quatre clients, deux mécanismes

| Client | Mécanisme | Emplacement | Effet |
|---|---|---|---|
| Hermes — profil par défaut | client MCP natif, transport HTTP | `/root/.hermes/config.yaml` → `mcp_servers.ansari` | outil `mcp__ansari__answer_islamic_question` |
| Hermes — profils `gardien` et `karubi` | idem | `profiles/<nom>/config.yaml` | idem ; gateway `gardien` redémarré, `karubi` sans gateway actif (effet au prochain lancement) |
| Claude Code | entrée MCP **portée au niveau utilisateur** | `/root/.claude.json` → `mcpServers.ansari` (`type: http`) | outil `mcp__ansari__answer_islamic_question` |
| Claude Code | Agent Skill officiel | `/root/.claude/skills/ansari/SKILL.md` | déclenchement sur question islamique, appel direct de l'API |
| Qoder CLI | entrée MCP utilisateur | `/root/.qoder/settings.json` → `mcpServers.ansari` (`type: http`) | écrit ; statut **non vérifié**, cf. §4 |
| Qoder CLI | Agent Skill officiel | `/root/.qoder/skills/ansari/SKILL.md` | `ansari [Enabled]` (discovered) |

Source du skill conservée au serveur : `/root/ansari-skill` (clone du dépôt
`ansari-project/ansari-skill`, v3.4.1). Les trois copies du `SKILL.md` — source,
Claude Code, Qoder — portent la **même empreinte** (`e01f4ee551ff0adb0dfa1498d4c67161`).

Aucune écriture n'a été faite à la main dans un `config.yaml` : les entrées Hermes
passent par `hermes mcp add`, les entrées Claude Code et Qoder par leurs CLI
respectives (`claude mcp add`, `qodercli mcp add`).

## 2. Ce que le service est — et ce qu'il n'est pas

- **Un service hébergé**, sans authentification ni clé : `https://mcp.ansari.chat/mcp`,
  transport *streamable-http*, **un seul outil** exposé, `answer_islamic_question(question)`.
- **Sans état** : chaque appel est indépendant, une question de relance doit se
  suffire à elle-même. Coût de latence mesuré : **3 à 11 s** par appel.
- **Un assistant de tradition sunnie généraliste**, ancré sur Coran, recueils de
  hadith et encyclopédie de fiqh, réponses en anglais, **avec citation** ; le serveur
  **exige** que l'attribution à `ansari.chat` soit transmise à l'utilisateur, et le
  dit dans le corps de chaque réponse.
- **Pas un dépôt de texte primaire.** Il rend une synthèse citante, pas la page. Il
  ne peut donc pas tenir lieu de source au sens du §VII du protocole racine : la
  levée d'un `to-source` reste la vérification du texte par Sidy.
- **Backend open source (MIT)**, donc auto-hébergeable : la dépendance porte sur
  l'instance hébergée, non sur un code fermé.

## 3. Ce qui est vérifié — sorties réelles, pas déclarations

| Épreuve | Résultat mesuré |
|---|---|
| `initialize` sur `/mcp` | HTTP 200, `serverInfo: Ansari 1.0.0`, protocole `2024-11-05` |
| `tools/list` | **1** outil : `answer_islamic_question` |
| `GET /mcp` | `{"status":"ready","transport":"streamable-http","authentication":"none"}` |
| Appel réel (conditions de la salât, quatre madhabs) | HTTP 200 en **10,6 s**, réponse structurée, mention d'attribution comprise |
| Robustesse de l'en-tête `Accept` | 200 avec `application/json` **seul**, comme avec `text/event-stream` |
| Hermes — `hermes mcp test ansari` (3 profils) | connecté, **1607 ms** / **1604 ms** / **1619 ms**, 1 outil découvert |
| Hermes — `hermes tools list` (3 profils) | `ansari  all tools enabled` |
| Hermes — bout-en-bout en session neuve | appel par l'agent, **9,1 s**, réponse restituée avec la réserve d'absence de texte précis |
| Claude Code — `claude mcp list` | `ansari: … (HTTP) - ✔ Connected` |
| Qoder — `qoder skills list` | `ansari [Enabled]`, `/root/.qoder/skills/ansari/SKILL.md` |
| API du skill — `POST /api/v2/mcp-complete` | HTTP 200 en **3,4 s**, réponse réelle (cinq piliers) |

## 4. Ce qui n'est PAS vérifié — déclaré, non comblé

- **Le transport MCP de Qoder.** `qoder mcp list` et `qoder mcp get ansari` renvoient
  `✗ Disconnected`. Le format d'entrée est conforme à la documentation Qoder
  (`url` + `type: http`) et le transport n'est **pas** la cause plausible :
  §3 montre que le même point d'entrée répond 200 quel que soit l'en-tête `Accept`.
  L'épreuve de session réelle a été refusée par le CLI lui-même —
  `Not logged in · Please run /login` : **aucune session Qoder authentifiée n'existe
  sur ce serveur**, donc le témoin manque. Deux hypothèses restent ouvertes et sont
  laissées telles quelles : session absente (statut purement local), ou défaut de
  transport de `qodercli 1.1.47`. Revalidation : `/mcp reload` depuis une session
  connectée.
- **Le bout-en-bout Claude Code.** La passe a heurté la limite d'abonnement du
  poste (`You've hit your session limit · resets 12:20am (UTC)`). La connexion est
  établie, la découverte des outils a lieu, mais **aucun aller-retour de question
  n'a été obtenu depuis Claude Code**. L'équivalent a été obtenu côté Hermes.
- **La fraîcheur du skill.** v3.4.1, clone du 2026-09-15, **aucune mise à jour
  automatique branchée** : la copie vieillira.

## 5. Réserve de régime — la portée du skill, à ne pas confondre avec une source

Le `SKILL.md` officiel impose à l'agent qui le porte trois garde-fous explicites :
**ne pas répondre depuis sa propre connaissance islamique**, **ne pas substituer une
recherche web**, **ne pas répondre par un autre moyen si l'API tombe** — et annoncer
l'indisponibilité. Conséquence opérationnelle, énoncée sans détour : pour les clients
où le skill est actif (Claude Code, Qoder), Ansari **n'est pas une source parmi
d'autres, c'est la source** sur ces questions.

Cela n'élève pas le service au rang de source du dépôt. Trois raisons, indépendantes
l'une de l'autre :

1. il ne fournit pas de texte primaire à citer, seulement une synthèse attribuée ;
2. il porte une tradition généraliste qui n'est pas la ligne de sources propre au
   dépôt, et ne peut donc pas en tenir lieu ;
3. l'agent qui le consulte est un exécutant : le verdict sur un contenu reste humain
   (Cmd 13). **Aucune fiche doctrinale ne s'adosse à sa seule réponse.**

## 6. La tension avec la finalité du pôle — déclarée, pas dissimulée

La mission du pôle `rd/` est l'**émancipation progressive de tout intermédiaire de
service tiers**. Cette intégration fait l'inverse : elle **ajoute** une dépendance à
un service tiers hébergé, sur lequel nous n'avons ni mesure, ni journal, ni garantie
de disponibilité. Le fait est consigné comme tel.

Ce qui borne la dépendance :

- le code du backend et du skill est **ouvert et auto-hébergeable** (MIT) : la sortie
  de la dépendance est un déploiement, pas une réécriture ;
- **aucune clé, aucun compte, aucun quota** : rien n'est souscrit, rien n'est lié ;
- l'outil est **appelé explicitement** par l'agent, il ne s'active pas seul ;
- le retrait tient en une commande par client (§7).

## 7. Réversibilité (Cmd 10)

```
hermes mcp remove ansari                      # + --profile gardien|karubi
claude mcp remove ansari -s user
qodercli mcp remove ansari -s user
qodercli skills uninstall ansari
```

Sauvegarde prise avant écriture : `/root/.hermes/config.yaml.bak-preansari-202609142344`.
**Rien n'a été supprimé.** Le harnais de développement du dépôt tiers (`AGENTS.md`,
`CLAUDE.md`, `codev/`) a été **déplacé** — non supprimé — vers
`/root/ansari-skill/_harnais-developpement/` : ces fichiers sont des fichiers de
contexte projet qu'un agent travaillant dans ce dossier chargerait comme directives,
ce qu'on ne veut pas d'un dépôt tiers installé dans le home.

## 8. Contrôles et points laissés ouverts

- `verifier-invariants.py --racine /root/wiki` : **0 erreur**, **71 avertissements**
  (C5/C6 d'étanchéité inversée, tous antérieurs et inchangés).
- `carte-du-depot.py --repo /root/wiki` : artefact dérivé régénéré — **820 fiches**.
- **Aucune forme de `infra_verif` ne couvre ce cas.** Le champ reconnu par
  `verifier-coherence-infrastructure.py` porte `profil`, `cron_job`,
  `discord_home_channel`, `discord_allowed_channels` : rien pour `mcp_servers`.
  L'affirmation « trois profils Hermes portent cette entrée » n'est donc **pas**
  vérifiable par le contrôle mécanique aujourd'hui — elle l'est à la main
  (`hermes --profile <p> mcp list`). Une extension du vérificateur serait un chantier
  `OUT` : **non ouvert ici**.
- **Non fait, volontairement** : extension aux onze autres profils Hermes (non
  demandée) ; mise à jour de
  [[atelier/rd/infrastructure/cartographie-routing-infrastructure]] (une passe
  dédiée, une page = un sujet) ; inscription au registre des chantiers (acte de
  verdict).
- **Relevé hors sujet, non corrigé** : Claude Code signale quatre règles
  d'autorisation trop larges dans `/root/.claude/settings.local.json` — l'étoile y
  précède la fin de la commande (`Bash(cp -r doctrinal/* /root/wiki/doctrinal/)`),
  donc elle approuve aussi toute option insérée à cette position, sans prompt.
  Signalé, à la main de Sidy.
