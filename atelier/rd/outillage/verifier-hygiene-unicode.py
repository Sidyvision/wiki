#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier-hygiene-unicode.py — contrôle mécanique du Cmd 15 (hygiène Unicode).

Motif d'ouverture. Le Cmd 15 interdit d'introduire dans le dépôt des caractères
invisibles. Jusqu'au 2026-09-14 il était le seul commandement SANS contrôle :
`verifier-invariants.py` n'en portait aucune trace. Trois récidives en trois
semaines l'ont établi (2026-08-22 contamination ZWJ, 2026-09-07 commentaire de
code, 2026-09-14 deux fois dans une même session). Le constat généralisable est
consigné en `atelier/rd/incidents/` : **un constat consigné en prose récidive ;
un constat institué en contrôle ne récidive pas.**

DÉTERMINISTE, sans LLM, sans réseau. Ne corrige rien : il constate.

Périmètre — TOUS les fichiers suivis par git, pas les seuls `.md`. La troisième
récidive était dans un `.py` ; un contrôle restreint au markdown ne l'aurait pas
vue. Les fichiers binaires ou non décodables en UTF-8 sont ignorés et comptés.

Discipline d'écriture de cet instrument, et raison de son épreuve : les
codepoints surveillés ne sont JAMAIS écrits en caractères littéraux, seulement
en entiers hexadécimaux. La deuxième récidive du 2026-09-14 venait précisément
d'avoir écrit des bornes d'intervalle en caractères littéraux dans un script —
l'instrument devenait porteur de ce qu'il traquait. Corollaire vérifiable :
**cet instrument doit se scanner lui-même sans se déclencher.** C'est l'épreuve
E4 de `eprouver-hygiene-unicode.py`.

Trois classes, rapportées SÉPARÉMENT et jamais fondues (Cmd 12) :

  [1] VIOLATION Cmd 15 — le jeu nommé par le commandement, et lui seul.
      Seule classe bloquante (code de sortie 1).
  [2] SIGNALEMENT bidi — contrôles d'enrobage directionnel. HORS Cmd 15.
      Légitimes dans un texte arabe brut, illégitimes dans du code. Le dépôt a
      déjà tranché que la frontière du Cmd 15 ne se franchit pas dans un
      instrument (cf. E1d de `eprouver-mesure-ocr-arabe.py`) : ils se comptent
      à part et ne font jamais échouer.
  [3] SIGNALEMENT mise en page — saut de page, tabulation verticale. HORS
      Cmd 15. Résidus de `pdftotext`. Motif : un saut de page a faussé trois
      fois un comptage de chapitres le 2026-09-14, et le nombre faux était
      stable — donc crédible. Non bloquant.

Registre des exceptions déclarées (ouvert 2026-09-14, verdict de Sidy, OUT-16).
`config/hygiene-unicode-exceptions.yaml` porte les résidus déjà tranchés, chacun
avec son motif et le renvoi à la fiche qui l'a tranché. Motif : un résidu connu
et motivé, rapporté indéfiniment comme violation, transforme le contrôle en
bruit, et un contrôle bruyant cesse d'être lu — c'est ce qui s'est produit dans
OUT-C2. L'instrument ne rend ici aucun verdict : il en porte un déjà rendu.

Le garde-fou en est la clause portante. Une exception couvre un compte EXACT,
jamais un fichier en bloc : ce qui dépasse le compte déclaré reste bloquant,
une exception sans objet est signalée caduque, et `--sans-exceptions` restitue
l'état brut. Sans quoi une exception absorberait en silence toute contamination
ultérieure du même fichier — soit une qualification implicite rendue sans être
avouée, la faute même que consigne
`atelier/rd/incidents/2026-09-14_amortissement-constat-doctrinal-traduction-ihya.md`.
Éprouvé par l'échec en E7-E10.

