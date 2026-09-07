---
title: "OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : spécification"
type: outillage
chantier: OUT-08
tags: [atelier, rd, outillage, ocr, arabe, chantier, spec]
created: 2026-09-02
updated: 2026-09-07
sources: []
links:
  - "[[atelier/rd/registre-chantiers]]"
  - "[[atelier/rd/outillage/out-08-ocr-arabe-futuhat/intent]]"
  - "[[atelier/rd/outillage/gabarit-triptyque-chantier]]"
---

# OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : spécification

> Chantier de qualification, non de production logicielle : ce `spec.md` compare
> des pistes sur un échantillon commun (page 300 du PDF source), comme fixé par le
> « signe de réussite » de `intent.md`, plutôt que de spécifier le comportement d'un
> outil à construire — aucune des pistes testées à ce jour n'a franchi le seuil qui
> justifierait d'écrire un script.

## Échantillon commun

`raw/Al Futuhat Al Makkiyya - maymaniya_p1.pdf`, page 300 (choix arbitraire, DOC-07
portait sur un échantillon différent, ligne 5000 du `.md` produit). Extraction via
`pdftoppm -f 300 -l 300 -r <dpi> -png`, dans un bac à sable `/tmp`, jamais committé.

## Pistes comparées

### Piste 1 — réglage de paramètres Tesseract (DPI, `--psm`)

**Comportement observé** : DPI 300 → 400, `--psm` 3 (défaut) / 4 / 6 : les quatre
sorties recomposent les mots au hasard de la même façon. Aucune variante ne réduit la
corruption structurelle relevée en DOC-07.

**Verdict** : négatif. Le réglage de paramètres seul ne touche pas la cause du défaut.

### Piste 2 — `--oem 1` (moteur LSTM seul) contre le défaut

