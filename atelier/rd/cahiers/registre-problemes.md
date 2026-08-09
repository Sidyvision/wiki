---
title: "Registre des problèmes — pôle R&D (cahier append-only)"
type: meta
created: 2026-08-08
updated: 2026-08-09
tags: [atelier, rd, cahier, registre, laboratoire]
sources: []
links: []
---

# Registre des problèmes du pôle R&D

Cahier append-only des problèmes, erreurs, blocages et anomalies rencontrés dans
les travaux du pôle `rd/` — et de leur résolution. Ouvert le 2026-08-08 (verdict
Sidy), premier cahier concret de la phase 2 de la proposition de pôle (discipline
de laboratoire, §V, règle 3 : « Un échec se consigne comme un succès »).

**Format** — miroir du bloc 🧪 Expérience, appliqué à l'erreur :

- **Symptôme** : le fait brut, tel qu'observé, sans interprétation (§VIII.2 : le
  résultat brut précède toujours l'interprétation).
- **Diagnostic** : l'interprétation, séparée du fait et flaguée comme telle.
- **Résolution** : ce qui a été fait — ou « aucune — abandon assumé ».
- **Compréhension tirée** : la leçon réutilisable. C'est le but du registre.
- **Liens** : fiches, commits, chantier concerné.
- **Statut** : `ouvert | resolu | abandonne | reporte`.

**Règle** : jamais de réécriture ni de suppression ; un problème clos reste
consigné. Insertion en tête (la plus récente en haut), marqueur ci-dessous.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-09] resolu | Contenu du sas `_inbox/` poussé par erreur sur le dépôt

- **Symptôme** : le commit `d73cdb6` (intégration de la fiche synchro
  Obsidian) contient les fichiers `_inbox/karubi-mehdi.md` et
  `_inbox/image.jpeg`, ajoutés par un `git add -A` trop large.
