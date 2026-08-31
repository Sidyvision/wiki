---
title: "Migration modulaire des 11 agents restants et intégration de la contribution de Sidy au Choura"
type: experience
statut_experience: exploratoire
statut: brouillon
created: 2026-08-31
updated: 2026-08-31
tags: [atelier, rd, hermes, agents, prompts, choura, hook, discord, conservation]
sources: []
links:
  - "[[atelier/rd/cahiers/2026-08-31_rapport-investigation-architecture-modulaire-agents]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
---

# Migration modulaire des 11 agents restants et contribution de Sidy au Choura

**Statut** : rapport de passe, remis au pôle R&D à la demande de Sidy
(« occupe-toi des points 1. et 2. et consigne ton rapport au R&D »).
Deux chantiers distincts, menés dans la même session, sans dépendance entre eux.

---

## Point 1 — Éclatement modulaire des 11 agents restants

### Ce qui a été fait

L'agent 08 avait servi de cas test (commit `c7afbc7`). Les onze autres prompts
monolithiques ont été éclatés selon la **même nomenclature**, commit `53ca630` :

```
meta/projet-unifie/hermes-prompts/NN-<fonction>/
├── NN-principe.md      # invariant : toujours chargé (→ SOUL.md)
└── mandats/*.md        # expertise : chargée à la demande (→ skills/)
```

Règle de découpe, appliquée uniformément :

| Va au **principe** | Va au **mandat** |
|---|---|
| Mission, Archetype served, Zodiac principle, Your sign in Sidy's natal chart, Governance, Scope, Guardrails, Handoffs | Reference & standards, Typical commands, et toute section dont le titre porte « mandate » |

Neuf agents ont un mandat unique. Deux en ont deux, parce que leur prompt en
portait déjà deux : `09-studio-sound-engineer` (`studio-sound-engineer`,
`infrastructure-veille`) et `10-protocol-guardian` (`protocol-guardian`,
`veille-protocole`).

**Les garde-fous restent au principe**, jamais distribués dans les mandats :
aucun mandat chargé à la demande ne doit pouvoir desserrer une interdiction. C'est
la conséquence retenue de la lecture de « Solve et Coagula » — le *coagula* est
l'invariant, et une opération qui ne fait que dissoudre n'est pas une transmutation.

### Vérification mécanique (§VIII.2) — sortie brute

Contrôle de conservation des douze agents, chacun confronté à son monolithe
d'origine relu dans git (`--source-git <ref>^:<chemin>`) :

```
01-ar-music-artistic-direction             PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
02-visual-editorial-artistic-direction     PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
03-production-manager                      PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
04-administration-legal                    PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
05-accounting-management                   PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
06-distribution                            PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
07-marketing-communication                 PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
08-publication-site                        PERDUES : 0 | AJOUTÉES : 14 (14 déclarées, 0 non déclarées) | FUITES : 0 | UNICODE : 0
09-studio-sound-engineer                   PERDUES : 0 | AJOUTÉES : 10 (10 déclarées, 0 non déclarées) | FUITES : 0 | UNICODE : 0
10-protocol-guardian                       PERDUES : 0 | AJOUTÉES : 10 (10 déclarées, 0 non déclarées) | FUITES : 0 | UNICODE : 0
11-fanzine-editor                          PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
12-commerce-profitability                  PERDUES : 0 | AJOUTÉES :  6 (6 déclarées, 0 non déclarées)  | FUITES : 0 | UNICODE : 0
```

**12/12 : aucune ligne perdue, aucun ajout hors de la liste déclarée, aucune
fuite de périmètre, aucun caractère invisible.** Les ajouts déclarés sont les
en-têtes de fichier et l'index des mandats — la découpe est iso-contenu, verbatim,
en anglais. Aucune traduction, aucune condensation : ce serait un changement de
fond déguisé en réorganisation, et invérifiable par construction.

### Défaut trouvé dans mon propre contrôle

Le premier passage a rendu « PERDUES : 346 » **identique pour les douze agents** —
signe qu'un même fichier était relu douze fois. `--source-git` attend un
`REF:chemin` complet, pas un `REF` seul : `git show 53ca630^` renvoie le texte du
commit, pas celui du prompt. Faute dans le contrôle, pas dans les données ; la
mention est ici parce qu'un chiffre uniforme sur douze cas hétérogènes est le
signal qui l'a trahi, et vaut d'être retenu.

### État du déploiement — non fait, et pourquoi

`--derive` confronte chaque fiche du wiki au `SOUL.md` réellement chargé :

```
publication   3595 / 3595   ✅ synchronisé
11 autres                   ⛔ 4 à 27 lignes du wiki absentes du moteur
studio                      ⛔ + 3 caractères Unicode invisibles (Cmd 15)
VERDICT : 11 agent(s) en écart sur 12.
```

Onze agents tournent toujours sur un prompt antérieur aux calibrations zodiacales
et aux mandats votés. **Le déploiement n'a pas été exécuté** : il modifie douze
agents vivants, donc Cmd 13 — porte humaine. Il est présenté à blanc, prêt, en
attente du verdict de Sidy. La procédure est dans
`meta/projet-unifie/hermes-prompts/08-publication-site/deployer-prompt-agent.md`,
éprouvée sur `publication`, seul profil aujourd'hui synchronisé.

