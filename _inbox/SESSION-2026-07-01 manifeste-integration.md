# Manifeste de session — 2026-07-01 (Instrument, session A3)

> **Double usage.** (1) Pour **Claude Code** : la liste ordonnée et dédoublonnée
> de tout ce qui doit entrer au dépôt, avec la version finale de chaque fichier à
> écrasement clairement désignée. (2) Pour **Sidy** : le récapitulatif d'état pour
> mettre à jour les travaux dans une autre session.
>
> Ce document est **descriptif**, produit par claude.ai. Il ne remplace pas les
> `MASTER-UPDATES.md` de chaque lot : ceux-ci restent la consigne détaillée
> fiche par fiche. Ici, la vue d'ensemble et l'ordre.
>
> ⚠️ **Rappel de discipline** : aucun auto-accept ; le script `compare` reste le
> seul verdict mécanique ; toute écriture est vérifiée avant exécution ; les
> paraphrases et transcriptions restent distinctes des sources primaires.

---

## 1. Les six lots de la session (ordre d'intégration OBLIGATOIRE)

Certains fichiers sont produits en plusieurs versions successives : **l'ordre
ci-dessous doit être respecté**, la version la plus récente écrasant la
précédente. Chaque ZIP est dans `/mnt/user-data/outputs/`.

| # | Lot (ZIP) | Objet |
|---|---|---|
| 1 | `lot-generateur-manifeste-2026-07-01` | Phase 1 : spec + script + données v0.1 |
| 2 | `lot-arbitrages-v0_3-2026-07-01` | Architecture v0.3 (arbitrages §8) + données v0.2 |
| 3 | `lot-transcription-gloton-pp38-41-2026-07-01` | Addendum degrés 17-38 + modes 39-50 |
| 4 | `lot-angles-noms-divins-manazil-2026-07-01` | Addendum pp. 46-47 + angles + images |
| 5 | `lot-table-complete-28-noeuds-2026-07-01` | Addendum pp. 44-48 + script amendé + données v0.3 |
| 6 | `lot-relectures-discernement-prototype-2026-07-01` | Relectures + discernement + prototype |

---

## 2. Fichiers à écrasement — VERSION FINALE À DÉPOSER

