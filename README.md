# Wiki

> **Finalité.** Ce dépôt n'a d'autre but que **la quête, l'étude et le service de la
> Vérité**. Tout ce qui s'y structure et s'y optimise sert une seule chose : **faciliter
> la Connaissance, jamais en être un obstacle** — sans oublier **l'Art, la créativité et
> l'Amour**. Les circuits, les Sceaux, les contrôles décrits ci-dessous sont des moyens ;
> un moyen qui commence à se prendre pour une fin se démonte, il ne se perfectionne pas.
> *(Parole de Sidy, 2026-09-18, inscrite en tête sur sa demande.)*

Dépôt personnel de transmission, d'étude et de création — contenu Markdown
structuré en cinq circuits étanches. Le protocole transversal vit dans
[CLAUDE.md](CLAUDE.md) ; chaque circuit porte son `CLAUDE.md` local (Sceau,
nomenclature, actions propres).

## Structure

- `doctrinal/` — le corps vivant des connaissances (doctrines, traditions,
  symboles, autorites, deviations, etudes, discernement, sources)
- `atelier/` — métier et références (materiel, entretiens, etudes-de-cas, rd/)
- `label/` — la maison de création (direction-artistique, musique, film,
  photographie, production, administratif, distribution, marketing-communication)
- `hermeneutique/` — navigation du domaine intermédiaire (auteurs, œuvres,
  expression)
- `meta/` — domaine réservé : outillage, protocoles archivés, transmissions
- `raw/` — sources brutes immuables (`assets/` : iconographie, schémas, scans)
- `_inbox/` — sas de déchargement, vidé après chaque intégration validée

## Outillage de dépôt (racine)

- `verifier-invariants.py` — vérification structurelle (frontmatter, annales,
  liens, étanchéité des circuits)
- `carte-du-depot.py` — comptage mécanique des liens entrants
- `atelier/rd/outillage/graphe/` — cartographie vivante du dépôt (script + rendu
  HTML ; sortie `graphe-cartographie.json` toujours à la racine)
