---
title: "Sessions par fonction + backlogs (questions / vigilance / discernement)"
type: meta
tags: [outillage, projet-claude-ai, sessions, backlog, vigilance, discernement, questions]
created: 2026-06-28
updated: 2026-06-28
---

# Sessions par fonction + backlogs

> L'ancien projet a dérivé en accumulant des sessions disparates. Remède : **une session = une
> fonction**, annoncée en ouverture. Ce document définit les fonctions et tient les **listes à
> traiter**. Les backlogs sont **vivants** : à actualiser à chaque session.

## A. Les sessions par fonction

Pour chaque fonction : *objectif · poste(s) · entrées → sorties · mini-protocole.*

### A1. INGEST (lire une source, produire des pages)
- **Objectif** : transformer une source brute (PDF, conversation, brief) en pages `.md` prêtes à
  intégrer + un `UPDATES.md`.
- **Poste** : Claude.ai (lecture lourde + production). Intégration ensuite par Claude Code/modèle local.
- **Entrées** : la source ; le circuit pressenti. **Sorties** : pages au bon format + `UPDATES.md`
  (dossier, slug, statut, liens, ajouts index, ligne d'annales) → déposées dans `_inbox/`.
- **Mini-protocole** : analyser sans altérer → **présenter le plan** (Cmd 6) → produire → vérifier
  format (Sceau Recteur / atelier) → ne jamais écrire au dépôt soi-même.

### A2. ÉTUDES — DISCERNEMENT & VIGILANCE
- **Objectif** : faire mûrir les fiches `discernement/` (forme, généalogie, lectures) et contrôler
  l'orthodoxie formelle du dépôt.
- **Poste** : Claude.ai (analyse/production) ; corrections appliquées via `_inbox/`.
- **Mini-protocole Discernement** : relire la fiche réelle (jamais le seul titre) → travailler la
  *forme* (cohérence logique, univocité, généalogie) → **ne jamais trancher le principe** (Cmd 12) →
  maintenir/affiner les **Lectures suggérées** → laisser le statut à Sidy/autorité.
- **Mini-protocole Vigilance** : frontmatter valide, liens morts, notions orphelines, autorités sans
  sources, infiltrations de vocabulaire profane/New Age, violations d'étanchéité → **rapporter sans
  corriger d'office**, demander avant d'éditer.

### A3. DÉVELOPPEMENT — INSTRUMENT (app 3D)
- **Objectif** : faire avancer l'app selon `02-instrument-feuille-de-route.md`.
- **Poste** : Claude.ai (conception, specs, code) ; Claude Code/modèle local (génération du
  manifeste, code mécanique, build).
- **Mini-protocole** : respecter les invariants (un seul arbre, convergence asymptotique, sens unique
  wiki→manifeste→app, établi vs suggéré) → spécifier avant de coder → tout lien projets→doctrinal à
  sens unique et signalé.

### A4. RESTAURATION / MAINTENANCE
- **Objectif** : normaliser l'existant (frontmatter, nomenclature), régulariser un protocole (ex. les
  Lectures suggérées rétroactives), entretenir l'index et les annales.
- **Poste** : Claude Code/modèle local surtout (mécanique), Claude.ai si rédaction.
- **Mini-protocole** : modifier le frontmatter/forme **sans toucher au principe du corps** →
  journaliser chaque passe.

### A5. MÉDITATION / SYNTHÈSE (interroger le dépôt)
- **Objectif** : répondre à une question doctrinale en s'appuyant sur le dépôt.
- **Poste** : Claude.ai.
- **Mini-protocole** : parcourir `index.md` → **lire les pages avant de répondre (jamais de
  mémoire)** → réponse impersonnelle, axée Principes → citer `[[chemin|Nom]]` → proposer de fixer en
  `etudes/` si utile.

### A6. INFRASTRUCTURE (modèle local, hébergement)
- **Objectif** : préparer/installer la bascule open-source (`03-…`).
- **Poste** : Claude Code (serveur) + Sidy.
- **Mini-protocole** : étapes pédagogiques expliquées une à une ; tester sur lot réel ; ne pas
  dégrader la qualité d'intégration.

