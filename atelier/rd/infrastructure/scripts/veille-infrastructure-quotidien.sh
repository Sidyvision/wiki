#!/usr/bin/env bash
# Veille infrastructure quotidienne — Studio Sound Engineer (position 9, Vierge)
# Phase 3 — exécution des 3 scripts déterministes + empreinte serveur
# Canal : #infrastructure (Discord)
# Fréquence : quotidien 12:00 UTC (14:00 Paris été / 13:00 Paris hiver)
# Gouvernance : strict par défaut, suggestions validées avant journalisation
set -euo pipefail

WIKI="/root/wiki"
cd "$WIKI"

echo "=== RAPPORT STUDIO — VEILLE INFRASTRUCTURE ==="
echo "Date : $(date -u '+%Y-%m-%d %H:%M UTC')"
echo ""

# 1. Vérificateur d'invariants
echo "━━━ 1. INVARIANTS ━━━"
python3 verifier-invariants.py --racine "$WIKI" 2>&1 || true
echo ""

# 2. Cartographie
echo "━━━ 2. CARTOGRAPHIE ━━━"
python3 Graphe/generer-cartographie.py 2>&1 || true
echo ""

# 3. Fichiers non trackés
echo "━━━ 3. NON TRACKÉS ━━━"
python3 atelier/rd/outillage/detecter-non-tracke.py 2>&1 || true
echo ""

# 4. Empreinte serveur
echo "━━━ 4. EMPREINTE SERVEUR ━━━"
echo "RAM : $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "Swap : $(free -h | grep Swap | awk '{print $3 "/" $2}')"
echo "CPU : $(uptime | awk -F'load average:' '{print $2}')"
echo "Disk / : $(df -h / | tail -1 | awk '{print $3 "/" $2 " (" $5 " utilisé)"}')"
echo "Disk wiki : $(du -sh /root/wiki 2>/dev/null | awk '{print $1}')"
echo "Git : $(git rev-parse --short HEAD 2>/dev/null || echo 'N/A')"
echo "Uptime : $(uptime -p 2>/dev/null || echo 'N/A')"
echo ""

echo "━━━ 5. SUGGESTIONS ━━━"
# Suggestions automatiques basées sur les résultats
echo "[Suggestions soumises à validation avant journalisation]"
echo ""

echo "=== FIN RAPPORT ==="
echo "Gardien (vigilance infrastructure) — Studio Sound Engineer"
