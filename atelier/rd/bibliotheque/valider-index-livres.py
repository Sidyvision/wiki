#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validation mecanique des fiches `type: index-livre`.

Lignee `carte-du-depot.py` : DETERMINISTE (stdlib seule, aucun LLM, aucun
reseau, relances octet-identiques) / LECTURE SEULE (n'ecrit jamais dans le
depot) / AUCUN JUGEMENT (constate et compte, ne resume ni ne qualifie) /
ARTEFACT DERIVE (le depot fait foi) / HORS CORPS DOCTRINAL.

Sortie brute, une ligne par anomalie. Code de retour non nul si bloquant.
Substitue le script `compare` : son objet (comparer le declare au reel dans
`_inbox/`) est ici la verification des fiches d'index deposees au sas.
"""

import argparse
import os
import re
import sys
import unicodedata

# --- Cmd 15 : points de code interdits, et EUX SEULS. -----------------------
# Les diacritiques combinantes (translitteration sanskrite : r-point, s-aigu,
# a-macron...) sont LEGITIMES. Un filtre "non-ASCII" naif les detruirait.
INTERDITS = {
    chr(0x200B): "U+200B ZERO WIDTH SPACE",
    chr(0x200C): "U+200C ZERO WIDTH NON-JOINER",
    chr(0x200D): "U+200D ZERO WIDTH JOINER",
    chr(0x200E): "U+200E LEFT-TO-RIGHT MARK",
    chr(0x200F): "U+200F RIGHT-TO-LEFT MARK",
}
# Les points de code sont declares par `chr()` et jamais ecrits en clair :
# un validateur qui contient litteralement ce qu'il interdit se declenche
# sur lui-meme (piege connu du depot).
BOM = chr(0xFEFF)

CLES_REQUISES = ["title", "type", "livre", "nature", "dossier_raw",
                 "photos_source", "pages_couvertes", "created", "updated"]
# `dossier_raw` est REQUIS : sans lui le controle H1 (photo declaree vs photo
# reelle) ne s'arme pas et la validation echoue en silence (fail-open).
NATURES = {"index_rerum", "index_nominum", "glossaire", "table"}
RE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_PAGES = re.compile(r"^(\d+)\s*[-–]\s*(\d+)$")
RE_IMG = re.compile(r"^IMG_(\d{4})$")
ENTETE_ATTENDUE = ["terme_ar", "terme_translit", "terme_fr", "pages"]
# Renvoi de page tel qu'IMPRIME, jamais normalise : un nombre, eventuellement
# suivi d'une lettre de colonne ou d'appareil (a, b, n...), une plage, ou une
# forme prefixee (`st. 12`). Volontairement large — voir T5.
RE_RENVOI = re.compile(
    r"^(st\.?\s*)?\d+\s*[a-z]?(\s*[-–]\s*\d+\s*[a-z]?)?$", re.IGNORECASE)


class Rapport:
    def __init__(self):
        self.bloquantes = 0
        self.signalements = 0

    def bloque(self, fiche, code, msg):
        self.bloquantes += 1
        print("BLOQUANT  %-40s %-4s %s" % (fiche, code, msg))

    def signale(self, fiche, code, msg):
        self.signalements += 1
        print("SIGNAL    %-40s %-4s %s" % (fiche, code, msg))


def lire_frontmatter(texte):
    """Parse minimal du frontmatter YALM plat (cle: valeur, listes inline)."""
    if not texte.startswith("---"):
        return None, texte
    fin = texte.find("\n---", 3)
    if fin == -1:
        return None, texte
    brut = texte[3:fin]
    corps = texte[fin + 4:]
    fm = {}
    for ligne in brut.splitlines():
        if not ligne.strip() or ligne.lstrip().startswith("#"):
            continue
        if ":" not in ligne:
            continue
        cle, _, val = ligne.partition(":")
        fm[cle.strip()] = val.strip()
    return fm, corps


def liste_yaml(val):
    val = val.strip()
    if not (val.startswith("[") and val.endswith("]")):
        return None
    dedans = val[1:-1].strip()
    if not dedans:
        return []
    return [e.strip().strip('"').strip("'") for e in dedans.split(",")]


def controle_unicode(rap, fiche, texte):
    """U1 — points de code interdits. Bloquant. Cmd 15."""
    for num, ligne in enumerate(texte.splitlines(), 1):
        for car, nom in INTERDITS.items():
            if car in ligne:
                col = ligne.index(car) + 1
                rap.bloque(fiche, "U1",
                           "l.%d c.%d : %s interdit (Cmd 15)" % (num, col, nom))
    # BOM tolere en tete de fichier uniquement, jamais au milieu.
    if BOM in texte[1:]:
        rap.bloque(fiche, "U2", "U+FEFF present hors tete de fichier (Cmd 15)")


def controle_frontmatter(rap, fiche, fm):
    if fm is None:
        rap.bloque(fiche, "F0", "aucun frontmatter delimite par `---`")
        return
    for cle in CLES_REQUISES:
        if cle not in fm:
            rap.bloque(fiche, "F1", "cle manquante : `%s`" % cle)
    if fm.get("type") != "index-livre":
        rap.bloque(fiche, "F2",
                   "type attendu `index-livre`, trouve `%s`" % fm.get("type"))
    nat = fm.get("nature", "")
    if nat and nat not in NATURES:
        rap.bloque(fiche, "F3", "nature hors nomenclature : `%s`" % nat)
    for cle in ("created", "updated"):
        v = fm.get(cle, "")
        if v and not RE_DATE.match(v):
            rap.bloque(fiche, "F4", "%s non conforme YYYY-MM-DD : `%s`" % (cle, v))
    # Champ de jugement : sa presence est une faute de conception.
    if "completude" in fm:
        rap.bloque(fiche, "F5",
                   "champ `completude` interdit : la contiguite est calculee, "
                   "non jugee (principe Aucun jugement)")


def controle_pages(rap, fiche, fm):
    """P1/P2 — pages_couvertes numerique et croissante. Bloquant."""
    v = fm.get("pages_couvertes", "") if fm else ""
    if not v:
        return
    m = RE_PAGES.match(v.strip().strip('"'))
    if not m:
        rap.bloque(fiche, "P1",
                   "pages_couvertes non numerique (attendu `debut-fin`) : `%s`" % v)
        return
    a, b = int(m.group(1)), int(m.group(2))
    if b < a:
        rap.bloque(fiche, "P2", "pages_couvertes decroissant : %d-%d" % (a, b))


def controle_photos(rap, fiche, fm, racine_raw):
    """H1 bloquant (photo declaree absente) / H2 signalement (trou de serie).

    La contiguite est DERIVEE ici, jamais declaree par l'agent.
    """
    if not fm:
        return
    photos = liste_yaml(fm.get("photos_source", ""))
    if photos is None:
        rap.bloque(fiche, "H0",
                   "photos_source n'est pas une liste YAML inline `[\"...\"]`")
        return
    if not photos:
        rap.signale(fiche, "H3", "photos_source vide")
        return
    dossier = fm.get("dossier_raw", "").strip().strip('"')
    if dossier and racine_raw:
        chemin = os.path.join(racine_raw, dossier)
        if os.path.isdir(chemin):
            presents = set()
            for nom in os.listdir(chemin):
                presents.add(os.path.splitext(nom)[0])
            for p in photos:
                if p not in presents:
                    rap.bloque(fiche, "H1",
                               "photo declaree absente du dossier : %s" % p)
        else:
            rap.signale(fiche, "H4", "dossier_raw introuvable : %s" % dossier)
    nums = []
    for p in photos:
        m = RE_IMG.match(p)
        if not m:
            rap.signale(fiche, "H5", "nom de photo hors format IMG_NNNN : %s" % p)
        else:
            nums.append(int(m.group(1)))
    if len(nums) >= 2:
        nums.sort()
        trous = []
        for i in range(len(nums) - 1):
            ecart = nums[i + 1] - nums[i]
            # Le compteur de l'appareil peut reboucler (9999 -> 0001) : on ne
            # signale que les ecarts internes plausibles, jamais le rebouclage.
            if 1 < ecart <= 100:
                trous.append("%04d..%04d" % (nums[i] + 1, nums[i + 1] - 1))
        if trous:
            rap.signale(fiche, "H2",
                        "trou(s) de serie : %s (constat, non corrige)" % ", ".join(trous))


def controle_table(rap, fiche, corps):
    """T1 entete exacte (bloquant) / T2 doublons (signalement, jamais fusionnes)
    / T3 melange de scripts dans une meme cellule (bloquant, prevention Cmd 15).
    """
    lignes = [l for l in corps.splitlines() if l.strip().startswith("|")]
    if not lignes:
        rap.bloque(fiche, "T0", "aucune table trouvee dans le corps")
        return
    entete = [c.strip() for c in lignes[0].strip().strip("|").split("|")]
    if entete != ENTETE_ATTENDUE:
        rap.bloque(fiche, "T1",
                   "entete attendue %s, trouvee %s" % (ENTETE_ATTENDUE, entete))
        return
    vus = {}
    for num, ligne in enumerate(lignes[2:], 1):
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) != 4:
            rap.bloque(fiche, "T4",
                       "ligne %d : %d cellules au lieu de 4" % (num, len(cellules)))
            continue
        ar, translit, fr, pages = cellules
        # T3 — arabe et latin ne partagent jamais une cellule. C'est la cause
        # mecanique des marques bidi : on l'empeche par construction.
        for idx, cel in enumerate(cellules[:3]):
            if melange_scripts(cel):
                rap.bloque(fiche, "T3",
                           "ligne %d colonne %s : arabe et latin dans une meme "
                           "cellule (cause des marques bidi, Cmd 15)"
                           % (num, ENTETE_ATTENDUE[idx]))
        if pages and pages != "to-verify":
            for morceau in re.split(r"[,;]", pages):
                morceau = morceau.strip()
                if not morceau:
                    continue
                if not RE_RENVOI.match(morceau):
                    # T5 est un SIGNALEMENT, jamais un bloquant. Chaque ouvrage
                    # a sa convention de renvoi (Langlois : `110 b` page+colonne,
                    # `178 n` note, `st. 12` stance) et un motif construit sur
                    # les trois formes deja vues serait trop serre : il
                    # detruirait la source une seconde fois. La convention se
                    # declare verbatim en frontmatter `convention_pages` et
                    # c'est elle, non ce motif, qui porte le sens au lecteur.
                    # Un controle bloquant qu'il faut desserrer a chaque
                    # ouvrage n'est pas un controle.
                    rap.signale(fiche, "T5",
                                "ligne %d : renvoi hors formes connues `%s` "
                                "(constat ; cf. `convention_pages`)" % (num, morceau))
        cle = (translit or fr or ar).lower()
        if cle:
            vus.setdefault(cle, []).append(num)
    for cle, lignes_vues in sorted(vus.items()):
        if len(lignes_vues) > 1:
            rap.signale(fiche, "T2",
                        "terme en doublon `%s` lignes %s (signale, JAMAIS fusionne "
                        "d'autorite)" % (cle, lignes_vues))


def melange_scripts(texte):
    arabe = latin = False
    for car in texte:
        if unicodedata.combining(car) or not car.isalpha():
            continue
        nom = unicodedata.name(car, "")
        if nom.startswith("ARABIC"):
            arabe = True
        elif nom.startswith("LATIN"):
            latin = True
    return arabe and latin


def compte_to_verify(corps):
    return corps.count("to-verify")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dossier", default=os.path.dirname(os.path.abspath(__file__)),
                    help="dossier contenant les fiches index-*.md")
    # Defaut resolu vers le `raw/` du depot : le controle H1 doit s'armer
    # aussi quand l'appelant (generateur, shim) ne passe pas l'option.
    _defaut_raw = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))), "raw")
    ap.add_argument("--raw", default=_defaut_raw,
                    help="racine des dossiers de photographies (defaut : %s)" % _defaut_raw)
    args = ap.parse_args()

    fiches = sorted(f for f in os.listdir(args.dossier)
                    if f.startswith("index-") and f.endswith(".md"))
    rap = Rapport()
    print("valider-index-livres — %d fiche(s) examinee(s)" % len(fiches))
    print("-" * 72)
    for nom in fiches:
        chemin = os.path.join(args.dossier, nom)
        with open(chemin, encoding="utf-8") as fh:
            texte = fh.read()
        controle_unicode(rap, nom, texte)
        fm, corps = lire_frontmatter(texte)
        controle_frontmatter(rap, nom, fm)
        controle_pages(rap, nom, fm)
        controle_photos(rap, nom, fm, args.raw)
        controle_table(rap, nom, corps)
        n = compte_to_verify(corps)
        if n:
            rap.signale(nom, "V1", "%d cellule(s) `to-verify` en attente de Sidy" % n)
    print("-" * 72)
    print("bloquantes: %d | signalements: %d" % (rap.bloquantes, rap.signalements))
    return 1 if rap.bloquantes else 0


if __name__ == "__main__":
    sys.exit(main())
