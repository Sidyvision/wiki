---
title: "Proposition — Pôle Fiqh, double face du Gardien du Protocole, Rapport du matin"
type: meta
tags: [outillage, projet-claude-ai, fiqh, label, gardien, hermes, proposition]
created: 2026-07-06
updated: 2026-07-06
---

# Proposition — Pôle Fiqh du dépôt et harmonisation Label ↔ Doctrine

> **Statut : validée par Sidy le 2026-07-06** sur les deux points ouverts :
> 1. **Répartition 04/10 confirmée** (pas de 13ᵉ agent : 04 instruit le fiqh, 10
>    harmonise) — la correspondance duodénaire n'est pas affectée.
> 2. **Textes de base de l'école confirmés** : *Mukhtaṣar al-Akhḍarī* (base), puis
>    *Mukhtaṣar Khalīl* (niveau avancé) — **non encore possédés en bibliothèque
>    physique** : acquisition prioritaire ; toutes les fiches du pôle restent
>    `to-source` jusqu'à vérification sur texte. Note opérative : l'Akhḍarī couvre
>    les ʿibādāt ; pour les muʿāmalāt du label, le texte opératoire est Khalīl
>    (appui : la Risāla d'Ibn Abī Zayd).
>
> Le lot d'amorçage (fiches, prompts v2, amendements CLAUDE.md) a été produit le
> même jour — voir `UPDATES.md` du lot.

---

## 1. Principe et périmètre

L'ancrage éthique (§V.c) a posé que les actes contractuels et commerciaux du label se
règlent sur les principes ancrés. Le Fiqh est précisément **la science traditionnelle
qui norme les actes** — son introduction n'est donc pas une extension arbitraire mais
le **reflet nécessaire** du §V.c : là où le §V.c disait « examinable contre les
principes », le pôle Fiqh fournit le corpus normatif de cet examen, pour les activités
relevant de son cadre.

**Périmètre initial** (chapitre des *muʿāmalāt* — transactions) :

| Acte du label | Chapitre de fiqh applicable | Observation |
|---|---|---|
| Don des 300 vinyles aux dépositaires | *hiba* (don) | Convergence remarquable : la doctrine du don du label trouve dans le fiqh de la *hiba* son cadre normatif traditionnel — conditions de validité, révocabilité, intention |
| Vente directe (Bandcamp, boutique) | *bayʿ* (vente) | Licéité de l'objet, du prix, absence de *gharar* |
| Dépôt-vente disquaires | *wadīʿa* / mandat de vente | À qualifier précisément (dépôt vs commission) |
| Contrats de collaboration | *ijāra* / *juʿāla* | Rémunération des prestations |
| Registre de transmission (idée long terme) | à instruire | Le « bénéfice émergent jamais promis » devra aussi être examiné contre *riba* et *gharar* |
| Actifs de la structure | *zakāt* des biens de commerce | Pont existant en bibliothèque : Gilis, *Métaphysique de la Zakât* |

Ce tableau est un **amorçage** : chaque ligne appelle sa fiche sourcée (`to-source`
tant que non vérifiée sur texte malikite).

---

## 2. Fiches d'amorçage du pôle (lot Fiqh 2026-07-06)

- `doctrinal/traditions/madhhab-maliki.md` — école de préséance, fondements, chaîne textuelle
- `doctrinal/autorites/imam-malik.md` — éponyme, auteur du Muwaṭṭaʾ, rôle dans le dépôt
- `doctrinal/symboles/fiqh.md` — science des statuts, divisions (ʿibādāt / muʿāmalāt), rôle opératoire du pôle
- `doctrinal/sources/al-madrasah-al-hanbaliyyah.md` — ressource de recours ḥanbalite, cursus de fiqh

Toutes : `to-source` confirmés tant que les textes malikites de base ne sont pas en bibliothèque physique.

---

## 3. Double face du Gardien (Hermes 04 & 10)

### Agent 04 — Administration & Legal (v2, 2026-07-06)
- **Instruction du fiqh** : instruit les questions de droit traditionnel (quelle école, quelles sources, commentaires de position), output : ⚖️ candidate fiches (`to-source`, sources attribuées à leur école et texte)
- **Limites claires** : compile, ne décide jamais ; recours aux écoles documenté ; pas de talfīq
- **Interface avec 10** : remonte les fiches candidates et les cas de non-couverture

### Agent 10 — Protocol Guardian (v2, 2026-07-06)
- **Harmonisation** : relit les plans/contrats/textes du label à travers la double face (droit français + fiqh)
- **Trois signaux** : ✅ conforme à la position adoptée (source), ⚠️ non-conformité (détail + correction proposée), ❓ chapitre non encore instruit (demande recherche à 04)
- **Rapport du matin** : verdicts en attente (⚖️ et 🔍), tâches de l'artiste, signaux du Gardien, échéances, état des sas
- **Limites claires** : signalisation, jamais de décision religieuse ou légale ; escalade à l'artiste

### Harmonisation des tensions
La tension **Commerce (12) ↔ Gardien (10)** est structurelle et voulue. Pas de hiérarchie entre eux : chacun parle depuis sa source, l'artiste arbitre.

---

## 4. Pipeline d'étude ⚖️

Chaque question de fiqh instruite → une étude datée `doctrinal/etudes/YYYY-MM-DD_<question>.md` avec :
- Bloc normalisé **⚖️ Statut de Fiqh**
- Question en termes généraux (jamais cas concret)
- Positions sourcées (école, texte, auteur)
- Recours subsidiaires si besoin (documenté, pas de talfīq)
- Verdict : adopté par Sidy (taqlīd d'une position établie) | confirmé par autorité textuelle | renvoyé au savant
- Lien à sens unique vers le cas concret en `label/` (si applicable)

---

## 5. Acquisition prioritaire

Les **textes de base de l'école mālikite** ne sont pas en bibliothèque physique (recension 2026-06-28) :
- **Mukhtaṣar al-Akhḍarī** — niveau fondamental, ʿibādāt
- **Mukhtaṣar Khalīl** — niveau avancé, muʿāmalāt (texte opératoire du pôle)
- **al-Risāla** (Ibn Abī Zayd al-Qayrawānī) — appui classique

Acquisition = **condition de levée des marqueurs `to-source`** de l'ensemble du pôle.

---

## 6. Chronologie d'intégration

| Date | Action | Statut |
|---|---|---|
| 2026-07-06 | Fiches amorçage (4 fiches doctrinales) | Intégrées |
| 2026-07-06 | Prompts des agents 04 & 10 (v2) | Intégrées |
| 2026-07-06 | Amendements CLAUDE.md (§V.c.6, action EXAMEN DE FIQH, Rapport du matin) | Intégrées |
| 2026-07-06 | Proposition (présente fiche) | Archivée comme fiche de conception |
| À l'acquisition | Instruction des questions du label | En attente |
| À l'arbitrage Sidy | Verdicts (hiba, bayʿ, ijāra, etc.) | Ouvert |

---

## 7. Alertes récurrentes

- **to-source** : tous les faits du pôle demeurent marqués jusqu'à vérification sur texte malikite physique
- **Talfīq** : règle de préséance stricte — mālikite d'abord, recours documenté et justifié question par question, jamais mélange d'écoles au sein d'un acte
- **Escadale légale** : les questions juridiques (CNM, Sacem, droits) ne sont jamais tranchées sans professionnel qualifié ; le fiqh les complète, ne les remplace pas
- **Discernement / Verdicts** : la machine documente et propose ; l'artiste décide (Cmd 13)