Portée et limite, énoncée pour n'être pas surestimée : cet instrument balaye le
dépôt. Or les invisibles qui faussent les MESURES agissent dans des fichiers de
travail hors dépôt (`/tmp`), que ce contrôle ne voit pas. Il est nécessaire, il
n'est pas suffisant ; la parade pour les mesures est la cinquième clause de la
fiche d'incident, qui porte sur l'inspection des octets avant tout comptage.

Usage :
    python3 verifier-hygiene-unicode.py [--racine .] [--tout] [--json]
                                        [--strict] [chemin ...]

Codes de sortie :
    0  aucune violation du Cmd 15
    1  au moins une violation du Cmd 15 (ou, avec --strict, un signalement)
    2  erreur d'exécution de l'instrument lui-même
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Les jeux surveillés. ENTIERS SEULEMENT — aucun caractère littéral ici.
# ---------------------------------------------------------------------------

# [1] Le jeu nommé par le Cmd 15, dans sa lettre exacte. Ni plus, ni moins.
CMD15 = {
    0x200B: "U+200B ZERO WIDTH SPACE",
    0x200C: "U+200C ZERO WIDTH NON-JOINER",
    0x200D: "U+200D ZERO WIDTH JOINER",
    0xFEFF: "U+FEFF ZERO WIDTH NO-BREAK SPACE (BOM)",
    0x200E: "U+200E LEFT-TO-RIGHT MARK",
    0x200F: "U+200F RIGHT-TO-LEFT MARK",
}

# [2] Enrobage bidi — HORS Cmd 15, compté à part, jamais ajouté au compte ci-dessus.
BIDI = {
    0x202A: "U+202A LEFT-TO-RIGHT EMBEDDING",
    0x202B: "U+202B RIGHT-TO-LEFT EMBEDDING",
    0x202C: "U+202C POP DIRECTIONAL FORMATTING",
    0x202D: "U+202D LEFT-TO-RIGHT OVERRIDE",
    0x202E: "U+202E RIGHT-TO-LEFT OVERRIDE",
    0x2066: "U+2066 LEFT-TO-RIGHT ISOLATE",
    0x2067: "U+2067 RIGHT-TO-LEFT ISOLATE",
    0x2068: "U+2068 FIRST STRONG ISOLATE",
    0x2069: "U+2069 POP DIRECTIONAL ISOLATE",
}

# [3] Mise en page — HORS Cmd 15. Résidus d'extraction PDF.
MISE_EN_PAGE = {
    0x000C: "U+000C FORM FEED (saut de page pdftotext)",
    0x000B: "U+000B LINE TABULATION",
}

CLASSES = (
    ("cmd15", "VIOLATION Cmd 15", CMD15, True),
    ("bidi", "SIGNALEMENT bidi (hors Cmd 15)", BIDI, False),
    ("mise_en_page", "SIGNALEMENT mise en page (hors Cmd 15)", MISE_EN_PAGE, False),
)

DOSSIERS_EXCLUS = {".git", "node_modules", "_inbox"}

EXCEPTIONS_DEFAUT = Path(__file__).resolve().parent / "config" / "hygiene-unicode-exceptions.yaml"


def charger_exceptions(chemin):
    """Charge le registre des exceptions déclarées.

    Ce registre porte des verdicts DÉJÀ rendus et consignés ; l'instrument ne
    s'en sert que pour ne pas rapporter indéfiniment un résidu tranché. Il n'y
    ajoute jamais rien de lui-même (Cmd 12).
    """
    if chemin is None or not Path(chemin).is_file():
        return [], None
    try:
        import yaml
    except ImportError:
        raise RuntimeError(
            "pyyaml absent : impossible de lire le registre d'exceptions. "
            "Relancer avec --sans-exceptions pour l'état brut.")
    d = yaml.safe_load(Path(chemin).read_text(encoding="utf-8")) or {}
    return list(d.get("exceptions") or []), str(chemin)


