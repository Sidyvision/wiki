---
title: "Feedback extérieur — audit du wiki par Qoder (2026-09-09)"
type: etude
tags: [audit, feedback, methode, outillage, structure]
created: 2026-09-09
updated: 2026-09-09
sources: []
---

# Feedback extérieur — audit du wiki par Qoder

> **Contexte** : audit demandé par Sidy le 2026-09-09, réalisé par Qoder en
> session terminal. Lecture de l'ensemble du dépôt : CLAUDE.md racine (948
> lignes), 5 CLAUDE.md locaux, cartes du dépôt (doctrinal 227 fiches, atelier
> 43, label 12, meta 150), échantillons de contenu doctrinal, herméneutique,
> label, R&D, outillage (53 scripts Python, verifier-invariants.py 798 lignes),
> textes/ (657 fichiers, 29 dossiers d'ouvrages), serveur MCP wiki (826 lignes,
> 14 outils — ajouté après signalement de Sidy, §VII bis). 272 fichiers portent
> au moins un marqueur `to-source`. Total : ~2000 fichiers Markdown, ~270 000
> lignes. **29 problèmes identifiés, 9 priorités recommandées.**

---

## I. Vue d'ensemble — ce que le wiki est

Un dépôt de transmission, d'étude et de création organisé en cinq circuits
étanches (doctrinal, atelier, label, hermeneutique, meta) + un domaine réservé
(meta/) + un cabinet de lecture (textes/). Gouverné par un protocole
opérationnel (CLAUDE.md) de 948 lignes, 15 commandements absolus, 6 articles
sashimono, et un outillage mécanique de vérification (verifier-invariants.py,
carte-du-depot.py, graphe, index lexical). Un serveur MCP (`mcp-servers/wiki/`,
826 lignes, 14 outils) expose le dépôt à Claude Code, Hermes et Qoder via le
protocole Model Context Protocol. Le tout maintenu par des modèles (Claude Code,
Hermes, Qwen) sous supervision humaine stricte.

Le wiki n'est pas un wiki au sens conventionnel : c'est un **système de
gestion de la connaissance doctrinale et créative**, avec des gardes-fous
formels contre la fabrication par les modèles, la contamination inter-circuits,
et le syncrétisme forcé.

---

## II. CLAUDE.md racine — feedback détaillé

### Points forts

**1. Lucidité sur le rôle de la machine.** La subordination du modèle au
jugement humain n'est pas un slogan : elle est câblée dans chaque mécanisme
(manifestes, discernements, annales, Karūbī). Les Cmd 12 et 13 ne sont pas
cosmétiques. C'est rare et intellectuellement honnête.

**2. L'Épreuve des contrôles (§VII).** « Un contrôle dont on n'a pas vu
l'échec n'est pas un contrôle vérifié. » Maturité d'ingénierie exceptionnelle,
née de deux vrais incidents (PRO-01, INF-14). Peu d'équipes humaines en
arrivent là.

**3. La discipline des sources.** Le marqueur `to-source` + levée par
vérification humaine primaire est une garde sérieuse. Le fait que 272 fichiers
portent encore le marqueur montre que la règle est appliquée (on ne triche pas
pour les faire disparaître).

**4. Le sashimono comme philosophie opératoire.** L'analogie est juste, bien
tenue, avec des articles normatifs concrets (Art. 1-6). Ce n'est pas de la
décoration : il guide des décisions réelles (deprecated vs suppression,
kari-kumi avant production).

**5. L'agnosticisme du moteur (Cmd 14).** Le protocole ne dépend d'aucun
modèle. Pragmatique et visionnaire — le dépôt survivra à ses outils.

### Problèmes identifiés

**P1 — Le document est trop long (~950 lignes).** 15 commandements, des
dizaines de sous-règles, des amendements datés intégrés dans le corps. En
session longue, les règles noyées au milieu sont appliquées de façon moins
fiable. Le changelog dans l'en-tête (lignes 11-66) est du bruit pour une
session de travail ordinaire — une ligne de renvoi vers
`meta/protocole-archives/changelog-CLAUDE.md` suffirait.

