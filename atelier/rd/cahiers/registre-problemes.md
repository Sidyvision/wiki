---
title: "Registre des problèmes — pôle R&D (cahier append-only)"
type: meta
created: 2026-08-08
updated: 2026-08-09
tags: [atelier, rd, cahier, registre, laboratoire]
sources: []
links: []
---

# Registre des problèmes du pôle R&D

Cahier append-only des problèmes, erreurs, blocages et anomalies rencontrés dans
les travaux du pôle `rd/` — et de leur résolution. Ouvert le 2026-08-08 (verdict
Sidy), premier cahier concret de la phase 2 de la proposition de pôle (discipline
de laboratoire, §V, règle 3 : « Un échec se consigne comme un succès »).

**Format** — miroir du bloc 🧪 Expérience, appliqué à l'erreur :

- **Symptôme** : le fait brut, tel qu'observé, sans interprétation (§VIII.2 : le
  résultat brut précède toujours l'interprétation).
- **Diagnostic** : l'interprétation, séparée du fait et flaguée comme telle.
- **Résolution** : ce qui a été fait — ou « aucune — abandon assumé ».
- **Compréhension tirée** : la leçon réutilisable. C'est le but du registre.
- **Liens** : fiches, commits, chantier concerné.
- **Statut** : `ouvert | resolu | abandonne | reporte`.

**Règle** : jamais de réécriture ni de suppression ; un problème clos reste
consigné. Insertion en tête (la plus récente en haut), marqueur ci-dessous.

<!-- INSERTION: EN-TÊTE -->

---

## [2026-08-09] reporte | Angle mort structurel de `verifier-invariants.py` — le contrôle C3 d'étanchéité n'existe pas pour les fichiers `annales.md`/`index.md`

- **Symptôme** : en tranchant le signalement `doctrinal/ → meta/personnel/`
  (entrée suivante), constat que le contrôle C3 d'étanchéité inter-circuits
  n'a **jamais** été en mesure de signaler ce cas, ni avant ni après
  résolution — ni comme erreur, ni comme avertissement.
