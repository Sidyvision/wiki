---
title: "Passation — session Instrument (terminal) vers Claude Code claude.ai, 2026-08-30 soir"
type: meta
status: transmis
tags: [brief, passation, instrument, incommensurable, guenon, prototype]
created: 2026-08-30
updated: 2026-08-30
---

# Passation — session Instrument vers Claude Code (claude.ai)

> **Motif** : budget de session épuisé côté terminal. La matière doctrinale est
> **intégrée et commitée** ; ce qui reste est un travail de **rendu sur le
> prototype**, qui n'a pas été commencé.

## 0. Suite donnée — session claude.ai du 2026-08-30 (soir)

> **La passation est exécutée.** Les deux pièces qui restaient sont closes.

| Point du brief | État |
|---|---|
| **§2 — LA TÂCHE : reporter les six trouvailles au prototype** | ✅ **fait** — sept stations de navigation (0-6), commit `d20de1c`. Détail : `atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable.md` §9 |
| **§5.3 — degrés 1-10 du *Nafas al-Raḥmān*** (« seule pièce qui demande une action de Sidy ») | ✅ **clos** — Sidy a fourni le cliché de la p. 35 le soir même ; `to-source` levé, commit `f09429b` |
| §5.1, §5.2, §5.4, §5.5, §5.6 | ouverts, non traités — hors périmètre |
| §6 — matière disponible en `raw/` | non exploitée (`raw/` gitignoré, inaccessible hors serveur) |

**Trois choses en sont sorties qui n'étaient pas prévues au brief :**

1. **Le halo du sommet du rendu était faux dans sa géométrie même** — un cône se
   rétrécissant vers le haut, donc une convergence, donc l'erreur exacte que la
   contrainte 2 interdit. Corrigé en bande de section constante.
2. **« Hāhūt » n'est pas de Gloton.** La collation de la p. 35 donne le titre que
   la source porte : « Le Degré divin ». L'assimilation venait du Gem (persona
   IA, jamais source) et **contredit la fiche-table elle-même**. Tension relevée,
   **non tranchée — verdict à Sidy** (voir `doctrinal/annales.md`).
3. **Une erreur de rendu commise et consignée** : des marques rigoureusement
   égales en coordonnées de monde se projettent **inégales** en perspective. Une
   figure juste dans le monde peut mentir à l'écran ; la caméra réintroduit la
   mesure que la géométrie avait exclue. Corrigé en espace-écran.

## 1. Reprise en trois commandes

```bash
cd /root/wiki
git pull origin main
python3 verifier-invariants.py --racine /root/wiki
```

État attendu : **`0 erreur(s), 0 avertissement(s)`**. Le faux positif [A6] a été
raffiné ce matin — toute régression est donc désormais visible. Manifeste :
`python3 atelier/rd/outillage/generer-manifeste.py --repo /root/wiki` →
`46 nœud(s), 23 ancrage(s), 4 registre(s), 0 avertissement(s)`.

## 2. LA TÂCHE — reporter les trouvailles au prototype

**C'est le seul travail restant, et il est entièrement décrit ici.**

Commande de Sidy, mot pour mot : « **reporte toutes les trouvailles au prototype
de l'instrument en incluant la précédente (plan, volume) de façon digeste,
navigable/pratique car il s'agit d'un instrument de "navigation" (*sulūk*,
contemplation). Aussi l'instrument prend évidemment pour référence l'état
humain.** »

Fichier : `atelier/rd/instrument/instrument-prototype.html` (1504 lignes).
Structure : `<canvas id="scene">` + panneaux `.panneau` (`#titre`, `#aide`,
`#info`, `#legende`), touche **U** = bascule vue éclatée / axe unifié, fonction
`toucher(cx,cy)` remplissant `#info-label` / `#info-deg` / `#info-src`.

**Aucune donnée n'est à modifier** : `instrument-donnees.yaml` est juste et
inchangé. Le travail est de **présentation**.

### Ce qu'il faut rendre navigable (les six trouvailles)

