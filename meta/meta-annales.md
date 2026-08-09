---
title: Annales du Domaine Réservé (meta/)
type: meta
updated: 2026-08-09
---

# Annales du Domaine Réservé (`meta/`)

Journal chronologique inverse des opérations propres au domaine `meta/`
(la plus récente en haut). Append-only. Nommage préfixé `meta-` pour ne
jamais se confondre avec les `annales.md` des quatre circuits — `meta/`
reste le Domaine Réservé (§VI CLAUDE.md), pas un sixième circuit.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-09] tranché | signalement `doctrinal/ → meta/personnel/` (sens interdit) résolu

- **Rappel** : entrée précédente signalait 4 fiches `meta/personnel/`
  (dont `gout-sucre-priere`) et `meta/projet-unifie/briefing-claude-ai`
  reçevant leur seul lien entrant depuis `doctrinal/annales.md`, sens
  interdit par §VI.
- **Correction factuelle** : vérification directe par grep — `gout-sucre-priere`
  n'a **aucun** lien depuis `doctrinal/annales.md` ; son unique lien entrant
  vient de `meta/genealogie/2026-06-20_oiseau-serpent-jumeau.md` (intra-`meta/`,
  conforme). L'ensemble réel est de **3 fiches** :
  `meta/personnel/2026-06-20_bourdonnement-tempe`,
  `meta/personnel/2026-06-20_taekwondo-hansu`,
  `meta/projet-unifie/briefing-claude-ai`.
- **Verdict** : les 3 liens vivent dans des entrées d'annales déjà publiées,
  datées (2026-06-20), append-only — non repris (Cmd 9/Cmd 10). Le hub
  `meta-index.md` leur donne désormais un lien entrant alternatif,
  intra-`meta/`, conforme. `doctrinal/index.md` (§IX), fichier non
  append-only, corrigé directement : lien `meta/sidy` retiré, remplacé par
  renvoi générique vers `meta-index.md`.
- **Détail complet** : voir `atelier/rd/cahiers/registre-problemes.md`,
  entrée `[2026-08-09] resolu | Tranché — signalement doctrinal/ →
  meta/personnel/`.
- **Commit** : fc0e1c6

---

## [2026-08-09] ouverture | création du hub `meta-index.md` / `meta-annales.md`

- **Constat** : le comptage mécanique des liens entrants (`carte-du-depot.py`,
  bug de résolution corrigé le même jour) faisait apparaître 80 fiches sans
  aucun lien entrant, dont 66 vivant dans `meta/` — faute de hub interne au
  domaine, contrairement aux quatre circuits qui disposent chacun d'un
  `index.md`/`annales.md`.
- **Verdict Sidy** : autorisation de traiter toutes les fiches orphelines, y
  compris personnelles ; nommage du hub propre à `meta/` avec préfixe `meta-`
  (`meta-index.md`, `meta-annales.md`) pour écarter tout risque de lecture
  comme sixième circuit.
- **Action** : création de `meta/meta-index.md`, recensant par sous-dossier
  (`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
  `projet-unifie/` y compris `hermes-prompts/`/`hermes-skills/`, fiches de
  premier niveau) les fiches du domaine — chacune reçoit ainsi un lien
  entrant légitime, intra-`meta/` exclusivement. Résout l'orphelinage des 66
  fiches `meta/`.
- **Scripts adaptés** : `verifier-invariants.py` (`NOMS_ANNALES`,
  `FICHIERS_EXEMPTS_C3`, détection `fichier_de_service` étendus aux nouveaux
  noms) et `carte-du-depot.py` (filtre d'orphelines étendu). `CLAUDE.md` §II,
  §VI et §X (Cmd 9) mis à jour en conséquence.
- **Hors périmètre, signalé séparément** (Cmd 7, non traité ici) : 4 fiches
  `meta/personnel/` et 1 fiche `meta/projet-unifie/` reçoivent leur seul lien
  entrant depuis `doctrinal/annales.md`, en sens interdit (§VI, sensible →
  neutre uniquement). Verdict humain toujours attendu — voir
  `atelier/rd/cahiers/registre-problemes.md`.
- **14 fiches restant orphelines hors `meta/`** (13 stubs `deprecated` de
  `atelier/projets/` + `doctrinal/discernement/_template.md`) : acceptées par
  conception, non traitées par lien artificiel — voir registre.
- **Commit** : fc0e1c6
