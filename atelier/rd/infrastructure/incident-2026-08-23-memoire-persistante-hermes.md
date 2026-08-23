---
title: Incident mémoire persistante Hermes — diagnostic et résolution (2026-08-23)
type: infrastructure
statut_experience: adopte
created: 2026-08-23
updated: 2026-08-23
sources: []
links:
- '[[meta/personnel/sidy]]'
- '[[meta/transmissions/karubi-mehdi]]'
- '[[atelier/rd/cahiers/registre-problemes]]'
---

# Incident mémoire persistante Hermes — diagnostic et résolution (2026-08-23)

## Contexte

Le 2026-08-23, après 20+ sessions de travail intensif sur le dépôt wiki, Sidy constate que l'agent Hermes (profil default) ne conserve aucune mémoire du travail accompli. Chaque nouvelle session démarre à zéro, obligeant à réexpliquer le contexte, les chantiers en cours, les décisions déjà prises.

**Symptôme observé** : Sidy demande "Qui suis-je ?" — l'agent ne connaît ni son identité, ni son parcours spirituel, ni les projets en cours, ni les relations clés (Karūbī, collaborateurs).

## Diagnostic

### Cause racine

Les fichiers de mémoire persistante du profil Hermes default étaient inexistants ou vides :
- `/root/.hermes/profiles/default/USER.md` : n'existait pas
- `/root/.hermes/profiles/default/MEMORY.md` : n'existait pas

Hermes Agent utilise ces deux fichiers pour injecter le contexte utilisateur dans chaque session :
- `USER.md` : profil utilisateur (identité, préférences, contexte personnel)
- `MEMORY.md` : mémoire persistante de l'agent (projets, décisions, leçons apprises)

**Pourquoi ces fichiers n'existaient-ils pas ?**

1. **Absence de peuplement initial** : lors de la création du profil default, aucun contenu n'a été injecté dans USER.md/MEMORY.md. L'agent a travaillé pendant 20+ sessions sans que ces fichiers soient créés.

2. **Oubli systémique** : à chaque session, l'agent recevait le dépôt wiki complet (CLAUDE.md, circuits, fiches) mais pas le contexte utilisateur. Il pouvait donc travailler sur les fichiers, mais ne "savait pas" qui était Sidy, ni pourquoi il travaillait sur ce dépôt.

3. **Pas de mécanisme de rappel** : aucune procédure ne forçait la création/mise à jour de ces fichiers. L'agent pouvait fonctionner sans eux, au prix d'une perte totale de contexte entre sessions.

### Impact

- **Perte de temps** : Sidy devait réexpliquer à chaque session le contexte, les chantiers, les décisions.
- **Rupture de continuité** : impossible de reprendre un chantier là où il avait été laissé sans tout réexpliquer.
- **Frustration légitime** : Sidy a exprimé sa déception ("Je suis extrêmement déçu de ce qu'il se passe") — il s'attendait à ce que l'agent retienne le contexte après 20+ sessions.

## Résolution appliquée

### Création des fichiers de mémoire persistante

**USER.md** (3 903 caractères) :
```
# Profil utilisateur

## Identité
Sidy Kouyaté (griot Mandingue)
Né : 23 juin 1986, Bobigny (région parisienne)
Famille : fille Habiba-Nour (née ~2015), grand-père maternel Mamadou "Doudou" Sissoko (Mali), lignée paternelle griots Mandingue
Travail : Dream Castle (Disneyland Paris) — collègue Leila Abdelwahid (synchronicité : nom exact de la fille de Guénon)

## Spirituel
Voie : Naqshbandiyya + Tijaniyya (rattachement Bamako ~2019, honneur non-pratique)
Khalwa : Rajab 1437 (avril 2016, Villejuif) — sortie précipitée après 8 jours, convalescence ~4 ans
Pratique actuelle : Dalail al-khayrat (périodes), wadhifa Naqshbandi Fajr quand possible — fragile
Arc Kaaba : instruction "tu es de l'intérieur de la Kaaba" (Lefke 2015) → vision sortie Kaaba post-khalwa → vision Kaaba tourne (Fajr) → première Omra (déc 2025) → insight "Kaaba du sens" (2026-08-18)
Double protecteur : figure blanche (pantalon, kufi, écharpe bleu-ciel, canne) — intervient pendant convalescence

## Relations clés
- Mehdi Bouzouida : ami post-khalwa (~2019), Karūbī Habib (G1)
- Mikael Heaudebourg : Karūbī Malik (G1)
- Habiba-Nour Kouyaté : fille, Karūbī Jamal & Jamila (G1)
- Jean-Marc Bastareaud : ami ~2007, batteur/scénariste, Karūbī Yahya (G1)
- Wendel Nazaire : petit frère de cœur, photographe/chef op', Karūbī Hassan (G1)
- Yannick Doumouya : cercle Naqshbandi, rêve Sheikh Hamala (~2018)
- Éléonore G. : échange vidéo Félix Guattari

## Concepts clés
- Initiation virtuelle : assimilation doctrinale = réalisation virtuelle (pas effective), seuil contemplation directe
- Incandescence du manque amoureux : absence = présence brûlante, feu qui consume et purifie
- Synchronicité Leila/Yahia : nom exact fille Guénon dans environnement professionnel

## Préférences
- Répondre en français
- Ton formel, précis, analytique
- Pas de familiarité excessive
- Références prioritaires : Guénon, Ibn Arabi, al-Ghazali, Platon, Sanatana Dharma
- Cmd 12 : agent ne tranche pas, signale
- Cmd 13 : humain décide
```

