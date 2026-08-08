---
title: "Instrument de la Tradition Primordiale — Architecture Fondamentale (v0.2)"
type: projet
tags: [architecture, mandala, tradition-primordiale, tasawwuf, kabbale, conceptuel]
created: 2026-06-28
updated: 2026-06-29
sources: []
links: ["[[doctrinal/traditions/tasawwuf]]", "[[doctrinal/symboles/alam-al-mithal]]", "[[doctrinal/symboles/hadarat-khams]]", "[[doctrinal/symboles/barzakh]]"]
---

# Instrument de la Tradition Primordiale — Architecture Fondamentale

> **Migration du 2026-08-08** : cette fiche a été déplacée de
> `atelier/projets/instrument-tradition-primordiale-architecture-v0.2.md` vers `atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.2.md` (ouverture du pôle R&D,
> verdict Sidy 2026-08-08 — proposition §IV). L'ancienne fiche subsiste
> comme stub `deprecated` avec pointeur (Cmd 10). Contenu inchangé,
> dates `created`/`updated` conservées.


> *Document conceptuel issu d'une session de spécification (2026-06-28), à destination de
> Claude Code (implémentation future) et du Gem René Guénon (revue doctrinale). Statut :
> esquisse fondamentale validée dans ses principes, non encore implémentée.*
>
> **Révisions** :
> - *2026-06-28* — §1.3 : ajout de l'attribut `directionnalite` ; §5 : renommage de l'onglet
>   apophatique.
> - *2026-06-29 (v0.2)* — §1.3/§4 : marquage visuel qualifié par nature ; §2 : correctif
>   *waswâs*/Qliphoth (étanchéité confirmée, `cible: null` par défaut) ; §3.4 : Al-Insān
>   al-Kāmil confirmé comme nœud traversant les cinq Présences, sourcé via
>   [[doctrinal/symboles/hadarat-khams]] ; §6 : schéma `wiki-manifest` figé en v0.2.1 ;
>   §8 (nouveau) : questions ouvertes consolidées, dont deux non tranchées repérées lors de
>   cet audit (lentille géométrique du *barzakh* ; Noms Divins et directions horizontales).

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

| Type | Sens | Plan | Traitement visuel |
|---|---|---|---|
| **équivalence** | Identité foncière d'un même principe ou d'un même degré de réalité ontologique à travers des voiles formels différents | essentiel / vertical | pointillé **rouge** si suggérée, trait plein rouge si établie |
| **complémentarité** | Deux aspects distincts mais articulés, participant ensemble à un même point de l'unité principielle, sans que l'un "soit" l'autre | substantiel / horizontal | pointillé **bleu** si suggérée, lien "tressé" bleu si établie |

Cette distinction n'est pas cosmétique : elle traduit directement le rappel fait en session —
les traditions n'expriment pas toujours la même chose, elles expriment souvent des aspects
**complémentaires** d'une même unité de principe. Confondre les deux catégories serait
recréer le syncrétisme que le Commandement III (Non-Syncrétisme) du wiki proscrit.

**Attribut de polarité/directionnalité** — un lien de type `complementarite` peut porter un
champ `directionnalite: none | ascendant | descendant`. Ce champ capture les cas où un
élément n'est ni équivalent ni simplement complémentaire au sens symétrique, mais relève
d'une **application plus contingente, un reflet atténué ou une spécification** d'un autre —
une hiérarchie descendante du Principe vers la manifestation. Quand `directionnalite: none`,
le lien est traité comme une complémentarité de plan égal (ex. *Puruṣa-Prakṛti*, Essence et
Substance).

**Sur la nature de l'intuition suggérée (revue Gem René Guénon, 2026-06-29)** — une
correspondance *suggérée* (non encore tranchée) porte déjà sa nature en germe : l'intuition
qui pressent un rapprochement perçoit une résonance déjà qualifiée (essentielle ou
substantielle), elle ne flotte pas dans un néant qualitatif en attendant un verdict humain.
Le champ `type` (equivalence/complementarite) est donc renseigné dès l'état `suggere`, et
non seulement à l'état `etabli` — le statut `🔍` ne signifie jamais « nature indéterminée »,
seulement « décret d'autorité non encore rendu ».

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

