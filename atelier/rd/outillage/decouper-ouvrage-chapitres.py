#!/usr/bin/env python3
"""Decoupe un .md OCR page-par-page en fichiers par chapitre.
Usage: decouper_chapitres.py <fichier.md> <dossier_sortie> <slug-prefixe>
                             [page-de-debut] [--langue=en|fr]

Detecte les en-tetes de chapitre en debut de page (tolerance OCR) :
  --langue=en (defaut) : CHAPTER <romain>, PREFACE, APPENDIX, INDEX, CONTENTS
  --langue=fr          : CHAPITRE <romain|PREMIER>, <n>e PARTIE, INTRODUCTION,
                         CONCLUSION, REPERTOIRE GENERAL, TABLE DES..., etc.
Jeu francais ajoute le 2026-09-02 pour Osman Yahia, Histoire et classification
de l'oeuvre d'Ibn 'Arabi (696 p.)."""
import re, sys, os, unicodedata

# tolerance OCR : I/l/1/T confondus, V/Y/U, X/K ; suffixes parasites
ROM = r"[IVXLTilU1Y|]{1,8}"
PATS_EN = [
    (re.compile(rf"^[\s|.,'\"]*[COG0][HKN]?A[PF]?TER\s*[-—]?\s*({ROM})\s*[.,;:\s]*$", re.I), "chapitre"),
    (re.compile(r"^\s*PREFACE\s*[.]?\s*$", re.I), "preface"),
    (re.compile(r"^\s*(?:TABLE OF )?CONTENTS\s*[.]?\s*$", re.I), "sommaire"),
    (re.compile(rf"^\s*APPENDIX\s*({ROM})?\b[.\s]*$", re.I), "appendice"),
    (re.compile(r"^\s*(?:GENERAL )?INDEX\s*[.]?\s*$", re.I), "index"),
    (re.compile(r"^\s*ERRATA\s*[.]?\s*$", re.I), "errata"),
]

# Jeu francais. 'CHAPITRE PREMIER' vaut I ; les titres courants repetes
# (REPERTOIRE GENERAL page apres page) sont fusionnes en aval comme 'index'.
PATS_FR = [
    (re.compile(rf"^[\s|.,'\"]*[C(]HAP[I1lT]TRE\s*[-—]?\s*(PREM[I1l]ER|{ROM})\s*[.,;:\s]*$", re.I), "chapitre"),
    (re.compile(r"^\s*(PREMI[EÈ]RE|DEUXI[EÈ]ME|TROISI[EÈ]ME|QUATRI[EÈ]ME|CINQUI[EÈ]ME)\s+PARTIE\s*[.]?\s*$", re.I), "partie"),
    (re.compile(r"^\s*(?:AVANT[-\s]PROPOS|PR[EÉ]FACE)\s*[.]?\s*$", re.I), "preface"),
    (re.compile(r"^\s*INTRODUCTION\s*[.]?\s*$", re.I), "introduction"),
    (re.compile(r"^\s*CONCLUSION\s*[.]?\s*$", re.I), "conclusion"),
    (re.compile(r"^\s*R[EÉ]PERTO[I1l]RE\s+G[EÉ]N[EÉ]RAL\b.*$", re.I), "repertoire"),
    (re.compile(r"^\s*B[I1l]BL[I1l]OGRAPH[I1l]E\s*[.]?\s*$", re.I), "bibliographie"),
    (re.compile(r"^\s*TABLE\s+DES\s+S[I1lC]GLES.*$", re.I), "sigles"),
    # ADDENDA n'ouvre une section que sous sa forme titree «A»/«B»/«C» : nu,
    # c'est un intertitre au fil du chapitre (constate p.117 d'Osman Yahia,
    # ou il coupait le chapitre V en deux).
    (re.compile(r"^\s*ADDENDA\s*[«\"'‹]\s*[A-Z0O]\s*[»\"'›]?.*$", re.I), "addenda"),
    # Tables recapitulatives : chacune a sa nature propre, sinon la fusion des
    # titres courants les agglomere en un seul bloc (constate : 156 pages
    # d'un coup pour la 3e partie d'Osman Yahia).
    (re.compile(r"^\s*TABLE\s+(?:ALPHAB[EÉ]TIQUE\s+)?DES\s+OUVRAGES\s+DU\s+R[EÉ]PERTO[I1l]RE.*$", re.I), "table-ouvrages"),
    (re.compile(r"^\s*TABLE\s+DES\s+OUVRAGES\s+(?:IMPRIM[EÉ]S|COMMENT[EÉ]S|TRADU[I1l]TS).*$", re.I), "table-ouvrages-imprimes"),
    (re.compile(r"^\s*TABLE\s+DES\s+CORRESPONDANCES.*$", re.I), "table-correspondances"),
    (re.compile(r"^\s*TABLE\s+(?:ALPHAB[EÉ]TIQUE\s+)?DES\s+NOMS\s+PROPRES.*$", re.I), "table-noms-propres"),
    (re.compile(r"^\s*TABLE\s+(?:ALPHAB[EÉ]TIQUE\s+)?DES\s+NOMS\s+D['’]OUVRAGES.*$", re.I), "table-noms-ouvrages"),
    (re.compile(r"^\s*TABLE\s+DES\s+MANUSCR[I1l]TS.*$", re.I), "table-manuscrits"),
    (re.compile(r"^\s*TABLE\s+DES\s+MATI[EÈ]RES\b[\s.,:;-]*$", re.I), "table-matieres"),
    (re.compile(r"^\s*(?:INDEX|ERRATA)\s*[.]?\s*$", re.I), "index"),
]
JEUX = {"en": PATS_EN, "fr": PATS_FR}

