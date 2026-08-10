---
title: "Méthode — Croisement des fiches doctrinal/discernement/ (script déterministe + clustering)"
type: outillage
tags: [outillage, discernement, methode, deterministe, croisement]
created: 2026-08-10
updated: 2026-08-10
sources: []
links: ["[[doctrinal/index]]"]
---

# Méthode — Croisement des fiches `discernement/`

> **Objet du présent rapport** : documenter le *moyen* utilisé pour croiser les
> 33 fiches `doctrinal/discernement/` entre elles et avec le reste du circuit
> doctrinal, à la demande de Sidy (session du 2026-08-10). Ce document décrit
> une méthode d'ingénierie (script + logique de tri) ; il ne contient et ne
> reformule **aucun** contenu doctrinal ni verdict de fond — ceux-ci restent
> dans les fiches concernées et dans l'échange avec Sidy.

## 1. Principe appliqué

Conformément à la discipline transversale du dépôt (§I — scripter le
déterministe, réserver le modèle à ce qui exige un jugement), la première
passe n'a comporté aucune lecture de fond : un script a extrait mécaniquement
les données structurelles des 33 fiches (hors `_template.md`) avant toute
analyse par le modèle.

## 2. Extraction déterministe

Commande utilisée (une itération par fichier `.md` du dossier
`doctrinal/discernement/`) :

```bash
for f in *.md; do
  [ "$f" = "_template.md" ] && continue
  sed -n '/^---$/,/^---$/p' "$f" | head -20        # frontmatter (title/type/status/tags/sources/cross_links)
  grep -A1 "^\*\*Statut\*\*" "$f"                    # statut affiché dans le bloc 🔍, si présent hors frontmatter
  grep -oE '\[\[[^]]+\]\]' "$f" | sort -u            # tous les wikilinks, dédupliqués
  grep -o "to-source" "$f" | wc -l                   # marqueurs to-source résiduels
  grep -oE 'hozo|kumiko|kari-kumi|jikugumi|zōsaku' "$f" | sort | uniq -c   # qualifications sashimono déjà posées
done
```

Sortie : un fichier texte unique (1099 lignes), une section par fiche, aucune
prose générée à ce stade — uniquement des extraits bruts.

## 3. Logique de croisement (à partir de l'extraction, sans nouvelle lecture)

1. **Partition par statut frontmatter** (`traditionnel` / `speculatif` /
   `contre-traditionnel`) — donne directement l'ensemble des fiches closes
   (ancrage disponible) et des fiches encore ouvertes (candidates).
2. **Graphe de co-citation** : pour chaque fiche ouverte, intersection de ses
   `cross_links`/wikilinks avec l'ensemble des fiches closes. Une fiche
   ouverte dont un ou plusieurs ancrages cités ont été clos *après* sa propre
   création est un candidat prioritaire — pas parce que le rapprochement est
   vrai, mais parce que le matériau sur lequel elle s'appuie a changé de statut
   sans qu'elle ait été rouverte.
3. **Contrôle de complétude du double contrôle (§VII, 2026-07-16)** :
   filtrage des fiches dont les tags/titre indiquent une matière polaire,
   axiale, septénaire ou métrologique (28), puis vérification qu'elles
   cross-linkent bien
   [[doctrinal/discernement/2026-07-02_gizeh-pole-scientifique-antediluvien]]
   directement (et non seulement via une fiche dérivée). Absence de lien
   direct = confrontation non consignée, donc geste manquant au sens de la
   règle.
4. **Détection d'artefacts** : toute convergence apparente qui transiterait
   par une fiche `contre-traditionnel` ou `invalidée` est écartée avant
   présentation — elle n'est pas une convergence, c'est un artefact de
   co-citation.
5. **Isolement des blocs mono-session** : les fiches créées le même jour à
   partir d'une même expérience ne sont pas comptées comme corroboration
   mutuelle (une séance = une source, quel que soit le nombre de fiches
   qu'elle produit).

## 4. Nature du livrable

Le résultat transmis à Sidy est un **signalement**, jamais un verdict (Cmd
12) : pour chaque fiche ouverte concernée, la question posée est « voici ce
qui a changé autour de vous depuis votre ouverture — voulez-vous rouvrir
l'examen ? », jamais « voici ce qui est désormais établi ». Aucun `Statut` de
fiche `discernement` n'a été modifié par cette méthode elle-même ; elle ne
produit qu'une liste de candidats à l'arbitrage humain.

## 5. Limites

- Aucune lecture intégrale des 33 corps de fiche n'a été effectuée à ce
  stade — seuls frontmatter, wikilinks et blocs 🔍 partiellement visibles en
  tête de fichier ont été extraits. Une instruction plus fine
  (correspondance de contenu, pas seulement de citation) demanderait une
  lecture complète, fiche par fiche.
- La méthode détecte des *candidats de réexamen*, pas des convergences
  réelles : elle ne remplace à aucun moment l'examen formel (Cmd 12) que
  seule une lecture attentive, puis l'arbitrage de Sidy, peuvent produire.
