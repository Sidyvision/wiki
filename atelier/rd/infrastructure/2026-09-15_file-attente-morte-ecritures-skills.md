---
title: "File d'attente morte — 238 écritures de skills stagées, jamais appliquées"
type: infrastructure
tags: [rd, infrastructure, agents, skills, porte-ecriture, anomalie, flotte-hermes]
created: 2026-09-15
updated: 2026-09-15
sources:
  - "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"
  - "https://hermes-agent.nousresearch.com/docs/reference/slash-commands"
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/infrastructure/cartographie-routing-infrastructure]]"
  - "[[atelier/rd/infrastructure/2026-09-15_integration-mcp-ansari]]"
---

# File d'attente morte — écritures de skills stagées, jamais appliquées

> **Objet de cette fiche** : constat, mesures et options de traitement d'une
> anomalie découverte le 2026-09-15 à l'occasion d'une correction de skill.
> **Passe « avant traitement »** : ce document ne modifie rien, aucune écriture
> n'a été faite dans la file. La passe « après traitement » viendra s'ajouter ici
> même, en §7, une fois le traitement décidé et exécuté — un seul document, deux
> passes datées (Cmd 14).
>
> **Relevé** : 2026-09-15 00:14 UTC. Le stock **croît en cours de rédaction** de
> cette fiche : les chiffres du §2 sont datés et à relire, pas à citer de mémoire.

## 1. Le dispositif, tel qu'il est fait

Trois pièces, toutes dans le dépôt `hermes-agent` (hors wiki) :

| Pièce | Rôle |
|---|---|
| `agent/background_review.py` | **Après chaque tour de conversation**, `run_conversation` peut lancer `spawn_background_review` : un **fork de l'agent** rejoue la conversation et se demande « faut-il enregistrer ou modifier un skill, un souvenir ? ». Le fork hérite du fournisseur, du modèle et des credentials du parent. |
| `tools/write_approval.py` | La **porte** : si le sous-système est sous approbation, l'écriture n'est pas appliquée, elle est **stagée** dans `<HERMES_HOME>/pending/skills/<id>.json`. |
| `hermes_cli/write_approval_commands.py` | La **seule surface de dépouillement** : `/skills pending`, `/skills approve <id>`, `/skills reject <id>`, `/skills diff <id>`, `/skills mode` — partagée entre la CLI et les gateways. |

Deux réglages, dans `config.yaml` : `skills.write_approval` (porte) et
`background_review.enabled` (commutateur maître du fork ; défaut `true`, non
déclaré dans le `config.yaml` racine — donc actif par défaut).

**Rien dans Hermes ne dépouille cette file automatiquement.** Aucun cron, aucun
service, aucune alerte : la porte retient, et c'est tout.

## 2. Les faits mesurés — flotte entière

| Profil | Positions en attente | Première | Dernière |
|---|---:|---|---|
| `default` | **168** | 2026-08-08 | 2026-09-15 |
| `gardien` | 24 | 2026-08-16 | 2026-08-25 |
| `studio` | 16 | 2026-08-17 | 2026-09-13 |
| `publication` | 5 | 2026-08-25 | 2026-09-13 |
| `marketing` | 2 | 2026-08-07 | 2026-08-07 |
| **TOTAL** | **215** | 2026-08-07 | 2026-09-15 |

- **238 opérations stagées** (215 enregistrements, certains portant plusieurs
  opérations) — environ **860 Ko** de contenu proposé, au seul profil `default`.
- **105 skills distincts** visés, dont **aucun** — zéro — n'est installé. Aucune
  position de cette file n'est jamais arrivée à destination.
- **29 paires (skill, action) répétées**, couvrant **92 positions** : le même
  skill proposé deux fois ou plus, jusqu'à **29 fois** pour
  `hermes-multi-profile-ops` (depuis le 2026-08-08).
- **Toutes** les positions portent l'origine `background_review` : la file est
  intégralement le produit du fork, et **aucune** n'est une écriture demandée en
  session par Sidy.
- Rythme : ~4,5 positions/jour au profil `default`. Le dispositif produit
  toujours, à l'heure de cette fiche (dernier arrivé : `30e4f9e1`, 00:10).

### L'asymétrie des deux portes

