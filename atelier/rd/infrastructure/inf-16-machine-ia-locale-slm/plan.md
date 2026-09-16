---
title: "INF-16 — Machine d'IA locale et développement SLM : plan"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, plan, slm, materiel]
created: 2026-09-07
updated: 2026-09-15
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# INF-16 — Machine d'IA locale et développement SLM : plan

> **Statut** : `vise` — **visa donné par Sidy en session le 2026-09-15** (« Tu peux
> passer le plan à visé »), après lecture. Ce chantier ne produit pas de code ; ce que
> le visa autorise ici, c'est l'**ordre des étapes** et les **dépenses de mesure** de
> l'étape 4 — dont **aucune** n'a été engagée à ce jour.
>
> *Historique* : le plan est resté `brouillon` du 2026-09-07 au 2026-09-15. L'état
> antérieur n'est pas effacé — il est dans git et dans les annales.

## Point de reprise — où en est le chantier

> **Lire ceci d'abord.** Chantier explicitement mené **par reprises successives**
> (demande de Sidy, 2026-09-07 : « je n'ai pas le temps de continuer là-dessus
> pour le moment, consigne le projet pour qu'on puisse y revenir au fur et à
> mesure »). Cette section est tenue à jour à chaque reprise et dit, en un coup
> d'œil, ce qui est acquis et ce qui attend. Elle **résume, elle ne remplace
> pas** les sections ci-dessous.

**État au 2026-09-15** — plan **visé**, trois relevés exécutés, **aucune dépense
engagée**.

*Ce qui a changé depuis le 2026-09-07 :*

1. **Le plan est visé** (Sidy, en session, 2026-09-15) : l'ordre des étapes et les
   dépenses de mesure de l'étape 4 sont autorisés. **Aucune n'a été engagée.**
2. **Les étapes 2, 3b et 3c sont faites** — relevés consignés au `spec.md`,
   § *Relevés du 2026-09-15* : prix Apple / NVIDIA / GPU loués (sourcés et datés),
   volume et forme du corpus (mesurés par script), mémoire des modèles candidats
   (calculée depuis les `config.json` publiés).
3. Deux faits neufs que ces relevés rendent visibles : le prix d'un Mac Studio se joue
   sur la **mémoire** (96 → 256 Go = 4 000 $, plus qu'un Mac mini M5 Pro entier) ; et la
   **mémoire par dollar la moins chère est l'occasion** (2 × RTX 3090 = 48 Go pour
   ≈ 1 600 $).
4. Deux réserves **portées, non tranchées** : les **droits** sur une partie de
   `textes/`, à instruire avant tout U4 ; l'**exclusion de `meta/`** de tout corpus
   d'entraînement (§VI).
5. **Un devis existe, et attend d'être lu** —
   [[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/devis-rafale-runpod-2026-09-16]] : une
   rafale d'entraînement sur GPU loué, chiffrée de ≈ 4 $ (A6000) à ≈ 28 $ (H100), scénario
   recommandé ≈ 11 $ (A100, 8 h), avec la discipline de facturation (**détruire, jamais
   arrêter** : 50 Go de volume arrêtés coûtent 10 $/mois). Demande de Sidy dans la nuit du
   15 au 16 septembre 2026 : « préparer le devis seul, et je tranche après l'avoir lu ».
   **Rien n'est lancé, aucun compte n'existe, rien n'est engagé.**
6. **E est ouverte** — **troisième verdict de Sidy, 2026-09-16** : « On ouvre à nouveau
   l'option E. » La rafale GPU à l'heure n'est plus subordonnée à l'existence préalable
   d'une machine possédée. Le devis est prêt ; **les préalables du run restent à faire**
   (jeu de données, jeu d'évaluation, runbook d'entraînement) et **la dépense reste sous
   porte humaine** (Cmd 13).
