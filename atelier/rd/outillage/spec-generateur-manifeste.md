---
title: "Spécification — Générateur de manifeste (wiki → wiki-manifest.json)"
type: projet
tags: [instrument, manifeste, generateur, phase-1, spec]
created: 2026-07-01
updated: 2026-08-20
sources: []
links: ["[[atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.2]]", "[[doctrinal/symboles/hadarat-khams]]", "[[doctrinal/symboles/table-28-degres-nafas-rahman]]"]
---

# Spécification — Générateur de manifeste

> **Migration du 2026-08-08** : cette fiche a été déplacée de
> `atelier/projets/spec-generateur-manifeste.md` vers `atelier/rd/outillage/spec-generateur-manifeste.md` (ouverture du pôle R&D,
> verdict Sidy 2026-08-08 — proposition §IV). L'ancienne fiche subsiste
> comme stub `deprecated` avec pointeur (Cmd 10). Contenu inchangé,
> dates `created`/`updated` conservées.


> **Phase 1 de la feuille de route de l'Instrument.** Ce document spécifie le script
> déterministe `generer-manifeste.py` qui produit `wiki-manifest.json` (schéma v0.2.1,
> figé dans la fiche architecture v0.2 §6) à partir de `doctrinal/` et d'un fichier
> déclaratif côté app, `instrument-donnees.yaml`. **Aucun LLM dans la boucle de
> génération** : parse mécanique uniquement, conformément au principe de la Phase 1.

---

## 1. Décisions d'architecture actées (session du 2026-07-01)

- **Moteur 3D** : Three.js / WebGL (question §8.3 de la fiche v0.2 — tranchée).
- **Cible** : web mobile d'abord (Safari iPad, installable en icône d'accueil).
- **Hébergement** : statique — le manifeste est un fichier JSON livré avec l'app.
- **Génération du manifeste** : script déterministe pur ; le LLM ne peut que *proposer*
  des ancrages `suggere` que Sidy inscrit lui-même dans `instrument-donnees.yaml`.

## 2. Pourquoi un fichier déclaratif côté app (et non le Sceau Recteur)

Le schéma v0.2.1 requiert des données que le frontmatter doctrinal ne porte pas :
`degre_vertical`, appartenance d'une fiche à un arbre de tradition, nature et état des
ancrages. Les inscrire dans les fiches doctrinales violerait l'étanchéité (« aucune page
doctrinale ne mentionne l'app », garde-fou §4 de `02-instrument-feuille-de-route.md`).
Ces données vivent donc dans **`atelier/rd/instrument/instrument-donnees.yaml`**, tenu à la
main par Sidy, avec liens à sens unique vers `doctrinal/` (règle d'étanchéité
projets → doctrinal respectée par construction).

Le générateur croise les deux couches : la **vérité doctrinale** (les fiches, leurs
titres, leurs statuts, les discernements en cours) et la **déclaration applicative**
(quels nœuds, quels degrés, quels ancrages).

## 3. Entrées / sorties

| | Chemin (défaut) | Rôle |
|---|---|---|
| Entrée 1 | `/root/wiki/doctrinal/` | fiches réelles : labels, existence, discernements |
| Entrée 2 | `/root/wiki/atelier/rd/instrument/instrument-donnees.yaml` | nœuds, degrés, ancrages |
| Sortie | `/root/wiki/atelier/rd/instrument/wiki-manifest.json` | manifeste v0.2.1 |

Le script accepte `--repo`, `--donnees`, `--sortie` pour surcharger ces chemins
(indispensable pour tester dans un bac à sable de type `regression-test`).

## 4. Règles de génération (déterministes)

1. **Nœuds** : uniquement ceux déclarés dans `instrument-donnees.yaml` (inclusion
   explicite — cohérent avec le « peuplé fiche par fiche en Phase 2 » du schéma).
   Pour chaque nœud : la fiche doctrinale doit exister ; `label` = champ `title` du
   frontmatter de la fiche (jamais retapé à la main) ; `id` = `<tradition>/<slug>`.
2. **`degre_vertical`** : recopié depuis la déclaration ; `null` si absent.
3. **`question_ouverte`** : calculée automatiquement. Le script parcourt
   `doctrinal/discernement/`, lit le frontmatter (`cross_links`) et le bloc 🔍
   normalisé ; si une fiche de discernement au **Statut : en cours** pointe vers la
   fiche du nœud, `question_ouverte` reçoit le wikilink de ce discernement. Sinon `false`.
4. **Ancrages** : recopiés depuis la déclaration, stockés **à sens unique** sur le nœud
   source (l'app reconstruit l'inverse), après validation (voir §5).
