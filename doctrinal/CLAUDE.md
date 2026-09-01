بسم الله الرحمن الرحيم

# CLAUDE.md — Protocole local : circuit `doctrinal/`

> **Statut : méthode à l'essai** (éclatement expérimental du 2026-08-12, verdict
> Sidy). Ce fichier porte la lettre complète des règles **propres** au circuit
> `doctrinal/` — Sceau, nomenclature, actions d'exécution spécifiques. Les règles
> **transversales** (étanchéité inter-circuits, discipline des sources, double
> contrôle sashimono/Gizeh, commandements absolus, supervision des agents) restent
> dans le `CLAUDE.md` racine, **toujours chargé** quel que soit le dossier de
> travail — ce fichier ne s'y substitue pas, il le complète. En cas de doute ou de
> silence de ce fichier sur un point, le `CLAUDE.md` racine fait foi. Version
> pré-éclatement intégrale : `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md`.

-----

## Nomenclature

`doctrinal/traditions/<slug>.md`, `symboles/<slug>.md`, `autorites/<slug>.md`,
`deviations/<slug>.md`, `sources/<slug>.md` ; `etudes/YYYY-MM-DD_titre-court.md` et
`discernement/YYYY-MM-DD_titre-court.md` (préfixe daté obligatoire).

Fichiers en minuscules, ASCII, sans accents, tirets `-`. Titres internes (H1)
respectent l'orthographe française. **Une page = un sujet** (Cmd 4).

## Le Sceau Recteur (frontmatter doctrinal)

Chaque page de `doctrinal/` s'ouvre impérativement par ce cartouche :

```yaml
---
title: "Titre exact de la page"
type: doctrine | tradition | symbole | autorite | deviation | etude | source | discernement
status: traditionnel | academique | profane | contre-traditionnel | speculatif
tradition_cadre: "islam"   # ou "hindouisme", "hellenisme", "universel", "none"
tags: [metaphysique, cosmologie, symbolisme]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["[[slug-source]]"]   # liste de "[[slug]]" — traçabilité machine-lisible
sources_count: 1               # entier = longueur de la liste ci-dessus
cross_links: ["[[autre-slug]]"]
---
```

- `sources` et `cross_links` : listes YAML de chaînes entre guillemets droits,
  chaque wikilink complet (`"[[slug]]"`). Liste vide = `[]`. JAMAIS `[[a], [b]]` ni
  `[a, b]`.
- Fait sans source → `sources: ["to-source"]` + signalement (levée du marqueur :
  discipline des sources, CLAUDE.md racine §VII).

### Définition des Statuts (`status`)

1. `traditionnel` : écrits sacrés ou maîtres spirituels authentiques. (Autorité suprême)
2. `academique` : travaux d'érudition universitaire. (Utiles pour les faits, aveugles pour l'esprit)
3. `profane` : philosophie moderne, science matérialiste. (Symptômes de la crise moderne)
4. `contre-traditionnel` : occultisme, spiritisme, théosophisme, Nouvel Âge. (Sévérité et discernement)
5. `speculatif` : hypothèse métaphysique personnelle de l'utilisateur, en attente de
   validation par une autorité textuelle ou par l'examen traditionnel. Statut
   transitoire — doit évoluer vers un statut définitif à la clôture du discernement.

> **Précision pour `type: deviation`** (amendement du 2026-07-28, verdict Sidy) : le
> `status` qualifie la **nature du contenu reproduit**, non le sujet traité. Une
> fiche `deviation` qui reproduit l'analyse d'une **autorité traditionnelle**
> portant sur un phénomène contre-traditionnel reçoit `status: traditionnel` —
> c'est la doctrine reçue qui est en jeu, non le phénomène qu'elle décrit. Une
> fiche `deviation` qui **expose pour elle-même** une matière contre-traditionnelle,
> sans qu'une autorité traditionnelle sourcée en fasse l'objet d'un jugement, reçoit
> `status: contre-traditionnel`. Exemples : [[doctrinal/deviations/contre-initiation]]
> (Guénon analyse) = `traditionnel` ; [[doctrinal/symboles/archeometre]] (l'objet
> lui-même est exposé, reçu et discuté comme tel) = `contre-traditionnel`.

