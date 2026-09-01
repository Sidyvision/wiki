---
title: "Jalon — chronologie de l'ouverture du pôle R&D (2026-08-08 → 2026-08-31)"
type: outillage
tags: [atelier, rd, cahier, jalon, chronologie]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# Jalon — chronologie de l'ouverture du pôle R&D

> **Pourquoi cette fiche existe.** La charte du pôle ([[atelier/rd/index]]) portait une
> section « État de la phase 1 partielle » qui, ouverte le 2026-08-08 pour dire ce qui
> était fait et ce qui restait, s'est allongée jusqu'à devenir un journal chronologique
> de près de cent lignes — un journal logé dans une charte. Le contenu est **déplacé ici
> sans la moindre retouche** (Cmd 10 : déplacement et pointeur, jamais suppression) ; la
> charte garde un résumé de dix lignes et renvoie à la présente fiche.
>
> Ce texte est un **jalon** : il dit ce qui s'est ouvert et quand, entre le 2026-08-08 et
> le 2026-08-31. Il ne dit pas l'état courant. Pour l'état courant des chantiers :
> [[atelier/rd/registre-chantiers]].

---

## Chronologie, telle qu'elle figurait dans la charte

*(Contenu déplacé sans retouche. Il commençait par l'état de la phase 1 partielle
et s'est progressivement allongé de tout ce qui s'ouvrait au pôle.)*

### État de la phase 1 partielle

- **Ouvert** : le lieu (présente charte + arborescence), le Sceau atelier étendu
  (§V.a : types `experience | infrastructure | outillage`, champ optionnel
  `statut_experience`), le régime de liens (§VI : `rd/` hérite du régime de
  `projets/`), l'élargissement de `liens_atelier` (§V.d), les annales de
  l'atelier au Cmd 9.
- **Migration effectuée le 2026-08-08** (fiche par fiche, §IV) : 16 fiches de
  `atelier/projets/` migrées vers `rd/instrument/` (15) et `rd/outillage/` (1),
  slugs conservés ; chaque ancienne fiche subsiste en stub `deprecated` avec
  pointeur (Cmd 10) ; assets (`assets-instrument/`), données
  (`instrument-donnees.yaml`, `wiki-manifest.json`), prototype et script
  `generer-manifeste.py` déplacés avec les fiches ; liens entrants repointés.
  `album-personnel.md` resté en `projets/` a été déplacé le même jour vers
  `label/production/` (verdict Sidy : création artistique, non R&D) — stub
  `deprecated` avec pointeur, 4 liens entrants `materiel/` coupés (étanchéité).
- **Non inclus dans la phase 1 partielle** (viennent ensuite) :
  la discipline de laboratoire complète (bloc 🧪 Expérience, règle de
  reproduction) — phase 2 ; l'agent de veille
  infrastructure (phase 3, sur désignation de Sidy) — voir
  [[atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11|proposition
  phase 3]] (archivée 2026-08-12, `brouillon`) : désignation de principe
  tranchée (Studio Sound Engineer, position 9, canal `#infrastructure`, cron
  quotidien midi, rapport en 5 sections), mais **aucune écriture
  d'automatisme effectuée** — extension du prompt d'agent, accès FS/exécution
  et mécanisme technique restent à instruire séparément (Cmd 6).
- **Registre des problèmes ouvert le 2026-08-08** (verdict Sidy, premier cahier
  concret de la phase 2) : [[atelier/rd/cahiers/registre-problemes]] — append-only, format
  Symptôme brut / Diagnostic / Résolution / Compréhension tirée / Liens / Statut ;
  amorcé rétroactivement avec 3 entrées de la session de migration. Tout problème,
  erreur ou blocage rencontré dans les travaux du pôle doit y être consigné ; un
  échec se consigne comme un succès (règle 3 du laboratoire).
- **Outillage déterministe (session du 2026-08-11)** :
  [[atelier/rd/outillage/spec-detecter-non-tracke|detecter-non-tracke.py]] —
  constat des fichiers non trackés par git, classé par circuit (même famille
  que `verifier-invariants.py`, ni LLM ni réseau).
- **Bilan pont inter-agents (2026-08-15)** :
  [[atelier/rd/cahiers/bilan-2026-08-15-pont-agents|bilan 2026-08-15]] — synthèse
  de la période 2026-08-08 → 2026-08-15 destinée à tout agent (Hermes terminal,
  Claude Code, ou autre) reprenant le fil des travaux R&D sans contexte antérieur :
  ce qui est tranché et committé, ce qui est en cours, chantiers ouverts par
  priorité, leçons transversales. Aucun contenu doctrinal.
