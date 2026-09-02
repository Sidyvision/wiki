---
title: "INS-15 — situation polaire, mode cosmologique de l'Instrument : plan"
type: projet
chantier: INS-15
tags: [atelier, rd, instrument, chantier, plan, polaire]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/instrument/ins-15-situation-polaire/spec]]"
  - "[[atelier/rd/instrument/ins-15-situation-polaire/intent]]"
---

# INS-15 — plan

> **Statut : `brouillon`.** Aucun code n'est écrit au dépôt ni au dépôt frère tant
> que Sidy n'a pas visé ce plan (Cmd 6 — pour un chantier `rd/`, ce fichier *est* le
> plan du Cmd 6).
>
> **Ce qui est déjà fait, et pourquoi c'est licite** : la Phase 0 (prototype et
> contrôles numériques) a été exécutée **hors dépôt**, dans
> `/root/sandbox-rd/ins-15-polaire/`, sur verdict explicite de Sidy du 2026-09-02
> (« éprouver la géométrie en bac à sable »). La charte du pôle range la sandbox
> « **hors dépôt** » — la règle du Cmd 6 porte sur le code du chantier, non sur
> l'épreuve préalable. Rien de ce bac à sable n'entre au dépôt : il est jetable, et
> ses valeurs sont écrites en dur, ce que le rendu s'interdit.

## Étapes

### Phase 0 — épreuve de la géométrie (FAITE le 2026-09-02, hors dépôt)

1. ✅ `proto-geometrie.html` — scène Three.js r128 autonome : horizon, sphère
   céleste, axe du monde, soleil, cercle du jour, trace de l'année, astres en
   révolution, aurore tournante, roue du Manvantara, esquisse de la bascule.
2. ✅ `verifier-geometrie.py` — **8 contrôles**, chacun rejoué sous biais.
   Résultat : 8 passent sur la géométrie réelle, **les 8 tombent** quand on la
   fausse. L'épreuve des contrôles est faite (§VII, motif PRO-01).
3. ✅ `comparer-js-python.js` + `comparer.py` — les fonctions de géométrie sont
   **extraites du HTML lui-même** (non recopiées : un contrôle qui recopie
   s'observe lui-même, c'est le motif PRO-01) et confrontées à la référence
   Python sur 560 cas. Écart maximal **3,7 × 10⁻¹⁴°** ; l'option `--fausser`
   détecte bien un écart injecté d'1°.
