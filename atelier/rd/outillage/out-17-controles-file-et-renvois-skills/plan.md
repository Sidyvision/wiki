---
title: "OUT-17 — Contrôles manquants de la file d'écritures de skills : plan"
type: outillage
chantier: OUT-17
tags: [atelier, rd, outillage, chantier, plan, skills, controles]
created: 2026-09-15
updated: 2026-09-15
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/infrastructure/2026-09-15_file-attente-morte-ecritures-skills]]"
---

# OUT-17 — Contrôles manquants de la file d'écritures de skills : plan

> **Statut** : `vise` — **visé par Sidy le 2026-09-15** : « Commite et pousse le tout et je
> valide l'ensemble pour la suite ». Les deux pièces décrites ici ont été **écrites et
> éprouvées dans la même passe** (§Vérification) : le visa est enregistré tel quel, et le
> fait qu'il suive l'écriture plutôt que de la précéder est **déclaré**, non lissé — le
> protocole veut le visa d'abord, et la consigne de Sidy portait bien sur l'ensemble du
> chantier.

## Étapes

1. **Lire** `drain-skill-queue.py` (8 866 o., embarqué par `hermes-skill-store-operations`,
   écrit par le fork, **non audité**) et en tirer ce qui est réutilisable — **ou l'écarter par
   écrit**. Lecture seule ; aucun usage tant qu'il n'a pas été lu.
2. **Écrire** `etat-file-skills.py` (~80 lignes) : parcours des profils, lecture des `*.json`,
   contrôle du contrat du magasin, sortie texte + `--json`.
3. **Écrire** `verifier-renvois-skills.py` (~70 lignes) : extraction des chemins déclarés
   *par section*, contrôle d'existence, sortie nommée.
4. **Éprouver les deux par l'échec** (§VII) en copie jetable : faute fabriquée → le contrôle
   crie ; pièce saine → silence. Résultat brut consigné, non résumé.
5. **Proposer** la ligne de rapport au job concerné — **sans l'y écrire** : modifier un job de
   production est un point de retour à l'humain.
6. **Inscrire** la ligne `OUT-17` au registre des chantiers et pointer ce dossier — une fois le
   registre libre (cf. points de retour).

## Fichiers touchés

- **Créés** : `atelier/rd/outillage/etat-file-skills.py`,
  `atelier/rd/outillage/verifier-renvois-skills.py`.
- **Modifiés** : `atelier/rd/registre-chantiers.md` (une ligne + `updated`),
  `atelier/annales.md` (entrée de passe, Cmd 9).
- **Aucun fichier copié, déplacé ni supprimé** — Cmd 10 : rien ne se supprime, un original
  devient `deprecated` s'il doit céder la place.
- **Hors dépôt, non modifié par ce chantier** : le prompt du job de rapport, qui vit dans le
  profil `studio` (`hermes cron edit`, hors dépôt).

## Vérification

- `python3 verifier-invariants.py --racine /root/wiki` — **0 erreur** attendue avant et après
  (ligne de base du dépôt au 2026-09-15 : 0 erreur, 71 avertissements, tous antérieurs).
- `python3 atelier/rd/outillage/etat-file-skills.py --json` — exécution réelle, sortie citée
  dans l'annale.
- `python3 atelier/rd/outillage/verifier-renvois-skills.py` — exécution réelle sur la flotte,
  sortie citée.
- **Épreuve de la faute** : copie jetable d'un skill portant un renvoi mort → le contrôle le
  nomme ; la copie est retirée ensuite, et la disparition du signalement est constatée.

## Points de retour à l'humain

1. **Le visa du présent plan** (Cmd 6) — sans lui, aucune ligne de code.
2. **La modification du job de rapport** (profil `studio`, hors dépôt) : elle change un
   rapport de production. Préparée, jamais appliquée sans accord.
3. **L'inscription au registre** : acte de verdict, et le fichier porte à cette heure une
   modification non commitée d'une autre passe — à faire après coup, ou sur accord explicite.
4. **Signalé, hors périmètre** : le sort des deux scripts de croisement quasi identiques
   (`croisement-tarifat.py` dans `default`, `tarifat-crossmatch.py` dans `gardien`) et
   l'absence de toute procédure pour la **vidéo** — deux points nés de la même passe, à traiter
   ailleurs.

## Journalisation

- **Annales** : `atelier/annales.md`, entrée `[YYYY-MM-DD] outillage | …`, SHA court du commit
  en dernière ligne (Cmd 9 : l'entrée s'écrit **après** le commit qu'elle décrit).
- **Registre** : `atelier/rd/registre-chantiers.md`, section 3 (`OUT`), ligne `OUT-17` +
  remontée de `updated` — **même passe** que le versement, ou la suivante si le registre est
  occupé.
- Aucune annales de circuit documentaire n'est concernée : le chantier ne touche que `rd/`.

## Résultats de la passe (2026-09-15) — versés après écriture

**Livré** : `etat-file-skills.py` (8,8 Ko) et `verifier-renvois-skills.py` (6,3 Ko), tous deux
déterministes, sans réseau, en lecture seule.

**Épreuve §VII — la faute fabriquée doit faire crier, la pièce saine doit se taire :**

| Épreuve | Fixture | Résultat |
|---|---|---|
| file saine | un profil avec une position conforme | **0 inapte**, code 0 |
| file fautive | description de 61 caractères, `name:` absent | **2 inaptes nommés**, code 1 |
| renvoi mort déclaré | `references/piece-jamais-livree.md` en liste | **RENVOI MORT** nommé, code 1 |
| citation en exemple | chemin dans un bloc de code et au fil d'une phrase | classé **mention non déclarée**, pas un renvoi mort |
| flotte réelle | 1302 skills sur 14 racines de profil | **17 renvois morts** (dont 14 fois le même, sur un skill **officiel**), 117 mentions non bloquantes |

**Sur la flotte réelle, l'instrument a payé d'emblée** : il a trouvé **six fichiers déclarés
jamais livrés, sur cinq skills** — `karubi-provisioning` (unité systemd), `doctrinal-integration`
(état de corpus Taʿrīfāt), `verdict-gated-work` (pièce de cas), `astrology-ephemeris` (deux
pièces), `deterministic-integrity-tooling` (architecture du dispositif Karūbī). **Quatre ont été
réparés par greffe depuis l'archive** — les pièces existaient, dans des positions écartées — et
**deux par retrait de la déclaration**, la pièce n'ayant jamais été proposée et le canon vivant
ailleurs au dépôt. *Mon audit manuel de la nuit en avait relevé trois : un contrôle outillé
trouve ce qu'une relecture ne trouve pas.*

**Défaut hérité, non traité car il n'est pas à nous** : `hermes-agent-skill-authoring`, skill
**officiel** présent dans les quatorze profils, déclare `scripts/run_tests.sh` qu'il ne livre
pas. Constaté, signalé, non touché.

**Reste à faire** : la ligne de rapport dans le job périodique — préparée, **non appliquée**
(point de retour à l'humain).
