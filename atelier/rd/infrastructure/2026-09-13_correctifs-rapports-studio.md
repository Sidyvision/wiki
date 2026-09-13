---
title: "Correctifs des rapports de monitoring Studio — exécution du 2026-09-13"
type: infrastructure
tags: [rd, infrastructure, monitoring, hermes, correctifs]
created: 2026-09-13
updated: 2026-09-13
sources: []
links:
  - "[[atelier/rd/infrastructure/monitoring-archive-charte]]"
  - "[[atelier/rd/infrastructure/monitoring-archive/registre-traitement]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
  - "[[atelier/rd/cahiers/journal-optimisations]]"
  - "[[atelier/rd/registre-chantiers]]"
original: []
infra_verif:
  - profil: studio
    cron_job: monitoring-infrastructure-quotidien
  - profil: studio
    discord_home_channel: "1536564394690084925"
---

# Correctifs des rapports de monitoring Studio — exécution du 2026-09-13

## 1. Motif et cadre

**Consigne de Sidy, `#infrastructure`, 2026-09-13** : « execute les correctifs
signalés dans tes rapports ». Elle porte sur les **propositions** des deux
derniers rapports quotidiens du pôle Studio — celui du 2026-09-12 et celui du
2026-09-13 (`§4.3` pistes 1–5, `§5.1–4`) — rédigées, comme le veut le mandat,
en **signalement** et non en actes (Discord-Validation).

**Pourquoi cette fiche existe.** La règle de validation est **conditionnelle** :
l'accord de Sidy sur un lot de propositions vaut à condition que la
documentation soit **en place avant l'exécution**, et cette fiche est le
**contrat** entre la session Hermes qui exécute et la revue Claude Code qui
auditera après coup. Chaque correctif y est donc nommé, mesuré, daté — et
**chaque écart aux règles en vigueur y est déclaré**, jamais silencieux
(§VII racine, *Épreuve des contrôles* ; Cmd 12).

**Ce que cette passe n'est pas.** Aucun correctif n'est appliqué « au passage » :
les six propositions ci-dessous sont exactement celles des rapports, ni plus
(rien n'est inventé) ni moins (rien n'est absorbé). Ce qui n'est pas exécuté
l'est pour un motif nommé (§3), pas par omission.

## 2. Correctifs exécutés

| Code | Correctif | Source | Nature |
|---|---|---|---|
| **C1** | Corriger le **prompt du job cron** `monitoring-infrastructure-quotidien` : chemin mort du script de cartographie, décompte faux des gateways | rapport 09-13 §4.3 **Piste 1**, §5.1 | hors dépôt (config Hermes, profil `studio`) |
| **C2** | **Committer** les 4 archives de rapports non suivies par git et poser leurs **entrées de traitement** | rapport 09-13 §4.3 **Piste 2**, §5.2 | dépôt — `monitoring-archive/` |
| **C3** | **Étendre et éprouver** le contrôle A de `verifier-invariants.py` aux cahiers append-only, et remettre en cohérence ce qu'il mord | rapport 09-13 §4.3 **Piste 3**, §5.4 | dépôt — outillage |
| **C4** | **Recompter** le §0 du registre des chantiers depuis ses propres lignes et **verser `INF-15` en §9** | rapport 09-13 §4.3 **Piste 4** | dépôt — registre |

### C1 — le prompt du cron portait un chemin mort (2ᵉ jour)

Mesure brute, telle que la consigne d'exécution la prescrit :

```
$ python3 Graphe/generer-cartographie.py --depot /root/wiki --verifier
python3: can't open file '/root/wiki/Graphe/generer-cartographie.py': [Errno 2] No such file or directory
exit_code: 2
```

Le script vit en `atelier/rd/outillage/graphe/` depuis le 2026-08-31. Deux
défauts dans le même prompt, tous deux corrigés : le **chemin mort** (le rapport
commençait par un `exit 2`) et le **décompte des gateways** (« santé des
**12** gateways » là où il y a **13** unités systemd et **14** profils, et où
`list-units` seul ne montre que les unités *chargées* — leçon de l'entrée
`[2026-09-01]` du registre des problèmes, « commerce absent du relevé »).

**Vérification exigée** : relecture du prompt persisté après édition (`jobs.json`)
**et** exécution réelle de la commande corrigée — jamais la seule foi d'un
`last_status: ok` (§VIII.2 du protocole racine).

