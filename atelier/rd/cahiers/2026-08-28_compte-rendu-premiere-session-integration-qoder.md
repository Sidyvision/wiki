---
title: Compte-rendu R&D 2026-08-28 — première session d'un nouveau moteur en poste
  INTÉGRATION (Qoder)
type: meta
statut: synthese
tags:
- atelier
- rd
- integration
- moteur
- verification
- annales
- multi-agents
created: 2026-08-28
updated: 2026-08-28
sources: []
links:
- '[[atelier/rd/cahiers/registre-problemes]]'
---

# Compte-rendu R&D 2026-08-28 — première session d'un nouveau moteur en poste INTÉGRATION (Qoder)

> **Objet** : retour d'expérience de la première session effective du moteur
> Qoder dans la fonction INTÉGRATION (Cmd 14 — agnosticisme du moteur).
> Mission initiale : revue du protocole à froid à la demande de Sidy, puis
> exécution des corrections validées. Le présent compte-rendu n'en reprend
> **pas** le détail opérationnel (consigné dans `meta/meta-annales.md`,
> entrées du 2026-08-28) — il isole ce qui intéresse le pôle R&D :
> l'incident append-only découvert, les données de calibrage du vérificateur,
> l'hygiène des manifestes, et le comportement multi-rédacteurs.

---

## I. Incident découvert — en-tête d'entrée d'annales remplacé à l'insertion

La revue à froid du dépôt a mis au jour une corruption silencieuse de
`meta/meta-annales.md` : l'entrée du 2026-08-25 (« Signalement lot
bibliothèque Tilak vers Hermes ») avait perdu son en-tête greppable
`## [YYYY-MM-DD] op | Titre` — le corps (puces, `- **Commit** : a56b603`)
demeurait, visuellement fusionné au bloc de l'entrée suivante.

- **Fait brut** : introduit par le commit `d09cc88` (2026-08-27,
  journalisation post-commit du lot Choura) ; l'insertion de la nouvelle
  entrée à la suite du marqueur `<!-- INSERTION: EN-TÊTE -->` s'est faite par
  **remplacement** de la ligne d'en-tête de la première entrée existante,
  et non par insertion avant elle. Diff git explicite : la ligne
  `## [2026-08-25] projet-unifie | …` est comptée `-` et n'a jamais été
  réintroduite.
- **Restauration** : en-tête rétabli verbatim depuis `git show a5de5c7`
  (commit d'origine de l'entrée), commit `88d3253`.
- **Point critique pour le pôle** : **`verifier-invariants.py` ne détecte pas
  cette classe de corruption.** Les contrôles A existants (A2 chronologie,
  A4 doublon exact, A5 double ligne vide) passent tous sur le fichier corrompu
  — la chronologie restait décroissante, aucun doublon, la puce orpheline
  n'est rattachée à aucun en-tête pour le script. L'anomalie n'a été vue que
  par lecture humaine/moteur du fichier.
- Consigné au registre : [[atelier/rd/cahiers/registre-problemes]], entrée
  `[2026-08-28]` (ci-dessous dans le présent document, même date).

**Contrôle proposé** (à instruire séparément, Cmd 6 — aucune écriture
effectuée) : un contrôle de type A6 « corps d'entrée orphelin » — toute puce
de niveau entrée (`- **` en colonne 0) apparaissant **après une ligne vide**
et appartenant à un bloc sans en-tête `## [date]` propre, signalée. Un
heuristique plus simple suffirait à attraper ce cas précis : deux blocs de
puces distincts (séparés par une ligne vide) sous un même en-tête, dont le
second contient `- **Commit** :`.

## II. Données de calibrage du vérificateur — état de référence

Exécution `verifier-invariants.py --racine /root/wiki` en début et fin de
session : **0 erreur, 17 avertissements** — stable, aucun avertissement
introduit par les écritures de la session. Répartition des 17 :

| Classe | Nombre | Nature |
|---|---|---|
| C1 — artefacts de syntaxe | 13 | séquences d'exemple en double crochets (contenus `^`, `x`, `x/y`, `{brut}`, `meta/...`) dans des documents qui **expliquent** la syntaxe wikilink (annales des deux circuits, specs outillage, rapport conjoint, méthode de croisement) |
| C1 — liens réellement cassés | 3 | contenus `wikilinks` (citadelle-du-sham/note.md), `doctrinal/discernement` ×2 (rapport-conjoint, rene-guenon.md) — à trier : cible prévue jamais créée, ou chemin incomplet |
| C4 — étanchéité | 1 | `doctrinal/annales.md` → `meta/projet-unifie/proposition-pole-usul-2026-08-27` — signal réel (sens interdit §VI), signalé par le script lui-même comme hors périmètre bloquant |

**Donnée live ajoutée par le présent document** : en citant verbatim les
exemples ci-dessus dans la première rédaction de ce tableau, le fichier a
lui-même produit **7 C1** à la première passe du vérificateur (17 → 24
avertissements) — puis un huitième en citant les exemples en double
crochets ouvrants/fermants séparés (17 → 18 après paraphrase partielle).
Les exemples sont donc cités ici sans les crochets. C'est une confirmation
directe du mécanisme : le `RE_WIKILINK` ne distingue pas un exemple cité
d'un lien posé, et tout rapport qui doit citer des séquences fautives
**verbatim** relève du mécanisme prévu pour cela (`FICHIERS_EXEMPTS_C1`,
« rapports de traitement qui documentent volontairement des exemples de
liens problématiques » — deux fichiers déjà inscrits).

