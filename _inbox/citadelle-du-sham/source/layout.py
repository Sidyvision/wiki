import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

HALL_HALF = 7

def spine(start_axis_edge, cross_fixed, dx, dy, metas, corr_len=6, corr_hw=2):
    """dx,dy: exactly one nonzero, the cardinal direction of the spine.
    start_axis_edge: signed distance along that axis where the previous boundary is.
    cross_fixed: the fixed coordinate on the perpendicular axis (usually 0).
    Returns (rooms, corridors) with x0,y0,x1,y1,cx,cy for each.
    """
    sign = dx if dx != 0 else dy
    rooms = []
    corridors = []
    prev_far = start_axis_edge
    for m in metas:
        half = m['half']
        near = prev_far + corr_len
        center_d = near + half
        far = center_d + half
        cx_axis = sign * center_d
        if dx != 0:
            cx, cy = cx_axis, cross_fixed
            x0, x1 = cx - half, cx + half
            y0, y1 = cy - half, cy + half
        else:
            cx, cy = cross_fixed, cx_axis
            x0, x1 = cx - half, cx + half
            y0, y1 = cy - half, cy + half
        room = dict(m); room.update(cx=cx, cy=cy, x0=x0, y0=y0, x1=x1, y1=y1)
        rooms.append(room)
        # corridor from prev_far to near, along axis, width corr_hw on cross axis
        c_near_axis = sign * prev_far
        c_far_axis = sign * near
        if dx != 0:
            cxa0, cxa1 = sorted([c_near_axis, c_far_axis])
            corridor = dict(x0=cxa0, x1=cxa1, y0=cross_fixed-corr_hw, y1=cross_fixed+corr_hw, wing=m['wing'])
        else:
            cya0, cya1 = sorted([c_near_axis, c_far_axis])
            corridor = dict(x0=cross_fixed-corr_hw, x1=cross_fixed+corr_hw, y0=cya0, y1=cya1, wing=m['wing'])
        corridors.append(corridor)
        prev_far = far
    return rooms, corridors

hall = dict(id='hall', key=None, name='Grand Hall de la Citadelle',
            flavor="Trois couloirs partent d'ici : l'Atelier a l'ouest, le Corpus Doctrinal au nord, l'Hermeneutique a l'est.",
            wing='hall', cx=0, cy=0, x0=-HALL_HALF, x1=HALL_HALF, y0=-HALL_HALF, y1=HALL_HALF)

rd_metas = [
    dict(id='rd-instrument', key='rd/instrument', name="Chambre de l'Instrument",
         flavor="Une maquette suspendue de l'arbre ontologique akbarien tourne lentement sur son axe de trente-huit degres.",
         wing='rd', half=5),
    dict(id='rd-outillage', key='rd/outillage', name="Atelier des Outils",
         flavor="Scripts et gabarits pour tenir le depot : generateurs de manifeste, detecteurs du non-trackee.",
         wing='rd', half=5),
    dict(id='rd-cahiers', key='rd/cahiers', name="Cahiers de Chantier",
         flavor="Le brouillon en cours du pole R&D, encre encore mouillee.",
         wing='rd', half=5),
]
rd_rooms, rd_corr = spine(HALL_HALF, 0, -1, 0, rd_metas)

# branch: zodiac alcove off cahiers (south)
cahiers = rd_rooms[2]
zod_metas = [dict(id='rd-zodiaque', key='rd/cahiers/brouillons-extension-zodiacale', name="Alcove du Zodiaque",
             flavor="Douze esquisses epinglees au mur, une par signe -- studio, distribution, production, jusqu'au gardien du Capricorne.",
             wing='rd', half=3)]
zod_rooms, zod_corr = spine(cahiers['y1'], cahiers['cx'], 0, 1, zod_metas, corr_len=5, corr_hw=2)

