# Procédure de déploiement — wiki → moteur (agent 08)

**Statut : EXÉCUTÉE le 2026-08-31**, sur go explicite de Sidy (Cmd 13), en même temps
que la bascule de routage rendue nécessaire par l'épuisement du Qwen Token Plan
jusqu'au 5 septembre. Vérification de bout en bout au bas de cette page.

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

## Séquence (exécutée le 2026-08-31)

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


---

## Exécution du 2026-08-31 — trace

**Routage.** Le profil `publication` était **déjà** sur `auto/best-free` via
`custom:omniroute` (`config.yaml` du profil, posé le 2026-08-26 ; process redémarré le
2026-08-30, donc config chargée). Rien à changer : le dernier cycle Choura du 2026-08-30
tournait déjà en `model=auto/best-free`. Les erreurs `HTTP 429 token-plan quota
exhausted` du journal datent des 27-28 août, quand ce profil était encore sur Qwen.

`auto/best-free` est confirmé exposé par omniroute (`GET /v1/models`, 511 modèles),
avec `tool_calling: true` — condition nécessaire pour un agent outillé.

**Prompt.** Séquence appliquée :

| Étape | Résultat |
|---|---|
| Sauvegarde | `SOUL.md.bak-20260831-072908` (1 601 o), hors dépôt |
| `08-principe.md` → `SOUL.md` | 3 628 o, 62 lignes, 0 caractère invisible |
| 3 mandats → `skills/hermes/<nom>/SKILL.md` | frontmatter `name`/`description` validé en YAML |
| `comparer-prompts-hermes.py --derive` | **publication ✅ synchronisé** — premier agent aligné dépôt↔moteur (11 restants en écart) |

**Redémarrage.** Nécessaire — et pour une seule raison, vérifiée dans le code du moteur :
`load_soul_md()` relit `SOUL.md` à chaque construction de prompt, sans cache, donc le
principe seul n'aurait pas exigé de redémarrage ; mais `build_skills_system_prompt()`
garde un cache LRU en process dont **la clé ne contient ni mtime ni manifeste** — les
trois mandats seraient restés invisibles jusqu'à la fin de vie du process.

**Correction d'une donnée fausse du dépôt** : `bureau/modules/hermes_status.py`
affirmait en docstring que « les agents tournent en process de fond, pas en service
systemd — vérifié le 2026-08-15 ». C'est faux aujourd'hui : `hermes-gateway-publication.service`
est un service **systemd user**, `enabled`. Le redémarrage est donc supervisé et sûr.

**Vérification de bout en bout** (l'agent interrogé en direct) :

```
$ hermes --profile publication -z "ton signe zodiacal, puis les noms exacts de tes trois mandats"
Sagittarius ; site-orchestration, bibliothecaire, veille-referencement.
```

L'ancien `SOUL.md` ne contenait **aucune** section « Zodiac principle » : la réponse
prouve que le nouveau principe est chargé, et la liste des mandats que l'index des
skills est reconstruit. Route confirmée au journal : `model=auto/best-free`,
`provider=custom base_url=http://localhost:20128/v1`.

**Retour arrière** (inchangé, toujours valable) :

```bash
cp ~/.hermes/profiles/publication/SOUL.md.bak-20260831-072908 ~/.hermes/profiles/publication/SOUL.md
rm -rf ~/.hermes/profiles/publication/skills/hermes
hermes --profile publication gateway restart
```

---

## Généralisation aux 11 autres agents — EXÉCUTÉE le 2026-08-31 14:26

Sur go explicite de Sidy (Cmd 13). Même séquence, appliquée aux onze profils restants.
`publication` n'a pas été retouché : il était déjà synchronisé.

### Sauvegardes (point de retour, hors dépôt)

`~/.hermes/profiles/<profil>/SOUL.md.bak-20260831-142649` — un par profil, pris avant
écriture. Retour : `cp SOUL.md.bak-20260831-142649 SOUL.md` puis redémarrage de la
passerelle si elle tourne.

### Résultat — sortie brute de `--derive` après déploiement

```
profil            wiki  SOUL.md  état
ar-music          2842     2842  ✅ synchronisé
visual-da         4167     4167  ✅ synchronisé
production        2386     2386  ✅ synchronisé
admin-legal       2800     2800  ✅ synchronisé
accounting        2783     2783  ✅ synchronisé
distribution      2679     2679  ✅ synchronisé
marketing         2605     2605  ✅ synchronisé
publication       3595     3595  ✅ synchronisé
studio            3711     3711  ✅ synchronisé
gardien           2880     2880  ✅ synchronisé
fanzine           2693     2693  ✅ synchronisé
commerce          3266     3266  ✅ synchronisé

VERDICT : 0 agent(s) en écart sur 12.
```

Hygiène Unicode (Cmd 15) sur le moteur, `SOUL.md` **et** `SKILL.md` : **0 résultat**.
Les 3 U+200D résiduels de `studio/SOUL.md`, hors dépôt et donc hors du nettoyage du
2026-08-22, sont partis avec ce déploiement.

### Mandats déployés en skills

| profil | skills posés |
|---|---|
| studio | `infrastructure-veille`, `studio-sound-engineer` |
| gardien | `protocol-guardian`, `veille-protocole` |
| les 9 autres | un skill homonyme du poste |

Chaque `SKILL.md` porte le frontmatter `name` + `description` attendu par le moteur, le
corps restant le mandat verbatim. La description dit **quand** charger le mandat : c'est
elle seule qui reste en contexte.

### Redémarrages — et pourquoi ils étaient nécessaires

`SOUL.md` est relu à chaque construction de prompt : le principe était donc actif sans
redémarrage. Les **skills** passent par un cache dont la clé ne porte ni mtime ni
manifeste : sans redémarrage, un mandat déposé sur le disque reste invisible à l'agent.

Quatre passerelles tournaient (`gardien`, `publication`, `studio` — permanentes — et
`visual-da`) ; elles ont été redémarrées une à une par `systemctl --user restart`.
**Jamais `hermes --profile X -z` sur un profil vivant** : cette vérification arrête
l'agent (constaté sur `distribution` le 2026-08-31).

Les huit profils dormants n'ont pas été réveillés : ils prendront principe et mandats à
leur prochaine ouverture de fenêtre par l'orchestrateur. La RAM (3 819 Mo, ~730 Mo
disponibles après redémarrage) ne permettait pas de les lever ensemble.

### Vérification côté moteur (§VIII.2) — sortie brute

Le disque ne prouve pas le chargement. Le compte de skills annoncé par la passerelle le
prouve :

```
gardien      08:56 → 84 skill(s)   |  14:27 → 86 skill(s)
studio       08:56 → 84 skill(s)   |  14:27 → 86 skill(s)
publication  08:56 → 87 skill(s)   |  14:27 → 87 skill(s)   (inchangé, déjà déployé)
```

+2 sur les deux profils qui reçoivent deux mandats, 0 sur celui qui n'en reçoit aucun de
nouveau. Le hook Choura s'est réenregistré au passage :
`2026-08-31 14:27:15 shell hook registered: pre_llm_call -> …/choura-contribution-sidy.py`.
