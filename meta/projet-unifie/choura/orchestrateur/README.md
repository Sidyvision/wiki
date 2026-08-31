# Orchestrateur de fenêtres du Choura — copie de référence

**Ces fichiers ne sont pas ceux qui s'exécutent.** Ils vivent hors dépôt :

| Ici (référence) | En production |
|---|---|
| `choura-window-orchestrator.py` | `/root/.hermes/scripts/choura-window-orchestrator.py` |
| `cron.d-choura-orchestrator` | `/etc/cron.d/choura-orchestrator` |

Versés au dépôt le 2026-08-31 : l'orchestrateur pilotait les douze agents sans
qu'aucune trace n'en existe ici. Même classe de dérive que les `SOUL.md` — un
composant opératoire que le dépôt ne connaissait pas, donc que personne ne
pouvait relire ni corriger depuis le dépôt.

## Ce qu'il fait

Trois agents tiennent la veille en permanence (`gardien`, `publication`,
`studio`). Les neuf autres **se réveillent pour leur contribution puis
s'éteignent** : l'orchestrateur, appelé chaque minute par cron, démarre le
gateway d'un profil une heure avant son tour et l'arrête une heure après.

Motif : 14 gateways à ~136 Mo plus OmniRoute daemonisé (~1,6 Go) ne tiennent pas
dans les 3,7 Go de l'hôte — incident du 2026-08-28
(`atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite.md`),
dont la « compréhension tirée » demandait exactement cette logique de gateway à
la demande.

Les tours étant espacés de 2h et les fenêtres larges de 2h, **au plus un dormant
est éveillé à la fois** : 3 permanents + 1 dormant ≈ 544 Mo.

## Invariant à tenir

La table `ORDRE` doit rester synchrone avec les expressions cron `cycle-choura`
des profils, posées par `../_reprogrammer-choura.py`. **Un désaccord ne produit
aucune erreur visible** : l'agent est simplement endormi à l'heure de son tour,
et son tour manque au cycle sans que rien ne le signale.

C'est ce qui s'est produit le 2026-08-31 : la rotation a été reprogrammée en
heure de Paris alors que `ORDRE` portait encore des heures UTC figées. Corrigé le
jour même — l'orchestrateur raisonne désormais en `Europe/Paris`, ce qui absorbe
aussi le changement d'heure du 25 octobre.

## Contrôle

```bash
python3 meta/projet-unifie/choura/orchestrateur/verifier-synchronisation.py
```

Lit les heures réelles dans les `jobs.json` des profils et les confronte à
`ORDRE`. Sortie attendue : `0 désynchronisé(s)`.
