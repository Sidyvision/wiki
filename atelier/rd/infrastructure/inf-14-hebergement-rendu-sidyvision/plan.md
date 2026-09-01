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

> **Statut : `execute`** — plan approuvé, exécuté, et **mis en production le
> 2026-09-01** après validation explicite de Sidy dans la session courante (Action
> PUBLICATION du label, point 4). Le rendu est servi sur
> **`https://sidyvision.com/instrument/`**. Les six critères du `spec.md` ont été
> contrôlés en ligne, le critère 1 en premier : page d'accueil **octet pour octet
> identique** à la capture de référence.

## Le blocage du compte, levé le 2026-09-01

Le premier jeton transmis ouvrait un compte **créé le jour même, portant zéro site** :
`sidyvision.com` était détenu par un autre compte. Sidy a rectifié. Le second jeton
ouvre le bon compte — site `lively-mousse-a649f7`, domaine propre `sidyvision.com`,
alias `sidykouyate.com`, dernier déploiement du 2026-05-11, **aucun dépôt lié**.

## Le montage retenu, après épreuve

Le proxy est écarté (401 *edge-access*, voir étape 3). Le montage effectif est plus
simple encore que la voie 1 envisagée : **un déploiement direct par l'API**, portant la
page d'accueil et le rendu dans le même site. Aucune construction, aucune liaison
GitHub, aucun secret dans un service tiers.

**Conséquence à connaître** : le déploiement par empreintes **remplace l'intégralité du
site** — tout fichier non listé disparaît. La page d'accueil est donc renvoyée à chaque
passe, et le script vérifie son empreinte SHA-1 *avant* l'envoi. Sans ce garde-fou, une
capture altérée effacerait silencieusement la page. C'est le contrôle le plus important
du chantier.

**Contrepartie levée le jour même, sur demande de Sidy.** La mise à jour automatique
est en place — mais **pas** par liaison Netlify → dépôt, qui aurait été le réflexe. Deux
raisons de l'écarter : elle exige une autorisation OAuth par navigateur, impossible
depuis le serveur ; et surtout le site aurait publié **la racine du dépôt frère**, donc
**écrasé la page d'accueil de `sidyvision.com`**. Le déploiement par empreintes
remplaçant l'intégralité du site, la page d'accueil doit être renvoyée à chaque passe —
ce qu'une liaison ne sait pas faire.

La voie retenue est une **GitHub Action** dans le dépôt frère
(`.github/workflows/publier.yml`, PR #1), qui rejoue exactement l'API et le garde-fou du
script local : elle récupère la page d'accueil depuis la capture de référence versionnée
au wiki — public, donc sans identifiant —, **vérifie son empreinte SHA-1 avant tout
envoi**, publie, puis contrôle le résultat en ligne. Deux secrets déposés par l'API
GitHub : `NETLIFY_AUTH_TOKEN` et `NETLIFY_SITE_ID`.

Éprouvée de bout en bout le 2026-09-01 (`workflow_dispatch`, exécution `33560404893`,
`success`) : *page d'accueil conforme à la référence* → *publié* → *page d'accueil
intacte* → *rendu en ligne identique au dépôt* → *manifeste servi : 46 nœuds*.

**Ce qui reste non éprouvé, et il faut le dire** : le déclencheur `on: push` filtré sur
`src/**` n'a pas encore été vu s'exécuter — la fusion de la PR ne touchait pas `src/`, et
fabriquer une modification artificielle pour le prouver n'aurait rien prouvé de bon. Il
fera ses preuves à la première modification réelle du rendu.

**Friction levée le jour même, sur verdict de Sidy** : `enforce_admins` est aligné sur la
doctrine du wiki — `false`, flux par pull request non imposé, garde-fou local en relais
(PRO-01). Force-push et suppression de branche restent interdits : la forme exacte du
wiki.

**Mais l'alignement retirait une garde qui servait.** Depuis `publier.yml`, une poussée
sur `main` touchant `src/**` **publie en production** ; la pull request tenait lieu de
porte humaine. Elle n'est plus exigée, donc **la porte se déplace dans le hook
`pre-push`** — elle ne disparaît pas (Cmd 13 ; Action PUBLICATION, point 4). Le hook
refuse une poussée de `src/` sur `main` sans `PUBLIER=1`, et le dit en toutes lettres.
Éprouvé dans un clone jetable, sans rien publier : refus sans la variable, passage avec.

**Un défaut trouvé en chemin, et il est du même genre que celui de PRO-01.** Les deux
hooks cherchaient le motif `fetch('wiki-manifest.json')`, parenthèse fermante comprise ;
l'appel réel est `fetch('wiki-manifest.json', {cache: 'no-cache'})`. **Zéro
correspondance** : le contrôle de fraternité de dossier n'avait jamais rien inspecté
depuis son écriture. C'est exactement la faute caractérisée au wiki le 2026-08-31 — une
porte gardée par un contrôle qui ne regarde rien — reproduite le jour même dans du code
neuf, et découverte par hasard en instrumentant les hooks pour un tout autre motif.
Corrigé, puis **éprouvé dans les deux sens** : vert sur le dépôt sain, refus en bac à
sable quand le manifeste manque. Un contrôle dont on n'a pas vu l'échec n'est pas
vérifié — c'est la leçon, et elle vient de se payer deux fois.

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
