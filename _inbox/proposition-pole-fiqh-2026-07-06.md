---
title: "Proposition — Pôle Fiqh, double face du Gardien du Protocole, Rapport du matin"
type: meta
tags: [outillage, projet-claude-ai, fiqh, label, gardien, hermes, proposition]
created: 2026-07-06
updated: 2026-07-06
---

# Proposition — Pôle Fiqh du dépôt et harmonisation Label ↔ Doctrine

> **Statut : proposition soumise au verdict de Sidy** (Cmd 6 : pas d'écriture de fiches
> sans plan validé). Ce document étudie et élabore la demande du 2026-07-06 :
> introduction du pôle Fiqh par reflet de l'ancrage éthique (§V.c du protocole),
> double face du Gardien du Protocole, et compte rendu matinal. Les amendements
> `CLAUDE.md` proposés figurent en §8, prêts à intégrer après validation.

---

## 1. Principe et périmètre

L'ancrage éthique (§V.c) a posé que les actes contractuels et commerciaux du label se
règlent sur les principes ancrés. Le Fiqh est précisément **la science traditionnelle
qui norme les actes** — son introduction n'est donc pas une extension arbitraire mais
le **reflet nécessaire** du §V.c : là où le §V.c disait « examinable contre les
principes », le pôle Fiqh fournit le corpus normatif de cet examen, pour les activités
relevant de son cadre.

**Périmètre initial** (chapitre des *muʿāmalāt* — transactions) :

| Acte du label | Chapitre de fiqh applicable | Observation |
|---|---|---|
| Don des 300 vinyles aux dépositaires | *hiba* (don) | Convergence remarquable : la doctrine du don du label trouve dans le fiqh de la *hiba* son cadre normatif traditionnel — conditions de validité, révocabilité, intention |
| Vente directe (Bandcamp, boutique) | *bayʿ* (vente) | Licéité de l'objet, du prix, absence de *gharar* |
| Dépôt-vente disquaires | *wadīʿa* / mandat de vente | À qualifier précisément (dépôt vs commission) |
| Contrats de collaboration | *ijāra* / *juʿāla* | Rémunération des prestations |
| Registre de transmission (idée long terme) | à instruire | Le « bénéfice émergent jamais promis » devra aussi être examiné contre *riba* et *gharar* |
| Actifs de la structure | *zakāt* des biens de commerce | Pont existant en bibliothèque : Gilis, *Métaphysique de la Zakât* |

Ce tableau est un **amorçage** : chaque ligne appelle sa fiche sourcée (`to-source`
tant que non vérifiée sur texte malikite).

---

## 2. Règle de préséance des madhāhib

1. **École de référence : le madhhab mālikite** (Imam Mālik b. Anas). Toute question
   est d'abord instruite dans ses sources.
2. **Subsidiarité** : à défaut de ressource malikite accessible sur la question, recours
   aux écoles shāfiʿite, ḥanafite ou ḥanbalite — **documenté question par question**,
   avec justification explicite (« à défaut de ressource malikite sur ce point »).
3. **Jamais de talfīq silencieux** : on ne compose pas un même acte à partir de morceaux
   d'écoles différentes choisis par commodité. Le recours subsidiaire porte sur une
   question entière, il est signalé, et la position retenue est attribuée à son école.
   (Ce principe est lui-même une exigence classique du fiqh ; il est aussi l'exact
   analogue du Commandement 3 — non-syncrétisme — appliqué à l'intérieur de la
   tradition islamique : convergence montrée, formes jamais confondues.)
4. **Branche ḥanbalite — ressource de référence** : Al-Madrasah Al-Hanbaliyyah
   (almadrasahalhanbaliyyah.com) — institut traditionnel à chaînes de transmission
   (asānīd) et ijāzāt, cursus gradué (Akhṣar al-Mukhtaṣarāt d'Ibn Balbān → ʿUmdat
   al-Ṭālib → al-Iqnāʿ / al-Muntahā), enseignement disponible en anglais et en
   français. Point de convergence méthodologique : leur pédagogie proscrit le fiqh
   comparatif avant la maîtrise d'une seule école — ce qui conforte la préséance
   malikite du présent protocole. → fiche `doctrinal/sources/` à créer.
