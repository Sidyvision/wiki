---
title: "Briefing Claude.ai — Projet Wiki (handoff serveur → iPad)"
type: meta
created: 2026-06-20
updated: 2026-06-20
---

# Briefing Claude.ai — Projet Wiki

> **À déposer dans le projet Claude.ai (app iPad).** Ce document consolide, en une
> seule pièce, ce que la session **Claude Code** (serveur Hetzner) sait et applique :
> protocole `CLAUDE.md`, mémoire de travail, stratégie d'ingest, état des travaux au
> **2026-06-20**. Objectif : que tu (Claude.ai) produises du contenu déjà conforme,
> intégrable sans friction. En cas de conflit, le `CLAUDE.md` du dépôt fait foi.

---

## 0. Qui fait quoi (règle économique impérative)

| Poste | Rôle | Peut committer ? |
|---|---|---|
| **Claude.ai** (toi, app iPad) | **LECTURE lourde** (PDF, longs textes) + **PRODUCTION** du contenu (pages + fichier d'instructions) | ❌ Non |
| **Claude Code** (serveur, via Termius) | **INTÉGRATION** : range, répare le frontmatter, met à jour index/annales, VIGILANCE, commit/push | ✅ Oui |
| **Obsidian** (iPad) | Consultation (auto-pull du dépôt GitHub) | — |

Tu produis, le serveur range. Le serveur ne lit jamais de PDF lourd et ne rédige pas de
doctrine (coût API au token). Toi tu ne touches jamais au dépôt directement.

**Mode pédagogique** : Sidy apprend Git/SSH/YAML ; toute manip technique s'explique pas à pas.

---

## 1. Architecture du dépôt (`/root/wiki`)

```
wiki/
├── CLAUDE.md              ← protocole (invariant)
├── raw/                   ← sources brutes immuables (PDF) — gitignoré
├── _inbox/                ← SAS d'entrée : tu déposes ici tes fichiers produits
├── doctrinal/             ← le corps doctrinal (Sceau Recteur obligatoire)
│   ├── index.md           ← Le Catalogue Universel (liste FAISANT FOI des pages)
│   ├── annales.md         ← journal chronologique (append-only)
│   ├── doctrines/ traditions/ symboles/ autorites/ deviations/ etudes/ sources/
│   └── discernement/      ← spéculations personnelles datées (NOUVEAU circuit)
├── atelier/               ← métier audio + création (hors Sceau Recteur)
│   ├── materiel/ entretiens/ projets/
└── meta/                  ← domaine réservé : outils, fiches perso, généalogie, ijâza
```

**Trois circuits étanches** : `doctrinal/` (la doctrine) · `atelier/` (le métier/art) · `meta/`
(le personnel). Voir §6 pour les règles de liens.

---

## 2. Le Sceau Recteur — frontmatter EXACT des pages `doctrinal/`

⚠️ **Le transfert iPad mange le YAML** : produis du **YAML strict** — trois tirets `---`
(jamais `-----`), `title:` (jamais `## title:`), **guillemets droits** `"` (jamais courbes
`« » " "`). Le serveur répare au besoin, mais vise juste.

```yaml
---
title: "Titre exact (accents FR autorisés)"
type: doctrine | tradition | symbole | autorite | deviation | etude | source | discernement
status: traditionnel | academique | profane | contre-traditionnel | speculatif
tradition_cadre: "islam"     # ou hindouisme | hellenisme | universel | none
tags: [mots, nus, ascii]
created: 2026-06-20
updated: 2026-06-20
sources: ["[[slug]]"]        # liste de wikilinks ; si aucune source réelle : ["to-source"]
sources_count: 1             # entier = longueur de la liste sources
cross_links: ["[[autre-slug]]"]   # [] si vide
---
```

- `sources` / `cross_links` : listes YAML de chaînes `"[[slug]]"`. Liste vide = `[]`.
  JAMAIS `[[a], [b]]` ni `[a, b]`.
- Toute affirmation factuelle doit être sourcée dans le corps (`— source : …`) ; sinon
  `sources: ["to-source"]` + tag `stub`.

### Où classer
| Nature | Dossier | type |
|---|---|---|
| Forme traditionnelle (voie, école, dharma) | `traditions/` | tradition |
| Principe, symbole, **science traditionnelle** (logique, ʿilm al-ḥurūf, oniromancie, firāsa…) | `symboles/` | symbole |
| Personne-autorité (maître, érudit orthodoxe) | `autorites/` | autorite |
| Erreur moderne / occultisme / pseudo-science | `deviations/` | deviation |
| Analyse transversale datée | `etudes/` (préfixe `YYYY-MM-DD_`) | etude |
| Fiche de lecture (le document lui-même) | `sources/` | source |
| **Spéculation métaphysique personnelle de Sidy** | `discernement/` (préfixe `YYYY-MM-DD_`) | discernement |

---

## 3. Les statuts (`status`)

1. **traditionnel** — écrits sacrés, maîtres authentiques (autorité suprême)
2. **academique** — érudition universitaire (utile pour les faits)
3. **profane** — philosophie/science moderne matérialiste
4. **contre-traditionnel** — occultisme, spiritisme, théosophisme, New Age
5. **speculatif** — hypothèse personnelle de Sidy, ni validée ni rejetée (statut **transitoire** ;
   évolue à la clôture du discernement)

---

## 4. Circuit Discernement (`doctrinal/discernement/`)

Pour les **spéculations métaphysiques personnelles** de Sidy (catégorie A+C du triage : récit
vécu à portée doctrinale). Fichier `YYYY-MM-DD_titre-court.md`, `type: discernement`,
`status: speculatif`. **Une page = une spéculation.** Après le récit, insère ce bloc normalisé :

```markdown
> 🔍 **Discernement — Spéculation Personnelle**
> **Statut** : en cours | validée | invalidée
> **Hypothèse initiale** (datée, reformulée fidèlement) : …
> **Généalogie des idées** :
>   - *Filiation orthodoxe possible* : [[symbole-ou-autorite]] — nature du rapprochement
>   - *Parenté hétérodoxe possible* : [[deviation]] — nature du rapprochement
> **Examen formel** (cohérence logique/terminologique — jamais le principe) : …
> **Conclusion** : attribuée par Sidy ou une autorité textuelle citée, JAMAIS auto-décrétée par l'IA.
```

**Étanchéité inversée** : une page `symbole/` ou `autorite/` orthodoxe ne pointe pas vers un
discernement `en cours` — *sauf* lien **défensif/généalogique** (mise en garde, ou déviation
documentant son origine), admis par jurisprudence (2026-06-20). Un discernement peut, lui, lier
librement vers symboles/autorites/deviations/etudes (généalogie des idées).

---

## 5. Circuit Atelier (`atelier/`) — frontmatter allégé

```yaml
---
title: "Titre exact"
type: materiel | manuel | entretien | projet
tags: [audio, compression]
created: 2026-06-20
updated: 2026-06-20
sources: []
links: []
---
```
- `materiel/` et `entretiens/` ne lient JAMAIS vers `doctrinal/`.
- `projets/` peut pointer vers `doctrinal/` en **sens unique** (œuvre inspirée d'un principe).

---

## 6. Domaine réservé `meta/` + étanchéité

`meta/` = outillage, fiche perso (`sidy`), **généalogie familiale**, **ijâza** (transmissions
nominales), journal, archives de conversation, toute mention privée.

**Hiérarchie** (du + sensible au + neutre) : `meta/` → `atelier/projets/` → `doctrinal/`+`atelier/`.
- Lien autorisé : du sensible VERS le neutre uniquement.
- INTERDIT : inscrire un fait personnel dans une page neutre (ex. « a délivré une ijâza à Sidy »
  dans une page d'autorité). Signaler tout croisement.
- En cas de doute sur le circuit : **demander avant de créer**.

---

## 7. Les 12 Commandements Absolus (résumé)

1. Primauté du Principe (la vérité ne change pas) · 2. Rigueur des termes (psychique ≠ spirituel)
· 3. Non-syncrétisme · 4. Une page = un sujet · 5. Aucune affirmation sans source · 6. Pas
d'écriture sans plan validé · 7. Étanchéité des circuits · 8. `created` immuable, `updated`
à chaque édition · 9. Journaliser aux annales · 10. Pas de suppression sans confirmation ·
11. Vocabulaire : « **restauration** », jamais « réforme » ·
12. **L'IA est *upakarana* (instrument subordonné), discernement forme/principe** : sur la
   **forme** (validité d'un raisonnement, univocité des termes, conformité) le modèle se prononce ;
   sur le **principe** (perception métaphysique directe) il ne statue pas, ni pour affirmer ni pour
   nier, et renvoie à l'autorité qualifiée. Référer n'est pas valider par participation. Voir
   `meta/directive-discernement-domaines.md`.

---

## 8. Nomenclature

Fichiers en **minuscules ASCII, sans accents, tirets `-`**. Titres H1 internes : accents FR OK.
Études et discernements : préfixe `YYYY-MM-DD_`.

---

## 9. Ce que tu PRODUIS et comment le livrer (format de sortie)

Le **format idéal** (rodé le 2026-06-20, intégration parfaite) :

1. Produis chaque page `.md` **déjà au Sceau Recteur**, **rangée dans l'arborescence exacte**
   (`doctrinal/symboles/…`, `doctrinal/discernement/…`, `meta/…`, etc.).
2. Joins **un fichier d'instructions unique** `MASTER-UPDATES.md` à la racine du lot, contenant :
   - la **liste des fichiers par dossier** ;
   - les **ajouts à `doctrinal/index.md`** (une ligne `[[chemin|Titre]]` par page, par section) ;
   - **une entrée pour `annales.md`** (préfixe `## [YYYY-MM-DD] <action> | Titre`) ;
   - les **points sensibles** et **liens à vérifier**.
3. Emballe le tout en **ZIP** (Sidy le déposera dans `_inbox/` via Termius SFTP).
   → Sidy lance `claude` et dit **« intègre `_inbox/` »** ; le serveur vérifie collisions /
   frontmatter / étanchéité, range, met à jour index+annales, commit/push, vide le sas.

**Règles de production** :
- **Une page = un sujet.** Ne recrée pas une page existante → **enrichis-la** (consulte
  `doctrinal/index.md`, qui fait foi).
- Lien vers une cible inexistante : **signale-la** dans `MASTER-UPDATES.md` plutôt qu'un lien mort
  (ou crée un stub `to-source`).
- Blocs normalisés : `> 🌐 **Forme Traditionnelle Divergente** : …` (divergence entre traditions) ;
  `> ⚠️ **Déviation Profane** : …` (erreur moderne/occulte) ; `> 🔍 **Discernement** …` (spéculation).

---

## 10. Points de vigilance récurrents

- **Citations non vérifiables** : ne jamais attribuer une citation précise à Ibn ʿArabī, al-Ghazālī,
  Guénon, Cheikh Nazim… sans édition fiable. Marquer `to-source` + signaler.
- **Non-syncrétisme** : montrer la convergence métaphysique SANS fusionner les formes (ex. ne pas
  identifier crûment istiʿdād akbarien et tülku vajrayāna ; les rapprocher en signalant la cloison).
- **Personnel → neutre interdit** : ijâza, généalogie, noms de personnes réelles, expériences
  vécues → `meta/` ou `discernement/`, jamais dans une page de référence orthodoxe.
- **`ne-pas-partager`** : documents privés (ex. notes Isaghuji) → tag `#ne-pas-partager`, aucun lien.
- **Dédicace nominale** : un texte dédié nominalement à Sidy bascule en `meta/`.
- **Autorité spirituelle** : une question d'application personnelle (suis-je dans tel état/maqām ?)
  relève du Cheikh vivant, jamais d'une auto-évaluation ni de l'IA → `discernement/`, statut en cours.

---

## 11. État des travaux (au 2026-06-20)

**Acquis** : protocole restauré « Guénon V1 » (2026-06-11/12) ; circuit Discernement + Commandement 12
intégrés ; sas `_inbox/` opérationnel. Lots intégrés : cluster soufisme/Ibn ʿArabī, astrologie, Islam &
IA, Wazifa, al-Jīlī, Hasbiyallah, étude upakarana, dossier discernement LLM, **session ChatGPT-export
(50 fichiers, 37 conversations, catégorie A+C)**.

**Reste à traiter de l'export ChatGPT** (triage des 140 conversations) : **catégorie A ≈ 39 · B ≈ 13 ·
C ≈ 25 · B+C ≈ 4**. Continuer par lots, format ZIP + `MASTER-UPDATES.md`.

**PDF de `raw/` restants** (non lus) : matériel audio (Revox, Tascam, Neve, Distressor, Logic Pro →
`atelier/`), logique (Isaghuji, Zaytuna → `symboles/`, Isaghuji-notes `#ne-pas-partager`), académique
divers, prières/awrâd arabes, ijâza-94/95 (→ `meta/`).

---

## 12. Pages existantes — NE PAS recréer (consulte `doctrinal/index.md` qui fait foi)

Instantané indicatif (l'index est la liste exacte) :
- **traditions** : tasawwuf, ahl-al-sunnah-wa-l-jamaa, sanatana-dharma, naqshbandiyya
- **autorites** : ibn-arabi, al-ghazali, rene-guenon, platon, ibn-sina, idris, ahmad-al-buni,
  al-jazari, al-khwarizmi, ouattara-brahima, ali-hussain, yaqub-chaudhary, abd-al-karim-al-jili,
  abd-al-qadir-al-jilani, ibn-qayyim, muhammad-nazim-al-haqqani, abdullah-daghestani, faraz-rabbani,
  hamza-yusuf (stub), ibn-sirin, al-nabulusi
- **symboles** : wahdat-al-wujud, barzakh, walaya, al-insan-al-kamil, ilm-al-huruf, ilm-al-nujum,
  asma-al-husna, talisman-sihr, wird-awrad, salawat, khatm-al-khawajakan, tawakkul, futuwwa, shukr,
  ghafla, tibb-e-nabawi, tibb-yunani, alam-al-mithal, khalwa, waqia, istidad, tarbiyya-rabbaniyya,
  habl-allah, influx-spirituel-sommet-cranien, taabir-al-ruya, firasa, taawil-par-le-nom,
  fal-wa-tatayyur + motifs oniriques (vol/uriner/marcher-sur-eau/cheveux-blancs/elephant/chat/
  homme-pieux/chaussure/axe-corde/animaux-en-reve-comparatisme), lieux-saints-france, maqamat-meknes
- **deviations** : morphopsychologie, body-types, reincarnation-vies-anterieures, technologisation-pseudo-scientifique
- **etudes** : 2026-06-04_islam-et-ia, 2026-06-20_etre-psyche-intellect-raison-upakarana
- **sources** : awrad-ibn-arabi, jesus-and-enoch-in-ibn-arabi, shams-al-maarif,
  ilm-al-nujum-astrologie-traditionnelle, islam-and-artificial-intelligence, hasbiyallah-rabbani,
  universal-man-jili, wazifa, mawlid-al-rasul, conversation-llm-intellect-2026-06-11
- **discernement** : 2026-06-11_llm-wiki-modalite-intellect, 2026-06-11_llm-wiki-correction-doctrinale,
  + 7 fiches du 2026-06-20 (visions-centre-nocturne, matrices-artificielles-barzakh,
  triptyque-medine-jeu-de-piste, experience-lefke-materia-secunda, epreuve-tariqa-tarbiyya-rabbaniyya,
  signaletique-spirituelle-kiswa, pierres-astres-barzakh)

---

*Ce briefing remplace, pour l'usage iPad, les anciens `meta/ingest-brief.md` et
`meta/protocole-archivage-claude-ai.md` (antérieurs au circuit Discernement et au sas `_inbox/`).
Tiens-le à jour à chaque évolution du protocole.*
