---
title: "Proposition — Image organique du Discernement (champ, semence, fruit)"
type: meta
tags: [outillage, projet-claude-ai, discernement, doctrinal, proposition]
created: 2026-08-27
updated: 2026-08-27
---

# Proposition — Image organique du Discernement

> **Statut : validée par Sidy le 2026-08-27, exécution partielle — gabarit
> seul.** `doctrinal/discernement/_template.md` amendé (champ `maturite`
> ajouté au Sceau). **Rétroportage sur les ~38 fiches `discernement/`
> existantes explicitement différé** (décision Sidy, pas un oubli) : les
> agents renseigneront le champ au fil de leurs éditions de fond
> quotidiennes, ce qui sert aussi d'étalonnage progressif du critère avant
> toute passe systématique. `doctrinal/CLAUDE.md` n'est pas amendé par cette
> exécution (le bloc 🔍 normalisé n'y référence pas encore `maturite` —
> laissé pour une passe ultérieure si l'usage du champ le justifie).

## 1. Rapport à l'existant

`doctrinal/discernement/` porte déjà un bloc normalisé 🔍 avec un champ
**Statut** à trois valeurs : `en cours | validée | invalidée` (issu de
`meta/proposition-discernement.md`, `deprecated` mais adopté en substance ;
gabarit vivant : `doctrinal/discernement/_template.md`). Ce champ qualifie
**l'issue** d'une spéculation (close ou non, et dans quel sens).

La présente proposition **n'y touche pas** et **ne le remplace pas**. Elle
ajoute un axe orthogonal : la **maturation** — où en est le développement
d'une fiche, indépendamment de son issue finale. Une fiche peut rester
`en cours` pendant tout son trajet de `germe` à `fruit-mûr` ; la maturation
est ce qui se passe *avant* que le Statut ne bascule vers `validée` ou
`invalidée`.

## 2. L'image

Sidy formule l'image ainsi : « Discernement est un champ, irrigué par le
flux d'entrée et la communication du dépôt. Chaque fiche est une semence dont
on espère cueillir les fruits. »

Cinq états de maturation proposés :

1. **Aucune pousse** — la semence est là (la fiche existe, l'hypothèse est
   formulée) mais rien n'a progressé : pas de généalogie des idées engagée,
   pas d'examen formel substantiel. Dormante ou à l'abandon.
2. **Grain germé** — un premier examen formel est amorcé : au moins une
   tension ou une cohérence formelle relevée, même ténue.
3. **Plante** — la généalogie des idées est identifiée (au moins une
   filiation orthodoxe ou une parenté hétérodoxe pointée avec justification,
   pas seulement un lien nu), l'examen formel devient substantiel.
4. **Arbre** — cohérence structurelle mûre : plusieurs croisements établis
   (`cross_links`, liens vers `etudes/`, convergences avec d'autres fiches
   `discernement/` sur un motif proche — cf. la « double ancrage », déjà
   nommée comme signal de vigilance dans `doctrinal/CLAUDE.md`).
5. **Fruit** (avec degrés — `fruit-vert` / `fruit-mûr`) — la fiche est prête
   pour un verdict : l'examen formel est complet, la généalogie est
   documentée, rien ne manque pour que Sidy (ou une autorité textuelle
   citée) tranche. `fruit-vert` = presque prête, un point reste à éclaircir ;
   `fruit-mûr` = prête, aucun obstacle formel identifié à la clôture.

## 3. Champ de Sceau proposé

```yaml
maturite: aucune-pousse | germe | plante | arbre | fruit-vert | fruit-mur
```

Ajouté au Sceau Recteur des fiches `type: discernement` uniquement (pas les
autres types doctrinaux). Coexiste avec `status` sans le recouvrir :

| `status` | `maturite` typique |
|---|---|
| `speculatif` (en cours) | tout le spectre `aucune-pousse` → `fruit-mûr` |
| `traditionnel` / `contre-traditionnel` (validée/invalidée) | fixé au moment de la clôture, généralement `fruit-mûr` (le verdict a suivi une fiche mûre) — sauf clôture anticipée par Sidy sur une fiche moins mûre, cas possible et non interdit |

## 4. Pourquoi ceci reste un jugement de forme (Cmd 12)

Point à anticiper explicitement, pour qu'un futur examen n'y voie pas un
verdict métaphysique déguisé sous une métaphore agricole : la `maturite`
mesure des critères **structurels et vérifiables** — nombre et qualité des
liens de généalogie, présence d'un examen formel substantiel, densité des
`cross_links`, sourcing effectif (`sources_count` réel vs `to-source`
persistant). Aucun de ces critères ne porte sur la validité du principe
métaphysique invoqué. Un « fruit mûr » peut tout à fait être promis à un
verdict `invalidée` — la maturation qualifie la préparation du dossier, pas
la conclusion. C'est le même geste que l'« Examen formel » déjà pratiqué
(jurisdiction Claude, jamais le principe) : la maturation est cet examen
formel rendu visible et graduel plutôt que binaire.

## 5. Mission de veille proposée

Objectif formulé par Sidy : « m'avertir lorsqu'un fruit est mûr, ou bien
m'informer de la pousse d'une fiche. »

- **Signal de fruit mûr** : dès qu'une fiche passe (ou est évaluée comme
  devant passer) à `fruit-mur`, remontée dans le canal existant — Rapport du
  matin (section verdicts en attente, déjà prévue) ou signalement ad hoc
  selon le contexte de la session.
- **Signal de croissance** : tout changement d'état de maturation d'une
  fiche (ex. `germe` → `plante`) mentionné au fil de la session qui l'a
  produit, et consigné dans `doctrinal/annales.md` comme n'importe quelle
  autre opération de fond (Cmd 9).
- **Pas d'automatisation codée dans cette proposition** : conformément à la
  décision prise avec Sidy, cette fiche reste un document de conception ; le
  déclenchement du signal reste, pour l'instant, un geste manuel de la
  session Claude Code ou d'un agent de fonction qui relit une fiche
  `discernement/` — pas un script de scan automatique.

## 6. Points ouverts

- Faut-il un seuil formel (ex. nombre minimal de `cross_links`) pour
  distinguer `arbre` de `fruit-vert`, ou cette évaluation reste-t-elle
  qualitative, laissée au jugement de la session qui relit la fiche ?
- Articulation avec le pôle Usûl (`proposition-pole-usul-2026-08-27.md`) : une
  fiche de discernement qui s'appuie sur une branche Usûl (ex. Manṭiq pour
  affiner l'examen formel) mûrit-elle plus vite, structurellement ? Non
  tranché ici — signalé comme piste.
- Si validée, cette proposition nécessite un amendement de
  `doctrinal/discernement/_template.md` (ajout du champ `maturite` et d'une
  ligne dans le bloc 🔍 ou juste après) — non réalisé dans ce chantier.