# Sections a fusionner quand elles se repetent (titre courant de page).
FUSION = ("index", "errata", "sommaire", "repertoire", "sigles", "bibliographie",
          "addenda", "table-ouvrages", "table-correspondances",
          "table-noms-propres", "table-noms-ouvrages", "table-manuscrits",
          "table-matieres", "table-ouvrages-imprimes")

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "section"

AMBIG = {"I": ["I"], "L": ["I", ""], "1": ["I"], "T": ["I"], "|": ["I"],
         "U": ["V", "II", "III"], "Y": ["V"], "V": ["V"], "X": ["X"]}

def _val(t):
    vals = {"I": 1, "V": 5, "X": 10}
    if not t or any(c not in vals for c in t):
        return None
    n, prev = 0, 0
    for c in reversed(t):
        v = vals[c]
        n = n - v if v < prev else n + v
        prev = max(prev, v)
    return n if 1 <= n <= 30 else None

def rom_candidates(s):
    """Toutes les valeurs entieres plausibles d'un romain OCR-bruite."""
    s = s.upper()
    # 'CHAPITRE PREMIER' (francais) vaut I.
    if s.startswith("PREM"):
        return {1}
    out = set()
    for src in (s, s[:-1]):  # dernier caractere = point mal lu
        variants = [""]
        ok = True
        for c in src:
            if c not in AMBIG:
                ok = False
                break
            variants = [v + a for v in variants for a in AMBIG[c]]
            if len(variants) > 64:
                break
        if not ok:
            continue
        for v in variants:
            n = _val(v)
            if n:
                out.add(n)
    return out


