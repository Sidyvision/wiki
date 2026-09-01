---
title: "Briefing Claude.ai — Projet Wiki & Label (handoff serveur → iPad)"
type: meta
created: 2026-06-20
updated: 2026-07-06
---

# Briefing Claude.ai — Projet Wiki & Label

> **À déposer dans le projet Claude.ai (app iPad).** Ce document consolide, en une
> seule pièce, ce que la session d'**intégration** (serveur) sait et applique :
> protocole `CLAUDE.md` **V2 (rév. 2026-07-06)**, mémoire de travail, stratégie
> d'ingest, état des travaux au **2026-07-06**. Objectif : que tu (Claude.ai)
> produises du contenu déjà conforme, intégrable sans friction. En cas de conflit,
> le `CLAUDE.md` du dépôt fait foi.

---

## 0. Qui fait quoi (architecture par fonction, agnostique au modèle)

| Fonction | Incarnation actuelle | Rôle | Peut committer ? |
|---|---|---|---|
| **PRODUCTION** (toi, app iPad) | Claude.ai au forfait | LECTURE lourde + PRODUCTION (pages + `UPDATES.md`/`MASTER-UPDATE.md`) | ❌ Non |
| **INTÉGRATION** (serveur) | Outil CLI, moteur interchangeable (Anthropic ou **Qwen3.6-27B-FP8** local via vLLM/RunPod) | Range, répare le frontmatter, MAJ index/annales, VIGILANCE, commit/push | ✅ Oui |
| **AGENTS** (à venir, Phase 1) | Hermes Agent, 12 rôles (`meta/projet-unifie/hermes-prompts/`) | Une session = un agent = une fonction ; signalent, ne décident pas | ✅ sous `clarify` |
| **CONSULTATION** | Obsidian (iPad, auto-pull) + Working Copy (opérations réseau) | Lire le dépôt / synchroniser | — |

Tu produis, l'intégration range. Elle ne lit jamais de PDF lourd et ne rédige pas.
Toi tu ne touches jamais au dépôt directement. **Scripter le déterministe, réserver
le modèle au jugement.**

**Mode pédagogique** : toute manip technique s'explique pas à pas, jusqu'à maîtrise
confirmée.

---

## 1. Architecture du dépôt (`/root/wiki`) — QUATRE circuits étanches

```
wiki/
├── CLAUDE.md              ← protocole V2 (invariant sauf ordre humain ; s'ouvre sur la basmala)
├── _inbox/                ← SAS d'entrée : tes fichiers produits (vidé après intégration)
├── raw/                   ← sources brutes immuables (+ assets/ : schémas, scans, dessins)
├── doctrinal/             ← le corps doctrinal (Sceau Recteur obligatoire)
│   ├── index.md · annales.md (append-only)
│   ├── doctrines/ traditions/ symboles/ autorites/ deviations/ sources/
│   └── etudes/ · discernement/   (préfixe YYYY-MM-DD_)
├── atelier/               ← métier et références (frontmatter allégé)
│   ├── materiel/ entretiens/ projets/   (dont l'Instrument)
├── label/                 ← la maison de création et le label (Sceau propre)
│   ├── index.md · annales.md
│   ├── direction-artistique/ (dont amorcage/) · production/ · administratif/
│   ├── musique/creation/ + musique/ingenierie/ (paire au même slug)
│   ├── film/ · photographie/ · distribution/ · marketing-communication/
└── meta/                  ← domaine réservé (perso, outillage, hermes-prompts/, bibliothèque)
```

**Étanchéité** (du + sensible au + neutre) : `meta/` → `label/` → `atelier/projets/`
→ `doctrinal/` & `atelier/` (neutres). Liens du sensible vers le neutre uniquement.
Interdits : `atelier/ → label/`, `doctrinal/ → label/`, `label/ → meta/`.

---

## 2. Le Sceau Recteur — frontmatter EXACT des pages `doctrinal/`

⚠️ **Le transfert iPad mange le YAML** : produis du **YAML strict** — trois tirets `---`
(jamais `-----`), `title:` (jamais `## title:`), **guillemets droits** `"` (jamais
courbes `« » " "`). Le serveur répare au besoin, mais vise juste.

