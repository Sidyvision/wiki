#!/bin/bash
# verifier-coherence-infrastructure-cron.sh — enveloppe pour exécution en job
# H‍ermes no_agent. Motif : le mécanisme --script d'un job no_agent ne transmet
# aucun argument au script invoqué, et le champ workdir du job (/root/wiki)
# ne s'applique pas au cwd d'un script no_agent (constaté le 2026-08-18 : le
# script réel, sans --racine, retourne silencieusement "aucune affirmation
# trouvée" au lieu d'une erreur — faux négatif, pas un échec visible). Cette
# enveloppe fixe --racine en dur pour éliminer la dépendance au cwd effectif
# du process H‍ermes. Voir atelier/rd/cahiers/registre-problemes.md,
# entrée [2026-08-18] (mise à jour) et
# atelier/rd/outillage/spec-archiver-monitoring-quotidien.md.
set -euo pipefail
exec python3 /root/wiki/atelier/rd/outillage/verifier-coherence-infrastructure.py --racine /root/wiki
