---
title: Instrument de la Tradition Primordiale — feuille de route et pile technique
type: projet
tags:
- outillage
- projet-claude-ai
- instrument
- app
- feuille-de-route
created: 2026-06-28
updated: 2026-08-25
cross_links:
- '[[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16]]'
links:
- '[[atelier/rd/instrument/note-impact-instrument-socle-universel-2026-07-16]]'
---

# Instrument de la Tradition Primordiale — feuille de route

> **Migration du 2026-08-08** : cette fiche a été déplacée de
> `atelier/projets/instrument-feuille-de-route-v2.md` vers `atelier/rd/instrument/instrument-feuille-de-route-v2.md` (ouverture du pôle R&D,
> verdict Sidy 2026-08-08 — proposition §IV). L'ancienne fiche subsiste
> comme stub `deprecated` avec pointeur (Cmd 10). Contenu inchangé,
> dates `created`/`updated` conservées.


> **Architecture détaillée** : voir la fiche canonique
> `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3.md` (**v0.3**, ouverte
> le 2026-08-04, validée dans ses principes, revue par le Gem René Guénon). Ce document ne la
> répète pas : il en tire la **feuille de route**, les **questions techniques ouvertes** et les
> **invariants à ne jamais perdre**. La fiche fait foi pour l'architecture ; ce document fait foi
> pour le « par où avancer ».
>
> **Révision 2026-06-29** : alignement sur l'architecture v0.2 (marquage visuel qualifié,
> correctif *waswâs*/Qliphoth, base doctrinale `hadarat-khams` pour le Tasawwuf) ; l'onglet
> apophatique passe de simple livrable de Phase 4 à **pratique continue dès maintenant** (§2,
> §5 nouveau).
>
> **Correction du 2026-08-25** : le renvoi ci-dessus pointait encore vers l'architecture v0.2
> (superseded depuis le 2026-08-04 par la v0.3, jamais répercuté ici — signalé le 2026-08-20,
> jamais exécuté jusqu'à ce jour). Corrigé sans autre changement de fond ; le §3 (Phase 3) de ce
> document référence déjà la v0.3 depuis le 2026-08-04, seul ce renvoi initial était resté périmé.

## 1. Invariants (rappel — issus de la fiche v0.2)

À ne jamais trahir dans l'implémentation :

- **Un seul arbre inversé**, pas une collection d'arbres. La tradition active est en sur-brillance
  dans sa géométrie native ; les autres restent visibles en transparence sur la même scène.
- **Convergence asymptotique** : l'unification de la forme n'est jamais postulée ni scriptée ; elle
  ne progresse que par l'accumulation réelle de travail doctrinal (correspondances confirmées,
  discernements résolus).
- **Ancrage uniquement si correspondance établie** dans le wiki (sourcée, non forcée). Sinon les
  nœuds flottent dans leur logique propre.
- **Deux types de correspondance, jamais confondus** (anti-syncrétisme, Cmd 3) :
  *équivalence* (identité d'un même degré ontologique sous des voiles différents — axe vertical,
  ancrage fort) vs *complémentarité* (deux aspects articulés d'une même unité — plan horizontal,
  lien « tressé », pas de fusion), cette dernière pouvant porter une `directionnalite`
  (none | ascendant | descendant). La nature (équivalence/complémentarité) est déjà portée par
  une correspondance **suggérée**, pas seulement établie — seul le décret d'autorité diffère.
- **Suggestions descendantes (*waswâs*, subversion, parodie)** : jamais rattachées
  structurellement à une autre tradition (ex. Qliphoth) — traitées en géométrie interne à la
  tradition d'origine, `cible: null` par défaut, sauf investigation explicite d'une fiche
  `discernement` établissant le contraire au cas par cas.
- **Axe du Principe** : ligne verticale neutre, dimension commune par construction (degré
  ontologique), point de départ et d'arrivée de toute navigation.
