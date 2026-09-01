---
title: "INF-14 — hébergement du rendu sur sidyvision.com : plan"
type: infrastructure
chantier: INF-14
tags: [atelier, rd, infrastructure, chantier, plan, instrument, hebergement, netlify]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-14-hebergement-rendu-sidyvision/spec]]"
---

# INF-14 — plan

> **Statut : `brouillon`** — en attente du visa de Sidy, et **bloqué sur un fait
> matériel** : le jeton transmis n'ouvre pas le compte qui détient `sidyvision.com`
> (voir *Blocage* ci-dessous). Aucune manipulation du site en l'état.

## Blocage constaté le 2026-09-01 — le jeton n'ouvre pas le bon compte

Le jeton fonctionne : l'API répond, l'identité est `sidyvision@gmail.com`. Mais le
compte a été **créé le 2026-09-01** et porte **zéro site**, dans une équipe unique
`sidyvision-qgqrdly` (Free). Or `sidyvision.com` est bien servi par Netlify — en-têtes
`server: Netlify`, `x-nf-request-id`, DNS pointant sur les répartiteurs de Netlify — et
un site à domaine propre suppose nécessairement un compte.

**Conclusion, non supposition** : le site est détenu par un **autre compte Netlify** que
celui du jeton. Vraisemblablement une autre adresse de courriel, ou un compte ouvert par
un tiers ayant réalisé la page. Tant que le jeton du compte détenteur n'est pas
disponible, les étapes 2, 3 et 5 ne peuvent pas commencer — non par prudence, mais parce
que l'API ne voit pas le site.

Ce qui a pu avancer sans lui a avancé : la sauvegarde (étape 0) et la préversion
(étape 4) sont faites.

## Étape 0 — la sauvegarde d'abord, avant tout accès

La page de `sidyvision.com` **n'existe qu'en un exemplaire**, sur le CDN de Netlify :
aucun dépôt ne la porte. Toute manipulation ultérieure du déploiement pourrait
l'effacer sans recours. Elle est donc capturée et versionnée **avant** que quiconque
touche au site — y compris avant de se connecter.

```
curl -sSL https://sidyvision.com/ -o site-sidyvision-capture-2026-09-01.html
sha256sum site-sidyvision-capture-2026-09-01.html
```

La capture et son empreinte vivent dans le dépôt du site (étape 2). Tant que cette
étape n'est pas faite, aucune autre ne commence.

## Étape 1 — l'accès, transmis sans passer par la conversation

Un jeton d'accès personnel Netlify (*User settings → Applications → Personal access
tokens*) suffit ; il n'y a pas besoin du mot de passe du compte.

**Il ne se colle pas dans la conversation** — tout ce qui y est écrit est conservé dans
la transcription de session. Il se dépose hors de portée :

```
# à taper directement dans le terminal, jamais dicté à la machine
printf 'NETLIFY_AUTH_TOKEN=%s\n' 'le-jeton' > ~/.netlify-token && chmod 600 ~/.netlify-token
```

Le jeton est **révocable en un clic** depuis la même page, et le sera à la fin du
chantier — un accès permanent n'est pas nécessaire pour une mise en place.

## Étape 2 — mettre le site sous contrôle (le gain réel du verdict « chemin »)

Le verdict `sidyvision.com/instrument` oblige à toucher au déploiement du site ; autant
que ce passage obligé produise quelque chose. Un dépôt `Sidyvision/sidyvision-site` est
créé, portant :

- `index.html` — la capture de l'étape 0, **inchangée**, anomalie de forme comprise
  (la reproduire à l'identique est la seule preuve que rien n'a bougé) ;
- `_redirects` — la règle de service du rendu (étape 3) ;
- la capture horodatée et son empreinte, conservées comme jalon.

Le site Netlify existant est alors rattaché à ce dépôt. À partir de là, il est
redéployable par n'importe qui, depuis le serveur, sans clic — critère 5.

## Étape 3 — servir `/instrument` : le montage par proxy est ÉCARTÉ

> **Amendement du 2026-09-01, à l'exécution.** Le plan prévoyait une réécriture
> `_redirects` de `/instrument/*` vers un second site Netlify. **Éprouvé, cela ne
> marche pas** — et c'est une contrainte de l'hébergeur, pas une erreur de montage.

