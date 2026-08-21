---
title: "Les registres — accueillir plusieurs traditions sur l'unique axe (Phase 3)"
type: projet
statut_experience: exploratoire
tags: [instrument, phase-3, kabbale, sephiroth, registres, architecture]
created: 2026-08-20
updated: 2026-08-20
sources: []
links: ["[[atelier/rd/instrument/instrument-tradition-primordiale-architecture-v0.3]]", "[[atelier/rd/instrument/2026-08-20_etat-avancement-pistes-developpement]]", "[[atelier/rd/outillage/spec-generateur-manifeste]]", "[[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]]", "[[doctrinal/sources/kabbale-10-sefirot-structure]]", "[[doctrinal/sources/sefer-yetsira-ramban]]", "[[doctrinal/sources/traite-emanation-gauche-isaac-ha-kohen]]", "[[doctrinal/discernement/2026-07-28_sept-tours-sitra-ahra]]", "[[doctrinal/discernement/2026-07-02_mont-qaf-meru-topologie-apex]]"]
---

# Les registres — accueillir plusieurs traditions sur l'unique axe

> Circuit **atelier**, pôle R&D. Document d'instrumentation, non doctrinal.
> Liens vers `doctrinal/` en sens unique, signalés.

> **Révision intégrale du 2026-08-20.** Une première version de cette fiche
> concluait que les sources kabbalistiques ne pouvaient pas être instrumentées
> sans nouveaux verdicts. Cette conclusion reposait sur **deux erreurs de
> raisonnement**, redressées par Sidy le jour même et corrigées ici (§1). La
> version fautive est remplacée, non conservée : elle n'énonçait aucun fait
> utile, seulement un blocage mal fondé.

## 1. Le redressement

Rappel du cadre, tel que Sidy l'a restitué :

- L'Instrument est la représentation de l'**unique Arbre Universel**. Arbre
  Universel et Homme Universel sont **équivalents dans le principe**, chacun
  favorisant des aspects variés d'une même Réalité.
- L'identité *al-Insān al-Kāmil = Adam Qadmôn = Wang = Vaishwânara* étant
  **close** ([[doctrinal/discernement/2026-07-26_adam-qadmon-insan-kamil-wang-vaishvanara]],
  2026-07-26), **il s'agit du même axe vertical**.
- *Sephiroth* et *chakras* sont des **centres décrivant des domaines** qui
  s'établissent le long de cet axe.
- Chaque tradition orthodoxe est l'expression particulière de la **même**
  Réalité, et **n'a pas à rendre une même notion par une même expression**.
- La correspondance **s'explicitera nécessairement au fur et à mesure de la
  reconstitution de l'ensemble** — elle n'a pas à être complète d'avance.

**Les deux erreurs corrigées :**

1. **« Incommensurabilité 38 / 5 / 7 »** — erreur de cadre. Un *domaine* n'est
   pas un *degré*. Le dépôt pratique déjà cette distinction : les cinq
   *Ḥaḍarāt* **enveloppent** les 38 degrés sans se confondre avec eux (bandes
   Lāhūt 11-14, Jabarūt 15-18, Barzakh supérieur 19-20, Malakūt planétaire
   21-27, Nāsūt 28-38). Un septénaire de domaines n'est donc pas incompatible
   avec une échelle de 38 degrés : c'est **une autre partition du même axe**.
   Le mécanisme existait déjà ; il n'était simplement pas généralisé.
2. **« Transitivité non autorisée »** — erreur factuelle. Le raisonnement
   supposait que le joint axial restait à établir. **Il est acquis** depuis le
   2026-07-26. Situer un centre sur un axe dont l'identité est déjà verdictée
   n'est pas importer une correspondance : c'est employer un verdict rendu.

Une troisième affirmation était fausse : la fiche prétendait qu'il manquait
« une fondation équivalente à `hadarat-khams` pour la Kabbale ». Elle existe —
[[doctrinal/sources/kabbale-10-sefirot-structure]], `status: traditionnel`,
donnant les 10 Sephiroth, leurs **trois colonnes** et leurs rangs, sourcée
Guénon (via Vulliaud) et texte primaire du *Sefer Yetsira* (commentaire du
Ramban).

## 2. L'architecture proposée : le registre

