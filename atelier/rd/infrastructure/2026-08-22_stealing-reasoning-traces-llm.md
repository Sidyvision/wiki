---
title: "Stealing Reasoning Traces from Proprietary LLM APIs"
type: outillage
statut_experience: reproduit
tags:
  - security
  - llm
  - infrastructure
  - research
created: 2026-08-22
updated: 2026-08-23
sources:
  - "[[2608.09867]]"
links:
  - "[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]"
---

# Stealing Reasoning Traces from Proprietary LLM APIs

Ressource R&D structurante — amorçage infrastructure/architecture/laboratoire

- **Auteurs** : A. Panfilov, D. Schmotz, I. Shumailov, L. Beurer-Kellner, J. Schaeffer, A. Prabhu, J. Geiping, M. Andriushchenko
- **Affiliations** : MATS Research, ELLIS Institute Tübingen, MPI for Intelligent Systems, Tübingen AI Center, AI Security Company, Snyk, University of Tübingen
- **Source** : arXiv:2608.09867v1 [cs.CR] — 10 août 2026
- **PDF** : /root/wiki/raw/2608.09867.pdf (116 pages)
- **Site** : stolen-thoughts.com

---

## Enjeu central

Les LLM frontier génèrent des traces de raisonnement (chain-of-thought) avant de produire une réponse visible. Pour protéger la propriété intellectuelle et limiter les fuites d'information, les providers (Anthropic, OpenAI, Google) ont abandonné le texte brut au profit de blocs chiffrés côté client.

**Vulnérabilité critique identifiée** : ces blocs chiffrés sont compatibles et interchangeables entre sessions, utilisateurs et modèles d'un même écosystème provider. Cette portabilité permet une extraction à grande échelle des traces de raisonnement via un modèle "décoder" plus faible et moins protégé.

---

## Architecture vulnérable : état de l'art (juillet 2026)

### Conception stateless des API reasoning

Les API modernes renvoient les traces de raisonnement sous forme de blocs opaques chiffrés (AEAD — Authenticated Encryption with Associated Data) contenant :
- En-tête (model name, block type, version, key ID)
- Nonce
- Tag d'authentification (MAC)
- Ciphertext

**Fonctions opérationnelles** :
1. **Confidentialité** : opaque pour les compétiteurs (anti-distillation)
2. **Intégrité** : MAC empêche la manipulation
3. **Statelessness** : le client stocke et repasse le bloc à chaque requête multi-tours (pas de stockage serveur)

**Faiblesse fondamentale** : la portabilité requise par le design stateless implique qu'une clé globale unique chiffre tous les blocs d'un provider. Aucun identifiant utilisateur ou conversation n'est intégré dans l'enveloppe AEAD.

### Matrice de compatibilité cross-modèle (juillet 2026)

**Claude** : toutes les traces de tous les modèles sont rejouables par tous les autres, SAUF Fable 5.

**GPT** : la série GPT-5.6 peut rejouer les traces de toutes les générations antérieures.

**Gemini** : les traces de n'importe quel modèle sont rejouables dans n'importe quel autre.

**Pattern récurrent** : les modèles faibles/économiques (Haiku 4.5, GPT-5.6 Luna, Gemini Robotics 1.6) peuvent décoder les traces des modèles frontier (Opus 4.8, GPT-5.6 Sol, Gemini 3.1 Pro).

---

## Vecteurs d'attaque identifiés

### Première partie (First-Party Attacker)

#### 3.1 Distillation de raisonnement propriétaire

**Mécanisme** : capturer les traces chiffrées d'un modèle frontier → les injecter dans un modèle faible compatible → forcer le décodage verbatim via jailbreak ad-hoc (balises `<thinking-copy>`).

**Gain par rapport à la distillation output-only** : les traces de raisonnement fournissent un signal de supervision bien plus dense (décomposition du problème, déductions intermédiaires, stratégie de solution) que les seules réponses finales.

**Coût économique** : ~720 USD pour décoder 10k traces de 12k tokens input/output avec Claude Haiku 4.5.

