---
title: Annales du circuit Herméneutique
type: meta
created: 2026-08-04
updated: 2026-09-09
---

# Annales du circuit Herméneutique

Journal chronologique inverse des opérations (la plus récente en haut). Append-only,
entrées insérées **après ce header**.
<!-- INSERTION: EN-TÊTE -->

## [2026-09-09] archivage | `categorie-editoriale` — le seul mot ajouté au vocabulaire d'annotation

- **Ordre de Sidy** : « ajoute un genre pour les catégories éditoriales ». Comble le manque que l'entrée précédente avait **rapporté sans le combler** : le champ `type:` de ce protocole ne nomme pas cette catégorie, et l'inventer d'office aurait été un mot de la machine, non du protocole. Sur verdict, il devient un mot du protocole.
- **`categorie-editoriale`** — la catégorie de publication ou de classement sous laquelle une œuvre paraît ou se range : *shōnen*, *seinen*, *thriller*, *gothique*, *comédie*, *roman*. **10 poses** dans le circuit.
- **C'est le seul mot de tout ce vocabulaire qui ne vienne pas du champ `type:`**, et donc le seul à devoir **porter sa limite dans son nom**. Il la porte : *éditoriale* dit que la catégorie est celle du **marché du livre et de l'édition**, jamais une catégorie de connaissance. **Un *shōnen* n'est pas une `ecole`** — les confondre serait exactement la faute de catégorie que le Cmd 3 poursuit, avec la rigueur accrue que ce circuit lui doit.
- **Deux noms voisins écartés pour collision**, et la raison vaut d'être consignée : **`registre`** est déjà un champ du Sceau de ce circuit (`registre: analyse | expression`) — l'employer aurait donné deux sens à un même mot au même endroit ; **`genre`** seul se serait confondu avec `data-genre`, l'attribut qui le porte.
- **Ce que le mot ne couvre pas, et qui reste sans genre** (Cmd 12) : un **métier** (*mangaka*), une **structure de production** (studio, éditeur), et **`saga`**, que ce protocole traite déjà comme une règle de fiche-hub. Le manque est rapporté plutôt que comblé **en étirant le mot** — un genre qui s'étire cesse d'être clos, et le vocabulaire perdrait la seule propriété qui le rend contrôlable.
- **Genres en usage dans le circuit** : 18 `oeuvre`, 10 `categorie-editoriale`, 5 `auteur`, 5 `dispositif`, 4 `figure`, 4 `concept`, 1 `entite`, 1 `principe`.
- **Épreuve des contrôles (§VII)** — *vert* : dépôt vivant, « 321 fiches annotées, 936 annotations. OK — aucune anomalie », code 0 ; bac à sable, `categorie-editoriale` dans une fiche du circuit ne lève **rien**. *Refus* : le même genre posé dans `doctrinal/symboles/` — « data-genre='categorie-editoriale' est valide, mais son circuit (doctrinal) ne l'admet pas », **D6**, code 2.
- **Vérification** — `verifier-invariants.py` : 1418 fichiers, **0 erreur, 0 avertissement**. Graphe régénéré : **arêtes identiques** — huitième vérification du régime apparié.
- **Commit** : à renseigner ci-dessous.

## [2026-09-09] archivage | Vocabulaire d'annotation propre au circuit, et 13 poses qu'il ouvre