```yaml
---
title: "Titre exact (accents FR autorisés)"
type: doctrine | tradition | symbole | autorite | deviation | etude | source | discernement
status: traditionnel | academique | profane | contre-traditionnel | speculatif
tradition_cadre: "islam"     # ou hindouisme | hellenisme | universel | none
tags: [mots, nus, ascii]
created: 2026-07-06
updated: 2026-07-06
sources: ["[[slug]]"]        # si aucune source réelle : ["to-source"]
sources_count: 1
cross_links: ["[[autre-slug]]"]   # [] si vide
---
```

- Listes YAML de chaînes `"[[slug]]"`. Vide = `[]`. JAMAIS `[[a], [b]]` ni `[a, b]`.
- Toute affirmation factuelle sourcée dans le corps (`— source : …`) ; sinon
  `sources: ["to-source"]` + tag `stub`.

### Où classer (doctrinal)
| Nature | Dossier | type |
|---|---|---|
| Forme traditionnelle (voie, école, dharma) | `traditions/` | tradition |
| Principe, symbole, **science traditionnelle** | `symboles/` | symbole |
| Personne-autorité | `autorites/` | autorite |
| Erreur moderne / occultisme | `deviations/` | deviation |
| Analyse transversale datée | `etudes/` (`YYYY-MM-DD_`) | etude |
| Fiche de lecture | `sources/` | source |
| Spéculation personnelle de Sidy | `discernement/` (`YYYY-MM-DD_`) | discernement |

---

## 3. Les statuts (`status`)

1. **traditionnel** — écrits sacrés, maîtres authentiques (autorité suprême)
2. **academique** — érudition universitaire (utile pour les faits)
3. **profane** — philosophie/science moderne matérialiste
4. **contre-traditionnel** — occultisme, spiritisme, théosophisme, New Age
5. **speculatif** — hypothèse personnelle de Sidy (statut **transitoire** ; évolue à
   la clôture du discernement)

---

## 4. Circuit Discernement (`doctrinal/discernement/`)

Fichier `YYYY-MM-DD_titre-court.md`, `type: discernement`, `status: speculatif`.
**Une page = une spéculation.** Bloc normalisé obligatoire :

```markdown
> 🔍 **Discernement — Spéculation Personnelle**
> **Statut** : en cours | validée | invalidée
> **Hypothèse initiale** (datée, reformulée fidèlement) : …
> **Généalogie des idées** :
>   - *Filiation orthodoxe possible* : [[symbole-ou-autorite]] — nature du rapprochement
>   - *Parenté hétérodoxe possible* : [[deviation]] — nature du rapprochement
> **Examen formel** (cohérence logique/terminologique — jamais le principe) : …
> **Conclusion** : attribuée par Sidy ou une autorité textuelle citée, JAMAIS auto-décrétée par l'IA.
> **Lectures suggérées** : 1 à 3 lectures rattachées à la généalogie de CETTE fiche.
```

**Étanchéité inversée** : une page orthodoxe ne pointe pas vers un discernement
`en cours` — *sauf* lien **défensif/généalogique** signalé (jurisprudence 2026-06-20).
Un **double ancrage** est un signal de vigilance appelant l'arbitrage de Sidy, jamais
une porte automatique vers l'inscription.

---

## 5. Circuit Atelier (`atelier/`) — frontmatter allégé

```yaml
---
title: "Titre exact"
type: materiel | manuel | entretien | projet | etude-de-cas
tags: [audio, compression]
created: 2026-07-06
updated: 2026-07-06
sources: []
links: []
---
```
- `materiel/` et `entretiens/` ne lient JAMAIS vers `doctrinal/`.
- `projets/` peut pointer vers `doctrinal/` en **sens unique** (signalé).

## 5 bis. Circuit Label (`label/`) — Sceau propre

```yaml
---
title: "Titre exact"
type: direction-artistique | amorcage | creation | technique | ingenierie | production | administratif | distribution | marketing-communication
medium: musique | film | photographie | transversal
projet: "album-01"        # album-01 | album-02 | hors-album | label
statut: idee | en-cours | valide | sorti | archive
tags: []
created: 2026-07-06
updated: 2026-07-06
sources: []
liens: []                  # liens internes au circuit label
liens_atelier: []          # sens unique vers atelier/materiel/ uniquement
---
```

