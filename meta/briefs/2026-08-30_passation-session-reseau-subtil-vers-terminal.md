---
title: "Passation — session « réseau subtil » (web) vers session terminal"
date: 2026-08-30
type: brief
status: transmis
destinataires: [sidy, session-terminal]
created: 2026-08-30
updated: 2026-08-30
references:
  - doctrinal/discernement/2026-08-30_nadis-du-coeur-sentiers-sephirothiques-tiferet.md
  - doctrinal/discernement/2026-08-30_ternaire-temporel-nadis-janus-bifrons.md
  - atelier/rd/cahiers/2026-08-30_rapport-erreurs-session-hindouisme-soufisme.md
  - atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable.md
  - doctrinal/symboles/table-28-degres-nafas-rahman.md
---

# Passation — de la session web à la session terminal

> **Motif de la passation** (Sidy, 2026-08-30) : `raw/` est inaccessible depuis
> la session web — le dossier est *gitignored* par construction, et les ouvrages
> de Guénon s'y trouvent. La suite du travail demande d'y accéder, donc de
> reprendre depuis le serveur (`/root/wiki`).
>
> **Ce document est le point de reprise.** Il ne résume pas la session — les
> annales le font — il dit **où en est chaque chantier et ce qui l'attend**.

## 1. Reprendre : les trois commandes

```bash
cd /root/wiki
git pull origin main          # tout est sur main, rien n'est en attente ailleurs
python3 verifier-invariants.py --racine /root/wiki
```

