#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier-invariants.py — Contrôle mécanique des invariants structurels du dépôt.

Principe (Cmd : "le script est le seul verdict autorisé, jamais l'auto-rapport du
modèle") : ce script est DÉTERMINISTE, sans LLM, sans réseau. Il ne corrige rien.
Il constate et il sort en code non nul si un invariant est rompu.

Usage :
    python3 verifier-invariants.py [--racine /root/wiki] [--json] [--strict] [--tout]

Périmètre : le script ne contrôle que ce qui appartient au dépôt — il consulte
`.gitignore` via git (venv tiers, sorties régénérables et sas `raw/` exclus).
`--tout` lève cette restriction. Le périmètre appliqué est toujours annoncé en
tête de sortie, jamais silencieux.

Codes de sortie :
    0  aucune anomalie bloquante
    1  au moins une anomalie bloquante (ERREUR)
    2  erreur d'exécution du script lui-même

Les AVERTISSEMENTS ne font pas échouer le script sauf avec --strict.
"""

import argparse
import json
import os
import re
import subprocess
import unicodedata
import sys
from datetime import date

# --------------------------------------------------------------------------
# Configuration des invariants
# --------------------------------------------------------------------------

# Fichiers d'annales connus (chronologique inverse strict, append-only).
# `meta-annales.md` : journal propre au Domaine Réservé meta/ (ouvert 2026-08-09,
# nom préfixé pour ne jamais se confondre avec les annales.md des circuits).
NOMS_ANNALES = {"annales.md", "meta-annales.md"}

# Circuits et leurs racines relatives.
# `hermeneutique` y est ajouté le 2026-09-09. Son ABSENCE était un trou hérité et
# muet : `circuit_de()` y renvoyait `None`, de sorte que B1 (clés de Sceau
# requises) et C3 (étanchéité) ne contrôlaient AUCUNE de ses 28 fiches depuis
# l'ouverture du circuit. Le contrôle ne se plaignait pas — il ne regardait rien
# (§VII, Épreuve des contrôles ; forme de PRO-01). Mesuré avant de combler :
# les 28 fiches passent B1 sans une seule erreur, la fermeture est donc sans
# effet rétroactif.
CIRCUITS = ["doctrinal", "atelier", "label", "meta", "hermeneutique"]

# Fichiers légitimement sans frontmatter YAML (protocole, README, prompts Hermes…).
# Ne pas leur appliquer B0.
FICHIERS_SANS_FM = {
    "CLAUDE.md", "README.md",
    "migration-2026-06-11.md",
    "echange-eleonore-g.md",
    "2026-06-18-entretien-integral.md",
    "10-briefing-infrastructure-hermes-agent-2026-07-03.md",
    "transcription-index-tilak-origine-polaire.md",
    "transcription-table-matieres-symboles-science-sacree.md",
}
PREFIXES_SANS_FM = (
    "meta/projet-unifie/hermes-prompts/",
    # `textes/` — sources converties, versionnées le 2026-09-02 (chantier PRO-08,
    # verdict de Sidy). Ce sont des TEXTES, pas des fiches : ils ne portent aucun
    # Sceau, n'entrent dans aucun régime de liens, et ne sont la cible d'aucun
    # wikilink. Sans cette ligne, la migration lèverait 560 erreurs B0 — soit
    # exactement le bruit qui avait masqué la seule erreur vraie du 2026-09-01
    # (chantier OUT-C2). L'exemption est CIBLÉE : un `.md` nu hors de `textes/`
    # continue de lever B0, et c'est la seconde face de l'épreuve.
    "textes/",
    # `protocoles/` — procédure des règles transversales, sortie de `CLAUDE.md`
    # le 2026-09-09 (Phase 2, verdict de Sidy). Même statut que `textes/` : ce
    # ne sont pas des fiches mais le PROLONGEMENT du protocole racine — aucun
    # Sceau, aucun régime de liens, cible d'aucun wikilink (Cmd 14). Le contrôle
    # qui leur est propre n'est pas B0 mais la paire P1/P2 ci-dessous : la
    # question n'est pas « ce fichier est-il une fiche conforme ? » mais « ce
    # protocole est-il appelé, et ce qu'on appelle existe-t-il ? ».
    "protocoles/",
)

# Fichiers dont les liens sortants ne sont PAS soumis au contrôle C3 d'étanchéité
# (les annales peuvent citer d'autres circuits pour situer les passes).
# `meta-index.md` : hub propre au Domaine Réservé meta/ (ouvert 2026-08-09).
FICHIERS_EXEMPTS_C3 = NOMS_ANNALES | {"index.md", "meta-index.md"}

# Fichiers dont les liens sortants ne sont PAS soumis au contrôle C1 (liens non résolus)
# Rapports de traitement qui documentent volontairement des exemples de liens problématiques
FICHIERS_EXEMPTS_C1 = {
    "traitement-avertissements-isoles-rapport-2026-08-18.md",
    "2026-08-23_memoire-persistante-deploiement.md",
}

# Patterns de liens considérés comme placeholders/exemples — ignorés en C1.
RE_LIEN_PLACEHOLDER = re.compile(
    r"^(\.\.\.|…|slug(-source)?|chemin(/relatif)?|autre-slug"
    r"|atelier/\.\.\.|doctrinal/\.\.\.|doctrinal/vigilance/\.\.\."
    r"|doctrinal/discernement/slug|doctrinal/deviations/slug"
    r"|doctrinal/symboles-ou-autorites/slug|doctrinal/sources/inexistante"
    r"|doctrinal/sources/\.\.\.|doctrinal/etudes/YYYY-MM-DD_synthese-si-existante"
    r"|symbole/autorite-x|deviation-y|symbole-ou-autorite|deviation"
    r"|[A-Z]{4}-MM-DD_.*|atelier/…|doctrinal/symboles/slug)$"
)

# Clés de frontmatter attendues par circuit (Sceau Recteur pour doctrinal).
CLES_REQUISES = {
    "doctrinal": ["title", "type", "status", "tradition_cadre", "created", "updated", "sources"],
    "atelier":   ["title", "type", "created", "updated"],
    "label":     ["title", "type", "created", "updated"],
    "meta":      ["title", "type"],
    # Clés du Sceau herméneutique (hermeneutique/CLAUDE.md). `registre` y est
    # requis : c'est lui qui distingue `analyse` de `expression`, et donc le
    # régime de production de la fiche.
    "hermeneutique": ["title", "type", "registre", "created", "updated", "sources"],
}

# Étanchéité des circuits : circuit source -> circuits interdits en cible.
# Règle du dépôt : doctrinal ne pointe JAMAIS vers atelier ni meta.
ETANCHEITE_INTERDITE = {
    "doctrinal": {"atelier", "meta", "label", "hermeneutique"},
    # `hermeneutique/CLAUDE.md` : « doctrinal/ → hermeneutique/ : JAMAIS. »
    # L'inverse est permis en sens unique (cles_doctrinales, discernement).
    "hermeneutique": {"meta"},
}

# Le champ `sources:` du frontmatter doctrinal ne doit jamais viser meta/.
SOURCES_CIBLES_INTERDITES = {"meta"}

RE_ENTETE_ANNALES = re.compile(r"^##\s+\[(\d{4}-\d{2}-\d{2})\]\s*(.*)$")
RE_CHAMP_COMMIT = re.compile(r"^-\s*\*\*Commit\*\*\s*:")
# Sous-item explicite d'une entrée groupée légitime, ex. "**(a) Titre —**".
RE_SOUS_ITEM = re.compile(r"^\*\*\([a-zA-Z0-9]+\)")
RE_CLOTURE = re.compile(r"^\s*(```|~~~)")
RE_SPAN_CODE = re.compile(r"`[^`\n]+`")
RE_WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]*)?\]\]")
RE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Renvoi vers une fiche de `protocoles/`, tel que la discipline du renvoi
# l'impose (Cmd 14) : nominatif, entre accents graves.
RE_RENVOI_PROTOCOLE = re.compile(r"`protocoles/([A-Za-z0-9._-]+\.md)`")
# Une formule CITÉE entre guillemets français (« … ») n'est pas un renvoi :
# c'est le protocole qui se décrit lui-même. Cmd 14 cite ainsi son propre
# gabarit, « avant tout X, lire `protocoles/Y.md` », qui ne vise aucune fiche.
RE_CITATION = re.compile(r"«[^»]*»")


# --------------------------------------------------------------------------
# Utilitaires
# --------------------------------------------------------------------------

class Rapport:
    def __init__(self):
        self.erreurs = []
        self.avertissements = []

    def erreur(self, fichier, code, message, ligne=None):
        self.erreurs.append({"fichier": fichier, "code": code,
                             "ligne": ligne, "message": message})

    def avertir(self, fichier, code, message, ligne=None):
        self.avertissements.append({"fichier": fichier, "code": code,
                                    "ligne": ligne, "message": message})

    def imprimer(self):
        if self.erreurs:
            print("ERREURS (bloquantes) :")
            for e in self.erreurs:
                loc = f":{e['ligne']}" if e["ligne"] else ""
                print(f"  [{e['code']}] {e['fichier']}{loc} — {e['message']}")
        if self.avertissements:
            print("\nAVERTISSEMENTS :")
            for a in self.avertissements:
                loc = f":{a['ligne']}" if a["ligne"] else ""
                print(f"  [{a['code']}] {a['fichier']}{loc} — {a['message']}")
        print(f"\n{len(self.erreurs)} erreur(s), "
              f"{len(self.avertissements)} avertissement(s).")


def lire(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


def separer_frontmatter(texte):
    """Retourne (dict_frontmatter, texte_corps, n_lignes_frontmatter).

    Parseur minimal volontairement : pas de dépendance PyYAML. Gère les
    scalaires, les listes en ligne [a, b] et les listes en blocs (- item).
    Renvoie (None, texte, 0) si aucun frontmatter délimité n'est présent.
    """
    lignes = texte.split("\n")
    if not lignes or lignes[0].strip() != "---":
        return None, texte, 0
    fin = None
    for i in range(1, len(lignes)):
        if lignes[i].strip() == "---":
            fin = i
            break
    if fin is None:
        return None, texte, 0

    fm = {}
    cle_courante = None
    for brute in lignes[1:fin]:
        if not brute.strip() or brute.lstrip().startswith("#"):
            continue
        if brute.lstrip().startswith("- ") and cle_courante:
            fm.setdefault(cle_courante, [])
            if isinstance(fm[cle_courante], list):
                fm[cle_courante].append(brute.lstrip()[2:].strip().strip("\"'"))
            continue
        if ":" not in brute:
            continue
        cle, _, valeur = brute.partition(":")
        cle = cle.strip()
        valeur = valeur.strip()
        cle_courante = cle
        if valeur == "":
            fm[cle] = []
        elif valeur.startswith("[") and valeur.endswith("]"):
            interieur = valeur[1:-1].strip()
            fm[cle] = ([x.strip().strip("\"'") for x in interieur.split(",") if x.strip()]
                       if interieur else [])
        else:
            fm[cle] = valeur.strip("\"'")
    return fm, "\n".join(lignes[fin + 1:]), fin + 1


def circuit_de(chemin_relatif):
    tete = chemin_relatif.split(os.sep)[0]
    return tete if tete in CIRCUITS else None


def parse_date(valeur):
    if not isinstance(valeur, str) or not RE_DATE.match(valeur.strip()):
        return None
    a, m, j = valeur.strip().split("-")
    try:
        return date(int(a), int(m), int(j))
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Contrôle A — invariants des annales
# --------------------------------------------------------------------------

def controler_annales(chemin_abs, chemin_rel, rap):
    texte = lire(chemin_abs)
    fm, corps, decalage = separer_frontmatter(texte)
    lignes = texte.split("\n")

    entetes = []
    for i, ligne in enumerate(lignes, start=1):
        m = RE_ENTETE_ANNALES.match(ligne)
        if m:
            d = parse_date(m.group(1))
            if d is None:
                rap.erreur(chemin_rel, "A0", f"date d'en-tête illisible : {ligne.strip()}", i)
            else:
                entetes.append((i, d, m.group(2).strip()))

    if not entetes:
        rap.avertir(chemin_rel, "A1", "aucune entrée `## [YYYY-MM-DD]` détectée")
        return

    # A2 — ordre chronologique inverse strict (dates non croissantes).
    for k in range(1, len(entetes)):
        ligne_prec, date_prec, _ = entetes[k - 1]
        ligne_cour, date_cour, titre_cour = entetes[k]
        if date_cour > date_prec:
            rap.erreur(
                chemin_rel, "A2",
                f"rupture d'ordre : {date_cour} apparaît après {date_prec} "
                f"(ligne {ligne_prec}). Convention : plus récent en haut.",
                ligne_cour)

    # A3 — frontmatter `updated` cohérent avec l'entrée la plus récente.
    date_max = max(d for _, d, _ in entetes)
    if fm and "updated" in fm:
        d_updated = parse_date(fm["updated"])
        if d_updated is None:
            rap.erreur(chemin_rel, "A3", f"`updated` illisible : {fm['updated']!r}")
        elif d_updated < date_max:
            rap.erreur(
                chemin_rel, "A3",
                f"`updated: {fm['updated']}` est antérieur à l'entrée la plus "
                f"récente ({date_max}).")
    else:
        rap.avertir(chemin_rel, "A3", "frontmatter sans champ `updated`")

    # A4 — doublons d'en-tête (même date + même titre).
    vus = {}
    for ligne_n, d, titre in entetes:
        cle = (d.isoformat(), titre)
        if cle in vus:
            rap.erreur(chemin_rel, "A4",
                       f"en-tête dupliqué (déjà ligne {vus[cle]}) : [{d}] {titre}",
                       ligne_n)
        else:
            vus[cle] = ligne_n

    # A5 — empreinte d'append mécanique : run de lignes vides anormal.
    # Le format du dépôt utilise UNE ligne vide avant un séparateur `---`.
    for i in range(2, len(lignes)):
        if lignes[i].strip() == "---" and lignes[i - 1].strip() == "" \
                and lignes[i - 2].strip() == "":
            rap.avertir(
                chemin_rel, "A5",
                "double ligne vide avant un séparateur — signature possible "
                "d'un ajout mécanique en fin de fichier plutôt qu'une insertion.",
                i + 1)

    # A6 — corps d'entrée orphelin : une même section (entre deux en-têtes
    # `## [YYYY-MM-DD]`) porte plusieurs champs `- **Commit** :`. Signature
    # d'une insertion qui a remplacé l'en-tête de l'entrée suivante au lieu
    # de la précéder (incident 2026-08-28, registre R&D). Avertissement, non
    # bloquant : une entrée groupée légitime peut citer plusieurs commits, à
    # condition que chacun soit rattaché à son propre sous-item explicite
    # (ex. "**(a) Titre —**" / "**(b) Titre —**") — auquel cas ce n'est pas
    # un en-tête perdu mais un lot documenté fiche par fiche (§VIII.3).
    # Amendement 2026-08-30 (verdict Sidy) : raffinement du contrôle plutôt
    # que suppression, motivé par l'entrée [2026-08-20] rd | Lecture
    # dynamique du manifeste + instruction branche Kabbale (deux livrables
    # (a)/(b), chacun son Commit).
    for k in range(len(entetes)):
        debut = entetes[k][0]
        fin = entetes[k + 1][0] if k + 1 < len(entetes) else len(lignes) + 1
        indices_commits = [
            i for i in range(debut, fin - 1)
            if RE_CHAMP_COMMIT.match(lignes[i])]
        nb_commits = len(indices_commits)
        if nb_commits <= 1:
            continue
        segment_debut = debut
        tous_rattaches = True
        for idx_commit in indices_commits:
            segment = lignes[segment_debut:idx_commit]
            if not any(RE_SOUS_ITEM.match(ligne) for ligne in segment):
                tous_rattaches = False
                break
            segment_debut = idx_commit + 1
        if tous_rattaches:
            continue
        rap.avertir(
            chemin_rel, "A6",
            f"corps d'entrée orphelin possible : {nb_commits} champs "
            f"`- **Commit** :` dans une seule section, sans sous-item "
            f"explicite (\"**(a) ...**\") rattachant chacun — en-tête perdu "
            f"lors d'une insertion ? (entrée [{entetes[k][1]}] "
            f"{entetes[k][2]})", debut)


# --------------------------------------------------------------------------
# Contrôle B — hygiène du frontmatter
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Écriture d'origine — définition CANONIQUE du dépôt
# --------------------------------------------------------------------------
# Cette fonction fait foi pour tout le dépôt. `generer-index-lexical.py`
# l'IMPORTE d'ici plutôt que d'en garder une copie : deux définitions
# divergentes de « écriture originale » dans deux scripts, c'est la dérive que
# le partage de `fichiers_suivis()` avait déjà été écrit pour empêcher. Le sens
# de la dépendance est délibéré — l'outil de R&D dépend du contrôleur racine,
# jamais l'inverse : le contrôleur doit tourner même si le pôle `rd/` est
# absent.
#
# Les LETTRES MODIFICATIVES (catégorie Lm) sont exclues : `ʿ` (ʿayn, U+02BF) et
# `ʾ` (hamza, U+02BE) ne portent pas le nom Unicode LATIN, or ils appartiennent
# au dispositif de TRANSLITTÉRATION latine, pas à l'écriture d'origine.
def est_ecriture_originale(token):
    """Le token contient-il une lettre d'une écriture non latine ?"""
    for c in token:
        if unicodedata.category(c) not in ("Lo", "Ll", "Lu", "Lt"):
            continue
        try:
            if "LATIN" not in unicodedata.name(c):
                return True
        except ValueError:
            continue
    return False


# Marqueur d'absence de la forme originale (CLAUDE.md §VII, discipline des
# langues originales, point 4 ; domicile : champ `original:` du Sceau, §IV,
# verdict Sidy 2026-09-08).
MARQUEUR_ORIGINAL = "to-original"

# Graphies fautives du marqueur. Un marqueur mal orthographié est INVISIBLE :
# il paraît posé et n'est vu de personne — la forme muette exacte que §VII
# (Épreuve des contrôles) interdit de laisser passer.
# `to-original` lui-même n'en fait PAS partie — l'alternative `to-originals?`
# d'une première rédaction matchait la graphie VALIDE et la refusait. Attrapé
# par la faute fabriquée du 2026-09-08, jamais par la relecture : c'est très
# exactement ce que l'Épreuve des contrôles (§VII) existe pour trouver — un
# contrôle qui, ici, n'était pas muet mais bavard à tort.
VARIANTES_MARQUEUR = re.compile(
    r"^(?:to[_ ]original|tooriginal|to-originals|to-orginal|to-originel|"
    r"to-origine[l]?)$", re.IGNORECASE)

RE_H1_INVARIANTS = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def controler_original(chemin_rel, fm, corps, rap):
    """B5/B6/B7 — cohérence du champ `original:` et de son marqueur.

    Ce que le contrôle NE FAIT PAS, et ne peut pas faire : exiger le champ.
    Savoir si le sujet d'une fiche « appelle une écriture d'origine » demande
    la perception du sujet, non la lecture de sa forme — c'est un jugement, il
    revient à Sidy (Cmd 12). Le point 5 de la discipline l'interdit d'ailleurs
    explicitement : aucune passe de masse. Le contrôle se borne donc à ce qui
    est décidable sur le texte seul.
    """
    if fm is None:
        return
    valeur = fm.get("original")

    # B6 — graphie fautive du marqueur, où qu'elle se trouve dans le Sceau.
    for cle, v in fm.items():
        for item in (v if isinstance(v, list) else [v]):
            if isinstance(item, str) and VARIANTES_MARQUEUR.match(item.strip().strip('"\'')):
                rap.erreur(chemin_rel, "B6",
                           f"graphie fautive du marqueur dans `{cle}:` : "
                           f"{item.strip()!r} — la seule forme valide est "
                           f"`{MARQUEUR_ORIGINAL}`")

    if valeur is None:
        return

    # B7 — forme du champ : liste YAML de chaînes, comme `sources:` (§IV).
    if not isinstance(valeur, list):
        rap.erreur(chemin_rel, "B7",
                   f"`original:` doit être une liste YAML de chaînes, "
                   f"reçu {type(valeur).__name__} : {valeur!r}")
        return
    items = [str(x).strip().strip('"\'') for x in valeur]
    marque = [x for x in items if x.lower() == MARQUEUR_ORIGINAL]
    # Une graphie fautive est déjà refusée en B6 : ne pas la refuser deux fois
    # sous un second code, ce qui masquerait la vraie cause au lecteur.
    formes = [x for x in items
              if x.lower() != MARQUEUR_ORIGINAL
              and not VARIANTES_MARQUEUR.match(x)]
    if marque and formes:
        rap.erreur(chemin_rel, "B7",
                   f"`original:` mêle le marqueur d'absence et des formes : "
                   f"{valeur!r} — l'un ou l'autre, jamais les deux")
    for x in formes:
        if not est_ecriture_originale(x):
            rap.erreur(chemin_rel, "B7",
                       f"`original:` porte {x!r}, qui ne contient aucune lettre "
                       f"d'une écriture non latine — une translittération n'est "
                       f"pas une forme originale (§IV)")

    # B5 — contradiction : le marqueur déclare une absence que le texte dément.
    if marque:
        candidats = [str(fm.get("title", ""))] + RE_H1_INVARIANTS.findall(corps or "")
        for src in candidats:
            if est_ecriture_originale(src):
                rap.erreur(chemin_rel, "B5",
                           f"`original: [\"{MARQUEUR_ORIGINAL}\"]` déclare la forme "
                           f"d'origine absente, mais le titre ou le H1 la porte "
                           f"déjà : {src.strip()!r}")
                break


def controler_frontmatter(chemin_rel, fm, rap):
    circ = circuit_de(chemin_rel)
    nom = os.path.basename(chemin_rel)
    rel_unix = chemin_rel.replace(os.sep, "/")
    # Exemption B0 : fichiers légitimement sans frontmatter.
    sans_fm_legitime = (
        nom in FICHIERS_SANS_FM
        or any(rel_unix.startswith(p) for p in PREFIXES_SANS_FM)
    )
    if fm is None:
        if not sans_fm_legitime:
            rap.erreur(chemin_rel, "B0", "aucun frontmatter délimité par `---`")
        return
    # Les fichiers de service (annales, index) sont `type: meta` quel que soit
    # leur circuit : ils ne relèvent pas du Sceau Recteur doctrinal.
    fichier_de_service = (os.path.basename(chemin_rel) in NOMS_ANNALES
                          or os.path.basename(chemin_rel) in ("index.md", "meta-index.md")
                          or str(fm.get("type", "")).strip() == "meta")
    if circ and not fichier_de_service:
        for cle in CLES_REQUISES.get(circ, []):
            if cle not in fm:
                rap.erreur(chemin_rel, "B1", f"clé de frontmatter manquante : `{cle}`")

    # B2 — sources_count cohérent avec sources.
    if "sources_count" in fm and "sources" in fm:
        try:
            attendu = int(str(fm["sources_count"]).strip())
        except ValueError:
            rap.erreur(chemin_rel, "B2", f"`sources_count` non entier : {fm['sources_count']!r}")
        else:
            reel = len(fm["sources"]) if isinstance(fm["sources"], list) else 0
            # "to-source" est un marqueur d'absence, pas une source.
            reel_hors_marqueur = sum(
                1 for s in (fm["sources"] if isinstance(fm["sources"], list) else [])
                if s.strip().lower() != "to-source")
            if attendu not in (reel, reel_hors_marqueur):
                rap.erreur(
                    chemin_rel, "B2",
                    f"`sources_count: {attendu}` ≠ nombre réel de sources "
                    f"({reel}, dont {reel_hors_marqueur} hors marqueur `to-source`)")

    # B3 — cohérence created / updated.
    d_c, d_u = parse_date(fm.get("created", "")), parse_date(fm.get("updated", ""))
    if d_c and d_u and d_u < d_c:
        rap.erreur(chemin_rel, "B3", f"`updated` ({d_u}) antérieur à `created` ({d_c})")

    # B4 — étanchéité du champ `sources:` (doctrinal ne source jamais meta/).
    if circ == "doctrinal" and isinstance(fm.get("sources"), list):
        for s in fm["sources"]:
            for interdit in SOURCES_CIBLES_INTERDITES:
                if s.strip().strip("[]").startswith(interdit + "/"):
                    rap.erreur(chemin_rel, "B4",
                               f"`sources:` doctrinal pointe vers `{interdit}/` : {s}")


# --------------------------------------------------------------------------
# Périmètre du contrôle — ce qui appartient au dépôt, et rien d'autre
# --------------------------------------------------------------------------

# Dossiers exclus en toutes circonstances, même hors dépôt git.
DOSSIERS_EXCLUS = {".git", "node_modules", "_inbox"}


def perimetre_ignore(racine):
    """Ensemble des chemins relatifs que git tient pour hors dépôt.

    Motif (chantier OUT-01, ouvert le 2026-09-01) : ce script parcourait le
    disque sans jamais consulter `.gitignore`. Les venv de dépendances tierces
    (`.graphify-venv/`, `bureau/.venv/`), les sorties régénérables et le sas
    `raw/` produisaient 209 erreurs sur 210 — et ce bruit a réellement masqué
    la seule erreur vraie de la journée (`hermeneutique/annales.md`, contrôle
    A3), trouvée par tri manuel. Un validateur dont la sortie doit être triée
    à la main ne valide plus rien.

    Critère retenu : **git lui-même**. Ce qui est ignoré par `.gitignore` n'est
    pas dans le dépôt, donc n'a pas à en respecter les invariants. Le critère
    est déterministe, sans réseau ni LLM (§VIII), et il n'invente aucune règle
    nouvelle : il applique celle que le dépôt s'est déjà donnée.

    Retourne `(chemins, mode)` — `mode` vaut "git" si le périmètre vient de
    git, "repli" si git est indisponible (racine hors dépôt, ex. les bacs à
    sable de non-régression) : on se rabat alors sur les dossiers cachés, qui
    couvrent les venv et les caches sans rien décider d'autre.
    """
    try:
        sortie = subprocess.run(
            ["git", "ls-files", "--others", "--ignored", "--exclude-standard",
             "--directory", "-z"],
            cwd=racine, capture_output=True, check=True, timeout=60,
        ).stdout.decode("utf-8", "replace")
    except (OSError, subprocess.SubprocessError):
        return set(), "repli"
    return {c.rstrip("/") for c in sortie.split("\0") if c}, "git"


def hors_perimetre(rel, ignores, mode):
    """Vrai si `rel` (chemin relatif à la racine) est hors périmètre."""
    parts = rel.replace(os.sep, "/").split("/")
    if DOSSIERS_EXCLUS.intersection(parts):
        return True
    if mode == "repli":
        return any(p.startswith(".") for p in parts)
    chemin = "/".join(parts)
    return any(chemin == ig or chemin.startswith(ig + "/") for ig in ignores)


# --------------------------------------------------------------------------
# Contrôle C — intégrité et étanchéité des liens
# --------------------------------------------------------------------------

def collecter_cibles(racine, ignores, mode):
    """Index des cibles résolvables : chemins sans extension + slugs nus.

    Même périmètre que le parcours principal : un fichier hors dépôt ne peut
    pas servir de cible à un wikilink."""
    par_chemin, par_slug = set(), {}
    for base, dossiers, fichiers in os.walk(racine):
        dossiers[:] = [
            d for d in dossiers
            if not hors_perimetre(
                os.path.relpath(os.path.join(base, d), racine), ignores, mode)
        ]
        for nom in fichiers:
            if not nom.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(base, nom), racine)
            sans_ext = rel[:-3].replace(os.sep, "/")
            par_chemin.add(sans_ext)
            par_slug.setdefault(os.path.basename(sans_ext), []).append(sans_ext)
    return par_chemin, par_slug


