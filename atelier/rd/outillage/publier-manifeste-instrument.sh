#!/usr/bin/env bash
# =============================================================================
# publier-manifeste-instrument.sh — pousse le manifeste du wiki vers le dépôt frère
#
#   Chantier INF-13. Étage MANUEL du flux à sens unique du §VII :
#       instrument-donnees.yaml → generer-manifeste.py → wiki-manifest.json
#                              → Sidyvision/instrument (src/wiki-manifest.json)
#
#   Le manifeste est POUSSÉ depuis le wiki, jamais tiré par l'interface : un dépôt
#   destiné à devenir public ne détient à aucun moment de droit de lecture sur le
#   wiki privé.
#
#   Déterministe, AUCUN LLM dans la boucle — même famille que verifier-invariants.py
#   et verifier-coherence-infrastructure.py.
#
#   Usage :
#     bash publier-manifeste-instrument.sh              # constate, n'écrit rien
#     bash publier-manifeste-instrument.sh --publier    # copie + commit côté frère
#
#   L'automatisation (workflow GitHub poussant via secret PAT) est SPÉCIFIÉE mais
#   NON ACTIVÉE : un jeton d'écriture croisée engage (Cmd 13), et l'article 4 de la
#   convention Sashimono veut le montage à blanc avant le définitif.
# =============================================================================
set -euo pipefail

WIKI="${WIKI:-/root/wiki}"
FRERE="${FRERE:-/root/instrument}"
MANIFESTE="$WIKI/atelier/rd/instrument/wiki-manifest.json"
CIBLE="$FRERE/src/wiki-manifest.json"
PUBLIER=0
[ "${1:-}" = "--publier" ] && PUBLIER=1

echo "== publier-manifeste-instrument =="
echo "   wiki  : $WIKI"
echo "   frère : $FRERE"

# --- 1. Régénérer dans un fichier temporaire, jamais par-dessus le versionné -----
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
python3 "$WIKI/atelier/rd/outillage/generer-manifeste.py" \
        --repo "$WIKI" --sortie "$TMP/manifeste.json" >/dev/null

# --- 2. Comparer SUR LE FOND -----------------------------------------------------
#   generated_at et source_commit changent à chaque exécution : ce sont des tampons
#   de provenance, pas des changements de contenu. Les compter comme tels ferait
#   publier à chaque passe et rendrait l'historique du dépôt frère illisible.
normaliser() {
  python3 -c '
import json,sys
d=json.load(open(sys.argv[1]))
for tampon in ("generated_at","source_commit"):
    d.pop(tampon,None)
print(json.dumps(d,sort_keys=True,ensure_ascii=False,indent=1))
' "$1"
}

if [ ! -f "$MANIFESTE" ]; then
  echo "ERREUR : manifeste versionné absent — $MANIFESTE" >&2; exit 2
fi

if diff -q <(normaliser "$MANIFESTE") <(normaliser "$TMP/manifeste.json") >/dev/null; then
  echo "   ✓ manifeste versionné à jour sur le fond (tampons de provenance exclus)"
else
  echo "   ⚠ DIVERGENCE DE FOND entre instrument-donnees.yaml et le manifeste versionné."
  echo "     Le manifeste n'est PAS régénéré d'office : le fait se rapporte (Cmd 12)."
  echo "     Régénérer explicitement, relire le diff, puis relancer."
  diff <(normaliser "$MANIFESTE") <(normaliser "$TMP/manifeste.json") | head -40 || true
  exit 3
fi

# --- 3. Comparer au dépôt frère --------------------------------------------------
if [ ! -d "$FRERE/.git" ]; then
  echo "   ⚠ dépôt frère absent en $FRERE — rien à publier."; exit 0
fi

if [ -f "$CIBLE" ] && diff -q <(normaliser "$MANIFESTE") <(normaliser "$CIBLE") >/dev/null; then
  echo "   ✓ le dépôt frère porte déjà ce manifeste — rien à faire."
  exit 0
fi

echo "   → le dépôt frère est en retard sur le manifeste du wiki."
if [ "$PUBLIER" -eq 0 ]; then
  echo "     (constat seul ; relancer avec --publier pour copier et commiter)"
  exit 0
fi

# --- 4. Publier ------------------------------------------------------------------
SHA="$(git -C "$WIKI" rev-parse --short HEAD)"
mkdir -p "$(dirname "$CIBLE")"
cp "$MANIFESTE" "$CIBLE"
git -C "$FRERE" add src/wiki-manifest.json
# `MANIFESTE_RECU=1` : le garde-fou pre-commit du dépôt frère refuse toute
# modification de src/wiki-manifest.json, sauf publication légitime déclarée.
# Ce script EST cette voie — il le déclare donc lui-même.
#
# ⚠ DÉFAUT CORRIGÉ LE 2026-09-02 : il ne le déclarait pas, de sorte que la seule
# voie légitime de publication était systématiquement REFUSÉE par le garde-fou
# écrit pour la protéger. Le défaut n'avait jamais paru parce que `--publier`
# n'avait pas été rejoué depuis la pose du hook (INF-14). Même famille que
# PRO-01 : un contrôle dont on n'avait pas éprouvé le comportement réel.
MANIFESTE_RECU=1 git -C "$FRERE" commit -q -m "manifeste reçu du wiki ($SHA)

Poussé par publier-manifeste-instrument.sh. Le manifeste est reçu, jamais
édité ici : la source est instrument-donnees.yaml au dépôt wiki (§VII, flux
à sens unique)."
echo "   ✓ publié — commit créé dans $FRERE (source wiki $SHA). Push non fait : Cmd 13."
