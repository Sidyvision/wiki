---
title: Annales de l'Atelier (Projets et Matériels)
type: meta
updated: 2026-08-10
---

# Annales de l'Atelier

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-10] outillage | Méthode de croisement des fiches `discernement/`

- **Directive Sidy** : instruire le pôle R&D d'un rapport des moyens et méthode
  utilisés pour croiser les 33 fiches `doctrinal/discernement/` entre elles et
  avec le reste du circuit doctrinal (demande formulée sans accès serveur
  possible côté Claude.ai — angle mort visé par la présence d'un agent côté
  dépôt).
- **Créé** : [[atelier/rd/outillage/2026-08-10_methode-croisement-discernement]]
  — documente le passage déterministe (script bash d'extraction frontmatter/
  wikilinks/`to-source`/termes sashimono, exécuté avant toute lecture par le
  modèle) et la logique de clustering (partition par statut, graphe de
  co-citation, contrôle de complétude du double contrôle Gizeh, détection
  d'artefacts, isolement des blocs mono-session). Rapport d'ingénierie pur —
  aucun contenu doctrinal.
- **Vérification** : `verifier-invariants.py` → 0 erreur, 1 avertissement
  (`[C1] lien non résolu : [[^]]` — faux positif : le motif regex bash cité en
  exemple dans le corps de la fiche contient la séquence `[[^]]`, lue à tort
  comme un wikilink par le scanner mécanique ; aucun lien réellement cassé).
- **Commit** : `3e2f6c7` — OUTILLAGE: Méthode de croisement des fiches discernement (rapport R&D)

---

## [2026-08-09] integration | fiche Obsidian/Working Copy/GitHub du sas → `rd/infrastructure/`

- **Directive Sidy** : tout ce qui relève de l'infrastructure se consigne au
  pôle R&D (« tu n'oublieras pas de tout rapporter au R&D »).
- **Fiche intégrée** : `_inbox/fiche-setup-obsidian-git-sync.md` (rédigée
  2026-06-29, dépannage de la synchro iPad) →
  `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`
  (`type: infrastructure`, dates conservées/bumpées, contenu repris avec
  l'avis technique Hermes du 2026-08-09 sur la décision SSH/PAT — verdict
  Sidy toujours attendu).
- **Sas vidé** : la fiche originale est retirée de `_inbox/` après
  intégration ; `karubi-mehdi.md` et `image.jpeg` restent au sas.
- **Rappel connexe** : entrée registre des problèmes [2026-08-09]
  (vault désynchronisé = 6 commits serveur non poussés, `resolu`).

---

## [2026-08-08] arbitrage | `album-personnel.md` déplacé vers `label/production/` (verdict Sidy)

- **Verdict Sidy** : l'album personnel relève de la **création artistique**
  (œuvre et production) — circuit `label/`, non le pôle R&D. Arbitrage
  `rd/` vs `label/` (proposition §IV) tranché en faveur de `label/`.
- **Déplacement** : `atelier/projets/album-personnel.md` →
  `label/production/album-personnel.md` ; contenu transféré à l'identique,
  Sceau Recteur §V.b appliqué (`type: production`, `medium: musique`,
  `projet: label`, `statut: en-cours`), note de gouvernance ajoutée.
- **Cmd 10 respecté** : stub `deprecated` avec pointeur conservé en `projets/`.
- **4 liens entrants coupés** (étanchéité §VI) :
  `materiel/{neve-1073spx, studio-principal, tascam-model-12, technics-su-8080}`
  pointaient vers la fiche (neutre → plus sensible, interdit) ; frontmatter et
  corps purgés, `updated` bumped. La référence légitime vit désormais côté
  label (`liens_atelier`, §V.b, sens licite label → materiel).
- **Index mis à jour** : `label/index.md` (§III, nouvelle sous-section
  « Œuvre »), `atelier/index.md`, `rd/index.md`, `doctrinal/index.md` §VIII
  (repointé), arborescence §II et journal CLAUDE.md.
- **Registre des problèmes** : nouvelle entrée consignée ; entrée
  « 10 anomalies » → `partiellement-resolu` (4/10 levées).
- **Vérification mécanique** : `verifier-invariants.py --racine /root/wiki` →
  **0 erreur(s), 0 avertissement(s)** ; graphe → 6 anomalies préexistantes
  hors périmètre (consignées au registre).

---

## [2026-08-08] restauration | Ouverture du registre des problèmes du pôle `rd/` (phase 2 — discipline de laboratoire)

- **Verdict Sidy** : mécanisme approuvé, avec amorçage rétroactif depuis la
  session de migration (3 entrées).
- **Fichier créé** : `atelier/rd/cahiers/registre-problemes.md` — cahier
  append-only, premier cahier ouvert du pôle ; format miroir du bloc 🧪
  Expérience appliqué à l'erreur (Symptôme brut / Diagnostic / Résolution /
  Compréhension tirée / Liens / Statut).
- **Amorçage rétroactif (3 entrées)** :
  1. `graphe-cartographie.json` jamais régénéré (bloqué par les anomalies du
     graphe) — ouvert ;
  2. 10 anomalies bloquantes du graphe (8 étanchéité + 2 frontmatter),
     pré-existantes, vérifiées contre la baseline HEAD — ouvert ;
  3. lien mort `manvantara → v0_2` (version inexistante), corrigé vers `v0.3`
     lors de la migration — résolu.
- **Index** : `rd/index.md` mis à jour (le registre entre dans l'arborescence).
- **Rien d'autre** : pas de modification de CLAUDE.md (Sceau et type `meta`
  suffisent), aucun nouveau circuit, aucune règle de lien nouvelle.

---

## [2026-08-08] migration | `atelier/projets/` → `rd/` — 16 fiches migrées (proposition §IV exécutée)

- **Opération** : migration fiche par fiche du dossier `projets/` vers le pôle
  `rd/` (verdict Sidy 2026-08-08, proposition §IV : « le dossier devient rd/
  par migration fiche à fiche ; chaque fiche migrée garde son slug, l'ancienne
  reçoit deprecated avec pointeur »).
- **Migrées vers `rd/instrument/` (15 fiches)** : architecture v0.1, v0.2,
  v0.3, v0_3 ; feuille-de-route-v2 ; spec-technique-axe-38-degres ;
  spec-anneau-zodiacal ; angles-de-l-espace ;
  references-visuelles-astronomiques-phase-5 ; soumission-gem-convergence-28 ;
  soumission-gem-reponse-geometrie-3d ; soumission-gem-reponse-gloton ;
  soumission-gem-reponse-visuelle-28 ;
  2026-07-26_investigation-referentiels-stellaires-cycles ;
  note-impact-instrument-socle-universel-2026-07-16.
- **Migrée vers `rd/outillage/` (1 fiche)** : spec-generateur-manifeste.
- **Cmd 10 respecté** : aucune suppression — chaque ancienne fiche reste en
  `projets/` comme stub `type: deprecated` avec pointeur vers la fiche
  canonique ; contenu des fiches inchangé, dates conservées, bandeau de
  migration inséré.
- **Assets et outillage déplacés avec les fiches** (git mv) :
  `assets-instrument/` (4 images), `instrument-donnees.yaml`,
  `wiki-manifest.json`, `instrument-prototype.html`, `generer-manifeste.py`
  (chemins par défaut du script mis à jour).
- **Scripts mis à jour** : `generer-manifeste.py` (chemins données/sortie →
  `rd/instrument/`) ; `Graphe/generer-cartographie.py` (rang d'étanchéité
  `atelier/rd` = 1, hérité de projets/, CLAUDE.md §VI).
- **Liens repointés** : 15 wikilinks entrants (atelier/index, doctrinal/index,
  4 fiches doctrinal/sources) + références textuelles (meta/projet-unifie/02,
  README, doctrinal/symboles/manvantara — pointait une version `v0_2`
  inexistante, corrigé vers v0.3 ; doctrinal/discernement/zodiaque-barzakh).
  Les annales et les cartes générées ne sont pas repointées (documents
  historiques / artefacts dérivés).
- **Non migré** : `album-personnel.md` — arbitrage `rd/` vs `label/` requis
  (proposition §IV : « à trancher fiche par fiche » ; verdict Sidy en attente).
- **Vérifications** : invariants (0 erreur), cartographie (0 nouvelle anomalie
  vs baseline : 9 anomalies d'étanchéité pré-existantes, identiques avant/après),
  manifeste régénéré (43 nœuds, 9 ancrages).

---

## [2026-08-08] restauration | Ouverture du pôle R&D `atelier/rd/` (verdict Sidy : Option C, phase 1 partielle)

- **Verdict consigné** : « Option C, nom `rd/`, phase 1 partielle. Tout ce qui
  en relève doit systématiquement y être consigné avec comme but l'entretien,
  le développement qualitatif, l'optimisation à mesure de l'infrastructure
  globale hardware/software, l'émancipation progressive de tout intermédiaire
  de service tiers par souveraineté des moyens de production/déploiement/
  information. Un des agents sera chargé de veiller à cette tâche spécifique. »
  Cinq circuits, inchangés (pas de sixième circuit).
- **Créé** : `atelier/rd/index.md` (charte du lieu, mission verbatim,
  frontières, état de phase) ; arborescence `rd/{instrument,infrastructure,
  audio,outillage,cahiers}/` (.gitkeep).
- **Amendements CLAUDE.md** : note de révision (second amendement 2026-08-08) ;
  §II arborescence atelier ; §V.a Sceau atelier étendu (types
  `experience | infrastructure | outillage`, `statut_experience` optionnel,
  `projets/` et `rd/` même régime de lien) ; §V.d `liens_atelier` élargi à
  `atelier/etudes-de-cas/` et `atelier/rd/` ; §VI hiérarchie d'étanchéité
  (rd/ hérite du régime de projets/, frontière meta/rd précisée) ; Cmd 9
  (annales de l'atelier inscrites à la liste).
- **Amendé** : `atelier/index.md` — régimes référence/recherche, section R&D,
  destination de migration de `projets/` signalée.
- **Déposé** : `meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08.md`
  (proposition d'origine, brouillon, commitée avec l'opération qu'elle a fondée).
- **Non inclus dans la phase 1 partielle** : migration de `atelier/projets/`
  (fiche par fiche, Cmd 10), discipline de laboratoire (phase 2), agent de
  veille infrastructure (phase 3, sur désignation de Sidy).
- **Vérification** : `python3 verifier-invariants.py --racine /root/wiki` →
  `0 erreur(s), 0 avertissement(s).` (exécuté avant le commit).
- **Commit** : 3c1b3d8

## [2026-08-08] archivage | Studio Principal — fiche-hub de l'espace d'atelier

- **Créé** : `atelier/materiel/studio-principal.md` (depuis `_inbox/studio-principal.md`) —
  fiche-hub de l'espace audio (trois pôles : synthèse/composition, enregistrement
  analogique, monitoring). `sources: ["to-source"]`, plusieurs points marqués
  incertains dans le corps (placement Yamaha H5, sync Tascam/Logic, configuration
  rack, acoustique).
- **Chevauchement traité** : deux appareils décrits dans la source
  (Neve 1073SPX, Tascam Model 12) avaient déjà leur fiche propre, sourcée
  (`chatgpt-export-2026-05-10`) — `atelier/materiel/neve-1073spx.md` et
  `atelier/materiel/tascam-model-12.md`. Décision (Sidy) : fiche-hub sans
  duplication — les deux fiches existantes sont référencées par wikilink et non
  redécrites ; seuls les éléments nouveaux (Moog Voyager, Fender Rhodes, Revox A77,
  micros, Yamaha H5, Distressor EL8x, chaîne de capture) sont documentés en propre.
- **Deux fichiers déjà déposés à l'appui, non encore confrontés au texte** :
  `raw/assets/studio-principal-vue-generale.jpeg`, `raw/assets/routing-schema.html`
  — signalés en §« Sources à déposer » de la fiche.
- **`atelier/index.md`** : ajout d'une entrée sous « Matériels & Techniques ».
- `verifier-invariants.py --racine /root/wiki` : à exécuter avant commit.

## [2026-07-27] spec-anneau + instrument-donnees.yaml | Dédoublement 19/20, 7 prophètes planétaires

- **Opération** : ARCHIVAGE ET CORRECTION — intégration spec anneau zodiacal et mise à jour YAML avec 7 ancrages établis + paramètres zodiaque.
- **Créé** : `atelier/projets/spec-anneau-zodiacal.md` (copié de _inbox/, quatre amendements appliqués)
- **Modifié** : `atelier/projets/instrument-donnees.yaml` (v0.3.1 → v0.3.2 *draft*)
- **Contenu des amendements à spec-anneau** :
  * **§3.1** : dédoublement confirmé (19/20, Toit/Terre du Jardin), avec justification doctrinale Gloton pp. 39-40. Two constantes `degre_falak_al_buruj: 19` + `degre_falak_al_manazil: 20` (12 signes vs 28 manāzil).
  * **§3.3** : paramètre époque validé (`epoque_reference`), avec justification ad-dahr (le Temps pur siège au degré 19).
  * **§3.1 (addendum)** : confirmation degré 19 par trois voies (Gloton, hiérarchie islamique, table 28 degrés) — point ouvert 5 clos.
  * **§3.4** : non-alignement renforcé, deux divisions cessent d'être superposées sur support unique.
- **Contenu YAML (v0.3.2)** :
  * 7 ancrages prophètes planétaires ajoutés (degrés 21-27) : Abraham/Saturne/samedi → Adam/Lune/lundi, source Gloton pp. 39-40 + Mahdi Rouge articles I-II, statut `etabli`.
  * Section `zodiaque:` ajoutée : `degre_falak_al_buruj: 19`, `degre_falak_al_manazil: 20`, `obliquite_deg: 23.44`, `epoque_reference: null` (à paramétrer Phase 5).
  * Nœuds/ancrages structurants inchangés ; version YAML remise à jour sans validation de manifeste (crédit API insuffisant en fin de session).
- **Validation** : spec-anneau relue (4 amendements grammaticaux + jusifications doctrinales), YAML syntaxe valide (grep/inspection manuelle).
- **Points de vigilance** :
  * Dédoublement 19/20 : correction ergonomique *et* doctrinale. Deux anneaux concentriques à deux hauteurs distinct (rendu à décider : deux couronnes ou deux niveaux différents selon Phase 5 UI).
  * Paramètre époque : validé comme concept, valeur concrète (JD ou UTC) à fixer en Phase 5 (calcul astrologique multi-méthodes) — actuellement `null`.
  * Prophètes planétaires : ancrage établi sur identité prophète↔ciel↔degré (données akbariennes primaires), distinct de l'ancrage Aqtâb guénonien (Phase 3). Aucun élément dans instrument-donnees.yaml tant que fiche discernement septénaire transversal n'est pas close.
  * Aucune génération manifeste en fin de session (crédit API insufficient) — à valider en prochaine session après rédaction fiche discernement.
- **Prochaine étape** : rédaction fiche discernement [[doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil]] (plan consigné), fermeture du lot B, validation manifeste + commit final du v0.3.2.
- **Note de méthode** : le dédoublement 19/20 rend visible une articulation doctrinale explicitée par la source (Gloton) — pas de « correction pour le confort visuel » mais exécution d'une structure sourcée que la table implicite. Aucun ancrage dans YAML tant que la fiche discernement n'est pas validée (Cmd 13).

---

## [2026-07-17] archivage | instrument-donnees.yaml v0.3.1 + ancrage Aqtâb (Phase 2)

- **Opération** : ARCHIVAGE — intégration d'une version mise à jour du YAML applicatif.
- **Remplacé** : `atelier/projets/instrument-donnees.yaml` (v0.3 du 2026-07-01) → v0.3.1
  du 2026-07-17.
- **Contenu** :
  * 36 nœuds déclarés (8 notionnels structurants/traversants + 28 nœuds-degrés 11-38).
  * 3 ancrages `établi` :
    - (a) table-28 ↔ manazil-al-qamar (convergence des 28, inchangé depuis v0.3)
    - (b) table-28 ↔ nafas-rahmani (convergence des 28, inchangé depuis v0.3)
    - (c) **NOUVEAU** : table-28 ↔ sept-Pôles/Aqtâb guénoniens, **cible: null**, sourcé par
      `doctrinal/discernement/2026-07-16_sept-poles-aqtab-malakut-planetaire`. Identité
      doctrinale (non-syncrétisme), confirmée par convergences textuelles guénoniennes
      (3 sources indépendantes) + source akbarienne antérieure (1911).
- **Validation** : exécuté `python3 generer-manifeste.py --repo /root/wiki` → ✓ 0 erreur,
  36 nœuds, 3 ancrages, 0 avertissements, commit 996ee452c13d.
- **Point de vigilance** :
  * Ancrage (c) sans nœud cible : l'Instrument ne modélise actuellement que la tradition
    `tasawwuf` (Phase 2, multi-traditions, Phase 3 non ouverte). L'ancrage est porté sur
    le nœud structurant `table-28-degres-nafas-rahman` en attente de déclaration d'un
    nœud `aqtab` formel. Placement confirmé par Sidy avant intégration.
  * Réserve résiduelle (fiche doctrinal) : lien explicite wirātha↔aqtāb non localisé dans
    extrait transmis du Futūḥāt ch. 36 — à rechercher pour ancrage (c) plus complet.
- **Génération manifeste** : `wiki-manifest.json` produit sans anomalie.

---