- **Diagnostic** : faute d'opérateur — le sas `_inbox/` est par définition
  non versionné tant que l'intégration n'a pas eu lieu (cf. entrée
  [2026-08-09] ci-dessous, vault désynchronisé : « laissé non versionné — ne
  doit pas partir sur le dépôt sans passage par le circuit d'intégration »).
  `git add -A` à la racine ramasse tout, sas compris.
- **Résolution** : commit correctif immédiat `87ca442`
  (`git rm --cached` sur les deux fichiers + push). Les fichiers ne sont plus
  suivis ; l'historique du remote conserve toutefois le blob du commit fautif
  (dépôt privé — pas de réécriture d'historique sans verdict Sidy).
- **Compréhension tirée** : dans ce dépôt, ne jamais committer par
  `git add -A` depuis la racine ; ajouter nommément les fichiers intégrés
  (ou utiliser `git add -A -- <chemins>` hors `_inbox/`). Le sas est
  intouchable par Git tant que l'intégration n'est pas faite.
- **Liens** : commits `d73cdb6`, `87ca442` ; entrée ci-dessous
  (vault désynchronisé).
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Vault Obsidian (iPad) désynchronisé — 6 commits serveur jamais poussés

- **Symptôme** : le vault Obsidian sur l'iPad de Sidy n'est « plus du tout à
  jour » depuis un certain temps. Le vault = le dépôt wiki lui-même, consulté
  sur iPad via Obsidian en auto-pull depuis GitHub (`Sidyvision/wiki`,
  `CLAUDE.md` §postes : CONSULTATION).
- **Diagnostic** : aucun problème de configuration Obsidian côté serveur —
  l'auto-pull de l'iPad tire `origin/main`, or le serveur était en avance de
  6 commits non poussés (ouverture du pôle rd/, migration `projets/ → rd/`,
  arbitrage `album-personnel`, annales) plus 3 fichiers de travail non
  commités (registre des problèmes, thème natal corrigé, mise en regard
  roue/thème). La « connexion cassée » était simplement une chaîne de push
  interrompue côté serveur.
- **Résolution** : commit des 3 fichiers en attente puis `git push origin main`
  (7 commits au total). L'auto-pull de l'iPad récupérera l'état complet au
  prochain cycle. `_inbox/` (sas en attente d'intégration, contient des PDF
  bancaires) laissé non versionné — ne doit pas partir sur le dépôt sans
  passage par le circuit d'intégration.
- **Compréhension tirée** : un vault « cassé » peut n'être qu'un dépôt local en
  avance sur son remote. Avant d'incriminer l'outil de consultation (Obsidian,
  ses plugins, sa synchro), vérifier l'état git (`git status -sb`,
  `rev-list --left-right --count origin/main...HEAD`) : c'est le maillon serveur
  qui portait le retard.
- **Liens** : `CLAUDE.md` §postes (CONSULTATION = Obsidian iPad auto-pull) ;
  remote `git@github.com:Sidyvision/wiki.git`.
- **Statut** : `resolu`.

---

## [2026-08-08] resolu | Vision Hermes en 404 sur l'endpoint Qwen (auto-détection auxiliaire mal routée)

- **Symptôme** : l'outil `vision_analyze` échoue systématiquement avec
  `Error code: 404` ; mêmes échecs consignés pour les tâches auxiliaires
  `compression` et `title_generation` dans `~/.hermes/logs/agent.log` et
  `errors.log`. La conversation principale fonctionne normalement par ailleurs.
- **Diagnostic** : les tâches auxiliaires sont par défaut en `provider: auto`.
  L'auto-détection réécrit l'URL de base
  `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic` →
  `.../apps/v1` (règle générique pour les endpoints « anthropic-compatibles »),
  puis le SDK Anthropic ajoute `/v1/messages` : l'appel arrive sur
  `.../apps/v1/v1/messages`, qui n'existe pas. L'endpoint Qwen n'expose que la
  surface `anthropic_messages` sur `/apps/anthropic/v1/messages` (vérifié :
  le fil OpenAI `/apps/v1/chat/completions` renvoie lui aussi 404). Test
  discriminant : le même appel épinglé sur `custom:qwen` réussit (réponse
  correcte à l'analyse d'image), l'appel auto-détecté échoue en 404.
- **Résolution** : épinglage
  `auxiliary.{vision,compression,title_generation,web_extract}.provider: custom:qwen`
  via `hermes config set` sur le profil principal ET les 12 profils Discord
  (ar-music, visual-da, production, admin-legal, accounting, distribution,
  marketing, publication, studio, gardien, fanzine, commerce). Vérification en
  direct après coup : `vision_analyze` répond correctement (test carré rouge →
  « Red »).
- **Compréhension tirée** : quand le provider principal est un endpoint
  Anthropic-compatible qui n'expose QUE cette surface, l'auto-détection
  auxiliaire (`auto`) est trompeuse — elle présuppose que l'endpoint parle aussi
  OpenAI. Il faut épingler explicitement toutes les tâches auxiliaires sur le
  provider nommé. Un échec « vision » peut donc être un problème de routage
  auxiliaire, pas du modèle.
- **Liens** : `~/.hermes/config.yaml` (profil `default` + 12 profils) ;
  `~/.hermes/logs/agent.log` ; code Hermes `agent/auxiliary_client.py`
  (`_to_openai_base_url`, `resolve_vision_provider_client`) ;
  [[meta/projet-unifie/15-architecture-discord-hermes-2026-08-07]].
- **Statut** : `resolu`.

---

## [2026-08-08] resolu-partiel | 4 anomalies d'étanchéité `materiel → album-personnel` coupées

- **Symptôme** : 4 des 10 anomalies bloquantes du graphe (entrée ci-dessous) :
  `atelier/materiel/{neve-1073spx, studio-principal, tascam-model-12,
  technics-su-8080}.md` (neutre, rang 0) → `atelier/projets/album-personnel.md`
  (rang 1) — liens remontants, interdits (§VI).
- **Diagnostic** : liens historiques hérités de la création des fiches materiel
  (2026-06-20), antérieurs à la formalisation de l'étanchéité. Devenus sans
  objet légal après le déplacement d'`album-personnel` vers `label/` (rang 2) :
  le sens licite est label → materiel, porté par `liens_atelier` (§V.b) de la
  fiche canonique.
- **Résolution** : les 4 liens coupés le 2026-08-08 — frontmatter (`links`) et
  corps de texte — lors de l'exécution du verdict d'arbitrage. Aucune fiche
  supprimée ; l'information de contexte (« projet dans lequel cet appareil est
  utilisé ») subsiste côté label.
- **Compréhension tirée** : un arbitrage de circuit est l'occasion naturelle de
  purger les violations d'étanchéité qui pointaient vers la fiche arbitrée —
  le déplacement change le rang de la cible et rend caducs les liens entrants
  du neutre.
- **Liens** : entrée ci-dessous (10 anomalies) ; [[label/production/album-personnel]] ;
  [[atelier/projets/album-personnel]] (stub) ; `CLAUDE.md` §VI.
- **Statut** : `resolu` pour les 4 liens ; l'entrée « 10 anomalies » passe à
  6 anomalies restantes (4 doctrinal → v0_3 + 2 frontmatter).

