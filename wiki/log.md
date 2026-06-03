---
title: Journal des sessions
type: meta
updated: 2026-05-24
---

# Journal des sessions

Entrées chronologiques inverses (la plus récente en haut). **Une entrée par session de travail**, ajoutée systématiquement à la fin de chaque opération INGEST / LINT / COMPARTIMENTALISER.

Distinct de `wiki/logs/` qui stocke des pages de type `log` (événements datés conservés comme contenu).

## Format d'une entrée

```markdown
## YYYY-MM-DD — opération

- **Opération** : INGEST | QUERY | LINT | COMPARTIMENTALISER
- **Domaine(s)** : ...
- **Créé** : [[slug-1]], [[slug-2]]
- **Modifié** : [[slug-3]]
- **Supprimé / déprécié** : —
- **Notes** : remarques utiles à la session suivante.
```

---

<!-- entrées ci-dessous, plus récente en premier -->

## 2026-06-02 — INGEST Shams al-Maʿārif al-Kubrā (traduction française)

- **Opération** : INGEST
- **Domaine(s)** : `general`
- **Créé** :
  - sources : [[shams-al-maarif]]
  - entities : [[ahmad-al-buni]], [[ouattara-brahima]]
  - concepts : [[ilm-al-huruf]], [[asma-al-husna]], [[talisman-sihr]]
- **Modifié** : `wiki/index.md`
- **Supprimé / déprécié** : —
- **Source brute** : `raw/shams-al-maarif-traduit-complet.pdf` — 631 p., traduction française partielle par Ouattara Brahima (nov. 2025)
- **Notes** : Troisième INGEST PDF. Source de type pratique (praticien soufi ouest-africain, non académique) — signalé dans la fiche source. Le concept [[talisman-sihr]] est marqué `#stub` (débat licite/illicite non traité). Lien établi entre [[ahmad-al-buni]] et [[ibn-arabi]] (contemporains, univers conceptuel commun).

## 2026-06-02 — INGEST Jesus and Enoch in Ibn ʿArabī

- **Opération** : INGEST
- **Domaine(s)** : `general`
- **Créé** :
  - sources : [[jesus-and-enoch-in-ibn-arabi]]
  - entities : [[idris]]
  - concepts : [[barzakh]], [[wahdat-al-wujud]]
- **Modifié** : [[ibn-arabi]] (enrichi — prophétologie, miʿrāj, étymologie, wahdat al-wujud), [[ali-hussain]] (enrichi — publication JMIAS 2016), `wiki/index.md`
- **Supprimé / déprécié** : —
- **Source brute** : `raw/Jesus_And_Enoch_In_Ibn_'arabi.pdf` — article académique, JMIAS Vol. 60, 2016, Dr. Ali Hussain, 11 p.
- **Notes** : Deuxième INGEST PDF. Même auteur que [[awrad-ibn-arabi]]. Concepts non encore dotés de page propre (tanzīh/tashbīh, tajallī, nafas al-raḥmān) : candidats pour un prochain LINT.

## 2026-06-02 — INGEST Awrad Ibn Arabi

- **Opération** : INGEST
- **Domaine(s)** : `general`
- **Créé** :
  - sources : [[awrad-ibn-arabi]]
  - entities : [[ali-hussain]]
  - concepts : [[wird-awrad]], [[salawat]], [[walaya]]
- **Modifié** : [[ibn-arabi]] (stub enrichi, tag `#stub` retiré), `wiki/index.md`
- **Supprimé / déprécié** : —
- **Source brute** : `raw/Awrad_Ibn_Arabi.pdf` — 177 p., bilingue arabe/anglais, Dr. Ali Hussain (ISCA, 2022)
- **Notes** : Premier INGEST PDF. Tag `#stub` d'[[ibn-arabi]] retiré : page désormais sourcée. [[ali-hussain]] créé comme entité distincte.

## 2026-06-02 — premier INGEST (profil utilisateur)

- **Opération** : INGEST
- **Domaine(s)** : `perso` (page principale + source), `general` (stubs de références)
- **Créé** :
  - perso : [[sidy]], [[chatgpt-export-2026-05-10]]
  - general : [[ibn-arabi]], [[al-ghazali]], [[rene-guenon]], [[platon]], [[sanatana-dharma]], [[ahl-al-sunnah-wa-l-jamaa]], [[tasawwuf]]
- **Modifié** : `wiki/index.md` (sections perso + general)
- **Supprimé / déprécié** : —
- **Source** : export ChatGPT du 2026-05-10 (`raw/`, non versionné).
- **Étanchéité** : liens uniquement `perso → general` (descendants). Aucun lien retour `general → sidy` créé (remontée interdite sans signalement).
- **Notes** : 140 conversations de l'export **non ingérées** (réserve pour futurs INGEST thématiques : spiritualité, symbolisme, rêves, plantes/santé…). PII (téléphone, e-mail) volontairement exclue ; export brut protégé par `.gitignore`. Les 7 stubs `general` sont à enrichir (`#stub`, `to-source`).

## 2026-06-02 — mise à jour onboarding

- **Opération** : maintenance méta (hors INGEST/QUERY/LINT/COMPARTIMENTALISER)
- **Domaine(s)** : —
- **Créé** : —
- **Modifié** : `schema/onboarding.md` (Obsidian → résolu ; clé API → persistée ; table infra ; prochaines étapes)
- **Supprimé / déprécié** : —
- **Notes** : (1) synchro Obsidian iPad désormais automatique (pull on startup + intervalle). (2) `ANTHROPIC_API_KEY` persistée dans `~/.bashrc` — nettoyage de 4 lignes `export` cassées, une seule conservée ; clé hors repo. Reste à faire : alimenter `raw/`, premier INGEST.