7. **Les trois préalables du devis sont faits — sauf le compte.** Le **jeu de données** est
   constitué **par script** (872 enregistrements, 11,5 Mo, empreinte `c776d5e213814c48…`,
   écrit **hors du dépôt** ; deux gardes éprouvées par leur refus) ; le **jeu d'évaluation**
   est écrit et émis (13 tâches, quatre familles) ; le **runbook d'entraînement** est écrit.
   Restent le **choix du modèle de base** (proposé : Qwen3-8B) et le **compte RunPod** —
   c'est **lui**, l'engagement.

*Ce qui n'a pas changé :* les quatre questions en attente ci-dessous — dont la
question 1, la seule à commander la taille de modèle, donc la machine, donc le prix ; le
choix de la voie 4a / 4b / 4c ; et la règle qu'**aucun prix ne s'engage sans re-relevé**
(le marché NVIDIA est en pénurie ouverte).

*Ce qui reste faisable sans verdict :* l'**étape 3a** — et elle attend **vos chiffres**
(abonnements, API) ; et, si vous le voulez, les **préalables du devis** (§5 : jeu de
données, jeu d'évaluation, runbook d'entraînement, tous gratuits en argent). Les
étapes 2, 3b et 3c sont faites.

*Prochaine action, inchangée :* répondre à la question 1. **Une seule ligne suffit.**

**État au 2026-09-07** — chantier ouvert, aucune dépense engagée, aucune décision
prise.

*Acquis (ne pas réinstruire) :*

1. Le serveur Hetzner ne peut rien porter — pas de GPU, RAM déjà saturée. Toute
   option passe par une machine nouvelle ou par du calcul distant.
2. Sept options et douze critères sont posés (`spec.md`). Aucune cellule de la
   matrice n'est encore remplie.
3. Le GPU à l'heure (E) a été **écarté puis rouvert sous condition** le même
   jour. Fond retenu : servir un SLM et l'entraîner sont deux charges
   différentes — capacité continue et modeste d'un côté, forte et rare de
   l'autre. Les confondre était l'erreur d'origine.
4. Un critère est né du premier verdict et vaut désormais pour tout le
   chantier : **ce qui est loué ne devient jamais un bien**. Il pèse sur D
   autant que sur E.
5. L'option **G** (montage étagé) est, à ce stade, l'hypothèse la plus
   consistante — machine possédée pour servir, GPU loué par rafales pour
   entraîner, LLM cloud pour le raisonnement lourd. **Hypothèse, pas verdict.**

*En attente de Sidy, par ordre de blocage :*

| # | Question | Pourquoi elle bloque |
|---|---|---|
| 1 | **La charge de référence** : lesquels des cinq usages U1–U5 comptent ? | Commande la taille de modèle, donc la machine, donc le prix. Rien ne peut être comparé avant. |
| 2 | Le **budget** ou sa fourchette | Sans elle, la matrice classe sans pouvoir conclure (Cmd 13). |
| 3 | Le sort de l'**option D** (serveur GPU loué au mois) | Le critère de propriété semble l'emporter, mais l'écarter serait une décision, pas un relevé. |
| 4 | Le **lieu d'installation** (proximité du studio → le bruit est-il une contrainte réelle ?) | Renseigne le critère 7. |

*Prochaine action concrète, dès qu'il y a du temps* : répondre à la question 1.
Une seule ligne suffit — les usages retenus — et l'étape 2 (relevé des prix)
peut démarrer sans rien d'autre.

*Ce qui n'a pas besoin de Sidy et peut être fait entre deux reprises* : l'étape 2
(relever les prix datés et sourcés) et l'étape 3a (relever le coût récurrent
réel de la couche modèle actuelle). Ces deux relevés ne dépendent d'aucun
verdict et rempliraient déjà deux colonnes de la matrice.

## Étapes

