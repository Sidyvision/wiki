---
title: "Soup CLI / Soup Zero — post-entraînement local d'un LLM (relevé pour INF-16)"
type: experience
statut_experience: exploratoire
chantier: INF-16
tags: [veille, post-entrainement, fine-tuning, lora, slm, souverainete, mlx, cuda, quantisation, infra-16]
created: 2026-09-15
updated: 2026-09-15
sources:
  - "https://trysoup.dev/zero"
  - "https://trysoup.dev/"
  - "https://trysoup.dev/docs/external-validation"
  - "https://trysoup.dev/support"
  - "https://github.com/MakazhanAlpamys/Soup"
  - "https://pypi.org/project/soup-cli/"
  - "https://doi.org/10.5281/zenodo.21771064"
links:
  - "[[atelier/rd/veille/index]]"
  - "[[atelier/rd/veille/registre]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# Soup CLI / Soup Zero — post-entraînement local d'un LLM (relevé pour INF-16)

**Source** : lien pointé par Sidy en session le 2026-09-15 (`https://trysoup.dev/zero`).
Investigation menée par le poste de veille d'infrastructure, rapportée sur Discord
`#infrastructure`, puis consignée ici sur validation de Sidy (« Validé »).

**Avertissement de lecture** : un compteur et un prix sont des **photographies**. Tous
les relevés ci-dessous portent leur date (2026-09-15) et leur instrument ; ils se
re-relèvent avant tout engagement.

## 1. Ce que la page est — et ce qu'elle n'est pas

`/zero` **n'est pas un logiciel** : c'est une page de **concept** (« Soup Zero ·
Coming soon », mention explicite « Concept preview. The engine underneath
(fine-tuning, evals, deploy) ships today as the open-source Soup CLI »).

- Dix stations annoncées ; **trois livrées** dans le CLI : fine-tuning, evals, deploy.
- **Sept non livrées** : playground, data, prompt studio, RAG / knowledge, agents &
  tools, monitoring, team — chacune marquée « In development », sans date.
- **Aucun formulaire de capture, aucune liste d'attente** : le seul appel à l'action
  renvoie au CLI (`Get Started` → documentation).
- L'objet réellement utilisable aujourd'hui : `pip install "soup-cli[train]"`.

L'écart entre ce que la page vend et ce qui existe est donc **déclaré par la page
elle-même** — c'est une page de vision assumée comme telle, pas une promesse de
disponibilité. Elle annonce en revanche une direction commerciale possible (« un clic
vers des GPU cloud que vous contrôlez ») : c'est le point par lequel un tiers pourrait
rentrer plus tard (voir §6).

## 2. Mesures vérifiées (relevées hors de la page, le 2026-09-15)

