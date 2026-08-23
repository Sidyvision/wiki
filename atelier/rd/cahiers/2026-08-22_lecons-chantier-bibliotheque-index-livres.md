---
title: "Leçons du chantier bibliothèque — index et glossaires d'ouvrages"
type: experience
statut_experience: exploratoire
tags: [rd, bibliotheque, outillage, supervision, agents, unicode]
created: 2026-08-22
updated: 2026-08-22
sources: []
links: []
---

# Leçons du chantier bibliothèque — index et glossaires d'ouvrages

Cahier de retour d'expérience du chantier ouvert le 2026-08-22 : outiller la
transcription des index et glossaires photographiés des ouvrages de la
bibliothèque physique, sous supervision, l'exécution (OCR, gros du travail)
revenant à l'agent Hermes. Consigné ici au titre de la mission du pôle : les
leçons de la formation d'un agent reviennent à `atelier/rd/`.

Aucun contenu doctrinal. Ce cahier porte sur la méthode, pas sur les textes.

## 1. Un malentendu de cadrage, et ce qu'il coûte

Le premier plan produit fut hors sujet : il traitait la demande comme un
chantier global sur `raw/`, avec transcription de PDF et amendement du Sceau.
La demande réelle était étroite — trois dossiers de photographies, en extension
du catalogue de la bibliothèque physique, pour savoir *où chercher*.

**Leçon** : un périmètre énoncé par exemples (« /root/wiki/raw/X ; Y ; Z ») est
un périmètre *fermé*, non une illustration d'un ensemble plus vaste. La
généralisation spontanée d'un exemple en catégorie est le mode d'échec propre à
la supervision — elle produit un plan cohérent, ambitieux, et faux. Le coût est
payé avant toute écriture, ce qui est le meilleur cas ; d'où l'intérêt du Cmd 6.

## 2. La contamination Unicode se propage par copie, pas par faute

Quatre violations du Cmd 15 ont été commises **dans la même passe qui traitait
un incident Cmd 15**, dont une dans la cellule de tableau documentant le
problème. Aucune n'était une frappe : toutes venaient d'une copie depuis un
contexte déjà affecté — y compris un rendu d'interface.

Une **cinquième** a été commise dans le présent cahier, à la rédaction même de
ce paragraphe (occurrence de « Hermes » recopiée). Détectée et retirée par le
balayage de fin de passe. Le fait est consigné plutôt que corrigé en silence :
il confirme le diagnostic mieux qu'aucune démonstration.

**Leçon structurelle** : le vecteur est le *copier depuis un contexte affecté*,
jamais la saisie. Un balayage mécanique en fin de passe sur l'intégralité des
fichiers touchés est donc non négociable, y compris — surtout — quand la passe
porte sur l'hygiène Unicode elle-même.

## 3. Le piège de l'outil qui contient ce qu'il interdit

Le validateur déclarait initialement les points de code interdits **en clair**
dans son dictionnaire : il se déclenchait sur lui-même. Corrigé en les déclarant
par `chr(0x200B)` etc.

**Leçon** : tout contrôle qui énumère des motifs interdits doit les construire,
jamais les littéraliser. Vaut au-delà d'Unicode — c'est la même famille que le
bruit `C1` des documents citant des wikilinks bruts, connu du dépôt.

## 4. Le jugement ne se déclare pas, il se calcule

Le schéma de fiche prévoyait d'abord un champ `completude`. C'était un champ de
*jugement*, que l'agent aurait rempli par affirmation. Il a été supprimé : la
contiguïté des vues est désormais **dérivée** par le validateur à partir des
numéros de photographies déclarés.

**Leçon** (§VIII.2, fiabilité d'action ≠ fiabilité narrative) : chaque fois
qu'un schéma demande à un agent d'attester une propriété vérifiable
mécaniquement, le champ est à supprimer et le contrôle à écrire.

## 5. La panne silencieuse : un contrôle qui ne s'arme pas

Découverte tardive, et la plus instructive. Le contrôle H1 (photographie
déclarée vs photographie réelle) — précisément la garantie que le script
`compare` perdu apportait — ne s'armait qu'à deux conditions : `dossier_raw`
présent en frontmatter, et `--raw` passé en ligne de commande. Or `dossier_raw`
n'était pas dans les clés requises, `--raw` valait `None` par défaut, et le
shim ne le transmettait pas. **Par le chemin automatisé, le contrôle ne
s'exécutait jamais** : une fiche déclarant une photographie inexistante passait
avec un code de retour 0.

Constaté empiriquement avant correction (fiche déclarant `IMG_9999`) :
générateur `code: 0`, validateur autonome avec `--raw` `code: 1`.

**Leçon** : un contrôle qui « passe » n'est pas un contrôle qui s'est exécuté.
Tout garde-fou conditionnel doit être éprouvé sur un cas qu'il *doit* rejeter —
sinon on mesure son silence, pas sa vigilance. Corrigé : `dossier_raw` requis,
`--raw` par défaut résolu vers le `raw/` du dépôt, transmission par le shim.

Corollaire noté dans le shim : il avale la sortie détaillée. « Le générateur
valide » ne veut pas dire « le générateur rapporte ».

## 6. Prévenir par construction plutôt que nettoyer

Les marques bidirectionnelles (U+200E/U+200F) que l'OCR émet naturellement sur
du texte mêlant arabe et latin ne sont pas nettoyées après coup : le schéma de
table **sépare les colonnes par écriture**, l'arabe et le latin ne partageant
jamais une cellule. La cause est retirée, non la trace.

## 7. Absence de dépôt git — signalée, non contournée

`/root/wiki` n'est pas un dépôt git : `git status` ne rend rien. Le Cmd 9 (SHA
court en fin d'entrée d'annales) est donc **insatisfaisable**, et la surface de
relecture par `git diff` n'existe pas.

Le rétablissement du protocole `_inbox/` (verdict Sidy du 2026-08-22) répare
partiellement ce manque : en l'absence de git, **le sas *est* le mécanisme de
réversibilité**. Rien n'entre dans un circuit sans avoir été déposé, relu et
versé. Point restant au verdict de Sidy.

## 8. Ce qui reste à éprouver

Le dispositif n'a pas encore rencontré son objet : aucun lot n'a été traité par
l'agent. Les leçons ci-dessus sont celles de la *conception* de l'outillage. Le
retour d'expérience de la formation proprement dite — qualité de l'OCR,
obéissance aux points d'arrêt `clarify`, taux de `to-verify` — reste à écrire
après le lot 1 (Rig-Véda, 16 vues, le plus petit : les erreurs de formation y
coûtent le moins).
