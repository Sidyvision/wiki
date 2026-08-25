---
title: "État d'avancement et pistes de développement — Instrument de la Tradition Primordiale (2026-08-20)"
type: meta
statut: synthese
tags: [instrument, rd, bilan, pistes-developpement, feuille-de-route]
created: 2026-08-20
updated: 2026-08-25
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
| — | Prototype de rendu | **Existe et fonctionne** (correction d'un constat erroné, voir §2) — `instrument-prototype.html`, Three.js réel, v0.1 datée du 2026-07-01 : axe des 38 degrés, Barzakh supérieur, filament d'al-Insān al-Kāmil, boucle 38→11, anneau des nœuds notionnels. **Mis à jour le 2026-08-20** (§5, deux passes) : sept nœuds Aqtâb + nœud Homme Universel rendus, filament enrichi, anneau zodiacal (12 signes + 28 manāzil, deux degrés distincts) |
| 2 | Rendu de la tradition pilote (Tasawwuf) | **En cours** — sur la validation du rendu d'Al-Insān al-Kāmil. ⚠️ **Correction du 2026-08-25** : le constat ci-contre était périmé — Lettre/Nom Divin/Manzil des degrés 21-23 et 25-27 sont complets depuis le 2026-08-25 (transcription pp. 46-47 Gloton, [[doctrinal/symboles/table-28-degres-nafas-rahman]]) ; seule la colonne façç (Fuṣūṣ), non utilisée par `instrument-donnees.yaml`, reste to-source et n'est pas bloquante |
| 3 | Multi-traditions et ancrages | **Plus avancée qu'évalué initialement** (correction §0.2) — ouverte le 2026-08-04, **deux** jalons universels **clos par discernement et désormais intégralement déclarés et rendus** (2026-08-20) : (a) sept Pôles/Aqtâb ↔ Malakūt planétaire (verdict 2026-07-16/08-04) ; (b) Adam Qadmôn = al-Insān al-Kāmil = Wang = Vaishwânara, l'Homme Universel à quatre voiles (verdict 2026-07-26, [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]]) — `instrument-donnees.yaml` v0.3.4, `wiki-manifest.json` régénéré, prototype à jour. Kabbale et Vedānta restent non ouverts comme arbres-traditions propres (la fiche (b) ne les ouvre pas, elle établit un nœud transversal) |
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
1. ~~Déclarer le nœud universel **Homme Universel**~~ — **fait le 2026-08-20**
   (§5, feu vert explicite de Sidy) : nœud `universel/homme-universel` et son
   ancrage (`equivalence`, `etabli`) déclarés dans `instrument-donnees.yaml`
   v0.3.4, cible `tasawwuf/al-insan-al-kamil`, source
   [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]].
   `wiki-manifest.json` régénéré (`generer-manifeste.py`, 44 nœuds, 10
   ancrages, 0 erreur). Prototype enrichi en conséquence.
2. ~~Vérifier le sort de la tension Burckhardt/Jurjānī~~ — sans objet, close depuis le 2026-07-09 (§0.1, §2.3).

**P2 — débloquer la Phase 2 (rendu Tasawwuf, actuellement « en cours »)**
3. ~~Dépouiller Gloton (*De la mort à la résurrection*) pour compléter les degrés 21-23 et 25-27 de la table des 38 degrés (Lettre/Nom Divin/Façç/Manzil).~~ **Fait le 2026-08-25** pour Lettre/Nom Divin/Manzil (pp. 46-47) ; seule la colonne façç reste ouverte, non bloquante (cf. correction §2 ci-dessus).
4. Valider (ou réviser) le rendu d'Al-Insān al-Kāmil — actuellement une proposition non validée dans le prototype.
5. Spécifier le détail optique de la lentille barzakh (degrés 19-20), laissé ouvert par l'architecture v0.3.

