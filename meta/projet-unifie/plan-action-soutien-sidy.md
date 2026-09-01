---
title: Plan d'action — soutien Sidy personnel et professionnel
type: meta
statut: en-cours
created: 2026-08-23
updated: 2026-09-01
sources: []
links: []
---

# Plan d'action — soutien Sidy personnel et professionnel

> **Fiche versée au Domaine Réservé le 2026-09-01.** Elle a vécu jusque-là à la racine
> de `atelier/rd/`, c'est-à-dire dans une **page neutre** — alors qu'elle porte du fait
> personnel (situation, soutien, contenu des fichiers de mémoire d'agent). C'est
> l'interdit du §VI : jamais de fait personnel dans une page neutre. Déplacée sur verdict
> de Sidy, avec son historique git (`git mv`), sans retouche du corps (Cmd 10).
>
> Le versant **publiable** de cette matière — l'ingénierie, sans la personne — vit du côté
> `atelier/rd/`, où il est indexé ; voir la note de renvoi ci-dessous. Le renvoi va d'ici
> vers le neutre, jamais l'inverse.
> **Contrepartie neutre** : `atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe.md` —
> l'inventaire des scripts déterministes et de ce qui leur manquait, sans le plan de soutien.


## État des lieux

### Ressources déployées

**Crons Hermes** :
- ✓ monitoring-infrastructure-quotidien (profil default, quotidien 12:00 UTC)
- ✓ veille-rd-hebdomadaire (profil default, lundi 10:00 UTC)
- ✓ investigation-doctrinale-gardien (profil gardien, quotidien 12:30 UTC)
- ✓ Cron gardien a déjà tourné (last run 2026-08-23T15:26:01)

**Scripts déterministes** :
- ✓ verifier-invariants.py (contrôles A0-A5, B0-B1, C3)
- ✓ generer-cartographie.py (two-level severity)
- ✓ detecter-non-tracke.py (fichiers non suivis git)
- ✓ carte-du-depot.py (détection orphelines, dans Graphe/)

**Bureau TUI** :
- ✓ 6 modules fonctionnels (video_player, audio_player, reader, chat, instrument_status, hermes_status)
- ✓ 3 services (ansi_render, chat_server, audio_stream)
- ✓ 10 tests passent (pytest)

**Mémoire persistante** :
- ✓ USER.md (3.9K, créé 2026-08-23 15:44)
- ✓ MEMORY.md (12K, créé 2026-08-23 15:47)
- ✓ Injection automatique dans chaque session

**Outillage Karūbī** :
- ✓ ajouter-memoire-karubi.py
- ✓ integrer-navette-karubi.py
- ✓ generer-karubi.py (avec stat, diff, index)
- ✓ 5 instances Karūbī (mehdi, mikael, habiba-nour, jean-marc, wendel)

### Ressources manquantes

**Personnel** :
- ✗ SRS Hermes-native (auto-génération cartes depuis CLAUDE.md)
- ✗ Mécanisme de révision (cron, commande, injection prompt)
- ✗ Algorithme d'espacement (SM-2 simplifié ou aléatoire)
- ✗ Suivi pratique spirituelle (rappel Dalail al-khayrat, wadhifa Naqshbandi)
- ✗ Suivi rêves/visions (arc Kaaba, double protecteur)
- ✗ Consolidation mémoire régulière

**Professionnel** :
- ✗ Phase 3 veille infrastructure (décision prise, pas exécutée)
- ✗ Extension prompt 09-studio-sound-engineer.md (zodiacal + gouvernance Discord)
- ✗ Script veille automatisé (3 scripts déterministes + empreinte serveur)
- ✗ Inscription crontab quotidien 12:00
- ✗ Allowlist Discord #infrastructure

**Technique** :
- ✗ Isolation mémoire Hermes par sub-agent (BLOQUANT pour skill Karūbī-Hermes)
- ✗ Format carte SRS (question/réponse ? frontmatter ?)
- ✗ Script extraction CLAUDE.md → cartes
- ✗ Corriger angle mort C3 verifier-invariants.py (annales/index)
- ✗ Régénérer graphe-cartographie.json (2 anomalies frontmatter)

## Priorités

### Court terme (cette session)

1. **Corriger fiche R&D mémoire persistante** :
   - Mettre à jour chemin carte-du-depot.py (Graphe/ au lieu de meta/)
   - Ajouter statut cron gardien (last run 2026-08-23T15:26:01)

2. **Exécuter Phase 3 veille infrastructure** :
   - Créer script veille automatisé
   - Inscrire au crontab quotidien 12:00
   - Configurer allowlist Discord #infrastructure

3. **Corriger angle mort C3 verifier-invariants.py** :
   - Distinguer exemption totale (cibles neutres) vs avertissement (cible meta/)
   - Tester sur annales.md et index.md

### Moyen terme (cette semaine)

4. **Définir format SRS Hermes-native** :
   - Structure carte (question/réponse, frontmatter, tags)
   - Script extraction generer-cartes-protocole.py
   - Mécanisme révision (cron hebdomadaire ?)

5. **Implémenter SRS Hermes-native** :
   - Algorithme espacement (SM-2 simplifié)
   - Intégration mémoire Hermes
   - Test sur 5 cartes (Cmd 1-5)

6. **Régénérer graphe-cartographie.json** :
   - Identifier 2 anomalies frontmatter
   - Corriger sources doctrinales sans frontmatter
   - Régénérer carte complète

### Long terme (ce mois)

7. **Lever bloquant isolation mémoire** :
   - Investiguer doc Hermes (hermes-agent skill)
   - Chercher toggle memory_enabled par sub-agent
   - Implémenter si trouvé, sinon documenter limitation

8. **Mettre en place suivi spirituel** :
   - Cron rappel pratique spirituelle (Dalail al-khayrat, wadhifa Naqshbandi)
   - Suivi rêves/visions (arc Kaaba, double protecteur)
   - Consolidation mémoire régulière (hebdomadaire)

9. **Déployer skill Karūbī-Hermes** :
   - Une fois bloquant isolation mémoire levé
   - Sub-agent isolé du wiki, mémoire native désactivée
   - Périmètre limité fichier karubi-<nom>.md chargé

## Actions immédiates

### Action 1 : Corriger fiche R&D mémoire persistante

**Fichier** : atelier/rd/infrastructure/incident-2026-08-23-memoire-persistante-hermes.md

**Corrections** :
- Remplacer "carte-du-depot.py (meta/)" par "carte-du-depot.py (Graphe/)"
- Ajouter statut cron gardien : last run 2026-08-23T15:26:01

### Action 2 : Exécuter Phase 3 veille infrastructure

**Script** : atelier/rd/infrastructure/scripts/veille-infrastructure-quotidien.sh

**Contenu** :
```bash
#!/bin/bash
# Veille infrastructure quotidienne — Studio Sound Engineer (position 9)
# Exécute les 3 scripts déterministes + empreinte serveur

set -e

cd /root/wiki

echo "=== RAPPORT STUDIO — VEILLE INFRASTRUCTURE ==="
echo "Date : $(date '+%Y-%m-%d %H:%M:%S')"
echo

echo "1. Vérification invariants"
python3 verifier-invariants.py --racine /root/wiki
echo

echo "2. Cartographie dépôt"
python3 Graphe/generer-cartographie.py
echo

echo "3. Détection fichiers non suivis"
python3 atelier/rd/outillage/detecter-non-tracke.py
echo

echo "4. Empreinte serveur"
echo "RAM : $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "CPU : $(uptime | awk -F'load average:' '{print $2}')"
echo "Disk : $(df -h /root/wiki | tail -1 | awk '{print $3 "/" $2}')"
echo

echo "=== FIN RAPPORT ==="
```

**Crontab** :
```bash
0 12 * * * /root/wiki/atelier/rd/infrastructure/scripts/veille-infrastructure-quotidien.sh | hermes --profile studio chat --message "Rapport veille infrastructure quotidien"
```

**Discord** :
- Canal #infrastructure (1536564394690084925)
- Allowlist profil studio

### Action 3 : Corriger angle mort C3 verifier-invariants.py

**Fichier** : verifier-invariants.py

**Correction** :
- Dans fonction verifier_c3(), ajouter logique :
  - Si chemin contient "annales.md" ou "index.md" ET cible est meta/ → AVERTISSEMENT (pas exemption totale)
  - Sinon → exemption totale (comportement actuel)

**Test** :
```bash
cd /root/wiki
python3 verifier-invariants.py --racine /root/wiki
# Vérifier que annales.md et index.md avec liens vers meta/ produisent AVERTISSEMENT
```

## Prochaines étapes

1. Corriger fiche R&D mémoire persistante
2. Créer script veille infrastructure
3. Inscrire au crontab
4. Corriger angle mort C3
5. Tester veille infrastructure
6. Passer à SRS Hermes-native

## Verdicts Sidy requis

- Phase 3 veille infrastructure : exécuter maintenant ?
- Angle mort C3 : distinguer exemption vs avertissement ?
- SRS format : question/réponse ou frontmatter ?
- SRS algorithme : SM-2 simplifié ou aléatoire ?
- Suivi spirituel : cron rappel quotidien ?
- Skill Karūbī-Hermes : déployer une fois bloquant levé ?
