---
title: "Infrastructure — Configuration Hermex (webui via Tailscale)"
type: infrastructure
tags: [rd, infrastructure, hermex, webui, tailscale, hermes]
created: 2026-08-23
updated: 2026-08-23
sources: []
links: [atelier/rd/infrastructure/incident-2026-08-23-disfonctionnements-discord-hermex.md]
---

# Configuration Hermex (webui via Tailscale)

**Date configuration :** 2026-08-23  
**Version webui :** v0.52.262  
**Statut :** opérationnel

## Architecture

```
iPhone/iPad → Tailscale VPN → https://wiki.tail7ce5ca.ts.net
                                      ↓
                              Tailscale Funnel (proxy HTTPS → HTTP)
                                      ↓
                              http://127.0.0.1:8787 (webui local)
                                      ↓
                              Hermes Agent (12 profils gateway Discord + CLI)
```

## Configuration serveur

### Webui
- **Port d'écoute :** 127.0.0.1:8787
- **Version :** v0.52.262 (expérimentale)
- **Emplacement :** `/root/hermes-webui/`
- **Logs :** `~/.hermes/webui.log`
- **PID file :** `~/.hermes/webui.pid`

### Tailscale Funnel
```bash
tailscale funnel --bg 8787
```

**État actuel :**
- URL publique : `https://wiki.tail7ce5ca.ts.net`
- Proxy : `http://127.0.0.1:8787`

### Endpoints API

| Endpoint | Méthode | Description | Statut |
|----------|---------|-------------|--------|
| `/` | GET | Interface web (HTML) | ✅ 200 |
| `/health` | GET | Healthcheck | ✅ 200 |
| `/api/sessions` | GET | Liste des sessions | ✅ 200 |
| `/api/profiles` | GET | Liste des profils | ✅ 200 |
| `/api/session/stream` | GET | SSE pour streaming temps réel | ✅ 200 |
| `/api/sessions/gateway/stream` | GET | SSE pour événements gateway | ✅ 200 |
| `/ws` | WebSocket | Non supporté | ❌ 404 |

## Accès client

### Option 1 : PWA via Safari (recommandé)

1. Ouvrir Safari sur iPhone
2. Naviguer vers `https://wiki.tail7ce5ca.ts.net`
3. Appuyer sur le bouton "Partager" (carré avec flèche)
4. Sélectionner "Sur l'écran d'accueil"
5. Confirmer avec "Ajouter"

**Fonctionnalités :**
- ✅ Utilise les endpoints SSE natifs du webui (streaming temps réel)
- ✅ Liste les sessions CLI (20 sessions visibles au 2026-08-23)
- ✅ Reprendre une session CLI : cliquer sur la session dans la sidebar, envoyer un message via `/api/chat/start` (HTTP 200 confirmé)
- ✅ Créer de nouvelles sessions depuis le webui
- ✅ Pas besoin d'app tierce
- ✅ Mise à jour automatique (pas de version à gérer)
- ✅ Authentification via Tailscale

**Test effectué (2026-08-23 18:17 UTC) :**
```bash
curl -X POST "https://wiki.tail7ce5ca.ts.net/api/chat/start" \
  -H "Content-Type: application/json" \
  -d '{"session_id":"20260823_172945_e2b43f","message":"test"}'
# → HTTP 200, turn_id retourné
```

### Option 2 : App native Hermex (déconseillé)

L'app mobile Hermex tente d'utiliser des WebSockets (`/ws`) qui ne sont pas supportés par le webui actuel. Elle retourne "Impossible de se connecter au serveur".

**Cause :** incompatibilité de protocole (WebSocket vs SSE)

**Workaround possible :** installer nginx comme reverse proxy pour supporter WebSockets, mais non testé.

## Maintenance

### Redémarrer le webui
```bash
# Arrêter
kill $(cat ~/.hermes/webui.pid)

# Démarrer
cd /root/hermes-webui
/usr/local/lib/hermes-agent/venv/bin/python server.py --host 127.0.0.1 --port 8787 --foreground
```

### Mettre à jour le webui
```bash
cd /root/hermes-webui
git pull origin master
# Puis redémarrer (voir ci-dessus)
```

### Vérifier l'état
```bash
# État du funnel
tailscale funnel status

# État du webui
curl http://127.0.0.1:8787/health

# Logs
tail -f ~/.hermes/webui.log
```

## Historique

- **2026-08-23 17:50 UTC :** reconfiguration funnel Tailscale (port 20128 → 8787)
- **2026-08-23 18:00 UTC :** mise à jour webui v0.51.923 → v0.52.262
- **2026-08-23 18:10 UTC :** diagnostic complet, recommandation PWA

## Références

- Documentation webui : `/root/hermes-webui/README.md`
- Documentation Tailscale Funnel : https://tailscale.com/kb/1223/funnel
- Incident initial : `atelier/rd/infrastructure/incident-2026-08-23-disfonctionnements-discord-hermex.md`