---

## [2026-08-08] ouvert | `graphe-cartographie.json` jamais régénéré (bloqué par les anomalies du graphe)

- **Symptôme** : `generer-cartographie.py` refuse d'écrire
  `graphe-cartographie.json` en présence d'anomalie bloquante ; le JSON de
  cartographie est absent du dépôt (jamais régénéré depuis son introduction).
- **Diagnostic** : conséquence directe de l'entrée suivante — le générateur est
  strict par conception (une anomalie = échec). Tant que les 10 anomalies
  pré-existantes ne sont pas traitées, l'artefact dérivé ne peut pas être produit.
- **Résolution** : aucune pour l'instant — le fichier n'a jamais été tracké ; la
  migration `projets/ → rd/` n'est pas en cause (vérifié par comparaison avec la
  baseline HEAD).
- **Compréhension tirée** : un générateur strict bloque tous les artefacts dérivés
  dès qu'une anomalie pré-existe. Deux issues possibles : soit traiter les
  anomalies à la source, soit doter le script d'un mode tolérant qui écrit
  l'artefact en signalant les anomalies plutôt que d'échouer. À arbitrer (verdict
  Sidy).
- **Liens** : entrée suivante ; `Graphe/generer-cartographie.py` ;
  [[meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08|proposition de pôle]].
- **Statut** : `ouvert`.

---

## [2026-08-08] ouvert | 10 anomalies bloquantes du graphe (8 étanchéité + 2 frontmatter), pré-existantes

- **Symptôme** : `generer-cartographie.py` remonte 10 anomalies :
  - 2 `frontmatter` — frontmatter absent (le fichier ne commence pas par `---`) :
    `doctrinal/sources/transcription-index-tilak-origine-polaire.md`,
    `doctrinal/sources/transcription-table-matieres-symboles-science-sacree.md` ;
  - 4 `étanchéité` — `atelier/materiel/*` (neutre) →
    `atelier/projets/album-personnel.md` (plus sensible) ;
  - 4 `étanchéité` — `doctrinal/sources/guenon-*` (neutre) →
    `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
    (plus sensible).
- **Diagnostic** : toutes pré-existantes à la migration `projets/ → rd/` — vérifié
  point par point contre un export `git archive` de HEAD (mêmes 10 anomalies avant
  et après). La migration n'en introduit aucune.
- **Résolution** : aucune pour l'instant. Les 4 liens `materiel → album-personnel`
  dépendent du verdict d'arbitrage `album-personnel` (`rd/` vs `label/`) ; les
  4 liens `doctrinal/sources → v0_3` sont un sens de lien interdit par §VI (le
  neutre ne pointe pas vers le plus sensible), à traiter fiche par fiche.
- **Compréhension tirée** : avant d'attribuer une régression à une opération,
  comparer contre la baseline (HEAD) — ici la comparaison a innocenté la migration
  et isolé un passif ancien. Le registre doit consigner les anomalies dès leur
  découverte, pas seulement celles qu'on introduit.
- **Liens** : `Graphe/generer-cartographie.py` ; arbitrage `album-personnel.md`
  (verdict Sidy rendu le 2026-08-08 : `label/`) ; `CLAUDE.md` §VI.
- **Statut** : `partiellement-resolu` — 4/10 levées le 2026-08-08 (liens
  `materiel → album-personnel` coupés, voir entrée ci-dessus) ; restent
  4 `étanchéité` doctrinal → v0_3 et 2 `frontmatter`.

---

## [2026-08-08] resolu | Lien mort `manvantara → v0_2` (version inexistante)

- **Symptôme** : `doctrinal/symboles/manvantara.md` pointait vers une version
  `v0_2` (underscore) de l'architecture de l'Instrument, inexistante dans le dépôt.
- **Diagnostic** : coquille de slug — la cible `v0_2` n'existe pas ; le lien a été
  repointé vers `v0.3` conformément aux annales de la migration.
- **Résolution** : lien repointé vers `v0.3` lors de la migration (repérage des
  liens entrants).
- **Compréhension tirée** : les slugs de versions sont proches (`v0.3` / `v0_3`)
  et faciles à confondre ; un lien mort de ce type est silencieux tant qu'un
  générateur ou une relecture ne le remonte pas. À terme, un contrôle des liens
  entrants (ou le manifeste) devrait signaler toute cible inexistante.
- **Liens** : `doctrinal/symboles/manvantara.md` ;
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`.
- **Statut** : `resolu`.
