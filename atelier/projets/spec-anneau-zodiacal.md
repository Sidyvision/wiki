---
title: "Spécification technique — Anneau zodiacal de l'Instrument"
type: projet
tags: [instrument, rendu, zodiaque, manazil, three-js, phase-2]
created: 2026-07-26
updated: 2026-07-26
sources: []
links: ["[[doctrinal/symboles/table-28-degres-nafas-rahman]]", "[[doctrinal/symboles/manazil-al-qamar]]", "[[doctrinal/symboles/ilm-al-nujum]]", "[[atelier/projets/instrument-tradition-primordiale-architecture-v0.3]]"]
---

# Spécification technique — Anneau zodiacal de l'Instrument

> Circuit **atelier**. Document de rendu, non doctrinal. Liens vers `doctrinal/` en sens
> unique (signalés ci-dessus, conformément à §V.a du protocole). Aucune page doctrinale
> ne pointe vers ce document.

## 0. Objet et statut

Rendu du bandeau zodiacal, absent du prototype `instrument-prototype-v0.2.html` alors que
la donnée existe intégralement dans le dépôt. **Manque de rendu, non manque de donnée.**

Cette spécification **n'établit aucun ancrage nouveau** et n'engage aucune correspondance
inter-traditionnelle. Elle visualise une matière déjà sourcée et déjà tranchée.

## 1. Fondement de données

- Colonnes **`Manzil`** et **`Signe (portion)`** des degrés 11–38 de
  [[doctrinal/symboles/table-28-degres-nafas-rahman]], sourcées Gloton
  (*De la mort à la résurrection*, Albouraq, pp. 45–48).
- **Convergence des 28** — premier ancrage `etabli` du dépôt (*Futūḥāt* ch. 198) :
  28 fuṣūṣ = 28 lettres = 28 degrés du *Nafas al-Raḥmān* = 28 *Manāzil al-Qamar*.
  C'est ce qui rend légitime, sans engagement nouveau, l'affichage conjoint des degrés
  et des arcs de l'écliptique : un *manzil* **est** un arc de l'écliptique.

**Règle des manifestes (§VII)** : aucune valeur zodiacale n'est écrite en dur dans le
code de rendu. L'anneau lit `wiki-manifest.json`, généré depuis `instrument-donnees.yaml`
par `generer-manifeste.py`. Flux à sens unique, inchangé.

## 2. Arbitrages (Sidy, 2026-07-26)

| Question | Verdict |
|---|---|
| Géométrie de l'anneau | **Anneau fixe à un degré cosmologique précis** (sphère des signes / *falak al-burūj*) — l'anneau est un objet cosmologique à sa place propre dans la hiérarchie, non une projection en plan de l'échelle verticale |
| Rapport aux quatre Angles (AS/DS/MC/FC) | **Repère au sol séparé, aucun contact visuel** |
| Obliquité de l'écliptique sur l'axe polaire | **Inclinée, astronomiquement réelle** |

## 3. Géométrie

### 3.1 Position verticale — dédoublement confirmé (Sidy, 2026-07-27, vérification Gloton)

L'anneau zodiacal occupe **deux degrés cosmologiques distincts**, répartissant les deux divisions non commensurables :

- **Degré 19 = Falak al-Burūj** (*Toit du Jardin paradisiaque*) : porte les **12 signes** 
- **Degré 20 = Falak al-Manāzil** (*Terre des Jardins paradisiaques*) : porte les **28 Demeures lunaires**

Justification doctrinale (Gloton, pp. 39-40) : le degré 19 constitue « le Toit ou Voûte du Jardin paradisiaque et non pas sa terre » ; le degré 20 porte « la Terre des Jardins paradisiaques ». Les deux degrés forment donc un couple explicite — voûte et sol d'un même Jardin. Ce dédoublement n'est pas une correction ergonomique : il rend visible une articulation que la source énonce et renforce la règle §3.4 (non-alignement des deux divisions).

Valeurs à inscrire dans `instrument-donnees.yaml` : 
```
zodiaque:
  degre_falak_al_buruj: 19          # 12 signes
  degre_falak_al_manazil: 20        # 28 manāzil
```

Levée du `to-source` : vérification du texte primaire (Gloton pp. 39-40) par l'utilisateur lui-même (CLAUDE.md §VII, discipline des sources, règle 2).

**⚠️ Point à vérifier à l'intégration** : le degré 19 figurait, dans la transcription du
2026-07-01, comme lettre « manquante probable » et Degré cosmique « à compléter » — les
Addenda Gloton du 2026-07-16 sont censés avoir clos ce point pour l'ensemble de la table.
Confirmer que `table-28-degres-nafas-rahman.md` porte déjà, pour le degré 19, la mention
« Falak al-Atlas/Falak al-Burūj » ; sinon, corriger la table à cette occasion (même
source, même vérification).