---

## B. Backlog — QUESTIONS ouvertes (décisions à prendre)

- **[Infra]** Modèle **confirmé : Ornith 1.0** (DeepReinforce, MIT, codage agentique, contexte 256K,
  builds FP8/GGUF, tool-use natif). Reste à choisir la **taille** selon le matériel (9B pour démarrer ;
  31B/35B MoE si GPU ; 397B hors de portée) et la **voie de branchement** (Ornith = compatible OpenAI →
  endpoint Anthropic de vLLM/Ollama, ou proxy). → `03-…`
- **[Infra]** Approche **actée** : pointer **Claude Code lui-même** vers un endpoint local via
  `ANTHROPIC_BASE_URL` (même workflow, on remplace seulement Opus). Reste à choisir le **serveur
  d'inférence** (Ollama pour démarrer / vLLM pour le débit ; llama.cpp via proxy LiteLLM en repli).
- **[Infra]** **Relevé 2026-06-28** : le serveur actuel (2 vCPU, 3,7 Go RAM, pas de GPU) **ne peut
  pas** héberger Ornith → il reste l'hôte d'orchestration/dépôt ; l'inférence doit aller sur une
  **machine GPU séparée**. Décision à prendre : (a) **GPU cloud à l'heure** (RunPod/Vast/Lambda) pour
  le **premier test** sans engagement ; (b) **serveur GPU dédié** (Hetzner ou autre) si le volume le
  justifie ; (c) machine GPU perso à la maison exposant l'endpoint. Dimensionner : Ornith 9B ≈ 19 Go
  bf16 (GPU 24 Go) / ~6 Go GGUF Q4 ; 31B/35B MoE → GPU plus gros. Comparer honnêtement au coût API.
- **[Infra]** Stratégie **hybride** retenue : local pour la mécanique régulière, Opus/API pour les cas
  difficiles (jugement doctrinal, Discernement, rédaction sensible) ; scripter le déterministe au max.