| Sous-système | Porte | Effet |
|---|---|---|
| `skills` | **`write_approval: true`** — dans **12 profils sur 13** | les compétences sont **retenues** |
| `memory` | `write_approval: false` | les souvenirs sont **appliqués directement** |

L'agent **se souvient** donc de tout depuis six semaines — et n'**apprend** rien.
Douze profils portent la porte à `true` ; seul `karubi` ne l'a pas déclarée, et
n'a de ce fait aucune file.

## 3. Diagnostic — la lecture, séparée du fait

1. **Le fork travaille pour une boîte morte.** Il examine chaque tour, produit une
   proposition argumentée, et cette proposition n'a **aucun chemin** vers
   l'application sans un geste humain qui n'a jamais eu lieu. Depuis le 2026-08-07 :
   38 jours, 215 propositions, 0 application.
2. **Il ne peut pas le savoir.** Le fork ne consulte pas la file : il ne voit pas
   qu'il a déjà proposé 28 fois `hermes-multi-profile-ops`. Les doublons ne sont pas
   un défaut de qualité de ses propositions, c'est la **preuve** de son aveuglement
   sur la file. Il repart de la conversation, pas du stock.
3. **Le coût est réel et invisible.** Un fork LLM par tour de conversation, dans
   chaque profil actif, dont le produit est jeté par construction. Aucun poste de
   dépense ne le nomme ; aucun rôle ne le surveille.
4. **C'est un silence, pas une panne.** Rien ne casse : les sessions tournent, les
   gateways répondent, les rapports sortent. C'est précisément ce qui rend le fait
   sérieux — *un contrôle qui ne crie jamais n'est pas un contrôle vert, c'est un
   contrôle muet.* Il n'existe aujourd'hui **aucun** indicateur qui aurait signalé
   cette file, dans aucun des rapports périodiques de la flotte.
5. **Conséquence sur ce qui a pu être affirmé.** Toute formulation passée du type
   « compétence apprise / skill créé » à propos du travail d'un agent est, sur cette
   période, **fausse par construction** — sauf pour l'unique position appliquée à la
   main (§4). Il n'y a pas lieu de supposer une intention : il y a lieu de constater
   que l'affirmation n'était vérifiable par rien.

**Ce que ce n'est pas** : ni une contamination, ni un crash, ni une perte de
données. Rien n'a disparu — tout est **retenu**, et lisible.

## 4. Les deux positions sorties de la file ce jour

| Position | Nature | Sort |
|---|---|---|
| `1c523999` | patch de `hermes-agent` — deux pièges du `hermes mcp add` (interactif ; `HERMES_PROFILE` ignoré) | **appliquée à la main** (patch direct du fichier, contenu relu par le chargeur de skills), puis **rejetée** de la file pour éviter une double application |
| `30e4f9e1` | propositions de `mcp-server-integration` et `wiki-corpus-journaling`, 4 opérations | **en attente**, non touchée. Ironie utile : le fork propose, en fin de session, la compétence qui décrirait **le travail que cette session vient de faire**. |

Le premier cas montre la seule voie praticable aujourd'hui pour faire sortir une
position : **à la main, hors de la file** — la surface `/skills approve` n'étant
accessible que dans une session ouverte, et pas depuis un shell.

## 5. Options de traitement (aucune engagée)

| # | Option | Effet | Coût / risque |
|---|---|---|---|
| **A** | Dépouiller la file : `/skills pending` puis `approve`/`reject` position par position, profil par profil | fidèle à l'intention de la porte ; 105 skills éventuels | 215 décisions humaines ; impraticable tel quel |
| **B** | **Dédupliquer d'abord**, puis juger : les 29 paires (skill, action) redites couvrent 92 positions ; n'en garder qu'une par paire, rejeter les 63 redites, puis revue groupée des survivantes | 215 → **152** positions, 105 noms ; revue par sujet au lieu d'une revue par position | demande une règle de dédup assumée (quelle position garde-t-on ?) |
| **C** | **Éteindre la porte** (`skills.write_approval: false` sur chaque profil) et vider la file | retour au régime antérieur au 08/08 : le fork écrit directement | réintroduit des écritures de skills **non revues** ; l'effet est immédiat et silencieux lui aussi |
| **D** | **Éteindre le fork** (`background_review.enabled: false`) — éventuellement au cas par cas, en le gardant là où il sert | supprime la source : plus de propositions mortes | supprime aussi la capture automatique des **souvenirs**, qui, elle, fonctionne (`memory.write_approval: false`) — sauf à distinguer les deux, ce que la configuration ne permet pas aujourd'hui |

