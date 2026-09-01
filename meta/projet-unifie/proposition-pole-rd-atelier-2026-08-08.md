---
title: "Proposition — le pôle R&D de l'atelier (vers le dépôt-laboratoire)"
type: proposition-structure
statut: brouillon
cible: "CLAUDE.md — §II, §V.a, §VI ; atelier/ ; clôt la question ouverte de la v3 du lot Kojima (liens_atelier)"
created: 2026-08-08
updated: 2026-09-01
---

# Proposition — le pôle R&D de l'atelier

> **Statut au dépôt de la fiche (2026-08-08)** : `brouillon`, non visé. Rien de ce
> qui suit n'est exécuté ; c'est un plan présenté avant toute écriture (Cmd 6),
> intégralement réversible (Art. 5). Le verdict d'architecture appartient à Sidy
> (Cmd 13).
>
> **État au 2026-09-01 — VALIDÉE ET EXÉCUTÉE le jour même.** Le verdict de Sidy
> (Option C, nom `rd/`, phase 1 partielle) est tombé le 2026-08-08 et le pôle a été
> ouvert dans la foulée : `atelier/rd/index.md` en porte la charte, `atelier/CLAUDE.md`
> la structure, 16 fiches ont été migrées de `atelier/projets/` fiche par fiche
> (stubs `deprecated` avec pointeur, Cmd 10), et le pôle compte aujourd'hui neuf
> sous-dossiers actifs. Entrée d'annales : `atelier/annales.md`, `[2026-08-08]`,
> commit `3c1b3d8`. Le champ `statut: brouillon` du frontmatter et le paragraphe
> ci-dessus n'ont jamais été retouchés après exécution — ils sont **conservés tels
> quels** (Cmd 10) et ne décrivent plus que l'état du jour de leur rédaction.
> Le champ frontmatter lui-même est laissé en l'état : aucun vocabulaire de `statut:`
> n'est établi pour les propositions, l'arrêter relève de Sidy (point ouvert).

---

## I. La demande, reformulée fidèlement

Ouvrir un pôle **R&D** qui rassemble tout ce qui relève de l'ingénierie —
technique, musicale, matérielle et logicielle, outillage et scripts — et qui
accueille naturellement l'Instrument. Horizon déclaré : que le dépôt devienne,
à terme, un **véritable laboratoire**.

## II. État des lieux (ce qui existe déjà, dispersé)

Le dépôt fait déjà de la R&D sans le dire. Relevé d'après les annales :

| Matière | Où elle vit aujourd'hui | Nature réelle |
|---|---|---|
| Architecture de l'Instrument, specs (axe 38 degrés, anneau zodiacal) | `atelier/projets/` | **développement** (specs, itérations, notes d'impact) |
| Scripts déterministes (`generer-manifeste.py`, `generer-karubi.py`, `verifier-invariants.py`, `compare`) | `meta/` et racine | **outillage** de laboratoire, déjà versionné |
| Fiches machines (Neve 1073SPX…), routing | `atelier/materiel/` | **référence**, pas recherche |
| Études de cas (Stones Throw, Kojima Productions) | `atelier/etudes-de-cas/` | **recherche comparative** normée par framework |
| Briefs d'infrastructure, hermes-prompts | `meta/projet-unifie/` | **conception de système** (sensible : reste en meta) |
| Ingénierie musicale par morceau | `label/musique/ingenierie/` | ingénierie **d'œuvre** (reste au label, paire creation/ingenierie) |

Le constat : la fonction R&D existe, éclatée entre trois circuits. Ce qui
manque n'est pas de la matière, c'est **un lieu et une discipline**.

## III. Trois options d'architecture, et la recommandation

**Option A — un sixième circuit `rd/`.** Écartée. Multiplier les circuits
étanches multiplie les règles de liens ; et la R&D touche par nature à tout
(matériel, label, meta), ce qui ferait de son étanchéité une fiction. Un
circuit qui doit lier partout n'est pas un circuit.

**Option B — renommer `atelier/` en `rd/`.** Écartée. `atelier/materiel/` et
`atelier/entretiens/` sont de la **référence**, pas de la recherche ; les fondre
dans un pôle R&D confondrait deux régimes (consulter ≠ expérimenter). Et la
stabilité des noms de circuits est une valeur en soi dans un dépôt versionné.

