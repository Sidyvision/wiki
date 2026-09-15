---
title: "Index de conversion — Curt Jaimungal, « Consciousness, Irreducibility, and the Local to Global » (transcription ASR)"
type: ressource
tags: [transcription, asr, jaimungal, theories-of-everything]
created: 2026-09-15
sources:
  - "raw/sources/jaimungal-consciousness-irreducibility-local-to-global-q2Zgp2EhSk8.mp3"
---

# Curt Jaimungal — *Consciousness, Irreducibility, and the Local to Global*

Conférence plénière de Curt Jaimungal (chaîne *Theories of Everything*), suivie d'une
séance de questions. Vidéo YouTube `q2Zgp2EhSk8`, titre et chaîne confirmés par l'API
oEmbed de YouTube le 2026-09-15 ; 56 min 14 s. **Identifiée par Sidy** comme la vidéo
qu'il avait en mémoire (« je crois qu'il s'agit de cette vidéo »). Date de mise en ligne
et nom de la conférence : `to-source` (non accessibles depuis le serveur ; la
transcription nomme Matt Segall comme hôte).

## Chaîne

1. **Accès** : YouTube refuse l'adresse du serveur (« Sign in to confirm you're not a
   bot ») ; Piped et Invidious aussi. Audio obtenu par **notube** (consigne de Sidy),
   piloté en ligne de commande par ses trois appels (`recover_weight.php`,
   `recover_file.php`, `download.php`) : mp3 de 81 Mo, conservé dans `raw/sources/`
   (hors git).
2. **Transcription locale** : `atelier/rd/outillage/transcrire-audio-whisper.py`,
   faster-whisper 1.2.1, modèle `small`, int8 sur CPU, beam 1, filtre VAD, langue `en`,
   **tranches de 10 minutes**. Deux premiers essais tués par le noyau (« Out of memory »,
   3,1 Go puis 2,7 Go sur 3 Go) : l'audio décodé d'un seul tenant ne tenait pas en
   mémoire ; le découpage en tranches a été ajouté à l'outil. 982 segments, 13,2 min de
   calcul.
3. **Versement** : `verser-dossier-textes.py`, identique octet pour octet à sa source.
   Aucune correction.

## Qualité — avant de citer

**Transcription automatique, non relue.** Noms et termes techniques défigurés, conservés :
« Kurt Geimungle » (Curt Jaimungal), « Gertl's theorem » / « Girdle's theorem » (Gödel),
« Saraitis paradox » (sorites), « Steve's theory » (sheaf theory), « piano axioms »
(Peano), « Tecmarc » (Tegmark), « Veltan Shao'un » (*Weltanschauung*), « to rock and
boil » (Turok et Boyle). Les **coupures de tranche** (00:10:00, 00:20:00 … 00:50:00)
peuvent tomber au milieu d'un mot — visible à 00:10:00 (« one c- / concept »). Toute
citation se vérifie sur l'audio.

## Repères (horodatages de la transcription)

| Temps | Contenu |
|---|---|
| 00:00:00 | Présentation de l'orateur |
| 00:00:55 | Un texte « whiteheadien » qui s'avère être Gemini décrivant une machine à laver |
| 00:01:53 | « Erreurs que font les intellectuels » (dont : « les Védas l'avaient dit ») |
| 00:11:05 | L'« éléphant inversé » : accord local, pas d'objet global |
| 00:12:04 | **Son graphe des théories** (« my landscape of theories of everything ») |
| 00:14:51 | Trois sens de l'irréductibilité de la conscience |
| 00:34:04 | Les types de théories du tout, A à E |
| 00:38:00 | Concepts « phénoménalement épais » — dont la compréhension prêtée aux LLM |
| 00:40:19 | Conseils aux chercheurs |
| 00:45:12 | Questions |
| 00:55:12 | Fin ; début de l'orateur suivant, coupé |
