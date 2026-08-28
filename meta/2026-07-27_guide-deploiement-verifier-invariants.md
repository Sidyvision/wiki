---
title: "Guide de déploiement — verifier-invariants.py"
type: procédure
status: operationnel
tags: [meta, infrastructure, verification, deployment]
created: 2026-07-27
updated: 2026-08-28
sources: []
links: ["[[CLAUDE.md]]", "[[meta/philosophie-sashimono]]", "[[correctif-etendu-invariants-depot]]"]
---

# Guide de déploiement — `verifier-invariants.py`

## 1. Placement au dépôt

Copier le fichier à la **racine du dépôt**, au même niveau que :
- `CLAUDE.md`
- `.gitignore`
- `git` configs

```bash
# Depuis Hetzner
cd /root/wiki
cp verifier-invariants.py .
chmod +x verifier-invariants.py

# Vérifier
ls -l verifier-invariants.py
python3 verifier-invariants.py --help
```

Maintenir **en versioning** (pas dans `.gitignore`) — c'est un outil de dépôt,
pas un artéfact temporaire.

---

## 2. Commandes usuelles

### 2.1 Audit complet — mode interactif (terminal)

```bash
cd /root/wiki
python3 verifier-invariants.py --racine .
```

Affiche les erreurs (bloquantes, code sortie 1) et les avertissements (informatifs).
Exemple de sortie :

```
ERREURS (bloquantes) :
  [A2] doctrinal/annales.md:26 — rupture d'ordre : 2026-07-16 apparaît après...
  [B2] doctrinal/fiche-test.md — `sources_count: 5` ≠ nombre réel...

AVERTISSEMENTS :
  [C1] doctrinal/fiche-test.md — lien non résolu : [[doctrinal/sources/...]]

10 erreur(s), 2 avertissement(s).
```

Code de sortie : `0` si OK, `1` si erreurs bloquantes, `2` si crash du script.

### 2.2 Audit en JSON — pour traitement ultérieur (CI/outillage)

```bash
python3 verifier-invariants.py --racine . --json > audit-$(date +%Y-%m-%d).json
```

Fichier JSON brut (schema : `{erreurs: [...], avertissements: [...]}`), pas de
texte narratif. À utiliser pour **archiver les résultats** ou les passer à un
autre outil.

### 2.3 Mode strict — avertissements = bloquant

```bash
python3 verifier-invariants.py --racine . --strict
```

Fait échouer le script (code sortie 1) si au moins un avertissement est présent.
À utiliser en **CI/pré-commit**, jamais en mode interactif (trop agressif pour la
calibrage initiale).

### 2.4 Audit ciblé — un seul circuit

```bash
# Vérifier seulement doctrinal/
find /root/wiki/doctrinal -name "*.md" | python3 verifier-invariants.py --racine /root/wiki

# Shortcut shell : créer un alias dans ~/.bashrc
alias audit-wiki="python3 /root/wiki/verifier-invariants.py --racine /root/wiki"
alias audit-strict="python3 /root/wiki/verifier-invariants.py --racine /root/wiki --strict"
```

---

## 3. Intégration dans le workflow de clôture

**Ajouter à `CLAUDE.md` §Action d'intégration générale**, comme étape obligatoire
après `compare` et avant `git diff --stat` destiné à Sidy :

> **Étape 7bis — Vérification structurelle du dépôt (nouveau, 2026-07-27)** :
> exécuter `python3 verifier-invariants.py --racine /root/wiki` et consigner le
> résultat brut (entier stdout/stderr) dans un bloc code de l'entrée d'annales.
> Cette étape ne doit pas être sautée, même en mode non-bloquant initial.
> Codage :
> - Phase d'**intégration** (toutes les opérations < 50 fiches) : non-bloquant
>   (`--json` optionnel) ; avertissements rapportés, erreurs investigiguées.
> - Phase de **calibrage** (première quinzaine après déploiement) : non-bloquant ;
>   résultats archivés en JSON daily pour déterminer les faux positifs.
> - Phase de **production** (après calibrage) : `--strict` ; bloquant, pas de
>   relâchement.

**Placement dans la séquence** :

```
AVANT (existant) :
  1. Lire UPDATES.md / manifeste
  2. Traitement fiche par fiche / lot par lot
  3. Mise à jour index.md, annales.md
  4. git add / git commit
  5. Exécuter compare → vérification mécanique (Cmd : le verdict)
  6. Consigner résultat dans l'entrée d'annales + git push

APRÈS (proposé) :
  1-6 : idem
  7. Exécuter verifier-invariants.py
  8. Consigner résultat brut dans l'entrée d'annales (ou JSON en archive)
  9. git diff --stat pour révision Sidy
  10. git push final
```

