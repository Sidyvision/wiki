---
title: "OUT-17 — Contrôles manquants de la file d'écritures de skills : intention"
type: outillage
chantier: OUT-17
tags: [atelier, rd, outillage, chantier, intent, skills, controles]
created: 2026-09-15
updated: 2026-09-15
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/infrastructure/2026-09-15_file-attente-morte-ecritures-skills]]"
  - "[[atelier/rd/outillage/2026-08-23_inventaire-outillage-deterministe]]"
---

# OUT-17 — Contrôles manquants de la file d'écritures de skills : intention

## Le besoin

Constaté le 2026-09-15, **non supposé** : la file d'écritures de skills de la flotte Hermes a
retenu **215 positions pendant 38 jours** (238 opérations, 105 sujets distincts, **0
appliquée**) sans qu'aucun contrôle ni rapport périodique ne le dise. Le dépouillement a mis
au jour **trois vérifications absentes**, chacune ayant coûté un silence :

1. **À l'entrée** — rien ne confronte une proposition au contrat du magasin de skills :
   description bornée à 60 caractères, frontmatter YAML valide, champ `name:` présent. Sur
   les onze requêtes retenues d'un même lot, **cinq étaient inaptes** ; une sixième n'avait
   même pas de champ `name:`.
2. **En file** — rien ne publie ce qui est retenu. Aucun cron, aucun rapport, aucune alerte ;
   la seule surface de dépouillement est `/skills pending`, dans une session ouverte.
3. **À la sortie** — rien ne confronte les fichiers qu'un skill déclare (`references/`,
   `templates/`, `scripts/`, `assets/`) à ceux réellement livrés. **Trois renvois morts** ont
   été trouvés à la main ce jour-là, sur 22 skills créés.

Mesures, méthode et écarts : [[atelier/rd/infrastructure/2026-09-15_file-attente-morte-ecritures-skills]].

## Qui le porte

Sidy (verdict, et visa du plan) ; la session Hermes du profil par défaut pour l'écriture.
Destinataires : les profils de la flotte — `gardien`, `studio`, `publication` en premier —
et l'agent de veille qui produit déjà un rapport quotidien.

## Hors périmètre

- **Ne touche pas au code de Hermes.** Le défaut d'entrée vit dans l'amont
  (`tools/write_approval.py`, `tools/skill_manager_tool.py`) : ce chantier **constate de
  l'extérieur** et ne patche pas le produit. Un correctif amont est une autre affaire, à
  porter ailleurs si verdict.
- **Ne dépouille pas la file.** Approuver ou rejeter une position est un acte de verdict
  (Cmd 13) ; le chantier mesure et publie, il ne décide rien.
- **Ne touche ni à la porte ni au fork.** Les options C et D ont été tranchées le
  2026-09-15 : rien n'est éteint.
- **N'écrit aucune fiche doctrinale.** Il ne touche que `rd/outillage/`.

## Contraintes doctrinales

- **Cmd 6** : aucun code écrit avant un `plan.md` visé — la présente intention ne vaut pas
  autorisation.
- **Cmd 12** : rien n'est tranché ici. Un désaccord sur *ce qu'il faut mesurer* revient à
  Sidy ; le chantier ne choisit pas à sa place.
- **Cmd 10** : réversibilité — les scripts créés sont neufs, aucune pièce existante n'est
  modifiée ni supprimée ; l'inscription au registre est additive.
- **§VII, Épreuve des contrôles** : un contrôle s'éprouve **par l'échec** (faute fabriquée →
  le contrôle crie), jamais réputé bon parce qu'il est vert. Contre-exemple de référence :
  PRO-01 (2026-08-31), le contrôle qui gardait `main` sans rien regarder.
- **Cmd 14** : le détail de l'affaire vit dans la fiche d'infrastructure ; cette intention ne
  recopie rien.

## Le signe de réussite

**Une ligne** dans un rapport périodique qui existe déjà, nommant : le nombre de positions en
file par profil, la plus ancienne, et le nombre de propositions **inaptes**. Et un contrôle de
sortie qui, lancé sur la flotte, désigne **nommément** tout skill déclarant un fichier absent.
Observable : une sortie de commande citée, jamais une promesse.

## Ce qui reste ouvert

- **Le rapport d'accueil** — le rapport Studio du matin (où `verifier-invariants.py` a été
  réintégré le 2026-09-13) est le candidat naturel : **à confirmer par Sidy**, cela modifie un
  job de production.
- **L'audit de `drain-skill-queue.py`** (8 866 o., embarqué par le skill
  `hermes-skill-store-operations`, écrit par le fork) : **à lire avant tout usage** — il n'est
  pas adopté.
- **L'inscription de la ligne `OUT-17` au registre** : différée. Le registre porte, à l'heure
  de cette fiche, une modification **non commitée d'une autre passe** (chantier `OUT-16`), et
  l'inscription est un acte de verdict.
- **Le numéro** : `OUT-16` étant porté par la ligne non commitée de cette autre passe,
  `OUT-17` est pris par défaut. Si cette ligne n'est pas retenue, renuméroter — jamais
  supprimer.
