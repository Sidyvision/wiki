---
title: "INF-16 — Devis : une rafale d'entraînement RunPod pour produire un adaptateur LoRA"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, inf-16, devis, gpu-loue, runpod, lora, budgétisation]
created: 2026-09-16
updated: 2026-09-16
sources:
  - "https://docs.runpod.io/pods/pricing"
  - "https://docs.runpod.io/accounts-billing/billing"
  - "https://www.thundercompute.com/blog/nvidia-h100-pricing"
links:
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/intent]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/spec]]"
  - "[[atelier/rd/infrastructure/inf-16-machine-ia-locale-slm/plan]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# Devis — une rafale d'entraînement RunPod, pour obtenir un adaptateur LoRA

> **Ce que cette fiche est** : le devis demandé par Sidy **dans la nuit du 15 au
> 16 septembre 2026** (horloge du serveur : `2026-09-16`) — « préparer le
> devis seul, et je tranche après l'avoir lu ». Elle est faite pour être lue, puis
> tranchée.
>
> **Ce qu'elle n'est pas** : une décision, une réservation, ni une dépense. **Rien n'est
> lancé. Aucun compte n'existe à ce jour. Aucun euro n'est engagé.**

## 1. Objet

Produire, en **une rafale unique sur GPU loué**, un **adaptateur LoRA** entraîné sur un
sous-ensemble borné du corpus du dépôt, afin de savoir *si* la voie U4 est praticable —
et à quel coût réel sur *notre* corpus.

C'est un **run de faisabilité**, pas un run de production. Ce qu'on achète, c'est une
réponse et un premier artefact ; pas un modèle livrable (voir §4).

## 2. Ce qui serait lancé, exactement

