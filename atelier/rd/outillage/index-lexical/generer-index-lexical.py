#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer-index-lexical.py — Index lexical du dépôt (termes, noms, définitions).
Version 1.0 (2026-09-08)

Flux (à sens unique, CLAUDE.md §VII, règle commune des manifestes) :

    dépôt (.md)  →  index-lexical.json  →  outil MCP / Obsidian

Aucun LLM n'intervient dans cette boucle. L'index dit *où chercher*, jamais
*quoi conclure* : il ne lève aucun `to-source` et ne porte aucun contenu
doctrinal.

--------------------------------------------------------------------------------
DEUX RÉGIMES DE RÉCOLTE, JAMAIS CONFONDUS
--------------------------------------------------------------------------------
  CIRCUITS (doctrinal, atelier, label, hermeneutique, meta)
      Récolte structurelle (tags, slugs, translittérations, définitions) et
      annotée (<dfn>, <span data-nom>, <abbr>). Renvois en WIKILINK.

  textes/  (CLAUDE.md §II — le cabinet de lecture)
      Récolte par OCCURRENCE SEULE, en lecture stricte. Jamais d'écriture
      (règle d'immuabilité). Les renvois sont des CHEMINS NUS, jamais des
      wikilinks : `textes/` ne devient pas cible de lien, ne reçoit aucun
      Sceau, et ne devient pas un sixième circuit.

--------------------------------------------------------------------------------
CE QUI EST RÉCOLTÉ COMME TERME
--------------------------------------------------------------------------------
  tag         — valeur de `tags:` du frontmatter (vocabulaire curé à la main)
  translit    — token portant un diacritic ABSENT du français (ā ṛ ṇ ś ḥ ṭ ...).
                Signal déterministe et propre à ce corpus : c'est très
                exactement le nom propre ou le terme technique que la recherche
                naïve manque (« martanda » ne trouve pas « Mārtāṇḍa »).
  definition  — amorce `**Terme** :` (motif déjà établi dans le dépôt, repris
                de carte-du-depot.py, RE_SOUS_SECTION)
  annotation  — <dfn data-terme>, <span data-nom>, <abbr title> (phase 2 ;
                aucune n'existe encore, le lecteur est en place avant elles)
  titre       — tête du `title:` du Sceau, des H1 et des H2 (correctif B,
                2026-09-08). CLAUDE.md §VII, discipline des langues
                originales, point 3 : le `title:` et le H1 sont le SITE
                CANONIQUE de la forme originale. Trois portes d'admission,
                toutes déterministes — écriture originale, translittération,
                composant du slug de la fiche (cette dernière réservée au
                `title:`/H1). Aucune heuristique de capitale : elle ferait
                entrer « Proposition », « Rapport », « Désactivation ».

--------------------------------------------------------------------------------
APPARIEMENT LATIN <-> ÉCRITURE ORIGINALE (champ `apparie`)
--------------------------------------------------------------------------------
CLAUDE.md §VII, point 6 — réciprocité : l'index doit atteindre le terme DANS
LES DEUX SENS. Le champ `apparie` est renseigné SEULEMENT sur une paire que le
texte du dépôt énonce lui-même — « Tomoe (巴) », « **Buddhi** (Sanskrit :
बुद्धि) ». Aucun jugement de modèle n'y entre, aucune translittération n'y est
devinée : là où le dépôt se tait, le champ reste vide, et la clé est déclarée
orpheline plutôt que complétée. C'est la règle « établi vs suggéré » du §VII
(manifestes, règle 3) appliquée au lexique.

--------------------------------------------------------------------------------
PLANCHER DE NON-VACUITÉ (refus D3)
--------------------------------------------------------------------------------
Le script REFUSE d'écrire un index vide, ou dont un circuit déclaré ne produit
aucune entrée. Motif : `glossaire-unifie.md` a été commité à « Termes
distincts : 0 » sans que rien ne s'en plaigne — la forme exacte de PRO-01 et
INF-14 (CLAUDE.md §VII, Épreuve des contrôles). Un index vide n'est pas un
index vert.
"""

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

VERSION = "1.0"

CIRCUITS = ["doctrinal", "atelier", "label", "hermeneutique", "meta"]
DOSSIER_TEXTES = "textes"

# Fichiers de gouvernance : ils parlent DU dépôt, ils n'en sont pas la matière.
EXCLUS = {"CLAUDE.md", "index.md", "annales.md", "meta-index.md", "meta-annales.md"}

# Matière tierce vendorisée : un virtualenv, des paquets installés, un cache.
# Elle vit dans l'arborescence sans être matière du dépôt — l'indexer y ferait
# entrer la documentation de bibliothèques Python comme si Sidy l'avait écrite.
VENDOR = {"node_modules", "__pycache__", "site-packages", ".git"}


def fichiers_suivis(racine: Path):
    """Ensemble des `.md` suivis par git, ou None si git est indisponible.

    C'est la définition exacte de « matière du dépôt ». Un fichier ignoré
    (`graphify-out/`, un virtualenv) existe sur ce disque mais pas chez qui
    clone : l'indexer fabrique des renvois morts. Le contrôle C1 de
    `verifier-invariants.py` l'a signalé — c'est lui qui a trouvé la faute.
    """
    try:
        r = subprocess.run(
            ["git", "-C", str(racine), "ls-files", "-z", "*.md"],
            capture_output=True, check=True)
        return {x for x in r.stdout.decode("utf-8").split("\0") if x}
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError):
        return None


def vendorise(chemin: Path, base: Path) -> bool:
    """Vrai si le chemin traverse un dossier caché ou vendorisé."""
    for part in chemin.relative_to(base).parts:
        if part in VENDOR or (part.startswith(".") and part != "."):
            return True
    return False

# Lettres accentuées du français. Un token qui n'en porte QUE de celles-ci est
# un mot français ordinaire ; un token portant autre chose est une
# translittération (ou un nom propre étranger) — c'est le discriminant.
FRANCAIS = set("àâäçéèêëîïôöùûüÿœæÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸŒÆ")

# Harakat, tatweel et signes coraniques : bruit de vocalisation à replier pour
# que la même racine arabe se retrouve sous une clé unique.
ARABE_DIACRITIQUES = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")

# Marques combinantes (categories Unicode Mn/Mc), construites PAR CATEGORIE et
# jamais a la main. Motif : `\w` de Python EXCLUT Mn/Mc, de sorte que
# `[^\W\d_]+` eclate toute ecriture qui les emploie —
#     बिंदु -> ['ब','द']   ·   תּוֹרָה -> ['ת','ו','ר','ה']
# — et jusqu'au francais en encodage NFD (`realisation` -> `re` + `alisation`).
# L'arabe non vocalise et le han y echappaient (aucune marque), d'ou le
# contraste trompeur « arabe 469 cles / devanagari 0 ».
# Corrige le 2026-09-08 au titre de la discipline des langues originales
# (CLAUDE.md, §VII). Mesure prealable sur les 2131 fichiers du depot :
# 3043 cles en ecriture originale recollees, 2578 fragments resorbes,
# ZERO cle latine alteree (les 3 disparues — alisation, pendance, tudes —
# sont elles aussi des recollages NFD).
_MARQUES = "".join(
    re.escape(chr(cp)) for cp in range(0x300, 0x1AB0)
    if unicodedata.category(chr(cp)) in ("Mn", "Mc")
)
_LETTRE = r"[^\W\d_](?:[^\W\d_]|[" + _MARQUES + r"])*"
RE_MOT = re.compile(_LETTRE + r"(?:['’\-]" + _LETTRE + r")*", re.UNICODE)
RE_DEFINITION = re.compile(r"^\s*\*\*([^*\n]{2,60})\*\*\s*:", re.MULTILINE)
RE_DFN = re.compile(r"<dfn\b[^>]*\bdata-terme=\"([^\"]+)\"", re.IGNORECASE)
RE_NOM = re.compile(r"<span\b[^>]*\bdata-nom=\"([^\"]+)\"", re.IGNORECASE)
RE_ABBR = re.compile(r"<abbr\b[^>]*\btitle=\"([^\"]+)\"", re.IGNORECASE)
RE_CODE = re.compile(r"```.*?```|`[^`\n]+`", re.DOTALL)
RE_LIGNE_TABLE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)
RE_SEPARATEUR = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
RE_PREFIXE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}[_-]")

# --- Correctif B (2026-09-08, CLAUDE.md §VII, discipline des langues
# originales, points 3 et 6) ------------------------------------------------
# Le `title:` du Sceau et le H1 sont déclarés SITE CANONIQUE de la forme
# originale. Ils n'étaient pas récoltés : `tomoe` et `巴` restaient absents de
# l'index malgré une fiche entière qui leur est consacrée. Forme exacte de la
# faute muette (PRO-01, INF-14) — l'index paraissait riche à 9841 termes.
RE_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
RE_H2 = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)

# Un titre du dépôt se lit « Terme — glose » ou « Terme : glose ». La glose est
# de la prose : seule la TÊTE porte le sujet de la fiche. Mesuré sur les 716
# titres : 434 portent `—`, 114 `:`, 3 `–`, 1 ` - ` ; le reste est une tête
# nue (« René Guénon »).
RE_TETE_TITRE = re.compile(r"\s+[—–:]\s+|\s+-\s+")

# Écritures d'origine reconnues par plage : hébreu, arabe, devanagari, grec,
# han, kana. Une lettre hors de l'alphabet latin — au sens de la catégorie
# Unicode L* et du bloc — vaut forme originale.
def est_ecriture_originale(token: str) -> bool:
    """Le token est-il écrit dans une écriture non latine ?

    Les LETTRES MODIFICATIVES (catégorie Lm) sont exclues : `ʿ` (ʿayn) et `ʾ`
    (hamza) ne portent pas le nom LATIN, or ils appartiennent au dispositif de
    TRANSLITTÉRATION latine, pas à l'écriture d'origine. Sans cette exclusion,
    `Chaussure (naʿl)` et `Laṭāʾif (subtils)` étaient lus comme des paires
    latin/original — mesuré, deux faux appariements sur 97.
    """
    for c in token:
        if unicodedata.category(c) not in ("Lo", "Ll", "Lu", "Lt"):
            continue
        try:
            if "LATIN" not in unicodedata.name(c):
                return True
        except ValueError:
            continue
    return False


# Appariement attesté PAR LE TEXTE : « Tomoe (巴) », « Bindu (बिंदु) »,
# « **Buddhi** (Sanskrit : बुद्धि) ». Aucun jugement de modèle n'entre ici —
# le dépôt énonce lui-même la paire, ou elle n'existe pas (§VII, règle 3 des
# manifestes : établi vs suggéré, jamais fondus).
RE_APPARIEMENT = re.compile(
    r"\*{0,2}([A-Za-z\u00C0-\u024F\u1E00-\u1EFF\u02BF\u02BE'\u2019-]{2,30})\*{0,2}"
    r"\s*\(\s*(?:[^():]{0,30}:\s*)?([^()]{1,40}?)\s*\)"
)

# Bruit de balisage et mots-outils : jamais des termes d'index.
ARRET = {
    "les", "des", "une", "aux", "par", "pour", "dans", "sur", "avec", "sans",
    "que", "qui", "quo", "est", "sont", "ete", "cette", "ces", "son", "sa",
    "the", "and", "for", "with", "http", "https", "www", "com", "org", "md",
    "note", "voir", "cf", "ibid", "etc", "page", "pages", "tome", "vol",
    "true", "false", "null", "yaml", "json", "html", "css", "div", "span",
    # Anglais : le repli diacritique fait tomber « wasʿ » sur « was ». Sans ce
    # garde-fou, un terme arabe légitime capte 1700 occurrences parasites.
    "was", "has", "its", "are", "this", "that", "from", "have", "been", "they",
    "were", "which", "will", "not", "but", "all", "any", "may", "can", "one",
    "out", "use", "see", "per", "via", "his", "her", "their", "there", "when",
    # Français : mots-outils et vocabulaire de gouvernance du dépôt.
    "tout", "tous", "dont", "sous", "entre", "meme", "aussi", "ainsi", "donc",
    "mais", "leur", "elle", "cela", "chaque", "autre", "comme", "fait", "bien",
    "tres", "deja", "encore", "alors", "apres", "avant", "plus", "non", "ceux",
    "fiche", "fiches", "depot", "index", "titre", "champ", "statut", "commit",
}

# Étiquettes de champ : `**Statut** :`, `**Source** :` balisent un champ, elles
# ne définissent rien. Au-delà de ce nombre de fiches distinctes, une amorce est
# tenue pour une étiquette et perd le rôle `definition`.
SEUIL_ETIQUETTE = 10

# Au-delà, une cellule de table est tenue pour de la prose et non pour une
# liste de noms : sa majuscule initiale est écartée.
CELLULE_COURTE = 4

# Nombre de fiches au-delà duquel le condensé cesse d'énumérer et se contente
# de compter.
SEUIL_ENUMERATION = 8

# Part minimale de formes capitalisées pour qu'un token récolté en table SEULE
# soit tenu pour un nom propre. Mesuré sur le corpus, jamais codé en dur : un
# nom propre est presque toujours capitalisé (« Indra »), un mot commun
# presque jamais (« monde »). Le corpus tranche, pas une liste d'exclusion.
PART_CAPITALE = 0.60

MIN_LONGUEUR = 3


def normaliser(txt: str) -> str:
    """Replie une forme attestée sur sa clé de recherche.

    NFD, chute des marques combinantes, minuscules, ASCII. « Mārtāṇḍa » et
    « Martanda » tombent sur la même clé — c'est tout l'objet : la recherche
    naïve retrouve la forme diacritée qu'elle ne sait pas taper.
    """
    txt = ARABE_DIACRITIQUES.sub("", txt)
    txt = unicodedata.normalize("NFD", txt)
    txt = "".join(c for c in txt if not unicodedata.combining(c))
    txt = txt.replace("ʿ", "").replace("ʾ", "")   # ʿayn, hamza
    txt = txt.replace("’", "'").replace("ـ", "")
    return txt.casefold().strip()


def est_translittere(token: str) -> bool:
    """Le token porte-t-il un diacritic étranger au français ?"""
    for c in token:
        if ord(c) < 128:
            continue
        if c in FRANCAIS:
            continue
        if unicodedata.category(c).startswith("L"):
            return True
    return False


def lire_frontmatter(texte: str) -> dict:
    """Frontmatter minimal : on ne lit que ce dont l'index a besoin."""
    if not texte.startswith("---"):
        return {}
    parties = re.split(r"^---\s*$", texte, maxsplit=2, flags=re.MULTILINE)
    if len(parties) < 3:
        return {}
    fm = {}
    for ligne in parties[1].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_\-]*)\s*:\s*(.*)$", ligne)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def extraire_tags(brut: str) -> list:
    brut = brut.strip()
    if brut.startswith("[") and brut.endswith("]"):
        brut = brut[1:-1]
    return [t.strip().strip("\"'") for t in brut.split(",") if t.strip()]


