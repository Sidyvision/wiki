# Action : VIGILANCE (contrôle d'orthodoxie et de forme)

> **Rattachement** : `CLAUDE.md`, §VII, *Actions transversales*. Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

- Frontmatter complet et valide (Sceau du circuit concerné — `CLAUDE.md` local).
- Notions orphelines, liens morts, pages d'autorités sans sources — via
  `atelier/rd/outillage/graphe/generer-cartographie.py` (régénérer si
  `graphe-cartographie.json` est antérieur au dernier commit doctrinal).
- Infiltrations de vocabulaire profane ou « New Age » dans les pages de Symboles.
- Violations d'étanchéité entre les cinq circuits (§VI).
- **Rapporter sans corriger d'office** ; demander avant d'éditer.
- Les annales sont **append-only** : un `Update` d'annales qui échoue ne doit JAMAIS
  être suivi d'un `Write` global.
- **Convention d'insertion** (amendement 2026-07-27, verdict Sidy) : tout fichier
  append-only déclare sa convention dans son propre en-tête via un marqueur HTML :
  - `<!-- INSERTION: EN-TÊTE -->` — nouvelle entrée insérée immédiatement après le
    bloc d'introduction (chronologique inverse). Cas des `annales.md`.
  - `<!-- INSERTION: QUEUE -->` — nouvelle entrée ajoutée en fin de fichier
    (chronologique direct). Cas des registres de chaîne.
  Un agent qui écrit dans un fichier append-only **lit d'abord ce marqueur**. Absence
  de marqueur = écriture interdite, signalement à Sidy.
