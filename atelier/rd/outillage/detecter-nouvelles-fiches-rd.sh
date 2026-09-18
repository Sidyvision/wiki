#!/bin/bash
# Détecte les fiches nouvelles ou modifiées dans `atelier/rd/` depuis le dernier
# relevé consommé.
#
# Sortie : « Nouvelles fiches : » / « Fiches modifiées : » avec un chemin par
# ligne, ou « aucune-nouvelle-fiche ».
#
# Deux défauts corrigés le 2026-09-18 (rapport Studio du 2026-09-16, P3 ;
# verdict de Sidy) :
#
#   (a) LE PÉRIMÈTRE IGNORAIT `.gitignore`. `find atelier/rd -name '*.md'`
#       rendait 424 fichiers là où le dépôt en compte 251 : 173 de bruit, dont
#       les licences tierces de `.whisper-venv/`. Sur un relevé de 26 lignes,
#       19 venaient de ce venv. C'est le défaut exact qu'`OUT-C2` avait corrigé
#       pour `verifier-invariants.py` le 2026-09-01, et la leçon consignée
#       alors vaut ici mot pour mot : « le bruit a effectivement caché la seule
#       erreur vraie ». Le remède est le même — INTERROGER GIT, dans la vue
#       suivis + non-suivis non-ignorés : une fiche qui vient d'être écrite est
#       encore non suivie, et c'est précisément celle qu'on cherche.
#
#   (b) LA LECTURE N'ÉTAIT PAS IDEMPOTENTE. Le relevé avançait son instantané
#       en fin d'exécution : un second appel le même jour rendait
#       « aucune-nouvelle-fiche », et le premier appel était le seul valide —
#       ce que l'agent de veille déclarait lui-même dans son rapport, faute de
#       pouvoir l'éviter. Désormais l'instantané n'avance qu'UNE FOIS PAR JOUR :
#       tout appel ultérieur du même jour REJOUE la sortie enregistrée, à
#       l'identique. Un relevé qui change de réponse selon qu'on le lit une ou
#       deux fois n'est pas un relevé.
#
# Options :
#   --rejouer    n'avance jamais l'instantané ; rend la dernière sortie connue.
#   --forcer     avance l'instantané même si c'est le second appel du jour.

set -uo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo /root/wiki)" || exit 1

DOSSIER="atelier/rd/outillage/.snapshots-rd"
PRECEDENT="$DOSSIER/rd-snapshot-previous.txt"
COURANT="$DOSSIER/rd-snapshot-current.txt"
SORTIE="$DOSSIER/rd-derniere-sortie.txt"
JOUR="$DOSSIER/rd-dernier-jour.txt"
mkdir -p "$DOSSIER"

MODE="normal"
for arg in "$@"; do
    case "$arg" in
        --rejouer) MODE="rejouer" ;;
        --forcer)  MODE="forcer" ;;
    esac
done

# (a) — périmètre git, jamais le disque nu.
git ls-files --cached --others --exclude-standard -- atelier/rd \
    | grep '\.md$' \
    | while IFS= read -r f; do
          [ -f "$f" ] && printf '%s %s\n' "$f" "$(stat -c '%Y' "$f")"
      done | sort > "$COURANT"

# (b) — un second appel le même jour rejoue, il ne recalcule pas.
AUJOURDHUI="$(date +%F)"
DERNIER="$(cat "$JOUR" 2>/dev/null || echo '')"
if [ "$MODE" = "rejouer" ] || { [ "$MODE" != "forcer" ] && [ "$DERNIER" = "$AUJOURDHUI" ]; }; then
    if [ -f "$SORTIE" ]; then
        cat "$SORTIE"
        echo "(rejeu — relevé déjà consommé le $DERNIER ; --forcer pour avancer)"
        exit 0
    fi
fi

if [ ! -f "$PRECEDENT" ]; then
    cp "$COURANT" "$PRECEDENT"
    echo "aucune-nouvelle-fiche" | tee "$SORTIE"
    echo "$AUJOURDHUI" > "$JOUR"
    exit 0
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cut -d' ' -f1 "$COURANT"   | sort > "$TMP/courant"
cut -d' ' -f1 "$PRECEDENT" | sort > "$TMP/precedent"
comm -23 "$TMP/courant" "$TMP/precedent" > "$TMP/nouveaux"
comm -12 "$TMP/courant" "$TMP/precedent" > "$TMP/communs"

: > "$TMP/modifies"
while IFS= read -r fichier; do
    c="$(grep -F "$fichier " "$COURANT"   | head -1 | cut -d' ' -f2)"
    p="$(grep -F "$fichier " "$PRECEDENT" | head -1 | cut -d' ' -f2)"
    [ "$c" != "$p" ] && printf '%s\n' "$fichier" >> "$TMP/modifies"
done < "$TMP/communs"

{
    if [ ! -s "$TMP/nouveaux" ] && [ ! -s "$TMP/modifies" ]; then
        echo "aucune-nouvelle-fiche"
    else
        if [ -s "$TMP/nouveaux" ]; then
            echo "Nouvelles fiches :"; cat "$TMP/nouveaux"
        fi
        if [ -s "$TMP/modifies" ]; then
            echo "Fiches modifiées :"; cat "$TMP/modifies"
        fi
    fi
} | tee "$SORTIE"

cp "$COURANT" "$PRECEDENT"
echo "$AUJOURDHUI" > "$JOUR"
