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
RANG 2 — APPARIEMENT PAR AUTORITÉ TEXTUELLE (champ `jurjani`)
--------------------------------------------------------------------------------
Verdict Sidy, 2026-09-08. Un second champ, `jurjani`, porte les appariements
que le *Kitāb al-Taʿrīfāt* d'al-Jurjānī — transcrit au dépôt — établit, chacun
avec son NUMÉRO DE DÉFINITION, qui est sa source. Il est **strictement séparé**
de `apparie` et ne s'y déverse jamais : deux rangs de crédibilité dans un même
champ seraient indistinguables. **Le rang 1 prime** — une clé que la fiche
apparie elle-même ne reçoit aucun renvoi Jurjānī.

Réciprocité (§VII, point 6) : la forme latine reçoit le renvoi inverse
SEULEMENT si elle est déjà une clé de l'index. On n'injecte pas le vocabulaire
du dictionnaire dans un index qui est celui du DÉPÔT — ce serait indexer
Jurjānī, non le wiki. Mesure du 2026-09-08 : 132 appariements, dont 84
réciproques.

Deux refus francs gardent ce rang, éprouvés le 2026-09-08 : source absente, et
récolte sous le plancher de non-vacuité (207 entrées mesurées, plancher 150).
Un dictionnaire vide ne se plaint jamais de lui-même.

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
import importlib.util
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
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
# --- Appariement JURJĀNĪ (rang 2) — champ `jurjani`, distinct de `apparie` ---
# Verdict Sidy, 2026-09-08 : « donne un champ propre à Jurjani et intègre les
# 132 à l'index ». Le champ est SÉPARÉ de `apparie` et ne s'y déverse jamais :
# `apparie` porte ce que la fiche énonce d'elle-même (rang 1), `jurjani` porte
# ce qu'une autorité textuelle transcrite au dépôt établit (rang 2). Deux rangs
# de crédibilité dans un même champ seraient indistinguables — c'est très
# exactement ce que la règle « établi vs suggéré » interdit (§VII, manifestes,
# règle 3).
#
# La source est le *Kitāb al-Taʿrīfāt* d'al-Jurjānī, transcrit au dépôt. Chaque
# appariement porte son NUMÉRO DE DÉFINITION : c'est sa source, vérifiable au
# texte. Aucun modèle n'intervient — le motif ci-dessous est la seule forme que
# ces deux fiches emploient.
SOURCES_JURJANI = (
    "doctrinal/sources/kitab-tarifat-corps-transcription.md",
    "doctrinal/sources/kitab-tarifat-index-transcription.md",
)

RE_JURJANI = re.compile(
    r"^###\s+(\d{4})\s+—\s+\*([^*]+?)\*\s+—\s+(\S.*?)\s*$", re.MULTILINE)

# Plancher de non-vacuité propre à la source (même motif que le refus D3) :
# 207 entrées mesurées le 2026-09-08. Si l'extraction s'effondre — motif changé,
# fiche renommée, transcription tronquée —, le script REFUSE au lieu de produire
# un index silencieusement privé de son rang 2. Un dictionnaire vide ne se
# plaint jamais de lui-même.
PLANCHER_JURJANI = 150

RE_TETE_TITRE = re.compile(r"\s+[—–:]\s+|\s+-\s+")

