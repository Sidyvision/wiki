---
title: "Spécification technique — Axe des 38 degrés du Nafas al-Raḥmān (v1.0)"
type: projet
tags: [instrument, three-js, architecture-3D, nafas-rahmani, axe-vertical]
created: 2026-07-01
updated: 2026-07-01
sources: ["[[doctrinal/symboles/table-28-degres-nafas-rahman]]"]
---

# Spécification technique — Axe des 38 degrés du Nafas al-Raḥmān

> **Migration du 2026-08-08** : cette fiche a été déplacée de
> `atelier/projets/spec-technique-axe-38-degres.md` vers `atelier/rd/instrument/spec-technique-axe-38-degres.md` (ouverture du pôle R&D,
> verdict Sidy 2026-08-08 — proposition §IV). L'ancienne fiche subsiste
> comme stub `deprecated` avec pointeur (Cmd 10). Contenu inchangé,
> dates `created`/`updated` conservées.


> **Autorité doctrinale** : Gem René Guénon (directives reçues 2026-07-01).
> Toutes les décisions géométriques ci-dessous sont validées doctrinalement.
> Claude Code applique, ne redécide pas.
> **Moteur cible** : Three.js / WebGL (décision d'architecture confirmée implicitement).

---

## 1. Structure de l'axe — vue d'ensemble

L'axe vertical est l'unique colonne vertébrale de la scène 3D.
Il comporte 38 degrés organisés en six zones distinctes.

```
Zone 0 — HAAHUT (degrés 1-10)      : VIDE — source lumineuse invisible
Zone 1 — LAHUT  (degrés 11-14)     : 4 nœuds, espacement resserré
Zone 2 — JABARUT (degrés 15-18)    : 4 nœuds, blancheur fixe
Zone 3 — BARZAKH sup. (deg. 19-20) : 2 disques rotatifs larges
Zone 4 — MALAKUT (degrés 21-27)    : 7 nœuds + anneaux inclinés
Zone 5 — NASUT (degrés 28-38)      : 11 nœuds, espacement exponentiel
Boucle  — RETOUR (38 → 11)         : CatmullRomCurve3 permanente, pulsante
```

---

## 2. Zone 0 — Ḥāhūt (degrés 1–10) : Vide absolu

**Directive** : Aucune géométrie visible. Pas de nœud, pas de sphère, pas de disque.

**Implémentation** :
```javascript
// Source lumineuse invisible au sommet — l'axe "sourd" de cette clarté
const haahutLight = new THREE.PointLight(0xffffff, 1.5, 200);
haahutLight.position.set(0, Y_HAAHUT, 0); // Y_HAAHUT = sommet + marge
scene.add(haahutLight);

// Gradient de luminosité sur l'axe supérieur (shader ou fog inverse)
// L'axe s'éclaircit progressivement vers le haut sans jamais montrer
// un point de source.
```

**Interaction** : Au survol de la zone Y_HAAHUT → Y_11, afficher en overlay
les 10 formules d'unification (Hadîth du Trésor caché, Basmala, Kalimatan, etc.)
comme texte immuable en arrière-plan, non en popup.

---

## 3. Zone 1 — Lāhūt (degrés 11–14) : Densité archétypale

**Espacement** : resserré — tension maximale avant le déploiement.
Suggestion : Y_11 → Y_14 = 20% de l'espace total de l'axe.

**Degré 11 (Alif/Hamza)** : nœud particulier — doit visuellement « envelopper »
l'ensemble de la colonne. Sphère légèrement plus grande, halo lumineux étendu.

**Nœuds 12–14** : sphères standard, couleur Lāhūt (blanc pur ou or pâle).

---

## 4. Zone 2 — Jabarūt (degrés 15–18) : Quaternaire fixe

**Directive** : nœuds de pure blancheur géométrique, fixes, impersonnels.
Pas d'animation. Pas d'inclinaison. Stabilité absolue.

**Couleur** : blanc pur (#ffffff ou légèrement bleuté).
**Géométrie** : SphereGeometry standard, taille uniforme.

---

## 5. Zone 3 — Barzakh supérieur (degrés 19–20) : Disques rotatifs

**Directive** : mutation de signature visuelle. Ces deux degrés ne sont plus
des points — ils se déploient horizontalement en disques concentriques ou cercles
en rotation. Ils sont la "porte des cieux" — la lumière se fragmente ici.

**Implémentation** :
```javascript
// Degré 19 (falak al-atlas — Sphère sans étoiles)
const disc19 = new THREE.Mesh(
  new THREE.TorusGeometry(RADIUS_BARZAKH, 0.05, 8, 64),
  new THREE.MeshBasicMaterial({ color: 0xaaddff, transparent: true, opacity: 0.6 })
);
disc19.position.y = Y_19;
// Rotation continue sur Y
function animate() { disc19.rotation.y += 0.003; }

// Degré 20 (falak al-kawakib — Étoiles fixes) : anneau plus grand, rotation inverse
const disc20 = new THREE.Mesh(
  new THREE.TorusGeometry(RADIUS_BARZAKH * 1.4, 0.05, 8, 64),
  new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.8 })
);
disc20.position.y = Y_20;
function animate() { disc20.rotation.y -= 0.002; } // sens inverse
```

---

## 6. Zone 4 — Malakūt planétaire (degrés 21–27) : Nœud + anneau incliné

**Directive** : chaque ciel planétaire = nœud central (pivot spirituel) ceinturé
par un anneau en rotation lente, inclinaison variant légèrement d'un degré à l'autre
(évocateur de l'écliptique et du mouvement planétaire propre à chaque sphère).

**Implémentation** :
```javascript
const PLANETS = [
  { deg: 21, name: 'Saturne', color: 0x8899aa, inclination: 0.05 },
  { deg: 22, name: 'Jupiter', color: 0x99aacc, inclination: 0.08 },
  { deg: 23, name: 'Mars',    color: 0xcc6644, inclination: 0.12 },
  { deg: 24, name: 'Soleil',  color: 0xffdd66, inclination: 0.00 }, // équatorial
  { deg: 25, name: 'Venus',   color: 0xeeeedd, inclination: 0.10 },
  { deg: 26, name: 'Mercure', color: 0xaabbaa, inclination: 0.15 },
  { deg: 27, name: 'Lune',    color: 0xddddee, inclination: 0.18 },
];

PLANETS.forEach(p => {
  // Nœud central
  const node = new THREE.Mesh(
    new THREE.SphereGeometry(0.12),
    new THREE.MeshStandardMaterial({ color: p.color, emissive: p.color, emissiveIntensity: 0.3 })
  );
  node.position.y = Y_MAP[p.deg];

  // Anneau orbital incliné
  const ring = new THREE.Mesh(
    new THREE.TorusGeometry(0.35, 0.02, 6, 48),
    new THREE.MeshBasicMaterial({ color: p.color, transparent: true, opacity: 0.4 })
  );
  ring.rotation.x = Math.PI / 2 + p.inclination;
  ring.position.y = Y_MAP[p.deg];
  // Rotation lente en animation
});
```

---

## 7. Zone 5 — Nāsūt (degrés 28–38) : Espacement exponentiel

**Directive** : l'espacement entre nœuds s'élargit exponentiellement vers le bas.
Plus on descend, plus la sédimentation est lourde, plus la multiplicité se déploie.

**Calcul de positions** :
```javascript
// Y_28 à Y_38 : espacement exponentiel croissant vers le bas
// Si Y_axis_bottom = -100 et Y_28 = Y_27 - delta_base
const DELTA_BASE_NASUT = 3;    // espacement minimal (entre éléments)
const EXPONENT_NASUT   = 1.25; // facteur d'élargissement
let y = Y_MAP[27];
for (let deg = 28; deg <= 38; deg++) {
  y -= DELTA_BASE_NASUT * Math.pow(EXPONENT_NASUT, deg - 28);
  Y_MAP[deg] = y;
}
// Résultat : espace 28-29 = 3, espace 37-38 ≈ 24 (×8 plus large)
```

**Transition 36→37 (Djins → Homme)** : variation de texture/couleur au seuil
(pas de courbe remontante — barzakh local géré par signature colorimétrique).

---

## 8. Boucle de rétroaction (38 → 11) : Permanente et unique

**Directive** :
- Permanente, subtile, jamais déclenchée uniquement par événement
- Fil lumineux discret, presque transparent, en pulsation rythmique continue
- Au survol/activation du nœud 38 : illumination intense
- STRICTEMENT UNIQUE — pas d'autres boucles remontantes dans la scène

**Implémentation** :
```javascript
// Courbe spline remontant le long de l'axe (légèrement décalée en X pour visibilité)
const returnCurve = new THREE.CatmullRomCurve3([
  new THREE.Vector3(0.3, Y_MAP[38], 0),
  new THREE.Vector3(0.5, (Y_MAP[38] + Y_MAP[11]) / 2, 0),
  new THREE.Vector3(0.2, Y_MAP[11], 0),
]);
const tubeGeo = new THREE.TubeGeometry(returnCurve, 64, 0.015, 6, false);

// Matériau pulsant (shader custom ou MeshBasicMaterial avec opacity oscillante)
const tubeMat = new THREE.MeshBasicMaterial({
  color: 0xffffff,
  transparent: true,
  opacity: 0.15, // discret au repos
});
const returnTube = new THREE.Mesh(tubeGeo, tubeMat);
scene.add(returnTube);

// Pulsation continue
let pulse = 0;
function animate() {
  pulse += 0.02;
  tubeMat.opacity = 0.1 + 0.08 * Math.sin(pulse); // 0.02 à 0.18
}

// Activation sur nœud 38
node38.on('click', () => {
  tubeMat.opacity = 0.85; // illumination intense
  setTimeout(() => tubeMat.opacity = 0.15, 3000);
});
```

---

## 9. Positionnement Y — Table de référence (à calibrer)

```javascript
// Valeurs indicatives — à ajuster lors du rendu pour équilibre visuel
const Y_MAP = {
  // Lāhūt (resserré)
  11: 80,  12: 72,  13: 65,  14: 59,
  // Jabarūt
  15: 50,  16: 41,  17: 32,  18: 23,
  // Barzakh supérieur
  19: 12,  20: 4,
  // Malakūt planétaire
  21: -8,  22: -18, 23: -28, 24: -38, 25: -48, 26: -58, 27: -68,
  // Nāsūt (exponentiel)
  // Calculé par la fonction ci-dessus (§7)
};
```

---

## 10. Attributs de données par nœud (wiki-manifest)

Chaque nœud Three.js reçoit ses données depuis le wiki-manifest :

```javascript
node.userData = {
  degre: 24,
  manzil: 14,
  lettre: 'ن',
  lettre_rom: 'nun',
  nom_divin: 'an-Nur',
  nom_divin_fr: 'la Lumière',
  degre_cosmique: 'Soleil (shams)',
  hadra: 'malakut',
  prophete_siege: 'Idrīs (Enoch)',
  prophete_facss: 'ʿUzayr (Esdras)',
  jour: 'dimanche',
  manzil_nom: "Simāk ʿAzal",
  manzil_etoile: "L'Épi (Spica)",
  signe_zodiaque: 'vierge',
  source: 'ibn-arabi-de-la-mort-a-la-resurrection-gloton, p.46',
};
```
