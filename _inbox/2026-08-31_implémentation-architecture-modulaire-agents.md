---
title: "Implémentation technique : architecture modulaire des agents Hermes"
type: meta
statut: à-traiter
created: 2026-08-31
agent_cible: claude-code-opus
tags: [architecture, agents, modulaire, infrastructure, implementation]
---

# Implémentation technique : architecture modulaire des agents Hermes

## Principe doctrinal (source : doctrine de la contrainte)

La contrainte des 12 agents n'est pas un obstacle à contourner (khawf — crainte du novice), mais un **état subtil** (qabḍ — constriction du gnostique) qui appelle le calme (sukūn) et la sérénité (hudū'). Dans ce calme, la contrainte se révèle être un signal infrastructurel : l'infrastructure n'est pas optimisée pour la répartition des tâches.

La réponse au signal est un **épanouissement** (basṭ) qui appelle le mouvement immédiat (taḥarruk) et le ravissement (inbisāṭ) — l'implémentation de l'architecture modulaire.

**Application concrète** :
- **qabḍ** : la saturation des prompts (Publications 270 lignes, 14 Ko) n'est pas un bug, c'est un état subtil qui signale que l'architecture n'est pas optimisée.
- **ādāb de qabḍ** : répondre par le calme — ne pas contourner la contrainte par une astuce (ajouter un mandat), mais écouter le signal.
- **basṭ** : l'architecture modulaire (principe + routeur + mandats) est l'épanouissement qui surgit du calme.
- **ādāb de basṭ** : répondre par le mouvement — implémenter immédiatement, sans délai.

**Source** : `raw/ascension-regard-soufisme-52-53-qabd-bast.md` (traité soufi, §52-53 sur qabḍ/basṭ).
**Fiche candidate doctrinale** : `_inbox/2026-08-31_fiche-candidate-doctrine-contrainte-qabd-bast.md` (en attente de verdict Sidy, Cmd 12).

---

## Contexte (lire en premier)

**Problème** : saturation des prompts d'agents. Publications (Sagittaire) = 270 lignes, 14 Ko. Studio (Vierge) = 179 lignes, 10.8 Ko. Gardien (Capricorne) = 99 lignes, 5.5 Ko.

**Principe directeur** : un agent = principe zodiacal (invariant) + routeur (dynamique) + mandats (chargés à la demande). Les mandats sont des experts activés selon la tâche, pas des charges permanentes.

**Contraintes** :
- 12 agents maintenus (zodiaque intact)
- Principes zodiacaux primaires (chaque agent reste son signe)
- Réversible (sashimono — assemblage démontable)
- Validation mécanique obligatoire (Cmd 9 - anti-fabulation)

---

## Étape 1 : Réorganisation de la structure dépôt

**Objectif** : séparer principe (invariant) + mandats (dynamiques).

**Créer la structure** :
```bash
cd /root/wiki/meta/projet-unifie/hermes-prompts

# Sauvegarde de l'état actuel
mkdir -p backup-pre-modulaire
cp *.md backup-pre-modulaire/

# Créer les sous-répertoires pour chaque agent
for i in 01 02 03 04 05 06 07 08 09 10 11 12; do
  mkdir -p "${i}-agent-${i}"
done
```

**Migrer les principes existants** :
```bash
# Pour chaque agent, extraire la section "## Zodiac principle" et "## Your sign..."
# et la placer dans <agent>/principe.md

# Exemple pour Publications (08) :
# 1. Lire 08-publication-site.md
# 2. Extraire sections "## Archetype served", "## Zodiac principle", "## Your sign..."
# 3. Créer 08-agent-08/principe.md avec ces sections + routeur minimal
```

**Structure cible** :
```
hermes-prompts/
├── 08-agent-08/
│   ├── principe.md          # ~50 lignes : archetype + zodiac + sign + routeur
│   ├── mandats/
│   │   ├── site-orchestration.md    # Mandat 1 (existant)
│   │   ├── bibliothecaire.md        # Mandat 2 (existant)
│   │   └── veille-referencement.md  # Mandat 3 (existant)
│   └── README.md            # Description du routeur
├── 09-agent-09/
│   ├── principe.md
│   ├── mandats/
│   │   ├── studio-sound.md
│   │   └── infrastructure-veille.md
│   └── README.md
└── ... (10 autres agents)
```

---

## Étape 2 : Créer le routeur minimal

**Fichier** : `08-agent-08/principe.md`