def appliquer_exceptions(violations, exceptions, perimetre=None):
    """Répartit les violations Cmd 15 entre bloquantes, honorées et excédents.

    Règle du garde-fou, et c'est tout l'enjeu : une exception couvre un compte
    EXACT, jamais un fichier en bloc. Ce qui dépasse le compte déclaré reste
    bloquant — sans quoi une exception absorberait en silence toute
    contamination ultérieure du même fichier, ce qui serait une qualification
    implicite rendue sans être avouée.

    Caducité et périmètre — défaut relevé le 2026-09-18. Zéro occurrence
    observée ne veut dire « exception périmée » QUE si le fichier a
    effectivement été lu. Sur un périmètre partiel — le cas de TOUS les appels
    du hook `pre-commit`, qui ne passe que les chemins indexés —, un fichier
    non lu rendait zéro, et son exception était déclarée caduque à chaque
    commit : un rapport vrai sur un périmètre faux, la famille d'`OUT-16` et
    d'`OUT-18`. Le registre le plus soigneusement tenu se serait mis à mentir
    par la seule répétition du signal. `perimetre` (ensemble des chemins
    réellement lus, relatifs à la racine) lève l'ambiguïté ; à None, le
    comportement d'avant est conservé.

    Retourne (bloquantes, honorees, excedents, caduques, hors_perimetre).
    """
    par_cle = {}
    for v in violations:
        cle = (v["fichier"], v["codepoint"].split()[0])
        par_cle.setdefault(cle, []).append(v)

    bloquantes, honorees, excedents, caduques, hors_perimetre = [], [], [], [], []
    consommees = set()

    for i, exc in enumerate(exceptions):
        cle = (exc.get("fichier"), exc.get("codepoint"))
        declare = int(exc.get("occurrences", 0))
        observees = par_cle.get(cle, [])
        consommees.add(cle)
        n = len(observees)
        if n == 0:
            if perimetre is not None and exc.get("fichier") not in perimetre:
                hors_perimetre.append({**exc, "observe": None,
                                       "raison": "fichier hors du périmètre lu — "
                                                 "ni honorée ni caduque, non jugée"})
                continue
            caduques.append({**exc, "observe": 0,
                             "raison": "aucune occurrence : fichier nettoyé ou disparu"})
            continue
        honorees.extend(observees[:declare])
        if n > declare:
            surplus = observees[declare:]
            excedents.extend(surplus)
            bloquantes.extend(surplus)
        elif n < declare:
            caduques.append({**exc, "observe": n,
                             "raison": f"{n} occurrence(s) observée(s) pour {declare} déclarée(s)"})

    for cle, items in par_cle.items():
        if cle not in consommees:
            bloquantes.extend(items)

    return bloquantes, honorees, excedents, caduques, hors_perimetre



def lister_fichiers(racine, tout):
    """Fichiers à contrôler, et mode de périmètre.

    Critère retenu : git lui-même, comme `verifier-invariants.py`, mais dans la
    vue SUIVI + NON-SUIVI NON-IGNORÉ (`--cached --others --exclude-standard`),
    et non `git ls-files` nu.

    Motif, relevé le 2026-09-15 : `git ls-files` nu ne rend que les fichiers
    DÉJÀ suivis. Or le Cmd 15 porte « avant commit » — les fichiers qui
    s'apprêtent à entrer au dépôt sont, par définition, encore non suivis. Le
    périmètre nu les manquait donc tous, et rendait « PROPRE » sans les avoir
    lus : un rapport vrai sur un périmètre faux. Les 36 fichiers du chantier
    Ghazâlî sont passés sous ce trou.

    Ce qui reste hors périmètre est ce que git ignore — `raw/` au premier chef,
    immuable et jamais commité. L'exclusion est donc celle du dépôt lui-même,
    non une exclusion propre à cet instrument.

    Repli par parcours disque si git est indisponible (bacs à sable hors dépôt).
    """
    if not tout:
        try:
            sortie = subprocess.run(
                ["git", "ls-files", "-z", "--cached", "--others",
                 "--exclude-standard"], cwd=str(racine),
                capture_output=True, text=True, check=True,
            ).stdout
            chemins = [racine / c for c in sortie.split("\0") if c]
            return chemins, "git-commitable"
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    chemins = []
    for p in racine.rglob("*"):
        if not p.is_file():
            continue
        if any(part in DOSSIERS_EXCLUS for part in p.relative_to(racine).parts):
            continue
        chemins.append(p)
    return chemins, ("aucun" if tout else "repli")


