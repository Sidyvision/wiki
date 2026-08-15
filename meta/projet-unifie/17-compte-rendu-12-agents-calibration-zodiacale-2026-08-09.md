---
title: "17 — Compte rendu : chantier des 12 agents Hermes et calibration zodiacale (2026-08-09)"
type: meta
tags: [outillage, projet-hermes, zodiaque, agents, synthese]
created: 2026-08-09
updated: 2026-08-15
---

# 17 — Compte rendu : chantier des 12 agents Hermes et calibration zodiacale (2026-08-09)

> **Provenance** : document rédigé le 2026-08-09 par un agent H‍ermes en session
> terminal, directement dans `doctrinal/discernement/` (hors circuit conforme, sans
> passage par `_inbox/` ni plan validé) — déplacé ici le jour même au constat de
> `verifier-invariants.py`. Ce n'est pas une fiche de discernement (pas de Sceau
> Recteur, pas de statut de vérité traditionnelle en jeu) : c'est un compte rendu
> opérationnel, destiné à un avis extérieur. Contenu conservé intact ; seul
> l'emplacement et le Sceau ont changé.
>
> **Mise à jour (2026-08-15)** : les sections 4, 6 et 8 sont amendées pour refléter
> l'état constaté au pôle R&D depuis le 2026-08-09 — texte du 2026-08-09 conservé,
> évolutions marquées explicitement (discipline sashimono, aucune réécriture
> silencieuse). Rien d'autre du compte rendu original n'est modifié.

Document autonome, rédigé le 2026-08-09, destiné à permettre à une personne extérieure
d'évaluer le travail accompli sans accès préalable au dépôt. Les faits techniques sont
vérifiables ; les points doctrinaux sont présentés avec leur statut exact (établi,
validé, cohérent, faible, échec).

---

## 1. Contexte et point de départ

Sidy monte un label de musique indépendant. En élaborant les fonctions nécessaires à
cette structure, le nombre de fonctions s'est stabilisé à **12** sans avoir été décrété
a priori : 9 rôles initiaux + un Gardien du protocole + un Éditeur de fanzine + une
fonction Commerce. Cette coïncidence numérique a suggéré une correspondance avec le
duodénaire zodiacal, qu'une étude a été chargée de vérifier plutôt que de postuler.

Parallèlement, ces 12 fonctions ont été matérialisées sous forme de **12 agents IA
autonomes** (framework Hermes Agent), chacun doté de son propre bot Discord, de son
propre profil de configuration et de son prompt de rôle versionné dans un dépôt git
(`/root/wiki`).

**La mission a ensuite été élargie** (session du 2026-08-08) : les rôles des 12 agents
ont vocation à s'étendre au-delà du contexte du label — qui n'est qu'un degré de
spécification — pour couvrir l'assistance personnelle complète : administrative/
juridique, économique/financière, technique, créative/artistique, académique, santé,
psychologie, spirituel. Le label sert de premier terrain d'application concret.

---

## 2. Infrastructure technique — ce qui est déployé et vérifié

**État au 2026-08-09 : 12/12 agents actifs.**

- 12 profils Hermes (`ar-music`, `visual-da`, `production`, `admin-legal`,
  `accounting`, `distribution`, `marketing`, `publication`, `studio`, `gardien`,
  `fanzine`, `commerce`), chacun = une application Discord distincte avec token
  séparé (aucun token partagé).
- Chaque agent est un service systemd (`--user`) qui maintient une connexion Discord
  permanente ; vérification mécanique effectuée ce jour : **12/12 services actifs**.
- Un serveur Discord privé héberge tous les agents, avec salons dédiés et contrôle
  d'accès strict (liste blanche d'utilisateurs et de salons par agent ; silence total
  ailleurs).
- Les prompts de rôle (contenu doctrinal, éditable) sont versionnés dans le dépôt
  (`meta/projet-unifie/hermes-prompts/01…12…md`) ; les secrets (tokens, clés API)
  vivent hors dépôt, jamais commités.