## Règles de liens propres au circuit

- Étanchéité inversée : une page orthodoxe ne pointe jamais vers un `discernement`
  non tranché (exception : lien défensif/généalogique signalé).
- `doctrinal/` → `hermeneutique/` : **jamais**. Aucune fiche doctrinale, y compris
  de discernement, ne pointe vers ce circuit.
- `atelier/projets/` et `atelier/rd/` PEUVENT pointer vers `doctrinal/` en sens
  unique, tout lien signalé — l'inverse est interdit.
- `label/` → `doctrinal/` autorisé (œuvre s'inspirant d'un principe, ou acte de
  structure réglant sa conduite sur un principe), signalé, marqué suggéré (🔍) tant
  qu'un discernement afférent n'est pas tranché.
- Hiérarchie complète de l'étanchéité entre les cinq circuits : CLAUDE.md racine §VI.

## Actions d'exécution propres au circuit

### Action : EXAMEN DE DISCERNEMENT (spéculations personnelles)

Lorsqu'une page `type: discernement` est créée ou enrichie, insérer/maintenir
impérativement ce bloc normalisé :

> 🔍 **Discernement — Spéculation Personnelle**
> **Statut** : en cours | validée | invalidée
> **Hypothèse initiale** (datée, reformulée fidèlement) : …
> **Généalogie des idées** :
>   - *Filiation orthodoxe possible* : [[doctrinal/symboles-ou-autorites/slug]] — nature du rapprochement.
>   - *Parenté hétérodoxe possible* : [[doctrinal/deviations/slug]] — nature du rapprochement.
> **Examen formel** (cohérence logique/terminologique — jamais le principe) : …
> **Conclusion** : attribuée par l'utilisateur ou par une autorité textuelle citée, jamais auto-décrétée par l'IA.
> **Lectures suggérées** (champ ajouté 2026-06-28) : 1 à 3 lectures réellement rattachées à la généalogie de *cette* fiche (pages du wiki, `meta/bibliotheque-physique.md`, ou candidates à `raw/`).

Rappels : Commandement 12 (*upakarana*) — l'IA documente la généalogie et signale
les tensions formelles ; elle ne tranche jamais la validité métaphysique. Une
convergence multiple (« double ancrage ») est un **signal de vigilance** appelant
l'arbitrage humain, jamais une porte automatique vers l'inscription.

### Action : EXAMEN D'USÛL (sciences traditionnelles formelles — remplace l'EXAMEN DE FIQH)

> **Amendement du 2026-08-27** (verdict Sidy, exécution de
> `meta/projet-unifie/propositions/proposition-pole-usul-2026-08-27.md`, laquelle supersède
> `meta/projet-unifie/propositions/proposition-pole-fiqh-2026-07-06.md`, désormais
> `deprecated` avec pointeur). Le pôle Fiqh validé le 2026-07-06 devient la
> **branche `fiqh`** d'un pôle **Usûl** élargi (racines/méthodologie des
> sciences traditionnelles), qui accueille aussi les branches `mantiq`
> (logique formelle) et `mustalah-hadith` (critique de chaîne et de texte).
> Rien du fiqh déjà instruit n'est perdu : le bloc ⚖️ et ses règles restent
> utilisables tels quels comme cas particulier `branche: fiqh` du bloc
> générique ci-dessous.

Toute question du pôle Usûl instruite (règle V.c.6 du protocole label, pour la
branche fiqh) = une étude datée `doctrinal/etudes/YYYY-MM-DD_<question>.md`,
**générale et neutre** (jamais de mention du cas d'application, qui vit en
`label/` avec lien à sens unique), portant ce bloc normalisé :

