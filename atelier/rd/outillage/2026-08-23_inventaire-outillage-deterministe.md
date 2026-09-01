---
title: "Inventaire de l'outillage déterministe du dépôt (relevé du 2026-09-01)"
type: outillage
tags: [rd, outillage, inventaire, scripts, verification]
created: 2026-09-01
updated: 2026-09-01
sources: []
links:
  - "[[atelier/rd/index]]"
  - "[[atelier/rd/registre-chantiers]]"
---

# Inventaire de l'outillage déterministe du dépôt

> **Contrepartie neutre**, écrite le 2026-09-01, d'un plan d'action du 2026-08-23 versé le
> même jour au Domaine Réservé : ce plan mêlait à un inventaire d'outillage un volet de
> soutien personnel, ce que le §VI interdit dans une page neutre. Ne subsiste ici que
> l'inventaire — l'outil, pas la personne qu'il sert.
>
> **Ce que cette fiche n'est pas** : une documentation de chaque script. Chacun porte la
> sienne (`spec-*.md` de `rd/outillage/`, guide de déploiement au Domaine Réservé pour le
> vérificateur). Elle répond à une seule question : *quels contrôles mécaniques le dépôt
> possède-t-il, et lequel appeler ?*

## Principe

Tous ces scripts obéissent à la même règle, celle du §VIII : **déterministes, sans LLM,
sans réseau**. Ils constatent, ils ne corrigent pas, et ils sortent en code non nul quand
un invariant est rompu. C'est la contrepartie du constat des tests de 2026-06-29 →
07-03 — *fiabilité d'action ≠ fiabilité narrative* : l'auto-rapport d'un modèle n'est pas
une preuve, la sortie d'un script en est une.

## Ce que le dépôt possède, vérifié au disque le 2026-09-01

| Script | Ce qu'il établit | Quand l'appeler |
|---|---|---|
| `verifier-invariants.py` (racine) | Sceaux et frontmatter (A, B), intégrité et étanchéité des liens (C), discipline append-only des annales | **Avant chaque commit** — c'est le juge de paix |
| `carte-du-depot.py` (racine) | Cartes dérivées par circuit, détection des fiches orphelines | après une passe qui crée ou déplace des fiches |
| `atelier/rd/outillage/graphe/generer-cartographie.py` | `graphe-cartographie.json` — graphe du dépôt, sévérité à deux niveaux (bloquant / avertissement) | après une passe structurante |
| `atelier/rd/outillage/detecter-non-tracke.py` | Fichiers présents mais non suivis par git, classés par circuit | quand on soupçonne un dépôt incomplet |
| `atelier/rd/outillage/verifier-coherence-infrastructure.py` | Confronte les `infra_verif` des fiches à la configuration Hermes réelle — **contrôle anti-fabulation** | dès qu'une fiche déclare une configuration appliquée |
| `atelier/rd/outillage/archiver-monitoring-quotidien.py` | Archive `.txt` du rapport de monitoring, rétention 40 jours | appelé par son enveloppe cron |
| `atelier/rd/outillage/generer-manifeste.py` | `wiki-manifest.json` depuis `instrument-donnees.yaml`, validations bloquantes, zéro LLM dans la boucle | à chaque évolution des données de l'Instrument |
| `atelier/rd/outillage/srs.py` | Cartes de révision espacée du protocole | chantier `OUT-03`, format non arrêté |
| `atelier/rd/bibliotheque/valider-index-livres.py` | Contrôles bloquants des index d'ouvrages (Cmd 15, pages, couverture, doublons signalés jamais fusionnés) | avant toute génération du lexique |
| `atelier/rd/bibliotheque/generer-glossaire-unifie.py` | Lexique unifié dérivé — **refuse de générer si le validateur bloque** | après validation des index |
| `atelier/rd/outillage/hooks/` (`pre-commit`, `pre-push`) | Garde-fous locaux : hygiène Unicode à chaque commit, invariants + Unicode à chaque push | installés une fois par clone (`installer-hooks.sh`) |

Le dossier `Graphe/` que citait le plan d'origine **n'existe pas** à la racine : les deux
scripts qu'il lui attribuait sont `carte-du-depot.py` (racine) et
`atelier/rd/outillage/graphe/generer-cartographie.py`. Corrigé ici.

## Ce qui manque encore

- **`OUT-02`** — l'étanchéité n'est contrôlée mécaniquement que dans un sens :
  `ETANCHEITE_INTERDITE` ne porte que la clé `doctrinal`, de sorte qu'un lien
  `atelier/rd/` → `meta/` ne remonte qu'en avertissement, jamais en erreur bloquante.
- **`OUT-05`** — aucun contrôle ne détecte un corps d'entrée d'annales orphelin. L'incident
  du 2026-08-28 (en-tête d'entrée mangé à l'insertion) n'a été vu par aucun script.
- **`OUT-03`** — le SRS Hermes-native n'a ni format arrêté, ni mécanisme de révision.

## Le contrôle serveur (ajouté le 2026-09-01)

Le workflow `lint` de GitHub, qui garde la branche `main`, exécute désormais les deux
mêmes contrôles bloquants que le hook `pre-push` — `verifier-invariants.py` puis l'hygiène
Unicode — dans le même ordre. C'est délibéré : **un push accepté localement doit être vert
côté serveur**, sinon le garde-fou local donne confiance à tort.

Jusqu'au 2026-09-01 ce contrôle ne validait rien : il parcourait un dossier `wiki/`
inexistant, hérité de l'arborescence abandonnée le 2026-06-11, et rendait vert sur zéro
fichier (chantier `PRO-C3`).

## Ce qui a changé le 2026-09-01

`verifier-invariants.py` ne parcourt plus le disque entier : il interroge git et ne
contrôle que ce qui appartient au dépôt (chantier `OUT-C2`, clos). Sur le dépôt réel il
rendait 210 erreurs, dont 209 de bruit venant de venv de dépendances tierces et du sas
`raw/` — et ce bruit avait masqué la seule erreur vraie du jour. Il rend désormais
**0 erreur, 0 avertissement sur 709 fiches**, et annonce en tête le périmètre qu'il a
appliqué. `--tout` restitue le comportement antérieur : rien n'est hors de portée, c'est
un choix d'appel.

`generer-cartographie.py` portait **le même défaut**, découvert en régénérant le graphe
dans la foulée : 112 anomalies de frontmatter venues du venv de l'essai Graphify, et un
refus d'écrire le manifeste. Même correction — exclusion des dossiers cachés (règle que
`carte-du-depot.py` appliquait déjà) puis consultation de git. Le graphe se régénère de
nouveau. C'est le signe que le défaut était de famille et non d'un script : tout outil qui
parcourt le disque doit se demander ce qui appartient au dépôt.
