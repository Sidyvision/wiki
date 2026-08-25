---
title: "Incident de contamination par caractères Unicode invisibles (U+200D)"
type: outillage
statut_experience: reproduit
created: 2026-08-22
updated: 2026-08-25
status: resolu
severity: moyen
affected_systems: [wiki, documentation]
---

# Incident de contamination par caractères Unicode invisibles (U+200D)

## Résumé

**Date de découverte** : 2026-08-22  
**Nature** : Contamination par caractères Unicode Zero Width Joiner (U+200D)  
**Étendue** : 31 fichiers markdown, 156 occurrences  
**Impact** : Aucun impact fonctionnel direct, mais risque de sécurité latent  
**Statut** : Résolu — nettoyage complet effectué  

## Description de l'incident

Lors de l'analyse du document `raw/2608.09867.pdf` (étude de sécurité sur l'extraction de traces de raisonnement LLM), le système de sécurité d'Hermes a détecté la présence de caractères Unicode invisibles dans un fichier `CLAUDE.md`. Investigation immédiate menée pour déterminer l'étendue de la contamination.

### Caractéristiques techniques

- **Caractère concerné** : U+200D (Zero Width Joiner / ZWJ)
- **Propriétés** : Invisible, non-imprimable, longueur nulle à l'affichage
- **Usage légitime** : Composition de ligatures emoji (ex: emoji famille = 👨[ZWJ]👩[ZWJ]👧[ZWJ]👦)
- **Usage détecté** : Insertion systématique entre le "H" et le reste du mot "Hermes" → `H[ZWJ]ermes`

## Investigation

### Méthodologie

1. Détection initiale : alerte système sur caractère invisible
2. Recherche exhaustive dans tout le dépôt
3. Analyse de répartition par circuit
4. Vérification d'hypothèses (watermark légale, marqueur sémantique)
5. Nettoyage complet
6. Vérification post-nettoyage

### Étendue de la contamination

```
Circuit        Fichiers touchés    Occurrences ZWJ
─────────────────────────────────────────────────
meta/          17                  44
atelier/       11                  106
doctrinal/     3                   3
_inbox/        1                   1
─────────────────────────────────────────────────
TOTAL          31 fichiers         156 occurrences
```

### Pattern identifié