### C2 — quatre archives hors de git, zéro entrée de traitement

Deux contrôles indépendants désignent **les mêmes fichiers** — c'est la
démonstration que le défaut est réel et non un artefact de l'un d'eux :

```
$ python3 atelier/rd/outillage/verifier-rapports-traites.py --racine /root/wiki
Registre : 26 entrée(s) de traitement.
Archives : 31 fichier(s) total, dont 14 antérieur(s) à l'ouverture du registre (2026-09-02, hors périmètre).

4 rapport(s) SANS entrée de traitement :
  ! atelier/rd/infrastructure/monitoring-archive/2026-09-12_41dc3e7e492c.txt
  ! atelier/rd/infrastructure/monitoring-archive/2026-09-12_ad3152b237bb.txt
  ! atelier/rd/infrastructure/monitoring-archive/2026-09-13_41dc3e7e492c.txt
  ! atelier/rd/infrastructure/monitoring-archive/2026-09-13_ad3152b237bb.txt

$ python3 atelier/rd/outillage/detecter-non-tracke.py --racine /root/wiki
  4 fichier(s) non tracké(s), par circuit :

  [atelier] 4
    ??  atelier/rd/infrastructure/monitoring-archive/2026-09-12_41dc3e7e492c.txt
    ??  atelier/rd/infrastructure/monitoring-archive/2026-09-12_ad3152b237bb.txt
    ??  atelier/rd/infrastructure/monitoring-archive/2026-09-13_41dc3e7e492c.txt
    ??  atelier/rd/infrastructure/monitoring-archive/2026-09-13_ad3152b237bb.txt
```

Le rapport du 09-13 comptait **3** fichiers ; ils sont **4** depuis la production
du rapport du jour même (l'archivage fonctionne, c'est le maillon suivant qui
manquait). Les quatre reçoivent une entrée **une par rapport**, jamais par lot —
c'est la règle d'usage du registre lui-même.

> **⚠ Écart déclaré (C2).** La charte de `registre-traitement.md` porte :
> « **Qui écrit ici** : Sidy directement, ou une session Claude Code sous
> consigne explicite — même gouvernance que `queue-idees.md`. **Les agents
> Hermes eux-mêmes n'écrivent jamais ici** (Discord-Validation, comme partout
> ailleurs : signalement seulement). »
>
> Cette passe y écrit **quatre entrées**, sur la **consigne explicite et
> nominative de Sidy** du 2026-09-13 — c'est-à-dire par la porte que la règle
> nomme elle-même (Discord-Validation levée par Sidy, Cmd 13). L'écart est
> **déclaré ici, visible au dépôt, réversible par `git revert`** ; si la lecture
> juste est que la clause « les agents Hermes n'écrivent jamais ici » n'est pas
> levable par une consigne en canal, la correction est un seul commit arrière.
> Deux des quatre entrées portent en outre leur motif propre : les rapports
> **Publication** sont archivés et commités ici, leur **contenu n'est pas
> instruit** par la session Studio (mandat distinct, consigne parallèle adressée
> au profil `publication`) — l'entrée le dit en clair plutôt que de laisser
> croire à un traitement.

### C3 — trois cahiers append-only hors contrôle, et le contrôle éprouvé

Trois fichiers portaient la discipline des annales (Cmd 8 : `updated:` cohérent
avec l'entrée la plus récente) **sans partager sa garde** : `verifier-invariants.py`
n'appliquait A0–A6 qu'aux seuls `annales.md` / `meta-annales.md`.

**Inspection préalable exigée par le rapport (§5.4)** — « ne pas livrer un
contrôle qui rougit sur ce qui n'est pas une faute ». Constats mesurés avant
d'écrire une ligne de code :

- `registre-traitement.md` **n'est pas** en ordre chronologique inverse : son
  en-tête d'insertion est `<!-- INSERTION: EN-TÊTE -->`, mais ses entrées se
  suivent dans l'**ordre des passes de traitement** (`[09-08] studio`, puis
  `[09-10] publication`, puis `[09-08] publication` — la dernière entrée posée
  concerne un rapport plus ancien). Lui appliquer **A2** (dates non croissantes)
  l'aurait fait rougir sur ce qui est sa discipline réelle. **A2 est donc
  écarté** pour les cahiers, et le motif est inscrit dans le code.
