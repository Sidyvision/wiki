---
title: Bilan R&D 2026-08-15 — pont inter-agents
type: meta
statut: synthese
tags:
- atelier
- rd
- bilan
- pont
- continuite
created: 2026-08-15
updated: 2026-09-01
sources: []
links:
- '[[atelier/rd/cahiers/registre-problemes]]'
---

# Bilan R&D 2026-08-15 — pont inter-agents

> **Jalon daté du 2026-08-15 — ne décrit pas l'état courant.** Ce bilan est la photographie de la période 2026-08-08 → 2026-08-15. Il est conservé tel quel.
> L'état **vivant** des chantiers (tous pôles, doctrine incluse) est tenu depuis le
> 2026-09-01 dans [[atelier/rd/registre-chantiers]], qui cite la présente fiche comme
> décision d'ouverture des chantiers qu'elle a ouverts. Corps non retouché (Cmd 10).

> **Objet** : document de synthèse destiné à tout agent (Hermes terminal,
> Claude Code, ou autre) qui reprendrait le fil des travaux R&D sans avoir
> participé aux sessions antérieures. Couvre la période 2026-08-08 → 2026-08-15.
> Ne contient aucun contenu doctrinal — uniquement de l'ingénierie, des
> verdicts tranchés, et des chantiers ouverts.
>
> **Comment reprendre le travail** : lire ce document en entier, puis
> consulter les fichiers référencés. Aucun contexte antérieur n'est requis
> au-delà de ce qui est consigné ici.

---

## I. Ce qui est tranché et committé (résolu)

### 1. Pôle R&D — ouverture et structure (2026-08-08)

- `atelier/rd/` ouvert comme sous-pôle de `atelier/`, pas un sixième circuit
- Arbo : `instrument/`, `infrastructure/`, `audio/`, `outillage/`, `cahiers/`
- Migration : 16 fiches `atelier/projets/` → `rd/instrument/` (15) + `rd/outillage/` (1)
- Registre des problèmes ouvert (append-only) : `cahiers/registre-problemes.md`
- Sceau atelier étendu : types `experience | infrastructure | outillage`

### 2. Outillage déterministe du dépôt (2026-08-09 → 2026-08-11)

| Script | Emplacement | Rôle | Statut |
|---|---|---|---|
| `verifier-invariants.py` | racine wiki | Contrôles A0-A5 (append-only), B0-B1 (frontmatter), C3 (étanchéité) | Actif, 5 erreurs bloquantes + 43 avertissements (41 C4) |
| `generer-cartographie.py` | `Graphe/` | Two-level severity (BLOQUANT vs AVERTISSEMENT) | Actif, v1.1 |
| `detecter-non-tracke.py` | `atelier/rd/outillage/` | Fichiers non suivis git, classés par circuit | Actif |
| `carte-du-depot.py` | `meta/` | Détection orphelines + résolution étendue (nom fichier final) | Actif, 80 orphelines réelles (14 par conception) |

### 3. Outillage Karūbī — append-only + admin Agent 10 (2026-08-15)

**Scripts créés :**
- `meta/transmissions/ajouter-memoire-karubi.py` : insert §8/§9 sans LLM, refuse si zone scellée présente après le point d'insertion
- `meta/transmissions/integrer-navette-karubi.py` : intégration mécanique d'une navette revenue dans `_inbox/` — vérifie sceau, compare zones scellées, extrait ajouts §8/§9, archive, journalise
- `meta/transmissions/generer-karubi.py` : 3 commandes ajoutées (`statut`, `diff`, `index`)

**Amendements G0 validés par Sidy :**
- A : articulation Agent 10 (Gardien) dans §7
- B : zone scellée §7 re-scellée (nouveau hash `32534654...`, ancien `f7f286fb...`)
- C : registre Silsila (vocabulaire `session` + entrée `rescellement`)

**Commits associés :** `8d46d6a`, `19d1f43`, `a03fbe7`

### 4. Spec rôle G0 — brouillon §4 (actualisation Karūbī)

- Fichier : `meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md`
- **Statut : brouillon kari-kumi**, en attente verdict Sidy
- Résout : Sidy n'a plus à rédiger §4 (État des travaux) de mémoire à chaque retour de navette
- Collecte depuis les hubs (index/annales) des circuits pertinents, rédaction au même niveau d'abstraction que l'existant
- Sortie en `meta/transmissions/brouillons-section4/<dest>-<date>.md`, jamais dans le canonique
- **Séparation stricte** d'avec le sub-agent Karūbī côté destinataire (`spec-skill-karubi-hermes.md`) — ces deux rôles ne partagent ni contexte, ni session, ni sub-agent

### 5. Note outillage navette dans `meta/CLAUDE.md` (2026-08-15)