---

## 4. Calibrage initial — sur 2-3 semaines

**Première exécution** : lancez-le en mode interactif, ne pas bloquant.

```bash
cd /root/wiki
python3 verifier-invariants.py --racine . 2>&1 | tee audit-initial.log
```

**Expected output** : un certain nombre d'erreurs bloquantes (dont au moins la
dérive de `annales.md` du 07-27), un certain nombre d'avertissements. Ne pas
paniquer si 50+ erreurs apparaissent — c'est normal lors d'un premier passage sur
un dépôt non conçu en pensant à un vérificateur.

**Actions à la sortie** :

1. **Trier les faux positifs** : y a-t-il des erreurs que tu sais être fausses
   (par ex. un format de lien ou une clé du Sceau que je ne connais pas) ?
   Lister-les.

2. **Ajouter à `verifier-invariants.py`** les exemptions appropriées :
   - `CLES_REQUISES` pour les variantes du Sceau
   - Formes de wikilinks non prévues dans `RE_WIKILINK`
   - Fichiers de service (type: meta) mal reconnus

3. **Archiver en JSON** chaque run de calibrage : `python3 ... --json >
   audit-calibrage-$(date +%s).json`. Permet de voir la stabilité du résultat
   d'une journée à l'autre et de confirmer que les erreurs qu'on corrige ne
   reviennent pas.

4. **Une fois < 5 faux positifs** : passer au mode `--strict` pour les nouvelles
   opérations, garder l'ancien mode pour les re-vérifications de bulk.

---

## 5. Codes de diagnostic

Tous les codes sont deux caractères alphabétiques + un chiffre : `[A2]`, `[B1]`,
etc. Les regrouper par catégorie pour lire les résultats rapidement.

### Catégorie A — Annales (chronologie)

| Code | Niveau | Sens |
|---|---|---|
| A2 | erreur | Une date d'en-tête `## [YYYY-MM-DD]` apparaît après une date antérieure — rompt la chronologie inverse |
| A3 | erreur | `updated:` du frontmatter est antérieur à la date de la dernière entrée d'annales |
| A4 | erreur | Un en-tête d'annales est en doublon exact (même date, même titre) |
| A5 | avertissement | Double ligne vide avant un séparateur — **signature d'un ajout mécanique plutôt qu'insertion propre** |
| A6 | avertissement | Plusieurs champs `- **Commit** :` dans une même section d'annales — **corps d'entrée orphelin : en-tête détruit par une insertion qui a remplacé au lieu de précéder** (incident 2026-08-28) |

### Catégorie B — Frontmatter (hygiène)

| Code | Niveau | Sens |
|---|---|---|
| B0 | erreur | Aucun frontmatter délimité `---` détecté |
| B1 | erreur | Une clé requise manque (Sceau Recteur pour le circuit) |
| B2 | erreur | `sources_count` ≠ nombre réel de `sources:` |
| B3 | erreur | `updated` antérieur à `created` |
| B4 | erreur | `sources:` doctrinal pointe vers `meta/` (étanchéité rompue) |

### Catégorie C — Liens (intégrité et étanchéité)

| Code | Niveau | Sens |
|---|---|---|
| C1 | avertissement | Lien `[[…]]` non résolu (pas de cible au dépôt) |
| C2 | avertissement | Slug ambigu : plusieurs cibles possibles |
| C3 | erreur | Étanchéité rompue : ex. `doctrinal/` pointe vers `atelier/` |
| C4 | avertissement | Fichier de service (`annales.md`/`index.md`) d'un circuit neutre pointant vers `meta/` — sens interdit par §VI, signalé sans bloquer (append-only des annales déjà publiées) |

**Convention code (2026-08-28)** : un wikilink entre backticks (span inline)
ou dans une clôture ```` ``` ````/`~~~` est de la syntaxe citée en exemple —
documentation d'un motif, code du validateur lui-même — jamais un lien vivant.
C1/C3/C4 l'ignorent. Pour citer un wikilink dans une fiche sans le rendre
vivant, l'écrire entre backticks.

---

## 6. Résolution des anomalies courantes

### A2 — Rupture d'ordre des annales

**Symptôme** : `[A2] doctrinal/annales.md:26 — rupture d'ordre : 2026-07-16 après 2026-07-14`

**Cause** : une entrée a été ajoutée en fin de fichier plutôt qu'insérée après
l'en-tête.

**Fix** : relocaliser l'entrée en haut du fichier (après le bloc d'introduction),
conformément au correctif étendu §8, étape 3. Commander à Claude Code ou éditer
manuellement.