**Comportement observé** : `tesseract page-300.png out --oem 1 --psm 3` produit une
sortie **strictement identique** (`diff` vide) à `tesseract page-300.png out --psm 3`
sans `--oem`. Cause : `/usr/share/tesseract-ocr/5/tessdata/ara.traineddata` ne
contient pas les composants du moteur legacy (confirmé par l'erreur de Tesseract à
la tentative de `--oem 0` : *"Tesseract (legacy) engine requested, but components
are not present"*) — le moteur par défaut (`--oem 3`, « les deux si disponibles »)
retombe donc déjà sur LSTM seul, faute d'alternative installée.

**Verdict** : négatif, et **sans objet** — il n'existe pas ici de choix de moteur à
faire : un seul est présent. Piste épuisée sans qu'aucune installation n'ait été
nécessaire pour la clore.

### Piste 3 — bibliothèques de conversion documentaire (`markitdown`, `anydoc`)

Examinée le 2026-09-02, `anydoc` sur signalement de Sidy. **Piste close, et non
pas seulement négative** : elle est fermée par le protocole, pas par la mesure.

| | OCR local | Chemin OCR proposé |
|---|---|---|
| `markitdown` (Microsoft) | aucun | plugin → API LLM Vision (clé OpenAI) ou Azure |
| `anydoc` (Firecrawl) | aucun | `--ocr hosted` → API Firecrawl Parse |

`markitdown` a été **exécuté** sur un extrait de la Maymaniyya : **0 octet**. Il
repose sur `pdfminer`/`pdfplumber`, qui ne lisent que du texte déjà encodé.
`anydoc` n'a pas eu besoin de l'être, sa documentation étant explicite — *« does
no OCR, so a PDF with scanned or image-only pages fails with `NeedsOcr` »*.

Les deux échouent **au même endroit et pour la même raison** : ce sont des
convertisseurs de documents *déjà porteurs de texte*, non des moteurs d'OCR. Leur
option OCR est un renvoi vers un service tiers — et pour `anydoc`, *« the whole
document goes, since Parse has no page selection »* : les 779 pages du tome
partiraient chez un tiers. Contraire au §VIII (déterministe, sans LLM, sans
réseau).

**Verdict** : la piste « OCR cloud » de `intent.md` ne bute pas sur une dépense
ou un paquet manquant, mais sur le protocole. **Ne pas re-tester ces outils sur
un scan** sans élément neuf. Ils restent en veille pour les formats nativement
structurés (`.docx`, `.epub`, `.pptx`, `.xlsx`) — usage **non éprouvé ici**, à
mesurer sur pièce le jour où un tel fichier arrivera, jamais à inscrire sur la
foi d'une documentation.

## Critères d'acceptation (pour une piste qui franchirait le seuil)

1. Sur la page 300, un échantillon de texte reconnu redevient lisible mot à mot
   (comparaison visuelle contre l'original scanné) — pas seulement « moins pire ».
2. Le résultat se reproduit sur au moins une deuxième page prise ailleurs dans le
   tome (le défaut pourrait ne pas être uniforme, cf. `intent.md`, dernier point
   ouvert).
3. Le coût de la piste (paquet à installer, dépense, temps de traitement sur 779 p.)
   est nommé et présenté à Sidy avant tout essai à l'échelle du tome (Cmd 13).

Aucune piste testée à ce jour n'atteint le critère 1.

## Cas limites

Sans objet à ce stade — aucune piste n'a produit de sortie exploitable à comparer
finement (faux positifs, caractères ambigus, etc.).

## Ce qui reste `to-source`

Sans objet : ce chantier ne produit aucune fiche doctrinale (rappel `intent.md`,
Cmd 5) — rien à sourcer ici.

## Verdict de cette spécification

Les deux pistes ne demandant **aucune installation** sont épuisées, toutes deux
négatives. Une troisième — les bibliothèques de conversion documentaire
(`markitdown`, `anydoc`) — est **close par le §VIII** et non par la mesure :
aucune ne fait d'OCR local, toutes deux renvoient vers un service tiers.

Restent donc, parmi les pistes de `intent.md` : le **prétraitement d'image** et
un **moteur alternatif** installé localement. L'une et l'autre supposent un
paquet absent du serveur — point de retour à Sidy (Cmd 13) avant tout nouvel
essai. Sans ce verdict, aucun `plan.md` ne peut être écrit (Cmd 6, gabarit §2).

## Pistes 4 et 5 — modèle de langue et prétraitement (2026-09-07)

Menées après le verdict Cmd 13 de Sidy du 2026-09-07. **Fait relevé à
l'ouverture, et qui commande tout ce qui suit** : le modèle en service,
`/usr/share/tesseract-ocr/5/tessdata/ara.traineddata`, fait **1 432 056 octets et
date du 30 octobre 2019** — c'est `tessdata_fast`, la variante **la moins précise
des trois**. Les pistes 1 et 2 de cette spécification avaient donc toutes deux
été mesurées sur le modèle le plus faible disponible, sans que ce soit relevé.

### Protocole

Pages d'épreuve **fixées avant tout essai** : page 300 (échantillon commun) et
page 600 (règle déterministe 300 + 300). Mesure par
`atelier/rd/outillage/mesurer-qualite-ocr-arabe.py`, dont l'épreuve du §VII est
passée (vert sur du Coran normalisé à I1 = 0,44 %, dégradation monotone sous
corruption croissante, refus sur entrée muette). Épreuve **E0** faite d'abord :
`--tessdata-dir` sur un dossier vide **échoue** (code 1), et la sortie diffère du
témoin — le modèle désigné est réellement celui qui travaille.

### Piste 4 — modèle de langue seul (aucune installation)

Quatre modèles téléchargés dans `/root/out08/tessdata/` (sha256 au journal du
chantier) : `tessdata` standard (2 494 806 o), `tessdata_best` (12 603 724 o),
`script/Arabic` standard (10 021 388 o) et best (17 095 279 o). `/usr/share/`
n'a pas été touché.

**Verdict : négative.** Le meilleur modèle seul (`tessdata` standard) donne
I1 = 2,38 % sur la page 300 — sous le seuil — mais **5,20 % sur la page 600**,
au-dessus du seuil de 4,07 %. Le critère 2 (reproduction sur une seconde page)
n'est pas satisfait.

Trois constats acquis au passage :
- **`tessdata_best` est moins bon que `tessdata` standard** sur ce scan. Le
  modèle le plus lourd n'est pas le meilleur ici.
- Les modèles `script/Arabic` sont les pires **et** injectent 89 à 95 caractères
  invisibles interdits par le **Cmd 15**. Écartés à double titre.
- 400 dpi reste négatif **y compris recombiné au nouveau modèle** : la conclusion
  de la piste 1 tient, elle n'était pas un artefact du modèle rapide.

### Piste 5 — prétraitement d'image, Pillow seul (aucune installation)

Pillow 12.3.0 était **déjà installé** — la supposition qu'un prétraitement
exigeait un paquet absent était fausse. Binarisation Otsu (seuil sur
`im.histogram()`, Python pur), agrandissement ×2 Lanczos, redressement par
variance du profil de lignes, marge blanche.

**Verdict : franchit le seuil mécanique sur les deux pages.**

| variante | page 300 | page 600 |
|---|---|---|
| témoin (modèle Debian, `--psm 1`) | 4,72 | 8,13 |
| seuil de passage (moitié du témoin) | ≤ 2,36 | ≤ 4,07 |
| piste 4 — meilleur modèle seul | 2,38 | 5,20 ✗ |
| **piste 5 — `x2 + Otsu`, `--psm 6`** | **1,56** ✅ | **2,97** ✅ |

Le **redressement ne sert à rien** : l'angle détecté est `+0,00°` sur neuf essais
sur dix — le scan n'est pas de travers. Retiré de la chaîne retenue, qui se
réduit à **agrandissement ×2, binarisation Otsu, `--psm 6`**.

### Critère 1 — extraits à lire (le verdict appartient à Sidy, Cmd 12)

Même passage, page 300, sept lignes. Le seul écart entre les deux blocs est la
chaîne de conversion.

**Témoin — modèle Debian, sans prétraitement (I1 = 4,72 %)**

```text
أوالمند ؤب غيرا نك اذانص رفت ف المباح فتهمرف فيه على حضورانه مبام وان الشارع لولاما أباحسهلكمانصمرّفت
فئّهفتسكون مأجورافسباحك لامن حي ثكونهمباحاالامن حيث اعانك بهانه شرع من عند النهفان 11> لاينتة لل
بعدمؤت رسو لاله صل التهع ليهو سإ فان ال1->م هوعين الشسرع وقد سد ذلك البابفالمباح مباحلا يكون واجبا
ولاحظورا ,بدا وك ذلك كل واحدمن الاحكام وان خط رلاك شاطرفى فرض فتماليهبلاث_لك فانهمن الملأث واذا
خظرلك ناظرفمندوت فاحفظ أولالخاطرفانهة_د يكونمن ابلس فاًثستعليه فاذاخطرلكانتتر كه لدوب
نوهو على منه وول فلاتك_د لعن الاولوأثيت عليهواحفتا الثاقوافعلالاولولايد فاذافرغتمئه اشرعى
الثانى فافءله أيضافان ا لشنيءلان برجع نا سما بلا لك حيث م شفق لهمةصودهو بهذا الدواءيذهب ميض الث_يطان
```

**Chaîne retenue — `x2 + Otsu`, `--psm 6` (I1 = 1,56 %)**

```text
ولا محظلورا أبدا وكذ لاك كل واحد من الاحكاروان خطارلاك خا طرف فرض ,اليه بلاش_.ك فأنه من الملا واذا
خط رلك تاطرق مندوب فاحفظ أول الخاطرفائه ةد يكون من ! بلاس فأنت عليه فاذا خطارلاك ان ثتر كهلادوب
اخ هوا على م نه وا ولى فلات دل عن الاول واثنبت عليه واحفنا الثاق وافعلالاول ولايد فاذاف رغتمنه اشرع ف
الثاتى فا فمإم ا إضافان 'لشيءلان برجم شاسثابلاشك حيث لم فق له مقع ود هو هذا الدواء يذهب عرض | لش_يطان
من نفسك ونكون ججرىالقاءما بلقاك الشرطان فج الاسلك اغير فك !اذ اعاماته ل هذا فافظ على مانوتك
عليه قان الله قدا نتى على الذبن يسارءون فىالخيرات وهرطاسابقون و يان هذا القدر وا يقول احاتى وهو
بهد السبيل
```

> **Réserve portée par la machine qui a mené les essais.** L'indice est divisé
> par trois, mais **à l'œil le texte reste corrompu** : mots soudés et lettres
> fausses subsistent dans les deux blocs. Cette réserve est consignée parce
> qu'elle tempère la mesure — elle ne tranche pas. Un chiffre qui s'améliore
> n'est pas un texte qui devient citable, et aucune de ces lignes ne dit que
> le critère 1 est franchi.

### Critère 3 — coût nommé

Aucune installation de paquet n'a été nécessaire : 42 Mo de fichiers de données
téléchargés, effaçables. Débit mesuré ~10 s/page à 2 CPU, prétraitement compris —
soit **~2 h 10 pour le tome 1** et **~7 h 20 pour les 2 630 pages des quatre
tomes**. Ce budget rend la reprise après coupure nécessaire, et c'est la seule
raison d'écrire un lanceur propre au chantier (voir `plan.md`, étape 6).