**Étape 1 — Arrêter la charge de référence.** Sidy retient, parmi les cinq usages
candidats du `spec.md` (U1 tri des tâches Hermes, U2 filtre d'étanchéité, U3
recherche sémantique, U4 fine-tuning, U5 distillation depuis un modèle large),
ceux qui comptent. C'est la seule étape qui ne peut pas être préparée par la
machine : elle décide de la taille de modèle, donc de la machine, donc du prix.
La ligne de verdict est consignée ici même, **en début de ligne**, sous la forme
exacte `charge de reference arretee : <usages> — <date>`, que le critère
d'acceptation 1 va chercher (motif corrigé le 2026-09-15 : l'ancien contrôle
trouvait le gabarit et sa propre ligne de tableau, donc était vert par construction).

**Étape 2 — Relever les prix, datés et sourcés.** Pour chaque option A à G : prix
d'acquisition de la configuration réellement visée (pas l'entrée de gamme, qui
n'est presque jamais la configuration utile), et coût récurrent. Aucun prix écrit
de mémoire (Cmd 5). Ce relevé inclut les paliers Apple au-dessus de l'entrée de
gamme, les cartes NVIDIA neuves **et** d'occasion, et les tarifs d'hébergeurs
GPU.

**Étape 3 — Mesurer ce qui est mesurable sans rien acheter.** Trois mesures :
(a) le **coût récurrent réel actuel** de la couche modèle — relevé, jamais
estimé, en nommant sa provenance ; (b) le volume et la forme du corpus qui
servirait à U3/U4 (`textes/` : 560 fichiers versés le 2026-09-02 ; `doctrinal/`
et les autres circuits) ; (c) la taille mémoire des modèles candidats, d'après
leurs fiches publiées. Cette étape retire à elle seule plusieurs cellules du
« non relevé ».

**~~Étape 3 bis~~ — sans objet depuis le 2026-09-07.** Le motif de la suspension
des containers GPU cloud est établi (verdict de Sidy, §*Verdict* du `spec.md`) :
configuration trop fastidieuse, facturation maintenue à l'arrêt, coût
disproportionné pour du matériel non possédé. L'étape est conservée barrée
plutôt que retirée (Cmd 10) — c'est la trace de ce qui a été cherché.

**Étape 4 — refondue le 2026-09-07.** La version initiale prévoyait de louer
quelques heures de GPU cloud comme **instrument de mesure** avant tout achat.
Elle tombe : le premier point du verdict — la configuration fastidieuse — vaut
identiquement pour un essai d'une heure et pour un usage durable, et le
troisième vaut a fortiori pour une dépense qui ne laisse aucun bien. Prétendre
maintenir l'étape en la disant « petite » reviendrait à contourner le verdict
plutôt qu'à en tenir compte.

Il n'existe donc **plus de moyen de mesurer avant d'acheter**. C'est un fait du
chantier, pas un échec : il faut le porter, non le masquer. Trois voies de
remplacement, à trancher par Sidy :

| Voie | Ce qu'elle donne | Ce qu'elle coûte |
|---|---|---|
| **4a — Décider sur données publiées** | débits et durées repris de mesures tierces, sourcées et datées | ce ne sont pas *nos* mesures sur *notre* charge : la matrice le porte en toutes lettres, jamais fondu avec du mesuré (§VII) |
| **4b — La machine la moins chère devient l'instrument de mesure** | on acquiert d'abord le plus petit matériel qu'on voudrait de toute façon (option B), on y mesure la charge de référence réelle, et l'on ne décide qu'ensuite d'un éventuel palier supérieur | une dépense engagée avant la comparaison complète — mais sur un bien possédé, revendable, et utile même si le verdict final va ailleurs |
| **4c — Renoncer à la mesure préalable** | on tranche sur la seule matrice documentaire | risque assumé de surdimensionner ou de sous-dimensionner, à couvrir par le critère 10 (réversibilité) |

**La voie 4b mérite d'être regardée en premier** : elle retourne la contrainte
en méthode. Le matériel devient lui-même le banc d'essai, la dépense reste
proportionnée, et la réversibilité (Cmd 10) y est réelle — un bien possédé se
revend ou se réaffecte, une heure de location ne laisse rien. C'est aussi, dans
l'esprit du dépôt, un montage à blanc au sens propre : on éprouve avant
d'engager le gros.

