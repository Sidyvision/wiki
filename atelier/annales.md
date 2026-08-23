---
title: Annales de l'Atelier (Projets et Matériels)
type: meta
updated: 2026-08-23
---

# Annales de l'Atelier

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

<!-- INSERTION: EN-TÊTE -->

## [2026-08-23] archivage | Ihwan al-Safa' (Marquet) — 5 fiches, lot 2

Transcription manuelle intégrale du lot 2 (34 photographies, `raw/La Philosophie
des Ihwan al-Safa/`) — décision d'emblée manuelle (méthode OCR Hermes écartée dès
le départ, taux d'échec confirmé sur le lot 1). Plan validé par Sidy : 4 fiches de
base + fiche séparée pour l'Introduction, Bibliographie et Liste des abréviations
regroupées en une seule fiche.
- **Fiche 1** : `index-notions-ihwan-al-safa.md` (pages 613-616, IMG_0001-0004)
- **Fiche 2** : `index-noms-ihwan-al-safa.md` (pages 609-612, IMG_9996-9999)
- **Fiche 3** : `table-ihwan-al-safa.md` (pages 617-620, IMG_0005-0008)
- **Fiche 4** : `bibliographie-ihwan-al-safa.md` (pages 600-608, IMG_9987-9995 — Liste
  des abréviations + Bibliographie regroupées)
- **Fiche 5** : `introduction-ihwan-al-safa.md` (pages V, VII-XV, IMG_9975-9986 —
  ordre de lecture réel restitué, distinct de l'ordre brut des prises de vue ;
  lacune réelle notée : page VI absente du corpus photographié)
- **Dépôt** : `atelier/rd/bibliotheque/` (Sceau atelier, type: ressource)
- **Contrôle** : verifier-invariants.py → aucune erreur ni avertissement sur les 5
  fiches (5 erreurs et 62 avertissements préexistants, sans rapport avec ce lot)
- **Discipline des sources** : sources marquées `to-source` ; `to-verify` préservés
  sur les passages denses en colonnes (Index des notions, pages VIII/IX-XI/XIV de
  l'Introduction) et les deux photos de bibliographie sous-exposées (IMG_9989,
  IMG_9995)
- **Git** : staging ciblé des 5 chemins exacts uniquement (`git add` nommé, jamais
  `-A`) — le dépôt contient par ailleurs des travaux non liés en cours, non touchés

Prochain lot en attente : La Porte du Ciel (lot 3, ~52 images).

- **Commit** : 804c38a

## [2026-08-23] archivage | Index et table des matières Rig-Veda (Langlois/Foucaux)

Intégration du lot 1 de photographies indexées (Rig-Veda, 11 images).
- **Fiche 1** : `index-rig-veda.md` (nature: index_rerum, pages 628-654, ~1670 entrées OCR manuel)
- **Fiche 2** : `index-rig-veda-table.md` (nature: table, pages 41-599, 8 sections × 8 lectures)
- **Dépôt** : `atelier/rd/bibliotheque/` (Sceau atelier, type: ressource)
- **Contrôle** : verifier-invariants.py → aucune erreur nouvelle
- **Discipline des sources** : sources marquées `to-source` ; convention_pages en `to-verify` où résolution insuffisante (légende IMG_0093)

Travaux amont (session antérieure + cette session) : transcription manuelle des 4 images bloquées par panne Hermes silent (IMG_0100-0103) ; tentative OCR ciblé légende (IMG_0093) — abandon après deux échecs identiques (0-byte output) ; construction des deux fiches selon modèle atelier/rd.

Prochains lots en attente : Ihwān al-Ṣafā' (lot 2, 34 images), La Porte du Ciel (lot 3, 59 images).

- **Commit** : fa86680

## [2026-08-22] correction | Panne silencieuse du controle photo + repercussions d'index

Passe de correction faisant suite a l'ouverture de `rd/bibliotheque/` le meme
jour, sur trois points non couverts par la passe initiale.

1. **Controle H1 en panne silencieuse (bloquant).** Le controle « photographie
   declaree vs photographie reelle » de `valider-index-livres.py` ne s'armait
   qu'a deux conditions cumulees : `dossier_raw` present en frontmatter et
   `--raw` passe en argument. Or `dossier_raw` n'etait pas dans `CLES_REQUISES`,
   `--raw` valait `None` par defaut, et `valider_index_livres_shim.py` ne le
   transmettait pas — donc **par le chemin automatise (generateur), le controle
   ne s'executait jamais**. Constat empirique avant correction, sur une fiche
   declarant `IMG_9999` inexistant : generateur `code: 0`, validateur autonome
   avec `--raw` `code: 1` (H1 bloquant). Correction : `dossier_raw` ajoute aux
   cles requises, `--raw` par defaut resolu vers le `raw/` du depot, argument
   transmis par le shim. Re-test apres correction : generateur `code: 1`, REFUS.
   C'est la garantie meme que le script `compare` perdu apportait.
2. **`atelier/index.md`** — non repercute lors de la passe initiale (seul le
   sous-index `rd/index.md` l'avait ete). `rd/bibliotheque/` y figure desormais.
   `updated` porte a 2026-08-22.
3. **Cahier de lecons** — `2026-08-22_lecons-chantier-bibliotheque-index-livres.md`,
   livrable explicite de la mission (les lecons de la formation d'un agent
   reviennent a `rd/`). Huit sections, aucun contenu doctrinal.

Divers : marqueur `<!-- INSERTION: QUEUE -->` de `_inbox/UPDATES.md` remis en
queue de fichier (il precedait la premiere entree, ce qui aurait inverse
l'ordre des insertions suivantes).

**Cmd 15 — cinquieme occurrence de la journee**, commise dans le paragraphe du
cahier qui decrit ce mode d'echec. Detectee au balayage de fin de passe,
retiree, et **consignee dans le cahier lui-meme** plutot que corrigee en
silence.

**Verification mecanique independante, rapportee brute** (`verifier-invariants.py`) :
`5 erreur(s), 62 avertissement(s)` — identique a la cloture de la passe
precedente. Les 5 erreurs sont **anterieures et non imputables a ces passes** :
`atelier/stealing-reasoning-traces-rd.md` (B0, aucun frontmatter) et les deux
fiches `atelier/rd/incidents/2026-08-22_*` (B1, `created`/`updated` manquants).
Les 62 avertissements sont le bruit `C1` connu des documents citant des
wikilinks bruts.

**Cmd 9 non satisfait** : `/root/wiki` n'est pas un depot git, aucun SHA
disponible. Signale, non contourne. Point au verdict de Sidy.


## [2026-08-22] ouverture | Instrument de repérage — `atelier/rd/bibliotheque/`

Ouverture du chantier des index et glossaires photographiés de la bibliothèque
physique, sous supervision (l'exécution OCR revient à l'agent Hermes, rôle #13).

- **Vidange du sas** `_inbox/` avant travail (verdict Sidy) : deux rapports
  studio/gardien versés en `atelier/rd/cahiers/`, `citadelle-du-sham/` versé en
  `atelier/rd/citadelle-du-sham/`. Création de `_inbox/UPDATES.md` (append-only).
- **Déplacement** de `meta/bibliotheque-physique.md` vers
  `atelier/rd/bibliotheque/catalogue-bibliotheque.md` (verdict Sidy). Motif : un
  catalogue d'ouvrages disponibles au travail n'est pas un fait personnel, et en
  `meta/` aucun circuit ne pouvait le citer (§VI, aucun lien entrant). Tombstone
  `deprecated` conservé à l'ancien chemin (Cmd 10). `type: meta` → `type: ressource`.
- **Deux références de `CLAUDE.md` reprises** (l. 180 arborescence, §VII
  discipline des sources), sauvegarde `CLAUDE.md.bak-2026-08-22-pre-deplacement-bibliotheque`.
- **Ajout au catalogue** de *La Philosophie des Ihwān al-Ṣafā'* — seul des trois
  ouvrages du chantier réellement absent. Rectification : *Rig-Véda* (l. 128) et
  *La Porte du ciel* (l. 53) y figuraient déjà ; ma recherche initiale, sans
  accent, les avait manqués.
- **Deux scripts écrits**, lignée `carte-du-depot.py` (déterministe, stdlib
  seule, lecture seule, aucun jugement, artefact dérivé) :
  `valider-index-livres.py` et `generer-glossaire-unifie.py`.

Substitution assumée : le script `compare` prévu par §VIII.9 est introuvable au
dépôt ; `valider-index-livres.py` en reprend la fonction (§VIII.2, la
vérification mécanique indépendante est seul juge) sur l'objet du présent
chantier. Choix de conception : `completude` a été retiré du schéma de fiche —
c'était un champ de jugement qu'un agent aurait rempli ; la contiguïté des
photographies est désormais **calculée** par le validateur.

Incident Cmd 15, signalé sans être dissimulé : deux fichiers écrits ce jour
contenaient des points de code interdits — la ligne `grep` du prompt #13
(caractères littéraux au lieu de leurs échappements) et le dictionnaire
`INTERDITS` du validateur, qui se déclenchait ainsi sur lui-même. Corrigés dans
la même passe ; les points de code sont maintenant déclarés par `chr()`.
Recontrôle des huit fichiers écrits : **0 point de code interdit**.

Cmd 9 non satisfaite : `/root/wiki` n'est pas un dépôt Git (`git status` muet),
aucun SHA court n'est disponible. Signalé à Sidy, non contourné.


## [2026-08-22] rd | Incident sécurité — contamination ZWJ, nettoyage, Commandement 15

- **Détection** : caractères U+200D (Zero Width Joiner) détectés dans 31 fichiers
  du dépôt (156 occurrences), tous dans le mot « Hermes » (pattern `H[ZWJ]ermes`).
- **Investigation** : pas un marqueur sémantique (agent vs figure mythologique),
  pas une watermark légale — artefact de formatage (copier-coller contaminé ou
  éditeur).
- **Nettoyage** : suppression complète des 156 occurrences via `sed`.
- **Commandement 15** ajouté au protocole racine `CLAUDE.md` (§X) : interdiction
  formelle d'insérer des caractères Unicode invisibles (U+200B/C/D, U+FEFF,
  U+200E/F).
- **Pre-commit hook** installé (`.git/hooks/pre-commit`, exécutable) : détection
  automatique bloquante avant commit.
- **Rapport d'incident** : `atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`.
- **Brief Studio/Gardien** : `meta/briefs/2026-08-22_brief-incident-zwj-mise-a-jour-securite.md`.
- **Commit** : 4c1604c
- **Correction hook** : `grep -P` remplace `perl -ne` (bug encodage UTF-8).
  Commit 350fd8a.

## [2026-08-20] rd | Compte-rendu de clôture — malentendu Gardien et reprise de session

- **Contexte** : consigne explicite de Sidy pour clore la session — instruire
  l'atelier/R&D du malentendu signalé plus tôt (« l'agent Gardien n'a pas
  compris ma demande »), en compte-rendu complet.
- **Fiche créée** :
  [[atelier/rd/cahiers/2026-08-20_compte-rendu-malentendu-gardien-reprise-session]].
  Diagnostic à deux causes distinctes : l'enlisement technique (déjà consigné,
  [[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]])
  explique pourquoi les agents désignés n'ont rien produit, **pas** pourquoi le
  rapport écrit à leur place par l'orchestrateur a dérivé vers un audit de
  vigilance plutôt que vers les pistes de développement demandées — dérive de
  cadrage distincte, le nom de l'agent ayant fini par déterminer le contenu du
  livrable au lieu de sa consigne.
- **Chronologie complète de la reprise** consignée (11 étapes, commits cités) :
  réparation mécanique, pistes de développement Instrument + infrastructure,
  mise à jour du prototype en plusieurs passes, ouverture de l'architecture des
  registres, registres hindouisme-tantra et vedanta, ancrage Homme Universel →
  Vaishwânara.
- **Auto-critique assumée** : la première instruction sur l'ouverture d'une
  branche Kabbale était factuellement fautive sur deux points (confusion
  domaine/degré ; présomption qu'un joint axial restait à établir alors qu'il
  était clos depuis le 2026-07-26) — corrigée par Sidy en session ; la
  correction a produit l'architecture des registres, réutilisée trois fois de
  plus dans la même session sans nouvelle extension du schéma.
- **Cinq leçons transversales** consignées pour l'atelier/R&D (revalider
  l'objet d'une tâche après incident ; ne pas laisser le nom d'un agent
  déterminer le contenu d'un livrable ; le formalisme protocolaire empêche
  l'importé et le supposé, pas l'établi ; la traçabilité prime sur
  l'inférence documentaire ; une architecture générique bien posée absorbe
  mieux une correction qu'un blocage ponctuel).
