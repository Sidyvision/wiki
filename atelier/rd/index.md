---
title: "Pôle R&D de l'atelier — charte du lieu"
type: index
tags: [atelier, rd, infrastructure, souverainete]
created: 2026-08-08
updated: 2026-08-30
sources: []
links: []
---

# Pôle R&D de l'atelier (`atelier/rd/`)

Ouvert le 2026-08-08 sur verdict de Sidy (Option C, nom `rd/`, phase 1
partielle). Ce pôle n'est **pas un sixième circuit** : il vit à l'intérieur du
circuit `atelier/`, dont il hérite le Sceau (§V.a) et le régime de liens
(§VI). Proposition d'origine :
(cf. Domaine Réservé, fiche le pôle R&D de l'atelier) (brouillon visé pour son architecture par le verdict).

## Mission (verdict du 2026-08-08)

> « Tout ce qui en relève doit systématiquement y être consigné avec comme but
> l'entretien, le développement qualitatif, l'optimisation à mesure de
> l'infrastructure globale hardware/software, l'émancipation progressive de
> tout intermédiaire de service tiers par souveraineté des moyens de
> production / déploiement / information. Un des agents sera chargé de veiller
> à cette tâche spécifique. »

Le pôle est donc un **lieu de consignation systématique** : tout travail
d'ingénierie — technique, matérielle, logicielle, outillage, infrastructure —
a vocation à y laisser trace. Horizon : que le dépôt devienne
un véritable laboratoire ; visée : la souveraineté des moyens.

**Nature du pôle** (précision Sidy, 2026-08-08) : `rd/` est dédié aux aspects
**ingénierie / technique / mécanique** de l'infrastructure — informatique,
studio audio, etc. Ce n'est **pas un département d'expression créative** au
sens strict ; la créativité n'y existe que sous sa forme ingénieriale (la
résolution de problème). Les œuvres, leur écriture, leur direction artistique
relèvent du label — jamais de `rd/`.

## Arborescence

```
atelier/rd/
├── index.md           ← la présente charte
├── instrument/        ← l'Instrument (migration depuis atelier/projets/, fiche par fiche)
├── infrastructure/    ← setup réel : serveur, agents, hardware/software
│                         (destination de la transposition Mother Base §5 bis)
│   └── monitoring-archive/  ← archive .txt du rapport monitoring quotidien
│                              (rétention 40 j, ouvert 2026-08-18)
├── audio/             ← ingénierie son GÉNÉRIQUE (bancs d'essai, chaînes, mesures) ;
│                         l'ingénierie PAR MORCEAU reste au label
├── outillage/         ← scripts, leur documentation, leurs bancs de test
├── veille/            ← veille externe R&D (GitHub, arXiv, dépôts) —
│                         ouvert 2026-08-18, hebdomadaire, qualitatif
├── cahiers/           ← cahiers append-only : registre-problemes.md (ouvert
│                         2026-08-08, échecs/blocages), journal-optimisations.md
│                         (ouvert 2026-08-30, réussites — miroir du registre),
│                         bilan-pont 2026-08-15, comptes-rendus de sessions ;
│                         cahiers d'expérience à venir (phase 2)
├── bibliotheque/      ← catalogue de la bibliothèque physique (déplacé de
│                         `meta/` le 2026-08-22), fiches `index-livre`
│                         transcrites des index et glossaires photographiés,
│                         validateur et générateur du lexique unifié
└── citadelle-du-sham/ ← prototype 3D reçu au sas, versé ici le 2026-08-22
```

### `bibliotheque/` — instrument de repérage (ouvert 2026-08-22)

| pièce | rôle |
|---|---|
| `catalogue-bibliotheque.md` | recension des ouvrages possédés (ex-`meta/bibliotheque-physique.md`) |
| `index-<slug>.md` | un index ou glossaire transcrit par ouvrage — `terme → page`, aucun contenu doctrinal |
| `valider-index-livres.py` | contrôles bloquants : Cmd 15, pages numériques, couverture photo, doublons signalés jamais fusionnés |
| `generer-glossaire-unifie.py` | lexique unifié dérivé — refuse de générer si le validateur bloque |
| `glossaire-unifie.md` | **artefact dérivé, jamais édité à la main** |

Usage : savoir *où chercher*. La levée d'un `to-source` reste la vérification du
texte primaire par Sidy (§VII) — l'instrument dit où regarder, jamais quoi
conclure. `doctrinal/` ne lie jamais vers `atelier/` : la consultation est
humaine, sans wikilink.

## Régime des deux sous-régimes de l'atelier

- **référence** : `atelier/materiel/`, `atelier/entretiens/` — ce qu'on consulte ;
- **recherche** : `atelier/rd/` et `atelier/etudes-de-cas/` — ce qu'on instruit.

## Ce qui vit où (frontières)

| Matière | Destination |
|---|---|
| Specs, itérations, notes d'impact de l'Instrument | `rd/instrument/` (migration de `projets/`) |
| Architecture générique du serveur et des agents, bancs, mesures | `rd/infrastructure/` (ex. [[atelier/rd/infrastructure/synchro-obsidian-working-copy-github]], [[atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11]]) |
| Motifs des décisions, credentials, prompts d'agents | **reste en `meta/projet-unifie/`** (sensible — §VI) |
| Ingénierie d'une œuvre, par morceau | **reste au label** (`label/musique/ingenierie/`) |
| Expression créative : œuvre, écriture, direction artistique | **label** (direction-artistique / production) — jamais `rd/` |
| Fiches machines, manuels, routing | **reste en `atelier/materiel/`** (référence) |
| Scripts déterministes du dépôt et leur documentation | `rd/outillage/` |
| Veille externe R&D (GitHub, arXiv, dépôts scrutés) | `rd/veille/` (ouvert 2026-08-18, hebdomadaire) |
| Sandbox (éprouve de montages issus de veille) | **hors dépôt** (`/root/sandbox-rd/`) |

La frontière `meta/` ↔ `rd/` suit la règle existante : jamais de fait personnel
ni de motif sensible dans une page neutre ; `rd/` reçoit ce qui est publiable
dans le dépôt.

## État de la phase 1 partielle

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
