---
title: "INF-16 — Machine d'IA locale et développement SLM : spécification"
type: infrastructure
chantier: INF-16
tags: [atelier, rd, infrastructure, chantier, spec, slm, materiel, comparaison]
created: 2026-09-04
updated: 2026-09-04
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
| **D** | Serveur GPU dédié loué (hébergeur) | le SLM, mais **chez un tiers** — souveraineté d'usage, pas de possession | le matériel lui-même, et le LLM |
| **E** | GPU à l'heure (RunPod, Vast, Lambda) pour rafales d'entraînement | rien en continu ; l'entraînement ponctuel seulement | tout le reste |
| **F** | Statu quo — aucune machine, montée de RAM du Hetzner seule | rien | tout (état actuel) — **c'est la référence à battre** |
| **G** | Combinaisons étagées (ex. B maintenant + C plus tard ; ou E pour entraîner + B pour servir) | selon l'étage | selon l'étage |

**Note sur E** : les containers GPU cloud ont déjà été utilisés puis suspendus
(mentionné dans [[atelier/rd/veille/2026-08-31_tencent-angelspec-speculative-decoding]]
§État actuel). Le motif exact de la suspension n'est pas consigné au dépôt — à
retrouver avant de conclure quoi que ce soit sur cette option.

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

## Ce qui est déjà établi (relevé du 2026-09-04)

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

- Le motif de la **suspension des containers GPU cloud** : mentionné dans la
  fiche AngelSpec, jamais consigné en propre. Sans lui, l'option E ne peut être
  ni retenue ni écartée honnêtement.
- Les **débits réels** (tok/s en inférence, durée d'un fine-tuning de référence)
  par famille de matériel : aucune valeur publiée ne remplace une mesure sur la
  charge de référence retenue. Marqués `to-source` jusqu'à l'essai de l'étape 4
  du plan.
- La **consommation électrique** de chaque option sous charge soutenue, et le
  tarif applicable — sans quoi le critère 8 reste vide.