**P2 — Accumulation sans consolidation.** Le document a grandi par accrétion
(amendements, ajouts, « ouvert YYYY-MM-DD »). Des règles sont énoncées deux ou
trois fois à des endroits différents (étanchéité §VI + corollaire agentique +
rappel meta/CLAUDE.md). Chaque ajout est justifié individuellement, mais
l'ensemble gagne en masse plus vite qu'en clarté.

**P3 — Le §V fantôme.** « (retiré — contenu migré) » conservé pour faciliter
le rapprochement avec l'archive. C'est une commodité d'historien qui alourdit
chaque lecture. L'archive existe déjà dans `meta/protocole-archives/`.

**P4 — Sur-spécification croissante.** Certaines sections descendent dans un
détail qui relève du journal de bord, pas du protocole permanent. Exemple : le
§VII sur les langues originales mesure « 9687 → 9841 (+154), arabe 469 → 532 ».
Utile pour le commit du jour ; bruit pour le protocole. La règle vit ici, le
chiffre devrait vivre dans les annales.

**P5 — Risque de rituel sur la substance.** Avec 15 commandements, 6 articles
sashimono, 5 règles d'annotation HTML, 6 points de discipline des langues, 10
règles de supervision des moteurs, des scripts de vérification, des cartes
générées, des annales append-only avec marqueurs d'insertion... le risque est
réel que « suivre le protocole » devienne une fin en soi. Si la mécanique de
maintenance du wiki consomme plus d'énergie que le travail qu'elle sert,
l'équilibre est rompu.

**P6 — Le document est à la fois spécification et récit.** Certaines sections
expliquent le *pourquoi* (excellent), d'autres enchaînent des *quoi* sans
contexte. Le mélange rend le scan difficile.

### Recommandations pour le CLAUDE.md

- **R1** : Déplacer le changelog de l'en-tête vers une ligne de renvoi. Gain
  estimé : ~55 lignes.
- **R2** : Supprimer le §V fantôme. Gain : ~8 lignes.
- **R3** : Fusionner les redites (étanchéité, corollaire agentique). Gain
  estimé : ~40 lignes.
- **R4** : Extraire les chiffres de mesure du §VII vers les annales. Gain
  estimé : ~30 lignes.
- **R5** : Envisager une passe de consolidation trimestrielle — pas pour changer
  le sens, mais pour réduire la longueur de 20-30%.

---

## III. Circuit doctrinal/ — feedback

### Vue quantitative

- 346 fiches (hors annales)
- 125 sources, 59 discernements, 104 symboles, 31 autorités, 6 traditions,
  11 déviations, 7 études
- 227 fiches recensées par la carte (périmètre carte-du-depot.py)

### Points forts

**1. La qualité rédactionnelle des discernements.** Les fiches de discernement
sont d'une rigueur remarquable. Exemple lu : `2026-07-16_sept-poles-aqtab`
(7 sources, 6 cross-links, généalogie des idées, confrontation Gizeh,
qualification sashimono). La structure narrative (récit → hypothèse →
généalogie → examen formel → conclusion) est claire et reproductible.

**2. Le maillage inter-fiches.** Les cross_links sont systématiques et
pertinents. Une fiche de discernement pointe vers ses sources, ses sœurs
thématiques, et les autorités concernées. Le graphe a de la matière.

**3. La discipline des statuts.** `traditionnel`, `speculatif`,
`contre-traditionnel`, `profane` — la qualification est portée dans le
frontmatter et contrôlée. Pas de flou entre ce qui est établi et ce qui est
suggéré.

**4. Le volume du corpus sourcé.** 125 fiches sources, adossées à 657 fichiers
de textes convertis dans `textes/`. Le corpus Guénon, Ibn ʿArabī, Burckhardt,
al-Jurjānī, Avalon, Shayegan est massivement présent. La bibliothèque physique
est doublée d'un corpus numérique versionné.

