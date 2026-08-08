---
title: "Instrument de la Tradition Primordiale — feuille de route et pile technique"
type: meta
tags: [outillage, projet-claude-ai, instrument, app, feuille-de-route]
created: 2026-06-28
updated: 2026-08-07
---

# Instrument de la Tradition Primordiale — feuille de route

> **Architecture détaillée** : la fiche canonique est désormais
> `atelier/projets/instrument-tradition-primordiale-architecture-v0.2.md` (v0.2 développée ; la v0.1
> `atelier/projets/instrument-tradition-primordiale-architecture.md` reste conservée comme jalon
> historique). La **spécification géométrique de l'axe des 38 degrés** (dictée par le Gem René
> Guénon) est fixée dans `atelier/projets/spec-technique-axe-38-degres.md`. Ce document ne les
> répète pas : il en tire la **feuille de route**, les **questions ouvertes** et les **invariants**.
> Les fiches font foi pour l'architecture ; ce document fait foi pour le « par où avancer ».
>
> **Contexte au 2026-08-07** : en parallèle, les agents H‍ermes et le circuit Discord ont été
> déployés avec succès (voir fiches 13-14-15). L'Instrument lui-même reste en Phase 0-1 (spec
> format manifeste, pas encore de code généré). Cette feuille de route reste valable dans son
> cadre ; les deux chantiers (Instrument et H‍ermes/Discord) avancent indépendamment.

## 1. Invariants (rappel — issus de la fiche v0.1)

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
  (none | ascendant | descendant).
- **Axe du Principe** : ligne verticale neutre, dimension commune par construction (degré
  ontologique), point de départ et d'arrivée de toute navigation.
- **Établi vs suggéré** : trait plein (sourcé) vs pointillé + 🔍 (non tranché) — miroir du statut
  `speculatif` et du bloc Discernement.
- **Onglet « Instrument de délimitation apophatique »** : visualise tout travail inachevé
  (discernements `en cours`, tensions 🌐, liens `to-source`, non-syncrétismes signalés). Aussi
  important que le reste.
- **Flux à sens unique pour la doctrine** : `wiki → manifeste → app`. L'app ne réécrit jamais le
  wiki ; une suggestion ne devient fiche `discernement/` que par **validation humaine explicite**
  (Cmd 12).
- **Découplage strict** : le moteur 3D ne parse jamais le markdown ; il consomme une couche
  intermédiaire structurée (`wiki-manifest`, JSON/YAML) générée et maintenue par l'intégration
  (Claude Code aujourd'hui, modèle local demain).

## 2. Feuille de route par phases

### Phase 0 — Décisions d'architecture technique (avant tout code)
- Choix du moteur de rendu (voir §3).
- **Spécification du format `wiki-manifest`** (le contrat entre le dépôt et l'app) — livrable
  prioritaire, car il découple les deux chantiers et permet de les avancer en parallèle.
- Choix de la cible (web mobile d'abord, vu l'usage iPad ? application native ?).

### Phase 1 — Générateur de manifeste (côté intégration)
- Un script déterministe (`doctrinal/ → wiki-manifest.json`) que Claude Code/modèle local exécute.
- Extrait : nœuds (depuis le frontmatter + corps), degré vertical, ancrages (équivalence /
  complémentarité / suggérée), statut, questions ouvertes (renvois discernement).
- Idéalement : pas de LLM dans la boucle de génération (parse mécanique du frontmatter normalisé) —
  le LLM n'intervient que pour **proposer** des correspondances suggérées, jamais pour les figer.

### Phase 2 — Rendu de la tradition pilote (Tasawwuf)
- Modéliser les degrés du Tasawwuf comme premier arbre (cohérent avec son avancement dans le wiki :
  `tasawwuf`, `barzakh`, `walaya`, `al-insan-al-kamil`, etc.).
- Axe du Principe + navigation interne propre + bande de sélection des traditions (fixe à l'écran).

### Phase 3 — Multi-traditions et ancrages
- Charger d'autres traditions en transparence ; afficher équivalences/complémentarités **établies**.
- Cas particulier Kabbale/Sitra Ahra dans son expression dialectique propre (pas de transposition
  générique de l'« ombre »).

### Phase 4 — Onglet apophatique + pipeline de suggestion
- Vue du travail inachevé ; marquage 🔍 des suggestions ; pipeline « suggestion → (validation
  humaine) → fiche discernement ».

### Phase 5 — Couche astrologique
- Calcul astrologique multi-méthodes (échelle individuelle : thème ; échelle cosmique : cycles,
  précession, Yuga), proposé selon la situation. À spécifier séparément.
- **Premier ancrage établi (2026-07-01)** : la **convergence des 28** (fuçûç = lettres = degrés du
  *Nafas al-Raḥmān* = *Manāzil al-Qamar*, *Futūhāt* ch. 198) relie la Phase 2 (degrés ontologiques)
  à la Phase 5 (couche astrologique) — **correspondance établie** validée par le Gem, sourcée. Voir
  `doctrinal/symboles/table-28-degres-nafas-rahman`, `nafas-rahmani`, `manazil-al-qamar`, `hadarat-khams`.
- **Géométrie de l'axe des 38 degrés fixée** (spec technique) : distribution Hāhūt (1-10, vide
  invisible) → Lāhūt (11-14) → Jabarūt (15-18) → Barzakh supérieur (19-20, disques en rotation) →
  Malakūt planétaire (21-27) → Nāsūt (28-38, espacement exponentiel) ; boucle 38→11 permanente.
- **Question ouverte §8.2 (directions horizontales)** — à arbitrer par Sidy : Noms Divins abstraits
  vs quatre angles astrologiques AS/DS/MC/FC (Sec/Humide/Chaud/Froid) ; les deux pistes ne s'excluent
  pas. Source : `fin-des-temps-modernes-ilm-al-nujum-bases-mahdi-rouge` + schéma manuscrit Sidy.

## 3. Questions techniques ouvertes (à arbitrer)

- **Moteur 3D** : Three.js/WebGL (web, compatible iPad, déployable simplement) vs natif. Le web
  semble le plus cohérent avec le workflow iPad — **recommandation à confirmer**.
- **Format exact du manifeste** : schéma des nœuds (cf. esquisse YAML de la fiche v0.1), versionnage
  du schéma, granularité (un manifeste global vs par tradition).
- **Hébergement de l'app** : statique (le manifeste est un fichier livré avec l'app) vs service.
- **Génération du manifeste** : pur script déterministe vs assistée par LLM pour les suggestions —
  et, le cas échéant, par **quel** modèle (lien avec `03-…`).
- **Qui développe le code** : Claude Code (API) aujourd'hui ; à terme, part possible sur modèle local
  pour le code mécanique répétitif.

## 4. Garde-fous doctrinaux propres à l'app

- L'app **ne tranche jamais** une équivalence métaphysique (Cmd 12) ; elle affiche l'état du
  discernement collectif, lacunes comprises.
- Aucune page doctrinale ne mentionne l'app (étanchéité : projets→doctrinal à sens unique).
- Toute correspondance affichée comme « établie » doit être **sourcée dans le wiki** ; à défaut, elle
  est « suggérée » (pointillé + 🔍), jamais fondue avec les établies.
