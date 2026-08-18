---
title: "Charte — Archive du monitoring infrastructure quotidien"
type: infrastructure
tags: [rd, infrastructure, monitoring, hermes, archive]
created: 2026-08-18
updated: 2026-08-18
sources: []
links: ["[[atelier/rd/outillage/spec-archiver-monitoring-quotidien]]", "[[atelier/rd/infrastructure/activation-monitoring-studio-cron-2026-08-17]]", "[[atelier/rd/cahiers/registre-problemes]]"]
---

# Charte — `atelier/rd/infrastructure/monitoring-archive/`

## Motif

Suggestion Sidy, 2026-08-18 : conserver en parallèle, dans un dossier
d'archive au pôle R&D, le « Rapport monitoring infrastructure quotidien »
reçu via Discord, pour une durée de 40 jours — afin de renforcer le
monitoring de l'agent lui-même (pas seulement de l'infrastructure qu'il
surveille).

## Contenu du dossier

`atelier/rd/infrastructure/monitoring-archive/<YYYY-MM-DD>_<job_id>.txt` —
une copie par exécution du job H‍ermes `monitoring-infrastructure-quotidien`
(profil `studio`, id `41dc3e7e492c`), format `.txt` **délibérément**, jamais
`.md` (raison détaillée : [[atelier/rd/outillage/spec-archiver-monitoring-quotidien]]
§3 — le rapport cite des tokens `[[...]]` littéraux qui feraient s'auto-
déclencher `verifier-invariants.py`/`generer-cartographie.py` sur l'archive
elle-même). Ces fichiers ne portent pas de Sceau : ce ne sont pas des fiches
du dépôt, mais un journal technique brut.

## Alimentation

Script déterministe [[atelier/rd/outillage/spec-archiver-monitoring-quotidien|
archiver-monitoring-quotidien.py]] : copie ce que H‍ermes a déjà persisté sur
disque (`/root/.hermes/profiles/studio/cron/output/`), sans toucher au job de
production ni à Discord. Purge les copies au-delà de 40 jours.

**Ingestion — décision en attente de Sidy** : le script existe et fonctionne
(testé en dry-run puis appliqué le 2026-08-18, 2 rapports archivés :
2026-08-17 et 2026-08-18). Reste ouverte la question du déclenchement
récurrent :
- **manuel**, à la discrétion de Sidy ou d'une session d'intégration
  (`python3 atelier/rd/outillage/archiver-monitoring-quotidien.py --appliquer`) ;
- ou **cron dédié** côté H‍ermes (`no_agent`, script pur — même famille que le
  job `coherence-infrastructure-brute` cassé, cf. §« Note » ci-dessous),
  planifié après l'exécution du job monitoring (ex. `10 12 * * *`).

Aucune automatisation n'est affirmée tant que ce choix n'est pas tranché et
qu'un cron correspondant n'est pas vérifié en état `last_status: "ok"` — cf.
`infra_verif` et le principe de non-fabulation narrative (§VIII.2 du
protocole racine).

## Rétention

40 jours glissants dans ce dossier. **Ce n'est pas une fenêtre d'historique
absolue** : tout fichier commité dans git avant sa purge reste retrouvable
indéfiniment dans l'historique du dépôt — la purge allège l'arborescence
courante, elle n'efface rien de versionné.

## Note — job H‍ermes `coherence-infrastructure-brute` cassé (découverte annexe)

Sans lien direct avec cette archive, mais découverte en investiguant le job
monitoring pour cette tâche : un second job cron du profil `studio`
(`coherence-infrastructure-brute`, id `ca9593f3a03d`) échoue depuis sa
création — script introuvable au chemin que H‍ermes résout pour un job
`no_agent`. Détail : [[atelier/rd/outillage/spec-archiver-monitoring-quotidien]]
§6 et `registre-problemes.md`. Signalé, non corrigé (décision humaine requise
sur le remède).