Deux constats entrent dans le choix, et sont de simples mesures : la file ne
contient **que** du `background_review` (§2), donc l'éteindre ne priverait d'aucune
écriture demandée en session ; et **105 noms pour 215 positions**, dont aucun
n'est installé, signifie que la question n'est pas « approuver ou rejeter 215
choses » mais **« veut-on 105 skills de plus, ou très peu ? »**.

**Recommandation, soumise et non exécutée** : **B puis D partiel** — dédupliquer et
juger par sujet (quelques candidats nets : `mcp-server-integration`,
`hermes-multi-profile-ops`, `wiki-change-journaling`), puis décider du fork en
connaissance de cause : le garder pour la mémoire et couper son versant skills
n'étant pas exprimable dans la configuration actuelle, le point se tranche entre
« tout garder » et « tout couper ».

## 6. Entrée de registre préparée, NON déposée

Le cas a sa place au `atelier/rd/cahiers/registre-problemes.md` (symptôme /
diagnostic / résolution / compréhension tirée). **Elle n'y a pas été déposée** :
c'est le même régime que l'entrée du 2026-09-13, dont l'écriture au registre a
exigé de Sidy une **levée nominative** de l'interdiction portée par un mandat.
Texte prêt, à déposer sur un mot de Sidy :

> **## [2026-09-15] Une porte qui retient depuis 38 jours, sans que rien ne le dise**
> **Symptôme** : `skills.write_approval: true` dans 13 profils ; 215 positions
> stagées du 2026-08-07 au 2026-09-15 (238 opérations, 105 skills distincts) ;
> **aucune** n'a jamais été appliquée ; 92 positions sont des redites du même
> skill. Toutes d'origine `background_review`, aucune demande humaine.
> **Diagnostic** : la porte n'est pas défaillante — elle *retient* : c'est sa
> fonction. Ce qui manque est une **surface de dépouillement praticable** et un
> **signal** : la file était invisible de tout rapport périodique, et le fork
> ignore son propre stock, d'où les redites.
> **Résolution** : (à trancher) — options A/B/C/D du §5.
> **Compréhension tirée** : un mécanisme d'écriture sous approbation **sans
> indicateur de file** n'est pas un garde-fou, c'est un puits. Tout dispositif
> qui *retient* doit publier **ce qu'il retient** ; sinon le contrôle est vert
> parce que personne ne le regarde, ce que §VII refuse déjà ailleurs.
> **Statut** : `ouvert`

## 7. Passe « après traitement » — étape 1 : déduplication exécutée

**Verdict de Sidy du 2026-09-15** (formulaire) : « Dédupliquer puis juger par sujet — je dédup les 62 redites, je vous présente la liste courte des candidats, le reste est rejeté. » Puis, sur la seconde question : « Oui, dépose-la maintenant — c'est mon accord nominatif » (entrée de registre, cf. §6).

### Ce qui a été fait (2026-09-15, ~00:45 UTC)

- **Règle appliquée** : pour chaque couple (skill, action), une seule position survit — la plus récente. Une proposition identique répétée est une redite, pas un renforcement.

- **Mesure** : **215 positions → 155**, soit **60 rejetées** (`default` 55, `studio` 2, `gardien` 3 ; `publication` et `marketing` sans redite).

- **Voie employée** : `write_approval.discard_pending` — la fonction même qu'appelle `/skills reject`. Aucun fichier détruit : chaque position rejetée est **copiée** dans `pending/skills/rejetees-2026-09-15/` du profil concerné, avec un `MANIFESTE.md` qui porte la règle, la liste et la procédure de restauration (Cmd 10).

- **Écart déclaré** : la fiche annonçait 62 redites (relevé de 00:14) ; la règle exacte appliquée à 00:45 en mesure **60**. Le stock bouge pendant qu'on le compte — c'est la réserve inscrite en tête de fiche, pas une correction.


### Ce qui reste à juger — 155 positions, 105 sujets

La déduplication exacte ne suffit pas : **105 sujets distincts subsistent**, dont beaucoup sont des quasi-synonymes du même objet (le premier jeton du nom les regroupe). La liste ci-dessous est donc présentée **par grappe**, la plus lourde d'abord ; dans chaque grappe, seule la plus volumineuse est proposée comme **candidat**, les autres comme **rejetables** (redites de sujet). Proposition mécanique, soumise — pas décidée.

