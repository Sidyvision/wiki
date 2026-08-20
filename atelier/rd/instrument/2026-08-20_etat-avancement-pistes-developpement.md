---
title: "État d'avancement et pistes de développement — Instrument de la Tradition Primordiale (2026-08-20)"
type: meta
statut: synthese
tags: [instrument, rd, bilan, pistes-developpement, feuille-de-route]
created: 2026-08-20
updated: 2026-08-20
sources: []
links: ["[[atelier/rd/instrument/instrument-feuille-de-route-v2]]", "[[atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3]]", "[[atelier/rd/instrument/spec-anneau-zodiacal]]", "[[atelier/rd/instrument/spec-technique-axe-38-degres]]", "[[atelier/rd/instrument/angles-de-l-espace]]", "[[atelier/rd/instrument/2026-07-26_investigation-referentiels-stellaires-cycles]]", "[[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16]]", "[[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]]", "[[doctrinal/discernement/tension-hadarat-burckhardt-jurjani]]", "[[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]]", "[[atelier/rd/cahiers/registre-problemes]]"]
---

# État d'avancement et pistes de développement — Instrument de la Tradition Primordiale

## Contexte de cette fiche

Le rapport conjoint Studio–Gardien du 2026-08-20 (`_inbox/rapport-conjoint-studio-gardien-etude-depot-20260820.md`) devait déterminer les pistes de développement du dépôt/infrastructure en général et de l'Instrument en particulier. Le Gardien s'est enlisé techniquement en session (contexte massif, échec de compression — voir
[[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]]) et l'orchestrateur a produit à sa place un rapport de vigilance pure, hors sujet par rapport à la demande initiale. Cette fiche reprend la demande d'origine côté Instrument. Le pendant infrastructure générale est consigné séparément dans
[[atelier/rd/infrastructure/2026-08-20_pistes-developpement-infrastructure]].

**Méthode** : lecture intégrale des 13 fichiers de `atelier/rd/instrument/` (feuille de route, trois versions d'architecture, 2 specs techniques, 4 soumissions au persona « Gem René Guénon », note d'impact, investigation référentiels stellaires, catalogue de références visuelles), confrontée au prototype et aux données réellement présents sur disque (`instrument-prototype.html`, `instrument-donnees.yaml`, `wiki-manifest.json`).

**Posture** : signalement et pistes, aucun verdict (Cmd 12/13). Les priorités proposées sont des propositions de travail, pas des arbitrages.

---

## 0. Corrections apportées suite au retour de Sidy (même session, 2026-08-20)

Sidy a signalé deux erreurs dans la première version de cette fiche :

1. **Traçabilité en défaut** : le point « tension Burckhardt/Jurjānī disparue
   sans trace » (ancien §2.3) était une fausse alerte — la tension **est close
   depuis le 2026-07-09** (voir [[doctrinal/discernement/tension-hadarat-burckhardt-jurjani]],
   `status: traditionnel`, verdict de Sidy), bien avant l'écriture de la v0.3
   (2026-08-11). La méthode initiale (diff des deux versions du seul document
   Instrument) n'avait pas consulté `doctrinal/discernement/`. Corrigé ci-dessous
   (§2). Leçon consignée : [[atelier/rd/cahiers/registre-problemes]], entrée
   `[2026-08-20] resolu | Traçabilité en défaut`.
2. **Phase 3 sous-évaluée** : Sidy estimait le chantier plus avancé en Phase 3,
   compte tenu des sources récemment intégrées. Vérification faite : un
   **second nœud universel est déjà établi** (discernement clos
   `status: traditionnel`) mais n'a jamais été porté dans
   `instrument-donnees.yaml` ni dans le prototype — voir §1 et §3 P1 ci-dessous.

**Action déjà effectuée dans cette même passe** (sur consigne explicite de
Sidy — « commence par mettre à jour le prototype ») : `instrument-prototype.html`
a été mis à jour pour rendre ce qui est établi mais n'était pas rendu — voir
§1 et §5.

---

## 1. Où en est réellement le chantier — par phase

