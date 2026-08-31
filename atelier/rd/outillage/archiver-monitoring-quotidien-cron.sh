#!/bin/bash
# archiver-monitoring-quotidien-cron.sh — enveloppe pour exécution en job
# Hermes no_agent. Même motif que verifier-coherence-infrastructure-cron.sh :
# le mécanisme --script d'un job no_agent ne transmet aucun argument au
# script invoqué (constaté le 2026-08-18, voir
# atelier/rd/cahiers/registre-problemes.md, entrée [2026-08-18]). Cette
# enveloppe fixe --source/--job-id/--archive/--appliquer en dur. Ordonnancé
# 10 minutes après le job monitoring-infrastructure-quotidien (id
# 41dc3e7e492c, cron 0 12 * * *) pour que la sortie du jour soit déjà
# persistée sur disque au moment de la copie. Voir
# atelier/rd/outillage/spec-archiver-monitoring-quotidien.md.
set -euo pipefail
exec python3 /root/wiki/atelier/rd/outillage/archiver-monitoring-quotidien.py \
  --source /root/.hermes/profiles/studio/cron/output \
  --job-id 41dc3e7e492c \
  --archive /root/wiki/atelier/rd/infrastructure/monitoring-archive \
  --appliquer