- **Ordre de Sidy** : « étends le vocabulaire clos pour hermeneutique/ ». Les sept genres transversaux (`autorite`, `lieu`, `ouvrage`, `entite`, `ecole`, `cycle`, `principe`) ne savaient nommer ni une œuvre profane, ni un personnage, ni un dispositif d'œuvre : sur 90 poses proposées ici la veille, **53 avaient dû être rejetées faute de mot**.
- **Cinq genres propres, et ce ne sont pas des mots nouveaux.** `oeuvre`, `auteur`, `figure`, `dispositif`, `concept` sont, **terme pour terme, les valeurs du champ `type:` que ce protocole local déclare déjà**. L'annotation emprunte au circuit son propre vocabulaire et hérite du même coup de la garde Cmd 3 qui y est attachée : `auteur` « emprunte la forme d'archivage de `doctrinal/autorites/` sans en partager la fonction — aucun statut d'autorité conféré ni supposé » ; **`oeuvre` ne se fond jamais dans `ouvrage`**, réservé au traité traditionnel. Ne pas fondre ces deux registres est le fond même du non-syncrétisme.
- **`entite` reste admis ici**, à côté de `figure`. J'avais d'abord voulu l'exclure du circuit, en tirant argument de « le *hozo* y est exclu par défaut » — mais cette clause régit les **joints entre traditions**, non la faculté de nommer une entité reçue. Une fiche du circuit en cite légitimement une dans la même phrase qu'une figure de fiction : c'est même son sujet. La garde **ouvre les deux mots** au lieu de trancher à la place de Sidy (Cmd 12).
- **Migration des annotations de la veille, dans le même commit que l'amendement** : les 35 poses employaient `ouvrage` pour *Death Stranding*, *Metal Gear*, *Frankenstein* et `autorite` pour Kojima, Mary Shelley, Naoki Urasawa. **16 passent à `oeuvre`, 5 à `auteur`.** Sans cela, deux conventions auraient coexisté dans le circuit — et le validateur les aurait acceptées **toutes deux**, de sorte que rien n'en aurait averti plus tard.
- **13 poses nouvelles**, ouvertes par l'extension : 4 `figure` (Big Boss, Chimera Ant, monstre), 4 `dispositif` (Mother Base, iDroid, matrices artificielles), 4 `concept` (restriction, autotransmutation, immortalité, transposition), 1 `oeuvre`. **Genres en usage dans le circuit** : 17 `oeuvre`, 5 `auteur`, 4 `figure`, 4 `dispositif`, 4 `concept`, 1 `entite`, 1 `principe`.
- **Un défaut du proposeur trouvé et fermé** : il **sautait toute fiche déjà annotée**, de sorte qu'une extension du vocabulaire n'aurait **jamais** pu atteindre les 15 fiches de la passe précédente — 20 fiches et 52 poses étaient invisibles, et rien ne l'aurait dit. Il n'écarte désormais que les **clés** déjà posées, ce qui tient D5 sans geler la fiche, et il masque les balises existantes pour qu'une pose nouvelle ne puisse pas s'**emboîter** dans une ancienne. Contrôle après passe : **0 emboîtement**.
- **Un trou hérité, découvert en câblant la garde et comblé** : `verifier-invariants.py` portait `CIRCUITS = ["doctrinal", "atelier", "label", "meta"]`. **`hermeneutique` n'y figurait pas** — `circuit_de()` renvoyait `None`, de sorte que **B1** (clés de Sceau requises) et **C3** (étanchéité) n'ont **jamais contrôlé aucune des 28 fiches** de ce circuit depuis son ouverture. Le contrôle ne se plaignait pas : il ne regardait rien — forme exacte de PRO-01. Trouvé parce que le nouveau refus **D6** avait besoin d'un résolveur de circuit. **Mesuré avant de combler** : les 28 fiches passent B1 sans une seule erreur. `ETANCHEITE_INTERDITE` inscrit enfin « `doctrinal/` → `hermeneutique/` : jamais », que ce protocole local énonçait **sans que rien ne le garde**.
- **Épreuve des contrôles (§VII)** — le refus **D6** ne porte pas sur un genre inconnu (VOC le refusait déjà) mais sur un genre **valide posé dans le mauvais circuit**, et c'est cette face-là qui a été éprouvée. *Vert* : dépôt vivant, 320 fiches / 926 annotations, aucune anomalie ; bac à sable où `oeuvre` en herméneutique et `entite` en doctrinal ne lèvent **rien**. *Refus* : `data-genre="oeuvre"` dans `doctrinal/symboles/` et `data-genre="dispositif"` dans `atelier/rd/` — **deux refus**, chacun nommant son fichier **et son circuit**, code 2.
- **Ce qui reste sans genre, et le reste sciemment** (Cmd 12) : les catégories et genres éditoriaux — *shōnen*, *seinen*, *mangaka*, *thriller*, *gothique*, *comédie*, *roman*, *saga* — et les structures de production (*Kojima Productions*). Le vocabulaire `type:` du circuit ne les nomme pas, et **leur inventer un genre aurait été un mot de la machine, non du protocole**.
- **Vérification** — `verifier-invariants.py` : 1418 fichiers, **0 erreur, 0 avertissement**. Graphe régénéré : **arêtes identiques** — septième vérification du régime apparié.
- **Commits** : 4ccd523 (amendement et migration), cdee8f8 (les 13 poses).