# Écritures d'origine reconnues par plage : hébreu, arabe, devanagari, grec,
# han, kana. Une lettre hors de l'alphabet latin — au sens de la catégorie
# Unicode L* et du bloc — vaut forme originale.
def _invariants():
    """Charge `verifier-invariants.py` (racine du dépôt) comme module.

    Le contrôleur racine détient la définition CANONIQUE de « écriture
    originale ». On l'importe plutôt que d'en garder une copie : deux
    définitions divergentes dans deux scripts, c'est la dérive que le partage
    de `fichiers_suivis()` avait déjà été écrit pour empêcher. Le sens de la
    dépendance est délibéré — l'outil de R&D dépend du contrôleur, jamais
    l'inverse. Son absence est une ERREUR FRANCHE, jamais un repli silencieux
    sur une copie locale : un index construit sur une seconde définition
    paraîtrait juste et ne le serait pas (§VII, Épreuve des contrôles).
    """
    chemin = Path(__file__).resolve().parents[4] / "verifier-invariants.py"
    if not chemin.is_file():
        # `refus()` est défini plus bas dans le fichier : l'appeler ici lève un
        # NameError, refus obtenu mais illisible. Constaté à l'épreuve du
        # 2026-09-08, corrigé — un refus doit NOMMER sa cause.
        sys.exit(f"REFUS — définition canonique de l'écriture originale "
                 f"introuvable : {chemin}\n"
                 f"Le générateur ne se replie JAMAIS sur une copie locale "
                 f"(§VII, Épreuve des contrôles).")
    spec = importlib.util.spec_from_file_location("_invariants", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


est_ecriture_originale = _invariants().est_ecriture_originale


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
                # Rang 2 — appariement par une autorité textuelle transcrite
                # au dépôt, avec son numéro de définition. JAMAIS fondu dans
                # `apparie`, qui est le rang 1.
                "jurjani": None,
                # Tradition SOURCÉE par la ou les fiches qui DÉFINISSENT le
                # terme — jamais par un décompte des fiches qui le citent.
                "tradition": None,
                # Langue DU TERME — axe distinct de la tradition, qui est un
                # cadre. Verdict Sidy 2026-09-09.
                "langue": None,
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
        # Une lettre grecque isolée est un LABEL dans ce dépôt, jamais un
        # terme : mesuré sur α, δ, γ, π, φ, tous employés comme variables ou
        # numéros de système (« système (α) », « conversion (δ) → (γ) »). Un
        # caractère han isolé, lui, est un terme plein (巴) — d'où la
        # distinction par écriture et non par longueur.
        if len(original.strip()) == 1 and "GREEK" in unicodedata.name(
                original.strip(), ""):
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


def charger_jurjani(racine: Path) -> dict:
    """Dictionnaire {forme arabe normalisée -> (n° de définition, translit)}.

    Refus francs plutôt que dégradation silencieuse : source absente, ou
    récolte sous le plancher de non-vacuité.
    """
    dico = {}
    for rel in SOURCES_JURJANI:
        f = racine / rel
        if not f.is_file():
            refus(f"source Jurjānī absente : {rel} — le rang 2 de l'index ne "
                  f"peut pas être produit, et un index privé de son rang 2 "
                  f"sans le dire serait un index muet")
        for num, lat, ar in RE_JURJANI.findall(f.read_text(encoding="utf-8")):
            lat = re.sub(r"\s*\([^)]*\)", "", lat).strip()
            if est_ecriture_originale(ar) and not est_ecriture_originale(lat):
                dico.setdefault(normaliser(ar), (num, lat, ar))
    if len(dico) < PLANCHER_JURJANI:
        refus(f"récolte Jurjānī sous le plancher : {len(dico)} entrées pour "
              f"{PLANCHER_JURJANI} attendues au minimum — motif de lecture "
              f"probablement caduc")
    return dico


# --- Langue du terme (verdict Sidy, 2026-09-09) ----------------------------
# « une alternative serait de classifier par langue plutôt que par tradition,
#   puisque chaque tradition trouve son véhicule en une langue ».
# L'axe est ONTOLOGIQUEMENT plus juste que la tradition : la langue est une
# propriété DU TERME, la tradition une propriété du CADRE où on le cite — d'où
# la divergence structurelle qui a fait échouer la voie du consensus.
# Il n'a qu'un défaut, mesuré : le dépôt n'énonce presque jamais la langue.
# Mais il a l'endroit pour le faire — le champ `original:` du Sceau (§IV,
# ouvert le 2026-09-08). L'axe se renforce donc EXACTEMENT au rythme de la
# discipline des langues originales, sans travail propre.
# Seules les écritures EXCLUSIVES donnent la langue. Le han (CJK) est
# volontairement absent : il sert le chinois ET le japonais, et `巴` (tomoe) y
# aurait été déclaré « chinois » alors que le terme est japonais. Une écriture
# partagée ne source pas une langue — elle source une écriture, ce qui n'est
# pas la même chose. Constaté à la première génération, retiré.
# Le devanagari sert aussi le hindi et le marathi ; dans CE dépôt il ne porte
# que du sanskrit, mais c'est un fait de corpus et non de l'écriture : la
# provenance est donc toujours déclarée avec la valeur.
ECRITURES_LANGUE = (("ARABIC", "arabe"), ("HEBREW", "hebreu"),
                    ("DEVANAGARI", "sanskrit"),
                    ("HIRAGANA", "japonais"), ("KATAKANA", "japonais"),
                    ("GREEK", "grec"), ("SYRIAC", "syriaque"))

LANGUES_NOMMEES = ("sanskrit", "arabe", "hebreu", "grec", "latin", "japonais",
                   "chinois", "persan", "arameen", "tibetain", "pali",
                   "avestique", "syriaque")

RE_LANGUE_PROSE = re.compile(
    r"\*\*([^*\n]{2,40})\*\*\s*\(\s*(%s)\s*[:,]"
    % "|".join(LANGUES_NOMMEES).replace("hebreu", "h[ée]breu")
                               .replace("arameen", "aram[ée]en")
                               .replace("tibetain", "tib[ée]tain"),
    re.IGNORECASE)


def langue_de_lecriture(txt: str):
    """Langue déduite de l'ÉCRITURE — déterministe, jamais devinée."""
    for c in txt:
        try:
            nom = unicodedata.name(c)
        except ValueError:
            continue
        for prefixe, langue in ECRITURES_LANGUE:
            if nom.startswith(prefixe):
                return langue
    return None


def langue_par_terme(racine: Path, index: Index, rapport: dict):
    """Pose `langue`, avec sa PROVENANCE, sur trois sources et jamais autrement.

      1. `original:` du Sceau de la fiche dont le slug EST le terme — la forme
         y est déclarée par Sidy, l'écriture donne la langue. Source la plus
         forte, et celle qui grandira.
      2. La langue ÉNONCÉE en prose : « **Buddhi** (Sanskrit : बुद्धि) ».
      3. L'écriture de la forme appariée (`apparie`, rang 1) ou de la forme
         originale que Jurjānī donne (`jurjani`, rang 2).

    Aucune quatrième voie. En particulier, PAS de déduction depuis la graphie
    de la translittération (`al-`, `ḥ`, `ṣ`) : ce serait une heuristique
    d'orthographe, et une heuristique n'est pas une source (Cmd 5).
    """
    par_original = {}
    base = racine / "doctrinal"
    if base.is_dir():
        for f in base.rglob("*.md"):
            try:
                fm = lire_frontmatter(f.read_text(encoding="utf-8"))
            except OSError:
                continue
            brut = str(fm.get("original", "")).strip()
            if not brut or "to-original" in brut.lower():
                continue
            lg = langue_de_lecriture(brut)
            if lg:
                par_original[slug_de(f)] = (lg, str(f.relative_to(racine)))

    prose = defaultdict(set)
    # Les DOCUMENTS DE GOUVERNANCE sont exclus de la lecture. Un protocole, un
    # journal ou un changelog qui écrit « **Buddhi** (Sanskrit : बुद्धि) » le
    # fait à titre d'EXEMPLE : il ne source rien, il illustre une règle.
    # Constaté le 2026-09-09 — `buddhi` citait `atelier/annales.md` et
    # `meta/protocole-archives/changelog-CLAUDE.md` parmi ses sources de langue,
    # c'est-à-dire des textes que cette même session venait d'écrire. C'est le
    # piège de l'auto-référence, déjà rencontré deux fois : le marqueur
    # d'insertion cité en prose, et la convention d'annotation citée en prose.
    GOUVERNANCE = ("meta/protocole-archives/",)
    for circuit in CIRCUITS:
        b = racine / circuit
        if not b.is_dir():
            continue
        for f in b.rglob("*.md"):
            rel_f = str(f.relative_to(racine))
            if f.name in EXCLUS or rel_f.startswith(GOUVERNANCE):
                continue
            try:
                txt = f.read_text(encoding="utf-8")
            except OSError:
                continue
            for terme, lg in RE_LANGUE_PROSE.findall(txt):
                prose[normaliser(terme)].add(
                    (lg.lower().replace("é", "e"), str(f.relative_to(racine))))

    n = Counter()
    for cle, e in index.termes.items():
        if cle in par_original:
            lg, src = par_original[cle]
            e["langue"] = {"langue": lg, "provenance": "sceau-original",
                           "source": [src]}
            n["sceau-original"] += 1
            continue
        p = prose.get(cle)
        if p and len({x[0] for x in p}) == 1:
            lg = next(iter(p))[0]
            e["langue"] = {"langue": lg, "provenance": "prose",
                           "source": sorted(x[1] for x in p)}
            n["prose"] += 1
            continue
        forme = None
        if e["apparie"]:
            forme = sorted(e["apparie"])[0]
        elif e["jurjani"] and e["jurjani"].get("original"):
            forme = e["jurjani"]["original"]
        elif e["jurjani"] and e["jurjani"].get("translit"):
            # Le Kitāb al-Taʿrīfāt est un lexique de la langue arabe : un terme
            # qui y a son entrée est arabe, et le numéro de définition le source.
            e["langue"] = {"langue": "arabe", "provenance": "jurjani",
                           "source": ["definition " + e["jurjani"]["definition"]]}
            n["jurjani"] += 1
            continue
        if forme:
            lg = langue_de_lecriture(forme)
            if lg:
                e["langue"] = {"langue": lg, "provenance": "forme-appariee",
                               "source": [forme]}
                n["forme-appariee"] += 1
    rapport["langue_posee"] = dict(n)


def tradition_par_terme(racine: Path, index: Index, rapport: dict):
    """Tradition d'un terme, SOURCÉE par la fiche qui le DÉFINIT.

    Distinction décisive, mesurée le 2026-09-09. Compter les `tradition_cadre`
    de toutes les fiches qui MENTIONNENT un terme est un vote, et un vote n'est
    pas une source (Cmd 5) : `barzakh` y donnerait islam 36 / universel 12 /
    kabbale 2, parce que `tradition_cadre` décrit LE CADRE DE LA FICHE et non
    l'origine du terme — les fiches comparatives portent `universel` tout en
    citant des termes de partout.

    Ne sont donc retenues que les fiches qui **traitent** le terme : celles où
    il porte le rôle `definition` (amorce `**Terme** :`) ou `titre` (il est le
    sujet du `title:`/H1). Une fiche qui définit un terme déclare le cadre dans
    lequel elle le définit : c'est une assertion sourcée, citable, et non un
    décompte.

    Le champ n'est posé que sur UNANIMITÉ des fiches traitantes. Divergence =
    pas de champ, et le désaccord est rapporté : deux fiches qui définissent un
    même terme sous deux cadres différents posent une question doctrinale, que
    la machine signale et ne tranche pas (Cmd 12).
    """
    trad_fiche = {}
    base = racine / "doctrinal"
    if base.is_dir():
        for f in base.rglob("*.md"):
            try:
                fm = lire_frontmatter(f.read_text(encoding="utf-8"))
            except OSError:
                continue
            t = str(fm.get("tradition_cadre", "")).strip().strip('"')
            if t and not t.startswith("["):
                trad_fiche[str(f.relative_to(racine))] = t

    # Traditions RATIFIÉES par Sidy — la source est le verdict, non un
    # décompte. Elles priment toute dérivation, et sont marquées comme telles.
    ratifiees = {}
    f_rat = racine / "atelier/rd/outillage/index-lexical/traditions-ratifiees.json"
    if f_rat.is_file():
        try:
            bloc = json.loads(f_rat.read_text(encoding="utf-8"))
            ratifiees = bloc.get("ratifie", {})
            rapport["traditions_ratifiees"] = len(ratifiees)
        except (OSError, json.JSONDecodeError):
            refus(f"table de ratification illisible : {f_rat}")

    n_pose = 0
    divergents = {}
    for cle, cadre in ratifiees.items():
        if cle in index.termes:
            index.termes[cle]["tradition"] = {
                "cadre": cadre, "degre": "ratifie-sidy",
                "source": ["verdict Sidy 2026-09-09"]}
            n_pose += 1
    for cle, e in index.termes.items():
        if e["tradition"]:
            continue                       # ratifiée : le verdict prime
        # Deux degrés de source, le premier primant absolument sur le second.
        #  1. La fiche DONT LE SLUG EST LE TERME : elle a le terme pour sujet,
        #     sans ambiguïté possible. C'est la source la plus forte.
        #  2. À défaut, les fiches qui le DÉFINISSENT en prose (amorce
        #     `**Terme** :`, rôle `definition`).
        # Le rôle `titre` a d'abord été admis, puis RETIRÉ : il se pose dès que
        # le terme est composant du slug, si bien que les soixante fiches
        # `guenon-*.md` « traitaient » de `guenon` et faisaient diverger le
        # cadre. Un signal trop large ne mesure plus ce qu'on lui demande.
        propres = {rel: trad_fiche[rel] for rel in e["fiches"]
                   if rel in trad_fiche and slug_de(Path(rel)) == cle}
        traitantes = propres or {
            rel: trad_fiche[rel]
            for rel, v in e["fiches"].items()
            if rel in trad_fiche and "definition" in v["roles"]
        }
        if not traitantes:
            continue
        cadres = set(traitantes.values())
        if len(cadres) == 1:
            e["tradition"] = {"cadre": cadres.pop(),
                              "source": sorted(traitantes),
                              "degre": "fiche-propre" if propres else "definition"}
            n_pose += 1
        else:
            divergents[cle] = {r: t for r, t in sorted(traitantes.items())}
    rapport["tradition_posee"] = n_pose
    rapport["tradition_divergente"] = divergents


def apparier_jurjani(index: Index, racine: Path, rapport: dict):
    """Rang 2 — pose le champ `jurjani`, dans les deux sens quand c'est possible.

    Ne touche JAMAIS `apparie` (rang 1), et ne s'applique qu'aux clés que le
    rang 1 n'a pas déjà appariées : une paire que la fiche énonce elle-même
    prime toute autorité extérieure.
    """
    dico = charger_jurjani(racine)
    rapport["jurjani_entrees"] = len(dico)
    n_orig = n_retour = 0
    for cle, e in list(index.termes.items()):
        if e["apparie"] or not est_ecriture_originale(cle):
            continue
        trouve = dico.get(cle)
        if not trouve:
            continue
        num, lat, forme_ar = trouve
        e["jurjani"] = {"translit": lat, "definition": num}
        n_orig += 1
        # Réciprocité (§VII, point 6) : la forme latine reçoit le renvoi
        # inverse — mais SEULEMENT si elle est déjà une clé de l'index. On
        # n'injecte pas le vocabulaire du dictionnaire dans un index qui est
        # celui du DÉPÔT : ce serait indexer Jurjānī, non le wiki.
        cle_lat = normaliser(lat)
        if cle_lat in index.termes and not index.termes[cle_lat]["apparie"]:
            index.termes[cle_lat]["jurjani"] = {"original": forme_ar,
                                                "definition": num}
            n_retour += 1
    rapport["jurjani_apparies"] = n_orig
    rapport["jurjani_reciproques"] = n_retour


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
            # Sources d'appariement : le `title:` et le H1 SEULEMENT — le
            # site que le §VII, point 3, déclare canonique. Les H2 y ont été
            # essayés puis RETIRÉS le 2026-09-08 : ce sont des intertitres de
            # section, et ils ont produit `systeme` ↔ `α` depuis
            # « ... — système (α) ». La forme à barre oblique
            # (« chikai to seiyaku / 誓約と制約 ») a été essayée et retirée de
            # même : aucune paire vraie, et c'est d'ailleurs une paire de
            # SYNTAGMES, que cet index — dont les clés sont des tokens — ne peut
            # structurellement pas porter. Limitation rapportée, non contournée.
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
            "jurjani": e["jurjani"],
            "tradition": e["tradition"],
            "langue": e["langue"],
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
         ">",
         "> Colonne *cadre / langue* : **✓** = cadre lu sur la fiche qui a le",
         "> terme pour sujet · **⚖** = cadre **ratifie par verdict**, non mesure",
         "> · *italique* = langue du terme. Les deux axes sont distincts : la",
         "> tradition est le cadre ou l on cite, la langue une propriete du",
         "> terme (CLAUDE.md §VII, verdict Sidy 2026-09-09).",
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
              "| terme | formes attestees | appariement | cadre / langue |"
              " roles | fiches | textes/ | occ. |",
              "|---|---|---|---|---|---|---|---|"]
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
            # Colonne d'appariement — les deux rangs y sont LISIBLEMENT
            # distincts : le rang 1 (attesté par la fiche) est nu, le rang 2
            # porte le sigle de son autorité et son numéro de définition. Un
            # lecteur ne doit jamais avoir à deviner d'où vient une paire.
            if e["apparie"]:
                app = " · ".join(f"`{x}`" for x in e["apparie"])
            elif e.get("jurjani"):
                j = e["jurjani"]
                forme = j.get("translit") or j.get("original")
                app = f"`{forme}` — Jurjānī déf. {j['definition']}"
            else:
                app = "—"
            # Colonne des deux axes. La PROVENANCE est rendue visible : un
            # cadre ratifié par verdict et un cadre lu sur la fiche du terme
            # n'ont pas la même force, et le lecteur doit le voir sans avoir à
            # ouvrir le JSON.
            axes = []
            if e.get("tradition"):
                t = e["tradition"]
                marque = "✓" if t["degre"] == "fiche-propre" else "⚖"
                axes.append(f"{marque} {t['cadre']}")
            if e.get("langue"):
                axes.append(f"*{e['langue']['langue']}*")
            L.append(f"| `{cle}` | {formes} | {app} | {' · '.join(axes) or '—'} "
                     f"| {', '.join(e['roles'])} | "
                     f"{' · '.join(fiches) or '—'} | {textes} | "
                     f"{e['occurrences']} |")
        L.append("")
    return "\n".join(L) + "\n"


