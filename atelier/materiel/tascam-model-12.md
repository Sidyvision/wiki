---
title: "Tascam Model 12 — table/interface centrale"
type: materiel
tags: [audio, interface, tascam, mastering]
created: 2026-06-20
updated: 2026-08-18
sources: ["[[chatgpt-export-2026-05-10]]", "[[raw/facture-woodbrass-4902304-2025-11-07-tascam-model12]]", "[[raw/Model12_OM_EFS_RevH3]]"]
links: ["[[atelier/materiel/neve-1073spx]]", "[[atelier/materiel/studio-principal]]"]
---

# Tascam Model 12 — table/interface centrale

## Nature de l'appareil

Table de mixage/enregistreur numérique avec interface audio USB, utilisée comme nœud central entre l'iPad (GarageBand/Logic Pro), le [[atelier/materiel/neve-1073spx]], et le monitoring.

## Points d'usage retenus des conversations sources

- Possède un chemin analogique réel (préamplis et circuits sommateurs propres), ce qui donne une sensation de son plus dense que l'écoute purement numérique dans GarageBand — constat fait directement par Sidy.
- **Routage type** : sortie dédiée de Logic Pro/GarageBand (jamais la sortie Master) → entrée ligne du Model 12 → vers le Neve si traitement souhaité → retour en entrée ligne (jamais entrée micro, pour éviter un cumul de préamplis) → nouvelle piste audio en enregistrement.
- **Mastering avec le Model 12** : exporter le morceau sans limiteur (WAV 24 bits, -6 dB de marge), le repasser dans la chaîne analogique du Model 12, viser une cible de **-14 LUFS intégrés / True Peak -1 dB** pour compatibilité streaming (Spotify, Apple Music, YouTube) — ne plus chercher à « écraser » le mix comme à l'époque du CD, car les plateformes renormalisent un signal trop fort.

## Identification et acquisition

- **Modèle** : Tascam Model 12
- **Date d'achat** : 2025-11-07
- **Lieu d'achat** : Woodbrass.com
- **Prix TTC** : 639,00 €
- **Facture** : n° 4902304, PDF conservé en `raw/facture-woodbrass-4902304-2025-11-07-tascam-model12.pdf`
- **Garantie** : 3 ans

## Spécifications techniques (extraites du manuel constructeur)

- **Entrées micro** (1–6, 7, 9) : XLR-3-31, max +10 dBu, nominal −8 dBu, gain 0–50 dB, impédance 1,8 kΩ
- **Entrées ligne/inst** (1–6) : jack 6,35 mm TRS, max +22 dBu (ligne) / 19,8 dBV (inst), nominal +4 dBu / 1,8 dBV, gain −10 à +40 dB, impédance 22 kΩ (ligne) / 1 MΩ (inst)
- **Entrées ligne** (7/9 L, 8/10 R) : jack 6,35 mm TRS, max +22 dBu, nominal +4 dBu, gain −20 à +30 dB, impédance 18 kΩ
- **Inserts** (1–2) : jack 6,35 mm TRS (send/return), max entrée +18 dBu, max sortie +18 dBu
- **Enregistrement** : WAV (BWF) 44,1/48 kHz, 16/24 bit, max 12 canaux (10 + 2 stéréo)
- **Support** : cartes SD/SDHC/SDXC (classe 10 ou supérieure)
- **Bluetooth** : v5.1, classe 2 (~10 m), profils A2DP, codecs SBC/AAC, protection SCMS-T
- **Performance audio** :
  - Rapport signal/bruit : 103 dB (pondération A)
  - Distorsion harmonique totale : 0,003 %
  - Réponse en fréquence : 20 Hz – 20 kHz (+0,3/−0,7 dB)
  - Diaphonie : −95 dB (entre canaux et entrée/sortie)
  - Gain maximal : 74 dB (MIC → MAIN), 54 dB (MIC → INSERT)
- **Alimentation** : adaptateur PS-M1524, AC 100–240 V, DC 15 V / 2,4 A
- **Consommation** : 16 W
- **Dimensions** : 343 × 98,8 × 360 mm (avec flancs) / 315 × 98,8 × 360 mm (sans flancs)
- **Poids** : 4,3 kg
- **Interface USB** : USB 2.0 HIGH SPEED, type C, jusqu'à 24-bit / 48 kHz
- **Pilotes** : ASIO 2.0, WDM (Windows) ; Core Audio (Mac) ; iOS 11+
- **MIDI** : IN/OUT, DIN 5 broches, format standard

## Historique maintenance

*Aucun incident consigné à ce jour. Section prête à recevoir les entrées.*

---

## Liens

- [[atelier/materiel/neve-1073spx]] — appareil inséré via cette table.
- [[atelier/materiel/studio-principal]] — fiche-hub de l'espace d'atelier.
