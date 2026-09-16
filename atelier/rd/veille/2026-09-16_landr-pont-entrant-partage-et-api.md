---
title: "LANDR — pont entrant : partage, flux et API (relevé du 2026-09-16)"
type: experience
statut_experience: exploratoire
tags: [veille, landr, mastering, api, partage, pont-entrant, souverainete]
created: 2026-09-16
updated: 2026-09-16
sources:
  - "https://api.landr.com/mastering/openapi/v1/openapi.json"
  - "https://api.landr.com/mastering/openapi_redoc/index.html"
  - "https://www.landr.com/pro-audio-mastering-api"
  - "https://support.landr.com/hc/en-us/articles/115009734288-My-track-library"
  - "https://support.landr.com/hc/en-us/articles/36101701002135-What-are-library-and-file-storage-limits"
  - "https://support.landr.com/hc/en-us/articles/4405587296151-What-if-I-need-the-same-master-in-a-different-file-format"
  - "https://support.landr.com/hc/en-us/articles/18342363971479-What-are-the-system-requirements-to-use-LANDR-Mastering-Plugin"
  - "https://www.landr.com/desktop-app"
links:
  - "[[atelier/rd/veille/index]]"
  - "[[atelier/rd/veille/registre]]"
---

# LANDR — pont entrant : partage, flux et API (relevé du 2026-09-16)

**Circonstance.** Question de Sidy en session (`#infrastructure`, 2026-09-16) : « est-ce
que LANDR prévoit un accès serveur direct ? », précisée ensuite en **« je voulais un pont
entrant »** — faire descendre sur le serveur des morceaux déjà déposés dans son compte
LANDR. Un lien de partage public a été fourni pour l'éprouve (piste « 01 - Wake up »).

**Avertissement de lecture.** Tout chiffre ci-dessous est une **photographie datée**
(2026-09-16, 02:00–02:20 UTC) avec son instrument. Aucun identifiant n'a été employé,
aucune session ouverte, aucun contournement tenté : seuls ont été sollicités le lien de
partage fourni et les points d'entrée que ce lien expose publiquement.

## 1. Le compte et l'API sont deux portes distinctes

C'est le fait principal, et il commande tout le reste.

- L'**API** de LANDR (`https://api.landr.com`, titre « LANDR Mastering Api », version
  `v1`, OpenAPI 3.0.0, spécification lue et conservée le 2026-09-16, sha256 court
  `14d4d164…`, 40 675 octets) expose **huit chemins, dix opérations** : créer un master
  (`POST /v1/master/single`), créer une pré-écoute (`POST /v1/preview/single`), lire un
  statut, lire une URL de téléchargement, et quatre opérations de webhook
  (`POST|PUT|GET /v1/webhook`, `POST /v1/webhook/secret`).
- **Aucune de ces opérations ne touche au compte** : il n'existe ni listing de
  bibliothèque, ni lecture d'un master existant, ni accès aux crédits ou aux releases.
  L'API **crée du neuf à partir d'un `inputUri`** ; elle ne relit jamais l'existant.
- Authentification : une seule **clé d'en-tête** `x-landr-mastering-api-key`. Pas
  d'OAuth, pas de compte. (Le champ `flows` que la spécification porte sous un schéma
  `apiKey` est un **artefact de génération**, non un flux d'autorisation : un schéma
  `apiKey` n'en admet pas.)
- Accès commercialement gardé : obtention par **« Contact sales »**, tarif annoncé **à
  partir de 2,50 $/titre**, remise au volume ; page cadrée **partenaires/plateformes**.
  Le centre d'aide ne porte **aucun article API** (recherche exacte « API » → 0
  résultat) ; l'inscription RapidAPI existe mais renvoie vers la même page commerciale —
  **pas de clé en libre-service**.
- Modèle **pull** : `inputUri` est un URI, et l'état `downloading` de la machine à états
  (« The input file is being downloaded on our server ») confirme que **LANDR vient
  chercher le fichier**. Aucun point d'entrée de téléversement n'existe.
- Débits annoncés : **50 créations/heure** ; statut et téléchargement **100
  requêtes/minute**. Un master **expiré** rend `410 Gone` — la copie chez LANDR n'est pas
  un archivage.
- Posture réseau mesurée : une requête non authentifiée sur `api.landr.com/v1/*` reçoit
  **403 AccessDenied** (AmazonS3/CloudFront, POP `FRA56-P11`, 2026-09-16 01:52 UTC) ;
  seuls les chemins de documentation sont publics — `…/mastering/openapi/v1/openapi.json`
  → HTTP 200, portail de documentation → HTTP 200.