**Correctif acté (2026-06-29, suite à un examen contradictoire avec le Gem René Guénon)** —
ce principe d'étanchéité s'applique également aux **suggestions descendantes** (*waswâs*,
infiltrations subversives ou parodiques). Une tentative initiale de rattacher
structurellement le *waswâs* du Tasawwuf au *Sitra Ahra* kabbalistique a été examinée et
**rejetée** : elle aurait imposé au Tasawwuf une structure de miroir qliphothique qu'il ne
possède pas nativement — exactement ce que ce paragraphe interdit. Le *waswâs* reste
documenté dans son cadre propre (*nafs*, *shayāṭīn* — `doctrinal/deviations/` ou
`doctrinal/vigilance/`). Voir §4 et §6 pour la traduction technique de ce correctif.

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

**Base doctrinale du déploiement vertical (acquis le 2026-06-29, nuancé le 2026-06-30)** —
la loi de déploiement vertical du Tasawwuf s'appuie sur une fiche doctrinale dédiée,
[[doctrinal/symboles/hadarat-khams]] (les Cinq Présences divines), sourcée principalement
sur Burckhardt. L'ordre retenu, du sommet vers la base : *Hāhūt → Lāhūt → Jabarūt → Malakūt
→ Nāsūt*. **Al-Insān al-Kāmil** y est confirmé comme le nœud central qui **traverse
verticalement** l'ensemble des cinq degrés, plutôt que d'être circonscrit à l'un d'eux — il
reste donc, dans l'arbre, un nœud à part de la chaîne verticale ordinaire, et non un
cinquième point sur l'axe parmi d'autres.

**Tension non résolue (ajout 2026-06-30)** — l'intégration du *Kitāb al-Taʿrīfāt*
d'al-Jurjānī a révélé que ce dernier expose les Cinq Présences (déf. 0631) selon une
structure différente de celle de Burckhardt : non cinq paliers séquentiels, mais des
dichotomies emboîtées (Mystère absolu/relatif, chacun à deux faces), avec un cinquième
degré *synthétique* attribué à l'Homme plutôt qu'un palier de plus sur l'axe — ce qui
recoupe partiellement, sans s'y superposer clairement, la fonction déjà attribuée à
Al-Insān al-Kāmil ci-dessus. Cette divergence est documentée mais **non tranchée** — voir
[[doctrinal/discernement/tension-hadarat-burckhardt-jurjani]]. Tant qu'elle n'est pas
résolue, les valeurs de `degre_vertical` qui seront peuplées en Phase 2 devront rester
cohérentes avec la nomenclature de Burckhardt (déjà retenue), sans présumer que la lecture
de Jurjānī s'y intègre sans reste.

Le rôle exact du [[doctrinal/symboles/barzakh]] comme *fonction de transition* entre deux
degrés adjacents (ex. entre *Jabarūt* et *Malakūt*) est doctrinalement étayé comme principe
général (chaque degré/monde est « présidé par un *barzakh* », interface entre domaines
consécutifs) — point désormais confirmé par une source primaire directe (Jurjānī,
*Taʿrīfāt*, déf. 0295-0296, 0509), et non plus seulement par une source secondaire. Mais
**son application nommée à une paire précise de Présences reste une inférence, non une
citation littérale** — voir [[doctrinal/symboles/hadarat-khams]] pour le détail de cette
nuance. La traduction technique de ce principe en nœud ou lentille visuelle 3D **n'a
toujours pas été validée** (voir §8, point ouvert n°1).

---

## 4. Mécanisme de suggestion (établi vs suggéré)

Distinction à deux niveaux dans le modèle de données, miroir du statut `speculatif` du wiki :

- **correspondances établies** : sourcées, attestées dans le wiki (équivalence ou
  complémentarité, cf. §1.3).