| # | Trouvaille | Source au dépôt |
|---|---|---|
| 1 | **La figure est dimensionnelle** : un état est une **surface**, l'être total un **volume** ; l'épaisseur d'un état sur l'axe est infinitésimale. La figure juste n'est pas une échelle mieux graduée, c'est un **saut de dimension** (plan → volume, par intégration) | `doctrinal/sources/guenon-symbolisme-croix-ch26-27-…` |
| 2 | **Ampleur / exaltation** — le vocabulaire juste : *ampleur* = extension dans un état (plan horizontal), *exaltation* = hiérarchie entre états (axe vertical) ; la différence des modalités est « **rigoureusement nulle** » suivant l'exaltation, un état entier s'y réduisant à **un point** | `doctrinal/sources/guenon-etats-multiples-ch3-10-11-12-…` |
| 3 | **L'incommensurabilité est absolue**, « ne dépendant d'aucune convention » — aucun réglage d'échelle ne la rend ni ne la résorbe | idem #1 |
| 4 | **Le centre n'est pas un lieu fixe de l'axe** : les guṇas se répartissent relativement à l'état pris pour base, et n'importe quel état peut devenir central selon où se détermine le plan de réflexion du Rayon Céleste | `doctrinal/sources/guenon-symbolisme-croix-ch5-trois-gunas` |
| 5 | **L'état humain est la référence** — et c'est fondé : « le plan qui sert de base est **indéterminé en principe** […] ce n'est que **secondairement** qu'on le détermine comme représentant l'état humain ». Rapporter les états à l'état humain est « **assurément légitime** ». **Exigence unique : que le rendu déclare ce choix comme un point de vue, non comme un absolu.** | `doctrinal/sources/guenon-etats-multiples-ch3-10-11-12-…`, ch. XI |
| 6 | **La surface des Eaux** = plan de séparation formel/informel = **plan de réflexion du Rayon Céleste** = lieu de la **discontinuité unique** (le *Fiat Lux*). Les deux ouvrages se referment sur ce terme | idem #2 (ch. XII) + ch. XXVII |

### Contraintes de rendu, non négociables (déjà établies au chantier §2)

1. L'Inconditionné **n'est pas le sommet de la série** — s'il est en haut de
   l'axe, il en est le dernier degré, donc commensurable.
2. **La discontinuité est égale depuis chaque degré** — désormais **sourcé** :
   « tous sont parfaitement équivalents quand ils sont envisagés de l'Infini »
   (ch. XXVII). Exclut tout halo croissant, tout dégradé, toute convergence.
3. **La hiérarchie des états demeure** — il ne s'agit pas d'aplatir.

Et une quatrième, tirée du ch. III : **l'Être n'est pas infini** ; seul l'ensemble
Être + Non-Être l'est. Le halo « Hāhūt non manifesté » du rendu actuel doit être
relu à cette lumière.

### Registre à tenir

Sidy insiste : c'est un instrument de **navigation** (*sulūk*), de contemplation —
pas un diagramme d'exposition. « Digeste, navigable, pratique. » Le rendu doit
pouvoir être **parcouru**, pas lu.

## 3. Ce qui a été fait aujourd'hui (déjà commité et poussé)

| Commit | Objet |
|---|---|
| `6a26046` | Table des 38 degrés corrigée — la contradiction bloquante n'existait pas |
| `548a770` | Chantier « Figurer l'incommensurable » **débloqué** + règle de métier 6 |
| `47ee330` | Ouverture du discernement Kursī ↔ Hokhmah/Binah |
| `3671100` | Numérotation Vêdânta : deux éditions, double numérotation, pierre tombale |
| `151e181`, `f41f1f8` | Jurjānī p. 47 et p. 441, transcription intégrale |
| `da3c669` | **Verdict *kumiko*** + *Symbolisme de la Croix* ch. V, XXVI, XXVII |
| `585fa1a` | *Les états multiples de l'être* ch. III, X, XI, XII |

Les deux entrées d'annales couvrant ces opérations sont en place
(`doctrinal/annales.md`, `atelier/annales.md`), SHA portés.

