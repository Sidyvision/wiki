---
title: "Proposition — amendement de la règle d'immuabilité de `textes/` (§II du protocole racine)"
type: meta
tags: [protocole, textes, immuabilite, unicode, proposition, vise]
created: 2026-09-15
updated: 2026-09-15
---

# Proposition — amendement de la règle d'immuabilité de `textes/`

> **Statut : visé par Sidy le 2026-09-15** — « Je valide la proposition, commit ».
> La fiche portait au propre un amendement **déjà rendu oralement** par Sidy le
> 2026-09-14, afin qu'il cesse de n'exister que dans le fil d'une session. Le visa
> rendu, le §5 a été exécuté : le §II du protocole racine porte la rédaction du
> point 2, l'amendement est consigné au
> `meta/protocole-archives/changelog-CLAUDE.md`, et la version antérieure du
> protocole est archivée en `meta/protocole-archives/CLAUDE-v5_2026-09-15.md`.
> Le point 4 (champ `updated:` dans `textes/`) **reste ouvert** : il est déclaré,
> non tranché, conformément aux termes mêmes de cette fiche.

## 0. Pourquoi cette fiche existe

Sidy a rendu le 2026-09-14 le verdict suivant :

> « `textes/` peux être corrigé sans problème lorsque que c'st qualitativement
> justifier »

Ce verdict **amende** le §II du protocole racine, qui énonce aujourd'hui, à
plat :

> **Règle d'immuabilité** : un texte de `textes/` ne se corrige pas. Une
> conversion meilleure le remplace, datée.

L'amendement a été appliqué le 2026-09-15 (retrait de 220 sauts de page U+000C
dans `textes/a-popular-dictionary-of-shinto-bocking/`). Mais il n'est **consigné
nulle part de durable** : la session qui lira le protocole demain y trouvera la
règle non amendée et s'en tiendra à elle. C'est exactement ce que le Cmd 14
proscrit — la lettre de toute règle en vigueur doit figurer dans le protocole,
et elle seule.

La machine ne peut pas amender le texte du protocole (Cmd 13 : la porte humaine
porte sur tout ce qui engage). Elle peut en rédiger la proposition. C'est
l'objet de cette fiche, et c'est sa seule prétention.

## 1. La difficulté que l'amendement tranche

Deux corrections ont été appliquées à `textes/` sans que la règle nue ne les
autorise, chacune sur le même raisonnement :

| Date | Objet | Raisonnement tenu |
|---|---|---|
| 2026-09-14 | 1562 contrôles bidirectionnels, `textes/ghazali-ihya-ulum-al-din-arabe/` | « ces marques n'appartiennent pas à l'œuvre, elles sont injectées par la couche de rendu » |
| 2026-09-15 | 220 sauts de page U+000C, `textes/a-popular-dictionary-of-shinto-bocking/` | même motif, et le repère de page est déjà porté en clair par `<!-- page N -->` |

Dans les deux cas, ce qui a été retiré n'était **pas du texte** : c'était de
l'artefact d'extraction, produit par l'outil et non par l'auteur. La règle nue
ne distinguait pas les deux, et c'est cette indistinction que l'amendement lève.

Il y a en outre un motif propre, qui n'est pas d'élégance. Un U+000C invisible
**fausse les mesures sans s'annoncer** : le comptage des chapitres de la
traduction anglaise de l'Ihyâ' a donné 64 au lieu de 41 pendant deux tours, la
classe `[[:space:]]` d'une ancre `grep` absorbant ce caractère. Un texte qu'on
ne corrige jamais est un texte sur lequel on mesure faux indéfiniment.
Consigné en `atelier/rd/incidents/2026-09-14_amortissement-constat-doctrinal-traduction-ihya.md`.

## 2. Rédaction proposée pour le §II

Remplacer le paragraphe « Règle d'immuabilité » du §II (section
`textes/` — le cabinet de lecture) par :

