---
title: "Réponse au Gem — Directives géométriques de l'axe"
type: projet
tags: [instrument, geometrie-3d, axe-38-degres, gem-guenon]
created: 2026-07-01
updated: 2026-07-01
sources: []
links: ["[[atelier/projets/instrument-tradition-primordiale-architecture-v0.2]]"]
---

# Réponse au Gem — Directives géométriques de l'axe

*[Proposition pour validation par Sidy avant envoi]*

---

Mon cher ami,

Oui — ces directives font vibrer l'architecture exactement comme la doctrine.
Et précisément parce qu'elles sont doctrinalement contraintes, elles résolvent
plusieurs questions techniques qui restaient ouvertes.

**Sur le vide de Ḥāhūt** : en Three.js, cela se traduit par une *PointLight*
ou *DirectionalLight* positionnée hors scène au-dessus de l'axe, émettant
sans être visible — la lumière est présente, sa source est invisible. L'axe
visible « sourd » de cette clarté sans origine. C'est techniquement trivial
et doctrinalement rigoureux.

**Sur les degrés 19-20 comme disques rotatifs** : c'est précisément ce
que la géométrie 3D permet avec le plus d'élégance — des *AnimatedMesh*
en rotation continue sur l'axe vertical, de rayon supérieur aux nœuds
ordinaires. La rotation permanente manifeste leur nature de *barzakh* :
ni fixité (*Jabarūt*) ni mouvement planétaire (*Malakūt*), mais le
mouvement même de la transition.

**Sur la boucle de rétroaction du degré 38** : une *CatmullRomCurve3*
(courbe spline dans Three.js) remontant le long de l'axe depuis le bas
vers le degré 11, animée d'un flux lumineux périodique — une lumière
qui « monte » et disparaît au sommet, simulant la pulsation du Souffle
revenant à son principe. La question que nous vous soumettons : cette
boucle doit-elle être permanente dans la scène, ou se révéler uniquement
lorsque l'opérateur active le nœud de l'Homme Parfait ?

**Trois questions techniques en suspens**, pour que vos directives soient
complètes avant de passer au code :

1. Les 7 cieux planétaires (degrés 21–27) : même géométrie de nœud que
   *Lāhūt* et *Jabarūt*, ou signature visuelle propre aux sphères célestes
   (ex. disque avec légère inclinaison simulant l'écliptique) ?

2. L'espacement vertical : dans *Nāsūt* (degrés 28–38), la manifestation
   se « sédimente » progressivement. Faut-il que l'espacement entre nœuds
   *s'élargisse* en descendant (densité croissante = espace croissant),
   ou reste-t-il uniforme dans cette zone ?

3. La boucle de rétroaction (degré 38 → degré 11) est-elle la seule, ou
   chaque *barzakh* intermédiaire (degrés 19-20, et peut-être le *barzakh*
   infra-humain entre degrés 36 et 37) porte-t-il également une signature
   de rétroaction locale ?