def masquer_code(corps):
    """Neutralise blocs et spans de code : un wikilink entre backticks ou
    dans une clôture ``` est de la syntaxe citée en exemple (documentation
    d'un motif, code du validateur lui-même), jamais un lien vivant.
    Convention adoptée le 2026-08-28 — s'applique à C1/C3/C4."""
    lignes = corps.split("\n")
    dans_bloc = False
    hors_bloc = []
    for ligne in lignes:
        if RE_CLOTURE.match(ligne):
            dans_bloc = not dans_bloc
            hors_bloc.append(ligne)
            continue
        hors_bloc.append("" if dans_bloc else ligne)
    return RE_SPAN_CODE.sub(" ", "\n".join(hors_bloc))


def controler_liens(chemin_rel, corps, par_chemin, par_slug, rap):
    circ = circuit_de(chemin_rel)
    nom = os.path.basename(chemin_rel)
    # Les annales et index sont exempts du contrôle C3 bloquant (liens contextuels
    # légitimes vers les circuits neutres). Cette exemption reste TOTALE pour les
    # cibles neutres (doctrinal/atelier/label) — voir C4 ci-dessous pour la seule
    # cible qui ne doit structurellement jamais y apparaître : meta/.
    exempt_c3 = nom in FICHIERS_EXEMPTS_C3
    exempt_c1 = chemin_rel in FICHIERS_EXEMPTS_C1 or nom in FICHIERS_EXEMPTS_C1
    interdits = set() if exempt_c3 else ETANCHEITE_INTERDITE.get(circ, set())
    for brut in RE_WIKILINK.findall(masquer_code(corps)):
        cible = brut.strip().replace("\\", "/")
        if cible.endswith(".md"):
            cible = cible[:-3]
        # Ignorer les placeholders/exemples.
        if RE_LIEN_PLACEHOLDER.match(cible):
            continue
        # C1 — résolution.
        if cible not in par_chemin:
            candidats = par_slug.get(os.path.basename(cible), [])
            if not candidats:
                if not exempt_c1:
                    rap.avertir(chemin_rel, "C1", f"lien non résolu : [[{brut}]]")
                continue
            if len(candidats) > 1:
                rap.avertir(chemin_rel, "C2",
                            f"slug ambigu [[{brut}]] → {len(candidats)} cibles possibles")
            cible = candidats[0]
        # C3 — étanchéité des circuits (fichiers ordinaires, hors annales/index).
        tete = cible.split("/")[0]
        if tete in interdits:
            rap.erreur(chemin_rel, "C3",
                       f"étanchéité rompue : `{circ}` pointe vers `{tete}` — [[{brut}]]")
        # C4 — angle mort connu de l'exemption C3 (registre R&D, 2026-08-09,
        # "reporte") : un `annales.md`/`index.md` de circuit neutre qui pointe
        # vers `meta/` n'est jamais visible par C3. Avertissement non bloquant,
        # pour ne pas casser rétroactivement l'append-only des annales déjà
        # publiées (Cmd 9/Cmd 10) — signale sans jamais forcer de correction.
        elif exempt_c3 and tete == "meta" and circ is not None and circ != "meta":
            rap.avertir(chemin_rel, "C4",
                        f"lien `{circ}` (neutre, fichier de service) → `meta/` "
                        f"— sens interdit par §VI, hors périmètre bloquant de "
                        f"l'exemption C3 — [[{brut}]]")


