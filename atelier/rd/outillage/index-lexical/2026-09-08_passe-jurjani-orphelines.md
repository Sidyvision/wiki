---
title: "Passe Jurjānī sur les clés orphelines de l'index lexical — relevé mécanique"
type: artefact-derive
tags: [index-lexical, langues-originales, jurjani, appariement, releve]
created: 2026-09-08
updated: 2026-09-08
sources: ["[[doctrinal/sources/kitab-tarifat-corps-transcription]]", "[[doctrinal/sources/kitab-tarifat-index-transcription]]"]
links: []
original: []
---

# Passe Jurjānī sur les clés orphelines de l'index lexical

> ⚙️ **Relevé mécanique.** Ce document est produit par croisement déterministe entre
> `index-lexical.json` et les deux transcriptions du *Kitāb al-Taʿrīfāt* versées au
> dépôt. Il porte `type: artefact-derive` : l'index ne s'indexe pas lui-même.
>
> **Verdict rendu par Sidy le 2026-09-08** : « donne un champ propre à Jurjani et
> intègre les 132 à l'index ». Les appariements du §4 sont désormais **posés**, dans
> un champ `jurjani` **distinct de `apparie`** — le rang 2 ne se fond jamais dans le
> rang 1. Ce document reste le relevé de la passe et la trace de sa mesure.

## 1. Objet

CLAUDE.md §VII, discipline des langues originales, **point 6** : l'index doit atteindre
le terme *dans les deux sens*. Le champ `apparie` du générateur ne se renseigne que sur
une paire que **la fiche elle-même énonce** — `Tomoe (巴)`. Restaient donc des clés en
écriture originale sans forme latinisée attachée : les **orphelines**. Sidy, en session :
« il suffira de se reporter à Jurjani et voir si l'on trouve le terme ou sinon tu feras
la traduction par tes propres moyens et on sourcera plus tard ».

## 2. Les trois rangs, jamais fondus

Le relevé distingue trois rangs de crédibilité, et ce document n'en verse aucun dans le
champ `apparie`, qui reste réservé au premier (§VII, manifestes, règle 3 — établi vs
suggéré) :

| Rang | Ce qui l'établit | Compte |
|---|---|---|
| **1 — attesté par la fiche** | la fiche énonce la paire dans son `title:`/H1 ou en tête de définition | **59 paires** (déjà dans `apparie`) |
| **2 — attesté par Jurjānī** | correspondance exacte avec une définition transcrite du *Kitāb al-Taʿrīfāt*, numéro de définition cité | **132 clés** (§4) |
| **3 — de mon fait, non sourcé** | translittération produite par la machine, `to-source` obligatoire | **voir §5 — le rang est VIDE** |

Les rangs 1 et 2 vivent désormais tous deux à l'index, **dans deux champs séparés** :
`apparie` (rang 1) et `jurjani` (rang 2, portant le numéro de définition). Le condensé
`index-lexical.md` les distingue à l'œil dans sa colonne *appariement* — un renvoi nu
pour le rang 1, `— Jurjānī déf. NNNN` pour le rang 2. Un lecteur n'a jamais à deviner
d'où vient une paire.

## 3. Mesure

- Clés en écriture originale à l'index : **1200**
- Dont appariées par la fiche (rang 1) : **59** clés en écriture originale (soit 118
  clés au total, les deux côtés de chaque paire)
- **Orphelines : 1141**
- Couvertes par Jurjānī (rang 2) : **132**
- Résidu : **1009** — réparti : arabic 393, cjk 363, hebrew 218, greek 21, autre 9, hiragana 4, devanagari 1

**Le résidu n'est pas un gisement de termes.** Après retrait des lettres isolées (les
clés `ف`, `ا`, `ر`… sont les lettres de l'alphabet, relevées des tableaux de
translittération) et des tokens ne portant aucun rôle de terme, il ne reste que
**6 clés** sur 1009. C'est le fait principal de cette passe : la question
« que faire des mille orphelines » n'avait pas lieu d'être — mille d'entre elles ne sont
pas des termes.

## 4. Rang 2 — les 132 clés couvertes par Jurjānī

