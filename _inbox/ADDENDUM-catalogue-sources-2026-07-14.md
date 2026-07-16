# Addendum — Catalogue bibliothèque physique + upgrade sources (2026-07-14)

## 1. Ajouts à `meta/bibliotheque-physique.md`

```
- René Guénon, *Symboles de la Science sacrée* (Gallimard, coll. Tradition/NRF) —
  contient notamment ch. XXIII « Les mystères de la lettre Nûn » et ch. XXXVI
  « Le symbolisme du Zodiaque chez les pythagoriciens » (table des matières
  vérifiée sur exemplaire physique de Sidy, 2026-07-14). Contient aussi ch. XXXV
  « Les Portes solsticiales », non encore exploité — candidat naturel pour tout
  approfondissement futur du dossier Gizeh/portes solsticiales.
- Bâl Gangâdhar Tilak, *Origine polaire de la tradition védique* (trad. Jean et
  Claire Remy, Arché, Milano, 1979 — titre original *The Arctic Home in the
  Vedas*). Ouvrage académique (philologie comparée, XIXe-XXe s.), à statut
  `academique` et non `traditionnel` : étude érudite sur l'hypothèse d'une origine
  arctique/polaire de la tradition védique, table des matières et index complets
  photographiés. Pertinence potentielle pour tout approfondissement futur du
  volet védique de [[doctrinal/discernement/2026-06-20_fajr-vajra-indra-vritra]]
  (mythe Indra/Vritra) — non exploité à ce stade, simple entrée au catalogue.
```

## 2. Upgrade de `doctrinal/sources/guenon-mysteres-lettre-nun.md`

Remplacer la mention de fiabilité :
```
Récupéré via clipping web (index-rene-guenon.org) déposé par Sidy — à considérer comme fiable
(index de référence de l'œuvre de Guénon), mais non vérifié sur exemplaire physique.
```
par :
```
Chapitre XXIII de l'exemplaire physique de Sidy (*Symboles de la Science sacrée*,
Gallimard, coll. Tradition) — présence confirmée par la table des matières
photographiée le 2026-07-14. Vérification physique complète (texte intégral) encore
à faire ; le clipping web (index-rene-guenon.org) reste la source du texte cité tant
que la page physique n'a pas été elle-même photographiée.
```

## 3. Upgrade de `doctrinal/sources/guenon-zodiaque-pythagoriciens.md`

Même traitement, remplacer :
```
Récupéré via clipping web (index-rene-guenon.org), non vérifié sur exemplaire physique.
```
par :
```
Chapitre XXXVI de l'exemplaire physique de Sidy (*Symboles de la Science sacrée*,
Gallimard, coll. Tradition) — présence confirmée par la table des matières
photographiée le 2026-07-14. Vérification physique complète (texte intégral) encore
à faire ; le clipping web (index-rene-guenon.org) reste la source du texte cité tant
que la page physique n'a pas été elle-même photographiée.
```

## 4. Fiche source à créer

`doctrinal/sources/tilak-origine-polaire-tradition-vedique.md` :
```yaml
---
title: "Origine polaire de la tradition védique — Bâl Gangâdhar Tilak"
type: source
status: academique
tradition_cadre: "hindouisme"
tags: [tilak, vedas, origine-polaire, philologie, academique]
created: 2026-07-14
updated: 2026-07-14
sources: []
sources_count: 0
cross_links: ["[[doctrinal/discernement/2026-06-20_fajr-vajra-indra-vritra]]"]
---
```
Corps : *The Arctic Home in the Vedas* (trad. franç. Jean et Claire Remy, Arché,
Milano, 1979). Treize chapitres, de la période glaciaire aux « références avestiques »
et à la « mythologie comparée » (ch. XII) — hypothèse d'une origine arctique de la
tradition védique fondée sur l'astronomie et la philologie comparée. Statut
`academique` : étude savante, non un texte traditionnel primaire — à ne pas confondre
avec une source doctrinale de rang égal aux textes akbariens ou guénoniens du dépôt.
Utile en filigrane pour tout futur travail sur le mythe Indra/Vritra
([[doctrinal/discernement/2026-06-20_fajr-vajra-indra-vritra]]), non exploité à ce
stade — simple entrée au catalogue, table des matières et index complets
photographiés par Sidy.

## 5. `doctrinal/annales.md` — entrée dédiée (append-only)

```markdown
## [2026-07-14] catalogue | Deux ouvrages physiques ajoutés + upgrade sourçage
- **Opération** : DISCIPLINE DES SOURCES — catalogue.
- **Créé** : [[doctrinal/sources/tilak-origine-polaire-tradition-vedique]].
- **Modifié** : [[doctrinal/sources/guenon-mysteres-lettre-nun]],
  [[doctrinal/sources/guenon-zodiaque-pythagoriciens]] — statut de fiabilité
  amélioré (présence confirmée sur exemplaire physique via table des matières ;
  texte intégral encore à vérifier page par page).
- **Point sensible** : aucun.
- **Note de méthode** : *Symboles de la Science sacrée* contient aussi le ch. XXXV
  « Les Portes solsticiales », non encore exploité — à consulter en priorité si le
  dossier Gizeh ou le motif des portes solsticiales est repris.
```
