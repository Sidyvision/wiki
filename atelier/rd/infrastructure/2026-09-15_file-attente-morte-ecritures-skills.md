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

## 7. Passe « après traitement »

*(à écrire — traitement non décidé à l'heure de cette fiche)*
