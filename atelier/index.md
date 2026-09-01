---
title: "Atelier — Ressources & Études de Cas"
type: index
tags: [atelier, ressources, index, instrument]
created: 2026-07-07
updated: 2026-09-01
---

# Atelier — Index

Ressources opératoires, matériaux de travail, études de cas et documentation pratique.

**Deux régimes** (depuis le verdict du 2026-08-08) :
- **référence** — `materiel/`, `entretiens/` : ce qu'on consulte ;
- **recherche** — `rd/` et `etudes-de-cas/` : ce qu'on instruit.

> **Où regarder en premier si vous reprenez le fil.**
> [[atelier/rd/registre-chantiers]] — la carte vivante de **tous** les chantiers ouverts
> du dépôt (Instrument, infrastructure et agents, outillage, bibliothèque, études de cas,
> process, doctrinal), ouverte le 2026-09-01 sur demande de Sidy. Elle recense et pointe,
> elle n'absorbe rien : chaque chantier reste instruit dans sa fiche et dans son circuit.
> Les fiches de pistes du 2026-08-20 et le bilan-pont du 2026-08-15 restent au dépôt
> comme **jalons datés** — ils ne décrivent que leur jour.

---

## R&D — Recherche & Développement (`rd/`)

Pôle ouvert le 2026-08-08 (verdict Sidy : Option C, phase 1 partielle). Consigne
systématiquement tout ce qui relève de l'ingénierie — technique, musicale,
matérielle, logicielle, outillage, infrastructure — avec pour but l'entretien, le
développement qualitatif, l'optimisation à mesure de l'infrastructure globale
hardware/software, et l'émancipation progressive de tout intermédiaire de service
tiers. Charte et arborescence : [[atelier/rd/index|charte du pôle R&D]].

- `rd/instrument/` — l'Instrument (migration depuis `projets/` effectuée le
  2026-08-08, fiche par fiche ; les anciennes fiches restent en `projets/` comme
  stubs `deprecated` avec pointeur — Cmd 10)
- `rd/infrastructure/` — serveur, agents, hardware/software ; voir
  [[atelier/rd/infrastructure/cartographie-routing-infrastructure|cartographie
  de routing (hardware, software, canaux, points forts/fragiles —
  2026-09-01)]] pour la vue d'ensemble, et
  [[atelier/rd/infrastructure/2026-08-20_pistes-developpement-infrastructure|pistes
  de développement infrastructure (2026-08-20)]] pour l'historique des pistes
- `rd/audio/` — ingénierie son générique
- `rd/outillage/` — scripts et bancs de test
- `rd/cahiers/` — cahiers append-only (registre des problèmes, journal des
  optimisations, comptes-rendus de session, jalons) ; cahiers d'expérience à
  venir (phase 2)
- `rd/veille/` — veille externe qualifiée (GitHub, arXiv, dépôts), ouverte le
  2026-08-18
- `rd/incidents/` — rapports d'incident caractérisés (contamination Unicode
  2026-08-22, crash gateway 2026-08-25) ; cf. Cmd 15 du protocole racine
- `rd/citadelle-du-sham/` — prototype 3D reçu au sas, versé le 2026-08-22
- `rd/bibliotheque/` — catalogue de la bibliothèque physique (déplacé de `meta/`
  le 2026-08-22) et index/glossaires transcrits des ouvrages ; instrument de
  repérage pour savoir *où chercher*, voir
  [[atelier/rd/bibliotheque/catalogue-bibliotheque|catalogue]]

---

## Instrument de la Tradition Primordiale

Application web 3D contemplative (Three.js/WebGL) visualisant l'arbre ontologique
akbarien sur l'axe des 38 degrés du *Nafas al-Raḥmān*. Voir
(cf. Domaine Réservé, fiche feuille de route et pile technique) pour l'état d'avancement par phase.