**GitHub** — API `repos/MakazhanAlpamys/Soup`, non paraphrasée :
`stargazers_count 6495`, `forks_count 1018`, `open_issues_count 147`,
licence `apache-2.0`, `created_at 2026-02-20T11:05:01Z`,
`pushed_at 2026-09-14T18:06:19Z`, `archived false`. Souscripteurs : 47.
**Contributeurs : 61** (en-tête `Link` de l'API, `rel="last"` page 61 à `per_page=1`).

**PyPI** — `soup-cli` **0.75.0** (publiée le 2026-09-12), **177 releases**,
`requires_python <3.13,>=3.10`. Cadence et régime : 0.71 → 0.75 en un peu plus de
deux mois, avec ruptures assumées — depuis v0.75 une **clé de configuration inconnue
refuse le chargement** (`exit 1`, `ValueError`), et `grpo_variant: gspo` change
d'objectif au point de **ne plus reproduire** les runs antérieurs.

**DOI** — `10.5281/zenodo.21771064` (concept) résout en HTTP 200 ; version courante
v3 : `10.5281/zenodo.21918325`.

**Contenu de la roue 0.75.0** (téléchargée et inspectée, sans installation) :
2,18 Mo, 504 modules `.py`, **aucun hook d'installation**. Télémétrie :
`is_telemetry_enabled()` renvoie **False** sauf `SOUP_TELEMETRY` ∈ {1, true, yes, on} —
donc **éteinte par défaut** ; la voie d'opt-in vise `us.i.posthog.com` avec un UUID
anonyme stocké en `~/.soup/telemetry_id`, et la clé embarquée
(`phc_soup_public_write_only`) est traitée par le code comme un **placeholder**.
La page affirme « Soup sends no telemetry » : **exact par défaut**, à la nuance près
qu'une voie d'opt-in existe.

**Téléchargements** — la page annonce 95,4 k ; **pypistats, miroirs exclus : 33 338**
cumulés du 2026-03-23 au 2026-09-14, dont **3 106** sur les 14 premiers jours de
septembre (165–300/jour). Deux comptages (pepy inclut les miroirs), pas une
contradiction — mais c'est 33 338 la valeur calibrée.

**Qui** — projet de Rafik Mamedov et Alpamys Makazhan, adossé à **MePlay, Inc.**
(Delaware). Page `Support` : dons seulement, « no paid tier, no license upgrade ».

## 3. Ce que vaut la prétention centrale (et sa méthode)

Prétention : entraîner un **8B en NF4 sur 4 Go de VRAM** en gardant le modèle gelé
hors du GPU (« layer streaming », une couche de décodeur à la fois, depuis la RAM ou
le NVMe). Le projet a publié sa propre réfutation partielle et son propre défaut :

- Réplication sur **8×H100 80 Go loués** (hardware non possédé) : 113,00 tok/s médian
  contre 119,6 tok/s sur la carte d'origine, **même pic de 3,32 Go**. Le chiffre
  vedette est donc **antérieur à une réparation** ultérieure et déclaré comme tel.
- **Défaut trouvé là-bas** : au-dessus d'environ **165 Mo par couche NF4**, les
  gradients étaient **faux** alors que le forward restait bit-exact, la perte
  identique au chiffre près et la sortie à 0. Borné (163,8 exact / 171,5 cassé),
  réparé en v0.73.0, coût mesuré (+2,9 % de pic, −4,8 % de débit au 32B).
- **Explication retirée** dans la v3 du papier (l'ancienne thèse « borné par le
  transfert hôte→GPU » est fausse à la configuration publiée : 1,4 %).
- Leur propre conclusion de méthode : **quatre des douze défauts** trouvés sur cette
  machine étaient des fonctions **jamais exécutées une seule fois**, dont deux
  produisaient des runs « réussis » à sortie 0.

C'est un écho direct à notre §VII, *Épreuve des contrôles* — « un contrôle dont on n'a
pas vu l'échec n'est pas un contrôle vérifié » — arrivé par un autre chemin, et c'est
la raison principale de conserver cette source.

## 4. Motifs d'ingénierie repérables (sans adopter le code)

- **`soup ship`** : chaque run se termine par un verdict **SHIP / DON'T SHIP**, sortie
  0 ou 2, avec une preuve **committable** à côté des poids qui l'ont produite.
- **`soup mcp serve --allow-execute`** : un run planifié ne s'exécute que derrière un
  **jeton de confirmation à usage unique généré par le serveur**, avec la
  configuration figée au moment du plan et les chemins protégés digérés par contenu —
  « qu'un modèle ne puisse pas être échangé entre la planification et l'exécution ».
  Motif identique à notre porte humaine (Cmd 6, Cmd 13) et à notre gouvernance
  Discord-Validation, sur un serveur MCP comme le nôtre.
- **« Une clé de configuration inconnue refuse le chargement »** (v0.75) : la forme de
  nos gardes `B0` / `P1` / `P2` — un refus **nommé** plutôt qu'un silence.

Ces trois motifs sont reprenables **sans rien installer** : ils s'énoncent, ils ne
s'importent pas. Aucune proposition d'emprunt n'est faite ici (elle demanderait un
chantier et un verdict).

## 5. Rapprochement avec `INF-16`

