#!/usr/bin/env bash
# =============================================================================
# ornith-test.sh — Test de non-régression de l'intégration _inbox/
#   But : vérifier qu'un modèle local (Ornith) motorisant Claude Code intègre un
#   lot témoin aussi proprement qu'Opus (la référence = l'état committé du dépôt).
#
#   Bac à sable ISOLÉ : copie du dépôt SANS .git (réinitialisé sans remote) ⇒
#   même si le modèle suit le protocole et fait `git push`, il ne peut PAS
#   atteindre origin/main. Le vrai dépôt /root/wiki n'est jamais touché.
#
#   Lot témoin : 3 fiches atelier/materiel + 1 fiche meta (taekwondo).
#   (album-personnel est exclu : sa référence a été enrichie plus tard par la
#    catégorie C, ce qui rendrait la comparaison ambiguë.)
#
#   Sous-commandes :
#     prepare   construit le bac à sable prêt à intégrer (à lancer AVANT le test)
#     compare   compare le résultat du modèle à la référence Opus (APRÈS le test)
#     selftest  intégration simulée parfaite (copie de la référence) → doit PASSER
#     clean     supprime le bac à sable
# =============================================================================
set -euo pipefail

WIKI=/root/wiki
ROOT=/root/ornith-test
SANDBOX="$ROOT/sandbox"
GOLDEN="$ROOT/golden"

WITNESS=(
  "atelier/materiel/neve-1073spx.md"
  "atelier/materiel/tascam-model-12.md"
  "atelier/materiel/technics-su-8080.md"
  "meta/2026-06-20_taekwondo-hansu.md"
)
MAT_SLUGS=( neve-1073spx tascam-model-12 technics-su-8080 )

say() { printf '\n\033[1m%s\033[0m\n' "$*"; }

# ---------------------------------------------------------------------------
cmd_prepare() {
  command -v git >/dev/null || { echo "git requis"; exit 1; }
  rm -rf "$ROOT"; mkdir -p "$GOLDEN" "$SANDBOX"

  say "[1/5] Capture de la RÉFÉRENCE Opus (état committé actuel)"
  for f in "${WITNESS[@]}"; do
    mkdir -p "$GOLDEN/$(dirname "$f")"; cp "$WIKI/$f" "$GOLDEN/$f"
  done
  cp "$WIKI/doctrinal/index.md"   "$GOLDEN/index.md"
  cp "$WIKI/doctrinal/annales.md" "$GOLDEN/annales.md"
  echo "  référence: ${#WITNESS[@]} fiches + index.md + annales.md"

  say "[2/5] Copie ISOLÉE du dépôt (sans .git, sans remote)"
  cp -a "$WIKI/." "$SANDBOX/"
  rm -rf "$SANDBOX/.git"

  say "[3/5] Rembobinage du lot témoin (état pré-intégration)"
  # 3a) supprimer les fichiers produits par le lot témoin
  for f in "${WITNESS[@]}"; do rm -f "$SANDBOX/$f"; done
  # 3b) remettre §VIII Matériel à "(vide)"
  python3 - "$SANDBOX/doctrinal/index.md" <<'PY'
import re,sys
p=sys.argv[1]; t=open(p,encoding="utf-8").read()
t=re.sub(r"(### Matériel \(`atelier/materiel/`\)\n)(.*?)(\n### Entretiens)",
         r"\1*(vide)*\3", t, flags=re.S)
open(p,"w",encoding="utf-8").write(t)
PY
  # 3c) retirer l'entrée d'annales "Catégorie B" pour forcer le modèle à la réécrire
  python3 - "$SANDBOX/doctrinal/annales.md" <<'PY'
import re,sys
p=sys.argv[1]; lines=open(p,encoding="utf-8").read().split("\n")
out=[]; skip=False
for l in lines:
    if l.startswith("## [") and "Catégorie B, atelier" in l: skip=True; continue
    if skip and l.startswith("## ["): skip=False
    if not skip: out.append(l)
open(p,"w",encoding="utf-8").write("\n".join(out))
PY

  say "[4/5] Chargement du sas _inbox/ (entrées du lot témoin + UPDATES.md)"
  find "$SANDBOX/_inbox" -maxdepth 1 -type f ! -name 'README.md' -delete 2>/dev/null || true
  for f in "${WITNESS[@]}"; do cp "$GOLDEN/$f" "$SANDBOX/_inbox/$(basename "$f")"; done
  cat > "$SANDBOX/_inbox/UPDATES.md" <<'UP'
# UPDATES — Lot témoin de test (catégorie B réduite)

> ⚠️ CECI EST UN TEST DE NON-RÉGRESSION. Intègre normalement selon CLAUDE.md,
> MAIS **NE COMMIT PAS et NE PUSH PAS** (bac à sable jetable).

## Pages à classer (4)
- `neve-1073spx.md`        → `atelier/materiel/neve-1073spx.md`
- `tascam-model-12.md`     → `atelier/materiel/tascam-model-12.md`
- `technics-su-8080.md`    → `atelier/materiel/technics-su-8080.md`
- `2026-06-20_taekwondo-hansu.md` → `meta/2026-06-20_taekwondo-hansu.md`
  (en meta/, PAS en atelier/ : ni audio ni création artistique au sens du protocole)

## Catalogue (doctrinal/index.md, §VIII → Matériel)
- [[atelier/materiel/neve-1073spx|Neve 1073SPX (préampli/EQ)]]
- [[atelier/materiel/tascam-model-12|Tascam Model 12 (table/interface)]]
- [[atelier/materiel/technics-su-8080|Technics SU-8080 (ampli hi-fi vintage)]]

## Annales
Ajouter une entrée datée (préfixe greppable `## [YYYY-MM-DD] archivage | …`)
mentionnant le matériel audio et taekwondo-hansu.
UP

  # baseline git SANS remote : 'git status'/'diff' exploitables, et 'git push' impossible
  git -C "$SANDBOX" init -q
  git -C "$SANDBOX" -c user.email=test@local -c user.name=test add -A
  git -C "$SANDBOX" -c user.email=test@local -c user.name=test commit -q -m "baseline pre-integration (test)"

  say "[5/5] Bac à sable prêt : $SANDBOX"
  cat <<EOF

PROCHAINE ÉTAPE (test réel avec Ornith) :
  1) Ouvre le tunnel SSH vers le GPU (cf. runbook §4).
  2) Dans un shell, pose les variables ANTHROPIC_* sur Ornith (runbook §5).
  3) cd $SANDBOX && claude
     puis : « intègre _inbox/ selon UPDATES.md et CLAUDE.md » (NE PAS committer/pusher)
  4) Reviens ici et lance :  bash $WIKI/meta/projet-unifie/ornith-test.sh compare