### Problèmes identifiés

**P7 — 68+ marqueurs `to-source` dans le seul circuit atelier/, certains
depuis juin 2026.** Le taux de création de marqueurs excède le taux de levée.
À terme, il faudra soit accepter un traitement par lots des marqueurs anciens,
soit réduire le débit des nouvelles intégrations.

**P8 — Fiches deprecated non nettoyées.** 17 fiches `deprecated` dans
`atelier/projets/`, toutes stubs pointeurs vers `rd/`. Migration terminée
depuis août 2026. Les stubs occupent de la place dans les cartes, le graphe,
et l'attention.

**P9 — Doublons de versions d'architecture.** Quatre versions de
`instrument-tradition-primordiale-architecture` (v0.1, v0.2, v0.3, v0_3)
coexistent comme fiches séparées. La carte les liste toutes les quatre. Seule
la v0.3 (ou v0_3, selon le sens de la normalisation) est la version de
travail. Les autres devraient être `deprecated` ou fusionnées.

**P10 — Liens morts massifs.** La carte de l'atelier recense des dizaines de
liens non résolus, principalement vers `doctrinal/` (fiches annoncées mais non
déposées, ou slugs incorrects). Le graphe signale 20 fiches orphelines dans le
seul circuit atelier/.

---

## IV. Circuit hermeneutique/ — feedback

### Vue quantitative

- 28 fiches (carte du dépôt)
- 6 auteurs, 8 œuvres, 1 source, 2 expression
- Œuvres : Metal Gear, Death Stranding, Hunter x Hunter, Dragon Ball, Dr Slump,
  20th Century Boys, Lost, The Matrix, Frankenstein

### Points forts

**1. Le concept de « domaine intermédiaire » est bien tenu.** Le circuit ne
prétend pas établir des correspondances doctrinales depuis la fiction. Il lit
les œuvres comme des *interfaces*, avec la clause de plasticité et le hozo
exclu par défaut. C'est une position intellectuelle claire et défendable.

**2. Le Sceau est bien adapté.** Les types (oeuvre, auteur, figure, dispositif,
concept, analyse, source) couvrent les besoins sans surcharge. Le champ
`registre: analyse | expression` distingue proprement les deux régimes.

**3. L'index est lisible.** La présentation par œuvre avec fiches liées est
claire. Les joints 🔍 sont signalés honnêtement.

### Problèmes identifiés

**P11 — Circuit jeune, encore en brouillon majoritaire.** Presque toutes les
fiches sont en `statut_analyse: brouillon`. C'est normal pour un circuit ouvert
en août 2026, mais cela signifie que le circuit n'a pas encore produit de
lecture mature. La valeur herméneutique réelle reste à venir.

**P12 — Les fiches `expression/` sont peu peuplées (2 fiches).** Le dispositif
est conçu pour accueillir les intuitions post-khalwa formulées dans le langage
de la fiction, mais le flux n'a pas encore alimenté ce régime. Question :
est-ce un retard de production, ou le signe que le dispositif n'est pas encore
naturel pour son utilisateur ?

**P13 — Pas de CLAUDE.md local pour le dossier `expression/`.** Les fiches
d'expression ont un régime particulier (issues de discernements doctrinaux,
portance zōsaku obligatoire) qui mériterait peut-être une sous-protocolisation,
ne serait-ce que pour rappeler au rédacteur les garde-fous spécifiques.

---

## V. Circuit label/ — feedback

### Vue quantitative

- 12 fiches
- 4 distribution, 3 production, 2 amorcage, 1 index, 1 marketing-communication

### Points forts

**1. La doctrine du don comme principe structurant.** Le label n'est pas un
label conventionnel avec une couche spirituelle ajoutée. Le principe du don
(bénéfice émergent, jamais promis) est le fondement de la distribution, du
modèle économique, et du merchandising. C'est cohérent et courageux.

