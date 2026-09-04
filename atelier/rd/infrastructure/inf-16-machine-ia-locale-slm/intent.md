---
title: "INF-16 — Machine d'IA locale et développement SLM : intention"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, intent, slm, souverainete, materiel]
created: 2026-09-04
updated: 2026-09-04
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/infrastructure/cartographie-routing-infrastructure]]"
  - "[[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]]"
---

# INF-16 — Machine d'IA locale et développement SLM : intention

## Le besoin

Trois faits déjà consignés au dépôt, aucun supposé :

1. **Aucune capacité d'inférence locale n'existe.** Le seul poste physique du
   routing applicatif est le serveur Hetzner : 2 vCPU AMD EPYC-Rome, 3,7 Gio de
   RAM, **aucun GPU** (Virtio GPU virtuel), 38 Gio de disque
   ([[atelier/rd/infrastructure/cartographie-routing-infrastructure]] §1). La RAM
   y est déjà la contrainte structurelle dominante du système (§5 de la même
   fiche, et [[atelier/rd/infrastructure/incident-2026-08-28-saturation-ram-indisponibilite]]).
   Ce poste ne peut pas porter un modèle, et le chantier ne prétend pas le lui
   faire porter.

2. **La veille a déjà buté sur cette absence.** `OUT-07` (speculative decoding,
   Tencent/AngelSpec) est au statut `bloque` avec pour prochaine action exacte :
   « rouvrir si un chantier d'inférence GPU locale est ouvert »
   ([[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]], §Pertinence).
   Le présent chantier est cette ouverture.

3. **La couche modèle est aujourd'hui entièrement chez des tiers, et ses
   fragilités sont mesurées** : quota Qwen épuisé le 2026-08-26, combo
   `auto/best-free` d'OmniRoute donnant retries et latences ~90 s, `omniroute`
   en point de défaillance unique consommant jusqu'à 28 % de la RAM du serveur
   ([[atelier/rd/infrastructure/cartographie-routing-infrastructure]] §4.2).
   L'incident du 2026-09-03 a montré qu'une mise à jour npm interrompue suffit à
   couper toute la couche modèle
   ([[atelier/rd/infrastructure/incident-2026-09-03-omniroute-npm-interrompu-durcissement-ssh]]).

Face à cela, la charte du pôle fixe une finalité explicite : « l'émancipation
progressive de tout intermédiaire de service tiers par souveraineté des moyens de
production / déploiement / information » ([[atelier/rd/index]] §Mission). Aucun
moyen matériel n'a jamais été instruit en regard de cette finalité.

## Qui le porte

Sidy — la demande est venue en session le 2026-09-04, à partir d'un intérêt
déclaré pour la nouvelle gamme Mac Studio, puis d'une hypothèse propre : héberger
le SLM en local sur un Mac mini et garder l'accès au LLM par abonnement/API. La
consigne donnée est explicite : **ouvrir le chantier en explorant les diverses
options jusqu'à trouver la meilleure** — donc ne pas partir d'une solution.

Pour qui l'on construit : le pôle R&D d'abord (développement SLM proprement dit),
et par ricochet la couche agentique (les 12 profils Hermes, dont l'essentiel du
travail est du tri et de l'orchestration, non du raisonnement de frontière).

## Hors périmètre

- **La crise de RAM du serveur Hetzner.** Elle est réelle et documentée, mais
  c'est un autre problème : aucune machine d'inférence achetée ne libère la RAM
  des gateways Hermes. Le confondre ferait payer deux fois la même ligne.
- **Le choix du modèle SLM lui-même** (architecture, famille, taille). Il dépend
  de la charge de référence, qui n'est pas encore arrêtée — donc il vient après,
  pas ici.
- **Toute décision d'achat.** Ce chantier produit une comparaison instruite ;
  l'engagement de dépense appartient à Sidy (Cmd 13).
- **Le remplacement du poste PRODUCTION.** L'iPad reste le poste de lecture
  lourde et de rédaction (§I du protocole racine) ; aucune machine envisagée ici
  ne le remplace.
- **Tout entraînement à partir de zéro (*pre-training*).** Hors d'atteinte de
  tout matériel de ce périmètre — la fiche AngelSpec chiffre le training à 8 GPU
  minimum. Ce qui est visé est le fine-tuning, la distillation et la
  quantization.

## Contraintes doctrinales

- **Cmd 13 (porte humaine sur ce qui engage)** : une dépense de cet ordre est
  préparée par la machine, tranchée par Sidy. S'y ajoute, dans le plan, toute
  location horaire de calcul, si modeste soit-elle.
- **Cmd 5 (aucune affirmation factuelle sans source)** : chaque prix, chaque
  spécification, chaque débit porté dans la comparaison est daté et sourcé, ou
  marqué comme non relevé. Une valeur de mémoire de modèle n'a pas sa place dans
  une matrice de décision.
- **§VI (étanchéité)** : toute option qui envoie de la matière du dépôt à un
  tiers — c'est le cas de toute option gardant le LLM au cloud — est examinée
  sous cet angle. Rien de `meta/` ne sort, jamais, y compris pour un essai.
- **Cmd 10 (réversibilité)** : la réversibilité de chaque option est un critère
  de comparaison à part entière, pas une remarque de fin de fiche.
- **§VII, épreuve des contrôles** : si le chantier produit un contrôle mécanique
  (mesure de débit, garde-fou de filtrage), son refus devra avoir été observé
  avant qu'on lui fasse confiance.
- **Cmd 12** : rien ici ne relève du doctrinal. La « souveraineté » est traitée
  comme une propriété d'infrastructure mesurable (quelle couche cesse de dépendre
  d'un tiers), jamais comme un principe à interpréter.

## Le signe de réussite

Une matrice **options × critères** dans laquelle chaque cellule est soit une
valeur mesurée, soit une valeur sourcée et datée, soit explicitement marquée non
relevée — et à partir de laquelle Sidy peut trancher **sans avoir à chercher une
seule information supplémentaire**. Le signe observable : aucun « ça dépend » non
qualifié ne subsiste dans la matrice.

Corollaire assumé : le chantier peut réussir en concluant que **la meilleure
option est de ne rien acheter** (option F du `spec.md`). Une comparaison dont le
résultat serait connu d'avance n'en serait pas une.

## Ce qui reste ouvert

| Inconnue | Destinataire |
|---|---|
| Quels usages réels le SLM doit servir (la *charge de référence*) — sans elle, aucune comparaison n'a de sens | **Sidy** : c'est la première étape du plan |
| Le budget, ou la fourchette, que Sidy accepte d'engager | **Sidy** (Cmd 13) |
| Le lieu d'installation (proximité du studio → contrainte de bruit réelle ou non) | **Sidy** |
| Prix exacts des configurations NVIDIA et des paliers Apple au-delà de l'entrée de gamme | **mesure** : relevé daté à faire (étape 2 du plan) |
| Débits réels (tok/s) d'un SLM candidat sur chaque famille de matériel | **mesure** : non mesurable sans essai (étape 4 du plan) |
| Coût récurrent réel de la couche modèle actuelle (API + abonnements) | **mesure** : à relever, jamais estimé |
