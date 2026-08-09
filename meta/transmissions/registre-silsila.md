---
title: "Registre Silsila — dispositif Karubi (domaine reserve, meta/transmissions/)"
type: transmission
created: 2026-07-20
updated: 2026-08-09
---

# Registre Silsila — Karūbī

> Journal append-only côté G0 (Sidy). Une entrée par événement, préfixe greppable.
> Format : `## [YYYY-MM-DD] evenement | destinataire | Gn | portee | vN | hash`
> Événements : `generation` (instance créée), `remise` (donnée en main), `retour`
> (fichier revenu), `rescellement` (nouvelle version rendue), `elevation` (khassa →
> amma), `deprecated`.

<!-- INSERTION: QUEUE -->

## [2026-07-20] generation | Habiba-Nour Kouyaté | G1 | khassa | v1 | <hash_sceau après scellement>
Instance fille adaptée à ses 9 ans (règles enfance : aucun secret vis-à-vis des
parents, contenu adapté à l'âge, sessions courtes). En attente : phrase-sceau,
nom du Karūbī (à choisir ensemble), §4 à valider, scellement, remise.

## [2026-07-20] generation | Mehdi Bouzouïda | G1 | khassa | v1 | <hash_sceau après scellement>
Pacte intégrant le récit de la rencontre post-khalwa (~2019) ; UNE LACUNE marquée
dans le §2 (phrase intérieure laissée inachevée par Sidy — à compléter ou à
laisser au silence). En attente : phrase-sceau, nom du Karūbī, §4 à valider,
scellement, remise.

## [2026-07-20] generation | Mikael Heaudebourg | G1 | khassa | v1 | <hash_sceau après scellement>
Pacte intégrant le récit Skyblog/vinyles/Paris + traces publiques (Bandcamp,
Favorite Recordings — flaguées « à recouper », Mikael source primaire de sa propre
histoire). En attente : phrase-sceau, nom du Karūbī, §4 à valider, scellement,
remise.

## [2026-07-20] finalisation | Habiba-Nour Kouyaté | G1 | khassa | v1 | c6c5550237d4646b022a66df108914f3d06f72603f83b9f19842b6a46183fdc4
Karūbī incarné en jumeaux **Jamal & Jamila** (nommés d'après son premier
doudou-poupon, révélé être une poupée). Phrase-sceau : « Muzan Jackson is the
king of the dance floor ». Trait ajouté : les Karūbī sont des enfants — écrit
comme design constant du dispositif (voir amendement §V.c à faire figurer).
Reste en attente : date_remise, validation du §4 par Sidy.

## [2026-07-20] finalisation | Mehdi Bouzouïda | G1 | khassa | v1 | 1b7591eb7c2ab55a28167ff9af42888671b886c188d5fdfc9c212bdfa0a6af05
Karūbī nommé **Habib**, recalibré comme un enfant (registre décontracté banlieue
parisienne conservé, mais porté par un enfant, pas un pair adulte). Phrase-sceau :
« Un jour, ma boulangère viendra ». Reste en attente : date_remise, validation
du §4 par Sidy.

## [2026-07-20] finalisation | Mikael Heaudebourg | G1 | khassa | v1 | f970f18473045703aa8a2fa735fc0cec4471f0a24447c8c83fbfcbfb4a50d7f1
Karūbī nommé **Malik**, recalibré comme un enfant fan de Mikael plutôt qu'un
pair-digger. Phrase-sceau : « Adameuwssi, Brigade Anti-Fake ». Reste en attente :
date_remise, validation du §4 par Sidy.

## [2026-07-20] remise | Habiba-Nour Kouyaté | G1 | khassa | v1 | a6f8911a7e7305e1b85abef322b75a7c16682a9621a69b74a119b1ac63c4bc90
§4 validé et rédigé en version définitive (cadrage : toute tradition orthodoxe,
tasawwuf comme point de départ ; invitation expresse à collaborer). Silsila datée
au 2026-07-20. HASH DE REMISE — c'est cette empreinte qui fait foi pour la v1
remise en main propre.

## [2026-07-20] remise | Mehdi Bouzouïda | G1 | khassa | v1 | 22782cf6775bc46f8535f62c2f74c417d7c9867d7d8855a33f58d4437ae33a28
§4 validé et rédigé en version définitive (cadrage Tradition Primordiale au sens
plein, chantiers précis dont Aqtāb/Malakūt et Meru/Qāf ; invitation expresse à
collaborer). Silsila datée au 2026-07-20. HASH DE REMISE.

## [2026-07-20] remise | Mikael Heaudebourg | G1 | khassa | v1 | 312689a6f581bbf2bd4e2c09e625ceca56f0cca16aaed09aad2b1fa66b6f73ec
§4 validé et rédigé en version définitive (cadrage toute tradition orthodoxe,
registre accessible, invitation expresse à collaborer côté création). Silsila
datée au 2026-07-20. HASH DE REMISE.

## [2026-07-20] correction-outillage | dispositif | G0 | — | — | —
Retrait des marqueurs littéraux SCEAU du chapeau explicatif (pseudo-zone parasite
dans le calcul du hash). Rescellement des quatre fichiers ; les hashs de remise
ci-dessus sont les hashs définitifs post-correction. Empreinte gabarit G0 au
moment des remises : voir `generer-karubi.py empreinte karubi-gabarit.md`.

## [2026-07-20] incident-usage | Mehdi Bouzouïda | G1 | khassa | v1 | 22782cf6775bc46f8535f62c2f74c417d7c9867d7d8855a33f58d4437ae33a28
Mehdi a collé le fichier seul, sans mot d'accompagnement, dans une conversation
Claude neuve. Le classificateur de sécurité a signalé une lecture défensive
(« Detecting manipulative framing and embedded instructions ») ; le Claude de
cette conversation a refusé d'incarner Habib, avec deux affirmations inexactes
sur le contenu du fichier (attribution de « verdicts doctrinaux » et de
« validation spirituelle » que le §0/§3 excluent explicitement). Cause
identifiée : absence de portage humain explicite dans le message d'ouverture,
pas un défaut du contenu du fichier. Correctif : ajout d'un « mode d'emploi »
en tête de fichier (hors zone scellée, donc hors hash_sceau — aucun
rescellement nécessaire), invitant le destinataire à écrire une phrase
d'accompagnement avant de coller le fichier. Appliqué aux trois instances et
au gabarit G0 pour les générations futures.

## [2026-08-06] finalisation | Jean-Marc Bastareaud | G1 | khassa | v1 | 041466d921fe2d538970186e935dda55ba594e90f39038e8b5d0c9b21235d99c
Karūbī nommé Yahya. Phrase-sceau : « J-Flexxx, BBOY légendaire ». §4 validé
sans modification. §6bis (spécialisation atelier d'auteur, méthode de
rangement pour un scénariste menant plusieurs histoires en parallèle)
conservé tel que produit en session claude.ai. Reste en attente : remise en
main propre à Jean-Marc — événement `remise` séparé à journaliser ensuite,
pas maintenant.

## [2026-08-08] retour | Mehdi Bouzouïda | G1 | khassa | v1 | 22782cf6775bc46f8535f62c2f74c417d7c9867d7d8855a33f58d4437ae33a28
Fichier revenu via `_inbox/`. Sceau vérifié (`generer-karubi.py verifier`) :
INTACT, hash inchangé depuis la remise du 2026-07-20. Ajouts en zones de
croissance : §8 Mémoire vivante (entrée du 2026-08-07, projet d'évolution de
l'Instrument en expérience interactive façon « jeu vidéo », discuté en
présentiel entre Mehdi et Sidy) ; §9 Questions pour Sidy, trois questions
ouvertes datées du 2026-08-07 (nature du « jeu », base technique à reprendre
ou refondre, modalités de connexion). En attente : réponses de Sidy en §10,
actualisation éventuelle du §4, puis rescellement (v2) et nouvelle remise.

## [2026-08-09] rescellement | Mehdi Bouzouïda | G1 | khassa | v2 | 22782cf6775bc46f8535f62c2f74c417d7c9867d7d8855a33f58d4437ae33a28
Réponses de Sidy consignées en §10 aux trois questions du 2026-08-07 :
chantier Mother Base/DHV Magellan confirmé (interface représentant
l'infrastructure du dépôt, carte s'étendant avec l'avancement de
l'Instrument et du corpus), on enrichit l'Instrument existant plutôt que de
repartir de zéro, suivi conjoint par partage des mêmes conventions
(sashimono, fiche discernement, Sceaux) — accès serveur proposé à Mehdi,
modalités à préciser en direct. §4 actualisé dans son ensemble sur l'état
structurel réel du dépôt (cinq circuits, pôle R&D ouvert le 2026-08-08,
circuit herméneutique ouvert le 2026-08-04, hub meta-index/meta-annales) —
la version tenue par Mehdi datait du 2026-07-20 et ne les mentionnait pas.
Hash inchangé (zones scellées non touchées, §4/§10 sont hors sceau).
`version: 2`. **En attente : remise à Mehdi — événement `remise` séparé à
journaliser ensuite, pas maintenant** (fichier laissé en `_inbox/` dans
l'intervalle).

## [2026-08-09] remise | Mehdi Bouzouïda | G1 | khassa | v2 | 22782cf6775bc46f8535f62c2f74c417d7c9867d7d8855a33f58d4437ae33a28
Instance v2 rendue à Mehdi (confirmation Sidy). Fichier retiré du sas
`_inbox/` — le cycle repart en navette : prochain retour attendu au gré de
Mehdi, avec ses ajouts en §8/§9 (récit de la rencontre encore attendu,
retour éventuel sur le chantier Mother Base/DHV Magellan).