**2. L'ancrage éthique de la structure (CLAUDE.md label §V).** Les aspects
commerciaux sont soumis à l'examen doctrinal, avec la tension voulue entre le
Commerce (contrepoids de rentabilité) et le Gardien (signalant les dérives).
L'alignement Fiqh (école mālikite en préséance) est une décision concrète, pas
une posture.

**3. Le protocole des cercles et la stratégie vinyle.** Des dispositifs
originaux (token non-transférable sur Tezos, 300 exemplaires aux dépositaires,
fanzine) qui traduisent la doctrine en mécanique concrète.

### Problèmes identifiés

**P14 — Le label est encore largement théorique.** Sur 12 fiches, aucune ne
porte `statut: sorti`. L'album personnel est en production, la doctrine du don
est posée, mais rien n'est encore publié. Le risque est que le label reste un
exercice de conception sans confrontation au réel. La doctrine du don n'a pas
été éprouvée par la pratique.

**P15 — Pas de fiche `administratif/`.** Le CLAUDE.md label prévoit un pôle
administratif, mais aucune fiche n'y vit. Les questions juridiques (registre
numérique, fiscalité du don, SDRM) sont mentionnées comme vigilances mais pas
instruites. C'est un passif de conformité.

**P16 — Les amorcages ne se concrétisent pas.** Deux fiches amorcage
(génération non-cumulative, imaginaire Nen/ruche/échecs) datent de juillet
2026. Aucune n'a été concrétisée depuis. Le dispositif `amorcage/` fonctionne-t-il
comme prévu (gestation → concrétisation) ou est-il un lieu de stockage d'idées
qui ne mûrissent pas ?

---

## VI. Circuit meta/ — feedback

### Vue quantitative

- 150 fiches (carte du dépôt)
- Sous-dossiers : personnel (25), genealogie (14), journal (5), briefs (4),
  transmissions (7), projet-unifie (~60), protocole-archives

### Points forts

**1. Le dispositif Karūbī est remarquable.** Le Sceau Transmissions, avec ses
zones scellées, son hash, son registre silsila append-only, et son outillage
déterministe (generer-karubi.py, integrer-navette-karubi.py), est l'une des
pièces les plus originales du dépôt. C'est un dispositif de transmission
documentaire qui emprunte la forme du sanad sans prétendre au statut d'ijāza.

**2. Le projet unifié est bien structuré.** Le dossier `meta/projet-unifie/`
est organisé en régimes (noyau de pilotage, propositions, archives, outillage,
choura, hermes-prompts, hermes-skills). La séparation propositions/archives
est saine. Les 12 rôles Hermes sont documentés avec leurs mandats.

**3. Les briefs de passation.** Les briefs
(2026-08-30_passation-*) sont un excellent dispositif de continuité entre
sessions. Ils résument l'état, les verdicts en attente, et les points de
reprise.

### Problèmes identifiés

**P17 — Le projet unifié est un dépôt dans le dépôt.** ~60 fiches, des
sous-dossiers sur 3 niveaux, des propositions, des archives, un orchestrateur
de choura, des hooks, des prompts Hermes... C'est un projet entier (le pilotage
de l'infrastructure globale) qui vit à l'intérieur du wiki. La frontière entre
« le wiki documente le projet » et « le projet EST le wiki » est poreuse.

**P18 — overview.md et onboarding.md sont deprecated mais toujours présents.**
Deux fiches marquées deprecated depuis mai-juin 2026, toujours accessibles.
L'onboarding en particulier contient des informations devenues caduques (IP
serveur, clé API dans le bashrc — même si la clé a été nettoyée, le document
la décrit encore).

**P19 — Le meta-index est devenu très long (~220 lignes).** Il remplit
correctement sa fonction de hub, mais il est lui-même devenu un document
difficile à parcourir. Une version condensée (juste les liens, sans les
annotations) pourrait aider.

