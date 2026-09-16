---
title: "Gloton, lexique coranique — journal de la moisson des racines (section A, 28 photographies)"
type: outillage
tags: [index-lexical, gloton, lexique-coranique, moisson, transcription-photo, journal-de-passe, reprise]
created: 2026-09-16
updated: 2026-09-16
sources:
  - "Maurice Gloton, Une approche du Coran par la grammaire et le lexique, section III A — lexique coranique complet, pp. 233-782. Photographies de l'exemplaire physique de Sidy (raw/Une approche du Coran - Gloton/, hors git, 82 JPG 5712x4284)."
  - "Légende des 14 cases, pp. 231-232 du même ouvrage."
links: []
original: []
---

# Journal de la moisson — où en est le dépouillement, et comment le reprendre

> ⚙️ **Pièce de reprise, pas de doctrine.** Ce document existe pour qu'une session
> neuve puisse continuer le dépouillement sans rien redécouvrir. Il consigne l'état
> exact du travail, l'outil, les contrôles éprouvés, et ce qui reste à faire.

---

## 1. Ce que l'on cherche, et pourquoi

Verdict de Sidy du 2026-09-16 : le dépôt fait de la recherche ; les lexiques,
dictionnaires, index et glossaires y servent à **instruire, référencer, compléter,
renforcer**. Une adresse de lexique n'instruit rien. Un **sens** instruit.

Conséquence opératoire, déjà actée : la moisson retient pour chaque bloc-racine de la
section A la **case 4 — les traductions de la racine**, et pas seulement ses
coordonnées. Destination : une fiche `type: index-livre` dans
`atelier/rd/bibliotheque/`, qui alimente `glossaire-unifie.md` par
`generer-glossaire-unifie.py`. Cette destination **ne se redemande pas** : elle
découle de la finalité du dépôt.

## 2. État au 2026-09-16

**80 racines transcrites** avec numéro, radicales, case 2 et case 4, dans
`atelier/rd/outillage/index-lexical/moisson-racines-gloton.tsv` — cinq colonnes
séparées par tabulation : `numero`, `radicales`, `case2`, `page`,
`traductions_de_la_racine`. Trié par numéro.

Numéros couverts :
0036-0059 · 0213-0219 · 0298-0323 · 0425-0438 · 0527-0535.

Sur environ **185 blocs-racines lisibles** dans les 28 photographies de section A.
Reste donc environ 105.

## 3. L'outil

`atelier/rd/outillage/extraire-bandeaux-racines-gloton.py` — détecte sans OCR les
bandeaux gris des blocs-racines et les empile en planches lisibles.

Principe : seuil de gris **adaptatif** et non absolu. L'éclairage varie d'une page à
l'autre d'une même double page ; un seuil fixe prend le papier blanc de la page
sombre pour le bandeau gris de la page claire. Chaque ligne est donc comparée au blanc
**propre à sa page** (90e centile des médianes de luminance), avec `ratio = 0.935`.
Mesure par ligne : la **médiane** de luminance, robuste au texte.

Invocation (dépasse 120 s — à lancer en arrière-plan) :

```
cd "/root/wiki/raw/Une approche du Coran - Gloton" && rm -rf /tmp/bx && \
python3 /root/wiki/atelier/rd/outillage/extraire-bandeaux-racines-gloton.py \
  --sortie /tmp/bx IMG_058*.JPG IMG_059*.JPG IMG_060*.JPG IMG_0610.JPG
```

Produit **107 planches** dans `/tmp/bx/`. Sortie volatile : la relancer coûte deux
minutes, rien n'est perdu à ne pas la conserver.

**Limites observées** : la marge de recadrage rogne parfois la parenthèse de la case 2
sous le numéro (cas de 0434), et prend parfois du texte courant ou un bord de tissu
pour un bandeau (faux positifs sans gravité). Une reprise gagnerait à augmenter
légèrement `marge`.

## 4. Planches lues et planches restantes

**48 planches lues**, de `IMG_0581G_00` à `IMG_0594D_01`.