- **correspondances suggérées** : non tranchées, proposées soit par heuristique de
  position (proximité structurelle détectée par l'app), soit par Claude au moment de
  l'actualisation (note rédigée lors de la modulation du manifeste). Jamais fondues
  visuellement avec les établies.

**Marquage visuel qualifié** (révisé 2026-06-29) :
- équivalence : trait plein rouge si établie, pointillé rouge si suggérée ;
- complémentarité : lien "tressé" bleu si établie, pointillé bleu si suggérée ;
- icône **🔍** accompagne tout lien suggéré, quelle que soit sa nature — elle signale
  l'absence de décret d'autorité humaine, jamais une nature indéterminée (cf. §1.3).

**Suggestions descendantes (*waswâs*, subversion, parodie)** — traitement distinct, non
confondu avec les suggestions ascendantes ci-dessus : pointillé irrégulier/« brisé », teinte
grise/livide, marqueur ⚠. Ce lien ne relie jamais deux traditions entre elles (cf. correctif
§2) — il s'affiche comme une **géométrie interne** à la tradition concernée (direction
descendante ou périphérique au sein de son propre arbre), jamais comme un pont visuel vers
une autre tradition.

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

L'onglet est nommé **Instrument de délimitation apophatique** (variante : *Axe de
discernement négatif*) — le terme initial de « moteur de déduction » a été écarté, car il
évoquait l'exercice de la raison discursive, par définition incapable de s'élever jusqu'aux
vérités métaphysiques, qui relèvent de l'intuition intellectuelle. La démarche reste analogue
à la théologie apophatique (*al-tanzīh* dans le Tasawwuf, *neti neti* dans le Vedānta) :
l'identification des lacunes, des tensions doctrinales et des zones de résistance formelle
permet de cerner, en négatif, ce qui dépasse les formes.

**Précision de méthode (2026-06-29)** — cette fonction ne doit pas être traitée comme un
livrable de fin de chaîne (Phase 4 dans `02-instrument-feuille-de-route.md`), mais comme une
**démarche parallèle au développement lui-même**, dès maintenant. La présente révision (v0.2)
en est elle-même un exemple concret : l'écart entre l'architecture figée et les décisions
prises en session n'a été repéré qu'a posteriori, sur question explicite — précisément le
type de dérive que cet onglet est censé signaler en continu. Voir §8 pour la conséquence
proposée sur la feuille de route.

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

### Schéma de nœud — figé en v0.2.1 (2026-06-29)

```yaml
schema_version: "0.2.1"
generated_at: "<ISO8601>"
source_commit: "<sha git>"

nodes:
  - id: "tasawwuf/al-insan-al-kamil"      # "<tradition>/<slug>"
    tradition: "tasawwuf"
    label: "Al-Insān al-Kāmil"
    source: "[[doctrinal/symboles/al-insan-al-kamil]]"
    degre_vertical: null                  # null par défaut ; peuplé fiche par fiche en Phase 2
    question_ouverte: false               # ou "[[doctrinal/discernement/slug]]"
    ancrages:
      - type: equivalence | complementarite | subversion | parodie
        etat: etabli | suggere | identifie
        directionnalite: none | ascendant | descendant   # surtout pertinent si complementarite
        cible: "<id du nœud cible>"        # null si suggérée sans source, OU si subversion/
                                            # parodie sans correspondance inter-tradition démontrée
        source: "[[doctrinal/...]]"        # ou "[[doctrinal/vigilance/...]]"
        note: ""
```