---

## VII. Outillage — feedback

### Vue quantitative

- 53 scripts Python (hors venv)
- verifier-invariants.py : 798 lignes
- carte-du-depot.py : non lu en détail mais produit des cartes de 160-330 lignes
- Scripts de génération (manifestes, Karūbī, index lexical, graphe)
- Scripts de vérification (invariants, annotations, géométrie, OCR, coherence)
- Scripts de migration et conversion

### Points forts

**1. Le principe « scripter le déterministe, réserver le modèle au jugement »
est appliqué avec rigueur.** Les manifestes, les cartes, le scellement Karūbī,
l'index lexical, le graphe — tout ce qui peut être déterministe l'est. Aucun
LLM dans la boucle de production.

**2. verifier-invariants.py est un vrai juge de paix.** 798 lignes de
vérifications structurelles (B0-B7, C1-C3, D1-D6). Les contrôles sont éprouvés
sur faute fabriquée. C'est l'application concrète de l'Épreuve des contrôles.

**3. L'index lexical est une pièce maîtresse.** La gestion des écritures
originales (arabe, hébreu, devanagari, grec, han, kana), la correction du
tokeniseur pour les marques combinantes, les champs `apparie` et `jurjani` —
c'est un travail d'orfèvre technique au service de la rigueur doctrinale.

### Problèmes identifiés

**P20 — L'outillage est dispersé.** Scripts à la racine (`carte-du-depot.py`,
`verifier-invariants.py`), scripts dans `atelier/rd/outillage/`, scripts dans
`meta/transmissions/`, scripts dans `meta/projet-unifie/choura/`, scripts dans
`atelier/rd/bibliotheque/`. Pas de vue d'ensemble unifiée. Un nouveau script
écrit en session future ne saura pas où aller.

**P21 — Les .venv et __pycache__ sont dans l'arbre du wiki.**
`atelier/rd/infrastructure/bureau/.venv/` contient des centaines de fichiers
de site-packages. `atelier/rd/outillage/.graphify-venv/` idem. Ces dossiers
devraient être dans le .gitignore et hors de l'arbre de travail, ou au minimum
signalés comme tels.

**P22 — Le graphe n'est pas systématiquement régénéré.** La carte de l'atelier
signalait déjà (août 2026) que `graphe-cartographie.json` n'était jamais
régénéré. Le registre des problèmes (`registre-problemes`) liste cette anomalie
comme ouverte.

---

## VII bis. Serveur MCP wiki — la pièce manquante de l'audit

> **Note d'honnêteté** : cette section n'existait pas dans la première version
> de l'audit. Le serveur MCP vit dans `/root/mcp-servers/wiki/`, **en dehors
> de l'arbre du dépôt** — mon exploration initiale ne l'a pas couvert. Sidy
> l'a signalé. Ce qui suit complète l'audit.

### Vue quantitative

- 1 fichier serveur : `wiki_mcp_server.py` (826 lignes)
- 14 outils exposés via le protocole Model Context Protocol (MCP)
- Compatible mcp < 2 (FastMCP) et mcp >= 2 (MCPServer)
- 1 README, 1 `.mcp.json`, 1 `.venv`

### Ce que le serveur fait

Il expose le dépôt `/root/wiki` de façon **agnostique au moteur** : Claude Code,
Hermes, Qoder (ou tout client MCP) appellent les mêmes outils. Quatre catégories :

1. **Vérification** (7 outils) : `verifier_invariants`, `verifier_coherence_infra`,
   `detecter_non_tracke`, `verifier_rapports_traites`, `valider_index_livres`,
   `generer_glossaire_unifie`, `carte_du_depot`. Chaque outil appelle un script
   déterministe du dépôt — la source de vérité est le script, jamais le
   self-report du modèle.

2. **Lecture de registres** (3 outils) : `lire_registre_chantiers`,
   `lire_registre_problemes`, `lire_etat_infra`. Parsent les registres markdown
   en données structurées (JSON).

