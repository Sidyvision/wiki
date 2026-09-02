#!/usr/bin/env python3
"""Decoupe un .md OCR page-par-page en fichiers par chapitre.
Usage: decouper_chapitres.py <fichier.md> <dossier_sortie> <slug-prefixe>
Detecte les en-tetes CHAPTER <romain>, PREFACE, APPENDIX, INDEX, CONTENTS
en debut de page (tolerance OCR)."""
import re, sys, os, unicodedata

# tolerance OCR : I/l/1/T confondus, V/Y/U, X/K ; suffixes parasites
ROM = r"[IVXLTilU1Y|]{1,8}"
PATS = [
    (re.compile(rf"^[\s|.,'\"]*[COG0][HKN]?A[PF]?TER\s*[-—]?\s*({ROM})\s*[.,;:\s]*$", re.I), "chapitre"),
    (re.compile(r"^\s*PREFACE\s*[.]?\s*$", re.I), "preface"),
    (re.compile(r"^\s*(?:TABLE OF )?CONTENTS\s*[.]?\s*$", re.I), "sommaire"),
    (re.compile(rf"^\s*APPENDIX\s*({ROM})?\b[.\s]*$", re.I), "appendice"),
    (re.compile(r"^\s*(?:GENERAL )?INDEX\s*[.]?\s*$", re.I), "index"),
    (re.compile(r"^\s*ERRATA\s*[.]?\s*$", re.I), "errata"),
]

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


def main(src, outdir, prefix, start_page=1):
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
                for pat, kind in PATS:
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
        if fused and s["kind"] in ("index", "errata", "sommaire") and fused[-1]["kind"] == s["kind"]:
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
    sp = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sp))
