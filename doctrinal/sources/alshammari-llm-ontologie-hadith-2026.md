---
title: "Large Language Models for Automated Islamic Ontology Construction and Knowledge Integration"
type: source
status: academique
tradition_cadre: "islam"
tags: [ia, llm, gpt-4, ontologie, coran, hadith, semantique, knowledge-representation, outils-computationnels]
created: 2026-08-10
updated: 2026-08-10
sources: []
sources_count: 0
cross_links: ["[[doctrinal/etudes/2026-08-09_llm-ontologie-islamique-derive-kari-kumi]]"]
---

# Large Language Models for Automated Islamic Ontology Construction and Knowledge Integration

## Notice bibliographique

- **Auteurs** : Ibtisam Khalaf Alshammari¹'², Eric Atwell¹, Mohammad Ammar Alsalka¹
- **Titre complet** : Large language models for automated Islamic ontology construction and knowledge integration
- **Journal** : *Academia AI and Applications*
- **Volume/Numéro** : 2026;2
- **Date de publication** : 18 juin 2026
- **DOI** : https://doi.org/10.20935/AcadAI8357
- **Affiliations** : 
  1. School of Computer Science, University of Leeds, Leeds, UK
  2. College of Computer Science and Engineering, University of Hafr Al Batin, Hafr Al Batin, Saudi Arabia
- **Contact principal** : ikalshammari@uhb.edu.sa

**Catégorie** : Article de recherche en informatique appliquée et génie des connaissances, domaine spécialisé religieux.

## Objet et méthodologie générale

Cet article propose une approche automatisée pour unifier les ressources qurʾāniques et hadithiques dans une ontologie islamique cohérente, utilisant GPT-4 pour l'extraction de topics et OWL (Web Ontology Language) pour la formalisation sémantique. L'objectif principal est de dépasser la fragmentation des ressources islamiques numériques en créant un cadre de représentation des connaissances machine-lisible et interopérable.

### Matériaux utilisés

1. **QuranOntology** — ontologie structurée du Qurʾān couvrant les métadonnées qurʾāniques provenant du site Tanzil, exégèses (Tafsīr al-Jalālayn, al-Muyassar, Ibn Kathīr), données sémantiques QurSim, et annotations du dataset QurAna.

2. **Corpus Hadith LK (Leeds and King Saud University)** — corpus bilingue arabe-anglais de 39 038 aḥādīth annotés des six collections canoniques (Kutub al-Sitta), segmentés en Isnād et Matn, contenant plus de 10 millions de tokens et 238 chapitres de hadith distincts.

3. **RQHT (Related Qurʾan–Hadith Topics) ontology** — lie topics qurʾāniques et hadithiques via embeddings de similarité sémantique et le plugin Cellfie, basée sur le QH_dataset d'Altammami et al. intégrant paires verset/enseignement avec métadonnées associées.

### Processus principal

**Phase 1 : Extraction de connaissance** — GPT-4 est appliqué au corpus LK-Hadith pour générer des topics sémantiques clairs pour chaque Hadith Matn (corps du hadith). Une approche de baseline utilisant BERTopic (Bidirectional Encoder Representations from Transformers Topic Modelling) avec modèle transformer arabe pré-entraîné est utilisée pour comparaison. Les outputs sont organisés en dataset bilingue arabe-anglais `Hadith_Teaching_Topics (HTT)`.

**Phase 2 : Prétraitement des données** — standardisation de la numérotation des versets à un schéma global (versets 1-6236), correction du tri lexical des identifiants qurʾāniques, assignation d'identifiants hiérarchiques uniques (ex. Quran1-1-2-Seg1) pour versets, mots et segments, enrichissement linguistique via translittération Buckwalter et tags part-of-speech (POS). Les données Hadith sont consolidées en fichier Excel structuré avec chaque collection canonique sur feuille séparée.

**Phase 3 : Spécification du domaine et intégration sémantique** — mappings entre topics qurʾāniques et hadithiques via identifiants uniques et propriété `relatedTo`, fondés sur correspondances savantes et affinements par représentations GPT-4 et BERT. L'ontologie résultante formalise relations de concepts au-delà de l'agrégation structurelle, soutenant requêtes sémantiques, récupération cross-texte, raisonnement et découverte de connaissances.