| Phase | Objet | État réel |
|---|---|---|
| 0 | Décisions d'architecture technique | **Close** — moteur Three.js/WebGL, cible web mobile, hébergement statique, format `wiki-manifest v0.2.1` figé (arbitrages du 2026-07-01, actés en v0.3 §8.3) |
| 1 | Générateur de manifeste (dépôt → manifeste) | **Livré** — `generer-manifeste.py`, déterministe, zéro LLM dans la boucle ; `wiki-manifest.json` réellement généré (36 nœuds : 8 notionnels/structurants + 28 nœuds-degrés) |
| — | Prototype de rendu | **Existe et fonctionne** (correction d'un constat erroné, voir §2) — `instrument-prototype.html`, Three.js réel, v0.1 datée du 2026-07-01 : axe des 38 degrés, Barzakh supérieur, filament d'al-Insān al-Kāmil, boucle 38→11, anneau des nœuds notionnels. **Mis à jour le 2026-08-20** (§5) : sept nœuds Aqtâb rendus, filament enrichi de son identité à quatre voiles |
| 2 | Rendu de la tradition pilote (Tasawwuf) | **En cours** — bloqué sur la table des 38 degrés (colonnes Lettre/Nom Divin/Façç/Manzil manquantes pour les degrés 21-23 et 25-27, dépouillement Gloton requis) et sur la validation du rendu d'Al-Insān al-Kāmil |
| 3 | Multi-traditions et ancrages | **Plus avancée qu'évalué initialement** (correction §0.2) — ouverte le 2026-08-04, **deux** jalons universels déjà **clos** par discernement : (a) sept Pôles/Aqtâb ↔ Malakūt planétaire (verdict 2026-07-16/08-04, dans `instrument-donnees.yaml`, désormais rendu au prototype) ; (b) Adam Qadmôn = al-Insān al-Kāmil = Wang = Vaishwânara, l'Homme Universel à quatre voiles (verdict 2026-07-26, [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]], `status: traditionnel`) — **établi mais jamais déclaré dans `instrument-donnees.yaml`**, seul le filament tasawwuf-seul était rendu. Kabbale et Vedānta restent non ouverts comme arbres-traditions propres (la fiche (b) ne les ouvre pas, elle établit un nœud transversal) |
| 4 | Onglet apophatique (implémentation applicative) | **Pratiquée manuellement en continu** depuis le 2026-06-29 (validé 2026-07-01) ; non codée dans le prototype |
| 5 | Couche astrologique (calcul multi-méthodes) | **La moins avancée** — aucune spécification de calcul ; seulement des matériaux préparatoires (angles de l'espace, investigation stellaire *speculatif*, images de référence) et des paramètres laissés en attente dans les specs existantes (obliquité paramétrable, origine tropical/sidéral, paramètre d'époque) |