## [2026-09-01] correction | `updated` du présent fichier remonté (Cmd 8)

Le frontmatter de ces annales portait `updated: 2026-08-30` alors que leur entrée la plus
récente était datée du 2026-09-01 — écriture incomplète au sens du Cmd 8, signalée par le
contrôle A3 du vérificateur d'invariants. Champ corrigé au 2026-09-01. Aucune entrée du
journal n'a été touchée.

Relevé au cours de la passe d'organisation des pôles `atelier/` et `meta/projet-unifie/`
du même jour (voir `atelier/annales.md`). C'était la **seule erreur réelle** que le
vérificateur signalait ce jour-là, noyée dans 209 lignes de bruit provenant de
dépendances tierces — motif du chantier `OUT-01` au registre des chantiers.

- **Commit** : 13eee60


## [2026-09-01] création | Expression : athanor-matrices-artificielles (phase 2, mise en regard)

- **Fiche créée** : `hermeneutique/expression/2026-09-01_athanor-matrices-artificielles.md` (type: concept, registre: expression, statut: brouillon)
- **Contexte** : ouverture de la phase 2 analytique du discernement Barzakh (2026-06-20) et des fiches symboles Golem (2026-08-30) et Frankenstein (2026-08-30). Demande de Sidy (2026-09-01) : mise en regard de l'athanor de Burckhardt avec la figure des cinq matrices artificielles.
- **Portance** : zōsaku. Aucun impact sur l'armature doctrinale.
- **Substance** : (1) relevé de l'opposition structurelle — Burckhardt : autotransmutation (athanor = l'opérateur lui-même) vs. Golem/Frankenstein : fabrication de tiers ; (2) relevé de la convergence — contenant-qui-cède, danger de la rupture du scellement, Burckhardt décrit en termes très proche de la failure mode des matrices ; (3) deux blocs 🪵 Restitution (Golem, Barzakh/alam-al-mithal) ; (4) Confrontation Gizeh : matière axiale présente (calumet comme canal subtil), aucun ancrage au pôle gizeene.
- **Clés doctrinales** : [[doctrinal/symboles/golem]], [[doctrinal/symboles/barzakh]], [[doctrinal/symboles/alam-al-mithal]] — sens unique, 🔍 suggéré par défaut.
- **Discernement** : [[doctrinal/discernement/2026-06-20_matrices-artificielles-barzakh]] — matière issue du discernement.
- **Sources** : [[doctrinal/sources/burckhardt-alchimie-ch13-athanor-transcription]].
- **Héritages non-levés** : Golem et Frankenstein demeurent phase 1, sources: ["to-source"]. Cette fiche les cite, elle ne les valide pas. Statut de la mise en regard : brouillon, en attente de verdict doctrinal le cas échéant.
- **Étanchéité** : correction appliquée simultanément : les trois liens doctrinal→hermeneutique en sens interdit (golem.md:65, discernement:50, annales:229) ont été vidés de leurs wikilinks hermeneutique. Le texte narratif est conservé ; les fichiers demeurent dans une écriture append-only. Cf. correction d'étanchéité dans doctrinal/annales.md (2026-09-01).