**Un registre est la partition de l'unique axe vertical propre à une
tradition.** Les registres coexistent sur le même axe sans être alignés entre
eux.

Le dépôt avait déjà résolu ce problème de méthode ailleurs, sans le nommer :
l'anneau zodiacal porte **12 signes et 28 manāzil superposés et non
commensurables**, dont les frontières ne coïncident jamais — et
[[atelier/rd/instrument/spec-anneau-zodiacal]] §3.4 pose que *« le décalage
est une donnée, pas un défaut de rendu »* (Art. 3 sashimono, jamais de joint
forcé). Le registre applique cette même discipline aux traditions.

Deux formes de domaine, **exclusives l'une de l'autre** :

| Forme | Quand | Exemple |
|---|---|---|
| `degres: [a, b]` | la tradition situe elle-même le domaine sur l'échelle des 38 degrés | Ḥaḍarāt akbariennes |
| `rang: n` + `colonne:` | la tradition donne un **ordre** le long de l'axe, sans échelle de degrés | Sephiroth |

**Le point décisif est que ces deux formes s'excluent mécaniquement.** Un
domaine portant à la fois `rang` et `degres` est **refusé par le générateur** :
ce serait déclarer en donnée une correspondance point à point qu'aucune
tradition ne donne — précisément ce que le Cmd 3 réserve à une fiche
`discernement` tranchée. La règle n'est plus seulement écrite dans le
protocole, elle est **appliquée par l'outil**.

Corollaire : **déclarer un registre ne pose aucun joint.** C'est documenter une
tradition dans son expression propre. Aucun ancrage inter-registres n'est
déclaré, et le rendu ne trace aucune ligne d'un registre à l'autre.

## 3. Ce qui est fait (2026-08-20)

- **`instrument-donnees.yaml` v0.4.0** — bloc `registres:` ouvert, avec deux
  registres : `tasawwuf` (axe principal, 5 Ḥaḍarāt en bornes de degrés — reprise
  en donnée des bandes jusque-là codées en dur) et `qabbalah` (axe parallèle,
  10 Sephiroth en rangs + colonnes, aucun degré attribué).
- **`generer-manifeste.py` v0.2.3** — propage `registres` avec validations
  dédiées : id de registre et de domaine uniques, `axe` contrôlé, fiche
  doctrinale devant exister, `degres`/`rang` exclusifs, bornes ordonnées.
  Trois cas de rejet vérifiés en test, dont le point-à-point implicite.
- **Prototype** — rendu du registre parallèle : trois colonnes, en retrait du
  tronc akbarien, **sans aucune ligne vers les degrés**. Les 10 Sephiroth se
  répartissent sur **7 niveaux dérivés mécaniquement** des rangs et colonnes
  déclarés (un domaine « gauche » suivant immédiatement un « droite » partage
  son niveau — couple symétrique). Résultat obtenu : Kether / Hokhma-Bina /
  Hesed-Gevurah / Tiferet / Netzach-Hod / Yesod / Malkhut. Cette réduction
  **n'est pas posée à la main : elle tombe des données** — et recoupe celle que
  Guénon décrit en projetant les couples latéraux sur la colonne du milieu
  (*Études sur l'Hindouisme*, « Kundalinî-Yoga »).
- La hauteur attribuée aux centres est une **répartition proportionnelle sur
  l'étendue de l'axe** : c'est de la présentation, jamais une correspondance,
  et l'info-bulle de chaque centre le dit explicitement.

## 4. Sur la Sitra Ahra — requalification

La version fautive traitait le *Traité de l'Émanation Gauche* comme bloqué. Ce
diagnostic confondait deux choses distinctes :

- ce que le **correctif du 2026-06-29** a rejeté : le rattachement **structurel
  du *waswâs* du Tasawwuf à la Sitra Ahra**, qui imposait au Tasawwuf une
  structure de miroir qliphothique qu'il ne possède pas nativement ;
- ce que l'architecture v0.3 §2 **prescrit** au contraire : *« Tout ce qui y est
  intégré se fait dans son expression dialectique propre »*, la Kabbale portant
  seule sa dialectique Sephiroth/Qliphoth complète.

Autrement dit, le correctif interdit d'**imposer** la Sitra Ahra au tasawwuf ;
il n'interdit pas de la **rendre dans son cadre kabbalistique propre**. Comme
Sidy le formule : le tasawwuf envisage et exprime cela autrement — *l'autre
côté de la Montagne Qāf* — et le dépôt porte déjà cette matière
([[doctrinal/discernement/2026-07-02_mont-qaf-meru-topologie-apex]],
`traditionnel`, validée).

**Voie praticable, sans verdict nouveau** : un registre `qabbalah-sitra-ahra`,
envers du registre séphirothique, déclaré dans sa seule expression
kabbalistique, sans aucun ancrage vers le tasawwuf ni vers l'axe des degrés —
exactement le régime des registres. Non exécuté ici : cela relève d'un lot de
déclaration à part, et
[[doctrinal/discernement/2026-07-28_sept-tours-sitra-ahra]] est encore « en
cours » (le générateur le remonte déjà comme `question_ouverte`). À dire
clairement : ce discernement ouvert n'interdit pas le rendu du registre — il
laisse ouverte la question des *correspondances*, qui ne sont précisément pas
déclarées.

## 5. Suites proposées

1. ~~**Registre hindou**~~ — **fait le 2026-08-20** (verdict Sidy : « poursuis »).
   Voir §6. La source était déjà au dépôt
   ([[doctrinal/sources/guenon-kundalini-yoga-etudes-hindouisme]], ouverte le
   2026-07-14) : cette session n'a pas eu accès à `raw/` (exclu du dépôt git,
   `.gitignore` — vide dans un clone distant), mais n'en avait pas besoin, le
   texte primaire ayant été déposé directement par Sidy dans la conversation.
