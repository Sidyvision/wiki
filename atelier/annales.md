---
title: Annales de l'Atelier (Projets et Matériels)
type: meta
updated: 2026-08-08
---

# Annales de l'Atelier

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

<!-- INSERTION: EN-TÊTE -->

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