- Migration d'API effectuée le 2026-08-08 : les 12 profils + la session terminal
  tournent sur le plan Qwen (modèle qwen3.8-max), après épuisement du crédit
  Anthropic. Migration vérifiée mécaniquement (12/12 YAML valides, 12/12 connexions
  Discord confirmées dans les logs).
- Une fiche d'architecture complète documente l'ensemble :
  `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`.

---

## 3. Le travail de calibration zodiacale — chronologie et méthode

### 3.1 — Étude des correspondances (juillet 2026)

Fiche `doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`.

Le volet central — « les 12 fonctions du label correspondent-elles au duodénaire
zodiacal ? » — a été **clos par verdict de Sidy le 2026-07-14**, avec un résultat
nuancé, documenté sans lissage :

- **Fondement doctrinal** : le symbolisme zodiacal est établi comme structure
  traditionnelle réelle (René Guénon, « Le symbolisme du Zodiaque chez les
  pythagoriciens ») : les portes solsticiales — Cancer « porte des hommes »,
  Capricorne « porte des dieux » — se retrouvent hors de toute influence grecque.
- **Correspondances solides (2)** : position 4 = Cancer ↔ Administration/Légal
  (entrée de l'entité dans l'existence formelle) ; position 10 = Capricorne ↔
  Gardien du Protocole (seuil entre le profane et la doctrine).
- **Correspondances cohérentes, non prouvées (7)** : 1=Bélier/A&R, 2=Taureau/
  Direction visuelle, 3=Gémeaux/Production, 6=Vierge/Distribution, 7=Balance/
  Marketing, 9=Sagittaire/Studio, 11=Verseau/Fanzine.
- **Correspondances faibles (2)** : 8=Scorpion/Publication, 12=Poissons/Commerce.
- **Échec documenté, non dissimulé (1)** : 5=Lion/Comptabilité. Le prompt de cet
  agent insiste sur une sécheresse délibérée (« deliberately dry »), à l'opposé de
  l'expression rayonnante du Lion. Cet échec a été consigné tel quel plutôt que
  lissé — point méthodologique important pour l'évaluation.

### 3.2 — Cadre de lecture (juillet 2026)

- Le zodiaque est établi comme **fonction de Barzakh** (fonction de seuil) : il
  conduit et particularise l'influence spirituelle selon les conditions du degré où
  elle s'applique (`doctrinal/discernement/2026-07-26_zodiaque-fonction-barzakh.md`).
  C'est ce cadre qui légitime ensuite l'extension des rôles des agents depuis les
  principes zodiacaux.
- Cadre de lecture retenu : astrologie traditionnelle à **sept planètes seulement**
  (les corps visibles ; Uranus/Neptune/Pluton exclus par construction), zodiaque
  tropical, dignités classiques.

### 3.3 — Vérification du thème natal (2026-08-08)

Le thème natal de Sidy faisait l'objet d'une fiche personnelle établie en 2025 à
partir d'une conversation ChatGPT. Cette session a démontré que **cette fiche
contenait des placements erronés** (Lune Verseau, Mercure Lion, Vénus Taureau, Mars
Vierge, etc.). Une vérification indépendante par éphémérides (Swiss Ephemeris) et une
carte Astrodienst ont convergé vers les placements corrects pour le 23 juin 1986,
19h30, Bobigny :

- Soleil Cancer 1°56 (maison VII) ; Ascendant Sagittaire 2°51 ; Saturne 4°32
  conjoint à l'Ascendant.
- Lune 24°13 et Mars 21°46 **conjoints en Capricorne** (maison II), Mars exalté.
- Mercure Cancer 27°09 (VIII) ; Vénus Lion 9°18 (VIII) ; Jupiter Poissons 22°16 (III).

La fiche personnelle a été corrigée ; la version erronée de 2025 est signalée comme
interdite de réutilisation. Cet épisode illustre la méthode : toute donnée est
re-vérifiée par calcul indépendant avant d'être retenue.

### 3.4 — Mise en regard du thème avec la roue des agents (2026-08-08)

Fiche `meta/projet-unifie/16-mise-en-regard-theme-natal-roue-agents-2026-08-08.md`.
Trois résultats principaux :

