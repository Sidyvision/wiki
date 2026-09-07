---
title: "Extension du contrôle C1 au cartouche — verifier-invariants.py (épreuve §VII)"
type: experience
statut_experience: adopte
tags: [rd, cahier, outillage, verifier-invariants, controle, epreuve-vii, wikilinks, methode]
created: 2026-09-04
updated: 2026-09-06
sources: []
links: ["[[atelier/rd/cahiers/registre-problemes]]"]
---

# Extension du contrôle C1 au cartouche

> Rapport versé au pôle R&D sur verdict de Sidy (2026-09-04) : la matière est
> **outillage**, non doctrine. Les annales `doctrinal/` n'en gardent qu'un
> pointeur. Origine : l'épreuve des contrôles menée lors de l'intégration
> *The Sabri Ben Rommane's Theory* le même jour.

## 1. Ce que l'épreuve a d'abord fait croire — et pourquoi c'était faux

Une première épreuve §VII avait conclu que `verifier-invariants.py`
« ne contrôle pas l'existence des cibles de wikilinks ». **C'est faux, et le
constat a été rectifié le jour même (Cmd 5).** Le contrôle C1 « lien non résolu »
existe et fonctionne. Le faux lien avait été injecté dans le **cartouche**, non
dans le corps, et la distinction n'avait pas été faite.

Épreuve refaite, **même chaîne morte** aux deux emplacements :

| Emplacement du lien mort | Résultat |
|---|---|
| corps de la fiche | ✅ `[C1] lien non résolu` — refus |
| `cross_links:` du cartouche | ❌ 0 erreur, 0 avertissement — silence |

**Portée exacte du trou** : C1 lisait le **corps** seul. Les wikilinks déclarés
dans le frontmatter n'étaient vus que par B2, qui compare `sources_count` à la
longueur de la liste sans jamais vérifier qu'une cible existe. Un cartouche vert
attestait donc des listes **bien formées et bien comptées**, non des liens qui
**aboutissent**.

## 2. Reprise préalable des renvois vers `raw/`

Le relevé faisait d'abord apparaître des renvois `sources: ["[[raw/…]]"]`. Verdict
de Sidy : ce n'est pas une convention à entériner mais un **report oublié** —
`textes/` est né de la règle « aucun `.md` n'a sa place en `raw/` », et les liens
des fiches n'ont pas été repris dans la foulée. La forme correcte est fixée par le
protocole racine (« la ligne de coupe est le format, non le contenu : `raw/` garde
les **binaires** ») et par le précédent Gloton, qui nomme ses clichés en **chemin
nu**, jamais en wikilink : `raw/` est hors régime de liens et ignoré du graphe.

**Neuf renvois convertis** de `"[[raw/X]]"` en `"raw/X.pdf"` :
`atelier/materiel/revox-a77.md` (3), `tascam-model-12.md` (2), `neve-1073spx.md`
(2), `distressor-el8.md` (1), `doctrinal/deviations/body-types.md` (1). Extension
exacte ajoutée, **existence de chaque PDF vérifiée** avant écriture ; `raw/` non
modifié ; `updated:` porté au 2026-09-04. Seule la forme du renvoi a changé.

## 3. Le changement porté au script

`controler_liens_cartouche()`, appelée dans la boucle principale après
`controler_liens()`. Elle applique **C1 et C2 seulement** aux wikilinks portés par
`sources:`, `cross_links:` et `links:`, et **nomme le champ fautif** dans le
message.

**Portée délibérément étroite** : C3/C4 ne sont *pas* reportés au cartouche —
l'étanchéité y relève de B4 ; l'y étendre serait un **changement de règle**, non
une extension de couverture, et demanderait son propre verdict. Sont ignorés sans
bruit le marqueur `to-source` et les chemins nus vers `raw/`.

Version antérieure du script conservée : `/tmp/verifier-avant-C1-cartouche.py`.

## 4. Épreuve §VII — « vert sur X, refus sur Y »

Copie jetable `/tmp/bac-C1` ; **le dépôt vivant n'a à aucun moment porté la faute**.

