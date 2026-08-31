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
- Rapport conjoint avec Gardien si résonance détectée
- Toute décision engageante → signalement à Sidy, pas d'autonomie
```

### 3.4 Prompt Gardien étendu

**Ajouts au prompt actuel** (`meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`) :

```markdown
### Mandat vigilance doctrinale sur veille Studio (2026-08-31, verdict Sidy)

**Déclenchement** : signal de Studio (fiche de veille avec résonance théorique).

**Actions** :
1. Lire la fiche de veille dans `atelier/rd/veille/`
2. Examiner la section "Concepts théoriques extraits"
3. Qualifier la résonance doctrinale :
   - **hozo** : équivalence établie avec un principe doctrinal (sourdé)
   - **kumiko** : complémentarité (treillis en plan)
   - **kari-kumi** : suggéré/non tranché (montage à blanc)
4. Ajouter un bloc dans la fiche :
   ```markdown
   ### Qualification doctrinale (Gardien, YYYY-MM-DD)
   
   **Résonance** : hozo | kumiko | kari-kumi
   **Principe(s) concerné(s)** : [[doctrinal/...]]
   **Analyse** : [explication de la résonance, sans trancher le principe]
   **Verdict** : verser au doctrinal | rester dans rd/veille | abandonner
   ```
5. Rapport conjoint avec Studio → Sidy (verdict Cmd 12)

**Règles** :
- Le Gardien qualifie, ne tranche jamais le principe (Cmd 12)
- Le verdict final appartient à Sidy
- Rapport conjoint avec Studio (jamais de rapport séparé)
- Si aucun concept théorique n'est extrait, le Gardien n'intervient pas
```

-----

## 4. Discipline de rapport conjoint

**Règle** : Studio et Gardien produisent **toujours un rapport conjoint** (jamais de rapports séparés en parallèle), conformément au protocole existant.

**Flux** :
1. Studio génère la fiche de veille + extrait les concepts théoriques
2. Studio signale au Gardien (via cron ou fichier de signal)
3. Gardien lit la fiche + qualifie la résonance doctrinale
4. Gardien + Studio rédigent un rapport conjoint (fiche `rapport-conjoint-YYYY-MM-DD-<slug>.md` dans `atelier/rd/cahiers/`)
5. Rapport soumis à Sidy (verdict Cmd 12/13)

**Format du rapport conjoint** :
```markdown
---
title: "Rapport conjoint Studio + Gardien — <sujet>"
type: meta
date: YYYY-MM-DD
signataires: [studio, gardien]
---

# Rapport conjoint — <sujet>

## Contexte
[Studio : ce qui a été trouvé, pourquoi c'est pertinent]

## Analyse technique (Studio)
[Extraits de la fiche de veille, pertinence infrastructure]

## Qualification doctrinale (Gardien)
[Résonance hozo/kumiko/kari-kumi, principe(s) concerné(s)]

## Recommandation conjointe
- Verser au doctrinal ? [oui/non, motif]
- Développer l'outil ? [oui/non, motif]
- Éprouver en sandbox ? [oui/non, motif]
- Abandonner ? [oui/non, motif]

## Verdict Sidy (Cmd 12/13)
[À remplir par Sidy]
```

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
3. **Signal Gardien** : fichier de signal (`.veille-signal`) ou message direct via Hermes (cron → Gardien) ?
4. **Archivage** : les fiches non pertinentes sont-elles archivées (cmd 10) ou supprimées ?
5. **Sandbox** : validation préalable de Sidy avant chaque clonage, ou autonomie Studio pour clonage (pas pour déploiement) ?

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