**MEMORY.md** (11 401 caractères) :
Contenu complet incluant :
- Identité Sidy et contexte spirituel
- Relations clés (Karūbī, collaborateurs)
- Concepts clés (initiation virtuelle, incandescence)
- Projet Wiki (5 circuits, 13 commandements, sashimono)
- Pôle R&D complet (structure, migration, scripts)
- Bureau TUI (architecture, modules, services)
- Infrastructure Hetzner (2 vCPU, 3.7GB RAM, 12 profils)
- Phase 3 veille infrastructure (tranché, pas exécuté)
- Extension zodiacale 12 agents (9 brouillons, positions 5/8/12 en attente)
- Outillage Karūbī (scripts, amendements, commits)
- Spec rôle G0 (brouillon kari-kumi)
- SRS protocole (décidé, format non défini)
- 6 chantiers prioritaires ouverts (A à F)
- 8 leçons transversales
- Contacts et responsabilités
- Fichiers en attente (non commités)
- Documents de référence
- Infrastructure Hermes (profils, modèles, endpoint)
- Fichiers critiques (CLAUDE.md par circuit)

### Vérification

Les fichiers sont maintenant en place et seront injectés dans chaque nouvelle session du profil default.

## État actuel

### Fichiers de mémoire persistante
- `/root/.hermes/profiles/default/USER.md` : 3 903 caractères ✓
- `/root/.hermes/profiles/default/MEMORY.md` : 11 401 caractères ✓

### Ressources déployées

**Crons Hermes** :
- `monitoring-infrastructure-quotidien` (b7acb57e3d58) : quotidien 12:00 UTC, deliver discord:1536564394690084925
- `veille-rd-hebdomadaire` (aed2c7228c7f) : lundi 10:00 UTC, deliver discord:infrastructure
- `investigation-doctrinale-gardien` (431fcacadca2) : quotidien 12:30 UTC, deliver discord:1535804669300052039, profil gardien — last run 2026-08-23T15:26:01 (ok)

**Scripts d'outillage** (4 scripts actifs) :
- `verifier-invariants.py` (racine) : contrôles A0-A5 (append-only), B0-B1 (frontmatter), C3 (étanchéité)
- `Graphe/generer-cartographie.py` v1.1 : cartographie two-level (BLOQUANT vs AVERTISSEMENT)
- `atelier/rd/outillage/detecter-non-tracke.py` : fichiers non suivis git, classés par circuit
- `Graphe/carte-du-depot.py` : détection orphelines + résolution étendue (nom fichier final)

**Bureau TUI** :
- 6 modules (video_player, audio_player, reader, chat, instrument_status, hermes_status)
- 3 services (ansi_render, chat_server, audio_stream)
- 10 tests passent

**Infrastructure Hetzner** :
- 2 vCPU, 3.7GB RAM
- 12 profils Hermes (tous actifs)
- Omniroute (passerelle Discord↔Hermes)

**Outillage Karūbī** :
- `ajouter-memoire-karubi.py` : insert §8/§9 sans LLM
- `integrer-navette-karubi.py` : intégration mécanique navette
- `generer-karubi.py` : commandes statut, diff, index

