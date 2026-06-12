---
title: "Brief d'archivage des PDF de raw/ (post-Restauration doctrinale)"
type: meta
updated: 2026-06-11
---

# Mission : archivage des PDF de `raw/` dans le wiki restauré

> Fiche d'instruction pour la session **app iPad Claude AI** (lecture des PDF,
> gratuite sur forfait) qui produit le contenu, intégré ensuite par la session
> **Claude Code** du serveur. Rédigée le 2026-06-02, **refondue le 2026-06-11**
> après la Restauration doctrinale (« Guénon V1 »). Voir aussi
> [[protocole-archivage-claude-ai]] (briefing court) et le `CLAUDE.md` du dépôt
> (protocole complet).

Tu es dans `/root/wiki`. AVANT TOUT : lis `CLAUDE.md` et applique-le à la lettre
(protocoles ARCHIVAGE & MAILLAGE / MÉDITATION & SYNTHÈSE / VIGILANCE, Sceau
Recteur, slugs ASCII, « une page = un sujet », source pour tout fait, les 3
Commandements). En cas de doute, c'est `CLAUDE.md` qui tranche.

## Deux circuits distincts

Le dépôt a **deux circuits** depuis la Restauration :

1. **Doctrinal** (`doctrinal/…`) — métaphysique, traditions, autorités, symboles,
   sciences traditionnelles (y compris la **logique**), déviations, études. Frontmatter
   « Sceau Recteur » obligatoire (voir plus bas).
2. **Atelier** (`atelier/…`) — circuit **NON-doctrinal** pour le métier audio/studio
   (manuels de matériel, entretiens). Hors Sceau Recteur, frontmatter allégé. Ne
   JAMAIS mélanger les deux circuits ni lier de l'un vers l'autre.

## Opération demandée

Archivage de TOUS les PDF de `/root/wiki/raw/*.pdf`, en profondeur EXHAUSTIVE
(restitue le contenu utile : chapitre par chapitre pour les textes, réglage par
réglage pour les manuels audio). NE traite PAS l'export « ChatGPT historique »
(phase ultérieure).

## Workflow réel (app iPad → intégration serveur)

L'app iPad ne peut PAS éditer le dépôt ni committer. En deux temps :

1. **Toi (app iPad)** : tu lis le PDF et tu produis le CONTENU — une page par
   sujet + un fichier `UPDATES.md` (voir « Sortie attendue »).
2. **Session serveur (Claude Code)** : range les pages dans le bon dossier,
   **répare ton frontmatter**, applique les UPDATES à `doctrinal/index.md` et
   `doctrinal/annales.md`, lance le LINT, commit/push. C'est elle qui garantit la
   conformité.

> ⚠️ Le transfert iPad altère souvent le frontmatter (`---` → `-----`, `title:`
> → `## title:`, guillemets droits `"` → courbes `« » " "`). Vise le format exact
> ci-dessous : produis du **YAML strict** (trois tirets, guillemets droits, pas
> de `#` dans le frontmatter). La session serveur répare au besoin.

## Sceau Recteur — frontmatter EXACT des pages doctrinales

```yaml
---
title: "Titre exact (accents FR autorisés)"
type: doctrine | tradition | symbole | autorite | deviation | etude | source
status: traditionnel | academique | profane | contre-traditionnel
tradition_cadre: "islam"        # ou "hindouisme", "hellenisme", "universel", "none"
tags: [metaphysique, logique, cosmologie]   # mots nus, ASCII, sans guillemets
created: 2026-06-11             # date du jour, ISO
updated: 2026-06-11
sources_count: 1                # nombre de sources réelles citées
cross_links: ["[[autre-slug]]"] # liste de [[slug]] vers d'autres pages
---
```

- `cross_links` : liste YAML de chaînes `"[[slug]]"`. Liste vide = `[]`.
- `sources_count` : un entier. Toute affirmation factuelle doit être sourcée dans
  le corps (`— source : [[…]]`) ; si la source manque, signale la page comme à
  compléter dans `UPDATES.md`.
- Choix du `status` : `traditionnel` (sacré, maîtres authentiques) ·
  `academique` (érudition) · `profane` (moderne, matérialiste) ·
  `contre-traditionnel` (occultisme, pseudo-religion).

## Où classer (circuit doctrinal)