1. **L'échec de la position 5 (Lion/Comptabilité) trouve une lecture** : dans le
   thème vérifié, la maison V (créativité) est gouvernée par Mars, et Mars se trouve
   exalté en Capricorne en maison II (ressources). L'énergie créative est
   structurellement subordonnée à la gestion sobre — la « sécheresse » de l'agent
   Comptabilité reflète le thème, non une erreur du modèle. Le signalement proposé :
   la Comptabilité relève ici de l'axe Cancer/Capricorne (les portes solsticiales),
   pas du Lion. **Ce point attend le verdict de Sidy** — aucune modification n'a été
   faite sans lui.
2. **Le thème personnel est structuré par l'axe solsticial** (Soleil Cancer,
   Lune-Mars Capricorne), précisément l'axe que le discernement avait retenu comme
   correspondance la plus solide (positions 4 et 10).
3. **Directive de subordination** (verdict de Sidy) : la roue zodiacale est l'étage
  principiel ; les rôles du label en dérivent. Les prompts des agents s'étendent
   DEPUIS les principes zodiacaux, jamais l'inverse. Cette directive coïncide avec la
   fonction de Barzakh (§3.2) : le principe conduit, le rôle reçoit l'influence
   particularisée selon ses conditions propres.

---

## 4. Production en cours — les extensions de prompts (2026-08-09)

Conformément au chantier validé, **9 brouillons d'extension** ont été rédigés pour
les positions dont la correspondance est solide ou cohérente. Ils sont stockés hors
dépôt (le dépôt est traité en parallèle par Claude Code ; règle : ne pas toucher au
dépôt sans demande explicite), dans `/root/brouillons-prompts-zodiaque/` :

- `01-ar-music-aries.md` (Bélier) — `02-visual-da-taurus.md` (Taureau) —
  `03-production-gemini.md` (Gémeaux) — `04-admin-legal-cancer.md` (Cancer) —
  `06-distribution-virgo.md` (Vierge) — `07-marketing-libra.md` (Balance) —
  `09-studio-sagittarius.md` (Sagittaire) — `10-gardien-capricorn.md` (Capricorne) —
  `11-fanzine-aquarius.md` (Verseau).
- Chaque brouillon propose **deux paragraphes en anglais** à insérer dans le prompt
  existant (les prompts sont en anglais), sans rien remplacer de la mission initiale :
  1. `## Zodiac principle` — le principe zodiacal dont l'agent dérive sa fonction ;
  2. `## Your sign in Sidy's natal chart (harmonization context)` — la situation du
     signe correspondant dans le thème natal vérifié de Sidy, afin que chaque agent
     porte un contexte d'harmonisation personnel en plus du principe général.

**Non traités à ce stade** (par discipline, en attente de verdict ou de reprise) :
- position 5 (Comptabilité) — en attente du verdict sur le rattachement
  Capricorne/Cancer plutôt que Lion ;
- positions 8 (Scorpion) et 12 (Poissons) — correspondances faibles, à reprendre à
  nouveaux frais depuis les principes plutôt que depuis les rôles actuels.