**Option C — un pôle `atelier/rd/` à l'intérieur du circuit existant.**
**Recommandée.** L'atelier reste le circuit du métier ; il se structure en deux
régimes explicites :

- **référence** : `materiel/`, `entretiens/` — ce qu'on consulte ;
- **recherche** : `rd/` (nouveau) et `etudes-de-cas/` — ce qu'on instruit.

C'est la solution la plus économe : zéro nouveau circuit, zéro règle
d'étanchéité nouvelle, migration minimale, réversibilité maximale.

> *Homologie notée en passant, sans en faire un argument* : c'est aussi la
> structure relevée dans la fiche Mother Base (§5 bis) — pôles disjoints par
> fonction, la R&D étant précisément l'un d'eux. La convergence est plaisante ;
> la justification est ci-dessus, pas dans le jeu.

## IV. Arborescence proposée

```
atelier/
├── index.md · annales.md          ← annales propres au circuit (à ouvrir, Cmd 9)
├── materiel/                      ← RÉFÉRENCE (inchangé)
├── entretiens/                    ← RÉFÉRENCE (inchangé)
├── etudes-de-cas/                 ← RECHERCHE comparative (inchangé)
└── rd/                            ← RECHERCHE & DÉVELOPPEMENT (nouveau)
    ├── instrument/               ← migration de atelier/projets/ (specs, notes d'impact)
    ├── infrastructure/           ← setup réel : serveur, agents, hardware/software
    │                                (destination de la transposition Mother Base §5bis)
    ├── audio/                    ← ingénierie son GÉNÉRIQUE (bancs d'essai, chaînes,
    │                                mesures) — l'ingénierie PAR MORCEAU reste au label
    ├── outillage/                ← scripts, leur doc, leurs bancs de test
    └── cahiers/                  ← cahiers d'expérience (voir §V) — append-only
```

**Sort de `atelier/projets/`** : le dossier devient `rd/` par migration fiche à
fiche ; chaque fiche migrée garde son slug, l'ancienne reçoit `deprecated` avec
pointeur (Cmd 10 — jamais de suppression sèche). `album-personnel` part vers
`label/` s'il y a lieu, ou reste en `rd/` s'il est d'ordre technique : à
trancher fiche par fiche au moment de la migration, pas en bloc (§VIII.3).

## V. La discipline de laboratoire (le cœur de la proposition)

Un laboratoire n'est pas un dossier : c'est un **protocole de preuve**. Le dépôt
en possède déjà tous les organes pour le doctrinal ; il s'agit de les
transposer au technique, terme à terme :

| Organe doctrinal existant | Transposé au laboratoire |
|---|---|
| Bloc 🔍 Discernement (hypothèse → généalogie → examen → conclusion humaine) | Bloc 🧪 **Expérience** (hypothèse → montage → résultat brut → verdict humain) |
| `to-source` (fait non vérifié) | `non-reproduit` (résultat obtenu une fois, jamais reproduit) |
| Levée du `to-source` par vérification primaire humaine | Levée du `non-reproduit` par **reproduction indépendante** (autre session, autre moteur, ou script) |
| Annales append-only | **Cahier d'expérience** append-only, un par chantier |
| Statut `speculatif` → définitif | `exploratoire` → `reproduit` → `adopte` (ou `abandonne`, jamais effacé) |

### Le bloc 🧪 Expérience (normalisé)

> 🧪 **Expérience**
> **Hypothèse** (datée) : ce qu'on cherche à établir, falsifiable.
> **Montage** : matériel/logiciel exact, versions, paramètres — reproductible
> par un tiers sans rien deviner.
> **Résultat brut** : mesures et sorties telles quelles, sans interprétation
> (miroir du §VIII.2 : rapport du résultat BRUT).
> **Interprétation** : séparée du résultat, flaguée comme telle.
> **Statut** : exploratoire | reproduit | adopte | abandonne.
> **Verdict** : adopté par Sidy — jamais auto-décrété (Cmd 12-13).

### Les trois règles du laboratoire