4. ✅ Deux erreurs commises et conservées, plutôt qu'effacées :
   — le contrôle « le soleil ne passe jamais au nord » tombait à 90° et **avait
   tort** (au pôle exact, le repère d'azimut est dégénéré) ;
   — l'aurore polaire avait d'abord été présentée comme **confirmant** le chiffre
   de Tilak, alors qu'elle **en montre l'origine** : sa fourchette 45-60 j est
   l'image de sa propre fourchette de seuils 16°-20°. Contrôle 7 ajouté pour
   l'établir, et `spec.md` §2.2 porte la rectification.
5. ✅ Prototype envoyé à Sidy.

### Phase 1 — le triptyque (FAITE, c'est le présent dossier)

6. ✅ `intent.md`, `spec.md`, `plan.md`. Ligne INS-15 au registre, annales.

### ⛔ VISA DE SIDY — rien au-delà de cette ligne sans lui

### Phase 2 — la donnée et le producteur

6 bis. **Verser les contrôles au dépôt — première étape de la phase, avant toute
    autre.** Défaut relevé à la relecture du présent plan : les critères 1 et 2 du
    `spec.md` désignent `verifier-geometrie.py` et `comparer.py`, qui vivent dans un
    bac à sable **déclaré jetable et non versionné en trois endroits**. Une phase 2
    conduite par une autre session — ou par celle-ci après nettoyage — trouverait donc
    une section *Vérification* dont **aucune commande n'existe**, et l'épreuve des
    contrôles ne serait attestée nulle part dans le dépôt. C'est exactement la forme
    de PRO-01 : une garde dont on croit qu'elle tient parce qu'un rapport l'a dit une
    fois.

    Geste : `verifier-geometrie.py` et le couple `comparer-js-python.js` /
    `comparer.py` sont versés en `atelier/rd/outillage/`, avec un
    `spec-controles-geometrie-polaire.md`, sur le patron de
    `valider-index-livres.py` et de sa spec. Le comparateur cesse alors de lire le
    prototype du bac à sable pour lire **le rendu réel** du dépôt frère — ce qui le
    rend plus utile qu'il ne l'est aujourd'hui, puisqu'il gardera la géométrie
    effectivement servie. Le bac à sable, lui, reste jetable et peut disparaître sans
    rien emporter.

7. Ouvrir le bloc `polaire:` dans `instrument-donnees.yaml`, à la forme du
   `spec.md` §3.1. Version de la déclaration : **v0.8.0** (bloc nouveau).
8. `generer-manifeste.py` → schéma **v0.2.6** : propager le bloc, **dériver**
   `obliquite_deg` et `epoque_reference` depuis `zodiaque:` (jamais les redéclarer),
   implanter les sept gardes G1-G7 du `spec.md` §3.2.
9. Mettre à jour `spec-generateur-manifeste.md` : le schéma change, sa spec suit.
10. Régénérer le manifeste, contrôler la sortie.

### Phase 3 — le rendu, au dépôt frère

11. `/root/instrument/src/index.html` : calque `polaire`, sur le modèle exact du
    calque des six stations (IIFE, `monde.add(calque)`). Le disque `plan` existant
    reçoit son second état — il n'est pas dupliqué (Cmd 10).
12. La bascule : bouton d'abord (iPad), touche ensuite, comme les stations.
13. Le refus d'ouverture sans manifeste (`spec.md` §5) — **soumis à Sidy**, car il
    inaugure un comportement que le rendu n'a pas.
14. Vérifier les douze critères d'acceptation.

### Phase 4 — publication

15. Manifeste poussé depuis le wiki par `publier-manifeste-instrument.sh`.
16. Mise en production : **porte humaine** (`PUBLIER=1`, INF-14).

## Fichiers touchés

| fichier | opération |
|---|---|
| `atelier/rd/instrument/ins-15-situation-polaire/{intent,spec,plan}.md` | **créés** |
| `atelier/rd/registre-chantiers.md` | modifié — ligne INS-15 |
| `atelier/annales.md` | modifié — entrée du 2026-09-02 |
| `doctrinal/annales.md` | modifié — entrée du 2026-09-02 (second circuit touché) |
| `doctrinal/sources/tilak-origine-polaire-tradition-vedique.md` | modifié — § *Fiabilité* |
| `atelier/rd/instrument/instrument-donnees.yaml` | modifié — bloc `polaire:` (**après visa**) |
| `atelier/rd/outillage/generer-manifeste.py` | modifié — schéma v0.2.6 (**après visa**) |
| `atelier/rd/outillage/spec-generateur-manifeste.md` | modifié (**après visa**) |
| `atelier/rd/outillage/verifier-geometrie-polaire.py` | **créé** — versement des contrôles (**après visa**, étape 6 bis) |
| `atelier/rd/outillage/comparer-geometrie-rendu.py` | **créé** — idem, lit le rendu réel |
| `atelier/rd/outillage/spec-controles-geometrie-polaire.md` | **créé** — idem |
| `atelier/rd/instrument/wiki-manifest.json` | **régénéré** — artefact, jamais édité |
| `/root/instrument/src/index.html` | modifié — calque polaire (**après visa**) |
| `/root/sandbox-rd/ins-15-polaire/` | **hors dépôt**, jetable, non versionné |

Rien n'est supprimé ni déplacé (Cmd 10).

## Vérification

Les commandes qui **prouvent** chaque critère du `spec.md` §4 :

```bash
# Critères 1, 2 — la géométrie, et l'accord scène ↔ contrôle
#   AVANT le versement (Phase 0, bac à sable jetable) :
cd /root/sandbox-rd/ins-15-polaire
python3 verifier-geometrie.py                 # 8 OK passe 1, 8 ÉCHEC passe 2
node comparer-js-python.js && python3 comparer.py
python3 comparer.py --fausser                 # DOIT détecter
#   APRÈS le versement (étape 6 bis) — c'est cette forme qui fait foi :
cd /root/wiki
python3 atelier/rd/outillage/verifier-geometrie-polaire.py
python3 atelier/rd/outillage/comparer-geometrie-rendu.py --rendu /root/instrument/src/index.html

# Critère 6 — le manifeste porte le bloc
cd /root/wiki
python3 atelier/rd/outillage/generer-manifeste.py --repo /root/wiki
jq -e '.polaire.cycles.yugas | length == 4' atelier/rd/instrument/wiki-manifest.json

# Critère 7 — chaque garde bloque VRAIMENT (une par une, puis restaurer)
#   G1 : fausser latitude_min_deg    → refus attendu
#   G3 : ajouter obliquite_deg       → refus attendu (Cmd 14)
#   G5 : porter Kali-Yuga à 6500     → refus attendu
#   G7 : vider une source `etabli`   → refus attendu

# Critère 8 — le dépôt reste sain
python3 verifier-invariants.py                # 0 erreur, 0 avertissement
```

**Le contrôle qui n'observe rien n'est pas un contrôle.** Chaque garde G1-G7 est
éprouvée par l'échec avant d'être déclarée en place — c'est la leçon de PRO-01 (un
contrôle gardait `main` en parcourant des dossiers inexistants et imprimait
« Frontmatter OK » sur zéro fichier), et celle des hooks d'INF-14 (un motif `grep`
qui ne correspondait jamais, la même faute reproduite dans du code neuf).

## Points de retour à l'humain (Cmd 13)

1. **Le visa de ce plan.** Rien de la Phase 2 ne commence avant.
2. **Le refus d'ouverture sans manifeste** (`spec.md` §5) : il tranche *contre* le
   précédent du repli. Décision de rendu, donc de Sidy.
3. **La mise en production** sur `sidyvision.com/instrument/` (`PUBLIER=1`).
4. **Verdicts doctrinaux, aucun n'appartient à la machine** : Balance polaire ↔
   Balance zodiacale ; sapta-ṛkṣa ↔ sept Aqtâb ; ouverture d'un chantier `DOC-` pour
   l'ingest des deux ouvrages de Tilak, dont la matière intégrale est au sas.
5. **Rien à porter au protocole** : la clause de lecture lourde était réputée non
   poussée, mais vérification faite elle est bien sur `main` depuis le 2026-09-01
   (`89f5b51`, §I, « Clôture économique PRODUCTION/INTÉGRATION — levée »). C'était la
   session locale qui n'avait pas tiré. Aucune action ; le point est clos et laissé
   ici pour que le doute ne se rouvre pas.

## Journalisation

- `atelier/annales.md` — circuit de ce chantier (Cmd 9).
- `doctrinal/annales.md` — second circuit touché, pour la seule correction de la
  fiche Tilak. ⚠ Cette entrée **ne nomme ni le chantier, ni l'Instrument, ni aucune
  fiche `rd/`** : le Sceau atelier pose le sens unique, « aucune page doctrinale ne
  mentionne jamais un projet ni une fiche `rd/`, l'Instrument inclus ».
- `atelier/rd/registre-chantiers.md` — ligne INS-15, statut et pointeur de triptyque,
  mise à jour dans la même passe (section *Entretien* du registre).