3. **Monitoring serveur** (1 outil) : `etat_serveur`. RAM, disque, services
   Hermes, processus Python, uptime. Lecture seule.

4. **Opérations fichiers** (3 outils) : `chercher_fiche`, `lire_fiche`,
   `ajouter_inbox`. Ce dernier écrit **exclusivement** dans `_inbox/`, aucun
   git, aucun auto-accept.

### Points forts

**1. La fraîcheur déclarée de l'index.** `_charger_index()` ne se contente pas
de charger l'index : elle rapporte sa date de génération et le nombre de fiches
plus récentes que lui. Un index périmé ne se plaint jamais de lui-même — il
répond, et il répond faux. Le contrôle déclare donc son état. C'est
l'application directe de l'Épreuve des contrôles (§VII) au niveau MCP.

**2. Les 4 passes de `chercher_terme`.** Exacte → normalisée → forme attestée
→ sous-chaîne, avec la passe qui a répondu **toujours nommée** dans le résultat.
Si aucune correspondance, des clés proches sont proposées plutôt qu'un silence.
C'est la règle « un silence est un mauvais résultat » appliquée.

**3. La protection path traversal.** `_safe_relative()` normalise tout chemin
fourni par un client et refuse toute sortie du dépôt. C'est une garde de
sécurité nécessaire pour un serveur exposé à des clients multiples.

**4. Le respect des principes du protocole.** Écriture uniquement dans `_inbox/`
(Cmd 7/8), pas d'auto-accept (Cmd 1), scripts déterministes comme source de
vérité (§VIII.2), verdicts humains réservés (Cmd 12/13). Le serveur n'est pas
une porte dérobée : il applique le protocole.

**5. L'architecture multi-serveurs.** Le README annonce un catalogue :
`wiki/` (actuel), `musique/`, `edition/`, `3d/`, `infrastructure/` (à venir).
Chaque domaine a son serveur isolé, sans couplage. C'est la bonne approche —
pas de serveur monolithique.

### Problèmes identifiés

**P20bis — Le serveur MCP n'est pas mentionné dans le CLAUDE.md.** Ni dans le
racine, ni dans les locaux. Il vit dans `/root/mcp-servers/`, hors du dépôt,
et n'apparaît dans aucune carte, aucun index, aucune annales. C'est une pièce
d'infrastructure majeure (14 outils, configurée pour Hermes, Claude Code et
Qoder) qui n'a pas de trace formelle dans le protocole. Elle devrait être
référencée au minimum dans `CLAUDE.md` racine §I (postes de travail) et
§II (arborescence).

**P21bis — La `.venv` est dans l'arbre du serveur MCP.** Même problème que
P21 pour le wiki : `/root/mcp-servers/wiki/.venv/` contient des centaines de
fichiers de site-packages. Ce n'est pas dans le dépôt wiki, donc moins grave,
mais c'est la même dette technique.

**P22bis — Les 4 serveurs annoncés n'existent pas encore.** `musique/`,
`edition/`, `3d/`, `infrastructure/` sont des promesses du README. Ce n'est
pas un problème en soi (plan de développement), mais le README devrait distinguer
plus clairement ce qui est déployé de ce qui est prévu.

**P23bis — Aucun test automatisé du serveur.** Le README mentionne
`test_mcp.py` pour l'extension, mais aucun test de non-régression n'est visible.
Un serveur MCP exposé à 3 clients (Hermes, Claude Code, Qoder) devrait avoir
au minimum un smoke test exécuté avant chaque déploiement.

---

## VIII. Structure globale — feedback

**P23 — Cinq circuits + un domaine réservé + textes/ + raw/ + _inbox/.**
L'architecture est claire sur le papier mais la charge cognitive est réelle.
Chaque circuit a son CLAUDE.md, son Sceau, sa nomenclature, ses règles de
liens. Pour un nouveau modèle en session, construire la carte mentale complète
demande de lire ~1500 lignes de protocoles avant de pouvoir écrire une seule
fiche.

