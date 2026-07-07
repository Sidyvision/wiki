# PATCH CLAUDE.md — Convention Sashimono (ordre humain du 2026-07-07)

Édition de CLAUDE.md **validée explicitement par l'utilisateur** (session claude.ai
du 2026-07-07). Le protocole étant invariant sauf ordre humain, cet ordre est ici
consigné. Application par édition ciblée (jamais de réécriture globale du fichier),
diff relu avant commit.

## Édition 1 — Note de révision (en-tête)

Dans le bloc de citation d'en-tête (`> Protocole issu de la Restauration...`),
ajouter à la fin de l'énumération des révisions, avant la phrase sur le mot
« réforme » :

```
> **Révisé le 2026-07-07** : adoption de la philosophie et de la convention
> terminologique Sashimono (§VII, « Convention Sashimono » ; directive détaillée :
> `meta/philosophie-sashimono.md`).
```

## Édition 2 — Nouvelle sous-section en fin de §VII

Insérer le bloc suivant **après** la sous-section « Vigilance documentaire (clôture
de session) » et **avant** le séparateur `-----` qui précède le §VIII :

```markdown
### Convention Sashimono (philosophie d'assemblage — validée 2026-07-07)

Le dépôt adopte le **sashimono** (menuiserie japonaise assemblée sans clou : la
solidité vient de la justesse du joint, jamais d'un fixateur étranger) comme
philosophie d'assemblage et convention terminologique. Directive détaillée :
`meta/philosophie-sashimono.md`. Statut : **analogie opératoire, jamais
doctrinale** (la question doctrinale est instruite dans
`doctrinal/discernement/2026-07-07_sashimono-metier-traditionnel.md`, verdict
réservé). Lettre des six articles :

1. **Aucune pièce ne tient par colle** : ce qui ne repose que sur une assertion de
   modèle (ni source primaire, ni script déterministe) se démonte ou se marque
   🔍/`to-source`.
2. **La coupe avant l'assemblage** : normaliser avant d'intégrer ; un lot mal
   taillé retourne au sas, il ne s'ajuste jamais au marteau côté intégration.
3. **Jamais de joint forcé** : toute résistance formelle suspend l'assemblage ; on
   documente et on pose les pièces côte à côte.
4. **Tout assemblage se présente à blanc** : 🔍, bac à sable, préversion — rien de
   définitif sans validation humaine.
5. **L'assemblage reste démontable** : réversibilité de chaque phase, `deprecated`
   plutôt que suppression, traçabilité intégrale.
6. **Le joint parfait est invisible, jamais secret** : l'interface masque la
   jointure ; le dépôt (git, annales) la documente intégralement.

**Lexique conventionnel** (orthographes `to-source`, valides comme convention
interne) : **kigumi** = la philosophie elle-même (Art. 1) ; **hozo** (tenon-
mortaise) = ancrage d'équivalence ; **kumiko** (treillis en plan) = ancrage de
complémentarité ; **kari-kumi** (montage à blanc) = tout état suggéré 🔍 — l'onglet
apophatique est la *vue kari-kumi du chantier* (les joints non taillés et les
pièces manquantes s'y voient) ; **sumi-tsuke** (traçage à l'encre) = la fiche
discernement, le trait précède la coupe ; **ki-dori** (choix de la pièce dans le
bois brut) = VIGILANCE et travail sur `raw/`, la recherche de la pièce manquante.
Termes esthétiques à charge doctrinale propre (*ma*, *wabi-sabi*...) : **exclus**
de la convention sans fiche `discernement` préalable (Cmd 3).
```

## Vérification post-édition

1. `git diff` relu intégralement (les deux insertions, rien d'autre).
2. Contrôle : le §VIII et les Commandements sont inchangés.
3. Commit dédié : `RESTAURATION: convention sashimono (CLAUDE.md §VII, ordre humain 2026-07-07)`.