**P3 — mettre le prototype à niveau de l'architecture v0.3 (le reste)**
6. ~~Intégrer l'anneau zodiacal~~ — **fait le 2026-08-20** (§5) : deux degrés distincts (19 signes / 20 manāzil), obliquité 23,44°, 12 signes peuplés dans `instrument-donnees.yaml`. Reste ouvert : origine du zodiaque et époque de référence, renvoyés à la Phase 5 (P4.8).
7. ~~Intégrer les nœuds universels (sept Pôles/Aqtâb)~~ — **fait le 2026-08-20** (§5) : sept nœuds rendus, équivalence établie visuellement marquée. Second nœud universel (Homme Universel) également fait (P1.1).

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
**Vérification effectuée (première passe)** : syntaxe JavaScript valide
(`new Function`) ; exécution du bloc de rendu testée hors navigateur (mocks
Three.js minimaux, sans WebGL) — les sept nœuds Aqtâb se créent aux bonnes
hauteurs (degrés 21→27), avec les bons libellés et la bonne source ; le
filament porte le nouveau texte attendu ; total des objets interactifs
conforme (43 = 28 degrés + 7 Aqtâb + 6 notionnels + 1 filament + 1 Barzakh).

### Seconde passe (feu vert de Sidy, même session) : Homme Universel + anneau zodiacal

4. **Nœud Homme Universel ajouté** — sphère positionnée près du filament
   (offset symétrique aux Aqtâb), reliée par une ligne d'équivalence établie
   au point traversant du filament, info-bulle citant
   [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]].
   Donnée déclarée en amont dans `instrument-donnees.yaml` v0.3.4 (§ P1.1) et
   manifeste régénéré (44 nœuds, 10 ancrages, 0 erreur/avertissement).
