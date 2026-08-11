---
title: "Synchronisation Obsidian / Working Copy / GitHub (circuit CONSULTATION)"
type: infrastructure
tags: [atelier, rd, infrastructure, obsidian, git, ipad, synchronisation]
created: 2026-06-29
updated: 2026-08-11
sources: []
links: []
---

# Synchronisation Obsidian / Working Copy / GitHub

> **Intégration du 2026-08-09** : cette fiche a été intégrée depuis le sas
> `_inbox/fiche-setup-obsidian-git-sync.md` (rédigée 2026-06-29, dépannage du
> jour même) vers `atelier/rd/infrastructure/` sur directive Sidy : tout ce
> qui relève de l'infrastructure globale hardware/software se consigne au
> pôle R&D. Contenu repris, dates `created`/`updated` conservées/bumpées.

## 1. Architecture de synchronisation

- **Obsidian (iPad)** : interface de lecture/édition (poste CONSULTATION,
  `CLAUDE.md` §postes). Le plugin communautaire **Obsidian Git** gère les
  commits *locaux* directement depuis l'app.
- **Working Copy (iPad)** : client Git natif iOS, lié en « Folder Sync » au
  dossier réel du vault Obsidian. Gère l'intégralité des opérations réseau
  (fetch/pull/push) vers GitHub.
- **GitHub** (`Sidyvision/wiki.git`) : dépôt central, remote `origin`,
  protocole **SSH** (`git@github.com:Sidyvision/wiki.git`).
- **Serveur Hetzner** : intègre le contenu et pousse ses commits vers le même
  dépôt GitHub, indépendamment du circuit iPad.

Division des rôles validée : **Obsidian Git = commits locaux uniquement.
Working Copy = tout le réseau (fetch/pull/push).**

## 2. Panne du 2026-06-29

### Symptôme initial
- Obsidian Git : `Can't find a valid git repository. Please create one via the
  given command or clone an existing repo.`
- Working Copy : repo « à jour » en apparence mais figé depuis le 12/06/2026.

### Diagnostic établi
1. Le lien **Working Copy ↔ dossier du vault Obsidian** (« Folder Sync »)
   s'était rompu, sans cause identifiée avec certitude (hypothèses : mise à
   jour iOS, redémarrage d'app). Conséquence : Working Copy travaillait sur un
   clone interne déconnecté du vrai dossier vault, et Obsidian Git ne trouvait
   plus de `.git` valide dans le dossier qu'il lisait.
2. Le repo Git sous-jacent (dans Working Copy) était sain : branche `main`,
   remote `origin` correctement configuré en SSH, aucune corruption. Un simple
   Fetch + Pull a suffi à le remettre à jour (24 commits récupérés).

### Cause racine confirmée (limite structurelle, pas un bug isolé)
**Le moteur Git interne du plugin Obsidian Git (implémentation JS embarquée,
pas un vrai client système) ne sait pas parler le protocole SSH.**

Erreur obtenue lors d'une tentative de push directement depuis Obsidian :
```
Git remote "git@github.com:Sidyvision/wiki.git" uses an unrecognized transport protocol: "ssh"
```

Limitation documentée dans la communauté Obsidian (les tutoriels tiers
utilisent systématiquement des URLs `https://` + Personal Access Token pour
que le plugin push/pull en autonomie). Contrainte du plugin, quel que soit le
client Git iOS utilisé en complément.

## 3. Procédure de réparation appliquée (2026-06-29)

1. **Working Copy** → « Status and Configuration » du repo `wiki` → menu du
   titre (« wiki ⌄ ») → **Link Repository to → Directory** → sélection du
   dossier réel du vault (`On My iPad → Obsidian → wiki`).
2. Constat : apparition du dossier `.obsidian/` (5 fichiers + 1 répertoire)
   précédemment invisible du clone Working Copy — preuve que le lien pointe
   désormais vers le vrai dossier vault.
3. Ajout au `.gitignore` :
   ```
   # Configuration locale Obsidian (par appareil, jamais versionnée)
   /.obsidian/
   ```
   Choix : ignorer tout le dossier plutôt qu'un filtrage fin (workspace
   uniquement), pour garder chaque appareil indépendant en plugins/réglages.
4. Commit du `.gitignore` depuis **Obsidian Git** (commit local OK).
5. Tentative de push depuis Obsidian Git → échec (erreur SSH ci-dessus).
6. Push effectué depuis **Working Copy** (Fetch → Pull/Merge → Push) → succès
   (`Push transmitted 32.4 Kbytes to origin/main`).
7. Vérification finale via l'historique Working Copy : `HEAD`, `main` et
   `origin/main` alignés sur le même commit de merge, incluant à la fois le
   commit `.gitignore` (iPad) et les commits d'intégration du jour faits
   depuis le serveur Hetzner — synchronisation confirmée dans les deux sens.

## 4. Routine de fonctionnement

1. Éditer et committer normalement dans **Obsidian** (panneau Source Control
   du plugin Git).
2. Basculer vers **Working Copy** pour Fetch → Pull → Push (jamais de
   push/pull réseau depuis Obsidian directement).

## 5. Décision — statu quo SSH (verdict Sidy, 2026-08-11)

**Question posée** : fallait-il migrer le remote `origin` de SSH vers HTTPS +
Personal Access Token (PAT), pour permettre à Obsidian Git de push/pull en
autonomie complète sans repasser par Working Copy ?

- **Avantage potentiel écarté** : un seul geste, tout dans l'app Obsidian,
  contre le détour actuel par Working Copy (3 touchers).
- **Inconvénient déterminant** : un PAT introduit un secret supplémentaire à
  créer, stocker dans les réglages du plugin et renouveler à expiration, alors
  que la clé SSH actuelle est déjà en place des deux côtés (Hetzner + Working
  Copy) et n'expire pas.
- **Verdict (2026-08-11)** : **statu quo — le remote reste en SSH.** Suit
  l'avis technique Hermes du 2026-08-09 (zéro secret à gérer, clé
  n'expirant pas ; le coût du détour Working Copy est jugé inférieur au coût
  de gestion d'un secret supplémentaire). Aucune modification du remote
  `origin` (`git@github.com:Sidyvision/wiki.git`) n'est à effectuer.
- **Réouverture** : cette décision n'est pas figée dans l'absolu — à
  rouvrir seulement si la routine §4 (détour Working Copy) devient un
  point de friction réel et répété, pas par principe.

## 6. Points de vigilance

- Le lien Folder Sync (Working Copy ↔ dossier vault) est un point de
  fragilité connu et documenté dans la communauté Obsidian (rupture possible
  après mise à jour iOS, redémarrage d'app). En cas de nouvelle panne
  (`Can't find a valid git repository`) : réappliquer la section 3, étapes 1-2.
- Le `.gitignore` exclut `/.obsidian/` en plus de la règle sur `/raw/*`
  (sources brutes non versionnées). Toute nouvelle règle d'exclusion s'ajoute
  à ce même fichier, à la racine du dépôt.
- Ne pas confondre « Fetch » (télécharge l'historique distant sans l'appliquer
  aux fichiers) et « Pull » (fusionne réellement les commits dans le dossier
  de travail) dans Working Copy — les deux actions sont nécessaires en
  séquence, le Fetch seul ne suffit pas.
- Un vault « cassé » peut n'être qu'un dépôt local en avance sur son remote :
  avant d'incriminer l'outil de consultation, vérifier l'état git côté serveur
  (`git status -sb`, `git rev-list --left-right --count origin/main...HEAD`) —
  cf. registre des problèmes, entrée [2026-08-09] vault désynchronisé.