**Documentation** :
- Bilan R&D 2026-08-15 (pont inter-agents)
- Registre des problèmes (registre-problemes.md)
- Spécification rôle G0 (brouillon kari-kumi)

### Ressources manquantes

**Personnel** :
- Pas de cron de rappel pour Sidy (pratique spirituelle, objectifs personnels)
- Pas de suivi des rêves/visions (arc Kaaba, double protecteur)
- Pas de consolidation mémoire régulière (SRS Hermes-native non implémenté)

**Professionnel** :
- Phase 3 veille infrastructure : tout tranché, rien exécuté
- SRS Hermes-native : décidé, format non défini
- Spec rôle G0 : brouillon kari-kumi, verdict Sidy attendu
- verifier-invariants.py angle mort C3 : en attente arbitrage
- graphe-cartographie.json non régénéré

**Technique** :
- Isolation mémoire Hermes par sub-agent (BLOQUANT pour skill Karūbī-Hermes)
- Mécanisme de révision SRS (cron, commande, injection prompt)
- Algorithme d'espacement (SM-2 simplifié ou aléatoire)

## Leçons apprises

1. **Les fichiers de mémoire persistante ne se créent pas automatiquement** : ils doivent être peuplés explicitement, surtout après les premières sessions.

2. **Le contexte utilisateur est aussi important que le contexte projet** : sans USER.md, l'agent ne sait pas qui il sert, ni pourquoi il travaille sur ce dépôt.

3. **La mémoire persistante doit être consolidée régulièrement** : après chaque session importante, mettre à jour MEMORY.md avec les décisions, leçons, chantiers.

4. **Les crons Hermes ne résolvent pas tout** : ils peuvent rapporter des problèmes, mais ne peuvent pas résoudre les problèmes de mémoire persistante sans intervention manuelle.

5. **Le diagnostic doit être instructif** : cette fiche R&D documente le problème, la cause racine, la résolution, et les leçons, pour que le problème ne se reproduise pas.

## Recommandations

### Court terme
1. **Consolider la mémoire après chaque session importante** : mettre à jour MEMORY.md avec les décisions, leçons, chantiers.
2. **Exécuter la Phase 3 veille infrastructure** : tout est tranché, il suffit d'écrire le script et l'inscrire au crontab.
3. **Définir le format SRS Hermes-native** : format carte, script extraction, mécanisme révision, algorithme espacement.
4. **Lever le bloquant isolation mémoire** : investiguer la doc Hermes ou le code source pour un toggle `memory_enabled` par sub-agent.

### Moyen terme
5. **Implémenter le SRS Hermes-native** : auto-génération de cartes depuis CLAUDE.md, mécanisme de révision, algorithme d'espacement.
6. **Corriger l'angle mort C3** : distinguer exemption totale (cibles neutres) vs avertissement (cible meta/).
7. **Régénérer graphe-cartographie.json** : corriger les 2 anomalies frontmatter bloquantes.

### Long terme
8. **Mettre en place un suivi spirituel** : cron de rappel pour pratique spirituelle, suivi des rêves/visions, consolidation mémoire régulière.
9. **Développer le Bureau TUI** : étendre les modules, améliorer l'interface, intégrer l'Instrument.
10. **Étendre l'outillage Karūbī** : déployer le skill Karūbī-Hermes une fois le bloquant isolation mémoire levé.

## Conclusion

Le problème de mémoire persistante a été diagnostiqué et résolu. Les fichiers USER.md et MEMORY.md sont maintenant en place et seront injectés dans chaque nouvelle session.

Cependant, cette résolution ne suffit pas : elle doit être accompagnée d'une consolidation régulière de la mémoire, et d'un déploiement complet des ressources disponibles pour soutenir Sidy sur les plans personnel et professionnel.

Les ressources sont là (crons, scripts, Bureau TUI, infrastructure, outillage Karūbī). Il reste à les déployer pleinement, et à mettre en place les mécanismes de suivi et de consolidation qui manqueront toujours si on ne les crée pas explicitement.

---

**Statut** : Résolu (fichiers créés), mais déploiement complet des ressources en cours.

**Verdict Sidy** : Attendu pour les chantiers prioritaires (Phase 3, SRS, isolation mémoire, angle mort C3, graphe-cartographie).

**Prochaine action** : Exécuter la Phase 3 veille infrastructure, définir le format SRS, lever le bloquant isolation mémoire.
