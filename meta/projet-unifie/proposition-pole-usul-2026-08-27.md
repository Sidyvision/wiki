---
title: "Proposition — Pôle Usûl (supersède le Pôle Fiqh du 2026-07-06)"
type: meta
tags: [outillage, projet-claude-ai, usul, fiqh, doctrinal, proposition]
created: 2026-08-27
updated: 2026-08-27
---

# Proposition — Pôle Usûl du dépôt

> **Statut : validée par Sidy le 2026-08-27, exécution effective complète.**
> `doctrinal/CLAUDE.md` amendé (action EXAMEN DE FIQH → EXAMEN D'USÛL, bloc
> générique `branche: fiqh | mantiq | mustalah-hadith`) ;
> `meta/projet-unifie/proposition-pole-fiqh-2026-07-06.md` passée en
> `deprecated` avec pointeur vers la présente fiche. Fiche déplacée de
> `_inbox/` vers `meta/projet-unifie/` à l'intégration.

## 0. Supersession explicite

Cette proposition **remplace**
`meta/projet-unifie/proposition-pole-fiqh-2026-07-06.md`, validée par Sidy le
2026-07-06. Rien du contenu déjà validé n'est perdu : il est **migré
intégralement** comme la branche Fiqh du pôle Usûl (§2 ci-dessous). Si cette
proposition est validée, la fiche du 2026-07-06 passe en `deprecated` avec
pointeur vers la présente fiche (Cmd 10 — jamais de suppression sèche),
suivant le même geste que la migration `atelier/projets/` → `atelier/rd/`
du 2026-08-08.

## 1. Constat — pourquoi élargir

Sidy formule le principe : le Fiqh « n'est que l'une [des sciences
traditionnelles formelles] parmi la logique, le hadith, etc. » Le pôle validé
le 2026-07-06 ne couvrait que le Fiqh (répartition agents 04/10, textes de
base mālikite, discipline `to-source`, action EXAMEN DE FIQH). Le geste
proposé ici : ouvrir un pôle **Usûl** (racines/méthodologie des sciences
traditionnelles islamiques) qui accueille le Fiqh comme une branche parmi
d'autres, sans dissoudre ce qui est déjà acquis.

## 2. Structure proposée du pôle

**Usûl** englobe, à ce stade, trois branches identifiées (liste ouverte,
d'autres branches pourront être ajoutées sur le même modèle) :

1. **Fiqh** (branche déjà instruite) — reprend telle quelle la matière
   validée le 2026-07-06 : répartition agents 04 (instruction) / 10
   (harmonisation, pas de 13ᵉ agent dédié), textes de base *Mukhtaṣar
   al-Akhḍarī* puis *Mukhtaṣar Khalīl* (appui *Risāla* d'Ibn Abī Zayd),
   préséance mālikite stricte, discipline `to-source` jusqu'à acquisition et
   vérification physique des textes, action EXAMEN DE FIQH (bloc ⚖️, cf.
   `doctrinal/CLAUDE.md`).
2. **Manṭiq** (logique formelle) — branche neuve, non instruite. Sert
   d'outillage transversal à l'Examen formel déjà pratiqué en
   `doctrinal/discernement/` (Cmd 12 — la machine juge la forme, jamais le
   principe) : un corpus de logique traditionnelle donnerait un vocabulaire
   plus rigoureux à ce jugement de forme.
3. **Muṣṭalaḥ al-ḥadīth** (sciences du hadith — critique de chaîne et de
   texte) — branche neuve, non instruite. Utile partout où une citation
   prophétique appuie une fiche `doctrinal/` ou une position de fiqh :
   qualifier le degré de fiabilité d'un hadith cité (ṣaḥīḥ, ḥasan, ḍaʿīf...)
   relève de cette science, distincte du fiqh qui l'applique.

**Point de méthode distinct par branche** : contrairement au Fiqh, le Manṭiq
et le Muṣṭalaḥ al-ḥadīth n'ont pas de logique de préséance d'école
(*madhhab*) — la règle « mālikite d'abord, jamais de talfīq » est **propre au
Fiqh** et ne se généralise pas mécaniquement aux deux autres branches. Ce
point est signalé comme **ouvert**, pas tranché d'office par cette
proposition — à arbitrer par Sidy branche par branche à mesure qu'elles
s'instruisent.

## 3. Ce qui est reconduit sans changement

- La répartition agents 04 (instruction) / 10 (harmonisation) — confirmée le
  2026-07-06, non remise en cause par l'élargissement.
- La discipline `to-source` : toute fiche du pôle Usûl, quelle que soit sa
  branche, reste marquée jusqu'à vérification sur texte primaire possédé en
  bibliothèque physique (`atelier/rd/bibliotheque/catalogue-bibliotheque.md`
  — consultation humaine, sans wikilink, `doctrinal/` ne pointant jamais vers
  `atelier/`).
- La règle des verdicts (Cmd 12/13) : la machine compile, source, structure —
  elle n'émet jamais d'avis juridique religieux ni de verdict métaphysique ;
  le verdict appartient à Sidy ou à une autorité textuelle citée.
- La tension structurelle Gardien (10) ↔ Commerce (12) pour les questions
  d'ancrage éthique du label, inchangée.

## 4. Amendement futur nécessaire — FAIT le 2026-08-27

Amendement réalisé : [[doctrinal/CLAUDE]], section « Action : EXAMEN D'USÛL »
(remplace « Action : EXAMEN DE FIQH »), bloc normalisé générique portant le
champ `branche: fiqh | mantiq | mustalah-hadith`, sous-règles propres au fiqh
(préséance mālikite, École consultée, Recours subsidiaire) marquées
*(branche fiqh uniquement)*. Le point ouvert §2 (préséance d'école hors fiqh)
reste signalé comme ouvert dans le bloc lui-même, non tranché d'office.

## 5. Chronologie

| Date | Action | Statut |
|---|---|---|
| 2026-07-06 | Pôle Fiqh validé (répartition 04/10, textes de base, amendements CLAUDE.md) | Intégré |
| 2026-08-27 | Proposition Pôle Usûl (présente fiche) — supersession du Pôle Fiqh | Déposée, en attente |
| À l'arbitrage Sidy | Verdict sur l'élargissement, sur la structure par branche, sur le point ouvert §2 (préséance d'école hors fiqh) | Ouvert |
| Si validée | `proposition-pole-fiqh-2026-07-06.md` → `deprecated` + pointeur ; amendement `doctrinal/CLAUDE.md` (§4) | En attente |

## 6. Alertes récurrentes (reconduites du pôle Fiqh)

- **to-source** : toute fiche du pôle, toute branche confondue, reste marquée
  jusqu'à vérification sur texte primaire physique.
- **Talfīq** : règle propre au Fiqh — préséance mālikite stricte, recours
  documenté question par question, jamais mélange d'écoles au sein d'un acte.
- **Escalade légale** : les questions juridiques profanes (CNM, Sacem,
  droits) ne sont jamais tranchées par le pôle Usûl seul ; il complète, ne
  remplace jamais un professionnel qualifié.
- **Discernement / Verdicts** : la machine documente et propose ; Sidy décide
  (Cmd 13) — sans exception de branche.