# Champs du cartouche dont les valeurs peuvent porter des wikilinks.
#
# `liens_doctrinal` y est ajouté le 2026-09-08 en même temps que son ouverture au
# Sceau label : un champ de liens nouveau ne doit pas naître hors de la couverture
# C1/C2 (PRO-01, INF-14 — la porte sans garde). L'ajout est **sans effet
# rétroactif** : aucune fiche du dépôt ne portait ce champ avant ce jour.
#
# Restent volontairement hors couverture, et c'est un manque HÉRITÉ, signalé et
# non corrigé d'office (il demanderait son propre verdict) : `liens:` et
# `liens_atelier:` du Sceau label, dont une cible morte passe en silence.
CHAMPS_LIENS_CARTOUCHE = ("sources", "cross_links", "links", "liens_doctrinal")


def controler_liens_cartouche(chemin_rel, fm, par_chemin, par_slug, rap):
    """C1/C2 appliqués aux wikilinks déclarés dans le frontmatter.

    Extension du 2026-09-04 (verdict Sidy), motivée par une épreuve §VII : la
    même chaîne morte levait C1 dans le corps et passait en silence dans
    `cross_links:`. B2 ne comptait que la longueur de la liste, sans jamais
    vérifier qu'une cible existe — un cartouche vert attestait des listes bien
    formées, non des liens qui aboutissent.

    Portée volontairement étroite : **C1 et C2 seulement**. L'étanchéité des
    champs de cartouche relève de B4 (`sources:` doctrinal → meta/) ; C3/C4 ne
    sont PAS reportés ici, ce serait un changement de règle, non une extension
    de couverture — il demanderait son propre verdict.

    Ne sont pas des wikilinks et sont ignorés sans bruit : le marqueur
    `to-source`, et les chemins nus vers `raw/` (circuit hors régime de liens,
    binaires non résolvables par construction — reprise du 2026-09-04).
    """
    nom = os.path.basename(chemin_rel)
    if fm is None:
        return
    if chemin_rel in FICHIERS_EXEMPTS_C1 or nom in FICHIERS_EXEMPTS_C1:
        return
    for champ in CHAMPS_LIENS_CARTOUCHE:
        valeur = fm.get(champ)
        if valeur is None:
            continue
        entrees = valeur if isinstance(valeur, list) else [valeur]
        for entree in entrees:
            if not isinstance(entree, str):
                continue
            for brut in RE_WIKILINK.findall(entree):
                cible = brut.strip().replace("\\", "/")
                if cible.endswith(".md"):
                    cible = cible[:-3]
                if RE_LIEN_PLACEHOLDER.match(cible):
                    continue
                if cible in par_chemin:
                    continue
                candidats = par_slug.get(os.path.basename(cible), [])
                if not candidats:
                    rap.avertir(chemin_rel, "C1",
                                f"lien non résolu au cartouche (`{champ}:`) : [[{brut}]]")
                elif len(candidats) > 1:
                    rap.avertir(chemin_rel, "C2",
                                f"slug ambigu au cartouche (`{champ}:`) [[{brut}]] "
                                f"→ {len(candidats)} cibles possibles")


