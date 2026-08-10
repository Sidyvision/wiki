---
title: "LLM et ontologie islamique automatisée — cas d'école de dérive kari-kumi (Alshammari, Atwell, Alsalka 2026)"
type: etude
status: academique
tradition_cadre: "islam"
tags: [ia, ontologie, epistemologie, kari-kumi, methodologie, gpt-4, correspondances]
created: 2026-08-09
updated: 2026-08-10
sources: ["[[doctrinal/sources/alshammari-llm-ontologie-hadith-2026]]"]
sources_count: 1
cross_links: ["[[doctrinal/discernement/2026-08-09_wahhabisme-effondrement-califat-grande-subversion]]"]
---

# LLM et ontologie islamique automatisée — cas d'école de dérive kari-kumi

> Note d'ingest : fiche `sources/` créée (2026-08-10) — [[doctrinal/sources/alshammari-llm-ontologie-hadith-2026]].
> Cette étude analyse la méthodologie de l'article, non son contenu islamologique — elle est
> transversale à la discipline du dépôt, pas une fiche de lecture doctrinale.

**Référence** : Alshammari IK, Atwell E, Alsalka MA. « Large language models for automated
Islamic ontology construction and knowledge integration ». *Academia AI and Applications*
2026;2. DOI 10.20935/AcadAI8357. Publié 18 juin 2026.

## 1. Ce que fait l'article

GPT-4 est appliqué au corpus LK-Hadith (39 038 aḥādīth des six collections canoniques) pour
extraire des topics, organisés en un jeu de données bilingue Hadith_Teaching_Topics. Ces
topics sont ensuite liés automatiquement aux versets coraniques par similarité sémantique
(embeddings + GPT-4), puis l'ensemble est formalisé en une ontologie OWL, validée par
raisonneurs (HermiT, Pellet) et par une enquête d'experts a posteriori.

## 2. Le point de rupture méthodologique — Table 2 de l'article

Un cas rapporté par les auteurs eux-mêmes constitue le nœud de cette étude : une paire
verset/hadith reçoit un score de similarité GPT-4 de **0,5321**. Un expert islamologue,
consulté après coup, juge la connexion **partielle** — le verset est général (licéité de
l'ornement, dont le vêtement), le hadith porte spécifiquement sur l'interdiction de traîner
son vêtement par orgueil. La connexion existe, mais n'est pas celle que le score suggère
telle quelle ; elle est qualifiée, pas simplement quantifiée.

Les auteurs eux-mêmes formulent la limite en présentant leurs résultats : ils notent que des
scores en dessous de 0,90 « peuvent indiquer des liens significatifs quand la connexion est
partielle ou contextuelle, sans être pleinement alignée » — une reconnaissance implicite que
le chiffre seul ne suffit jamais à qualifier la nature d'un rapprochement.

## 3. Diagnostic structurel — pourquoi ce cas concerne le dépôt

Ce que l'article documente sans le nommer ainsi est une **dérive de kari-kumi** : une
correspondance techniquement plausible (score de similarité, raisonnement OWL cohérent,
absence de contradiction logique détectée par HermiT/Pellet) est produite et intégrée à une
structure de connaissance *avant* qu'une autorité qualifiée n'ait statué sur sa nature — et
la vérification humaine, quand elle a lieu, arrive **après coup**, sur échantillon, sous
forme d'enquête qualitative (87-89 % d'accord global rapporté), non comme condition
préalable et systématique à l'inscription.

Comparaison directe avec les protocoles de ce dépôt :

| | Article (Alshammari et al. 2026) | Protocole de ce dépôt |
|---|---|---|
| Qui propose le lien | GPT-4 (embeddings + prompt fixe) | IA (proposition uniquement) |
| Qui vérifie | Sondage d'experts, après intégration, sur échantillon | Sidy, systématiquement, avant tout ancrage |
| Statut par défaut du lien | Intégré à l'ontologie dès le score calculé | `speculatif` / kari-kumi jusqu'à verdict |
| Mécanisme de contrôle | Raisonneurs logiques (HermiT, Pellet) — cohérence formelle, pas validité de fond | Circuit discernement (Cmd 12) — jamais mécanique pour le fond |
| Trace de la décision | Score numérique + accord qualitatif global | Bloc EXAMEN DE DISCERNEMENT, daté, attribué |

La cohérence logique (aucune contradiction dans les axiomes OWL) et la validité doctrinale
d'une correspondance sont deux choses distinctes — l'article les traite largement comme
substituables l'une à l'autre pour l'essentiel de son ontologie, ne réservant l'examen humain
qualifié qu'à un sous-échantillon final. C'est précisément la distinction que Commandement 12
et le principe kari-kumi-avant-hozo rendent non négociable : *aucune cohérence formelle,
aussi robuste soit-elle, ne vaut verdict de fond.*

## 4. Limite de la comparaison

Cette étude ne prétend à aucune équivalence entre le corpus de l'article (Coran-Hadith,
strictement) et le corpus doctrinal de ce dépôt (Ibn ʿArabī, Guénon, Akbarien/Vedānta). Le
rapprochement porte exclusivement sur la **structure épistémologique du contrôle qualité**,
non sur le contenu religieux traité. Aucun contenu de l'article n'est repris comme source
doctrinale.

## 5. Valeur d'usage

Fiche de référence méthodologique, citable dans `CLAUDE.md` ou dans tout futur signalement
touchant à la tentation d'automatiser une correspondance sur la seule base d'un score de
similarité ou d'une absence de contradiction logique détectée par script. Utile en particulier
pour tout futur travail sur l'Instrument (mécanisme de suggestion établi/suggéré, §4 de
`instrument-tradition-primordiale-architecture-v0.3.md`) : ce cas est un exemple externe et
concret de ce que produit l'absence de porte humaine systématique.