def corps_sans_frontmatter(texte: str) -> str:
    if texte.startswith("---"):
        parties = re.split(r"^---\s*$", texte, maxsplit=2, flags=re.MULTILINE)
        if len(parties) >= 3:
            return parties[2]
    return texte


def slug_de(chemin: Path) -> str:
    return RE_PREFIXE_DATE.sub("", chemin.stem)


class Index:
    def __init__(self):
        self.termes = {}
        self.casse = defaultdict(lambda: [0, 0])   # cle -> [capitale, minuscule]

    def entree(self, cle: str) -> dict:
        if cle not in self.termes:
            self.termes[cle] = {
                "cle": cle,
                "formes": set(),
                "roles": set(),
                "fiches": defaultdict(lambda: {"roles": set(), "n": 0}),
                "textes": defaultdict(int),
                "occurrences": 0,
                # Réciprocité de l'index (§VII, point 6) : la clé latine porte
                # sa forme originale et réciproquement. Renseigné SEULEMENT
                # sur appariement attesté par le texte du dépôt.
                "apparie": set(),
            }
        return self.termes[cle]

    def declarer(self, forme: str, role: str, chemin_rel: str):
        cle = normaliser(forme)
        # Le plancher de longueur est une heuristique LATINE : « il », « du »
        # n'apprennent rien. Il ne vaut pas pour une écriture originale, où le
        # caractère est dense — 巴 (tomoe) et 神道 (shintō) sont des termes
        # pleins que MIN_LONGUEUR faisait tomber en silence.
        if len(cle) < MIN_LONGUEUR and not est_ecriture_originale(cle):
            return None
        # `tag` et `annotation` sont posés à la main par Sidy : ce vocabulaire
        # fait autorité et ne se filtre pas. Seul l'heuristique est filtré.
        if cle in ARRET and role not in ("tag", "annotation"):
            return None
        e = self.entree(cle)
        e["formes"].add(forme)
        e["roles"].add(role)
        e["fiches"][chemin_rel]["roles"].add(role)
        return cle


    def apparier(self, latin: str, original: str):
        """Enregistre une paire ATTESTÉE PAR LE TEXTE, dans les deux sens."""
        if not est_ecriture_originale(original) or est_ecriture_originale(latin):
            return
        a, b = normaliser(latin), normaliser(original)
        if not a or not b or a == b:
            return
        if a not in self.termes or b not in self.termes:
            return
        self.termes[a]["apparie"].add(b)
        self.termes[b]["apparie"].add(a)


