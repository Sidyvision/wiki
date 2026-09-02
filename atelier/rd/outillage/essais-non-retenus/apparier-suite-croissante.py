"""Appariement global : plus longue suite strictement croissante de rangs,
une ligne au plus par rang ET un rang au plus par ligne.

Motif : l'appariement glouton choisit toujours le plus petit candidat et se
trompe des que l'OCR a perdu la dizaine ('الثامن والعشرون' -> {18, 28} : il
prend 18). Le choix ne peut se faire qu'au vu de toute la suite.

Piege corrige : avec des back-pointers vers une table mutable, la chaine
reconstruite peut reutiliser une meme ligne pour deux rangs (constate :
bab 5 et bab 15 pointant la ligne 'الخامس والثلاثون'). On chaine donc des
noeuds IMMUABLES.
"""

def apparier(cand_par_ligne):
    """cand_par_ligne : liste de set(int) (index = numero de ligne, ordre du
    document). Rend [(index_ligne, rang), ...] croissant en index ET en rang."""
    # noeud = (longueur, cout, rang, index_ligne, parent_noeud|None) : immuable
    nodes = []
    best = {}          # rang -> noeud (meilleur connu, lignes deja traitees)
    for i, cands in enumerate(cand_par_ligne):
        nouveaux = []
        for v in sorted(cands):
            parent, bl, bc = None, 0, 0
            for w, nd in best.items():
                if w < v and (nd[0] > bl or (nd[0] == bl and nd[1] < bc)):
                    parent, bl, bc = nd, nd[0], nd[1]
            node = (bl + 1, bc + v, v, i, parent)
            cur = best.get(v)
            if cur is None or node[0] > cur[0] or (node[0] == cur[0] and node[1] < cur[1]):
                nouveaux.append((v, node))
        for v, node in nouveaux:      # appliques apres la ligne, jamais pendant
            best[v] = node
            nodes.append(node)
    if not best:
        return []
    end = max(best.values(), key=lambda nd: (nd[0], -nd[1]))
    out = []
    nd = end
    while nd is not None:
        out.append((nd[3], nd[2]))
        nd = nd[4]
    return list(reversed(out))
