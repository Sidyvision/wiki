---
title: "État des lieux du chantier d'indexation, et document de reprise (2026-09-09)"
type: experience
statut_experience: reproduit
tags: [rd, cahier, reprise, indexation, annotation, langues-originales, etat-des-lieux, verdicts-attendus]
created: 2026-09-09
updated: 2026-09-09
sources: []
links: ["[[atelier/rd/cahiers/2026-09-09_rapport-session-indexation-html-annotations]]", "[[atelier/rd/outillage/2026-09-08_serveur-mcp-wiki]]", "[[atelier/rd/cahiers/registre-problemes]]"]
original: []
---

# État des lieux du chantier d'indexation — et comment le reprendre

> **Ce document sert à REPRENDRE, pas à raconter.** Le récit de la première moitié du
> chantier vit dans [[atelier/rd/cahiers/2026-09-09_rapport-session-indexation-html-annotations]] ;
> celui-ci décrit **l'état au 2026-09-09 au soir**, ce qui **attend un verdict**, ce qui
> a été **essayé et écarté** — pour qu'on ne le retente pas —, et **les commandes** pour
> tout régénérer et tout vérifier.

## 1. Où en est le chantier, en une table

| | |
|---|---|
| Commits de la session | `274ddc6..5f18f60` (50) |
| Termes indexés | **10 695** — 420 103 occurrences, 758 fiches, 657 textes |
| Fiches annotées | **321**, **935 annotations** |
| Appariements rang 1 (`apparie`, attesté par la fiche) | **59 paires**, 118 clés |
| Appariements rang 2 (`jurjani`, n° de définition) | **132**, dont 84 réciproques |
| Traditions sourcées (`tradition`) | **310**, dont 42 `ratifie-sidy`, le reste `fiche-propre` / `definition` |
| Langues sourcées (`langue`) | **52** — 48 `forme-appariee`, 4 `prose`, **0 `sceau-original`** |
| Refus mécaniques | **20** dans `verifier-invariants.py`, **15** dans `valider-annotations.py` |
| Outils MCP | **16** (14 + `chercher_terme` + `etat_index_lexical`) |

État sain à la clôture : `verifier-invariants` **0 erreur / 0 avertissement** ;
`valider-annotations` **0 anomalie**, 4 signalements S1 (tous légitimes, § 4).

## 2. Les pièces, et ce que chacune détient

**Trois définitions canoniques, détenues en un seul point et importées.** Le sens de la
dépendance est délibéré : l'outil de R&D dépend du contrôleur racine, jamais l'inverse.

| définition | détenteur | importée par |
|---|---|---|
| `fichiers_suivis()` — la matière du dépôt | générateur d'index | validateur |
| `est_ecriture_originale()` | **`verifier-invariants.py`** | générateur |
| `circuit_de()` | **`verifier-invariants.py`** | validateur |

L'absence du détenteur provoque un **refus franc et nommé**, jamais un repli sur une
copie locale.

**Une seule divergence assumée** : le serveur MCP vit **hors du dépôt**
(`/root/mcp-servers/wiki/`) et doit tourner si le pôle `rd/` est absent — il
réimplémente donc `normaliser()` au lieu de l'importer. La divergence est **déclarée en
commentaire** et rattrapée par la remontée des clés proches quand une recherche échoue.

**Les champs de l'entrée d'index**, et ce qui les source :

| champ | ce qu'il porte | source |
|---|---|---|
| `apparie` | rang 1 — la paire que **la fiche énonce** | `Tomoe (巴)` au `title:`/H1, ou en tête de définition |
| `jurjani` | rang 2 — autorité textuelle | *Kitāb al-Taʿrīfāt*, **numéro de définition** |
| `tradition` | le **cadre** | fiche dont le slug **est** le terme · fiche qui le **définit** · **verdict Sidy** |
| `langue` | la langue **du terme** | `original:` du Sceau · prose · écriture de la forme appariée |

**Les deux rangs et les deux axes ne se fondent jamais**, ni dans l'artefact, ni dans le
condensé, ni chez le consommateur MCP. Chaque valeur porte sa provenance : *un verdict et
une mesure n'ont pas la même force, et le lecteur doit le voir sans ouvrir le JSON.*

