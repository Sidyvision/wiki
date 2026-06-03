# Mission : INGEST exhaustif des PDF de raw/ dans le wiki

> Fiche d'instruction destinée à une session **Claude Code** lancée sur le
> serveur (abonnement Pro/Max), dans le dépôt `/root/wiki`. Rédigée le
> 2026-06-02. Objectif : déporter le gros du travail de lecture des PDF hors
> de l'API payante au token.

Tu es dans le dépôt d'un wiki personnel en français situé à `/root/wiki`.
AVANT TOUT : lis `/root/wiki/CLAUDE.md` et applique ses règles À LA LETTRE
(les 4 opérations, le frontmatter obligatoire, slugs kebab-case ASCII sans
accents, dates ISO, « une page = un sujet », source obligatoire pour tout fait,
étanchéité des domaines, journalisation). En cas de doute sur une règle,
c'est `CLAUDE.md` qui tranche.

## Opération demandée

INGEST de TOUS les fichiers de `/root/wiki/raw/*.pdf`, en profondeur
DÉTAILLÉE / EXHAUSTIVE (pas un simple résumé : restitue le contenu utile,
réglage par réglage pour les manuels, chapitre par chapitre pour les textes).
NE traite PAS l'export « ChatGPT historique » pour l'instant (phase ultérieure).

## Workflow réel (app iPad Claude AI → intégration serveur)

L'app iPad ne peut PAS éditer le dépôt à la source ni committer. Le travail se
fait donc en deux temps :

1. **Toi (app iPad)** : tu lis le PDF et tu produis le CONTENU — une page par
   sujet + un fichier d'instructions `UPDATES` (voir plus bas). C'est l'étape
   coûteuse en lecture ; elle est gratuite sur le forfait Pro.
2. **Session serveur (Claude Code / API)** : récupère tes fichiers, applique les
   UPDATES à `index.md`/`log.md`, **normalise et répare le frontmatter**, range
   les pages, puis commit/push. C'est elle qui garantit la conformité.

### Ce que tu dois produire (app iPad)

- **Une page par sujet**, nommée `<slug>.md` (slug kebab-case ASCII), avec le
  frontmatter et le corps complets. Indique le dossier cible dans le nom ou en
  tête (`type:` suffit : entity→entities, concept→concepts, source→sources).
- **UN seul fichier `UPDATES-index-log.md`** par lot, contenant : (1) les lignes
  à ajouter à `wiki/index.md` par section, (2) l'entrée datée pour `wiki/log.md`,
  (3) la liste des fichiers existants à remplacer (pages enrichies).
- **UNE seule version par page** : ne génère pas de copies ni de variantes.

> ⚠️ Le transfert iPad altère souvent le frontmatter (`---` → `-----`, titres
> transformés en `## title:`, guillemets droits → courbes). Ce n'est pas grave :
> l'étape 2 le répare. Mais vise le format ci-dessous au plus près.

## Méthode de travail (impérative, à cause des limites d'usage Pro)

1. Travaille UN document à la fois.
2. Après chaque document terminé : `git add -A && git commit` avec un message
   clair (`INGEST: <sujet>`), puis `git push` si un remote est configuré.
3. Tiens une checklist de progression (coche les docs faits) pour pouvoir
   reprendre après une coupure. Au démarrage, relis `wiki/log.md` et l'index
   pour savoir ce qui est déjà fait et NE PAS le refaire.
4. Garde les GROS SCANS pour la fin : `shams-al-maarif` (57 Mo), `REVOX
   multilingue`, `logic-pro-ipad` (1100 p), `Model12`. Lis-les en plusieurs
   passes si besoin.

## Procédure par document

- Lis le document en entier.
- Crée UNE fiche `source` pour le document (`wiki/sources/<slug>.md`).
- Crée/enrichis les pages `entity` et `concept` que le contenu justifie
  (`wiki/entities/`, `wiki/concepts/`), une page par sujet, frontmatter complet.
