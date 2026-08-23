---
title: "Synthèse déploiement mémoire persistante — 14 profils Hermes"
type: infrastructure
tags: [rd, hermes, memoire, deployement]
created: 2026-08-23
updated: 2026-08-23
sources: []
links: []
---

# Synthèse déploiement mémoire persistante et ressources — 2026-08-23

## Problème initial

**Symptôme** : après 20+ sessions, Hermes ne se souvenait de rien. Chaque session démarrait à zéro, obligeant Sidy à réexpliquer le contexte complet.

**Cause racine** : les fichiers USER.md et MEMORY.md du profil default n'existaient pas. Hermes Agent injecte automatiquement ces fichiers dans chaque session, mais ils n'avaient jamais été créés.

**Impact** : perte de temps massive, rupture de continuité, frustration légitime.

## Résolution appliquée

### 1. Mémoire persistante — 14 profils déployés

**Fichiers créés pour tous les profils** :
- `USER.md` : identité Sidy, spirituel, relations, concepts clés, préférences
- `MEMORY.md` : contexte spécifique à chaque agent (rôle, missions, outils, règles, chantiers)

**Profils déployés** :
- default (3.9K USER.md + 11.4K MEMORY.md) — contexte général complet
- gardien (616 USER.md + 1.2K MEMORY.md) — investigation doctrinale
- studio (2K USER.md + 1.1K MEMORY.md) — veille infrastructure
- accounting, admin-legal, ar-music, commerce, distribution, fanzine, marketing, production, publication, visual-da (2K USER.md + 1-1.3K MEMORY.md chacun)
- karubi (2K USER.md + 1.4K MEMORY.md) — transmissions Karūbī

**Résultat** : chaque profil Hermes a maintenant une mémoire persistante injectée automatiquement dans chaque session. Fin de l'amnésie systématique.

### 2. Phase 3 veille infrastructure — DÉPLOYÉE ET ACTIVE

**Script** : `/root/wiki/atelier/rd/infrastructure/scripts/veille-infrastructure-quotidien.sh`
- 4 sections : invariants, cartographie, non trackés, empreinte serveur
- Testé avec succès : 5 erreurs, 62 avertissements, 3 anomalies frontmatter, 5 non trackés