def recolter_titre(index: Index, source: str, rel: str, slug: str,
                   role: str, avec_slug: bool):
    """Récolte la TÊTE d'un titre (§VII, point 3 — site canonique).

    Trois portes d'admission, toutes déterministes, aucune heuristique de
    capitale — celle-ci ferait entrer « Désactivation », « Proposition »,
    « Rapport » et noierait l'index sous le vocabulaire de gouvernance :
      (a) écriture originale — toujours, quelle que soit la longueur ;
      (b) translittération — le signal déjà établi du corpus ;
      (c) composant du slug de la fiche — c'est très exactement ce que le
          défaut faisait perdre (`bindu`, `furin`, `muqarnas`, `tomoe`,
          `tughyan`, `voilette`, `morphopsychologie` : sept fiches invisibles
          dans leur propre index). Réservé au `title:`/H1, jamais aux H2.
    """
    tete = RE_TETE_TITRE.split(source, maxsplit=1)[0]
    morceaux = f"-{slug}-"
    for token in RE_MOT.findall(tete):
        if est_ecriture_originale(token) or est_translittere(token):
            index.declarer(token, role, rel)
    if not avec_slug:
        return
    # La porte du slug s'applique au titre ENTIER, non à sa seule tête : elle
    # est déjà close par elle-même — le token doit être un composant du nom de
    # fichier. Restreinte à la tête, elle manquait `voilette`, dont le titre
    # est « Le voile du visage — hijab/niqab islamique et voilette... ».
    for token in RE_MOT.findall(source):
        cle = normaliser(token)
        if cle and (cle == slug or f"-{cle}-" in morceaux):
            index.declarer(token, role, rel)


