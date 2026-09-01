#!/usr/bin/env bash
# Installe les hooks git du dépôt.
#
# Ouvert le 2026-09-01 (chantier PRO-01). Motif : `.git/hooks/` n'est pas
# versionné. Le hook `pre-commit` d'hygiène Unicode existait depuis le
# 2026-08-22 — écrit après l'incident ZWJ — mais **uniquement sur cette
# machine** : un clone frais du dépôt repartait sans lui, et personne ne
# l'aurait su. Un garde-fou qui ne survit pas à un clone n'est pas un garde-fou
# du dépôt, c'est une habitude locale.
#
# Les hooks vivent donc ici, suivis par git, et ce script les installe.
#
#   bash atelier/rd/outillage/hooks/installer-hooks.sh
#
# Aucune sauvegarde n'est jamais écrasée : un hook déjà en place et différent
# est mis de côté, horodaté, avant d'être remplacé (Cmd 10 — jamais de
# suppression sèche).

set -euo pipefail

RACINE="$(git rev-parse --show-toplevel)"
SOURCE="$RACINE/atelier/rd/outillage/hooks"
CIBLE="$RACINE/.git/hooks"
HORODATAGE="$(date +%Y%m%d-%H%M%S)"

if [ ! -d "$CIBLE" ]; then
    echo "Pas de $CIBLE — ce n'est pas un dépôt git normal." >&2
    exit 1
fi

echo "Installation des hooks depuis $SOURCE"

for chemin in "$SOURCE"/*; do
    nom="$(basename "$chemin")"
    case "$nom" in
        installer-hooks.sh|README.md) continue ;;
    esac

    destination="$CIBLE/$nom"

    if [ -f "$destination" ] && ! cmp -s "$chemin" "$destination"; then
        sauvegarde="$destination.bak-$HORODATAGE"
        cp "$destination" "$sauvegarde"
        echo "  · $nom — version en place différente, sauvegardée :"
        echo "      $(basename "$sauvegarde")"
    fi

    install -m 0755 "$chemin" "$destination"
    echo "  ✓ $nom installé"
done

echo
echo "Vérification :"
for nom in pre-commit pre-push; do
    if [ -x "$CIBLE/$nom" ]; then
        echo "  ✓ $nom présent et exécutable"
    else
        echo "  ✗ $nom manquant ou non exécutable"
    fi
done

cat <<'FIN'

Rappel : ces hooks sont des garde-fous, pas des serrures.
  git commit --no-verify   contourne le pre-commit
  git push   --no-verify   contourne le pre-push
Les contourner est une décision assumée ; les subir par inattention ne l'est pas.
FIN