**Correction à noter** (§2) : le prototype `instrument-prototype.html` (v0.1) rend déjà une partie substantielle de l'axe. Le chantier n'est donc pas « sans aucune ligne de rendu 3D » mais **avec un prototype fonctionnel non mis à jour** depuis les arbitrages v0.3 (pas d'anneau zodiacal, pas de lentille barzakh optique détaillée, pas de nœuds universels). La piste de développement la plus concrète est donc une **mise à jour du prototype existant**, pas un démarrage ex nihilo.

## 2. Écarts documentaires relevés (hygiène, à corriger)

1. **Feuille de route périmée** : `instrument-feuille-de-route-v2.md` (updated 2026-08-04) désigne encore, dans son bandeau d'ouverture, l'architecture **v0.2** comme document canonique « validé dans ses principes », alors que la v0.3 (updated 2026-08-11) existe, la remplace, et tranche 4 des 5 questions ouvertes listées au §3 de la feuille de route (moteur 3D, hébergement, directions horizontales, méthode de vigilance apophatique — seule reste ouverte la question du modèle assistant la génération du manifeste). La feuille de route elle-même porte une clause de vigilance documentaire (§5) qui aurait dû déclencher cette mise à jour. **Non corrigé dans cette passe** (document pivot, à revoir par Sidy plutôt que réécrit d'office) — signalé ici pour action.
2. **`to-source` non répercuté** : l'architecture v0.3 §8 liste encore l'appariement qualités↔angles (AS=Sec, DS=Humide, MC=Chaud, FC=Froid) comme un point restant, alors que `angles-de-l-espace.md` (même date, 2026-07-01) le lève explicitement — confirmé par Sidy sur le manuscrit original. Simple désynchronisation de statut entre deux fiches du même jour.
3. ~~Tension Burckhardt/Jurjānī disparue sans trace~~ — **corrigé (§0.1), n'est pas un écart.** La v0.2 §3.4 documentait cette tension comme non résolue ; le paragraphe n'apparaît plus dans la v0.3 parce que [[doctrinal/discernement/tension-hadarat-burckhardt-jurjani]] a été **close le 2026-07-09** (verdict Sidy : les deux nomenclatures traitées comme deux découpages complémentaires d'une même doctrine, Cmd 3 respecté) — cinq semaines avant l'écriture de la v0.3 (2026-08-11). Le retrait du paragraphe est la conséquence normale de la clôture, pas un oubli de traçabilité.
4. **Soumissions « Gem » jamais closes formellement** : les 4 fiches `soumission-gem-*.md` (toutes datées du 2026-07-01) sont des brouillons de dialogue avec un persona IA — par construction « reconstruction plausible », jamais source (discipline des sources, CLAUDE.md racine §VII). Leur contenu de fond a été absorbé le même jour dans `spec-technique-axe-38-degres.md` et l'architecture v0.3 §8, mais les 4 fiches elles-mêmes ne portent aucune mention de clôture et restent, en l'état, lisibles comme si les questions qu'elles posent étaient encore ouvertes. Piste d'hygiène (non exécutée ici, verdict Sidy requis) : leur ajouter un bandeau de statut (« absorbée dans spec-technique-axe-38-degres.md, 2026-07-01 ») pour éviter qu'un futur agent les relise comme des questions en attente de réponse.

## 3. Pistes de développement proposées (classées, aucune tranchée)

**P1 — Phase 3 : formaliser ce qui est déjà établi (le plus mûr, le moins cher)**
1. Déclarer le nœud universel **Homme Universel** (Adam Qadmôn = al-Insān
   al-Kāmil = Wang = Vaishwânara) dans `instrument-donnees.yaml`, à la manière
   des sept nœuds `universel/aqtab-*` — discernement déjà clos
   ([[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]],
   `status: traditionnel`), il ne s'agit que de traduction technique d'un
   verdict déjà rendu, pas d'un nouvel arbitrage (Cmd 6). Régénérer ensuite
   `wiki-manifest.json` (`generer-manifeste.py`) et enrichir le prototype en
   conséquence (le filament porte déjà la mention textuelle, §5, mais pas
   encore de nœud/ancrage déclaré en donnée).
2. ~~Vérifier le sort de la tension Burckhardt/Jurjānī~~ — sans objet, close depuis le 2026-07-09 (§0.1, §2.3).

**P2 — débloquer la Phase 2 (rendu Tasawwuf, actuellement « en cours »)**
3. Dépouiller Gloton (*De la mort à la résurrection*) pour compléter les degrés 21-23 et 25-27 de la table des 38 degrés (Lettre/Nom Divin/Façç/Manzil).
4. Valider (ou réviser) le rendu d'Al-Insān al-Kāmil — actuellement une proposition non validée dans le prototype.
5. Spécifier le détail optique de la lentille barzakh (degrés 19-20), laissé ouvert par l'architecture v0.3.

**P3 — mettre le prototype à niveau de l'architecture v0.3 (le reste)**
6. Intégrer l'anneau zodiacal (`spec-anneau-zodiacal.md` : deux degrés distincts 19/20, obliquité ≈23°26′ paramétrable, noms des 12 signes encore à peupler dans `instrument-donnees.yaml`) — actuellement spécifié mais absent du prototype.
7. ~~Intégrer les nœuds universels (sept Pôles/Aqtâb)~~ — **fait le 2026-08-20** (§5) : sept nœuds rendus, équivalence établie visuellement marquée. Reste à intégrer le second nœud universel (P1.1).

**P4 — amorcer la Phase 5 (couche astrologique), aujourd'hui la moins avancée**
8. Statuer sur le paramètre d'époque et l'origine du zodiaque (tropical/sidéral) — questions explicitement renvoyées à cette phase par `spec-anneau-zodiacal.md` §3.3/§7.
9. Décider si l'hypothèse H3 de `2026-07-26_investigation-referentiels-stellaires-cycles.md` (convergence Gizeh/Idrīs/Hermès au degré 24) — qualifiée par le document lui-même de « peut-être la pièce la plus neuve » mais non instruite, `status: speculatif`, `to-source` — mérite l'ouverture d'une fiche `discernement` dédiée avant toute intégration.
10. Constituer la bibliothèque prioritaire signalée par cette même investigation (Guénon *Le Roi du Monde*, *La Grande Triade*, *Symbolisme de la Croix*, Tilak) pour vérifier ses hypothèses sur texte primaire — actuellement aucune n'est sourcée.

**P5 — hygiène documentaire (bas risque, exécutable rapidement sur validation)**
11. Remettre à jour le bandeau de `instrument-feuille-de-route-v2.md` pour pointer vers la v0.3 (écart §2.1).
12. Marquer les 4 fiches `soumission-gem-*` comme absorbées, avec pointeur vers les documents qui en ont repris le fond (écart §2.4).

**P6 — chantiers de fond, non urgents**
13. Fondation équivalente à `hadarat-khams` pour la branche séphirothique (dix Sephiroth, trois colonnes) avant tout ancrage Kabbale complet dans l'Arbre unique.
14. Étudier ultérieurement (piste non exclusive, non prioritaire) un rattachement des Noms Divins aux quatre Angles de l'espace, écarté pour l'instant au profit de la lecture élémentaire (Sec/Humide/Chaud/Froid).

---

## 5. Mise à jour du prototype effectuée le 2026-08-20 (sur consigne de Sidy)

`instrument-prototype.html` a été modifié pour rendre ce que les données
établissent déjà (`instrument-donnees.yaml` v0.3.3, `wiki-manifest.json`
généré le 2026-08-08) mais que le prototype v0.1 (2026-07-01, antérieur à
l'ouverture de la Phase 3) ne rendait pas encore :

1. **Sept nœuds Aqtâb ajoutés** — une sphère par pôle (degrés 21-27), reliée
   par une ligne d'équivalence établie (même traitement visuel que la
   « convergence des 28 ») au nœud-degré correspondant, avec info-bulle
   citant [[doctrinal/discernement/2026-07-16_sept-poles-aqtab-malakut-planetaire]]
   comme source. Légende mise à jour (nouvelle entrée « nœud universel »).
2. **Filament d'al-Insān al-Kāmil enrichi** — label et info-bulle mentionnent
   désormais l'identité à quatre voiles traditionnelles (Adam Qadmôn/Wang/
   Vaishwânara) établie le 2026-07-26, avec citation de la fiche
   `discernement` correspondante en plus de la fiche `symboles/al-insan-al-kamil`.
3. **Non fait dans cette passe** : le nœud universel « Homme Universel »
   lui-même n'a pas de sphère/ancrage dédié dans le prototype — il n'existe
   pas encore comme nœud déclaré dans `instrument-donnees.yaml` (P1.1
   ci-dessus). L'enrichissement du filament (point 2) est un correctif de
   surface (texte de l'info-bulle), pas l'intégration complète en donnée.
   L'anneau zodiacal (P3.6) n'a pas non plus été touché.

**Vérification effectuée** : syntaxe JavaScript valide (`new Function`) ;
exécution du bloc de rendu testée hors navigateur (mocks Three.js minimaux,
sans WebGL) — les sept nœuds Aqtâb se créent aux bonnes hauteurs (degrés
21→27), avec les bons libellés et la bonne source ; le filament porte le
nouveau texte attendu ; total des objets interactifs conforme (43 = 28
degrés + 7 Aqtâb + 6 notionnels + 1 filament + 1 Barzakh). **Rendu visuel
non vérifié dans un navigateur réel** : le prototype charge Three.js depuis
un CDN externe (cdnjs/unpkg), bloqué par la politique réseau de cet
environnement de session (`gateway 403` confirmé) — à vérifier par Sidy en
conditions réelles (iPad/Safari, connexion internet).

---

## 6. Rappel de méthode

Aucune des pistes de la section 3 n'engage une intégration YAML, un ancrage
`hozo` nouveau, ou une modification supplémentaire du prototype sans
validation explicite de Sidy (Cmd 6, Cmd 12, Cmd 13). La modification
effectuée en §5 est une exception délibérée, sur consigne explicite et
immédiate de Sidy en session, strictement limitée au rendu d'un ancrage déjà
établi (aucun nouvel arbitrage) ; `instrument-donnees.yaml` et
`wiki-manifest.json` n'ont pas été modifiés.