def retenir(f: Path, racine: Path, base: Path, rel: str, suivis) -> bool:
    """Le fichier est-il matière indexable du dépôt ?"""
    if f.name in EXCLUS:
        return False
    if suivis is not None:
        return rel in suivis
    return not vendorise(f, base)      # repli quand git est indisponible


def recolter(racine: Path, index: Index, rapport: dict, suivis):
    """Passe 1 — le vocabulaire, récolté sur les circuits SEULEMENT."""
    paires = []
    for circuit in CIRCUITS:
        base = racine / circuit
        if not base.is_dir():
            rapport["circuits_absents"].append(circuit)
            continue
        n_fiches = 0
        for f in sorted(base.rglob("*.md")):
            rel = str(f.relative_to(racine))
            if not retenir(f, racine, base, rel, suivis):
                continue
            try:
                texte = f.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                rapport["illisibles"].append(f"{f} : {exc}")
                continue
            fm = lire_frontmatter(texte)
            if fm.get("type") == "artefact-derive":
                continue                      # jamais s'indexer soi-même
            n_fiches += 1
            corps = RE_CODE.sub(" ", corps_sans_frontmatter(texte))

            for tag in extraire_tags(fm.get("tags", "")):
                index.declarer(tag, "tag", rel)
            for forme in RE_DEFINITION.findall(corps):
                index.declarer(forme.strip(), "definition", rel)
            for forme in RE_DFN.findall(corps):
                index.declarer(forme, "annotation", rel)
            for forme in RE_NOM.findall(corps):
                index.declarer(forme, "annotation", rel)
            for forme in RE_ABBR.findall(corps):
                index.declarer(forme, "annotation", rel)
            for token in RE_MOT.findall(corps):
                cle_t = normaliser(token)
                if cle_t:
                    index.casse[cle_t][0 if token[:1].isupper() else 1] += 1
                if est_translittere(token):
                    index.declarer(token, "translit", rel)
            for ligne in RE_LIGNE_TABLE.findall(corps):
                if RE_SEPARATEUR.match(ligne):
                    continue
                for cellule in ligne.strip().strip("|").split("|"):
                    tokens = RE_MOT.findall(cellule)
                    # Une cellule courte est une liste de noms (« Dhātṛ ·
                    # Aryaman ») : toute capitale y est un nom propre. Une
                    # cellule longue est de la prose, et sa première capitale
                    # n'est qu'une majuscule de phrase — on l'écarte.
                    debut = 0 if len(tokens) <= CELLULE_COURTE else 1
                    for token in tokens[debut:]:
                        if len(token) >= 4 and token[:1].isupper():
                            index.declarer(token, "table", rel)

            slug = slug_de(f)

            # --- Correctif B : le titre et les intertitres -----------------
            titre = fm.get("title", "").strip().strip("\"'")
            sources_titre = ([titre] if titre else []) + RE_H1.findall(corps)
            for src in sources_titre:
                recolter_titre(index, src, rel, slug, "titre", True)
            # Les H2 sont 4054 contre 881 H1 : ce sont des intertitres de
            # section, donc de la prose française. Admission STRICTE — jamais
            # la porte du slug, sans quoi le vocabulaire de gouvernance entre.
            for src in RE_H2.findall(corps):
                recolter_titre(index, src, rel, slug, "titre", False)
            # Appariement attesté : seulement là où le dépôt énonce la paire.
            # Différé — les deux clés d'une paire ne sont pas nécessairement
            # récoltées par le même fichier ; on apparie une fois la récolte
            # close, jamais au fil de l'eau.
            for src in sources_titre:
                paires.extend(RE_APPARIEMENT.findall(src))
            for ligne in corps.splitlines():
                if ligne.lstrip().startswith("**"):
                    paires.extend(RE_APPARIEMENT.findall(ligne))

            for cle in list(index.termes):
                if cle and (cle == slug or f"-{cle}-" in f"-{slug}-"):
                    index.termes[cle]["fiches"][rel]["roles"].add("fiche")
        rapport["fiches_par_circuit"][circuit] = n_fiches

    for latin, orig in paires:
        index.apparier(latin, orig)
    rapport["appariements"] = sum(
        1 for e in index.termes.values() if e["apparie"])


