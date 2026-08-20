---
title: "État d'avancement et pistes de développement — Instrument de la Tradition Primordiale (2026-08-20)"
type: meta
statut: synthese
tags: [instrument, rd, bilan, pistes-developpement, feuille-de-route]
created: 2026-08-20
updated: 2026-08-20
sources: []
links: ["[[atelier/rd/instrument/instrument-feuille-de-route-v2]]", "[[atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3]]", "[[atelier/rd/instrument/spec-anneau-zodiacal]]", "[[atelier/rd/instrument/spec-technique-axe-38-degres]]", "[[atelier/rd/instrument/angles-de-l-espace]]", "[[atelier/rd/instrument/2026-07-26_investigation-referentiels-stellaires-cycles]]", "[[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16]]", "[[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]]"]
---

# État d'avancement et pistes de développement — Instrument de la Tradition Primordiale

## Contexte de cette fiche

Le rapport conjoint Studio–Gardien du 2026-08-20 (`_inbox/rapport-conjoint-studio-gardien-etude-depot-20260820.md`) devait déterminer les pistes de développement du dépôt/infrastructure en général et de l'Instrument en particulier. Le Gardien s'est enlisé techniquement en session (contexte massif, échec de compression — voir
[[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]]) et l'orchestrateur a produit à sa place un rapport de vigilance pure, hors sujet par rapport à la demande initiale. Cette fiche reprend la demande d'origine côté Instrument. Le pendant infrastructure générale est consigné séparément dans
[[atelier/rd/infrastructure/2026-08-20_pistes-developpement-infrastructure]].

**Méthode** : lecture intégrale des 13 fichiers de `atelier/rd/instrument/` (feuille de route, trois versions d'architecture, 2 specs techniques, 4 soumissions au persona « Gem René Guénon », note d'impact, investigation référentiels stellaires, catalogue de références visuelles), confrontée au prototype et aux données réellement présents sur disque (`instrument-prototype.html`, `instrument-donnees.yaml`, `wiki-manifest.json`).

**Posture** : signalement et pistes, aucun verdict (Cmd 12/13). Les priorités proposées sont des propositions de travail, pas des arbitrages.

---

## 1. Où en est réellement le chantier — par phase