**Architecture** :
- [[atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3|Architecture
  v0.3]] — arbitrages actés (Phase 0 close, convention `degre_vertical`, lentille
  barzakh, quatre Angles de l'Espace) ; v0.1 et v0.2 conservées comme jalons
- [[atelier/rd/outillage/spec-generateur-manifeste|Spécification du générateur de
  manifeste]]

**Données et génération** (Phase 1, livrée) :
- `instrument-donnees.yaml` — v0.5.0, 44 nœuds (8 notionnels/structurants + 28 nœuds-degrés + 8 nœuds universels : 7 Aqtâb + Homme Universel) + 12 signes du zodiaque + **4 registres**
- `generer-manifeste.py` — v0.2.4, générateur déterministe, validations bloquantes, zéro LLM dans la boucle
- [[atelier/rd/instrument/angles-de-l-espace|Angles de l'Espace]] — les quatre Angles astrologiques (AS/DS/MC/FC), relectures tranchées

**Registres** (ouvert 2026-08-20) — partitions du même axe vertical, une par
tradition, non alignées entre elles (Art. 3 sashimono) :
[[atelier/rd/instrument/2026-08-20_instruction-branche-kabbale-phase3|architecture
et instruction]]. `tasawwuf` (axe principal, 5 Ḥaḍarāt en bornes de degrés),
`qabbalah` (axe parallèle, 10 Sephiroth/3 colonnes → 7 niveaux dérivés
mécaniquement), `hindouisme-tantra` (axe parallèle, 6 chakras + sahasrāra,
colonne unique — *Kundalinî-Yoga*), `vedanta` (axe parallèle, 4 états d'Âtmâ —
Vaishwânara/Taijasa/Prājña/Turīya — *L'Homme et son devenir selon le
Vêdânta*). Un seul ancrage inter-registre déclaré : Homme Universel →
Vaishwânara (traduction du verdict du 2026-07-26, aucun nouvel arbitrage) ;
tout le reste en attente. Refus mécanique par le générateur de tout domaine
portant à la fois `degres` et `rang` (Cmd 3).

**Prototype** :
- `instrument-prototype.html` — prototype Three.js, axe des 38 degrés, Barzakh supérieur, filament d'al-Insān al-Kāmil, boucle 38→11, anneau des nœuds notionnels ; **mis à jour le 2026-08-20** : sept nœuds Aqtâb + nœud Homme Universel rendus (équivalences établies), anneau zodiacal ajouté (12 signes au degré 19, 28 manāzil au degré 20, obliquité 23,44°), et surtout **lecture dynamique de `wiki-manifest.json`** — le prototype dérive désormais ses données du manifeste au lieu de les porter en dur (repli conservé si le fichier est inaccessible, provenance affichée) — voir [[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement|§5]] et [[atelier/rd/outillage/spec-generateur-manifeste|spec §5 ter]]

**Socle métaphysique universel** (en cours, 2026-07-16) — fondations de la trilogie
guénonienne (*Le Symbolisme de la Croix*, *Les États multiples de l'être*,
*L'Homme et son devenir selon le Vêdânta*) sur lesquelles les traditions multiples
de l'Arbre unique s'articulent :
- [[doctrinal/discernement/2026-07-16_sept-poles-aqtab-malakut-planetaire|Les sept
  Pôles/Aqtâb et le Malakūt planétaire]] — close (traditionnel)
- Fiches source associées : ch. II-III, IV, XI-XIII, XXIII+XXIX du *Symbolisme de la
  Croix* ; ch. IV, IX, XIII des *États multiples de l'être* ; ch. X, XV, XVI de
  *L'Homme et son devenir* ; *Tartîbut-Taçawwuf* (Abdul-Hâdî, 1911) ; *Futūḥāt* ch. 36
  — voir `doctrinal/index.md` §VI pour la liste complète
- [[doctrinal/sources/qabbalah-matiere-trilogie-guenonienne|Matière kabbalistique
  consolidée]] — `to-source` partiel, aucun ancrage YAML sans discernement dédié
- [[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16|Note d'impact]]
  — état *kari-kumi*, six *hozo* proposés (non taillés), chantiers ouverts (branche
  Kabbale, versant Sanātana Dharma, six directions de l'espace)

**Chantiers ouverts** : tenus au registre, plus ici — le bandeau zodiacal horizontal
(`INS-13`), le versant Sanātana Dharma (`INS-14`) et la réserve *wirātha* ↔ pôles
(`DOC-05`) y figurent avec leur statut et leur prochaine action. Voir
[[atelier/rd/registre-chantiers]] §1 et §7. Cette page ne tient plus de seconde liste :
c'est la double tenue qui périmait les deux.

**État d'avancement et pistes de développement (2026-08-20)** :
[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement|synthèse
par phase]] — Phase 3 plus avancée qu'évaluée initialement (deux nœuds
universels déjà établis par discernement clos) ; prototype mis à jour le
2026-08-20 (Aqtâb rendus, filament enrichi) ; pistes classées P1 à P6
(formalisation Phase 3, déblocage Phase 2, mise à niveau du prototype, amorce
Phase 5, hygiène documentaire, chantiers de fond).

---

## Matériels & Techniques

Ressources de fabrication, spécifications techniques, catalogues de matériaux.

- `/atelier/materiel/` — fiches matériaux, spécifications, sourcing
- [[atelier/materiel/studio-principal|Studio Principal]] — fiche-hub de l'espace d'atelier audio, `to-source`
- [[atelier/materiel/tascam-model-12|Tascam Model 12]] — table/interface centrale
- [[atelier/materiel/neve-1073spx|Neve 1073SPX]] — préampli/EQ analogique
- [[atelier/materiel/distressor-el8|Distressor EL8]] — compresseur-limiteur
- [[atelier/materiel/revox-a77|Revox A77]] — magnétophone à bande
- [[atelier/materiel/moog-voyager|Moog Voyager]] — monosynthétiseur analogique
- [[atelier/materiel/neumann-tlm103|Neumann TLM 103]] — micro à condensateur

---

## Entretiens & Témoignages

Enregistrements, retranscriptions, dialogues avec praticiens.

- `/atelier/entretiens/` — enregistrements, retranscriptions, approches

---

## Projets & Expériences (résiduel)

Le dossier `atelier/projets/` a été migré vers `rd/` le 2026-08-08 (ouverture du
pôle R&D, verdict Sidy). Il ne contient plus que des **stubs `deprecated`** :
- ceux des 16 fiches migrées (chacun pointe vers sa fiche canonique en `rd/` —
  Cmd 10, jamais de suppression sèche) ;
- celui d'`album-personnel.md`, déplacé le 2026-08-08 vers
  [[label/production/album-personnel]] (verdict Sidy : l'album relève de la
  création artistique — circuit `label/`, arbitrage `rd/` vs `label/` tranché).

Les expériences nouvelles ont vocation à être consignées directement en `rd/`.

---

## Études de Cas

Analyses systématiques d'entreprises, marques, maisons de référence — applications du framework d'étude de cas à des instances réelles.

Cadre : (cf. Domaine Réservé, fiche Framework d'étude de cas — Master Framework)

Chaque étude sépare strictement : **Faits** (sourcés), **Analyse** (interprétation raisonnée), **Transposition** (principes et garde-fous pour *Dans l'Absolu*, suggérés 🔍 jusqu'à validation humaine).

**Études disponibles** :
- [[etudes-de-cas/stones-throw|Stones Throw Records]] — cas d'école : indépendance, curation, longévité, diversification revenue sans dilution du propos (musique/vinyle, 1996–)
- [[etudes-de-cas/kojima-productions|Kojima Productions]] — studio-auteur, indépendance financée projet par projet, absence de backlist propre, dépendance structurelle à deux individus (jeu vidéo, 2015–), en anglais
- [[etudes-de-cas/zellige-grande-mosquee-paris|Zellige de la Grande Mosquée de Paris]] — lecture géométrique d'un pan de mur (frise, pavage girih, rosace centrale) à partir d'une photographie terrain non redressée ; aucune donnée anchorable dans l'Instrument en l'état, chantier ouvert sur le Quadrivium et l'Épître 6 des Ikhwān al-Ṣafāʾ (proportion arithmétique/géométrique/harmonique)
- [[etudes-de-cas/forteresses-architecture-defensive|Forteresses — données d'architecture défensive]] — fiche de **phase corpus** (méthode en deux phases validée 2026-08-24) : données brutes d'un reel de vulgarisation (terrain, couches, autarcie, dissuasion), sans interprétation ; tout item `to-source` ; recherches complémentaires ajoutées (recoupées sur la fortification concentrique)
- [[etudes-de-cas/dougong-consoles-bois|Dougong — consoles en bois à encorbellement]] — fiche de **phase corpus** : données brutes d'un reel de vulgarisation sur le système de consoles de la charpenterie chinoise (position, transfert de charge, comportement sismique, comparaison isolation de base), sans interprétation ; tout item `to-source` ; recherches complémentaires ajoutées (recoupées sur des sources académiques : Fang 2001, Yang 2023, Cao 2023)
- [[etudes-de-cas/refroidissement-passif-traditionnel|Refroidissement passif traditionnel — cours, eau, masse thermique]] — fiche de **phase corpus** : données brutes d'un reel de vulgarisation (tirage par effet de cheminée, refroidissement évaporatif, inertie thermique), sans interprétation ; litige factuel observé dans les commentaires consigné sans être tranché ; tout item `to-source` ; recherches complémentaires ajoutées (sources académiques ; antériorité exclusive du reel réfutée)
- [[etudes-de-cas/xuankong-temple-suspendu|Xuankong Si — temple suspendu du mont Heng]] — fiche de **phase corpus** (première à bénéficier de la consigne de recherches complémentaires, verdict Sidy 2026-08-24) : données brutes du reel sur l'ancrage en falaise, puis section distincte d'identification et de recoupement (27 poutres, fondation 491, colonnes non porteuses) avec écarts relevés ; tout item `to-source`

---
