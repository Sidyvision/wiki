# Agent 08 — Publication / Site Orchestrator (Sagittaire)

Éclatement modulaire du 2026-08-31 : le prompt monolithique
`08-publication-site.md` (270 lignes) devient un **principe invariant** et
trois **mandats** chargés à la demande.

## Contrat de chargement

| Pièce | Rôle | Chargement |
|---|---|---|
| `08-principe.md` | Invariant : rôle, mission, principe zodiacal, contexte d'harmonisation, périmètre, guardrails, handoffs | **Toujours** |
| `mandats/*.md` | Expert d'une tâche : périmètre, commandes, standards propres | **À la demande, un seul à la fois** |

Le principe porte les guardrails et les interdits de périmètre (« Never: HTML
creation, copy writing, publication decisions » ; l'arrêt obligatoire à l'URL de
preview). Un mandat ne peut donc pas les desserrer : ils restent chargés quel que
soit le mandat actif. C'est le point d'équilibre de l'éclatement — dissoudre le
monolithe sans fixer l'invariant produirait une dispersion, pas une modularité.

## Ce que ces fichiers ne font pas

Ils ne routent rien par eux-mêmes. Un routeur écrit en markdown (« tâche X →
charger `mandats/Y.md` ») n'a aucun exécutant : rien dans le dépôt ni dans le
moteur ne lit ce répertoire. Le chargement à la demande est assuré par le
**mécanisme de skills du moteur Hermes**
(`~/.hermes/profiles/publication/skills/<mandat>/SKILL.md` : seule la
`description` du frontmatter reste en contexte, le corps n'est tiré que lorsque
la tâche le demande).

## Où cela vit réellement

| Ici (source de vérité) | Moteur (exécution) |
|---|---|
| `08-principe.md` | `~/.hermes/profiles/publication/SOUL.md` |
| `mandats/X.md` | `~/.hermes/profiles/publication/skills/hermes/X/SKILL.md` |

**Déployé : non.** Au 2026-08-31, le `SOUL.md` du profil `publication` porte
1 575 octets contre 14 256 documentés ici : 203 lignes du dépôt n'ont jamais
atteint l'agent, dont les trois mandats votés le 2026-08-24 et le principe
zodiacal. Le déploiement modifie un agent en fonctionnement : il relève de la
porte humaine (Cmd 13) et attend un go explicite de Sidy. Procédure et retour
arrière : `deployer-prompt-agent.md` dans ce répertoire.

## Vérification

```bash
python3 atelier/rd/outillage/comparer-prompts-hermes.py \
    --conservation 08-publication-site \
    --source-git <sha-avant-éclatement>:meta/projet-unifie/hermes-prompts/08-publication-site.md
python3 atelier/rd/outillage/comparer-prompts-hermes.py --derive
```

L'éclatement est **iso-contenu** : aucune ligne du monolithe n'a été traduite,
condensée ni réécrite. Toute reformulation ultérieure est un acte distinct,
soumis au verdict de Sidy.