- **Index mis à jour** : `atelier/rd/index.md` (pointeur, `updated:`).
- **Commit** : `00a4a9a`

## [2026-08-20] rd | Registre vedanta — quatre états d'Âtmâ (v0.5.0)

- **Contexte** : Sidy demande de mettre l'ensemble en regard avec *L'Homme et
  son devenir selon le Vêdânta* pour compléter.
- **Renommage** `hindouisme` → `hindouisme-tantra` : deux expositions
  distinctes de Guénon (*Kundalinî-Yoga*/chakras vs États d'Âtmâ/*Vêdânta*) ne
  doivent pas partager un même id (« une page = un sujet »).
- **`instrument-donnees.yaml` v0.5.0** : quatrième registre `vedanta`, axe
  parallèle, 4 domaines en rang — Vaishwânara (veille), Taijasa (rêve),
  Prājña (sommeil profond), Turīya (le Quatrième) — colonne unique (états
  d'un même être, pas de structure droite/gauche). Sources déjà au dépôt,
  `traditionnel` :
  [[doctrinal/sources/guenon-homme-devenir-vedanta-ch10-15-16-brahma-turiya]]
  et [[doctrinal/sources/guenon-homme-devenir-vedanta-ch9-14]] (ch. XIV,
  Taijasa). Turīya porte l'asymétrie posée par le texte lui-même (les trois
  premiers pâdas ne comptent que pour un quart, le Quatrième vaut les trois
  autres quarts), reprise telle quelle.
- **Un ancrage déclaré, et un seul** : `universel/homme-universel` →
  `vedanta/vaishvanara`, `etabli`, même source que l'ancrage existant vers
  `tasawwuf/al-insan-al-kamil` (discernement clos 2026-07-26). **Ce n'est pas
  une correspondance nouvelle** — Vaishwânara fait déjà partie de l'identité
  Adam Qadmôn = al-Insān al-Kāmil = Wang = Vaishwânara. Taijasa, Prājña,
  Turīya et tous les domaines de qabbalah/hindouisme-tantra restent **sans
  ancrage** : le verdict ne nomme que Vaishwânara.
- **`generer-manifeste.py` v0.2.4** (commit séparé, préalable) : extension
  mécanique — un ancrage peut désormais viser un domaine de registre, pas
  seulement un nœud. Registres validés avant la boucle des ancrages, id de
  domaines fusionnés dans le même espace que les nœuds ; collision d'id
  bloquante (testée). Aucune donnée modifiée par cette seule extension (sortie
  strictement identique avant toute nouvelle donnée).
- **Prototype** : la sphère Vaishwânara reçoit une ligne d'équivalence établie
  vers le nœud Homme Universel, **pilotée par la donnée**
  (`HOMME_UNIVERSEL.cibles`, lu depuis le manifeste) — pas codée en dur.
  Vérifié hors navigateur : 65 objets interactifs, cibles dérivées
  correctement, ligne confirmée dans le graphe de scène.
- **Manifeste régénéré** : 44 nœuds, 11 ancrages, 4 registres, 0
  erreur/avertissement.
- **Fiches** :
  [[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3]] §6
  (renommé) et §7 (nouveau) ; `atelier/index.md`.
- **Vigilance** : aucun ancrage inter-registre nouveau au-delà de la
  traduction d'un verdict déjà clos (Cmd 3, Cmd 12).
- **Commits** : `5a01d00` (extension du générateur), `679b904` (registre
  vedanta).

---

## [2026-08-20] rd | Registre hindouisme — chakras sur sushumnā (v0.4.1)

- **Contexte** : Sidy demande de poursuivre avec le registre hindou,
  signalant que le corpus Guénon se trouve déjà en `raw/`.
- **Note d'accès** : `raw/` est exclu du dépôt git (`.gitignore`) et donc vide
  dans le clone de cette session — non bloquant : le texte primaire
  (*Kundalinî-Yoga*, *Études sur l'Hindouisme*) avait été déposé directement
  dans la conversation, et la fiche source correspondante existait déjà au
  dépôt depuis le 2026-07-14
  ([[doctrinal/sources/guenon-kundalini-yoga-etudes-hindouisme]],
  `traditionnel`).
- **`instrument-donnees.yaml` v0.4.1** : troisième registre, `hindouisme`
  (axe parallèle). 7 domaines en rang — 6 chakras + sahasrāra (Guénon
  lui-même : « les six chakras et sahasrâra ne forment qu'un total de
  sept »), colonne unique (`milieu`) : à la différence de la Kabbale, tous
  les centres sont sur l'axe central (*sushumnā*). *Idā* et *pingalā* sont
  des canaux, non des centres — documentés en donnée (champ `canaux`,
  informatif) mais non rendus comme domaines. Manifeste régénéré : 44
  nœuds, **3 registres**, 0 erreur/avertissement.
- **Signalement, non exécution** : Guénon donne dans ce même texte (§34-36)
  une correspondance rang-par-rang **explicite** entre les 7 niveaux
  séphirothiques et les 7 domaines hindous (Kether/Sahasrāra,
  Hokmah-Binah/Ājnā, Hesed-Geburah/Vishuddha, Tiphereth/Anāhata,
  Netsah-Hod/Manipūra, Iesod/Mūlādhāra — avec sa propre réserve sur le
  dernier couple). Sourcée et signalée dans
  [[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3]] §6
  comme candidat de premier ordre à une fiche `discernement` — **non
  déclarée comme ancrage** : un verdict, pas une exécution mécanique
  (Cmd 3, Cmd 12).
- **Index mis à jour** : `atelier/index.md` (pointeur registres, comptage).
- **Commit** : `b36834c`

---

## [2026-08-20] rd | Ouverture des registres — plusieurs traditions sur l'unique axe

- **Contexte** : redressement doctrinal de Sidy. L'instruction déposée plus tôt
  le même jour concluait que les sources kabbalistiques ne pouvaient être
  instrumentées sans nouveaux verdicts — conclusion fondée sur **deux erreurs
  de raisonnement**, corrigées ici :
  1. *« Incommensurabilité 38 / 5 / 7 »* — erreur de cadre : un **domaine**
     n'est pas un **degré**. Le dépôt pratique déjà la distinction (les cinq
     Ḥaḍarāt enveloppent les 38 degrés). Un septénaire de domaines est une
     **autre partition du même axe**, non une échelle concurrente.
  2. *« Transitivité non autorisée »* — erreur factuelle : le joint axial est
     **acquis** depuis le 2026-07-26
     ([[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]],
     clos). Situer un centre sur un axe déjà verdicté n'importe aucune
     correspondance.
  Était également faux : « il manque une fondation séphirothique » — elle
  existe ([[doctrinal/sources/kabbale-10-sefirot-structure]], `traditionnel`,
  10 Sephiroth sur 3 colonnes).
- **Architecture ouverte — le registre** : partition de l'unique axe vertical
  propre à une tradition. Les registres coexistent **sans être alignés**, même
  discipline que les 12 signes et les 28 manāzil de l'anneau zodiacal (Art. 3
  sashimono : le décalage est une donnée, pas un défaut).
- **`instrument-donnees.yaml` v0.4.0** : bloc `registres:` — `tasawwuf` (axe
  principal, 5 Ḥaḍarāt en bornes de degrés, reprise en donnée des bandes
  jusque-là codées en dur) et `qabbalah` (axe parallèle, 10 Sephiroth en rangs
  + colonnes, **aucun degré attribué**).
- **`generer-manifeste.py` v0.2.3** : propagation et validations dédiées. Un
  domaine portant à la fois `degres` et `rang` est **refusé** — ce serait
  déclarer en donnée une correspondance point à point qu'aucune tradition ne
  donne. Le Cmd 3 cesse d'être seulement écrit au protocole : il est
  **appliqué par l'outil**. Trois cas de rejet vérifiés en test.
- **Prototype** : rendu du registre parallèle en trois colonnes, en retrait du
  tronc akbarien, **sans aucune ligne vers les degrés**. Les 10 Sephiroth se
  répartissent sur **7 niveaux dérivés mécaniquement** des rangs et colonnes
  déclarés (couple droite/gauche = même niveau) : Kether / Hokhma-Bina /
  Hesed-Gevurah / Tiferet / Netzach-Hod / Yesod / Malkhut. **La réduction tombe
  des données**, elle n'est pas posée à la main — et recoupe celle que Guénon
  décrit en projetant les couples latéraux sur la colonne du milieu.
- **Requalification de la Sitra Ahra** : le correctif du 2026-06-29 rejetait le
  rattachement **structurel** du *waswâs* à la Sitra Ahra (imposer au tasawwuf
  une structure de miroir qu'il n'a pas nativement), **non** le rendu de la
  Sitra Ahra dans son expression kabbalistique propre — que l'architecture
  v0.3 §2 prescrit au contraire. Le tasawwuf l'exprime autrement (l'autre côté
  de la Montagne Qāf, cf.
  [[doctrinal/discernement/2026-07-02_mont-qaf-meru-topologie-apex]]). Voie
  praticable documentée, **non exécutée**.
- **Fiches** : [[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3]]
  (révision intégrale — la version fautive est remplacée, non conservée :
  elle n'énonçait aucun fait utile, seulement un blocage mal fondé) ;
  [[atelier/rd/outillage/spec-generateur-manifeste]] §5 quater.
- **Vigilance** : aucun ancrage inter-registres déclaré, aucun joint qualifié,
  aucune fiche doctrinale créée ou modifiée (Cmd 3, Cmd 12).
- **Commit** : `18e85b3`

---

## [2026-08-20] rd | Lecture dynamique du manifeste par le prototype + instruction branche Kabbale

- **Contexte** : deux demandes de Sidy — (a) rendre la lecture du manifeste
  dynamique dans le prototype (« plus cohérent »), (b) instruire l'ouverture
  d'une branche Kabbale, sources signalées comme devant « s'emboîter très
  facilement », avec dépôt d'un extrait de Guénon (*Études sur l'Hindouisme*,
  « Kundalinî-Yoga ») rapprochant *Sephiroth* et *chakras*.

**(a) Lecture dynamique — exécutée.** `instrument-prototype.html` lit
désormais `wiki-manifest.json` (`fetch`, chemin relatif, avant Three.js) et en
dérive l'intégralité de ses données doctrinales : 28 nœuds-degrés, 6
notionnels de l'anneau, ancrages rendus, 7 Aqtâb, Homme Universel, filament,
Barzakh, bloc zodiacal. Le flux `dépôt → manifeste → interface` devient
effectif de bout en bout. Trois garde-fous (Art. 5 sashimono) : repli intégral
en littéraux si le manifeste est inaccessible (`file://`, fichier absent) ;
provenance affichée dans le panneau de titre (schéma, SHA court, nombre de
nœuds — ou mention « données de repli ») ; délai de garde de 4 s. Sens de
lecture inchangé — l'interface lit, ne réécrit jamais (Cmd 12). Limite
assumée : bandes de présentation et géométrie restent en dur (rendu, non
donnée doctrinale). Documenté :
[[atelier/rd/outillage/spec-generateur-manifeste]] §5 ter. Vérifié : les deux
chemins testés hors navigateur ; `fetch` du chemin relatif vérifié contre un
serveur HTTP local (HTTP 200 sur page et manifeste). Rendu visuel toujours non
vérifié en navigateur réel (CDN Three.js bloqué en session).
- **Commit** : `44c8c13`

**(b) Branche Kabbale — instruite, non exécutée.** Fiche créée :
[[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3]].
Conclusion de l'instruction : la matière est réelle et abondante, mais
l'emboîtement **n'est pas immédiat** — trois obstacles formels documentés :
(1) incommensurabilité des divisions (38 degrés / 5 Ḥaḍarāt / 7 niveaux
séphirothiques — la clé de réduction est un acte doctrinal, non technique) ;
(2) transitivité non autorisée (Cmd 3) — Guénon pose *Sephiroth ↔ chakras*,
jamais *Sephiroth ↔ 38 degrés akbariens*, et le second joint n'existe pas au
dépôt ; (3) verrou de la Sitra Ahra — correctif de rejet acté le 2026-06-29,
validation bloquante dans `generer-manifeste.py`, et
[[doctrinal/discernement/2026-07-28_sept-tours-sitra-ahra]] encore « en
cours », déjà remonté comme `question_ouverte` par le générateur sur le nœud
`universel/homme-universel`. Croisement des deux septénaires (niveaux
séphirothiques ↔ sept Aqtâb) **signalé comme signal de vigilance**, laissé
entier ; confrontation Gizeh restant à faire (matière septénaire, §VII).
Chemin proposé en 5 étapes, aucune exécutée. **Aucun ancrage proposé, aucun
joint qualifié, aucune fiche doctrinale créée ou modifiée** (Cmd 6, Cmd 12).
- **Commit** : `39ab0f2`