def filtrer_etiquettes(index: Index, rapport: dict):
    """Déclasse les amorces `**X** :` qui balisent un champ au lieu de définir.

    `**Statut** :` ouvre un champ dans 34 fiches ; ce n'est pas une définition.
    Le terme perd le rôle `definition`, et disparaît s'il n'en avait pas d'autre.
    """
    communs = []
    for cle, e in list(index.termes.items()):
        if e["roles"] != {"table"}:
            continue                       # une autre preuve suffit à le tenir
        maj, minu = index.casse.get(cle, [0, 0])
        total = maj + minu
        if total and maj / total < PART_CAPITALE:
            del index.termes[cle]
            communs.append(cle)
    rapport["mots_communs_ecartes"] = len(communs)

    retires = []
    for cle, e in list(index.termes.items()):
        n = sum(1 for v in e["fiches"].values() if "definition" in v["roles"])
        if n <= SEUIL_ETIQUETTE:
            continue
        e["roles"].discard("definition")
        for v in e["fiches"].values():
            v["roles"].discard("definition")
        retires.append(cle)
        if not e["roles"]:
            del index.termes[cle]
    rapport["etiquettes_declassees"] = sorted(retires)


def compter(racine: Path, index: Index, rapport: dict, avec_textes: bool, suivis):
    """Passe 2 — les occurrences. Un seul balayage, dictionnaire en mémoire."""
    simples = {c for c in index.termes if " " not in c and "'" not in c}
    phrases = [c for c in index.termes if c not in simples]

    cibles = [(c, racine / c, "circuit") for c in CIRCUITS]
    if avec_textes:
        cibles.append((DOSSIER_TEXTES, racine / DOSSIER_TEXTES, "texte"))

    for nom, base, genre in cibles:
        if not base.is_dir():
            continue
        n = 0
        for f in sorted(base.rglob("*.md")):
            rel = str(f.relative_to(racine))
            if not retenir(f, racine, base, rel, suivis):
                continue
            try:
                texte = f.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                rapport["illisibles"].append(f"{f} : {exc}")
                continue
            # Sans ce garde-fou, l'index compte SES PROPRES occurrences à la
            # régénération suivante et gonfle indéfiniment. Un artefact dérivé
            # n'est jamais matière : il est reflet.
            if lire_frontmatter(texte).get("type") == "artefact-derive":
                continue
            corps = RE_CODE.sub(" ", corps_sans_frontmatter(texte))
            local = defaultdict(int)
            for token in RE_MOT.findall(corps):
                cle = normaliser(token)
                if cle in simples:
                    local[cle] += 1
                    index.termes[cle]["formes"].add(token)
            if phrases:
                plat = normaliser(" ".join(RE_MOT.findall(corps)))
                for cle in phrases:
                    k = plat.count(cle)
                    if k:
                        local[cle] += k
            for cle, k in local.items():
                e = index.termes[cle]
                e["occurrences"] += k
                if genre == "texte":
                    e["textes"][rel] += k
                else:
                    e["fiches"][rel]["n"] += k
                    e["fiches"][rel]["roles"].add("corps")
            n += 1
        if genre == "texte":
            rapport["textes_balayes"] = n


