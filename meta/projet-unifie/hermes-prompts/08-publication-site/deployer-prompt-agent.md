# Procédure de déploiement — wiki → moteur (agent 08)

**Statut : présentée à blanc, NON exécutée.** Le déploiement modifie un agent en
fonctionnement (`hermes_cli.main --profile publication gateway run`, process de
fond) : il relève de la porte humaine (Cmd 13) et attend un go explicite de Sidy.

## Pourquoi cette procédure existe

Il n'existe aucun chemin déterministe du dépôt vers le moteur. Ce qui est décidé
et commité ici n'atteint l'agent que si quelqu'un le recopie à la main dans
`~/.hermes/profiles/`. Constat mécanique du 2026-08-31
(`comparer-prompts-hermes.py --derive`) : **12 agents sur 12 en écart**.

| profil | wiki | `SOUL.md` déployé | écart |
|---|---|---|---|
| publication | 14 256 o | 1 575 o | 203 lignes absentes du moteur |
| gardien | 5 458 o | 1 679 o | 52 lignes |
| studio | 10 714 o | 10 717 o | 3 lignes (ZWJ, Cmd 15) |
| les 9 autres | 2 688 – 5 241 o | 1 306 – 3 824 o | 17 à 24 lignes chacun |

L'agent 08 n'a donc jamais reçu ses trois mandats votés le 2026-08-24, ni son
principe zodiacal, ni son contexte d'harmonisation. La saturation diagnostiquée à
14 Ko était **documentaire, pas opérationnelle**.

## Correspondance des pièces

| Dépôt (source de vérité) | Moteur (exécution) | Chargement |
|---|---|---|
| `08-principe.md` | `~/.hermes/profiles/publication/SOUL.md` | toujours |
| `mandats/X.md` | `~/.hermes/profiles/publication/skills/hermes/X/SKILL.md` | à la demande |

Le mécanisme de chargement conditionnel n'est pas à écrire : c'est le sélecteur
de skills du moteur. Un `SKILL.md` porte un frontmatter `name` + `description` ;
seule la description reste en contexte, le corps n'est tiré que lorsque la tâche
le demande. C'est exactement le « mandat expert activé selon la tâche » de la
fiche `_inbox/` — implémenté par le moteur, pas par une consigne markdown que
rien n'exécute.

Frontmatter à poser en tête de chaque `SKILL.md` au moment du déploiement (le
corps reste le mandat verbatim) :

```yaml
---
name: site-orchestration
description: "Publication du site : fiches label/ à statut sorti|valide, manifeste déterministe, zones HTML marquées, preview puis production après go explicite."
---
```
```yaml
---
name: bibliothecaire
description: "Index et glossaires de la bibliothèque physique : transcription depuis photographies en fiches de repérage terme → page, jamais d'interprétation."
---
```
```yaml
---
name: veille-referencement
description: "Conformité frontmatter et investigation documentaire (cron 11:00) : contrôle de forme puis recherche de sources, sans qualification doctrinale."
---
```

## Séquence (à exécuter sur go de Sidy, jamais avant)

```bash
P=~/.hermes/profiles/publication
W=/root/wiki/meta/projet-unifie/hermes-prompts/08-publication-site

# 1. Point de retour, HORS dépôt (le SOUL.md courant n'est pas versionné)
cp "$P/SOUL.md" "$P/SOUL.md.bak-$(date +%Y%m%d-%H%M%S)"

# 2. Principe → SOUL.md
cp "$W/08-principe.md" "$P/SOUL.md"

# 3. Mandats → skills (frontmatter posé, corps verbatim)
for m in site-orchestration bibliothecaire veille-referencement; do
  mkdir -p "$P/skills/hermes/$m"
  # frontmatter ci-dessus + corps de $W/mandats/$m.md
done

# 4. Contrôle AVANT redémarrage — doit rendre « ✅ synchronisé » pour publication
python3 /root/wiki/atelier/rd/outillage/comparer-prompts-hermes.py --derive

# 5. Redémarrage du seul profil publication, puis observation d'un cycle
```

## Retour arrière

```bash
cp "$P/SOUL.md.bak-<horodatage>" "$P/SOUL.md"
rm -rf "$P/skills/hermes/"{site-orchestration,bibliothecaire,veille-referencement}
```

Réversible en une commande, sans toucher au dépôt : l'assemblage reste démontable
(sashimono art. 5).

## Points à trancher avant déploiement

1. **Charge réelle.** Le principe fait 50 lignes contre 30 au `SOUL.md` actuel :
   l'agent 08 recevra *plus* de contexte permanent qu'aujourd'hui, pas moins. Le
   gain n'est pas une réduction de charge, c'est l'isolation de périmètre et la
   réversibilité — le dire ainsi, ne pas annoncer une décharge qui n'existe pas.
2. **Hiérarchie ontologique.** Le principe porte la section « Your sign in Sidy's
   natal chart ». `meta/CLAUDE.md` (corollaire agentique, art. 1) exige que toute
   donnée personnelle injectée dans un prompt porte sa qualification *zōsaku* en
   clair dans le texte. Aucun des douze prompts ne la porte aujourd'hui. Écart
   antérieur à ce chantier, signalé, non corrigé en douce ici.
3. **Les onze autres agents** restent en écart : hors périmètre de cette passe.