**Révision du 2026-09-07 (même jour, second verdict de Sidy).** La location
horaire redevient disponible, mais **dans un ordre**, et cet ordre est le fond de
l'affaire : l'objection de configuration visait un setup où le seul poste est un
iPad ; une station de travail locale la lève. Donc la séquence n'est plus
« mesurer puis acheter », elle est **acquérir le petit poste, puis mesurer avec
lui — y compris à distance**.

Cela ne restaure pas la version initiale de l'étape 4 : elle prévoyait de louer
un GPU *pour décider s'il faut acheter*, ce que le premier verdict a rendu
impraticable et que le second ne rétablit pas. Ce qui devient possible est autre
chose — louer un GPU *depuis* la machine acquise, pour les rafales
d'entraînement que cette machine ne peut pas porter (U4, U5). La voie 4b et
l'option E cessent d'être concurrentes : elles s'enchaînent.

Garde maintenue quelle que soit la voie : **aucune matière de `meta/` ne quitte
le dépôt** (§VI), y compris pour un essai et y compris sous forme d'extrait.

**Signalé, non enregistré d'office (Cmd 12).** Le troisième verdict — **E ouverte** le
2026-09-16 — **rouvre une possibilité que cette étape avait fermée** : louer du GPU comme
**instrument de mesure** *avant* tout achat, ce qui était la version initiale de l'étape 4
(écartée le 2026-09-07 : la configuration était fastidieuse pour un setup sans machine
locale, et la dépense tombait sur du matériel non possédé). Ce n'est **pas** repris ici :
rouvrir une option n'est pas réinstruire une étape, et la voie de l'étape 4 (4a / 4b / 4c)
reste à trancher par Sidy. **Point signalé, à trancher.**

**Étape 5 — Remplir la matrice.** Les 7 options × 12 critères, chaque cellule
mesurée, sourcée+datée, ou explicitement « non relevé ». L'option F (statu quo)
est renseignée comme les autres.

**Étape 6 — Rendre la recommandation à Sidy.** Proposée, argumentée, jamais
tranchée (Cmd 13). Elle nomme l'option retenue **et** ce qu'elle coûte en
souveraineté : une option qui laisse la couche LLM chez un tiers est présentée
comme telle, en toutes lettres.

**Étape 7 — Clore.** Entrée d'annales avec le SHA (Cmd 9), ligne de registre mise
à jour dans la même passe, et **réouverture d'`OUT-07`** (speculative decoding)
si — et seulement si — l'option retenue apporte un GPU local.

## Fichiers touchés

| Fichier | Nature |
|---|---|
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent.md` | créé (2026-09-07) |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec.md` | créé (2026-09-07) |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan.md` | créé (2026-09-07), le présent fichier |
| `atelier/rd/registre-chantiers.md` | modifié — ligne `INF-16` + recomptage du §0 |
| `atelier/annales.md` | modifié — entrée append-only en tête (Cmd 9) |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/matrice.md` | **à créer** à l'étape 5, pas avant |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec.md` | modifié (2026-09-15) — relevés des étapes 2, 3b et 3c |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan.md` | modifié (2026-09-15) — visa (`brouillon` → `vise`) et point de reprise |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/devis-rafale-runpod-2026-09-16.md` | **créé** (2026-09-16) — devis d'une rafale d'entraînement RunPod, **en attente de lecture** |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/eval-jeu-de-taches-2026-09-16.md` | **créé** (2026-09-16) — jeu d'évaluation, **source de vérité** des tâches |
| `atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/runbook-rafale-entrainement-2026-09-16.md` | **créé** (2026-09-16) — runbook de la charge d'entraînement |
| `atelier/rd/outillage/generer-jeu-donnees-entrainement.py` | **créé** (2026-09-16) — constitution du jeu de données (déterministe, deux gardes **éprouvées par leur refus**) |
| `atelier/rd/outillage/generer-jeu-evaluation.py` | **créé** (2026-09-16) — émission du jeu d'évaluation depuis sa fiche (trois gardes **éprouvées par leur refus**) |