| Critère d'`INF-16` | Ce que ce relevé apporte |
|---|---|
| **5 — aptitude au fine-tuning** | SFT, DPO, ORPO, SimPO, KTO, GRPO ; LoRA/QLoRA ; 23 méthodes, 163 recettes annoncées. Entraîne sur une carte modeste (4 Go annoncés, 3,32 Go mesurés) **ou via MLX sur Apple M1–M4**, sans CUDA. |
| **6 — maturité d'écosystème** | Le point fort du relevé : **un même outil couvre CUDA et MLX**, avec un papier, des archives de mesure publiées et une validation externe. C'est exactement « constaté sur un projet réel, pas sur une réputation ». |
| **11 — étanchéité §VI** | Exécution locale, hors ligne, télémétrie éteinte par défaut. **Mais** : entraîner sur le corpus du dépôt (U4) produit un **artefact dérivé qui porte le corpus** — un adaptateur de poids. Le dépôt n'a aujourd'hui aucun régime pour cet objet. C'est une **question ouverte**, pas un constat à trancher ici (Cmd 12, Cmd 13). |
| **12 — charge d'exploitation** | Stack Python lourde (extras `train` / `serve` / `ui`), cadence de publication cassante : toute utilisation exigerait une version **épinglée** et un **re-run des evals**. |
| Option **E** (GPU à l'heure, rouverte sous condition) | Ce que la rafale louée laisse derrière elle — l'adaptateur, le GGUF — **reste un bien**. L'objection de Sidy (« du matériel dont on n'est pas propriétaire ») porte sur la **capacité permanente**, moins sur l'artefact intermittent. Cela **n'ouvre ni ne ferme** E : cela n'informe que la jambe entraînement. |
| Options **A / B** (Mac) | La compatibilité MLX native est le seul élément de ce relevé qui parle directement à la branche Apple du chantier, et au back-end `mlx` du CLI. |

**Ce que ce relevé ne fait pas** : il **ne remplit aucune cellule** de la matrice
(pas construit), il **ne lève pas `OUT-07`** (AngelSpec reste `bloque` sur l'absence
d'inférence locale : ceci documente l'outillage d'entraînement, pas l'inférence), et il
**ne préjuge pas** de la charge de référence — laquelle reste la question 1 en attente.

## 6. Zones d'ombre et ce qui n'a pas été relevé

- Projet de **sept mois**, **un mainteneur principal** face à 61 contributeurs, une
  société derrière : la continuité n'est pas garantie par la seule licence Apache-2.0.
- `/zero` annonce « un clic vers des GPU cloud que vous contrôlez » : surface
  commerciale **future** possible, donc lieu de réintroduction d'un tiers.
- Compteurs marketing non calibrés (95,4 k contre 33 338 miroirs exclus).
- **Non relevé** dans cette passe : coût réel d'usage, sécurité de la chaîne de
  publication PyPI (attestations non vérifiées), état de l'issue amont
  `bitsandbytes#2034`, comportement réel sur Apple Silicon (aucun Mac dans le parc),
  coût de maintenance récurrent.
- **Non éprouvé** : rien n'a été installé ni exécuté. Le seul poste physique est le
  serveur Hetzner — **aucun GPU**, 3,7 Gio de RAM, 8,3 Gio de disque libres :
  l'éprouve en sandbox est hors de portée aujourd'hui, comme pour `INF-16` entier.

## 7. Verdict

**Retenu** comme référence technique du chantier `INF-16`, pour les **critères 5 et
6** principalement. **Rien à engager** : aucune machine n'existe, la charge de
référence n'est pas arrêtée, et ce relevé ne crée aucune obligation.

**Statut** : `exploratoire` — au sens de la charte de `veille/` (point 3), aucune
fiche de veille n'est close tant que le projet n'a pas été éprouvé en sandbox ou
invalidé. La reprise naturelle de cette fiche est le jour où une machine est choisie :
c'est alors qu'elle devient une ligne de matrice.
