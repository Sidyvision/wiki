#!/usr/bin/env python3
"""Juge de paix de la transcription du corps du Kitab al-Ta'rifat (CLAUDE.md SVIII.2).

Lecture seule. Rapporte des faits bruts, ne corrige rien :
  1. chaque cliche distinct de raw/Transcription Jurjani/ est-il cite dans la fiche ?
  2. les numeros de definition croissent-ils avec les numeros de page ?
  3. aucune definition ne manque a l'interieur d'une page (suite ininterrompue) ?
  4. aucune definition ne manque entre deux pages consecutives photographiees ?
  5. hygiene Unicode (Cmd 15) sur la fiche.
Usage : python3 atelier/rd/outillage/verifier-transcription-jurjani.py [--racine /root/wiki]
"""
import argparse, hashlib, pathlib, re, sys, unicodedata

FICHE = "doctrinal/sources/kitab-tarifat-corps-transcription.md"
# Codepoints construits, jamais ecrits en clair : ce fichier doit lui-meme
# rester exempt des caracteres qu il detecte (CLAUDE.md Cmd 15).
INVISIBLES = "".join(chr(c) for c in (0x200B, 0x200C, 0x200D, 0x200E, 0x200F, 0xFEFF))


def cliches(racine):
    """Chemins des cliches, dedupliques par empreinte (les noms sont en forme
    de normalisation Unicode non reproductible a la saisie : on les enumere)."""
    dossiers = [p for p in racine.glob("raw/*") if p.is_dir() and "Jurjani" in p.name
                and "Downloads" not in str(p)]
    vus, out = {}, []
    for d in dossiers:
        for f in sorted(x for x in d.iterdir() if x.is_file()):
            h = hashlib.md5(f.read_bytes()).hexdigest()
            if h in vus:
                continue
            vus[h] = f.stem
            out.append(f.stem)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".")
    a = ap.parse_args()
    racine = pathlib.Path(a.racine).resolve()
    texte = (racine / FICHE).read_text(encoding="utf-8")
    erreurs = 0

    attendus = cliches(racine)
    cites = set(re.findall(r"IMG_\d{4}", texte))
    manquants = [c for c in attendus if c not in cites]
    surplus = sorted(cites - set(attendus))
    print(f"[1] cliches distincts sur disque : {len(attendus)}")
    print(f"    cliches cites dans la fiche  : {len(cites)}")
    print(f"    non transcrits               : {manquants or 'aucun'}")
    print(f"    cites sans fichier           : {surplus or 'aucun'}")
    erreurs += len(manquants) + len(surplus)

    entetes = re.findall(r"(?m)^## p\. (\d+) — déf\. \[?(\d{4})", texte)
    couples = [(int(p), int(d)) for p, d in entetes]
    desordre = [(couples[i - 1], couples[i]) for i in range(1, len(couples))
                if couples[i][0] > couples[i - 1][0] and couples[i][1] < couples[i - 1][1]]
    print(f"[2] pages numerotees dans la fiche : {len(couples)}")
    print(f"    inversions page/definition     : {desordre or 'aucune'}")
    erreurs += len(desordre)

    blocs = re.split(r"(?m)^## ", texte)
    lacunes, ruptures, precedent = [], [], None
    for b in blocs:
        titre = b.split("\n")[0]
        if " — déf. " not in titre:
            continue
        nums = sorted({int(x) for x in re.findall(r"(?m)^### (?:\[déf\. )?(\d{4})", b)})
        if not nums:
            continue
        attendu = nums[-1] - nums[0] + 1
        if len(nums) != attendu:
            manque = sorted(set(range(nums[0], nums[-1] + 1)) - set(nums))
            lacunes.append((titre.split(" — ")[0], manque))
        if precedent is not None and nums[0] < precedent:
            ruptures.append((titre.split(" — ")[0], precedent, nums[0]))
        precedent = nums[-1]
    print(f"[3] definitions manquantes dans une page : {lacunes or 'aucune'}")
    print(f"[4] discontinuites entre pages voisines  : {ruptures or 'aucune'}")
    erreurs += len(lacunes) + len(ruptures)

    trouves = sorted({c for c in texte if c in INVISIBLES})
    print(f"[5] caracteres invisibles (Cmd 15) : "
          f"{[unicodedata.name(c) for c in trouves] or 'aucun'}")
    erreurs += len(trouves)

    defs = sorted({int(x) for x in re.findall(r"(?m)^### (?:\[déf\. )?(\d{4})", texte)})
    print(f"[i] definitions distinctes transcrites : {len(defs)} "
          f"(de {defs[0]:04d} a {defs[-1]:04d})")

    print(f"\nRESULTAT : {erreurs} anomalie(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