- `registre-problemes.md` : `updated: 2026-09-09`, entrée la plus récente
  `[2026-09-04]`. Le rapport signalait là « un écart de 5 jours, non signalé
  jusqu'ici » : **c'est faux, et l'inspection le montre** — A3 exige seulement
  `updated ≥ entrée la plus récente` ; 09-09 ≥ 09-04, le fichier est **sain**.
  La « staleness » de la dernière entrée n'est pas une faute et n'est pas
  contrôlée.
- `journal-optimisations.md` : `updated: 2026-09-02`, entrée la plus récente
  `[2026-09-13]` → **9 jours d'écart, faute réelle** au sens de Cmd 8.

**Le geste** : une liste **nommée** (`CAHIERS_APPEND_ONLY`), jamais un glob —
le dépôt refuse les passes de masse —, et l'application aux cahiers des **seuls
invariants qui les décrivent** : **A3** (`updated` vs entrée la plus récente) et
**A4** (en-tête dupliqué). A2, A5 et A6 sont des empreintes de corps d'annales,
non des règles de registre : les y appliquer eût été de l'accumulation, pas de
la précision.

**Épreuve exigée (§VII racine, *Épreuve des contrôles*)** : un contrôle dont on
n'a pas vu l'échec n'est pas un contrôle vérifié. Les deux faces sont observées
dans un bac à sable jetable, jamais dans le dépôt vivant : vert sur l'état sain,
**refus sur la faute fabriquée exprès** (`updated:` reculé), puis remise de
l'état sain. Les deux résultats sont consignés aux annales — « vert sur X, refus
sur Y » — et non le seul vert.

### C4 — le §0 du registre des chantiers divergeait de ses propres lignes

Recompte mécanique des tableaux §1–§7 depuis les lignes elles-mêmes :

| Pôle | ouvert | en-cours | bloqué | attente-verdict | total | Écart au §0 |
|---|---|---|---|---|---|---|
| `INS` | 9 | 2 | 1 | 3 | 15 | — |
| `INF` | 8 | 3 | 1 | **2** | **14** | ✗ §0 déclarait 3 / 15 (`INF-15` clos, non descendu) |
| `OUT` | 7 | — | 1 | — | 8 | — |
| `BIB` | 1 | — | 1 | 1 | 3 | — |
| `CAS` | 1 | — | 1 | — | 2 | — |
| `PRO` | 3 | — | — | **3** | **6** | ✗ §0 déclarait 2 / 5 |
| `DOC` | 4 | — | — | 1 (+3 hors vocabulaire) | 8 | — |

