# UPDATES — Lot « Formalisation Sashimono » (2026-07-07, rév. lexique + patch)

Produit côté PRODUCTION (session claude.ai, moteur Fable 5). Trois pièces + le présent
manifeste. Intégration fiche par fiche, dans l'ordre ci-dessous.

**Révision du lot** : la directive intègre désormais le §6 « Lexique conventionnel »
(kigumi, hozo, kumiko, kari-kumi, sumi-tsuke, ki-dori) validé par l'utilisateur, et
le lot inclut le patch CLAUDE.md — l'édition de CLAUDE.md a reçu l'**ordre humain
explicite** en session du 2026-07-07.

## 1. `philosophie-sashimono.md`

- **Destination** : `meta/philosophie-sashimono.md`
- **Nature** : directive opératoire transversale (interface conceptuelle de la
  démarche — quatre circuits). Type `meta`, hors Sceau Recteur doctrinal.
- **Action index** : aucune entrée dans `doctrinal/index.md` (document meta).
- **Note** : l'édition de CLAUDE.md liée à cette directive est désormais validée —
  voir pièce 3 ci-dessous.

## 2. `2026-07-07_sashimono-metier-traditionnel.md`

- **Destination** : `doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md`
- **Nature** : fiche discernement candidate, `status: speculatif`, verdict réservé.
  Marqueurs `to-source` présents (Guénon *Aperçus sur l'Initiation*, Coomaraswamy
  *Principes et méthodes de l'art sacré*, contexte traditionnel du sashimono) — ne
  pas lever sans vérification primaire humaine.
- **Action index** : ajouter le lien dans la section discernement de
  `doctrinal/index.md`.
- **Attention** : les slugs de sources `[[apercus-sur-l-initiation]]` et
  `[[principes-et-methodes-de-l-art-sacre]]` supposent des fiches `sources/` qui
  n'existent peut-être pas encore — si absentes, laisser les liens en rouge
  (création de fiches source = travail futur côté PRODUCTION, bibliothèque physique
  d'abord), ne rien créer d'office.

## 3. `claude-md-patch-sashimono.md`

- **Destination** : ne s'intègre pas comme fiche — c'est une **consigne d'édition
  ciblée de CLAUDE.md** (deux insertions : note de révision d'en-tête + sous-section
  « Convention Sashimono » en fin de §VII). Ordre humain consigné dans le patch.
- **Exécution** : str_replace/édition ciblée uniquement, jamais de réécriture
  globale ; diff relu intégralement ; commit dédié (message indiqué dans le patch).
- Après application, le fichier patch peut être archivé dans `meta/projet-unifie/`
  ou supprimé du sas (au choix de l'utilisateur).

## 4. Annales

Une seule entrée groupée dans `doctrinal/annales.md` (append-only, Cmd 9) :

`## [2026-07-07] archivage | Formalisation Sashimono — directive meta, lexique, discernement candidat, révision CLAUDE.md`

Contenu : adoption du sashimono comme philosophie d'assemblage opératoire
(`meta/philosophie-sashimono.md`, 6 articles normatifs + lexique conventionnel) ;
révision de CLAUDE.md sur ordre humain (convention Sashimono, §VII) ; ouverture de
la fiche discernement sur le fondement doctrinal (verdict réservé, to-source actifs).

## 5. Rappels d'intégration

- Jamais d'auto-accept ; relire chaque écriture ; `git diff --stat` avant commit.
- Commit : `ARCHIVAGE: formalisation sashimono (directive meta + discernement)`.
- Vider `_inbox/` après intégration validée.
# UPDATES — Lot « Framework études de cas » (2026-07-06)

## Fichiers du lot

| Fichier | Destination | Langue | Statut |
|---|---|---|---|
| `framework-etude-de-cas.md` | `meta/projet-unifie/` | FR | nouveau |
| `stones-throw.md` | `atelier/etudes-de-cas/` | EN (sujet international) | nouveau |

## Opérations demandées

1. **Créer le sous-dossier** `atelier/etudes-de-cas/` (nouveau).
2. Déplacer `framework-etude-de-cas.md` vers `meta/projet-unifie/`.
3. Déplacer `stones-throw.md` vers `atelier/etudes-de-cas/`.
4. Répercuter dans les index concernés ; consigner dans les annales :
   `## [2026-07-06] archivage | Framework études de cas + étude Stones Throw`.

## ⚠️ Point requérant validation humaine (Cmd 13)

- **Extension du Sceau atelier** : ajout du type `etude-de-cas` à la liste
  `type: materiel | manuel | entretien | projet` du §V.a de CLAUDE.md.
  Sans validation, alternative de repli : `type: entretien` avec tag
  `etude-de-cas` (non recommandé — sémantique faussée).
- Si l'extension est validée, amender CLAUDE.md §V.a en conséquence
  (vigilance documentaire, §VII).

## Règles de liens

- `atelier/etudes-de-cas/` : circuit atelier standard — jamais de lien vers
  `doctrinal/` ni depuis `label/` → sens unique `label/ → atelier/` autorisé
  via `liens_atelier` quand une fiche label s'inspirera d'une étude.
- Le bloc Transposition 🔍 de chaque étude reste suggéré tant que non tranché.

## Flags de données (étude Stones Throw)

- Revenu annuel ~$7,2M : estimation RocketReach, **crédibilité D**, non
  recoupée — conserver le flag.
- Structure capitalistique (indépendance formelle) : `to-source`.
- Contrats de distribution actuels : `to-source`.

## Prochaines études candidates (backlog, ordre à trancher par Sidy)

Lemaire (FR → étude en français) · Fever-Tree · Kojima Productions ·
Brownswood/Gilles Peterson · NTS Radio.