**Confirmation du degré 19 — Point ouvert 5 clos** : le degré 19 est confirmé par trois voies indépendantes :
- Vérification textuelle Gloton pp. 39-40 par Sidy (2026-07-27)
- Hiérarchie cosmogonique islamique (Mahdi Rouge, article II : *falak al-burūj* = degré 19)
- Table des 28 degrés du *Nafas al-Raḥmān* (degré 19 = Falak al-Atlas/Burūj)

**Adjacence avec le Barzakh supérieur — observation structurelle** : les degrés 19-20 sont
déjà spécial-traités dans le prototype comme zone de la **lentille de transition** du
Barzakh (architecture v0.3 §3.4 ; bande décimale 19.5). L'anneau zodiacal se pose donc
exactement à l'un des deux degrés que la lentille relie. Dans le prototype actuel, la
lentille et ses disques restent proches de l'axe (petit rayon), tandis que l'anneau
s'étend à un rayon bien plus large (2,60–2,95, §3.5) — a priori aucune collision
géométrique directe, seulement un partage de hauteur (Y). À vérifier visuellement à
l'implémentation ; si un ajustement s'impose, il portera sur le rayon ou l'opacité, jamais
sur un déplacement du degré (qui est une donnée, pas un paramètre de confort visuel). La
sphère sans étoiles se tenant au contact du seuil du Barzakh est une observation
structurelle — observation notée, pas affirmation doctrinale.

Implémentation : constantes `DEGRE_FALAK_AL_BURUJ` et `DEGRE_FALAK_AL_MANAZIL`, alimentées
depuis le manifeste (`meta.degre_falak_al_buruj`, `meta.degre_falak_al_manazil`). Le
module continue de refuser de s'afficher si l'une des valeurs est absente — la confirmation
vaut pour cette spécification, pas encore pour les données déployées tant qu'elles n'ont
pas été intégrées.

### 3.2 Inclinaison

L'anneau est incliné sur le plan perpendiculaire à l'axe polaire. Valeur courante de
l'obliquité : **≈ 23° 26′** (paramètre `OBLIQUITE_DEG`, non constante littérale).

Ce choix **maintient visuellement la distinction polaire/solaire** au lieu de l'effacer :
l'axe demeure polaire, l'écliptique est solaire, et l'angle entre eux se voit. C'est le
rendu le plus favorable à la vigilance transversale du pôle Gizeh (§5).

**Crochet Phase 5** : l'obliquité n'est pas fixe à l'échelle des cycles (≈ 22,1° → 24,5°
sur ~41 000 ans). Le paramètre est donc conçu comme variable dès maintenant, sans être
animé à ce stade.

### 3.3 Orientation dans son plan — paramètre d'époque, validé (Sidy, 2026-07-27)

L'origine du zodiaque (position de 0° du premier signe) et la ligne des nœuds
équinoxiaux dépendent du référentiel retenu (tropical / sidéral) et de la date de
référence (époque de calcul). **Paramètre validé** : l'anneau sera paramétré par une
constante `epoque_reference` alimentée depuis le manifeste.

Justification doctrinale (Gloton pp. 39-40) : le degré 19 porte l'Avènement des Jours
(*ḥudūth al-ayyām*), le Nom *ad-dahr* (le Temps pur, indifférencié, sans partition), et
l'actualisation des Jours cosmiques, des mois et des années. C'est exactement ce qu'on
attend du *falak al-burūj*, et cela rend **doctrinalement approprié** le paramètre
d'époque validé : la mesure du temps appartient à ce degré.

Implémentation : constante `EPOQUE_REFERENCE` (format UTC/jours juliens), alimentée depuis
le manifeste (`meta.epoque_reference`).

Matière de rattachement le moment venu :
[[doctrinal/sources/fin-des-temps-modernes-equinoxes-zodiaque-mahdi-rouge]].

### 3.4 Double division — ne jamais aligner

L'anneau porte **deux divisions superposées et non commensurables** :

- **12 secteurs** de 30° (les signes) ;
- **28 arcs** de ≈ 12° 51′ 26″ (les *manāzil*), soit **2 ⅓ manzil par signe**.

Les frontières des deux séries **ne coïncident pas**, sauf au point d'origine. Aucun
arrondi, aucun ajustement visuel, aucune graduation « harmonisée » ne doit les faire
tomber ensemble — Art. 3 de la convention sashimono (*jamais de joint forcé*). Le
décalage est une donnée, pas un défaut de rendu.

