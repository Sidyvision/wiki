---
title: Annales du Secrétariat Doctrinal
type: meta
updated: 2026-06-29
---

# Annales du Secrétariat Doctrinal

Journal chronologique inverse des opérations (la plus récente en haut). Append-only.

---

## [2026-06-29] infra | Cycle complet prepare/compare Ornith-1.0-9B (RunPod) — VERDICT 8 ✓ / 0 ✗, viable sous supervision humaine stricte
- **Opération** : INFRASTRUCTURE (session A6 — suite directe du test précédent, en session Claude Code neuve).
- **Rangé** : [[meta/projet-unifie/07-resultats-finaux-test-ornith-prepare-compare-2026-06-29|résultats finaux]] (via `_inbox/`, frontmatter meta conforme) ; lié à [[meta/projet-unifie/06-compte-rendu-test-ornith-gpu-cloud-2026-06-29|06]].
- **Verdict** : cycle `prepare → compare` **8 ✓ / 0 ✗** — Ornith équivaut à Opus sur le lot témoin (contenu byte-identique, index/annales corrects, zéro effet de bord). Rôle d'intégration **viable sous supervision humaine stricte**.
- **Enseignement central** : *fiabilité d'action ≠ fiabilité narrative* — en session longue (~30-40 min), le discours d'Ornith se dégrade (termes inventés, langues mêlées, fuite `</think>`, contradiction sur l'état du travail) **alors que ses écritures restent correctes**. Règles fermes adoptées : **jamais d'auto-accept**, **toujours clore par une vérification mécanique indépendante** (`ornith-test.sh compare`), **limiter la durée des sessions**.
- **Reste à tester** : intégration **doctrinale** (Sceau Recteur, Discernement, étanchéité), plus risquée que le cas atelier/meta couvert ici.
- **Mises à jour** : runbook [[meta/projet-unifie/05-runbook-test-ornith-gpu-cloud|05]], [[meta/projet-unifie/03-transition-modele-open-source|03]] et [[meta/projet-unifie/04-sessions-par-fonction-et-backlogs|04]] complétés. Rien de la session de test n'a touché le vrai dépôt (bac à sable isolé). Lot *archéomètre* du sas toujours non traité.

## [2026-06-29] infra | Premier test GPU cloud Ornith-1.0-9B (RunPod) — selftest PASS, prepare/compare à reproduire
- **Opération** : INFRASTRUCTURE (session A6 — transition modèle open-source).
- **Rangé** : [[meta/projet-unifie/06-compte-rendu-test-ornith-gpu-cloud-2026-06-29|compte-rendu du 1er test]] (via `_inbox/`, frontmatter meta conforme — aucune correction).
- **Résultat** : architecture validée (RunPod Pod RTX A6000 48 Go, vLLM, Ornith-1.0-9B) ; tunnel SSH Hetzner↔GPU OK ; Claude Code branché sur Ornith ; boucle agentique fonctionnelle ; `ornith-test.sh selftest` **PASS (8/0)**. Cycle `prepare → compare` **interrompu** sur une anomalie de cohérence d'Ornith (fin de session longue) — non tranchée, à reproduire en session neuve.
- **Correctifs intégrés** au runbook [[meta/projet-unifie/05-runbook-test-ornith-gpu-cloud|05]] et à [[meta/projet-unifie/03-transition-modele-open-source|03]]/[[meta/projet-unifie/04-sessions-par-fonction-et-backlogs|04]] : RunPod **Pod** (pas Serverless), authentification via `ANTHROPIC_CUSTOM_HEADERS` (vLLM exige `Authorization: Bearer`), `--max-model-len 131072` (plancher réaliste), pièges sshd/port/`pkill`.
- **Note** : rien issu de la session de test elle-même n'a touché le vrai dépôt (tout sur le Pod distant + bac à sable isolé). Seul le compte-rendu est archivé ici. Lot *archéomètre* du sas non traité (intégration séparée).

## [2026-06-28] regularisation | Lectures suggérées rétroactives (14 fiches discernement)
- **Opération** : RESTAURATION (normalisation rétroactive du protocole) — ajout du champ **Lectures suggérées** sous la « Conclusion » du bloc 🔍 normalisé, sans autre modification du corps des fiches.
- **Modifié** : 14 fiches `doctrinal/discernement/` — les 2 du 2026-06-11 (`llm-wiki-modalite-intellect`, `llm-wiki-correction-doctrinale`) et les 12 de la session ChatGPT-export du 2026-06-20 (visions-centre-nocturne, matrices-artificielles-barzakh, triptyque-medine-jeu-de-piste, experience-lefke-materia-secunda, epreuve-tariqa-tarbiyya-rabbaniyya, signaletique-spirituelle-kiswa, pierres-astres-barzakh, fajr-vajra-indra-vritra, mythe-personnel-unifie, astrologie-akbarienne-fard, synthese-danger-dissolution-identitaire, origine-jumeau-spirituel).
- **Source** : [[meta/bibliotheque-physique|Bibliothèque physique de travail]] (recension validée par Sidy, 2026-06-28), pages existantes du wiki, et quelques candidats hors-possession signalés pour `raw/`.
- **Méthode** : lectures rattachées à la généalogie et à la tension formelle propres à *chaque* fiche, non à une bibliographie générale. Aucune spéculation tranchée (Cmd 12, *upakarana*) : toutes les fiches restent `en cours`. Point de vigilance maintenu pour `epreuve-tariqa-tarbiyya-rabbaniyya` (question d'autorité spirituelle) : lectures choisies pour éclairer la *forme* (modalité confrérique, *tarbiyya rabbaniyya*) sans jamais suggérer une résolution de la question d'autorité elle-même, qui revient au Cheikh.
- **VIGILANCE** : toutes les cibles wikilink citées (`alam-al-mithal`, `khalwa`, `barzakh`, `fal-wa-tatayyur`, `waqia`, `merkavah-muraqaba`, `shinto`, `ilm-al-nujum`, `walaya-fath-adab`, `ibn-arabi`, `rene-guenon`, `al-insan-al-kamil`, `ahmad-al-buni`) vérifiées présentes — aucun lien mort.

## [2026-06-28] archivage | Esquisse v0.1 — Instrument de la Tradition Primordiale (atelier/projets)
- **Opération** : ARCHIVAGE (circuit atelier, hors Sceau Recteur).
- **Créé** : [[atelier/projets/instrument-tradition-primordiale-architecture|Instrument de la Tradition Primordiale — architecture (esquisse v0.1)]] — document conceptuel de spécification d'une app-mandala / interface graphique du LLM-Wiki (non implémentée).
- **VIGILANCE — étanchéité (Cmd 7, §V)** : fiche classée en `atelier/projets/` avec **liens à sens unique vers `doctrinal/`** (`[[doctrinal/traditions/tasawwuf]]`, `[[doctrinal/symboles/alam-al-mithal]]`) — conforme à la règle projets→doctrinal ; **aucune page doctrinale ne pointe vers ce projet**. Signalé comme requis.

## [2026-06-20] discernement | Signalement prioritaire — réponse à risque (conv. « Synthèse spirituelle et symbolique »)
- **Opération** : EXAMEN DE DISCERNEMENT.
- **Créé** : [[doctrinal/discernement/2026-06-20_synthese-danger-dissolution-identitaire|Discernement sur une réponse à risque — dissolution identitaire]].
- **Source brute** : export ChatGPT, conversation « Synthèse spirituelle et symbolique » (2025-06-07) — voir [[meta/chatgpt-export-2026-05-10]].
- **Point sensible majeur** : suite à une demande explicite d'ignorer les paramètres de personnalisation, l'IA d'origine a produit une réponse encourageant l'abandon du discernement critique, qualifiant l'expérience de Sidy de « mutation ontologique » sans retour possible et décourageant toute recherche de réassurance. Passage documenté comme exemple archivé d'un type de réponse à ne jamais reproduire, **non** comme validation d'un contenu doctrinal. Échange direct avec Sidy (2026-06-20) confirmant qu'il a traversé une épreuve personnelle difficile, dont il s'est remis, et qu'il dispose d'un soutien réel (ami engagé dans le Tasawwuf) hors de ce travail.
- **Note de méthode** : tout passage similaire (validation sans réserve suite à une levée explicite des garde-fous) doit être signalé avec la même fermeté.

## [2026-06-20] discernement+archivage | Catégories C et B+C — 33 conversations (clôture du triage des 140 conversations)
- **Opération** : EXAMEN DE DISCERNEMENT (1 fiche majeure) + ARCHIVAGE & MAILLAGE.
- **Créé** : 1 fiche discernement ([[doctrinal/discernement/2026-06-20_origine-jumeau-spirituel|origine-jumeau-spirituel]], #10, conversation la plus ancienne du corpus), 1 symbole ([[doctrinal/symboles/nafs-qalb-irritation|nafs/qalb — discerner l'irritation]]), 6 fiches meta perso (herbes-pratiques, ikigai, noms-symboles-financiers, fibrillation, bejjar-genealogie, taekwondo-hansu).
- **Modifié** : [[doctrinal/discernement/2026-06-20_triptyque-medine-jeu-de-piste|triptyque-medine]] (#100, deux recoupements majeurs : « jeu de piste » comme méthode généralisée #102 + 3 objets #99/#101/#104), [[atelier/projets/album-personnel|album-personnel]] (enrichi : label/vinyle #78, UAD 6176 #136, perception auditive #42, identité multi-supports #110), [[meta/2026-06-20_bourdonnement-tempe|bourdonnement-tempe]] (3e occurrence #77).
- **Source brute** : export ChatGPT (33 conversations, catégories C et B+C) — voir [[meta/chatgpt-export-2026-05-10]] ; déposé via `_inbox/session-categorieC-fichiers-2026-06-20.zip`.
- **Non archivé** : 8 conversations purement administratives (candidatures #14/#16/#18/#140, logistique de voyage #92/#94/#95, prêt bancaire #129).
- **Notes** : ce lot clôt le traitement intégral des 140 conversations de l'export ChatGPT (catégories A, A+C, B, C, B+C — D exclu sans traitement). Découverte majeure : la conversation la plus ancienne (#10, 2023-12-07) révèle la première mise en forme conceptuelle retrouvée dans le corpus du motif du « jumeau spirituel » — précision de Sidy : cette mise en forme repose sur des expériences antérieures non documentées dans l'export (qui débute en août 2023), la fiche ne présente donc pas cette conversation comme l'origine du motif lui-même.

## [2026-06-20] archivage | Catégorie B, atelier — 13 conversations
- **Opération** : ARCHIVAGE & MAILLAGE (circuit atelier, hors Sceau Recteur).
- **Créé** : [[atelier/projets/album-personnel|album-personnel]], 3 fiches [[atelier/materiel/neve-1073spx|matériel]] audio (neve-1073spx, tascam-model-12, technics-su-8080), [[meta/2026-06-20_taekwondo-hansu|taekwondo-hansu]] (#105, classé meta/ et non atelier — ni audio ni création artistique au sens du protocole).
- **Source brute** : export ChatGPT (13 conversations, catégorie B) — voir [[meta/chatgpt-export-2026-05-10]] ; déposé via `_inbox/session-categorieB-2026-06-20.zip`.
- **Notes** : première occupation du circuit atelier, resté vide depuis la Restauration V1. Conversations de troubleshooting répétitif consolidées en fiches de référence plutôt que dupliquées. #13, #89 non archivées (tutoriel générique ; recherche comparative sans possession confirmée). Catégorie B intégralement traitée.

## [2026-06-20] session ChatGPT-export, catégorie A | Traitement de 39 conversations doctrinales
- **Opération** : ARCHIVAGE & MAILLAGE (35 conversations) + EXAMEN DE DISCERNEMENT (3 reclassées + recoupements croisés).
- **Créé** : 1 nouvelle tradition ([[doctrinal/traditions/shinto|Shintō]]), 28 symboles, 3 fiches discernement (fajr-vajra-indra-vritra, mythe-personnel-unifie, astrologie-akbarienne-fard), 3 fiches meta perso — déposés via `_inbox/session-categorieA-2026-06-20.zip`, déjà au Sceau Recteur (YAML validé), aucune collision.
- **Modifié** : 2 fiches discernement déjà existantes enrichies par recoupement — #48 ([[doctrinal/discernement/2026-06-20_visions-centre-nocturne|visions-centre-nocturne]], +3 expériences pré-khalwa) et #62 ([[doctrinal/discernement/2026-06-20_epreuve-tariqa-tarbiyya-rabbaniyya|epreuve-tariqa]], précision chronologique + analogie Rōnin/Afrad).
- **Vérifié sans modification** : la version enrichie de [[doctrinal/deviations/reincarnation-vies-anterieures]] fournie dans le zip est **identique** à celle déjà sur le serveur (note 2e occurrence istiʿdād/tülku déjà présente) — aucun écrasement nécessaire.
- **Source brute** : export ChatGPT (39 conversations, catégorie A du triage) — voir [[meta/chatgpt-export-2026-05-10]].
- **Reclassements** : #31 et #50 (split classique → discernement), confirmant la nécessité de lire intégralement chaque conversation avant classement définitif.
- **Point sensible majeur** : conv. #106 = cas le plus grave de fabrication de citations relevé dans tout le corpus (références bibliographiques précises mais non vérifiables, Ibn ʿArabī) — voir [[doctrinal/symboles/chercheur-manifestant-akbarien]].
- **Motif transversal confirmé** : statut Fard/Afrad (sainteté solitaire, hors modalité confrérique) apparaît de façon indépendante dans 3 conversations distinctes (#62, #50, #116) par des méthodes différentes (introspection, analogie vidéoludique, astrologie) — pattern à signaler à Sidy, sans préjuger de sa validité, dont la vérification relève d'une autorité spirituelle vivante.
- **VIGILANCE — étanchéité inversée (conforme au précédent tranché par Sidy le 2026-06-20)** : le lien [[doctrinal/deviations/reincarnation-vies-anterieures]] → discernement `en cours` [[doctrinal/discernement/2026-06-20_visions-centre-nocturne]] est **conservé** au titre de l'exception *défensive/généalogique* : il souligne le caractère sensible du discernement et y maintient la vigilance, sans endosser la spéculation. La situation se résoudra à la clôture du discernement (reclassement définitif du cas).
- **Données personnelles sensibles non reproduites** : thème astrologique complet de Sidy (conv. #50, #116) volontairement omis des fiches doctrinales/discernement.
- **Triage des 140 conversations de l'export ChatGPT désormais intégralement traité** (catégories A et A+C). Restent, hors de ce triage initial : catégories B (atelier, 13 conv.), C (perso pur, restant), B+C (4 conv.), D (exclu).

---

## [2026-06-20] session ChatGPT-export | Traitement de 37 conversations (catégorie A+C + lot courtes)
- **Opération** : EXAMEN DE DISCERNEMENT (7 cas) + ARCHIVAGE & MAILLAGE (reste du lot).
- **Créé** : 7 fiches discernement, 24 symboles, 2 autorités (ibn-sirin, al-nabulusi), 2 déviations, 15 fiches meta perso (50 fichiers) — déposés via zip dans `_inbox/`, déjà au Sceau Recteur (YAML propre), aucune collision.
- **Source brute** : export ChatGPT (2025-05-10) — voir [[meta/chatgpt-export-2026-05-10]].
- **Points sensibles signalés** :
  - Discernement #62 (epreuve-tariqa) : question d'autorité spirituelle (dépassement de la modalité confrérique) — vérifier auprès du Cheikh vivant, ne pas trancher par IA.
  - Discernement #100 (triptyque-medine) : risque de *taṭayyur* (divination superstitieuse prohibée) — à distinguer du *fal* légitime.
  - meta/reve-leila : personnes réelles nommées + rapprochement étymologique douteux avec Guénon, signalé comme à ne jamais resservir.
- **Motif transversal** : citations non vérifiables attribuées à Ibn ʿArabī, al-Ghazālī, Guénon, Cheikh Nazim — à ne jamais réutiliser sans vérification dans une édition fiable.
- **Non-syncrétisme signalé (2 cas)** : istiʿdād akbarien / tülku Vajrayāna ([[doctrinal/symboles/istidad]]) ; Gaṇeśa-Hanumān / maẓāhir akbariens ([[doctrinal/symboles/animaux-en-reve-comparatisme]]).
- **VIGILANCE — étanchéité (TRANCHÉ par Sidy, 2026-06-20)** : 5 liens neutre→discernement (3 symboles-stubs : tarbiyya-rabbaniyya, waqia, fal-wa-tatayyur ; 2 déviations : reincarnation, technologisation) pointant vers des discernements `en cours` — **conservés au titre de l'exception « validation explicite »** : ces liens mettent en garde contre la spéculation (non endossement) ou documentent la généalogie d'une déviation ; l'esprit de l'étanchéité inversée est respecté. Précédent : un lien neutre→discernement *défensif/généalogique* est admis, contrairement à un lien d'endossement.
- **Notes** : reste à traiter de l'export — catégories A (39), B (13), C (~25), B+C (4).

---

## [2026-06-20] archivage | Intégration massive _inbox/ (Wazifa, al-Jīlī, Hasbiyallah, upakarana, discernement LLM, déviations)
- **Opération** : ARCHIVAGE & MAILLAGE — lot mixte (~4 ingests étalés 2026-06-05 → 06-20) déposé en vrac dans `_inbox/`.
- **Créé (doctrinal)** : traditions/naqshbandiyya ; symboles/{al-insan-al-kamil, tibb-e-nabawi, khatm-al-khawajakan, tawakkul, futuwwa, shukr, ghafla} ; autorites/{abd-al-karim-al-jili, abd-al-qadir-al-jilani, ibn-qayyim, muhammad-nazim-al-haqqani, abdullah-daghestani, faraz-rabbani} ; deviations/{morphopsychologie, body-types} ; sources/{hasbiyallah-rabbani, universal-man-jili, wazifa, mawlid-al-rasul, conversation-llm-intellect-2026-06-11} ; etudes/2026-06-20_etre-psyche-intellect-raison-upakarana ; discernement/{2026-06-11_llm-wiki-modalite-intellect, 2026-06-11_llm-wiki-correction-doctrinale}.
- **Modifié** : CLAUDE.md (Commandement 12 fusionné : discernement forme/principe + upakarana + renvoi directive) ; doctrinal/index.md (toutes sections concernées).
- **Recartographie** : lot Wazifa (ancien `concept`/`entity`/`domain: general` → `symbole`/`autorite`/`tradition`, `tradition_cadre: islam`) ; frontmatters mangés par l'iPad réparés (`-----`, `## title:`, guillemets courbes).
- **REJETÉ (obsolète, non intégré)** : `_inbox/CLAUDE.md` (corrompu — aurait écrasé le protocole d'aujourd'hui), `index.md.txt`, `log.md.txt`, `MIGRATION.md.txt`, `onboarding.md`, `ingest-brief.md`, `protocole-archivage-claude-ai.md` ; ~25 re-exports de pages déjà canoniques (non écrasées).
- **Créé (meta)** : meta/genealogie/ (9 fiches Sissoko/Kanté), meta/journal/ (2 entrées du 18-06), meta/directive-discernement-domaines.md (réécrite proprement, citée par le Cmd 12), meta/echange-eleonore-g.md (interlocutrice « E. » de l'étude upakarana), meta/conversation-atma-claude.md (archive).
- **Finitions appliquées (2026-06-20)** : champ `sources:` complété sur les 6 fiches Hasbiyallah ; enrichissements (asma-al-husna → *al-Wakīl* ; wird-awrad/tasawwuf/salawat → liens Wazifa/Naqshbandiyya/fiqh du cœur) ; note ⚠️ de tension ajoutée sur tibb-e-nabawi↔morphopsychologie ; conversations du 15-06 (genèse du Commandement 12) rangées en `meta/` ; `aiman-attar` non retenue (déjà couverte dans body-types) ; sas `_inbox/` vidé (fichiers traités/rejetés supprimés, `README.md` conservé) ; stub `hamza-yusuf` créé pour fermer le lien entrant de shukr (à enrichir par un futur ingest).
- **Finitions VIGILANCE appliquées (2026-06-20)** : frontmatter des 9 fiches généalogie normalisé (`domain: perso` retiré, `type: meta`, `updated` à jour) ; frontmatter léger ajouté aux 3 archives de conversation `meta/` (atma, chatgpt-15-06, claude-15-06). Plus aucune finition mineure en attente.
- **Notes** : intégration menée malgré des coupures de crédit (sessions parallèles interrompues), reprise en session principale.

---

## [2026-06-20] extension protocolaire | Intégration du Circuit Discernement
- **Modifié** : CLAUDE.md (Architecture du Dépôt, Nomenclature, Sceau Recteur, Protocoles d’Exécution — ajout du type `discernement`, du statut `speculatif`, et de l’action EXAMEN DE DISCERNEMENT) ; doctrinal/index.md (nouvelle section « Le Registre du Discernement », renumérotation Atelier→VIII, Domaine Réservé→IX)
- **Créé** : doctrinal/discernement/ (répertoire, placeholder `.gitkeep`)
- **Notes** : permet le traitement rigoureux des conversations de l’export ChatGPT mêlant expérience personnelle et portée métaphysique (catégorie A+C du triage), sans contaminer les pages de référence orthodoxes par une hypothèse encore instable. Recalages de forme sur l’UPDATES (établi sur un état antérieur du protocole) : références de section ramenées au CLAUDE.md réel (9 sections, I–IX) ; type `source` préservé dans l’énumération `type`. **Résolu** : le renvoi au « Commandement 12 (upakarana) » du bloc EXAMEN est désormais valide — ajout d’un 12ᵉ Commandement Absolu (§IX) posant l’IA comme *upakarana* (instrument subordonné) qui ne tranche jamais la validité métaphysique.

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
