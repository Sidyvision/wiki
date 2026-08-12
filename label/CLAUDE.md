بسم الله الرحمن الرحيم

# CLAUDE.md — Protocole local : circuit `label/`

> **Statut : méthode à l'essai** (éclatement expérimental du 2026-08-12, verdict
> Sidy). Ce fichier porte la lettre complète des règles **propres** au circuit
> `label/` — Sceau, ancrage éthique de la structure, nomenclature, Action
> Publication. Les règles **transversales** (étanchéité inter-circuits, discipline
> des sources, double contrôle sashimono/Gizeh, commandements absolus, supervision
> des agents) restent dans le `CLAUDE.md` racine, **toujours chargé** quel que soit
> le dossier de travail — ce fichier ne s'y substitue pas, il le complète. En cas
> de doute ou de silence de ce fichier sur un point, le `CLAUDE.md` racine fait foi.
> Version pré-éclatement intégrale :
> `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md`.

-----

## Structure du circuit

`direction-artistique/` (dont `amorcage/` : idées en gestation) ·
`musique/creation/` + `musique/ingenierie/` (une paire par morceau, même slug) ·
`film/creation/` + `film/technique/` · `photographie/creation/` +
`photographie/technique/` · `production/` · `administratif/` · `distribution/` ·
`marketing-communication/`.

## Nomenclature

`label/<pole>/<slug>.md`. Morceaux : `label/musique/creation/<slug>.md` +
`label/musique/ingenierie/<slug>.md` — la paire partage le **même slug**. Le
suffixe d'export `.ex` des titres de travail est **toujours retiré** des slugs et
des titres définitifs. Table des slugs de l'album 01 : figée dans
`label/production/album-01.md` — toute fiche morceau s'y conforme.

## Le Sceau label

```yaml
---
title: "Titre exact"
type: direction-artistique | amorcage | creation | technique | ingenierie | production | administratif | distribution | marketing-communication
medium: musique | film | photographie | transversal
projet: "album-01"        # album-01 | album-02 | hors-album | label
statut: idee | en-cours | valide | sorti | archive
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
liens: []                  # liens internes au circuit label
liens_atelier: []          # renvois sens unique vers atelier/materiel/ uniquement
---
```

- **`amorcage/`** : `statut` prend `en-gestation | concretise` ; à la
  concrétisation, `liens` pointe la fiche née. Une fiche amorçage n'est jamais
  supprimée : elle documente la généalogie de l'œuvre.
- **`musique/ingenierie/`** : champs additionnels recommandés `bpm`, `tonalite`,
  `signature`, `daw` (données objectives ; les captures d'écran du DAW sont une
  source valide pour les renseigner).
- **Règles de liens** : `label/ → atelier/materiel/` autorisé (sens unique, via
  `liens_atelier`) ; `label/ → doctrinal/` pour une œuvre s'inspirant d'un
  principe **ou pour un acte de structure réglant sa conduite sur un principe**
  (même régime que `atelier/projets/`), **signalé**, et **marqué suggéré (🔍)**
  tant qu'un discernement afférent n'est pas tranché. Interdits :
  `atelier/ → label/`, `doctrinal/ → label/`, `label/ → meta/`.

## Ancrage éthique de la structure (règles des 2026-07-06)

Les aspects contractuels et commerciaux du label (`administratif/`, `production/`,
`distribution/`, `marketing-communication/`) sont soumis à la **même logique
d'ancrage et d'alignement doctrinal que les œuvres**, afin d'assurer une conduite
éthique de la structure :

1. Tout engagement de la structure (contrat, prix, produit, campagne, texte
   public) est **examinable contre les principes ancrés** dans le dépôt — au
   premier chef la doctrine du don : le bénéfice est **émergent, jamais promis**
   (frontière à la fois doctrinale et légale — refus de l'accumulation, de la
   spéculation, du bénéfice contractuellement promis).
2. Cet examen s'incarne dans la **tension conçue** des fonctions : le Commerce
   assure le contrepoids de rentabilité (la maison doit tenir), le Gardien du
   Protocole **signale** toute dérive contre l'intention ; ni l'un ni l'autre ne
   tranche — **l'humain décide** (Cmd 13). La tension entre eux est voulue, pas un
   dysfonctionnement.
3. L'alignement ne transforme jamais une fiche commerciale en page doctrinale : la
   fiche `label/` ne porte que les **conséquences de conduite** ; les principes
   restent en `doctrinal/`, les correspondances non tranchées en `discernement/`
   (statut `speculatif`), les motifs personnels en `meta/`.
4. Tant que la correspondance doctrine ↔ organisation n'est pas tranchée par
   l'utilisateur, elle demeure **suggérée (🔍)** — l'examen éthique des actes
   n'attend pas, lui, le verdict : la doctrine du don gouverne la distribution dès
   à présent.
5. **Compétence qualifiée** : les questions juridiques, fiscales et
   réglementaires sont cadrées et sourcées par la machine, **jamais tranchées sans
   professionnel qualifié** ; les sujets à risque réglementaire (registre
   numérique, fiscalité du don, droits mécaniques même pour un tirage offert) sont
   **flagués**, jamais validés d'office.
6. **Alignement Fiqh** : pour les activités relevant de son cadre (transactions,
   dons, contrats), la structure règle sa conduite sur le **fiqh**, école
   **mālikite** en préséance ; à défaut de ressource malikite, recours subsidiaire
   documenté aux écoles shāfiʿite, ḥanafite ou ḥanbalite — question par question,
   **jamais de talfīq silencieux**. Chaque question instruite = une étude datée
   `doctrinal/etudes/` portant le bloc ⚖️ (Action Examen de Fiqh, voir
   `doctrinal/CLAUDE.md`), générale et neutre — l'application au cas concret vit
   en `label/` avec lien à sens unique. Le Gardien du Protocole harmonise (une
   face vers le label, une face vers le corpus fiqh doctrinal) en **signalant** ;
   le verdict d'adoption appartient à l'humain (Cmd 13), le renvoi au savant
   qualifié restant toujours ouvert pour les cas nouveaux.

## Action : PUBLICATION (site *Dans l'Absolu* — organe public du label)

Flux : **dépôt (`label/`) → `site-manifest.json` (script déterministe) → zones
marquées des pages HTML → déploiement PRÉVERSION → validation humaine →
PRODUCTION → annales.**

1. Déclencheur : fiche `label/` à `statut: sorti` (ou `valide`) portant un bloc
   `publication:` (cible, media, lineage).
2. Le manifeste obéit à la règle commune des manifestes (CLAUDE.md racine §VII) :
   généré par script déterministe, jamais par LLM, flux à sens unique
   dépôt → manifeste → interface, correspondances « établies » vs « suggérées »
   distinguées.
3. L'injection ne touche que les zones `<!-- BEGIN:auto-x --> … <!-- END:auto-x -->`.
4. **Porte humaine non négociable** : préversion d'abord, production seulement
   après validation explicite dans la session courante. Aucune exception —
   c'est l'équivalent publication de l'interdiction d'auto-accept.
5. Le site ne réécrit jamais le dépôt. Chaque publication = une ligne d'annales
   label (`label/annales.md`).