| Phase | Objet | État réel |
|---|---|---|
| 0 | Décisions d'architecture technique | **Close** — moteur Three.js/WebGL, cible web mobile, hébergement statique, format `wiki-manifest v0.2.1` figé (arbitrages du 2026-07-01, actés en v0.3 §8.3) |
| 1 | Générateur de manifeste (dépôt → manifeste) | **Livré** — `generer-manifeste.py`, déterministe, zéro LLM dans la boucle ; `wiki-manifest.json` réellement généré (36 nœuds : 8 notionnels/structurants + 28 nœuds-degrés) |
| — | Prototype de rendu | **Existe et fonctionne** (correction d'un constat erroné, voir §2) — `instrument-prototype.html`, Three.js réel, v0.1 datée du 2026-07-01 : axe des 38 degrés, Barzakh supérieur, filament d'al-Insān al-Kāmil, boucle 38→11, anneau des nœuds notionnels |
| 2 | Rendu de la tradition pilote (Tasawwuf) | **En cours** — bloqué sur la table des 38 degrés (colonnes Lettre/Nom Divin/Façç/Manzil manquantes pour les degrés 21-23 et 25-27, dépouillement Gloton requis) et sur la validation du rendu d'Al-Insān al-Kāmil |
| 3 | Multi-traditions et ancrages | **Ouverte le 2026-08-04**, un seul jalon posé (nœuds universels, sept Pôles/Aqtâb) ; Kabbale et Vedānta non ouverts dans l'arbre |
| 4 | Onglet apophatique (implémentation applicative) | **Pratiquée manuellement en continu** depuis le 2026-06-29 (validé 2026-07-01) ; non codée dans le prototype |
| 5 | Couche astrologique (calcul multi-méthodes) | **La moins avancée** — aucune spécification de calcul ; seulement des matériaux préparatoires (angles de l'espace, investigation stellaire *speculatif*, images de référence) et des paramètres laissés en attente dans les specs existantes (obliquité paramétrable, origine tropical/sidéral, paramètre d'époque) |

**Correction à noter** (§2) : le prototype `instrument-prototype.html` (v0.1) rend déjà une partie substantielle de l'axe. Le chantier n'est donc pas « sans aucune ligne de rendu 3D » mais **avec un prototype fonctionnel non mis à jour** depuis les arbitrages v0.3 (pas d'anneau zodiacal, pas de lentille barzakh optique détaillée, pas de nœuds universels). La piste de développement la plus concrète est donc une **mise à jour du prototype existant**, pas un démarrage ex nihilo.

## 2. Écarts documentaires relevés (hygiène, à corriger)

1. **Feuille de route périmée** : `instrument-feuille-de-route-v2.md` (updated 2026-08-04) désigne encore, dans son bandeau d'ouverture, l'architecture **v0.2** comme document canonique « validé dans ses principes », alors que la v0.3 (updated 2026-08-11) existe, la remplace, et tranche 4 des 5 questions ouvertes listées au §3 de la feuille de route (moteur 3D, hébergement, directions horizontales, méthode de vigilance apophatique — seule reste ouverte la question du modèle assistant la génération du manifeste). La feuille de route elle-même porte une clause de vigilance documentaire (§5) qui aurait dû déclencher cette mise à jour. **Non corrigé dans cette passe** (document pivot, à revoir par Sidy plutôt que réécrit d'office) — signalé ici pour action.
2. **`to-source` non répercuté** : l'architecture v0.3 §8 liste encore l'appariement qualités↔angles (AS=Sec, DS=Humide, MC=Chaud, FC=Froid) comme un point restant, alors que `angles-de-l-espace.md` (même date, 2026-07-01) le lève explicitement — confirmé par Sidy sur le manuscrit original. Simple désynchronisation de statut entre deux fiches du même jour.
3. **Tension Burckhardt/Jurjānī disparue sans trace** : la v0.2 §3.4 documentait une tension non résolue entre la lecture de Burckhardt (cinq paliers séquentiels) et celle d'al-Jurjānī (*Kitāb al-Taʿrīfāt*, dichotomies emboîtées) sur la structure des Cinq Présences, renvoyée à une fiche `doctrinal/discernement/tension-hadarat-burckhardt-jurjani`. Ce paragraphe **n'apparaît plus dans la v0.3** — sans mention de clôture ni de fiche de discernement citée en remplacement. Point à vérifier par Sidy : la tension a-t-elle été tranchée ailleurs, ou simplement omise lors de la réécriture de la v0.3 ?
4. **Soumissions « Gem » jamais closes formellement** : les 4 fiches `soumission-gem-*.md` (toutes datées du 2026-07-01) sont des brouillons de dialogue avec un persona IA — par construction « reconstruction plausible », jamais source (discipline des sources, CLAUDE.md racine §VII). Leur contenu de fond a été absorbé le même jour dans `spec-technique-axe-38-degres.md` et l'architecture v0.3 §8, mais les 4 fiches elles-mêmes ne portent aucune mention de clôture et restent, en l'état, lisibles comme si les questions qu'elles posent étaient encore ouvertes. Piste d'hygiène (non exécutée ici, verdict Sidy requis) : leur ajouter un bandeau de statut (« absorbée dans spec-technique-axe-38-degres.md, 2026-07-01 ») pour éviter qu'un futur agent les relise comme des questions en attente de réponse.

## 3. Pistes de développement proposées (classées, aucune tranchée)

**P1 — débloquer la Phase 2 (rendu Tasawwuf, actuellement « en cours »)**
1. Dépouiller Gloton (*De la mort à la résurrection*) pour compléter les degrés 21-23 et 25-27 de la table des 38 degrés (Lettre/Nom Divin/Façç/Manzil).
2. Valider (ou réviser) le rendu d'Al-Insān al-Kāmil — actuellement une proposition non validée dans le prototype.
3. Spécifier le détail optique de la lentille barzakh (degrés 19-20), laissé ouvert par l'architecture v0.3.

**P2 — mettre le prototype à niveau de l'architecture v0.3**
4. Intégrer l'anneau zodiacal (`spec-anneau-zodiacal.md` : deux degrés distincts 19/20, obliquité ≈23°26′ paramétrable, noms des 12 signes encore à peupler dans `instrument-donnees.yaml`) — actuellement spécifié mais absent du prototype v0.1.
5. Intégrer les nœuds universels (sept Pôles/Aqtâb, §3.5 v0.3, ajoutés le 2026-08-04) — absents du prototype v0.1, postérieur uniquement à la v0.2.

**P3 — amorcer la Phase 5 (couche astrologique), aujourd'hui la moins avancée**
6. Statuer sur le paramètre d'époque et l'origine du zodiaque (tropical/sidéral) — questions explicitement renvoyées à cette phase par `spec-anneau-zodiacal.md` §3.3/§7.
7. Décider si l'hypothèse H3 de `2026-07-26_investigation-referentiels-stellaires-cycles.md` (convergence Gizeh/Idrīs/Hermès au degré 24) — qualifiée par le document lui-même de « peut-être la pièce la plus neuve » mais non instruite, `status: speculatif`, `to-source` — mérite l'ouverture d'une fiche `discernement` dédiée avant toute intégration.
8. Constituer la bibliothèque prioritaire signalée par cette même investigation (Guénon *Le Roi du Monde*, *La Grande Triade*, *Symbolisme de la Croix*, Tilak) pour vérifier ses hypothèses sur texte primaire — actuellement aucune n'est sourcée.

**P4 — hygiène documentaire (bas risque, exécutable rapidement sur validation)**
9. Remettre à jour le bandeau de `instrument-feuille-de-route-v2.md` pour pointer vers la v0.3 (écart §2.1).
10. Vérifier/clarifier le sort de la tension Burckhardt/Jurjānī (écart §2.3).
11. Marquer les 4 fiches `soumission-gem-*` comme absorbées, avec pointeur vers les documents qui en ont repris le fond (écart §2.4).
12. Ouvrir la fiche `discernement` « Adam Qadmôn = al-Insān al-Kāmil » avant tout ancrage YAML de la branche Kabbale (rappel de `note-impact-instrument-socle-universel-2026-07-16.md` §C.6 — le document indique qu'un verdict a été rendu le 2026-07-26, à vérifier/confirmer).

**P5 — chantiers de fond, non urgents**
13. Fondation équivalente à `hadarat-khams` pour la branche séphirothique (dix Sephiroth, trois colonnes) avant tout ancrage Kabbale complet dans l'Arbre unique.
14. Étudier ultérieurement (piste non exclusive, non prioritaire) un rattachement des Noms Divins aux quatre Angles de l'espace, écarté pour l'instant au profit de la lecture élémentaire (Sec/Humide/Chaud/Froid).

---

## 4. Rappel de méthode

Aucune de ces pistes n'engage une intégration YAML, un ancrage `hozo`, ou une modification du prototype sans validation explicite de Sidy (Cmd 6, Cmd 12, Cmd 13). Cette fiche consigne un état des lieux et des directions de travail ; elle ne clôt aucune question ouverte et ne modifie ni `instrument-donnees.yaml`, ni `instrument-prototype.html`, ni les fiches citées.