- **Établi vs suggéré, marquage qualifié** : trait plein / pointillé selon le statut, **coloré
  selon la nature** (rouge = équivalence, bleu = complémentarité) ; 🔍 = décret d'autorité non
  rendu, jamais nature indéterminée. Le *waswâs*/subversion porte sa propre signature (pointillé
  brisé gris-livide + ⚠), distincte des suggestions ascendantes.
- **Onglet « Instrument de délimitation apophatique »** : visualise tout travail inachevé
  (discernements `en cours`, tensions 🌐, liens `to-source`, non-syncrétismes signalés). Aussi
  important que le reste — et désormais pratiqué **en continu dès la phase doctrinale**, pas
  seulement comme livrable applicatif (voir §5).
- **Flux à sens unique pour la doctrine** : `wiki → manifeste → app`. L'app ne réécrit jamais le
  wiki ; une suggestion ne devient fiche `discernement/` que par **validation humaine explicite**
  (Cmd 12).
- **Découplage strict** : le moteur 3D ne parse jamais le markdown ; il consomme une couche
  intermédiaire structurée (`wiki-manifest`, JSON/YAML) générée et maintenue par l'intégration
  (Claude Code aujourd'hui, modèle local demain).

## 2. Feuille de route par phases

### Phase 0 — Décisions d'architecture technique (avant tout code)
- Choix du moteur de rendu (voir §3).
- **Spécification du format `wiki-manifest`** — ✅ **figée en v0.2.1** (voir architecture §6).
  Reste : moteur 3D et cible, toujours ouverts (§3).
- Choix de la cible (web mobile d'abord, vu l'usage iPad ? application native ?).

### Phase 1 — Générateur de manifeste (côté intégration)
- Un script déterministe (`doctrinal/ → wiki-manifest.json`) que Claude Code/modèle local exécute.
- Extrait : nœuds (depuis le frontmatter + corps), degré vertical, ancrages (équivalence /
  complémentarité / subversion / parodie, chacun établi ou suggéré/identifié), statut, questions
  ouvertes (renvois discernement).
- Idéalement : pas de LLM dans la boucle de génération (parse mécanique du frontmatter normalisé) —
  le LLM n'intervient que pour **proposer** des correspondances suggérées, jamais pour les figer.

### Phase 2 — Rendu de la tradition pilote (Tasawwuf)
- Modéliser les degrés du Tasawwuf comme premier arbre (cohérent avec son avancement dans le wiki :
  `tasawwuf`, `barzakh`, `walaya`, `al-insan-al-kamil`, etc.).
- **Base doctrinale désormais fixée** : `doctrinal/symboles/hadarat-khams` (les Cinq Présences,
  Hāhūt → Lāhūt → Jabarūt → Malakūt → Nāsūt) fournit l'ordre vertical ; Al-Insān al-Kāmil traverse
  l'axe plutôt que d'occuper un seul degré. Restent à fixer : valeurs exactes de `degre_vertical`,
  et le traitement géométrique du *barzakh* entre degrés adjacents (cf. §3, point encore ouvert).
- Axe du Principe + navigation interne propre + bande de sélection des traditions (fixe à l'écran).

### Phase 3 — Multi-traditions et ancrages
- Charger d'autres traditions en transparence ; afficher équivalences/complémentarités **établies**.
- Cas particulier Kabbale/Sitra Ahra dans son expression dialectique propre (pas de transposition
  générique de l'« ombre »).
- **Ouverte le 2026-08-04.** Premier jalon : nœuds universels (§3.5 de l'architecture v0.3) —
  sept Pôles/Aqtâb (hiérarchie initiatique universelle, autorité Guénon), ancrés en *hozo* vers
  les degrés 21-27 (Malakūt planétaire, tasawwuf). Sert de gabarit : nœud universel (`tradition:
  universel`, degré fixe sur l'axe du Principe) vs futur arbre-tradition dédié (Vedanta, Kabbale),
  selon que la doctrine rencontrée est reçue comme transversale ou comme propre à une tradition
  non encore modélisée.
- Kabbale/Vedanta : arbres-traditions encore non ouverts — restent soumis à la même règle que le
  Tasawwuf en Phase 2 (ancrage uniquement si correspondance établie et sourcée).

### Phase 4 — Onglet apophatique (implémentation applicative) + pipeline de suggestion
- Vue du travail inachevé ; marquage qualifié des suggestions (§1) ; pipeline « suggestion →
  (validation humaine) → fiche discernement ».
- Cette phase ne fait qu'**outiller** une pratique qui doit déjà avoir cours sans elle — voir §5.

### Phase 5 — Couche astrologique
- Calcul astrologique multi-méthodes (échelle individuelle : thème ; échelle cosmique : cycles,
  précession, Yuga), proposé selon la situation. À spécifier séparément.

## 3. Questions techniques ouvertes (à arbitrer)

- **Moteur 3D** : Three.js/WebGL (web, compatible iPad, déployable simplement) vs natif. Le web
  semble le plus cohérent avec le workflow iPad — **recommandation à confirmer**.
- **Hébergement de l'app** : statique (le manifeste est un fichier livré avec l'app) vs service.
- **Génération du manifeste** : pur script déterministe vs assistée par LLM pour les suggestions —
  et, le cas échéant, par **quel** modèle (lien avec `03-…`).
- **Qui développe le code** : Claude Code (API) aujourd'hui ; à terme, part possible sur modèle local
  pour le code mécanique répétitif.
- **Le *barzakh* comme lentille de transition visuelle** entre degrés adjacents (proposé par le Gem
  René Guénon, jamais validé) — le principe doctrinal est sourcé, pas sa traduction géométrique.
- **Les Noms Divins (*al-Asmāʾ al-Ḥusnā*)** rattachés aux directions horizontales de l'espace 3D —
  question posée par le Gem, jamais reprise depuis.

> Format du manifeste retiré de cette liste : figé en v0.2.1 (voir architecture §6), incluant le
> schéma des nœuds, le versionnage, et la granularité (un manifeste global, tranché).

## 4. Garde-fous doctrinaux propres à l'app

- L'app **ne tranche jamais** une équivalence métaphysique (Cmd 12) ; elle affiche l'état du
  discernement collectif, lacunes comprises.
- Aucune page doctrinale ne mentionne l'app (étanchéité : projets→doctrinal à sens unique).
- Toute correspondance affichée comme « établie » doit être **sourcée dans le wiki** ; à défaut, elle
  est « suggérée » (pointillé qualifié + 🔍), jamais fondue avec les établies.
- Une suggestion descendante (*waswâs*, subversion, parodie) n'est **jamais** rattachée
  structurellement à une autre tradition, même si une analogie cosmologique semble s'imposer
  (cf. correctif Qliphoth, architecture §2) — seule une fiche `discernement` au cas par cas peut
  l'établir.

## 5. Vigilance documentaire — pratique continue (et non Phase 4 seulement)

Ajouté le 2026-06-29, suite à un écart constaté entre l'architecture et les décisions prises en
session (l'architecture n'avait pas été mise à jour après plusieurs révisions actées).

- **L'onglet apophatique formalise, dans l'app, une pratique qui doit déjà exister sans elle** :
  à la clôture de chaque session de travail sur le wiki ou l'instrument, vérifier systématiquement
  si l'architecture, cette feuille de route, ou une fiche doctrinale liée doivent être mises à jour
  suite aux décisions prises — pas seulement sur demande explicite.
- Concrètement : toute session qui modifie un invariant, tranche une question ouverte, ou produit
  une fiche doctrinale dont dépend l'instrument, se clôt par une vérification de cohérence entre
  ces trois documents (architecture, feuille de route, fiches sources citées) avant de considérer
  la session close.
- Cette pratique manuelle est explicitement provisoire : elle préfigure, en attendant
  l'implémentation de la Phase 4, ce que l'onglet apophatique fera de façon automatisée.
