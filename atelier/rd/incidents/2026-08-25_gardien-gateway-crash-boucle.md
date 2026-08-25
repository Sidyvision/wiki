---
title: "Gardien — Gateway crash en boucle (exit code 1)"
type: outillage
statut_experience: reproduit
tags: [hermes, gateway, gardien, crash, systemd]
created: 2026-08-25
updated: 2026-08-25
sources: []
links: []
---

# Gardien — Gateway crash en boucle (exit code 1)

## Résumé

Le 2026-08-25, le gateway du profil `gardien` crashait en boucle (exit code 1, restart counter = 3). Le diagnostic a révélé un conflit entre systemd et le module "self-improvement review" lors du redémarrage automatique.

## Chronologie

- **2026-08-25 ~16:00 UTC** : Sidy signale que le Gardien est injoignable sur Discord
- **Diagnostic initial** : PID 2181543 actif, mais WebSocket Discord `socket_closed` (16:04 et 18:32)
- **Tentative restart** : `systemctl --user restart hermes-gateway-gardien` → bloqué (on ne peut pas restart depuis l'intérieur d'un gateway)
- **Kill manuel** : `kill 2181543` → systemd relance automatiquement, mais crash immédiat
- **Logs systemd** : restart counter = 3, exit code 1 systématique
- **Délégation diagnostic** : sub-agent lancé pour analyser hors contexte gateway

## Diagnostic détaillé

### Logs capturés

```
WARNING gateway.run: Shutdown context: signal=SIGTERM under_systemd=yes
↻ Updated gateway user service definition to match the current Hermes install
[bannière démarrage Hermes Gateway]
💾 Self-improvement review: User profile updated
Main process exited, code=exited, status=1/FAILURE
```

**Points clés** :
- Pas de traceback Python → crash volontaire (`sys.exit(1)`), pas exception
- `Previous gateway life exited UNCLEANLY (no exit path ran — SIGKILL / OOM / VM death)`
- Mémoire disponible : ~449MB, swap utilisé 1.1GB
- Le module "self-improvement review" écrivait USER.md puis terminait avec exit(1)

### Cause racine

Race condition lors du redémarrage automatique systemd :
1. L'ancien processus reçoit SIGTERM
2. systemd le relance immédiatement (`Restart=always`)
3. La nouvelle instance lance le "self-improvement review" qui écrit USER.md
4. Après écriture, le processus termine avec exit(1) au lieu de continuer
5. systemd redémarre → boucle infinie

**Hypothèse** : le module self-improvement review a une logique de sortie post-écriture qui entre en conflit avec le démarrage normal lors d'un restart automatique.

## Résolution

### Actions effectuées

```bash
# 1. Stopper la boucle de restart
systemctl --user stop hermes-gateway-gardien

# 2. Réinitialiser le compteur d'échecs
systemctl --user reset-failed hermes-gateway-gardien

# 3. Démarrage propre
systemctl --user start hermes-gateway-gardien
```

### Résultat

- ✅ Gateway active (PID 2226126)
- ✅ 113MB RAM, 0 swap
- ✅ Restart counter remis à zéro
- ✅ Stable depuis 2+ minutes
- ✅ WebSocket Discord reconnecté

## Leçons apprises

1. **Ne jamais restart depuis l'intérieur d'un gateway** : SIGTERM se propage aux processus enfants, le restart échoue. Utiliser `systemctl --user` depuis un shell externe ou déléguer à un sub-agent isolé.

2. **Crash en boucle systemd** : si restart counter > 2 et exit code 1 systématique, suspecter un conflit entre modules de démarrage et restart automatique. Solution : stop + reset-failed + start propre.

3. **Module self-improvement review** : ce module écrit USER.md au démarrage. Si un crash survient juste après "User profile updated", c'est ce module qui termine volontairement le processus. À investiguer si récidive.

4. **Diagnostic hors contexte** : pour diagnostiquer un gateway, utiliser `delegate_task` pour lancer un sub-agent isolé. Le sub-agent peut exécuter `systemctl`, lire les logs, lancer manuellement le gateway sans être tué par SIGTERM.

5. **Mémoire et swap** : si swap > 1GB et mémoire disponible < 500MB, le système est sous pression. Un OOM killer peut tuer le gateway de manière imprévisible.

## Vérification

```bash
# Vérifier état gateway
systemctl --user status hermes-gateway-gardien

# Vérifier logs récents
journalctl --user -u hermes-gateway-gardien -n 50 --no-pager

# Vérifier PID actif
ps aux | grep "gardien gateway" | grep -v grep
```

## Références

- Profil gardien : `/root/.hermes/profiles/gardien/`
- Service systemd : `hermes-gateway-gardien.service`
- Logs : `/root/.hermes/profiles/gardien/logs/gateway.log`
- Journal systemd : `journalctl --user -u hermes-gateway-gardien`

## Prévention

Si le problème récidive :
1. Investiguer le code du module "self-improvement review" dans `hermes-agent`
2. Ajouter un flag pour désactiver ce module au démarrage (`--no-self-improvement`)
3. Ou wrapper le gateway pour capturer l'erreur exacte post-USER.md
4. Envisager une logique de backoff exponentiel pour systemd (`RestartSec=5`, `RestartSec=10`, `RestartSec=20`)

---

**Statut** : Résolu  
**Date résolution** : 2026-08-25 16:20 UTC  
**Durée incident** : ~20 minutes (de 16:00 à 16:20)  
**Impact** : Gardien injoignable sur Discord pendant l'incident