- Ajout de 23 lignes sous le Sceau Transmissions (§7)
- Documente le cycle navette-retour automatisé pour destinataires ayant rejoint le serveur
- Précise le rôle G0 de brouillon §4 (collecte, pas écriture finale)
- Rappel : §9→§10 reste une réponse directe de Sidy, mot pour mot, hors périmètre de tout automatisme

### 6. Bureau TUI — première version (2026-08-15)

- **10 tests passent** (pytest, 0.21s)
- Architecture Textual : `bureau/app.py` — grille de tuiles, mode monocle (`Entrée`/`Échap`)
- **6 modules** sous `bureau/modules/` : `video_player`, `audio_player`, `reader`, `chat`, `instrument_status`, `hermes_status`
- **3 services** sous `bureau/services/` : `ansi_render` (demi-blocs), `chat_server` (asyncio websockets), `audio_stream` (HTTP streaming)
- **Chat/audio** bindés sur `127.0.0.1` (accès via SSH/Tailscale uniquement)
- **Dépendances** ajoutées : `Pillow`, `websockets`, `textual`, `pypdf`
- Conformité protocole : lecture seule, aucun secret dans git
- Fiche : `atelier/rd/infrastructure/bureau-tui-architecture.md`

### 7. Infrastructure Hetzner (2026-08-11 → 2026-08-15)

- Cartographie complète : 2 vCPU, 3.7 GB RAM total, 2.2 Go utilisés + swap
- 12 profils Hermes (tous sur Qwen, custom:qwen)
- Verdict SSH statu quo (remote reste en SSH, pas de PAT)
- Omniroute (passerelle Discord↔Hermes) active

### 8. Phase 3 — veille infrastructure (2026-08-11, décisions entièrement tranchées)

- **Agent désigné** : Studio Sound Engineer (position 9, Sagittaire)
- **Canal** : `#infrastructure` (créé par Sidy sur Discord)
- **Fréquence** : quotidien, 12:00
- **Accès FS** : accordé (cloisonnement Hermes levé sur ce point)
- **Gouvernance** : strict par défaut, auto-accept optionnel ad hoc
- **Mécanisme de post** : l'agent compose → demande validation Discord → poste lui-même (pas de webhook tiers)
- **Rapport** : 5 sections (en-tête, verifier-invariants, cartographie, detecter-non-tracke, empreinte serveur, suggestions)
- **Nature** : rapport de suggestion/révision, toute suggestion doit être validée avant journalisation

### 9. Extension zodiacale des 12 agents (2026-08-11)

- 9 brouillons intégrés en `atelier/rd/cahiers/brouillons-extension-zodiacale/`
- Frontmatter `statut_experience: exploratoire`, étanchéité rappelée
- Agent 09 étendu (principe zodiacal + signe dans thème Sidy + gouvernance Discord)
- Positions 5, 8, 12 en attente de verdict

### 10. SRS protocole — verdict Sidy (2026-08-15)

- **Décidé** : intégration Hermes-native (pas de SRS tiers Mnemosyne/Anki)
- Cartes auto-générées depuis CLAUDE.md → mémoire Hermes
- Format de carte, script d'extraction, mécanisme de révision : NON encore définis
- Fiche : `atelier/rd/outillage/2026-08-15_piste-srs-assimilation-protocole.md`

---

## II. Ce qui est en cours (non commité)

### Fichiers modifiés non commités (2026-08-15)

| Fichier | Modification | Nature |
|---|---|---|
| `meta/CLAUDE.md` | +23 lignes | Note outillage navette Karūbī (§7 Sceau Transmissions) |
| `meta/transmissions/registre-silsila.md` | +26 lignes | Entrée `[2026-08-15] correction-outillage` (mise en service `integrer-navette-karubi.py`) |

### Fichiers non trackés

| Fichier | Nature | Statut |
|---|---|---|
| `meta/transmissions/integrer-navette-karubi.py` | Script déterministe intégration navette | Prêt à committer (testé à blanc, positif, garde-fou) |
| `meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md` | Spec rôle G0 brouillon §4 | **Brouillon kari-kumi**, verdict Sidy attendu |

→ Ces 4 fichiers attendent une passe d'intégration (Cmd 9) ou un verdict Sidy (spec G0).

---

## III. Chantiers ouverts — par priorité

### A. Bloquant technique — isolation mémoire Hermes par sub-agent

- **Problème** : le skill Karūbī-Hermes ne peut pas être déployé tant qu'on
  n'a pas un toggle `memory_enabled` par sub-agent (un sub-agent qui
  administrerait Karūbī ne doit pas avoir accès à la mémoire Hermes
  principale — étanchéité)
- **Statut** : aucune config Hermes trouvée permettant ce toggle
- **Piste** : investiguer la doc Hermes (`hermes-agent` skill) ou le code source
  pour un mécanisme d'isolation mémoire par session/sub-agent

### B. Verdict Sidy attendu — spec rôle G0 brouillon §4

- Fichier : `meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md`
- Statut : brouillon, kari-kumi
- Attend : verdict Sidy + définition du canal de déclenchement explicite