| grappe | sujet | pos. | poids | dernier dépôt | profil | proposition |
|---|---|---:|---:|---|---|---|
| wiki | wiki-change-journaling | 1 | 24620 o. | 2026-09-13 | default | **candidat** |
| wiki | wiki-infra-correctifs | 2 | 21776 o. | 2026-09-13 | studio | rejetable |
| wiki | wiki-depot-integration | 4 | 20656 o. | 2026-08-30 | publication | rejetable |
| wiki | wiki-graph-maintenance | 2 | 15133 o. | 2026-08-18 | studio | rejetable |
| wiki | wiki-depot-correctifs-forme | 1 | 15104 o. | 2026-09-13 | publication | rejetable |
| wiki | wiki-transcription-bibliotheque | 2 | 13044 o. | 2026-08-29 | default | rejetable |
| wiki | wiki-protocol-ops | 2 | 12486 o. | 2026-08-08 | default | rejetable |
| wiki | wiki-sidyvision-protocol | 2 | 12403 o. | 2026-09-02 | default | rejetable |
| wiki | wiki-protocol | 2 | 9758 o. | 2026-08-08 | default | rejetable |
| wiki | wiki-corpus-integration | 2 | 9043 o. | 2026-08-24 | studio | rejetable |
| wiki | wiki-rd-methodology | 2 | 8959 o. | 2026-08-15 | default | rejetable |
| wiki | wiki-depot-restoration | 2 | 8819 o. | 2026-08-23 | gardien | rejetable |
| wiki | wiki-repository-ops | 2 | 8482 o. | 2026-08-09 | default | rejetable |
| wiki | wiki-repo-governance | 2 | 8194 o. | 2026-08-08 | default | rejetable |
| wiki | wiki-transmission | 1 | 8058 o. | 2026-08-31 | default | rejetable |
| wiki | wiki-depot-ops | 2 | 7565 o. | 2026-08-09 | default | rejetable |
| wiki | wiki-depot-restauration | 2 | 7080 o. | 2026-08-23 | gardien | rejetable |
| wiki | wiki-doctrinal-depot | 1 | 7028 o. | 2026-08-31 | default | rejetable |
| wiki | wiki-vault-sync | 2 | 6707 o. | 2026-08-09 | default | rejetable |
| wiki | wiki-protocol-v2 | 2 | 6508 o. | 2026-08-08 | default | rejetable |
| wiki | wiki-structural-grounding | 1 | 6050 o. | 2026-08-30 | default | rejetable |
| wiki | wiki-interview-deposit | 2 | 5867 o. | 2026-08-18 | default | rejetable |
| wiki | wiki-repo-verification | 2 | 5581 o. | 2026-08-09 | default | rejetable |
| wiki | wiki-source-integration | 2 | 5285 o. | 2026-08-28 | studio | rejetable |
| wiki | wiki-integration | 1 | 5002 o. | 2026-08-18 | default | rejetable |
| wiki | wiki-inbox-ventilation | 1 | 4510 o. | 2026-08-22 | default | rejetable |
| wiki | wiki-invariant-maintenance | 1 | 4500 o. | 2026-08-18 | studio | rejetable |
| hermes | hermes-gateway-operations | 2 | 19467 o. | 2026-09-13 | default | **candidat** |
| hermes | hermes-multi-profile-ops | 2 | 17466 o. | 2026-08-25 | default | rejetable |
| hermes | hermes-multi-profile | 2 | 12642 o. | 2026-08-23 | default | rejetable |
| hermes | hermes-character-profiles | 2 | 11972 o. | 2026-08-15 | default | rejetable |
| hermes | hermes-operations | 2 | 10567 o. | 2026-09-10 | default | rejetable |
| hermes | hermes-profile-operations | 2 | 10491 o. | 2026-08-17 | default | rejetable |
| hermes | hermes-infra-ops | 2 | 8672 o. | 2026-08-23 | default | rejetable |
| hermes | hermes-profile-orchestration | 2 | 8653 o. | 2026-08-20 | default | rejetable |
| hermes | hermes-infra-diagnostics | 2 | 8185 o. | 2026-08-28 | default | rejetable |
| hermes | hermes-multiprofile-ops | 2 | 6825 o. | 2026-09-11 | default | rejetable |
| hermes | hermes-gateway-orchestration | 1 | 6610 o. | 2026-08-30 | default | rejetable |
| hermes | hermes-scoped-gateway | 1 | 6325 o. | 2026-08-16 | default | rejetable |
| hermes | hermes-agent-prompt-deployment | 1 | 5848 o. | 2026-08-16 | gardien | rejetable |
| hermes | hermes-cron-orchestration | 1 | 5451 o. | 2026-08-24 | default | rejetable |
| hermes | hermes-profile-ops | 1 | 4330 o. | 2026-09-07 | default | rejetable |
| hermes | hermes-profile-isolation | 1 | 3875 o. | 2026-08-15 | default | rejetable |
| mcp | mcp-server-integration | 1 | 23198 o. | 2026-09-15 | default | **candidat** |
| mcp | mcp-server-authoring | 2 | 9597 o. | 2026-09-08 | default | rejetable |
| github | github-automation-infrastructure | 2 | 9071 o. | 2026-08-28 | default | **candidat** |
| github | github-repo-audit | 1 | 7949 o. | 2026-08-31 | default | rejetable |
| github | github-issue-authoring | 1 | 5396 o. | 2026-09-05 | default | rejetable |
| github | github-config | 1 | 3767 o. | 2026-09-06 | default | rejetable |
| github | github-repo-setup | 1 | 3709 o. | 2026-08-28 | default | rejetable |
| github | github-wiki-automation | 1 | 1616 o. | 2026-08-28 | default | rejetable |
| depot | depot-doctrinal-integration | 2 | 13014 o. | 2026-08-25 | gardien | **candidat** |
| depot | depot-integrity-workflow | 1 | 9237 o. | 2026-08-18 | studio | rejetable |
| depot | depot-restauration | 2 | 8901 o. | 2026-08-23 | gardien | rejetable |
| doctrinal | doctrinal-integration | 2 | 11616 o. | 2026-08-25 | gardien | **candidat** |
| doctrinal | doctrinal-wiki-ingest | 1 | 7015 o. | 2026-08-20 | gardien | rejetable |
| doctrinal | doctrinal-source-integration | 1 | 6085 o. | 2026-08-25 | publication | rejetable |
| doctrinal | doctrinal-source-ingestion | 1 | 5912 o. | 2026-08-30 | default | rejetable |
| structured | structured-wiki-methodology | 1 | 11254 o. | 2026-08-31 | default | **candidat** |
| structured | structured-spiritual-interview | 1 | 6917 o. | 2026-08-18 | default | rejetable |
| structured | structured-depot-methodology | 1 | 6260 o. | 2026-08-31 | default | rejetable |
| karubi | karubi-provisioning | 2 | 13312 o. | 2026-08-21 | gardien | **candidat** |
| karubi | karubi-transmissions | 2 | 7566 o. | 2026-08-21 | gardien | rejetable |
| scanned | scanned-book-to-markdown | 2 | 9492 o. | 2026-09-02 | default | **candidat** |
| scanned | scanned-book-to-markdown-corpus | 2 | 9205 o. | 2026-09-02 | default | rejetable |
| governed | governed-correction-pass | 1 | 17905 o. | 2026-09-13 | studio | **candidat** |
| external | external-material-integration | 2 | 9366 o. | 2026-09-05 | default | **candidat** |
| external | external-research-integration | 1 | 7329 o. | 2026-08-31 | default | rejetable |
| studio | studio-documentation | 2 | 16459 o. | 2026-08-07 | marketing | **candidat** |
| frontmatter | frontmatter-repair-pass | 1 | 15793 o. | 2026-09-13 | publication | **candidat** |
| book | book-scan-to-markdown-corpus | 2 | 13483 o. | 2026-09-02 | default | **candidat** |
| scan | scan-to-verified-corpus | 3 | 12520 o. | 2026-09-02 | default | **candidat** |
| sidy | sidy-wiki-protocol | 2 | 9022 o. | 2026-08-15 | default | **candidat** |
| sidy | sidy-wiki-interview | 1 | 3172 o. | 2026-08-18 | default | rejetable |
| scoped | scoped-correspondent-channel | 2 | 10901 o. | 2026-08-21 | gardien | **candidat** |
| taabir | taabir-ruya | 1 | 10076 o. | 2026-09-07 | default | **candidat** |
| yaml | yaml-frontmatter-batch | 1 | 9980 o. | 2026-08-30 | default | **candidat** |
| pdf | pdf-book-conversion | 1 | 8390 o. | 2026-09-05 | default | **candidat** |
| open | open-source-project-investigation | 1 | 8275 o. | 2026-08-31 | default | **candidat** |
| structural | structural-invariant-repair | 1 | 8071 o. | 2026-08-17 | studio | **candidat** |
| photo | photo-page-transcription | 2 | 7976 o. | 2026-08-29 | default | rejetable |
| multi | multi-agent-collaboration | 1 | 5969 o. | 2026-08-20 | default | rejetable |
| multi | multi-profile-cron-fleet | 1 | 1880 o. | 2026-08-27 | default | rejetable |
| cron | cron-multi-profile-ops | 1 | 7130 o. | 2026-08-30 | default | rejetable |
| astrology | astrology-ephemeris | 2 | 6916 o. | 2026-08-08 | default | rejetable |
| git | git-hooks | 1 | 6693 o. | 2026-08-22 | default | rejetable |
| rd | rd-veille | 1 | 6411 o. | 2026-08-18 | default | rejetable |
| document | document-archival | 1 | 6399 o. | 2026-08-20 | gardien | rejetable |
| daily | daily-agent-report-processing | 1 | 6130 o. | 2026-08-30 | default | rejetable |
| content | content-security-audit | 1 | 6101 o. | 2026-08-22 | default | rejetable |
| atelier | atelier-materiel-documentation | 1 | 5632 o. | 2026-08-18 | default | rejetable |
| deterministic | deterministic-integrity-tooling | 1 | 5099 o. | 2026-08-15 | default | rejetable |
| agents | agents-circuits-wiki | 1 | 4955 o. | 2026-08-23 | default | rejetable |
| choura | choura-orchestration | 1 | 4542 o. | 2026-09-01 | default | rejetable |
| discord | discord-operations | 1 | 4498 o. | 2026-08-16 | gardien | rejetable |
| biographical | biographical-interview-deposit | 1 | 4379 o. | 2026-08-22 | default | rejetable |
| authenticated | authenticated-web-automation | 1 | 4352 o. | 2026-08-18 | default | rejetable |
| research | research-paper-analysis | 1 | 4004 o. | 2026-08-22 | default | rejetable |
| reminiscence | reminiscence-interview | 1 | 3883 o. | 2026-08-18 | default | rejetable |
|  |  | 1 | 3088 o. | 2026-08-18 | default | rejetable |
| sidyvision | sidyvision-wiki | 1 | 2760 o. | 2026-08-31 | default | rejetable |
| protocol | protocol-driven-repository | 1 | 2695 o. | 2026-08-31 | default | rejetable |
| sanad | sanad-wiki-maintenance | 1 | 2168 o. | 2026-08-27 | default | rejetable |
| infrastructure | infrastructure-operations | 2 | 1749 o. | 2026-08-28 | default | rejetable |
| autonomous | autonomous-ai-agents:hermes-agent | 1 | 1209 o. | 2026-08-27 | default | rejetable |