---

## [2026-08-30] création | Frankenstein (phase 1, corpus brut)

- **Fiches créées** :
  - `hermeneutique/frankenstein/frankenstein.md` — œuvre (roman, Mary Shelley, 1818)
  - `hermeneutique/auteurs/mary-shelley.md` — auteur
- **Type** : œuvre (roman), registre analyse
- **État** : phase 1 (corpus brut, to-source)
- **Contenu** : figure moderne de la création artificielle d'un être par un savant. Contexte (1816, Villa Diodati), structure du roman, processus de création, la Créature, thèmes centraux, portée symbolique (Prométhée, écho sécularisé du Golem)
- **Lien avec discernement en cours** : signalé comme piste pour [[doctrinal/discernement/2026-06-20_matrices-artificielles-barzakh]] (matrices artificielles et Barzakh) et [[doctrinal/symboles/golem]] (figure traditionnelle analogue) — aucun lien doctrinal inscrit tant que le discernement n'est pas tranché
- **Procédure appliquée** : exploitation du graphe (2026-08-30) — fiches orphelines, liens signalés mais non inscrits, en attente de verdict Sidy (Cmd 12)
- **Commit** : 659808c

---

## [2026-08-20] réparation | Rétablissement de la convention d'insertion (A2)

- **Contexte** : rapport conjoint Studio–Gardien déposé en `_inbox/`
  (`rapport-conjoint-studio-gardien-etude-depot-20260820.md`), point 4.
- L'entrée « [2026-08-20] expression | Barzakh onirique et interface littéraire »
  avait été insérée en **queue** de fichier au lieu de l'**en-tête**, en rupture
  de la convention chronologique inverse (`<!-- INSERTION: EN-TÊTE -->`).
  Remontée à sa place, immédiatement après ce header.
- `updated:` remonté au 2026-08-20 (Cmd 8).
- **Commit** : `dafc266`

---

## [2026-08-20] expression | Barzakh onirique et interface littéraire

- **Circuit ouvert** : exploration conceptuelle en registre `expression` (portance: zōsaku)
- **Fiche** : [[hermeneutique/expression/2026-08-20_barzakh-onirique-interface-litteraire]]
- **Source** : [[doctrinal/sources/elbenni-dreaming-ummah-islamofuturism-2025]]
- **Idée explorée** : l'ʿālam al-mithāl comme espace d'interface entre rêve et politique, entre intention et manifestation — lieu de naissance de la science fiction.
- **Vigilance** : ne clôt aucun discernement ; ne prétend pas que l'usage esthétique du barzakh coïncide avec le barzakh métaphysique (Ibn ʿArabī). Distinction maintenue.
- **Statut** : brouillon — attend verdict explicite (Cmd 12) si migration vers discernement.

---

## [2026-08-16] archivage | Lot Toriyama / Urasawa — 5 fiches (2 auteurs + 3 oeuvres)

- **Contenu archivé** : 5 fiches rédigées avec sourcing web, statut global `brouillon`, joints doctrinaux en l'état suggéré (*kari-kumi*, portance *zōsaku*).
  - `hermeneutique/auteurs/akira-toriyama.md` — biographique, aucune clé doctrinale.
  - `hermeneutique/dragon-ball/dragon-ball.md` — joint 🔍 vers [[doctrinal/symboles/lignees-celestes-taoisme]].
  - `hermeneutique/dr-slump/dr-slump.md` — comédie pure, aucune clé doctrinale.
  - `hermeneutique/auteurs/naoki-urasawa.md` — biographique, aucune clé doctrinale.
  - `hermeneutique/20th-century-boys/20th-century-boys.md` — deux joints 🔍 vers [[doctrinal/deviations/contre-initiation]] et [[doctrinal/deviations/renversement-des-symboles]].
