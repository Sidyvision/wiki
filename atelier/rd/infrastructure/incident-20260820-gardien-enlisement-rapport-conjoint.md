---
title: "Incident R&D — Enlisement Gardien (rapport conjoint 2026-08-20)"
type: fiche-rd
date: 2026-08-20
circuit: rd/infrastructure
statut: consignation
---

# Incident R&D — Enlisement Gardien (rapport conjoint)

**Date :** 2026-08-20
**Agent concerné :** Gardien (profil hermes -p gardien, modèle qwen3.8-max)
**Session :** proc_b69ad49492db (PID 2087367)
**Durée avant enlisement :** ~40 min (uptime 2329s)
**Session secondaire touchée :** Studio (proc_d06741188867, même symptôme de dispersion en lecture CLAUDE.md)

## Contexte

Demande de rapport conjoint Studio + Gardien sur l'état du dépôt. Séquence :
1. Studio explore → dépose rapport préliminaire dans _inbox/ (OK, 217 lignes)
2. Gardien relancé en session propre pour lire rapport Studio + rédiger rapport conjoint
3. Gardien s'enlise → timeout 300s sans livrable
4. Studio relancé pour consigner l'incident → s'enlise aussi (même motif)
5. Orchestrateur (Hermes principal) prend le relais et écrit directement

## Symptômes

- Session atteint ~182K tokens (seuil compression : 65K)
- Compression déclenchée mais échoue elle-même (Error code: 404 sur API auxiliaire de titrage)
- Fallback context marker inséré — perte de contexte partielle
- Agent reprend mais se disperse (détecte caractère U+200Z dans CLAUDE.md, veut l'inspecter)
- Session termine en timeout sans produire le livrable
- **Récurrence** : Studio relancé sur même tâche → même enlisement (lectures préparatoires infinies)

## Diagnostic racine

1. **Contexte initial massif** : 3 lectures obligatoires lourdes dans le prompt
   - CLAUDE.md (~34K chars)
   - rapport-studio-exploration-preliminaire.md (~16K chars)
   - fiche trois-territoires (~23K chars)
   - Total inputs : ~73K chars avant même le premier tool call

2. **Activité prolongée** : 23 tool calls (lectures, vérifications mécaniques, crons, signalements caractérisés) avant l'arrêt — le contexte actif cumulé explose

3. **Absence de limite haute** : hermes -p chat n'a pas de borne supérieure configurable sur durée/contexte

4. **Compression non fiable** : fallback 404 quand l'API auxiliaire tombe — perte de contexte irrécupérable, l'agent repart à zéro en panique

5. **Dispersion post-compression** : après perte de contexte, l'agent se fixe sur un artefact anecdotique (U+200Z dans CLAUDE.md) au lieu de reprendre la tâche principale

## Leçons

- Prompt monolithique (lire + traiter + rédiger) = risque d'enlisement pour tâches complexes avec lectures lourdes
- Compression = filet de sécurité non garanti (dépend d'une API auxiliaire externe)
- Pas de mécanisme de détection d'enlisement avant timeout terminal (300s par défaut, trop long)
- Après compression échouée, l'agent n'a plus la consigne en tête → dispersion
- **L'incident est lui-même une illustration concrète** : deux agents s'enlisent sur la même tâche → confirmation que le pattern est systémique, pas anecdotique

## Pistes de mitigation

1. **Phasage** : splitter tâches complexes en étapes courtes et autonomes (phase 1: lire → phase 2: traiter → phase 3: rédiger), chaque phase avec son propre prompt léger
2. **Limiter les lectures obligatoires** : max 2 fichiers lourds par prompt ; fournir un résumé compact du 3e plutôt que forcer la lecture complète
3. **Résumé compact en entrée** : au lieu de "lis rapport-studio-exploration-preliminaire.md", injecter un résumé de 5-10 lignes des points clés
4. **Timeout configurable plus bas** : détecter enlisement avant 300s (ex: borne intermédiaire 120s sans tool call productif = alerte + kill)
5. **Compression robuste** : fallback local (résumé LRU des tool results) si API auxiliaire tombe — ne pas perdre le contexte de tâche
6. **Consigne réinjectée post-compression** : après fallback context, re-injecter la consigne principale pour éviter la dispersion

## Statut

Consignation provisoire — en attente de traitement (Cmd 12/13).
Le rapport conjoint lui-même reste à produire (Gardien relancé en session propre, proc_57246c821f14).