def rendre_md_eclate(data: dict, dossier: Path, max_renvois: int = 5) -> int:
    """Écrit le condensé ÉCLATÉ : un hub + un fichier par initiale.

    Motif mesuré : le condensé d'un seul tenant pesait 1,2 Mo, ce qui est
    hostile à Obsidian sur iPad — or la consultation Obsidian est l'un des deux
    consommateurs déclarés du chantier. Éclater ne change rien au contenu :
    c'est le même rendu, découpé sur la même frontière (l'initiale) que le
    fichier unique employait déjà pour ses sections.

    Tous les fichiers produits portent `type: artefact-derive` : l'index ne
    s'indexe pas lui-même.
    """
    dossier.mkdir(parents=True, exist_ok=True)
    entier = rendre_md(data, max_renvois)
    tete, _, reste = entier.partition("\n## ")
    sections = ("## " + reste).split("\n## ") if reste else []
    sections = [s if s.startswith("## ") else "## " + s for s in sections]

    def _fm(titre: str) -> str:
        return ("---\n"
                f'title: "{titre}"\n'
                "type: artefact-derive\n"
                "tags: [index-lexical, artefact-derive]\n"
                f"created: {date.today().isoformat()}\n"
                f"updated: {date.today().isoformat()}\n"
                "sources: []\n"
                "links: []\n"
                "---\n\n")

    def _nom(initiale: str) -> str:
        c = initiale.strip("# ").strip()[:1]
        if c.isascii() and c.isalpha():
            return c.lower()
        if c.isdigit() or c == "#":
            return "chiffres-et-symboles"
        return "ecritures-originales"

    groupes: dict[str, list[str]] = {}
    for sec in sections:
        groupes.setdefault(_nom(sec.splitlines()[0]), []).append(sec)

    ecrits = 0
    for nom, secs in sorted(groupes.items()):
        cible = dossier / f"{nom}.md"
        cible.write_text(_fm(f"Index lexical — {nom}") + "\n".join(secs),
                         encoding="utf-8")
        ecrits += 1

    lignes = [_fm("Index lexical — hub du condensé éclaté").rstrip("\n"), "",
              "# Index lexical — hub", "",
              "> Condensé **éclaté par initiale**. Le contenu est identique au",
              "> rendu d'un seul tenant ; seul le découpage change, sur la même",
              "> frontière que les sections employaient déjà. L'index intégral",
              "> reste `index-lexical.json` (outil MCP `chercher_terme`).", ""]
    t = data.get("totaux", {})
    lignes += [f"**Termes distincts : {t.get('termes')} — occurrences : "
               f"{t.get('occurrences')} — fiches indexees : "
               f"{t.get('fiches_indexees')} — textes balayes : "
               f"{t.get('textes_balayes')}**", "", "## Tranches", ""]
    for nom in sorted(groupes):
        lignes.append(f"- [[atelier/rd/outillage/index-lexical/condense/{nom}]]")
    (dossier / "hub.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return ecrits + 1


def main():
    ap = argparse.ArgumentParser(description="Index lexical du depot.")
    ap.add_argument("--racine", default="/root/wiki")
    ap.add_argument("--sortie-json", default="")
    ap.add_argument("--sortie-md", default="")
    ap.add_argument("--sortie-md-eclate", default="",
                    help="dossier du condense ECLATE (un fichier par initiale)")
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
    # Après le filtre des étiquettes (une clé déclassée ne doit pas recevoir de
    # renvoi Jurjānī) et avant le comptage, qui ne touche pas aux appariements.
    tradition_par_terme(racine, index, rapport)
    langue_par_terme(racine, index, rapport)
    apparier_jurjani(index, racine, rapport)
    compter(racine, index, rapport, avec_textes, suivis)
    controler(index, rapport, avec_textes)

    data = serialiser(index, rapport, avec_textes)
    sortie_json.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    sortie_md.write_text(rendre_md(data), encoding="utf-8")
    if args.sortie_md_eclate:
        n = rendre_md_eclate(data, Path(args.sortie_md_eclate))
        print(f"  \u2192 {args.sortie_md_eclate} ({n} fichiers)")

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
