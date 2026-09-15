---
title: "INF-16 — Machine d'IA locale et développement SLM : spécification"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, spec, slm, materiel, comparaison]
created: 2026-09-07
updated: 2026-09-15
sources:
  - "https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/"
  - "https://www.macworld.com/article/2973459/2026-mac-studio-m5-release-date-specs-price-rumors.html"
  - "https://petapixel.com/2026/08/25/apples-new-mac-studio-supports-up-to-512gb-of-unified-memory/"
  - "https://www.macrumors.com/roundup/mac-mini/"
  - "https://www.mindstudio.ai/blog/apple-mac-studio-mini-pricing-specs"
links:
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]]"
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/infrastructure/cartographie-routing-infrastructure]]"
  - "[[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]]"
---

# INF-16 — Machine d'IA locale et développement SLM : spécification

## Comportement observable

Le chantier ne produit pas de logiciel : il produit une **décision instruite**.
Vu du dehors, il rend trois choses, et rien d'autre :

1. Une **charge de référence** écrite : la liste arrêtée des usages que le
   dispositif doit servir, chacun avec la façon dont on constatera qu'il est
   servi. Sans elle, comparer des machines revient à comparer des chiffres sans
   objet.
2. Une **matrice options × critères** (§ci-dessous), dont chaque cellule est
   mesurée, ou sourcée et datée, ou marquée non relevée.
3. Une **recommandation argumentée** — proposée, jamais tranchée (Cmd 13).

## Les options à explorer

Sept options, tenues ouvertes jusqu'à la matrice remplie. Aucune n'est écartée
d'avance ; l'ordre ci-dessous n'est pas un classement.