| Élément | Valeur |
|---|---|
| Fournisseur | **RunPod — « Pods »**, jamais « Serverless » : le Serverless n'offre ni SSH ni tunnel (constat de l'antécédent de juin 2026) |
| GPU | selon scénario : A6000 48 Go · A100 80 Go · H100 80 Go |
| Image | pile d'entraînement PyTorch/CUDA + `soup-cli[train]` — l'outil exige **Python 3.10-3.12** |
| Disque conteneur | 50 Go (temporaire, effacé à l'arrêt) |
| Volume | 50 Go — le modèle de base 8B pèse **16,38 Go** en bf16 : premier téléchargement à prévoir |
| Durée | par blocs de 2 h ; **pod détruit à la fin**, jamais « arrêté » (§3) |
| Données | un JSONL préparé **hors** du pod puis téléversé ; **`meta/` exclu par construction** |
| Sortie | l'adaptateur (quelques Mo à quelques centaines de Mo), rapatrié au dépôt **hors git** (`raw/`), puis pod détruit |
| Sécurité | aucun secret du dépôt sur le pod ; port d'inférence **jamais exposé** ; accès par tunnel SSH depuis le serveur (dispositif éprouvé en juin 2026, dont les enseignements — SSH à réinstaller après chaque redémarrage, port externe qui change à chaque restart — restent valables) |

## 3. Coût — trois scénarios

Tarifs GPU relevés le **2026-09-15** ; le coût A6000 est celui **observé chez nous** en
juin 2026 (≈ 0,50 $/h) et non un tarif public.

| Scénario | Tarif horaire | 4 h | 6 h | 8 h | 12 h |
|---|---|---|---|---|---|
| **Sobre** — A6000 48 Go | ≈ 0,50 $/h *(mesuré, juin 2026)* | 2,00 $ | 3,00 $ | **4,00 $** | 6,00 $ |
| **Recommandé** — A100 80 Go | 1,39 $/h (RunPod ; 1,09 $/h chez Thunder) | 5,56 $ | 8,34 $ | **11,12 $** | 16,68 $ |
| **Rapide** — H100 80 Go | 3,49 $/h (RunPod ; 3,29 $/h Lambda) | 13,96 $ | 20,94 $ | **27,92 $** | — |

**Enveloppe du devis : de ≈ 4 $ (sobre) à ≈ 28 $ (rapide)**, avec un scénario
recommandé à **≈ 11 $** (A100, 8 h). Hors coût de préparation (§5), qui n'est pas de
l'argent mais du temps.

**Stockage — et le piège à éviter.** Grille RunPod officielle (consultée le
**2026-09-16**) :

| Type | En marche | À l'arrêt |
|---|---|---|
| Disque conteneur | 0,10 $/Go/mois | **non facturé** — effacé à l'arrêt |
| Volume | 0,10 $/Go/mois | **0,20 $/Go/mois** |
| Volume réseau | 0,07 $/Go/mois | 0,07 $/Go/mois (permanent) |

Un volume de 50 Go **arrêté** coûte **10,00 $/mois** — le double de son coût en marche,
pour ne rien calculer. **On éteint en détruisant.** Sur 48 h de pod vivant, le volume
coûte 0,33 $ : le stockage n'est un coût que si on oublie de détruire.

**Seuils opérationnels** : il faut **au moins 1 h de calcul en solde** pour louer ; le
plafond de dépense par défaut du compte est de **80 $/h** (garde-fou, pas un budget) ;
à solde nul RunPod arrête tout, et un pod **sans volume réseau perd ses données**.

## 4. Ce que l'argent achète — et ce qu'il n'achète pas

**Il achète** : la réponse à « est-ce que ça tourne sur *notre* corpus, à quelle vitesse,
et avec quelle qualité ? », plus un premier artefact à examiner.

**Il n'achète pas un adaptateur jugeable.** Sans jeu d'évaluation, ce qui sort n'est pas
un livrable mais un **fichier indécidable** : c'est la forme d'échec récurrente du
domaine — un run qui se termine, sort en code 0, affiche une courbe de perte normale, et
est faux. Les évals sont donc un **préalable**, jamais une étape d'après.

**Il n'achète pas le droit d'entraîner.** Deux questions restent ouvertes, non tranchées
ici :
- les **droits** sur une partie de `textes/` (cf. `spec.md`, relevé du 2026-09-15, §B) ;
- le **régime de l'artefact** : un adaptateur **porte** ce sur quoi il a été entraîné. Il
  vivra donc **hors git** (`raw/`), avec sa fiche de provenance — le dépôt n'a pas encore
  de régime pour cet objet (critère 11).

## 5. Préalables — gratuits en argent, pas en temps

1. **Le jeu de données** : un JSONL borné, recette choisie (affinage supervisé ou
   pré-entraînement continu), `meta/` exclu par construction.
2. **Le jeu d'évaluation** : ce qui rendra le verdict possible (`soup ship` en a besoin).
3. **Le choix du modèle de base** et de sa taille — mémoire déjà calculée au `spec.md`
   (étape 3c).
4. **Le runbook d'entraînement** : le frère de celui de l'inférence de juin, qui reste à
   écrire pour la charge d'entraînement.
5. **Un compte RunPod et un moyen de paiement** — à créer. *C'est cela, l'engagement* :
   le compte, pas la rafale.

## 6. Ce que ce devis ne tranche pas

- **Le verdict « E seule » — LEVÉ le 2026-09-16.** Le verdict du 2026-09-07 n'autorisait le
  GPU à l'heure qu'**en complément** de l'option B, *jamais seule ni comme capacité
  permanente*. Le **troisième verdict** (« On ouvre à nouveau l'option E. ») **lève cette
  condition** : la rafale n'est plus subordonnée à l'existence préalable d'une machine
  possédée. Ce qui n'est pas levé pour autant : les **préalables** du §5, la **charge de
  référence** (étape 1), et la **porte humaine sur la dépense** (Cmd 13).
- **La charge de référence** (étape 1) et le **choix de la voie 4a / 4b / 4c** (étape 4).
  *Signalé sans être tranché* : E ouverte **rouvre la possibilité que l'étape 4 avait
  fermée** — louer du GPU comme instrument de mesure *avant* tout achat. Rouvrir une option
  n'est pas réinstruire une étape.
- Les **droits** et le **régime de l'artefact** (§4), inchangés.

## 7. Validité

Un tarif est une photographie. Le marché relevé le même jour le montre : la RTX 5090 va
de 2 000 $ de prix conseillé à 9 500 $ en boutique selon la source. **Ce devis se
re-relève avant tout lancement** ; passé deux semaines, il est réputé périmé.

*Conseil de sobriété, si la rafale est tranchée :* le scénario **sobre** suffit pour une
faisabilité — la carte de juin, à ≈ 0,50 $/h, a déjà servi un modèle de 9B, et un 8B en
4 bits tient dans 4 Go. Payer une H100 pour un premier run serait payer de la vitesse
avant d'avoir payé de la clarté.