**Total : 105 sujets — 22 candidats nets (≥ 8000 o.), 83 rejetables.**

Rien n'est rejeté à ce stade : la liste est soumise, le jugement se fait par grappe, sur un mot. La porte et le fork restent **inchangés** — les options C et D du §5 demeurent ouvertes.

### Étape 2 — jugement par sujet, exécuté (2026-09-15, ~00:40 UTC)

**Verdict de Sidy**, consigné verbatim : « Mais il suffit d'accepter les requêtes légitimes et c'est tout », puis, en cours de passe : « oui crée le skill s'il est légitime et bon pour l'infrastructure ».

**Trois règles déclarées**, appliquées à la lettre :

1. **R1** — une requête qui redit une autre requête n'est pas une requête légitime *distincte* : une seule survit, la plus complète. L'examen des descriptions a montré 13 variantes pour « travailler dans `/root/wiki` », 8 pour « flotte Hermes », 7 pour « scan/OCR » : la liste mécanique de 80 « approuvables » de l'étape 1 était donc trompeuse — elle triait par volume, pas par sujet.
2. **R2** — une requête qui refait un skill **déjà installé** n'est pas appliquée (ex. toute la famille `github-*`, qui refaisait `github-issues`, `github-repo-management`, `github-pr-workflow` ; `research-paper-analysis`, qui refaisait `research-paper-writing` ; `wiki-vault-sync`, qui refaisait `obsidian`).
3. **R3** — tout ce qui touche la personne, la transmission, le doctrinal, les interviews ou les dispositifs nominatifs est **réservé** : ni approuvé, ni rejeté, laissé dans la file au verdict de Sidy.

