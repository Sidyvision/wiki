---
title: "Proposition — Veille automatique Studio (recherche repos + interface Gardien)"
type: meta
statut: brouillon
date: 2026-08-31
created: 2026-08-31
updated: 2026-08-31
tags: [proposition, studio, gardien, veille, automatisation, cron]
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]]"
---

# Proposition — Veille automatique Studio (recherche repos + interface Gardien)

**Statut** : `brouillon` — soumis à verdict Sidy (Cmd 6) avant exécution.

**Contexte** : la veille R&D a été ouverte le 2026-08-18 (verdict Sidy) avec mandat hebdomadaire pour le Studio Sound Engineer. Cette proposition étend le mandat à une **veille quotidienne automatisée** avec interface Gardien pour la vigilance doctrinale.

**Source de la proposition** : investigation AngelSpec (2026-08-31) — Sidy a validé le principe d'une veille automatique qui recherche, extrait, analyse, et développe les outils pertinents pour l'infrastructure, sous autorité doctrinale du Gardien.

-----

## 1. Objectifs

1. **Automatiser la recherche** de repos GitHub/papers arXiv pertinents pour l'infrastructure (inference LLM, souveraineté, optimisation)
2. **Extraire et analyser** automatiquement (README, structure, dépendances, benchmarks)
3. **Éprouver en sandbox** (`/root/sandbox-rd/`) les projets pertinents
4. **Développer les outils** qui soutiennent l'infrastructure (sur verdict Sidy)
5. **Interface Gardien** : qualification doctrinale des résonances théoriques (hozo/kumiko/kari-kumi)

