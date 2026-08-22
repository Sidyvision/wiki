---
title: "Cordis — paradigme de composabilité spatiotemporelle pour systèmes dynamiques"
type: outillage
tags: [rd, outillage, paradigme, composition-dynamique, hermes, cordis, sashimono]
statut: brouillon
created: 2026-08-16
updated: 2026-08-16
sources: []
links: ["[[atelier/rd/index]]", "[[atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11]]", "[[atelier/rd/cahiers/registre-problemes]]", "[[meta/philosophie-sashimono]]", "[[doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel]]"]
statut_experience: exploratoire
---

# Cordis — paradigme de composabilité spatiotemporelle pour systèmes dynamiques

> **Statut** : `brouillon`, `exploratoire`. Fiche d'instruction d'une source
> déposée en `raw/` (lecture de fond du 2026-08-16, contrainte
> PRODUCTION/INTÉGRATION temporairement levée). Ne tranche rien sur une
> application au dépôt Hermes — pose seulement les fondations d'un chantier
> ultérieur (kari-kumi, montage à blanc).

## 1. Provenance

Source : `raw/A Programming Paradigm for Spatiotemporal Composability.pdf`
(88 p.), Shi, Zhang, Cui — Peking University / DeepSeek-AI. Papier de
recherche en génie logiciel, formel, sans contenu doctrinal — relève
entièrement du pôle `atelier/rd/`.

Précision de Sidy (2026-08-16) : cette étude accompagne la sortie du
**DeepSeek Harness**, déjà public. Sidy ne l'a pas testé lui-même, mais a
suivi des retours d'utilisateurs. Ce rapprochement est donc signalé
**kari-kumi** (suggéré, non vérifié de première main) — à confronter au
DeepSeek Harness lui-même si un test direct a lieu.

## 2. Le problème adressé