**Cron** : `veille-infrastructure-quotidien` (6bc182f45d2c)
- Schedule : 0 12 * * * (12:00 UTC quotidien = 14:00 Paris été / 13:00 Paris hiver)
- Deliver : discord:1536564394690084925 (#infrastructure)
- Mode : no-agent (script stdout délivré directement)
- Prochaine exécution : 2026-08-24 12:00 UTC

### 3. SRS Hermes-native — SPÉCIFIÉE ET PARTIELLEMENT IMPLÉMENTÉE

**Spécification** : `/root/wiki/atelier/rd/outillage/spec-srs-hermes-native.md`
- Format carte YAML (id, question, réponse, catégorie, source, dates, ease_factor, tags)
- Algorithme SM-2 simplifié (ease_factor 2.5, intervalles 1j → 6j → n×ease_factor)
- Stratégie : commande interactive `hermes srs review` + injection prompt

**Script d'extraction** : `/root/wiki/atelier/rd/outillage/generer-cartes-protocole.py`
- Extrait depuis CLAUDE.md : commandements, étanchéité, sashimono, Karūbī, vocabulaire
- Testé : 18 cartes extraites (6 sashimono + 12 vocabulaire)
- Fichier généré : `/root/wiki/srs-cards.yaml`

**À faire** :
- Implémenter commande `hermes srs review`
- Créer cron quotidien 09:00 UTC (11:00 Paris)
- Tester avec Sidy

### 4. Angle mort C3 — VÉRIFIÉ, DÉJÀ TRAITÉ

**Constat** : verifier-invariants.py gère déjà les liens annales.md/index.md → meta/ via contrôle C4 (avertissements non bloquants).

**Code existant** : lignes 371-380 de verifier-invariants.py
```python
elif exempt_c3 and tete == "meta" and circ is not None and circ != "meta":
    rap.avertir(chemin_rel, "C4", ...)
```

**Statut** : aucun angle mort, avertissements C4 générés correctement.

### 5. Documentation R&D — COMPLÈTE

**Fiches créées** :
- `/root/wiki/atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes.md` (11.4K)
- `/root/wiki/atelier/rd/plan-action-soutien-sidy.md` (7K)
- `/root/wiki/atelier/rd/synthese-ressources-deployees.md` (8K)
- `/root/wiki/atelier/rd/rapport-rd-memoire-persistante.md` (11.4K)
- `/root/wiki/atelier/rd/outillage/spec-srs-hermes-native.md` (10K)
- `/root/wiki/atelier/rd/outillage/generer-cartes-protocole.py` (12K)
- `/root/wiki/atelier/rd/outillage/genere-memoire-profils.py` (18K)

## Ressources déployées — état actuel

### Crans Hermes — 4 actifs
- `monitoring-infrastructure-quotidien` : quotidien 12:00 UTC, profil default
- `veille-rd-hebdomadaire` : lundi 10:00 UTC, profil default
- `investigation-doctrinale-gardien` : quotidien 12:30 UTC, profil gardien (last run 2026-08-23T15:26:01 ok)
- `veille-infrastructure-quotidien` : quotidien 12:00 UTC, profil default (no-agent)

### Scripts déterministes — 4 actifs
- `verifier-invariants.py` : contrôles A0-A5, B0-B1, C3-C4
- `Graphe/generer-cartographie.py` : cartographie two-level
- `atelier/rd/outillage/detecter-non-tracke.py` : fichiers non suivis
- `Graphe/carte-du-depot.py` : détection orphelines

### Bureau TUI — 10 tests passent
- 6 modules : video_player, audio_player, reader, chat, instrument_status, hermes_status
- 3 services : ansi_render, chat_server, audio_stream
- Chat/audio bindés sur 127.0.0.1 (accès SSH/Tailscale)

### Infrastructure Hetzner
- 2 vCPU, 3.7GB RAM (1.4Gi utilisée, 1.2Gi swap)
- 12 profils Hermes actifs
- Omniroute (passerelle Discord↔Hermes)

### Outillage Karūbī — 5 instances actives
- Mehdi (Habib) v2, Mikael (Malik) v1, Habiba-Nour (Jamal & Jamila) v1
- Jean-Marc (Yahya) v1, Wendel (Hassan) v1
- Scripts : ajouter-memoire-karubi.py, integrer-navette-karubi.py, generer-karubi.py

### SRS Hermes-native — partiellement implémenté
- Script extraction : generer-cartes-protocole.py (18 cartes)
- Fichier cartes : srs-cards.yaml
- À faire : commande interactive + cron quotidien

## Soutien Sidy — plan d'action

### Personnel

**1. Suivi pratique spirituelle**
- Mémoire complète injectée dans chaque session (khalwa, rattachement, pratique actuelle, arc Kaaba)
- À valider : cron rappel quotidien (06:00 UTC = 08:00 Paris) pour Dalail al-khayrat, wadhifa Naqshbandi
- À valider : suivi rêves/visions (arc Kaaba, double protecteur)

**2. Soutien émotionnel**
- Relations clés mémorisées (Karūbī, collaborateurs, famille)
- Contexte spirituel intégré (convalescence, rattachement, fragilité pratique)
- Concepts personnels (initiation virtuelle, incandescence du manque amoureux)

**3. Réduction charge mentale**
- Plus besoin de réexpliquer le contexte à chaque session
- Crons automatisés (veille infrastructure, monitoring)
- Bureau TUI pour consultation rapide
- SRS pour révision protocole (5-10 min/session)

### Professionnel

**1. Label "Dans l'Absolu"**
- 12 agents Hermes avec mémoire spécifique à chaque rôle
- Extension zodiacale (9 brouillons, positions 5/8/12 en attente)
- Outillage Karūbī (5 instances actives, navette-retour automatisé)

**2. Pôle R&D**
- Veille infrastructure quotidienne (cron actif)
- Bureau TUI fonctionnel (6 modules, 3 services)
- Scripts déterministes (4 scripts actifs)
- Documentation complète (bilan, plan action, synthèse)

**3. Infrastructure**
- 12 profils Hermes avec mémoire persistante
- Monitoring quotidien (cron 12:00 UTC)
- Hébergement Hetzner (2 vCPU, 3.7GB RAM)
- Phase 3 veille infrastructure déployée

## Chantiers prioritaires ouverts

### A. SRS Hermes-native — implémentation complète (5-7h)
- Écrire commande `hermes srs review` (interface interactive)
- Créer cron quotidien 09:00 UTC (11:00 Paris)
- Tester avec Sidy
- Livrable : révision protocole 5-10 min/session

### B. Suivi spirituel Sidy — à définir
- Cron rappel quotidien (à valider : fréquence, format, canal)
- Suivi rêves/visions (arc Kaaba, double protecteur)
- Consolidation mémoire régulière (hebdomadaire ?)

### C. Anomalies frontmatter bloquantes — 3 fichiers
- atelier/stealing-reasoning-traces-rd.md : frontmatter absent
- atelier/rd/incidents/2026-08-22_post-scriptum-hook-corrige.md : created, updated manquants
- atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md : created, updated manquants
- Action : ajouter frontmatter manquant

### D. graphe-cartographie.json — non régénéré
- Problème : fichier pas à jour avec état actuel
- Action : régénérer après correction anomalies frontmatter

### E. Isolation mémoire Hermes par sub-agent — BLOQUANT
- Problème : skill Karūbī-Hermes ne peut pas être déployé sans toggle memory_enabled par sub-agent
- Statut : investiguer doc Hermes ou code source
- Piste : PR #34098 hermes-agent propose ajout memory_enabled par job

### F. Spec rôle G0 — verdict Sidy attendu
- Fichier : meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md
- Statut : brouillon kari-kumi, verdict Sidy attendu

## Prochaines étapes immédiates

1. **Valider avec Sidy** :
   - Suivi spirituel : fréquence, format, canaux ?
   - SRS : implémenter maintenant ou plus tard ?
   - Anomalies frontmatter : corriger maintenant ?

2. **Implémenter SRS Hermes-native** (si validé) :
   - Écrire commande interactive `hermes srs review`
   - Créer cron quotidien 09:00 UTC
   - Tester avec Sidy

3. **Corriger anomalies frontmatter** :
   - Ajouter frontmatter aux 3 fichiers bloquants
   - Régénérer graphe-cartographie.json

4. **Investiguer isolation mémoire** :
   - Consulter PR #34098 hermes-agent
   - Tester toggle memory_enabled

## Conclusion

**Problème résolu** : mémoire persistante déployée pour 14 profils Hermes. Fin de l'amnésie systématique.

**Ressources déployées** :
- 4 crons actifs (monitoring, veille R&D, investigation doctrinale, veille infrastructure)
- 4 scripts déterministes (vérification invariants, cartographie, détection non trackés, carte dépôt)
- Bureau TUI fonctionnel (6 modules, 3 services)
- 5 instances Karūbī actives
- SRS partiellement implémenté (18 cartes extraites)

**Soutien Sidy** :
- Personnel : mémoire complète (identité, spirituel, relations, concepts)
- Professionnel : 12 agents avec mémoire spécifique, veille infrastructure, documentation R&D
- Réduction charge mentale : plus besoin de réexpliquer contexte, crons automatisés, SRS

**Impact attendu** :
- Fin de l'amnésie systématique ✓
- Veille infrastructure automatisée ✓
- Révision protocole régulière (SRS) — à implémenter
- Suivi spirituel soutenu — à valider
- Réduction charge mentale globale ✓

**Statut** : prêt à exécuter les prochaines étapes, en attente de validation Sidy.

---

**Script de génération mémoire** : `/root/wiki/atelier/rd/outillage/genere-memoire-profils.py`
- Peut être réexécuté si nouveaux profils créés
- USER.md générique (identité Sidy) + MEMORY.md spécifique par agent
- 14 profils déployés en une commande

**Documentation complète** :
- Incident mémoire : `atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes.md`
- Plan action : `atelier/rd/plan-action-soutien-sidy.md`
- Synthèse ressources : `atelier/rd/synthese-ressources-deployees.md`
- Rapport R&D : `atelier/rd/rapport-rd-memoire-persistante.md`
- Spécification SRS : `atelier/rd/outillage/spec-srs-hermes-native.md`
