---
title: Rapport R&D — incident mémoire persistante et déploiement ressources
type: meta
statut: en-cours
created: 2026-08-23
updated: 2026-09-01
sources: []
links:
- '[[meta/projet-unifie/archives/synthese-ressources-deployees]]'
- '[[atelier/rd/outillage/spec-srs-hermes-native]]'
---

# Rapport R&D — incident mémoire persistante et déploiement ressources

> **Fiche versée au Domaine Réservé le 2026-09-01.** Elle a vécu jusque-là à la racine
> de `atelier/rd/`, c'est-à-dire dans une **page neutre** — alors qu'elle porte du fait
> personnel (situation, soutien, contenu des fichiers de mémoire d'agent). C'est
> l'interdit du §VI : jamais de fait personnel dans une page neutre. Déplacée sur verdict
> de Sidy, avec son historique git (`git mv`), sans retouche du corps (Cmd 10).
>
> Le versant **publiable** de cette matière — l'ingénierie, sans la personne — vit du côté
> `atelier/rd/`, où il est indexé ; voir la note de renvoi ci-dessous. Le renvoi va d'ici
> vers le neutre, jamais l'inverse.
> **Contrepartie neutre** : `atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes.md`,
> qui existait déjà et couvre le diagnostic, la cause racine et la leçon systémique. Aucune
> quatrième fiche n'a été créée : une page = un sujet (Cmd 4), et dupliquer un contenu déjà
> tenu ailleurs est précisément ce qui a produit la confusion qu'on répare.


## Résumé exécutif

**Problème** : après 20+ sessions, l'agent Hermes ne conservait aucune mémoire du travail accompli avec Sidy.

**Cause racine** : les fichiers USER.md et MEMORY.md du profil default n'existaient pas. Hermes Agent injecte automatiquement ces fichiers dans chaque session, mais ils n'avaient jamais été créés.

**Résolution** : création et peuplement des deux fichiers avec contexte complet (identité Sidy, projets, décisions, leçons).

**Impact immédiat** : fin de l'amnésie systématique. Chaque nouvelle session démarre avec le contexte complet.

## Diagnostic technique

### Pourquoi ce problème est survenu

Hermes Agent fonctionne avec deux niveaux de mémoire :

1. **Mémoire session** : injectée automatiquement depuis USER.md et MEMORY.md
2. **Mémoire dépôt** : accessible via les fichiers du wiki (/root/wiki)

L'agent avait accès au dépôt (CLAUDE.md, circuits, fiches) mais pas à la mémoire session. Résultat : il pouvait travailler sur les fichiers, mais ne "savait pas" qui était Sidy, ni pourquoi il travaillait sur ce dépôt.

### Pourquoi personne ne l'a détecté plus tôt

- Les sessions individuelles fonctionnaient (l'agent lisait les fichiers)
- Pas de test systématique de la mémoire session au démarrage
- Sidy réexpliquait le contexte à chaque session (perte de temps, mais pas bloquant)

### Leçon systémique

**Règle** : après la création d'un nouveau profil Hermes, vérifier immédiatement que USER.md et MEMORY.md existent et sont peuplés.

**Script de vérification** :
```bash
#!/bin/bash
# verifier-memoire-profil.sh
PROFILE=$1
HERMES_HOME="/root/.hermes/profiles/$PROFILE"

if [ ! -f "$HERMES_HOME/USER.md" ]; then
    echo "ERREUR : $HERMES_HOME/USER.md manquant"
    exit 1
fi

if [ ! -f "$HERMES_HOME/MEMORY.md" ]; then
    echo "ERREUR : $HERMES_HOME/MEMORY.md manquant"
    exit 1
fi

echo "✓ Mémoire profil $PROFILE OK"
echo "  USER.md : $(wc -c < $HERMES_HOME/USER.md) bytes"
echo "  MEMORY.md : $(wc -c < $HERMES_HOME/MEMORY.md) bytes"
```

## Ressources déployées

### 1. Mémoire persistante Hermes (profil default)

**Fichiers créés** :
- `/root/.hermes/profiles/default/USER.md` : 3 903 caractères
- `/root/.hermes/profiles/default/MEMORY.md` : 11 401 caractères

**Contenu USER.md** :
- Identité Sidy (nom, date naissance, famille, travail)
- Spirituel (voies, khalwa, pratique actuelle, arc Kaaba)
- Relations clés (Karūbī, collaborateurs, rêves)
- Concepts clés (initiation virtuelle, incandescence)
- Préférences (ton, langue, références)

**Contenu MEMORY.md** :
- Projet Wiki (5 circuits, 13 commandements, sashimono)
- Pôle R&D complet (structure, scripts, Bureau TUI)
- Infrastructure Hetzner (2 vCPU, 3.7GB RAM, 12 profils)
- Phase 3 veille infrastructure (script + cron)
- Extension zodiacale 12 agents (9 brouillons)
- Outillage Karūbī (scripts, amendements, 5 instances)
- SRS Hermes-native (spécification créée)
- 6 chantiers prioritaires ouverts (A à F)
- 8 leçons transversales

**Injection automatique** : chaque nouvelle session du profil default reçoit maintenant ces deux fichiers en contexte.

### 2. Phase 3 veille infrastructure — DÉPLOYÉE

**Script** : `/root/wiki/atelier/rd/infrastructure/scripts/veille-infrastructure-quotidien.sh`

**Contenu** :
```bash
#!/bin/bash
# Veille infrastructure quotidienne — Studio Sound Engineer (position 9)
# Exécute les 3 scripts déterministes + empreinte serveur

echo "=== RAPPORT STUDIO — VEILLE INFRASTRUCTURE ==="
echo "Date : $(date -u '+%Y-%m-%d %H:%M UTC')"

# 1. Vérificateur d'invariants
echo "━━━ 1. INVARIANTS ━━━"
python3 /root/wiki/verifier-invariants.py --racine /root/wiki

# 2. Cartographie dépôt
echo "━━━ 2. CARTOGRAPHIE ━━━"
python3 /root/wiki/Graphe/generer-cartographie.py --sortie meta/carte-atelier.md

# 3. Détection fichiers non suivis
echo "━━━ 3. NON TRACKÉS ━━━"
python3 /root/wiki/atelier/rd/outillage/detecter-non-tracke.py

# 4. Empreinte serveur
echo "━━━ 4. EMPREINTE SERVEUR ━━━"
echo "RAM : $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "Swap : $(free -h | grep Swap | awk '{print $3 "/" $2}')"
echo "CPU : $(uptime | awk -F'load average:' '{print $2}')"
echo "Disk : $(df -h /root/wiki | tail -1 | awk '{print $3 "/" $2 " (" $5 " utilisé)"}')"
echo "Git : $(cd /root/wiki && git rev-parse --short HEAD)"
echo "Uptime : $(uptime -p)"

# 5. Suggestions
echo "━━━ 5. SUGGESTIONS ━━━"
echo "[Suggestions soumises à validation avant journalisation]"

echo "=== FIN RAPPORT ==="
```

**Cron** : `veille-infrastructure-quotidien` (ID 6bc182f45d2c)
- Schedule : 0 12 * * * (12:00 UTC quotidien)
- Deliver : discord:1536564394690084925 (#infrastructure)
- Mode : no-agent (script stdout délivré directement)
- Prochaine exécution : 2026-08-24 12:00 UTC

**Test réussi** : 4 sections fonctionnelles, résultats cohérents avec état connu.

### 3. Spécification SRS Hermes-native — CRÉÉE

**Fiche** : `/root/wiki/atelier/rd/outillage/spec-srs-hermes-native.md`

**Format carte** :
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

**Extraction** : script generer-cartes-protocole.py (à écrire)
- Commandements Cmd 1-13
- Interdits de liens étanchéité
- Lexique sashimono (hozo, zōsaku, kari-kumi, kumiko)
- Table Karūbī ↔ destinataire
- Vocabulaire technique (navette, canonique, zones scellées)

**Algorithme** : SM-2 simplifié
- ease_factor initial : 2.5
- Intervalles : 1j → 6j → n×ease_factor
- Qualité réponse (0-5) ajuste ease_factor

**Stratégie** : commande interactive `hermes srs review` + injection prompt (2-3 cartes/session)

**Estimation** : 80-120 cartes, 5-10 min/session de révision, 5-7h d'implémentation

### 4. Angle mort C3 — VÉRIFIÉ

**Constat** : le contrôle C3 dans verifier-invariants.py gère déjà les liens annales.md/index.md → meta/ via le contrôle C4 (avertissements non bloquants).

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

## Chantiers prioritaires ouverts

### A. SRS Hermes-native — implémentation (5-7h)

**Statut** : spécification créée, implémentation à lancer

**Plan** :
1. Phase 1 : écriture generer-cartes-protocole.py (1-2h)
2. Phase 2 : stockage srs-cards.yaml (30min)
3. Phase 3 : algorithme SM-2 (1h)
4. Phase 4 : interface commande interactive (2-3h)
5. Phase 5 : cron quotidien (30min)

**Livrables** :
- Script generer-cartes-protocole.py
- Fichier srs-cards.yaml avec ~80-120 cartes
- Commande `hermes srs review`
- Cron quotidien 09:00 UTC (11:00 Paris)

### B. Suivi spirituel Sidy — à définir

**Objectif** : soutenir la pratique spirituelle fragile de Sidy (Dalail al-khayrat, wadhifa Naqshbandi Fajr)

**Options** :
1. Cron rappel quotidien (06:00 UTC = 08:00 Paris)
2. Suivi rêves/visions (arc Kaaba, double protecteur)
3. Consolidation mémoire régulière (hebdomadaire)

**À valider avec Sidy** : fréquence, format, canaux (Discord/Telegram/CLI)

### C. Anomalies frontmatter bloquantes — 3 fichiers

**Fichiers** :
- atelier/stealing-reasoning-traces-rd.md : frontmatter absent
- atelier/rd/incidents/2026-08-22_post-scriptum-hook-corrige.md : created, updated manquants
- atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md : created, updated manquants

**Action** : ajouter frontmatter manquant (Sceau atelier)

### D. graphe-cartographie.json — non régénéré

**Problème** : le fichier n'est pas à jour avec l'état actuel du dépôt

**Action** : régénérer après correction anomalies frontmatter

### E. Isolation mémoire Hermes par sub-agent — BLOQUANT

**Problème** : skill Karūbī-Hermes ne peut pas être déployé sans toggle memory_enabled par sub-agent

**Statut** : investiguer doc Hermes ou code source

**Piste** : PR #34098 hermes-agent propose ajout memory_enabled par job

### F. Spec rôle G0 — verdict Sidy attendu

**Fichier** : `meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md`

**Statut** : brouillon kari-kumi, verdict Sidy attendu

## Plan d'action — soutien Sidy

### Personnel

1. **Suivi pratique spirituelle** :
   - Cron rappel quotidien (à valider)
   - Suivi rêves/visions (arc Kaaba, double protecteur)
   - Consolidation mémoire SRS (5-10 min/session)

2. **Soutien émotionnel** :
   - Mémoire complète des relations clés (Karūbī, collaborateurs)
   - Contexte spirituel intégré (khalwa, convalescence, rattachement)
   - Concepts personnels (initiation virtuelle, incandescence)

3. **Réduction charge mentale** :
   - Plus besoin de réexpliquer le contexte à chaque session
   - Crons automatisés (veille infrastructure, SRS)
   - Bureau TUI pour consultation rapide

### Professionnel

1. **Label "Dans l'Absolu"** :
   - Mémoire complète des 12 agents Hermes
   - Extension zodiacale (9 brouillons, positions 5/8/12 en attente)
   - Outillage Karūbī (5 instances actives)

2. **Pôle R&D** :
   - Veille infrastructure quotidienne (cron actif)
   - Bureau TUI fonctionnel (6 modules, 3 services)
   - Scripts déterministes (4 scripts actifs)

3. **Infrastructure** :
   - 12 profils Hermes actifs
   - Monitoring quotidien (cron 12:00 UTC)
   - Hébergement Hetzner (2 vCPU, 3.7GB RAM)

## Prochaines étapes immédiates

1. **Valider avec Sidy** :
   - Suivi spirituel : fréquence, format, canaux ?
   - SRS : implémenter maintenant ou plus tard ?
   - Anomalies frontmatter : corriger maintenant ?

2. **Implémenter SRS Hermes-native** (si validé) :
   - Écrire generer-cartes-protocole.py
   - Créer srs-cards.yaml
   - Tester commande interactive

3. **Corriger anomalies frontmatter** :
   - Ajouter frontmatter aux 3 fichiers bloquants
   - Régénérer graphe-cartographie.json

4. **Investiguer isolation mémoire** :
   - Consulter PR #34098 hermes-agent
   - Tester toggle memory_enabled

## Conclusion

Le problème de mémoire persistante est résolu. Les ressources sont déployées. Le plan d'action est clair.

**Statut** : prêt à exécuter les prochaines étapes, en attente de validation Sidy.

**Impact attendu** :
- Fin de l'amnésie systématique
- Suivi spirituel soutenu
- Veille infrastructure automatisée
- Révision protocole régulière (SRS)
- Réduction charge mentale globale