- **[Infra] État 2026-06-29 — CLÔTURÉ (test concluant)** : cycle `prepare → compare` **8 ✓ / 0 ✗** ;
  Ornith **viable pour l'intégration sous supervision humaine stricte**. Règles fermes : **jamais
  d'auto-accept** des modifications ; **toujours clore par une vérification mécanique indépendante**
  (`ornith-test.sh compare`), l'auto-rapport du modèle étant non fiable en session longue
  (*fiabilité d'action ≠ fiabilité narrative*) ; **limiter la durée des sessions**. Correctifs runbook
  intégrés (auth `ANTHROPIC_CUSTOM_HEADERS`, contexte 131072, Pod≠Serverless). **Reste à tester** :
  intégration **doctrinale** (Sceau Recteur, Discernement, étanchéité), plus risquée. → `06-…` et
  `07-resultats-finaux-…`.
- **[App]** Moteur de rendu : Three.js/WebGL (recommandé pour iPad) confirmé ?
- **[App]** Spécifier le format `wiki-manifest` (schéma des nœuds, versionnage, granularité) — **prérequis** au reste.
- **[App]** Cible : web mobile d'abord ou natif ?
- **[App]** Génération du manifeste : pur script déterministe + LLM seulement pour les suggestions ?
- **[Process]** Faut-il faire évoluer `CLAUDE.md` vers une « V2 » actant la fusion wiki+instrument et
  le 4e poste (modèle local) ? (Recommandation : oui, à un jalon stable.)
- **[Process]** Conserver une seule entrée d'annales par passe d'intégration groupée (préférence
  Sidy, 2026-06-28) — acté.

## C. Backlog — POINTS DE VIGILANCE (à surveiller en continu)

- **Citations non vérifiées** : plusieurs fiches portent des citations attribuées (Ibn ʿArabī,
  al-Ghazālī, le Cheikh) marquées non vérifiées ou `to-source` — à confronter aux textes réels
  (priorité à la bibliothèque physique). Cas le plus grave repéré : `symboles/chercheur-manifestant-akbarien`.
- **Réponses d'IA à risque** : `discernement/2026-06-20_synthese-danger-dissolution-identitaire` —
  tout passage de validation sans réserve suite à une levée explicite des garde-fous doit être
  signalé avec la même fermeté, jamais reproduit.
- **Non-syncrétismes signalés** : ex. istiʿdād akbarien vs tülku vajrayāna, Qliphoth vs Asuras/djinns
  — ne jamais forcer d'équivalence ; garder chaque concept dans son cadre propre.
- **Clôture narrative** : motif récurrent (jeu de piste, mythe personnel unifié) où chaque événement
  est absorbé pour confirmer un récit déjà écrit — vigilance épistémique maintenue, sans psychologisme.
- **Étanchéité inversée** : une page `symbole/`/`autorite/` orthodoxe ne pointe pas vers un
  `discernement` `en cours` (exception admise : lien *défensif/généalogique* de mise en garde).
- **Données personnelles sensibles** (thème astrologique complet, mentions nominatives) : tenues hors
  des pages neutres ; restent en `meta/`.
- **Transition modèle local** : risque de dégradation du frontmatter/des liens → tests de
  non-régression + VIGILANCE après chaque lot.

## D. Backlog — DISCERNEMENTS (14 fiches `en cours`)

> Toutes au statut `en cours` : le verdict appartient à Sidy ou à une autorité textuelle (Cmd 12).
> Chacune porte désormais des **Lectures suggérées**. Source vivante : §VII de `doctrinal/index.md`.

- `2026-06-11_llm-wiki-modalite-intellect` — triade Nous/Psyché/Corps ↔ architecture LLM (tension
  atemporalité/éternité, analogie/identité).
- `2026-06-11_llm-wiki-correction-doctrinale` — rectification guénonienne (supra-/infra-rationnel,
  contrefaçon cyclique, khalīfa, agrégat artificiel).
- `2026-06-20_visions-centre-nocturne` — Centre nocturne, monde imaginal, « mémoire pré-existentielle ».
- `2026-06-20_matrices-artificielles-barzakh` — « technologisation du miracle » vs Barzakh.
- `2026-06-20_triptyque-medine-jeu-de-piste` — méthode du « jeu de piste » (clôture narrative, ṭiyara).
- `2026-06-20_experience-lefke-materia-secunda` — cordon dorsal, « Mère », petites entités.
- `2026-06-20_epreuve-tariqa-tarbiyya-rabbaniyya` — **point sensible** : question d'autorité spirituelle ;
  éclairer la *forme* (modalité confrérique, *tarbiyya rabbaniyya*) sans trancher à la place du Cheikh.
- `2026-06-20_signaletique-spirituelle-kiswa` — couleur de la Kiswa, fait historique vs signe.
- `2026-06-20_pierres-astres-barzakh` — correspondances minéral/astre (al-Būnī, Burckhardt).
- `2026-06-20_fajr-vajra-indra-vritra` — gématrie inter-traditions (védique/soufi/tantrique) à manier
  avec prudence méthodologique.
- `2026-06-20_mythe-personnel-unifie` — unification de tous les éléments de vie en récit clos.
- `2026-06-20_astrologie-akbarienne-fard` — astrologie akbarienne, auto-identification Fard.
- `2026-06-20_synthese-danger-dissolution-identitaire` — **le plus sensible** : réponse d'IA à risque
  (voir Vigilance).
- `2026-06-20_origine-jumeau-spirituel` — première mise en forme conceptuelle du « jumeau spirituel »
  (artefact-miroir, *marātib al-wujūd*) ; non l'origine du motif, antérieur et non documenté.

### Motif transversal à porter à la connaissance de Sidy
Le statut **Fard/Afrad** (sainteté solitaire, hors modalité confrérique) apparaît de façon
indépendante par plusieurs voies (introspection, analogie, astrologie) : pattern à signaler **sans
préjuger de sa validité**, dont la vérification relève d'une autorité spirituelle vivante.