5. **Anneau zodiacal ajouté** — deux groupes distincts, chacun incliné de
   23,44° (obliquité de l'écliptique) : au degré 19 (Falak al-Burūj), les 12
   signes en séparateurs radiaux pleine largeur + étiquette ; au degré 20
   (Falak al-Manāzil), 28 graduations discrètes sans étiquette permanente
   (spec §3.4 — non-commensurabilité 12/28 respectée, aucun alignement forcé,
   Art. 3 sashimono). Rayons 2,60–2,95 (2,60–2,74 pour les graduations), sous
   les jetons `--argent` de la palette existante, conformément à
   `spec-anneau-zodiacal.md` §3.5. Signes sourcés de la « TABLE COMPLÈTE À
   QUATRE COLONNES » de `doctrinal/symboles/table-28-degres-nafas-rahman.md`
   (colonne « Signe Zodiaque », Gloton pp. 45-48) — noms français uniquement,
   la table source ne donnant pas de nomenclature arabe des signes (non
   inventée). **Correction au passage** : le module inséré au §6 de la spec
   plaçait les deux divisions (signes ET manāzil) sur un seul groupe, au seul
   degré `degre_falak_al_buruj` — lecture devenue obsolète depuis l'arbitrage
   du dédoublement (§3.1, verdict Sidy 2026-07-27, postérieur à l'écriture du
   code de la spec) ; implémenté ici avec deux groupes à deux degrés distincts,
   fidèle à l'arbitrage le plus récent plutôt qu'à l'exemple de code.
6. ~~Lacune signalée~~ — **fermée le 2026-08-20 (troisième passe, sur
   demande explicite de Sidy)** : `generer-manifeste.py` propage désormais
   le bloc `zodiaque:` dans `wiki-manifest.json` (clé `zodiaque`, schéma
   manifeste v0.2.2), avec validations dédiées — bloquantes sur malformation
   structurelle (types, `label` de signe manquant), non bloquantes sur
   dérive plausible (degré sans nœud correspondant, nombre de signes ≠ 12).
   Documenté dans `spec-generateur-manifeste.md` §5 bis. Le prototype garde
   sa transcription manuelle (hébergement statique, aucun fetch réseau à
   l'exécution — inchangé), mais le manifeste est désormais la source
   complète et vérifiable mécaniquement ; un commentaire dans le prototype
   pointe vers cette convention. Testé : garde-fou vérifié en injectant un
   signe sans `label` (bloque, code retour 1) ; génération réelle sans
   erreur ni avertissement (44 nœuds, 10 ancrages, zodiaque inclus).

### Quatrième passe (2026-08-20) : lecture dynamique du manifeste par le prototype

7. **Le prototype lit désormais réellement `wiki-manifest.json`** (verdict
   Sidy : « plus cohérent »). `fetch` sur chemin relatif avant le chargement
   de Three.js ; dérivation intégrale des données doctrinales depuis le
   manifeste (28 nœuds-degrés, 6 notionnels de l'anneau, ancrages rendus,
   7 Aqtâb, Homme Universel, filament, Barzakh, bloc zodiacal). Plus aucune
   donnée doctrinale à retaper après une régénération : le flux
   `dépôt → manifeste → interface` est effectif de bout en bout, et non plus
   seulement déclaratif. Détail dans
   [[atelier/rd/outillage/spec-generateur-manifeste]] §5 ter.
   - **Repli conservé** (Art. 5 sashimono) : un instantané des mêmes données
     subsiste en littéraux ; si le manifeste est inaccessible (`file://` hors
     serveur, fichier absent), la scène s'affiche à l'identique — aucune
     régression d'usage sur iPad.
   - **Provenance affichée** dans le panneau de titre : schéma, SHA court du
     dépôt et nombre de nœuds quand le manifeste est lu ; mention explicite
     « données de repli » sinon.
   - **Délai de garde** de 4 s : une lecture qui n'aboutit pas bascule sur le
     repli, le rendu n'est jamais bloqué par le réseau.
   - **Limite assumée** : bandes de présentation (Lāhūt, Jabarūt…) et
     géométrie restent en dur — choix de rendu, non données doctrinales, non
     portées par le schéma du manifeste. Les étiquettes 3D abrègent
     mécaniquement les titres longs ; l'info-bulle porte toujours le libellé
     intégral.
   - **Vérifié** : les deux chemins testés hors navigateur (avec manifeste →
     provenance « manifeste v0.2.2 · dépôt 4616a97 · 44 nœuds », ancrages
     dérivés sur les identifiants complets ; sans manifeste → repli, mêmes
     44 objets interactifs). `fetch` du chemin relatif vérifié contre un
     serveur HTTP local (manifeste et page servis, HTTP 200). Rendu visuel
     toujours non vérifié en navigateur réel (CDN Three.js bloqué en session).

**Vérification effectuée (seconde passe)** : syntaxe JavaScript valide ;
exécution testée hors navigateur — 44 objets interactifs (43+1 Homme
Universel), 8 anneaux (`RingGeometry`) créés dont les 2 nouveaux du zodiaque,
aucune erreur. **Rendu visuel non vérifié dans un navigateur réel** dans les
deux passes : le prototype charge Three.js depuis un CDN externe
(cdnjs/unpkg), bloqué par la politique réseau de cet environnement de
session (`gateway 403` confirmé) — à vérifier par Sidy en conditions réelles
(iPad/Safari, connexion internet).

---

## 6. Rappel de méthode

Aucune des pistes restantes de la section 3 n'engage d'exécution
supplémentaire sans validation explicite de Sidy (Cmd 6, Cmd 12, Cmd 13).
Les deux passes du §5 sont des exceptions délibérées, sur consigne explicite
et immédiate de Sidy en session (« tu as le feu vert » pour la seconde),
strictement limitées à la traduction technique et au rendu d'ancrages déjà
établis par discernement clos (Homme Universel) ou de matière déjà sourcée
sans ancrage nouveau (anneau zodiacal) — aucun nouvel arbitrage doctrinal
n'a été pris dans l'une ou l'autre passe. `instrument-donnees.yaml` (v0.3.4)
et `wiki-manifest.json` ont été modifiés en seconde passe uniquement, tous
deux consignés ici et dans les annales.