def chemin_affiche(chemin, racine):
    """Chemin relatif à la racine, ou absolu s'il lui est extérieur.

    `Path.relative_to` lève sur un chemin hors racine : un fichier passé
    explicitement en argument (cas normal — épreuve, contrôle ponctuel d'un
    fichier de travail) faisait alors sortir l'instrument en code 2. Défaut
    attrapé par l'épreuve dès sa première passe, le 2026-09-14.
    """
    try:
        return chemin.relative_to(racine).as_posix()
    except ValueError:
        return chemin.as_posix()


def controler(chemin, racine):
    """Retourne (dict classe -> liste de trouvailles, lisible).

    Lecture en octets puis décodage strict : un fichier binaire ne doit pas être
    signalé à tort, et un BOM doit être vu là où il est — en tête d'octets.
    """
    try:
        brut = chemin.read_bytes()
    except OSError:
        return None, False
    if b"\0" in brut:
        return None, False
    try:
        texte = brut.decode("utf-8")
    except UnicodeDecodeError:
        return None, False

    trouvailles = {cle: [] for cle, _, _, _ in CLASSES}
    rel = chemin_affiche(chemin, racine)
    for no_ligne, ligne in enumerate(texte.split("\n"), start=1):
        for colonne, car in enumerate(ligne, start=1):
            point = ord(car)
            for cle, _, jeu, _ in CLASSES:
                if point in jeu:
                    trouvailles[cle].append(
                        {"fichier": rel, "ligne": no_ligne,
                         "colonne": colonne, "codepoint": jeu[point]}
                    )
    return trouvailles, True