Rien n'est déplacé, rien n'est supprimé. Aucun fichier existant du pôle n'est
réécrit hormis le registre et les annales, chacun selon sa discipline propre
(révisable en place pour le registre, append-only en tête pour les annales).

## Vérification

| Ce qu'on vérifie | Commande exacte |
|---|---|
| Invariants du dépôt, fiches du chantier comprises | `python3 verifier-invariants.py --racine /root/wiki` |
| La ligne de registre existe et pointe ici | `grep -n "INF-16" atelier/rd/registre-chantiers.md` |
| Les trois fiches portent bien le champ `chantier:` | `grep -c "^chantier: INF-16" atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/*.md` → `1` par fichier |
| Hygiène Unicode (Cmd 15) | contrôle du hook `pre-push` versionné (`atelier/rd/outillage/hooks/`) |
| La charge de référence a bien été arrêtée (critère 1) | `grep -nE '^charge de reference arretee : [^<]' atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan.md` — **éprouvé le 2026-09-15** : refus (code 1) sur le plan non rempli, vert sur copie jetable portant une ligne remplie |

**Ce que ces contrôles ne prouvent pas** : ils portent sur la forme des fiches,
jamais sur la justesse d'un prix ou d'une mesure. Aucun script ne peut vérifier
qu'un tarif relevé est le bon — c'est la source datée qui en répond, et elle se
re-relève avant d'engager. Le dire ici évite de prendre un vert de forme pour
une validation de fond (§VII, épreuve des contrôles).

Si l'étape 4 produit un contrôle mécanique (par exemple un garde-fou de filtrage
pour U2), son **refus devra avoir été observé** sur une faute fabriquée exprès,
en bac à sable, et les deux résultats consignés — vert sur l'état sain, refus sur
la faute (§VII).

## Points de retour à l'humain

Quatre, dont deux avant toute action :

1. **Le visa de ce plan** (Cmd 6) — rien ne démarre sans lui.
2. **L'arrêt de la charge de référence** (étape 1) — Sidy seul.
3. **Le sort de l'option D** (serveur GPU dédié loué) — le critère qui a fermé E
   (« trop coûteux pour du matériel dont on n'est pas propriétaire ») semble
   l'emporter de la même façon, mais l'écarter serait une décision, pas un
   relevé (Cmd 13). Question posée à Sidy, non tranchée ici.
4. **Le choix de la voie de mesure** (étape 4 : 4a documentaire, 4b la petite
   machine comme banc d'essai, 4c sans mesure préalable) — la voie 4b engage une
   dépense avant la fin de la comparaison, donc elle relève de Sidy.
5. **La décision d'achat** (étape 6) — préparée par la machine, tranchée par
   Sidy. C'est l'objet même du chantier, et son seul terme.

> **Ce que le verdict du 2026-09-07 a déjà retiré du plan** : la location de
> calcul, qui figurait ici en point 3. Elle n'est pas reportée, elle est fermée
> (option E, §*Verdict* du `spec.md`).

## Journalisation

Circuit : `atelier/annales.md`, préfixe `## [YYYY-MM-DD] chantier | INF-16 — …`,
SHA court du commit en dernière ligne, entrée rédigée **après** le commit (Cmd 9).
Ligne de registre `INF-16` mise à jour **dans la même passe** (section *Entretien*
du registre des chantiers).

Si le chantier produit une optimisation mesurée, elle va au
[[atelier/rd/cahiers/journal-optimisations]] ; s'il bute, au
[[atelier/rd/cahiers/registre-problemes]]. L'un ou l'autre, jamais les deux.