Chaque ligne porte son numéro de définition : c'est la source, vérifiable au texte
transcrit. **Le marqueur `to-source` reste dû** tant que Sidy n'a pas contrôlé la
correspondance au texte primaire (§VII, discipline des sources, point 2 — la levée
n'appartient pas à la machine).

| forme originale | translittération (Jurjānī) | déf. | occ. |
|---|---|---|---|
| الإباحة | *al-ibâḥa* | 0012 | 1 |
| الإباضيّة | *al-ibâḍiyya* | 0011 | 1 |
| الإتّحاد | *al-ittiḥâd* | 0013 | 1 |
| الإتفاقية | *al-ittifâqiyya* | 0015 | 1 |
| الإتّقان | *al-ittiqân* | 0014 | 1 |
| الإحسان | *al-iḥsân* | 0046 | 1 |
| الإحصار | *al-iḥṣâr* | 0044 | 1 |
| الإحصان | *al-iḥṣân* | 0045 | 1 |
| الاسراف | *al-isrâf* | 0120 | 1 |
| الاسلام | *al-islâm* | 0119 | 1 |
| الاهاب | *al-ihâb* | 0263 | 1 |
| الايمان | *al-îmân* | 0264 | 1 |
| البرزخ | *al-barzaḫ* | 0295 | 4 |
| البرغوثية | *al-burġûṯiyya* | 0298 | 1 |
| البرودة | *al-burûda* | 0294 | 1 |
| البستان | *al-bustân* | 0299 | 1 |
| البسيط | *al-basîṭ* | 0300 | 1 |
| البنانية | *al-banâniyya* | 0312 | 1 |
| البيان | *al-bayân* | 0313 | 1 |
| الجدال | *al-jaddâl* | 0519 | 1 |
| الجدل | *al-jadal* | 0518 | 1 |
| الجرس | *al-jaras* | 0520 | 1 |
| الحادث | *al-ḥâdiṯ* | 0562 | 2 |
| الحارثيّة | *al-ḥâriṯiyya* | 0567 | 2 |
| الحافظة | *al-ḥâfiẓa* | 0561 | 2 |
| الحال | *al-ḥâl* | 0563 | 6 |
| الحائطية | *al-ḥâʾiṭiyya* | 0566 | 2 |
| الحدود | *al-ḥudûd* | 0584 | 1 |
| الحمزية | *al-ḥamziyya* | 0667 | 1 |
| الحملة | *al-ḥumla* | 0665 | 1 |
| الحميّة | *al-ḥamiyya* | 0666 | 1 |
| الحوالة | *al-ḥawâla* | 0668 | 1 |
| الحَيِّز | *al-ḥayyiz* | 0669 | 2 |
| الدهر | *al-dahr* | 0745 | 1 |
| الدوْر | *al-dawr* | 0744 | 1 |
| الديّة | *al-diya* | 0749 | 1 |
| الدين | *al-dîn* | 0746 | 4 |
| الرآن | *al-rân* | 0761 | 1 |
| الراهب | *al-râhib* | 0760 | 1 |
| الرباعيّ | *al-rubâʿî* | 0763 | 1 |
| الربوا | *al-ribâ* | 0764 | 1 |
| الرؤية | *al-ruʾya* | 0762 | 1 |
| الشرع | *al-šarʿ* | 0886 | 1 |
| الشهامة | *al-šahâma* | 0914 | 1 |
| الشهوة | *al-šahwa* | 0913 | 1 |
| الشهود | *al-šuhûd* | 0912 | 1 |
| الشيبانية | *al-šaybâniyya* | 0917 | 1 |
| الشيطنة | *al-šayṭana* | 0915 | 1 |
| الشيعة | *al-šîʿa* | 0916 | 1 |
| الصفوة | *al-ṣafwa* | 0944 | 1 |
| الصَفَى | *al-ṣafî* | 0945 | 1 |
| الصُلح | *al-ṣulḥ* | 0946 | 1 |
| الصَلْم | *al-ṣalm* | 0948 | 1 |
| الصلوة | *al-ṣalâ* | 0947 | 1 |
| الضمار | *al-ḍimâr* | 0973 | 1 |
| الضنآئن | *al-ḍanâʾin* | 0978 | 1 |
| العَزل | *al-ʿazl* | 1065 | 1 |
| العُزْلَة | *al-ʿuzla* | 1066 | 1 |
| العَزيمة | *al-ʿazîma* | 1064 | 1 |
| الفِراش | *al-firâš* | 1195 | 1 |
| الفَرْد | *al-fard* | 1196 | 1 |
| الفَرْع | *al-farʿ* | 1197 | 1 |
| الفقر | *al-faqr* | 1217 | 2 |
| الفقه | *al-fiqh* | 1216 | 7 |
| الفَهْم | *al-fahm* | 1225 | 1 |
| الفَهْوانيّة | *al-fahwâniyya* | 1226 | 1 |
| الفَوْر | *al-fawr* | 1224 | 1 |
| القانت | *al-qânit* | 1235 | 2 |
| القبيح | *al-qabîḥ* | 1239 | 2 |
| القَتّات | *al-qattât* | 1240 | 2 |
| القَتْل | *al-qatl* | 1241 | 4 |
| الكَلِمَة | *al-kalima* | 1331 | 2 |
| المُتَعَدّى | *al-mutaʿaddî* | 1437 | 1 |
| المِثَال | *al-miṯâl* | 1438 | 1 |
| المُثَنّى | *al-muṯannâ* | 1439 | 1 |
| المَجاز | *al-majâz* | 1448 | 4 |
| المَجَلّة | *al-majalla* | 1453 | 1 |
| المُجْمَل | *al-mujmal* | 1452 | 1 |
| المَجْمُوع | *al-majmûʿ* | 1447 | 1 |
| المُذَكَّر | *al-muḏakkar* | 1491 | 1 |
| المِرآء | *al-mirâʾ* | 1501 | 1 |
| المُرابَحَة | *al-murâbaḥa* | 1507 | 1 |
| المُراد | *al-murâd* | 1496 | 1 |
| المُرادِف | *al-murâdif* | 1499 | 1 |
| المُراقَبَة | *al-murâqaba* | 1505 | 1 |
| المُراهِق | *al-murâhiq* | 1497 | 1 |
| المُرْتَجَل | *al-murtajal* | 1508 | 1 |
| المُرْجِئة | *al-murjiʾa* | 1498 | 1 |
| المُرشد | *al-muršid* | 1495 | 1 |
| المُرَكَّب | *al-murakkab* | 1509 | 3 |
| المُرُوَءَة | *al-murûʾa* | 1506 | 1 |
| المُريد | *al-murîd* | 1494 | 1 |
| المُسَلَّمات | *al-musallamât* | 1540 | 1 |
| المُشاهَدَة | *al-mušâhada* | 1545 | 1 |
| المَشْروع | *al-mašrûʿ* | 1543 | 1 |
| المُضارَبَة | *al-muḍâraba* | 1570 | 1 |
| المُطابَقَة | *al-muṭâbaqa* | 1574 | 1 |
| المُطالَعَة | *al-muṭâlaʿa* | 1576 | 1 |
| المُطاوَعَة | *al-muṭâwaʿa* | 1575 | 1 |
| المُطَرَّف | *al-muṭarraf* | 1577 | 1 |
| المُطلَق | *al-muṭlaq* | 1571 | 1 |
| المُعَانَدة | *al-muʿânada* | 1590 | 1 |
| المَعْدولَة | *al-maʿdûla* | 1589 | 1 |
| المُعْرَب | *al-muʿrab* | 1592 | 1 |
| المَعْرِفة | *al-maʿrifa* | 1591 | 1 |
| المَعْروف | *al-maʿrûf* | 1593 | 1 |
| المُعَلِّل | *al-muʿallil* | 1586 | 1 |
| المَعْنَوي | *al-maʿnawî* | 1588 | 1 |
| المَعْنى | *al-maʿnâ* | 1587 | 1 |
| المُناقَضَة | *al-munâqaḍa* | 1681 | 1 |
| المُنْتَشِرة | *al-muntašira* | 1684 | 1 |
| المَنْطِق | *al-manṭiq* | 1682 | 1 |
| المُنْفَصِلَة | *al-munfaṣila* | 1683 | 1 |
| المَنْقول | *al-manqûl* | 1685 | 1 |
| المَوات | *al-mawât* | 1704 | 1 |
| المَوْت | *al-mawt* | 1699 | 6 |
| النادر | *al-nâdir* | 1725 | 1 |
| النار | *al-nâr* | 1724 | 1 |
| الناقِص | *al-nâqiṣ* | 1726 | 1 |
| الناموس | *al-nâmûs* | 1723 | 1 |
| النَبات | *al-nabât* | 1728 | 1 |
| النَبَهْرَجَة | *al-nabahraja* | 1729 | 1 |
| النَبيّ | *al-nabî* | 1727 | 1 |
| النَجاريّة | *al-najjâriyya* | 1732 | 1 |
| النُجَبَآء | *al-nujabâʾ* | 1730 | 1 |
| النَجْش | *al-najš* | 1731 | 1 |
| اليَزيديّة | *al-yazîdiyya* | 1859 | 1 |
| اليَقْظَة | *al-yaqẓa* | 1860 | 1 |
| اليَقين | *al-yaqîn* | 1861 | 1 |
| اليَمين | *al-yamîn* | 1862 | 4 |
| بلى | *balâ* | 0311 | 1 |
| ضيآء | *al-ḍiyâʾ* | 0979 | 1 |

## 5. Rang 3 — ce qui aurait demandé une translittération de mon fait

**6 clés**, et aucune n'a exigé que j'invente quoi que ce soit — chacune est
résolue par une source déjà présente au dépôt :

- `باب` — occ. 32, rôles titre, translit
- `النون` — occ. 4, rôles titre, translit
- `الراء` — occ. 3, rôles titre, translit
- `誓約と制約` — occ. 3, rôles titre, translit
- `ЭКСМО` — occ. 1, rôles table, translit
- `Règle de conversion (δ) → (γ), vérifiée terme à terme` — occ. 0, rôles definition

Résolution de chacune, par la source :

- **باب** — *bâb* (chapitre, porte). Attesté au dépôt :
  `doctrinal/sources/kitab-tarifat-index-transcription.md:54`, règles de transcription
  (« ex. *bâb, kabîr, nûr* »).
- **الراء** — *al-Râʾ*, nom de la lettre. Attesté :
  `kitab-tarifat-index-transcription.md:6794` (« Lettre Râʾ / باب الراء »).
- **النون** — *al-Nûn*, nom de la lettre. Attesté : même fiche, ligne 6812.
- **誓約と制約** — *chikai to seiyaku*. Attesté par la fiche qui l'emploie :
  `hermeneutique/hunter-x-hunter/nen-systeme.md:98`. **L'index ne peut pas porter cette
  paire** : c'est un appariement de *syntagmes*, et les clés de cet index sont des
  tokens. Limitation structurelle rapportée, non contournée.
- **ЭКСМО** — *Eksmo*, maison d'édition russe. Attesté par le contexte de la fiche :
  `hermeneutique/sources/art-of-death-stranding.md:39`. Nom propre commercial, aucune
  portée doctrinale.
- **« Règle de conversion (δ) → (γ), vérifiée terme à terme »** — ce n'est pas un terme
  mais une **clé parasite** : une phrase entière captée par l'amorce `**X** :` de la
  récolte des définitions (`doctrinal/symboles/table-28-degres-nafas-rahman.md`).
  Signalée pour ce qu'elle est ; sa correction relève du filtre des définitions, non de
  cette passe.

**Rang 3 réel : zéro.** Aucune translittération de mon fait n'a été nécessaire, donc
aucun `to-source` de ce chef n'est à poser.

## 6. Ce qui n'a pas été fait, et pourquoi

- **Le rang 2 n'entre pas dans `apparie`** — verdict Sidy : il a reçu **son propre
  champ**, `jurjani`, portant le numéro de définition. Les fusionner aurait mêlé deux
  rangs de crédibilité dans un même champ sans moyen de les distinguer, ce que la règle
  « établi vs suggéré » interdit. **Le rang 1 prime** : une clé que la fiche apparie
  elle-même ne reçoit aucun renvoi Jurjānī.
- **Réciprocité partielle, et dite comme telle** (§VII, point 6) : sur les 132, **84**
  portent le renvoi dans les deux sens — la forme latine de Jurjānī y était déjà une clé
  de l'index. Les **48** autres ne l'ont que dans un sens : leur translittération
  n'apparaît nulle part dans le dépôt. On n'injecte pas le vocabulaire du dictionnaire
  dans un index qui est celui du **wiki** — ce serait indexer Jurjānī, non le dépôt.
- **Aucun `to-source` n'est levé.** Les 132 correspondances du §4 sont exactes au
  caractère près après normalisation, mais la levée du marqueur demande la vérification
  du texte primaire par Sidy lui-même (§VII, point 2).
- **Aucune fiche n'est modifiée.** Le champ `original:` (§IV) n'est posé sur aucune
  fiche : le point 5 interdit la passe de masse.

## 7. Deux défauts trouvés en construisant cette passe, corrigés

- **`systeme` ↔ `α`** — l'appariement lisait aussi les **H2**, et
  `doctrinal/symboles/table-28-degres-nafas-rahman.md:112` porte « ... — système (α) ».
  Les H2 sont retirés des sources d'appariement : seuls le `title:` et le H1 y entrent,
  le site que le point 3 déclare canonique.
- **`conversion` ↔ `δ`** — même famille, venue d'une tête de définition. Une lettre
  grecque isolée est un **label** dans ce dépôt (α, δ, γ, π, φ, tous employés comme
  variables), jamais un terme ; un caractère han isolé, lui, est un terme plein (巴).
  D'où une exclusion **par écriture**, non par longueur.

## 8. Reproduction

Ce relevé est régénérable. `index-lexical.json` est produit par
`generer-index-lexical.py` ; le croisement lit les deux transcriptions du *Kitāb
al-Taʿrīfāt* par le motif `### NNNN — *translittération* — forme arabe`, seule forme que
ces fiches emploient. Aucun modèle n'intervient dans la chaîne.