- **Diagnostic** : dans `verifier-invariants.py`, `FICHIERS_EXEMPTS_C3`
  (l.58) regroupe `NOMS_ANNALES` (tous les `annales.md`, `meta-annales.md`)
  et `{"index.md", "meta-index.md"}`. À l.344,
  `interdits = set() if nom in FICHIERS_EXEMPTS_C3 else ETANCHEITE_INTERDITE.get(circ, set())`
  — tout fichier portant un de ces noms, **dans n'importe quel circuit**, est
  purement et simplement exempté du contrôle, quelle que soit la cible du
  lien. Le motif de conception est légitime (« les annales peuvent citer
  d'autres circuits pour situer les passes ») mais la portée de l'exemption
  est **totale** : un `doctrinal/annales.md → meta/personnel/x` (interdit)
  est structurellement invisible au même titre qu'un
  `doctrinal/annales.md → atelier/materiel/x` (anodin, nécessaire au
  journal). Le script ne distingue pas les deux cas.
- **Compréhension tirée** (valeur pour le pôle R&D — mission de
  self-improvement de l'infrastructure) : une exemption large, conçue pour
  un besoin légitime et étroit (contextualiser un journal), a pour effet de
  bord de rendre **indétectable** la classe d'erreur la plus sensible du
  dépôt (fuite `meta/` vers un circuit neutre). Le signalement traité ici a
  été trouvé par relecture humaine, pas par le script — preuve que
  l'invariant mécanique actuel ne couvre pas ce risque. Piste
  d'amélioration identifiée, non implémentée à ce stade : distinguer, dans
  `FICHIERS_EXEMPTS_C3`, deux régimes plutôt qu'une exemption binaire —
  garder l'exemption totale pour les cibles neutres (`doctrinal/`,
  `atelier/`, `label/`, `hermeneutique/`), mais faire remonter un
  **avertissement** (pas une erreur bloquante, pour ne pas casser
  l'append-only rétroactivement) dès qu'un `annales.md`/`index.md` de
  circuit neutre contient un lien vers `meta/` — cas qui ne devrait
  structurellement jamais se produire hors du hub `meta-index.md` lui-même.
- **Résolution** : aucune, à dessein — signalement pur (Cmd 7), pas de
  modification de script sans verdict Sidy explicite sur l'approche
  (le risque d'un correctif hâtif est de générer de faux positifs sur des
  citations légitimes `annales.md → atelier/` ou `→ label/`, qui sont la
  majorité des cas et doivent rester silencieuses).
- **Liens** : `verifier-invariants.py` (`FICHIERS_EXEMPTS_C3`, l.56-58 ;
  usage l.344) ; entrée suivante (signalement résolu par relecture humaine,
  ayant révélé cet angle mort).
- **Statut** : `reporte` — piste d'amélioration ouverte pour le pôle R&D,
  en attente d'arbitrage Sidy sur l'implémentation.

---

## [2026-08-09] resolu | Tranché — signalement `doctrinal/ → meta/personnel/` (sens interdit), correction d'une erreur factuelle du signalement initial

- **Symptôme** : instruction explicite de Sidy (« tranche le signalement
  doctrinal/annales.md → meta/personnel/ ») demandant le verdict sur le
  signalement laissé ouvert dans l'entrée précédente — liens en sens
  neutre → sensible (interdit §VI) depuis `doctrinal/annales.md` vers
  `meta/personnel/` et `meta/projet-unifie/`.
- **Diagnostic** : vérification directe par grep de `doctrinal/annales.md`
  (et non plus par reprise de l'entrée précédente) donne un résultat
  différent des « 4 fiches » annoncées :
  - **Erreur corrigée** : `gout-sucre-priere` **n'a aucun lien entrant
    depuis `doctrinal/annales.md`** — grep exhaustif du fichier, zéro
    occurrence. Son seul lien entrant réel vient de
    `meta/genealogie/2026-06-20_oiseau-serpent-jumeau.md`, un lien
    **intra-`meta/`**, donc parfaitement conforme à §VI. L'entrée
    précédente de ce registre et l'entrée d'ouverture de
    `meta/meta-annales.md` reproduisaient cette erreur — non corrigées
    rétroactivement (Cmd 9, append-only), signalée ici (Cmd 5 : aucune
    affirmation factuelle erronée ne doit rester sans correction
    consignée).
  - **Ensemble réel, confirmé** : 3 liens, tous dans des entrées
    d'annales déjà publiées et datées du 2026-06-20 —
    `[[meta/2026-06-20_bourdonnement-tempe]]` (l.970),
    `[[meta/2026-06-20_taekwondo-hansu]]` (l.978),
    `[[meta/briefing-claude-ai]]` (l.853, résout vers
    `meta/projet-unifie/briefing-claude-ai`).
  - **Observation clé** : dans la même entrée que le lien
    `bourdonnement-tempe` (l.969-970), six autres fiches `meta/`
    personnelles sont nommées **en texte brut, sans crochets**
    (`herbes-pratiques, ikigai, noms-symboles-financiers, fibrillation,
    bejjar-genealogie, taekwondo-hansu`) — la convention rédactionnelle
    des annales tolère déjà de **citer sans lier**. Les 3 liens
    effectivement bracketés sont donc une inconsistance de forme au sein
    d'une pratique déjà établie de mention, non une nécessité qui
    forcerait à ouvrir une exception au principe §VI.
  - **Étanchéité mécanique** : confirmé dans `verifier-invariants.py`
    (`FICHIERS_EXEMPTS_C3`, l.58) que tout fichier `annales.md`/`index.md`,
    de tout circuit, est structurellement exempté du contrôle C3
    d'étanchéité — le script ne signalera jamais ce cas, dans un sens ou
    dans l'autre. Le verdict est donc de nature strictement éditoriale
    (Cmd 12), non mécanique.
  - **Découverte hors périmètre du signalement initial** : `doctrinal/index.md`
    (§IX) portait aussi `[[meta/sidy|Profil : Sidy]]` — même violation de
    sens, mais sur un fichier **non append-only** (à la différence des
    annales), donc directement corrigible sans tension avec Cmd 9/Cmd 10.
- **Résolution** :
  - `doctrinal/annales.md` : **aucune modification**. Les 3 liens vivent
    dans des entrées déjà publiées, datées, append-only (Cmd 9) — les
    rétracter serait une réécriture de l'historique (Cmd 10,
    non-révisionnisme), le remède serait pire que le mal pour un journal
    qui documente fidèlement l'état du dépôt au jour de sa rédaction. Le
    hub `meta-index.md` (ouvert la veille, entrée précédente) donne
    désormais à chacune des 3 fiches visées un lien entrant légitime,
    intra-`meta/`, qui existe indépendamment de ces liens historiques —
    l'étanchéité n'est donc plus la seule voie d'accès vers ces fiches
    depuis un contexte publié.
  - `doctrinal/index.md` (§IX) : lien `[[meta/sidy|Profil : Sidy]]`
    **retiré**, remplacé par un renvoi générique vers
    `[[meta/meta-index|meta-index]]` (le hub du domaine réservé lui-même
    porte déjà `[[meta/personnel/sidy|Sidy]]`, l.21 — aucun orphelinage
    introduit). Ce fichier n'étant pas append-only, la correction directe
    ne pose aucune tension avec Cmd 9/Cmd 10. `updated:` remonté à
    2026-08-09.
  - **Verdict de principe retenu pour le futur** : une entrée d'annales
    déjà publiée qui contrevient à §VI par un lien isolé n'est **pas**
    reprise après coup ; mais tout fichier non append-only du corps
    doctrinal (`index.md` notamment) qui contreviendrait de la même façon
    **est** corrigé sans délai, l'étanchéité y primant sur toute autre
    considération puisqu'aucune discipline d'immutabilité ne s'y oppose.
- **Vérification** : `python3 verifier-invariants.py --racine /root/wiki`
  → 0 erreur(s), 0 avertissement(s), avant et après les deux édits
  (`doctrinal/index.md`, `meta/meta-annales.md`). `carte-du-depot.py`
  régénéré, aucune orpheline nouvelle introduite.
- **Compréhension tirée** : un signalement de sens interdit sur un fichier
  append-only ne se résout pas comme sur un fichier ordinaire — la
  discipline d'immutabilité de Cmd 9/Cmd 10 prime sur §VI *a posteriori*,
  alors qu'elle ne le protège jamais *a priori* (rien n'empêchait de ne
  pas écrire ce lien en 2026-06-20). Le hub `meta-index.md`, en offrant un
  point d'entrée alternatif et conforme, absorbe la tension sans qu'il
  soit nécessaire de toucher au journal historique. Second enseignement :
  vérifier un signalement par grep direct avant de le trancher, plutôt que
  de faire confiance à sa reformulation dans une entrée antérieure — une
  erreur de recopie (`gout-sucre-priere`) avait survécu sans être
  requestionnée.
- **Liens** : [[meta/meta-index|meta-index]] ; [[meta/meta-annales|meta-annales]] ;
  entrée précédente (ouverture du hub, signalement initial, partiellement
  erronée sur `gout-sucre-priere`).
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Ouverture du hub `meta-index.md`/`meta-annales.md` — traitement des 66 orphelines de `meta/`, acceptation documentée des 14 restantes

- **Symptôme** : suite à l'entrée précédente (bug de résolution corrigé, 80
  orphelines réelles au comptage final), instruction explicite de Sidy : « Je
  t'autorise à traité toutes les fiches, même personnel ». Sur les 80, 66
  vivaient dans `meta/` (`personnel/`, `genealogie/`, `journal/`,
  `transmissions/`, `projet-unifie/` y compris `hermes-prompts/`) — matières
  couvertes par l'étanchéité §VI, non traitables par simple lien depuis un
  circuit.