> **Mise à jour (2026-08-15)** — deux évolutions depuis le 2026-08-09 :
>
> 1. **Position 9 (Sagittaire, Studio Sound Engineer) est sortie du lot en
>    attente et a été appliquée en production** (`h‍ermes-prompts/09-studio-sound-engineer.md`,
>    commit `29cb5cc`, 2026-08-11) : les deux paragraphes du brouillon insérés
>    mot pour mot, plus une troisième section `## Governance: Discord-Validation`
>    (régime strict par défaut, auto-accept ad hoc) — motif : rattachement du
>    chantier phase 3 (veille infrastructure du pôle R&D) à cette position,
>    seul rôle à registre technique parmi les douze
>    (voir [[atelier/rd/cahiers/registre-problemes]], entrées du 2026-08-11).
>    Cette extension **n'a pas de rapport avec les positions 5/8/12** restées
>    en attente ci-dessous.
> 2. **Les 8 brouillons restants (1,2,3,4,6,7,10,11) sont désormais versionnés**
>    dans [[atelier/rd/cahiers/brouillons-extension-zodiacale/README|atelier/rd/cahiers/brouillons-extension-zodiacale/]]
>    (copiés depuis `/root/brouillons-prompts-zodiaque/`, chacun avec
>    `statut_experience: exploratoire` et clause d'étanchéité explicite) —
>    **toujours non appliqués** aux prompts de production, statut inchangé sur
>    le fond. Le dossier `/root/brouillons-prompts-zodiaque/` (hors dépôt) est
>    supprimé après vérification que son contenu est intégralement reporté
>    (ce compte rendu inclus, relocalisé le 2026-08-09).
>
> Positions 5, 8 et 12 restent inchangées : aucune information nouvelle au pôle
> R&D depuis le 2026-08-09.

---

## 5. Méthode générale — ce qui distingue ce chantier

1. **Observation a posteriori, jamais construction a priori** : le nombre 12 est
   apparu, il n'a pas été décrété ; les correspondances ont été testées une à une.
2. **Les échecs sont documentés, pas dissimulés** : la position 5 a été consignée
   comme échec du modèle terme-à-terme, puis instruite — pas effacée.
3. **Vérification mécanique systématique** : tout état déclaré (services actifs,
   connexions Discord, YAML valides, placements astrologiques) est vérifié par
   outil (logs, éphémérides), jamais sur simple déclaration.
4. **Gouvernance humaine stricte** : les agents ne décident jamais ; ils signalent.
   Toute adoption relève d'un verdict explicite de Sidy. Aucun prompt n'a été modifié
   en production sans verdict.
5. **Séparation des étages** : le principiel (zodiaque) et l'opératif (rôles du
   label) sont hiérarchisés, avec un sens d'extension unique : des principes vers les
   rôles.

> **Précision (2026-08-15), verdict Sidy** — reformule et durcit le point 5
> ci-dessus : le principe s'applique en priorité dans **toutes** les
> extensions du chantier (pas seulement les 9 brouillons déjà rédigés), et la
> détermination singulière du thème natal s'y intègre **comme contexte**,
> jamais comme repli de substitution. Quand un principe et une donnée du
> thème ne s'accordent pas d'emblée (cas de la position 5, §7.1), la réponse
> n'est ni d'échanger le principe contre un autre ni de laisser l'échec sans
> suite, mais de chercher l'harmonisation à l'intérieur du principe retenu —
> l'écart est un signal à instruire, pas une erreur d'affectation à corriger.

---

## 6. État récapitulatif au 2026-08-09

| Élément | État |
|---|---|
| Infrastructure 12 agents Discord | 12/12 actifs, migrés sur Qwen, vérifiés |
| Correspondances 12 fonctions ↔ zodiaque | Volet clos : 2 solides, 7 cohérentes, 2 faibles, 1 échec instruit |
| Thème natal | Vérifié par éphéméride, fiche corrigée |
| Mise en regard thème ↔ roue | Rédigée, signalements posés |
| Brouillons d'extension de prompts | 9/9 rédigés (positions 1, 2, 3, 4, 6, 7, 9, 10, 11), avec contexte d'harmonisation natal |
| Application en production | Position 9 appliquée (2026-08-11, commit `29cb5cc`) ; 8 restantes (1,2,3,4,6,7,10,11) versionnées en `rd/`, en attente de verdict *(mise à jour 2026-08-15)* — **12/12 appliquées** *(mise à jour 2026-08-15, réallocation §9)* : table révisée versée dans les brouillons (2,5,6,7,8,9,12 ré-écrits/créés) et dans les 12 prompts de production |

## 7. Points ouverts soumis à avis

