---
title: "OUT-08 — OCR arabe de la Futūḥāt Maymaniyya : spécification"
type: outillage
chantier: OUT-08
tags: [atelier, rd, outillage, ocr, arabe, chantier, spec]
created: 2026-09-02
updated: 2026-09-02
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
négatives. Toute piste restante identifiée en `intent.md` (prétraitement d'image,
moteur alternatif, OCR cloud) suppose un paquet absent du serveur ou une dépense
tierce — point de retour à Sidy (Cmd 13) avant tout nouvel essai. Sans ce verdict,
aucun `plan.md` ne peut être écrit (Cmd 6, gabarit §2).