> ⚖️ **Statut d'Usûl**
> **Branche** : fiqh | mantiq | mustalah-hadith.
> **Question** : formulée en termes généraux.
> **École consultée** *(branche fiqh uniquement)* : mālikite (défaut) |
> shāfiʿite | ḥanafite | ḥanbalite. Sans objet pour `mantiq` et
> `mustalah-hadith` : ces deux branches n'ont pas de logique de préséance de
> *madhhab* — la règle mālikite est **propre au fiqh**, non généralisée
> mécaniquement (point ouvert de la proposition du 2026-08-27, à arbitrer par
> Sidy branche par branche à mesure qu'elles s'instruisent).
> **Position(s) sourcée(s)** : texte, auteur, référence — `to-source` si non vérifié.
> **Recours subsidiaire** *(branche fiqh uniquement)* : école + justification
> (« à défaut de ressource malikite sur ce point ») — jamais de talfīq.
> **Divergences notables** : signalées sans être fondues (🌐 si inter-écoles ou
> inter-positions).
> **Verdict** : adopté par Sidy (taqlīd documenté d'une position établie, ou
> arbitrage équivalent pour `mantiq`/`mustalah-hadith`) | confirmé par autorité
> textuelle citée | renvoyé au savant qualifié — jamais décrété par la machine.
> **Date du verdict** : YYYY-MM-DD.

Rappel (Cmd 12) : la machine **compile, source et structure** ; elle n'émet jamais
d'avis juridique religieux ni de jugement de validité logique/critique de hadith
qui vaudrait verdict. Le « trancher » humain est un **arbitrage d'adoption**
parmi des positions établies ; pour les cas nouveaux ou sans texte, la fiche
prépare la formulation de la question (istiftāʾ pour le fiqh, question ouverte
pour les autres branches) et reste ouverte. Répartition agents 04 (instruction) /
10 (harmonisation) reconduite pour les trois branches, discipline `to-source`
inchangée (`atelier/rd/bibliotheque/catalogue-bibliotheque.md`). Invoqué depuis
`label/` pour l'ancrage éthique de la structure (contrats, dons, prix), branche
fiqh : voir `label/CLAUDE.md`.

### Action : RESTAURATION (normalisation de l'existant)

Les pages antérieures à la Restauration portent l'ancien frontmatter (`domain:`,
`type: entity|concept`). Sur demande, les normaliser SANS toucher au corps :
`domain` → `tradition_cadre`, `entity` → `autorite`, `concept` → `symbole`, ajout
de `status`. Chaque passe est consignée dans les annales (`doctrinal/annales.md`).

-----

## Exploitation du graphe lors de l'intégration (signal d'orphelins)

Le dépôt dispose d'un graphe de maillage déjà produit :
`graphe-cartographie.json` (artefact dérivé, régénéré par
`atelier/rd/outillage/graphe/generer-cartographie.py`). Ce graphe est la **source de vérité
du maillage** — il n'y a pas lieu de créer un outil parallèle.

### Procédure à l'intégration d'une nouvelle fiche doctrinale

1. **Consulter le graphe** : lire `graphe-cartographie.json` et compter les
   liens entrants de la fiche intégrée (filtrer `edges` sur `target` = slug
   de la fiche). Si le graphe est stale (dernière génération antérieure au
   dernier commit doctrinal), le régénérer d'abord par
   `python3 atelier/rd/outillage/graphe/generer-cartographie.py`.
2. **Si zéro lien entrant** : la fiche est orpheline du graphe. L'agent
   peut **proposer** des liens (filiations orthodoxes/hétérodoxes, comme
   dans le bloc 🔍 des discernements — cf.
   [[doctrinal/discernement/2026-06-20_matrices-artificielles-barzakh]]),
   mais **ne les inscrit pas** dans le frontmatter.
3. **Verdict** : Sidy tranche (Cmd 12). Les `cross_links` validés sont
   ajoutés dans un second temps, puis le graphe est régénéré.

### Ce que la procédure ne fait pas

- Aucun lien forcé (la machine compile, ne tranche pas — Cmd 12).
- Aucune création d'outil supplémentaire (le graphe suffit).
- Aucun jugement sur la pertinence d'un lien (la qualification est un
   verdict humain).