| État | Résultat |
|---|---|
| base saine | 0 erreur, **7** avertissements |
| cible morte injectée dans `cross_links:` | 0 erreur, **8** — C1 nomme `cross_links:` |
| état sain restauré | 0 erreur, **7** |

Contre-épreuve déjà acquise au §1 : la même chaîne dans le **corps** levait C1
avant l'extension.

⚠️ **Nouvelle ligne de base du dépôt : 0 erreur, 7 avertissements**, et non plus
0/0. Les sept ne sont pas causés par l'extension : ils étaient là, invisibles.

## 5. Ce que le contrôle outillé trouve et que le relevé à la main manquait

Un relevé ad hoc annonçait « six liens de cartouche non résolus ». **Le compte
comme la liste étaient faux.** Le script, qui applique la règle de résolution
propre au dépôt — repli sur le **slug nu** quand le chemin complet échoue — en
relève **sept**, dont **trois jamais vus à la main** : listes YAML en blocs à
guillemets simples, identifiant arXiv employé comme wikilink, chemin à slash
final. Un premier balayage avait déjà manqué, pour la même raison de guillemets,
un neuvième renvoi `raw/`.

Inversement, deux cas comptés morts **résolvent** par le slug : `body-types` (la
page vit en `deviations/`, le lien dit `sources/`) et `2026-06-20_signature-kouyate`
(elle vit en `genealogie/`). Le dossier est faux, la cible existe, et C1 s'en
satisfait exactement comme dans le corps. **Écart de dossier signalé, non
corrigé** : point de règle, non faute de lien.

**Leçon de méthode** : deux balayages à la main ont chacun manqué des cas que le
contrôle outillé trouve, sur le même objet, à quelques minutes d'intervalle.
« Scripter le déterministe » n'est pas une préférence de style.

## 6. Les sept cibles non résolues — instruites une par une

Aucune n'est corrigée d'office : chacune demande de savoir **quelle page était
visée**, ce qui est un jugement (Cmd 12). Instruction en cours avec Sidy ;
l'issue de chaque cas sera consignée ici.

| # | Fiche | Cible non résolue | Issue (verdict Sidy, 2026-09-04) |
|---|---|---|---|
| 1 | `meta/…_guide-deploiement-verifier-invariants` | `correctif-etendu-invariants-depot` | ✅ **corrigé** — chemin complet rétabli vers `meta/2026-07-27_correctif-etendu-invariants-depot` (préfixe daté et dossier omis). Non doctrinal, tranché par la machine sur délégation. |
| 2 | `atelier/rd/outillage/out-08-ocr-arabe-futuhat/intent.md` | `atelier/rd/outillage/ocr-scan-vers-markdown` | ✅ **corrigé** → `spec-ocr-scan-vers-markdown`. Deux voisins portaient ce nom : un `.sh` (script, non liable) et la spec ; seule la spec est une page. Délégation. |
| 3 | `atelier/rd/cahiers/2026-08-29_compte-rendu-github-automation.md` | `atelier/rd/infrastructure/` | ✅ **corrigé** → `synchro-obsidian-working-copy-github`, seule fiche du domaine traitant du sujet du cahier. Le renvoi visait un **dossier** — écriture d'agent. Délégation. |
| 4 | `atelier/rd/infrastructure/2026-08-22_stealing-reasoning-traces-llm.md` | `2608.09867` | ✅ **corrigé** → `to-source`, identifiant `arXiv:2608.09867v1` conservé en commentaire et dans le corps. Verdict Sidy : « l'ingest de l'étude n'a pas été fait, il n'y a pas de fiche où pointer ». |
| 5 | `doctrinal/discernement/2026-07-01_rafi-ad-darajat-fonction-traversante.md` | `doctrinal/sources/coran-essai-traduction-gloton` | ✅ corrigé 2026-09-06 — `to-source` + dette de fiche signalée (§7) |
| 6 | `doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md` | `apercus-sur-l-initiation` | ✅ corrigé 2026-09-06 — quatrième fiche ch. XIV créée, lien repointé (§7) |
| 7 | idem | `principes-et-methodes-de-l-art-sacre` | ✅ corrigé 2026-09-06 — `to-source` + attribution rectifiée en deux endroits (§7) |

