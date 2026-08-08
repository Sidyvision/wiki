---
title: "Registre des problèmes — pôle R&D (cahier append-only)"
type: meta
created: 2026-08-08
updated: 2026-08-08
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
