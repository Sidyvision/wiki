---
title: "Charte — Archive du monitoring infrastructure quotidien"
type: infrastructure
tags: [rd, infrastructure, monitoring, hermes, archive]
created: 2026-08-18
updated: 2026-08-19
sources: []
links: ["[[atelier/rd/outillage/spec-archiver-monitoring-quotidien]]", "[[atelier/rd/infrastructure/activation-monitoring-studio-cron-2026-08-17]]", "[[atelier/rd/cahiers/registre-problemes]]"]
infra_verif:
  - profil: studio
    cron_job: archiver-monitoring-quotidien
  - profil: studio
    cron_job: coherence-infrastructure-brute
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
une copie par exécution du job Hermes `monitoring-infrastructure-quotidien`
(profil `studio`, id `41dc3e7e492c`), format `.txt` **délibérément**, jamais
`.md` (raison détaillée : [[atelier/rd/outillage/spec-archiver-monitoring-quotidien]]
§3 — le rapport cite des tokens `[[...]]` littéraux qui feraient s'auto-
déclencher `verifier-invariants.py`/`generer-cartographie.py` sur l'archive
elle-même). Ces fichiers ne portent pas de Sceau : ce ne sont pas des fiches
du dépôt, mais un journal technique brut.

## Alimentation

Script déterministe [[atelier/rd/outillage/spec-archiver-monitoring-quotidien|
archiver-monitoring-quotidien.py]] : copie ce que Hermes a déjà persisté sur
disque (`/root/.hermes/profiles/studio/cron/output/`), sans toucher au job de
production ni à Discord. Purge les copies au-delà de 40 jours.

**Ingestion — cron dédié, mis en place le 2026-08-18** (feu vert Sidy en
session : « tu as le feu vert pour tout rétablir »). Job Hermes créé, profil
`studio` : `archiver-monitoring-quotidien` (id `5eb46eed6ba0`, `no_agent`,
cron `10 12 * * *` — 10 minutes après `monitoring-infrastructure-quotidien`,
pour que la sortie `.txt` du jour soit déjà persistée sur disque au moment
de la copie). Le script réel (`atelier/rd/outillage/archiver-monitoring-
quotidien.py`) prend des arguments (`--source`/`--job-id`/`--archive`/
`--appliquer`) qu'un job `no_agent` ne peut pas transmettre (aucun canal
d'arguments — constaté en investiguant le job `coherence-infrastructure-
brute`, cf. §« Note » ci-dessous) : le job appelle donc une enveloppe,
`atelier/rd/outillage/archiver-monitoring-quotidien-cron.sh`, qui fixe ces
arguments en dur. Vérifié par lecture directe de la sortie persistée du job
(jamais sur la seule foi de `last_status: "ok"`, §VIII.2 du protocole
racine) : « 2 sortie(s) source, 2 déjà archivée(s), 0 à copier » — état
attendu, cohérent avec l'archivage manuel déjà fait le 2026-08-18.
`infra_verif` ci-dessus trace la présence du job de façon mécanique.

## Rétention

40 jours glissants dans ce dossier. **Ce n'est pas une fenêtre d'historique
absolue** : tout fichier commité dans git avant sa purge reste retrouvable
indéfiniment dans l'historique du dépôt — la purge allège l'arborescence
courante, elle n'efface rien de versionné.

## Note — job Hermes `coherence-infrastructure-brute` réparé (2026-08-18)

Découvert cassé en investiguant le job monitoring pour cette tâche (script
introuvable au chemin que Hermes résout pour un job `no_agent`), puis
réparé le même jour (feu vert Sidy) via une enveloppe symétrique à celle
ci-dessus — `atelier/rd/outillage/verifier-coherence-infrastructure-cron.sh`
— après qu'un premier remède par lien symbolique a été rejeté par Hermes
lui-même (garde-fou de résolution de chemin canonique), puis qu'une copie
réelle sans enveloppe a révélé un second défaut, plus grave : un faux
succès silencieux (0 affirmation vérifiée au lieu de 3, `--racine` non
transmis). Détail complet des deux défauts et de leur résolution :
[[atelier/rd/cahiers/registre-problemes]], entrée `[2026-08-18]` (« Suite de
l'entrée précédente »).