def refus(motif: str):
    print(f"REFUS : {motif}", file=sys.stderr)
    print("Rien n'a été écrit. Le dépôt est intact.", file=sys.stderr)
    sys.exit(2)


def controler(index: Index, rapport: dict, avec_textes: bool):
    """Plancher de non-vacuité (D3). Un index vide n'est pas un index vert."""
    if not index.termes:
        refus("l'index ne contient aucun terme.")
    for circuit, n in rapport["fiches_par_circuit"].items():
        if n == 0:
            refus(f"le circuit `{circuit}` n'a produit aucune fiche indexable.")
    porteurs = {c for c in CIRCUITS if rapport["fiches_par_circuit"].get(c)}
    vus = set()
    for e in index.termes.values():
        for rel in e["fiches"]:
            vus.add(rel.split("/", 1)[0])
    manquants = sorted(porteurs - vus)
    if manquants:
        refus(f"aucun terme récolté pour : {', '.join(manquants)}.")
    if avec_textes and rapport.get("textes_balayes", 0) == 0:
        refus("`textes/` est au périmètre mais aucun fichier n'a été balayé.")
    if sum(e["occurrences"] for e in index.termes.values()) == 0:
        refus("aucune occurrence comptée sur l'ensemble du dépôt.")


def serialiser(index: Index, rapport: dict, avec_textes: bool) -> dict:
    """Sérialise en internant les chemins.

    Les mêmes chemins se répètent des milliers de fois d'un terme à l'autre.
    Une table de chemins et des renvois entiers ramènent l'artefact de 17 Mo à
    ~1,5 Mo, du même ordre que `graphe-cartographie.json`.
    """
    chemins, idx = [], {}

    def ref(c):
        if c not in idx:
            idx[c] = len(chemins)
            chemins.append(c)
        return idx[c]

    termes = {}
    for cle, e in sorted(index.termes.items()):
        termes[cle] = {
            "formes": sorted(e["formes"]),
            "roles": sorted(e["roles"]),
            "apparie": sorted(e["apparie"]),
            "occurrences": e["occurrences"],
            # [renvoi_chemin, occurrences, roles]
            "fiches": [[ref(rel), v["n"], sorted(v["roles"])]
                       for rel, v in sorted(e["fiches"].items())],
            # [renvoi_chemin, occurrences] — chemins nus, jamais wikilinks
            "textes": [[ref(rel), n] for rel, n in sorted(e["textes"].items())],
        }
    return {
        "generateur": "generer-index-lexical.py",
        "version": VERSION,
        "genere": datetime.now().isoformat(timespec="seconds"),
        "perimetre": {"circuits": CIRCUITS, "textes": avec_textes},
        "totaux": {
            "termes": len(termes),
            "occurrences": sum(t["occurrences"] for t in termes.values()),
            "fiches_indexees": sum(rapport["fiches_par_circuit"].values()),
            "textes_balayes": rapport.get("textes_balayes", 0),
        },
        "rapport": rapport,
        "chemins": chemins,
        "termes": termes,
    }