État attendu au dernier commit poussé : **`0 erreur(s), 1 avertissement(s)`**
(l'avertissement [A6] est un faux positif documenté, §5 ci-dessous).

> La branche `claude/hinduism-sufism-rnd-o2b1k4` a été resynchronisée sur `main`
> après chaque poussée : les deux pointent sur le même commit. Rien à fusionner.

## 2. Ce qui attend un verdict de Sidy — par ordre d'importance

| # | Objet | Où | Ce qui est demandé |
|---|---|---|---|
| 1 | **Sentiers ↔ nâdîs : lecture par complémentarité** | `doctrinal/discernement/2026-08-30_nadis-du-coeur-sentiers-sephirothiques-tiferet.md` | L'Arbre est-il une **élévation** et les lotus des **plans** d'un même réseau ? Nature proposée : ***kumiko***, non *hozo*. **Instruisible tel quel** — ne dépend d'aucune source manquante |
| 2 | **De quel cœur rayonne le réseau** | même fiche, §3 et §4 quater | *Anāhata* (station de la série) ou le lotus à 8 pétales (siège du *jīva*, d'où sortent les 101) ? Ou la lecture par **positions de l'observateur** ? |
| 3 | **Cellules vides d'*Ājñā*** | `atelier/rd/instrument/instrument-donnees.yaml` | La table ne donne ni couleur de *tattva* ni *maṇḍala* ; la **Planche VII** montre un triangle inversé. Les combler serait juger que la planche prime la table. **Laissées vides** |
| 4 | **26 entrées d'annales sans SHA** (Cmd 9) | `doctrinal/annales.md`, `atelier/annales.md` | Autorisation de réparer. Les SHA sont retrouvables mécaniquement (`git log -S` sur le titre de l'entrée) |
| 5 | **23 fiches absentes de l'index** | `doctrinal/index.md` | Autorisation de compléter (21 `sources/`, 2 `discernement/`, toutes antérieures à la session) |
| 6 | **Faux positif [A6]** | `verifier-invariants.py` | Raffiner le contrôle, ou l'accepter tel quel |

## 3. Ce qui attend une collation sur exemplaire physique

**Ce sont des points de texte, pas d'interprétation. La machine ne peut pas les
trancher.**

### 3.1 ⚠️ Prioritaire — la contradiction de numérotation de la table des 38 degrés

`doctrinal/symboles/table-28-degres-nafas-rahman.md` porte **deux numérotations
incompatibles** :

| Système | Ce qu'il pose |
|---|---|
| « Jabarūt — degrés 9-12 (Figure 2, **p. 92**) » | 9 Corps universel · **10 ʿArsh** · **11 Kursī** · 12 Sphère sans étoiles |
| « degrés 1-10 pré-lettrés + degrés 11-38 = les 28 lettres » | le degré **11 est la *hamza*** |

Le degré 11 ne peut être à la fois le Piédestal et la première lettre. Et le
comptage Figure 1 (8 termes) + Figure 2 (4 termes) donne **12** pré-lettrés,
non 10.

- **À collationner** : Ibn ʿArabī / Gloton, *De la mort à la résurrection*,
  **pages 91-92**.
- **Pourquoi c'est prioritaire** : le rendu de l'Instrument suit le second
  système (degrés 11-38 sur l'axe, 1-10 en halo « non manifesté »). **La frontière
  manifesté / non-manifesté qu'il trace tombe exactement là où les deux
  numérotations divergent** — c'est-à-dire sur l'articulation Kursī → ʿArsh
  désignée comme figure de l'échelle pour le chantier de l'incommensurable.
  **Ce chantier est bloqué tant que ce point n'est pas tranché.**
- **Rien n'a été modifié** dans la fiche.

### 3.2 Les attributions de chapitres XIX-XXI

`doctrinal/sources/guenon-homme-devenir-vedanta-ch15-21.md` attribuait au ch. XXI
« le rejet ou la résorption finale » et plaçait les *nâdîs* au ch. XIX. Le texte
primaire montre que le ch. XXI est celui de **l'artère coronale et du Rayon
solaire**. Sections **conservées et marquées NON VÉRIFIÉES** (Cmd 10), à
collationner sur l'exemplaire.

## 4. Ce que l'accès à `raw/` débloque immédiatement

C'est le motif même de la passation. Trois pièces manquantes sont, ou peuvent
être, dans `raw/` :

| Pièce | Ce qu'elle débloque |
|---|---|
| **Guénon, *Symboles de la Science Sacrée*, ch. XVIII (« Quelques aspects du symbolisme de Janus », p. 123) et ch. XXXVII (« Le symbolisme solsticial de Janus », p. 228)** | le **volet solsticial de Janus** — les deux portes, les deux saints Jean, Cancer/Capricorne — explicitement laissé `to-source` dans [[doctrinal/symboles/janus-bifrons]]. Table des matières déjà transcrite au dépôt |
| **Shayegan, *Hindouisme et Soufisme*, ch. II du commentaire** (« Les disciplines spirituelles », §III) | la **liste ordonnée des sept *laṭāʾif* et de leurs régents** — seule pièce qui rende instruisible la comparaison *laṭāʾif* ↔ *cakra* (micro ↔ micro), demandée depuis le 2026-08-29 |
| **Avalon, chapitres II, III, IV, VI, VII** | non relevés ; copie de travail intégrale déjà en `_inbox/la-puissance-du-serpent.md`, donc **accessible sans `raw/`** |

> **Rappel de procédure** (§VIII.9) : un agent ne traite `raw/` qu'après validation
> du circuit `_inbox/` sur au moins **3 cycles sans anomalie**. Le traitement de
> `raw/` produit des **fiches candidates dans `_inbox/`** (+ `UPDATES.md`), jamais
> d'écriture directe dans les circuits. La chaîne reste :
> `raw/` → analyse → `_inbox/` → validation humaine → intégration standard.

## 5. État de l'outillage, pour ne pas le redécouvrir

```bash
# Générateur du manifeste — NOTER l'option --repo (défaut codé en dur : /root/wiki)
python3 atelier/rd/outillage/generer-manifeste.py --repo /root/wiki
# Attendu : 46 nœud(s), 23 ancrage(s), 4 registre(s), 0 avertissement(s)

# Vérification structurelle (clôture de session, §VII — ne pas sauter)
python3 verifier-invariants.py --racine /root/wiki
```

- **Faux positif connu — [A6]** : `verifier-invariants.py` signale « corps
  d'entrée orphelin possible » dès qu'une entrée d'annales porte deux
  `- **Commit** :`. Une entrée couvrant deux livrables en porte légitimement
  deux. Signalé, **non corrigé** (fichier append-only).
- **Prototype** : `atelier/rd/instrument/instrument-prototype.html` charge
  `wiki-manifest.json` puis Three.js **depuis un CDN**. Pour l'ouvrir hors ligne,
  vendorer `three.min.js` à côté et remplacer la première entrée de la liste de
  repli par `'./three.min.js'`. Touche **U** : bascule vue éclatée / axe unifié.

## 6. Les chantiers ouverts, et leur état exact

| Chantier | Fiche | État |
|---|---|---|
| **Figurer l'incommensurable** | `atelier/rd/instrument/2026-08-30_figuration-de-l-incommensurable.md` | 3 contraintes posées, 4 options de rendu soumises, **5 points à instruire avant tout rendu**. **Bloqué** par §3.1 |
| **Sentiers ↔ nâdîs** | discernement du 2026-08-30 | second examen fait ; **verdict attendu** sur la lecture *kumiko* ; prédiction structurelle posée pour plus tard |
| **Cieux planétaires ↔ *lokas*** (macro ↔ macro) | — | **jamais tentée** ; les deux séries sont au dépôt, la comparaison est licite |
| **Les 22 sentiers** | `doctrinal/sources/kabbale-10-sefirot-structure.md` | non documentés, et **aucun arrangement fixé**. Premier acte : fixer l'arrangement **sur source, pour ses raisons propres**, avant toute comparaison |
| **ʿArsh ↔ Kabbale** | — | ⚠️ le dépôt garde déjà en `doctrinal/symboles/merkavah-muraqaba.md` une **mauvaise version** de ce rapprochement (gématrie sans assise textuelle). Le rapprochement n'est pas jugé ; le mauvais chemin est cartographié |

## 7. À lire en premier depuis le terminal

Deux documents, dans cet ordre :

1. **`atelier/rd/cahiers/2026-08-30_rapport-erreurs-session-hindouisme-soufisme.md`**
   — les vingt défauts de la session, classés par **ce qui les a attrapés**, et
   les cinq règles de métier qui s'en dégagent. C'est le document qui évite de
   refaire les mêmes fautes.
2. **`doctrinal/discernement/2026-08-30_nadis-du-coeur-sentiers-sephirothiques-tiferet.md`**
   — la fiche a été **écrite deux fois le même jour**, les deux examens
   conservés. Son §9 porte la leçon de méthode : entre deux traditions, une
   contradiction apparente est d'abord une invitation à **chercher le point de
   vue depuis lequel les deux sont vraies** ; l'Art. 3 du Sashimono (« jamais de
   joint forcé ») vaut aussi contre une **séparation forcée**.

## 8. Ce qui a été poussé aujourd'hui

`73b215a` · `96e57bc` · `ea0f7ba` · `a94968e` · `fbd50ef` · `2a6f825` ·
`0ccc243` · `3fb961c`, plus leurs entrées d'annales et le merge `d8322d8`.
Tout est sur `main`.