5. **Bibliothèque physique — constat et acquisitions** : la recension du 2026-06-28 ne
   contient **aucun manuel de fiqh mālikite**. Candidats classiques à l'acquisition
   (traductions françaises existantes, à vérifier par Sidy) : *al-Muwaṭṭaʾ* (Imam
   Mālik), *al-Risāla* d'Ibn Abī Zayd al-Qayrawānī, *Mukhtaṣar* d'al-Akhḍarī
   (ʿibādāt), *Mukhtaṣar Khalīl* (référence de l'école, pour les muʿāmalāt). Le
   *Kitāb al-Taʿrīfāt* de Jurjānī (possédé) fournit dès maintenant le **lexique**
   (thème B de son index : ≈ 250 définitions de droit). Cohérence d'héritage : la
   bibliothèque porte déjà l'aire malikite ouest-africaine (Cheikh Ahmadou Bamba).

---

## 3. Logement dans le dépôt — sans mutation du Sceau

Le pôle Fiqh s'installe **dans la structure existante** (aucune modification du Sceau
Recteur ni de l'arborescence — option conservatrice, réversible) :

- **`doctrinal/traditions/madhhab-maliki.md`** — l'école comme forme traditionnelle
  (et, au besoin, fiches sœurs des trois autres écoles, créées à la première occurrence
  d'un recours subsidiaire).
- **`doctrinal/autorites/imam-malik.md`** — puis, au fil des sources : Ibn Abī Zayd
  al-Qayrawānī, Khalīl b. Isḥāq, al-Akhḍarī…
- **`doctrinal/symboles/fiqh.md`** — la science elle-même (les sciences
  traditionnelles vivent déjà en `symboles/` : logique, ʿilm al-ḥurūf…), avec au
  besoin des pages de chapitre (`fiqh-al-hiba`, `fiqh-al-buyu`) quand le volume le
  justifie (une page = un sujet).
- **`doctrinal/sources/`** — fiches des textes et ressources (al-Risāla, Mukhtaṣar
  Khalīl, al-madrasah-al-hanbaliyyah…), statut selon nature.
- **Questions appliquées** : `doctrinal/etudes/YYYY-MM-DD_<question>.md` — une
  question de fiqh instruite = une étude datée portant le **bloc ⚖️** (§4). La fiche
  reste **générale et neutre** (ex. « Statut du dépôt-vente en fiqh mālikite »), sans
  jamais mentionner le label (étanchéité).
- **Application au cas concret** : fiche `label/administratif/` (ou du pôle concerné)
  qui cite la fiche doctrinale **à sens unique**, et ne porte que la conséquence de
  conduite (ex. clause à retirer d'un contrat).

**Alternative (non recommandée à ce stade)** : sous-dossier dédié `doctrinal/fiqh/` +
`type: fiqh` au Sceau. À n'ouvrir que si le volume des fiches l'exige — c'est une
mutation du protocole (ordre humain requis), réexaminable au premier bilan du pôle.

---

## 4. Bloc normalisé « ⚖️ Statut de Fiqh »

À insérer dans toute étude de question de fiqh (miroir du bloc 🔍 du discernement) :

> ⚖️ **Statut de Fiqh**
> **Question** : formulée en termes généraux, sans mention du cas d'application.
> **École consultée** : mālikite (défaut) | shāfiʿite | ḥanafite | ḥanbalite.
> **Position(s) sourcée(s)** : texte, auteur, référence — `to-source` si non vérifié.
> **Recours subsidiaire** (le cas échéant) : école + justification (« à défaut de
> ressource malikite sur ce point ») — jamais de talfīq.
> **Divergences notables** : signalées sans être fondues (🌐 si inter-écoles).
> **Verdict** : adopté par Sidy (taqlīd documenté d'une position établie) | confirmé
> par autorité textuelle citée | **renvoyé au savant qualifié** (question restée
> ouverte) — jamais décrété par la machine.
> **Date du verdict** : YYYY-MM-DD.

Rappel du cadre (Cmd 12, *upakarana*) : la machine **compile, source et structure** les
positions ; elle n'émet **jamais** d'avis juridique religieux. Le « trancher » de Sidy
est un **arbitrage d'adoption** : choisir, parmi des positions établies et sourcées,
celle sur laquelle la structure règle sa conduite — et/ou la confirmer. Pour les cas
nouveaux, sans texte, ou engageant une application personnelle, la fiche prépare la
**formulation de la question** (istiftāʾ) et reste ouverte jusqu'à consultation d'une
autorité vivante qualifiée, si Sidy en décide — même régime que la règle existante sur
l'autorité spirituelle (briefing, vigilances récurrentes).

---

## 5. La double face du Gardien du Protocole

Élaboration de la suggestion : le Gardien (agent 10) devient l'**interface
d'harmonisation** entre les deux pôles — une face tournée vers `label/`, une face
tournée vers le corpus fiqh de `doctrinal/`.

**Extension de périmètre (agent 10)** :
1. **Lecture** (jamais d'écriture) des fiches fiqh doctrinales, en plus de son
   périmètre label actuel.
2. **Cartographie** : pour tout plan, contrat, produit ou texte public produit par un
   autre agent, identifier le(s) chapitre(s) de fiqh applicable(s) (table §1).
3. **Trois signaux possibles** : ✅ conforme à la position adoptée (fiche citée) ;
   ⚠️ non-conformité ou zone grise (fiche citée, phrase exacte pointée, correction
   proposée) ; ❓ **absence de fiche** — le chapitre applicable n'est pas encore
   instruit → demande de recherche (vers l'agent 04) et inscription au Rapport du
   matin.
4. **Toujours signaler, jamais statuer** : le Gardien cite, pointe, propose, s'arrête.
   Le verdict ⚖️ appartient à Sidy (§4).

**Répartition avec l'agent 04 (Administration & Legal)** — pas de 13ᵉ agent :
- **04 instruit** : à son périmètre actuel (droit positif français : Sacem, SDRM,
  structures) s'ajoute le **référencement fiqh** — compiler les positions sourcées
  selon la préséance §2, préparer les fiches ⚖️ candidates. Son archétype est déjà
  **Gardien** ; la fonction reste une (veille des limites, deux ordres normatifs).
- **10 harmonise** : il consomme les fiches produites, confronte les actes, alerte.
- **Conflit entre les deux ordres normatifs** (droit positif ↔ fiqh) : ni 04 ni 10 ne
  hiérarchise — dossier des deux côtés, **escalade à Sidy** (Cmd 13).
- Motif du choix : la fiche `discernement/2026-07-05_correspondances-…` a elle-même
  noté qu'une 13ᵉ fonction fragiliserait la correspondance duodénaire (suggérée 🔍).
  Étendre 04 préserve les 12 fonctions **et** évite de créer une fonction pour un
  besoin qui est structurellement une veille de limites. Si Sidy préfère néanmoins un
  agent dédié « Recherche Fiqh », la fiche discernement devra être réexaminée (son
  propre examen formel le prévoit).

**Note de discernement** : la formule « une face tournée vers chaque pôle » évoque
immédiatement le Barzakh (l'isthme aux deux faces). Conformément au Cmd 3 et au régime
des correspondances de l'Instrument, cette évocation reste **suggérée (🔍)** — belle,
plausible, non tranchée. Elle peut être versée à la fiche discernement du 2026-07-05
(le Gardien y est déjà l'un des cinq archétypes) plutôt que d'ouvrir une fiche
séparée. Les documents opératifs (prompts, protocole) emploient le terme neutre
« interface d'harmonisation ».

---

## 6. Le Rapport du matin (spécification)

**Objet** : compte rendu quotidien soumis à l'attention de Sidy, listant ce qui
requiert l'Intellect humain — et rien d'autre. C'est l'incarnation quotidienne du
principe « les agents signalent, l'humain tranche ».

**Sections normalisées** (ordre fixe, sections vides omises) :

1. **Verdicts en attente** — fiches ⚖️ ouvertes, discernements 🔍 non tranchés,
   correspondances suggérées, tensions Commerce ↔ Gardien à arbitrer.
2. **Tâches de Sidy** — références de fiqh à rapporter de l'extérieur (textes à
   consulter, acquisitions bibliothèque, question à porter à un savant), documents à
   remplir ou signer, décisions de nommage, validations `clarify` en attente.
3. **Signaux du Gardien** — non-conformités ⚠️ et chapitres non instruits ❓ relevés
   depuis le dernier rapport.
4. **Échéances** — délais administratifs (04 : Sacem/SDRM, semaines d'inscription),
   jalons de production (03), fenêtres de publication.
5. **État des sas** — contenu de `_inbox/`, cycles `compare` réussis/attendus,
   lots en attente d'intégration.
6. **Divers** — rappels personnels et éléments récréatifs, **session séparée**
   (étanchéité de la dimension personnelle, briefing 10 §6).

**Règles** : signalement pur — le rapport ne déclenche rien ; chaque item pointe la
fiche ou le canal où agir ; pas d'inférence doctrinale (la mémoire d'agent reste
opérationnelle, §VIII.7 du protocole).

**Incarnations** :
- **Cible (Hermes, Phase 3+)** : cron quotidien de la gateway, compilé par le Gardien
  (lecture transversale — c'est déjà sa nature), livré sur **WhatsApp** (canal
  préféré), copie possible sur Discord avec boutons `clarify` pour les validations
  d'un tap.
- **Intermédiaire (dès maintenant)** : consigne manuelle en ouverture de session —
  « fais-moi le Rapport du matin » — servie depuis les backlogs (`04-sessions-…`),
  les index et les fiches ouvertes. Le format §6 s'applique dès la version manuelle,
  pour roder la structure avant l'automatisation.

---

## 7. Ce que le pôle ne change pas

- Le Fiqh entre au dépôt comme **corpus doctrinal sourcé**, pas comme service de
  fatwa : Cmd 5 et discipline des sources s'appliquent intégralement (`to-source`
  levé sur texte primaire, positions attribuées à leur école et leur ouvrage).
- L'étanchéité demeure : les fiches fiqh doctrinales ignorent le label ; le label
  cite à sens unique.
- Le verdict appartient à Sidy ou à l'autorité qualifiée (Cmd 12/13) — la machine
  prépare, structure, signale.

---

## 8. Amendements `CLAUDE.md` proposés (texte exact, à intégrer après validation)

**8.1 — §V.c, ajout d'un point 6 :**

> 6. **Alignement Fiqh** : pour les activités relevant de son cadre (transactions,
>    dons, contrats), la structure règle sa conduite sur le **fiqh**, école
>    **mālikite** en préséance ; à défaut de ressource malikite, recours subsidiaire
>    documenté aux écoles shāfiʿite, ḥanafite ou ḥanbalite — question par question,
>    **jamais de talfīq silencieux**. Chaque question instruite = une étude datée
>    portant le bloc ⚖️ (§VII) ; le Gardien du Protocole harmonise (une face vers le
>    label, une face vers le corpus fiqh doctrinal) en **signalant** ; le verdict
>    d'adoption appartient à l'humain (Cmd 13), le renvoi au savant qualifié restant
>    toujours ouvert pour les cas nouveaux.

**8.2 — §VII, blocs normalisés (ARCHIVAGE), ajout :**

> ⚖️ **Statut de Fiqh** : [Question générale · École consultée · Position(s)
> sourcée(s) · Recours subsidiaire justifié le cas échéant · Divergences signalées ·
> Verdict : Sidy / autorité citée / renvoyé au savant qualifié · Date].

**8.3 — §I, ligne AGENTS DE FONCTION, complément :**

> Sortie quotidienne normalisée : le **Rapport du matin** (signalement pur, sections
> fixes, canal WhatsApp) — voir `meta/projet-unifie/` pour la spécification.

---

## 9. Ordre des opérations (après verdict de Sidy sur la présente proposition)

1. **Amender `CLAUDE.md`** (§8) — lot de maintenance protocolaire, ordre humain.
2. **Fiches d'amorçage du pôle** (lot `_inbox/` + UPDATES) :
   `traditions/madhhab-maliki`, `autorites/imam-malik`, `symboles/fiqh`,
   `sources/al-madrasah-al-hanbaliyyah` — toutes sobres, `to-source` là où le texte
   physique manque.
3. **Première étude ⚖️ pilote** : la *hiba* (le don) — c'est le cœur battant du label
   et le meilleur test du bloc normalisé.
4. **Mise à jour des prompts** agents 04 et 10 (`meta/projet-unifie/hermes-prompts/`)
   selon §5 — versions anglaises, patch minimal.
5. **Vigilance documentaire** : refléter le pôle dans `10-briefing-…hermes` (§5-6),
   `00-instructions-projet` et `briefing-claude-ai` ; ajouter les acquisitions
   malikites (§2.5) au backlog et à `meta/bibliotheque-physique.md` (section
   « à acquérir »).
6. **Rapport du matin** : roder la version manuelle dès la prochaine session ;
   automatiser en Phase 3 Hermes.
