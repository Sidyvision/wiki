---
title: "Session corrections rapports quotidiens et rotation HMAC"
type: session
date: 2026-08-30
participants: [studio, publication, sidy]
statut: terminee
---

# Session 2026-08-30 — Corrections rapports quotidiens et rotation HMAC

## Contexte

Reprise de la demande initiale : traiter les rapports quotidiens des agents Studio et Publication qui signalaient plusieurs problèmes à corriger.

## Actions exécutées

### 1. Corrections frontmatter
- `2026-08-29_compte-rendu-github-automation.md` : `type: compte-rendu` → `type: infrastructure` (conforme Sceau atelier)
- `2026-08-30_conversion-chemins-nus-wikilinks.md` : ajout `created`/`updated` manquants

### 2. Corrections incohérences sources
- 37 fiches doctrinales : suppression du marqueur `to-source` quand `sources_count: 0`
- Exemples : `tibb-e-nabawi.md`, `ibn-qayyim.md`, `ibn-sina.md`, `ibn-sirin.md`, `imam-malik.md`
- Résultat : `sources: []` cohérent avec `sources_count: 0`

### 3. Identification source candidate
- Publication §2 signale `raw/Body_Types_Book.pdf` comme source probable pour `tibb-e-nabawi`
- PDF vérifié : 94 pages, ouvrage d'Aiman Attar sur les types constitutionnels en médecine islamique
- Décision : ne pas sourcer (Publication ne sourcera pas)

### 4. Rotation HMAC — rapport Studio §4.1
- Problème signalé : secret HMAC `69a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5` en clair dans `2026-08-29_compte-rendu-github-automation.md` ligne 65
- Risque : dépôt publié sur GitHub Pages = secret potentiellement public
- Actions exécutées :
  - Remplacement du secret par renvoi vers registre
  - Annotation URL Cloudflare comme éphémère
  - Webhook GitHub supprimé manuellement (Sidy)
  - Vérification : `gh api repos/Sidyvision/wiki/hooks` retourne liste vide
  - Ancien webhook pointait vers `https://chronicle-raised-zones-admit.trycloudflare.com/` (tunnel Cloudflare éphémère, HTTP 502)
- Décision (verdict Sidy) : ne pas recréer le webhook maintenant
  - Raison : infrastructure instable (8/11 gateways désactivés)
  - Condition de recréation : tunnel persistant ou URL stable requise

### 5. Mise à jour registre des problèmes
- Nouvelle entrée [2026-08-30] documentant :
  - Suppression webhook GitHub
  - Raison : tunnel éphémère inactif, infrastructure instable
  - Leçon : webhook nécessite URL stable, sinon point de défaillance silencieux

## Vérifications

```bash
# Vérificateur invariants
python3 verifier-invariants.py --racine /root/wiki
# Résultat : 3 erreurs B0 (raw/, immuables) + 1 avertissement A6 (faux positif connu)

# Générateur de graphe
python3 Graphe/generer-cartographie.py --verifier
# Résultat : 1475 arêtes, 106 avertissements
```

## État du dépôt

- 3 erreurs B0 dans `raw/` (fichiers sans frontmatter, immuables par protocole)
- 1 avertissement A6 dans `atelier/annales.md` (faux positif légitime connu)
- 1475 arêtes dans le graphe
- 40 lacunes `to-source` (fiches sans sources identifiées)

## Fichiers modifiés

- `atelier/rd/cahiers/2026-08-29_compte-rendu-github-automation.md`
- `atelier/rd/cahiers/registre-problemes.md`
- `atelier/rd/infrastructure/2026-08-30_conversion-chemins-nus-wikilinks.md`
- 37 fiches doctrinales (autorités, symboles, sources, études, traditions)

## Points en attente

- Rotation token ANTHROPIC compromis (action manuelle requise)
- Traitement 3b : jetons `[[...]]` cités comme données
- Traitement 3d : 65 liens morts (rapport de tri)
- Reconfiguration webhook GitHub quand infrastructure stabilisée

## Références

- Registre des problèmes : `atelier/rd/cahiers/registre-problemes.md` [2026-08-30]
- Rapport Studio 2026-08-29 : `~/.hermes/profiles/studio/cron/output/41dc3e7e492c_20260829_120342.txt`
- Rapport Publication 2026-08-29 : `~/.hermes/profiles/publication/cron/output/ad3152b237bb_20260829_110321.txt`

## Commandes critiques

```bash
# Vérifier webhooks GitHub
gh api repos/Sidyvision/wiki/hooks

# Vérifier état du dépôt
python3 verifier-invariants.py --racine /root/wiki
python3 Graphe/generer-cartographie.py --verifier
```
