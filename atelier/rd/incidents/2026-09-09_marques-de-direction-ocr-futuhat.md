---
title: "Incident Cmd 15 — marques de direction (U+200E/U+200F) dans l'OCR des Futūḥāt"
type: outillage
statut_experience: reproduit
created: 2026-09-09
updated: 2026-09-09
status: resolu
severity: faible
affected_systems: [wiki, textes, conversion-ocr]
original: []
---

# Incident Cmd 15 — marques de direction dans l'OCR des *Futūḥāt al-Makkiyya*

## Résumé

Le lot `_inbox/al-futuhat-al-makkiyya-maymaniya-p1.md` — *Al-Futūḥāt al-Makkiyya*,
édition Maymaniya, tome 1, 779 pages océrisées — portait **2112 caractères Unicode
invisibles** : **1302 U+200F** (RIGHT-TO-LEFT MARK) et **810 U+200E** (LEFT-TO-RIGHT
MARK). Le **Commandement 15** les interdit nommément.

Détecté **avant** tout versement, à la lecture du lot demandée par Sidy
(« verse-les dans textes/ »).

## Ce qui a détecté, et ce qui ne l'aurait pas fait

| Dispositif | Aurait-il vu ? |
|---|---|
| `verifier-invariants.py` | **Non** — `_inbox/` est dans `DOSSIERS_EXCLUS`, jamais parcouru |
| hook `pre-push` | **Oui**, mais **au push**, donc après commit |
| contrôle manuel de session | **Oui** — c'est celui qui a joué |

Le lot a séjourné au sas du **2026-09-07 au 2026-09-09** sans qu'aucun contrôle
automatique ne le regarde. **Le sas est un angle mort mécanique** : c'est cohérent
(`_inbox/` n'est pas encore matière du dépôt), mais cela signifie qu'un lot n'est
contrôlé qu'au moment où quelqu'un décide de l'intégrer. Rapporté comme tel, non corrigé
d'office — étendre le contrôle au sas demanderait son propre verdict.

## Le dépôt était intégralement propre

Mesure de contexte, prise avant toute écriture :

- **0 fichier sur 641** de `textes/` portait une marque de direction — y compris les
  94 fichiers en écriture arabe.
- **0 fiche** des cinq circuits n'en portait.

L'incident n'est donc pas une contamination du dépôt mais **une propriété de la sortie
de l'outil de conversion**, arrêtée à la porte.

## Origine

`pdftoppm 300dpi + tesseract 5 (ara)`, déclaré dans l'en-tête du lot. Tesseract insère
des marques de direction aux frontières où l'ordre bidirectionnel est ambigu — typiquement
autour des chiffres et des rares glyphes latins que l'OCR a cru reconnaître. **Ce ne sont
pas des caractères du texte imprimé** : un livre n'a pas de caractères invisibles. Ce sont
des artefacts de la **conversion**.

## Résolution, et pourquoi elle ne contrevient pas à la règle d'immuabilité

Le §II pose que « un texte de `textes/` ne se corrige pas ; une conversion meilleure le
remplace, datée ». Il y avait donc une tension apparente : garder les marques viole le
Cmd 15, les retirer semble corriger un texte reçu.

**La tension se dissout sur la ligne de coupe déjà posée par le protocole** : ce qui est
reçu, c'est le **texte** ; les marques de direction n'en font pas partie — elles
appartiennent au **dispositif de conversion**, exactement comme les marques ʿayn et hamza
appartiennent au dispositif de translittération et non à l'écriture d'origine (distinction
établie le 2026-09-08 pour `est_ecriture_originale`). Les retirer ne corrige donc pas le
texte : cela **produit une conversion meilleure**, ce que le §II prescrit précisément.

Le retrait est **littéral et sans exception** — aucun autre caractère n'est touché —, il
est **daté** dans l'en-tête du fichier versé, et il est **reproductible** : le hook
`pre-push` du dépôt nomme lui-même le remède
(`sed 's/[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{200E}\x{200F}]//g'`).

## Ce qui reste, et qui n'est PAS résolu par cet incident

La qualité de l'OCR est **médiocre**, et le retrait des marques n'y change rien. Mesuré
sur les 386 933 mots arabes du lot :

- **8078 mots de plus de 15 caractères** (2,1 %) — agglutinations où l'OCR a perdu
  l'espace : `وال مكروهاجتنبهقعلا`.
- **1399 séquences latines ou chiffrées insérées au milieu d'un mot arabe** — `ال1->م`,
  `خ8٠`, `ؤ<ذ` : des glyphes que l'OCR a mal reconnus.

**Un texte de `textes/` est cité en source par les fiches doctrinales.** Une transcription
à ce niveau de bruit ne peut pas servir de source primaire — et le §VII est explicite :
la levée d'un `to-source` demande la vérification du **texte primaire par Sidy lui-même**.
Ce lot ne lèvera donc jamais rien par lui-même, quelle que soit sa place.

Le verdict sur ce point appartient à Sidy (Cmd 12) et n'est **pas** tranché ici. Trois
voies ouvertes, aucune retenue d'office :

1. **Verser tel quel**, comme repère de localisation — savoir *qu'un passage existe* et
   *à quelle page*, sans jamais citer la graphie. C'est l'usage déjà admis pour les
   photographies de sommaires et d'index de la bibliothèque R&D (§VII, discipline des
   sources, point 1).
2. **Attendre une meilleure conversion** — le §II la prévoit explicitement, datée, en
   remplacement.
3. **Ne verser que ce qui est exploitable**, si une partie du volume est de meilleure
   qualité que le reste. Non mesuré page par page à ce jour.

## Références

- `CLAUDE.md` racine, **Cmd 15** (hygiène Unicode) et **§II** (`textes/`, immuabilité)
- Incident fondateur : `atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`
- Correctif du hook : `atelier/rd/incidents/2026-08-22_post-scriptum-hook-corrige.md`