Les systèmes qui composent des modules à l'exécution (plugins, hot-reload,
architectures à composants dynamiques) souffrent typiquement de deux failles
non formalisées ensemble jusqu'ici :
- décharger un composant laisse des effets de bord non défaits (fuite d'état) ;
- un composant ne sait pas réagir proprement à l'apparition/disparition de
  ses dépendances (couplage fragile, redémarrages complets nécessaires).

## 3. Le paradigme : deux axes

- **Composabilité temporelle — effets réversibles** : chaque effet appliqué
  par un composant porte son inverse ; le runtime compose ces effets et peut
  les défaire proprement au déchargement (retour à un état antérieur garanti,
  pas de fuite).
- **Composabilité spatiale — coeffets réactifs** : chaque composant déclare
  ses dépendances comme une spécification ; le système notifie
  activation/désactivation/neutre à mesure que le contexte partagé change,
  sans redémarrage global.

Les deux dimensions sont unifiées dans un unique **type de contexte**, sur
lequel les auteurs bâtissent un calcul formel (composants, fibres, registres)
avec sémantique opérationnelle (cycle Inactive/Active, transitions de
rechargement/déchargement inertiel) et preuves de métathéorie (préservation,
composabilité temporelle et spatiale, progrès, confluence).

## 4. Cordis — l'implémentation

Méta-framework TypeScript :
- bibliothèque cœur (`ctx.effect`, `ctx.get/set`, `ctx.use`, accès au contexte
  médié par Proxy) ;
- **chargeur de composants déclaratif** (entrées de config avec id/url/
  isolate/intercept/config/disabled, réconciliation incrémentale, isolation
  par royaume réassignable) ;
- moteur de **Hot Module Replacement** en 3 phases : classification des
  modules par point fixe du graphe de dépendances → détection des entrées
  périmées → rechargement transactionnel avec retour arrière (rollback).

## 5. Validation empirique — Koishi

Cordis est validé sur **Koishi**, framework de chatbot open-source en
production depuis 4 ans, 4000+ plugins communautaires. Ce n'est pas un
prototype de laboratoire : c'est un système déployé à l'échelle qui a servi
de banc d'essai réel au paradigme.

## 6. Ce que la source dit elle-même de son avenir

Point notable (conclusion, p.79) : les auteurs citent explicitement comme
direction future les **« self-evolving agent harnesses »** — un agent IA qui
génère et remplace en continu les composants de son propre harnais, avec peu
de supervision humaine. Cette mention n'est pas une extrapolation de ma part :
c'est la propre projection des auteurs, à prendre pour ce qu'elle est (une
piste de recherche affichée, pas un résultat).

## 7. Qualification sashimono — résonance de forme avec Cordis

*(Double contrôle, §VII du protocole racine — geste de relevé, ne tranche
rien.)*

Le paradigme décrit ne se contente pas de côtoyer la convention Sashimono
déjà adoptée par le dépôt (`meta/philosophie-sashimono.md`) : il en
**instancie littéralement plusieurs articles**, en ingénierie logicielle pure.
Qualification : **homologie** (ressemblance de forme, pas généalogie alléguée
— les auteurs du papier n'ont aucune connaissance de la convention du dépôt).
Portance : **zōsaku** — l'analogie n'engage rien structurellement, elle
n'est qu'un éclairage.

- **Article 5, « l'assemblage reste démontable »** : c'est très exactement la
  thèse centrale de la composabilité temporelle — tout effet appliqué porte
  formellement son inverse, le déchargement d'un composant restitue un état
  garanti, réversibilité intégrale. L'écho le plus direct des six articles.
- **Article 3, « jamais de joint forcé »** : les coeffets réactifs — un
  composant ne s'active que si sa dépendance est effectivement présente dans
  le contexte ; sinon il reste neutre, jamais forcé à fonctionner sur un
  manque.
- **Article 4, « tout assemblage se présente à blanc »** : le rechargement
  transactionnel du HMR (phase de détection puis rechargement avec retour
  arrière) est un montage à blanc technique — rien n'est définitif avant que
  la transaction n'aboutisse, exactement le geste kari-kumi.
- **Article 1, « aucune pièce ne tient par colle »** : le refus de l'état non
  traçable — un effet qui ne porterait pas son inverse serait précisément une
  pièce qui « colle » silencieusement au contexte, contre quoi le calcul
  formel du papier se construit.
- **Article 6, « le joint parfait est invisible, jamais secret »** : l'accès
  au contexte médié par Proxy masque la jointure côté composant (le
  développeur du plugin ne voit pas la mécanique), tandis que le registre
  et la trace des effets la documentent intégralement côté runtime — masqué
  à l'usage, jamais opaque à l'audit.

Ce que cette résonance **ne dit pas** : elle ne fait pas de Cordis une
« application » de la philosophie du dépôt (aucune généalogie), et elle ne
tranche pas la piste Hermes du §8 — elle observe seulement qu'un paradigme
d'ingénierie logicielle indépendant, formalisé et validé en production
(Koishi), converge de forme avec un vocabulaire déjà opératoire ici. Verdict
sur la portée de ce rapprochement : à Sidy (Cmd 12).

### 7.1 Hypothèse de Sidy — une source orientale plus large (renvoi signalé)

Sidy formule une hypothèse plus forte que la simple homologie ci-dessus : que
la démarche de Cordis serait **inspirée de l'esprit oriental**, lui-même à la
source du sashimono, l'architecture traditionnelle chinoise intégrant ces
principes **explicitement**, avec une parenté claire à l'artisanat japonais.
Cette hypothèse porte une **filiation alléguée** (`restitution`, non
`homologie`), non vérifiable depuis le seul papier source (sommaire et
sections lues ne revendiquent aucune inspiration culturelle), et déborde le
cadre non-doctrinal de la présente fiche. Elle est instruite, en tant que
telle, dans la fiche `discernement` doctrinale déjà existante et enrichie ce
jour : `doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md`
(statut `speculatif`, verdict réservé — lien signalé, sens unique autorisé
`atelier/rd/` → `doctrinal/`).

## 8. Pistes pour le dépôt (kari-kumi, non tranché)

Rapprochement suggéré avec l'infrastructure Hermes documentée en
`atelier/rd/infrastructure/` — **aucune décision d'implémentation ici** :

- les 12 agents Hermes fonctionnent comme des composants chargés à l'exécution
  (gateways `systemctl --user`) ; un rechargement à chaud sans redémarrage
  complet du service, avec garantie de retour arrière propre, répond
  directement à un besoin déjà rencontré (frictions de déploiement notées au
  registre) ;
- les dépendances entre agents/gateways (accès scopés, canaux Telegram/Discord,
  `_inbox/` comme confluence) pourraient se déclarer comme coeffets plutôt que
  câblées en dur ;
- la mention explicite des « self-evolving agent harnesses » par les auteurs
  fait écho à la trajectoire du dépôt (agents qui orchestrent, jamais ne
  décident — §VIII du protocole racine), sans que cela n'implique une
  automatisation de la décision : la composition dynamique concerne l'
  infrastructure d'exécution, pas le verdict (Cmd 12 reste intact).

Ces pistes n'engagent aucun développement : elles posent seulement un jalon
pour un chantier ultérieur, à instruire séparément si Sidy le juge pertinent.

## 9. Non traité dans cette fiche

- Section 4.4 (preuves de métathéorie détaillées) et section 7 (travaux
  connexes) du papier : non résumées ici, jugées non essentielles au cadrage
  R&D.
- Aucun test du DeepSeek Harness lui-même : Sidy ne l'a pas encore essayé.
- Aucune décision d'architecture pour Hermes : §8 ci-dessus est un jalon, pas
  un plan.

## 10. Liens

- Charte du pôle : `atelier/rd/index.md`.
- Infrastructure Hermes : `atelier/rd/infrastructure/infrastructure-architecture-global-2026-08-11.md`.
- Registre des problèmes (frictions de déploiement citées en §7) :
  `atelier/rd/cahiers/registre-problemes.md`.
