# UPDATES — Lot « Pôle Fiqh » (2026-07-06)

> Lot touchant la **racine** (`CLAUDE.md`), `doctrinal/` et `meta/`. Intégration
> **fiche par fiche, dans l'ordre ci-dessous**, chaque écriture relue (jamais
> d'auto-accept), annales en append-only, clôture par vérification mécanique
> (`compare`/diff). Ce fichier ne se range pas : le supprimer du sas en fin de course.

---

## 0. Préalable — articulation avec le lot « Révision protocolaire V2 rév. 2026-07-06 »

Le `CLAUDE.md` de ce lot **inclut** la révision protocolaire précédente (basmala,
protocoles in extenso, discipline des sources, manifestes, ancrage éthique §V.c) **et**
les amendements du pôle Fiqh (§V.c.6, action EXAMEN DE FIQH ⚖️, Rapport du matin en
§I). Deux cas :
- Si le lot précédent n'est **pas encore intégré** : intégrer directement ce
  `CLAUDE.md`-ci (il le remplace), avec les deux documents dérivés du lot précédent
  (`00-instructions-projet`, `briefing-claude-ai`) inchangés.
- S'il est **déjà intégré** : simple remplacement de `CLAUDE.md` par la présente
  version.

## 1. Ordre d'intégration séquencé

### Séquence A — Racine

1. **`CLAUDE.md`** → `/root/wiki/CLAUDE.md` — remplacement intégral (voir §0).
   Vérifier après écriture : la basmala en ligne 1, la section §V.c à 6 points,
   l'action « EXAMEN DE FIQH » présente en §VII.

### Séquence B — Doctrinal (fiche par fiche)

2. **`doctrinal/traditions/madhhab-maliki.md`** — création. `to-source` assumé
   (aucun texte malikite en bibliothèque). Vérifier cibles `cross_links`
   (`imam-malik` créé au point 3 → l'intégrer AVANT de valider les liens, ou créer
   dans l'ordre 3 puis 2 ; `fiqh` créé au point 4 ; `ahl-al-sunnah-wa-l-jamaa`
   existe).
3. **`doctrinal/autorites/imam-malik.md`** — création.
4. **`doctrinal/symboles/fiqh.md`** — création. Cible `kitab-al-tarifat-jurjani`
   existe (vérifier le slug exact dans l'index).
5. **`doctrinal/sources/al-madrasah-al-hanbaliyyah.md`** — création.
6. **`doctrinal/index.md`** — Update ciblé :
   - §I Formes Traditionnelles : `[[doctrinal/traditions/madhhab-maliki|Le madhhab mālikite (école de l'Imam Mālik)]]`
   - §II Sciences Traditionnelles : `[[doctrinal/symboles/fiqh|Le Fiqh (la science des statuts de la Loi)]]`
   - § Autorités : `[[doctrinal/autorites/imam-malik|L'Imam Mālik b. Anas]]`
   - § Sources : `[[doctrinal/sources/al-madrasah-al-hanbaliyyah|Al-Madrasah Al-Hanbaliyyah]]`
7. **`doctrinal/annales.md`** — append-only, une entrée :
   `## [2026-07-06] archivage | Ouverture du pôle Fiqh — madhhab mālikite (préséance), Imam Mālik, science du fiqh, ressource ḥanbalite ; amendement protocolaire §V.c.6 + bloc ⚖️`

### Séquence C — Meta

8. **`meta/projet-unifie/hermes-prompts/04-administration-legal.md`** — remplacement
   (v2 : mission de référencement fiqh, préséance mālikite, jamais d'avis religieux).
9. **`meta/projet-unifie/hermes-prompts/10-protocol-guardian.md`** — remplacement
   (v2 : double face d'harmonisation, signaux ✅/⚠️/❓, spec du Rapport du matin).
10. **`meta/projet-unifie/proposition-pole-fiqh-2026-07-06.md`** — création
    (proposition validée, archivée comme document de conception).
11. **`meta/bibliotheque-physique.md`** — **append ciblé** (ne pas réécrire la
    fiche) : ajouter en fin de document la section suivante, à l'identique :

```markdown
---

## À acquérir — pôle Fiqh (validé 2026-07-06)

*Aucun manuel de fiqh mālikite en bibliothèque à ce jour — acquisition prioritaire
pour lever les `to-source` du pôle.*

- **Mukhtaṣar al-Akhḍarī** — texte de base de l'école (ʿibādāt). Confirmé par Sidy.
- **Mukhtaṣar Khalīl** (Khalīl b. Isḥāq) — référence de l'école, niveau avancé ;
  texte opératoire pour les muʿāmalāt (questions du label). Confirmé par Sidy.
- *al-Risāla* (Ibn Abī Zayd al-Qayrawānī) — exposé classique, appui suggéré.
- *al-Muwaṭṭaʾ* (Imam Mālik) — ouvrage fondateur, appui suggéré.
```

## 2. Contrôles VIGILANCE de fin de lot

1. Frontmatters au Sceau (Recteur pour les 4 fiches doctrinales ; meta pour le reste).
2. Aucun lien `doctrinal/ → label/` introduit (les fiches du pôle sont générales et
   neutres — vérifier qu'aucune ne mentionne le label).
3. `sources_count` = longueur des listes `sources`.
4. Entrée d'annales insérée en append, jamais de réécriture.
5. `git diff --stat` cohérent avec la liste ci-dessus ; commit :
   `ARCHIVAGE: ouverture du pole Fiqh + protocole V.c.6` puis push.
6. Vider le sas, y compris ce fichier.

## 3. Points sensibles

- **Tout le pôle est `to-source`** : c'est voulu — la levée n'interviendra que sur
  vérification des textes physiques par Sidy (discipline des sources, §VII).
- L'étude ⚖️ pilote (*hiba*) n'est **pas** dans ce lot : elle attend l'acquisition
  des textes (Khalīl/Risāla) pour ne pas naître entièrement à vide.
- Le Rapport du matin en version manuelle peut être demandé dès la prochaine session
  Claude.ai (« fais-moi le Rapport du matin ») — l'automatisation attend la Phase 3
  Hermes.