- **Note de constat** : les quatre Sceaux incomplets signalés comme bloquants
  par le rapport conjoint (lot kabbale + fiche veille) sont réparés — la garde
  `Graphe/generer-cartographie.py --verifier` ne remonte plus aucune anomalie
  bloquante (116 avertissements non bloquants subsistent).

---

## [2026-08-20] rd | generer-manifeste.py propage le bloc zodiaque (schéma manifeste v0.2.2)

- **Contexte** : suite directe des deux entrées précédentes — Sidy a demandé
  de fermer l'écart signalé (le bloc `zodiaque:` déclaré en données depuis
  le 2026-07-26/27 mais jamais propagé dans `wiki-manifest.json`).
- **`generer-manifeste.py`** : nouvelle fonction `valider_zodiaque()` ;
  schéma du manifeste porté de v0.2.1 à v0.2.2. Validations bloquantes sur
  malformation structurelle (types, signe sans `label`) ; avertissements non
  bloquants sur dérive plausible (degré `falak_al_*` sans nœud correspondant,
  nombre de signes ≠ 12). Garde-fou testé (signe sans label → code retour 1,
  manifeste non produit) puis génération réelle : 44 nœuds, 10 ancrages,
  zodiaque inclus, 0 erreur/avertissement.
- **`spec-generateur-manifeste.md`** : §5 bis documente l'extension et son
  motif (règle commune des manifestes, CLAUDE.md racine §VII).
- **`instrument-prototype.html`** : commentaire ajouté sur le littéral
  `ZODIAQUE` pointant vers la nouvelle convention — le prototype garde sa
  transcription manuelle (hébergement statique, aucun fetch réseau à
  l'exécution), mais le manifeste est désormais la source complète et
  vérifiable mécaniquement.
- **Fiche mise à jour** :
  [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]
  (§5, point 6 — lacune fermée).
- **Commit** : `57e4bd1`

---

## [2026-08-20] rd | Homme Universel déclaré (v0.3.4) + anneau zodiacal rendu (feu vert Sidy)

- **Contexte** : suite directe de l'entrée précédente — Sidy a donné le feu
  vert pour exécuter les deux items encore ouverts de la fiche de pistes
  ([[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]])
  et a demandé explicitement où en était l'anneau zodiacal.
- **`instrument-donnees.yaml` v0.3.4** : nœud `universel/homme-universel`
  déclaré (Adam Qadmôn = al-Insān al-Kāmil = Wang = Vaishwânara), ancrage
  `equivalence`/`etabli` vers `tasawwuf/al-insan-al-kamil`, source
  [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]]
  (traduction technique d'un verdict déjà clos, aucun nouvel arbitrage —
  Cmd 6). Section `zodiaque.signes` peuplée : 12 signes sourcés de la
  « TABLE COMPLÈTE À QUATRE COLONNES » de
  [[doctrinal/symboles/table-28-degres-nafas-rahman]] (colonne « Signe
  Zodiaque », Gloton pp. 45-48) — noms français uniquement, pas de
  nomenclature arabe dans la source, non inventée (discipline des sources,
  CLAUDE.md racine §VII).
- **`wiki-manifest.json` régénéré** (`generer-manifeste.py`, déterministe) :
  44 nœuds, 10 ancrages, 0 erreur/avertissement.
- **`instrument-prototype.html`** : nœud Homme Universel rendu (satellite
  du filament, équivalence établie visuellement) ; anneau zodiacal rendu en
  deux groupes distincts — 12 signes au degré 19 (Falak al-Burūj), 28
  manāzil au degré 20 (Falak al-Manāzil), obliquité 23,44°, conformément à
  [[atelier/rd/instrument/spec-anneau-zodiacal]] §3.1 (dédoublement confirmé,
  verdict Sidy 2026-07-27). Correction au passage : le module de code inséré
  §6 de la spec plaçait les deux divisions sur un seul degré — lecture
  devenue obsolète depuis l'arbitrage du dédoublement, postérieur à
  l'écriture du code ; implémenté fidèlement à l'arbitrage le plus récent,
  pas à l'exemple de code.
- **Vérifié** : syntaxe JS valide, exécution du bloc de rendu testée hors
  navigateur (mocks Three.js, sans WebGL) — 44 objets interactifs, 8 anneaux
  dont les 2 nouveaux, 0 erreur. Rendu visuel non vérifié en navigateur réel
  (CDN Three.js bloqué par la politique réseau de la session) — à confirmer
  par Sidy.
- **Lacune signalée, non corrigée** : `generer-manifeste.py` ne propage pas
  la section `zodiaque:` dans le manifeste (seuls `noeuds`/`ancrages` le
  sont) — préexistante, non introduite ici.
- **Fiche mise à jour** :
  [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]
  (§1, §3 P1/P3 marquées faites, §5 seconde passe, §6) ; `atelier/index.md`.
- **Commit** : `08b2b3c`

---

## [2026-08-20] rd | Prototype de l'Instrument mis à jour (Aqtâb, filament) + correction de traçabilité Phase 3

- **Contexte** : retour de Sidy sur la fiche de pistes de développement du
  même jour — signalement de deux erreurs : (1) la tension
  Burckhardt/Jurjānī déclarée « disparue sans trace » de l'architecture
  était en réalité close depuis longtemps ; (2) la Phase 3 de l'Instrument
  jugée sous-évaluée compte tenu des sources récemment intégrées.
- **Vérification** : [[doctrinal/discernement/tension-hadarat-burckhardt-jurjani]]
  close le 2026-07-09 (verdict Sidy, `status: traditionnel`) — la fiche de
  synthèse a été corrigée en conséquence. Découverte d'un second nœud
  universel déjà établi et jamais intégré :
  [[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]]
  (Adam Qadmôn = al-Insān al-Kāmil = Wang = Vaishwânara, `status: traditionnel`,
  clos le 2026-07-26).
- **Prototype mis à jour** (consigne explicite de Sidy) :
  `atelier/rd/instrument/instrument-prototype.html` — sept nœuds Aqtâb
  rendus (degrés 21-27, équivalence établie visuellement, source citée),
  filament d'al-Insān al-Kāmil enrichi de son identité à quatre voiles.
  Vérifié : syntaxe JS valide, exécution du bloc de rendu testée hors
  navigateur (mocks Three.js, sans WebGL — CDN externe bloqué par la
  politique réseau de la session) ; rendu visuel non vérifié en navigateur
  réel, à confirmer par Sidy.
- **Fiches mises à jour** :
  [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]
  (§0 corrections, §1 Phase 3 réévaluée, §2 écart retiré, §3 pistes
  renumérotées P1-P6, §5 journal de la mise à jour du prototype) ;
  [[atelier/rd/cahiers/registre-problemes]] (leçon de méthode : consulter
  systématiquement `doctrinal/discernement/` avant de signaler une
  disparition documentaire comme anomalie) ; `atelier/index.md`.
- **Hors périmètre de cette passe** (Cmd 6) : déclaration du nœud « Homme
  Universel » dans `instrument-donnees.yaml`, régénération du manifeste,
  anneau zodiacal — restent en piste P1/P3.
- **Commit** : `3c72bd8`

---

## [2026-08-20] rd | Pistes de développement — Instrument et infrastructure (reprise du rapport conjoint)

- **Contexte** : le rapport conjoint Studio–Gardien du 2026-08-20 devait
  déterminer les pistes de développement du dépôt/infrastructure en général et
  du chantier Instrument en particulier. Le Gardien s'est enlisé techniquement
  en session (voir
  [[atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint]]),
  et le rapport produit à sa place par l'orchestrateur a dérivé vers un simple
  audit de vigilance, hors sujet par rapport à la demande. Reprise sur demande
  explicite de Sidy.
