---
title: "Studio Principal — Espace d'Atelier"
type: materiel
tags: [synthese, enregistrement-analogique, composition, monitoring, hub]
created: 2026-08-08
updated: 2026-08-08
sources: ["to-source"]
links: ["[[atelier/materiel/neve-1073spx]]", "[[atelier/materiel/tascam-model-12]]", "[[atelier/materiel/distressor-el8]]", "[[atelier/materiel/revox-a77]]", "[[atelier/materiel/moog-voyager]]", "[[atelier/materiel/neumann-tlm103]]"]
---

# Studio Principal — Espace d'Atelier

> ⚠️ **Source `to-source`.** Fiche produite de mémoire visuelle générale
> (session claude.ai, 2026-08-08), non recoupée avec les deux fichiers déposés
> à l'appui (`raw/assets/studio-principal-vue-generale.jpeg`,
> `raw/assets/routing-schema.html`). Plusieurs points restent marqués
> incertains dans le corps (placement, synchronisation, acoustique). Article 1
> sashimono : cette pièce ne tient, pour l'instant, que par la mémoire —
> **à recouper contre la photo et le schéma avant toute levée du marqueur.**

## Nature de la fiche

Vue d'ensemble de l'espace d'atelier audio, en configuration à trois pôles
(synthèse/composition, enregistrement analogique, monitoring). Cette fiche
est une **fiche-hub** : deux appareils qu'elle mentionne ont déjà leur fiche
propre, sourcée et en place —
[[atelier/materiel/neve-1073spx]] et [[atelier/materiel/tascam-model-12]] —
et ne sont **pas** redécrits ici en détail, seulement resitués dans l'espace
et le workflow. Cette fiche documente ce qui est **nouveau** par rapport à
elles : les autres instruments et appareils du pôle, l'agencement physique,
et la chaîne de capture bout en bout.

## Configuration générale

Espace de création intégré en configuration L, trois pôles fonctionnels
distincts : synthèse/composition, enregistrement analogique (magnétique),
monitoring/écoute. Surface totale ~25 m² (`to-source`, estimation).
Circulation : axe gauche (enregistrement) ↔ centre (composition) ↔ droite
(synthèse).

## Pôle Synthèse & Composition

### Moog Voyager

- Voir fiche dédiée : [[atelier/materiel/moog-voyager]]
- État : actif, en utilisation régulière.

### Fender Rhodes 73

- Clavier électromécanique à marteaux (tines), 72 touches, ~1970s–1980s
  (`to-source`, estimation visuelle).
- Sortie ampli intégré ou préamplificateur, son percussif et chaud.
- État : actif, instrument signature en composition.

## Pôle Enregistrement Analogique

### Revox A77

- Voir fiche dédiée : [[atelier/materiel/revox-a77]]
- État : **actif en production** — instrument de capture analogique principal.

### Micros

| Modèle | Type | Usage |
|---|---|---|
| [[atelier/materiel/neumann-tlm103|Neumann TLM 103]] | Condensateur large membrane, XLR +48V | Capture vocale, sources acoustiques de précision, via [[atelier/materiel/neve-1073spx]] |
| Shure Beta 58A | Dynamique supercardioïde, XLR | Voix, sources proches/rejet larsen, via [[atelier/materiel/neve-1073spx]] |
| Shure 565SD | Dynamique omnidirectionnel vintage, XLR | Couleur rétro, capture directe (sans préampli, via Tascam CH3) |

## Pôle Monitoring & Traitements

### Yamaha H5

- Moniteur nearfield 2-way, réponse plate 50 Hz–20 kHz.
- Placement exact : `to-source` — probablement étagères hautes ou muret
  droit, non confirmé.

### Distressor EL8

- Voir fiche dédiée : [[atelier/materiel/distressor-el8]]
- Configuration : `to-source` — probablement post-production ou monitoring, non confirmé.

## Rangement et plan de travail

- Rangement mural haut : disques LP, boîtiers CD/K7, documentation papier.
- Étagères modulables centrales : câbles, adaptateurs, microSD/USB,
  maintenance.
- Plan de travail central bois naturel, chaise face aux claviers et au Revox.

## Environnement `to-source`

Lumière (fenêtre large + plafonnier diffus), traitement acoustique et
qualité des réflexions précoces : non documentés, à confirmer.

## Workflow — DAW

Logic Pro sur iPad, utilisé comme station mobile pour composition/écriture
rapide, scratch numérique et automation légère. Synchronisation Revox ↔
Logic (timecode ou manuelle) : `to-source`, non documentée.

## Chaîne de capture

Le [[atelier/materiel/tascam-model-12]] est le point focal du routage
hybride analogique/numérique (voir sa fiche pour le détail des canaux et
sorties). Chaînes observées :

1. **Mic principale** — TLM103/Beta 58A → [[atelier/materiel/neve-1073spx]]
   (+48V, EQ 3 bandes) → Tascam CH1/CH2 ; 565SD → Tascam CH3 direct (sans
   préampli).
2. **Instruments électriques** — Fender Rhodes → Tascam CH5–6 (stéréo) ;
   Moog Voyager → Tascam CH7–8 (stéréo).
3. **Hybride iPad/bande** — Logic Pro iPad ↔ Tascam (USB-C bi-directionnel)
   → bus stéréo Tascam → Send Out → Revox A77 → Return In → bus de mix
   final → Monitor Out (Yamaha H5 + casque).
4. **Bande** — Tascam REC OUT → Revox IN ; 7.5 ips (économie) ou 15 ips
   (brillance) ; Revox OUT → Tascam RETURN (boucle monitoring/ré-enregistrement).
5. **Mastering/vinyle** — mix final capturé sur bande via Revox → export
   numérique via Tascam/Logic (DDP/WAV), ou alternative lacquer cutting
   externe.
6. **Technique expérimentale — Re-Record Loop** : Tascam → Revox →
   ré-enregistrement en Tascam, génère saturation et compression entre
   générations successives. Références citées (J Dilla, D'Angelo) :
   `to-source`, non vérifiées contre une déclaration primaire de l'artiste.

## Points à confirmer avant levée du `to-source`

- Placement exact du Yamaha H5.
- Configuration rack ou standalone du Neve/Distressor.
- Synchronisation Tascam/Logic (timecode ou manuelle).
- Gestion câblage et masses (XLR/jack hybride).
- Recoupement intégral avec `raw/assets/studio-principal-vue-generale.jpeg`
  et `raw/assets/routing-schema.html`.

## Sources à déposer

1. `raw/assets/studio-principal-vue-generale.jpeg` — déjà présent, non encore
   confronté au texte de cette fiche.
2. `raw/assets/routing-schema.html` — déjà présent, non encore confronté.
