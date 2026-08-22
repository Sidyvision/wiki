---
title: "Spécification — Archivage du rapport de monitoring infrastructure quotidien"
type: outillage
tags: [rd, outillage, infrastructure, monitoring, hermes]
created: 2026-08-18
updated: 2026-08-19
sources: []
links: ["[[atelier/rd/infrastructure/monitoring-archive-charte]]", "[[atelier/rd/cahiers/registre-problemes]]"]
---

# Spécification — `archiver-monitoring-quotidien.py`

> Suggestion Sidy, 2026-08-18 : « le 'Rapport monitoring infrastructure
> quotidien' que je reçois via Discord soit conservé en parallèle dans un
> dossier d'archive au R&D pour une durée de 40 jours [...] ça nous permettra
> de renforcer le monitoring de l'agent aussi. » Script déterministe, même
> famille que `verifier-invariants.py`, `detecter-non-tracke.py` : ni LLM, ni
> réseau, ne corrige rien.

## 1. Problème traité

Le job Hermes `monitoring-infrastructure-quotidien` (profil `studio`, cron
`0 12 * * *`) livre son rapport uniquement sur Discord (canal
`#infrastructure`) — aucune trace n'en subsiste dans le dépôt. Un rapport
manqué, un incident Discord, ou simplement le besoin de relire l'historique
sur plusieurs jours n'a aujourd'hui aucun support hors du canal lui-même.

**Constat mécanique (2026-08-18)** : Hermes persiste déjà chaque exécution de
job cron sur disque, indépendamment du canal de livraison — deux copies par
run, `.txt` et `.md`, sous
`/root/.hermes/profiles/<profil>/cron/output/`. Ce script n'a donc **aucune
dépendance à Discord ni à une extension du prompt du job monitoring** : il
copie une sortie qui existe déjà. Conséquence directe : le job de production
`monitoring-infrastructure-quotidien` n'a besoin d'aucune modification pour
que cette archive existe — voir §4.

## 2. Fonctionnement

```
atelier/rd/outillage/archiver-monitoring-quotidien.py \
    --source /root/.hermes/profiles/studio/cron/output \
    --job-id 41dc3e7e492c \
    --archive atelier/rd/infrastructure/monitoring-archive \
    [--retention-jours 40] [--appliquer]
```

1. Liste les sorties `.txt` du job `--job-id` déjà écrites par Hermes dans
   `--source` (motif de nom `<job_id>_<YYYYMMDD>_<HHMMSS>.txt`).
2. Compare à ce qui est déjà présent dans `--archive` (motif
   `<YYYY-MM-DD>_<job_id>.txt`) ; ne copie que le manquant (idempotent).
3. Sans `--appliquer` : constat seul (ce qui serait copié, ce qui serait
   purgé). Avec `--appliquer` : copie effective, puis purge des copies
   d'archive dépassant `--retention-jours` (40 par défaut).

**Codes de sortie** : `0` exécution correcte · `1` rien à archiver (source
introuvable ou job jamais exécuté) · `2` erreur d'exécution du script
lui-même.

## 3. Format d'archive : `.txt`, jamais `.md`

Décision délibérée, pas un détail. Le rapport cite la sortie brute de
`generer-cartographie.py --verifier` et `verifier-invariants.py`, laquelle
contient des tokens `[ [...] ]` littéraux (liens morts signalés, ex. la
séquence double-crochet autour de `wiki-contrainte-integration-levee`). Un
fichier `.md` portant ces tokens,
walké par ces deux mêmes scripts lors d'une vérification ultérieure du dépôt,
se déclencherait sur son propre contenu — piège déjà rencontré une fois
(voir `registre-problemes.md`, entrée `[2026-08-18]`) et qui se reproduirait
ici quarante fois en continu si l'archive était au format `.md`. Vérifié :
les deux scripts filtrent sur `.endswith(".md")` — un `.txt` est
structurellement hors de leur périmètre. Corollaire : les fichiers d'archive
ne portent pas de Sceau atelier (pas des fiches du dépôt au sens du
protocole, simple journal technique) et ne sont donc pas comptés dans la
cartographie des liens ni les invariants.