**Fréquence** : quotidienne (au lieu d'hebdomadaire — verdict Sidy 2026-08-31).

-----

## 2. Architecture du flux

```
┌─────────────────────────────────────────────────────────────┐
│  Cron quotidien (profil studio, 6h du matin)                │
│  Script: veille-automatique-studio.sh                       │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 1 — Recherche (API GitHub + arXiv)                   │
│  Mots-clés: speculative decoding, llm inference, vllm,      │
│             qwen optimization, sovereign infrastructure,     │
│             multi-gateway, discord bot scaling               │
│  Filtrage: stars > 50, licence permissive, activité < 6 mois │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 2 — Extraction (GitHub API)                          │
│  Téléchargement: README, structure, pyproject.toml, LICENSE │
│  Analyse: dépendances, exigences matérielles, benchmarks    │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 3 — Analyse de pertinence (Studio)                   │
│  Critères:                                                  │
│  - Résonance stack (vLLM, Qwen, providers cloud,            │
│    souveraineté)                                            │
│  - Exigences matérielles (GPU vs CPU, RAM)                  │
│  - Licence (production-safe)                                │
│  - Maintenance (activité, issues, PRs)                      │
│  Verdict Studio: exploitable immédiat / à instruire /       │
│                  non pertinent                              │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 4 — Fiche de veille                                  │
│  Fichier: atelier/rd/veille/YYYY-MM-DD_<slug>.md            │
│  Format: type: experience, statut: exploratoire             │
│  Sections:                                                  │
│  - Contexte                                                 │
│  - Innovations techniques                                   │
│  - Benchmarks                                               │
│  - État du projet (GitHub stats, issues, PRs)               │
│  - Pertinence pour infrastructure (actuelle + future)       │
│  - Concepts théoriques extraits (si résonance détectée)     │
│  - Liens                                                    │
└───────────────────┬─────────────────────────────────────────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
┌─────────────────┐   ┌──────────────────────────────────────┐
│ Pas de résonance │   │ Résonance théorique détectée         │
│ doctrinale       │   │ → Signal au Gardien                  │
│                  │   │   (fiche + extrait concepts)         │
│ → Commit + fin   │   └─────────────────┬────────────────────┘
└─────────────────┘                     │
                                        ▼
                    ┌──────────────────────────────────────┐
                    │  Gardien lit la fiche                │
                    │  Qualifie résonance:                 │
                    │  - hozo (équivalence établie)        │
                    │  - kumiko (complémentarité)          │
                    │  - kari-kumi (suggéré/non tranché)   │
                    └─────────────────┬────────────────────┘
                                      │
                                      ▼
                    ┌──────────────────────────────────────┐
                    │  Rapport conjoint Studio + Gardien   │
                    │  → Sidy (verdict Cmd 12/13)          │
                    │  - Versement doctrinal ?             │
                    │  - Développement outil ?             │
                    │  - Éprouve sandbox ?                 │
                    └──────────────────────────────────────┘
```

-----

## 3. Composants techniques

### 3.1 Script de veille automatique

**Fichier** : `atelier/rd/outillage/scripts/veille-automatique-studio.py`

**Fonctionnement** :
1. Requête API GitHub (search/repositories) avec mots-clés configurables
2. Requête API arXiv (search) avec mots-clés configurables
3. Filtrage automatique (stars, licence, activité)
4. Pour chaque résultat pertinent : extraction README + métadonnées
5. Génération d'une fiche de veille brouillon dans `_inbox/`
6. Si résonance théorique détectée (mots-clés : principle, paradigm, theory, concept), signal au Gardien

**Configuration** : fichier YAML `atelier/rd/outillage/config/veille-mots-cles.yaml`
```yaml
mots_cles:
  - speculative decoding
  - llm inference optimization
  - vllm plugin
  - qwen optimization
  - sovereign infrastructure
  - multi-gateway
  - discord bot scaling
  - container orchestration
  - gpu inference
  - speculative execution
filtrage:
  min_stars: 50
  max_age_months: 6
  licences_permises: [Apache-2.0, MIT, BSD-2-Clause, BSD-3-Clause]
  langues: [Python, Rust, Go, C++]
```

### 3.2 Cron quotidien

**Nom** : `veille-automatique-studio`
**Profil** : `studio`
**Schedule** : `0 6 * * *` (6h du matin, quotidien)
**Action** : exécuter le script, générer fiches, signaler Gardien si résonance

**Script d'enveloppe** : `atelier/rd/outillage/scripts/veille-automatique-cron.sh`
```bash
#!/bin/bash
# Enveloppe cron pour veille automatique Studio
# Appelée par Hermes cron (profil studio)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/veille-automatique-studio.py"

# Vérifier si des fiches ont été générées
FICHES=$(find /root/wiki/_inbox -name "veille-*.md" -mmin -60 | wc -l)

if [ "$FICHES" -gt 0 ]; then
  echo "$FICHES fiche(s) de veille générée(s) dans _inbox/"
  # Signal au Gardien si résonance détectée
  if grep -q "resonance_doctrinale: true" /root/wiki/_inbox/veille-*.md 2>/dev/null; then
    echo "RESONANCE_DETECTEE"
  fi
fi
```

### 3.3 Prompt Studio étendu

**Ajouts au prompt actuel** (`meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md`) :

```markdown
### Mandat veille automatique (2026-08-31, verdict Sidy)

**Fréquence** : quotidienne (cron 6h du matin).

**Actions** :
1. Exécuter `veille-automatique-studio.py` (recherche GitHub/arXiv)
2. Pour chaque fiche générée dans `_inbox/` :
   - Relire, enrichir avec analyse de pertinence
   - Déplacer vers `atelier/rd/veille/YYYY-MM-DD_<slug>.md`
   - Commit + push
3. Si résonance théorique détectée (section "Concepts théoriques extraits") :
   - Signaler au Gardien via rapport conjoint
   - Ne jamais verser au doctrinal sans verdict Sidy (Cmd 12)

**Interface Gardien** :
- Le Gardien lit les fiches de veille avec résonance théorique
- Qualifie la résonance (hozo/kumiko/kari-kumi)
- Rapport conjoint Studio + Gardien → Sidy
- Studio n'a aucune autorité doctrinale : le Gardien est l'autorité doctrinale

**Éprouve sandbox** :
- Si pertinence confirmée + verdict Sidy : clonage dans `/root/sandbox-rd/<projet>/`
- Test d'installation, test fonctionnel minimal
- Fiche `resultats-sandbox.md` dans `atelier/rd/veille/<projet>/`
- Rapport à Sidy : exploitable / non exploitable / à développer

**Développement d'outils** :
- Si sandbox réussie + verdict Sidy : développement de l'outil
- Respect du protocole wiki (fiches, annales, commits, VIGILANCE)
- Intégration au dépôt via `_inbox/` → validation → commit

**Règles** :
- Jamais d'installation en production sans verdict Sidy (Cmd 13)
- Jamais de versement doctrinal sans verdict Sidy (Cmd 12)
- Communication Studio ↔ Gardien exclusivement via le Cycle Choura
- Toute décision engageante → signalement à Sidy dans le Choura, pas d'autonomie
```

### 3.4 Prompt Gardien étendu

**Ajouts au prompt actuel** (`meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`) :

```markdown
### Mandat vigilance doctrinale sur veille Studio (2026-08-31, verdict Sidy)

**Déclenchement** : contribution Studio dans le Cycle Choura signalant des concepts théoriques extraits de la veille.

**Actions** :
1. À son tour de Choura, lire la contribution Studio
2. Si Studio a signalé des concepts extraits :
   - Lire la fiche de veille dans `atelier/rd/veille/`
   - Qualifier la résonance doctrinale dans sa propre contribution Choura :
     - **hozo** : équivalence établie avec un principe doctrinal (sourdé)
     - **kumiko** : complémentarité (treillis en plan)
     - **kari-kumi** : suggéré/non tranché (montage à blanc)
   - Ajouter un bloc dans sa contribution :
     ```
     **Qualification doctrinale** (veille Studio) :
     - Concept A : **hozo/kumiko/kari-kumi** — [principe(s) concerné(s)]
     ```
3. Sidy lit le cycle et tranche (Cmd 12/13)

**Règles** :
- Le Gardien qualifie, ne tranche jamais le principe (Cmd 12)
- Le verdict final appartient à Sidy
- Si Studio ne signale aucun concept, le Gardien n'intervient pas sur la veille
- Communication exclusivement via le Choura, jamais de rapport séparé
```

-----

## 4. Articulation avec le Cycle Choura

**Principe** : le Choura est le lieu unique de communication entre agents. La veille automatique n'a **aucun mécanisme de signal séparé** — tout transite par le cycle.

### Flux intégré au Choura

```
Phase 1 — Cron quotidien Studio (6h du matin)
  ↓
Phase 2 — Recherche GitHub/arXiv, extraction, analyse
  ↓
Phase 3 — Fiche de veille dans atelier/rd/veille/
  ↓
Phase 4 — Studio dépose la matière dans son tour de Choura
  (prochain cycle, ~2h après ou au tour suivant)
  ↓
Phase 5 — Gardien, à son tour (00:00 ou prochain tour),
  lit la contribution Studio, qualifie la résonance doctrinale
  (hozo/kumiko/kari-kumi) dans sa propre contribution
  ↓
Phase 6 — Sidy lit le cycle Choura, tranche (Cmd 12/13)
```

### Format de contribution Studio dans le Choura

```markdown
## [HH:MM] studio (rôle 9, Vierge)

**S'appuyant sur** : [contribution du précédent]

**Tâches en cours** : veille automatique quotidienne (cron 6h)

**Veille du jour** :
- N fiches générées dans `atelier/rd/veille/`
- Résumé des repos/papers pertinents trouvés
- [Si résonance théorique détectée] Concepts extraits signalés
  pour qualification doctrinale :
  - Concept A : [description brève]
  - Concept B : [description brève]

**État du dépôt perçu** : [inchangé ou mise à jour]

**Perspective** : [propositions techniques si pertinent]
```

### Format de contribution Gardien dans le Choura

```markdown
## [00:00] gardien (rôle 10, Balance)

**S'appuyant sur** : studio (rôle 9) — veille du jour

**Qualification doctrinale** (si Studio a signalé des concepts) :
- Concept A : **kumiko** — complémentarité avec [[doctrinal/...]]
- Concept B : **kari-kumi** — suggéré, non tranché, à examiner

**Tâches en cours** : vigilance protocolaire, lecture des fiches de veille

**État du dépôt perçu** : [inchangé ou signalement]

**Perspective** : [recommandation pour Sidy]
```

### Suppression du rapport conjoint séparé

**Avant** : Studio + Gardien rédigeaient un `rapport-conjoint-YYYY-MM-DD-<slug>.md` séparé.

**Maintenant** : tout se passe dans le fichier de cycle Choura (`meta/projet-unifie/choura/cycle-YYYY-MM-DD.md`). Sidy lit le cycle, voit la contribution Studio (veille + concepts extraits), puis la qualification doctrinale du Gardien, puis tranche.

**Avantages** :
- Pas de redondance (un seul lieu de communication)
- Traçabilité intégrée au Choura (Cmd 9)
- Les autres agents voient aussi la veille (transparence)
- Le Gardien qualifie dans son propre tour, pas dans un rapport séparé
- Sidy a une vue synoptique du cycle complet pour trancher

-----

## 5. Plan d'exécution (sur verdict Sidy)

| Étape | Action | Auteur |
|---|---|---|
| 1 | Rédiger script `veille-automatique-studio.py` | Studio (ou agent WebUI sur consigne) |
| 2 | Rédiger config `veille-mots-cles.yaml` | Studio |
| 3 | Rédiger script cron `veille-automatique-cron.sh` | Studio |
| 4 | Étendre prompt Studio (`09-studio-sound-engineer.md`) | Sidy (ou agent WebUI sur consigne) |
| 5 | Étendre prompt Gardien (`10-protocol-guardian.md`) | Sidy (ou agent WebUI sur consigne) |
| 6 | Créer cron Hermes `veille-automatique-studio` | Agent WebUI (profil `studio`) |
| 7 | Test manuel (exécuter le script, vérifier fiche générée) | Studio + Sidy |
| 8 | Activation cron quotidien | Sidy (verdict final) |

-----

## 6. Questions ouvertes

1. **Mots-clés supplémentaires** : ajouter des termes spécifiques à l'infrastructure Hermes (ex: `hermes agent`, `discord bot scaling`) ou rester sur les termes génériques ?
2. **Seuil de stars** : 50 est-il pertinent, ou ajuster (ex: > 100 pour réduire le bruit) ?
3. **Archivage** : les fiches non pertinentes sont-elles archivées (cmd 10) ou supprimées ?
4. **Sandbox** : validation préalable de Sidy avant chaque clonage, ou autonomie Studio pour clonage (pas pour déploiement) ?

-----

## 7. Verdict Sidy (Cmd 6)

**À remplir par Sidy** :

- [ ] Valide le plan d'exécution en 7 étapes
- [ ] Valide la fréquence quotidienne (cron 6h du matin)
- [ ] Valide l'interface Gardien (qualification doctrinale)
- [ ] Valide la discipline de rapport conjoint
- [ ] Répond aux questions ouvertes (§6)
- [ ] Autorise l'exécution

**Date du verdict** : _______________

**Commentaires** : _______________
