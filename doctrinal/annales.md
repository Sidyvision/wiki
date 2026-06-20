---
title: Annales du Secrétariat Doctrinal
type: meta
updated: 2026-06-20
---

# Annales du Secrétariat Doctrinal

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

---

## [2026-06-20] extension protocolaire | Intégration du Circuit Discernement
- **Modifié** : CLAUDE.md (Architecture du Dépôt, Nomenclature, Sceau Recteur, Protocoles d’Exécution — ajout du type `discernement`, du statut `speculatif`, et de l’action EXAMEN DE DISCERNEMENT) ; doctrinal/index.md (nouvelle section « Le Registre du Discernement », renumérotation Atelier→VIII, Domaine Réservé→IX)
- **Créé** : doctrinal/discernement/ (répertoire, placeholder `.gitkeep`)
- **Notes** : permet le traitement rigoureux des conversations de l’export ChatGPT mêlant expérience personnelle et portée métaphysique (catégorie A+C du triage), sans contaminer les pages de référence orthodoxes par une hypothèse encore instable. Recalages de forme sur l’UPDATES (établi sur un état antérieur du protocole) : références de section ramenées au CLAUDE.md réel (9 sections, I–IX) ; type `source` préservé dans l’énumération `type`. **À clarifier (VIGILANCE)** : le bloc EXAMEN renvoie au « Commandement 12 (upakarana) » alors que la Section IX n’en compte que 11.

---

## [2026-06-12] restauration | Révision du protocole CLAUDE.md
- **Opération** : RESTAURATION (protocole)
- **Modifié** : CLAUDE.md (workflow iPad/serveur documenté, circuit atelier + projets,
  doctrinal/sources/ ajouté, meta/ clarifié, Sceau Recteur enrichi du champ sources,
  procédure post-ingest pédagogique, vocabulaire « restauration »)
- **Créé** : atelier/{materiel,entretiens,projets}/, doctrinal/sources/
- **Notes** : le mot « réforme » est banni du dépôt ; MIGRATION.md archivé en meta/.

---

## 2026-06-11 — Restauration structurelle complète

- **2026-06-11** : Restauration structurelle complète du dépôt. Abandon des nomenclatures profanes (`recherche`, `business`, `ingest`, `lint`). Passage à l'architecture doctrinale (`doctrinal/{doctrines,traditions,symboles,autorites,deviations,etudes}` + `meta/`) selon le nouveau `CLAUDE.md`. Migration sans perte des fiches existantes (Soufisme, Astrologie, Islam & IA). Frontmatters convertis au Sceau Recteur (`type`/`status`/`tradition_cadre`/`sources_count`/`cross_links`). Frontmatters corrompus (iPad) réparés : al-jazari, al-khwarizmi, ibn-sina, yaqub-chaudhary, islam-et-ia, islam-and-artificial-intelligence, al-ghazali. `UPDATE al-ghazali.md` fusionné dans `autorites/al-ghazali.md` ; `UPDATES-index-log.md` appliqué puis retiré. Fiches à mention personnelle (`sidy`, export ChatGPT) maintenues hors `doctrinal/` (dossier `meta/`, étanchéité). `talisman-sihr` classé en `symboles/` (science traditionnelle) avec bloc de distinction du *siḥr* (contre-traditionnel). Snapshot de sauvegarde réalisé avant migration. Synchronisation Obsidian Git validée.

---

## 2026-06-04 — Archivage : Islam and Artificial Intelligence

- **Opération** : ARCHIVAGE & MAILLAGE
- **Cadre** : islam (academique)
- **Créé** : source [[doctrinal/sources/islam-and-artificial-intelligence]] ; autorités [[doctrinal/autorites/yaqub-chaudhary]], [[doctrinal/autorites/ibn-sina]], [[doctrinal/autorites/al-jazari]], [[doctrinal/autorites/al-khwarizmi]] ; étude [[doctrinal/etudes/2026-06-04_islam-et-ia]]
- **Modifié** : [[doctrinal/autorites/al-ghazali]] (enrichi)
- **Source brute** : `raw/islam-and-artificial-intelligence.pdf` — chapitre académique, Cambridge UP, Yaqub Chaudhary, pp. 109–128
- **Notes** : Ingéré via l'app iPad ; frontmatters réparés et fiches reclassées lors de la restauration du 2026-06-11.