**59 planches restantes**, dans l'ordre :
IMG_0580D_00 · IMG_0580G_00 · IMG_0580G_01 · IMG_0583G_01 · IMG_0583G_02 ·
IMG_0595D_00 · IMG_0595D_01 · IMG_0595G_00 · IMG_0595G_01 · IMG_0596D_00 ·
IMG_0596D_01 · IMG_0596G_00 · IMG_0597D_00 · IMG_0597G_00 · IMG_0597G_01 ·
IMG_0598D_00 · IMG_0598G_00 · IMG_0598G_01 · IMG_0599D_00 · IMG_0599D_01 ·
IMG_0599G_00 · IMG_0599G_01 · IMG_0599G_02 · IMG_0600D_00 · IMG_0600D_01 ·
IMG_0600G_00 · IMG_0600G_01 · IMG_0600G_02 · IMG_0601D_00 · IMG_0601D_01 ·
IMG_0601G_00 · IMG_0601G_01 · IMG_0602D_00 · IMG_0602D_01 · IMG_0602G_00 ·
IMG_0603D_00 · IMG_0603D_01 · IMG_0603G_00 · IMG_0604D_00 · IMG_0604D_01 ·
IMG_0604G_00 · IMG_0604G_01 · IMG_0605D_00 · IMG_0605G_00 · IMG_0605G_01 ·
IMG_0606D_00 · IMG_0606D_01 · IMG_0606G_00 · IMG_0607D_00 · IMG_0607G_00 ·
IMG_0607G_01 · IMG_0608D_00 · IMG_0608G_00 · IMG_0608G_01 · IMG_0610D_00 ·
IMG_0610D_01 · IMG_0610D_02 · IMG_0610G_00 · IMG_0610G_01.

Suffixe `G` = page de gauche, `D` = page de droite ; le numéro à deux chiffres est
l'ordre du bandeau du haut vers le bas de la page.

## 5. Carte de couverture de la campagne

Relevée au fil de la lecture. Elle n'existait jusqu'ici que dans les notes de session.

| photographies | entrées | pages |
|---|---|---|
| IMG_0580 | calibrage (légende + ouverture) | 232-233 |
| IMG_0581-0583 | 0036-0059 | 244-249 |
| IMG_0584 | 0213-0219 | 300-301 |
| IMG_0585-0589 | 0298-0323 | 324-331 |
| IMG_0590-0591 | 0425-0436 | 362-365 |
| IMG_0592 | 0437-0438 | 366-367 |
| IMG_0593-0594 | 0527-0535 | 394-397 |
| IMG_0595 | 0578-0583 | 412-413 |
| IMG_0596-0598 | 0995-1012 | 546-551 |
| IMG_0599-0600 | 1139-1151 | 594-597 |
| IMG_0601-0603 | 1270-1298 | 636-647 |
| IMG_0604-0606 | 1440-1459 | 692-697 |
| IMG_0607-0608 | 1694-1702 | 772-775 |
| IMG_0610 | 0518-0521 | 390-391 |

IMG_0585 et IMG_0586 sont **deux prises de la même double page** (pp. 324-325). Cette
redondance n'est pas un gaspillage : elle fonde un contrôle (§6).

## 6. Les contrôles, et lesquels ont été vus refuser

Épreuve des contrôles (§VII du protocole racine) : *un contrôle dont on n'a pas vu
l'échec n'est pas un contrôle vérifié.* Trois contrôles ont maintenant refusé une
lecture.

**1. Voisinage numérique et alphabétique — vu refuser deux fois.**
Consigné dans `2026-09-16_gloton-adressage-15-racines.md` §5 (0055 et 1150).

**2. Photographie en double — vu refuser trois fois, 2026-09-16.**
IMG_0585 (pp. 324-325) est sous-exposée ; IMG_0586 rephotographie la même double page
nettement. Les cases 2 lues sur IMG_0585 ont été **refusées** par IMG_0586 :

