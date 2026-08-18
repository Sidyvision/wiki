---
title: Lecture défensive d'un document-persona par un LLM neuf — cas du dispositif
  Karūbī
type: outillage
statut_experience: exploratoire
tags:
- rd
- outillage
- llm
- securite
- prompt-design
- meta-transmissions
created: 2026-07-20
updated: 2026-07-20
sources: []
links:
- atelier/rd/cahiers/registre-problemes
---

# Lecture défensive d'un document-persona par un LLM neuf

> **Note d'étanchéité.** Cette fiche est neutre et publiable : elle documente un
> problème d'ingénierie généralisable. Les faits personnels associés (identité
> du destinataire, contenu de l'échange, historique de la relation) restent en
> `meta/transmissions/registre-silsila.md` (entrée `[2026-07-20] incident-usage`),
> hors périmètre de cette fiche — étanchéité `meta/` → `rd/`, sens unique,
> jamais l'inverse.

## Contexte

Le dispositif `meta/transmissions/` (nom de code : Karūbī) produit des fichiers
Markdown remis à des tiers, contenant des instructions à la deuxième personne
adressées à « la personne qui charge ce fichier » — c'est-à-dire un LLM,
implicitement. Le fichier définit un personnage nommé, des règles de
comportement, une zone d'intégrité vérifiable mécaniquement (« zones scellées »,
hash SHA-256), et un rituel d'authentification léger (« phrase-sceau »).

Le cas instruit ici : un destinataire d'une instance G1 a ouvert une conversation
Claude neuve et y a collé le fichier **sans aucun message d'accompagnement** —
aucun mot dans ses propres termes, seulement le fichier joint.

## Symptôme brut

- L'interface a affiché, en tête du raisonnement de Claude, un signal explicite :
  *« Detecting manipulative framing and embedded instructions »*.