Traitement visuel distinct et hiérarchisé :
- signes : séparateurs radiaux pleins, étiquette portée ;
- *manāzil* : graduations courtes sur le bord intérieur, plus discrètes, sans étiquette
  permanente (nom au survol/sélection).

### 3.5 Dimensions

Le prototype réserve déjà le rayon 1,15–1,22 aux anneaux des bandes de Présences. L'anneau
zodiacal se place **au-delà**, pour ne pas entrer en concurrence de lecture :

| Élément | Rayon | Note |
|---|---|---|
| Bandes de Présences (existant) | 1,15 – 1,22 | inchangé |
| Anneau zodiacal — bord intérieur | 2,60 | |
| Anneau zodiacal — bord extérieur | 2,95 | |
| Graduations *manāzil* | 2,60 → 2,74 | vers l'intérieur |
| Séparateurs de signes | 2,60 → 2,95 | pleine largeur |

Palette : reprise stricte des jetons du prototype (`--or` `#d4a94e`, `--or-pale`
`#e8cf9a`, `--argent` `#aab4c8`). L'anneau est traité en **argent atténué** — l'or reste
réservé aux nœuds-degrés, qui demeurent le sujet principal.

## 4. Ce qui n'est pas rendu

- **Aucun lien visuel avec les quatre Angles** (arbitrage 2). Les Angles restent au sol,
  dans leur repère propre. Conséquence favorable : cela **écarte mécaniquement** le
  risque de conflation entre les qualités élémentaires des Angles (AS=Sec, DS=Humide,
  MC=Chaud, FC=Froid) et les attributions élémentaires classiques des douze signes —
  rapprochement qui exigerait une fiche `discernement` et n'en a pas.
- **Aucun trait reliant un nœud-degré à son arc.** L'anneau étant un objet cosmologique
  à son degré propre (arbitrage 1) et non une projection de l'échelle, tracer 28 rayons
  vers lui reviendrait à réintroduire par le rendu la lecture « projection » qui a été
  écartée.

**Point ouvert qui en découle** (voir §7) : la colonne `Signe (portion)` appartient à
*chaque* degré 11–38, alors que l'anneau n'occupe qu'un degré. Proposition par défaut —
la portion de signe d'un degré s'affiche **en texte, dans le panneau d'information du
nœud sélectionné**, sans géométrie de liaison. À valider.

## 5. Vigilances consignées

**Confrontation Gizeh** (double contrôle §VII, obligatoire) : matière confrontée au pôle
Gizeh et à sa vigilance polaire/solaire — **aucun ancrage établi**. Le rendu incliné
retenu *sert* la vigilance plutôt qu'il ne l'expose : il inscrit dans la géométrie même
la distinction entre l'axe polaire (Tradition primordiale) et l'écliptique solaire, au
lieu de les rendre coaxiaux. Aucune donnée métrologique de Gizeh n'entre dans ce module.

**Qualification sashimono** : aucun joint inter-traditionnel n'est taillé par cette
spécification. L'ensemble est un rendu de matière akbarienne déjà sourcée — **ni *hozo*,
ni *kumiko*, ni *kari-kumi*** : il n'y a pas de joint.

**Incommensurabilité 28/12** : voir §3.4. Rappel — un conflit sur la **position 5** du
cycle zodiacal (Gémeaux/Hermès) est déjà documenté et non résolu dans
[[doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise]].
Ce module **ne le touche pas** et ne doit pas être lu comme le tranchant.

**Adjacence Barzakh (degrés 19-20) — confirmée, non plus seulement observée** : voir
§3.1. Sidy a verdicté (2026-07-26) que cette adjacence n'est pas une coïncidence de
rendu : le zodiaque remplit, à son degré propre, une fonction de *barzakh* — il conduit
et traduit l'influence spirituelle vers les degrés inférieurs de la manifestation.
Discernement clos : `doctrinal/discernement/2026-07-26_zodiaque-fonction-barzakh.md`
(lien à sens unique, non répercuté vers cette spécification — rappel pour mémoire
uniquement). La coexistence visuelle anneau/lentille peut donc être assumée comme
signifiante, sans modification de rendu requise par ce seul verdict.

## 6. Module de rendu (insérable)

Dépendances dans `instrument-prototype-v0.2.html` : le groupe `monde`, la fonction
`etiquette(texte, taille, couleur)` et la table `yDegInt[]` (degré → ordonnée), déjà
présents. Le module n'introduit aucune bibliothèque nouvelle.