def rendre_md(data: dict, max_renvois: int = 5) -> str:
    """Rend un CONDENSÉ, non la totalité.

    L'index intégral pèse 2,5 Mo : injouable dans Obsidian sur iPad. Le `.md`
    sert l'orientation humaine — un terme y figure s'il croise au moins deux
    fiches, ou s'il relève du vocabulaire curé (tag, annotation, définition).
    Le détail exhaustif vit dans le JSON, que l'outil MCP interroge.
    """
    t = data["totaux"]
    chemins = data["chemins"]
    CURE = {"tag", "annotation", "definition"}
    retenus = {
        cle: e for cle, e in data["termes"].items()
        if len(e["fiches"]) >= 2 or CURE & set(e["roles"])
    }
    omis = len(data["termes"]) - len(retenus)

    L = ["---",
         'title: "Index lexical — termes, noms et definitions du depot"',
         "type: artefact-derive",
         'generateur: "generer-index-lexical.py"',
         "created: 2026-09-08",
         f"updated: {date.today().isoformat()}",
         "sources: []",
         "links: []",
         "---",
         "",
         "# Index lexical — termes, noms et definitions du depot",
         "",
         "> **ARTEFACT DERIVE — ne jamais editer a la main.** Regenere par",
         "> `generer-index-lexical.py` a partir des circuits et de `textes/`.",
         "> Le depot fait foi.",
         ">",
         "> Instrument de reperage : il dit *ou chercher*, jamais *quoi",
         "> conclure*. La levee d'un `to-source` reste la verification du",
         "> texte primaire par Sidy (CLAUDE.md §VII).",
         ">",
         "> Les renvois vers `textes/` sont des **chemins nus**, jamais des",
         "> wikilinks : `textes/` n'est pas un circuit et n'est la cible",
         "> d'aucun lien (CLAUDE.md §II).",
         "",
         f"**Termes distincts : {t['termes']} — occurrences : {t['occurrences']}"
         f" — fiches indexees : {t['fiches_indexees']}"
         f" — textes balayes : {t['textes_balayes']}**",
         "",
         f"Condense : {len(retenus)} termes affiches, {omis} termes d'occurrence",
         "isolee omis de cette vue. L'index integral est dans",
         "`index-lexical.json` (outil MCP `chercher_terme`).",
         ""]

    groupes = defaultdict(list)
    for cle, e in retenus.items():
        groupes[cle[0].upper() if cle[:1].isalpha() else "#"].append((cle, e))

    for initiale in sorted(groupes):
        L += [f"## {initiale}", "",
              "| terme | formes attestees | roles | fiches | textes/ | occ. |",
              "|---|---|---|---|---|---|"]
        for cle, e in sorted(groupes[initiale], key=lambda x: -x[1]["occurrences"]):
            formes = ", ".join(e["formes"][:4])
            if len(e["formes"]) > 4:
                formes += f" (+{len(e['formes']) - 4})"
            nf = len(e["fiches"])
            # Au-delà du seuil, énumérer cinq fiches sur quatre-vingt-dix-sept
            # est un choix arbitraire déguisé en information : on donne le
            # compte, et l'outil MCP sert la liste exacte à la demande.
            if nf > SEUIL_ENUMERATION:
                fiches = [f"**{nf} fiches**"]
            else:
                fiches = [f"[[{chemins[i][:-3]}]]"
                          for i, _, _ in e["fiches"][:max_renvois]]
                if nf > max_renvois:
                    fiches.append(f"+{nf - max_renvois}")
            nt = len(e["textes"])
            textes = "—" if not nt else (
                Path(chemins[e["textes"][0][0]]).name
                + (f" +{nt - 1}" if nt > 1 else ""))
            L.append(f"| `{cle}` | {formes} | {', '.join(e['roles'])} | "
                     f"{' · '.join(fiches) or '—'} | {textes} | "
                     f"{e['occurrences']} |")
        L.append("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Index lexical du depot.")
    ap.add_argument("--racine", default="/root/wiki")
    ap.add_argument("--sortie-json", default="")
    ap.add_argument("--sortie-md", default="")
    ap.add_argument("--sans-textes", action="store_true",
                    help="exclut textes/ du perimetre")
    args = ap.parse_args()

    racine = Path(args.racine).resolve()
    avec_textes = not args.sans_textes
    ici = Path(__file__).resolve().parent
    sortie_json = Path(args.sortie_json) if args.sortie_json else ici / "index-lexical.json"
    sortie_md = Path(args.sortie_md) if args.sortie_md else ici / "index-lexical.md"

    rapport = {
        "fiches_par_circuit": {},
        "circuits_absents": [],
        "illisibles": [],
        "etiquettes_declassees": [],
        "mots_communs_ecartes": 0,
        "filtre_git": False,
        "textes_balayes": 0,
    }

    suivis = fichiers_suivis(racine)
    rapport["filtre_git"] = suivis is not None
    if suivis is None:
        print("  git indisponible : repli sur le filtre vendor.", file=sys.stderr)

    index = Index()
    recolter(racine, index, rapport, suivis)
    filtrer_etiquettes(index, rapport)
    compter(racine, index, rapport, avec_textes, suivis)
    controler(index, rapport, avec_textes)

    data = serialiser(index, rapport, avec_textes)
    sortie_json.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    sortie_md.write_text(rendre_md(data), encoding="utf-8")

    t = data["totaux"]
    print(f"OK — {t['termes']} termes distincts, {t['occurrences']} occurrences, "
          f"{t['fiches_indexees']} fiches, {t['textes_balayes']} textes.")
    if rapport["circuits_absents"]:
        print(f"  circuits absents : {', '.join(rapport['circuits_absents'])}")
    if rapport["illisibles"]:
        print(f"  illisibles : {len(rapport['illisibles'])}")
    print(f"  → {sortie_json}")
    print(f"  → {sortie_md}")


if __name__ == "__main__":
    main()
