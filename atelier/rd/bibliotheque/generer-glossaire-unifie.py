#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere le lexique unifie a partir des fiches `type: index-livre`.

Lignee `carte-du-depot.py`, cinq principes non negociables :
  1. DETERMINISTE — stdlib seule, aucun LLM, aucun reseau, relances
     octet-identiques (tri stable, aucune horodatation dans le corps).
  2. LECTURE SEULE — n'ecrit qu'un seul fichier, le glossaire derive.
  3. AUCUN JUGEMENT — recopie et compte. Ne resume pas, ne qualifie pas,
     ne fusionne jamais deux termes proches d'autorite.
  4. ARTEFACT DERIVE — le depot fait foi ; ce fichier se regenere et ne
     s'edite JAMAIS a la main.
  5. HORS CORPS DOCTRINAL — instrument de reperage, jamais une source.

Sortie : terme -> ouvrage(s) -> page(s). Refuse de generer si
`valider-index-livres.py` signale une anomalie bloquante.
"""

import argparse
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import valider_index_livres_shim  # noqa: E402  (voir plus bas)

RE_LIGNE = re.compile(r"^\|")


def cle_tri(terme):
    """Tri alphabetique insensible aux diacritiques, mais qui les CONSERVE
    dans l'affichage. Deterministe : NFD, retrait des combinantes, casefold."""
    plie = "".join(c for c in unicodedata.normalize("NFD", terme)
                   if not unicodedata.combining(c))
    return (plie.casefold(), terme)


def lire_fiche(chemin):
    with open(chemin, encoding="utf-8") as fh:
        texte = fh.read()
    fm, corps = valider_index_livres_shim.lire_frontmatter(texte)
    if fm is None:
        return None, []
    lignes = [l for l in corps.splitlines() if RE_LIGNE.match(l.strip())]
    entrees = []
    for ligne in lignes[2:]:
        cel = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cel) != 4:
            continue
        ar, translit, fr, pages = cel
        entrees.append({"ar": ar, "translit": translit, "fr": fr, "pages": pages})
    return fm, entrees


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dossier", default=ici)
    ap.add_argument("--sortie", default=os.path.join(ici, "glossaire-unifie.md"))
    ap.add_argument("--sans-validation", action="store_true",
                    help="genere malgre les anomalies bloquantes (a n'utiliser "
                         "que sur demande explicite de Sidy)")
    args = ap.parse_args()

    if not args.sans_validation:
        code = valider_index_livres_shim.valider(args.dossier)
        if code != 0:
            print("REFUS : le validateur signale des anomalies bloquantes.",
                  file=sys.stderr)
            print("Corriger les fiches, ou relancer avec --sans-validation "
                  "sur decision de Sidy.", file=sys.stderr)
            return 1

    fiches = sorted(f for f in os.listdir(args.dossier)
                    if f.startswith("index-") and f.endswith(".md"))
    lexique = {}
    ouvrages = []
    for nom in fiches:
        fm, entrees = lire_fiche(os.path.join(args.dossier, nom))
        if fm is None:
            continue
        livre = fm.get("livre", nom).strip().strip('"')
        ouvrages.append((livre, nom, len(entrees)))
        for e in entrees:
            terme = e["translit"] or e["fr"] or e["ar"]
            if not terme:
                continue
            lexique.setdefault(terme, []).append({
                "livre": livre, "pages": e["pages"],
                "ar": e["ar"], "fr": e["fr"],
            })

    lignes = []
    lignes.append("---")
    lignes.append('title: "Glossaire unifie — lexique de reperage"')
    lignes.append("type: artefact-derive")
    lignes.append('generateur: "generer-glossaire-unifie.py"')
    lignes.append("created: 2026-08-22")
    lignes.append("updated: 2026-08-22")
    lignes.append("sources: []")
    lignes.append("links: []")
    lignes.append("---")
    lignes.append("")
    lignes.append("# Glossaire unifie — lexique de reperage")
    lignes.append("")
    lignes.append("> **ARTEFACT DERIVE — ne jamais editer a la main.** Regenere par")
    lignes.append("> `generer-glossaire-unifie.py` a partir des fiches `index-livre`")
    lignes.append("> du meme dossier. Le depot fait foi.")
    lignes.append(">")
    lignes.append("> Instrument de reperage : il dit *ou chercher*, jamais *quoi")
    lignes.append("> conclure*. La levee d'un `to-source` reste la verification du")
    lignes.append("> texte primaire par Sidy (CLAUDE.md §VII).")
    lignes.append("")
    lignes.append("## Ouvrages depouilles")
    lignes.append("")
    lignes.append("| ouvrage | fiche | entrees |")
    lignes.append("|---|---|---|")
    if ouvrages:
        for livre, nom, n in sorted(ouvrages):
            lignes.append("| %s | `%s` | %d |" % (livre, nom, n))
    else:
        lignes.append("| — | — | 0 |")
    lignes.append("")
    lignes.append("## Lexique")
    lignes.append("")
    lignes.append("| terme | arabe | francais | ouvrage | pages |")
    lignes.append("|---|---|---|---|---|")
    if lexique:
        for terme in sorted(lexique, key=cle_tri):
            for occ in lexique[terme]:
                lignes.append("| %s | %s | %s | %s | %s |"
                              % (terme, occ["ar"], occ["fr"],
                                 occ["livre"], occ["pages"]))
    else:
        lignes.append("| — | — | — | — | — |")
    lignes.append("")
    lignes.append("Termes distincts : %d — occurrences : %d — ouvrages : %d"
                  % (len(lexique), sum(len(v) for v in lexique.values()),
                     len(ouvrages)))
    lignes.append("")

    with open(args.sortie, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lignes))
    print("ecrit : %s (%d termes, %d ouvrages)"
          % (args.sortie, len(lexique), len(ouvrages)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
