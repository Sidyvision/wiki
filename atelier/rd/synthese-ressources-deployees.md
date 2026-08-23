---
title: Synthèse ressources déployées — soutien Sidy (2026-08-23)
type: meta
statut: en-cours
created: 2026-08-23
updated: 2026-08-23
sources: []
links:
- '[[atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes]]'
- '[[atelier/rd/plan-action-soutien-sidy]]'
---

# Synthèse ressources déployées — soutien Sidy (2026-08-23)

## État des lieux

### Ressources déployées

**Mémoire persistante Hermes (profil default)**
- ✓ `/root/.hermes/profiles/default/USER.md` : 3.9K (identité, spirituel, relations, concepts, préférences)
- ✓ `/root/.hermes/profiles/default/MEMORY.md` : 11.4K (projet wiki, R&D, Karūbī, infrastructure, leçons)
- ✓ Injection automatique dans chaque nouvelle session
- **Impact** : fin de l'amnésie systématique après 20+ sessions

**Crons Hermes**
- ✓ monitoring-infrastructure-quotidien (b7acb57e3d58) : quotidien 12:00 UTC, deliver discord:1536564394690084925
- ✓ veille-rd-hebdomadaire (aed2c7228c7f) : lundi 10:00 UTC, deliver discord:infrastructure
- ✓ investigation-doctrinale-gardien (431fcacadca2) : quotidien 12:30 UTC, deliver discord:1535804669300052039, profil gardien
  - Last run 2026-08-23T15:26:01 (ok)

**Scripts d'outillage (4 scripts actifs)**
- ✓ `verifier-invariants.py` (racine) : contrôles A0-A5 (append-only), B0-B1 (frontmatter), C3 (étanchéité)
- ✓ `Graphe/generer-cartographie.py` v1.1 : cartographie two-level (BLOQUANT vs AVERTISSEMENT)
- ✓ `atelier/rd/outillage/detecter-non-tracke.py` : fichiers non suivis git, classés par circuit
- ✓ `Graphe/carte-du-depot.py` : détection orphelines + résolution étendue (nom fichier final)

