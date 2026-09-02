#!/bin/bash
# OCR page-par-page -> markdown. Usage: ocr_pdf2md.sh <pdf> <sortie.md> <titre>
set -u
PDF="$1"; OUT="$2"; TITRE="$3"
WORK=$(mktemp -d /tmp/ocrwk.XXXX)
NP=$(pdfinfo "$PDF" | awk '/^Pages:/{print $2}')
echo "[$(date +%T)] $PDF : $NP pages -> $OUT"

ocr_one() {
  p=$1; pdf=$2; wk=$3
  pdftoppm -r 300 -gray -f $p -l $p "$pdf" "$wk/pg$p" 2>/dev/null
  img=$(ls "$wk"/pg$p-*.pgm 2>/dev/null | head -1)
  [ -z "$img" ] && { echo "" > "$wk/$p.txt"; return; }
  tesseract "$img" "$wk/$p" -l eng --psm 1 2>/dev/null
  rm -f "$img"
}
export -f ocr_one
seq 1 $NP | xargs -P 2 -I{} bash -c 'ocr_one {} "$0" "$1"' "$PDF" "$WORK"

{
  echo "---"
  echo "titre: \"$TITRE\""
  echo "source: $PDF"
  echo "pages: $NP"
  echo "conversion: pdftoppm 300dpi + tesseract 5 (eng), $(date -I)"
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