Les 3 caractères invisibles de `studio/SOUL.md` sont hors dépôt : ils partiront
avec son déploiement, pas avant.

---

## Point 2 — Contribution de Sidy intégrée au tour sans `@mention`

### Le diagnostic, qui n'était pas celui attendu

La demande — « lorsque je poste dans le salon de la Choura, que ce soit intégré au
tour comme ma contribution sans avoir à mentionner les agents par `@` » — laissait
supposer que le moteur exigeait une mention. **Il ne l'exige pas** : la passerelle
Discord d'un profil reçoit tous les messages des salons listés dans
`discord.allowed_channels` et les passe au modèle.

Le trou n'était pas dans l'écoute, il était dans **l'écriture**. Rien ne versait la
parole de Sidy dans `cycle-AAAA-MM-JJ.md`. Un agent qui se réveille à 2 h du matin
pour son tour ne lit pas l'historique Discord : il lit le fichier de cycle. La
contribution existait dans le salon et n'existait pas dans le tour.

### La réponse

Un hook `pre_llm_call`, `/root/.hermes/scripts/choura-contribution-sidy.py`,
copie de référence dans `meta/projet-unifie/choura/hook-contribution-sidy/`.
Il inscrit le message dans le fichier de cycle avant le marqueur
`## Gabarit d'entrée`, relève `updated:` (Cmd 8), et renvoie le texte en `context`
au tour en cours.

Trois choix de conception qui méritent d'être consignés :

1. **Un hook, pas une consigne de prompt.** Une consigne (« recopie les messages
   de Sidy dans le cycle ») dépend de l'obéissance de l'agent à chaque tour. Un
   hook s'exécute en amont du modèle : il ne peut pas être oublié par un tour
   bavard. §VIII.2, littéralement — fiabilité d'action ≠ fiabilité narrative.
2. **Branché sur le seul `gardien`.** Il tient la veille en permanence et ouvre le
   cycle ; les neuf dormants ne sont éveillés qu'autour de leur tour. Le brancher
   partout produirait une entrée par profil éveillé pour un même message.
3. **La date de cycle bascule à 12:00 heure de Paris**, comme la rotation. Avant
   midi, le cycle courant est celui de la veille — même règle que celle injectée
   dans les douze prompts de tour, sinon un message de 10 h ouvrirait un cycle
   fantôme.

Idempotence par `sha256(session_id|message)`, état borné à 500 entrées. Toute
erreur est avalée : un hook qui échoue ne doit jamais empêcher un agent de répondre.

### Vérification

Trois charges Discord réalistes rejouées à 11:13 heure de Paris :
l'entrée s'est écrite dans `cycle-2026-08-30.md` (correct sous la règle de midi),
rendue en `## [2026-08-31 11:13] sidy (contribution humaine, salon Choura)` ; le
rejeu à l'identique n'a rien réécrit ; une charge portant un autre salon a été
ignorée. L'entrée d'essai et le fichier d'état ont été retirés, le cycle rendu à
son état antérieur.

Enregistrement confirmé dans `agent.log` du gardien, sortie brute :

```
shell hook registered: pre_llm_call -> /root/.hermes/scripts/choura-contribution-sidy.py
  (matcher=None, timeout=15s, fail_closed=False)
```

---

## Ce qui reste ouvert

| Objet | Nature | Qui tranche |
|---|---|---|
| Déploiement des 11 principes vers `SOUL.md` | prêt, présenté à blanc | Sidy (Cmd 13) |
| `OMNIROUTE_API_KEY` divulguée en clair par une expansion shell de ma main | à révoquer et régénérer | Sidy (§VIII.8) |
| Hiérarchie ontologique *zōsaku* absente des 12 prompts (meta/CLAUDE.md, corollaire agentique art. 1) | écart réel, antérieur à ce chantier | Sidy — passe distincte |
| Qualification du joint qabḍ/basṭ : *zōsaku × kari-kumi / homologie* proposé contre *kumiko* | proposition, pas conclusion | Sidy (Cmd 12) |
| Rapprochement Guénon ↔ soufisme (note 15, *contrainte = lier = coagula*) | signalé 🔍, non versé — joint neuf entre formes traditionnelles | Sidy (Cmd 3) |
| 3 fichiers encore contaminés ZWJ (2 archives `.bak`, `library-full.json`) | résidu de l'incident du 2026-08-22 | à finir |
| ACL de `_inbox/` reconstruite plus permissive que l'originale | reconstruction, pas restauration | Sidy |
| Routage réel de `distribution` et `marketing` | inféré de l'absence de 429, non confirmé par une ligne `model=` | à confirmer |

## Deux règles tirées de la passe

- **Ne jamais lancer `hermes --profile X -z` sur un profil dont la passerelle
  tourne** : la vérification arrête l'agent (« stopped by an unexpected signal »).
  Constaté sur `distribution`, à ses dépens.
- **Une panne silencieuse doit être rendue bruyante.** Reprogrammer les tours en
  heure de Paris sans toucher l'orchestrateur de fenêtres aurait laissé chaque
  dormant endormi à son propre tour, **sans lever la moindre erreur** — le symptôme
  exact que la passe venait de diagnostiquer, reproduit par sa propre correction.
  D'où `meta/projet-unifie/choura/orchestrateur/verifier-synchronisation.py`, qui
  confronte les heures réelles des `jobs.json` à la table de l'orchestrateur.