- **Index et annales mises à jour** : `hermeneutique/index.md` et `hermeneutique/annales.md`.
- **Vigilance** : trois clés doctrinales 🔍 resteront suggérées (verdict réservé à l'utilisateur, Cmd 12) ; aucune fiche `discernement` ouverte.
- **Méthode** : archivage selon UPDATES.md, validation double-contrôle sashimono appliquée, aucune clé établie.
- **Commit** : `14383f0`

---

## [2026-08-13] verdict | Fondement du lien de source aux fiches d'auteur — filiation, non navigation

- **Porte sur** : `25078de` (réciproque des liens) et sur l'entrée qui la consigne.
  Aucun fichier de contenu modifié : les liens posés **tiennent inchangés**, seul
  leur fondement est corrigé.
- **Verdict de Sidy, 2026-08-13** : « En tant qu'auteur avéré, la filiation est
  justifiée. » Le lien de `auteurs/hideo-kojima` et `auteurs/yoji-shinkawa` vers
  `sources/art-of-death-stranding` repose sur une **filiation d'auteur** — les deux
  sont auteurs avérés de la pièce, la fiche de source portant
  `createur: "Yoji Shinkawa (direction artistique) — Kojima Productions"`.
- **Rectification de la lecture de la machine** : l'entrée précédente qualifiait ce
  lien de « navigationnel, non probatoire », et le tenait pour hors de portée de la
  clause du protocole (`6a800ca`). Ce qualificatif est **remplacé** : le lien relève
  de la filiation d'auteur, relation distincte de celle que vise la clause — laquelle
  règle le rapport d'une source aux fiches qu'elle **appuie** (champ `sources:`), non
  son rapport à ceux qui l'ont **faite** (champ `liens:`). Les deux fiches d'auteur
  demeurent `sources: ["to-source"]` : la filiation ne lève aucun `to-source` et ne
  touche pas leur `statut_analyse`.
- **Réserve maintenue** : aucun rang d'autorité n'est conféré ni supposé par le
  `type: auteur` (Cmd 3, clause de la nomenclature du circuit).

---

## [2026-08-13] correction | Réciproque du lien de source chez Kojima et Shinkawa

- **Commit** : 25078de
- **Point signalé le même jour, tranché par Sidy** : la fiche
  `hermeneutique/sources/art-of-death-stranding` pointait vers les deux fiches
  d'auteur sans réciproque, alors que les `liens:` du circuit sont jusqu'ici
  bidirectionnels. `[[hermeneutique/sources/art-of-death-stranding]]` ajouté aux
  `liens:` de `auteurs/hideo-kojima` et `auteurs/yoji-shinkawa` ; `updated`
  incrémenté à 2026-08-13 sur les deux (Cmd 8), `created` intact.
- **Articulation avec la clause du protocole amendée en `6a800ca`** — « elle est
  citée par le champ `sources:` des fiches qu'elle appuie, **non par leur `liens:`** » :
  cette clause vise les fiches que la source **appuie**. Les deux fiches d'auteur
  demeurent `sources: ["to-source"]` et ne tirent aucune assertion de la pièce ; le
  lien posé ici est **navigationnel, non probatoire**, et ne modifie ni leur statut
  de source ni leur `statut_analyse`. **Lecture de la machine, soumise à révision**
  si Sidy entend la clause plus largement — auquel cas le lien se retire, ou se
  déplace en `sources:`, en une édition.
- `verifier-invariants.py` contrôle la résolution (C1), **non la réciprocité** :
  celle-ci reste un contrôle à l'œil, et n'a jamais été attestée par le script.
- **Vérification mécanique** : `0 erreur(s), 48 avertissement(s)` — les 48
  préexistants, **aucun** sur les deux fiches d'auteur.

---

## [2026-08-13] amendement | Protocole local — `sources/` et `type: source` inscrits au Sceau

- **Commit** : 6a800ca
- **Verdict** : donné par Sidy le 2026-08-13, sur diff soumis intégralement avant
  écriture. Lève le signalement « amendement dû, non appliqué » porté depuis
  `b857e5d` (Cmd 12 satisfait : la lettre du protocole n'a été touchée qu'après
  verdict explicite).
- **Trois insertions, aucune suppression** dans `hermeneutique/CLAUDE.md` :
  1. **Nomenclature** — `hermeneutique/sources/<slug>.md` ajouté à l'énumération.
  2. **Sceau** — `type: … | source` (l'énumération portait
     `oeuvre | auteur | figure | dispositif | concept | analyse`).
  3. **Glose du type** — pièce déposée servant d'appui documentaire ; vit en
     `hermeneutique/sources/`, porte le slug de l'œuvre en `oeuvre:`, décrit chaîne
     d'édition, rang et avertissements d'usage ; **citée par le champ `sources:`**
     des fiches qu'elle appuie, non par leur `liens:` ; emprunte la forme de
     `doctrinal/sources/` sans en partager la fonction — **elle ne lève par
     elle-même aucun `to-source`**, la levée restant un verdict de l'utilisateur sur
     texte primaire (Cmd 5).
- **Cmd 8 sans objet** : le fichier n'a pas de frontmatter (il ouvre sur la basmala),
  aucun champ `updated` à incrémenter. La mention « Statut : méthode à l'essai
  (éclatement expérimental du 2026-08-12) » n'a pas été touchée.
- **Mises à jour de conséquence** : les mentions « amendement dû, signalé et non
  appliqué » de `hermeneutique/index.md` et de
  `hermeneutique/sources/art-of-death-stranding.md` — devenues fausses — sont
  remplacées par le constat de l'amendement.
- **Vérification mécanique** : `0 erreur(s), 48 avertissement(s)` — les 48
  préexistants, **aucun** sur les trois fichiers touchés.

---

## [2026-08-13] correction | Index du circuit — référencement du dossier `sources/`

- **Commit** : bdaf1da
- **Omission de la passe b857e5d, rattrapée** : `hermeneutique/index.md` énumère
  l'intégralité des fiches du circuit ; le dossier `sources/` et sa première fiche
  n'y figuraient pas. Section `## Sources` ajoutée avant `## Expression`, portant
  la fiche et le rappel du rang tertiaire de la pièce.
- L'**amendement dû** au `CLAUDE.md` local (dossier `sources/` et `type: source`
  absents de la nomenclature et du Sceau) est **rappelé dans l'index**, toujours
  **non appliqué** — verdict réservé à Sidy (Cmd 12).
