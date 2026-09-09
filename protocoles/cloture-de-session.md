# Vigilance documentaire — clôture de session

> **Rattachement** : `CLAUDE.md`, §VII, *Clôture de session*. Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

À la clôture de **chaque** session de travail (wiki, Instrument, label, infra) :
vérifier systématiquement si les documents amont (architecture, feuilles de route,
briefs `meta/projet-unifie/`, fiches doctrinales liées, et le présent protocole —
racine et locaux) doivent être mis à jour à la lumière des décisions prises.
Proactif, jamais sur demande seulement. Toute divergence constatée entre ce
protocole et un document d'instructions dérivé est signalée : **le CLAUDE.md
concerné fait foi** (racine pour le transversal, local pour le propre au circuit —
§II bis).

Tout contrôle mécanique écrit ou modifié pendant la session relève de l'**Épreuve des
contrôles** (§VII ci-dessus) : son refus doit avoir été observé, et le résultat consigné.

**Vérification structurelle obligatoire** (amendement 2026-07-27, verdict Sidy) :
exécuter `python3 verifier-invariants.py --racine /root/wiki` et consigner le
résultat brut dans l'entrée d'annales de la session. Cette étape ne doit pas être
sautée. Phase actuelle : **calibrage** (non-bloquant) — les erreurs sont investiguées
et rapportées, pas bloquantes. Passage en mode `--strict` après calibrage confirmé.

**Usage explicite du graphe** (amendement 2026-08-31, verdict Sidy) : toute session
qui crée ou modifie des fiches `doctrinal/` régénère le graphe —
`python3 atelier/rd/outillage/graphe/generer-cartographie.py` (sortie :
`graphe-cartographie.json`, racine du dépôt) — et le consulte pour détecter
notions orphelines et liens morts (§VII, Action VIGILANCE) avant la clôture de
session. Même discipline de non-correction d'office : une anomalie révélée par le
graphe se rapporte, ne se corrige pas silencieusement (Cmd 12).

**Statut des documents d'investigation** (amendement 2026-07-27) : les documents
produits en session claude.ai portent un statut explicite — `brouillon` (en
discussion) ou `vise` (revu par Sidy). Claude Code ne consigne dans les annales
que des opérations issues de documents `vise`.
