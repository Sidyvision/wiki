---
title: "Proposition — Circuit Discernement (spéculations personnelles)"
type: meta
updated: 2026-06-20
---

# Proposition d'extension du protocole — à intégrer dans `CLAUDE.md`

## 1. Nouveau dossier

```
doctrinal/
├── discernement/     ← NOUVEAU : spéculations personnelles de Sidy, datées, en cours de discernement
```

- Fichier : `doctrinal/discernement/YYYY-MM-DD_titre-court.md` (même convention que `etudes/`)
- `type: discernement` (nouveau type, à ajouter à l'énumération `type` du Sceau Recteur)
- Une page = une spéculation (ou un cluster de spéculations très proches issues d'une même conversation)

## 2. Sceau Recteur — 5e valeur de `status`

```yaml
status: traditionnel | academique | profane | contre-traditionnel | speculatif
```

`speculatif` = hypothèse personnelle de Sidy, ni validée ni rejetée par une autorité traditionnelle au moment de la rédaction. C'est un statut *transitoire* : à la clôture du discernement, soit la page passe à un statut définitif (`traditionnel` si confirmée comme lecture orthodoxe légitime, `contre-traditionnel`/`profane` si elle s'avère une dérive), soit elle reste `speculatif` avec mention « en cours ».

## 3. Le bloc normalisé — à ajouter en IV (Protocoles d'Exécution) du CLAUDE.md

```markdown
> 🔍 **Discernement — Spéculation Personnelle**
> **Statut** : en cours | validée | invalidée
> **Hypothèse initiale** (datée, reformulée fidèlement) : ...
> **Généalogie des idées** :
>   - Filiation orthodoxe possible : [[symbole/autorite-x]] — nature du rapprochement
>   - Parenté hétérodoxe possible : [[deviation-y]] — nature du rapprochement
> **Examen formel** (jurisdiction Claude — cohérence logique/terminologique, jamais le principe) : ...
> **Conclusion** : si validée → pourquoi et par quelle autorité ; si invalidée → la position orthodoxe de redressement, avec source ; si en cours → ce qui reste à éclaircir et ce qu'il faudrait pour trancher.
```

Rappel du Commandement 12 (upakarana) : Claude documente la généalogie, signale les tensions formelles, cite les positions orthodoxes existantes — mais ne tranche jamais lui-même la validité métaphysique d'une spéculation. Le statut "validée/invalidée" doit être attribué par Sidy (ou par une autorité textuelle citée), jamais auto-décrété par Claude.

## 4. Articulation avec `etudes/`

- `discernement/` = registre atomique, daté, une spéculation à la fois — le grain fin.
- `etudes/` = synthèse transversale quand un pattern émerge sur plusieurs entrées de `discernement/` (ex. une étude `2026-XX-XX_genealogie-des-jinns-chez-sidy.md` qui croise 3-4 pages de `discernement/` autour d'un même thème récurrent).
- Lien autorisé dans les deux sens entre `discernement/` et `etudes/` (les deux sont doctrinaux, pas de cloison entre eux).
- `discernement/` peut lier vers `deviations/` et `symboles/`/`autorites/` normalement (généalogie des idées) ; l'inverse (un symbole/autorité orthodoxe pointant vers une spéculation personnelle non tranchée) est à éviter sauf validation explicite, pour ne pas contaminer une page de référence par une hypothèse encore instable.

## 5. Impact sur le triage des 140 conversations

Les conversations classées **A+C** où le contenu personnel est en réalité une spéculation métaphysique (ex. #10 *Artefact Interaction*, #24 *Rayon fontanelle*, #67 *Idée depuis la Khalwa*, #115 *Expérience spirituelle et interprétation*, etc.) iront probablement vers `discernement/` plutôt qu'un simple éclatement A/C classique. Je repasserai sur ces lignes du triage pour proposer, au cas par cas, soit le split classique (symbolisme→doctrinal, récit brut→meta), soit une page `discernement/` si la spéculation a une vraie portée généalogique.

---

*Cette proposition est à valider puis à transmettre à la session Claude Code (serveur) pour intégration effective dans le `CLAUDE.md` du dépôt — l'app iPad ne peut pas committer.*