**Phase 3 veille infrastructure (exécutée 2026-08-23)**
- ✓ Script créé : `atelier/rd/infrastructure/scripts/veille-infrastructure-quotidien.sh`
- ✓ Testé avec succès (4 sections fonctionnelles)
- ✓ Cron créé : `veille-infrastructure-quotidien` (6bc182f45d2c)
  - Schedule : 0 12 * * * (12:00 UTC quotidien)
  - Deliver : discord:1536564394690084925 (#infrastructure)
  - Mode : no-agent (script stdout délivré directement)
  - Prochaine exécution : 2026-08-24 12:00 UTC
- ✓ Résultats test cohérents avec état connu du dépôt :
  - Invariants : 5 erreurs, 62 avertissements
  - Cartographie : 3 anomalies bloquantes (frontmatter)
  - Non trackés : 5 fichiers (dont script veille lui-même)
  - Empreinte serveur : RAM 1.4Gi/3.7Gi, Swap 1.2Gi/2.0Gi, CPU 0.54, Disk 63%, Uptime 13 semaines
- **Statut** : DÉPLOYÉ ET ACTIF

**Bureau TUI (10 tests passent)**
- ✓ 6 modules sous `atelier/rd/infrastructure/bureau/modules/` :
  - video_player, audio_player, reader, chat, instrument_status, hermes_status
- ✓ 3 services sous `atelier/rd/infrastructure/bureau/services/` :
  - ansi_render (demi-blocs), chat_server (asyncio websockets), audio_stream (HTTP streaming)
- ✓ Chat/audio bindés sur 127.0.0.1 (accès via SSH/Tailscale uniquement)
- ✓ Dépendances : Pillow, websockets, textual, pypdf

**Infrastructure Hetzner**
- ✓ 2 vCPU, 3.7GB RAM (1.4Gi utilisée, 1.2Gi swap)
- ✓ 12 profils Hermes (tous actifs) :
  - gardien, studio, ar-music, visual-da, production, admin-legal, accounting, distribution, publication, fanzine, commerce, librarian-archivist
- ✓ Omniroute (passerelle Discord↔Hermes) active
- ✓ SSH key rotation en place

**Outillage Karūbī**
- ✓ `meta/transmissions/ajouter-memoire-karubi.py` : insert §8/§9 sans LLM, refuse si zone scellée après point d'insertion
- ✓ `meta/transmissions/integrer-navette-karubi.py` : intégration mécanique navette _inbox/ — vérifie sceau, compare zones scellées, extrait §8/§9, archive, journalise
- ✓ `meta/transmissions/generer-karubi.py` : 3 commandes ajoutées (statut, diff, index)
- ✓ Amendements G0 validés Sidy (A, B, C) — commits 8d46d6a, 19d1f43, a03fbe7
- ✓ 5 instances Karūbī actives :
  - Mehdi Bouzouïda (Habib) — v2, hash 22782cf6...
  - Mikael Heaudebourg (Malik) — v1, hash f970f184...
  - Habiba-Nour Kouyaté (Jamal & Jamila) — v1, hash c6c55502...
  - Jean-Marc Bastareaud (Yahya) — v1, hash 041466d9...
  - Wendel Nazaire (Hassan) — v1, hash f5d808eb...

**Documentation R&D**
- ✓ Bilan R&D 2026-08-15 (pont inter-agents) : `atelier/rd/cahiers/bilan-2026-08-15-pont-agents.md`
- ✓ Registre des problèmes : `atelier/rd/cahiers/registre-problemes.md` (append-only)
- ✓ Spécification rôle G0 : `meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md` (brouillon kari-kumi)
- ✓ Incident mémoire persistante : `atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes.md`
- ✓ Synthèse ressources déployées : `atelier/rd/synthese-ressources-deployees.md`
- ✓ Plan action soutien Sidy : `atelier/rd/plan-action-soutien-sidy.md`
- ✓ Spécification SRS Hermes-native : `atelier/rd/outillage/spec-srs-hermes-native.md` (format, extraction, algorithme, plan implémentation)

### Angle mort C3 — Résolu

**Constat** : le contrôle C3 dans `verifier-invariants.py` gère déjà les liens `annales.md`/`index.md` → `meta/` via le contrôle **C4** (avertissements non bloquants).

**Code existant** (lignes 371-380) :
```python
# C4 — angle mort connu de l'exemption C3
elif exempt_c3 and tete == "meta" and circ is not None and circ != "meta":
    rap.avertir(chemin_rel, "C4",
                f"lien `{circ}` (neutre, fichier de service) → `meta/` "
                f"— sens interdit par §VI, hors périmètre bloquant de "
                f"l'exemption C3 — [[{brut}]]")
```

**Statut** : DÉJÀ TRAITÉ — aucun angle mort, avertissements C4 générés correctement.

### SRS Hermes-native — Spécification créée

**Fiche** : `atelier/rd/outillage/spec-srs-hermes-native.md`

**Format carte YAML** :
```yaml
- id: "cmd-01"
  question: "Quel est le commandement absolu numéro 1 ?"
  reponse: "Une session = une fonction."
  categorie: "commandement"
  source: "CLAUDE.md#cmd1"
  created: "2026-08-23"
  last_reviewed: null
  next_review: "2026-08-24"
  interval_days: 1
  ease_factor: 2.5
  repetitions: 0
  tags: ["fondamental", "session"]
```

**Mécanisme d'extraction** :
- Script `generer-cartes-protocole.py` lit CLAUDE.md
- Extraction : commandements (Cmd 1-13), interdits de liens, lexique sashimono, table Karūbī, vocabulaire technique
- Estimation : ~80-120 cartes

**Algorithme d'espacement** :
- SM-2 simplifié (facteur de facilité 2.5, intervalles 1j → 6j → n×ease_factor)
- Qualité réponse (0-5) ajuste ease_factor et interval_days

**Stratégie de révision** :
- Option A : cron quotidien 09:00 UTC (11:00 Paris) → rapport cartes à réviser
- Option B : commande interactive `hermes srs review`
- Option C : injection prompt (2-3 cartes par session)
- Recommandation : Option B + Option C en complément

**Plan d'implémentation** :
1. Phase 1 : écriture generer-cartes-protocole.py (1-2h)
2. Phase 2 : stockage srs-cards.yaml (30min)
3. Phase 3 : algorithme SM-2 (1h)
4. Phase 4 : interface commande interactive (2-3h)
5. Phase 5 : cron quotidien (30min)

**Estimation totale** : 5-7h d'implémentation, 5-10 min/session de révision

### Ressources manquantes

**Personnel**
- ✗ SRS Hermes-native (auto-génération cartes depuis CLAUDE.md)
  - Format carte : NON défini (question/réponse ? frontmatter ?)
  - Script extraction : NON créé
  - Mécanisme révision : NON défini (cron, commande, injection prompt ?)
  - Algorithme espacement : NON choisi (SM-2 simplifié ou aléatoire ?)
- ✗ Cron rappel pratique spirituelle (Dalail al-khayrat, wadhifa Naqshbandi)
- ✗ Suivi rêves/visions (arc Kaaba, double protecteur)
- ✗ Consolidation mémoire régulière (hebdomadaire ?)

**Professionnel**
- ✗ Extension prompt `hermes-prompts/09-studio-sound-engineer.md` (zodiacal Vierge + gouvernance Discord)
- ✗ Inscription crontab veille infrastructure (quotidien 12:00 UTC)
- ✗ Allowlist Discord #infrastructure pour profil studio
- ✗ Spec rôle G0 : verdict Sidy attendu (brouillon kari-kumi)
- ✗ verifier-invariants.py angle mort C3 (annales/index) : arbitrage Sidy attendu
- ✗ graphe-cartographie.json non régénéré (2 anomalies frontmatter)

**Technique**
- ✗ Isolation mémoire Hermes par sub-agent (BLOQUANT pour skill Karūbī-Hermes)
  - Problème : un sub-agent administrant Karūbī ne doit pas avoir accès mémoire Hermes principale
  - Statut : aucune config Hermes trouvée permettant toggle `memory_enabled` par sub-agent
  - Piste : investiguer doc Hermes (hermes-agent skill) ou code source

## Priorités

### Court terme (cette semaine)
1. **Inscription crontab veille infrastructure** : script créé et testé, reste à planifier (à valider avec Sidy)
2. **Corriger angle mort C3 verifier-invariants.py** : distinguer exemption totale (cibles neutres) vs avertissement (cible meta/)
3. **Définir format SRS Hermes-native** : structure carte, script extraction, mécanisme révision

### Moyen terme (ce mois)
4. **Implémenter SRS Hermes-native** : auto-génération cartes depuis CLAUDE.md, algorithme espacement
5. **Lever bloquant isolation mémoire** : investiguer doc/code Hermes
6. **Régénérer graphe-cartographie.json** : corriger 2 anomalies frontmatter
7. **Étendre prompt Studio** : zodiacal Vierge + gouvernance Discord

### Long terme (ce trimestre)
8. **Mettre en place suivi spirituel** : cron rappel pratique, suivi rêves/visions
9. **Consolidation mémoire régulière** : cron hebdomadaire mise à jour MEMORY.md
10. **Déployer skill Karūbī-Hermes** : une fois bloquant isolation mémoire levé

## Verdicts Sidy requis

- Inscription crontab veille infrastructure : quotidien 12:00 UTC ?
- Angle mort C3 : distinguer exemption vs avertissement ?
- SRS format : question/réponse ou frontmatter ?
- SRS algorithme : SM-2 simplifié ou aléatoire ?
- Suivi spirituel : cron rappel quotidien ?
- Skill Karūbī-Hermes : déployer une fois bloquant levé ?

## Leçons apprises

1. **La mémoire persistante ne se crée pas toute seule** : elle doit être peuplée explicitement après les premières sessions.
2. **Le contexte utilisateur est aussi important que le contexte projet** : sans USER.md, l'agent ne sait pas qui il sert.
3. **Les crons ne résolvent pas tout** : ils rapportent, mais ne consolident pas la mémoire sans intervention.
4. **Le diagnostic doit être instructif** : documenter problème, cause, résolution, leçons.
5. **Phase 3 veille était tranchée depuis le 2026-08-11** : il a fallu 12 jours pour créer le script. Leçon : exécuter dès que tout est tranché.

## Prochaines étapes

1. Valider avec Sidy inscription crontab veille infrastructure
2. Corriger angle mort C3 verifier-invariants.py
3. Définir format SRS Hermes-native
4. Investiguer bloquant isolation mémoire
5. Mettre à jour MEMORY.md avec cette synthèse