| entrée | lu sur IMG_0585 | imprimé, lu sur IMG_0586 |
|---|---|---|
| 0298 ح ج ر | 31 | **21** |
| 0299 ح ج ز | 3 | **2** |
| 0302 ح د د | 35 | **25** |

Le contrôle est donc éprouvé. Portée : il ne vaut que là où la campagne a doublé la
prise ; ailleurs, la case 2 d'une photographie sombre reste une lecture non recoupée.

**3. Folio imprimé et pas de deux — vu refuser une fois, 2026-09-16.**
Chaque photographie couvre une double page ; deux photographies consécutives avancent
exactement de deux pages. Chaîne vérifiée sur titres courants lus directement :
IMG_0587 = 326/327, IMG_0588 = 328/329, IMG_0589 = 330/331, IMG_0590 = 362/363,
IMG_0591 = 364/365, IMG_0592 = 366/367, IMG_0593 = 394/395, IMG_0594 = 396/397
(folios lus sur IMG_0587D 327, IMG_0588G 328, IMG_0589G 330, IMG_0590G 362,
IMG_0591G 364, IMG_0592G 366, IMG_0592D 367, IMG_0593G 394, IMG_0594G 396,
IMG_0594D 397).

Ce contrôle a **refusé une page déjà publiée** : 0429 خ ف ض était donné p. 364 au §2
de la fiche d'adressage ; le folio imprimé le met p. **363**. Correction portée à la
fiche, conformément au Cmd 10 (corriger visiblement, jamais effacer en silence).

## 7. Refus de lecture assumés

**0434 خ ل ط, case 2 : `?`.** Le recadrage a rogné la parenthèse sous le numéro et ce
qui restait était illisible. Plutôt que deviner, la valeur est portée inconnue
(Cmd 5). À récupérer par un recadrage de la page de droite d'`IMG_0591.JPG` avec une
marge haute plus large.

**0531 ر ب ب, case 4 : tronquée à droite.** La photographie coupe le bord droit du
bandeau ; les segments manquants sont marqués `[...]` dans le TSV.

## 8. Ce qui reste à faire

1. **Lire les 59 planches restantes** (§4) et porter au TSV, pour chaque bloc :
   case 1 (numéro), case 2 (nombre d'entrées), case 3 (radicales), **case 4
   (traductions de la racine)**.
2. **Récupérer la case 2 de 0434** par recadrage élargi.
3. **Déposer la moisson** en fiche `type: index-livre` dans
   `atelier/rd/bibliotheque/`, au format à quatre colonnes que
   `generer-glossaire-unifie.py` sait lire, puis **régénérer**
   `glossaire-unifie.md` — artefact dérivé, jamais édité à la main.
   `glossaire-unifie.md` est vide depuis le 2026-08-22 : le générateur, le
   validateur et le format de fiche existent tous, rien n'y a jamais été versé.
   C'est la forme concrète du « à chaque fois nous revenons au même point ».
4. **Transcription intégrale de la section B** (index, pp. 785-829, ~8000 entrées) :
   non engagée, réservée au verdict. Les trois contrôles mécaniques envisagés devront
   chacun avoir été **vus refuser** sur une faute fabriquée avant d'être tenus pour
   des contrôles.

## 9. Notes d'exécution

- Les photographies de la section A **sont** la source ; la table des matières,
  l'index et le glossaire sont d'orientation (discipline des sources, §VII).
- `convert`/`magick` ne sont pas installés. Recadrage et agrandissement par `python3`
  et PIL, `Image.LANCZOS`, sortie en `/tmp/`.
- Écrire de la prose française dans un `python3 - <<'PYEOF'` échoue sur les tirets
  cadratins. Passer par `cat <<'EOF' > fichier`.
- Le TSV se remplit **par lots au fil de la lecture**, jamais accumulé en mémoire de
  session : une session qui s'interrompt ne perd alors que son dernier lot.

## 10. Réservé au verdict

Rien de ce journal n'affirme sur le sens. Le seul point doctrinal rencontré pendant la
passe reste consigné au §8 de `2026-09-16_gloton-adressage-15-racines.md` et n'est pas
repris ici.
