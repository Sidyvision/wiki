---
title: "PRO-08 — un dossier versionné pour les textes convertis : plan"
type: infrastructure
chantier: PRO-08
tags: [atelier, rd, infrastructure, chantier, plan, migration]
created: 2026-09-02
updated: 2026-09-02
sources: []
links:
  - "[[atelier/rd/infrastructure/pro-08-textes-convertis-versionnes/spec]]"
  - "[[atelier/rd/infrastructure/pro-08-textes-convertis-versionnes/intent]]"
---

# PRO-08 — plan

> **Statut : `vise`** — Sidy, 2026-09-02. Les trois verdicts préalables sont
> rendus, et ils sont ici *verbatim* : « **`textes/` validé, dédoublonne avant
> migration, et amende le §II** ».
>
> Le plan visé *est* le plan du Cmd 6. L'exécution est donc autorisée pour les
> phases 1 à 4.
>
> ⚠️ **Reste non tranché** : le régime des **futurs** textes convertis
> (phase 5, point 17). Il n'est pas requis pour exécuter, et il n'est pas
> supposé.

## Étapes

### ✅ Préalable — les trois verdicts, rendus le 2026-09-02

1. **Le nom et la place** : **`textes/`**, dossier de premier niveau. Retenu.
2. **Les doublons** : **dédoublonnés AVANT migration**. Ce n'est donc plus un
   signalement mais un geste, et il lui faut une règle explicite de conservation
   — voir `spec.md` §4 amendé et l'étape 9 bis.
3. **L'amendement du `§II`** : autorisé.

### Phase 1 — la garde avant le geste