2. **Registre de la Sitra Ahra** (§4), en expression kabbalistique propre.
3. **Enrichir le registre `qabbalah`** : 22 sentiers, correspondance des
   Sephiroth aux membres (déjà dans la fiche source : bras droit/gauche,
   jambes, etc.), Noms divins — tout est sourcé, rien n'appelle de verdict.
4. **Le moment venu, et seulement sous verdict** : les ancrages
   inter-registres, quand la reconstitution les aura fait apparaître. Le schéma
   les accueillera sans modification — un ancrage se déclare déjà entre deux
   `id`, et les domaines en portent.

## 6. Registre hindouisme-tantra (2026-08-20)

> Renommé `hindouisme` → `hindouisme-tantra` à l'ouverture du registre védantique
> (§7) : deux expositions distinctes de Guénon, deux textes, deux id — pour ne
> pas laisser un même mot recouvrir deux sujets (« une page = un sujet »).

Déclaré dans `instrument-donnees.yaml` v0.4.1, sur la même source que celle
qui avait déjà servi à clore
[[doctrinal/discernement/2026-06-20_fajr-vajra-indra-vritra]] :
[[doctrinal/sources/guenon-kundalini-yoga-etudes-hindouisme]] (`traditionnel`,
au dépôt depuis le 2026-07-14).