| Réf. | Option | Ce qui devient local | Ce qui reste chez un tiers |
|---|---|---|---|
| **A** | Mac Studio (M5 Max / M5 Ultra) | SLM **et** modèles de référence larges (jusqu'à 512 Go de mémoire unifiée) | rien d'obligé — le LLM cloud devient facultatif |
| **B** | Mac mini (M6 ou M5 Pro) + LLM cloud (hypothèse de Sidy) | le SLM seul | le LLM : abonnements/API |
| **C** | Poste NVIDIA mono-GPU (24–32 Go de VRAM) | le SLM, entraînement compris, en écosystème CUDA | le LLM, sauf modèle ouvert de taille moyenne quantifié |
| **D** | Serveur GPU dédié loué (hébergeur) | le SLM, mais **chez un tiers** — souveraineté d'usage, pas de possession | le matériel lui-même, et le LLM — ⚠ voir le verdict ci-dessous |
| **E** | GPU à l'heure (RunPod, Vast, Lambda) pour rafales d'entraînement | rien en continu ; l'entraînement ponctuel seulement | tout le reste — ⚠ écartée puis **rouverte sous condition** le 2026-09-07 : justifiable en complément de B, jamais seule (voir ci-dessous) |
| **F** | Statu quo — aucune machine, montée de RAM du Hetzner seule | rien | tout (état actuel) — **c'est la référence à battre** |
| **G** | Combinaisons étagées (ex. B maintenant + C plus tard ; ou E pour entraîner + B pour servir) | selon l'étage | selon l'étage |

### Verdict de Sidy du 2026-09-07 — l'option E est fermée

Le motif de la suspension des containers GPU cloud, qui manquait au dépôt
(`to-source` levé ce jour par Sidy en session), tient en trois points :

1. **Configuration trop fastidieuse** dans l'état actuel du setup — le poste de
   travail est un iPad, aucune machine locale n'accompagne la mise en route.
2. **Facturation même à l'arrêt** : le conteneur éteint continue de coûter.
3. **Coût disproportionné pour du matériel dont on n'est pas propriétaire.**

Le troisième point n'est pas une remarque de circonstance : c'est un **critère**,
et il ne vise pas que E. Il frappe **l'option D de la même façon** — un serveur
GPU dédié est loué au mois, qu'on s'en serve ou non, et ne devient jamais un
bien. La conséquence est portée dans la matrice au critère 10 (réversibilité),
pas seulement au critère 2 (coût).

Statut retenu ce jour-là : **E écartée comme solution permanente**. Elle reste
mentionnée dans la matrice — un chantier de comparaison consigne pourquoi une
option tombe, il ne l'efface pas (Cmd 10). **D reste ouverte jusqu'à
confirmation de Sidy** : le même critère semble l'emporter, mais l'écarter
serait une décision, pas un relevé (Cmd 13).

### Révision du même jour — E rouverte sous condition

Sidy revient sur ce verdict quelques heures plus tard, en session : « il y avait
quelque chose que je n'avais pas tout à fait compris concernant l'option du GPU
Cloud dans la perspective spécifique du développement SLM — effectivement c'est
une option qui peut se justifier dans le contexte du setup Mac Mini ».

Les deux verdicts sont conservés, datés, dans leur ordre : le second ne
disqualifie pas le premier, il en **borne la portée**. Ce qui change tient à la
condition, et elle est précise :

- **L'objection 1 tombe dans le scénario B.** « Configuration trop fastidieuse
  dans l'état actuel du setup » visait un setup où le seul poste est un iPad.
  Un Mac Mini fournit la station de travail qui manquait : la mise en route d'un
  GPU distant cesse d'être fastidieuse quand une vraie machine locale la pilote.
  L'objection était **conditionnelle au setup**, pas intrinsèque à l'option.
- **Les objections 2 et 3 ne tombent pas — elles se repondèrent.** La
  facturation à l'arrêt et l'absence de propriété restent vraies. Mais elles
  pèsent contre une capacité *permanente* louée ; elles pèsent beaucoup moins
  contre des **rafales d'entraînement**, intermittentes par nature, quand le
  service courant tourne, lui, sur une machine possédée.
- **La perspective SLM est ce qui rend la distinction opérante.** Servir un SLM
  (U1, U2, U3) demande une capacité continue et modeste : la place d'une machine
  possédée. Entraîner ou affiner (U4, U5) demande une capacité forte et rare :
  la place, précisément, d'un GPU pris à l'heure. Ce n'est pas la même charge, ce
  n'est pas le même matériel — les traiter comme une seule question était
  l'erreur d'origine, des deux côtés.

**Statut de E au 2026-09-07, après révision** : `rouverte sous condition` —
justifiable **en complément** de l'option B (Mac Mini), pour l'entraînement
seulement, jamais comme capacité de service permanente. Elle reste écartée si
elle est prise isolément, ce qui était le cadre du premier verdict.

**Conséquence sur l'option G** (montages étagés) : elle cesse d'être une case de
complétude pour devenir l'hypothèse la plus consistante à instruire — machine
possédée pour servir, GPU loué par rafales pour entraîner, LLM cloud pour le
raisonnement lourd. À instruire, pas à retenir : la matrice n'est pas remplie.

## Les critères de comparaison

Douze critères. Chacun doit être renseignable par une valeur constatable — un
critère qui ne l'est pas est retiré plutôt que rempli au jugé.

| # | Critère | Comment il se renseigne |
|---|---|---|
| 1 | **Degré de souveraineté** | quelle couche (SLM / LLM / donnée) cesse de dépendre d'un tiers — énoncé, pas noté |
| 2 | **Coût d'acquisition** | prix relevé, daté, avec sa source |
| 3 | **Coût récurrent** | abonnements + API + électricité + hébergement, sur 12 et 36 mois |
| 4 | **Mémoire accessible au modèle** | Go réellement disponibles au modèle (VRAM ou mémoire unifiée), et bande passante |
| 5 | **Aptitude au fine-tuning** | pas seulement « fait tourner » : entraîne-t-on dessus, et à quelle taille de modèle |
| 6 | **Maturité de l'écosystème** | CUDA / MLX / autre, pour la tâche visée — constaté sur des projets réels, pas sur une réputation |
| 7 | **Bruit et lieu** | niveau sonore sous charge soutenue ; contrainte réelle vu la proximité du studio |
| 8 | **Consommation électrique** | watts sous charge, et coût annuel qui en découle |
| 9 | **Délai de disponibilité** | date d'expédition réelle de la configuration visée |
| 10 | **Réversibilité (Cmd 10)** | ce qui reste si l'on change d'avis à 6 mois : valeur de revente, engagement, verrou de format |
| 11 | **Étanchéité §VI** | ce qui sort du dépôt vers un tiers, et sous quelle garantie |
| 12 | **Charge d'exploitation** | qui l'entretient, et ce que ça ajoute à une infrastructure déjà tendue |

## Relevé du 2026-09-15 — outillage de post-entraînement (critères 5, 6, 11)

Relevé d'une source externe, sur lien pointé par Sidy en session et validé pour
consignation : [[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]]
(Soup CLI, Apache-2.0). **Il ne remplit aucune cellule** de la matrice — une cellule
demande une valeur mesurée ou sourcée et datée, pas une aptitude générale — mais il
informe trois critères :

- **5 (aptitude au fine-tuning)** : un unique outil en ligne de commande couvre SFT,
  DPO, ORPO, SimPO, KTO et GRPO en LoRA/QLoRA, et prétend entraîner un 8B quantifié
  sur 4 Go de VRAM (3,32 Go de pic mesuré, répliqué sur du matériel loué).
- **6 (maturité d'écosystème)** : le fait notable est la couverture **CUDA *et* MLX
  Apple** par le même outil, papiers et archives de mesure publiés — constat sur un
  projet réel, non sur une réputation.
- **11 (étanchéité)** : exécution locale et hors ligne, télémétrie éteinte par défaut ;
  mais un entraînement sur le corpus du dépôt produirait un **artefact dérivé portant
  le corpus**, objet dont le dépôt n'a pas encore de régime. **Question ouverte**, non
  tranchée ici (Cmd 12, Cmd 13).

**Ce que ce relevé ne fait pas** : il ne lève pas `OUT-07` (AngelSpec reste `bloque`
sur l'absence d'inférence locale) et il ne préjuge pas de la charge de référence, qui
reste la question 1 en attente.

## Ce qui est déjà établi (relevé du 2026-09-07)

Valeurs sourcées ce jour, à re-vérifier avant tout engagement — un prix est une
photographie :

| Fait | Valeur | Source |
|---|---|---|
| Mac Studio M5 Max / M5 Ultra — annonce | 25 août 2026 | Apple Newsroom |
| Mac Studio — expédition des configurations standard | 22 septembre 2026 | Macworld |
| Mac Studio — configuration 512 Go de mémoire unifiée | fin octobre 2026 | Macworld |
| Mac Studio M5 Ultra — cœurs | 36 CPU / 80 GPU | Apple Newsroom |
| Mac Studio — mémoire unifiée maximale et bande passante | 512 Go, 1,2 To/s | PetaPixel, Apple |
| Mac Studio — prix d'entrée | 2 499 $ (relevé à 1 999 $ avant juin 2026) | Macworld |
| Mac mini — gammes | M6 (16–32 Go) ou M5 Pro (jusqu'à 64 Go, 307 Go/s) | MacRumors, MindStudio |
| Mac mini M6 — prix d'entrée | 899 $ | MindStudio |
| Mac mini — lancement | 22 septembre 2026 | MindStudio |

**Non relevé à ce stade, donc absent de la matrice** : prix des paliers Apple
au-delà de l'entrée de gamme (c'est pourtant là que se joue la comparaison) ;
prix des cartes NVIDIA neuves et d'occasion ; tarifs des hébergeurs GPU ;
consommation électrique de chaque option ; **coût récurrent réel de la couche
modèle actuelle**. Aucune de ces valeurs ne sera écrite de mémoire (Cmd 5).

## Relevés du 2026-09-15 — étapes 2, 3b et 3c (exécutées sans aucun verdict)

> **Ce que cette section est** : les trois relevés que le `plan.md` déclarait faisables
> « entre deux reprises », sans dépendre d'aucune décision. **Ce qu'elle n'est pas** :
> la matrice de l'étape 5 — elle n'existe pas encore (`matrice.md` **à créer** à cette
> étape, jamais avant), et **aucune cellule n'est déclarée remplie ici**. Ces valeurs
> l'alimenteront, chacune avec sa source et sa date.
>
> **Règle de lecture** : un prix est une photographie. Rien ci-dessous n'est écrit de
> mémoire (Cmd 5) ; là où deux sources se contredisent, l'écart est **porté**, pas
> lissé (§VII, stratification de crédibilité).

### A. Prix — étape 2

**A1 · Apple — option A (Mac Studio), option B (Mac mini).** Annonce du 2026-08-25,
mise en vente générale le **2026-09-22**. Prix constructeur, USD, hors taxes.

| Configuration | Prix | Mémoire unifiée | Bande passante | Source |
|---|---|---|---|---|
| Mac mini M6 (12 cœurs CPU) | **899 $** (799 $ éducation) | 16 → **32 Go** | 170 Go/s | MacObserver, 2026-09-12 |
| Mac mini M5 Pro | **1 699 $** (1 599 $ éducation) | jusqu'à **64 Go** | 307 Go/s | MacObserver, RedShark |
| Mac Studio M5 Max (18 cœurs) | **2 499 $** (2 299 $ éducation) | jusqu'à **128 Go** | 614 Go/s | MacObserver, RedShark, Apple |
| Mac Studio M5 Ultra (36 cœurs) | **5 499 $** (5 099 $ éducation) | jusqu'à **512 Go** | 1,2 To/s | MacObserver, RedShark, Apple |

Paliers mémoire et disponibilité (AppleInsider, 2026-08-25) :
- le M5 Ultra **part de 96 Go** ; le passage 96 → **256 Go coûte 4 000 $** ;
- la configuration **512 Go n'est pas pré-commandable** — Apple annonce « fin octobre »
  sans publier de prix ; c'est précisément le palier où se joue l'option A ;
- configuration maximale commandable au 2026-09-15 : **18 299 $**
  (M5 Ultra 36 cœurs + 256 Go + 16 To) — arithmétique vérifiée :
  5 499 + 1 300 (CPU/GPU) + 4 000 (96→256 Go) + 7 500 (1 To→16 To).
- AppleInsider **estime** que le 512 Go portera la machine « bien au-delà de 20 000 $ » :
  c'est une estimation de presse, **pas un prix**, et elle est marquée comme telle.

*Non relevé* : prix des paliers mémoire du Mac mini ; prix du SSD hors le palier cité ;
prix hors États-Unis et hors Apple Store éducation.

**A2 · NVIDIA — option C (poste mono-GPU).** Marché du 2026-09-15, **volatil** (pénurie
documentée, hausses en cours).

| Carte | Mémoire | Prix relevé | Crédibilité |
|---|---|---|---|
| RTX PRO 6000 Blackwell | 96 Go GDDR7 ECC | **≈ 16 000 $** (TweakTown : +87 % sur le MSRP de lancement ; NVNexus affiche 16 843,20 $ le même jour) | deux sources marchandes concordantes — **à re-relever** |
| RTX 5090 | 32 Go | **disputé** : MSRP 1 999-2 000 $ · XDA « ≈ 3 500 $ au minimum » · Tom's Hardware « au moins 5 000 $ », jusqu'à 9 500 $ chez des revendeurs tiers | le MSRP est certain ; les prix de rue divergent d'un facteur ≈ 3 selon source et canal — **non tranché** |
| RTX 3090 d'occasion | 24 Go | **≈ 800 $** (XDA, eBay) | écosystème Ampere mature ; **deux cartes = 48 Go pour ≈ 1 600 $** |

**A3 · GPU loué par heure — options D et E.** Tarifs à la demande, GPU seul, relevés
« revus le 2026-09-11 » :

| GPU | Fourchette à l'heure | Points |
|---|---|---|
| H100 80 Go | **2,99 $** (Vultr) → **10,98 $** (Google Cloud) | Runpod 3,49 $ · Lambda 3,29 $ · Vast 5,65 $ · médiane ≈ 4-5 $ |
| A100 80 Go | **1,09 $** (Thunder Compute) → 5,07 $ | fourchette de marché, septembre 2026 |

Lecture : 40 h d'entraînement sur H100 = **120 à 140 $** selon l'hébergeur. L'heure n'est
donc **pas** l'obstacle : le verdict du 2026-09-07 portait sur la **propriété** et la
**friction de configuration**, pas sur le prix du calcul. Ce relevé ne rouvre ni D ni E —
il donne à la matrice les valeurs qui leur manquaient.

### B. Corpus servable — étape 3b (mesuré le 2026-09-15, par script)

| Circuit | Fichiers `.md` | Caractères |
|---|---|---|
| `textes/` | 732 | 23 104 279 |
| `atelier/` | 421 | 7 085 544 |
| `doctrinal/` | 362 | 3 244 525 |
| `meta/` | 172 | 2 848 505 |
| `hermeneutique/` | 29 | 213 198 |
| `label/` | 14 | 60 802 |
| `protocoles/` | 10 | 25 143 |
| **Total** | **1 741** | **36 592 746** |

Forme : 193 fiches < 2 Ko · 686 de 2 à 10 Ko · 726 de 10 à 50 Ko · 136 > 50 Ko.
Le rapport du 2026-09-07 annonçait « 560 fichiers » dans `textes/` ; le compte réel du
2026-09-15 est **732** — c'est une croissance, pas une contradiction.

*Estimation, et non mesure* : sans tokenizer appliqué, on ne peut donner qu'un ordre de
grandeur. À 3,5-4,5 caractères par token en français, `textes/` ≈ **5,1 à 6,6 M tokens**
et l'ensemble du dépôt ≈ **8,1 à 10,5 M tokens**. Le seul chiffre mesuré est celui des
caractères ; tout token avancé ailleurs serait une estimation déguisée.

**Deux réserves à porter, non tranchées ici :**

1. **Droits.** `textes/` contient des œuvres converties dont certaines sont sous droits
   (Shayegan, entre autres). Un entraînement dessus n'est pas un usage privé de lecture :
   la question s'instruit **avant** U4, elle ne se tranche pas d'office (Cmd 12, Cmd 13).
2. **Étanchéité (§VI).** `meta/` porte du personnel et les motifs privés des décisions
   publiques : **inconcevable dans un corpus d'entraînement**, quelle que soit l'option
   retenue. L'énumération ci-dessus vaut donc comme **mesure de volume**, jamais comme
   liste de ce qui serait entraînable. Et l'artefact d'un entraînement sur `doctrinal/`
   **porterait** le corpus : question laissée ouverte par la veille du 2026-09-15
   ([[atelier/rd/veille/2026-09-15_soup-cli-post-entrainement-local]], critère 11).

### C. Mémoire des modèles candidats — étape 3c

**Méthode** : les `config.json` publiés (Qwen3 dense, Hugging Face) sont récupérés, la
taille de paramètres est **calculée** depuis la configuration, puis la mémoire est
`paramètres × octets par paramètre`. Le nom commercial n'est pas pris pour la mesure —
il est recoupé : les valeurs calculées (0,60 · 1,72 · 4,02 · 8,19 · 14,77 · 32,76 Md)
s'écartent du nom de la part des têtes d'embedding non liées, ce qui est attendu.

| Modèle | Params (calculés) | bf16 | int8 | 4 bits | KV cache bf16 / token |
|---|---|---|---|---|---|
| Qwen3-0.6B | 0,60 Md | 1,19 Go | 0,60 Go | 0,30 Go | 112 Kio |
| Qwen3-1.7B | 1,72 Md | 3,44 Go | 1,72 Go | 0,86 Go | 112 Kio |
| Qwen3-4B | 4,02 Md | 8,04 Go | 4,02 Go | 2,01 Go | 144 Kio |
| Qwen3-8B | 8,19 Md | 16,38 Go | 8,19 Go | 4,10 Go | 144 Kio |
| Qwen3-14B | 14,77 Md | 29,54 Go | 14,77 Go | 7,38 Go | 160 Kio |
| Qwen3-32B | 32,76 Md | 65,52 Go | 32,76 Go | 16,38 Go | 256 Kio |

Le cache KV n'est pas un détail : il ne se quantifie pas comme les poids et il croît
**linéairement avec le contexte**.

| Modèle | 8k de contexte | 32k | 128k |
|---|---|---|---|
| Qwen3-4B / 8B | 1,21 Go | 4,83 Go | 19,33 Go |
| Qwen3-32B | 2,15 Go | 8,59 Go | 34,36 Go |

*Ce qui n'est pas relevé, et le restera jusqu'à la voie 4a/4b/4c* : les **débits**
(tokens/s), les latences et la qualité après quantification. Ce sont des mesures tierces
ou des mesures à faire — la voie 4a exige qu'elles soient marquées comme telles, jamais
fondues avec du mesuré (§VII).

### Ce que ces relevés changent — et ce qu'ils ne changent pas

Ils donnent des valeurs datées aux **critères 2 (coût d'acquisition), 3 (coût récurrent)
et 4 (mémoire accessible et bande passante)**, et ils éclairent deux faits qui n'étaient
pas visibles avant :

- **le prix se joue sur la mémoire, pas sur la machine** : passer de 96 à 256 Go coûte
  4 000 $ sur un Mac Studio, soit plus que le prix d'un Mac mini M5 Pro entier — ce qui
  éclaire directement l'option U5 (distillation) et le dimensionnement de l'option A ;
- **la mémoire par dollar la moins chère du relevé est l'occasion** : deux RTX 3090
  (48 Go) pour ≈ 1 600 $, dans l'écosystème CUDA le plus mûr — mais c'est une option C
  (poste mono-GPU, ici bi-GPU), donc une machine à posséder et à entretenir.

Ils **ne décident rien** : ils ne remplissent aucune cellule de la matrice, ne tranchent
ni D ni E, ne préjugent pas de la voie de mesure de l'étape 4, et ne dispensent pas de la
question 1 — la charge de référence, qui reste la seule à commander la taille de modèle,
donc la machine, donc le prix.

## Charge de référence — les candidats à arrêter

Cinq usages possibles, tirés des besoins réels du dépôt. Sidy arrête lesquels
comptent : c'est ce choix qui décide de la taille de modèle, donc de la machine.

| Réf. | Usage | Pourquoi il est candidat | Exigence matérielle pressentie |
|---|---|---|---|
| U1 | **Tri et routage des tâches des profils Hermes** | l'essentiel du travail des 12 profils est de l'orchestration, pas du raisonnement de frontière ; c'est aujourd'hui envoyé à Qwen/OmniRoute avec les fragilités mesurées | faible — un SLM de petite taille suffit |
| U2 | **Filtre d'étanchéité §VI avant tout envoi externe** | la règle « aucun fait personnel dans une page neutre » est aujourd'hui tenue **par protocole, jamais vérifiée mécaniquement** ; un modèle local pourrait la contrôler avant qu'une requête parte chez un tiers | faible, mais exige une fiabilité éprouvée (§VII) |
| U3 | **Recherche sémantique sur le dépôt** | le graphe actuel est **lexical** : il compte des liens, il ne comprend pas. 709 fiches + 560 textes convertis sans recherche par le sens | faible (embeddings) |
| U4 | **Fine-tuning d'un SLM sur le corpus du dépôt** | c'est le « développement SLM » au sens propre, et la seule ligne qui justifie une machine plutôt qu'un abonnement | moyenne à forte — le critère dimensionnant |
| U5 | **Distillation depuis un modèle large tenu localement** | seule justification d'une très grande mémoire unifiée (option A) : charger un gros modèle de référence pour en tirer un SLM | forte — 100 Go et plus |

**Le point de bascule est là** : si U5 est retenu, l'option A se justifie ; s'il
ne l'est pas, la grande mémoire du Mac Studio est un surdimensionnement et
l'option B devient proportionnée. Ce n'est pas une question de budget mais de
programme.

## Données consommées / produites

- **Consommé** : les fiches d'infrastructure déjà au dépôt (cartographie du
  routing, incidents, veille AngelSpec), les relevés de `monitoring-archive/`,
  et des relevés de prix externes datés.
- **Produit** : les trois fiches du présent dossier, une entrée d'annales, une
  ligne au registre des chantiers. **Aucun code**, aucun artefact exécutable.
- Rien de ce chantier ne touche `instrument-donnees.yaml`, le manifeste, ni le
  dépôt frère : le sens unique `dépôt → manifeste → interface` n'est pas
  concerné ici.

## Critères d'acceptation

1. La charge de référence est écrite et **visée par Sidy** — vérifiable :
   `grep -n "charge de reference arretee" atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan.md`
   rend une ligne datée du verdict.
2. La matrice porte les 7 options en lignes et les 12 critères en colonnes,
   sans cellule vide : toute cellule non mesurée porte la mention explicite
   « non relevé » — vérifiable à la lecture, aucune cellule blanche.
3. Chaque valeur de prix porte sa source et sa date de relevé — vérifiable :
   aucun nombre monétaire de la matrice n'apparaît sans lien ni date.
4. L'option F (statu quo) est renseignée **au même titre que les autres** — elle
   est la référence à battre, pas un repoussoir.
5. Le coût récurrent actuel de la couche modèle est un **relevé**, pas une
   estimation : la fiche nomme d'où le chiffre vient.
6. `python3 verifier-invariants.py --racine /root/wiki` rend 0 erreur sur les
   fiches du chantier.
7. La ligne `INF-16` du registre pointe vers ce dossier et porte le statut réel
   du jour — vérifiable : `grep -n "INF-16" atelier/rd/registre-chantiers.md`.

## Cas limites

- **Une configuration visée n'est pas disponible dans la fenêtre voulue** (cas
  réel : les 512 Go du Mac Studio glissent à fin octobre). Le délai est un
  critère, pas une note de bas de page.
- **Le prix bouge entre le relevé et la décision.** Toute valeur porte sa date ;
  une matrice de plus de quelques semaines se re-relève avant d'engager.
- **Le marché de l'occasion** (cartes NVIDIA d'ancienne génération) change le
  classement du critère 2 sans changer les autres — il est traité comme une
  variante d'option, jamais comme une remise.
- **Une option semble gagner sur tous les critères.** C'est le signal d'un
  critère mal choisi ou d'une valeur non relevée, pas d'une évidence : reprendre
  la matrice avant de conclure.
- **Souveraineté partielle** : les options B, D, E et F laissent la couche LLM
  chez un tiers. Ce n'est pas disqualifiant — c'est l'état actuel — mais cela
  s'inscrit en toutes lettres au critère 1, jamais en note de bas de page.

## Ce qui reste `to-source`

- ~~Le motif de la **suspension des containers GPU cloud**~~ — **levé le
  2026-09-07** par Sidy en session : configuration trop fastidieuse dans l'état
  du setup, facturation maintenue à l'arrêt, coût disproportionné pour du
  matériel non possédé. Consigné au §*Verdict de Sidy* ci-dessus.
- Les **débits réels** (tok/s en inférence, durée d'un fine-tuning de référence)
  par famille de matériel : aucune valeur publiée ne remplace une mesure sur la
  charge de référence retenue. Marqués `to-source` jusqu'à l'essai de l'étape 4
  du plan.
- La **consommation électrique** de chaque option sous charge soutenue, et le
  tarif applicable — sans quoi le critère 8 reste vide.