**Résultat mesuré** : **11 skills créés**, **118 positions rejetées** (archivées), **30 positions réservées** laissées dans la file.

| Profil | Skill créé | Poids |
|---|---|---:|
| `default` | `mcp-server-integration` | 7 495 o. |
| `default` | `wiki-change-journaling` | 7 122 o. |
| `default` | `hermes-gateway-operations` | 7 175 o. |
| `default` | `scan-to-verified-corpus` | 6 882 o. |
| `default` | `open-source-project-investigation` | 7 831 o. |
| `default` | `rd-veille` | 6 060 o. |
| `default` | `multi-agent-collaboration` | 5 560 o. |
| `default` | `git-hooks` | 6 190 o. |
| `default` | `astrology-ephemeris` | 3 477 o. |
| `gardien` | `discord-operations` | 3 870 o. |
| `studio` | `governed-correction-pass` | 7 123 o. |

**Vérification indépendante** : les 11 `SKILL.md` sont sur le disque, frontmatter YAML valide, nom conforme, description ≤ 60 caractères — **11/11**. Contrôle croisé par le chargeur : `hermes skills list --source local` les liste en `local / enabled`. Aucune de ces affirmations ne repose sur l'auto-rapport du script d'application.

#### Le second défaut, découvert en appliquant

**Cinq des onze requêtes retenues n'auraient pas pu être appliquées même porte ouverte.** Le magasin de skills refuse toute description dépassant **60 caractères** (« must fit the 60-char system-prompt budget — one sentence, trigger first, ends with a period ») et deux des frontmatter YAML proposés étaient invalides (deux-points dans une valeur non guillemetée). Ce sont des propositions **inaptes au magasin qu'elles visaient**.