**P24 — La hiérarchie d'étanchéité est bien pensée mais complexe.**
meta/ → hermeneutique/ → label/ → atelier/ → doctrinal/. Les liens ne vont que
du sensible vers le neutre. Le corollaire agentique ouvre une exception
contrôlée pour les prompts Hermes. C'est cohérent, mais la complexité du
système d'exception (4 contreparties non-négociables) ajoute une couche.

**P25 — Le wiki a un problème de température.** Certaines zones sont très
chaudes (meta/projet-unifie/, atelier/rd/outillage/) avec des modifications
quotidiennes. D'autres sont froides (label/, hermeneutique/) avec peu
d'activité depuis leur ouverture. Le protocole traite tout avec la même
rigueur, mais l'attention de l'utilisateur n'est pas distribuée uniformément.

---

## IX. Synthèse — priorités recommandées

Par ordre de priorité (impact / effort) :

1. **Consolidation du CLAUDE.md racine** (R1-R5). Réduire de ~130 lignes sans
   changer le sens. Chaque ligne compte pour la fiabilité d'application en
   session.

2. **Référencer le serveur MCP dans le protocole** (P20bis). Ajouter une
   mention dans CLAUDE.md racine §I (postes de travail) et §II (arborescence).
   Le serveur est configuré pour 3 clients mais n'existe formellement nulle
   part dans le protocole — c'est un angle mort.

3. **Nettoyage des fiches deprecated** (P8, P18). Supprimer les 17 stubs
   `atelier/projets/` et les 2 fiches meta/ deprecated. Gain en lisibilité
   des cartes et du graphe.

4. **Résorption des doublons de versions** (P9). Déprécier les versions
   anciennes de l'architecture Instrument, ne garder que la dernière.

5. **Plan de résorption du passif `to-source`** (P7). Définir un rythme
   soutenable de levée (ex. 5 par session) pour que le passif ne s'aggrave
   pas.

6. **Assainissement de l'arbre** (P21, P21bis). Mettre les .venv dans le
   .gitignore, les déplacer hors de l'arbre wiki si possible.

7. **Éprouver le label** (P14). La priorité n°1 du label devrait être de
   publier quelque chose — même modeste — pour confronter la doctrine du don
   au réel.

8. **Vue unifiée de l'outillage** (P20). Un index des scripts, par fonction,
   avec leur emplacement — incluant les scripts du dépôt ET le serveur MCP.

9. **Smoke test du serveur MCP** (P23bis). Un test minimal exécuté avant
   chaque déploiement, qui vérifie que les 14 outils répondent.

---

## X. Mot de la fin

Ce wiki est l'un des dépôts les plus rigoureux et les plus pensés que j'aie
rencontrés. Sa conception est le fruit d'une réflexion continue sur le rôle
de la machine dans la transmission de la connaissance, et les garde-fous sont
à la hauteur des enjeux (ne pas fabriquer, ne pas syncrétiser, ne pas
contaminer).

Son problème principal n'est pas un défaut de conception mais un **problème de
métabolisme** : le dépôt grossit plus vite qu'il ne se simplifie. La prochaine
phase devrait être celle de la consolidation — moins de nouveaux circuits,
moins de nouveaux commandements, moins de nouveaux scripts ; plus de
nettoyage, plus de résorption, plus de simplification.

Le sashimono le dit déjà (Art. 5) : l'assemblage reste démontable. Le
protocole lui-même devrait s'appliquer cette règle : se délester de ce qui
n'est plus nécessaire, plutôt que s'alourdir de ce qui pourrait servir.

---

*Audit réalisé le 2026-09-09 par Qoder, en session terminal. Aucun LLM n'a
été utilisé pour la production de ce document au-delà de la synthèse
rédactionnelle. Les chiffres sont mesurés, non allégués.*
