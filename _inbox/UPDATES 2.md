# UPDATES — Lot « Révision protocolaire V2 rév. 2026-07-06 » (3 fichiers)

> Lot de maintenance protocolaire, **ordre humain explicite** (le protocole est
> « invariant sauf ordre humain » — l'ordre est donné par Sidy, session Claude.ai du
> 2026-07-06). Intégration fiche par fiche, chaque écriture relue (jamais
> d'auto-accept), clôture par vérification mécanique.

## 1. Fichiers et destinations (remplacements à l'identique)

| Fichier du sas | Destination | Opération |
|---|---|---|
| `CLAUDE.md` | `/root/wiki/CLAUDE.md` | **Remplacement intégral** (V2 → V2 rév. 2026-07-06) |
| `00-instructions-projet.md` | `meta/projet-unifie/00-instructions-projet.md` | Remplacement intégral |
| `briefing-claude-ai.md` | `meta/briefing-claude-ai.md` (chemin existant à confirmer via `git ls-files | grep briefing-claude-ai`) | Remplacement intégral |

## 2. Contenu de la révision (pour l'entrée d'annales)

- `CLAUDE.md` s'ouvre désormais sur la basmala (بسم الله الرحمن الرحيم).
- Protocoles d'exécution réintégrés **in extenso** (auto-suffisance, corollaire du
  Cmd 14) ; §IX retramé.
- **Discipline des sources** (bibliothèque physique, levée du `to-source` par
  vérification primaire humaine, persona IA flagué, crédibilité par item).
- **Règle commune des manifestes** (Instrument + site) ; double ancrage = signal de
  vigilance dans EXAMEN DE DISCERNEMENT ; vigilance documentaire en clôture de session.
- **§V.b — Ancrage éthique des actes de la structure** : les aspects contractuels et
  commerciaux du label sont soumis à la logique d'ancrage doctrinal (bénéfice
  émergent jamais promis ; tension Commerce ↔ Gardien ; porte humaine Cmd 13 ;
  questions juridiques/fiscales jamais tranchées sans professionnel qualifié) ;
  Cmd 3 étendu en conséquence.
- **§VIII étendu à 10 règles** (mémoire/skills auditables, allowlist des canaux,
  extension `raw/` conditionnelle, bascule par double exécution).
- Documents dérivés (`00-instructions-projet`, `briefing-claude-ai`) alignés :
  quatre circuits, Sceau label, 14 Commandements, état des travaux au 2026-07-06.

## 3. Consignes d'intégration

1. Sauvegarder l'état courant avant remplacement : `git status` propre exigé.
2. Remplacer les trois fichiers (relire chaque écriture).
3. `doctrinal/annales.md` — **Update append-only**, une entrée :
   `## [2026-07-06] restauration | Protocole V2 rév. — basmala, auto-suffisance, discipline des sources, ancrage éthique du label, supervision étendue`
4. Aucun autre fichier touché. Vérifier `git diff --stat` : exactement 3 fichiers
   modifiés + annales.
5. Commit : `RESTAURATION: protocole V2 rev. 2026-07-06` puis push.
6. Supprimer ce `UPDATES.md` du sas en fin de course.

## 4. Points sensibles

- `CLAUDE.md` est à la **racine** du dépôt, pas dans un circuit.
- Le chemin exact de `briefing-claude-ai.md` doit être vérifié avant écriture
  (meta/ ou meta/projet-unifie/) — ne pas créer de doublon.
- L'entrée d'annales est une insertion, **jamais** une réécriture du fichier.
