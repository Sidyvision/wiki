#!/bin/bash
# OCR page-par-page -> markdown.
# Usage: ocr-scan-vers-markdown.sh <pdf> <sortie.md> <titre> [langue]
#   langue : code tesseract, defaut 'eng'. Ex: fra, ara, fra+ara.
#   (parametre ouvert le 2026-09-02 : la langue etait figee a 'eng' dans la
#    commande ET dans le frontmatter, ce dernier mentait des qu'on patchait
#    la commande a la main.)
set -u
PDF="$1"; OUT="$2"; TITRE="$3"; OCRLANG="${4:-eng}"

# Garde : une langue non installee produirait un fichier vide sans erreur —
# une tache de fond echouerait alors en silence (meme piege que le 'chmod +x'
# refuse, cf. spec §6). On constate et on sort, on ne corrige pas.
for l in $(echo "$OCRLANG" | tr '+' ' '); do
  if ! tesseract --list-langs 2>/dev/null | tail -n +2 | grep -qx "$l"; then
    echo "ERREUR: langue tesseract '$l' non installee (paquet tesseract-ocr-$l)" >&2
    echo "langues disponibles : $(tesseract --list-langs 2>/dev/null | tail -n +2 | tr '\n' ' ')" >&2
    exit 2
  fi
done

WORK=$(mktemp -d /tmp/ocrwk.XXXX)
NP=$(pdfinfo "$PDF" | awk '/^Pages:/{print $2}')
echo "[$(date +%T)] $PDF : $NP pages -> $OUT"

ocr_one() {
  p=$1; pdf=$2; wk=$3
  pdftoppm -r 300 -gray -f $p -l $p "$pdf" "$wk/pg$p" 2>/dev/null
  img=$(ls "$wk"/pg$p-*.pgm 2>/dev/null | head -1)
  [ -z "$img" ] && { echo "" > "$wk/$p.txt"; return; }
  tesseract "$img" "$wk/$p" -l "$OCRLANG" --psm 1 2>/dev/null
  rm -f "$img"
}
export -f ocr_one
export OCRLANG
seq 1 $NP | xargs -P 2 -I{} bash -c 'ocr_one {} "$0" "$1"' "$PDF" "$WORK"

{
  echo "---"
  echo "titre: \"$TITRE\""
  echo "source: $PDF"
  echo "pages: $NP"
  echo "conversion: pdftoppm 300dpi + tesseract 5 ($OCRLANG), $(date -I)"
  echo "---"
  echo
  for p in $(seq 1 $NP); do
    echo "<!-- page $p -->"
    echo
    if [ -s "$WORK/$p.txt" ]; then cat "$WORK/$p.txt"; fi
    echo
  done
} > "$OUT"
rm -rf "$WORK"
echo "[$(date +%T)] FINI $OUT : $(wc -c < "$OUT") octets"
