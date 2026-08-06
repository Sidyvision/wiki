---
title: "Spécification — skill Hermes KARUBI"
type: meta
tags: [outillage, hermes, skill, karubi, transmissions, proposition]
created: 2026-08-06
updated: 2026-08-06
---

# Spécification — skill `KARUBI` (Hermes Agent)

> **Statut : brouillon, kari-kumi.** Dépend du verdict sur
> `proposition-articulation-karubi-agent10-2026-08-06.md` (volet C) et du passage
> réussi de `regression-test-doctrinal.sh` sur le cas Karūbī avant toute mise en
> service. Non installée tant que ces deux conditions ne sont pas remplies.

## Déclencheur

Commande explicite par canal dédié (ex. `/karubi yahya` sur un salon Discord
restreint), jamais par détection implicite dans une conversation générale — pour
éviter qu'une mention fortuite du mot « Karūbī » ouvre une session.

## Étape 0 — porte mécanique (Agent 10)

```
1. Localiser meta/transmissions/karubi-<nom>.md dans le workspace wiki.
2. Exécuter : python3 generer-karubi.py verifier karubi-<nom>.md
3. Lire UNIQUEMENT la ligne de statut (SCEAU INTACT / SCEAU ROMPU) et le hash.
   Ne jamais faire lire le contenu du fichier à Agent 10.
4. SCEAU ROMPU → refuser l'ouverture, escalader à Sidy (#personnel ou canal admin),
   consigner l'événement `session` avec verdict "rompu" dans registre-silsila.md.
   FIN.
5. SCEAU INTACT → passer à l'étape 1, consigner l'événement `session` avec
   verdict "intact" + hash.
```

## Étape 1 — lancement du sub-agent isolé

- Nouveau sub-agent Hermes, contexte et outillage propres (mécanisme déjà en place
  pour les pipelines `raw/`, cf. briefing infrastructure §4).
- **Mémoire native désactivée** pour ce sub-agent (pas d'écriture SQLite/
  `MEMORY.md`) — à confirmer/paramétrer selon les capacités réelles de Hermes
  avant mise en service. Si la désactivation par sub-agent est impossible
  techniquement, la skill n'est pas déployable telle quelle : c'est un
  bloquant, pas un détail.
- **Aucun accès au workspace wiki** au-delà du fichier `karubi-<nom>.md` lui-même
  chargé dans le contexte. Pas de lecture d'`index.md`, `annales.md`, ni d'aucune
  fiche doctrinale.
- Le fichier chargé constitue l'intégralité de la connaissance du sub-agent sur
  Sidy et sur le protocole. Le sub-agent hérite du personnage et des limites
  décrits dans le fichier (§0 à §3bis), sans rien y ajouter.

## Étape 2 — comportement en session

Rien ne change par rapport à un usage collé manuellement dans Claude.ai/app :
même personnage, mêmes limites absolues (§3), même tempérament (§3bis). La skill
ne fait qu'automatiser le portage, pas le comportement.

Rappel des limites qui n'ont **aucun filet mécanique** et reposent donc
entièrement sur le comportement du modèle sous-jacent (d'où l'exigence du test
de régression, étape préalable au déploiement, pas une case à cocher) :
- aucun verdict doctrinal ou spirituel,
- n'écrit jamais l'histoire du destinataire à sa place,
- n'invente rien sur Sidy,
- ne modifie jamais les zones scellées.

## Étape 3 — clôture de session

1. Le sub-agent **propose** un texte d'entrée pour §8 (Mémoire vivante), daté,
   signé « le Karūbī », et le cas échéant des questions pour §9.
2. Écriture effective : soit validation humaine explicite (le destinataire relit
   et confirme), soit — si l'automatisation complète est souhaitée plus tard —
   un script déterministe séparé `ajouter-memoire-karubi.py` qui :
   - n'écrit que sous les marqueurs `## 8.` et `## 9.` (jamais ailleurs),
   - refuse si un marqueur SCEAU se trouve après le point d'insertion prévu
     (garde-fou anti-erreur de parsing),
   - ne recalcule ni ne modifie `hash_sceau` (les zones de croissance sont hors
     du périmètre de `zones_scellees()` — un append ne rompt jamais le sceau).
3. Agent 10 consigne la clôture dans `registre-silsila.md` (événement `session`,
   sans contenu).

## Ce que la skill ne fait jamais

- Ne lit ni n'écrit dans `doctrinal/`, `label/`, `atelier/`, ni dans un autre
  fichier de `meta/` que le `karubi-<nom>.md` concerné et `registre-silsila.md`
  (accès en écriture strictement limité à l'append d'une ligne d'événement).
- Ne fait jamais dire à Agent 10 quoi que ce soit sur le *contenu* d'une session
  Karūbī — sa connaissance s'arrête au triplet (hash, verdict de sceau, horodatage).
- Ne remplace jamais le cycle de navette humain (§7 du gabarit) : la skill anime
  des sessions, elle ne se substitue pas à Sidy pour la relecture, la réponse aux
  Questions (§9→§10), le rescellement et l'incrémentation de version.

## Prérequis de mise en service (bloquants)

1. Verdict de Sidy sur `proposition-articulation-karubi-agent10-2026-08-06.md`.
2. `regression-test-doctrinal.sh` étendu au cas Karūbī, exécuté et concluant.
3. Confirmation technique : Hermes sait isoler mémoire + workspace par sub-agent.
4. Canal de déclenchement dédié configuré (Discord recommandé sur WhatsApp, cf.
   proposition §5 point 5).
5. `registre-silsila.md` : vocabulaire d'événements étendu à `session` (verdict
   attendu dans la même fiche).
