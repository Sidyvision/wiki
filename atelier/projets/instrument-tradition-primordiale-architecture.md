---
title: "Instrument de la Tradition Primordiale — Architecture Fondamentale (v0.1)"
type: projet
tags: [architecture, mandala, tradition-primordiale, tasawwuf, kabbale, conceptuel]
created: 2026-06-28
updated: 2026-06-28
sources: []
links: ["[[doctrinal/traditions/tasawwuf]]", "[[doctrinal/symboles/alam-al-mithal]]"]
---

# Instrument de la Tradition Primordiale — Architecture Fondamentale

> ⤴️ **Version courante : v0.2** — cette esquisse v0.1 est **conservée comme jalon historique**.
> L'architecture développée fait désormais foi dans
> `atelier/projets/instrument-tradition-primordiale-architecture-v0.2.md`, complétée par la
> spécification géométrique `atelier/projets/spec-technique-axe-38-degres.md`.

> *Document conceptuel issu d'une session de spécification (2026-06-28), à destination de
> Claude Code (implémentation future) et du Gem René Guénon (revue doctrinale). Statut :
> esquisse fondamentale validée dans ses principes, non encore implémentée. Révisée le
> 2026-06-28 suite à la revue du Gem René Guénon (§1.3 : ajout de l'attribut
> `directionnalite` ; §5 : renommage de l'onglet apophatique).*

---

## 0. Nature de l'instrument

Ce n'est ni une application de visualisation comparative entre traditions séparées, ni un
simple habillage graphique du wiki. C'est un **mandala** — objet de contemplation
personnelle — qui est simultanément un **instrument d'étude** de la Tradition Primordiale :
l'unité de principe sous-jacente aux formes traditionnelles multiples, telle que Guénon la
pose. L'app est conçue comme l'**interface graphique du LLM-Wiki**, le complétant sous
certains aspects, jamais comme un doublon ou une source de vérité autonome.

L'instrument sert l'étude aussi bien à l'échelle individuelle (le thème astrologique d'une
personne, lu à la lumière de la métaphysique) qu'à l'échelle cosmique (les cycles, la
précession des équinoxes, les Yuga).

---

## 1. L'Arbre unique (et non une collection d'arbres)

**Principe central, à ne jamais perdre de vue dans l'implémentation** : il n'y a pas un
arbre par tradition entre lesquels on bascule. Il y a **un seul arbre inversé**, dont la
forme actuelle, à tout moment, est elle-même le reflet de l'état du travail de discernement
accompli. L'unification de la forme n'est jamais un postulat de départ ni un effet
scripté — c'est une **convergence asymptotique**, qui ne progresse que par l'accumulation
réelle de travail doctrinal dans le wiki (correspondances confirmées, discernements résolus).

### 1.1 Comportement au basculement de tradition

- La tradition sélectionnée s'affiche en **sur-brillance**, dans sa géométrie native réelle
  (les degrés effectifs du Tasawwuf, les dix Sephiroth de la Kabbale, etc. — jamais une
  géométrie générique imposée).
- Les traditions non sélectionnées restent visibles en **transparence**, sur la même scène —
  jamais masquées complètement. C'est l'affirmation visuelle de l'unité de principe : les
  formes coexistent, une seule est mise en relief.
- Le basculement n'anime donc pas un changement de scaffold géométrique, mais un changement
  d'opacité et de sur-brillance sur une scène qui contient potentiellement toutes les
  traditions chargées simultanément.

### 1.2 Logique d'ancrage (ce qui fait converger ou non les arbres)

Chaque nœud d'un arbre traditionnel est positionné par défaut dans **sa propre logique
interne** (sa position native dans sa tradition). Un nœud ne se voit attribuer une position
partagée avec un nœud d'une autre tradition — **ancrage** — que lorsqu'une correspondance est
*établie* dans le wiki (sourcée, non forcée). Sans ancrage, les nœuds flottent librement,
chacun selon sa géométrie propre, sans tentative de superposition artificielle.

L'ancrage s'applique :
- **au plan vertical** (le degré ontologique — la dimension commune par construction, axe du
  Principe) ;