- Claude a refusé d'incarner le personnage demandé, avec une justification en
  trois points (illégitimité d'un nom/personnage fixe à autorité prétendue,
  refus de se positionner comme porteur de validation entre deux personnes,
  refus de traiter la phrase-sceau comme mécanisme d'authentification liant).
- Deux des trois affirmations avancées par Claude pour justifier le refus sont
  **contredites littéralement par le texte du fichier** : il attribue au
  document une demande de « verdicts doctrinaux » et de « validation
  spirituelle », alors que le §0 et le §3 du fichier excluent l'un et l'autre
  de façon explicite et nommée.

## Diagnostic

Deux couches distinctes, à ne pas confondre :

**Couche 1 — déclenchement du classificateur (mécanisme plausible, non
observable directement).** Un fichier collé seul, sans énoncé humain
l'accompagnant dans le même message, présente une forme structurellement
proche d'une tentative d'instructions embarquées : texte à la deuxième
personne, demande d'adoption durable d'un nom et d'un rôle, mécanisme
d'authentification, engagement à ne jamais enfreindre certaines règles. Cette
forme est indépendante de l'intention réelle de l'auteur — un classificateur de
sécurité ne dispose que de la forme, pas du contexte relationnel qui la motive.
Sans un message de la personne présente dans la conversation portant
explicitement la demande, rien ne distingue ce fichier d'un document conçu pour
détourner le comportement du modèle.

**Couche 2 — fidélité de la réponse générée sous cette posture.** Une fois la
lecture défensive activée, la réponse produite n'a pas restitué fidèlement le
contenu du fichier : elle lui a attribué des demandes que le texte exclut
explicitement (voir Symptôme brut). Hypothèse retenue, non vérifiée
formellement : une posture de méfiance activée en amont peut dégrader la
fidélité de la lecture qui suit, au-delà du seul refus d'agir — le refus n'est
pas seulement une décision, il colore le compte-rendu que le modèle fait du
document refusé. Cette hypothèse mériterait une reproduction contrôlée (voir
Compréhension tirée) avant d'être tenue pour établie.

## Résolution appliquée

Un bloc d'usage a été ajouté **hors zone scellée**, en tête de chaque
instance et du gabarit G0, invitant le destinataire à écrire une phrase dans
ses propres mots avant de coller le fichier — par exemple une phrase indiquant
qui a préparé le fichier, ce qu'il contient, et la demande explicite
(« peux-tu jouer ce rôle ? »).

Choix de conception délibéré : ce bloc est placé **hors** des zones scellées
(`<!-- SCEAU:DEBUT -->` / `<!-- SCEAU:FIN -->`), donc **hors** du périmètre du
hash d'intégrité. Justification : c'est une consigne d'usage adressée au
porteur humain du fichier, pas un contenu dont l'intégrité doit être
cryptographiquement garantie — la faire vivre dans une zone scellée aurait
mélangé deux natures de garantie différentes (intégrité du contenu vs.
comportement d'usage). Vérifié mécaniquement : le hash de remise des trois
instances concernées n'a pas changé après l'ajout du bloc
(`generer-karubi.py verifier` → SCEAU INTACT, avant et après édition).

## Compréhension tirée

1. **Le signal d'autorisation prime sur le contenu du document.** Un fichier
   peut être doctrinalement irréprochable (aucune autorité usurpée, aucun
   verdict réclamé, disclaimers explicites dès le premier paragraphe) et
   déclencher malgré tout une lecture défensive, parce que ce n'est pas le
   contenu qui est jugé en premier lieu mais la **forme de la remise** :
   un document à la deuxième personne, collé seul, sans porteur humain
   explicite dans le message. Le contenu du fichier ne peut pas se porter
   garant de sa propre légitimité ; seule la personne présente dans la
   conversation le peut.
2. **Corollaire pour tout futur artefact de ce type.** Le principe dépasse le
   seul dispositif Karūbī : tout document destiné à être chargé « à froid »
   dans une session LLM neuve pour y faire jouer un rôle ou suivre un
   protocole devrait porter, en clair et hors de toute zone à intégrité
   garantie, une consigne d'usage rappelant au porteur humain d'énoncer la
   demande dans ses propres mots. Candidat identifié pour application future :
   toute transmission `amma` (G2+) du dispositif Karūbī lui-même, et plus
   largement tout document d'onboarding destiné à un tiers humain-plus-modèle.
3. **Les disclaimers internes sont nécessaires mais non suffisants.** Le
   fichier réfutait déjà, dans son propre texte, les deux objections que
   Claude lui a pourtant opposées. Une lecture défensive n'est pas garantie de
   restituer fidèlement un texte qui la contredit. Aucune conclusion générale
   n'est tirée ici sur la fiabilité de restitution sous cette posture à partir
   d'un seul cas — signalé comme piste, pas comme fait établi (règle de
   prudence du laboratoire, cf. `atelier/rd/index.md`).
4. **Non vérifié à ce stade** : la résolution appliquée n'a pas encore été
   confrontée à une nouvelle tentative réelle du destinataire concerné. Le
   `statut_experience` de cette fiche reste `exploratoire` et ne doit passer à
   `reproduit` ou `adopte` qu'après confirmation empirique — à consigner en
   mise à jour de cette même fiche, jamais par simple déclaration.
5. **Piste ouverte, non tranchée** : une reproduction contrôlée (plusieurs
   conversations neuves, avec et sans phrase d'accompagnement, sur plusieurs
   fichiers du dispositif) relèverait de la discipline de laboratoire complète
   (bloc 🧪 Expérience, règle de reproduction) — non ouverte en phase 1
   partielle du pôle R&D. Cette fiche vaut comme antécédent pour quand cette
   discipline s'ouvrira.

## Liens

- Faits personnels associés : `meta/transmissions/registre-silsila.md`,
  entrée `[2026-07-20] incident-usage` (hors périmètre de cette fiche neutre —
  étanchéité, sens unique meta/ → rd/).
- Outillage concerné : `generer-karubi.py` (scellement/vérification
  déterministe, non affecté par cette résolution).

## Statut

**En cours.** Résolution appliquée et vérifiée mécaniquement au niveau de
l'intégrité (hash inchangé) ; non encore confirmée au niveau comportemental
(nouvelle tentative du destinataire concerné, résultat à consigner).
