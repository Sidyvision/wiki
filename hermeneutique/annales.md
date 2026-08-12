---
title: Annales du circuit Herméneutique
type: meta
created: 2026-08-04
updated: 2026-08-12
---

# Annales du circuit Herméneutique

Journal chronologique inverse des opérations (la plus récente en haut). Append-only,
entrées insérées **après ce header**.
<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-12] archivage | iDroid — dispositif satellite de Mother Base

- **Fiche créée** : `hermeneutique/metal-gear/idroid.md` — `type: dispositif`,
  `registre: analyse`, `statut_analyse: brouillon`, `sources: ["to-source"]`.
- **Provenance** : déposée en `_inbox/` le 2026-08-11, statut d'origine
  « kari-kumi / brouillon — en attente du visa de Sidy ». Visa donné le
  2026-08-12 par consigne explicite d'intégrer le reste du sas.
- **Anomalie corrigée avant intégration** : le Sceau livré portait
  `oeuvre: "metal-gear-solid"` et `liens: ["hermeneutique/metal-gear-solid/mother-base"]`
  — slug incohérent avec le dossier réel `hermeneutique/metal-gear/` (ouvert
  2026-08-08, lot Kojima). Corrigé en `oeuvre: "metal-gear"` et
  `liens: ["[[hermeneutique/metal-gear/mother-base]]"]` (wikilink complet,
  convention §IV). Corps de la fiche inchangé.
- Aucune clé doctrinale invoquée (§4 de la fiche, piste non retenue) —
  hozo/kumiko/kari-kumi sans objet ici.
- `verifier-invariants.py --racine /root/wiki` : voir entrée groupée
  `atelier/annales.md` du même jour pour le résultat brut consolidé.
- **Commit** : 3e846e9

## [2026-08-12] archivage | Marqueur d'insertion ajouté (mise en conformité)

- Ajout du marqueur `<!-- INSERTION: EN-TÊTE -->` (absent jusqu'ici, seul journal
  du dépôt dans ce cas) — mise en conformité avec la convention transversale
  (CLAUDE.md racine §VII, amendement 2026-07-27) préalable à l'écriture de
  l'entrée d'archivage ci-dessous. Aucune autre modification du fichier.
- **Commit** : 9e9681d

## [2026-08-12] archivage | Lot Hunter x Hunter — œuvre, auteur, dispositif, concept

- **Fiches créées** :
  - `hermeneutique/hunter-x-hunter/hunter-x-hunter.md` — `type: oeuvre`, fiche-hub
  - `hermeneutique/auteurs/togashi-yoshihiro.md` — `type: auteur`
  - `hermeneutique/hunter-x-hunter/hunter-association-licence.md` — `type: dispositif`
  - `hermeneutique/hunter-x-hunter/nen-systeme.md` — `type: concept` (fiche pivot)
- **Statut d'ensemble** : lot *kari-kumi* / `brouillon`, `to-source` intégral
  (Hunter x Hunter absent de `meta/bibliotheque-physique.md`).
- **Joint doctrinal ouvert** : `nen-systeme.md` §5-6 → fiche
  `doctrinal/discernement/2026-08-12_nen-pacte-restriction-ascetique` (sens
  hermeneutique → doctrinal, suggéré 🔍 ; hozo exclu). Voir `doctrinal/annales.md`
  pour l'entrée correspondante.
- **Anomalies corrigées avant intégration** (verdict Sidy, session 2026-08-12) :
  `cross_links` de la fiche discernement pointait vers `hermeneutique/` (sens
  interdit) — vidé à `[]` ; bloc normalisé `🔍 Discernement — Spéculation
  Personnelle` absent — ajouté en tête de fiche par synthèse fidèle du contenu
  existant (§0-§8 inchangés).
- **Points fragiles signalés** (portés par le lot, non résolus) : nomenclature de
  la technique « Kō », ordre de l'hexagone d'affinité, chronologie des hiatus de
  publication, citations Coran/Guénon à recouper sur édition physique.
- **Commit** : 9e9681d

## [2026-08-08] archivage | Premier lot Kojima — Metal Gear, Death Stranding

- Amendement de portance adopté et exécuté (voir `doctrinal/annales.md`
  [2026-08-08]) : taxonomie élargie (types `auteur`, `figure`, `dispositif`),
  axe de **portance** (*jikugumi*/*zōsaku*) et axe de **nature**
  (*restitution*/*homologie*) des joints doctrinaux, convention du bloc 🪵
  Restitution — clé doctrinale.
- Sept fiches créées : `hermeneutique/auteurs/hideo-kojima.md`,
  `hermeneutique/auteurs/yoji-shinkawa.md`,
  `hermeneutique/metal-gear/{metal-gear,big-boss,mother-base}.md`,
  `hermeneutique/death-stranding/{death-stranding,dhv-magellan}.md`. Une
  huitième fiche connexe créée hors circuit : `atelier/etudes-de-cas/kojima-productions.md`
  (étude de cas, anglais, étanchéité vérifiée — zéro wikilink vers `hermeneutique/`).
- Fiches-hub de saga : Metal Gear (9 opus, 1987-2015) traité en une seule fiche
  `type: oeuvre` par section, conformément à la règle 4 de l'amendement.
- Six clés doctrinales restituées, toutes ***zōsaku*** / ***kari-kumi***, aucun
  *hozo* ni *kumiko* : Big Boss → `confusion-psychique-spirituel` (homologie de
  contraste) ; Metal Gear (saga) → `alam-al-mithal` + `confusion-psychique-spirituel`
  (homologie, repère de vigilance) ; Yoji Shinkawa → `outil-faculte-objectivee`
  (homologie) ; Death Stranding → `barzakh` (**restitution**, filiation
  `to-source`) + `habl-allah` (homologie). Mother Base et DHV Magellan
  n'invoquent aucune clé — justifié explicitement en corps de fiche (§6bis) :
  le nouvel axe de portance ne requiert pas une clé partout.
- Quatre cibles manquantes signalées, aucun lien à faux posé (§VII.3) :
  structure de la transmission (Big Boss §3, Metal Gear saga §3) ; Homo
  ludens/Ludens (Yoji Shinkawa §4) ; réseau/support subtil commun (Death
  Stranding §6.3) ; cible `meta/`ou`atelier/projets/` pour le module de
  transposition d'infrastructure (Mother Base §5bis).
- Deux fiches restent `statut_analyse: brouillon` — Death Stranding et DHV
  Magellan — dans l'attente du dépôt des mails du premier volet et du Corpus
  du second ; blocage explicite de tout usage en appui d'une fiche
  `registre: expression` tant que non levé.
- Correction de source : wikilink `doctrinal/sources/kitab-tarifat` (cible
  inexistante) corrigé en `doctrinal/sources/kitab-al-tarifat-jurjani`
  (vérifiée) dans DHV Magellan §5, avant écriture.
- `verifier-invariants.py --racine /root/wiki` : `0 erreur(s), 0 avertissement(s)`.
- **Commit** : d5edf59

## [2026-08-04] ouverture | Circuit hermeneutique/ ouvert (5e circuit du dépôt)

- Circuit ouvert sur validation de Sidy, architecture seule — aucune œuvre ni fiche d'expression déposée à ce stade.
- Détail de l'amendement protocolaire : voir `doctrinal/annales.md` [2026-08-04].
- Prochaines étapes attendues : ingest Death Stranding, Evangelion ; reprise en registre `expression` d'idées issues des fiches `doctrinal/discernement/` existantes (chaque fiche pointant vers son discernement d'origine, sans le clore).