## 4. Verdicts rendus par Sidy ce jour — à ne pas rouvrir

- **Kursī ↔ Hokhmah/Binah : joint *kumiko* approuvé** (complémentarité, non
  équivalence). Fiche close, `status: traditionnel`.
- **L'Instrument prend l'état humain pour référence** (§2 #5 ci-dessus).
- Table cakra/*laṭāʾif* : **maintenue en *kari-kumi***.
- Sentiers ↔ nâdîs (P1) : **lecture *kumiko* approuvée**.
- Cellule `mandala` d'*Ājñā* : comblée d'après la Planche VII.
- [A6] : raffiné, non supprimé.

## 5. Points ouverts, dans l'ordre d'importance

1. **Le report du joint Kursī↔Hokhmah/Binah en ancrage** n'est **pas décidé**. Un
   ancrage `qabbalah/hokhma ↔ tasawwuf/degre-18` serait le premier joint entre un
   registre `parallele` et l'échelle des degrés, et **fermerait un triangle de
   transitivité** avec l'ancrage `hokhma ↔ ājñā` établi le 2026-08-29 — le
   troisième côté n'ayant jamais été instruit (Cmd 3). Détail dans la fiche de
   discernement, §6.
2. **(P2)** « De quel cœur rayonne le réseau » — Sidy : « je ne suis pas encore
   fixé ». À rapprocher de la trouvaille #4 (le centre n'est pas fixe), qui y
   arrive par un autre chemin.
3. **Degrés 1-10 du *Nafas al-Raḥmān*** — entièrement à établir. Exigent les pages
   **antérieures à la p. 36** de Gloton, non photographiées. *Seule pièce qui
   demande une action de Sidy.*
4. **Une troisième numérotation de *L'Homme et son devenir*** : les renvois du
   *Symbolisme de la Croix* précisent « 3ᵉ éd. » avec des numéros incompatibles
   avec les deux déjà connues. Constat versé, règle non étendue.
5. **27 fiches absentes de `doctrinal/index.md`** (dont 2 légitimement : le
   `_template` et la pierre tombale `ch21`). Sidy pensait le point réglé — la
   mesure dit le contraire. Non traité, hors périmètre de la session.
6. Divergence *Vishuddha* table/planche d'Avalon — non tranchée.

## 6. Disponible en `raw/`, non exploité

- **`Transcription Jurjani` — 57 clichés** non transcrits. Consigne permanente de
  Sidy : « transcris **toutes** les définitions que tu trouves ».
- *Les états multiples* : ch. II, V-VIII, XIV-XVIII encore non intégrés.
- *Le Symbolisme de la Croix* : XIV-XXII, XXV, XXVIII, XXX non intégrés (dont
  **XX « Le vortex sphérique universel »** et **XVIII « Passage des coordonnées
  rectilignes aux coordonnées sphériques »**, tous deux probablement utiles au
  rendu).
- *Rig-Veda* (16 clichés), *Origine polaire* (18), *Ihwan al-Safa* (34),
  *La Porte du Ciel* (59) — tous non transcrits.

## 7. Pièges connus

- `raw/` est **gitignoré** : inaccessible hors du serveur.
- Les noms de dossiers de `raw/` portent des accents composés — `ls`/`find`
  échouent, **passer par `python3` + `os.listdir`**.
- `doctrinal/annales.md` et `atelier/annales.md` sont **append-only** : ne jamais
  réécrire une entrée existante (c'est la raison d'être de la pierre tombale
  `guenon-homme-devenir-vedanta-ch21-…`).
- Une page orthodoxe (`type: symbole`, `source`) **ne pointe jamais** vers un
  discernement non tranché (`doctrinal/CLAUDE.md`, étanchéité inversée).
- `to-source` : la levée du 2026-08-30 ne couvre **que** *Symboles de la Science
  sacrée*. Les fiches *Symbolisme de la Croix* et *États multiples* restent
  `to-source` — le clipping porte l'édition Trédaniel 1996, l'exemplaire de Sidy
  est Véga.
