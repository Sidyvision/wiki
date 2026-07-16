# MASTER-UPDATES — Lot « Relectures tranchées + discernement + prototype » (2026-07-01)

> Lot produit par Claude.ai. Trois objets : (1) consignation des quatre lectures
> [?] tranchées par Sidy sur pièces ; (2) la fiche de discernement commandée par
> Sidy (Rafîʿ ad-Darajât ↔ fonction traversante) ; (3) le **premier prototype
> Three.js de l'axe** (syntaxe JS vérifiée mécaniquement avant livraison).

## 1. Fichiers du lot, par dossier

### doctrinal/discernement/
- `2026-07-01_rafi-ad-darajat-fonction-traversante.md` — **nouvelle fiche**,
  statut « en cours », verdict réservé à Sidy. Formulée en termes purement
  doctrinaux (aucune mention de l'app : étanchéité).

### atelier/projets/
- `angles-de-l-espace.md` — **remplace** la version du lot 4 : lectures tranchées
  (« humide » : graphie رطبات ou رطنات, sans point diacritique sur le manuscrit,
  sens confirmé ; mentions rouges = les quatre noms d'angles lus dans le sens
  horaire : Descendant, Fond du Ciel, Ascendant, Milieu du Ciel — la lecture
  « Devenant » était fautive).
- `instrument-prototype.html` — **nouveau** : prototype v0 de l'axe (fichier
  unique, Three.js r128, données du manifeste embarquées, hors ligne).

## 2. Éditions ciblées à appliquer

### 2a. Addendum pp. 38-41 (dans la fiche source Gloton)
- Item 48 : retirer le « [?] » après **kanîyât** — lecture confirmée par Sidy
  sur pièce (l'hypothèse *kawnîyât* émise en session était fausse). Retirer
  aussi la mention correspondante de la note de fin d'addendum si présente.

### 2b. Addendum pp. 46-47 (dans la fiche source Gloton)
- Degré 29 : retirer le « [?] » après **Samâwiyyaʾ** — lecture confirmée.

### 2c. `doctrinal/index.md`
- Section des discernements : ajouter
  `[[doctrinal/discernement/2026-07-01_rafi-ad-darajat-fonction-traversante|Rafîʿ ad-Darajât et la fonction traversante d'al-Insān al-Kāmil]] — 🔍 en cours`.

### 2d. `meta/projet-unifie/04-sessions-par-fonction-et-backlogs.md`
- §B : « relectures [?] » → **FAIT (2026-07-01, tranchées par Sidy)**.
- §D (discernements en cours) : ajouter la fiche Rafîʿ ad-Darajât.
- §B : ajouter « **[App]** Prototype v0 livré ; à tester sur iPad ; prochaines
  itérations : chargement du wiki-manifest.json réel (fetch) au lieu des données
  embarquées, bascule de tradition, lentille barzakh (rendu optique). »

## 3. Entrée pour `annales.md` (une seule)

```
## [2026-07-01] creation | Discernement Rafîʿ ad-Darajât ouvert — relectures tranchées — prototype v0 de l'axe
Les quatre lectures [?] du jour tranchées par Sidy sur pièces (kanîyât confirmé ;
humide رطبات/رطنات sans point diacritique ; mentions rouges = noms des quatre
angles en sens horaire ; Samâwiyyaʾ confirmé) et consignées. Fiche de discernement
2026-07-01_rafi-ad-darajat-fonction-traversante ouverte à la demande de Sidy
(statut en cours, verdict réservé). Premier prototype Three.js de l'axe livré
(atelier/projets/instrument-prototype.html) : 38 degrés avec Hāhūt non manifesté
et espacement exponentiel du Nāsūt, disques en rotation du Barzakh supérieur,
filament al-Insān al-Kāmil, boucle 38→11, anneau des nœuds notionnels,
convergence des 28 en trait plein, quatre Angles de l'Espace au sol.
```

## 4. Points sensibles

- **Effet automatique à connaître** : la nouvelle fiche de discernement étant
  « en cours » avec des cross_links vers al-insan-al-kamil, table-28-degres et
  hadarat-khams, le générateur de manifeste posera automatiquement
  `question_ouverte` sur ces trois nœuds au prochain run — c'est le comportement
  voulu (l'onglet apophatique en donnée).
- **Étanchéité inversée** : aucune page orthodoxe ne pointe vers le discernement
  tant qu'il est en cours (rappelé dans la fiche elle-même).
- Le prototype embarque les données ; il ne lit PAS wiki-manifest.json (choix
  volontaire pour tourner en local sur iPad sans serveur). L'itération suivante
  branchera le fetch quand l'app sera servie en statique.
- Ordre d'intégration : après tous les lots précédents du jour (celui-ci
  remplace `angles-de-l-espace.md` du lot 4).