def main():
    ap = argparse.ArgumentParser(
        description="Contrôle mécanique du Cmd 15 — hygiène Unicode du dépôt.")
    ap.add_argument("chemins", nargs="*", help="fichiers précis ; défaut : tout le dépôt")
    ap.add_argument("--racine", default=".", help="racine du dépôt (défaut : .)")
    ap.add_argument("--tout", action="store_true",
                    help="ignorer le périmètre git : parcourir le disque")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--strict", action="store_true",
                    help="les signalements hors Cmd 15 font aussi échouer")
    ap.add_argument("--exceptions", default=None,
                    help=f"registre d'exceptions déclarées (défaut : {EXCEPTIONS_DEFAUT})")
    ap.add_argument("--sans-exceptions", action="store_true",
                    help="ignorer le registre : état brut du dépôt")
    args = ap.parse_args()

    racine = Path(args.racine).resolve()
    if args.chemins:
        fichiers = [Path(c).resolve() for c in args.chemins]
        mode = "explicite"
    else:
        fichiers, mode = lister_fichiers(racine, args.tout)

    total = {cle: [] for cle, _, _, _ in CLASSES}
    lus = ignores = 0
    perimetre_lu = set()
    for f in sorted(fichiers):
        if not f.is_file():
            continue
        trouvailles, lisible = controler(f, racine)
        if not lisible:
            ignores += 1
            continue
        lus += 1
        perimetre_lu.add(chemin_affiche(f, racine))
        for cle in total:
            total[cle].extend(trouvailles[cle])

    if args.sans_exceptions:
        exceptions, source_exc = [], None
    else:
        chemin_exc = args.exceptions or EXCEPTIONS_DEFAUT
        exceptions, source_exc = charger_exceptions(chemin_exc)

    brut = list(total["cmd15"])
    (total["cmd15"], honorees, excedents, caduques,
     hors_perimetre) = appliquer_exceptions(brut, exceptions, perimetre_lu)

    bloquants = sum(len(total[cle]) for cle, _, _, bloque in CLASSES if bloque)
    signales = sum(len(total[cle]) for cle, _, _, bloque in CLASSES if not bloque)

    if args.json:
        print(json.dumps({"mode": mode, "fichiers_lus": lus,
                          "fichiers_ignores": ignores,
                          "violations_cmd15": bloquants,
                          "signalements_hors_cmd15": signales,
                          "registre_exceptions": source_exc,
                          "cmd15_brut": len(brut),
                          "exceptions_honorees": len(honorees),
                          "exceptions_excedents": len(excedents),
                          "exceptions_caduques": caduques,
                          "exceptions_hors_perimetre": hors_perimetre,
                          "detail": total}, ensure_ascii=False, indent=2))
    else:
        libelle = {"git-commitable": "vue git commitable : suivis + non-suivis "
                                     "non-ignorés (ce qui peut entrer au commit)",
                   "repli": "repli hors dépôt git : parcours disque",
                   "aucun": "--tout : parcours disque, aucune exclusion",
                   "explicite": "chemins fournis en argument"}[mode]
        print(f"Périmètre : {libelle} — {lus} fichier(s) lu(s), "
              f"{ignores} ignoré(s) (binaire ou non-UTF-8).")
        if args.sans_exceptions:
            print("Exceptions : AUCUNE appliquée (--sans-exceptions) — état brut.")
        elif source_exc:
            print(f"Exceptions : {len(exceptions)} déclarée(s) lue(s) dans "
                  f"{Path(source_exc).name} — {len(honorees)} occurrence(s) "
                  f"honorée(s) sur {len(brut)} relevée(s).")
        else:
            print("Exceptions : aucun registre trouvé — toutes les occurrences "
                  "sont rapportées.")
        for cle, titre, _, bloque in CLASSES:
            items = total[cle]
            if not items:
                continue
            print(f"\n{titre} — {len(items)} occurrence(s)"
                  f"{'' if bloque else ', non bloquant'} :")
            for it in items[:200]:
                print(f"  {it['fichier']}:{it['ligne']}:{it['colonne']} — {it['codepoint']}")
            if len(items) > 200:
                print(f"  … et {len(items) - 200} autre(s).")
        if excedents:
            print(f"\nEXCÉDENT SUR EXCEPTION — {len(excedents)} occurrence(s) "
                  f"au-delà du compte déclaré, bloquante(s) : une exception "
                  f"couvre un compte exact, jamais un fichier en bloc.")
            for it in excedents[:50]:
                print(f"  {it['fichier']}:{it['ligne']}:{it['colonne']} — {it['codepoint']}")
        if hors_perimetre and not args.json:
            print(f"Exceptions non jugées : {len(hors_perimetre)} — leur fichier "
                  f"est hors du périmètre lu (ni honorée, ni caduque).")
        if caduques:
            print(f"\nEXCEPTION(S) CADUQUE(S) — {len(caduques)}, non bloquant, "
                  f"le registre est à mettre à jour :")
            for c in caduques:
                print(f"  {c.get('fichier')} [{c.get('codepoint')}] — {c['raison']}")
        print()
        if bloquants == 0:
            suffixe = (f" {len(honorees)} occurrence(s) sous exception déclarée."
                       if honorees else "")
            print(f"Cmd 15 : PROPRE — 0 violation non couverte."
                  f"{suffixe} {signales} signalement(s) hors Cmd 15.")
        else:
            print(f"Cmd 15 : {bloquants} VIOLATION(S). "
                  f"{signales} signalement(s) hors Cmd 15.")

    if bloquants:
        return 1
    if args.strict and signales:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # défaut de l'instrument, distinct d'une violation
        print(f"erreur d'exécution de l'instrument : {exc}", file=sys.stderr)
        sys.exit(2)