doc_metas = [
    dict(id='doc-hub', key='doctrinal', name="Salle du Catalogue",
         flavor="Le grand index veille ici ; toutes les salles de l'aile doctrinale s'y rattachent.",
         wing='doctrinal', half=6),
    dict(id='doc-autorites', key='doctrinal/autorites', name="Galerie des Autorites",
         flavor="Ibn Arabi, Guenon, Jurjani et les autres -- ceux dont la parole fait reference.",
         wing='doctrinal', half=5),
    dict(id='doc-traditions', key='doctrinal/traditions', name="Salle des Traditions",
         flavor="Les grandes formes traditionnelles, rangees cote a cote, cloisons intactes.",
         wing='doctrinal', half=5),
    dict(id='doc-symboles', key='doctrinal/symboles', name="Scriptorium des Symboles",
         flavor="Des dizaines de rouleaux, un par symbole -- du barzakh au khatm, de la khalwa a la walaya.",
         wing='doctrinal', half=5),
    dict(id='doc-sources', key='doctrinal/sources', name="Reserve des Sources",
         flavor="Traductions et transcriptions primaires, gardees pour verification avant tout usage.",
         wing='doctrinal', half=5),
    dict(id='doc-etudes', key='doctrinal/etudes', name="Cabinet d'Etudes",
         flavor="Rapprochements savants tenus a distance de tout verdict.",
         wing='doctrinal', half=5),
    dict(id='doc-discernement', key='doctrinal/discernement', name="Chambre du Discernement",
         flavor="Hypotheses encore ouvertes -- rien n'y est tranche sans autorite textuelle.",
         wing='doctrinal', half=5),
    dict(id='doc-deviations', key='doctrinal/deviations', name="Chambre Scellee des Deviations",
         flavor="Ce qui s'ecarte de la voie droite, conserve pour etre reconnu, jamais suivi.",
         wing='doctrinal', half=5),
]
doc_rooms, doc_corr = spine(HALL_HALF, 0, 0, -1, doc_metas)

herm_metas = [
    dict(id='herm-hub', key='hermeneutique', name="Salle des Interfaces",
         flavor="Le seuil du domaine intermediaire : ici, la fiction est tenue pour passage.",
         wing='hermeneutique', half=6),
    dict(id='herm-mg', key='hermeneutique/metal-gear', name="Chambre de la Mother Base",
         flavor="Une base flottante reduite en maquette -- infrastructure et loyaute comme memes materiaux.",
         wing='hermeneutique', half=5),
    dict(id='herm-ds', key='hermeneutique/death-stranding', name="Chambre du Lien Rompu",
         flavor="Un DHV Magellan miniature relie les rives d'un monde disloque.",
         wing='hermeneutique', half=5),
    dict(id='herm-hxh', key='hermeneutique/hunter-x-hunter', name="Chambre du Nen",
         flavor="Le voeu et la restriction, graves au mur comme une loi de puissance.",
         wing='hermeneutique', half=5),
    dict(id='herm-auteurs', key='hermeneutique/auteurs', name="Galerie des Auteurs",
         flavor="Kojima, Togashi, Shinkawa -- ceux qui ont bati ces mondes tenus pour interfaces.",
         wing='hermeneutique', half=5),
]
herm_rooms, herm_corr = spine(HALL_HALF, 0, 1, 0, herm_metas)

all_rooms = [hall] + rd_rooms + zod_rooms + doc_rooms + herm_rooms
all_corr = rd_corr + zod_corr + doc_corr + herm_corr

# sanity check bounds
xs = [r['x0'] for r in all_rooms]+[r['x1'] for r in all_rooms]
ys = [r['y0'] for r in all_rooms]+[r['y1'] for r in all_rooms]
print("bounds x:", min(xs), max(xs), "y:", min(ys), max(ys))
print("rooms:", len(all_rooms), "corridors:", len(all_corr))
for r in all_rooms:
    print(r['id'], r['x0'],r['y0'],r['x1'],r['y1'])

with open(os.path.join(HERE, 'rooms.json'), 'w') as f:
    json.dump({'rooms': all_rooms, 'corridors': all_corr}, f, ensure_ascii=False)
