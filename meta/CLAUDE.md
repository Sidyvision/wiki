بسم الله الرحمن الرحيم

# CLAUDE.md — Protocole local : Domaine Réservé `meta/`

> **Statut : méthode à l'essai** (éclatement expérimental du 2026-08-12, verdict
> Sidy). Ce fichier porte la lettre complète des règles **propres** au Domaine
> Réservé `meta/` — Sceau Transmissions/Karūbī, rappel d'étanchéité, corollaire
> agentique Hermes. Les règles **transversales** (étanchéité inter-circuits dans
> son intégralité, discipline des sources, double contrôle sashimono/Gizeh,
> commandements absolus, supervision des agents) restent dans le `CLAUDE.md`
> racine, **toujours chargé** quel que soit le dossier de travail — ce fichier ne
> s'y substitue pas, il le complète. En cas de doute ou de silence de ce fichier
> sur un point, le `CLAUDE.md` racine fait foi. Version pré-éclatement intégrale :
> `meta/protocole-archives/CLAUDE-v2-monolithique_2026-08-12.md`.

-----

## Objet du domaine

`meta/` accueille : outillage, briefs d'infrastructure, fiche personnelle,
transmissions nominales, généalogie, **motifs privés des décisions publiques**
(ex. contexte de l'identité publique), les configurations d'agents
(`hermes-prompts/`), et le catalogue de la bibliothèque physique. `meta/` **n'est
pas un sixième circuit** : c'est un Domaine Réservé, régime propre.

## Hub interne

`meta/meta-index.md` / `meta/meta-annales.md` — nommage préfixé `meta-` pour ne
jamais être confondu avec les `index.md`/`annales.md` des circuits. `meta-index.md`
recense par sous-dossier (`personnel/`, `genealogie/`, `journal/`, `transmissions/`,
`projet-unifie/`) les fiches du domaine, chacune reçoit un lien entrant légitime,
**intra-`meta/`** exclusivement — jamais un lien depuis un circuit vers `meta/`
(sens interdit). `meta-annales.md` suit la même discipline append-only que les
annales de circuit (marqueur `<!-- INSERTION: EN-TÊTE -->`).

## Rappel d'étanchéité (règle complète : CLAUDE.md racine §VI)

Hiérarchie du plus sensible au plus neutre : `meta/` → `hermeneutique/` →
`label/` → `atelier/projets/` et `atelier/rd/` → `doctrinal/` et `atelier/`
(neutres). Liens autorisés : du sensible VERS le neutre uniquement.

- INTERDIT : inscrire un fait personnel dans une page neutre. `meta/projet-unifie/`
  garde ce qui est **sensible** (motifs, credentials, prompts d'agents) ;
  `atelier/rd/infrastructure/` reçoit ce qui est **publiable** (voir
  `atelier/CLAUDE.md`).
- Ne jamais copier de contenu `meta/` ailleurs sans demande explicite.
- En cas de doute sur le circuit d'une nouvelle page : demander avant de créer.

## Sceau Transmissions (`meta/transmissions/`, dispositif Karūbī)

**Nom du Karūbī ≠ nom du destinataire** (source de confusion signalée le
2026-08-13) : chaque instance personnifie un personnage-enfant portant son
propre nom (champ `nom_karubi` du Sceau), distinct de celui de la personne à
qui elle est remise. Table de correspondance (mise à jour à chaque
`finalisation` journalisée dans `registre-silsila.md`) :

| destinataire | nom_karubi |
|---|---|
| Mehdi Bouzouïda | Habib |
| Mikael Heaudebourg | Malik |
| Habiba-Nour Kouyaté | Jamal & Jamila |
| Jean-Marc Bastareaud | Yahya |
| Wendel Nazaire | Hassan |

Circuit du plus sensible : un fichier-protocole personnifié, remis de main à main
à un destinataire nommé, qui vit par cycles de navette entre lui et Sidy. Sceau
propre, allégé (pas de Sceau Recteur doctrinal) :

```yaml
---
title: "Titre exact"
type: transmission
generation: 0 | 1 | 2 ...
emetteur: "..."
destinataire: "..."
nom_karubi: "..."
date_remise: "YYYY-MM-DD"
portee: khassa | amma
version: n
hash_sceau: "sha256"        # calculé par generer-karubi.py sceller — jamais à la main
hash_parent: "sha256 | none"
phrase_sceau: "..."
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Règles propres au circuit :
- **Zones scellées** (`<!-- SCEAU:DEBUT -->` / `<!-- SCEAU:FIN -->`) : intouchables
  hors édition G0 ; intégrité vérifiée mécaniquement (`generer-karubi.py
  verifier`), jamais sur déclaration.
- **Zones de croissance** (Mémoire vivante, Questions pour Sidy) : append-only,
  même discipline que les annales.
- **Étanchéité** : `meta/transmissions/` ne lie jamais vers `doctrinal/`, `label/`
  ni `atelier/`, et réciproquement.
- **Journalisation** : chaque événement (génération, remise, retour, rescellement,
  élévation de portée, deprecated) est consigné dans
  `meta/transmissions/registre-silsila.md`, format greppable
  `## [YYYY-MM-DD] evenement | destinataire | Gn | portee | vN | hash`.
- **Non-syncrétisme (Cmd 3)** : le dispositif emprunte la forme du sanad
  (traçabilité documentaire) sans prétendre au statut d'une ijāza spirituelle —
  ce rappel figure explicitement dans le §0 de chaque instance.
- **Porte humaine (Cmd 13)** : toute remise, toute élévation `khassa → amma`,
  toute suppression (`deprecated`, jamais de suppression sèche — Cmd 10) est
  décidée par Sidy seul.

### Outillage d'automatisation de la navette (ouvert 2026-08-15)

Le cycle de navette-retour (§7 du gabarit) dispose désormais d'un outillage
mécanique, **pour les destinataires ayant rejoint le serveur** (accès `_inbox/`
en écriture, cas Mehdi) — la première remise reste humaine/physique, inchangée.

- `meta/transmissions/integrer-navette-karubi.py` — script déterministe (aucun
  LLM), réutilise `generer-karubi.py` et `ajouter-memoire-karubi.py` comme
  primitives. Vérifie le sceau du canonique, compare les zones scellées
  navette vs canonique (refuse et n'écrit rien en cas d'écart — incident, pas
  navette normale), extrait et applique les ajouts append-only de §8/§9,
  archive la navette dans `meta/transmissions/navettes-archivees/
  <destinataire>/`, journalise dans `registre-silsila.md`. Ne touche **jamais**
  à §4, §10, `hash_sceau` ni `version` — ces champs restent sous plume humaine
  (Cmd 13).
- Rôle G0 de brouillon §4 (collecte, pas écriture finale) — voir
  `meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md`.
  Sortie dans `meta/transmissions/brouillons-section4/`, jamais dans le
  canonique. Distinct et sans lien de contexte avec le sub-agent Karūbī
  côté destinataire (`spec-skill-karubi-hermes.md`), qui reste isolé du wiki.
- §9→§10 (Questions pour Sidy → Réponses) reste une réponse directe de Sidy,
  mot pour mot, hors périmètre de tout automatisme.

## Corollaire agentique (2026-08-09) — couche opérative Hermes

L'étanchéité ci-dessus régit les **circuits du dépôt** (doctrinal, atelier,
hermeneutique, label) : elle continue d'interdire qu'un fait personnel migre dans
une fiche neutre, et qu'un motif privé s'y substitue à une conséquence de design
déclarée — rien de cela ne change. Elle **ne s'applique pas telle quelle à la
couche agentique** (Hermes, CLAUDE.md racine §I, §VIII) : la fonction de ces
agents est précisément de servir Sidy dans le concret d'un quotidien difficile, ce
qui suppose l'usage de son contexte personnel — l'en isoler par principe le
priverait de sa raison d'être. Ce point a été assumé explicitement par Sidy
(verdict Cmd 12, 2026-08-09) : la confrontation entre l'outil en développement et
le protocole existant, y compris `CLAUDE.md` lui-même, fait partie de la méthode
et non de sa violation.

Contrepartie non-négociable, pour que cette ouverture ne devienne pas un canal de
contamination doctrinale par un autre chemin :

1. Toute donnée personnelle (thème natal, situation, préférence) injectée dans un
   prompt d'agent porte sa hiérarchie ontologique **en clair, dans le texte du
   prompt** — pas seulement dans l'intention de celui qui l'a rédigé. Le principe
   invoqué **précède et structure** le rôle ; la détermination individuelle de
   Sidy le **colore sans le redéfinir** et n'engage personne d'autre.
   Qualification *zōsaku* explicite — une extrémité du joint est contingente et
   ne porte rien — jamais une mention à plat qui laisserait le principe et
   l'individuel de rang égal.
2. La donnée personnelle reste **lue en session par l'agent** ; elle n'est
   **jamais versée** dans une fiche `doctrinal/`, `label/` ou `hermeneutique/` —
   l'étanchéité de ces trois circuits reste pleine et entière.
3. « Aucun secret du dépôt sur machine d'inférence tierce » (CLAUDE.md racine
   §VIII.5) s'apprécie **au cas par cas** pour toute donnée personnelle selon le
   moteur qui la reçoit — signalé à chaque nouvel usage, jamais tranché une fois
   pour toutes.
4. Le registre **spirituel** reste hors champ de ce corollaire et hors champ des
   agents en général (Cmd 2, distinction psychique/spirituel) : un agent
   documente et organise le contexte personnel, il n'interprète ni ne conseille
   sur ce plan — la note Fard/Afrad (`meta/projet-unifie/hermes-prompts/`, voir
   fichier `04-sessions-par-fonction-et-backlogs.md`) rappelle que ce registre
   relève d'une autorité spirituelle vivante, non d'un modèle.