- **Position constante** : toujours entre "H" et "ermes"
- **Contexte** : 100% des occurrences dans le mot "Hermes" (l'outil technique)
- **Distribution** : tous les circuits touchés, concentration maximale dans `atelier/`

### Hypothèses testées et écartées

1. ❌ **Watermark de traçabilité légale** (EU AI Act) : U+200D n'est pas un mécanisme de signature cryptographique
2. ❌ **Marqueur sémantique** (distinguer Hermes Agent vs figure mythologique) : répartition incohérente avec cette hypothèse
3. ✅ **Artefact de formatage** : contamination par copier-coller depuis source externe ou éditeur configuré pour insertion automatique de ZWJ

## Analyse de sécurité

### Risques identifiés

#### 1. Risque de dissimulation de code malveillant

Les caractères invisibles peuvent être utilisés pour :
- Masquer des URLs malveillantes (ex: `https://evil[ZWJ].com` affiché comme `https://evil.com`)
- Cacher des commandes shell dans du texte apparent
- Obfusquer des identifiants ou tokens

**Exemple théorique** :
```bash
curl https://legitimate[ZWJ].evil.com/api  # Invisible dans l'éditeur
```

#### 2. Risque de contournement de filtres

Certains systèmes de détection (recherche de mots-clés, analyse de logs) peuvent être contournés par insertion de caractères invisibles :
- Mot-clé bloqué : `malware`
- Contournement : `mal[ZWJ]ware` (inchangé visuellement, mais échappe au filtre)

#### 3. Risque d'exfiltration de données

Si un système d'IA est entraîné ou config pour reconnaître des patterns avec ZWJ :
- Encodage de données dans la présence/absence de ZWJ
- Canal de communication covert entre sessions
- Signalisation d'état via motifs de ZWJ

#### 4. Risque de corruption de données

- Modification involontaire de noms de fichiers ou chemins
- Altération de commandes exécutables
- Corruption de données structurées (JSON, YAML)

### Facteurs aggravants

- **Ubiquité** : caractères invisibles dans 31 fichiers, dont des fichiers critiques (CLAUDE.md)
- **Persistence** : contamination présente depuis plusieurs mois (fichiers créés entre 2026-07 et 2026-08)
- **Propagation** : tous les circuits touchés, indiquant une source commune ou propagation croisée

### Facteurs atténuants

- **Aucune preuve d'exploitation malveillante** : pattern cohérent, pas de code exécutif caché
- **Pas d'impact fonctionnel** : les fichiers restent lisibles et interprétables
- **Détection précoce** : système de sécurité Hermes opérationnel
- **Origine probablement innocente** : artefact de formatage plutôt qu'attaque délibérée

## Actions correctives

### Actions immédiates (2026-08-22)

1. ✅ **Nettoyage complet** : suppression de tous les U+200D dans le dépôt
   ```bash
   find /root/wiki -type f -name "*.md" -exec sed -i 's/\xe2\x80\x8d//g' {} \;
   ```

2. ✅ **Vérification post-nettoyage** : confirmation 0 occurrence restante
   - Avant : 156 occurrences ZWJ
   - Après : 0 occurrence ZWJ
   - Total "Hermes" unifié : 456 occurrences

3. ✅ **Documentation** : rapport d'incident complet

### Actions recommandées (à planifier)

1. **Audit des outils d'édition** : identifier la source de contamination
   - Éditeur de texte utilisé pour rédaction manuelle
   - Outils de conversion (PDF → MD, DOCX → MD)
   - Systèmes de copier-coller (clipboard managers, navigateurs)

2. **Mise en place de détection automatique** :
   - Hook pre-commit git pour refuser caractères invisibles
   - Script de validation dans la CI/CD
   - Monitoring régulier du dépôt

3. **Formation et sensibilisation** :
   - Documenter le risque dans le protocole de sécurité
   - Informer les contributeurs (Sidy, agents Studio/Gardien)
   - Ajouter aux checklist de revue de code

4. **Renforcement du protocole de sécurité** :
   - Scanner tous les fichiers `raw/` avant intégration
   - Valider les fichiers externes avant import
   - Ajouter U+200D et autres caractères invisibles à la liste noire

## Recommandations pour le protocole de sécurité

### À intégrer dans CLAUDE.md racine

```markdown
### Commandement 16 : Hygiène Unicode (nouveau)

JAMAIS insérer de caractères Unicode invisibles dans le dépôt :
- U+200B (Zero Width Space)
- U+200C (Zero Width Non-Joiner)
- U+200D (Zero Width Joiner)
- U+FEFF (Byte Order Mark en milieu de fichier)
- U+00A0 (Non-Breaking Space) sauf usage explicite et documenté

Validation : tout fichier doit passer un scan Unicode avant commit.
En cas de détection : refus du fichier, investigation, rapport d'incident.
```

### À intégrer dans les procédures d'import

```markdown
### Procédure d'import de fichiers externes

1. Scanner le fichier source pour caractères invisibles
2. Nettoyer si contamination détectée
3. Documenter l'origine du fichier dans les métadonnées
4. Valider le contenu avant intégration au dépôt
```

## Leçons apprises

1. **Vigilance sur les caractères invisibles** : les éditeurs et outils modernes peuvent insérer des caractères non-imprimables sans avertissement

2. **Importance de l'audit régulier** : même sans exploitation malveillante, la contamination peut persister longtemps sans détection

3. **Sécurité en profondeur** : même les artefacts apparemment bénins doivent être traités comme des incidents de sécurité potentiels

4. **Documentation systématique** : tout incident, même résolu, doit être consigné pour référence future et amélioration des protocoles

## Annexes

### A. Liste des fichiers contaminés (avant nettoyage)

<details>
<summary>Cliquer pour déplier (31 fichiers)</summary>

- /root/wiki/meta/meta-annales.md
- /root/wiki/meta/CLAUDE.md
- /root/wiki/meta/carte-du-depot-meta.md
- /root/wiki/meta/projet-unifie/02-instrument-feuille-de-route.md
- /root/wiki/meta/projet-unifie/15-architecture-discord-hermes-2026-08-07.md
- /root/wiki/meta/projet-unifie/04-sessions-par-fonction-et-backlogs.md
- /root/wiki/meta/projet-unifie/01-contexte-demarche-etat.md
- /root/wiki/meta/projet-unifie/hermes-prompts/09-studio-sound-engineer.md
- /root/wiki/meta/projet-unifie/03-transition-modele-open-source.md
- /root/wiki/meta/projet-unifie/hermes-skills/spec-skill-karubi-actualisation-g0.md
- /root/wiki/meta/projet-unifie/17-compte-rendu-12-agents-calibration-zodiacale-2026-08-09.md
- /root/wiki/meta/carte-du-depot.md
- /root/wiki/meta/carte-du-depot-atelier.md
- /root/wiki/meta/carte-meta.md
- /root/wiki/meta/transmissions/registre-silsila.md
- /root/wiki/CLAUDE.md
- /root/wiki/atelier/CLAUDE.md
- /root/wiki/atelier/rd/outillage/spec-archiver-monitoring-quotidien.md
- /root/wiki/atelier/rd/outillage/2026-08-16_cordis-composabilite-spatiotemporelle.md
- /root/wiki/atelier/rd/cahiers/registre-problemes.md
- /root/wiki/atelier/rd/cahiers/proposition-phase3-agent-veille-infrastructure-2026-08-11.md
- /root/wiki/atelier/rd/index.md
- /root/wiki/atelier/rd/infrastructure/canal-telegram-mehdi-2026-08-16.md
- /root/wiki/atelier/rd/infrastructure/acces-scope-mehdi-habib-2026-08-12.md
- /root/wiki/atelier/rd/infrastructure/monitoring-archive-charte.md
- /root/wiki/atelier/rd/infrastructure/infrastructure-ssh-statu-quo.md
- /root/wiki/atelier/rd/infrastructure/bureau/README.md
- /root/wiki/atelier/annales.md
- /root/wiki/_inbox/rapport-conjoint-studio-gardien-etude-depot-20260820.md
- /root/wiki/doctrinal/discernement/2026-08-11_trois-territoires-inacheve-flux-speculatif-exploratoire.md
- /root/wiki/doctrinal/annales.md

</details>

### B. Commandes de nettoyage utilisées

```bash
# Nettoyage complet
find /root/wiki -type f -name "*.md" -exec sed -i 's/\xe2\x80\x8d//g' {} \;

# Vérification post-nettoyage
grep -r $'\u200D' /root/wiki --include="*.md" 2>/dev/null | wc -l
# Résultat attendu : 0
```

### C. Caractères Unicode à surveiller

```
U+200B  Zero Width Space          Invisible, souvent utilisé comme séparateur
U+200C  Zero Width Non-Joiner     Contrôle de ligature
U+200D  Zero Width Joiner         Composition de ligatures (emoji)
U+FEFF  Byte Order Mark           Indicateur d'encodage, problème en milieu de fichier
U+00A0  Non-Breaking Space        Espace insécable, peut causer des problèmes de parsing
U+200E  Left-to-Right Mark        Contrôle de direction de texte
U+200F  Right-to-Left Mark        Contrôle de direction de texte
```

## Conclusion

Incident résolu avec succès. Aucune preuve d'exploitation malveillante, mais le potentiel de risque justifie le renforcement des protocoles de sécurité. La contamination par caractères invisibles est un vecteur d'attaque connu dans la sécurité informatique ; sa détection et son traitement systématiques sont essentiels pour maintenir l'intégrité du dépôt.

**Prochaine étape** : validation par Sidy, puis intégration des recommandations dans le protocole de sécurité (CLAUDE.md racine) et communication aux agents Studio/Gardien pour mise à jour de leurs procédures.

---

**Rapport établi par** : Hermes Agent  
**Date** : 2026-08-22  
**Statut** : En attente de validation

---

## Post-scriptum — récidive du même jour (chantier bibliothèque)

**Découverte** : 2026-08-22, lors de l'ouverture de `atelier/rd/bibliotheque/`.
**Nature** : même famille que l'incident principal — points de code invisibles
émis à l'écriture, non détectés à la relecture visuelle.

Trois occurrences, toutes de ma main (session de supervision), toutes corrigées
dans la même passe :

| fichier | point de code | cause |
|---|---|---|
| `meta/projet-unifie/hermes-prompts/13-librarian-archivist.md` | U+200B, U+200C, U+200D, U+200E, U+200F, U+FEFF | ligne `grep` d'exemple écrite avec les caractères littéraux au lieu de leurs séquences d'échappement |
| `atelier/rd/bibliotheque/valider-index-livres.py` | idem | dictionnaire `INTERDITS` déclarant en clair ce qu'il interdit |
| `atelier/annales.md` | U+200D | graphie « Hermes » recopiée depuis un contexte contaminé |

**Enseignement — au-delà du nettoyage.** Les deux premiers cas partagent une
cause structurelle : *un outil qui contient littéralement ce qu'il proscrit se
déclenche sur lui-même*, et son autotest devient un faux positif permanent. La
correction retenue n'est pas un nettoyage mais un changement de forme — les
points de code sont désormais déclarés par `chr(0x200B)` etc., jamais écrits en
clair. Même principe appliqué en amont dans le schéma de fiche `index-livre` :
arabe et latin ne partagent jamais une cellule de table, ce qui **supprime la
cause** de l'émission de marques bidi par un moteur OCR au lieu de la nettoyer
après coup.

Le troisième cas rappelle que la contamination se propage par **copie depuis un
contexte déjà atteint**, y compris depuis un rendu d'interface : toute graphie
recopiée doit être vérifiée, pas seulement toute graphie saisie.

**Contrôle mécanique de clôture** : recontrôle des douze fichiers écrits ou
modifiés dans la passe — 0 point de code interdit.

## Post-scriptum 2 — défaillance de la commande de nettoyage suggérée par le hook (2026-08-25)

**Contexte** : nouvelle récidive de contamination ZWJ, même cause que le
post-scriptum précédent — trois fiches sources nouvelles
(`doctrinal/sources/guenon-*`) recopiant la graphie « Hermes » depuis un rendu
d'interface pollué du nom de la fiche
`doctrinal/discernement/2026-08-25_gizeh-degre-24-solaire-hermes-idris.md`.
Bloqué par le hook pre-commit (Cmd 15), comme prévu.

**Fait nouveau, distinct de la contamination elle-même** : la commande de
nettoyage que le hook affiche pour y remédier —
`sed -i 's/[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{200E}\x{200F}]//g' <fichier>` —
suppose une syntaxe d'échappement `\x{...}` que **GNU sed ne supporte pas**.
Exécutée telle quelle, elle n'échoue pas silencieusement : `sed` interprète la
chaîne comme une **classe de caractères littéraux** — `\`, `x`, `{`, `2`, `0`,
`B`, `}`, `C`, `D`, `F`, `E` — et supprime **toute occurrence de ces caractères
ASCII dans l'intégralité du fichier**. Effet observé sur les trois fiches :
`2026-08-25` → `6-8-5`, `degre-24` → `degre-4`, `Chapitre` → `hapitre`,
`Fiabilité` → `iabilité`, `exemplaire` → `eemplaire`, `Deux` → `eu`, etc. —
corruption massive et silencieuse (aucun message d'erreur), touchant dates,
slugs de wikilinks et prose.

**Détection et rattrapage** : la corruption a été repérée avant tout commit en
comparant l'état du fichier après `sed` à l'état déjà indexé par
`git add` (`git diff` entre index et working tree), puis annulée par
`git checkout -- <fichier>` (retour à l'état pré-corruption, encore propre de
ZWJ car issu de l'écriture originale). Le nettoyage effectif du seul caractère
visé a ensuite été fait avec
`perl -CSD -i -pe 's/\x{200D}//g' <fichier>` (échappement Perl valide,
correspond au comportement réellement voulu). Aucune corruption n'a atteint un
commit ni le dépôt distant.

**Enseignement** : un outil de remédiation (ici, le texte affiché par un hook
de sécurité) est lui-même une surface de risque et doit être vérifié avant
exécution, pas seulement le contenu qu'il corrige — la défaillance était dans
la commande *suggérée*, pas dans le hook de détection lui-même (qui a
correctement bloqué le commit). Recommandation : corriger le texte affiché par
le hook pre-commit pour proposer une commande fonctionnelle sur GNU sed —
`perl -CSD -i -pe 's/[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{200E}\x{200F}]//g'`
(remplace uniquement `sed` par `perl` dans la commande individuelle et dans la
commande de nettoyage complet du dépôt) — pour éviter qu'un futur agent ou
Sidy ne l'exécute telle quelle sans vérification et ne reproduise la
corruption sans le filet de sécurité `git diff`/`git checkout` qui a permis le
rattrapage cette fois-ci.

**Fichiers concernés par ce post-scriptum** : aucune trace de corruption dans
le dépôt (annulée avant commit) ; localisation exacte du hook pre-commit non
identifiée dans cette passe (probablement un hook git local, hors dépôt
versionné — à vérifier si une correction du texte affiché est engagée).