4. Écrire `atelier/rd/outillage/migrer-textes-convertis.py`. **Deux modes** :
   `--constater` (défaut, n'écrit rien) et `--migrer`. Le défaut ne touche
   jamais au disque — même discipline que `publier-manifeste-instrument.sh`.
5. Le script **refuse de migrer** tout fichier portant une donnée personnelle
   (e-mail, IBAN sur borne de mot, téléphone), toute collision de nom après
   normalisation, et tout fichier hors corpus. Il **rapporte** les doublons, il
   ne les tranche pas.
6. **Éprouver la garde avant de s'en servir** : fabriquer un fichier témoin
   portant une adresse e-mail, le présenter au script, **observer le refus**,
   retirer le témoin. Un contrôle dont on n'a pas vu l'échec n'est pas vérifié
   (§VII, motifs PRO-01 et INF-14).
   ⚠️ Le motif `IBAN` sera posé sur **bornes de mot** : un premier balayage
   d'instruction a signalé « IBAN » dans *Le Roi du Monde*, et c'était
   **« Liban »**. Le faux positif est consigné pour qu'il ne se reproduise pas.

### Phase 2 — l'amendement du vérificateur, éprouvé dans les deux sens

7. Ajouter `"textes/"` à `PREFIXES_SANS_FM` dans `verifier-invariants.py`.
8. **Épreuve à deux faces**, et la seconde est celle qui compte :
   - un `.md` nu **dans** `textes/` → **accepté** ;
   - un `.md` nu **hors** `textes/` → **`B0` levé**.
   Sans la seconde, rien ne distinguerait un amendement ciblé d'un désarmement
   général de B0. C'est exactement la faute de PRO-01 sous une autre forme.

### Phase 3 — la migration, en copie

9. `--constater` d'abord : lire le rapport en entier (comptes, doublons, refus).
9 bis. **Dédoublonnage, sur verdict de Sidy.** Règle de conservation, arrêtée
    parce que le verdict dit *quoi* faire et non *lequel garder* : entre deux
    copies identiques au bit près, on **conserve celle qui n'est pas sous
    `Downloads/`** — ce dossier est un dépôt de téléchargement, non un corpus
    rangé, et il redouble intégralement deux corpus déjà classés. À égalité
    (toutes sous `Downloads/`), on garde le premier chemin par ordre
    alphabétique, de façon déterministe. **Chaque écart est rapporté**, jamais
    silencieux. Les doublons ne sont pas supprimés de `raw/` (Cmd 10) : ils ne
    sont simplement **pas migrés**.
10. `--migrer` : **copie**, jamais déplacement. `raw/` reste intact (Cmd 10).
11. Écrire `textes/LISEZ-MOI.md` (Sceau atelier) : nature du dossier, provenance
    par corpus, règle d'immuabilité.
12. Contrôler les huit critères d'acceptation du `spec.md`.

### Phase 4 — le protocole, et le retour à Sidy

13. Amender le `§II` du protocole racine : entrée dans l'arbre, et la phrase de
    statut — `textes/` **n'est pas un sixième circuit**.
14. Consigner au changelog du protocole (`meta/protocole-archives/`).
15. **Retour à Sidy** : il tire depuis l'iPad et **ouvre un chapitre dans
    Obsidian**. C'est le seul critère qui compte vraiment, et le seul qu'aucun
    script ne peut rendre.

### Phase 5 — ce qui n'est PAS dans ce plan

16. Le **retrait des originaux** de `raw/` est une **seconde décision**, prise
    après que la migration a vécu. Elle n'est pas préparée ici.
17. Le **régime des futurs** textes convertis — passent-ils encore par `raw/`,
    ou directement par le sas vers `textes/` ? C'est la question qui évite que le
    problème se reforme dans six mois. Elle est **posée, non tranchée**.

## Fichiers touchés

| fichier | opération |
|---|---|
| `atelier/rd/infrastructure/pro-08-…/{intent,spec,plan}.md` | **créés** (fait) |
| `atelier/rd/registre-chantiers.md` | modifié — ligne PRO-08 |
| `atelier/rd/outillage/migrer-textes-convertis.py` | **créé** (après visa) |
| `verifier-invariants.py` | modifié — une ligne dans `PREFIXES_SANS_FM` (après visa) |
| `textes/` + `textes/LISEZ-MOI.md` | **créés** (après visa) |
| `CLAUDE.md` racine, `§II` | amendé (après **verdict de protocole**) |
| `meta/protocole-archives/changelog-CLAUDE.md` | entrée d'amendement |
| `raw/` | **inchangé** — copie, jamais déplacement |

Rien n'est supprimé (Cmd 10).

## Vérification

```bash
# Critère 1 — le vérificateur accepte les textes nus
python3 verifier-invariants.py --racine /root/wiki        # 0 erreur, 0 avertissement

# Critère 2 — ET il refuse toujours ailleurs (l'épreuve qui compte)
printf 'nu\n' > /root/wiki/essai-b0.md
python3 verifier-invariants.py --racine /root/wiki | grep B0   # DOIT lever
rm /root/wiki/essai-b0.md

# Critère 3 — le compte est juste
python3 atelier/rd/outillage/migrer-textes-convertis.py --constater
#   migrés + doublons + non migrés == 708

# Critère 4 — la garde « données personnelles » mord
#   fichier témoin avec une adresse, script relancé, refus observé, témoin retiré

# Critères 5-7
git status --short raw/                                   # vide
du -sh textes/                                            # ≈ 14 Mo
python3 atelier/rd/outillage/graphe/generer-cartographie.py
python3 -c "import json;g=json.load(open('graphe-cartographie.json'));\
print(sum(1 for n in g['nodes'] if str(n).startswith('textes/')))"   # 0
```

**Le critère 8 n'est pas dans ce bloc, et c'est voulu** : « Sidy ouvre un
chapitre dans Obsidian » ne s'automatise pas. Aucun de ces contrôles ne prouve
que le besoin est comblé — ils prouvent seulement que rien n'est cassé.

## Points de retour à l'humain (Cmd 13)

1. **Les trois verdicts préalables** — nom, doublons, amendement du `§II`.
2. **Le visa de ce plan.**
3. **L'amendement du protocole racine**, qui est une révision, non une
   application.
4. **Le retrait éventuel des originaux** de `raw/` — jamais dans la même passe
   que la migration.

## Journalisation

`atelier/annales.md` (Cmd 9) ; ligne PRO-08 du registre mise à jour dans la même
passe ; `meta/protocole-archives/changelog-CLAUDE.md` pour l'amendement du `§II`.