## 2. Ce que le lien de partage donne, sans compte (mesuré)

- La page s'ouvre **anonymement** : projet « 01 - Wake up », propriétaire
  Sidy-Lamine/Sidyvision, fichier « 01 - Wake up.mp3 », badges **MP3 · High · Warm ·
  MASTER**, durée affichée **02:23**. HTML servi : 6 189 octets, sha256 `dcd5e245…`.
  *(Lien de partage volontairement tronqué ici — `…/projects/24ba227c-…?publicToken=d675496d-…&sharing` :
  un jeton de partage est une **capacité**, il ne se recopie pas dans un fichier versionné.)*
- **Mécanisme de lecture anonyme**, extrait de leur propre bundle applicatif : un
  en-tête `X-LANDR-PUBLIC-TOKEN`, alimenté par le paramètre `publicToken` du lien quand
  aucune session n'existe.
- **Le fichier audio est tirable par le serveur, sans identifiant** :
  `https://projects.landr.com/assets/432a7dae-061c-4015-ab5c-6a9100015464/stream.mp3`
  → HTTP 200, **3 425 637 octets**, sha256 `57681f467146a5fb1df6c0382bd79a59…`
- Mesures `ffprobe` : **MP3 CBR 192 kbps**, 44,1 kHz, stéréo, **142,707 s** (02:23,
  conforme à l'affichage). Métadonnées du fichier côté LANDR : `intensity: High`,
  `productionStyle: PS1`, `genre: AMBIENT`, encodeur `Lavc58.13` (le fichier est
  **ré-encodé par leur chaîne**).
- Mesure de niveau (`ffmpeg -filter_complex ebur128`, EBU R128) : **-7,4 LUFS**
  intégrés, LRA **2,5 LU**, **crête vraie +0,3 dBFS** — donc au-dessus de 0 dBFS, ce
  qui est un fait de chaîne à retenir pour tout passage ultérieur sur bande.
- **Ce fichier est une copie d'écoute, pas le master livrable.** La documentation d'API
  de LANDR donne le master MP3 **livrable à 320 kbps** ; le flux mesuré est à **192**.
  Inférence, pas mesure directe : à confirmer en comparant avec le fichier téléchargé
  depuis le compte (taille, empreinte, niveau).
- **L'URL de flux ne vérifie pas le jeton** : elle est indexée sur l'UUID de la piste
  seule (UUID bidon → **404**, sans jeton ni cookie sinon 200). Qui connaît l'UUID tient
  le fichier.

## 3. Ce que le lien de partage refuse : le master livrable (mesuré)

Trois observations concordantes, plus les contrôles qui les rendent concluantes.

1. Bouton **« Download all »** de la page de partage → **redirection vers
   `accounts.landr.com/oauth2/register?…`** : compte exigé.
2. Requête de téléchargement — `query AssetDownloadUrl` → `chatAssetDownloadUrl`
   (texte extrait de leur bundle) — présentée **avec** le jeton public :
   **`UNAUTHENTICATED`**.
3. Le **modèle de permissions tel que leur serveur le déclare à un visiteur anonyme**
   porteur du jeton (`query ProjectPage`) :
   `canView: true`, **`canDownload: false`**, `canUpload: false`, `canAddComment: false`,
   `canEdit: false`, `canPinAsset: false`, `canAnnotate: false`.

**Épreuve des contrôles** (le refus n'est pas un artefact de la sonde) :

- Même requête de métadonnées **avec** le jeton → données renvoyées
  (`chatAssetById` rend l'identifiant) ;
- **sans** le jeton → `ShareableLinkNotFound` (code `API_ERROR`,
  `…/errors/ShareableLinkNotFound`, trace `00-aee1740c…`) — le jeton est bien ce qui
  ouvre ;
- requête triviale (`query { __typename }`) → **200 avec et sans en-tête** : le canal
  répond, ce n'est donc pas un refus de transport.

Conclusion : **le jeton ouvre la lecture, précisément pas le téléchargement.** Deux
verrous indépendants (permission à `false` pour l'anonyme, et résolveur qui exige une
session authentifiée).

## 4. Le pont entrant, tel qu'il se présente

- **Étage 1 — écoute, automatisable dès maintenant, sans identifiant** : à partir d'un
  lien de partage, un script déterministe peut descendre la copie 192 kbps de chaque
  piste partagée, et la mesurer (`ffprobe`, `ebur128`). Zéro dépense, zéro identifiant
  sur le serveur, rien à négocier.
- **Étage 2 — master livrable : fermé.** Voies sanctionnées : (a) le **geste humain** —
  téléchargement depuis le compte vers le sas `_inbox/`, le serveur prenant le relais
  ensuite ; (b) la **clé d'API partenaire**, qui ne rapatrie rien puisqu'elle **crée**.
- **Hypothèse non éprouvée, écartée par Sidy** : les privilèges de partage (« viewing
  and downloading ») pourraient, s'ils sont activables, faire basculer `canDownload`
  pour un visiteur anonyme. Le test était prêt (une bascule de réglage, deux sondes) ;
  **Sidy l'a écarté** le 2026-09-16 : « ce ne sont encore que des ébauches que j'avais
  testées ». L'hypothèse reste donc **ouverte et non tranchée** : les deux lectures — un
  réglage de partage en « écoute seule », ou un refus de politique pour tout visiteur
  anonyme — **ne sont pas séparées par la mesure**.
- **Ce qui n'a pas de voie serveur du tout** : la **bibliothèque entière**. Ni API, ni
  client Linux — l'application de bureau est **macOS 13+ / Windows 10 x64**, et le
  centre d'aide ne connaît pas « Linux » (0 résultat). Notre serveur, Ubuntu sans écran,
  ne peut pas l'exécuter.

## 5. Conservation côté compte (contexte, mesuré au centre d'aide)

- Bibliothèque : **4 Go** offerts à l'ouverture, **jusqu'à 500 Go** selon l'abonnement ;
  les fichiers distribués par leur service de distribution ne comptent pas dans le quota
  (article à jour du 2026-08-24). LANDR est un **espace de travail**, pas une archive.
- Un même master se retélécharge dans un autre format sans consommer de crédit
  supplémentaire **vers le bas** (MP3 depuis WAV) ; **vers le haut**, un crédit de plus
  est requis (article à jour du 2026-07-13).
- Le plugiciel de mastering (`LANDR Mastering Plugin`) est un **greffon local** :
  macOS 10.14+ / Windows 10+ (64 bits), VST3/AU/AAX, essai de 3 jours **filigrané**
  (articles à jour des 2026-09-02 et 2026-09-12). Il ne concerne pas le serveur.

## 6. Non mesuré, non éprouvé

- Aucun appel d'API authentifié : pas de clé, donc **aucun master produit**, aucun prix
  réel, aucune confirmation du comportement des webhooks.
- La nature exacte du **flux 192 kbps** (transcodage du master ou copie de l'original
  téléversé) n'est **pas établie** ; seule l'inférence 320 kbps ↔ 192 kbps est avancée,
  et elle se vérifie en comparant avec le fichier du compte.
- La sonde anonyme n'a pas non plus testé un **autre** partage ; le résultat
  `canDownload: false` vaut pour le lien éprouvé, à cette date.
- Rien n'a été écrit dans le dépôt à partir de ces mesures ; la copie d'éprouve vit hors
  dépôt, dans `/root/sandbox-rd/landr-inbound/` (3 425 637 octets, sha256 `57681f46…`).

## 7. Rapprochement dépôt

- **Aucun chantier ouvert** ne portait le mastering ni la distribution : les lignes de
  `atelier/rd/registre-chantiers.md` (§1–§7) ne les nomment pas, et le mot « LANDR »
  était absent du dépôt hors `textes/`. Il s'agit donc d'une **ouverture neuve**, non du
  remplissage d'une case existante.
- **Tension de fond, signalée et non tranchée** (Cmd 12) : la finalité du pôle `rd/` est
  l'**émancipation des intermédiaires de service tiers**. Or la voie automatique
  offerte par LANDR passe par une **clé commerciale** et par l'**exposition de nos
  masters à une URL publique** que leurs serveurs viennent chercher ; la voie gratuite
  passe par un **fichier de qualité d'écoute**. Le pont entrant « propre » n'existe, en
  l'état, ni chez eux ni chez nous.

## 8. Conséquence pratique retenue

**Le compte est la porte ; l'API est une autre porte ; la nôtre s'ouvre sur l'étage 1.**
Tant qu'un quatrième fait ne change pas la donne, l'entrant passe par le geste humain
vers `_inbox/` pour les masters, et peut passer par le script pour l'écoute et la
mesure — ce dernier restant à instruire comme outillage, sur verdict.