### C. SRS Hermes-native — implémentation (§VIII de la fiche piste)

Non encore fait :
- Format de carte (question/réponse ? frontmatter ?)
- Script d'extraction depuis CLAUDE.md (`generer-cartes-protocole.py`)
- Mécanisme de révision (cron, commande, injection prompt ?)
- Algorithme d'espacement (SM-2 simplifié ou aléatoire ?)

### D. Phase 3 — exécution de la veille (tout tranché, rien écrit)

- Extension du prompt `hermes-prompts/09-studio-sound-engineer.md`
- Script de veille automatisé (appelant les 3 scripts déterministes + empreinte serveur)
- Inscription au crontab (quotidien 12:00)
- Allowlist Discord pour `#infrastructure`

### E. verifier-invariants.py — angle mort C3 sur annales/index

- Les `annales.md`/`index.md` sont totalement exemptés du contrôle C3 (étanchéité)
- Piste : distinguer exemption totale (cibles neutres) vs avertissement (cible `meta/`)
- En attente d'arbitrage Sidy

### F. `graphe-cartographie.json` jamais régénéré

- 2 anomalies frontmatter bloquantes restantes (sources doctrinales sans frontmatter)
- Hors périmètre R&D/outillage (contenu doctrinal)

---

## IV. Leçons transversales (mémoire opérationnelle)

1. **Ne jamais faire confiance à un self-report chiffré d'un agent** — toujours
   vérifier par `verifier-invariants.py` + `carte-du-depot.py` (leçon [2026-08-09])
2. **Ne jamais `git add -A` à la racine** — `_inbox/` serait commité (leçon [2026-08-09])
3. **Lancer `verifier-invariants.py` dans la même session que tout commit de restructuration** — un reliquat invisible a survécu 24h faute de ce réflexe
4. **La direction d'un lien inter-circuit doit être vérifiée AVANT l'édition**, pas après relecture du diff
5. **Le sceau Karūbī protège les zones scellées, jamais la complétude des zones de croissance** — diff navette/canonique nécessaire
6. **Tout agent (quel que soit son moteur) est soumis au protocole** — §I, Cmd 14 (agnosticisme du moteur)
7. **Le double-commit est le mode normal du Cmd 9** (SHA après l'entrée qui le décrit)
8. **Les zones scellées Karūbī ne se modifient jamais hors amendement G0** — si la navette a une zone scellée différente, c'est un incident

---

## V. Pour reprendre le travail

### Si tu es un agent qui reprend le fil :

1. **Lire ce document en entier** (tu es ici)
2. **Lire `cahiers/registre-problemes.md`** en entier (1577 lignes, append-only, le fil complet des problèmes et résolutions)
3. **Lire `atelier/rd/index.md`** pour la charte du pôle
4. **Consulter `CLAUDE.md` racine + `atelier/CLAUDE.md`** pour le protocole
5. **Consulter `meta/CLAUDE.md`** pour les règles propres au Domaine Réservé

### Chantiers prioritaires (impact immédiat) :

- **A (isolation mémoire)** : bloquant pour le déploiement du skill Karūbī-Hermes — investiguer la doc Hermes ou le code source
- **C (SRS Hermes-native)** : définir le format de carte et le script d'extraction — fiche piste disponible
- **D (Phase 3 exécution)** : écrire le script de veille et l'inscrire au crontab — tout est tranché côté décision

### Fichiers en attente (non commités) :

- Les 4 fichiers listés en section II attendent soit une passe d'intégration standard (Cmd 9), soit un verdict Sidy (spec G0)
- **Ne pas committer la spec G0 sans verdict Sidy** — elle est marquée brouillon

### Vérification mécanique (toujours) :

```bash
cd /root/wiki
python3 verifier-invariants.py --racine /root/wiki
# Attendu : 5 erreurs bloquantes + 43 avertissements (état connu au 2026-08-15)

cd atelier/rd/infrastructure/bureau
source .venv/bin/activate
python -m pytest
# Attendu : 10 passed
```

---

## VI. Contacts et responsabilités

- **Sidy** : verdicts doctrinaux, validation humaine (Cmd 12/13), écriture §4/§10 Karūbī
- **Hermes Agent (profil default)** : agent de fonction, sessions terminal, outillage déterministe
- **Claude Code** : sessions d'intégration, restructuration de fichiers, travail de masse
- **Sub-agent Karūbī (destinataire)** : isolé du wiki, mémoire native désactivée, périmètre limité au fichier `karubi-<nom>.md` chargé
- **Rôle G0 (ce fichier spec)** : s'exécute côté G0 uniquement, jamais en session avec un destinataire

---

*Document généré le 2026-08-15. Tout changement postérieur doit être consigné dans une entrée dédiée du registre des problèmes (`cahiers/registre-problemes.md`), pas dans ce bilan.*