def main(src, outdir, prefix, start_page=1, langue="en"):
    pats = JEUX[langue]
    txt = open(src, encoding="utf-8", errors="replace").read()
    # separer frontmatter
    fm = ""
    if txt.startswith("---"):
        end = txt.find("\n---", 3)
        fm, txt = txt[:end+4], txt[end+4:]
    pages = re.split(r"(?m)^<!-- page (\d+) -->$", txt)
    # pages = [avant, num, corps, num, corps, ...]
    items = [(int(pages[i]), pages[i+1]) for i in range(1, len(pages)-1, 2)]

    sections, cur = [], {"titre": "front-matter", "kind": "front", "pages": []}
    chap_seq = [0]
    for num, body in items:
        head = None
        if num >= start_page:
            for line in body.strip().splitlines()[:14]:
                for pat, kind in pats:
                    m = pat.match(line)
                    if not m:
                        continue
                    if kind == "chapitre":
                        # exiger la sequence : seul le chapitre suivant est accepte.
                        # Variantes OCR : un dernier caractere peut etre un point
                        # lu comme lettre (I. -> IL, XIII. -> XIUL).
                        g = m.group(1) or ""
                        if chap_seq[0] + 1 not in rom_candidates(g):
                            continue
                    head = (kind, m.group(1) if m.groups() and m.group(1) else "", line.strip())
                    break
                if head:
                    break
        if head:
            if cur["pages"]:
                sections.append(cur)
            kind, num_rom, raw = head
            if kind == "chapitre":
                chap_seq[0] += 1
                titre = f"chapitre-{chap_seq[0]:02d}"
            else:
                titre = f"{kind} {num_rom}".strip() if num_rom else kind
            cur = {"titre": titre, "kind": kind, "raw": raw, "pages": []}
        cur["pages"].append((num, body))
    if cur["pages"]:
        sections.append(cur)

    # fusionner les sections consecutives de meme nature non numerotee
    # (index/errata : l'en-tete est un titre courant repete a chaque page)
    fused = []
    for s in sections:
        if fused and s["kind"] in FUSION and fused[-1]["kind"] == s["kind"]:
            fused[-1]["pages"].extend(s["pages"])
        else:
            fused.append(s)
    sections = fused

    os.makedirs(outdir, exist_ok=True)
    manifeste = []
    for i, s in enumerate(sections):
        p0, p1 = s["pages"][0][0], s["pages"][-1][0]
        name = f"{prefix}-{i:02d}-{slug(s['titre'])}.md"
        path = os.path.join(outdir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"source: {os.path.basename(src)}\n")
            f.write(f"section: \"{s['titre']}\"\n")
            f.write(f"pages_pdf: {p0}-{p1}\n")
            f.write("---\n\n")
            f.write(f"# {s.get('raw', s['titre'])}\n\n")
            for num, body in s["pages"]:
                f.write(f"<!-- page {num} -->\n{body.rstrip()}\n\n")
        manifeste.append((name, s["titre"], p0, p1, len(s["pages"])))

    print(f"{len(sections)} sections -> {outdir}")
    for n, t, a, b, c in manifeste:
        print(f"  {n:55s} p.{a}-{b} ({c}p)")

    # Controle d'integrite : aucune page perdue, aucune dupliquee.
    # Sort en code non nul si l'invariant est rompu (regle SVIII : constater,
    # ne pas corriger).
    repart = [n for s in sections for n, _ in s["pages"]]
    attendues = {n for n, _ in items}
    manquantes = sorted(attendues - set(repart))
    doublons = len(repart) - len(set(repart))
    print(f"\n[integrite] {len(repart)} pages reparties / {len(attendues)} lues "
          f"| manquantes={manquantes or 'aucune'} | doublons={doublons}")
    if manquantes or doublons:
        print("[integrite] ECHEC : le decoupage ne restitue pas le fichier source.")
        return 1
    return 0

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = [a for a in sys.argv[1:] if a.startswith("--")]
    langue = "en"
    for o in opts:
        if o.startswith("--langue="):
            langue = o.split("=", 1)[1].strip().lower()
    if langue not in ("en", "fr"):
        print(f"langue inconnue: {langue} (attendu: en, fr)", file=sys.stderr)
        sys.exit(2)
    sp = int(args[3]) if len(args) > 3 else 1
    sys.exit(main(args[0], args[1], args[2], sp, langue))
