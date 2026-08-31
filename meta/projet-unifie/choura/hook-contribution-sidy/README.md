# Hook « contribution de Sidy » — copie de référence

**Ce fichier n'est pas celui qui s'exécute.** Il vit hors dépôt :

| Ici (référence) | En production |
|---|---|
| `choura-contribution-sidy.py` | `/root/.hermes/scripts/choura-contribution-sidy.py` |
| (extrait de config) | bloc `hooks:` de `/root/.hermes/profiles/gardien/config.yaml` |

## Ce qu'il fait

Quand Sidy poste dans le salon Choura (`#général`, `1534857297321394248`), son
message est inscrit dans le fichier de cycle du jour comme sa contribution au
tour, **sans qu'il ait à mentionner un agent par `@`**.

## Pourquoi un hook, et pas une consigne de prompt

Le moteur Hermes n'a jamais exigé de `@mention` : la passerelle Discord d'un
profil reçoit les messages des salons autorisés (`discord.allowed_channels`) et
les passe au modèle. Ce qui manquait n'était pas l'écoute, c'était **l'écriture** :
rien ne versait la parole de Sidy dans `cycle-AAAA-MM-JJ.md`, si bien qu'un agent
qui se réveille à 2 h du matin ne pouvait pas la lire. Le hook comble ce trou en
amont du modèle — il ne dépend d'aucune obéissance de l'agent, donc il ne peut pas
être « oublié » par un tour bavard (§VIII.2 : fiabilité d'action ≠ fiabilité
narrative).

## Pourquoi sur le seul profil `gardien`

Le gardien tient la veille en permanence (`PERMANENTS` de l'orchestrateur de
fenêtres) et c'est lui qui ouvre et clôt le cycle. Brancher le hook sur chaque
profil produirait **une entrée par profil éveillé** pour un même message.

## Contrat

- **Événement** : `pre_llm_call`. Protocole : JSON sur stdin
  (`hook_event_name`, `session_id`, `cwd`, `extra`), JSON facultatif sur stdout
  (`{"context": "…"}` réinjecté dans le prompt du tour).
- **Filtres** : `platform == "discord"`, message non vide, et salon
  `1534857297321394248` lorsqu'un identifiant de salon est trouvable dans la charge.
- **Fichier visé** : `cycle-<date d'ouverture>.md` — la date bascule à **12:00
  heure de Paris**, comme la rotation des tours. Avant midi, le cycle courant est
  celui de la veille.
- **Insertion** : avant le marqueur `## Gabarit d'entrée`, en titre
  `## [AAAA-MM-JJ HH:MM] sidy (contribution humaine, salon Choura)` suivi du
  message en citation ; `updated:` du frontmatter relevé (Cmd 8).
- **Idempotence** : `sha256(session_id|message)` mémorisé dans
  `.choura-contributions-vues.json` (borné à 500 entrées) — un rejeu n'écrit pas
  deux fois.
- **Non bloquant** : toute erreur est avalée. Un hook qui échoue ne doit jamais
  empêcher un agent de répondre.

## Ce qui reste à la main de Sidy

`hooks_auto_accept: true` est nécessaire pour que le hook s'enregistre hors TTY.
Il vaut pour le profil `gardien` seul.