- Lie tout via `[[slug]]`. Si une cible manque, crée un stub minimal
  (frontmatter + tag `#stub` + `sources: ["to-source"]`) plutôt qu'un lien mort.
- Cite toute affirmation factuelle dans `sources` (la fiche source du doc).
- Mets à jour `wiki/index.md` et ajoute UNE entrée datée à `wiki/log.md`.

### Format EXACT du frontmatter (respecte-le au caractère près)

Les champs `sources` et `links` sont des **listes YAML de chaînes entre
guillemets**, chaque wikilink étant un `"[[slug]]"` complet :

```yaml
sources: ["[[slug-source]]"]
links: ["[[autre-page]]", "[[encore-une]]"]
tags: [soufisme, metaphysique]   # mots-clés nus, sans guillemets ni accents
```

- Liste vide = `[]`. Source absente = `["to-source"]` (+ tag `#stub`).
- N'écris JAMAIS `links: [[a], [b]]` ni `links: [a, b]` : c'est non conforme.

## Pages DÉJÀ existantes — à ENRICHIR, jamais à recréer

> Vérifie TOUJOURS `wiki/index.md` au démarrage : cette liste est un instantané,
> l'index fait foi.

- Entités : `sidy`, `ibn-arabi`, `al-ghazali`, `rene-guenon`, `platon`,
  `ali-hussain`, `idris`, `ahmad-al-buni`, `ouattara-brahima`
- Concepts : `tasawwuf`, `sanatana-dharma`, `ahl-al-sunnah-wa-l-jamaa`,
  `wird-awrad`, `salawat`, `walaya`, `barzakh`, `wahdat-al-wujud`,
  `ilm-al-huruf`, `asma-al-husna`, `talisman-sihr`, `ilm-al-nujum`
- Sources : `chatgpt-export-2026-05-10`, `awrad-ibn-arabi`,
  `jesus-and-enoch-in-ibn-arabi`, `shams-al-maarif`,
  `ilm-al-nujum-astrologie-traditionnelle`

Quand un PDF concerne l'un d'eux, complète la page existante et retire son
tag `#stub` une fois qu'elle est sourcée. Ne crée pas de doublon.

## Documents DÉJÀ traités (ne pas refaire)

- ✅ `Awrad_Ibn_Arabi.pdf`, `Jesus_And_Enoch_In_Ibn_'arabi.pdf`,
  `shams-al-maarif-traduit-complet.pdf` (cluster soufisme/Ibn Arabi — 2026-06-02).
- ✅ `LA FIN DES TEMPS MODERNES ‘ILM AL-NUJÛM … .pdf` (astrologie — 2026-06-03).
- Restent : les manuels audio, la logique, l'académique divers,
  les prières/awrâd arabes, et l'export ChatGPT (phase ultérieure).

## Domaines (rappel CLAUDE.md : recherche | perso | business | lecture | general)

- TOUS les manuels audio, textes de logique, soufisme, articles académiques,
  astrologie, prières → `general`.
- DEUX EXCEPTIONS à traiter avec soin :
  - **(a)** `Isaghuji logic full Notes ne pas partager.pdf` → domaine `lecture`,
    ajoute le tag `#ne-pas-partager`, et NE le lie depuis aucune page neutre.
  - **(b)** Les deux fichiers إجازة (ijâza) → **domaine `perso` (sensible)**.
    DÉCIDÉ (2026-06-03) : Sidy / Sidyvision est le destinataire de ces ijâza.
    Les fiches `source` des ijâza vont donc en `perso`. Elles PEUVENT pointer
    vers des entités `general` (le cheikh qui transmet, la *silsila*, la
    *tarîqa*…), mais n'inscris JAMAIS « a délivré une ijâza à Sidy » dans une
    page `general` (remontée perso→neutre interdite — signale tout croisement).
  - **(c)** Le `Mawlid` → `general` par défaut (texte dévotionnel public). Si en
    le traitant tu trouves une dédicace nominale à Sidy, bascule en `perso` et
    signale-le.