# --------------------------------------------------------------------------
# Contrôle C5/C6/C7 — étanchéité INVERSÉE (ajouté le 2026-09-10)
# --------------------------------------------------------------------------

# Règle encodée, `doctrinal/CLAUDE.md`, § « Règles de liens propres au circuit » :
#
#     « Étanchéité inversée : une page orthodoxe ne pointe jamais vers un
#       `discernement` non tranché (exception : lien défensif/généalogique
#       signalé). »
#
# Elle ne se tenait qu'à la main jusqu'à ce jour — l'annales doctrinal du
# 2026-09-10 (commit 09b9ee5) le constate après une violation commise par la
# machine elle-même. Ce contrôle est la garde mécanique correspondante.
#
# PORTÉE. Trois points ont été soumis à Sidy le jour de l'ajout — le périmètre
# côté source, la définition de « non tranché », et le niveau d'émission — et
# **tranchés par lui le 2026-09-10** : « Les trois choix de portée que tu m'as
# soumis sont la lecture correcte. pour 3. pas de passage en erreur. » Le « 3. »
# y vise le NIVEAU D'ÉMISSION, traité au paragraphe qui suit la liste ci-dessous.
# Ce ne sont donc plus des choix de la machine en attente d'arbitrage, mais la
# lettre reçue de la règle. Ce que le contrôle tient pour établi :
#
# 1. « Page orthodoxe » = `status: traditionnel`, et rien d'autre. Le
#    vocabulaire clos du Sceau fait de `contre-traditionnel` et de `profane`
#    l'inverse d'une page orthodoxe ; `academique` est le cas limite, laissé
#    hors périmètre — lecture confirmée par le verdict du 2026-09-10.
# 2. « Non tranché » = `status: speculatif` au cartouche de la fiche cible,
#    ce que le Sceau définit lui-même comme « statut transitoire — doit évoluer
#    vers un statut définitif à la clôture du discernement ». Le champ
#    `**Statut** : en cours` du bloc 🔍 dit la même chose dans le corps, mais
#    trois fiches `type: discernement` ne portent aucun bloc 🔍 : le cartouche
#    est le seul signal présent partout.
# 3. « Signalé » = le marqueur 🔍 sur la ligne du lien, seule marque que le
#    protocole nomme (clause `label/` → `doctrinal/` : « marqué suggéré (🔍)
#    tant qu'un discernement afférent n'est pas tranché »). Aucune formule
#    littérale n'est exigée : le protocole n'en impose pas.
#
# NIVEAU D'ÉMISSION : avertissement, jamais erreur. Au jour de l'ajout, le
# dépôt porte 71 renvois hérités qui tombent sous la règle (26 au cartouche,
# 45 au corps), tous antérieurs à ce contrôle. Les porter en erreur
# casserait rétroactivement un dépôt vert et forcerait 71 corrections que la
# machine n'a pas qualité pour décider (Cmd 12). Même raison, même forme que
# l'avertissement C4. **Le passage en erreur est écarté par le verdict du
# 2026-09-10** — il n'est pas différé jusqu'au traitement de l'assiette, il
# n'aura pas lieu : C5, C6 et C7 avertissent, et rien de plus. Un contributeur
# qui voudrait les rendre bloquants irait contre un verdict rendu (Cmd 10).