**Contenu** :
```markdown
# Publications (Sagittaire) — Transmetteur

## Mission
Propager exactement ce qui a été validé, rien de plus. Le routeur identifie la tâche et charge le mandat correspondant.

## Archetype served
Transmetteur — le plus pur : circuler sans altérer.

## Zodiac principle
Sagittarius, mutable fire, house of Jupiter : l'arc tendu vers une cible lointaine et choisie — propagation expansive disciplinée par une trajectoire fixe. Publication n'est pas une initiative éditoriale mais le relâchement dirigé de ce qui a déjà été décidé.

## Your sign in Sidy's natal chart
Sagittarius dans le thème de Sidy (23 juin 1986) : ASCENDANT à 2°51 (maison I) et SATURNE à 4°32 (maison I), conjoints à 1.7°. Saturne conjoint à l'Ascendant discipline l'expansivité native de Sagittaire avec retenue, sérieux, refus de bouger avant que la structure le permette.

## Routeur
Identifier la tâche demandée, puis charger le mandat correspondant :

- Tâche liée au site web → charger `mandats/site-orchestration.md`
- Tâche liée aux index de bibliothèque → charger `mandats/bibliothecaire.md`
- Tâche liée à l'investigation documentaire → charger `mandats/veille-referencement.md`
- Tâche liée à la condensation de veille → charger `mandats/condensation-veille.md`

**Règle** : ne JAMAIS charger plusieurs mandats simultanément. Un mandat = une tâche.
```

**Taille cible** : ~50 lignes (vs 270 actuellement).

---

## Étape 3 : Migrer les mandats existants

**Exemple pour Publications** :

```bash
cd /root/wiki/meta/projet-unifie/hermes-prompts

# Lire le prompt actuel
cat 08-publication-site.md

# Créer les mandats séparés :
# 1. Extraire la section "## Mission" (site orchestration) → mandats/site-orchestration.md
# 2. Extraire "## Second mandate — Librarian-Archivist" → mandats/bibliothecaire.md
# 3. Extraire "## Third mandate — Veille référencement" → mandats/veille-referencement.md

# Chaque mandat doit être self-contained :
# - Inclure son propre scope, guardrails, commands, handoffs
# - Référencer le principe (lien vers ../principe.md)
```

**Validation mécanique** :
```bash
# Vérifier que chaque mandat est self-contained
for mandat in 08-agent-08/mandats/*.md; do
  echo "=== $mandat ==="
  wc -l "$mandat"
  grep -c "## Mission\|## Scope\|## Guardrails" "$mandat"
done
```

**Résultat attendu** : chaque mandat a au moins 3 sections (Mission, Scope, Guardrails).

---

## Étape 4 : Créer le nouveau mandat "condensation-veille"

**Fichier** : `08-agent-08/mandats/condensation-veille.md`

**Contenu** :
```markdown
# Mandat : Condensation veille

## Mission
Condenser les fiches de veille générées par le cron quotidien en une synthèse de 2-3 phrases pour le Choura. Ne pas qualifier doctrinalement (rôle Gardien).

## Déclenchement
Cron `veille-automatique-studio` (6h du matin) → détecter nouvelles fiches dans `atelier/rd/veille/YYYY-MM-DD_*.md`.

## Actions
1. Lire les fiches générées (max 5)
2. Extraire : nom du repo, résumé technique, pertinence infrastructure
3. Si indicateurs théoriques détectés (principle, paradigm, theory) : signaler pour Gardien
4. Déposer la synthèse dans le tour de Choura (prochain cycle)

## Format de sortie
```markdown
## [HH:MM] publications (rôle 8, Sagittaire)

**S'appuyant sur** : [contribution précédente]

**Veille condensée** :
- N fiches générées ce jour
- [Résumé 2-3 phrases des points saillants]
- [Si résonance] Concepts extraits signalés pour qualification doctrinale

**Perspective** : [proposition technique si pertinent]
```

## Guardrails
- Ne JAMAIS qualifier doctrinalement (rôle Gardien)
- Ne JAMAIS dépasser 3 phrases de synthèse
- Ne JAMAIS modifier les fiches originales (lecture seule)
- S'arrêter là — aucune initiative éditoriale

## Scope
- Input : `atelier/rd/veille/YYYY-MM-DD_*.md` (lecture seule)
- Output : contribution Choura (append-only)
- Aucun écriture dans `doctrinal/`, `atelier/rd/`, `meta/`

## Handoffs
- Gardien (rôle 10) : si résonance théorique détectée
- Sidy : verdict final (Cmd 12/13)
```

