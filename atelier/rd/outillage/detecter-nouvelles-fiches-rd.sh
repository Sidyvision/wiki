#!/bin/bash
# Détecte les nouvelles fiches dans atelier/rd/ depuis le dernier snapshot
# Sortie : liste des nouveaux fichiers (un par ligne) ou "aucune-nouvelle-fiche"
# Usage : ./detecter-nouvelles-fiches-rd.sh

SNAPSHOT_DIR="/root/wiki/atelier/rd/outillage/.snapshots-rd"
SNAPSHOT_PREV="$SNAPSHOT_DIR/rd-snapshot-previous.txt"
SNAPSHOT_CURR="$SNAPSHOT_DIR/rd-snapshot-current.txt"

# Créer le répertoire de snapshots s'il n'existe pas
mkdir -p "$SNAPSHOT_DIR"

# Générer le snapshot courant (chemin + timestamp de modification)
find atelier/rd -type f -name "*.md" -exec stat -c '%n %Y' {} \; | sort > "$SNAPSHOT_CURR"

# Si le snapshot précédent n'existe pas, initialiser et sortir
if [ ! -f "$SNAPSHOT_PREV" ]; then
    cp "$SNAPSHOT_CURR" "$SNAPSHOT_PREV"
    echo "aucune-nouvelle-fiche"
    exit 0
fi

# Comparer : extraire les chemins des fichiers modifiés ou nouveaux
# Un fichier est "nouveau" s'il est dans CURR mais pas dans PREV
# Un fichier est "modifié" si son timestamp a changé

comm -23 <(cut -d' ' -f1 "$SNAPSHOT_CURR" | sort) <(cut -d' ' -f1 "$SNAPSHOT_PREV" | sort) > /tmp/nouveaux-fichiers.txt
comm -12 <(cut -d' ' -f1 "$SNAPSHOT_CURR" | sort) <(cut -d' ' -f1 "$SNAPSHOT_PREV" | sort) > /tmp/fichiers-communs.txt

# Pour les fichiers communs, vérifier si le timestamp a changé
MODIFIES=""
while IFS= read -r fichier; do
    timestamp_curr=$(grep "^$fichier " "$SNAPSHOT_CURR" | cut -d' ' -f2)
    timestamp_prev=$(grep "^$fichier " "$SNAPSHOT_PREV" | cut -d' ' -f2)
    if [ "$timestamp_curr" != "$timestamp_prev" ]; then
        MODIFIES="$MODIFIES$fichier\n"
    fi
done < /tmp/fichiers-communs.txt

# Afficher les résultats
NOUVEAUX=$(cat /tmp/nouveaux-fichiers.txt 2>/dev/null)

if [ -z "$NOUVEAUX" ] && [ -z "$MODIFIES" ]; then
    echo "aucune-nouvelle-fiche"
else
    if [ -n "$NOUVEAUX" ]; then
        echo "Nouvelles fiches :"
        echo "$NOUVEAUX"
    fi
    if [ -n "$MODIFIES" ]; then
        echo "Fiches modifiées :"
        echo -e "$MODIFIES"
    fi
fi

# Mettre à jour le snapshot précédent pour la prochaine exécution
cp "$SNAPSHOT_CURR" "$SNAPSHOT_PREV"

# Nettoyage
rm -f /tmp/nouveaux-fichiers.txt /tmp/fichiers-communs.txt