**Impact** : extraction du raisonnement brut verbatim, sans jamais interroger le modèle frontier directement, contournant les mécanismes anti-distillation.

#### 3.2 Jailbreaking via extraction

**Mécanisme** : leurre du modèle frontier pour qu'il raisonne sur un sujet nuisible tout en produisant une réponse visible bénigne → extraction de la trace chiffrée → décodage via modèle faible.

**Constat** : les modèles sont entraînés à ne pas divulguer d'informations nuisibles dans les sorties visibles, mais pas nécessairement à éviter de raisonner sur des sujets nuisibles (optimiser le contenu du CoT dégraderait la monitorabilité).

### Deuxième partie (Third-Party Attacker)

#### 4.1 Extraction de secrets (PII, credentials)

**Échelle démontrée** : scraping de 6 708 trajectoires d'agents publics (GitHub, HuggingFace) → 315 320 blocs de raisonnement décodés.

**Résultats** :
- 367 artefacts PII
- 182 credentials (62 API keys, 33 passwords, 24 access tokens, 7 private keys, 30 emails personnels, 6 adresses IP non-localhost)
- 4,9% des sessions fuient au moins un item sensible réel
- 64 artefacts absents de l'historique visible (injectés depuis la mémoire du modèle ou piégés après nettoyage visible)

**Pattern récurrent** : quand l'utilisateur demande un "nettoyage" ou une anonymisation, le modèle relit l'historique complet dans son raisonnement chiffré et reformule les valeurs sensibles qui doivent être supprimées.

#### 4.2 Prompt injections invisibles

**Mécanisme** : planter un bloc de raisonnement opaque qui a internalisé une instruction malicieuse → la victime rejoue ce bloc dans une session ultérieure → le modèle traite l'instruction comme son propre raisonnement antérieur.

