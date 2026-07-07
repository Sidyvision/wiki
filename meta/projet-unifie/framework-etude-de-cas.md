---
title: "Framework d'étude de cas — maisons, marques, structures"
type: outillage
usage: "Prompt-cadre pour agents (tout moteur) — étude de référence d'une entreprise/marque"
langue_des_etudes: "français si sujet français, anglais si sujet international"
destination_des_etudes: "atelier/etudes-de-cas/<slug>.md"
tags: [framework, etude-de-cas, strategie, label]
created: 2026-07-06
updated: 2026-07-06
sources: []
liens: []
---

# Framework d'étude de cas — Master Framework

## Objet

Grille d'analyse systématique d'une entreprise, marque ou maison de référence
(label, maison de couture, studio, marque de boisson, etc.), destinée à être
ingérée par tout modèle d'IA pour produire des études comparables entre elles
et exploitables par les agents du dépôt.

**Principe directeur** : chaque étude sépare strictement trois registres —
1. **Faits** (sourcés, stratifiés en crédibilité, jamais affirmés sans source) ;
2. **Analyse** (interprétation raisonnée, flaguée comme telle) ;
3. **Transposition** (leçons pour *Dans l'Absolu*, bloc final unique, suggéré 🔍
   tant que non validé par l'humain — Cmd 13).

## Règles d'exécution (pour l'agent)

- Langue : français pour un sujet français, anglais pour un sujet international.
- Slug : minuscules, ASCII, sans accents (`stones-throw`, `lemaire`, `fever-tree`).
- Toute donnée chiffrée disputée ou de source faible → tableau comparatif avec
  crédibilité flaguée **par item** ; à défaut de source → `to-source`.
- Aucune citation longue : paraphrase systématique, source en référence.
- Chaque module se clôt par un bloc `Signaux` (forts/faibles) même s'il est bref.
- L'étude n'idéalise pas : les crises, litiges et échecs sont des données de
  premier ordre (module 10).
- Frontmatter de l'étude : Sceau atelier étendu, `type: etude-de-cas`
  (extension à valider — voir UPDATES.md du lot fondateur).

## Frontmatter type d'une étude

```yaml
---
title: "Case Study — <Nom>"
type: etude-de-cas
secteur: musique | mode | jeu-video | boisson | edition | autre
tags: [etude-de-cas, <secteur>, <mots-cles>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["<url ou référence>", "..."]
links: []
statut_donnees: "vérifié partiel — items flagués individuellement"
---
```

---

## MODULE 1 — Fiche d'identité & genèse

**Données à collecter**
- Raison sociale, forme juridique, siège(s), date de fondation
- Fondateur(s) : parcours antérieur, compétences, capital symbolique initial
- Événement fondateur / blessure fondatrice (le « pourquoi » originel)
- Capital de départ (montant, provenance), premier produit/release
- Contexte de marché au moment de la fondation (qui dominait, quel vide)

**Questions d'analyse**
- La fondation répond-elle à un manque du marché ou à une nécessité intérieure ?
- Quel rapport entre l'histoire personnelle du fondateur et l'ADN de la maison ?

**Signaux** : fondation par nécessité intérieure = prédicteur de cohérence longue ;
fondation opportuniste = risque de dérive au premier vent contraire.

---

## MODULE 2 — Thèse & positionnement

**Données à collecter**
- La conviction fondatrice, formulable en une phrase
- L'espace occupé ET l'espace explicitement refusé
- Concurrents directs/indirects à la fondation et aujourd'hui
- Évolution du positionnement (élargissements, resserrements, dates)

**Questions d'analyse**
- La différenciation est-elle structurelle (modèle, curation, chaîne de valeur)
  ou cosmétique (ton, visuel) ?
- Le positionnement survit-il au fondateur ? Est-il codifié ou incarné ?
- Quelle est l'unité réelle du catalogue : genre, goût, méthode, personne ?

**Signaux** : capacité à dire non (projets refusés documentés) ; élargissement
du périmètre sans dilution perçue.

---

## MODULE 3 — Direction artistique & marque

**Données à collecter**
- Identité visuelle : direction artistique interne ou externe, figures clés
  (ex. rôle d'un art director historique), constance/mutations
- Identité sonore/matérielle : signature reconnaissable, formats fétiches
- Nom, logo, généalogie sémantique du nom
- Rapport signature/anonymat du fondateur et des artistes
- Gestion du canon : rééditions, anniversaires, éditions définitives

**Questions d'analyse**
- La marque précède-t-elle les produits (on achète « la maison ») ou l'inverse ?
- Cohérence sémiotique cross-média (pochettes, site, boutique, objets) ?
- Comment le canon est-il entretenu sans devenir musée ?

**Signaux** : achat « en confiance » (le public achète sans écouter/essayer) ;
existence d'un vocabulaire propre repris par la presse et le public.

---

## MODULE 4 — Produit & catalogue

**Données à collecter**
- Volume et rythme de sorties (par an, évolution)
- Ratio nouveautés (frontlist) / catalogue (backlist) dans l'activité
- Formats : vinyle, 45t, cassette, numérique, éditions limitées, audiophiles
- Politique de curation : qui décide, selon quels critères déclarés
- Sous-marques/imprints et leur logique (segmentation, laboratoire, réédition)

**Questions d'analyse**
- Le catalogue est-il un actif (rentes de backlist) ou un flux ?
- Les éditions limitées créent-elles de la rareté réelle ou artificielle ?
- Les imprints protègent-ils la marque-mère ou la diluent-ils ?

**Signaux** : backlist qui finance la prise de risque frontlist ; rééditions
anniversaires traitées comme des événements éditoriaux à part entière.

---

## MODULE 5 — Modèle économique

**Données à collecter**
- Flux de revenus : ventes physiques, numérique/streaming, publishing/sync,
  merchandising, licences, événements, activités annexes
- Marges par format (si disponibles), structure de coûts
- Taille : effectifs, CA estimé (flagué selon source), rentabilité déclarée
- Rapport au capital extérieur : indépendance, dettes, participations, rachats
- Deals types avec les artistes/créateurs (partage, durée, propriété des masters)

**Questions d'analyse**
- Quel flux paie les factures, quel flux porte le sens ? Sont-ils alignés ?
- Le modèle survivrait-il à la disparition d'un canal (ex. streaming) ?
- L'indépendance est-elle un choix économiquement soutenu ou une fragilité ?

**Signaux** : diversification des revenus SANS diversification du propos ;
publishing/sync développés en interne (signe de maturité administrative).

---

## MODULE 6 — Production & logistique

**Données à collecter**
- Chaîne de fabrication : presseurs, imprimeurs, façonniers, mastering
  (noms des partenaires si publics, ex. studio de gravure attitré)
- Localisation de la production, délais types, tailles de tirage
- Gestion des stocks, ruptures, repressages
- Contrôle qualité et standards revendiqués (grammage, gravure, packaging)

**Questions d'analyse**
- La qualité de fabrication est-elle un argument public ou un coût caché ?
- Quels partenaires sont stratégiques (irremplaçables) vs commodité ?

**Signaux** : partenaires de fabrication nommés publiquement et fidèles ;
le « behind the scenes » de fabrication utilisé comme contenu.

---

## MODULE 7 — Distribution

**Données à collecter**
- Circuits : direct-to-consumer (boutique propre), disquaires/détaillants,
  distributeurs tiers, plateformes numériques, export
- Part estimée du D2C, exclusivités boutique propre
- Géographie : marchés forts, bureaux à l'étranger
- Doctrine de rareté ou d'abondance (tirages limités vs disponibilité)

**Questions d'analyse**
- Qui possède la relation client : la maison ou l'intermédiaire ?
- Les exclusivités D2C nourrissent-elles ou cannibalisent-elles le réseau
  de détaillants ?

**Signaux** : exclusivités boutique propre pour les éditions les plus désirables ;
réseau de disquaires traité comme partenaire culturel, pas comme simple canal.

---

## MODULE 8 — Marketing & communication

**Données à collecter**
- Canaux : site propre, newsletter, réseaux, radio/presse, documentaires, livres
- Ton et registre ; rapport aux codes marketing dominants
- Rythme et rituels (anniversaires, séries, drops)
- Économie de l'attention vs économie de la confiance (acquisition vs fidélité)
- Rôle des prescripteurs (radios, DJs, boutiques, presse spécialisée)

**Questions d'analyse**
- La communication vend-elle des produits ou entretient-elle un monde ?
- Que ferait la maison si un canal disparaissait demain ?
- Anti-marketing revendiqué : posture ou pratique vérifiable ?

**Signaux** : newsletter/canaux propres > plateformes louées ; objets éditoriaux
(documentaire, livre, bar, radio) qui font le travail de marque sur la durée.

---

## MODULE 9 — Culture, communauté & gouvernance

**Données à collecter**
- Rapport aux artistes/créateurs : développement, rétention, départs notables
- Figures clés non-fondatrices (GM, art director, A&R) et leur rôle historique
- Contrats types, litiges publics, réputation dans le milieu
- Communauté : fans, collectionneurs, lieux physiques, événements
- Transmission : que se passe-t-il après/hors le fondateur ?

**Questions d'analyse**
- La maison fabrique-t-elle des carrières ou consomme-t-elle des talents ?
- Les fonctions critiques sont-elles institutionnalisées ou personnelles
  (risque : tout repose sur une relation) ?
- Les litiges révèlent-ils un défaut de structure (comptabilité, transparence,
  séparation des rôles) transposable en garde-fou ?

**Signaux** : alumni qui restent ambassadeurs après départ ; à l'inverse,
litiges récurrents sur la transparence financière = défaut structurel.

---

## MODULE 10 — Trajectoire & points d'inflexion

**Données à collecter**
- Chronologie des pivots : déménagements, changements de périmètre, crises
- Ce qui a failli tuer la maison (et ce qui l'a sauvée)
- Succès inattendus et leur gestion (a-t-on suivi le succès ou le cap ?)
- Position actuelle : croissance, plateau, transmission, rachat
- Longévité comparée au secteur

**Questions d'analyse**
- Les crises ont-elles renforcé la thèse ou l'ont-elles négociée ?
- Le succès commercial d'un produit a-t-il déformé la curation ?

**Signaux** : refus documenté de suivre un succès hors-thèse ; capacité à
survivre à l'effondrement d'un modèle de revenus.

---

## BLOC FINAL — Transposition 🔍 (suggéré)

Unique bloc autorisé à parler de *Dans l'Absolu*. Structure imposée :

1. **Trois principes transposables** (avec le module d'origine)
2. **Deux garde-fous** (leçons négatives : ce qu'il faut structurer pour éviter)
3. **Une expérimentation concrète** proposable à court terme
4. Rappel : toute adoption = décision humaine (Cmd 13) ; toute correspondance
   avec la doctrine du dépôt = fiche discernement, jamais supposée (Cmd 3).

---

## Annexe — Barème de crédibilité des sources

| Niveau | Type de source | Usage |
|---|---|---|
| A | Documents officiels, comptes publiés, site de la maison (faits propres) | Affirmable |
| B | Presse spécialisée établie, interviews directes du fondateur/dirigeants | Affirmable avec attribution |
| C | Wikipédia, agrégateurs, presse générale | Recoupable, à confirmer |
| D | Estimations tierces (revenus, parts de marché), bases commerciales | Toujours flagué « estimation, crédibilité faible » |

Un fait de niveau D jamais recoupé reste `to-source`.
