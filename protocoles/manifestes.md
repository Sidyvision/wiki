# Règle commune des MANIFESTES (Instrument et site)

> **Rattachement** : `CLAUDE.md`, §VII, *Manifestes*. Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

Toute couche de présentation consomme le dépôt via un **manifeste intermédiaire**,
jamais le markdown directement. Deux manifestes existent :
`instrument-donnees.yaml → generer-manifeste.py → app Instrument` et
`label/ → site-manifest.json → site`. Règles identiques :

1. Le manifeste est généré par **script déterministe à validations bloquantes**,
   **jamais** écrit à la main, **jamais** par LLM. Le LLM peut *proposer* des
   correspondances suggérées ; il n'en fige aucune.
2. **Flux à sens unique** : `dépôt → manifeste → interface`. L'interface ne réécrit
   jamais le dépôt ; une suggestion issue de l'app ne devient fiche `discernement/`
   que par validation humaine explicite (Cmd 12).
3. **Établi vs suggéré** : toute correspondance affichée « établie » est sourcée dans
   le wiki ; à défaut, elle est « suggérée » (pointillé + 🔍), jamais fondue avec les
   établies (miroir du statut `speculatif`).
4. Le journal du circuit concerné consigne chaque génération/déploiement.

5. **Le producteur reste en amont, le consommateur part en aval** (amendement
   2026-09-01, verdict Sidy — chantier INF-13). Le rendu de l'Instrument vit dans un
   **dépôt frère**, `Sidyvision/instrument` (public depuis le 2026-09-01, `main`
   protégée, `enforce_admins` actif), séparé de ce dépôt-ci. Ce n'est
   pas une commodité d'organisation : c'est la règle du sens unique ci-dessus
   exprimée en infrastructure plutôt qu'en discipline — tant que la source et
   l'interface partagent un arbre git, le sens unique ne tient que par la vigilance.
   La **ligne de coupe** est producteur/consommateur, jamais Instrument/reste :
   `instrument-donnees.yaml` (la donnée), `generer-manifeste.py` (le producteur),
   les fiches d'architecture, les mises en regard doctrinales, `assets-instrument/`
   et les chantiers `INS-` **restent ici** ; seule l'interface part. Le manifeste est
   **poussé depuis ce dépôt**, jamais tiré par l'interface — un dépôt destiné à
   devenir public ne détient à aucun moment de droit de lecture sur celui-ci. Le
   dépôt frère n'établit aucune correspondance (Cmd 3, Cmd 12) et ne réécrit rien
   ici. **Le rendu est servi depuis `sidyvision.com`** (verdict Sidy, 2026-09-01) —
   le dépôt frère porte la source, le site porte la diffusion ; ce troisième étage
   ne change pas le sens du flux, il le prolonge. La porte humaine de la
   *préversion avant production* vaut ici comme pour le site du label
   (`label/CLAUDE.md`, Action PUBLICATION, point 4) : aucune exception. Chantiers :
   `atelier/rd/infrastructure/inf-13-scission-depot-instrument/` (la scission) et
   INF-14 (l'hébergement).

Le détail propre au flux de publication du site (`label/`) vit dans
`label/CLAUDE.md`, Action PUBLICATION.