**Avantage attaque** : payload invisible pour les moniteurs externes (pas d'artefacts plaintext), transfert cross-modèles et cross-tâches.

**Démonstration** : injection d'instruction d'exfiltration de données dans des traces long-horizon (PostTrainBench) → le modèle frontal continue la trace et suit l'instruction malicieuse.

---

## Propositions de mitigation (Section 5.5)

### Révisions architecturales

**Approche radicale** : transition vers une architecture stateful où les traces de raisonnement restent entièrement côté serveur. Le client ne reçoit qu'un identifiant opaque et randomisé pour lookup par ID.

**Avantage** : élimine fondamentalement l'asset cryptographique du contrôle utilisateur.

**Inconvénient** : overhead base de données et stockage, complexité API accrue.

### Binding cryptographique contextuel

**Si architecture stateless préservée** : lier strictement les enveloppes cryptographiques à leur contexte d'origine.

**Implémentation** :
- Intégrer user ID et/ou conversation ID dans l'enveloppe AEAD (Associated Data)
- Hasher statefully le prompt précis et l'historique de conversation précédent dans le MAC
- Toute réinjection dans un contexte fabriqué invalide la signature

**Contrainte** : re-engineering fondamental des protocoles de compaction de session et de model switching.

### Infrastructure guardrails

**Isolation cross-modèle stricte** : les gateways API rejettent automatiquement les enveloppes AEAD générées par une version de modèle différente de celle actuellement requêtée.

**Détection d'anomalies** : velocity et anomaly detection pour flaguer les comptes soumettant des signatures identiques à travers des sessions disparates ou déclenchant des taux élevés d'erreurs de décodage.

### Révocation côté provider

**Mécanisme** : tracking et révocation active de signatures de traces spécifiques. Si pattern de replay anomal ou tentative d'extraction détectée, le provider invalide les clés/IDs associés.

**Avantage** : neutralise les compromis de traces tout en restant quasi-invisible pour les utilisateurs légitimes.

### Défenses niveau modèle

**Refusal training ciblé** : fine-tuning des modèles pour reconnaître et rejeter explicitement les prompts adversariaux conçus pour transcrire ou surfacedu raisonnement caché (jailbreaks avec balises `<thinking-copy>`).

**Combinaison** : guardrails comportementaux niveau modèle + binding cryptographique rigoureux.

### Limite structurelle fondamentale

**Constat critique** : quel que soit le modèle requêté, il doit par nécessité déchiffrer et traiter le contenu des tokens de raisonnement antérieurs. Donc, à moins de supposer le modèle lui-même pleinement robuste contre les tentatives d'extraction par prompt, les blocs de raisonnement chiffrés ne peuvent jamais être que semi-cachés — le contenu sous-jacent reste atteignable à travers le modèle qui détient implicitement la clé de déchiffrement.

**Recommandation utilisateur** : ne jamais traiter les blocs de raisonnement chiffrés comme un mécanisme de stockage confidentiel.

---

## Implications pour notre infrastructure/laboratoire

### Amorçage architecture

**Leçon 1 — Statelessness vs Security** : le design stateless (stockage client) crée des vulnérabilités systémiques par portabilité cryptographique. Notre architecture devra arbitrer explicitement entre cette simplicité opérationnelle et la sécurité par isolation contextuelle.

**Leçon 2 — Isolation cross-modèle** : toute famille de modèles déployés doit implémenter une isolation stricte des traces de raisonnement entre modèles de différentes capacités/générations. Pas de compatibilité automatique.

**Leçon 3 — Binding contextuel** : si traces chiffrées côté client, intégration obligatoire de context IDs (user, session, conversation, prompt hash) dans l'enveloppe AEAD.

### Amorçage infrastructure

**Composant 1 — Gateway avec isolation** : couche gateway API enforceant l'isolation cross-modèle et la détection d'anomalies (replay patterns, taux d'erreurs de décodage).

**Composant 2 — Key management** : infrastructure de gestion de clés avec révocation active et rotation. Possibilité d'invalider des traces spécifiques sans impacter les utilisateurs légitimes.

**Composant 3 — Audit de fuites** : pipeline de détection automatisée de PII/credentials dans les traces de raisonnement avant tout partage/publication.

### Amorçage laboratoire

**Capacité 1 — Évaluation de sécurité** : méthodologie d'évaluation de la robustesse de nos propres mécanismes de protection du raisonnement (tests de distillation, tests d'extraction de secrets, tests d'injection).

**Capacité 2 — Analyse de traces** : outils pour analyser ce qui fuit dans les traces de raisonnement (même chiffrées, via modèles décodeurs internes).

**Capacité 3 — Hygiène de publication** : protocoles stricts de nettoyage des traces avant toute publication de datasets ou de logs d'agents (strip systématique des blocs de raisonnement si information sensible exposée).

---

## Questions ouvertes pour le développement

1. **Arbitrage stateless/stateful** : quelle proportion de notre infrastructure sera stateless (simplicité, scalabilité) vs stateful (sécurité, isolation) ? Critères de décision ?

2. **Granularité du binding contextuel** : quel niveau de granularité pour le binding cryptographique (session, conversation, prompt, historique complet) ? Trade-off sécurité/complexité ?

3. **Modèles décodeurs internes** : comment tester la robustesse de nos propres modèles contre l'extraction de raisonnement ? Méthodologie de red-teaming ?

4. **Détection d'anomalies** : quels patterns spécifiques monitorer pour détecter les tentatives d'extraction/distillation ? Seuils et alertes ?

5. **Révocation** : comment implémenter la révocation de traces compromises sans impacter l'expérience utilisateur légitime ?

6. **Transparence vs Sécurité** : quelle politique de publication des vulnérabilités découvertes dans nos propres systèmes ?

---

## Références croisées (à compléter)

Ce document devra être étudié en regard de :
- [ ] Ressources sur l'architecture API stateless/stateful
- [ ] Documents sur la gestion de clés cryptographiques
- [ ] Protocoles de sécurité pour le déploiement de modèles
- [ ] Méthodologies d'évaluation de la robustesse des LLM
- [ ] Bonnes pratiques de publication de datasets d'agents

---

## Date d'analyse

2026-08-22