1. **Rien n'est établi tant que ce n'est pas reproduit** — le pendant technique
   de l'Art. 1 sashimono : un résultat unique est une pièce collée.
2. **Le résultat brut précède toujours l'interprétation** — extension directe
   du §VIII.2 (fiabilité d'action ≠ fiabilité narrative) aux expériences.
3. **Un échec se consigne comme un succès** — le cahier garde les montages qui
   n'ont pas marché ; c'est la moitié de la valeur d'un laboratoire, et le
   miroir du module 10 du framework d'étude de cas (les crises comme données
   de premier ordre).

## VI. Impacts sur le protocole (amendements à viser)

1. **§II** — arborescence `atelier/` mise à jour (§IV ci-dessus).
2. **§V.a** — Sceau atelier : `type:` s'étend à
   `materiel | manuel | entretien | etude-de-cas | experience | infrastructure | outillage` ;
   champ optionnel `statut_experience:` pour `rd/`.
3. **§VI** — hiérarchie d'étanchéité **inchangée**. `rd/` hérite du régime de
   `atelier/projets/` qu'il remplace : lien vers `doctrinal/` en sens unique,
   signalé (l'Instrument en dépend déjà). `meta/projet-unifie/` garde ce qui
   est **sensible** (motifs, credentials, prompts d'agents) ; `rd/infrastructure/`
   reçoit ce qui est **publiable dans le dépôt** (architecture générique, bancs,
   mesures). La frontière meta/rd suit la règle existante : jamais de fait
   personnel dans une page neutre.
4. **Clôture de la question v3** : le champ `liens_atelier` du Sceau
   `hermeneutique/` (§V.d) s'élargit de `atelier/etudes-de-cas/` à
   **`atelier/etudes-de-cas/ et atelier/rd/`** — toujours sens unique. La fiche
   Mother Base pourra alors pointer sa transposition vers
   `atelier/rd/infrastructure/` quand la fiche cible existera.
5. **Cmd 9** — `atelier/` reçoit ses annales propres (il n'en a pas ; les
   opérations atelier sont aujourd'hui consignées dans celles du doctrinal).

## VII. Trajectoire vers le laboratoire (suggérée, par phases réversibles)

**Phase 1 — le lieu** : ouvrir `rd/`, migrer `projets/`, ouvrir les annales
atelier. Aucune règle nouvelle en vigueur au-delà du Sceau étendu.
**Phase 2 — la discipline** : premier cahier d'expérience sur un chantier réel
(candidat naturel : le banc de comparaison des moteurs, §VIII.10, qui EST déjà
une expérience au sens du bloc 🧪 — double exécution comparée, verdict au
`compare`).
**Phase 3 — les agents** : un agent Hermes « Laborantin » (13ᵉ rôle) dont la
sortie entre dans le Rapport du matin : expériences en cours, résultats en
attente de reproduction, verdicts en attente. Signalement pur, §VIII inchangé.
**Phase 4 — l'ouverture éventuelle** : si un jour des travaux du laboratoire
sont publiés (le site du label en a déjà le canal), le flux existant s'applique
tel quel : manifeste déterministe, préversion, porte humaine. Rien à inventer.

Chaque phase est indépendamment réversible ; aucune n'engage la suivante.

## VIII. Ce que la proposition ne fait pas

- Elle ne touche **ni au doctrinal, ni au label, ni aux transmissions**.
- Elle ne déplace pas `meta/projet-unifie/` : le sensible reste en meta.
- Elle ne crée pas de circuit : **cinq circuits, inchangés**.
- Elle n'exécute rien : migration et amendements attendent le visa, puis se
  font fiche par fiche côté intégration, jamais en bloc.

## IX. À l'arbitrage de Sidy

1. Option C confirmée (pôle interne) — ou préférence pour A/B malgré l'analyse ?
2. Périmètre de `rd/audio/` : la frontière générique/par-morceau avec
   `label/musique/ingenierie/` convient-elle ?
3. Le nom du pôle : `rd/` (bref, ASCII) — ou `recherche/` en toutes lettres ?
4. La phase 2 : le banc des moteurs comme premier cahier — ou un autre chantier ?
