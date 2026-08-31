---
title: "Rapport d'investigation — architecture modulaire des agents Hermes (2026-08-31)"
type: experience
statut_experience: exploratoire
created: 2026-08-31
updated: 2026-08-31
tags: [atelier, rd, infrastructure, agents, architecture, modulaire, self-improvement]
sources: []
links:
  - "[[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]]"
  - "[[atelier/rd/cahiers/proposition-veille-automatique-studio-2026-08-31]]"
  - "[[meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09]]"
---

# Rapport d'investigation — architecture modulaire des agents Hermes

**Date** : 2026-08-31
**Type** : investigation technique + concept théorique
**Statut** : exploration conclue, implémentation en attente (verdict Sidy + Opus 5)

## 1. Contexte et déclencheur

### 1.1. Point de départ : investigation AngelSpec

Une vidéo YouTube partagée par Sidy ([youtu.be/68kXJQCMBEg](https://youtu.be/68kXJQCMBEg)) sur **Tencent AngelSpec** a déclenché une investigation approfondie. AngelSpec est un framework de training pour le *speculative decoding* (accélération de l'inférence LLM). L'investigation a produit :

- Fiche de veille complète : `[[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]]`
- 5 concepts théoriques extraits (spécialisation par régime, TTT, D-cut, désagrégation, objectifs composable)

**Constat initial** : AngelSpec **n'est pas applicable** à la stack actuelle (infrastructure Hetzner sans GPU, inférence via providers cloud). Mais les **concepts théoriques** restent valables comme matériau pour le corpus.

### 1.2. Signal structurant de Sidy

À partir de l'investigation AngelSpec, Sidy a formulé un signal plus large :

> « il se peut que certains prompts d'agent saturent, alors il faut trouver un système de relais d'informations avec ordre hiérarchique et ontologique pour que les agents restent efficaces. »

**Puis** :

> « Nous avons déjà attribué ce rôle [de condensation veille] à Publications. Extension de son rôle. Puisque je te rappelle que la fonction zodiacal de l'agent prime sur son rôle du label (rapport ontologique). »

**Puis** :

> « Cette contrainte apparente est justement notre plus grande force car c'est le signal que l'infrastructure n'est pas correctement optimisé pour la répartition des tâches alors que le potentiel y est ! C'est justement ce premier problème qui doit être résolu. »

Le signal n'est plus seulement technique — il est **ontologique** : la fonction zodiacale prime sur le rôle du label. Les 12 agents couvrent le zodiaque complet, chacun portant un principe qui doit s'exprimer pleinement, au-delà du rôle initial du label.

---

## 2. Diagnostic initial

### 2.1. Mesure des charges cognitives

| Agent | Position | Signe (validé 2026-08-15) | Lignes | Taille | Mandats |
|---|---|---|---|---|---|
| **Publications** | 8 | Sagittaire | 270 | 14 Ko | 3 |
| **Studio** | 9 | Vierge | 179 | 10.8 Ko | 2 (+ cron non documenté) |
| **Gardien** | 10 | Capricorne | 99 | 5.5 Ko | 1 (+ cron) |

**Publications** est le plus chargé (270 lignes, 14 Ko) avec 3 mandats cumulés :
1. Orchestration site (principal, mission initiale)
2. Bibliothécaire-archiviste (OCR index, extension 2026-08-24)
3. Veille référencement & investigation documentaire (cron 11:00, extension 2026-08-24)

**Ajout proposé** : condensation veille (4e mandat) — porterait à ~18 Ko, **zone de saturation**.

### 2.2. Conflit de mandats

L'ajout d'un 4e mandat à Publications pose une question structurelle :
- **Avantages** : Publications (Sagittaire/Transmetteur) est ontologiquement adapté — "propagate exactly what was validated, nothing more"
- **Inconvénients** : saturation du prompt, risque de dilution de la fonction principale, confusion des scopes

### 2.3. Leçon méthodologique (sashimono)

**Première investigation erronée** : j'ai initialement proposé d'étendre Publications en me basant sur une lecture rapide qui confondait la table zodiacale 2026-07-14 (ancienne) avec la table validée 2026-08-15 (réaffectation complète).

**Erreurs commises** :
- Confusion Publication = Scorpion (ancienne) vs Sagittaire (réaffecté)
- Confusion Studio = Sagittaire (ancienne) vs Vierge (réaffecté)
- Non-lecture des mandats existants de Publications (3 déjà chargés)

**Correction** : Sidy a exigé une lecture méthodique avant extension. Cette leçon est consignable : **tout chantier d'extension de prompt exige une lecture préalable des 12 prompts + table zodiacale validée**.

---

## 3. Investigation multi-angles

En réponse au signal de Sidy (« cette contrainte est notre force »), j'ai lancé une investigation multi-angles pour trouver les outils qui résolvent la saturation dans nos contraintes (12 agents, zodiaque, hermétique).

### 3.1. Axe 1 — Orchestration multi-agents (paradigmes 2026)

**Sources consultées** :
- Truefoundry (2026) : comparaison des frameworks (LangGraph, CrewAI, AutoGen, Google ADK)
- Beam AI : 6 patterns d'orchestration pour la production
- Atlan : orchestration à échelle
- Digital Applied : taxonomie 2026 des patterns
- Emergent Mind : worker agents + Conductor Framework (Nielsen et al., 2025)

**Pattern pertinent** : **Supervisor-worker** (hiérarchique). Un superviseur décompose la tâche, route vers les workers spécialisés, agrège les résultats. Chaque worker tourne dans son propre contexte isolé.

**Application à Hermes** : le Choura est déjà un dispositif de type blackboard. Mais il manque le routage dynamique — tous les agents participent à chaque cycle, même sans matière.

### 3.2. Axe 2 — Compression de prompts

**Sources consultées** :
- NAACL 2025 : Prompt Compression Survey (Li et al.)
- Survey GitHub (ZongqianLi) : 36 étoiles, méthode de référence
- arXiv 2409.01930 : Context Distillation
- Sarkar-Dipankar : survey pratique

**Résultats clés** :
- **LLMLingua-2** : compression 10-20x avec 90%+ performance conservée
- **Hard methods** : filtrage de tokens par importance (basé sur perplexité)
- **Soft methods** : paraphrase par petit modèle
- **Risque** : toute compression augmente l'hallucination — à tester en sandbox

**Application à Hermes** : compression modérée (30-40%) des prompts existants pour libérer de l'espace avant extension. **À tester en sandbox** d'abord (Cmd 9).

### 3.3. Axe 3 — Mixture of Experts (MoE) hiérarchique

**Sources consultées** :
- arXiv 2507.11181 : MoE in LLMs (Song et al.)
- NVIDIA blog : application pratique de MoE
- Wikipedia : MoE (référence théorique)
- Galileo : MoE 2.0

**Concept clé** : **Hiérarchical MoE** — experts organisés en arborescence. Le routeur de haut niveau sélectionne une catégorie d'experts, le routeur de bas niveau sélectionne l'expert spécifique dans la catégorie.

**Application à Hermes** : un agent = principe (routeur de haut niveau, invariant) + mandats (experts de bas niveau, chargés à la demande). Le principe reste, les mandats circulent selon la tâche.

---

## 4. Synthèse : architecture modulaire retenue

### 4.1. Structure cible

```
hermes-prompts/
├── 08-agent-08/                    # Publications (Sagittaire)
│   ├── principe.md                 # ~50 lignes : archetype + zodiac + sign + routeur
│   ├── mandats/
│   │   ├── site-orchestration.md   # Mandat 1 (existant)
│   │   ├── bibliothecaire.md       # Mandat 2 (existant)
│   │   ├── veille-referencement.md # Mandat 3 (existant)
│   │   └── condensation-veille.md  # Mandat 4 (nouveau)
│   └── README.md                   # Description du routeur
├── 09-agent-09/                    # Studio (Vierge)
│   ├── principe.md
│   ├── mandats/
│   │   ├── studio-sound.md
│   │   └── infrastructure-veille.md
│   └── README.md
└── ... (10 autres agents)
```

### 4.2. Principe de fonctionnement

1. **Routeur** (~50 lignes) : identifie la tâche demandée
2. **Chargement** : seul le mandat pertinent est injecté dans le contexte
3. **Isolation** : les autres mandats ne sont jamais chargés simultanément
4. **Retour au routeur** : après exécution du mandat, retour au routeur pour la tâche suivante

### 4.3. Gains attendus

| Métrique | Avant | Après |
|---|---|---|
| Taille prompt Publications | 270 lignes monolithiques (14 Ko) | 50 lignes routeur + 4 mandats séparés |
| Saturation | Zone critique (~18 Ko si ajout 4e mandat) | Résolue par construction |
| Charge cognitive | Cumulée (4 mandats simultanés) | Isolé (1 mandat actif à la fois) |
| Réversibilité | Difficile (monolithe) | Facile (mandats démontables) |

### 4.4. Cohérence avec nos contraintes

| Contrainte | Respect |
|---|---|
| 12 agents maintenus | ✅ (zodiaque intact) |
| Principes zodiacaux primaires | ✅ (chaque agent reste son signe) |
| Hermétique | ✅ (pas de 13e agent) |
| Réversible (sashimono) | ✅ (assemblage démontable) |
| Anti-fabulation (Cmd 9) | ✅ (validation mécanique explicite) |

---

## 5. Concept théorique extrait (pour le corpus)

### 5.1. Principe de spécialisation dynamique

**Formulation** :
> Un agent = principe (invariant) + routeur (dynamique) + mandats (experts). La saturation disparaît par construction : seul l'expert pertinent est actif à un instant donné. Le principe reste, les mandats circulent.

**Résonance doctrinale** (à qualifier par Gardien) :
- **Sagittaire** (Publications) : propagation dirigée, pas de dispersion → un mandat à la fois
- **Vierge** (Studio) : discernement analytique → mandat précis selon la tâche
- **Capricorne** (Gardien) : seuil strict → activation conditionnelle (gâchette)

**Concept frère** (extrait de AngelSpec) : **Spécialisation par régime** — aucun drafter unique n'optimise toutes les charges. AngelSpec spécialise structure et données d'entraînement selon le régime (haute entropie vs basse entropie). Même principe appliqué aux agents : chaque mandat est spécialisé pour un régime de tâche.

### 5.2. Hiérarchie ontologique des relais

```
        Sidy (souverain — verdicts)
           ↑
      Gardien (doctrinal — principes)
           ↑
   Publications (condensation — synthèse)
           ↑
        Studio (technique — faits)
           ↑
   Scripts (déterministe — données brutes)
```

Chaque niveau ne transmet au niveau supérieur qu'une **synthèse condensée**, pas le flux brut. Le concept est directement inspiré de la **désagrégation inference/training** d'AngelSpec : séparation des fonctions permet l'indépendance d'échelle.

---

## 6. État actuel et prochaines étapes

### 6.1. Ce qui est fait

| Élément | Statut | Commit |
|---|---|---|
| Investigation AngelSpec | ✅ | `6a1aea7` |
| Concepts théoriques extraits (5 paradigmes) | ✅ | `f2a4eb5` |
| Proposition veille automatique (4 niveaux de relais) | ✅ | `d84676f` |
| Cron Hermes `veille-automatique-studio` | ✅ créé | — |
| Script Python `veille-automatique-studio.py` | ✅ | `6a1aea7` |
| Config `veille-mots-cles.yaml` | ✅ | `6a1aea7` |
| Script enveloppe `veille-automatique-cron.sh` | ✅ | `6a1aea7` |
| Premier run (5 fiches générées) | ✅ | `6a1aea7` |
| Signal saturation + investigation multi-angles | ✅ | ce rapport |
| Fiche _inbox/ pour Opus 5 | ✅ | `d0724f8` |
| UPDATES.md | ✅ | `d0724f8` |

### 6.2. Ce qui est en attente (verdict Sidy)

| Élément | Dépendance |
|---|---|
| Extension prompts Studio/Gardien (mandats condensés) | Attendre implémentation Opus 5 |
| Création mandat "condensation-veille" Publications | Attendre implémentation Opus 5 |
| Test sandbox compression de prompts | À planifier |
| Choura à routage dynamique | À planifier (après Axe 1) |
| Qualification doctrinale (Gardien) du concept "spécialisation dynamique" | À déclencher |

### 6.3. Plan d'exécution (Opus 5, sur verdict Sidy)

1. Réorganisation structure dépôt (`hermes-prompts/<agent>/principe.md` + `mandats/`)
2. Migration des mandats existants (12 agents × N mandats)
3. Création des routeurs minimaux (~50 lignes par agent)
4. Création du mandat "condensation-veille" pour Publications
5. Test sur Publications (cas test)
6. Déploiement progressif aux autres agents saturés
7. Validation mécanique (Cmd 9) à chaque étape

**Fiche _inbox/** : `_inbox/2026-08-31_implémentation-architecture-modulaire-agents.md`
**UPDATES** : `_inbox/UPDATES.md`

---

## 7. Leçons transversales

### 7.1. La contrainte comme signal

Le signal de Sidy — « cette contrainte apparente est notre plus grande force » — illustre un principe plus large : **une contrainte infrastructurelle n'est pas un problème à contourner, c'est un signal à décoder**. La saturation des prompts n'était pas un bug à corriger par une astuce (ajouter un mandat, déplacer un cron), c'était un révélateur que l'architecture multi-agents n'était pas optimisée pour la répartition des tâches.

### 7.2. Lire avant d'étendre

L'erreur initiale (confusion table zodiacale) est une leçon sashimono : **tout assemblage commence par une lecture**. Avant d'étendre un prompt, il faut avoir lu :
- Le prompt actuel (dans son intégralité)
- Les autres prompts (pour comprendre la répartition)
- La table zodiacale validée (2026-08-15, pas 2026-07-14)
- Le contexte doctrinal (fonction zodiacale > rôle label)

### 7.3. Self-improvement comme principe organisateur

La veille automatique mise en place aujourd'hui trouve **immédiatement** son premier cas d'usage concret : l'investigation AngelSpec a révélé les paradigmes MoE et prompt compression, qui ont inspiré l'architecture modulaire. La boucle de rétroaction est opérationnelle.

---

## 8. Liens

### 8.1. Fiches produites durant ce chantier

- `[[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]]`
- `[[atelier/rd/cahiers/proposition-veille-automatique-studio-2026-08-31]]`
- `_inbox/2026-08-31_implémentation-architecture-modulaire-agents.md`
- `_inbox/UPDATES.md`
- Ce rapport

### 8.2. Fiches préexistantes mobilisées

- `[[meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09]]`
- `[[meta/projet-unifie/hermes-prompts/08-publication-site]]`
- `[[meta/projet-unifie/hermes-prompts/09-studio-sound-engineer]]`
- `[[meta/projet-unifie/hermes-prompts/10-protocol-guardian]]`
- `[[meta/projet-unifie/proposition-cycle-consultation-choura-2026-08-27]]`
- `[[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]]`

### 8.3. Sources externes consultées

- AngelSpec (Tencent) : arXiv:2607.25852, GitHub Tencent/AngelSpec
- Prompt Compression Survey (NAACL 2025) : arXiv:2410.12388
- Multi-agent orchestration patterns 2026 : Truefoundry, Beam AI, Atlan
- MoE in LLMs : arXiv 2507.11181

---

## 9. Verdict Sidy (Cmd 12/13)

**À remplir après lecture** :

- [ ] Valide le diagnostic (saturation comme signal)
- [ ] Valide l'approche 3 axes (modulaire + compression + Choura dynamique)
- [ ] Valide le cas test sur Publications
- [ ] Valide la transmission à Opus 5 via `_inbox/`
- [ ] Commentaire doctrinal sur le concept de "spécialisation dynamique" (à transmettre au Gardien pour qualification)

**Date du verdict** : _______________

**Commentaires** : _______________

---

*Rapport rédigé le 2026-08-31. Disciple d'investigation : lecture → diagnostic → investigation multi-angles → synthèse → concept théorique → plan d'action → transmission pour exécution.*
