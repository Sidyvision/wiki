---
title: "Registre de veille R&D — journal des scrutations"
type: registre
tags: [atelier, rd, veille, registre]
created: 2026-08-18
updated: 2026-09-16
sources: []
links:
  - "[[atelier/rd/veille/index]]"
---

# Registre de veille R&D

Journal append-only des scrutations menées dans le cadre de la veille
externe. Chaque entrée porte : ce qui a été scruté, pourquoi, le
verdict, le lien vers la matière extraite.

**Règle** : une scrutation sans verdict n'est pas consignable. On attend
d'avoir qualifié avant de noter. Le registre n'est pas un journal de
bord (quoi j'ai fait aujourd'hui) mais un journal de décisions (quoi
j'ai retenu, pourquoi).

---

## [2026-09-16] Investigation — LANDR : le compte et l'API sont deux portes ; pont entrant éprouvé sur un lien de partage

**Quoi** : question de Sidy — « est-ce que LANDR prévoit un accès serveur direct ? », précisée en **demande de pont entrant** (rapatrier sur le serveur des morceaux déjà déposés dans son compte LANDR). Scrutation menée **hors des pages** : spécification OpenAPI d'API récupérée et conservée (8 chemins, 10 opérations, sha256 court `14d4d164…`), sondes réseau datées sur `api.landr.com` (403 AccessDenied en périphérie hors chemins de documentation), centre d'aide interrogé par son API publique de recherche (« API » → 0 article, « Linux » → 0 article), bundle applicatif de la page de partage lu pour identifier le mécanisme d'accès anonyme (en-tête `X-LANDR-PUBLIC-TOKEN`), et **éprouve réelle** du lien de partage fourni par Sidy pour la piste « 01 - Wake up » — téléchargement du flux, mesure `ffprobe` et mesure de niveau `ebur128`, plus quatre contrôles de validité des sondes.

**Pourquoi** : décider s'il existe une voie serveur-à-serveur pour l'entrant (masters déjà produits côté LANDR) dans notre contexte — serveur Ubuntu sans écran, humain sur iPad, finalité de souveraineté du pôle `rd/` (émancipation des intermédiaires de service tiers).

**Verdict** : **le compte et l'API sont deux portes distinctes**. L'API (`api.landr.com`, clé d'en-tête unique, accès par « Contact sales » à partir de 2,50 $/titre) **crée du neuf à partir d'un URI et ne relit jamais l'existant** : aucune opération de bibliothèque, de compte, de crédits ou de releases. Le **pont entrant existe donc en deux étages** : (1) **écoute automatisable dès maintenant, sans identifiant** — le flux `projects.landr.com/assets/<uuid>/stream.mp3` se tire sans jeton (404 sur UUID bidon), mesuré à **3 425 637 octets**, MP3 CBR 192 kbps / 44,1 kHz / stéréo / 142,707 s, **-7,4 LUFS**, LRA 2,5 LU, **crête vraie +0,3 dBFS** ; (2) **master livrable fermé** — « Download all » redirige vers `accounts.landr.com/oauth2/register`, `chatAssetDownloadUrl` rend **`UNAUTHENTICATED`**, et le modèle de permissions déclaré par leur serveur à un visiteur anonyme porte **`canDownload: false`**. Le flux de l'étage 1 est une **copie d'écoute** (192 kbps) quand leur documentation donne le master MP3 livrable à **320 kbps** — donc utilisable pour vérifier et mesurer, pas comme master d'archive. **Conséquence** : l'entrant des masters passe par le **geste humain** vers `_inbox/` ; l'étage 1 reste à instruire comme outillage, sur verdict.

**Pertinence** : directe pour le poste studio (chaîne de mastering, critère de crête vraie au-dessus de 0 dBFS avant tout passage sur bande) et pour la finalité de souveraineté du pôle `rd/` — la voie automatique de LANDR impose une clé commerciale **et** l'exposition de nos masters à une URL publique que leurs serveurs viennent chercher. **Signalé et non tranché** (Cmd 12) : l'hypothèse d'un réglage de partage autorisant le téléchargement anonyme, écartée par Sidy le jour même (« ce ne sont encore que des ébauches ») — les deux lectures possibles ne sont pas séparées par la mesure.

**Liens** :
- Fiche : [[atelier/rd/veille/2026-09-16_landr-pont-entrant-partage-et-api]]
- Documentation d'API : <https://api.landr.com/mastering/openapi/v1/openapi.json>
- Page API : <https://www.landr.com/pro-audio-mastering-api>
- Copie d'éprouve (hors dépôt) : `/root/sandbox-rd/landr-inbound/stream.mp3` (sha256 `57681f46…`)

---

## [2026-09-15] Investigation — Soup CLI / Soup Zero (post-entraînement local d'un LLM)

**Quoi** : investigation du lien pointé par Sidy (`https://trysoup.dev/zero`), menée **hors de la page** : API GitHub (étoiles, forks, issues, contributeurs, dates), PyPI (version, nombre de releases, contraintes Python), DOI Zenodo, **téléchargement et inspection de la roue 0.75.0** (présence de hooks d'installation, régime de télémétrie) et comptage des téléchargements **miroirs exclus**. Constat de forme d'abord : `/zero` est une page de **concept** (« Coming soon », « Concept preview ») — 3 stations sur 10 livrées — et l'outil réellement utilisable est le CLI Apache-2.0 `soup-cli`.

**Pourquoi** : évaluer la pertinence pour le pôle de souveraineté et pour le chantier `INF-16` (machine d'IA locale et développement SLM), dont les critères 5 (aptitude au fine-tuning), 6 (maturité d'écosystème) et 11 (étanchéité §VI) sont directement concernés.

**Verdict** : **retenu** comme référence technique d'`INF-16`, statut `exploratoire`, **rien engagé** — aucune machine n'existe, la charge de référence n'est pas arrêtée, et rien n'a été installé ni exécuté (le seul poste physique n'a pas de GPU). Apports : un même outil couvre **CUDA et MLX Apple** ; le projet publie ses défauts silencieux et a fait répliquer sa prétention centrale sur du matériel loué, ce qui **rejoint par un autre chemin notre §VII, *Épreuve des contrôles***. Deux motifs d'ingénierie repérables **sans adopter le code** : un verdict committable par run (`soup ship`) et l'exécution d'un run planifié derrière un **jeton de confirmation à usage unique** (`soup mcp serve --allow-execute`).

**Pertinence pour le développement futur** :
- ✅ critère 6 nourri de faits mesurés (papier, archives de mesure publiées avec leurs retraits, validation externe) plutôt que d'une réputation
- ✅ compatibilité **MLX** native — seule pièce de ce relevé qui parle à la branche Apple d'`INF-16` (options A/B)
- ✅ l'artefact produit (adaptateur, GGUF) **reste un bien** même si le GPU est loué — n'informe que la jambe entraînement de l'option E, ne la rouvre ni ne la ferme
- ⚠️ projet jeune (sept mois, un mainteneur principal, cadence de publication cassante) : version à **épingler** et evals à re-passer avant tout usage
- ⚠️ question **ouverte, non tranchée** : un adaptateur entraîné sur le corpus **porte** le corpus — le dépôt n'a pas de régime pour cet objet (§VI, critère 11)
- ⏳ à reprendre le jour où la machine d'`INF-16` est choisie : c'est alors une ligne de matrice, pas avant

**Liens** :
- Fiche de veille : [[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]]
- Repo : <https://github.com/MakazhanAlpamys/Soup> · PyPI : <https://pypi.org/project/soup-cli/>
- Page pointée : <https://trysoup.dev/zero> · Validation externe : <https://trysoup.dev/docs/external-validation>
- Chantier concerné : [[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec]]

---

## [2026-08-31] Investigation GitHub — Tencent/AngelSpec (speculative decoding)

**Quoi** : investigation approfondie du repo `Tencent/AngelSpec` (framework de training pour speculative decoding) à partir d'une vidéo YouTube partagée par Sidy. Audit complet : API GitHub (stats, commits, issues, PRs), extraction du paper arXiv (2607.25852), lecture de la LICENSE, analyse de la PR #2 non mergée, consultation des modèles HuggingFace AngelSlim, couverture médiatique.

**Pourquoi** : évaluer la pertinence pour la stack d'inférence (inférence actuelle via providers cloud, pas de GPU local — voir incident 2026-08-28) et pour la souveraineté d'infrastructure (accélération inference LLM sans dépendance tierce).

**Verdict** : AngelSpec est une référence scientifique sérieuse (paper solide, benchmarks systématiques sur Hy3-A21B : 1.98–2.40× speedup, +30% accepted length vs baseline) mais un projet de code fragile (maintenance faible, 32 jours sans réponse à la PR #2 qui corrige 12 bugs de correctness dont un critique RoPE). Les drafter models pré-entraînés AngelSlim (Qwen3-8B_eagle3, 7 470 downloads) sont consommables directement sans le framework. Licence Apache-2.0, production-safe. **Fiche constituée comme référence technique à instruire pour un développement futur** — non exploitable immédiatement (infrastructure actuelle sans GPU), mais matériau de qualité si un chantier d'inférence locale GPU est ouvert.

**Pertinence pour le développement futur** :
- ✅ 6 architectures unifiées, benchmarks de référence (1.98–2.40× speedup), MTP+TTT (+13.6 pp acceptance)
- ✅ Modèle `AngelSlim/Qwen3-8B_eagle3` (7 470 downloads) directement utilisable si vLLM+Qwen3-8B sur GPU
- ⚠️ Maintenance faible — re-vérifier l'état du repo avant engagement futur
- ⏳ À re-consulter si un chantier d'inférence locale GPU est ouvert (containers, serveur dédié, etc.)

**Liens** :
- Fiche de veille : [[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]]
- Repo : <https://github.com/Tencent/AngelSpec>
- Paper : <https://arxiv.org/abs/2607.25852>

---

## [2026-08-18] Scrutation GitHub — implémentations Cordis

**Quoi** : recherche GitHub sur "spatiotemporal composability", "revertible effects", "reactive coeffects".

**Pourquoi** : identifier les implémentations open-source du paradigme Cordis (papier DeepSeek/Peking Univ), qualifier leur pertinence pour le dépôt.

**Verdict** : 7 repos trouvés, tous implémentations du paradigme dans différents langages (JVM, Rust, Go, Wasm, langage de recherche). Les plus pertinents :
- **cordis4j** (JVM, 4★) — implémentation la plus mature
- **spatiotemporal** (Rust, 2★) — articulation avec le borrow checker
- **cordis-wasm** — sandbox Wasm qui *force* le paradigme
- **spatiotemporal-composability-skill** — skill agent pour recomposition à l'exécution (potentiellement pertinent pour Hermes)

**Liens** :
- Matière extraite : `atelier/rd/veille/cordis/implementations-github.md`
- Repos scrutés : voir la fiche ci-dessus

**Questions ouvertes** :
- Quel est le dépôt source Cordis (TypeScript original) ?
- Qui est `inso1337` (auteur de 2 repos) ?
- Le repo `spatiotemporal-composability-skill` est-il une skill Hermes ?

---

## [2026-08-18] Ouverture du lieu

**Quoi** : ouverture de `atelier/rd/veille/` sur verdict de Sidy.
Première scrutation : périmètre Cordis/DeepSeek (source de la présente
extension).

**Pourquoi** : le papier *A Programming Paradigm for Spatiotemporal
Composability* (Shi, Zhang, Cui — Peking University / DeepSeek-AI)
décrit un paradigme d'ingénierie (composabilité spatiotemporelle,
effets réversibles, coeffets réactifs) qui résonne de forme avec la
convention Sashimono du dépôt et qui pourrait nourrir des chantiers
concrets (HMR pour les 12 agents, gestion des dépendances
inter-gateways). La présente extension vise à ne pas laisser cette
lecture isolée : garder un œil sur ce qui se fait dans le même registre,
archiver qualitativement, éprouver en sandbox.

**Verdict** : périmètre qualifié comme pertinent. Matière extraite vers
`cordis/` (équations, méthodes, notes de lecture, implémentations GitHub).
Sandbox à instruire séparément.

**Liens** :
- Matière extraite : `atelier/rd/veille/cordis/`
- Fiche d'instruction globale :
  [[atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle]]
- Proposition d'extension :
  [[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18]]
