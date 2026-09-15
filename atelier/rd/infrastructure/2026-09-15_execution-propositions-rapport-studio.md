---
title: "Exécution des propositions du rapport Studio du 2026-09-15 — fiche-contrat"
type: infrastructure
tags: [rd, infrastructure, monitoring, hermes, correctifs, contrat]
created: 2026-09-15
updated: 2026-09-15
sources: []
links:
  - "[[atelier/rd/infrastructure/2026-09-13_suite-points-ouverts-rapport-studio]]"
  - "[[atelier/rd/cahiers/registre-problemes]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/out-17-controles-file-et-renvois-skills/plan]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan]]"
  - "[[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]]"
original: []
infra_verif:
  - profil: studio
    cron_job: monitoring-infrastructure-quotidien
---

# Exécution des propositions du rapport Studio du 2026-09-15 — fiche-contrat

## 1. Motif et cadre

**Consigne de Sidy, en session Claude Code, 2026-09-15** : « oui, recopie la section du
brouillon 09 en meta et tu peux t'exécuter les propositions Studio P1 et P5 et le reste ».
Elle répond au compte rendu de traitement du rapport Studio du jour
(`monitoring-archive/2026-09-15_41dc3e7e492c.txt`, entrée du registre de traitement
`[2026-09-15]`).

Comme le 2026-09-13, cette fiche est le **contrat** du lot : elle est écrite et commitée
**avant** la première écriture d'exécution. Les gestes exécutés sont ceux du §2, ni plus ni
moins ; ce qui n'est pas exécuté l'est pour un motif nommé (§4).

## 2. Le lot