- **Point signalé, non tranché** : la fiche de source porte
  `liens: ["…death-stranding", "…yoji-shinkawa", "…hideo-kojima"]` sans réciproque
  chez les deux auteurs, alors que les `liens:` du circuit sont jusqu'ici
  bidirectionnels. `verifier-invariants.py` contrôle la résolution (C1), non la
  réciprocité : aucune fiche d'auteur n'a été touchée sans demande.
- **Vérification mécanique** : `0 erreur(s), 48 avertissement(s)` — les 48
  préexistants, **aucun** sur `hermeneutique/index.md` ni sur la fiche de source.

---

## [2026-08-13] confrontation | Artbook Death Stranding — dépouillement et ouverture de `sources/`

- **Commit** : b857e5d
- **Pièce** : `raw/TheArtOfDeathStranding(Ru-TO-Eng).pdf`, déposée le 2026-08-13
  par Sidy (258 pages). `raw/` immuable — pièce ni modifiée ni déplacée.
- **Rang établi** : artefact linguistique **tertiaire**. Chaîne Titan Books
  (Londres) → *Мир игры Death Stranding*, ЭКСМО 2019 → retraduction **automatique**
  RU→EN (`onlinedoctranslator.com`). Conséquence : la pièce ne peut fournir aucun
  terme comme lettre et **ne lève aucun `to-source`**. La décision de méthode du §5
  de la fiche-œuvre (vocabulaire non traité) en sort confirmée, non levée.