## 3. Le fil qui tient tout, et qui est actuellement à zéro

**Le champ `original:` (§IV) est le goulot du chantier, et il est vide.**

Il porte trois choses à lui seul :
1. la **forme d'origine** de la fiche (§VII, discipline des langues originales) ;
2. la **langue** du terme, par son écriture — provenance `sceau-original`, la plus forte
   des trois, et **la seule qui grandira** ;
3. les **appariements de syntagmes**, que l'index — dont les clés sont des tokens — ne
   peut structurellement pas porter (§VII, clarification du 2026-09-09).

**Mesuré au 2026-09-09 : aucun `original:` n'est peuplé dans le dépôt.** Tant qu'il le
reste, l'axe langue plafonne à 52 termes et les syntagmes n'ont pas de porteur. **Aucun
outillage n'y changera rien** — c'est la discipline qui avance, et le **point 5** interdit
d'y procéder en passe de masse : les fiches se complètent au fil des sessions qui les
touchent.

**C'est le point de reprise le plus rentable du chantier**, et il ne demande aucun code.

## 4. Ce qui attend un verdict de Sidy

| # | objet | état |
|---|---|---|
| 1 | **85 termes annotés sans tradition sourçable** | relevé prêt : `atelier/rd/outillage/index-lexical/2026-09-09_termes-sans-tradition-sourcee.md`. 42 des 127 ont été **ratifiés** le 2026-09-09 ; les 85 restants sont dispersés et demandent une décision terme par terme |
| 2 | **9 ratifications sous réserve** | `bhutas`, `matras`, `sat-chit-ananda`, `avarna`, `ativarna`, `swastika`, `mahatma`, `upaguru` portent `universel` alors que leur écriture est **sanskrite** ; `hokhmah` alors qu'elle est **hébraïque**. Listées dans `traditions-ratifiees.json`. **L'axe langue les tranchera de lui-même** dès que leur `original:` sera posé |
| 3 | **4 signalements S1** | `yuga`/`satya-yuga`, `yuga`/`kali-yuga` (×2 fiches), `janus`/`janus-bifrons` — tous jugés **légitimes** (genre/espèce, et aspect d'une entité). Maintenus après examen le 2026-09-09 |
| 4 | **`doctrinal/doctrines/`** | cité à l'arbre du §II, **absent du disque**. Écart antérieur à cette session |
| 5 | **Le sas comme angle mort mécanique** | `_inbox/` est dans `DOSSIERS_EXCLUS` : un lot n'y est contrôlé **qu'au moment où on décide de l'intégrer**. Le lot *Futūḥāt* y a séjourné deux jours avec 2112 caractères interdits par le Cmd 15. Étendre le contrôle au sas demande un verdict |
| 6 | **Qualité de l'OCR des *Futūḥāt*** | 8078 mots agglutinés sur 386 933 (2,1 %), 1399 glyphes parasites. Versé comme **repère de localisation**, jamais graphie citable. Trois voies ouvertes, aucune retenue : garder, attendre une meilleure conversion (§II le prévoit, datée), ou ne garder que l'exploitable |
| 7 | **Poids du condensé** | ramené de 1,2 Mo d'un seul tenant à **28 fichiers de 207 Ko au plus** (`condense/`). Si c'est encore trop pour Obsidian sur iPad, la coupe suivante serait la restriction aux termes multi-fiches |
| 8 | **`_inbox/` restant** | `2026-09-07_djinns-aident-humains-koly-cherif-keita.md` (fiche `type: source`, `status: transcripcion-en-cours` — coquille dans la valeur) et `audio/`. Lots antérieurs, non traités |

## 5. Registre des voies essayées et ÉCARTÉES — à ne pas retenter

C'est la section la plus utile à une reprise : chacune paraissait bonne, et **la mesure
l'a écartée**. Le motif est le même à chaque fois — *on élargit un signal pour couvrir
davantage, et l'on se met à couvrir autre chose.*

| voie essayée | pourquoi elle paraissait bonne | ce que la mesure a donné |
|---|---|---|
| **Consensus des `tradition_cadre`** des fiches qui citent un terme | la majorité a raison sur `barzakh` | **110 divergences sur 160**. `tradition_cadre` décrit le cadre de **la fiche**, jamais l'origine du terme. Un vote n'est pas une source, et une méthode qui a raison par majorité a **tort par construction** |
| **Rôle `titre`** comme signal de « fiche traitant le terme » | le titre nomme le sujet | se pose dès que le terme est **composant du slug** : les **60 fiches `guenon-*.md`** « traitaient » de Guénon. 808 traditions dont la moitié fausses, contre 310 après resserrement sur `slug == terme` |
| **Barre oblique** dans l'appariement (`X / ORIGINAL`) | forme attestée dans le dépôt | **aucune paire vraie, une fausse** (`systeme` ↔ `α`) |
| **H2 comme source d'appariement** | les intertitres portent des paires | a produit `systeme` ↔ `α` depuis « … — système (α) ». Retiré : seuls `title:` et H1 |
| **Côté latin de la regex élargi au syntagme** | apparier `chikai to seiyaku` | 5 paires distinctes, **3 de déchet** — la regex avale l'article et la conjonction (`et Muraqaba`, `Le Shintō`) |
| **Ancrage de l'appariement sur le slug** | le slug est le sujet de la fiche | 5 candidats, **2 valables** ; `merkavah-muraqaba` traite **deux** termes et ne s'apparie pas en bloc |
| **`RE_CODE` tolérant au retour à la ligne** | masquer un incise coupé en deux | rendu glouton par les backticks orphelins, il avalerait **186 819 caractères** de `doctrinal/annales.md`. *Le remède est pire que le mal* |
| **Déduire la langue de la graphie** (`al-`, `ḥ`, `ṣ`) | couvrirait bien plus que 52 termes | **heuristique d'orthographe** — pas une source (Cmd 5). Écartée par principe, mesure non faite |
| **Han comme écriture donnant la langue** | `巴` est une écriture d'origine | le han sert le chinois **et** le japonais : `巴` s'y déclarait « chinois » alors que *tomoe* est japonais. *Une écriture partagée ne source pas une langue* |
| **Créer 127 fiches doctrinales** | rendrait les termes typables partout | exigerait **127 `tradition_cadre` que rien ne source** — zéro appariement Jurjānī, zéro écriture originale attestée parmi elles |

**Deux gains réels valent d'être notés à côté** : le gisement de syntagmes non appariés
est **nul** (les deux paires légitimes du dépôt le sont déjà par le nom de famille), et
la réciprocité des 132 appariements Jurjānī a été fermée **chez le consommateur**
(`chercher_terme`) plutôt que dans l'artefact — sans qu'une clé de dictionnaire entre
dans un index qui est celui du **wiki**.

## 6. Trois pièges structurels, qui se redéclencheront

Ce ne sont pas des accidents : ce sont des propriétés d'un dépôt qui **documente son
propre outillage**. Tout scan qui lit le dépôt pour en tirer un fait doit exclure ce que
le dépôt dit **de lui-même**.

1. **Le marqueur d'insertion cité en prose** dans un fichier append-only — l'assertion
   d'unicité échoue, la cible doit être « première occurrence, vérifiée antérieure à la
   première entrée ».
2. **La convention d'annotation citée en prose** — `` `<dfn data-terme…>` `` dans une
   entrée d'annales était lu comme une pose. Corrigé en masquant le code **avant** la
   recherche des balises.
3. **La langue citée en exemple dans un document de gouvernance** — `buddhi` citait
   `atelier/annales.md` et le changelog parmi ses sources de langue. Les fichiers de
   service et `meta/protocole-archives/` sont désormais exclus de la lecture.

**Corollaire, appris deux fois** : une correction peut **créer** un contrôle mort. Après
avoir masqué le code en amont, la branche D4 « dans du code » est devenue inatteignable —
retirée, car un contrôle qui ne peut pas se déclencher est la forme muette même que le
§VII interdit, et le laisser en place donne **l'apparence** d'une garde.

## 7. Les commandes, pour reprendre sans rien chercher

```bash
cd /root/wiki

# 1. Régénérer l'index — JSON (hors dépôt), condensé éclaté (versionné)
python3 atelier/rd/outillage/index-lexical/generer-index-lexical.py \
  --racine /root/wiki \
  --sortie-json atelier/rd/outillage/index-lexical/index-lexical.json \
  --sortie-md /tmp/index-lexical.md \
  --sortie-md-eclate atelier/rd/outillage/index-lexical/condense

# 2. Valider les annotations — refus D1..D6, signalements S1
python3 atelier/rd/outillage/index-lexical/valider-annotations.py --racine /root/wiki

# 3. Contrôle structurel obligatoire (§VII, clôture de session)
python3 verifier-invariants.py --racine /root/wiki

# 4. Graphe — obligatoire si des fiches doctrinal/ ont bougé
python3 atelier/rd/outillage/graphe/generer-cartographie.py

# 5. Le témoin du régime apparié : les ARÊTES doivent être identiques
#    (les nœuds diffèrent des seuls `updated:` remontés)
```

**Le témoin du régime apparié se refait à chaque passe d'annotation** : régénérer le
graphe et comparer les **arêtes triées** avant/après. Elles ont été identiques **huit
fois** sur 935 annotations — c'est ce qui fait du régime un fait remesuré et non une
discipline affirmée. **Comparer le contenu trié, jamais le compte**, qui peut coïncider
par hasard.

Le serveur MCP vit hors dépôt et a son propre venv :

```bash
/root/mcp-servers/wiki/.venv/bin/python -c "..."   # chercher_terme, etat_index_lexical
```

`etat_index_lexical` déclare la **fraîcheur** de l'index à chaque appel : *un index périmé
ne se plaint jamais de lui-même — il répond, et il répond faux.*

## 8. Un audit externe attend, non traité

`atelier/rd/outillage/2026-09-09_audit-index-lexical-modularisation.md` — **audit
commandé par Sidy** et conduit par Qoder, déposé le 2026-09-09 à 06:42, 450 lignes. Il
relit ligne à ligne le générateur et le validateur décrits ici, et les exécute en live.
Encore **non suivi par git** au moment où ces lignes sont écrites.

**Ses conclusions ne sont pas reprises ici, et c'est délibéré** : les vérifier demande une
passe propre, et les résumer sans les avoir vérifiées reviendrait à leur prêter une
autorité qu'elles n'ont pas encore acquise — la même retenue que pour toute source
(Cmd 12). Ce n'est pas une réserve sur l'auditeur : c'est la règle qui vaut pour tout ce
qui n'a pas été mesuré par la session qui l'écrit.

**Une reprise doit l'ouvrir en premier.** C'est le seul regard porté sur cet outillage
depuis l'extérieur de la session qui l'a bâti — donc le seul qui puisse voir ce qu'elle
n'a pas su voir. Ses mesures d'en-tête concordent avec celles du § 1, ce qui est déjà un
recoupement indépendant.

**Deux avertissements C1 qu'il lève**, et qui ne sont pas des fautes de sa part : ses
`links:` pointent `[[…/generer-index-lexical]]` et `[[…/valider-annotations]]`, qui sont
des fichiers **`.py`**. Le contrôle C1 ne résout que des cibles `.md` — **le régime de
liens du dépôt n'a pas de forme pour citer un script**. C'est un écart de protocole
révélé par cet audit, rapporté et non corrigé.

## 9. Ce qu'une reprise devrait faire, dans l'ordre

1. **Poser `original:`** sur les fiches que la session touche — au fil, jamais en masse
   (§VII point 5). C'est le seul geste qui débloque **trois** choses à la fois (§ 3), et
   il ne demande aucun code.
2. **Instruire les 9 ratifications sous réserve** (§ 4, n° 2) — ou les laisser à l'axe
   langue, qui les tranchera de lui-même une fois leur `original:` posé.
3. **Trancher le sas** (§ 4, n° 5) : le lot *Futūḥāt* a montré qu'un lot peut y séjourner
   des jours avec des caractères interdits par le Cmd 15 sans qu'aucun contrôle le voie.
4. **Traiter l'audit Qoder** (§ 8) — le vérifier, puis l'intégrer ou le réfuter.
5. **Le reste** attend un verdict et n'est pas bloquant.

**Ce qu'une reprise ne devrait PAS faire** : rouvrir une des dix voies du § 5 sans
mesure nouvelle. Chacune a été essayée, chacune paraissait bonne, et c'est la mesure —
non le principe — qui les a écartées.
