---
title: "Plan — étage de mesure audio et banc de calibration de la chaîne analogique"
type: outillage
tags: [atelier, rd, audio, mesure, ebur128, ffmpeg, analogique, calibration, pedagogie]
created: 2026-09-16
updated: 2026-09-16
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/veille/2026-09-16_landr-pont-entrant-partage-et-api]]"
  - "[[atelier/materiel/tascam-model-12]]"
---

# Plan — étage de mesure audio et banc de calibration de la chaîne analogique

> **Statut** : **plan accepté par Sidy le 2026-09-16** (session Discord
> `#infrastructure`), **aucune exécution engagée**. Rien n'a été installé, aucun code
> n'a été écrit, aucune dépense n'a été ouverte. La reprise se fait à son feu vert, et
> commence par le point marqué *Reprise* en fin de fiche.
>
> **Ce que cette fiche est** : la forme consultable à froid d'un plan accepté
> verbalement, avec ses mesures de fondation, ses réserves non éprouvées et ses
> questions ouvertes — pour que la session suivante reprenne sans reconstituer.
> **Ce qu'elle n'est pas** : un `plan.md` de chantier (aucun identifiant de registre
> n'est ouvert, voir §7).

## 1. Mesures de fondation (faites le 2026-09-16, instruments nommés)

- **Le kit de mesure est déjà sur le serveur** : `ffmpeg 6.1.1-3ubuntu5` avec les
  filtres nécessaires — `ebur128` (LUFS intégrés, LRA, crête vraie), `astats` (crête,
  RMS, facteur de crête, offset continu, plancher de bruit, canal par canal),
  `aspectralstats` (centroïde, planéité, entropie), `stereotools` (équilibre M/S,
  largeur), `aphasemeter` (corrélation de phase), `silencedetect`, `acrossover`
  (analyse bande par bande), `showspectrumpic` / `showwavespic`, `loudnorm`,
  `volumedetect`. **Rien à installer, rien à acheter, aucune dépendance tierce.**
- **Le serveur n'a pas de carte son — c'est une machine virtuelle** : `/dev/snd` réduit
  à `seq` et `timer`, `lsusb` ne montrant que du virtuel (QEMU), aucun outil de capture
  installé. **Conséquence structurante : notre mesure est « par fichier », jamais en
  direct.** Le direct — alignement de niveau, double vérification avant tout signal
  chaud vers la bande ou les moniteurs — reste au studio, sous la main de Sidy ; la
  mesure *après coup* vit ici.
- **Nomenclature de styles** : MusicBrainz expose un vocabulaire **ouvert, sans clé** —
  **2 202 genres** listés, identifiants stables (deux refus « serveur occupé » avant
  une réponse 200, même jour). Une **convention documentée**, donc manipulable, citable
  et révisable — pas une vérité.
- **Tascam Model 12** (fiche `atelier/materiel/tascam-model-12.md`, tirée du manuel
  constructeur) : **aucune interface réseau** ; USB 2.0 type C jusqu'à 24 bits/48 kHz
  (ASIO 2.0 / WDM pour Windows, Core Audio pour macOS, iOS 11+ — **Linux non
  documenté**) ; **enregistreur autonome** WAV (BWF) 44,1/48 kHz, 16/24 bits, jusqu'à
  **12 canaux**, sur carte SD. Bluetooth A2DP = entrée de flux vers la table, pas un
  chemin vers nous.

## 2. Le plan accepté, dans l'ordre

1. **① Étage de mesure** — rendre à tout fichier audio un **jeu de mesures
   normalisées** : LUFS intégrés, LRA, crête vraie, crête et facteur de crête par
   canal, offset continu, plancher de bruit, pente et centroïde spectraux, largeur et
   équilibre M/S, corrélation de phase, durée. Livrable : un script déterministe (et,
   plus tard, son exposition en serveur **MCP** dans le moule du serveur `wiki`,
   §VIII.11 du protocole racine). **Commence ici.**
2. **② Banc de calibration de la chaîne analogique** — le protocole, écrit **avant**
   d'être exécuté : niveau (le `0 VU` étalonné), réponse en fréquence en boucle
   analogique, distorsion, plancher de bruit, appariement des canaux, ce que la bande
   fait au haut du spectre, contrôle d'azimut. **Limite dite** : la boucle de
   convertisseurs ne peut être isolée que par un **aller-retour témoin** enregistré au
   studio ; nous mesurons donc ce que *l'ensemble* chaîne + conversion a fait, et le
   témoin permet de retrancher la part du convertisseur. Tout cela suppose un
   **enregistrement fait au studio** et apporté ici.
3. **③ Table d'enveloppes de styles** — une fiche par famille, chaque cellule
   **sourcée ou marquée `to-source`**, construite par **mesure sur un corpus de
   référence choisi par Sidy** ; l'écart entre sa prise et la référence rendu en
   nombres. Aucune passe de masse, aucune cellule remplie d'office.
4. **④ Ingester d'entrant et épreuve de moteur libre** — l'ingester éprouvé le
   2026-09-16 (copie d'écoute 192 kbps, sans identifiant, cf. fiche de veille liée) ;
   et l'épreuve en sandbox de `matchering` (GPL-3.0, dépôt actif, paquet PyPI 2.0.6 du
   2022-10-19, `requires_python >= 3.8`) sur la même piste qu'un master existant, avec
   comparaison chiffrée. **Voie basse** : `matchering` tourne chez nous — pas de clé,
   pas d'exposition d'un master non publié.

**Ce que Sidy a explicitement écarté, ce jour** : rien du plan ; et il a écarté le test
du réglage de partage LANDR (« ce ne sont encore que des ébauches que j'avais testé »).

## 3. Clause de discernement — ce que la machine fait et ne fait pas

Énoncée en session et acceptée : **je décris, Sidy tranche.**

- Ce qui m'est accessible : la **nomenclature** des genres (données ouvertes) et les
  paramètres mesurables qui distinguent les familles (tempo, densité de transitoires,
  contenu bas du spectre, pente spectrale, largeur stéréo, dynamique, cible de niveau,
  forme des sections).
- Ce qui ne m'est **pas** accessible : l'écoute, l'intention, le goût, la hiérarchie
  voulue entre les éléments, le « ça sonne juste », et **tout verdict esthétique** —
  quel que soit le moteur (Cmd 12 du protocole racine : le verdict appartient à
  l'utilisateur ou à une autorité citée, jamais à l'IA).
- **Piège nommé** : un système qui prétend « tenir » un style tend à **moyenner** — il
  produit le centre du genre, c'est-à-dire du pastiche. L'outillage doit donc servir la
  comparaison, jamais engendrer le choix.
- **Marquage** : ce qui n'est pas sourcé se marque `to-source` ; ce qui n'est pas
  mesuré se déclare comme tel.

## 4. Contraintes et réserves non éprouvées

- **Linux + Model 12** : Tascam ne documente que ASIO/WDM, Core Audio et iOS. La
  reconnaissance en **classe USB Audio** sur Linux est **probable et non vérifiée** :
  elle se mesure (brancher, regarder, conclure), elle ne s'assume pas.
- **Boîte de capture au studio** (mini-ordinateur sur Tailscale, Model 12 en USB,
  transfert de **fichiers**) : piste évoquée, **non éprouvée**, non décidée.
- **Plafond de conversion** : le Model 12 s'arrête à **48 kHz** — toute ambition de
  mesure ou d'archivage à plus haute fréquence passerait par un autre convertisseur.
- **Pas de direct** : le serveur ne peut ni capturer ni lire de l'audio ; toute
  mesure suppose un fichier déjà constitué.

## 5. Question ouverte, bloquante, et unique

**Où vit physiquement l'hôte de virtualisation ?** C'est ce qui décide si les chemins
« carte SD » et « USB vers le poste du studio » suffisent, ou si une boîte de capture
au studio est la seule voie possible.

## 6. Chemin par défaut proposé en attendant

**La carte SD** : le Model 12 enregistre seul (WAV/BWF, jusqu'à 12 canaux), la carte
vient au serveur, la mesure suit. Zéro câble, zéro logiciel, zéro dépendance, et cela
fonctionne dès aujourd'hui sans toucher à l'infrastructure.

## 7. Ce qui n'est pas décidé (et ne le sera pas sans verdict)

- **Aucune ligne de chantier n'est ouverte** : si un porteur est voulu au registre
  (`OUT-…`), l'ajout déclenche le recomptage §0 de `atelier/rd/registre-chantiers.md`,
  et se fait sur ordre explicite.
- **Lieu des binaires audio** (fichiers d'éprouve, copies d'écoute) : `raw/` (immuable,
  hors git) ou hors dépôt — non tranché. Le sas `_inbox/` ne reçoit que de la matière
  rédigée.
- **Adoption de `matchering`** : nulle. Épreuve en sandbox seulement, et la licence
  **GPL-3.0** est à considérer avant toute intégration dans un objet distribué.
- **Le greffon LANDR Mastering Plugin** : écarté (met leur moteur dans le DAW, ne
  complète pas l'infrastructure, et va contre la finalité de souveraineté du pôle).

## 8. Reprise

**Point de reprise pour la prochaine session** : ouvrir **①**, l'étage de mesure, par
un cas réel — Sidy dépose **un WAV de sa main** dans le sas ; le script rend la fiche
de mesure complète devant lui, avant qu'aucune autre pièce ne soit construite. Rien
d'autre n'est entrepris avant que ce premier rendu soit vu et corrigé.