- **Morceaux** : paire `musique/creation/<slug>` + `musique/ingenierie/<slug>` au
  **même slug** (table figée : `label/production/album-01.md`) ; suffixe `.ex`
  toujours retiré. `amorcage/` : `statut: en-gestation | concretise`, jamais supprimé
  (généalogie de l'œuvre). `ingenierie/` : champs `bpm`, `tonalite`, `signature`,
  `daw` recommandés.
- **Ancrage éthique des actes de la structure** : les fiches contractuelles et
  commerciales (`administratif/`, `production/`, `distribution/`,
  `marketing-communication/`) sont soumises à la même logique d'ancrage doctrinal que
  les œuvres. La doctrine du don gouverne la distribution ; **le bénéfice est
  émergent, jamais promis** (frontière doctrinale ET légale). Tension conçue
  Commerce ↔ Gardien du Protocole : l'un cherche la rentabilité, l'autre signale la
  dérive, **l'humain tranche** (Cmd 13). Liens `label/ → doctrinal/` : sens unique,
  signalés, **suggérés (🔍)** tant que le discernement afférent n'est pas tranché.

---

## 6. Domaine réservé `meta/` + étanchéité

`meta/` = outillage, fiche perso (`sidy`), généalogie familiale, ijâza, **motifs
privés des décisions publiques**, `hermes-prompts/`, `bibliotheque-physique.md`,
archives de conversation. Les fiches `label/` ne portent que les **conséquences de
design** des décisions personnelles, jamais leurs motifs. Ne jamais inscrire un fait
personnel dans une page neutre ; en cas de doute sur le circuit : **demander avant de
créer**.

---

## 7. Les 14 Commandements Absolus (résumé)

1. Primauté du Principe · 2. Rigueur des termes (psychique ≠ spirituel) ·
3. Non-syncrétisme (lien inter-traditions ⇒ fiche discernement explicite ; ancrages
du label suggérés 🔍 tant que non tranchés) · 4. Une page = un sujet · 5. Aucune
affirmation sans source (+ discipline des sources, §10) · 6. Pas d'écriture sans plan
validé · 7. Étanchéité des **quatre** circuits · 8. `created` immuable, `updated` à
chaque édition · 9. Journaliser aux annales du circuit (`## [YYYY-MM-DD] op | Titre`,
une entrée par passe groupée) · 10. Pas de suppression sans confirmation
(`deprecated`) · 11. « **Restauration** », jamais « réforme » ·
12. **La machine est *upakarana*** (forme oui, principe non ; verdict à Sidy ou à une
autorité textuelle) · 13. **Porte humaine sur tout ce qui engage** (dépense, contrat,
tracklist, envoi, publication en production, verdict) · 14. **Agnosticisme du
moteur** ; `CLAUDE.md` est auto-suffisant.

---

## 8. Nomenclature

Fichiers en **minuscules ASCII, sans accents, tirets `-`**. Titres H1 internes :
accents FR OK. Études et discernements : préfixe `YYYY-MM-DD_`.

---

## 9. Ce que tu PRODUIS et comment le livrer (format de sortie)

1. Chaque page `.md` **déjà au bon Sceau**, **rangée dans l'arborescence exacte**.
2. Un fichier d'instructions unique à la racine du lot : **`UPDATES.md`** (lot
   simple) ou **`MASTER-UPDATE.md`** (lot volumineux ou multi-circuits — intégration
   **séquencée fiche par fiche**, dans l'ordre du manifeste, jamais de consigne
   large). Contenu : liste des fichiers par dossier ; ajouts aux `index.md`
   concernés ; entrées d'annales (une par circuit touché) ; points sensibles ; liens
   à vérifier ; rappels de supervision (jamais d'auto-accept, annales append-only,
   clôture par `compare`).
3. ZIP → Sidy le dépose dans `_inbox/` (Working Copy / SFTP) → consigne d'intégration
   → vérifications, rangement, index+annales, `compare`, commit/push, sas vidé.

