---
title: "OUT-15 — Échantillon B : pattern sandbox cordis-wasm (isolation physique des composants)"
type: outillage
chantier: OUT-15
created: 2026-09-05
updated: 2026-09-05
tags: [atelier, rd, outillage, sampling, cordis, wasm, sandbox, isolation, confinement]
sources:
  - "to-source"   # inso1337/cordis-wasm (commit f5c0562) — SPDX None, réappropriation conceptuelle
  - atelier/rd/veille/cordis/methodes.md
  - atelier/rd/veille/cordis/equations.md
links:
  - "[[atelier/rd/outillage/2026-09-05_sampling-fonction-studio-cordis]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# Échantillon B : pattern sandbox cordis-wasm

> **Ce que cette pièce est.** La seconde réappropriation conceptuelle du paradigme Cordis, focalisée sur l'**isolation physique** des composants via un sandbox (à la manière du WebAssembly). Contrairement à l'échantillon A (skill `spatiotemporal-composability`) qui couvre le contrat de composant et le cycle de vie, l'échantillon B couvre la **frontière physique** entre un composant et le reste du système — ce que le papier Cordis appelle la §6.1.
>
> **Ce qu'elle n'est pas.** Ni une copie du code de `cordis-wasm`, ni une dépendance à WebAssembly. C'est un pattern d'architecture adapté à notre stack (Python, systemd, bind mounts) qui reprend le *principe* du sandbox Wasm sans en utiliser la technologie.

---

## I. Le problème que le sandbox résout

Dans l'échantillon A (skill `spatiotemporal-composability`), la règle 2 dit : « toute dépendance est un service déclaré et typé ». Mais cette règle est une **convention** — un composant mal écrit peut toujours fouiller dans un registre global, un singleton, ou les entrailles d'un parent. La convention ne peut pas l'en empêcher physiquement.

Le sandbox Wasm résout ce problème en transformant la convention en **propriété physique** :

| Convention (skill A) | Propriété physique (sandbox B) |
|----------------------|-------------------------------|
| « Ne lis que les clés déclarées dans `inject` » | Un composant qui n'a pas importé `coeffect:kv` **ne peut pas** exprimer un appel vers cette clé — c'est une propriété de l'ensemble d'instructions |
| « L'accès non déclaré est une erreur » | L'instanciation elle-même échoue si des imports sont non résolus — pas de `INACTIVE_ACCESS` runtime |
| « Les effets passent par le contexte » | Tout effet passe par une frontière d'import que l'hôte entoure — la §6.1 du papier |

**En termes simples** : la skill A dit « fais confiance au composant ». Le sandbox B dit « le composant ne *peut pas* tricher, même s'il le veut ».

---

## II. Le mapping Cordis → sandbox (issu de DESIGN.md de cordis-wasm)

| Papier (calcul) | Sandbox Wasm | Adaptation Hermes |
|-----------------|-------------|-------------------|
| Composant `(d, p, e)` | Module `.wasm` | Agent Hermes (fichier config + scripts) |
| Spécification de coeffets `d` | Liste d'imports du module (`coeffect:<clé>.*`) | Skills/cron/discord déclarés dans `config.yaml` du profil |
| Provision `p` | Exports nommés `provide:<clé>.<op>` | Services que l'agent fournit (son rôle, ses outputs) |
| Fonction d'effet `e` | Fonction exportée `activate` | Fonction principale de l'agent (le tour LLM) |
| Contexte de coeffets Σ | Table côté hôte : clé → opérations du fournisseur actif | Registre des gateways actifs + skills chargés |
| L-Begin (γ ⊧ d) | L'instanciation elle-même — Wasm refuse d'instancier avec des imports non résolus | Le gateway refuse de démarrer un agent sans les skills/cron déclarés |
| Confinement (Def 48) | Le sandbox — un module ne peut physiquement pas atteindre ce qu'il n'a pas importé | L'agent ne peut pas accéder aux fichiers/compétences hors de son profil |
| Frontière système (§6.1) | La surface d'imports — à l'intérieur = mémoire linéaire, à lextérieur = appels hôte | Le bind-mount : à l'intérieur = espace de l'agent, à lextérieur = dépôt wiki (read-only) |
| Accumulateur / inverses | L'hôte enregistre un inverse pour chaque appel hôte effet-mportant ; le déchargement rejoue LIFO | Chaque opération mount/unmount dans le profil agent retourne un inverse |