| Code | Proposition du rapport | Geste | Portée |
|---|---|---|---|
| **G1** | (consigne) recopier la section du brouillon 09 en `meta/` | **aucune écriture** : vérifié que le texte est déjà dans `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer/09-principe.md`, identique à l'espace près | — |
| **P1** | périmètre et nom du contrôle OUT-17 | les deux commandes de l'étape 6 du job reçoivent le home Hermes de la flotte | **hors dépôt** — prompt du job cron |
| **P2** | contrôle du critère 1 d'INF-16 vert par construction | le contrôle cherche une ligne **remplie**, en début de ligne ; épreuve §VII | dépôt — `inf-16-…/plan.md` |
| **P3** | `carte_du_depot` cassé (OUT-18) | retrait de `--json` ; appel réel avant/après ; appel de chaque entrée du serveur | **hors dépôt** — `/root/mcp-servers/wiki/wiki_mcp_server.py` |
| **P4** | registre des problèmes à remettre à jour | trois entrées append-only (options C/D tranchées ; amortissement d'un constat doctrinal ; preuve des trois pins) | dépôt — `registre-problemes.md` |
| **P5 (i)** | `infra_verif` ne couvre pas `mcp_servers` | ouverture d'une ligne `OUT-19`, statut `ouvert`, §0 recompté | dépôt — `registre-chantiers.md` |
| **P5 (ii)** | régime d'un artefact dérivé porteur de corpus | **inscription** de la question aux points soumis à Sidy — aucun régime rédigé | dépôt — `registre-chantiers.md` |
| **S** | règles d'autorisation trop larges | retrait des règles élargissantes de `settings.local.json` | **hors dépôt** — `/root/.claude/settings.local.json` |
| **O** | `omniroute.service` `enabled` + `failed` | **aucun geste** (§4) | — |

## 3. Ce que chaque geste change, exactement

### G1 — rien à recopier

La section « Your sign in Sidy's natal chart » retirée du brouillon 09 le 2026-09-15
(`e8733c4`) différait du prompt `meta/` **par le seul retour à la ligne** : comparée mots à
mots (espaces normalisés), elle est identique. Écrire en `meta/` pour aligner un habillage
serait une modification que la consigne ne demande pas.

### P1 — le contrôle de flotte mesure enfin la flotte

**Correction de ce que j'avais écrit** au registre de traitement : aucun des deux scripts
n'est à modifier. Tous deux résolvent leur racine par `$HERMES_HOME` ; le job tourne avec
`HERMES_HOME=/root/.hermes/profiles/studio` et mesure donc un profil étiqueté `default`.
Le défaut est tout entier dans le **prompt**. Geste : préfixer les deux commandes par
`HERMES_HOME=/root/.hermes`. Mesure avant écriture, sur la flotte réelle :
`etat-file-skills.py` → **9 positions** (le rapport en voyait 4) ; `verifier-renvois-skills.py`
→ **1304 skills sur 14 racines, 14 renvois morts** (le rapport : 94 skills, 1 racine).

### P2 — un contrôle qui peut refuser

Le contrôle `grep -n "charge de reference arretee" plan.md` trouve toujours deux lignes : le
gabarit (l. 109) et sa propre ligne de tableau (l. 213). Nouveau motif :
`grep -nE '^charge de reference arretee : [^<]'` — ne répond qu'à une ligne **commençant**
par la formule et **remplie** (le gabarit commence par un accent grave et porte `<usages>`,
la ligne de tableau commence par `|`). L'étape 1 est précisée en conséquence (« en début de
ligne »). Épreuve : refus attendu sur le plan actuel (la charge n'est pas arrêtée), vert sur
une copie jetable portant une ligne remplie.

### P3 — `carte_du_depot`

`wiki_mcp_server.py` l. 248 passe `--json`, que `carte-du-depot.py` refuse
(`error: unrecognized arguments: --json`, code 2 — reproduit en session). Geste : retrait de
cet argument. Copie de l'état d'avant conservée hors dépôt (scratchpad de session) ; le
serveur n'étant pas versionné, la fiche en tient lieu de trace. Puis appel réel de chaque
entrée du serveur, sortie consignée au §9 — **appel**, non épreuve de refus entrée par
entrée : cette dernière reste le programme d'OUT-18.

### P4 — trois entrées append-only

(i) les options C/D (porte et fork) ont été **tranchées** le 2026-09-15 (« ne rien
éteindre », fiche `2026-09-15_file-attente-morte-ecritures-skills` §8) : deux entrées du même
jour portent une ligne de statut périmée — constaté, non réécrit ; (ii) l'amortissement d'un
constat doctrinal (incident du 2026-09-14), qu'aucune entrée ne couvrait ; (iii) la preuve
des trois pins, relue dans les trois `jobs.json`, qui clôt l'entrée `[2026-09-13]`. Écrites
par une session Claude Code sous consigne — l'interdiction de la charte vise les agents
Hermes.

### P5 — une ligne ouverte, une question inscrite

(i) `OUT-19` : étendre `verifier-coherence-infrastructure.py` à une clé `mcp_servers`.
**Seule la ligne est ouverte** : le code attend un triptyque visé (Cmd 6). §0 recompté
depuis les lignes : 60 → 61. (ii) Le régime d'un adaptateur de poids entraîné sur le corpus
est un verdict (Cmd 12/13) : la question est **inscrite**, jamais tranchée.

### S — autorisations

Retrait des sept règles dont une étoile élargit la portée au-delà de la commande
approuvée : `Bash(cp -r doctrinal/* /root/wiki/doctrinal/)`, `Bash(cp -r meta/* /root/wiki/meta/)`,
`Bash(cp _inbox/guenon-*.md doctrinal/sources/)`, `Bash(cp _inbox/tilak-*.md doctrinal/sources/)`,
`Bash(file /root/wiki/raw/assets/*.jpeg)`, la règle `mv` à glob, et `Bash(python3 -c ' *)`
(tout code Python sans demande). Effet : ces commandes redemanderont une autorisation. Copie
de l'état d'avant conservée.

## 4. Non exécuté — et pourquoi

- **O — `omniroute.service`** : le rapport le disait « non signalé jusqu'ici » ; c'est
  **faux**. L'arrêt est un geste conservatoire de Sidy du 2026-09-08 (saturation mémoire),
  consigné à l'addendum de
  [[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]], qui note
  expressément que le service reste `enabled` et que la décision structurelle est réservée
  (Cmd 13). Le `failed` est la trace d'un SIGTERM mal intercepté, non d'un échec de
  démarrage. `omniroute` reste en outre fournisseur de secours du profil `default` et des
  12 jobs `cycle-choura` désactivés : un `disable` changerait le comportement au prochain
  redémarrage. Statu quo, **déclaré** ici.
- **P5 (ii)** : aucun régime rédigé (Cmd 12/13).
- **OUT-19** : aucun code avant visa d'un plan.

## 5. Réversibilité

Chaque geste du dépôt est un commit ; les trois écritures hors dépôt ont leur état d'avant
copié (`studio-jobs.avant-2026-09-15.json`, `settings.local.avant.json`,
`wiki_mcp_server.avant.py`, scratchpad de la session) et se restaurent par copie.

## 6. Annexe — étape 6 du prompt du job, avant

```
6. File d'écritures de skills — état, inaptes au contrat du magasin, puis renvois déclarés par les skills :
   python3 atelier/rd/outillage/etat-file-skills.py
   python3 atelier/rd/outillage/verifier-renvois-skills.py
```

## 7. État d'exécution — exécuté le 2026-09-15

Contrat commité avant exécution : `5caf556`. Sorties brutes :

- **G1** : comparaison mots à mots de la section retirée (`e8733c4^`) et du prompt `meta/` →
  `identique à l'espace près : True`. Aucune écriture.
- **P1** : prompt relu **sur disque** après écriture (jamais l'auto-rapport) :
  ```
     HERMES_HOME=/root/.hermes python3 atelier/rd/outillage/etat-file-skills.py
     HERMES_HOME=/root/.hermes python3 atelier/rd/outillage/verifier-renvois-skills.py
  ```
  `jobs.json` confronté à sa copie d'avant, prompt exclu : identique ; indentation identique ;
  `enabled = True`. Mesures sur la flotte avec ce préfixe : `total : 9 position(s), 1
  inapte(s), 4 alerte(s)` et `total : 1304 skill(s), 14 renvoi(s) mort(s), 115 mention(s)
  manquante(s)`. Premier rapport à porter la ligne corrigée : celui du 2026-09-16.
- **P2** — épreuve §VII du nouveau contrôle :
  plan réel (charge non arrêtée) → `code=1` (**refus**) ; copie jetable portant
  `charge de reference arretee : U1, U3 — 2026-09-20` → `code=0` (**vert**) ; copie jetable
  portant le gabarit `<usages>` en début de ligne → `code=1` (**refus**). L'ancien motif
  trouvait **2** lignes sur le plan réel.
- **P3** : avant correctif, `carte-du-depot.py … --json` → `error: unrecognized arguments:
  --json`, code 2 ; après, `carte_du_depot()` → `ok: True, code 0`. Appel de chaque entrée du
  serveur (16) : `ok` pour 12 ; **code 1 comme résultat** pour `detecter_non_tracke` (les
  fichiers de la passe, non encore commités) et `valider_index_livres` (**défaut réel,
  hors serveur** : `atelier/rd/bibliotheque/index-noms-ihwan-al-safa.md` n'a pas le cartouche
  `index-livre` — cinq clés manquantes, `type: ressource` — signalé, non corrigé) ; **non
  appelées** : `ajouter_inbox` et `generer_glossaire_unifie` (elles écrivent). Ce sont des
  appels, pas des épreuves de refus : OUT-18 reste ouvert pour cela.
- **P4** : trois entrées déposées en tête du registre des problèmes ; l'entrée `[2026-09-13]`
  est close par la première.
- **P5** : ligne `OUT-19` ouverte ; recompte depuis les lignes après ajout :
  `61 {'en-cours': 9, 'ouvert': 34, 'bloque': 5, 'attente-verdict': 13}` ; question (ii)
  inscrite au point 7 des points soumis à Sidy.
- **S** : 7 règles retirées (`allow` : 233 → 226), fichier relu et JSON valide.
  **Rectification (2026-09-15, même soirée)** : la règle `Bash(python3 -c ' *)` a été
  **rétablie** sur demande de Sidy — c'est lui qui l'avait configurée. Bilan réel : **6 règles
  retirées** (`allow` : 233 → 227) ; la règle Python reste un choix délibéré de Sidy, non un
  défaut.
- **O** : aucun geste.