- **Fiches créées** :
  [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]] —
  état réel par phase du chantier Instrument (correction notable : un
  prototype Three.js v0.1 fonctionnel existe déjà, `instrument-prototype.html`,
  non mis à jour depuis l'architecture v0.3), écarts documentaires relevés
  (feuille de route pointant encore vers la v0.2, tension Burckhardt/Jurjānī
  disparue sans trace de la v0.3, soumissions « Gem » jamais closes
  formellement), pistes classées P1 à P5.
  [[atelier/rd/infrastructure/2026-08-20_pistes-developpement-infrastructure]] —
  état serveur/agents (omniroute non documenté, 28% de la RAM), chantiers déjà
  tranchés côté décision mais non exécutés (Phase 3 veille, Bureau TUI, SRS
  Hermes-native), piste d'applicabilité de la veille externe Cordis, pistes
  classées P1 à P4.
- **Index mis à jour** : `atelier/index.md`, pointeurs vers les deux fiches.
- **Méthode** : lecture intégrale des 13 fichiers de `rd/instrument/` et des
  documents infrastructure/cahiers/veille pertinents (délégué à un agent
  d'exploration en lecture seule), puis vérification directe contre les
  fichiers réels sur disque (le constat initial « aucune ligne de rendu 3D »
  était erroné — corrigé après inspection du prototype).
- **Vigilance** : signalement et pistes uniquement, aucune exécution, aucun
  accès credentials, aucune modification d'`instrument-donnees.yaml` ni du
  prototype (Cmd 6, Cmd 12, Cmd 13).
- **Commit** : `6e95a1a`

---

## [2026-08-20] réparation | Points mécaniques du rapport conjoint Studio–Gardien

- **Contexte** : rapport conjoint Studio–Gardien déposé en `_inbox/`
  (`rapport-conjoint-studio-gardien-etude-depot-20260820.md`), points 2, 14.
- Ajouté le Sceau atelier (`type`/`created`/`updated`/`sources`/`links`) à
  `atelier/rd/infrastructure/analyse-temporelle-code-meta-raisonnement-ia-2026-08-19.md`
  (fiche veille sans frontmatter, `type: infrastructure`).
- Complété `created`/`updated` sur
  `atelier/rd/infrastructure/incident-20260820-gardien-enlisement-rapport-conjoint.md`
  — blocage résiduel du manifeste apparu à la vérification de cette passe, non
  listé dans le tableau du rapport (fiche non trackée au moment de sa rédaction).
- Supprimé la double ligne vide avant séparateur (`atelier/annales.md:518`, A5).
- **Vérification mécanique** : `Graphe/generer-cartographie.py --verifier` :
  4 anomalies bloquantes (frontmatter) → 0 (après complément de l'incident) ;
  `verifier-invariants.py --racine /root/wiki` : 18 erreur(s) → 0.
- **Hors périmètre de cette passe** (décision réservée à Sidy, Cmd 12/13) :
  fusion du doublon `raw/` « Autorité Spirituelle et Pouvoir Temporel »,
  `atelier/R/`, déplacement de `organize_guenon.sh` vers `rd/outillage/`,
  qualification des 2 PDF du jour (`maymaniya_p1.pdf`,
  `claudes-constitution.pdf`), données personnelles en `raw/`, référence morte
  `UPDATES.md`/`MASTER-UPDATE.md`, convention du caractère ZWJ.
- **Commit** : `dafc266`

## [2026-08-20] rd | Rapport conjoint d'état du dépôt (préparation Gardien)

- **Fiche créée** : [[atelier/rd/infrastructure/rapport-conjoint-etat-depot-2026-08-20]]
  — synthèse d'exploration destinée au rapport conjoint avec Gardien.
  Observations consignées, aucune qualification rendue (Cmd 12).
- **Contenu** : carte vérifiée des circuits (doctrinal 260 / meta 118 /
  atelier 92 / hermeneutique 22 / label 13 `.md`), état du pôle `rd/`
  (68 fiches), vérifications mécaniques rejouées (`verifier-invariants`
  18 erreurs / 58 avertissements — dont 16 C1 d'auto-pollution d'un
  rapport du 08-18 ; `generer-cartographie --verifier` 4 anomalies
  frontmatter bloquantes ; bureau TUI 10 tests passés ; 3 cron sains),
  classification complète de `raw/` (444 fichiers : corpus Guénon 16
  dossiers, sources islamiques, manuels studio, documents administratifs
  signalés), état git (lot islamofuturisme du jour non committé), et
  11 points ouverts sans verdict — dont la découverte que `UPDATES.md`,
  référencé par le protocole, est absent du dépôt.
- **Complète** : [[atelier/rd/infrastructure/etude-depot-cartographie-inventaire-raw-2026-08-20]]
  (commit `6d0d43c`) — correction annexe : `/root/sandbox-rd/` existe
  mais est vide (l'étude du jour le disait absent).

## [2026-08-19] rd | Job cron Hermes `coherence-infrastructure-brute` réparé, archive du monitoring passée en cron dédié

- **Contexte** : suite de la clôture de session du 2026-08-18 (entrée
  ci-dessous) — deux points laissés en signalement seul y sont repris et
  résolus, sur feu vert explicite de Sidy en session (« tu as le feu vert
  pour tout rétablir »).
- **`coherence-infrastructure-brute` (id `ca9593f3a03d`, profil `studio`)** :
  réparé en deux temps. (1) « Script not found » — un premier remède par
  lien symbolique a été rejeté par Hermes lui-même (garde-fou de résolution
  de chemin canonique, hors du dossier `scripts/` du profil) ; remplacé par
  une copie réelle. (2) La copie réelle a révélé un second défaut, plus
  grave car silencieux : `last_status: "ok"` alors que le script, privé de
  `--racine` (un job `no_agent` ne transmet aucun argument), vérifiait 0
  affirmation au lieu de 3 — faux succès découvert par lecture directe de la
  sortie persistée, jamais par confiance dans le statut narré. Corrigé par
  une enveloppe (`verifier-coherence-infrastructure-cron.sh`) qui fixe
  `--racine /root/wiki` en dur. Re-vérifié : 3 affirmations, 0 écart.
- **Archive du monitoring quotidien — ingestion tranchée** : cron Hermes
  dédié (`archiver-monitoring-quotidien`, id `5eb46eed6ba0`, profil
  `studio`, `10 12 * * *`), via une enveloppe symétrique
  (`archiver-monitoring-quotidien-cron.sh`) pour la même raison (arguments
  fixés en dur). Déclenché manuellement pour vérification : sortie réelle
  lue directement, cohérente avec l'état déjà archivé.
- **Détail complet** : [[atelier/rd/cahiers/registre-problemes]], entrée
  `[2026-08-18]` (« Suite de l'entrée précédente ») ;
  [[atelier/rd/infrastructure/monitoring-archive-charte]] ;
  [[atelier/rd/outillage/spec-archiver-monitoring-quotidien]] ;
  [[atelier/rd/index]].
- **Commit** : c379f50

## [2026-08-18] rd | Cause racine cartographie corrigée, registre enrichi, archive monitoring quotidien (40j)

- **Contexte** : trois tâches de clôture de session R&D (Sidy) — (a) corriger
  à la racine `Graphe/generer-cartographie.py` pour qu'il lise les champs de
  liens français (`liens:`, `liens_atelier:`) en plus des champs anglais,
  au lieu du contournement précédent (chemins nus ajoutés côté agent) ;
  (b) consigner les leçons de la session au registre des problèmes R&D ;
  (c) archiver le rapport de monitoring infrastructure quotidien (livré via
  Discord) dans un dossier dédié du pôle R&D, rétention 40 jours, pour
  renforcer le monitoring de l'agent lui-même.
- **Actions** :
  1. `CHAMPS_LIENS` unifié dans `generer-cartographie.py` sur les 4 circuits
     (`sources`, `liens`, `liens_atelier`, `links`, `cross_links`) — mesure
     avant/après : 62 → 51 isolés du seul fait de cette correction, aucune
     régression d'étanchéité constatée.
  2. Deux entrées ajoutées à
     [[atelier/rd/cahiers/registre-problemes]] : la cause racine ci-dessus
     (avec quatre points ouverts pour verdict de Sidy) et une découverte
     annexe — le job cron Hermes `coherence-infrastructure-brute` (profil
     `studio`), censé être le contrôle anti-fabulation direct de l'étape 4
     du rapport quotidien, échoue depuis sa création (script introuvable au
     chemin résolu par Hermes pour un job `no_agent`) et n'est documenté
     nulle part. Signalé, non corrigé (modification d'un job de production,
     décision humaine requise).
  3. Nouveau dossier
     [[atelier/rd/infrastructure/monitoring-archive-charte|monitoring-archive/]]
     (charte + script déterministe
     [[atelier/rd/outillage/spec-archiver-monitoring-quotidien|
     archiver-monitoring-quotidien.py]]) : copie datée `.txt` (jamais `.md`,
     pour éviter que l'archive ne s'auto-déclenche sur ses propres tokens
     `[[...]]` cités en sortie brute) de chaque exécution du job Hermes
     `monitoring-infrastructure-quotidien`, purge au-delà de 40 jours.
     Découvert en cours de route : Hermes persiste déjà chaque sortie de job
     cron sur disque — le script se branche dessus sans toucher au job de
     production ni à Discord. Testé en dry-run puis appliqué : 2 rapports
     archivés (2026-08-17, 2026-08-18). Déclenchement récurrent (manuel ou
     cron dédié) laissé en attente de choix de Sidy.
  4. `atelier/rd/index.md` mis à jour (arborescence, état de phase).
- **Compréhension tirée** : troisième occurrence du motif « cron affirmé ≠
  cron fonctionnel » dans ce registre — un job `enabled + scheduled` ne
  garantit rien sur son historique réel de succès, seule une lecture directe
  de l'état Hermes (ou une inspection CLI qui manque aujourd'hui) le révèle.
- **Commit** : 61f3469

## [2026-08-18] archivage | Dossier SAV Neve 1073SPX + fiches matériel du studio

- **Contexte** : Sidy a signalé une panne de la fonction EQ sur le Neve 1073SPX
  (symptôme : aucun signal lorsque l'EQ est engagé). Retour SAV en cours
  (dossier STH 424556, appareil en cours de réception par AMS Neve).
- **Actions** :
  1. Factures Woodbrass déposées en `raw/` :
     - `facture-woodbrass-5003818-2026-02-05-neve-1073spx.pdf` (Neve 1073SPX,
       1 739 € TTC, achat 2026-02-05)
     - `facture-woodbrass-4902304-2025-11-07-tascam-model12.pdf` (Tascam Model
       12 + Neumann TLM 103 + stand, 1 960,90 € TTC, achat 2025-11-07)
  2. Fiche `neve-1073spx.md` enrichie : section `Identification et acquisition`
     (N° série 2255519, date d'achat, facture) + section `Historique
     maintenance` (timeline complète du dossier SAV) + source `raw/` du manuel
     constructeur ajoutée au frontmatter.
  3. Fiche `tascam-model-12.md` enrichie : section `Identification et
     acquisition` + section `Spécifications techniques` (extraites du manuel
     constructeur `raw/Model12_OM_EFS_RevH3.pdf`) + lien vers studio-principal
     ajouté.
  4. Fiches créées : `distressor-el8.md` (modèle EL8, correction 2026-08-18),
     `revox-a77.md`, `moog-voyager.md`, `neumann-tlm103.md`.
  5. **Enrichissement avec manuels constructeurs** (4 fiches sur 4 avec manuels
     disponibles dans `raw/`) :
     - `distressor-el8.md` : specs complètes extraites de
       `raw/distressor_manual.pdf`, marqueur `to-source` **levé**
     - `revox-a77.md` : specs complètes extraites des 3 manuels Revox
       (notice multilangue, owners, service), marqueur `to-source` **levé**
     - `tascam-model-12.md` : specs complètes extraites de
       `raw/Model12_OM_EFS_RevH3.pdf`, marqueur `to-source` **levé**
     - `neve-1073spx.md` : source du manuel ajoutée au frontmatter (specs
       déjà présentes dans la fiche)
     - `moog-voyager.md` et `neumann-tlm103.md` : pas de manuel disponible
       dans `raw/`, conservent le marqueur `to-source`
  6. Fiche `studio-principal.md` mise à jour : sections Distressor/Revox/Moog
     remplacées par liens vers fiches propres + lien vers TLM 103 dans tableau
     des micros.
  7. `atelier/index.md` enrichi avec les nouvelles fiches.
- **Liens** : [[atelier/materiel/neve-1073spx]], [[atelier/materiel/tascam-model-12]],
  [[atelier/materiel/distressor-el8]], [[atelier/materiel/revox-a77]],
  [[atelier/materiel/moog-voyager]], [[atelier/materiel/neumann-tlm103]],
  [[atelier/materiel/studio-principal]].
- **État final** :
  - Fiches avec marqueur `to-source` **levé** : distressor-el8, revox-a77,
    tascam-model-12, neve-1073spx (specs sourcées depuis manuels constructeurs)
  - Fiches conservant le marqueur `to-source` : moog-voyager, neumann-tlm103
    (pas de manuel disponible dans `raw/`), studio-principal (mémoire de session)
- **Vérification** : `verifier-invariants.py` → 0 erreur(s), 58 avertissement(s)
  (préexistants, non liés aux modifications de cette session).

## [2026-08-17] infrastructure | Synchronisation du mandat de l'agent studio (SOUL.md) avec sa configuration cron réelle

- **Symptôme** : question de Sidy — le rôle documenté de l'agent en charge du
  R&D (`SOUL.md` du profil `studio`) reflète-t-il les corrections de la
  session précédente (script `verifier-coherence-infrastructure.py`, second
  job cron `--no-agent`) ? Vérification mécanique (`jobs.json` du profil vs
  `SOUL.md`) : non — le job cron réel (`41dc3e7e492c`) portait déjà un prompt
  à 7 étapes incluant le script anti-fabulation en étape 4, mais `SOUL.md`
  décrivait toujours l'ancien mandat à 3 scripts / 5 sections, et ne
  mentionnait pas du tout le second job `coherence-infrastructure-brute`.
- **Diagnostic** : symétrique inverse du problème résolu plus haut le même
  jour — là, une fiche décrivait un état runtime inexistant ; ici, le runtime
  avait avancé sans que le mandat documenté de l'agent suive. Même famille
  d'angle mort (doc ↔ runtime), sens opposé.
- **Correction** : `SOUL.md` (`/root/.hermes/profiles/studio/`) et sa source
  canonique `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md`
  mis à jour à l'identique (diff vérifié vide après édition) : script 4
  ajouté à la liste du volet 1 avec sa justification (registre-problemes.md,
  entrée 2026-08-17), mention explicite du second job `--no-agent` comme
  garantie mécanique et de sa préséance en cas de désaccord, format de
  rapport porté de 5 à 8 sections.
- **Liens** : [[atelier/rd/cahiers/registre-problemes]] (entrée 2026-08-17,
  deuxième mise à jour), `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md`.
- **Commit** : b3de0c4

## [2026-08-17] outillage | Contrôle déterministe de cohérence infrastructure — angle mort doc/runtime

- **Symptôme** : investigation demandée par Sidy sur l'angle mort de
  continuité entre Claude Code, Hermes Terminal et les agents Discord.
  Mesure mécanique indépendante (§VIII.2) : `hermes --profile studio cron
  list --all` retournait « No scheduled jobs » alors que la fiche
  `activation-monitoring-studio-cron-2026-08-17.md`, commitée le jour même,
  affirmait la création d'un job `b7acb57e3d58` avec tableau de paramètres
  complet. Aucune trace côté log. 3ᵉ occurrence en 48h du motif « deux gestes
  distincts » (plan/prompt validé ≠ configuration Hermes opérée).
- **Diagnostic** : une consigne rédactionnelle seule (« vérifier avant de
  clore ») avait déjà été écrite dans cette même fiche et n'avait pas
  empêché la fiche elle-même de fabuler. Le remède ne pouvait pas être une
  nouvelle règle d'écriture.
- **Résolution** : entrée `registre-problemes.md` du 2026-08-17 ouverte puis
  close. Champ optionnel `infra_verif` ajouté au Sceau `type: infrastructure`
  (`atelier/CLAUDE.md`). Script déterministe `atelier/rd/outillage/
  verifier-coherence-infrastructure.py` (sans LLM, sans réseau) confrontant
  les affirmations `infra_verif` des fiches à l'état réel (`cron list --all`,
  `.env` Discord) — premier run : 1 écart reproduisant l'anomalie ; job cron
  `monitoring-infrastructure-quotidien` réellement créé (`41dc3e7e492c`,
  distinct de l'ID fabulé) ; second run : 0 écart. Second job cron
  `--no-agent --script` (`coherence-infrastructure-brute`, `ca9593f3a03d`)
  créé en garantie mécanique : livre le stdout brut du script sur
  `#infrastructure` chaque jour, sans passer par le LLM. `infra_verif` ajouté
  rétroactivement aux fiches des 16 et 17 août. `verifier-invariants.py` :
  0 erreur bloquante imputable à ces changements (2 erreurs préexistantes
  hors périmètre, non liées).
- **Leçon** : « fiabilité d'action ≠ fiabilité narrative » se blinde par un
  script, pas par une phrase — même écrite dans le bon document.
- **Liens** : [[atelier/rd/cahiers/registre-problemes]],
  [[atelier/rd/infrastructure/activation-monitoring-studio-cron-2026-08-17]],
  [[atelier/rd/infrastructure/activation-salon-infrastructure-studio-2026-08-16]].
- **Commit** : aae8660

## [2026-08-17] activation | monitoring quotidien (cron) + correction HOME_CHANNEL — profil studio

- **Constat** : après extension du SOUL.md du profil `studio` (volet 1
  monitoring + volet 2 R&D, validée le 2026-08-16 par le gardien), deux
  incohérences identifiées : (1) `DISCORD_HOME_CHANNEL` pointait vers
  `#analog-wizard` (`1535173127695241248`) au lieu de `#infrastructure`
  (`1536564394690084925`) — notifications de startup/shutdown dans le
  mauvais salon ; (2) aucun cron job créé pour le volet 1 du mandat
  (`hermes --profile studio cron list` → « No scheduled jobs »).
- **Action 1** : correction du `DISCORD_HOME_CHANNEL` dans
  `/root/.hermes/profiles/studio/.env` (`1535173127695241248` →
  `1536564394690084925`). Redémarrage du gateway (`hermes --profile
  studio gateway restart`, PID 2011978). Vérification au log : « Sent
  home-channel startup notification to discord:1536564394690084925 »
  — notification confirmée sur `#infrastructure`.
- **Action 2** : création du cron job `monitoring-infrastructure-quotidien`
  (job ID `b7acb57e3d58`), schedule `0 12 * * *`, deliver
  `discord:1536564394690084925`, workdir `/root/wiki`, toolsets
  `terminal/file/read_file/execute_code`. Prompt : orchestration des
  3 scripts déterministes + empreinte serveur + registre
  Hermes-Terminal, rapport 5 sections conforme au SOUL.md §Volet 1.
  Prochaine exécution : 2026-08-17 à 12h00 UTC.
- **Action 3 (volet 2 R&D — option a validée)** : Sidy a validé
  l'intégration de la détection de nouvelles fiches dans le prompt du
  cron quotidien (option a, plutôt que cron séparé). Création du script
  `atelier/rd/outillage/detecter-nouvelles-fiches-rd.sh` — compare des
  snapshots horodatés de `atelier/rd/` (stockés dans
  `.snapshots-rd/`), détecte fichiers nouveaux et modifiés. Mise à jour
  du prompt du job `b7acb57e3d58` : ajout du volet 2 après le volet 1,
  rapport passe de 5 à 6 sections (§5 R&D conditionnel, §6 Suggestions).
  Si aucune nouvelle fiche → pas de §5. Si fiches détectées → l'agent
  les lit, analyse, rapproche du `registre-problemes.md`, formule des
  propositions (marquées PROPOSITION, jamais décision). Recherche
  internet proactive : signalée dans §6, exécutée sur demande.
- **Leçon** : deux gestes distincts lors de l'extension d'un mandat
  agent — (a) écrire le prompt SOUL.md (fait par le gardien), (b)
  configurer les variables Hermes qui en découlent (HOME_CHANNEL,
  cron jobs, workdir, toolsets) — le (b) avait été omis. Vérifier
  systématiquement qu'un `cron list` confirme la présence effective
  du job après toute proposition acceptée.
- **Fiche** : [[atelier/rd/infrastructure/activation-monitoring-studio-cron-2026-08-17|activation-monitoring-studio-cron-2026-08-17]]

## [2026-08-16] infrastructure | Activation du salon #infrastructure — allowlist studio

- **Symptôme** : le salon Discord `#infrastructure`
  (`1536564394690084925`), créé en anticipation de la phase 3
  (veille infrastructure par le Studio Sound Engineer, pos. 9),
  était muet — l'agent `studio` ne répondait à aucun message
  malgré un service gateway actif et connecté.
- **Cause** : le salon n'avait jamais été ajouté à
  `DISCORD_ALLOWED_CHANNELS` du profil `studio`. Le comportement
  fail-closed de l'allowlist fait que tout message hors liste est
  silencieux (aucun log d'erreur — le silence est le comportement
  attendu).
- **Correction** : ajout de l'ID numérique dans l'allowlist,
  redémarrage du service (`systemctl --user restart
  hermes-gateway-studio.service`). Log confirmé : `Channel
  directory built: 9 target(s)` (était 8). Agent opérationnel
  dans le salon — vérification réelle par Sidy.
- **Leçon** : la création d'un salon Discord et l'autorisation
  d'un agent Hermes à y répondre sont deux gestes distincts — le
  premier est un acte Discord (humain/admin), le second un acte
  de configuration Hermes (`.env` du profil + restart). Pour
  tout futur salon confié à un agent, vérifier
  systématiquement `DISCORD_ALLOWED_CHANNELS` et, si souhaité,
  `DISCORD_FREE_RESPONSE_CHANNELS` (non activé dans cette passe
  — `studio` répond sur @mention uniquement dans
  `#infrastructure`).
- **Fiche R&D** :
  `atelier/rd/infrastructure/activation-salon-infrastructure-studio-2026-08-16.md`
  (diagnostic, correction, état, points ouverts).
- **Configuration Hermes** (`.env`, services systemd) : hors
  dépôt, jamais commitée — le présent commit ne porte que la
  documentation wiki (fiche + annales), vérifiée exempte de
  tout secret avant staging.
- **Vérification** : `verifier-invariants.py --racine /root/wiki`
  — 0 erreur(s), 50 avertissement(s) (baseline stable,
  avertissements pré-existants C4 sur liens `doctrinal` →
  `meta/` dans les annales/index doctrinaux).
- **Commit** : (à venir)

---

## [2026-08-16] correction | Canal Telegram Mehdi — architecture initiale en service

- **Écart initial** : session Hermes terminal a d'abord configuré Telegram sur
  le profil `karubi` (sous root, sans isolation OS). Verdict Sidy : reprendre
  l'architecture R&D initiale (profil dédié, isolation OS).
- **Correction** :
  - Module `hermes-agent[telegram]` installé dans le venv système
  - Token et allowlist retirés de `/root/.hermes/profiles/karubi/.env`
  - Service `hermes-gateway-karubi.service` arrêté et désactivé
  - Service `hermes-gateway-habib-mehdi.service` relancé — tourne sous
    l'utilisateur `mehdi` (uid 1000), isolation OS vérifiée
- **État final** : opérationnel, bot `@HabibKarubi_bot` connecté, Mehdi
  allowlisté (817763036), cwd `/home/mehdi/depot-lecture` (bind mount ro),
  message test envoyé via `sudo -u mehdi hermes --profile habib-mehdi send`
- **Fiche R&D** : `atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16.md`
  mise à jour (§5 : architecture corrigée et en service)
- **Configuration Hermes** (`.env`, `config.yaml`, services systemd) : hors dépôt,
  jamais commitée — le présent commit ne porte que la documentation wiki
  (fiches + annales + registre), vérifiée exempte de tout secret avant staging.
- **Commit** : 954712f

---

## [2026-08-16] archivage | Cordis — paradigme de composabilité spatiotemporelle

- Ingest de `raw/A Programming Paradigm for Spatiotemporal Composability.pdf`
  (Shi, Zhang, Cui — Peking University / DeepSeek-AI, accompagne la sortie du
  DeepSeek Harness).
- Fiche créée : `atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle.md`
  (`outillage`, `exploratoire`, `brouillon`).
- Qualification sashimono (§VII, double contrôle) : homologie de forme
  constatée avec plusieurs articles de la convention (art. 1, 3, 4, 5, 6),
  portance zōsaku, non tranchée.
- Hypothèse plus large de Sidy (filiation orientale/chinoise explicite,
  au-delà de la simple homologie) renvoyée en discernement doctrinal, lien
  signalé sens unique : `doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md`
  (enrichi ce jour, statut `speculatif`, verdict réservé).
- Pistes Hermes (§8 de la fiche) posées comme jalon, aucune décision
  d'implémentation.
- Passage par `_inbox/cordis-composabilite-spatiotemporelle/` avant intégration
  (validation Sidy des deux tours de plan, 2026-08-16).
- SHA : `ade0da6`

## [2026-08-15] archivage | Bilan R&D — pont inter-agents

Fiche `atelier/rd/cahiers/bilan-2026-08-15-pont-agents.md` créée : synthèse de la
période 2026-08-08 → 2026-08-15 destinée à tout agent (Hermes terminal, Claude
Code, ou autre) reprenant le fil des travaux R&D sans avoir participé aux sessions
antérieures. Couvre : ouverture et structure du pôle R&D, outillage déterministe
du dépôt, outillage Karūbī (append-only + admin Agent 10, verdict Sidy 2026-08-15),
spec rôle G0 de brouillon §4, Bureau TUI, infrastructure Hetzner, phase 3 veille,
extension zodiacale, SRS Hermes-native ; chantiers ouverts par priorité (dont le
blocage A — isolation mémoire Hermes par sub-agent : décision propre de Sidy,
assumée le même jour, pas une incohérence à corriger) ; leçons transversales
opérationnelles. Aucun contenu doctrinal. Lien entrant ajouté dans
`atelier/rd/index.md`. Committé dans le même lot que l'outillage de navette
Karūbī (`integrer-navette-karubi.py`, `spec-skill-karubi-actualisation-g0.md`,
note `meta/CLAUDE.md`, entrée `registre-silsila.md`) — verdict Sidy obtenu pour
l'ensemble.
- **Commit** : 2657421

## [2026-08-15] archivage | Intégration registre problèmes + fiche outillage R&D

Deux fichiers du sas `_inbox/` intégrés :

1. **Entrée registre-problemes** (`atelier/rd/cahiers/registre-problemes.md`) :
   ajout de l'entrée `[2026-07-20] Lecture défensive d'un document-persona par un LLM neuf`,
   relatant le cas Karūbī et le signal du classificateur de sécurité sur collage à froid.
   Chaîne d'observation complète → `atelier/rd/outillage/robustesse-documents-persona-llm`.

2. **Nouvelle fiche outillage** (`atelier/rd/outillage/robustesse-documents-persona-llm.md`,
   type `outillage`, statut `exploratoire`) : instrumentation complète du problème
   (forme / contenu, catégorisation du signal, résolution appliquée, pistes à vérifier).
   Étanchéité neutre, liens vers `meta/transmissions/registre-silsila.md` (faits personnels,
   hors circuit).

- **Commit** : c67275b

## [2026-08-15] outillage | Piste — SRS pour l'assimilation du protocole (CLAUDE.md)

Fiche d'instruction ouverte (`atelier/rd/outillage/2026-08-15_piste-srs-assimilation-protocole.md`)
en réponse à un double constat : (1) optimisation infrastructure Hermes —
lacunes observées entre sessions sur des règles protocolales denses (Cmd 9,
Cmd 12, nommage Karūbī — cf. registre 2026-08-13 §2 et §3) ; (2)
assimilation côté utilisateur CLI — le protocole (~10 000 mots) demande une
révision espacée pour passer de la conscience à l'automatisme.

La fiche instruit à frais égaux Mnemosyne (SRS local Maastricht, SM-2+,
équipe de recherche cognitive) et Anki (sync mobile native, écosystème
large), puis propose une troisième voie : intégration Hermes-native. Le
verdict Sidy (2026-08-15) tranche en faveur de cette dernière option :
sous-système de cartes auto-générées depuis CLAUDE.md, vivant dans la
mémoire Hermes (`MEMORY.md` ou extension), sans SRS tiers. §VIII (non
inclus) : format de carte, script d'extraction, mécanisme de révision
(cron Hermes, commande `hermes drill`, ou injection systématique dans le
prompt d'ouverture), algorithme d'espacement — font l'objet d'une fiche
ultérieure).

**Commit** : 5a83157

## [2026-08-15] infrastructure | Bureau TUI — première version

Tableau de bord terminal unique (`atelier/rd/infrastructure/bureau/`, Python +
Textual, esthétique "menu de jeu vidéo" — inspiration de forme relevée dans
`hermeneutique/metal-gear/mother-base` et `idroid`, aucune correspondance
doctrinale invoquée). Six modules indépendants (`modules/base.Module`) : état
de l'Instrument (lecture déterministe d'`instrument-donnees.yaml`), état des
12 agents Hermès (process `pgrep`, missions lues depuis
`meta/projet-unifie/hermes-prompts/`), lecteur textes/pdf/images (façon
Internet Archive, restreint aux quatre circuits publics), lecteur vidéo
(rendu ANSI demi-bloc via ffmpeg, déclenché à la demande uniquement — RAM
serveur limitée), streaming audio (serveur HTTP local, écoute côté client via
tunnel SSH/Tailscale), chat local (v1 humains uniquement, passerelle
Hermès/Discord explicitement différée). 10 tests unitaires verts, `ruff`
propre, fumée headless Textual (pilote) OK sur les 6 modules,
`verifier-invariants.py` : 0 erreur. Testé et validé par Sidy en terminal SSH
réel avant commit.

**Commit** : 5c688b4

## [2026-08-15] mise-a-jour | Brouillons zodiacaux alignés sur la table révisée des 12 fonctions

Suite à la réallocation complète des 12 correspondances signe↔fonction validée
par Sidy le même jour (`doctrinal/discernement/2026-07-05_...`, volet b rouvert),
les brouillons de `atelier/rd/cahiers/brouillons-extension-zodiacale/` sont mis
en cohérence avec la nouvelle table : positions 2 (Taureau→Balance), 6
(Vierge→Scorpion), 7 (Balance→Lion), 9 (Sagittaire→Vierge) renommées via `git mv`
(historique préservé) et réécrites ; positions 5 (Taureau), 8 (Sagittaire), 12
(Poissons) — absentes jusqu'ici — nouvellement rédigées. Positions 1, 3, 4, 10, 11
(signes inchangés) laissées en l'état. Chaque brouillon conserve son
`statut_experience: exploratoire` et sa clause d'étanchéité. Détail complet :
`meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md`
§9.

- **Commit** : 5a3aee3

## [2026-08-13] signalement | Fiches biographiques (2026-06-20) confrontées à AI et IRS

Demande de Sidy : mettre les fiches biographiques en relation avec le corpus, et
en particulier avec *Aperçus sur l'initiation* et *Initiation et Réalisation
spirituelle* (déposée ce jour).

- Créé `atelier/rd/outillage/2026-08-13_fiches-biographiques-confrontation-ai-irs.md`
  (`type: outillage`) — traitement fiche par fiche des douze `discernement/2026-06-20_*`.
- Règle d'appariement posée : un chapitre répond à la **question déclarée ouverte**
  par la fiche, jamais à son récit. Dix chapitres lus intégralement avant citation :
  AI V (`30`), AI VII (`32`), AI VIII (`33`), IRS V (`555`), IRS VI (`556`),
  IRS XVI (`566`), IRS XXI (`571`), IRS XXII (`572`), IRS XXIV (`574`),
  IRS XXVII (`577`).
- Question centrale de neuf fiches (« qui est habilité à reconnaître un *Fard* ? »)
  sourcée : AI V (rattachement « idéal » vain ; « juge et partie dans sa propre
  cause »), AI VIII (la chaîne), IRS V (virtuel/effectif), avec le contrepoint
  IRS XXIV (formes normales sans *Guru* individuel).
- `mythe-personnel-unifie` : AI VII, qui admet le cas *ativarna* tout en posant
  son critère — appariement bilatéral, non restrictif.
- `matrices-artificielles-barzakh` : IRS VI, où Guénon récuse le terme
  « égrégore » lui-même comme non traditionnel.
- `synthese-danger-dissolution-identitaire` : IRS XXVII, qui distingue trois cas
  (quiétistes / « fous en Christ » / *majdhûb*) — troisième catégorie doctrinale
  neuve pour le dépôt, sans critère de reconnaissance externe et sans application
  à un cas particulier.
- `origine-jumeau-spirituel` : IRS XXII, lu et instruit en complément le même jour
  (§ 5.3) — catégorie doctrinale de l'antériorité hors du temps humain
  (« réminiscence platonicienne »), assortie de l'avertissement de Guénon sur les
  « lueurs » pré-initiatiques, « d'ordre probablement plus psychique que
  spirituel ». Appariement bilatéral.
- Quatre fiches restent sans source guénonienne, signalées comme telles.
- Aucun `status`/`Statut` modifié. Création des fiches `doctrinal/sources/` et
  ajout des wikilinks : **proposés, non exécutés** — en attente d'accord.
- Signalement `raw/` : IRS ch. XXX (id 580) toujours absent — le fichier déposé
  est la page de sommaire de l'œuvre, non le chapitre.
- **Suite donnée le même jour** (accord de Sidy, « oui, crée les fiches ») : le § 7
  passe de *proposé* à **exécuté** — sept fiches `doctrinal/sources/` créées et
  huit rattachements posés dans le champ `sources:` des fiches biographiques.
  Opération consignée côté doctrinal (`doctrinal/annales.md`, entrée du même jour).
- Le présent document amendé en conséquence : § 5.2 corrigé (IRS XXVII ne distingue
  pas trois cas mais une **série** — au moins six positions sous une même apparence,
  dont les faux *majâdhîb* de deux sortes contraires et les jongleurs-initiés) ;
  § 7 marqué exécuté.
- **Double contrôle (§ VII) consigné après coup** au § 7 bis, avec mention de son
  retard : joint qualifié ***zōsaku* × *kari-kumi*** (une extrémité contingente,
  montage à blanc) ; Gizeh : **confronté, aucun ancrage**.
- **IRS ch. XXX (id 580) déposé par Sidy le même jour** — signalement de complétude
  levé, corpus IRS complet (34 fichiers, aucun identifiant manquant sur 551–583).
  Chapitre lu et instruit au § 6 bis ; huitième fiche source créée et rattachée à
  `matrices-artificielles-barzakh` et `visions-centre-nocturne` (consigné côté
  doctrinal). Double contrôle posé cette fois **au moment de la production**
  (§ 7 ter) : *zōsaku* × *kari-kumi*, nature **homologie** ; Gizeh due et instruite
  (matière axiale) — **aucun ancrage**, conflation polaire/solaire écartée.
- Commit: `0c3a7ba` ; complément IRS XXII : `96ab694` ; exécution du § 7 et
  correction du § 5.2 : `4795d2d` ; IRS ch. XXX : `e3a9ce6`.


## [2026-08-13] signalement | Tour d'horizon : déblocages ouverts par le corpus Guénon déposé

Dépôt de *La Grande Triade* dans `raw/` par Sidy. Confrontation de fond (et non
plus de forme) entre le corpus désormais intégral et les marqueurs d'inachèvement
des fiches `doctrinal/discernement/`.

- Créé `atelier/rd/outillage/2026-08-13_tour-horizon-corpus-guenon-deblocages.md`
  (`type: outillage`) — distinct du rapport de fidélité de citation du même jour.
- Quatre déblocages signalés : GT ch. XVII (`Chapitre=714`) sur la restriction de
  degré de `adam-qadmon-insan-kamil-wang-vaishvanara` ; GT ch. XXVI n. 11
  (`Chapitre=722`) sur le chantier de la Balance de `septenaire-transversal` ;
  GT ch. XV (`Chapitre=712`) candidat au sourçage d'un `to-source` sashimono ;
  lisibilité partielle de `sept-tours-sitra-ahra` (blocage kabbalistique intact).
- Candidat Cmd 3 signalé : équivalence *Es-Sakînah* / *Shekinah* posée par Guénon
  lui-même (GT ch. XXVI), portée par aucune fiche `discernement/`.
- Carte des identifiants `Chapitre=NNN` établie pour AI, IRS, GT, RM, SC, RQST.
- Signalement de complétude : *Initiation et Réalisation Spirituelle* id 580
  (ch. XXX) manquant dans `raw/`.
- Précision sur l'Instrument : yaml = 36 nœuds `tasawwuf` + 7 `universel`
  uniquement ; GT est matériau de fondation pour `universel/`, non ouverture
  d'un espace extrême-oriental.
- Cmd 12 respecté : aucun `status`/`Statut` de fiche `discernement/` modifié.
- Volet B (hygiène `raw/`) relevé, non instruit — Cmd 10.
- Commit: `37bf44d`.

---

## [2026-08-13] signalement | Confrontation de 5 fiches discernement/ au corpus Guénon (raw/)

- **Contexte** : contrainte production/intégration temporairement levée
  (cf. document « wiki-contrainte-integration-levee », mémoire) ; corpus Guénon complété en
  `raw/` (dépôt du chapitre RQST manquant, id 746, par Sidy).
- **Opération** : vérification mécanique de complétude des 7 œuvres Guénon
  déposées (0 trou après dépôt) via les champs `Chapitre=`/`sigle=` du
  frontmatter `source:`, puis confrontation verbatim de 5 fiches
  `doctrinal/discernement/` (celles citant, via wikilink, une des 12 fiches
  `doctrinal/sources/` confrontables) contre le texte brut correspondant.
- **Résultat** : 4 fiches confirmées exactes (citations et attributions de
  chapitre fidèles). 1 fiche —
  [[doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil]]
  — porte deux formulations entre guillemets attribuées à Guénon qui sont en
  réalité des paraphrases/synthèses, non du texte verbatim. Signalement remis
  à Sidy, aucun `Statut` modifié (Cmd 12).
- **Livrable** :
  [[atelier/rd/outillage/2026-08-13_confrontation-discernement-corpus-guenon]].
- **Non traité** : Volet B (doublons d'id AI 28/70, RQST 729/752, EME 881 ;
  fichiers possiblement mal classés ; `organize_guenon.sh`) — reporté, non
  commencé.
- Commit : `023a31c`.

---

## [2026-08-13] vigilance | Rapport R&D — défauts observés, intégration retour Karūbī Mehdi (Habib)

- Sur demande explicite de Sidy, consignation dans
  `atelier/rd/cahiers/registre-problemes.md` de trois observations tirées de
  l'intégration du retour `_inbox/karubi-mehdi-navette-20260812.md` : (1)
  écart d'append silencieux — une entrée §8 de la navette absente du fichier
  canonique, sceau intact n'ayant rien signalé (piste d'outillage : mode
  `diff` pour `generer-karubi.py`, ouvert) ; (2) confusion nom du Karūbī /
  nom du destinataire, déjà résolue par l'ajout d'une table à `meta/CLAUDE.md`
  (commit `6b4871e`) ; (3) friction récurrente du Cmd 9 (SHA après commit
  imposant un second commit de forme), confirmée comme comportement normal du
  protocole tel qu'écrit, non un défaut isolé (reporté).
- **Commit** : 76d08b0

---

## [2026-08-13] vigilance | Retour d'expérience R&D — première intégration sous CLAUDE.md éclaté

- Sur demande explicite de Sidy (« toute information instructive au R&D pour
  monitoring »), consignation dans `atelier/rd/cahiers/registre-problemes.md`
  des observations tirées de la première intégration `_inbox/` réalisée sous
  la convention CLAUDE.md éclatée (racine + cinq `CLAUDE.md` locaux,
  2026-08-12) : chargement confirmé fonctionnel des protocoles locaux,
  traitement du reliquat `Protocole.md` (doublon non nettoyé du commit
  d42c954, supprimé le 2026-08-12/13 — voir `meta/meta-annales.md`
  [2026-08-12]), confirmation de l'intégrité de l'archive canonique, et
  validation du principe d'auto-signalement du sas via la fiche
  `hermeneutique/metal-gear/idroid.md`.
- Aucune écriture de contenu hors du cahier R&D ; simple journalisation
  transversale de cette entrée pour Cmd 9 (opération conduite depuis
  l'atelier, sur un objet propre au pôle `rd/`).
- `verifier-invariants.py --racine /root/wiki` : `0 erreur(s), 45
  avertissement(s)` (inchangé, pré-existants, phase de calibrage).
- **Commit** : bddece0

## [2026-08-12] archivage | Audit de santé Claude Code (`/doctor`) versé dans rd/infrastructure

- **Fiche créée** : `atelier/rd/infrastructure/claude-code-health-check-2026-08-11.md`
  — `type: infrastructure`, `statut_experience: exploratoire`. Rapport brut
  (anglais d'origine) produit par Sidy le 2026-08-11 via `/doctor`,
  conservé tel quel — diagnostic mécanique de l'installation, non un
  jugement sur le contenu doctrinal.
- **Non exécuté** : les recommandations du rapport (notamment « trimmer
  `CLAUDE.md` », devenue sans objet après l'éclatement en protocoles
  locaux du 2026-08-12) restent hors périmètre, aucun plan validé ne les
  couvre (Cmd 6).
- **Commit** : 036635b

## [2026-08-12] archivage | Proposition phase 3 (agent de veille infrastructure) archivée dans rd/cahiers

- **Fiche créée** : `atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  — `type: meta` (précédent : `registre-problemes.md`, même dossier), statut
  `brouillon` conservé tel quel (contenu non ré-écrit, seule une section
  « Intégration (2026-08-12) » ajoutée en queue de fiche).
- **Provenance** : déposée en `_inbox/` le 2026-08-11 ; le document
  s'auto-déclarait sans écriture hors `_inbox/` (« cette note ne code encore
  aucun automatisme »). Archivage décidé le 2026-08-12 sur consigne explicite
  de Sidy (« intègre le reste »), question de placement posée et tranchée :
  destination `atelier/rd/index.md` telle qu'indiquée par le `cible:` du
  document lui-même.
- **Portée de l'archivage** : documente des décisions de principe déjà
  tranchées par Sidy le 2026-08-11 (agent désigné : Studio Sound Engineer,
  poste 9 ; canal `#infrastructure` ; cron quotidien midi ; rapport en 5
  sections). **N'exécute aucun automatisme** — le tableau récapitulatif de la
  fiche (extension du prompt d'agent, accès FS/exécution, mécanisme
  technique, récurrence de l'empreinte serveur) reste explicitement « à
  instruire »/« à trancher », conformément au Cmd 6.
- **Mise à jour de renvoi** : `atelier/rd/index.md`, §« État de la phase 1
  partielle » → « Non inclus », pointeur ajouté vers la fiche archivée.
- `python3 verifier-invariants.py --racine /root/wiki` : 1 erreur bloquante
  pré-existante (`Protocole.md`, sans rapport avec cette intégration), 44
  avertissements pré-existants — aucun nouveau signal introduit.
- **Commit** : 3e846e9

## [2026-08-11] infrastructure | Cartographie architecture infrastructure serveur/Hermes/omniroute

- **Opération** : création de document cartographique global unifiant mesures brutes, topologie 
  réseau, description des services (12 profils Hermes + omniroute), empreinte mémoire consolidée, 
  et identification des points de défaillance critiques pour diagnostic et audit. Document 
  d'architecture destiné à l'onboarding et à la base de comparaison historique.
- **Fichiers créés** :
  - `atelier/rd/infrastructure/infrastructure-architecture-globale-2026-08-11.md` : cartographie 
    complète (topologie, services, mémoire, uptime, circuits réseau, SPoF, points ouverts)
- **Fichiers modifiés** :
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la cartographie 
    comme résolution du point ouvert « infrastructure documentation globale »
- **Mesures et observations** :
  - Topologie : GitHub (SSH origin) ↔ Hetzner (2 vCPU, 3.7 GB RAM, 38 GB disk 51% libre) 
    ↔ iPad (Obsidian via Working Copy)
  - Services : 12 profils Hermes (639.5 MB total), omniroute 1040 MB (28% RAM, critique), 
    hermes-webui 9.8 MB
  - Uptime : 78j 18h ; load avg < 0.1
  - Swap utilisé : 1 GB / 2 GB (signal d'alerte mémoire au moment de la mesure)
  - SPoF identifiés : clé API Anthropic (11 agents paralysés), omniroute (fonction inconnue), 
    Hetzner SSH key (écriture dépôt), uptime Hetzner (tous les services)
- **Points ouverts à instruire** :
  1. omniroute : fonction exacte, dépendances, optimisation RAM ?
  2. Clé API Anthropic : impasse à Sidy (budget), en attente résolution
  3. Qwen sur gardien : clause « No API automation » — risque révocation à respecter
  4. Hermes accès meta/ : cloisonnement technique statu quo (retour d'expérience en cours)
  5. Historique de charge : aucune série temporelle (monitoring à installer)
- **Vérification** :
  - `verifier-invariants.py --racine /root/wiki` : 5 erreurs, 45 avertissements (baseline 
    stable +2 pour nouvelle fiche avec liens meta)
  - Aucune anomalie de structure ou de liens dans la cartographie créée
- **État** : cartographie complète, observation brute sans recommandations d'optimisation 
  (distinction §VIII.2 maintenue) ; base solide pour diagnostics et onboarding futurs
- **Commit** : (à venir)

---

## [2026-08-11] outillage | Implémentation des 4 pistes outillage instruites (pistes A, B, C, D) — documentation fiches et verification

- **Opération** : finalisation de la documentation et vérification des quatre pistes 
  d'outillage du pôle R&D (session 2026-08-11). Pistes A (C4 verifier-invariants) et C 
  (detecter-non-tracke.py) déjà implémentées en code et en spec, pistes B et D manquaient 
  de fiches dédiées.
- **Fichiers créés** :
  - `atelier/rd/outillage/spec-generer-cartographie-tolerant.md` : documentation de la 
    sévérité à deux niveaux du script v1.1 (BLOQUANT gouvernance, AVERTISSEMENT chantier) 
    — distinct d'un « mode tolérant », c'est une hiérarchisation des anomalies
  - `atelier/rd/infrastructure/infrastructure-ssh-statu-quo.md` : documentation du verdict 
    (statu quo SSH, pas de migration HTTPS+PAT), rationale (gestion de secret + coût 
    détour Working Copy) et clause de réouverture
- **Fichiers modifiés** :
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la complétude 
    de l'implémentation des quatre pistes (A, B, C, D tous en statut resolu) et les 
    résultats de vérification (baseline stable)
- **Vérification** : 
  - `verifier-invariants.py --racine /root/wiki` : 5 erreur(s), 43 avertissement(s) — 
    baseline stable (+2 warnings attendus pour les 2 nouvelles fiches avec liens meta)
  - `generer-cartographie.py --depot /root/wiki --verifier` : 2 anomalies BLOQUANT 
    (frontmatter absent) — inchangées
  - `detecter-non-tracke.py --racine /root/wiki` : identifie 2 fichiers non-trackés 
    (les 2 nouvelles fiches), aucune anomalie
- **État** : pistes B et D documentées. Piste A (C4 verifier-invariants) reste sans fiche 
  dédiée à ce stade (implémentation active en code, arbitrage verbal de Sidy en session 
  jugé suffisant pour cette passe). Piste C (spec existante et script testé) complète.
- **Commit** : 3650ed8

---

## [2026-08-11] agents-hermes | Extension du prompt agent 09 (Studio Sound Engineer, pos. 9 Sagittaire) — zodiacal + governance

- **Opération** : intégration au prompt en production des sections zodiacales 
  (principle + harmonisation thème natal) et de la clause de gouvernance Discord-validation 
  requise par le chantier phase 3. Trois sections insérées entre « ## Archetype served » 
  et « ## Scope » : (1) Zodiac principle (Sagittaire feu mutable jupitérien pédagogique), 
  (2) Your sign in Sidy's natal chart (contexte natal : Ascendant 2°51 Saturn conjonction 
  4°32, pédagogie disciplinée de Saturn), (3) Governance: Discord-Validation (stricte par 
  défaut, auto-accept ad hoc, traçabilité Discord, jamais d'actes silencieux).
- **Fichiers modifiés** : 
  - `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md` : trois sections 
    insérées (Zodiac principle copié du brouillon `/root/brouillons-prompts-zodiaque/09-studio-sagittarius.md` 
    tel quel, Your sign du brouillon tel quel, Governance rédigé pour l'occasion)
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant le symptôme 
    (brouillon en attente), le diagnostic (dépendance phase 3), la résolution (trois 
    sections intégrées), la compréhension (extension ≠ réforme structurelle)
- **Validation** : `verifier-invariants.py --racine /root/wiki` : baseline inchangée
  (5 erreur(s) pré-existantes, 40 avertissement(s))
- **État** : prompt agent 09 étendu, reste en régime exploratoire (statut_experience non 
  formalisé en frontmatter, déjà documenté par le registre) ; accès FS/gouvernance résolus 
  séparément ; déploiement effectif de la veille infrastructure reste un acte distinct (Cmd 6).
- **Commit** : 29cb5cc

---

## [2026-08-11] phase-3 | Explicitation du flux alchimique Discernement → R&D (théorie des trois territoires adoptée)

- **Opération** : enrichissement conceptuel de la proposition phase 3 pour nommer 
  explicitement sa position dans le flux adopté le même jour (trois territoires de 
  l'inachevé). La note documente une transition de la spéculation zodiacale 
  (Discernement) vers la mise en œuvre concrète (R&D exploratoire) ; cette transition 
  était implicite et doit être nommée par référence à la théorie.
- **Fichiers modifiés** : 
  - `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` : blockquote 
    architecturale ajoutée après l'en-tête (explicitant la transition Discernement → R&D 
    et la finalité non-achevée jusqu'à verdict de Sidy) ; §III.1 enrichi d'une 
    sous-section « Registre alchimique » décrivant l'incarnation du passage du Plan 
    théurgique à l'Acte
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la 
    transition alchimique, sa non-transparence antérieure, et son ancrage à la théorie 
    adoptée
- **Validation** : `verifier-invariants.py --racine /root/wiki` : baseline inchangée
  (5 erreur(s) pré-existantes, 40 avertissement(s))
- **État** : note phase 3 reste `brouillon`, enrichie de la dimension architecturale. 
  Aucun changement aux chantiers énumérés (accès FS, mécanisme technique, extension 
  du prompt) — leurs exécutions restent des actes séparés. Transition conceptuelle 
  maintenant explicite.
- **Commit** : 29cb5cc

---

## [2026-08-11] phase-3 | Réouverture §III.1 : réattribution veille infrastructure au Studio Sound Engineer (position 9)

- **Opération** : documentation de la réouverture du §III.1 de la proposition phase 3. 
  L'ancien verdict (poste INTÉGRATION) tranché en séance a été rouvert le même jour 
  (2026-08-11) ; réattribution à l'agent Studio Sound Engineer (position 9 Sagittaire).
- **Fichiers modifiés** : 
  - `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` : bloc de tête 
    mis à jour, §III.1 documentant l'ancien et nouveau verdict (discipline sashimono), 
    §IV confirmant que la réouverture ne rouvre PAS le §III.3, §VI récapitulatif des 
    chantiers ouverts après la réouverture
  - `atelier/rd/cahiers/registre-problemes.md` : nouvelle entrée documentant la réouverture, 
    le diagnostic (cartographie des 12 rôles), la résolution (accès FS accordé), la 
    compréhension tirée (traçabilité des décisions qui se chevauchent)
- **Validation** : `verifier-invariants.py --racine /root/wiki` : baseline inchangée
  (5 erreur(s) pré-existantes, 40 avertissement(s))
- **État** : `_inbox/` reste à traiter selon flux normal (INTÉGRATION, Cmd 8). 
  Registre-problemes consigné et tracé. Phase 3 ouverte en principe, chantiers 
  spécifiques (accès FS, mécanisme technique, récurrence empreinte) restent à 
  instruire avant écriture effective (Cmd 6).

---

## [2026-08-11] structure | Hypothèse méthodologique : Sandbox comme dépendance structurelle du R&D

- **Contexte** : réflexion sur la relation entre Discernement (spéculation personnelle),
  R&D (exploration exploratoire), et le Sandbox (espace de travail). Fiche de
  discernement rédigée (voir annales doctrinal du même jour).
- **Proposition** : expliciter que le Sandbox (`atelier/rd/cahiers/`) est la **poche
  de travail du R&D**, c'est-à-dire l'espace de non-finalité programmée — tout
  chantier en phase `exploratoire` y vit par défaut, demeure réversible jusqu'à
  validation explicite (Cmd 6, Cmd 13), et sort du Sandbox soit vers doctrine
  adoptée, soit vers archivage.
- **Impact sur rd/** : aucun changement immédiat au structure ni aux scripts. Change
  seulement la **clarté architecturale** et le régime de navigation entre chantiers.
- **Statut** : en attente de verdict (Cmd 12) sur l'opportunité de formaliser cette
  explicitation en CLAUDE.md.
- **Aucune écriture au registre rd/** : reste une hypothèse documentée ailleurs
  (discernement), non encore actionnable.

---

## [2026-08-11] archivage | Chantier 12 agents (zodiacal) — brouillons d'extension principielle versionnés en atelier/rd/

- **Opération** : déplacement de `/root/brouillons-prompts-zodiaque/` vers
  `atelier/rd/cahiers/brouillons-extension-zodiacale/` — 9 brouillons (pos.
  1, 2, 3, 4, 6, 7, 9, 10, 11) + README, avec frontmatter + clause
  d'étanchéité explicite (CLAUDE.md §VI). Positions 5, 8, 12 marquées en
  attente. Reste hors écriture : application en production, reste
  exploratoire (statut_experience). Détail au registre rd/:
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** : 9 fichiers créés/modifiés en
  `atelier/rd/cahiers/brouillons-extension-zodiacale/` (all with frontmatter +
  clause), README inclus.
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : c156226

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — accès FS accordé, gouvernance Discord-validation tranché, mécanisme de post tranché

- **Opération** : suite de la réouverture du §III.1 : Sidy accorde l'accès FS
  du Studio Sound Engineer aux scripts déterministes, définit la gouvernance
  (strict par défaut + auto-accept ad hoc), et fixe le mécanisme de post
  (l'agent compose et poste le rapport lui-même via Discord, plus de webhook
  tiers). Format des 5 sections conservé. Note mise à jour, blockquote de
  tête et §III.1 complétés, §VI mécanisme réécrit (pas de webhook, pas de
  crontab — c'est l'agent). Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md`
  (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : f94d0e1

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — §III.1 rouvert, veille réattribuée au Studio Sound Engineer

- **Opération** : Sidy rouvre le §III.1 (déjà tranché : routine poste
  INTÉGRATION) en le reliant explicitement au chantier de l'extension de
  rôle des 12 agents Hermes sur calibrage zodiacal (fiches
  `meta/projet-unifie/16-...`, `17-...`) et attribue la veille
  infrastructure à la **position 9 (Sagittaire), Studio Sound Engineer** —
  seul rôle des 12 de registre technique/matériel, après cartographie
  complète des 12 positions confirmant l'absence d'autre candidat naturel.
  Ancien verdict conservé barré (sashimono, réversibilité), cascade
  documentée sur le mécanisme du §VI (rouvert à son tour), §III.3 et §IV
  inchangés. Chantier FS/accès Hermes nommé, non résolu, hors périmètre.
  Détail au registre : [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (blockquote de tête, §III.1, §IV, §VI, toujours `brouillon`),
  `atelier/rd/cahiers/registre-problemes.md` (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : bd64d60

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — format et mécanisme proposés par délégation

- **Opération** : Sidy délègue explicitement le format précis du rapport et
  le mécanisme technique de post (« je me fie à ta suggestion le temps d'en
  faire l'expérience directe et j'optimiserai au besoin »). Proposition
  consignée au §VI de la note : format en 5 sections, mécanisme = webhook
  Discord simple (canal `#infrastructure`) + script Python dédié
  (`atelier/rd/outillage/`, à écrire), régime `statut_experience:
  exploratoire` (§V.a) invoqué explicitement. Écriture effective toujours
  hors périmètre (Cmd 6). Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (blockquote de tête + §VI, toujours `brouillon`),
  `atelier/rd/cahiers/registre-problemes.md` (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée) ; `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes pré-existantes (hors périmètre),
  inchangées.
- **Commit** : c92401e

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — heure et nature du rapport tranchées

- **Opération** : Sidy fixe l'heure du cron (12:00, midi) et la nature du
  rapport (suggestion, révision, développement — au-delà du simple constat
  brut). Tension identifiée et refermée dans le même énoncé : le caractère
  suggestif du rapport ne crée aucune dérogation à la porte humaine (§III.3,
  Cmd 13) — toute suggestion est validée par Sidy avant journalisation.
  Détail au registre : [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` (§VI,
  toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée).
- **Commit** : beee81f

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — fréquence quotidienne tranchée

- **Opération** : Sidy confirme la fréquence du cron proposée au §VI —
  **quotidienne**, cohérente avec le « Rapport du matin » déjà envisagé côté
  Hermes/gardien. Note mise à jour. Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` (§VI,
  toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée).
- **Commit** : c5acb2c

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — canal Discord `#infrastructure` créé

- **Opération** : Sidy communique en session le nom et l'identifiant du canal
  Discord dédié tranché au §V (`#infrastructure`). Note mise à jour (§VI) :
  nom consigné, identifiant numérique volontairement **non** consigné dans le
  dépôt (même régime que les secrets de configuration — cf.
  `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`). Détail
  au registre : [[atelier/rd/cahiers/registre-problemes]].
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md` (§VI,
  toujours `brouillon`), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée). Vérifié qu'aucun identifiant
  numérique Discord n'a été écrit dans le dépôt (`grep` négatif sur la
  totalité de `/root/wiki`).
- **Commit** : 59e0e78

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — désignation effective (§V) instruite

- **Opération** : instruction des deux volets laissés ouverts par le §III
  (déclencheur de la routine, canal Discord de signalement). Recherche menée
  sur l'architecture Discord Hermes (`meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`)
  et le prompt réel du profil `gardien`
  (`meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`), révélant que
  ce dernier a un mandat doctrinal/éthique et non technique malgré son
  étiquette « Vigie transversale ». Détail complet au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Verdicts Sidy (2026-08-11)** : (1) déclencheur = **planifié par cron**
  (nouvelle surface assumée, refermée par construction puisque la routine ne
  fait que signaler sur Discord, jamais écrire au dépôt) ; (2) canal =
  **nouveau canal dédié**, pas de réutilisation de `#gardien`.
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (nouveau §V « Désignation effective » et §VI « reste à faire », toujours
  `brouillon` — nom du canal, fréquence exacte, contenu du rapport et
  mécanisme de post restent à instruire, Cmd 6),
  `atelier/rd/cahiers/registre-problemes.md` (nouvelle entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée, après correction d'un lien mal
  formé — ZWJ intempestif dans deux chemins `meta/projet-unifie/`).
  `Graphe/generer-cartographie.py --verifier` : 2 anomalies bloquantes
  (les 2 `frontmatter` pré-existantes, hors périmètre — inchangé).
- **Commit** : 34bc9a2

---

## [2026-08-11] proposition/arbitrage | Phase 3 (agent de veille infrastructure) — §III tranché

- **Opération** : discussion des trois questions du §III de
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (qui, quoi, comment consigner). Détail complet, y compris le retour en
  arrière sur la question 3, au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Verdicts Sidy (2026-08-11)** : (1) routine côté poste INTÉGRATION, pas
  d'agent Hermes dédié ; (2) périmètre = 3 scripts déterministes + mesure
  d'empreinte serveur (récurrence de la mesure laissée en chantier séparé) ;
  (3) signalement via un canal Discord existant, aucune écriture
  automatique dans `registre-problemes.md`.
- **Fichiers modifiés** :
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`
  (§III et §V mis à jour, toujours `brouillon` — désignation effective non
  exécutée, Cmd 6), `atelier/rd/cahiers/registre-problemes.md` (nouvelle
  entrée).
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée).
- **Commit** : 380595a

---

## [2026-08-11] outillage/proposition | Session R&D (suite) — détecteur non-trackés, statu quo SSH, proposition phase 3

- **Opération** : suite de la session R&D du jour (voir entrée précédente pour
  la première passe C4/cartographie/fourche Instrument). Trois volets restants
  du plan validé, traités ici.
- **Piste outillage C** : création de
  `atelier/rd/outillage/detecter-non-tracke.py` (+ fiche
  [[atelier/rd/outillage/spec-detecter-non-tracke]]) — constat déterministe des
  fichiers non trackés par git, classé par circuit. Lié depuis
  [[atelier/rd/index]]. Détail au registre :
  [[atelier/rd/cahiers/registre-problemes]].
- **Piste outillage D** : décision statu quo SSH (question posée le
  2026-08-09) consignée — verdict Sidy, aucune migration HTTPS+PAT du remote
  `origin`. `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`
  §5 réécrite. Détail au registre.
- **Phase 3 (agent de veille infrastructure)** : note d'instruction déposée en
  sas — `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`,
  statut `brouillon`, non visée. Ne désigne aucun agent ; pose trois questions
  (qui, quoi, quand un signal devient une entrée du registre) et un risque
  (surface d'écriture si confiée à un agent Hermes) pour verdict de Sidy.
  Aucune écriture hors `_inbox/` pour ce volet (Cmd 6).
- **Fichiers modifiés** : `atelier/rd/index.md`,
  `atelier/rd/cahiers/registre-problemes.md` (2 nouvelles entrées),
  `atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md`.
- **Fichiers créés** : `atelier/rd/outillage/detecter-non-tracke.py`,
  `atelier/rd/outillage/spec-detecter-non-tracke.md`,
  `_inbox/proposition-phase3-agent-veille-infrastructure-2026-08-11.md`.
- **Validation** : `verifier-invariants.py --racine /root/wiki` : `0 erreur(s),
  40 avertissement(s)` (baseline inchangée). `Graphe/generer-cartographie.py
  --verifier` : 2 anomalies bloquantes (les 2 `frontmatter` pré-existantes,
  hors périmètre — inchangé).
- **Commit** : 37e6023

---

## [2026-08-11] outillage/correction | Session R&D — C4 (verifier-invariants.py), cartographie serveur, fourche Instrument v0_3/v0.3

- **Opération** : session R&D instruite sur les 3 priorités validées (outillage,
  cartographie infra, phase 3) — voir [[atelier/rd/index]] et
  [[atelier/rd/cahiers/registre-problemes]] pour le détail des entrées.
- **`verifier-invariants.py`** : ajout du contrôle C4 (non bloquant) — signale
  un `annales.md`/`index.md` de circuit neutre pointant vers `meta/`, angle mort
  de l'exemption C3 consigné au registre le 2026-08-09. Non bloquant, cohérent
  avec la phase de calibrage en cours (CLAUDE.md, amendement 2026-07-27).
- **Créé** : `atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11.md` —
  relevé factuel matériel + empreinte mémoire (12 profils Hermes, `omniroute`),
  sans interprétation ni recommandation. Lié depuis [[atelier/rd/index]].
- **Piste outillage « générateur tolérant »** : constat que
  `Graphe/generer-cartographie.py` est déjà en v1.1 (2026-07-22, antérieure au
  diagnostic du registre) avec deux niveaux de sévérité — aucun correctif
  nécessaire. En instruisant les 4 anomalies d'étanchéité résiduelles, découverte
  d'une fourche non documentée :
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
  (tiret bas) et `...v0.3.md` (point) coexistaient comme deux fiches
  indépendantes depuis la migration `projets/ → rd/` du 2026-08-08 (les deux
  fourches existaient déjà séparément côté `projets/`). Comparaison confirmant
  `v0.3` (point) à jour et strict superset de `v0_3` (tiret bas, figée au
  2026-07-01) : `v0_3.md` repassée `deprecated` (Cmd 10, fusion sans perte) ;
  les 4 liens `doctrinal/sources/guenon-*` (sens interdit §VI vers `v0_3`)
  retirés côté `doctrinal/` et reportés en sens licite dans `v0.3.md` ;
  `atelier/index.md` repointé.
- **Fichiers modifiés** : `verifier-invariants.py`, `atelier/index.md`,
  `atelier/rd/index.md`, `atelier/rd/cahiers/registre-problemes.md` (2 entrées
  mises à jour en place + 1 nouvelle entrée `resolu`),
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`,
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`,
  4 fiches `doctrinal/sources/guenon-*`.
- **Validation** : `Graphe/generer-cartographie.py --verifier` : 6 → 2 anomalies
  bloquantes (restent 2 `frontmatter` pré-existantes, hors périmètre — contenu
  doctrinal, cf. registre). `verifier-invariants.py --racine /root/wiki` :
  `0 erreur(s), 40 avertissement(s)` (avertissements C4 attendus).
- **Commit** : 48cfaa6
- **Reste de la session validée** : piste outillage C (détection de fichiers non
  trackés), consignation du statu quo SSH
  (`atelier/rd/infrastructure/synchro-obsidian-working-copy-github.md` §5),
  ouverture phase 3 (agent de veille infrastructure) — à traiter à la suite.

---

## [2026-08-10] outillage | Registre des problèmes R&D — near-miss étanchéité + récidive du piège de chiffre

- Consignation R&D (demande explicite de Sidy : « instruit le R&D s'il a
  quoi que ce soit de pertinent ») à la suite de la réparation des liens à
  référent vide du bloc `discernement/2026-06-20_*` (voir
  `doctrinal/annales.md` et `meta/meta-annales.md`, même jour) : une
  tentative de lien `doctrinal/ -> meta/` a été insérée puis interceptée et
  annulée **avant tout commit** (aucune trace dans l'historique git), et le
  chiffre de consigne (« 4 liens ») s'est révélé erroné à la revérification
  directe (5 réels) — troisième occurrence du même motif déjà consigné à
  deux reprises le 2026-08-09 dans ce registre. Entrée complète :
  [[atelier/rd/cahiers/registre-problemes]].
- **Commit** : 8e7dc07 (annales substantives de l'opération elle-même) — la
  présente entrée journalise séparément la mise à jour du cahier R&D.

---

## [2026-08-10] outillage | Méthode de traitement d'un lot mono-séance `discernement/` (qualification sashimono)

- Consignation R&D (demande explicite de Sidy : « rapporte tout ce que tu
  considères instructif au R&D ») du traitement du bloc
  `doctrinal/discernement/2026-06-20_*` (11 fiches) —
  [[atelier/rd/outillage/2026-08-10_methode-traitement-lot-discernement-sashimono]].
  Aucun contenu doctrinal reproduit ; méthode d'ingénierie uniquement
  (reconnaissance intégrale avant plan, distinguo ouverte/close/hors-catégorie,
  vérification mécanique indépendante de l'outil d'édition, séquence en deux
  commits substantif→annales). Complète
  [[atelier/rd/outillage/2026-08-10_methode-croisement-discernement]] pour le
  cas d'un lot mono-séance, hors périmètre de la méthode de croisement
  général.

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