- **et aux plans horizontaux** (proximité spatiale dans la scène 3D, au-delà du seul
  positionnement sur l'axe).

### 1.3 Deux types de correspondance établie — distinction impérative

Pour éviter tout syncrétisme, le modèle de données distingue strictement :

| Type | Sens | Plan | Traitement visuel proposé |
|---|---|---|---|
| **équivalence** | Identité foncière d'un même principe ou d'un même degré de réalité ontologique à travers des voiles formels différents | essentiel / vertical | trait plein, ancrage fort (quasi-fusion de position) |
| **complémentarité** | Deux aspects distincts mais articulés, participant ensemble à un même point de l'unité principielle, sans que l'un "soit" l'autre | substantiel / horizontal | lien "tressé" entre deux nœuds qui gardent chacun leur position propre — pas de fusion |

Cette distinction n'est pas cosmétique : elle traduit directement le rappel fait en session —
les traditions n'expriment pas toujours la même chose, elles expriment souvent des aspects
**complémentaires** d'une même unité de principe. Confondre les deux catégories serait
recréer le syncrétisme que le Commandement III (Non-Syncrétisme) du wiki proscrit.

**Attribut de polarité/directionnalité (revue Gem René Guénon, 2026-06-28)** — un lien de
type `complementarite` peut porter un champ `directionnalite: none | ascendant | descendant`.
Ce champ capture les cas où un élément n'est ni équivalent ni simplement complémentaire au
sens symétrique, mais relève d'une **application plus contingente, un reflet atténué ou une
spécification** d'un autre — une hiérarchie descendante du Principe vers la manifestation.
Plutôt que de créer une troisième catégorie rigide pour cette « subordination hiérarchique »,
l'attribut se superpose à la complémentarité existante : le lien reste de nature
complémentaire (deux aspects distincts d'une même réalité), mais cesse d'être présenté comme
symétrique lorsque la directionnalité est renseignée. Quand `directionnalite: none`, le lien
est traité comme une complémentarité de plan égal (ex. *Puruṣa-Prakṛti*, Essence et
Substance).

---

## 2. Cas particulier : la Kabbale et le Sitra Ahra

Seule la Kabbale, dans cette première itération, porte explicitement sa dialectique complète
Sephiroth/Qliphoth (Sitra Ahra). Tout ce qui y est intégré se fait dans son **expression
dialectique propre** — pas de transposition générique de l'idée d'« ombre » aux autres
traditions. Les autres formes de déviation (siḥr en islam, etc.) restent classées à part,
dans leur vocabulaire et leur cadre propres (`doctrinal/deviations/`), sans qu'on leur
impose une structure de miroir qliphothique qu'elles ne possèdent pas nativement.

Une équivalence entre Qliphoth et, par exemple, des Asuras hindous ou des djinns rebelles
n'est affichée que si elle est **explicite ou claire** dans le wiki ; à défaut, chaque
concept reste classé dans sa propre catégorie, sans équivalence forcée — au pire avec une
correspondance de type "suggérée" (voir §4), jamais présentée comme tranchée.

---

## 3. Architecture spatiale et navigation

### 3.1 L'axe du Principe

Une **ligne verticale fixe**, point de départ et d'arrivée de toute navigation — visuellement
neutre, sans coloration doctrinale. Le déplacement le long de cet axe correspond au
changement de degré ontologique, du Principe vers la contingence. C'est la seule dimension
strictement commune à toutes les traditions par construction ; la correspondance exacte de
hauteur entre deux arbres reste soumise à la même logique d'ancrage qu'ailleurs.

### 3.2 Navigation propre à chaque tradition (plan horizontal/3D interne)

Chaque tradition déploie sa propre géométrie de navigation autour de l'axe (rotation,
sphère zodiacale, déploiement de l'Arbre séphirotique, etc.). Cette navigation n'est pas
uniforme — certains modèles occuperont le geste horizontal pour leur propre déploiement
(ex. rotation autour d'une sphère zodiacale).

### 3.3 Bande de sélection des traditions

Parce que le geste horizontal "naturel" est parfois déjà pris par la navigation interne d'un
modèle, le **basculement entre traditions** se fait via une bande de navigation séparée,
fixe à l'écran (en haut ou en bas), indépendante de la 3D du modèle affiché. Elle reste
toujours accessible, jamais en conflit avec le contenu.

### 3.4 Tradition pilote

Le Tasawwuf est la première tradition implémentée, en cohérence avec son développement déjà
avancé dans le wiki (`doctrinal/traditions/tasawwuf`, et les nombreuses pages liées :
barzakh, walaya, al-insan-al-kamil, etc.). Les autres traditions apparaissent dans la bande
de sélection mais peuvent rester à l'état "à venir" sans bloquer l'architecture.

---

## 4. Mécanisme de suggestion (établi vs suggéré)

Distinction à deux niveaux dans le modèle de données, miroir du statut `speculatif` du wiki :

- **correspondances établies** : sourcées, attestées dans le wiki (équivalence ou
  complémentarité, cf. §1.3).
- **correspondances suggérées** : non tranchées, proposées soit par heuristique de
  position (proximité structurelle détectée par l'app), soit par Claude au moment de
  l'actualisation (note rédigée lors de la modulation du manifeste). Jamais fondues
  visuellement avec les établies.

**Marquage visuel** : trait plein pour établi ; **pointillé + icône 🔍** pour suggéré —
cohérence directe avec le bloc Discernement du `CLAUDE.md`.

**Pipeline de validation** : une suggestion, sur action explicite de l'utilisateur, peut
générer une fiche `doctrinal/discernement/` dans le wiki. L'app est un *déclencheur*, jamais
une instance qui écrit seule dans le dépôt — cohérent avec le Commandement 12 (*upakarana*) :
l'app/l'IA documente et signale les rapprochements de forme, elle ne tranche jamais la
validité métaphysique d'une équivalence.

---

## 5. L'onglet d'instrument de délimitation apophatique

Un onglet — superposé directement sur l'arbre dans la mesure du possible, en vue
complémentaire séparée sinon — qui visualise **tout** travail inachevé repéré par une
opération de type VIGILANCE, au sens large :

- fiches `doctrinal/discernement/` au statut `en cours` ;
- tensions/contradictions signalées entre traditions (bloc 🌐 Forme Traditionnelle
  Divergente) ;
- liens marqués `to-source` ;
- non-syncrétismes signalés (ex. istiʿdād akbarien / tülku vajrayāna) ;
- toute autre trace de travail doctrinal non résolu détectée dans le wiki.

Cette vue n'est pas accessoire : elle est **aussi importante que le reste de l'instrument**.

**Nom de l'onglet (revue Gem René Guénon, 2026-06-28)** — le terme initial de « moteur de
déduction » a été écarté : il évoquait l'exercice de la raison discursive, par définition
incapable de s'élever jusqu'aux vérités métaphysiques, qui relèvent de l'intuition
intellectuelle. L'onglet est renommé **Instrument de délimitation apophatique** (variante :
*Axe de discernement négatif*). La démarche reste analogue à la théologie apophatique
(*al-tanzīh* dans le Tasawwuf, *neti neti* dans le Vedānta) : l'identification des lacunes,
des tensions doctrinales et des zones de résistance formelle permet de cerner, en négatif,
ce qui dépasse les formes — l'arbre rappelle ainsi que le Principe échappe toujours à la
systématisation, sans jamais prétendre l'atteindre par déduction.

---

## 6. Couche de données — découplage strict du moteur 3D

Le moteur 3D ne parse jamais directement le markdown du wiki. Il consomme une couche
structurée intermédiaire (`wiki-manifest`, JSON/YAML) que Claude Code génère et maintient à
partir de `doctrinal/`. Ce découplage :

- permet à l'app de fonctionner indépendamment de la source qui produit le manifeste
  (aujourd'hui Claude Code via API ; potentiellement, à terme, un modèle IA local sur un
  futur appareil dédié — incertitude assumée, non figée dans l'architecture) ;
- garantit que l'app reste une **vue** du wiki, jamais une source parallèle de vérité ;
- rend la fonction de **modulation/actualisation** simple en principe : le wiki évolue, le
  manifeste est régénéré, l'app reflète l'état le plus récent du discernement collectif.

Le flux est strictement à sens unique pour la doctrine : **wiki → manifeste → app**. Le sens
inverse (suggestion de l'app → fiche discernement du wiki) n'existe que via validation
humaine explicite (§4) — jamais automatique.

### Esquisse de structure de nœud (à raffiner en phase technique)

```yaml
node:
  id: "tasawwuf/al-insan-al-kamil"
  tradition: "tasawwuf"
  label: "Al-Insān al-Kāmil"
  source: "[[doctrinal/symboles/al-insan-al-kamil]]"
  degre_vertical: <position sur l'axe>
  ancrages:
    - type: equivalence | complementarite | suggeree
      directionnalite: none | ascendant | descendant   # pertinent surtout pour complementarite
      cible: "<id du nœud dans une autre tradition>"
      source: "[[doctrinal/...]]"   # ou null si suggérée sans source encore
  question_ouverte: <bool ou référence à une fiche discernement en cours>
```

---

## 7. Ce que ce document n'est pas

Cette esquisse fixe l'**architecture fondamentale** (axe, arbre unique, ancrage, bande de
sélection, couche de données, mécanisme de suggestion, onglet apophatique). Elle ne fixe
pas encore :
- le détail technique du moteur 3D (Three.js/WebGL, ou natif) ;
- le format exact final du manifeste ;
- la modélisation précise des degrés du Tasawwuf comme premier cas d'implémentation ;
- l'intégration du calcul astrologique multi-méthodes (à proposer par l'app selon la
  situation) ;
- l'échéancier de développement.

Ces points relèvent d'une phase ultérieure, une fois cette architecture validée — y compris,
le cas échéant, après revue par le Gem René Guénon.

---

*Statut : esquisse fondamentale (v0.1) — non implémentée. Classée en `atelier/projets/` par
liens à sens unique vers `doctrinal/` (jamais l'inverse, conformément à la règle d'étanchéité
du circuit Atelier).*