Ces trois fichiers apparaissent dans plusieurs lots. **Ne déposer que la version
finale indiquée** (les versions antérieures sont listées seulement pour mémoire ;
si l'intégration se fait lot par lot dans l'ordre, l'écrasement est naturel).

| Fichier (chemin dépôt) | Versions traversées | ⭐ VERSION FINALE — source |
|---|---|---|
| `atelier/projets/generer-manifeste.py` | lot 1, lot 5 | **lot 5** (surcharge `id`/`label` vérifiée présente) |
| `atelier/projets/instrument-donnees.yaml` | lot 1 (v0.1), lot 2 (v0.2), lot 5 (v0.3) | **lot 5 — v0.3** (28 nœuds-degrés vérifiés) |
| `atelier/projets/angles-de-l-espace.md` | lot 4, lot 6 | **lot 6** (lectures tranchées vérifiées présentes) |

> Si Claude Code intègre les lots **dans l'ordre 1→6**, il lui suffit de laisser
> chaque version écraser la précédente au même chemin. S'il intègre en une passe,
> il **doit** prendre les trois fichiers ci-dessus depuis le lot indiqué.

---

## 3. Cartographie complète par emplacement de destination

### 3.1 `doctrinal/sources/ibn-arabi-de-la-mort-a-la-resurrection-gloton.md`
**Opération : APPEND** (trois addenda à la suite, dans l'ordre ; retirer le bloc
d'en-tête « Destination » de chaque addendum avant de l'appendre ;
`updated: 2026-07-01`) :
- lot 3 → `addendum-gloton-degres-17-38-modes-39-50.md` (degrés 17-38, modes 39-50)
- lot 4 → `addendum-gloton-pp46-47-noms-divins-manazil.md` (Noms Divins/Manāzil 18-31)
- lot 5 → `addendum-gloton-pp44-45-48-degres-11-17-32-38.md` (degrés 11-17, 32-38)

Correctifs de relecture à appliquer **dans ces addenda après append** (lot 6) :
- item 48 (modes du Souffle) : retirer « [?] » après **kanîyât** (confirmé Sidy).
- degré 29 : retirer « [?] » après **Samâwiyyaʾ** (confirmé Sidy).

### 3.2 `doctrinal/symboles/table-28-degres-nafas-rahman.md`
**Opération : ÉDITION** (compléter/sourcer les colonnes ; ne jamais inventer) :
- degrés 21-27 : Lettre/ciel/jour/prophète siégeant (lot 3, pp. 38-41) puis
  Nom Divin/Manzil (lot 4, pp. 46-47).
- degrés 11-17 et 32-38 : Nom Divin/Manzil/racines/portions (lot 5, pp. 44-45, 48).
- **Lever intégralement le `to-source`** du tableau synoptique (11-38).
- Ajouter la référence d'édition arabe (lot 5) : Futūḥāt, Dar al-Kotob al-Ilmiyah,
  Beyrouth, 1420/1999, t. 4, pp. 29-32.
- `updated: 2026-07-01`.

### 3.3 `doctrinal/discernement/`
**Opération : CRÉATION** (lot 6) :
- `2026-07-01_rafi-ad-darajat-fonction-traversante.md` — statut « en cours »,
  verdict réservé à Sidy.
- ⚠️ **Effet mécanique attendu** : au prochain run du générateur, `question_ouverte`
  se posera automatiquement sur `al-insan-al-kamil`, `table-28-degres-nafas-rahman`
  et `hadarat-khams` (cross_links de ce discernement). Comportement voulu.

### 3.4 `atelier/projets/`
**Opération : CRÉATION / ÉCRASEMENT** :
- `spec-generateur-manifeste.md` (lot 1 ; + note surcharge id/label du lot 5 au §4).
- `generer-manifeste.py` → **version lot 5** (`chmod +x` après dépôt).
- `instrument-donnees.yaml` → **version lot 5 (v0.3)**.
- `instrument-tradition-primordiale-architecture-v0_3.md` (lot 2 ; +
  micro-éditions des lots 4, 5, 6 — voir MASTER-UPDATES respectifs : filament
  validé §7, appariement angles acté §8, colonnes FAIT §8). Les v0.1 et v0.2
  restent au dépôt comme jalons, inchangées.
- `angles-de-l-espace.md` → **version lot 6**.
- `references-visuelles-astronomiques-phase-5.md` (lot 4).
- `instrument-prototype.html` (lot 6 — prototype v0.1, cadrage caméra corrigé).
- `assets-instrument/` (lot 4) : `img-0949-demeures-lunaires-zodiaque.gif`,
  `img-0950-angles-de-l-espace-schema.jpeg`,
  `img-0951-horizon-equateur-ecliptique.jpeg`,
  `img-0952-sphere-celeste-coordonnees.jpeg`.

### 3.5 `meta/projet-unifie/` (mises à jour amont — vigilance documentaire)
- `02-instrument-feuille-de-route.md` : Phase 0 close (Three.js/web/statique),
  Phase 1 livrée, §8.2 tranché, méthode continue actée (lots 2, 4).
- `04-sessions-par-fonction-et-backlogs.md` : clôtures multiples (lots 2→6) —
  voir §5 ci-dessous.

### 3.6 `annales.md`
**Opération : APPEND** — six entrées, une par lot (texte exact dans chaque
`MASTER-UPDATES.md`, section « Entrée pour annales.md »). Append-only,
préférence entrée unique par lot.

### 3.7 `doctrinal/index.md`
- Ajouter le discernement Rafîʿ ad-Darajât (🔍 en cours) — lot 6.
- (Aucune autre page doctrinale nouvelle ; les addenda enrichissent des fiches
  existantes.)

---

## 4. Vérifications mécaniques post-intégration (pour Claude Code)

À exécuter **après** dépôt, dans l'ordre, en rapportant les sorties à Sidy sans
corriger d'office (VIGILANCE) :

```bash
# 1. dépendance
apt install -y python3-yaml

# 2. rendre le script exécutable
chmod +x atelier/projets/generer-manifeste.py

# 3. générer le premier manifeste réel
python3 atelier/projets/generer-manifeste.py --repo /root/wiki
```

**Attendu** : `36 nœud(s), 2 ancrage(s), 0 erreur` (8 notionnels + 28 degrés).
Si des erreurs « fiche doctrinale introuvable » apparaissent, c'est un **écart de
slug** entre `instrument-donnees.yaml` et les fiches réelles du dépôt : corriger
les chemins dans le YAML (jamais les fiches), puis relancer. Ne PAS lever une
erreur en modifiant une fiche doctrinale.

Le script est **lecture seule** sur `doctrinal/` ; il n'écrit que
`atelier/projets/wiki-manifest.json`.

---

## 5. État des travaux (pour la session de mise à jour de Sidy)

### Acquis de la session
- **Phase 0 close** : Three.js/WebGL, web mobile d'abord, hébergement statique.
- **Phase 1 livrée** : générateur de manifeste déterministe (spec + script testé,
  garde-fous vérifiés en refus) + déclaration applicative.
- **Architecture v0.3** : cinq arbitrages du §8 consignés (lentille barzakh,
  quatre angles AS/DS/MC/FC à qualités élémentaires, Phase 0, vigilance continue) ;
  convention `degre_vertical` (échelle des 38 degrés).
- **Table des 28 degrés intégralement sourcée** (Gloton pp. 38-48) : Lettre, Nom
  Divin, réalité, Manzil, racine, portion zodiacale, prophète siégeant — pour les
  degrés 11-38. `to-source` du tableau synoptique entièrement levé.
- **28 nœuds-degrés générés** dans `instrument-donnees.yaml` v0.3 → axe complet en
  donnée. Filament al-Insān al-Kāmil validé.
- **Prototype v0.1** de l'axe (Three.js) : premier rendu visible du mandala.
- **Discernement ouvert** : Rafîʿ ad-Darajât ↔ fonction traversante (verdict réservé).
- Quatre relectures [?] tranchées par Sidy (kanîyât ; humide رطبات/رطنات ;
  mentions rouges = noms d'angles en sens horaire ; Samâwiyyaʾ).

### Reste ouvert (aucun bloquant pour l'intégration)
- **Test du prototype sur iPad** (via Safari, pas l'Aperçu rapide) → retours pour
  l'itération suivante.
- **Itérations prototype** : charger `wiki-manifest.json` réel (fetch) au lieu des
  données embarquées ; bascule de tradition ; rendu optique de la lentille barzakh.
- **Calcul astrologique multi-méthodes** (Phase 5) et **échéancier** : à spécifier.
- **Verdict** du discernement Rafîʿ ad-Darajât (Sidy, éventuellement après Gem).
- **Vérification `to-source` résiduelle** : citation Qurʾân 40-15 dans la fiche de
  discernement (marquée ⚠ à vérifier, ne pas citer de mémoire).

### Hors session Instrument (rappels de backlog inchangés)
- Transition Qwen (actions A→H) côté infrastructure.
- Verdict à consigner dans `tension-hadarat-burckhardt-jurjani`.
- Ingest du récit eschatologique discursif du ch. 198 (matière repérée pp. 39, 49).
- Développement du stub `nafas-rahmani` (matière : modes 39-50, addendum lot 3).

---

## 6. Index des `MASTER-UPDATES.md` (consigne détaillée par lot)

Chaque ZIP contient son `MASTER-UPDATES.md` avec le détail fiche par fiche, les
points sensibles et l'entrée d'annales. En cas de doute sur une opération précise,
**le MASTER-UPDATES du lot concerné fait foi** sur ce présent manifeste (qui n'en
est que la synthèse ordonnée).

*Fin du manifeste de session 2026-07-01.*