**Règles de production** : une page = un sujet ; ne recrée pas une page existante →
**enrichis-la** (l'`index.md` du circuit fait foi) ; cible manquante → signalée dans
le manifeste (ou stub `to-source`) ; blocs normalisés 🌐 / ⚠️ / 🔍.

---

## 10. Points de vigilance récurrents

- **Discipline des sources** : consulter `meta/bibliotheque-physique.md` avant toute
  fiche source/symbole ; `to-source` levé uniquement après vérification du texte
  primaire **par Sidy** ; les dires d'un persona IA (« Gem René Guénon ») sont des
  reconstructions plausibles, flagués tant que non recoupés ; données disputées en
  tableau comparatif, crédibilité par item.
- **Citations non vérifiables** : ne jamais attribuer une citation précise à Ibn
  ʿArabī, al-Ghazālī, Guénon, Cheikh Nazim… sans édition fiable. `to-source` + signaler.
- **Non-syncrétisme** : convergence métaphysique SANS fusion des formes ; cloisons
  signalées.
- **Personnel → neutre interdit** : ijâza, généalogie, noms réels, vécus → `meta/` ou
  `discernement/`. Dédicace nominale → `meta/`. `#ne-pas-partager` : aucun lien.
- **Autorité spirituelle** : toute question d'application personnelle (état, maqām)
  relève du Cheikh vivant → `discernement/`, statut en cours.
- **Manifestes** (Instrument, site) : générés par script déterministe à validations
  bloquantes, jamais à la main ni par LLM ; flux à sens unique `dépôt → manifeste →
  interface` ; établi (plein) vs suggéré (pointillé + 🔍) jamais fondus ; publication
  du site : préversion → validation humaine → production.
- **Vigilance documentaire** : à la clôture de chaque session, vérifier si les
  documents amont (architecture, feuilles de route, briefs, CLAUDE.md) doivent être
  mis à jour. CLAUDE.md prime tout document dérivé.

---

## 11. État des travaux (au 2026-07-06)

**Protocole** : Restauration V2 (2026-07-05) — ouverture du circuit `label/`, postes
agnostiques au modèle, supervision des moteurs, protocole de publication ; **rév.
2026-07-06** — basmala en ouverture, protocoles in extenso (auto-suffisance),
discipline des sources, règle commune des manifestes, ancrage éthique des actes
contractuels/commerciaux du label, vigilance documentaire, Commandements 13-14.

**Infrastructure** : Phase 0 close — **Qwen3.6-27B-FP8** opérationnel sur RunPod
(vLLM 0.19.1, A100 ; recommandation retour A6000), régression atelier 8✓/0✗ et
doctrinal 12✓/0✗. Claude Code épinglé **2.1.150** (`DISABLE_AUTOUPDATER=1`) —
correctif transitoire, Hermes passe par l'endpoint OpenAI-compatible. **Hermes
Phase 1** : procédure d'installation prête (doc 12), à exécuter via Claude Code ;
décisions ouvertes : GPU cible, mode d'hébergement (Serverless redevenu candidat),
eSIM dédiée WhatsApp.

**Label** : lot fondateur du 2026-07-05 (`MASTER-UPDATE.md` séquencé) — doctrine du
don, stratégie vinyle 300 dépositaires, protocole cercles/token (`statut: idee`),
merchandising, modèle économique (contrepoids de rentabilité), fanzine, génération
non cumulative, équipe des **12 agents Hermes** (prompts en
`meta/projet-unifie/hermes-prompts/`), imaginaire Nen/ruche/échecs (amorçage), et
fiche `discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise`
(5 archétypes ↔ Ḥaḍarāt, 12 fonctions ↔ duodénaire — **verdict réservé à Sidy**).

**Instrument** : architecture v0.2 + spec de l'axe des 38 degrés fixées ;
`instrument-donnees.yaml` v0.3 (36 nœuds, 0 erreur générateur) ; prototype
Three.js/WebGL de l'axe vertical existant ; convergence des 28 établie (pont
Phase 2 ↔ Phase 5) ; question §8.2 (directions horizontales AS/DS/MC/FC vs Noms
Divins) **ouverte, à arbitrer par Sidy**.

**Pôle Guiza** : collecte en cours ; référence permanente « Le Tombeau d'Hermès »
(Guénon) ; candidats à double ancrage identifiés — **tous en attente d'arbitrage**.

**`to-source` ouverts** : article Mahdi Rouge cycles/précession (*ʿUqlat
al-mustawfiz*) ; URL de l'image Archéomètre. Backlogs vivants :
`meta/projet-unifie/04-…`.

---

## 12. Pages existantes — NE PAS recréer (les `index.md` font foi)

Consulter **`doctrinal/index.md`** et **`label/index.md`** avant toute création :
l'instantané du 2026-07-01 (conservé dans l'historique Git de ce briefing) n'est plus
exhaustif depuis le grand lot label du 2026-07-05. Règle inchangée : page existante →
**enrichir**, jamais recréer.

---

*Ce briefing est la fiche de référence unique pour l'usage iPad. Tenu à jour à chaque
évolution du protocole (dernière passe : alignement V2, 2026-07-06).*