**Décisions de structure actées** :
- Stockage des ancrages **à sens unique** (un ancrage `tasawwuf/X → kabbale/Y` n'est stocké
  que dans le nœud source ; l'app reconstruit l'inverse à l'affichage) — évite toute
  désynchronisation entre deux copies d'un même fait doctrinal.
- **Un seul manifeste global**, pas un fichier par tradition — cohérent avec le principe de
  l'Arbre unique (§1) : fragmenter le fichier réintroduirait, au niveau de la donnée, la
  fragmentation que l'architecture refuse conceptuellement.
- `type: subversion | parodie` : `cible` reste `null` par défaut et ne se remplit que si une
  fiche `discernement` a *spécifiquement* investigué et établi une correspondance
  inter-traditionnelle — jamais de manière structurelle ou automatique (cf. correctif §2).

---

## 7. État d'implémentation des degrés du Tasawwuf (Phase 2 — amorcée)

La doctrine des cinq degrés est désormais fixée ([[doctrinal/symboles/hadarat-khams]]), ce
qui n'était pas le cas en v0.1. Restent à déterminer, en phase technique :
- la valeur numérique ou symbolique exacte de `degre_vertical` pour chacun des cinq nœuds ;
- le traitement géométrique du *barzakh* comme articulation entre degrés adjacents (§3.4,
  §8 point ouvert n°1) ;
- la position d'Al-Insān al-Kāmil dans la scène 3D, étant un nœud qui traverse l'axe plutôt
  que d'occuper un seul degré.

---

## 8. Questions ouvertes consolidées

À trancher avant ou pendant la phase technique — **aucune n'est tranchée par cette
révision**, elles sont seulement consolidées ici pour ne plus se perdre :

1. **Le *barzakh* comme lentille de transition visuelle** entre degrés adjacents — proposé
   par le Gem René Guénon (session du 2026-06-28), jamais validé par Sidy. Le principe
   doctrinal sous-jacent est désormais sourcé ; reste à décider s'il se traduit par un nœud
   dédié, un effet visuel sur la transition, ou autre chose.
2. **Les Noms Divins (*al-Asmāʾ al-Ḥusnā*) rattachés aux directions horizontales** de
   l'espace 3D — question posée par le Gem en fin de session du 2026-06-28, jamais reprise
   depuis.
3. **Moteur 3D** (Three.js/WebGL vs natif) et **cible** (web mobile vs application native) —
   toujours en Phase 0, non arbitrées (voir `02-instrument-feuille-de-route.md`).
4. **Conséquence de méthode (§5)** : faut-il réviser `02-instrument-feuille-de-route.md`
   pour que l'onglet apophatique/VIGILANCE soit pratiqué en continu dès maintenant plutôt que
   placé en Phase 4 ? Proposition à valider par Sidy.
5. **Tension terminologique Burckhardt/Jurjānī sur les Cinq Présences** (ajout 2026-06-30) —
   voir §3.4 et [[doctrinal/discernement/tension-hadarat-burckhardt-jurjani]]. Non bloquante
   pour la Phase 2 (la nomenclature de Burckhardt reste la référence retenue), mais à
   surveiller : une résolution future de cette tension pourrait modifier la valeur ou la
   nature même du `degre_vertical` pour un ou plusieurs des cinq nœuds.

---

## 9. Ce que ce document n'est pas

Cette esquisse fixe l'**architecture fondamentale** (axe, arbre unique, ancrage, bande de
sélection, couche de données, mécanisme de suggestion, onglet apophatique) et, depuis la
v0.2, la **base doctrinale du déploiement vertical Tasawwuf**. Elle ne fixe toujours pas :
- le détail technique du moteur 3D (Three.js/WebGL, ou natif) ;
- les valeurs exactes de `degre_vertical` pour les nœuds Tasawwuf ;
- le traitement géométrique précis du *barzakh* entre degrés (§8.1) ;
- l'intégration des Noms Divins aux directions horizontales (§8.2) ;
- l'intégration du calcul astrologique multi-méthodes ;
- l'échéancier de développement.

Ces points relèvent d'une phase ultérieure, une fois cette architecture validée — y compris,
le cas échéant, après revue par le Gem René Guénon.

---

*Statut : architecture fondamentale (v0.2) — non implémentée. Classée en `atelier/projets/`
par liens à sens unique vers `doctrinal/` (jamais l'inverse, conformément à la règle
d'étanchéité du circuit Atelier).*