La forme a donc été réparée — et **seulement la forme** : la ligne `description:` du frontmatter a été remplacée par une phrase de ≤ 60 caractères (ce qui répare du même coup les deux YAML invalides, en bornant le bloc). **Aucun autre octet du contenu proposé n'a été touché.** L'enregistrement d'origine de chaque requête ainsi corrigée est copié dans l'archive (`applique-forme-reparee-<id>.json`) : la version appliquée ne se substitue pas, dans la trace, à la version proposée.

Conséquence pour le diagnostic du §3 : la porte n'était pas le seul obstacle. Un dispositif qui **retient** des écritures que le magasin **refusera** produit exactement le même silence — et de fait, la file contenait les deux.

#### Rejet et réserve, réversibles

Les 118 positions rejetées sont **copiées** avant retrait dans `pending/skills/rejetees-2026-09-15/` du profil concerné (188 copies au total avec la passe de déduplication), et la même voie a été employée que pour l'étape 1 : `write_approval.discard_pending`, la fonction de `/skills reject` (Cmd 10).

Les 30 réservées — familles `karubi-*`, `transmission`, `doctrinal-*`, `wiki-doctrinal`, interviews (`sidy-wiki-interview`, `structured-spiritual-interview`, `reminiscence-interview`, `biographical-interview-deposit`), `hermes-character-profiles` (zones sacrées/profanes), `hermes-scoped-gateway` et `scoped-correspondent-channel` (isolation de compte Unix), `deterministic-integrity-tooling` (sceaux) — **restent dans la file, intactes**. Elles attendent un verdict nominatif, sujet par sujet.

#### Ce qui n'est pas résolu

- **La question du fork et de la porte (options C et D du §5) n'est pas tranchée.** Le fait qui pèse dessus est désormais double : la file se remplit toute seule (une position de plus pendant cette session), et une part de ce qu'elle contient est inapte par construction — donc **le silence se reformera**, sous deux formes au lieu d'une.
- **Un signal manque toujours.** Rien ne publie l'état de la file ; c'est le défaut de fond du §3, il n'est pas corrigé.
- **Les 30 réservées n'ont pas été jugées.**