---

## 2026-06-03 — Archivage : ʿIlm al-Nujûm (astrologie traditionnelle)

- **Opération** : ARCHIVAGE & MAILLAGE
- **Créé** : source [[doctrinal/sources/ilm-al-nujum-astrologie-traditionnelle]] ; symbole [[doctrinal/symboles/ilm-al-nujum]]
- **Modifié** : [[doctrinal/autorites/ibn-arabi]] (l'existence comme voyage, contexte astrologique)
- **Source brute** : `raw/LA FIN DES TEMPS MODERNES ‘ILM AL-NUJÛM - ASTROLOGIQUE TRADITIONNELLE.pdf` — <https://lafindestempsmodernes.blogspot.com>, 24 avril 2024
- **Notes** : Lien établi entre [[doctrinal/symboles/ilm-al-nujum]] et [[doctrinal/symboles/ilm-al-huruf]] (mêmes correspondances planétaires).

---

## 2026-06-02 — Archivage : Shams al-Maʿārif al-Kubrā

- **Opération** : ARCHIVAGE & MAILLAGE
- **Créé** : source [[doctrinal/sources/shams-al-maarif]] ; autorités [[doctrinal/autorites/ahmad-al-buni]], [[doctrinal/autorites/ouattara-brahima]] ; symboles [[doctrinal/symboles/ilm-al-huruf]], [[doctrinal/symboles/asma-al-husna]], [[doctrinal/symboles/talisman-sihr]]
- **Source brute** : `raw/shams-al-maarif-traduit-complet.pdf` — 631 p., trad. Ouattara Brahima (nov. 2025)
- **Notes** : Source de type pratique (praticien soufi ouest-africain). Lien établi entre [[doctrinal/autorites/ahmad-al-buni]] et [[doctrinal/autorites/ibn-arabi]].

---

## 2026-06-02 — Archivage : Jesus and Enoch in Ibn ʿArabī

- **Opération** : ARCHIVAGE & MAILLAGE
- **Créé** : source [[doctrinal/sources/jesus-and-enoch-in-ibn-arabi]] ; autorité [[doctrinal/autorites/idris]] ; symboles [[doctrinal/symboles/barzakh]], [[doctrinal/symboles/wahdat-al-wujud]]
- **Modifié** : [[doctrinal/autorites/ibn-arabi]] (prophétologie, miʿrāj, wahdat al-wujud), [[doctrinal/autorites/ali-hussain]] (publication JMIAS 2016)
- **Source brute** : `raw/Jesus_And_Enoch_In_Ibn_'arabi.pdf` — article académique, JMIAS Vol. 60, 2016, Dr. Ali Hussain, 11 p.

---

## 2026-06-02 — Archivage : Awrad Ibn Arabi

- **Opération** : ARCHIVAGE & MAILLAGE
- **Créé** : source [[doctrinal/sources/awrad-ibn-arabi]] ; autorité [[doctrinal/autorites/ali-hussain]] ; symboles [[doctrinal/symboles/wird-awrad]], [[doctrinal/symboles/salawat]], [[doctrinal/symboles/walaya]]
- **Modifié** : [[doctrinal/autorites/ibn-arabi]] (stub enrichi, sourcé)
- **Source brute** : `raw/Awrad_Ibn_Arabi.pdf` — 177 p., bilingue arabe/anglais, Dr. Ali Hussain (ISCA, 2022)

---

## 2026-06-02 — Premier archivage (profil utilisateur)

- **Opération** : ARCHIVAGE & MAILLAGE
- **Créé** : profil [[meta/sidy]], source [[meta/chatgpt-export-2026-05-10]] ; stubs d'autorités/formes : [[doctrinal/autorites/ibn-arabi]], [[doctrinal/autorites/al-ghazali]], [[doctrinal/autorites/rene-guenon]], [[doctrinal/autorites/platon]], [[doctrinal/traditions/sanatana-dharma]], [[doctrinal/traditions/ahl-al-sunnah-wa-l-jamaa]], [[doctrinal/traditions/tasawwuf]]
- **Étanchéité** : fiches personnelles tenues hors `doctrinal/`.
- **Notes** : 140 conversations de l'export non ingérées (réserve). PII (téléphone, e-mail) volontairement exclue ; export brut protégé par `.gitignore`.
