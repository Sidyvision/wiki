#!/bin/bash
# Sert atelier/rd/instrument/ en HTTP, lié à l'IP Tailscale courante uniquement
# (jamais 0.0.0.0 : le prototype ne doit être atteignable que depuis le tailnet).
# Résolution dynamique de l'IP à chaque démarrage : survit à un changement d'IP
# Tailscale après redémarrage du serveur.
set -euo pipefail
IP="$(tailscale ip -4)"
cd /root/wiki/atelier/rd/instrument
exec python3 -m http.server 8420 --bind "$IP"