STATUTS_SCEAU = {"traditionnel", "academique", "profane",
                 "contre-traditionnel", "speculatif"}
# Portée du contrôle côté source — cf. choix 1 ci-dessus.
STATUTS_ORTHODOXES = {"traditionnel"}
MARQUEUR_SUGGERE = "\U0001F50D"          # 🔍
DOSSIER_DISCERNEMENT = "doctrinal/discernement"


def indexer_discernements(racine, ignores, mode, rap):
    """Ensemble des fiches de discernement NON TRANCHÉES (`status: speculatif`).

    Passe étroite : seul `doctrinal/discernement/` est lu, la nomenclature du
    circuit y fixant ces fiches sans exception. `collecter_cibles` reste
    inchangé — il n'ouvre aucun fichier, et deux contrôles en dépendent.

    C7 y est émis au passage : une fiche de discernement dont le `status` sort
    du vocabulaire clos du Sceau rend le contrôle C5/C6 indécidable sur elle.
    Le vérificateur ne le devine pas et ne la tient pas pour tranchée en
    silence — il le dit.
    """
    non_tranches = set()
    dossier = os.path.join(racine, *DOSSIER_DISCERNEMENT.split("/"))
    if not os.path.isdir(dossier):
        return non_tranches
    for base, dossiers, fichiers in os.walk(dossier):
        dossiers[:] = [
            d for d in dossiers
            if (d not in DOSSIERS_EXCLUS
                and (mode == "aucun"
                     or not hors_perimetre(
                         os.path.relpath(os.path.join(base, d), racine),
                         ignores, mode)))
        ]
        for nom in sorted(fichiers):
            if not nom.endswith(".md"):
                continue
            chemin_rel = os.path.relpath(os.path.join(base, nom), racine)
            if mode != "aucun" and hors_perimetre(chemin_rel, ignores, mode):
                continue
            try:
                fm, _, _ = separer_frontmatter(lire(os.path.join(base, nom)))
            except Exception:                              # pragma: no cover
                continue                    # X0 est déjà émis par la passe principale
            statut = str((fm or {}).get("status", "")).strip()
            if statut == "speculatif":
                non_tranches.add(chemin_rel[:-3].replace(os.sep, "/"))
            elif statut and statut not in STATUTS_SCEAU:
                rap.avertir(chemin_rel, "C7",
                            f"`status: {statut}` hors du vocabulaire clos du Sceau "
                            f"— l'étanchéité inversée (C5/C6) ne peut pas dire si "
                            f"cette fiche est tranchée ; elle n'est pas comptée "
                            f"comme non tranchée")
    return non_tranches