**Quatre des sept résolus. Ligne de base : 0 erreur, 3 avertissements.** Les trois
restants sont doctrinaux et relèvent tous du même fond : une `sources:` pointe vers
un **ouvrage réel, cité en propre, dont aucune fiche source n'existe**. Ce n'est pas
une faute de lien mais une **dette de fiches**, et `to-source` est le marqueur prévu.

## 7. Les trois cas doctrinaux — instruits et clos le 2026-09-06

> **État au 2026-09-06 : les trois cas sont corrigés**, sur verdicts de Sidy des
> 2026-09-05 et 2026-09-06. La ligne de base du dépôt passe de **0 erreur / 3
> avertissements** à **0 erreur / 0 avertissement** (1399 fichiers). L'instruction
> ci-dessous est conservée telle qu'elle a été écrite le 2026-09-04 (Cmd 5 : on
> rectifie avec trace, on n'efface pas) ; ce qui a été décidé est ajouté sous chaque
> cas en « Issue ».

État au 2026-09-04 : **rien n'a été écrit dans ces trois fiches.** Deux des trois
verdicts reçus entrent en contradiction avec ce que le dépôt consigne lui-même ;
l'écart est signalé et non arbitré (Cmd 12). Section tenue à jour à mesure des
verdicts.

### Cas 5 — `rafi-ad-darajat` : la sourate nommée n'est pas celle de la fiche

Verdict reçu : « la fiche doit pointer vers la Sourate Al Aʿrâf de la traduction du
Coran de Gloton que j'avais prise en photo ».

Ce que la fiche consigne (lignes 32-35) : « Confirmation scripturaire (2026-07-14,
photographie de Sidy sur son exemplaire physique — *Le Coran : Essai de traduction*,
Maurice Gloton, Albouraq) — **Qurʾân 40:15, Sourate *Gâfir*, p. 468** ». La lecture
suggérée n° 3 reprend « Sourate 40 (*Gâfir*), v. 14-16, p. 468 ». Le discernement
est **clos** sur ce verset, verdict Sidy du 2026-07-14 : « la concordance est
explicite ». Le cliché d'al-Aʿrâf appartient à une **autre** fiche et à une autre
date (lexique Gloton, 2026-08-30).

L'ouvrage est donc bien le Gloton dans les deux cas ; c'est la **sourate** qui
diverge. La cible manquante (`doctrinal/sources/coran-essai-traduction-gloton`)
n'existe pas : l'édition Gloton est citée en propre dans plusieurs fiches sans avoir
jamais reçu la sienne. **Dette de fiche, pas erreur de lien.**

**Issue (2026-09-06).** Sidy rectifie son propre verdict : « je me souviens mieux,
il s'agit d'un élément complément au dossier que j'avais fourni ». Le cliché
d'al-Aʿrâf était un complément de dossier, non la source de la citation — la
contradiction relevée ci-dessus se dissout d'elle-même, la citation de *Ghâfir*
40:15 tient, et la clôture du 2026-07-14 n'est pas rouverte. Reste la seule dette
de fiche : le lien mort est remplacé par `to-source` (`sources_count: 3` inchangé)
et un bloc de signalement précise en fin de fiche que **le marqueur porte sur
l'absence de fiche, non sur la citation** — celle-ci ayant été vérifiée par Sidy
sur exemplaire physique, condition de levée du §VII. Mention explicite de ne pas
confondre avec la fiche du lexique Gloton, qui porte sur un autre ouvrage.

### Cas 6 — `sashimono` : la matière existe, mais dans `textes/`

Verdict reçu : « renvoi à ce que Guénon dit sur l'initiation de métier dans
l'ouvrage ». Le passage est localisé :
`textes/apercu-sur-l-initiation/apercus-sur-l-initiation-index-de-l-uvre-de-rene-guenon-7.md`
(chapitre 39), qui porte huit occurrences de « métier », dont « une certaine forme
d'initiation peut être liée à l'exercice d'un métier déterminé » et le passage
Compagnonnage / Maçonnerie.

Mais **`textes/` n'est la cible d'aucun wikilink** (PRO-08) et ne lève aucun
`to-source`. Le lien ne peut donc pas viser cette page. Trois fiches
`guenon-apercus-initiation-chNN-…` existent déjà dans `doctrinal/sources/` : la voie
normale est une quatrième, sur le chapitre 39.