- **Leçons du chantier bibliothèque (2026-08-22)** :
  [[atelier/rd/cahiers/2026-08-22_lecons-chantier-bibliotheque-index-livres|leçons
  chantier bibliothèque]] — retour d'expérience de la conception de l'outillage
  d'index/glossaires : malentendu de cadrage, propagation Unicode par copie,
  outil qui contient ce qu'il interdit, jugement calculé plutôt que déclaré,
  panne silencieuse d'un contrôle non armé, absence de dépôt git. Le retour
  sur la formation de l'agent proprement dite reste à écrire après le lot 1.
- **Compte-rendu — première session d'un nouveau moteur en poste INTÉGRATION
  (2026-08-28)** :
  [[atelier/rd/cahiers/2026-08-28_compte-rendu-premiere-session-integration-qoder|
  compte-rendu 2026-08-28]] — retour d'expérience de la première session du
  moteur Qoder dans la fonction INTÉGRATION (Cmd 14) : incident append-only
  découvert et restauré (en-tête d'entrée remplacé à l'insertion, non détecté
  par le vérificateur — entrée au registre même date), données de calibrage du
  vérificateur (0 erreur / 17 avertissements, typologie des C1), suppression du
  manifeste racine orphelin, observation multi-rédacteurs (5 commits Hermes
  concurrents sans collision), lisibilité du protocole par un moteur à froid.
  Propositions ouvertes : contrôle A6 « corps d'entrée orphelin », convention
  pour les wikilinks d'exemple, verdict sur un lien C4.
- **Compte-rendu — malentendu du rapport conjoint et reprise (2026-08-20)** :
  [[atelier/rd/cahiers/2026-08-20_compte-rendu-malentendu-gardien-reprise-session|compte-rendu
  2026-08-20]] — le Gardien n'avait pas répondu à la demande de Sidy (pistes
  de développement Instrument/infrastructure), diagnostic à deux causes
  distinctes (enlisement technique déjà consigné + dérive de cadrage),
  chronologie complète de la reprise (pistes, prototype, registres, Vêdânta),
  et auto-critique d'un raisonnement fautif corrigé en session par Sidy.
  Leçons transversales pour l'atelier/R&D.
- **Extension du mandat — veille externe + sandbox (2026-08-18)** :
  [[atelier/rd/cahiers/proposition-extension-veille-rd-2026-08-18|proposition
  extension veille R&D]] — ouverture de `rd/veille/` (veille hebdomadaire
  GitHub/arXiv/dépôts, qualitatif, temps long) et d'une sandbox isolée hors
  dépôt (`/root/sandbox-rd/`) pour éprouver des montages. Mandat élargi du
  Studio Sound Engineer (un seul agent, deux registres : infrastructure
  interne quotidienne + veille externe hebdomadaire). Exécution effective
  dès 2026-08-18 ; le mécanisme d'automatisation (cron, prompt) reste à
  instruire séparément (Cmd 6, non bloquant).
- **Archive du monitoring quotidien (2026-08-18, ingestion automatisée
  2026-08-19)** :
  [[atelier/rd/infrastructure/monitoring-archive-charte|charte de l'archive]]
  — suggestion Sidy, rétention 40 jours du rapport
  `monitoring-infrastructure-quotidien` livré via Discord, désormais aussi
  copié dans `rd/infrastructure/monitoring-archive/` (`.txt`, jamais `.md` —
  motif : [[atelier/rd/outillage/spec-archiver-monitoring-quotidien|
  archiver-monitoring-quotidien.py]]). Ingestion tranchée : cron Hermes dédié
  (`archiver-monitoring-quotidien`, profil `studio`, id `5eb46eed6ba0`, via
  enveloppe `archiver-monitoring-quotidien-cron.sh` — un job `no_agent` ne
  transmet aucun argument à son script). Découverte annexe du 2026-08-18 —
  le job cron `coherence-infrastructure-brute` (contrôle anti-fabulation
  censé exister depuis le 2026-08-17) échouait depuis sa création, jamais
  documenté — **réparée le même jour** en deux temps (script introuvable,
  puis faux succès silencieux découvert par vérification mécanique de la
  sortie persistée) : [[atelier/rd/cahiers/registre-problemes]], entrée
  `[2026-08-18]` (« Suite de l'entrée précédente »).