## 4. Ce que le script ne fait pas

- Ne modifie ni ne lit le job Hermes `monitoring-infrastructure-quotidien`
  lui-même (aucune édition de cron en production — modification d'un agent
  vivant hors du périmètre de ce script, Cmd 13).
- Ne stage ni ne commite l'archive dans git ; l'humain (ou une session
  d'intégration ultérieure) décide de committer le contenu produit.
- Ne juge pas le contenu des rapports archivés — simple copie et purge par
  date, aucune lecture sémantique.
- **Rétention 40 jours = fenêtre du dossier de travail, pas de l'historique
  git.** Un fichier purgé du dossier `monitoring-archive/` reste retrouvable
  dans l'historique git de tout commit qui l'aura inclus, indéfiniment. La
  purge allège l'arborescence courante, elle n'efface pas la trace versionnée.
- Ne déclenche rien lui-même : l'automatisation (ouverte le 2026-08-18, cf.
  `atelier/rd/infrastructure/monitoring-archive-charte.md`, §« Ingestion »)
  vit dans un job cron Hermes dédié qui appelle une enveloppe
  (`archiver-monitoring-quotidien-cron.sh`, args fixés en dur — un job
  `no_agent` ne transmet aucun argument à son `--script`), jamais dans une
  modification de ce script lui-même.

## 5. Écart avec la piste initialement envisagée

L'hypothèse de départ (avant vérification) était d'étendre le prompt du job
`monitoring-infrastructure-quotidien` pour qu'il écrive lui-même une copie
datée dans l'archive, en plus de la livraison Discord — modification d'un
job de production en cours d'exécution quotidienne réussie (`last_status:
"ok"`, 2 exécutions). Cette piste est abandonnée après constat que Hermes
persiste déjà la sortie complète sur disque sans qu'aucune modification du
job ne soit nécessaire : ce script se branche sur une donnée déjà produite,
zéro risque pour le job vivant.

## 6. Découverte annexe — trouvée cassée, réparée le même jour (2026-08-18)

En inspectant `/root/.hermes/profiles/studio/cron/jobs.json` pour retrouver
le prompt exact du job monitoring, un second job cron du même profil,
`coherence-infrastructure-brute` (id `ca9593f3a03d`, `no_agent: true`,
prévu comme contrôle anti-fabulation direct de l'étape 4 sans passage par un
LLM), s'est révélé **en échec systématique depuis sa création** (`last_status:
"error"`, deux exécutions, deux échecs) : `Script not found:
/root/.hermes/profiles/studio/scripts/verifier-coherence-infrastructure.py`
— le script réel vit dans le dépôt
(`atelier/rd/outillage/verifier-coherence-infrastructure.py`), pas dans le
dossier `scripts/` du profil Hermes que `--script` résout implicitement pour
un job `no_agent`. Ce job n'était documenté nulle part dans le dépôt (absent
de la fiche `activation-monitoring-studio-cron-2026-08-17.md`).

Réparé le même jour, feu vert Sidy en session (« tu as le feu vert pour tout
rétablir »), en deux temps — un lien symbolique d'abord tenté a été rejeté
par Hermes lui-même (chemin canonique résolu hors du dossier `scripts/` du
profil), puis une copie réelle a révélé un second défaut plus grave qu'un
échec visible : un faux succès silencieux (`last_status: "ok"` alors que le
script, privé de `--racine`, vérifiait 0 affirmation au lieu de 3). Les deux
défauts et leur résolution (enveloppe `verifier-coherence-infrastructure-
cron.sh`, même motif que l'enveloppe de ce script-ci) sont détaillés dans
[[atelier/rd/cahiers/registre-problemes]], entrée `[2026-08-18]` (« Suite de
l'entrée précédente »).