EOF
}

# ---------------------------------------------------------------------------
cmd_compare() {
  [ -d "$SANDBOX" ] || { echo "Pas de bac à sable. Lance 'prepare' d'abord."; exit 1; }
  local pass=0 fail=0

  say "A. Contenu des fiches produites (doit être IDENTIQUE à la référence Opus)"
  for f in "${WITNESS[@]}"; do
    if [ ! -f "$SANDBOX/$f" ]; then
      echo "  ✗ MANQUANT  $f"; fail=$((fail+1))
    elif diff -q "$GOLDEN/$f" "$SANDBOX/$f" >/dev/null; then
      echo "  ✓ identique $f"; pass=$((pass+1))
    else
      echo "  ✗ DIFFÈRE   $f"; fail=$((fail+1))
      diff -u "$GOLDEN/$f" "$SANDBOX/$f" | sed 's/^/      /' | head -25
    fi
  done

  say "B. Catalogue (doctrinal/index.md §VIII → Matériel)"
  for s in "${MAT_SLUGS[@]}"; do
    if grep -q "atelier/materiel/$s" "$SANDBOX/doctrinal/index.md"; then
      echo "  ✓ lien présent : $s"; pass=$((pass+1))
    else
      echo "  ✗ lien ABSENT  : $s"; fail=$((fail+1))
    fi
  done

  say "C. Annales (nouvelle entrée mentionnant le lot)"
  if [ -d "$SANDBOX/.git" ] && ! git -C "$SANDBOX" diff --quiet -- doctrinal/annales.md 2>/dev/null \
     && grep -qiE 'neve|tascam|technics|taekwondo' "$SANDBOX/doctrinal/annales.md"; then
    echo "  ✓ annales modifiées + mention du lot"; pass=$((pass+1))
  else
    echo "  ✗ pas de nouvelle entrée d'annales mentionnant le lot"; fail=$((fail+1))
  fi

  say "D. Effets de bord (git status du bac à sable — modifications inattendues ?)"
  if [ -d "$SANDBOX/.git" ]; then
    git -C "$SANDBOX" status --short | sed 's/^/    /' || true
    echo "    (attendu : 4 fiches créées + index.md + annales.md + _inbox vidé)"
  else
    echo "    (.git absent — bac à sable non encore committé en baseline)"
  fi

  say "VERDICT : $pass ✓ / $fail ✗"
  if [ "$fail" -eq 0 ]; then
    echo "  ✅ Ornith équivaut à Opus sur ce lot — rôle d'intégration VIABLE."
  else
    echo "  ⚠️  Écarts détectés — renforcer les scripts déterministes / garder l'hybride, puis re-tester."
  fi
}

# ---------------------------------------------------------------------------
cmd_selftest() {
  say "SELFTEST — intégration simulée PARFAITE (copie de la référence) → doit tout PASSER"
  cmd_prepare >/dev/null
  for f in "${WITNESS[@]}"; do
    mkdir -p "$SANDBOX/$(dirname "$f")"; cp "$GOLDEN/$f" "$SANDBOX/$f"
  done
  cp "$GOLDEN/index.md"   "$SANDBOX/doctrinal/index.md"
  cp "$GOLDEN/annales.md" "$SANDBOX/doctrinal/annales.md"
  find "$SANDBOX/_inbox" -maxdepth 1 -type f ! -name 'README.md' -delete 2>/dev/null || true
  cmd_compare
}

cmd_clean() { rm -rf "$ROOT"; echo "Bac à sable supprimé."; }

case "${1:-}" in
  prepare)  cmd_prepare ;;
  compare)  cmd_compare ;;
  selftest) cmd_selftest ;;
  clean)    cmd_clean ;;
  *) echo "Usage: $0 {prepare|compare|selftest|clean}"; exit 1 ;;
esac
