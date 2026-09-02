---
title: "PRO-08 — un dossier versionné pour les textes convertis : spécification"
type: infrastructure
chantier: PRO-08
tags: [atelier, rd, infrastructure, chantier, spec, raw, gitignore, invariants]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/infrastructure/pro-08-textes-convertis-versionnes/intent]]"
---

# PRO-08 — spécification

## 1. Le nom et la place — trois candidats, un recommandé

| candidat | pour | contre |
|---|---|---|
| **`raw/textes/`**, avec une négation dans `.gitignore` | ne touche pas au `§II` ; garde la sémantique « sources » | **contredit le constat de Sidy** : le dossier resterait *dans* `raw/`, dont il dit qu'il masque. Et une exception à l'intérieur d'un dossier exclu se relit mal à froid |
| **`textes/`** — dossier de premier niveau ⭐ | dit ce qu'il est ; visible d'Obsidian sans exception ; `§II` le déclare une fois, clairement | amende le `§II` |
| `doctrinal/textes/` ou `atelier/textes/` | pas de nouveau dossier racine | **faux** : ces textes ne relèvent d'aucun circuit — Guénon, Jurjani, Avalon et Shayegan ne sont ni doctrine tranchée ni métier |

**Recommandé : `textes/`**, avec la déclaration explicite, calquée sur ce que le
protocole fait déjà pour `meta/` :

> `textes/` **n'est pas un sixième circuit**. Il ne porte aucun Sceau, n'entre
> dans aucun régime de liens, et n'est la cible d'aucun wikilink. C'est le
> **cabinet de lecture** du dépôt : la source primaire convertie, telle qu'elle a
> été reçue, mise à portée du poste CONSULTATION.

### Arborescence

```
textes/
├── LISEZ-MOI.md          ← ce qu'est ce dossier, ce qu'il n'est pas (au Sceau atelier)
└── <ouvrage-en-slug>/    ← un dossier par ouvrage, nom normalisé
    └── <chapitre>.md     ← le texte converti, INTACT
```

⚠️ **Normalisation des noms, et le motif est concret.** Les dossiers actuels de
`raw/` portent leurs noms en Unicode **décomposé** (NFD : `Rene` + accent
combinant) là où un chemin tapé l'est en composé (NFC). Un accès littéral échoue
sur « No such file or directory » **sans rien dire de plus** — piège rencontré
deux fois dans la session du 2026-09-02. Les noms migrés sont donc mis en
**minuscules ASCII, sans accents, tirets** (§III du protocole racine), ce qui
supprime le piège à la racine.

## 2. Le comportement observable

1. Après `git pull`, Obsidian sur iPad affiche `textes/` et **ouvre les
   chapitres**.
2. `verifier-invariants.py` rend **0 erreur, 0 avertissement**.
3. `raw/` est **inchangé** : aucun binaire versionné, aucune pièce nominative
   dans git.
4. Le graphe ignore `textes/` : aucun nœud, aucune arête, aucune orpheline
   fabriquée.

## 3. Ce qu'il faut modifier — et pourquoi chaque ligne

### 3.1 `.gitignore`

Rien à y changer si le dossier est `textes/` : il n'est pas sous `/raw/`.
**C'est un argument de plus pour ce candidat** — la voie `raw/textes/` exigerait
une négation (`!/raw/textes/`), c'est-à-dire une exception à maintenir.

### 3.2 `verifier-invariants.py` — la contrainte dure, éprouvée

**Mesuré, non déduit** (essai du 2026-09-02) : un fichier `.md` sans frontmatter,
placé dans un dossier de premier niveau hors circuit, lève :

```
[B0] textes-essai/essai.md — aucun frontmatter délimité par `---`
1 erreur(s), 0 avertissement(s).
```

Sans amendement, la migration produirait donc **561 erreurs**, c'est-à-dire
exactement le bruit qui avait masqué la seule erreur vraie du 2026-09-01
(chantier OUT-C2). Le remède est d'une ligne, dans un mécanisme **qui existe
déjà** :

```python
PREFIXES_SANS_FM = (
    "meta/projet-unifie/hermes-prompts/",
    "textes/",        # sources converties : ce sont des TEXTES, pas des fiches
)
```

`FICHIERS_SANS_FM` et `PREFIXES_SANS_FM` sont le mécanisme prévu pour « les
fichiers légitimement sans frontmatter ». On ne crée aucune exception nouvelle :
on en déclare une de plus, au même endroit.

**Le contrôle des liens** (C3, étanchéité) ne s'applique pas : `circuit_de()`
rend `None` hors des quatre circuits, et `textes/` n'émet aucun wikilink.

### 3.3 `LISEZ-MOI.md` du dossier

Porte le Sceau atelier (`type: infrastructure`) et dit, en tête : ce que le
dossier est, ce qu'il n'est pas, la provenance de chaque corpus, et **la règle
d'immuabilité** — un texte de `textes/` ne se corrige pas, il se remplace par une
conversion meilleure, datée.

### 3.4 Protocole racine `§II`

Une entrée dans l'arbre, et une phrase de statut. **C'est un amendement du
protocole** : il relève du verdict de Sidy, il est préparé, non appliqué.

## 4. Cas limites, et ce que la spec ne tranche pas

| cas | comportement |
|---|---|
| **147 doublons exacts** (dont 130 dans `Downloads/`, qui redouble intégralement *Symboles de la Science sacrée* et *Études sur l'Hindouisme*) | La migration **ne dédoublonne pas d'office**. Elle les **rapporte**, avec la liste. Dédoublonner est une décision de contenu (Cmd 10, Cmd 13) |
| Un `.md` de `raw/` contenant une donnée personnelle | Le balayage n'en a trouvé **aucun**. Le script de migration **refait le balayage** et **refuse de migrer** tout fichier qui en porterait — garde, pas confiance |
| Collision de noms après normalisation | **Refus bloquant**, jamais d'écrasement silencieux |
| Fichier hors corpus (`Build Your Own Perplexity with Exa.md`) | **Signalé, non migré** : ce n'est pas un texte de source |
| Original dans `raw/` | **Conservé** (Cmd 10). Le retrait est une seconde décision, après que la migration a été éprouvée |

## 5. Critères d'acceptation

| # | critère | commande / observation |
|---|---|---|
| 1 | Le vérificateur accepte les textes nus | `python3 verifier-invariants.py --racine /root/wiki` → 0 erreur |
| 2 | **Et il refuse toujours ailleurs** | Poser un `.md` sans frontmatter **hors** `textes/` → `B0` levé. Sans ce second contrôle, l'amendement pourrait avoir désarmé B0 partout |
| 3 | Le compte est juste | nombre de fichiers migrés + doublons signalés + non migrés = 708 |
| 4 | Aucune donnée personnelle | le balayage du script sort vide ; le faire **échouer volontairement** sur un fichier témoin |
| 5 | `raw/` intact | `git status` ne montre aucun ajout sous `raw/` ; les binaires restent non suivis |
| 6 | Le poids reste tenu | `du -sh textes/` ≈ 14 Mo, et le dépôt ne franchit pas un ordre de grandeur |
| 7 | Le graphe n'invente rien | `generer-cartographie.py` → aucun nœud sous `textes/` |
| 8 | Obsidian les voit | vérification par Sidy, sur iPad, après `pull` — **c'est le seul critère qui compte vraiment**, et lui seul ne peut pas être automatisé |

## 6. Ce qui reste `to-source`

Rien de doctrinal. Ce chantier est de plomberie ; sa seule matière est le disque,
et il a été mesuré.