---

## III. Le pattern adapté à Hermes

### Le bind-mount comme frontière physique

Notre infrastructure utilise déjà des bind mounts en lecture seule pour isoler les accès (Mehdi/Habib, `depot-lecture/`). Ce bind-mount est **exactement** la §6.1 du papier :

```
┌─────────────────────────────────┐
│  Agent Hermes (profil)          │
│  ┌───────────────────────────┐  │
│  │  Mémoire linéaire         │  │  ← Ce que l'agent peut modifier librement
│  │  (skills, cron, .env)     │  │
│  └───────────────────────────┘  │
│                                 │
│  Frontière d'imports :          │  ← Bind-mount read-only
│  ┌───────────────────────────┐  │
│  │  /root/wiki/ (dépôt)      │  │  ← Acquisitions tracées, émissions compensées
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

- **Acquisitions** (lire une fiche du wiki) : tracées, attribuées au composant appelant, avec inverses enregistrées.
- **Émissions** (écrire dans le wiki) : la frontière les **refuse** sauf si l'agent a un droit explicite ( `_inbox/` only pour Mehdi). L'émission qui traverse la frontière sans autorisation est un `L-Raise` (trappe).
- **Invariant** : l'agent ne peut pas modifier le dépôt wiki lui-même — seule la session INTEGRATION peut le faire. C'est le même principe que le Wasm sandbox : le composant ne peut pas modifier la mémoire de l'hôte.

### Les skills comme coeffects importés

Dans cordis-wasm, un composant déclare ses coeffects via des imports Wasm. Dans Hermes, un agent déclare ses dépendances via `config.yaml` :

```yaml
# Un agent Cordis-Hermes déclarerait :
coeffects:
  inject: [discord, cron, skills, mémoire]    # ce dont il a besoin
  provide: [sa-fonction]                       # ce qu'il fournit
  apply:                                       # ses effets réversibles
    - ouvrir_session → fermer_session
    - enregistrer_cron → désenregistrer_cron
    - écrire_fiche → annuler_écriture
```

En l'état actuel, Hermes n'a pas cette structure déclarative. Mais le **principe** est déjà là : chaque profil agent a ses propres skills, cron, et .env — c'est un isolation par réalme (§II de l'échantillon A).

### Le cycle de vie inertiel

Dans cordis-wasm, l'activation est un **itérateur d'effets** : chaque pas est réversible, et entre les pas, le runtime peut observer le monde et dévier. Dans Hermes :

- Un tour LLM = un pas d'itération
- Le gateway peut interrompre entre les tours (pas au milieu d'un appel d'outil)
- Si le fournisseur de skills change (nouveau skill installé), l'agent est rechargé entre les tours
- Le déchargement revert les effets : les cron sont désenregistrés, les connexions fermées, les sessions nettoyées

---

## IV. Ce que cet échantillon ne couvre pas

- L'implémentation Wasm elle-même (pas pertinent pour notre stack Python)
- Le component model WIT (World Interface Types) — c'est un mécanisme de typage avancé, pas nécessaire pour un prototype
- Les async inverses sous garde L-Unload (Thm 63) — à implémenter quand on aura des agents à déchargement asynchrone

---

## V. Prochaine étape

Si l'échantillon B est validé par Sidy (✅ sur Discord), la prochaine étape serait de **formaliser la frontière physique** du dépôt wiki comme une §6.1 Cordis : documenter quelles opérations chaque agent peut faire sur le wiki, avec quelles inverses, et comment la frontière les拒ne. C'est un chantier distinct de l'échantillon A (qui couvre le contrat de composant).

---

*Provenance : cet échantillon réapproprie les concepts de `cordis-wasm` (inso1337, commit f5c0562) et du §6.1 du papier « A Programming Paradigm for Spatiotemporal Composability » (Shi, Zhang, Cui). La traçabilité du isnad est portée par cette fiche et par `atelier/rd/outillage/2026-09-05_sampling-fonction-studio-cordis.md`.*

*Statut license : le repo source `cordis-wasm` n'a aucune license déclarée (SPDX None). Cette fiche est une réappropriation conceptuelle documentée, pas une copie du code. Issue GitHub de demande de license ouverte : https://github.com/inso1337/cordis-wasm/issues/1*
