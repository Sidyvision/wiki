# Protocole de Restauration Traditionnelle du Wiki

> ⚠️ **Document d'archive (Restauration « Guénon V1 », 2026-06-11). Ne plus exécuter.** Conservé pour mémoire des opérations passées.

Ce fichier a servi d'instruction impérative à Claude Code pour migrer l'ancien formalisme profane vers le nouveau modèle traditionnel décrit dans le nouveau `CLAUDE.md`. L'objectif est d'exécuter la restructuration par manipulation de fichiers, sans ré-analyse textuelle coûteuse en tokens.

---

## Étape 1 : Remplacement du Cœur Opérationnel
1. Écrase le contenu de l'ancien `CLAUDE.md` par le nouveau texte de la "Refonte Intégrale" dicté par René Guénon.
2. Supprime l'ancien dossier `schema/` s'il contient des reliquats profanes (conserve `onboarding.md` en le déplaçant vers `meta/onboarding.md`).
3. Crée l'arborescence doctrinale si elle n'existe pas :
   `mkdir -p doctrinal/doctrines doctrinal/traditions doctrinal/symboles doctrinal/autorites doctrinal/deviations doctrinal/etudes meta/`

---

## Étape 2 : Migration et Ventilation de l'Existant (Sans re-lecture)
Déplace les fichiers actuellement indexés dans `wiki/` vers leurs nouveaux réceptacles sacrés dans `doctrinal/` selon les correspondances suivantes :

### A. Les Autorités (`wiki/entities/` → `doctrinal/autorites/`)
- `ibn-arabi.md` → `doctrinal/autorites/ibn-arabi.md`
- `al-ghazali.md` → `doctrinal/autorites/al-ghazali.md`
- `rene-guenon.md` → `doctrinal/autorites/rene-guenon.md`
- `platon.md` → `doctrinal/autorites/platon.md`
- `ali-hussain.md` → `doctrinal/autorites/ali-hussain.md`
- `ahmad-al-buni.md` → `doctrinal/autorites/ahmad-al-buni.md`

*Note Spéciale Perso* : L'entité `sidy.md` et `ouattara-brahima.md` (si lié aux ijâzas) doivent être déplacées vers `doctrinal/autorites/` mais leur frontmatter doit impérativement porter le statut `status: profane` ou `status: traditionnel` selon leur fonction, et le domaine `domain: perso` si la règle d'étanchéité l'exige.

### B. Les Concepts et Symboles (`wiki/concepts/` → `doctrinal/symboles/` ou `deviations/`)
- `tasawwuf.md`, `sanatana-dharma.md`, `ahl-al-sunnah-wa-l-jamaa.md`, `wird-awrad.md`, `salawat.md`, `walaya.md`, `barzakh.md`, `wahdat-al-wujud.md`, `ilm-al-huruf.md`, `asma-al-husna.md`, `ilm-al-nujum.md` → Déplacer vers `doctrinal/symboles/`.
- `talisman-sihr.md` → Analyser si le contenu traite de la magie profane ou de la science théurgique traditionnelle. Si profane/déviation → déplacer vers `doctrinal/deviations/`.

### C. Les Sources (`wiki/sources/` → `doctrinal/sources/` ou `raw/`)
Le dossier `wiki/sources/` devient obsolète. Toutes les fiches de lecture ou descriptions de sources doivent être centralisées selon leur nature. Les fichiers PDF bruts restent dans `raw/`.

---

## Étape 3 : Normalisation des Frontmatters (Script automatisé ou édition ciblée)
Pour chaque fichier déplacé, Claude Code doit modifier le frontmatter SANS toucher au corps du texte :
1. Remplacer `domain: general` ou `domain: recherche` par `tradition_cadre: "islam"` (pour le bloc soufisme) ou `"universel"`.
2. Ajouter le champ `status: traditionnel`.
3. Remplacer le champ `type: entity` ou `type: concept` par les types requis (`type: autorite`, `type: symbole`, etc.).

---

## Étape 4 : Initialisation des Méta-Pages
1. Écrase `wiki/index.md` (qui devient `doctrinal/index.md`) par le nouveau modèle de catalogue.
2. Nettoie `wiki/log.md` (qui devient `doctrinal/annales.md`) en actant la grande Restauration.
3. Supprime définitivement l'ancien dossier `wiki/` une fois vide pour éviter les doublons dans Obsidian.

---

## Étape 5 : Clôture et Validation
Exécute un `LINT` selon les règles du nouveau `CLAUDE.md` pour vérifier qu'aucun lien vertical n'est brisé. Effectue le commit :
`git add -A && git commit -m "CHG: Restauration doctrinale globale (Guénon V1)" && git push`