## Carte des slugs proposés (adapte si le contenu le justifie)

**AUDIO (general)**
- `distressor_manual.pdf` → `sources/distressor-manual` ; entity `empirical-labs-distressor` ; concept `compression-audio`
- Revox-A-77 Owners → `sources/revox-a77-owners-manual` ; entity `revox-a77`
- Revox-A-77 Service → `sources/revox-a77-service-manual`
- REVOX A77 multilingue → `sources/revox-a77-notice-multilingue`
- `Model12_OM_EFS` → `sources/tascam-model-12-manual` ; entity `tascam-model-12`
- `1073SPX` → `sources/neve-1073spx-manual` ; entity `neve-1073spx`
- `logic-pro-ipad` → `sources/logic-pro-ipad-guide` ; entity `logic-pro`
- Interview Russell Elevado → `sources/russell-elevado-interview` ; entity `russell-elevado`

**LOGIQUE**
- Intro_to_Logic (Zaytuna) → `sources/intro-to-logic-zaytuna` ; concepts (universaux, propositions…)
- Isaghuji_traditionnelle_FR → `sources/isaghuji-logique-traditionnelle-fr` ; concept `isagoge` ; entity `al-abhari`
- Isaghuji notes « ne pas partager » → `sources/isaghuji-notes` (domaine `lecture`, `#ne-pas-partager`)

**SOUFISME (general ; enrichit `ibn-arabi`, `tasawwuf`)**
- `Awrad_Ibn_Arabi` → `sources/awrad-ibn-arabi` ; concept `wird-awrad`
- `Jesus_And_Enoch_In_Ibn_Arabi` → `sources/jesus-and-enoch-in-ibn-arabi`
- `universal-man` → `sources/universal-man-jili` ; concept `al-insan-al-kamil` ; entity `abd-al-karim-al-jili`
- `shams-al-maarif` → `sources/shams-al-maarif` ; entity `ahmad-al-buni` ; concept `ilm-al-huruf`

**ACADÉMIQUE (general — identifie le titre exact en lisant)**
- `religions-16-00549` → `sources/<titre-réel>`
- `islam-and-artificial-intelligence` → `sources/islam-and-artificial-intelligence` ; concept `islam-et-ia`
- `Al-Hadj-Cheikh-Belmadi-2017` → `sources/al-hadj-cheikh-belmadi-2017` ; entity si pertinent
- `grr-academix-2026` → `sources/grr-academix-2026` (identifie le sujet)
- `Body_Types_Book` → `sources/body-types` ; concept `morphopsychologie`

**ASTROLOGIE (general)**
- ‘ILM AL-NUJÛM → `sources/ilm-al-nujum-astrologie-traditionnelle` ; concept `ilm-al-nujum`

**PRIÈRES / AWRÂD (general sauf signalement ijâza/Mawlid)**
- Dua of Laylatul Qadr → `sources/dua-laylatul-qadr`
- Prayer 15th Night of Shaʿbān → `sources/prayer-15th-shaban`
- Salat al-Kaffârât → `sources/salat-al-kaffarat`
- Wazifa → `sources/wazifa`
- إجازة-94 / إجازة-95 → `sources/ijaza-94` / `sources/ijaza-95` ⚠️ voir règle destinataire
- Mawlid al-Rasûl → `sources/mawlid-al-rasul` ⚠️ voir règle destinataire

## Étanchéité des domaines (CLAUDE.md COMPARTIMENTALISER)

- Une page = exactement un domaine.
- Liens autorisés : d'un domaine sensible (`perso`, `business`) VERS un domaine
  neutre (`general`, `lecture`). L'inverse doit t'être SIGNALÉ avant.
- Ne copie jamais de contenu `perso`/`business` dans une page neutre.

## Compte-rendu attendu

À la fin (ou à chaque coupure), résume : docs traités, pages créées/enrichies
(par slug), stubs restants, et TOUT point de domaine signalé (notamment les
ijâza/Mawlid). C'est ce compte-rendu qui sera rapporté.
