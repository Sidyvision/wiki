---
title: "Activation du salon #infrastructure — allowlist du profil studio (2026-08-16)"
type: infrastructure
tags: [rd, infrastructure, hermes, discord, studio, phase-3]
created: 2026-08-16
updated: 2026-08-17
sources: []
links: ["[[meta/projet-unifie/archives/15-architecture-discord-hermes-2026-08-07]]", "[[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11]]", "[[atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16]]"]
infra_verif:
  - profil: studio
    discord_allowed_channels: ["1535173127695241248", "1534857297321394248", "1536564394690084925"]
---

# Activation du salon `#infrastructure` — allowlist du profil `studio`

> **Synthèse** : le salon Discord `#infrastructure`
> (`1536564394690084925`), créé en anticipation de la phase 3
> (veille infrastructure par le Studio Sound Engineer, position 9),
> était muet — l'agent `studio` ne répondait à aucun message, bien
> que son service gateway fût actif et connecté. Cause : le salon
> n'avait jamais été ajouté à `DISCORD_ALLOWED_CHANNELS` du profil
> `studio`. Correction : ajout de l'ID numérique dans l'allowlist,
> redémarrage du service. Agent opérationnel dans le salon.

## 1. Contexte

La phase 3 de la veille infrastructure
([[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition
phase 3]], archivée 2026-08-12) prévoit qu'un agent dédié (Studio
Sound Engineer, profil `studio`, position 9 Sagittaire) surveille
l'infrastructure via un salon Discord dédié `#infrastructure`. Le
salon a été créé (ID `1536564394690084925`) mais l'agent n'y
répondait pas — symptôme rapporté par Sidy le 2026-08-16.

## 2. Diagnostic

Le service `hermes-gateway-studio.service` était bien actif
(`active (running)`), connecté en tant que `HermesStudio#4408`,
avec un channel directory à 8 cibles (dernière mise à jour
`13:28:34 UTC`). L'examen du `.env` du profil a révélé :

```
DISCORD_ALLOWED_CHANNELS=1535173127695241248,1534857297321394248
```

Seuls deux salons autorisés — `#infrastructure` n'était pas dans
la liste. Le comportement fail-closed de l'allowlist (règle
transversale, fiche 15 §2) fait que tout message reçu d'un salon
non listé est **silencieux** : l'agent ignore sans signaler, par
conception. Aucun log d'erreur — le silence est le comportement
attendu hors allowlist.

## 3. Correction appliquée

Édition de
`/root/.hermes/profiles/studio/.env` :

```
DISCORD_ALLOWED_CHANNELS=1535173127695241248,1534857297321394248,1536564394690084925
```

Redémarrage du service (`systemctl --user restart
hermes-gateway-studio.service`, exécuté hors du processus
gateway). Vérification au log : `Channel directory built: 9
target(s)` — confirmation que le salon est désormais reconnu.

Test réel : l'agent répond dans `#infrastructure` — confirmé par
Sidy.

## 4. Leçon tirée

La création d'un salon dédié dans le plan de phase 3 n'impliquait
pas automatiquement son activation côté allowlist du profil. Les
deux gestes sont distincts :

- **Création du salon** : acte Discord (humain ou bot admin).
- **Autorisation de l'agent à y répondre** : acte de configuration
  Hermes (édition du `.env` du profil concerné + restart).

Cette fiche documente le deuxième geste, qui avait été omis après
la création du salon. Pour tout futur salon confié à un agent
Hermes, vérifier systématiquement que son ID numérique figure dans
`DISCORD_ALLOWED_CHANNELS` **et**, si la réponse sans @mention est
souhaitée, dans `DISCORD_FREE_RESPONSE_CHANNELS` (ce dernier point
n'a pas été ajouté dans cette passe — `studio` répond dans
`#infrastructure` sur @mention uniquement, à confirmer avec Sidy
si le mode free-response est souhaité).

## 5. État après correction

| Élément | Valeur |
|---|---|
| Service | `hermes-gateway-studio.service`, `active (running)` |
| Salon autorisé | `#infrastructure` (`1536564394690084925`) ajouté à `DISCORD_ALLOWED_CHANNELS` |
| Cibles channel directory | 9 (était 8) |
| Mode free-response dans `#infrastructure` | Non activé (réponse sur @mention uniquement) |
| Agent opérationnel | Confirmé (test réel 2026-08-16) |

## 6. Points ouverts

- **Mode free-response** : si leStudio doit répondre sans @mention
  dans `#infrastructure` (comme dans son salon principal
  `#analog-wizard`), ajouter l'ID du salon dans
  `DISCORD_FREE_RESPONSE_CHANNELS` du même `.env` et redémarrer.
- **Côté `habib-mehdi` (Telegram, canal du 2026-08-16)** : même
  principe — tout nouvel utilisateur Telegram doit être ajouté à
  `TELEGRAM_ALLOWED_USERS` avant de pouvoir parler à Habib
  (allowlist fail-closed, voir
  [[atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16|fiche
  Telegram Mehdi]]). Aucun ajout demandé ni effectué.
- **Fiche 15 (`meta/projet-unifie/archives/15-architecture-discord-hermes-2026-08-07.md`)** :
  mise à jour pour refléter que `#infrastructure` est désormais
  actif (salon de l'agent `studio`).
