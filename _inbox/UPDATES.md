# UPDATES — Correctifs de frontmatter issus de l'audit de cartographie

**Date** : 2026-07-22
**Origine** : premier passage de `generer-cartographie.py --verifier` sur `/root/wiki`
(336 anomalies remontées, dont la majeure partie relevait d'un effet de cascade
du script v1.0, corrigé depuis en v1.1).
**Circuits touchés** : `doctrinal/`, `atelier/`
**Traitement** : **fiche par fiche**, dans l'ordre de ce manifeste (CLAUDE.md §VIII.3).

---

## Règles de la passe

1. **Aucune modification du corps des fiches.** Seul le frontmatter est touché,
   et uniquement les champs nommés ci-dessous.
2. **Pas d'auto-accept** (CLAUDE.md §VIII.1) : chaque `Update` est présenté et relu
   avant validation.
3. **Aucune invention de contenu.** Si une instruction ci-dessous ne peut être
   appliquée telle quelle, la fiche est **laissée en l'état** et signalée dans le
   compte rendu de fin de passe. Ne jamais combler par déduction.
4. **Clôture obligatoire** par une vérification mécanique indépendante :
   `python3 generer-cartographie.py --depot /root/wiki --verifier --rapport /tmp/apres.txt`
   Le rapport BRUT est restitué à Sidy — pas un résumé narratif (CLAUDE.md §VIII.2).
5. **Annales** : une seule entrée append-only pour toute la passe, incluant la
   liste nominative des fiches du Lot B (voir ci-dessous). Aucune suppression
   silencieuse (Commandement 9).

---

## LOT A — Recalcul de `sources_count` (27 fiches) — MÉCANIQUE

**Nature** : `sources_count` est, par définition du Sceau Recteur (CLAUDE.md §IV),
la longueur de la liste `sources`. Dans ces 27 fiches, le compteur est **inférieur**
au nombre réel d'entrées : il est simplement périmé. Aucune information n'est perdue
en le recalculant.

**Action** : pour chaque fiche du circuit `doctrinal/` où
`sources_count != len(sources)` **et** `sources_count < len(sources)` :
poser `sources_count = len(sources)`.

**Ne touche à rien d'autre.** Notamment : ne pas modifier la liste `sources` elle-même.

> ℹ️ Le script v1.1 liste ces fiches sous la catégorie `compteur` avec la mention
> `(inférieur)`. Générer la liste par :
> `python3 generer-cartographie.py --depot /root/wiki --verifier --rapport /tmp/avant.txt`
> puis `grep "(inférieur)" /tmp/avant.txt`

---

## LOT B — `sources_count` renseigné, champ `sources:` ABSENT (17 fiches) — MÉCANIQUE
### (révisé après vérification git — voir note ci-dessous)