### B2 — sources_count faux

**Symptôme** : `[B2] doctrinal/fiche.md — sources_count: 5 ≠ nombre réel (2, dont
1 hors marqueur `to-source`)`

**Cause** : le champ `sources_count:` du frontmatter n'a pas été mis à jour lors
d'une modification des `sources:`.

**Fix** : corriger manuellement le nombre ou demander à Claude Code de le
recalculer sur le lot. Le script gère `to-source` comme marqueur, pas comme source.

### C1 — Lien non résolu

**Symptôme** : `[C1] doctrinal/fiche.md — lien non résolu : [[doctrinal/sources/inexistante]]`

**Cause** : la fiche pointée n'existe pas au dépôt, ou le chemin est mal écrit.

**Fix** : vérifier que la cible existe ; si elle n'existe pas et qu'elle est
prévue, l'ajouter à une TODO ; si c'est un lien cassé, le corriger ou le
supprimer.

### A6 — Corps d'entrée orphelin

**Symptôme** : `[A6] doctrinal/annales.md:12 — corps d'entrée orphelin possible : 2 champs - **Commit** : ...`

**Cause** : une insertion en tête d'annales a *remplacé* l'en-tête `## [date]`
de l'entrée suivante au lieu de le précéder — le corps de l'ancienne entrée
se retrouve fusionné sous le nouvel en-tête, invisible pour A2/A4/A5.

**Fix** : retrouver l'en-tête original dans l'historique git
(`git log -S "motif du corps" -- <fichier>`, puis `git show <sha>:<fichier>`),
et le réinsérer tel quel au-dessus de son corps. Avertissement non bloquant :
une entrée groupée légitime peut citer plusieurs commits (ex. connu :
`atelier/annales.md`, entrée du 2026-08-20).

### C3 — Étanchéité rompue

**Symptôme** : `[C3] doctrinal/fiche.md — étanchéité rompue : doctrinal pointe vers atelier — [[atelier/…]]`

**Cause** : une fiche du circuit doctrinal contient un lien vers un autre circuit
interdit par la règle du Commandement 3.

**Fix** : relocaliser le lien ou la matière concernée. C'est une violation
structurelle, bloquer dessus systématiquement.

### C4 — Fichier de service neutre pointant vers `meta/`

**Symptôme** : `[C4] doctrinal/annales.md — lien doctrinal (neutre, fichier de service) → meta/ ...`

**Cause** : un `annales.md`/`index.md` de circuit neutre échappe à C3
(exemption légitime) mais porte un wikilink vers `meta/` — sens interdit
par §VI.

**Fix** : neutraliser le wikilink côté neutre (chemin entre backticks, texte
conservé verbatim — l'annales est append-only, ne jamais réécrire le fond), et
poser le lien vivant dans le sens autorisé : de la fiche `meta/` concernée
vers le circuit neutre.

---

## 7. Historique et archivage

Créer un dossier pour les rapports :

```bash
mkdir -p /root/wiki/meta/audits-invariants
# Puis, à chaque clôture d'intégration importante :
python3 verifier-invariants.py --racine . --json > \
  meta/audits-invariants/audit-$(date +%Y-%m-%d_%H%M%S).json
```

Permet de tracer l'historique et de détecter des dérives qui reviendraient
sporadiquement (notamment les `sources_count` qui tendent à redériver).

---

## 8. Limites du script

- **Liens ambigus** : Si deux fiches portent le même nom (ex. deux
  `discernement.md` dans des répertoires différents) et qu'un lien pointe par
  slug seul, le script les signale mais ne peut trancher laquelle. C'est correct
  — c'est un vrai problème à résoudre manuellement.
- **Frontmatter complexe** : Le parseur YAML est minimal, volontairement (zéro
  dépendance). Les structures très complexes (nesting profond, scalaires spéciaux)
  ne sont pas gérées. Ajouter des cas au fur et à mesure si besoin.
- **Wikilinks hors norme** : Les `[[…|…]]` avec alias custom ne sont pas parsés.
  Ajouter à `RE_WIKILINK` si besoin.

---

## 9. Prochaine étape

Lancer la première exécution dès demain matin sur le dépôt réel, archiver le
résultat, et nous transmettre la liste des faux positifs pour affiner le script
avant de le brancher en mode `--strict`.

```bash
# Le jour J
cd /root/wiki
python3 verifier-invariants.py --racine . --json > meta/audits-invariants/debut-calibrage-$(date +%Y-%m-%d).json
python3 verifier-invariants.py --racine .  # sortie lisible pour révision manuelle
```