5. **Métadonnées** : `generated_at` (ISO 8601 UTC), `source_commit` (SHA git du dépôt,
   ou `"inconnu"` hors dépôt git).

## 5. Validations bloquantes (VIGILANCE mécanique)

Le script refuse de produire un manifeste (code retour ≠ 0) si :

- un nœud déclaré pointe vers une fiche inexistante ;
- deux nœuds portent le même `id` ;
- un ancrage a un `type` hors {equivalence, complementarite, subversion, parodie},
  un `etat` hors {etabli, suggere, identifie}, ou une `directionnalite` hors
  {none, ascendant, descendant} ;
- un ancrage `etabli` n'a pas de `source` (une correspondance établie est sourcée
  dans le wiki, sans exception) ;
- la `cible` d'un ancrage ne correspond à aucun nœud déclaré (sauf `null`) ;
- un ancrage `subversion` ou `parodie` porte une `cible` non nulle **sans** que sa
  `source` soit une fiche `doctrinal/discernement/` (correctif *waswâs*/Qliphoth,
  fiche v0.2 §2 et §6 — jamais de pont inter-traditions structurel par défaut).

Avertissements non bloquants : `directionnalite` renseignée sur un ancrage non
`complementarite` ; fiche source d'ancrage introuvable dans le dépôt.

## 5 bis. Bloc `zodiaque:` (schéma v0.2.2, ajouté 2026-08-20)

Le bloc `zodiaque:` d'`instrument-donnees.yaml` (degrés du *falak al-burūj*/
*al-manāzil*, obliquité, `epoque_reference`, 12 `signes`) est propagé tel
quel dans le manifeste, sous la clé `zodiaque`, absente si le bloc l'est côté
données. Validations dédiées (fonction `valider_zodiaque`) :

- **Bloquantes** (malformation structurelle) : `zodiaque` non-mapping ;
  `degre_falak_al_buruj`/`degre_falak_al_manazil` non entiers (si présents) ;
  `obliquite_deg` non numérique (si présent) ; `signes` non-liste (si
  présent) ; une entrée de `signes` sans `label` non vide.
- **Non bloquantes** (dérive possible, pas une malformation) : un degré
  `falak_al_*` déclaré qui ne correspond à aucun `degre_vertical` de nœud
  déclaré ; `signes` ne comptant pas exactement 12 entrées.

Motif de l'ouverture : le bloc existait en donnée depuis le 2026-07-26/27
(`spec-anneau-zodiacal.md`) mais n'était jamais émis — le prototype le
transcrivait à la main sans passer par le manifeste, en contradiction avec
la règle commune des manifestes (CLAUDE.md racine §VII : flux à sens unique
dépôt → manifeste → interface). Fermé sur demande explicite de Sidy,
2026-08-20 — voir
[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]].

## 5 ter. Lecture dynamique par le prototype (2026-08-20, verdict Sidy)

Depuis le 2026-08-20, `instrument-prototype.html` **lit réellement**
`wiki-manifest.json` à l'ouverture (`fetch` sur chemin relatif, avant le
chargement de Three.js) et en dérive l'intégralité de ses données
doctrinales : nœuds-degrés, nœuds notionnels de l'anneau, ancrages rendus,
Aqtâb, Homme Universel, filament, Barzakh, bloc zodiacal. Plus aucune donnée
doctrinale n'a besoin d'être retapée dans le prototype à chaque
régénération — le flux `dépôt → manifeste → interface` est effectif de bout
en bout, et non plus seulement déclaratif.

Trois garde-fous, dans l'esprit de l'Art. 5 sashimono (l'assemblage reste
démontable) :

1. **Repli intégral** — un instantané des mêmes données subsiste en
   littéraux JS. Si le manifeste est inaccessible (ouverture en `file://`
   hors serveur, fichier absent, `fetch` indisponible), la scène s'affiche
   quand même, à l'identique. Aucune régression d'usage sur iPad.
2. **Provenance affichée** — le panneau de titre indique en clair la source
   effective : version de schéma, SHA court du dépôt et nombre de nœuds
   quand le manifeste est lu ; mention explicite « données de repli » sinon.
   L'utilisateur sait toujours s'il regarde l'état du dépôt ou l'instantané.
3. **Délai de garde** — une lecture qui n'aboutit pas (4 s) bascule
   automatiquement sur le repli ; le rendu n'est jamais bloqué par le
   réseau.

Sens de lecture inchangé (Cmd 12, règle des manifestes) : l'interface **lit
et ne réécrit jamais** le manifeste ni le dépôt.