| Nature | Dossier | type |
|---|---|---|
| Forme traditionnelle (voie, école, dharma) | `doctrinal/traditions/` | tradition |
| Principe, symbole, **science traditionnelle (logique, ʿilm al-ḥurūf…)** | `doctrinal/symboles/` | symbole |
| Personne-autorité (maître, auteur, érudit) | `doctrinal/autorites/` | autorite |
| Erreur moderne / occultisme / pseudo-religion | `doctrinal/deviations/` | deviation |
| Analyse transversale / réponse fixée | `doctrinal/etudes/` (préfixe `YYYY-MM-DD_`) | etude |
| Fiche de lecture (le document source lui-même) | `doctrinal/sources/` | source |

## Méthode de travail (impérative — limites d'usage)

1. UN document à la fois.
2. Au démarrage, relis `doctrinal/index.md` (Catalogue) et `doctrinal/annales.md`
   pour savoir ce qui est déjà fait et NE PAS le refaire.
3. Tiens une checklist de progression pour reprendre après coupure.
4. Garde les GROS SCANS pour la fin : `shams-al-maarif` (57 Mo, déjà fait),
   `REVOX multilingue`, `logic-pro-ipad` (1100 p), `Model12`.

## Procédure par document (doctrinal)

- Lis le document en entier.
- Crée UNE fiche `source` (`doctrinal/sources/<slug>.md`).
- Crée/enrichis les pages `autorite` / `symbole` / `tradition` que le contenu
  justifie — une page par sujet, Sceau Recteur complet.
- Lie via `[[slug]]` ou `[[doctrinal/chemin/slug|Nom]]`. Cible manquante : signale-la
  dans `UPDATES.md` plutôt que de créer un lien mort.
- Utilise les blocs normalisés si besoin :
  `> 🌐 **Forme Traditionnelle Divergente** : …` / `> ⚠️ **Déviation Profane** : …`

## Sortie attendue : `UPDATES.md`

```markdown
# UPDATES — <source>, <date>

## Pages créées
- doctrinal/<dossier>/<slug>.md — <une ligne>

## Pages modifiées
- doctrinal/<dossier>/<slug>.md — <quoi>

## Fiches personnelles (→ meta/, étanchéité)
- <slug> — <raison>

## Ajouts au Catalogue (doctrinal/index.md)
- §<section> : [[doctrinal/<dossier>/<slug>|Nom]]

## Entrée pour les Annales (doctrinal/annales.md, en tête)
## <YYYY-MM-DD> — Archivage : <titre>
- **Opération** : ARCHIVAGE & MAILLAGE
- **Cadre** : <tradition_cadre> (<status>)
- **Créé** : [[…]]
- **Modifié** : [[…]]
- **Source brute** : raw/<fichier.pdf>
- **Notes** : …
```

## Pages DÉJÀ existantes — à ENRICHIR, jamais à recréer

> L'index (`doctrinal/index.md`) fait foi ; cette liste est un instantané.