```javascript
// ── Anneau zodiacal ────────────────────────────────────────────────────────────
// Spec : atelier/projets/spec-anneau-zodiacal.md
// Lit le manifeste ; n'affiche rien tant que le degré du falak al-burūj
// n'est pas déclaré dans les données (aucune valeur par défaut silencieuse).

function construireAnneauZodiacal(manifeste) {
  var meta = manifeste.zodiaque || {};
  var degre = meta.degre_falak_al_buruj;          // à renseigner dans instrument-donnees.yaml
  if (degre == null || yDegInt[degre] == null) {
    console.warn("[anneau zodiacal] degré du falak al-burūj non déclaré — module inactif.");
    return null;
  }

  var OBLIQUITE_DEG = (meta.obliquite_deg != null) ? meta.obliquite_deg : 23.44;
  var R_INT = 2.60, R_EXT = 2.95, R_GRAD = 2.74;

  var groupe = new THREE.Group();
  groupe.position.y = yDegInt[degre];
  // Inclinaison sur le plan perpendiculaire à l'axe polaire (obliquité réelle).
  groupe.rotation.x = -Math.PI / 2 + THREE.Math.degToRad(OBLIQUITE_DEG);

  // -- Couronne de fond, argent atténué : l'or reste aux nœuds-degrés --
  var couronne = new THREE.Mesh(
    new THREE.RingGeometry(R_INT, R_EXT, 128),
    new THREE.MeshBasicMaterial({
      color: 0xaab4c8, transparent: true, opacity: 0.16, side: THREE.DoubleSide
    }));
  groupe.add(couronne);

  // -- Fonction utilitaire : segment radial dans le plan de l'anneau --
  function segmentRadial(angleRad, r1, r2, couleur, opacite) {
    var g = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(Math.cos(angleRad) * r1, Math.sin(angleRad) * r1, 0),
      new THREE.Vector3(Math.cos(angleRad) * r2, Math.sin(angleRad) * r2, 0)
    ]);
    return new THREE.Line(g, new THREE.LineBasicMaterial({
      color: couleur, transparent: true, opacity: opacite
    }));
  }

  // -- 12 secteurs : séparateurs pleine largeur + étiquette --
  // meta.signes : 12 entrées ordonnées, issues du manifeste (jamais codées en dur).
  var signes = meta.signes || [];
  for (var i = 0; i < 12; i++) {
    var a = (i / 12) * Math.PI * 2;
    groupe.add(segmentRadial(a, R_INT, R_EXT, 0xaab4c8, 0.55));
    if (signes[i]) {
      var aMil = ((i + 0.5) / 12) * Math.PI * 2;
      var e = etiquette(signes[i].label, 0.5, "rgba(170,180,200,.8)");
      e.position.set(Math.cos(aMil) * (R_EXT + 0.22),
                     Math.sin(aMil) * (R_EXT + 0.22), 0);
      groupe.add(e);
    }
  }

  // -- 28 manāzil : graduations courtes, bord intérieur, plus discrètes --
  // Non commensurables avec les 12 secteurs (2⅓ manzil par signe) :
  // le décalage est une donnée, il ne doit JAMAIS être ajusté.
  for (var m = 0; m < 28; m++) {
    var am = (m / 28) * Math.PI * 2;
    groupe.add(segmentRadial(am, R_INT, R_GRAD, 0xd4a94e, 0.34));
  }

  monde.add(groupe);
  return groupe;
}
```

**Note d'implémentation** : `THREE.Math.degToRad` est la forme de la révision utilisée par
le prototype ; sur une révision plus récente, remplacer par `THREE.MathUtils.degToRad`.
Vérifier contre la version réellement chargée avant intégration.

## 7. Points ouverts

1. ~~Degré du *falak al-burūj*~~ — **clos** (§3.1) : degré 19, Falak al-Atlas/Falak
   al-Burūj, vérifié par Sidy sur Gloton (2026-07-26).
2. **Affichage de la portion de signe par degré** — proposition : panneau d'information
   uniquement, sans géométrie de liaison (§4). À valider.
3. **Origine du zodiaque et référentiel** (tropical/sidéral, date de référence) —
   renvoyé à la Phase 5 (§3.3).
4. **Noms et ordre des douze signes dans le manifeste** — à peupler dans
   `instrument-donnees.yaml` depuis la table, avec la nomenclature arabe retenue par la
   source ; non renseigné ici pour ne rien poser de mémoire.
5. **Vérification de cohérence table/degré 19** — confirmer à l'intégration que
   `table-28-degres-nafas-rahman.md` porte déjà « Falak al-Atlas/Falak al-Burūj » pour
   le degré 19 (§3.1) ; sinon, corriger.
6. **Coexistence visuelle avec la lentille du Barzakh (degrés 19-20)** — à vérifier à
   l'implémentation, non anticipée comme problème (rayons très différents), mais non
   testée (§3.1, §5).
