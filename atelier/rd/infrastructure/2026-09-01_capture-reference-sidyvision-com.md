---
title: "Capture de référence de sidyvision.com — sauvegarde préalable à INF-14"
type: infrastructure
chantier: INF-14
tags: [atelier, rd, infrastructure, sauvegarde, netlify, sidyvision]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/infrastructure/inf-14-hebergement-rendu-sidyvision/plan]]"
---

# Capture de référence de `sidyvision.com`

> **Pourquoi cette fiche existe.** La page d'accueil de `sidyvision.com` n'existait,
> au 2026-09-01, **qu'en un seul exemplaire** : sur le CDN de Netlify. Le compte GitHub
> ne porte que `wiki` et `instrument` — aucun dépôt ne contient le site, qui est un
> déploiement manuel. Une erreur de manipulation lors du chantier INF-14 l'aurait donc
> effacée sans recours possible.
>
> La capture a été prise **avant tout accès au compte Netlify**, avant même la demande
> de jeton. C'est l'étape 0 du plan, et elle ne dépendait d'aucun verdict : sauvegarder
> ce qui n'existe qu'une fois ne se négocie pas.

## L'empreinte

| | |
|---|---|
| Fichier | `captures/2026-09-01_sidyvision-com-racine.html` |
| Taille | 466308 octets |
| SHA-256 | `8411bc963f9e725050f57aed213b65d370c5953b68c0843b395c76cb1e535aa6` |
| Prise le | 2026-09-01 |
| Source | `https://sidyvision.com/` (HTTP 200 ; `www` y redirige) |

Cette empreinte est la **référence du critère 1** d'INF-14 : après mise en service, la
page d'accueil doit rester octet pour octet identique. Une divergence arrête le
chantier et déclenche la restauration.

## Ce que la page contient

Document HTML statique servi par Netlify (en-têtes `server: Netlify`,
`x-nf-request-id`). Titre : « Dans l'Absolu — Sidy Kouyaté ». Le corps entier est une
**image JPEG encodée en base64**, mise en page par une feuille de style de quelques
lignes. Aucun CMS, aucun générateur détectable, aucun script.

## Anomalie de forme — relevée, non corrigée

La page porte **deux `<!DOCTYPE html>` et deux balises `<html>` imbriquées** : un
document HTML complet a été collé à l'intérieur d'un autre. Les navigateurs le tolèrent
et la page s'affiche correctement ; le document n'en est pas moins invalide.

Elle est **conservée telle quelle**, délibérément (Cmd 12 — on rapporte, on ne répare
pas d'office). Deux raisons : reproduire la page à l'identique est la seule preuve que
le chantier n'a rien altéré ; et une réparation, si Sidy la veut, est un chantier
distinct qui ne doit pas se glisser dans celui-ci.
