#!/bin/bash
# Veille automatique Studio — enveloppe cron
# Appelée par le job cron Hermes (profil studio, 6h du matin)
#
# Rôle :
#   - Exécute le script Python de veille (GitHub + arXiv)
#   - Archive les fiches de plus de 40 jours (cohérent avec monitoring-archive)
#   - Signale les résonances théoriques détectées (pour Choura)
#
# Verdict Sidy 2026-08-31 (proposition-veille-automatique-studio-2026-08-31.md).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WIKI_ROOT="/root/wiki"
VEILLE_DIR="$WIKI_ROOT/atelier/rd/veille"
ARCHIVE_DIR="$VEILLE_DIR/archive"

echo "[$(date -Iseconds)] Veille automatique Studio — démarrage"

# 1. Exécution du script principal
python3 "$SCRIPT_DIR/veille-automatique-studio.py"
EXIT_CODE=$?

# 2. Archivage des fiches anciennes (40 jours)
# Déplace les fiches non modifiées depuis 40 jours dans archive/
mkdir -p "$ARCHIVE_DIR"
ARCHIVE_COUNT=0

# Parcourt les .md de veille/ (pas les sous-dossiers, pas archive/)
while IFS= read -r -d '' fiche; do
    # Vérifie la date de modification (40 jours = 3456000 secondes)
    AGE_SECONDS=$(( $(date +%s) - $(stat -c %Y "$fiche") ))
    if [ "$AGE_SECONDS" -gt 3456000 ]; then
        mv "$fiche" "$ARCHIVE_DIR/"
        ARCHIVE_COUNT=$((ARCHIVE_COUNT + 1))
    fi
done < <(find "$VEILLE_DIR" -maxdepth 1 -name "*.md" -type f -print0)

if [ "$ARCHIVE_COUNT" -gt 0 ]; then
    echo "[$(date -Iseconds)] Archivage : $ARCHIVE_COUNT fiche(s) déplacée(s) vers archive/"
fi

# 3. Signal pour le cron
if [ $EXIT_CODE -eq 2 ]; then
    echo "RESONANCE_DETECTEE — Studio signalera dans son tour de Choura"
fi

echo "[$(date -Iseconds)] Veille automatique Studio — terminé"
exit 0
