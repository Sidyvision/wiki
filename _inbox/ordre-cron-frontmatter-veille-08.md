# Ordre de travail — à l'attention d'Hermes CLI (session avec accès serveur)

**Émis** : 2026-08-24, sur mandat explicite de Sidy, suite au contrôle du dépôt
2026-08-19→23 et à la fusion du rôle Librarian-Archivist (13) dans la position
08 (voir `meta/projet-unifie/hermes-prompts/08-publication-site.md`,
« Third mandate », et `meta/meta-annales.md` entrée `[2026-08-24]`).

Ce fichier ne demande **aucune intégration de contenu** dans un circuit — c'est
une instruction opérationnelle pure, à traiter puis retirer du sas comme
`ordre-lot1-rig-veda.md` précédemment. Créer le job relève de la porte humaine
(Cmd 13) : cette session (git seul, sans accès `hermes`/serveur) ne peut pas
l'exécuter elle-même.

## Action 1 — créer le cron « veille-frontmatter-quotidien »

- **Cadence** : `0 11 * * *` (tous les jours, 11:00 UTC — avant Studio
  12:00/12:05 et Gardien 12:30).
- **Profil** : celui qui sert la position 08 (`publication` dans la liste des
  12 profils actifs — à confirmer : le profil `librarian-archivist`, ouvert au
  moment de la création du rôle 13 jamais activé, existe peut-être encore
  séparément côté serveur. Si oui, signaler l'écart à Sidy avant de choisir
  lequel des deux porte ce cron — ne pas trancher silencieusement).
- **Canal** : `#infrastructure` (même canal que Studio).
- **Mode** : agent (pas `no_agent`) — le mandat exige un signalement sémantique
  (lecture de contenu, jugement de flag), pas seulement un script pur.
- **Prompt** : reprendre tel quel le texte de la section « Third mandate —
  Frontmatter veille » de `meta/projet-unifie/hermes-prompts/08-publication-site.md`
  (portée : **l'ensemble des fichiers du dépôt**, pas seulement le périmètre de
  la position 08 — tel que demandé par Sidy).

Précautions déjà documentées dans `atelier/rd/cahiers/registre-problemes.md`
(entrées `[2026-08-17]`, `[2026-08-18]`), à ne pas reproduire :
- Jamais de lien symbolique pour un script appelé par un job — copie réelle
  dans `~/.hermes/profiles/<profil>/scripts/` si un script est référencé.
- Un job `no_agent` ne reçoit aucun argument ni cwd différent du défaut —
  sans objet ici puisque le mode est agent, mais si le mandat évolue vers un
  script pur, prévoir un wrapper qui fixe `--racine /root/wiki` en dur.
- Vérifier par lecture directe du fichier de sortie persisté après la première
  exécution, jamais sur la seule foi de `last_status: "ok"`.

## Action 2 — réconcilier le cron `investigation-doctrinale-gardien`

Écart relevé lors du contrôle : ce cron (profil `gardien`, quotidien 12:30 UTC,
canal Discord `1535804669300052039`) tourne depuis avant ce contrôle mais
n'était documenté nulle part dans `meta/projet-unifie/hermes-prompts/
10-protocol-guardian.md` — contrairement au mandat de Studio, documenté dans
sa propre fiche. Une section « Cron mandate » a été ajoutée à la fiche
Gardien le 2026-08-24 pour combler ce vide, mais **sans reconstituer le texte
exact du prompt tournant côté serveur** (non retrouvé dans le dépôt — pas
fabriqué, Cmd 12). Comparer le prompt réellement configuré
(`hermes cron edit investigation-doctrinale-gardien -h` ou lecture directe de
`~/.hermes/profiles/gardien/cron/jobs.json`) à la Mission et aux Guardrails de
`10-protocol-guardian.md`, et signaler tout écart à Sidy plutôt que de choisir
unilatéralement lequel des deux (fiche ou job réel) fait foi.

## Action 3 — signalement pour verdict Sidy (pas d'action automatique)

Le job Studio (`monitoring-infrastructure-quotidien`, profil `default` ou
`studio` selon la source consultée — à vérifier) exécute déjà
`verifier-invariants.py --racine /root/wiki` comme §1 de son rapport
quotidien. Le nouveau job de l'Action 1 exécute le même appel, une heure plus
tôt, sous un profil et un canal différents — redondance délibérément
conservée pour l'instant (même précédent que le job `no_agent` parallèle du
Gardien), mais Sidy doit trancher explicitement s'il souhaite alléger le §1
de Studio une fois ce nouveau job confirmé fiable.

---

**Statut** : à traiter par la prochaine session ayant l'accès `hermes`/serveur.
Retirer ce fichier du sas une fois les trois actions exécutées ou explicitement
renvoyées à Sidy, sur le modèle de `ordre-lot1-rig-veda.md` (vidangé le
2026-08-23, commit `aa3c9ff`).