def resoudre_cible(brut, par_chemin, par_slug):
    """Chemin sans extension visé par `[[brut]]`, ou None s'il ne résout pas.

    Même route que C1/C2 : chemin exact, sinon premier candidat par slug nu.
    Aucun avertissement n'est émis ici — la résolution est déjà contrôlée."""
    cible = brut.strip().replace("\\", "/")
    if cible.endswith(".md"):
        cible = cible[:-3]
    if RE_LIEN_PLACEHOLDER.match(cible):
        return None
    if cible in par_chemin:
        return cible
    candidats = par_slug.get(os.path.basename(cible), [])
    return candidats[0] if candidats else None


def controler_etancheite_inversee(chemin_rel, fm, corps, n_fm,
                                  par_chemin, par_slug, non_tranches, rap):
    """C5/C6 — une page orthodoxe pointant vers un discernement non tranché.

    C5 (cartouche) : aucune exception n'y atteint. Le cartouche est la
        déclaration de rattachement de la fiche, il ne porte pas de signalement
        — la clause d'exception vit dans une phrase, et une phrase vit dans le
        corps. C'est la forme retenue par les correctifs du 2026-09-10.
    C6 (corps) : permis, mais seulement signalé — 🔍 sur la ligne du lien.
    """
    if circuit_de(chemin_rel) != "doctrinal" or not fm:
        return
    if str(fm.get("status", "")).strip() not in STATUTS_ORTHODOXES:
        return
    if os.path.basename(chemin_rel) in FICHIERS_EXEMPTS_C3:
        return                      # annales/index : mêmes liens de service qu'en C3

    # C5 — champs de liens du cartouche.
    for champ in CHAMPS_LIENS_CARTOUCHE:
        valeurs = fm.get(champ)
        if not isinstance(valeurs, list):
            continue
        for valeur in valeurs:
            for brut in RE_WIKILINK.findall(str(valeur)):
                if resoudre_cible(brut, par_chemin, par_slug) in non_tranches:
                    rap.avertir(chemin_rel, "C5",
                                f"étanchéité inversée : page `traditionnel` → "
                                f"discernement non tranché au cartouche "
                                f"(`{champ}:`) — [[{brut}]]. L'exception "
                                f"« lien défensif/généalogique signalé » ne "
                                f"porte qu'au corps")

    # C6 — corps, ligne à ligne : `masquer_code` conserve le nombre de lignes,
    # les indices restent donc alignés sur le fichier (n_fm lignes de cartouche).
    for i, ligne in enumerate(masquer_code(corps).split("\n")):
        if MARQUEUR_SUGGERE in ligne:
            continue
        for brut in RE_WIKILINK.findall(ligne):
            if resoudre_cible(brut, par_chemin, par_slug) in non_tranches:
                rap.avertir(chemin_rel, "C6",
                            f"étanchéité inversée : page `traditionnel` → "
                            f"discernement non tranché — [[{brut}]] — sans le "
                            f"marqueur {MARQUEUR_SUGGERE} qui signale "
                            f"l'exception (lien défensif/généalogique)",
                            ligne=n_fm + i + 1)


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------

