---
title: Infrastructure — Décision statu quo SSH (vs HTTPS+PAT)
type: infrastructure
tags:
- rd
- infrastructure
- git
- workflow
created: 2026-08-11
updated: 2026-08-11
sources: []
links:
- atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11
---

# Décision : Statu quo SSH sur `origin`

> Piste D des « 4 pistes outillage » instruites en session R&D du 2026-08-11.
> Verdict rendu par Sidy le 2026-08-11 après avis technique du 2026-08-09.

## 1. Question posée

Migrer le remote `origin` du dépôt wiki de SSH vers HTTPS + Personal Access Token (PAT)?

**Contexte** : Obsidian Git plugin (embarqué sur iPad) ne supporte nativement que HTTPS 
(limitation de l'implémentation JS de libgit2). Pour que Obsidian puisse push/pull de 
manière autonome, il faudrait passer à HTTPS+PAT. Actuellement, la routine est :
1. Éditer dans Obsidian (iPad)
2. Détour par Working Copy (push/pull manuels)
3. Obsidian auto-pull du remote après chaque cycle

## 2. Analyse technique du 2026-08-09

| Dimension | SSH (statu quo) | HTTPS+PAT |
|-----------|-----------------|-----------|
| **Secrets en jeu** | Clé SSH existante (Hetzner + Working Copy) | PAT supplémentaire à créer |
| **Renouvellement** | Jamais (clé ne s'expire pas) | Périodique (PAT expiration) |
| **Stockage** | Réseau SSH standard | Plugin Obsidian settings (ou CLI) |
| **Coût du détour** | Working Copy (3 taps) | Éliminé |
| **Risque de perte du PAT** | N/A | Nouveau secret → nouveau risque oubli |

**Avis technique** : SSH déjà en place et stable, coût de renouvellement quasi-zéro ; 
PAT introduit un nouveau secret et un risque de gestion. Le coût du détour Working Copy 
(3 gestes manuels) est jugé inférieur au coût de gestion d'un PAT.

## 3. Verdict (Sidy, 2026-08-11)

**Statu quo** — le remote `git@github.com:Sidyvision/wiki.git` reste en SSH, aucune 
migration effectuée.

**Rationale** :
- Clé SSH stable depuis des mois sur les deux côtés (serveur + Working Copy)
- Le détour Working Copy pour push/pull n'est pas présenté comme une friction 
  répétée ou bloquante en session
- Pas de gain de productivité majeur à peser contre un secret supplémentaire

## 4. Clause de réouverture

**Non figée pour l'éternité.** À rouvrir seulement si :
- La routine Working Copy devient un point de friction réel et répété en pratique
- Obsidian Git plugin ajoute un support natif d'authentification par clé SSH
- Un nouvel outil remplace Working Copy avec meilleure UX

En l'absence de ces conditions, maintenir le statu quo.

## 5. Implémentation

Aucune modification requise du remote ou de la configuration :
```bash
git remote -v
# origin  git@github.com:Sidyvision/wiki.git (fetch)
# origin  git@github.com:Sidyvision/wiki.git (push)
```

Reste inchangé à ce jour (2026-08-11).

## Références

- [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]] — context §4-5
- [[atelier/rd/cahiers/registre-problemes]] — entry [2026-08-11] piste D
- Avis technique H‍ermes : 2026-08-09 (cf. `meta/projet-unifie/15-architecture-discord-hermes-*`)