**Issue (2026-09-06).** Sidy pose la question de la forme : « puisque les textes de
Guénon sont dans `textes/`, est-ce qu'il ne serait pas plus propre de citer la
référence dans la fiche (chapitre, pages, etc.) et pointer directement vers le
livre en `textes/` ? » — instinct juste, et déjà le patron du dépôt : la référence
précise et le renvoi vivent dans une fiche `doctrinal/sources/`, qui est l'objet
pointable, et le renvoi vers `textes/` s'y fait en **chemin nu entre accents
graves**, jamais en wikilink. Aucune tension avec PRO-08 : la fiche est
l'intermédiaire qui la résout.

Créée : `doctrinal/sources/guenon-apercus-initiation-ch14-qualifications-initiatiques.md`.
Le `sources:` de la fiche sashimono pointe désormais vers elle, `sources_count: 2`
tient, C1 tombe.

**Le numéro de chapitre a été établi, non supposé** : le `Chapitre=39` de l'URL est
la pagination interne du site source, pas le chapitre du livre. Le décalage
constant de 25 est recoupé sur la fiche ch. VII existante, dont la transcription
porte `Chapitre=32` — d'où **ch. XIV**, confirmé par le corps du texte
(« Des qualifications initiatiques »). La **pagination**, elle, reste `to-source` :
la transcription ne porte pas de numéros de page. Le `to-source` de chapitre de la
fiche sashimono (ligne 33) est levé ; le renvoi de Guénon à
*Le Règne de la Quantité*, ch. VIII (note [5]) est signalé comme piste d'ingest, pas
comme lien mort.

### Cas 7 — `principes-et-methodes-de-l-art-sacre` : une attribution fautive dans le dépôt

Verdict reçu : « *Principes et méthodes de l'art sacré* est un livre de Burckhardt
dont je ne dispose pas mais qui a certainement été cité par Coomaraswamy dans *La
Porte du ciel* ».

Sur l'auteur, le verdict est **exact, et le dépôt a tort en deux endroits** :
- `atelier/rd/bibliotheque/catalogue-bibliotheque.md:61` range le titre sous
  **Coomaraswamy** et le porte comme **détenu** en bibliothèque physique ;
- le corps de la fiche sashimono (ligne 37) répète « Coomaraswamy, *Principes et
  méthodes de l'art sacré* ».

Le catalogue est vraisemblablement la **source** de l'erreur, la fiche l'ayant
recopié. Burckhardt figure bien au catalogue (lignes 99, 100, 162) mais avec trois
**autres** titres.

Sur la citation supposée, une réserve de datation : Coomaraswamy meurt en 1947,
l'ouvrage de Burckhardt paraît en 1958 — une citation **par lui** est impossible.
Un apparat éditorial moderne dans une anthologie pourrait en porter une ; ce n'est
pas la même chose et cela demanderait vérification sur pièce.

**Issue (2026-09-06).** Verdict de Sidy : « corrige comme tu peux ou bien on verra
ça plus tard ». Corrigé aux deux endroits, **avec trace et non par effacement**
(Cmd 5) : au catalogue, le titre sort de la liste Coomaraswamy avec une ligne de
rectification datée, et une entrée Burckhardt est ajoutée au §IV marquée
**❌ non détenu** ; dans le corps de la fiche sashimono, un bloc de rectification
précède la ligne fautive, désormais réduite à « Coomaraswamy (ouvrage exact
`to-source`) ». Le lien mort devient `to-source`. La piste de Sidy (cité par
Coomaraswamy dans *La Porte du ciel*) est **consignée comme hypothèse non
vérifiée**, avec la réserve de datation portée dans la fiche elle-même : « on verra
ça plus tard » vaut consignation, pas résolution.

`Burckhardt` est par
ailleurs **absent** de `bibliographie-porte-du-ciel.md` et de
`notices-porte-du-ciel.md`.

Trois choses distinctes attendent donc ici un verdict : le lien mort, l'attribution
fautive au catalogue, et l'attribution fautive dans le corps de la fiche.