> **Règle d'immuabilité, amendée le 2026-09-14 (verdict Sidy).** Un texte de
> `textes/` ne se corrige pas *dans sa substance* : ce qui relève de la leçon,
> de la graphie ou du découpage appelle une conversion meilleure, datée, qui
> remplace la précédente. Il se corrige en revanche **lorsque c'est
> qualitativement justifié**, et la justification est d'un seul ordre : ce qui
> est retiré n'appartient pas à l'œuvre, mais à la couche d'extraction qui l'a
> rendue — contrôles bidirectionnels, formes de présentation, sauts de page,
> invisibles du Cmd 15. Trois conditions tiennent ensemble, et aucune ne se
> dispense :
>
> 1. **Le retrait est démontré non substantiel**, par une mesure rapportée
>    brute — non par l'appréciation de qui l'opère.
> 2. **Il est exécuté par un script déterministe**, versionné au dépôt, dont le
>    garde-fou a été **vu refuser** sur un cas fabriqué (§VII, épreuve des
>    contrôles).
> 3. **Il est consigné dans l'`index-conversion.md` de la conversion** — date,
>    objet, nombre, chaîne, contrôle après coup. Le cartouche des tranches ne
>    porte rien : les tranches n'ont pas de cartouche, et l'index est le seul
>    porteur de métadonnée de la conversion.
>
> Ce qui se **dit** d'un texte continue de se dire dans une fiche
> `doctrinal/sources/`, qui porte le Sceau et le statut. L'index de conversion
> consigne ce qui a été **fait au fichier**, jamais ce qui se juge de l'œuvre.

## 3. Ce que la proposition ne fait pas

- Elle n'ouvre **aucune correction éditoriale** : ni orthographe, ni coquille
  d'OCR, ni normalisation de graphie. Une graphie fautive relève de la
  conversion meilleure, datée — la règle sur ce point est inchangée.
- Elle ne crée **aucune passe de masse**. Chaque correction porte sur une
  conversion nommée, et se consigne dans son index.
- Elle ne tranche pas la question ouverte du point 4 ci-dessous.

## 4. Point laissé au verdict — le champ `updated:` dans `textes/`

Constat, non proposition. Les tranches de texte de `textes/` **ne portent aucun
cartouche** : `01-a.md` du corpus Shinto commence directement par son marqueur
de pagination. Le seul fichier porteur d'un cartouche, dans chaque conversion,
est son `index-conversion.md` — et ni celui du Shinto (`created: 2026-09-10`) ni
celui de l'Ihyâ' arabe (`created: 2026-09-14`) ne porte de champ `updated:`.

Le Cmd 8 veut que toute écriture remonte `updated:`. La question est donc : un
`index-conversion.md` doit-il porter ce champ, et le recevoir lors d'une
correction comme celle du 2026-09-15 ? La machine ne l'a pas ajouté de sa propre
autorité — ce serait instituer une convention pour `textes/` sans verdict, et le
vérificateur ne la réclame pas (`textes/` est exempté du contrôle B0 par
`PREFIXES_SANS_FM`). L'écart est déclaré plutôt que comblé (Cmd 12).

## 5. Exécution, si visa

1. Amender le §II du protocole racine selon le point 2.
2. Consigner l'amendement dans
   `meta/protocole-archives/changelog-CLAUDE.md` (append-only), entrée
   `[2026-09-14] amendement | §II — Règle d'immuabilité de textes/`.
3. Archiver la version antérieure du protocole dans
   `meta/protocole-archives/` (Cmd 10 — jamais de suppression sèche).
4. Passer le statut de la présente fiche de `brouillon` à `vise`.
5. Trancher le point 4, ou le laisser ouvert en le nommant.

## Renvois

- `textes/a-popular-dictionary-of-shinto-bocking/index-conversion.md` — la
  correction du 2026-09-15, consignée.
- `textes/ghazali-ihya-ulum-al-din-arabe/index-conversion.md` — étape 3, le
  précédent sur lequel la seconde correction s'est fondée.
- `atelier/rd/incidents/2026-09-14_amortissement-constat-doctrinal-traduction-ihya.md`
  — cinquième clause, de l'inspection préalable des octets.
- `atelier/rd/outillage/nettoyer-sauts-de-page-textes.py` — la chaîne.