- **autorites/** : `ibn-arabi`, `al-ghazali`, `rene-guenon`, `platon`,
  `ali-hussain`, `idris`, `ahmad-al-buni`, `ouattara-brahima`, `ibn-sina`,
  `al-jazari`, `al-khwarizmi`, `yaqub-chaudhary`
- **traditions/** : `tasawwuf`, `sanatana-dharma`, `ahl-al-sunnah-wa-l-jamaa`
- **symboles/** : `wird-awrad`, `salawat`, `walaya`, `barzakh`, `wahdat-al-wujud`,
  `ilm-al-huruf`, `asma-al-husna`, `talisman-sihr`, `ilm-al-nujum`
- **sources/** : `awrad-ibn-arabi`, `jesus-and-enoch-in-ibn-arabi`,
  `shams-al-maarif`, `ilm-al-nujum-astrologie-traditionnelle`,
  `islam-and-artificial-intelligence`
- **etudes/** : `2026-06-04_islam-et-ia`
- **meta/** (hors doctrine) : `sidy`, `chatgpt-export-2026-05-10`

## Documents DÉJÀ traités (ne pas refaire)

- ✅ `Awrad_Ibn_Arabi.pdf`, `Jesus_And_Enoch_In_Ibn_'arabi.pdf`,
  `shams-al-maarif-traduit-complet.pdf` (cluster soufisme — 2026-06-02)
- ✅ `LA FIN DES TEMPS MODERNES ‘ILM AL-NUJÛM…pdf` (astrologie — 2026-06-03)
- ✅ `islam-and-artificial-intelligence.pdf` (Islam & IA — 2026-06-04)

## Carte des slugs proposés (adapte selon le contenu réel)

### SOUFISME / MÉTAPHYSIQUE (doctrinal ; cadre islam, traditionnel)
- `universal-man.pdf` → source `universal-man-jili` ; autorite `abd-al-karim-al-jili` ; symbole `al-insan-al-kamil`

### LOGIQUE — science traditionnelle (doctrinal ; cadre islam/universel)
- `Intro_to_Logic-FULL-(Zaytuna_College).pdf` → source `intro-to-logic-zaytuna` (status academique) ; symboles : `al-mantiq` (la logique), `universaux`, `proposition`…
- `Isaghuji_logique_traditionnelle_FR.pdf` → source `isaghuji-logique-traditionnelle-fr` ; symbole `isagoge` ; autorite `al-abhari`
- `Isaghuji logic full Notes ne pas partager .pdf` → source `isaghuji-notes` ⚠️ **ajoute le tag `ne-pas-partager` et NE le lie depuis aucune page** (note privée).

### PRIÈRES / AWRÂD (doctrinal ; cadre islam, traditionnel)
- `Dua of Laylatul Qadr.pdf` → source `dua-laylatul-qadr`
- `Prayer-on-the-Fifteenth-Night-of-Shabān.pdf` → source `prayer-15th-shaban`
- `Salat-al-Kaffarat-adh-Dhunub-20200629.pdf` → source `salat-al-kaffarat`
- `Wazifa.pdf` → source `wazifa`
- `مولد الرسول الأعظم…pdf` (Mawlid) → source `mawlid-al-rasul` (general/traditionnel) ⚠️ si dédicace nominale à Sidy → bascule en `meta/` et signale.

### ACADÉMIQUE / FIGURES (doctrinal ; identifie le titre exact en lisant)
- `Al-Hadj-Cheikh-Belmadi-2017.pdf` → autorite `<cheikh>` + source `al-hadj-cheikh-belmadi-2017`
- `religions-16-00549-with-cover.pdf` → source `<titre-réel>` (status academique)
- `grr-academix-2026.pdf` → source `grr-academix-2026` (identifie le sujet ; circuit selon contenu)

### ⚠️ IJÂZA — domaine personnel (→ `meta/`, PAS doctrinal)
- `إجازة-94.pdf` / `إجازة-95.pdf` → fiches `meta/ijaza-94`, `meta/ijaza-95`.
  **Sidy est le destinataire** (décidé 2026-06-03). Ces fiches PEUVENT pointer
  vers des `autorites/` (le cheikh transmetteur, la *silsila*, la *tarîqa*), mais
  n'inscris JAMAIS « a délivré une ijâza à Sidy » dans une page doctrinale
  (remontée perso → doctrinal interdite, Commandement Non-Syncrétisme). Signale
  tout croisement dans `UPDATES.md`.

### ATELIER — circuit NON-doctrinal (audio/studio ; PAS de Sceau Recteur)
> Range ces fiches sous `atelier/` avec un frontmatter allégé
> (`title`, `type: materiel|manuel|entretien`, `tags`, `created`, `updated`).
> Ne les lie depuis aucune page doctrinale.
- `distressor_manual.pdf` → `atelier/empirical-labs-distressor`
- `Revox-A-77-…Owners-Manual.pdf` / `…Service-Manual.pdf` / `REVOX A77 NOTICE MULTILINGUE.pdf` → `atelier/revox-a77-*`
- `Model12_OM_EFS_RevH3.pdf` → `atelier/tascam-model-12`
- `1073SPX_1.1_User_Manual…pdf` → `atelier/neve-1073spx`
- `logic-pro-ipad-user-guide.pdf` → `atelier/logic-pro-ipad`
- `Interview with Russell Elevado - Gearspace.pdf` → `atelier/russell-elevado-entretien`
- `Body_Types_Book.pdf` → **cas ambigu** (morphopsychologie moderne) : soit
  `atelier/` (référence métier), soit `doctrinal/deviations/` si traité
  critiquement comme pseudo-science. **Demande avant de trancher.**

## Compte-rendu attendu

À la fin (ou à chaque coupure) : docs traités, pages créées/enrichies (par slug
et dossier), pages à compléter restantes, et TOUT point sensible signalé
(ijâza, `ne-pas-partager`, Mawlid, Body_Types, croisements d'étanchéité).
