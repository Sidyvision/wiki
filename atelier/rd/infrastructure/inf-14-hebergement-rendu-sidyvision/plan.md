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

> **Statut : `brouillon`** — en attente du visa de Sidy et de l'accès Netlify (proposé
> par Sidy le 2026-09-01, non encore transmis). Aucune manipulation du site avant les
> deux.

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

## Étape 3 — servir `/instrument`

Netlify sait servir un chemin depuis un **autre** site par réécriture. Fichier
`_redirects` du dépôt du site :

```
/instrument/*  https://<site-instrument>.netlify.app/:splat  200
/instrument    /instrument/                                  301
```

Le code `200` est une réécriture, non une redirection : l'URL affichée reste
`sidyvision.com/instrument/`. La seconde ligne garantit la barre oblique finale, dont
dépend le `fetch` relatif du manifeste (contrainte INF-13).

Ce montage garde les deux dépôts **étanches** : le site ne contient pas le rendu, le
dépôt de rendu ne contient pas le site. Le joint est invisible à l'usage et
intégralement documenté dans git — article 6 de la convention Sashimono.

## Étape 4 — le site du rendu

Un site Netlify lié à `Sidyvision/instrument` : pas de commande de construction,
répertoire publié `src/`. Chaque poussée sur `main` redéploie (critère 4).

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
