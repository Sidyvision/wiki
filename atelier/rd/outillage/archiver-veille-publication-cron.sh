#!/bin/bash># archiver-veille-publication-cron.sh — enveloppe pour exécution en job
# Hermes no_agent. Même motif que archiver-monitoring-quotidien-cron.sh :
# le mécanisme --script d'un job no_agent ne transmet aucun argument au
# script invoqué (constaté le 2026-08-18, voir
# atelier/rd/cahiers/registre-problemes.md, entrée [2026-08-18]).
# Cette enveloppe fixe --source/--job-id/--archive/--appliquer en dur.
# Ordonné 10 minutes après le job veille-referencement-investigation-08
# (id ad3152b237bb, cron 0 11 * * *) pour que la sortie du jour soit
# déjà persistée sur disque au moment de la copie.
# Ouvert 2026-09-10 (verdict Sidy, clôture INF-15).
set -euo pipefail
exec python3 /root/wiki/atelier/rd/outillage/archiver-monitoring-quotidien.py \
  --source /root/.hermes/profiles/publication/cron/output \
  --job-id ad3152b237bb \
  --archive /root/wiki/atelier/rd/infrastructure/monitoring-archive \
  --appliquer