**Ce que le recompte corrige** : le rapport du 09-13 annonçait « attente-verdict :
10 déclaré / 9 réel » et imputait l'écart à `INF` seul. Le recompte complet montre
que **l'écart est réel mais se déplace** : `INF` 3 → **2** (juste) **et** `PRO`
2 → **3** (le rapport n'avait pas recompté cette section). Le total
`attente-verdict` reste donc **10**, et la somme générale — `33 / 5 / 5 / 10 = 53`,
+3 hors vocabulaire = **56 lignes** — est **inchangée**. Seules les deux lignes
de pôle `INF` et `PRO` sont fausses.

**Second geste, mécanique** : `INF-15` porte un statut `**clos 2026-09-10**` hors
vocabulaire, et reste en §2. Le registre énonce lui-même la règle : « Un chantier
clos n'est jamais supprimé (Cmd 10) : il garde son ID et **descend en §9** avec sa
date. » Application, sans réécrire son contenu.

**Ce que le recompte ne touche pas** : `INF-09` porte `ouvert` alors que son
propre texte dit le verdict rendu (« cycle mis en pause par Sidy ») — la
requalification d'un statut est un jugement, pas un recompte : **signalé, non
corrigé** (Cmd 12). Les trois statuts hors vocabulaire de `DOC`
(`fait` / `partiel` / `recensé`) restent tels quels : la question du vocabulaire
est explicitement **soumise à Sidy** (§4.3 du rapport, §*Points ouverts*).

## 3. Propositions inspectées et NON exécutées — motifs

| Proposition | Motif de non-exécution |
|---|---|
| **N1 — entrée au `registre-problemes.md`** (§5.3 du rapport 09-13 : consigner l'affirmation de résolution portée au nom de trois jobs sur la foi d'un seul) | **Interdiction de mandat, explicite** : le mandat `infrastructure-veille` porte « *jamais d'écriture directe à `atelier/rd/cahiers/registre-problemes.md`* ». Une consigne en canal ne la lève pas d'elle-même : le texte de l'entrée est **prêt** (§5 ci-dessous), il attend son dépositaire (Sidy, ou une session Claude Code). |
| **N2 — ouvrir une ligne `INF-17` (migration de provider)** (Piste 5) | Le rapport pose la proposition en **alternative soumise à verdict** : « ouvrir la ligne, **ou** acter qu'une optimisation n'appelle pas de ligne (verdict, Cmd 13) ». Trancher une convention de registre n'est pas de mon ressort. |
| **N3 — `_inbox/` : deux fichiers du sas suivis par git** (§3.3) | **Inspection faite, correctif écarté à tort par le rapport.** `git log` montre que le suivi des fichiers du sas est une **pratique récurrente et délibérée** — au moins quatre sessions depuis le 2026-08-28 (`INBOX:`, `SAS:`, `Fiche _inbox/ :`) — et non une récurrence de l'accident du `[2026-08-09]`, où l'incident portait sur `git add -A` ramassant une pièce **nominative** (`karubi-mehdi.md`, `image.jpeg`). Défaire un suivi délibéré serait un acte, pas un correctif. **Signalé** : la doctrine « le sas est intouchable par Git » et la pratique observée se contredisent ; la levée demande un verdict (règle `.gitignore`, ou reconnaissance de la pratique). **Non exécuté.** |
| **N4 — intégrer les deux fiches en attente du sas `_inbox/`** (5 jours pour la plus ancienne) | Acte d'**intégration** (`§IX`), qui relève d'un autre périmètre que celui de cet agent et suppose un plan validé (Cmd 6). **Signalé.** |
| **N5 — réintroduire `verifier-invariants.py` au §1 du rapport Studio** | Retiré **délibérément** le 2026-08-24 au profit du job `veille-frontmatter-quotidien` du profil `publication`. Conséquence à connaître, non à corriger d'office : le contrôle A étendu par **C3** mordra dans le **rapport Publication**, pas dans celui-ci. La demande de retour du script dans le rapport Studio est une décision de Sidy. |

## 4. Ce que cette passe change dans l'infrastructure — et comment on le vérifie

1. **Le rapport quotidien Studio ne commence plus par un échec** (C1).
2. **La chaîne d'archivage est complète** : rapport produit → archivé → **commité**
   → **entré au registre de traitement** (C2).
3. **Trois cahiers append-only passent sous contrôle**, dont la faute de
   `journal-optimisations.md` (9 jours) et celle de `registre-traitement.md` (2 jours)
   sont **mesurées par la même passe qui les corrige** (C3).
4. **Le §0 du registre des chantiers dit à nouveau la vérité de ses lignes** (C4).

**Vérifications exigées à la clôture** : `verifier-invariants.py --racine /root/wiki`
(sortie brute), `detecter-non-tracke.py`, `verifier-rapports-traites.py`,
`verifier-coherence-infrastructure.py`, `git status` vide — plus la **double face**
de l'épreuve du contrôle C3 (§2).

## 5. Textes prêts, non déposés (N1)

Entrée proposée pour `atelier/rd/cahiers/registre-problemes.md` — **à déposer par
Sidy ou une session Claude Code**, jamais par cet agent :

```markdown
## [2026-09-13] attente-verdict | Une résolution déclarée au nom de trois jobs, prouvée sur un seul

- **Symptôme** : l'entrée `[2026-09-11]` de `journal-optimisations.md` déclarait
  les `Connection error` des trois jobs cron résolues **au nom des trois**, sur
  la foi d'un seul run réussi (celui du profil `gardien`). Le rapport Studio du
  2026-09-13 a mesuré que le job Studio portait bien le pin attendu
  (`model = deepseek-flash`, `provider = deepseek`, `reasoning_effort = high`,
  `failure_streak = 0`, deux exécutions réussies les 09-12 et 09-13) — **le fait
  est vrai, la preuve ne le portait pas**.
- **Diagnostic** : défaut de *preuve*, non de configuration. Même classe que
  l'entrée `[2026-09-04]` (« un contrôle vert n'attestait pas que les liens du
  cartouche aboutissent ») et que §VII, *Épreuve des contrôles*. Instance datée
  sur le rapport lui-même.
- **Résolution** : (à trancher) — soit relecture des `jobs.json` des trois profils
  avec citation brute, soit entrée de correction au `journal-optimisations.md`.
- **Liens** : `journal-optimisations.md` `[2026-09-11]` ; rapport Studio du
  2026-09-13 §3.4 ; [[atelier/rd/cahiers/registre-problemes]] entrée `[2026-09-04]`.
```

## 6. Réversibilité

Tout est réversible par `git revert` **à l'exception de C1**, qui vit hors du
dépôt (prompt persisté dans `~/.hermes/profiles/studio/cron/jobs.json`) : le
texte du prompt **avant** correction est reproduit au §7, et sa restauration est
une édition de champ. Aucune suppression (Cmd 10) : l'archive commitée reste,
les entrées de registre s'ajoutent, le §0 est recompté et non réécrit, `INF-15`
quitte §2 **pour §9** — il garde son identifiant.

## 7. Annexe — prompt du job `monitoring-infrastructure-quotidien` avant C1

Texte intégral persisté avant correction (2310 caractères), pour restauration à
l'identique si la correction était défaite :

```
Rapport quotidien du pôle Studio (profil studio, canal #infrastructure). Depuis /root/wiki, exécute dans l'ordre et cite la sortie brute de chaque script (jamais un résumé) :

## §1 — Cartographie et cohérence structurelle

1. python3 Graphe/generer-cartographie.py --depot /root/wiki --verifier
2. python3 atelier/rd/outillage/detecter-non-tracke.py --racine /root/wiki
3. python3 atelier/rd/outillage/verifier-coherence-infrastructure.py --racine /root/wiki

(§1 était autrefois ouvert par verifier-invariants.py — retiré 2026-08-24, repris par le job veille-frontmatter-quotidien du profil publication, 11:00 UTC.)

## §2 — Empreinte serveur

4. df -h /, free -h

## §3 — Registre Hermes-Terminal

5. Intégrité des bind-mounts, santé des 12 gateways (systemctl --user list-units 'hermes-*'), staleness de _inbox/

## §4 — Volet R&D (prioritaire, non conditionnel)

6. ./atelier/rd/outillage/detecter-nouvelles-fiches-rd.sh
7. Lire TOUTES les fiches R&D nouvelles (pas de seuil « aucune-nouvelle-fiche » qui saute la section). Pour chaque fiche :
   a. La lire en entier.
   b. La rapprocher de atelier/rd/cahiers/registre-problemes.md : une entrée existante couvre-t-elle ce problème, ou est-ce un problème nouveau ?
   c. Formuler une PROPOSITION d'action concrète (jamais une décision).
   d. Identifier les dépendances entre fiches R&D : quelle fiche nourrit quelle autre, quel angle mort reste ouvert.
   e. Si la fiche implique un autre agent (Studio, Gardien, Publication, etc.), le nommer et proposer un handoff explicite.
8. Relire les 5 entrées les plus récentes de registre-problemes.md. Pour chacune : l'état a-t-il changé depuis la dernière exécution ? Une proposition antérieure a-t-elle été appliquée, rejetée, ou est-elle stagnante ?
9. Synthèse R&D : 3 à 5 pistes prioritaires pour la prochaine session, classées par urgence et faisabilité. Marquer chaque piste PROPOSITION.

## Format du rapport

§1 Cartographie et cohérence (sorties brutes des scripts 1-3)
§2 Empreinte serveur
§3 Registre Hermes-Terminal
§4 R&D — analyse engagée (fiches nouvelles, registre-problemes, pistes prioritaires)
§5 Suggestions transversales

Contrôle anti-fabulation : ne jamais reformuler la sortie des scripts, la coller telle quelle. Étape 3 est le même contrôle (registre-problemes.md, entrée 2026-08-17).
```

## 8. État d'exécution

**Rédigée avant exécution** (2026-09-13), conformément à la règle de validation
conditionnelle. Les résultats, les sorties brutes des vérifications et les SHA
des commits sont versés au §9 **après** l'exécution.