- **Diagnostic** : blocage structurel — `meta/` n'a ni `index.md` ni
  `annales.md`, contrairement aux quatre circuits qui en ont chacun un ; il
  n'existait donc aucun hub interne légitime depuis lequel créer des liens
  vers ces 66 fiches. Créer des fichiers nommés `index.md`/`annales.md` dans
  `meta/` aurait fait lire le domaine comme un sixième circuit, ce que
  CLAUDE.md dément explicitement (« Domaine Réservé », pas un circuit).
- **Signalement séparé, à part** (Cmd 7, non traité par cette entrée) : 4
  fiches `meta/personnel/` (`bourdonnement-tempe`, `gout-sucre-priere`,
  `taekwondo-hansu`) et `meta/projet-unifie/briefing-claude-ai` reçoivent leur
  seul lien entrant depuis `doctrinal/annales.md` — sens neutre → sensible,
  interdit par §VI. Consigné ici comme signalement ouvert ; aucune action
  corrective (hors périmètre de l'autorisation donnée, qui porte sur le
  traitement des orphelines, pas sur cette violation de sens inverse).
  Verdict humain toujours attendu.
- **Résolution** : verdict Sidy — donner à `meta/` son propre hub, nommé avec
  le préfixe `meta-` pour écarter tout risque de confusion avec les
  `index.md`/`annales.md` des circuits (proposition initiale de Sidy :
  « meta/ gets it's own referenced link with the same exact names, index and
  annales as the others circuits exept it will bare the prefix » ; nommage
  exact tranché par question : `meta-index.md` / `meta-annales.md`).
  - `CLAUDE.md` amendé (§II arborescence, §VI Domaine Réservé, §X Cmd 9) pour
    documenter le hub et son statut distinct d'un circuit.
  - `verifier-invariants.py` adapté : `meta-annales.md` ajouté à
    `NOMS_ANNALES` (contrôles A0-A5 d'append-only) ; `meta-index.md` ajouté à
    `FICHIERS_EXEMPTS_C3` et à la détection `fichier_de_service` (exemption
    Sceau Recteur, `type: meta`).
  - `carte-du-depot.py` adapté : `meta/meta-index` et `meta/meta-annales`
    exclus du décompte des orphelines dans `rendre_liens()`, au même titre
    que tout `*/index` et `*/annales`.
  - `meta/meta-index.md` créé : hub recensant par sous-dossier
    (`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
    `projet-unifie/` y compris `hermes-prompts/`/`hermes-skills/`, fiches de
    premier niveau) l'ensemble des fiches du domaine, chacune avec un
    wikilink de la forme `meta/<chemin>` accompagné du titre exact, fidèle à
    son titre ou en-tête réel — aucun
    contenu des 66 fiches n'a été modifié, seul un lien entrant a été créé.
    Résout d'un coup l'orphelinage des 66 fiches `meta/`.
  - `meta/meta-annales.md` créé : squelette minimal, append-only, première
    entrée `[2026-08-09] ouverture` documentant la création du hub.
  - Les 14 fiches restant orphelines hors `meta/` (13 stubs `deprecated` de
    `atelier/projets/`, pointant déjà vers leur fiche canonique en `rd/`, +
    `doctrinal/discernement/_template.md`, gabarit jamais destiné à être lié)
    ne reçoivent **aucun** lien artificiel — acceptées par conception, même
    régime que les fichiers de service. Consigné explicitement pour ne pas
    laisser un chiffre non expliqué.
- **Vérification** : `verifier-invariants.py --racine /root/wiki` → 0
  erreur(s), 0 avertissement(s), avant et après chaque étape. Régénération de
  `meta/carte-du-depot.md` → orphelines réelles : 80 → **14**, toutes
  documentées ci-dessus, aucune résiduelle non expliquée.
- **Compréhension tirée** : un domaine « réservé » qui n'est pas un circuit a
  quand même besoin d'un mécanisme de maillage interne — sinon toute fiche
  qu'on y range est structurellement condamnée à l'isolement, indépendamment
  de son contenu. Le nommage préfixé (`meta-` plutôt que nu) permet de doter
  un domaine réservé d'un hub sans lui faire perdre son statut distinct d'un
  circuit — la distinction se lit dans le nom du fichier, pas seulement dans
  la prose de CLAUDE.md.
- **Liens** : `CLAUDE.md` §II/§VI/§X ; `verifier-invariants.py` ;
  `carte-du-depot.py` ; [[meta/meta-index|meta-index]] ;
  [[meta/meta-annales|meta-annales]] ; entrée précédente (bug de résolution).
- **Statut** : `resolu` — 66/66 orphelines `meta/` traitées ; `ouvert` pour le
  signalement séparé (sens interdit `doctrinal/annales.md → meta/personnel/`,
  verdict humain attendu).

---

## [2026-08-09] resolu | Bug de résolution des liens entrants dans carte-du-depot.py (89 orphelines annoncées, 81 réelles) + traitement du lot non sensible

- **Symptôme** : suite à la clôture de l'épisode H‍ermes (entrée précédente),
  instruction de traiter les 89 fiches sans lien entrant listées en §VI de
  `meta/carte-du-depot.md`. Avant tout traitement, vérification individuelle
  d'un échantillon des 89 : `meta/genealogie/2026-06-20_signature-kouyate` est
  citée dans la liste, alors que `meta/genealogie/2026-06-20_oiseau-serpent-jumeau.md`
  contient un wikilink pointant vers elle (`[[meta/2026-06-20_signature-kouyate]]`),
  et `verifier-invariants.py` ne signale aucun lien mort sur cette cible.
- **Diagnostic** : lecture du code de `rendre_liens()` dans `carte-du-depot.py`.
  Le script résout les wikilinks par correspondance exacte de chemin, avec un
  repli par nom court (`par_nom`) — mais ce repli n'agit que si le lien est
  écrit **sans aucun préfixe de répertoire**. Un lien écrit avec un préfixe de
  répertoire partiel mais devenu obsolète (ex. `[[meta/2026-06-20_signature-kouyate]]`,
  rédigé avant que la fiche soit rangée sous `meta/genealogie/`) n'est reconnu
  ni comme résolu ni comme mort : il est silencieusement ignoré, et sa cible
  réelle est comptée à tort comme sans lien entrant. Vérification systématique
  par script (résolution étendue au nom de fichier final, quel que soit le
  préfixe présent) : sur les 89 annoncées, **7 ont en réalité un lien entrant**
  (`atelier/etudes-de-cas/stones-throw`,
  `meta/genealogie/2026-06-20_oiseau-serpent-jumeau`,
  `meta/genealogie/2026-06-20_signature-kouyate`,
  `meta/personnel/2026-06-20_bourdonnement-tempe`,
  `meta/personnel/2026-06-20_gout-sucre-priere`,
  `meta/personnel/2026-06-20_taekwondo-hansu`,
  `meta/projet-unifie/briefing-claude-ai`). Total réel : **81** orphelines, pas
  89. Classification des 81 par lot :
  - 12 stubs `deprecated` (`atelier/projets/*`, Cmd 10) — terminus par design ;
  - 1 gabarit (`doctrinal/discernement/_template`) — non-cible par nature ;
  - 2 fiches `rd/` référencées seulement en prose par `atelier/rd/index.md`
    (`cahiers/registre-problemes`, `infrastructure/synchro-obsidian-working-copy-github`) —
    seul défaut structurel réellement corrigible sans toucher à un circuit
    sensible ;
  - 7 fiches `meta/` déjà `status: deprecated` ou notes opérationnelles closes —
    isolement cohérent avec leur statut, aucune action ;
  - reste (~59) : `meta/genealogie/`, `meta/personnel/`, `meta/journal/`,
    `meta/transmissions/karubi-*`, `meta/projet-unifie/*` (dont plusieurs sans
    frontmatter, qui recoupent l'anomalie déjà ouverte le 2026-08-08) — tous
    dans des matières couvertes par l'étanchéité §VI ou déjà signalées
    ailleurs ; aucun lien ajouté sans verdict Sidy au cas par cas.
- **Résolution** : lot des 2 fiches `rd/` traité — `atelier/rd/index.md`
  converti en wikilinks réels (`[[atelier/rd/cahiers/registre-problemes]]` et
  ajout de `[[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]]`
  dans la table des frontières, absente jusqu'ici même en prose).
  `verifier-invariants.py` → 0 erreur, 0 avertissement. `carte-du-depot.py`
  régénéré → 87 fiches sans lien entrant (89 → 87, conforme). Les lots
  sensibles (généalogie, personnel, journal, transmissions, projet-unifié)
  restent en l'état, en attente de verdict Sidy fiche par fiche ou lot par
  lot.

  **Complément (même jour)** : correctif appliqué à `carte-du-depot.py` sur
  autorisation explicite. Dans `rendre_liens()`, ajout d'un second repli de
  résolution : quand une cible de lien n'est ni un chemin exact ni un nom
  court sans préfixe, tentative de correspondance sur le seul nom de fichier
  final (`c.rsplit("/", 1)[-1]`), retenue si un unique candidat du dépôt y
  correspond — même logique que le repli `par_nom` existant, étendue aux
  préfixes de répertoire partiels/obsolètes. `carte-du-depot.py` régénéré →
  87 → **80** fiches sans lien entrant ; les 7 faux positifs identifiés
  n'apparaissent plus dans la liste. `verifier-invariants.py` → 0 erreur, 0
  avertissement (inchangé, le correctif ne touche que la carte dérivée,
  jamais les invariants structurels). Chiffre définitif retenu : **80**
  orphelines réelles.
- **Compréhension tirée** : le même piège que le self-report H‍ermes s'applique
  à un artefact du dépôt lui-même — un chiffre produit par un script n'est
  fiable qu'après lecture de son mécanisme de calcul, pas seulement de sa
  sortie. Avant tout traitement de masse sur un signalement chiffré (« N
  fiches orphelines », « N liens morts »), vérifier individuellement un
  échantillon contre le dépôt réel et, en cas d'écart, lire le code du script
  générateur plutôt que de corriger les fiches pour faire correspondre le
  chiffre. Second enseignement : sur un dépôt à étanchéité stricte (§VI),
  « traiter des orphelines » ne veut pas dire « ajouter des liens partout » —
  la majorité des orphelines réelles sont orphelines *par construction*
  (stubs terminaux, gabarits, circuits sensibles isolés à dessein) et
  n'appellent aucune action.
- **Liens** : `carte-du-depot.py` (fonction `rendre_liens()`, résolution
  `par_nom` + repli nom de fichier final) ; `meta/carte-du-depot.md`
  (régénéré 2026-08-09, §VI, 80 orphelines) ; `atelier/rd/index.md` (2
  wikilinks ajoutés) ; entrée précédente du présent registre (self-report
  H‍ermes) pour le fil de l'investigation ; anomalie frontmatter du
  2026-08-08 pour le recoupement `hermes-prompts/*`.
- **Statut** : `resolu` pour le lot C traité, le bug de script diagnostiqué
  et corrigé ; `ouvert` implicitement pour les lots sensibles restants (80
  fiches), en attente de verdict — suivi à réouvrir en entrée dédiée si Sidy
  tranche sur un de ces lots.

---

## [2026-08-09] resolu | Self-report H‍ermes Agent erroné sur le maillage wikilinks (317/403 annoncés vs 89/390 réels)

- **Symptôme** : constat visuel sur la Vue graphique Obsidian (iPad, 2026-08-09) —
  un large anneau de points quasi sans liens, dont cinq fiches-sources
  doctrinales identifiées nommément :
  `guenon-etats-multiples-ch13-hierarchies-spirituelles`,
  `guenon-symbolisme-croix-ch4-directions-espace`,
  `guenon-kundalini-yoga-etudes-hindouisme`,
  `ibn-arabi-de-la-mort-a-la-resurrection-gloton`, `sept-etendards-califat`.
  Interrogé côté serveur sur ce constat, H‍ermes Agent a répondu par un
  self-report : « 317 fiches sur 403 sans lien entrant », répartition par
  circuit (doctrinal 151, meta 95, atelier 44, label 12, hermeneutique 9),
  et une explication selon laquelle le protocole relierait les fiches par
  « références textuelles » plutôt que par wikilinks (double crochets).
- **Diagnostic** : vérification mécanique intégrale des deux affirmations.
  `verifier-invariants.py --racine /root/wiki` → 0 erreur, 0 avertissement.
  `carte-du-depot.py` → 390 fiches parcourues, **89** sans lien entrant (pas
  317). Aucun script du dépôt ne reproduit ni le total de 403 fiches valides
  (403 = compte brut de fichiers `.md`, avant exclusion de `raw/` et des
  fichiers sans frontmatter YAML — `CLAUDE.md`, `README.md`, plusieurs
  `hermes-prompts/*.md`, etc. ; 390 est le chiffre correct), ni la
  répartition par circuit annoncée. Vérification individuelle des 5 fiches
  citées comme motif : **aucune n'est orpheline**. Toutes ont
  `cross_links`/`sources` renseignés conformément au Sceau Recteur (§IV) et
  des liens entrants réels et multiples (`doctrinal/index.md`,
  `doctrinal/annales.md`, et jusqu'à 15 fichiers citants pour la fiche
  Ibn ʿArabī/Gloton). L'explication d'H‍ermes (maillage hors wikilinks) est donc
  réfutée par les faits sur le cas précis qui l'a motivée : le mécanisme
  `sources`/`cross_links` en wikilinks, tel que défini par le protocole,
  fonctionne correctement pour ces cinq fiches.
- **Résolution** : aucune correction de maillage nécessaire — il n'y avait
  pas de défaut réel sur les fiches à l'origine du constat. Le déficit
  mécanique véritable (89/390 fiches sans lien entrant) reste réel mais d'un
  ordre de grandeur très différent de l'annonce d'H‍ermes, concentré
  principalement dans `meta/personnel/`, `meta/projet-unifie/`,
  `meta/genealogie/`, `meta/transmissions/` et les stubs `deprecated` de la
  migration `rd/` (orphelinage volontaire, non anormal) — traitement séparé,
  hors objet de cette entrée.
- **Compréhension tirée** : un self-report d'agent conversationnel — même
  chiffré avec précision et accompagné d'une explication plausible et
  conforme en apparence à la lettre du protocole — n'est pas une source
  fiable sur l'état structurel du dépôt. Ici, l'agent a produit un chiffre
  erroné (317 au lieu de 89, plus de 3× l'écart), une répartition par
  circuit sans fondement, et une explication qui contredit le Sceau Recteur
  tel qu'écrit. Avant tout signalement fondé sur un constat visuel Obsidian
  ou un rapport d'agent, exécuter systématiquement `verifier-invariants.py`
  et `carte-du-depot.py`, et vérifier individuellement toute fiche citée
  nommément comme preuve — jamais de self-report en position de source.
- **Liens** : `meta/carte-du-depot.md` (généré 2026-08-09 03:48 UTC, §VI
  « Fiches sans lien entrant (89) », §VII statistiques) ;
  `doctrinal/sources/guenon-etats-multiples-ch13-hierarchies-spirituelles.md` ;
  `doctrinal/sources/guenon-symbolisme-croix-ch4-directions-espace.md` ;
  `doctrinal/sources/guenon-kundalini-yoga-etudes-hindouisme.md` ;
  `doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md` ;
  `doctrinal/sources/sept-etendards-califat.md`.
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Contenu du sas `_inbox/` poussé par erreur sur le dépôt

- **Symptôme** : le commit `d73cdb6` (intégration de la fiche synchro
  Obsidian) contient les fichiers `_inbox/karubi-mehdi.md` et
  `_inbox/image.jpeg`, ajoutés par un `git add -A` trop large.
- **Diagnostic** : faute d'opérateur — le sas `_inbox/` est par définition
  non versionné tant que l'intégration n'a pas eu lieu (cf. entrée
  [2026-08-09] ci-dessous, vault désynchronisé : « laissé non versionné — ne
  doit pas partir sur le dépôt sans passage par le circuit d'intégration »).
  `git add -A` à la racine ramasse tout, sas compris.
- **Résolution** : commit correctif immédiat `87ca442`
  (`git rm --cached` sur les deux fichiers + push). Les fichiers ne sont plus
  suivis ; l'historique du remote conserve toutefois le blob du commit fautif
  (dépôt privé — pas de réécriture d'historique sans verdict Sidy).
- **Compréhension tirée** : dans ce dépôt, ne jamais committer par
  `git add -A` depuis la racine ; ajouter nommément les fichiers intégrés
  (ou utiliser `git add -A -- <chemins>` hors `_inbox/`). Le sas est
  intouchable par Git tant que l'intégration n'est pas faite.
- **Liens** : commits `d73cdb6`, `87ca442` ; entrée ci-dessous
  (vault désynchronisé).
- **Statut** : `resolu`.

---

## [2026-08-09] resolu | Vault Obsidian (iPad) désynchronisé — 6 commits serveur jamais poussés

- **Symptôme** : le vault Obsidian sur l'iPad de Sidy n'est « plus du tout à
  jour » depuis un certain temps. Le vault = le dépôt wiki lui-même, consulté
  sur iPad via Obsidian en auto-pull depuis GitHub (`Sidyvision/wiki`,
  `CLAUDE.md` §postes : CONSULTATION).
- **Diagnostic** : aucun problème de configuration Obsidian côté serveur —
  l'auto-pull de l'iPad tire `origin/main`, or le serveur était en avance de
  6 commits non poussés (ouverture du pôle rd/, migration `projets/ → rd/`,
  arbitrage `album-personnel`, annales) plus 3 fichiers de travail non
  commités (registre des problèmes, thème natal corrigé, mise en regard
  roue/thème). La « connexion cassée » était simplement une chaîne de push
  interrompue côté serveur.
- **Résolution** : commit des 3 fichiers en attente puis `git push origin main`
  (7 commits au total). L'auto-pull de l'iPad récupérera l'état complet au
  prochain cycle. `_inbox/` (sas en attente d'intégration, contient des PDF
  bancaires) laissé non versionné — ne doit pas partir sur le dépôt sans
  passage par le circuit d'intégration.
- **Compréhension tirée** : un vault « cassé » peut n'être qu'un dépôt local en
  avance sur son remote. Avant d'incriminer l'outil de consultation (Obsidian,
  ses plugins, sa synchro), vérifier l'état git (`git status -sb`,
  `rev-list --left-right --count origin/main...HEAD`) : c'est le maillon serveur
  qui portait le retard.
- **Liens** : `CLAUDE.md` §postes (CONSULTATION = Obsidian iPad auto-pull) ;
  remote `git@github.com:Sidyvision/wiki.git`.
- **Statut** : `resolu`.

---

## [2026-08-08] resolu | Vision Hermes en 404 sur l'endpoint Qwen (auto-détection auxiliaire mal routée)

- **Symptôme** : l'outil `vision_analyze` échoue systématiquement avec
  `Error code: 404` ; mêmes échecs consignés pour les tâches auxiliaires
  `compression` et `title_generation` dans `~/.hermes/logs/agent.log` et
  `errors.log`. La conversation principale fonctionne normalement par ailleurs.
- **Diagnostic** : les tâches auxiliaires sont par défaut en `provider: auto`.
  L'auto-détection réécrit l'URL de base
  `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic` →
  `.../apps/v1` (règle générique pour les endpoints « anthropic-compatibles »),
  puis le SDK Anthropic ajoute `/v1/messages` : l'appel arrive sur
  `.../apps/v1/v1/messages`, qui n'existe pas. L'endpoint Qwen n'expose que la
  surface `anthropic_messages` sur `/apps/anthropic/v1/messages` (vérifié :
  le fil OpenAI `/apps/v1/chat/completions` renvoie lui aussi 404). Test
  discriminant : le même appel épinglé sur `custom:qwen` réussit (réponse
  correcte à l'analyse d'image), l'appel auto-détecté échoue en 404.
- **Résolution** : épinglage
  `auxiliary.{vision,compression,title_generation,web_extract}.provider: custom:qwen`
  via `hermes config set` sur le profil principal ET les 12 profils Discord
  (ar-music, visual-da, production, admin-legal, accounting, distribution,
  marketing, publication, studio, gardien, fanzine, commerce). Vérification en
  direct après coup : `vision_analyze` répond correctement (test carré rouge →
  « Red »).
- **Compréhension tirée** : quand le provider principal est un endpoint
  Anthropic-compatible qui n'expose QUE cette surface, l'auto-détection
  auxiliaire (`auto`) est trompeuse — elle présuppose que l'endpoint parle aussi
  OpenAI. Il faut épingler explicitement toutes les tâches auxiliaires sur le
  provider nommé. Un échec « vision » peut donc être un problème de routage
  auxiliaire, pas du modèle.
- **Liens** : `~/.hermes/config.yaml` (profil `default` + 12 profils) ;
  `~/.hermes/logs/agent.log` ; code Hermes `agent/auxiliary_client.py`
  (`_to_openai_base_url`, `resolve_vision_provider_client`) ;
  [[meta/projet-unifie/15-architecture-discord-hermes-2026-08-07]].
- **Statut** : `resolu`.

---

## [2026-08-08] resolu-partiel | 4 anomalies d'étanchéité `materiel → album-personnel` coupées

- **Symptôme** : 4 des 10 anomalies bloquantes du graphe (entrée ci-dessous) :
  `atelier/materiel/{neve-1073spx, studio-principal, tascam-model-12,
  technics-su-8080}.md` (neutre, rang 0) → `atelier/projets/album-personnel.md`
  (rang 1) — liens remontants, interdits (§VI).
- **Diagnostic** : liens historiques hérités de la création des fiches materiel
  (2026-06-20), antérieurs à la formalisation de l'étanchéité. Devenus sans
  objet légal après le déplacement d'`album-personnel` vers `label/` (rang 2) :
  le sens licite est label → materiel, porté par `liens_atelier` (§V.b) de la
  fiche canonique.
- **Résolution** : les 4 liens coupés le 2026-08-08 — frontmatter (`links`) et
  corps de texte — lors de l'exécution du verdict d'arbitrage. Aucune fiche
  supprimée ; l'information de contexte (« projet dans lequel cet appareil est
  utilisé ») subsiste côté label.
- **Compréhension tirée** : un arbitrage de circuit est l'occasion naturelle de
  purger les violations d'étanchéité qui pointaient vers la fiche arbitrée —
  le déplacement change le rang de la cible et rend caducs les liens entrants
  du neutre.
- **Liens** : entrée ci-dessous (10 anomalies) ; [[label/production/album-personnel]] ;
  [[atelier/projets/album-personnel]] (stub) ; `CLAUDE.md` §VI.
- **Statut** : `resolu` pour les 4 liens ; l'entrée « 10 anomalies » passe à
  6 anomalies restantes (4 doctrinal → v0_3 + 2 frontmatter).

---

## [2026-08-08] ouvert | `graphe-cartographie.json` jamais régénéré (bloqué par les anomalies du graphe)

- **Symptôme** : `generer-cartographie.py` refuse d'écrire
  `graphe-cartographie.json` en présence d'anomalie bloquante ; le JSON de
  cartographie est absent du dépôt (jamais régénéré depuis son introduction).
- **Diagnostic** : conséquence directe de l'entrée suivante — le générateur est
  strict par conception (une anomalie = échec). Tant que les 10 anomalies
  pré-existantes ne sont pas traitées, l'artefact dérivé ne peut pas être produit.
- **Résolution** : aucune pour l'instant — le fichier n'a jamais été tracké ; la
  migration `projets/ → rd/` n'est pas en cause (vérifié par comparaison avec la
  baseline HEAD).
- **Compréhension tirée** : un générateur strict bloque tous les artefacts dérivés
  dès qu'une anomalie pré-existe. Deux issues possibles : soit traiter les
  anomalies à la source, soit doter le script d'un mode tolérant qui écrit
  l'artefact en signalant les anomalies plutôt que d'échouer. À arbitrer (verdict
  Sidy).
- **Liens** : entrée suivante ; `Graphe/generer-cartographie.py` ;
  [[meta/projet-unifie/proposition-pole-rd-atelier-2026-08-08|proposition de pôle]].
- **Statut** : `ouvert`.

---

## [2026-08-08] ouvert | 10 anomalies bloquantes du graphe (8 étanchéité + 2 frontmatter), pré-existantes

- **Symptôme** : `generer-cartographie.py` remonte 10 anomalies :
  - 2 `frontmatter` — frontmatter absent (le fichier ne commence pas par `---`) :
    `doctrinal/sources/transcription-index-tilak-origine-polaire.md`,
    `doctrinal/sources/transcription-table-matieres-symboles-science-sacree.md` ;
  - 4 `étanchéité` — `atelier/materiel/*` (neutre) →
    `atelier/projets/album-personnel.md` (plus sensible) ;
  - 4 `étanchéité` — `doctrinal/sources/guenon-*` (neutre) →
    `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0_3.md`
    (plus sensible).
- **Diagnostic** : toutes pré-existantes à la migration `projets/ → rd/` — vérifié
  point par point contre un export `git archive` de HEAD (mêmes 10 anomalies avant
  et après). La migration n'en introduit aucune.
- **Résolution** : aucune pour l'instant. Les 4 liens `materiel → album-personnel`
  dépendent du verdict d'arbitrage `album-personnel` (`rd/` vs `label/`) ; les
  4 liens `doctrinal/sources → v0_3` sont un sens de lien interdit par §VI (le
  neutre ne pointe pas vers le plus sensible), à traiter fiche par fiche.
- **Compréhension tirée** : avant d'attribuer une régression à une opération,
  comparer contre la baseline (HEAD) — ici la comparaison a innocenté la migration
  et isolé un passif ancien. Le registre doit consigner les anomalies dès leur
  découverte, pas seulement celles qu'on introduit.
- **Liens** : `Graphe/generer-cartographie.py` ; arbitrage `album-personnel.md`
  (verdict Sidy rendu le 2026-08-08 : `label/`) ; `CLAUDE.md` §VI.
- **Statut** : `partiellement-resolu` — 4/10 levées le 2026-08-08 (liens
  `materiel → album-personnel` coupés, voir entrée ci-dessus) ; restent
  4 `étanchéité` doctrinal → v0_3 et 2 `frontmatter`.

---

## [2026-08-08] resolu | Lien mort `manvantara → v0_2` (version inexistante)

- **Symptôme** : `doctrinal/symboles/manvantara.md` pointait vers une version
  `v0_2` (underscore) de l'architecture de l'Instrument, inexistante dans le dépôt.
- **Diagnostic** : coquille de slug — la cible `v0_2` n'existe pas ; le lien a été
  repointé vers `v0.3` conformément aux annales de la migration.
- **Résolution** : lien repointé vers `v0.3` lors de la migration (repérage des
  liens entrants).
- **Compréhension tirée** : les slugs de versions sont proches (`v0.3` / `v0_3`)
  et faciles à confondre ; un lien mort de ce type est silencieux tant qu'un
  générateur ou une relecture ne le remonte pas. À terme, un contrôle des liens
  entrants (ou le manifeste) devrait signaler toute cible inexistante.
- **Liens** : `doctrinal/symboles/manvantara.md` ;
  `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md`.
- **Statut** : `resolu`.