**Nature, établie par examen de l'historique** : dans ces 17 fiches, `sources:`
n'a **jamais existé**, sous aucune forme — ni liste remplie, ni `[]`, ni
`["to-source"]`. `git show 990bcfa:doctrinal/autorites/ibn-arabi.md` (commit de la
« Réforme doctrinale globale (Guénon V1) », 2026-06-11) le confirme : le frontmatter
posé ce jour-là contient `sources_count: 3` sans aucun champ `sources`. Un balayage
des 16 autres fiches du lot montre exactement le même motif, sans exception
(`grep -c "^sources:"` → 0 partout). Il ne s'agit donc pas d'une perte de données à
préserver (rien n'a jamais été rempli), mais d'une omission du Sceau Recteur au
moment de sa rédaction.

**Action** : pour chacune des 17 fiches listées ci-dessous, ajouter le champ
manquant : `sources: ["to-source"]` — conformément à CLAUDE.md §IV, *« Fait sans
source → `sources: ["to-source"]` + signalement »*. **Ne pas toucher à
`sources_count`** : il reste tel quel, et devient de fait cohérent avec une liste
d'une entrée `to-source` s'il valait déjà 1 — sinon l'écart residuel est du ressort
du Lot A une fois les sources réellement retrouvées et documentées.

Chaque fiche corrigée doit également apparaître, une fois la passe close, dans le
tableau de discipline des sources (`to-source` levé uniquement sur texte primaire
vérifié par Sidy — CLAUDE.md, discipline des sources, transversale).

Fiches concernées :

| Fiche | `sources_count` |
|---|---|
| `doctrinal/autorites/ibn-arabi.md` | 3 |
| `doctrinal/autorites/ali-hussain.md` | 2 |
| `doctrinal/symboles/ilm-al-huruf.md` | 2 |
| `doctrinal/autorites/ahmad-al-buni.md` | 1 |
| `doctrinal/autorites/al-ghazali.md` | 1 |
| `doctrinal/autorites/al-jazari.md` | 1 |
| `doctrinal/autorites/al-khwarizmi.md` | 1 |
| `doctrinal/autorites/ibn-sina.md` | 1 |
| `doctrinal/autorites/idris.md` | 1 |
| `doctrinal/autorites/ouattara-brahima.md` | 1 |
| `doctrinal/autorites/yaqub-chaudhary.md` | 1 |
| `doctrinal/symboles/asma-al-husna.md` | 1 |
| `doctrinal/symboles/ilm-al-nujum.md` | 1 |
| `doctrinal/symboles/salawat.md` | 1 |
| `doctrinal/symboles/talisman-sihr.md` | 1 |
| `doctrinal/symboles/wird-awrad.md` | 1 |
| `doctrinal/etudes/2026-06-04_islam-et-ia.md` | 1 |

---

## LOT C — Coquille de slug (1 fiche) — MÉCANIQUE

**Nature** : deux fiches pointent vers `[[table-28-degres-nafas-rahmân]]`, avec un
accent circonflexe. La fiche réelle est `doctrinal/symboles/table-28-degres-nafas-rahman.md`
(sans accent, conforme à la règle de nommage ASCII, CLAUDE.md §III).

**Action** : dans les frontmatter de
- `atelier/projets/spec-technique-axe-38-degres.md` (champ `sources`)
- `doctrinal/sources/transcription-anneau-28-lettres-figure4.md` (champ `cross_links`)

remplacer `[[table-28-degres-nafas-rahmân]]` par
`[[doctrinal/symboles/table-28-degres-nafas-rahman]]`.

**Vérifier d'abord** que la fiche cible existe bien sous ce nom exact. Si elle
n'existe pas : ne rien modifier, signaler.

---

## LOT D — Fiches sans frontmatter (3 fichiers) — RELEVÉ SEUL

**Nature** : trois fichiers ne commencent pas par `---`. Ils n'ont donc pas de Sceau
Recteur et sont invisibles pour tout manifeste.

- `doctrinal/sources/transcription-index-tilak-origine-polaire.md`
- `doctrinal/sources/transcription-table-matieres-symboles-science-sacree.md`
- `atelier/projets/note-impact-instrument-socle-universel-2026-07-16.md`

**Action** : **ne pas rédiger de frontmatter.** Les champs `type`, `status` et
`tradition_cadre` engagent une qualification qui relève de Sidy (Commandement 12).

Consigner ces trois chemins dans le compte rendu de fin de passe, avec pour chacun
la première ligne du fichier (pour identification), et rien de plus.

---

## HORS PÉRIMÈTRE DE CETTE PASSE — pour information

Les points suivants ont été remontés par l'audit mais **ne sont pas traités ici**,
car ils appellent un arbitrage de Sidy et non une correction mécanique :

1. **8 violations d'étanchéité** (CLAUDE.md §VI) — liens remontants du neutre vers
   le sensible :
   - `atelier/materiel/{neve-1073spx, tascam-model-12, technics-su-8080}.md`
     → `atelier/projets/album-personnel.md`
   - `doctrinal/sources/guenon-{homme-devenir…, symbolisme-croix-ch11-13, ch2-3, ch23-29}.md`
     → `atelier/projets/instrument-…-v0_3.md`
   - `doctrinal/sources/guenon-symbolisme-croix-ch4-directions-espace.md`
     → `atelier/projets/angles-de-l-espace.md`

   Ces liens sont **bloquants** dans le script. Deux issues possibles (à trancher) :
   retirer le lien remontant, ou reconnaître que la hiérarchie d'étanchéité codée
   dans le script ne reflète pas l'intention réelle pour `atelier/projets/`.

2. **`sources:` contenant des URLs ou des citations bibliographiques en texte libre**
   (`atelier/etudes-de-cas/stones-throw.md`, la référence Spence dans
   `2026-07-03_orientation-chronometre-guenon-spence.md`, la référence Guénon dans
   `2026-07-03_guenon-tombeau-hermes.md`). Le Sceau Recteur prévoit `"[[slug]]"` ou
   `"to-source"` ; la question de savoir si une source externe non-fichée a droit de
   cité dans ce champ n'est pas tranchée.

3. **Liens vers `meta/`** (`chatgpt-export-2026-05-10`, `philosophie-sashimono`,
   `hermes-prompts`, `2026-06-20_oiseau-serpent-jumeau`) : signalés comme morts
   uniquement parce que `meta/` est exclu du manifeste par défaut. Décision à prendre
   sur `--inclure-meta`.

4. **Fiche `autorite` jamais créée** : `doctrinal/autorites/charles-andre-gilis`,
   référencée par `doctrinal/sources/sept-etendards-califat.md`.

Ces quatre points sont à instruire en session avec Sidy, pas côté intégration.

---

## Ordre d'exécution

1. Lot A (27 fiches, une par une)
2. Lot B (17 fiches, une par une)
3. Lot C (2 fiches)
4. Lot D → consigner, **ne rien modifier**
5. `git diff --stat` présenté à Sidy pour validation **avant** tout commit
6. Vérification mécanique : `--verifier --rapport /tmp/apres.txt`, rapport brut restitué
7. Entrée d'annales unique, append-only