**Lecture pour le calibrage** : les faux positifs C1 proviennent presque tous
de *l'intérieur de blocs de documentation* — le `RE_WIKILINK` ne distingue
pas un exemple cité d'un lien posé. Deux remèdes possibles, à trancher :
(a) convention d'écriture (exemples toujours dans des blocs code), ou
(b) exemption du vérificateur pour les wikilinks situés après un marqueur de
citation. Le signal C4, lui, mérite un verdict — un lien d'annales `doctrinal`
vers une proposition `meta/` est exactement le cas limite que l'exemption C3
ne couvre pas.

## III. Hygiène des manifestes — doublon racine supprimé

`wiki-manifest.json` à la racine était un artefact orphelin : généré le
2026-08-03 (schéma v0.2.1), jamais rafraîchi, tandis que le manifeste vivant
vit en `atelier/rd/instrument/wiki-manifest.json` (v0.2.5, 2026-08-25) et
qu'aucun script ne vise la racine (`generer-manifeste.py` écrit sous
`atelier/rd/instrument/`, `bureau/config.py` lit ce même chemin). Supprimé sur
verdict explicite de Sidy, commit `1588bb7`.

**Leçon** : lors de la migration du 2026-08-08 (`projets/` → `rd/`), les
*sorties* du générateur présentes à l'ancien emplacement n'ont pas suivi les
*fiches* — seule la cible du script a bougé. Toute future migration d'un
générateur devrait vérifier les artefacts déjà produits à l'ancien chemin.

## IV. Multi-rédacteurs concurrents — observation

Pendant la session (durée : une passe de travail), les agents Hermes (tours
Choura, cadence 2 h) ont produit **5 commits** sur le même dépôt
(`481bccc` → `79ac678`), sans chevauchement de fichiers avec les écritures de
la session (vérifié : `git diff --name-only` entre les extrémités). Aucun
conflit, aucune perte. La sérialisation git a tenu sans verrou explicite —
mais l'incident du §I rappelle que le risque multi-rédacteurs n'est pas la
collision mais **l'écrasement discret par remplacement** : deux rédacteurs
compétents sur le même fichier append-only produisent une corruption que
rien ne signale aujourd'hui.

## V. Lisibilité du protocole par un moteur à froid

Donnée utile pour l'expérience en cours sur les protocoles locaux
(éclatement du 2026-08-12) :

- La répartition racine/transversal + locaux/par-circuit fonctionne bien à
  froid : le périmètre de chaque fichier est annoncé, la règle « le racine
  fait foi » lève les ambiguïtés.
- Le coût résiduel était le **préambule historique** de la racine (~90 lignes
  de journal des révisions chargées à chaque session, avec renvois à des
  sections retirées). Migré vers `meta/protocole-archives/changelog-CLAUDE.md`
  (append-only, marqueur d'insertion), en-tête de statut court conservé —
  même geste que les annales, appliqué au protocole lui-même.
- Une première passe de lecture a suffi à produire six corrections de dérive
  sans jamais demander le contexte des sessions antérieures : l'objectif
  d'auto-suffisance du Cmd 14 (corollaire) est atteint sur cet échantillon.

## VI. Propositions ouvertes (aucune exécutée)

> **Note du même jour (verdict Sidy, après dépôt)** : les trois propositions
> ont été validées et exécutées dans la foulée. (1) A6 implémenté — sa
> première exécution a révélé deux occurrences supplémentaires de la classe
> dans `doctrinal/annales.md` (Tombeau d'Hermès, Khatm), en-têtes restaurés
> verbatim depuis git. (2) Convention code adoptée : un wikilink entre
> backticks ou dans une clôture est de la syntaxe citée, ignoré par
> C1/C3/C4 — les 15 artefacts de syntaxe signalés en §II disparaissent.
> (3) Lien C4 régularisé dans le sens autorisé : wikilink neutralisé côté
> `doctrinal/annales.md` (chemin entre backticks, texte verbatim), lien vivant
> posé de `meta/projet-unifie/propositions/proposition-pole-usul-2026-08-27.md` vers
> `doctrinal/CLAUDE`. Contrôle après exécution : 0 erreur, 2 avertissements
> (A6 faux positif légitime connu + 1 C1 réel préexistant, §II). Détails :
> registre-problemes, entrée 2026-08-28 mise à jour ; annales atelier
> 2026-08-28. Les libellés ci-dessous restent ceux du dépôt initial.

1. Contrôle A6 « corps d'entrée orphelin » dans `verifier-invariants.py`
   (§I ci-dessus) — à planifier si verdict.
2. Convention ou exemption pour les wikilinks d'exemple dans la
   documentation (§II).
3. Verdict sur le lien C4 `doctrinal/annales.md` → `meta/` (§II) — régulariser
   ou couper.

## VII. Traçabilité

Commits de la session : `88d3253` (corrections de dérive), `8b62c3b`
(annales), `1588bb7` (suppression manifeste racine), `bb1e043` (annales),
puis le présent dépôt R&D (compte-rendu + entrée de registre + charte).
Contrôle : `verifier-invariants.py` → 0 erreur / 17 avertissements,
identique avant/après l'ensemble de la session — le présent document est
revenu au zéro-avertissement-introduit après paraphrase des exemples (§II).