- **Dossier ouvert** : `hermeneutique/sources/`, sur verdict de Sidy du 2026-08-13
  — le circuit est appelé à recevoir des sources visuelles pour une très grande
  part. Première fiche : `hermeneutique/sources/art-of-death-stranding.md`.
- **Amendement dû, signalé et NON appliqué** (Cmd 12) : `hermeneutique/CLAUDE.md`
  ne mentionne ni le dossier `sources/` dans sa nomenclature, ni le `type: source`
  employé par cette fiche — le Sceau du circuit énumère `oeuvre | auteur | figure |
  dispositif | concept | analyse`. Le tréfonds est en avance sur la lettre du
  protocole tant que Sidy n'a pas tranché la rédaction.
- **Confrontation Gizeh reprise** (§7 de la fiche-œuvre) sur matière neuve : deux
  emprunts égyptiens **déclarés par les concepteurs** (capsule du nourrisson relié,
  p. 26 du PDF ; personnage de Higgs, p. 64 du PDF), l'un et l'autre **vérifiés à
  l'image**, la planche de Higgs portant davantage que sa légende (masque funéraire,
  emblème à coiffe *nemes*). **Résultat : confronté, aucun ancrage** — emprunt
  ornemental, sans fonction polaire, sans contenu métrologique ni septénaire. Y
  voir un ancrage serait l'erreur de catégorie du CLAUDE.md racine §VII.2 (c).
  Consigné parce que **négatif**, non parce qu'inexistant : le « néant relevé »
  antérieur ne vaut plus pour ce registre.
- **Résultat négatif consigné** : le dispositif de l'aide asynchrone (§4), tenu par
  la fiche pour le sommet formel de l'œuvre, est **entièrement absent** de la pièce
  (recherche systématique sur la couche texte, zéro occurrence pertinente).
- **Portance inchangée** : aucun joint promu. Le bloc 🪵 Restitution du §6.1 voit sa
  seule clause factuelle devenue fausse corrigée (un document de production a
  désormais été consulté) ; le **verdict est préservé**, le classement en
  **homologie** tient. Le §6.3 reste sans cible. Tout demeure *zōsaku* / *kari-kumi*.
- **Statut** : la fiche-œuvre reste `statut_analyse: brouillon` — la pièce est un
  **cinquième** type de source, ne répondant à aucune des quatre priorités du §8.
  Elle ne peut toujours appuyer aucune fiche `registre: expression`.
- **Manquements de la machine, rattrapés avant commit** : (a) des noms de dispositifs
  repris de la couche traduction-machine avaient été employés comme lettre dans la
  section qui déclarait cette couche inutilisable — réécrits en termes génériques et
  requalifiés en corroboration **par l'image** ; (b) une filiation Odradek/Kafka
  affirmée sans texte consulté (Cmd 5) — rétrogradée en piste `to-source` explicite ;
  (c) une légende citée p. 24 alors qu'elle est p. 29 — corrigée, et le statut des
  pages (pages du PDF, non folios imprimés ; 258 vs 256, aucun folio dans la couche
  texte) désormais déclaré, la correspondance restant `to-source`.
- **Matière signalée et non versée** : collaboration vestimentaire avec la marque
  **Acronym**, relevant de `atelier/` ou `label/`. Sens de lien unique depuis ce
  circuit — rien n'est versé sans demande explicite.
- **Vérification mécanique** : `verifier-invariants.py` → `0 erreur(s), 48
  avertissement(s)`, les 48 préexistants (`atelier/rd/`, `doctrinal/annales.md`,
  `doctrinal/index.md`), **aucun** sur `death-stranding` ni sur la fiche de source.

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