**Le constat.** Le site de préversion a été créé et déployé
(`instrument-tradition-primordiale.netlify.app`, déploiement `ready`, les deux fichiers
téléversés). Il répond **`HTTP 401`** : Netlify place désormais les sous-domaines
`*.netlify.app` des comptes gratuits récents derrière une authentification
(*edge-access*), quel que soit le contenu. Une réécriture proxy vers cette origine
hériterait du 401 : le montage ne peut pas fonctionner.

**Ce que cela invalide, et ce que cela ne touche pas.** Le verdict de Sidy — un chemin,
`sidyvision.com/instrument` — reste exécutable. C'est le *mécanisme* qui change, pas
l'adresse. Deux voies subsistent :

1. **Le rendu est déployé *dans* le site lui-même**, sous `/instrument/`. Un seul site
   Netlify, aucun proxy, aucune origine à authentifier. Le site portant déjà un domaine
   propre, l'*edge-access* ne s'y applique pas. **Voie retenue** : c'est la seule qui
   satisfasse le verdict sans dépendre d'une origine verrouillée.
   L'étanchéité des dépôts est préservée par la **construction**, non par le rangement :
   le dépôt du site ne contient pas le rendu, il le **récupère au build** depuis le
   dépôt `Sidyvision/instrument`, désormais **public** — donc sans le moindre
   identifiant, et strictement à sens unique.
2. Attacher un domaine propre au site de rendu (`instrument.sidyvision.com`) lèverait
   aussi le 401 — mais c'est le sous-domaine que Sidy a écarté. Non retenu.

**Commande de construction du site**, sans secret ni dépendance :

```
mkdir -p instrument && curl -sSL \
  https://raw.githubusercontent.com/Sidyvision/instrument/main/src/index.html \
  -o instrument/index.html && curl -sSL \
  https://raw.githubusercontent.com/Sidyvision/instrument/main/src/wiki-manifest.json \
  -o instrument/wiki-manifest.json
```

Les deux fichiers restent **frères de dossier** (contrainte INF-13) et l'URL
`/instrument/` conserve sa barre oblique finale, dont dépend le `fetch` relatif.

## Étape 4 — le site de préversion

**Fait le 2026-09-01** : `instrument-tradition-primordiale.netlify.app`, déploiement par
l'API (empreintes SHA-1 des fichiers, téléversement, état `ready`). Il est conservé
comme **banc de préversion** — son 401 n'est pas un défaut dans ce rôle : le protocole
veut précisément qu'une préversion ne soit pas publique (Action PUBLICATION, point 4).

## Étape 5 — vérification, puis seulement, mise en service

Les six critères du `spec.md`, dans l'ordre, **le critère 1 en premier** : la page
d'accueil doit être octet pour octet identique à la capture. Si elle ne l'est pas, on
s'arrête et on restaure — on ne poursuit pas en espérant que cela se règle.

## Fichiers touchés

| Fichier | Nature |
|---|---|
| dépôt `Sidyvision/sidyvision-site` (nouveau) | création — `index.html`, `_redirects`, capture |
| `atelier/rd/infrastructure/2026-09-01_hebergement-instrument-netlify.md` | création — la fiche d'infrastructure, avec `infra_verif` si un contrôle mécanique est possible |
| ce dossier de chantier | mise à jour du statut |
| dépôt `Sidyvision/instrument` | **inchangé** — il est consommé, pas modifié |

Les éléments sensibles — jeton, identifiants de compte, identifiants de site — vont en
`meta/projet-unifie/`, **jamais** dans `rd/infrastructure/`, qui ne reçoit que ce qui
est publiable (`atelier/CLAUDE.md`).

## Points de retour à l'humain (Cmd 13)

- Le visa de ce plan.
- La transmission du jeton, puis sa révocation en fin de chantier.
- La mise en service effective : **préversion d'abord, production après validation
  explicite** — le point 4 de l'Action PUBLICATION du label, non négociable.
- La réparation du doctype doublé de la page d'accueil : chantier distinct, si Sidy le
  veut.

## Journalisation

`atelier/annales.md` et la ligne INF-14 du registre, même passe (Cmd 9).