**Limite assumée** : les regroupements de présentation (bandes des
Présences — Lāhūt, Jabarūt, Barzakh supérieur, Malakūt planétaire, Nāsūt) et
toute la géométrie restent en dur dans le prototype. Ce sont des choix de
rendu, non de la donnée doctrinale, et le schéma du manifeste ne les porte
pas. Les étiquettes 3D abrègent mécaniquement les titres doctrinaux longs
(fonction `abreger`, coupe au premier séparateur naturel) ; l'info-bulle
affiche toujours le libellé intégral du manifeste, jamais une reformulation.

## 5 quater. Bloc `registres:` (schéma v0.2.3, ajouté 2026-08-20)

Un **registre** est la partition de l'unique axe vertical propre à une
tradition (données `instrument-donnees.yaml` v0.4.0). Les registres coexistent
sur le même axe **sans être alignés entre eux** — même discipline que les 12
signes et les 28 manāzil de l'anneau zodiacal (Art. 3 sashimono).

Deux formes de domaine, **exclusives** :
- `degres: [debut, fin]` — la tradition situe le domaine sur l'échelle des 38
  degrés (cas des Ḥaḍarāt akbariennes) ;
- `rang: n` (+ `colonne:`) — la tradition donne un ordre le long de l'axe sans
  échelle de degrés (cas des Sephiroth).

**Validations bloquantes** : `registres` non-liste ; `id` de registre ou de
domaine manquant ou dupliqué ; `label` manquant ; `axe` hors
{`principal`, `parallele`} ; `fiche` manquante ou introuvable au dépôt ;
`domaines` vide ; domaine sans `degres` ni `rang` ; `degres` mal formé ou aux
bornes inversées ; `rang` non entier ≥ 1 ; **et surtout** un domaine portant à
la fois `degres` et `rang`.

Ce dernier refus est le cœur du dispositif : porter les deux reviendrait à
déclarer en donnée une **correspondance point à point** qu'aucune tradition ne
donne — précisément ce que le Cmd 3 réserve à une fiche `discernement`
tranchée. La règle cesse d'être seulement écrite dans le protocole : elle est
**appliquée mécaniquement par l'outil**.

**Avertissement non bloquant** : un registre mêlant les deux formes de domaine
(légitime en principe, assez inhabituel pour mériter un signalement).

Corollaire de méthode : **déclarer un registre ne pose aucun joint** — c'est
documenter une tradition dans son expression propre. Les ancrages
inter-registres restent hors de ce bloc et sous verdict (Cmd 3, Cmd 12).

## 6. Ce que le script ne fait pas

- Il ne parse jamais le corps des fiches, à une exception près : le bloc 🔍 normalisé
  des discernements (ligne `**Statut** : …`), qui est un format contrôlé par le protocole.
- Il ne propose, n'infère ni ne crée aucun ancrage.
- Il n'écrit rien dans `doctrinal/` (lecture seule stricte sur ce circuit).

## 7. Premier contenu (v0.1 des données)

`instrument-donnees.yaml` est livré avec : les nœuds Tasawwuf déjà mûrs dans le wiki
(barzakh, walaya, al-insān al-kāmil, waḥdat al-wujūd, hadarat-khams, table des 28-38
degrés, manāzil al-qamar, nafas raḥmānī), tous à `degre_vertical: null` (Phase 2 les
peuplera fiche par fiche), et **un premier ancrage établi : la convergence des 28**
(*Futūḥāt* ch. 198, validée par le Gem le 2026-07-01), reliant la table des 28 degrés
aux demeures lunaires — le pont Phase 2 ↔ Phase 5 inscrit dans la donnée.

**Nota** — Al-Insān al-Kāmil est déclaré comme nœud ordinaire à ce stade ; son
traitement de nœud *traversant* les cinq Présences (fiche v0.2 §3.4) relève du rendu
3D, pas du manifeste, et reste au point ouvert §8 de la fiche architecture.

## 8. Exécution côté serveur

```bash
python3 atelier/rd/outillage/generer-manifeste.py --repo /root/wiki
```

Dépendance unique : PyYAML (`apt install python3-yaml` sur le Hetzner — lecture du
frontmatter et du fichier déclaratif). Le script est exécutable par Claude Code
aujourd'hui, par Qwen demain, ou à la main : il est le même dans les trois cas, c'est
tout l'intérêt du déterminisme.

---

*Statut : spécification livrée avec le script et les données v0.1 (2026-07-01).
Classée en `atelier/projets/` ; liens à sens unique vers `doctrinal/`.*