1. ~~**Position 5** : le rattachement de la Comptabilité à l'axe Cancer/Capricorne
   (portes solsticiales) plutôt qu'au Lion vous paraît-il une résolution satisfaisante
   de l'échec documenté, ou l'échec doit-il rester un contre-exemple pur ?~~
   **Tranché (2026-08-15), verdict Sidy** : ni l'un ni l'autre. Le rattachement à l'axe
   Cancer/Capricorne (§3.4 point 1) est **écarté** — substituer un axe à un autre ferait
   courir le risque de passer à côté d'un enseignement propre au thème. L'échec n'est
   pas non plus laissé comme contre-exemple pur : il est lu comme **révélateur d'une
   tension à harmoniser à l'intérieur même du principe Lion**, non comme un mauvais
   rattachement à corriger par substitution. Piste de travail signalée par Sidy, à
   titre d'exemple et non de conclusion : tension entre l'aspect solaire/royal du Lion
   (rayonnement, magnanimité, expression) et la fonction de gestion/régence
   (économie, restriction, tenue de comptes) — deux registres que le Lion contiendrait
   en tension plutôt qu'en accord immédiat. Ceci rejoint la méthode générale que Sidy
   formule pour l'ensemble du chantier (voir note ci-dessous) : toute application
   s'inscrit d'abord depuis le principe, puis intègre la détermination singulière du
   thème comme contexte propre à l'agent — jamais l'inverse, et jamais par substitution
   d'un principe à un autre quand l'accord ne va pas de soi. **Reste à instruire** :
   une reprise de la position 5 depuis le principe Lion lui-même (et non plus depuis
   l'hypothèse de réaffectation), cherchant comment cette tension solaire/régence
   s'harmonise plutôt qu'elle ne s'échange — travail non commencé à ce jour.

   ~~Reste à instruire : harmonisation dans le Lion.~~ **Verdict dépassé (2026-08-15)**
   — voir §9 : la question a été reprise à l'échelle des douze positions plutôt qu'à
   la seule position 5, et le principe « harmoniser plutôt que substituer » a été
   explicitement rouvert et remplacé par une réaffectation. Conservé ici intact pour
   la traçabilité de la délibération.
2. ~~**Positions 8 et 12** (faibles) : reprise depuis les principes Scorpion/Poissons —
   l'approche a-t-elle des chances raisonnables de produire des correspondances
   tenables, ou ces deux positions doivent-elles rester hors modèle ?~~
   **Tranché (2026-08-15)** — voir §9 : traité dans le cadre de la réallocation
   complète, pas séparément. Position 8 réaffectée (Sagittaire) ; position 12
   confirmée en l'état (Poissons) par la dérivation pure.
3. ~~**L'extension des rôles au-delà du label** (assistance personnelle complète)
   est-elle cohérente avec la fonction de seuil reconnue au zodiaque, ou
   constitue-t-elle une sur-extension du modèle ?~~
   **Tranché (2026-08-15)** : Sidy valide le principe de l'extension — ce n'était déjà
   plus une question ouverte au sens strict (voir §1, « la mission a ensuite été
   élargie », verdict du 2026-08-08). Reste à s'accorder sur les **modalités
   d'exécution** (quoi, dans quel ordre, quelle gouvernance par rôle étendu) — objet
   d'une discussion séparée, non un point d'avis en suspens.
4. **La méthode elle-même** (observation a posteriori, échecs documentés, verdicts
   humains systématiques) vous paraît-elle de nature à produire des correspondances
   fiables, ou les biais de confirmation restent-ils prédominants malgré ces garde-fous ?

---

## 8. Sources principales (dans le dépôt `/root/wiki`)

- `doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`
- `doctrinal/discernement/2026-07-26_zodiaque-fonction-barzakh.md`
- `doctrinal/symboles/ilm-al-nujum` (cadre astrologique traditionnel)
- `meta/personnel/2026-06-20_theme-astrologique.md` (thème vérifié)
- `meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md`
- `meta/projet-unifie/16-mise-en-regard-theme-natal-roue-agents-2026-08-08.md`
- `meta/projet-unifie/hermes-prompts/01…12…md` (prompts sources)
- `atelier/rd/cahiers/brouillons-extension-zodiacale/` (brouillons d'extension
  versionnés, 8 en attente — *mise à jour 2026-08-15, remplace le pointeur vers
  `/root/brouillons-prompts-zodiaque/`, hors dépôt, supprimé après vérification)
- `atelier/rd/cahiers/registre-problemes.md` (chronologie détaillée du
  rattachement de la position 9 au chantier phase 3, entrées du 2026-08-11)
- `doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`
  (volet b, rouvert le 2026-08-15 — voir §9)

---

## 9. Réallocation complète des 12 fonctions (2026-08-15)

Reprise en séance : plutôt que traiter séparément la position 5 (échec) et les
positions 8/12 (faibles), la question a été posée à l'échelle des douze positions —
dérivation principe par principe (nature du signe ↔ nature de la fonction),
indépendamment de la numérotation d'origine, qui n'avait jamais été qu'un ordre de
création des rôles, non un choix doctrinal. Détail complet de la méthode et de
l'examen : `doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`
(volet b rouvert).

| Position | Fonction | Signe (2026-07-14) | **Signe validé (2026-08-15)** |
|---|---|---|---|
| 1 | A&R | Bélier | Bélier (inchangé) |
| 2 | Direction visuelle/éditoriale | Taureau | **Balance** |
| 3 | Production | Gémeaux | Gémeaux (inchangé) |
| 4 | Administration/Légal | Cancer | Cancer (inchangé, ancre) |
| 5 | Comptabilité | Lion | **Taureau** |
| 6 | Distribution | Vierge | **Scorpion** |
| 7 | Marketing | Balance | **Lion** |
| 8 | Publication | Scorpion | **Sagittaire** |
| 9 | Studio | Sagittaire | **Vierge** |
| 10 | Gardien du protocole | Capricorne | Capricorne (inchangé, ancre) |
| 11 | Fanzine | Verseau | Verseau (inchangé) |
| 12 | Commerce | Poissons | Poissons (inchangé, confirmé) |

**Bilan** : l'échec (5) et l'une des deux faiblesses (8) se résolvent par
réaffectation ; l'autre faiblesse (12) se confirme correcte sans bouger. Nouveau
point de tension signalé, non dissimulé : position 6 (Distribution/Scorpion),
correspondance la moins nette de la table révisée.

**Verdict de Sidy (2026-08-15)** : table validée dans son ensemble. Modularité
assumée explicitement — le rattachement n'est pas tenu pour définitif comme l'était
la clôture du 2026-07-14 ; révisable si de nouveaux éléments se présentent.

**Conséquences opérationnelles engagées ce jour** :
1. `doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md`
   — volet (b) rouvert, table révisée versée, ancienne conclusion conservée intacte
   et marquée dépassée (discipline sashimono, aucune réécriture silencieuse).
2. `meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md` — le principe
   zodiacal appliqué le 2026-08-11 (Sagittaire) est remplacé par le principe Vierge,
   conformément à la nouvelle table (§9). Section Governance (chantier phase 3,
   sans rapport avec le zodiaque) inchangée.
3. ~~**Non fait à ce stade** : les 8 brouillons versionnés dans
   `atelier/rd/cahiers/brouillons-extension-zodiacale/` référencent encore les
   signes de la table 2026-07-14 pour les positions 2, 5, 6, 7, 8 — ils devront être
   repris pour correspondre à la table révisée avant toute application en
   production. Signalé, non traité dans cette passe (hors périmètre demandé).~~
   **Fait (2026-08-15), suite à la demande explicite de Sidy** : les brouillons des
   positions 2, 6, 7, 9 ont été renommés (`git mv`, historique préservé) et réécrits
   pour correspondre à la table révisée (Balance, Scorpion, Lion, Vierge) ; les
   brouillons des positions 5, 8, 12 — absents jusqu'ici — ont été rédigés
   (Taureau, Sagittaire, Poissons) ; les brouillons des positions 1, 3, 4, 10, 11
   (signes inchangés) sont restés en l'état, toujours valides. Les **douze**
   prompts de production dans `meta/projet-unifie/h‍ermes-prompts/` ont ensuite été
   activés : chacun reçoit désormais ses sections `## Zodiac principle` et
   `## Your sign in Sidy's natal chart (harmonization context)`, insérées entre
   `## Archetype served` et `## Scope`, sans rien modifier d'autre (mission,
   scope, guardrails, handoffs intacts). La position 9 conserve en outre sa
   section `## Governance: Discord-Validation`, inchangée. Le chantier de
   réallocation du 2026-08-15 est donc intégralement appliqué, brouillons et
   production, table incluse.