**Phase 4 : Formalisation en OWL** — construction d'une ontologie Web Ontology Language (OWL) intégrant données qurʾāniques (chapitres, versets, mots, segments, topics multilingues, labels, concepts associés, sources Tafsīr) et données hadithiques (Hadith par livre canonique, chapitre, Isnād/Matn, grades d'authenticité, topics), avec propriétés de liaison inter-ressources (`isPartOf`, `relatedTo`).

## Résultats et validation

### Dataset et ontologie produits

L'approche génère un dataset bilingue structuré `HTT` et une ontologie OWL automatiquement construite, offrant à la fois formats machine-lisibles et lisibles-humains. Le cadre facilite interopérabilité, requêtes sémantiques, raisonnement et validation par experts à travers ressources islamiques intégrées.

### Évaluation humaine — deux phases

**Phase 1 : Qualité des topics générés** — Experts arabophones musulmans (juges humains) comparent qualitativement les représentations topics issues de GPT-4 et de BERTopic. Analyse de topics Hadith sélectionnés pour pertinence sémantique, clarté et utilité, privilégiant adéquation linguistique et sémantique sur interprétation théologique. Résultats rapportés : accord global de 87-89 % sur la qualité relative des topics.

**Phase 2 : Cohérence sémantique de liaison** — Un expert en études islamiques évalue indépendamment la cohérence sémantique entre topics qurʾāniques et hadithiques, vérifiant exactitude et interprétabilité des relations cross-texte au sein d'un contexte interprétatif plus large. Cet examen valide la méthodologie de liaison sémantique de l'ontologie plutôt que de conduire une évaluation statistique détaillée.

### Configuration méthodologique de GPT-4

Pour assurer reproductibilité, GPT-4 est utilisé avec prompt fixe pour tous textes Hadith. Template arabe unique instruit le modèle d'identifier topics principaux plutôt que résumer ou paraphraser. Paramètres constants : température basse (0.3) pour réduire variabilité, réponse max de 500 tokens pour topics concis et lisibles-humains. Topics extraits automatiquement et séquentiellement sur l'ensemble du corpus Hadith, résultats intermédiaires sauvegardés pour robustesse durant traitement à grande échelle.

## Cas de rupture méthodologique — Table 2 de l'article

L'article lui-même rapporte un cas instructif de limitation méthodologique documenté à Table 2 (discussion) :

Une paire verset/hadith reçoit score de similarité GPT-4 de **0.5321**. Un expert islamologue consulté après coup juge la connexion **partielle** — le verset est générique (licéité de l'ornement, dont vêtement), le hadith porte spécifiquement sur interdiction de traîner vêtement par orgueil. Connexion existe, mais n'est pas celle que le score suggère tel quel ; qualifiée, non simplement quantifiée.

Les auteurs eux-mêmes formulent la limite en notant que scores sous 0.90 « peuvent indiquer liens significatifs quand connexion est partielle ou contextuelle, sans être pleinement alignée » — reconnaissance implicite que chiffre seul ne suffit jamais à qualifier nature d'un rapprochement. **C'est un exemple éminent de dérive kari-kumi : correspondance techniquement plausible intégrée avant qu'autorité qualifiée ne statue sur sa nature.**

## Enjeux et réserves vis-à-vis du domaine religieux

L'article souligne que LLMs peuvent soutenir extraction et représentation sémantique dans textes qurʾāniques et hadithiques, particulièrement combinés à mécanismes d'ancrage et stratégies de prompting spécifiques au domaine. Il note en même temps des préoccupations persistantes : exactitude de citation, ancrage factuel, fiabilité en contextes religieux. L'évaluation humaine demeure centrale ; l'article propose une validation par experts plutôt que d'automatiser entièrement jugements doctrinaux ou herméneutiques.

## Utilité pour le dépôt

Source primaire pour toute évaluation des capacités et limites des LLMs appliqués à formalisation automatisée de connaissance religieuse. Particulièrement utile pour :

- Documenter et illustrer le risque de **kari-kumi prématuré** dans ontologisation automatisée (cas Table 2).
- Établir standards d'évaluation et points de contrôle obligatoires quand IA propose correspondances structurelles.
- Servir de référence méthodologique dans chaînes d'intégration d'Instrument ou du dépôt lui-même (voir [[doctrinal/etudes/2026-08-09_llm-ontologie-islamique-derive-kari-kumi]]).
- Préciser distinction entre cohérence formelle (ce que raisonneurs OWL valident) et validité doctrinale (ce que Sidy tranche).