**7 domaines en rang** (Guénon lui-même : *« les six chakras et sahasrâra ne
forment qu'un total de sept »*) : Mūlādhāra, Swādhishthāna, Manipūra, Anāhata,
Vishuddha, Ājnā, Sahasrāra. **Colonne unique** (`milieu`), à la différence de
la Kabbale — Guénon situe les six premiers sur les divisions successives de
la colonne vertébrale, en ordre ascendant ; *idā* et *pingalā* sont des
**canaux** (*nādīs*), non des centres : documentés en donnée (champ `canaux`,
non rendu géométriquement — le schéma des registres ne porte que des centres,
ouverture possible en piste de fond) mais non déclarés comme domaines.

**Un point à ne pas laisser filer** : Guénon donne dans ce même texte
(§34-36) une correspondance rang-par-rang **explicite** entre les 7 niveaux
séphirothiques et les 7 domaines hindous — Kether/Sahasrāra,
Hokmah-Binah/Ājnā, Hesed-Geburah/Vishuddha, Tiphereth/Anāhata,
Netsah-Hod/Manipūra, Iesod/Mūlādhāra (avec une réserve de Guénon lui-même sur
l'appariement Iesod/Malkuth ↔ Mūlādhāra/Swādhishthāna — « il semble qu'il y
ait lieu d'envisager une interversion »). **Elle n'est déclarée nulle part
ici.** Elle est sourcée, explicite, et signalée — c'est un candidat de premier
ordre pour une fiche `discernement` dédiée, au même titre que celle qui a
établi l'Homme Universel : mais c'est un verdict, pas une exécution
mécanique. Tant qu'elle n'est pas ouverte, les deux registres restent, comme
le veut la règle, **sans aucun ancrage entre eux**.

## 7. Registre vedanta — les quatre états d'Âtmâ (2026-08-20)

Demande de Sidy : « mettre tout ça en regard avec *L'Homme et son devenir
selon le Vêdânta* pour compléter ». Cette œuvre est distincte du texte utilisé
au §6 (*Kundalinî-Yoga*, dans *Études sur l'Hindouisme*) — d'où le renommage
ci-dessus, pour garder les deux expositions séparées plutôt que de les fondre
sous un même registre par simple proximité de tradition.

**Sources** : deux fiches, déjà au dépôt, `traditionnel` —
[[doctrinal/sources/guenon-homme-devenir-vedanta-ch10-15-16-brahma-turiya]]
(ch. XII cadre les quatre états, XIII = Vaishwânara, XV = Prājña, XVI = Turīya)
et [[doctrinal/sources/guenon-homme-devenir-vedanta-ch9-14]] (ch. XIV, nomme
Taijasa). Le schéma des registres ne porte qu'une `fiche:` par registre ; la
seconde source est citée en commentaire par domaine, faute de mieux — limite
assumée, non un défaut de traçabilité (chaque domaine garde sa citation).

**4 domaines en rang, colonne unique** — ce sont des états d'un même être, non
des positions latérales, à la différence de la Kabbale :
1. **Vaishwânara** — l'état de veille, manifestation grossière. Identifié à
   *Virâj* ; c'est le domaine que Guénon identifie explicitement à l'Homme
   Universel (ch. XIII).
2. **Taijasa** — l'état de rêve, manifestation subtile.
3. **Prājña** — le sommeil profond, état causal, informel et supra-individuel.
4. **Turīya** — le Quatrième, inconditionné. Le texte lui-même pose une
   asymétrie forte : les trois premiers pâdas ne comptent que pour un quart en
   importance métaphysique, le Quatrième vaut les trois autres quarts — reprise
   telle quelle, non lissée.

**Un ancrage déclaré — et un seul.** *Vaishwânara fait déjà partie* de
l'identité *Adam Qadmôn = al-Insān al-Kāmil = Wang = Vaishwânara*, verdict
clos le 2026-07-26. Ce n'est donc pas une correspondance nouvelle : c'est la
même traduction technique que celle déjà appliquée au nœud `universel/homme-
universel` lui-même (P1.1 de la fiche de pistes). Pour la déclarer proprement,
le générateur a dû être étendu (schéma manifeste v0.2.4) : un ancrage peut
désormais viser un domaine de registre, pas seulement un nœud — extension
mécanique, testée (collision d'id bloquante, ancrage nœud→domaine vérifié),
aucun nouvel arbitrage.

**Ce qui reste précisément hors de cet ancrage** : les trois autres domaines
de vedanta (Taijasa, Prājña, Turīya) et tous les domaines de qabbalah et de
hindouisme-tantra restent sans aucun ancrage. Le verdict du 2026-07-26 ne
nomme que Vaishwânara ; rien ne l'étend de soi-même aux autres pâdas ni aux
Sephiroth/chakras (cf. §6, correspondance Guénon non déclarée).

**Rendu** : dans le prototype, la sphère de Vaishwânara reçoit désormais une
ligne d'équivalence établie (rouge, même traitement que les Aqtâb) vers le
nœud Homme Universel — pilotée par la donnée (`HOMME_UNIVERSEL.cibles`, lu
depuis le manifeste), pas codée en dur : toute future extension des cibles de
ce nœud se rendrait automatiquement, sans toucher au prototype.

---

*Signalement et architecture. Aucun ancrage inter-traditionnel *nouveau*
déclaré — l'unique ancrage ajouté (Homme Universel → Vaishwânara) traduit un
verdict déjà clos. Aucun joint qualifié au-delà. Aucune fiche doctrinale créée
ou modifiée. Les verdicts restent réservés à Sidy (Cmd 12).*