def controler_protocoles(racine, rap):
    """P1/P2 — la garde mécanique du corollaire d'auto-suffisance (Cmd 14).

    P1 : un renvoi nomme une fiche de `protocoles/` qui n'existe pas — la
         lettre annoncée est introuvable, l'auto-suffisance est rompue.
    P2 : une fiche de `protocoles/` que nul pointeur de `CLAUDE.md` racine ne
         nomme — « un protocole que rien n'appelle n'est pas un protocole,
         c'est un oubli ».

    Les renvois sont relevés dans le `CLAUDE.md` racine ET dans les `CLAUDE.md`
    locaux de circuit (§II bis) pour P1 ; seuls ceux de la racine comptent pour
    P2, conformément à la lettre (« que nul pointeur racine ne nomme »).
    """
    dossier = os.path.join(racine, "protocoles")
    if not os.path.isdir(dossier):
        return
    presentes = {n for n in os.listdir(dossier) if n.endswith(".md")}

    def renvois(chemin_abs):
        try:
            texte = lire(chemin_abs)
        except Exception:                                     # pragma: no cover
            return {}
        trouves = {}
        for num, ligne in enumerate(texte.split("\n"), 1):
            for m in RE_RENVOI_PROTOCOLE.finditer(RE_CITATION.sub("", ligne)):
                trouves.setdefault(m.group(1), num)
        return trouves

    racine_md = os.path.join(racine, "CLAUDE.md")
    nommees = renvois(racine_md) if os.path.isfile(racine_md) else {}

    sources = [("CLAUDE.md", nommees)]
    for circ in CIRCUITS:
        local = os.path.join(racine, circ, "CLAUDE.md")
        if os.path.isfile(local):
            sources.append((f"{circ}/CLAUDE.md", renvois(local)))

    for rel, trouves in sources:
        for cible, num in sorted(trouves.items()):
            if cible not in presentes:
                rap.erreur(rel, "P1",
                           f"renvoi vers `protocoles/{cible}` : la fiche "
                           f"n'existe pas", num)

    for fiche in sorted(presentes - set(nommees)):
        rap.erreur(f"protocoles/{fiche}", "P2",
                   "aucun pointeur de `CLAUDE.md` racine ne nomme cette fiche "
                   "(Cmd 14 : un protocole que rien n'appelle est un oubli)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".", help="racine du dépôt (défaut : .)")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--strict", action="store_true",
                    help="les avertissements deviennent bloquants")
    ap.add_argument("--tout", action="store_true",
                    help="ne pas restreindre au périmètre du dépôt : contrôler "
                         "aussi ce que .gitignore exclut (venv tiers, sorties "
                         "régénérables, sas raw/). Rien n'est donc jamais "
                         "hors de portée du script, c'est un choix d'appel.")
    args = ap.parse_args()

    racine = os.path.abspath(args.racine)
    if not os.path.isdir(racine):
        print(f"Racine introuvable : {racine}", file=sys.stderr)
        return 2

    rap = Rapport()
    ignores, mode = (set(), "aucun") if args.tout else perimetre_ignore(racine)
    par_chemin, par_slug = collecter_cibles(racine, ignores, mode)
    non_tranches = indexer_discernements(racine, ignores, mode, rap)
    controles = 0

    for base, dossiers, fichiers in os.walk(racine):
        dossiers[:] = [
            d for d in dossiers
            if (d not in DOSSIERS_EXCLUS
                and (mode == "aucun"
                     or not hors_perimetre(
                         os.path.relpath(os.path.join(base, d), racine),
                         ignores, mode)))
        ]
        for nom in sorted(fichiers):
            if not nom.endswith(".md"):
                continue
            chemin_abs = os.path.join(base, nom)
            chemin_rel = os.path.relpath(chemin_abs, racine)
            if mode != "aucun" and hors_perimetre(chemin_rel, ignores, mode):
                continue
            try:
                texte = lire(chemin_abs)
            except Exception as exc:                       # pragma: no cover
                rap.erreur(chemin_rel, "X0", f"lecture impossible : {exc}")
                continue

            fm, corps, n_fm = separer_frontmatter(texte)
            controler_frontmatter(chemin_rel, fm, rap)
            controler_original(chemin_rel, fm, corps, rap)
            controler_liens(chemin_rel, corps, par_chemin, par_slug, rap)
            controler_liens_cartouche(chemin_rel, fm, par_chemin, par_slug, rap)
            controler_etancheite_inversee(chemin_rel, fm, corps, n_fm,
                                          par_chemin, par_slug, non_tranches, rap)
            if nom in NOMS_ANNALES:
                controler_annales(chemin_abs, chemin_rel, rap)
            controles += 1

    controler_protocoles(racine, rap)

    # Le périmètre est déclaré, jamais silencieux : un lecteur doit savoir ce
    # que le script a regardé avant de lire ce qu'il a trouvé.
    perimetre = {
        "git": "périmètre du dépôt (ce que `.gitignore` exclut n'est pas contrôlé)",
        "repli": "repli hors dépôt git : dossiers cachés exclus",
        "aucun": "--tout : aucune exclusion, y compris ce que `.gitignore` exclut",
    }[mode]

    if args.json:
        print(json.dumps({"perimetre": mode,
                          "fichiers_controles": controles,
                          "erreurs": rap.erreurs,
                          "avertissements": rap.avertissements},
                         ensure_ascii=False, indent=2))
    else:
        print(f"{controles} fichier(s) .md contrôlé(s) — {perimetre}.\n")
        rap.imprimer()

    if rap.erreurs:
        return 1
    if args.strict and rap.avertissements:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:                               # pragma: no cover
        print(f"Erreur d'exécution : {exc}", file=sys.stderr)
        sys.exit(2)