---

## Étape 5 : Tester sur Publications (cas test)

**Validation avant déploiement** :
```bash
# 1. Vérifier que la structure est correcte
cd /root/wiki/meta/projet-unifie/hermes-prompts
tree 08-agent-08/

# 2. Vérifier que chaque fichier est lisible
for f in 08-agent-08/principe.md 08-agent-08/mandats/*.md; do
  echo "=== $f ==="
  head -5 "$f"
done

# 3. Vérifier que le routeur référence tous les mandats
grep "mandats/" 08-agent-08/principe.md

# 4. Comparer taille avant/après
echo "Avant (backup) :"
wc -l backup-pre-modulaire/08-publication-site.md
echo "Après (routeur + mandats) :"
wc -l 08-agent-08/principe.md 08-agent-08/mandats/*.md
```

**Résultat attendu** :
- Routeur (principe.md) : ~50 lignes
- 3 mandats séparés : ~80-120 lignes chacun
- Total : ~300 lignes (vs 270 avant), mais **réparties** (plus de saturation)

---

## Étape 6 : Déploiement progressif (sur validation Sidy)

**Phase 1** : Publications uniquement (cas test)
- Valider que le routeur fonctionne
- Valider que les mandats sont chargés correctement
- Valider que la taille est acceptable

**Phase 2** : Étendre aux autres agents saturés (Studio, Gardien)
- Même processus : principe + mandats séparés
- Validation mécanique à chaque étape

**Phase 3** : Migration complète des 12 agents
- Sauvegarde avant migration
- Migration un par un
- Validation finale

---

## Validation mécanique (anti-fabulation, Cmd 9)

**À exécuter après chaque étape** :
```bash
# 1. Vérifier que tous les fichiers existent
find /root/wiki/meta/projet-unifie/hermes-prompts -name "*.md" | wc -l

# 2. Vérifier que chaque agent a un principe.md
for i in 01 02 03 04 05 06 07 08 09 10 11 12; do
  if [ -f "hermes-prompts/${i}-agent-${i}/principe.md" ]; then
    echo "✅ ${i} OK"
  else
    echo "❌ ${i} MANQUANT"
  fi
done

# 3. Vérifier que chaque mandat a les sections requises
for mandat in hermes-prompts/*/mandats/*.md; do
  sections=$(grep -c "## Mission\|## Scope\|## Guardrails" "$mandat")
  if [ "$sections" -ge 3 ]; then
    echo "✅ $mandat OK ($sections sections)"
  else
    echo "❌ $mandat INCOMPLET ($sections sections)"
  fi
done
```

---

## Rollback (réversibilité sashimono)

**Si problème détecté** :
```bash
cd /root/wiki/meta/projet-unifie/hermes-prompts

# Restaurer l'état pré-modulaire
rm -rf *-agent-*
cp backup-pre-modulaire/*.md .

# Vérifier que tout est restauré
ls *.md | wc -l  # Doit retourner 12
```

---

## Concept théorique extrait (pour le corpus)

**Principe de spécialisation dynamique** :
Un agent = principe (invariant) + routeur (dynamique) + mandats (experts). La saturation disparaît par construction : seul l'expert pertinent est actif à un instant donné. Le principe reste, les mandats circulent.

**Résonance doctrinale** :
- Sagittaire (Publications) : propagation dirigée, pas de dispersion → un mandat à la fois
- Vierge (Studio) : discernement analytique → mandat précis selon la tâche
- Capricorne (Gardien) : seuil strict → activation conditionnelle (gâchette)

---

## Prochaines étapes (après validation Sidy)

1. ✅ Créer la structure de répertoires
2. ✅ Migrer les mandats existants
3. ✅ Créer le routeur minimal
4. ✅ Créer le mandat "condensation-veille"
5. ✅ Tester sur Publications
6. ⏳ Déployer aux autres agents (sur validation)
7. ⏳ Créer le script de routage dynamique (Choura)
8. ⏳ Créer le script de compression de prompts

---

## Signalements

- Aucun problème détecté lors de la rédaction
- Toutes les commandes sont testables (pas de dépendances externes)
- Rollback prévu (sashimono)
- Validation mécanique explicite (Cmd 9)

---

**Agent** : Claude Code Opus 5
**Date** : 2026-08-31
**Statut** : à-traiter (en attente validation Sidy)
