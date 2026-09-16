#!/usr/bin/env python3
"""Extraction des bandeaux de tete des blocs-racines — Gloton, section A.

Chaque racine du lexique ouvre par un bandeau GRIS portant, sur une seule ligne :
  case 1 (numero) | case 2 (nb d'entrees) | case 3 (les radicales) | case 4 (traductions).

Le bandeau est detectable sans OCR : c'est une bande horizontale ou une large
proportion des pixels est grise (claire, desaturee). Le script isole ces bandes,
les recadre avec marge et les empile en planches lisibles, de facon a ce qu'une
lecture visuelle porte sur ~10 racines par image au lieu d'une page entiere.

L'outil ne lit rien : il prepare la lecture. Toute transcription reste manuelle.
"""
import argparse, os, sys
from PIL import Image

# Geometrie des doubles pages de la campagne (originaux 5712x4284).
PAGES = {"G": 0.045, "D": 0.495}   # abscisse relative du bord gauche de chaque page
LARGEUR_PAGE = 0.455
HAUT, BAS = 0.05, 0.97

def bandes_grises(im, ratio=0.935, hauteur_min=20):
    """Intervalles (y0, y1) des lignes dont le fond est gris.

    Seuil ADAPTATIF, et non absolu : l'eclairage varie d'une page a l'autre
    d'une meme double page (la page de droite est souvent plus sombre), si bien
    qu'un seuil fixe prend le papier blanc d'une page pour le bandeau gris d'une
    autre. On compare donc chaque ligne au blanc PROPRE de sa page.

    Mesure par ligne : la MEDIANE de luminance, robuste au texte. Une ligne de
    texte ordinaire a un fond blanc, donc une mediane proche du blanc de la page ;
    une ligne de bandeau a un fond gris, donc une mediane nettement plus basse,
    quel que soit le texte qu'elle porte.
    """
    g = im.convert("L")
    w, h = g.size
    px = g.resize((max(1, w // 6), h), Image.BILINEAR).load()
    wl = max(1, w // 6)
    med = []
    for y in range(h):
        ligne = sorted(px[x, y] for x in range(wl))
        med.append(ligne[wl // 2])
    blanc = sorted(med)[int(len(med) * 0.90)]        # blanc propre a cette page
    seuil = blanc * ratio
    gris = [m < seuil for m in med]
    bandes, debut = [], None
    for y, est_gris in enumerate(gris + [False]):
        if est_gris and debut is None:
            debut = y
        elif not est_gris and debut is not None:
            if y - debut >= hauteur_min:
                bandes.append((debut, y))
            debut = None
    return bandes

def extraire(chemin, tag, marge=26, echelle=1.7):
    im = Image.open(chemin)
    w, h = im.size
    x0 = int(w * PAGES[tag]); x1 = int(w * (PAGES[tag] + LARGEUR_PAGE))
    page = im.crop((x0, int(h * HAUT), x1, int(h * BAS)))
    out = []
    for (a, b) in bandes_grises(page):
        a = max(0, a - marge); b = min(page.height, b + marge)
        c = page.crop((0, a, page.width, b))
        c = c.resize((int(c.width * echelle), int(c.height * echelle)), Image.LANCZOS)
        out.append(c)
    return out

def planche(bandes, dest, largeur_max=2100, ecart=14):
    if not bandes:
        return False
    ech = min(1.0, largeur_max / max(b.width for b in bandes))
    bandes = [b.resize((int(b.width * ech), int(b.height * ech)), Image.LANCZOS)
              for b in bandes] if ech < 1.0 else bandes
    W = max(b.width for b in bandes)
    H = sum(b.height for b in bandes) + ecart * (len(bandes) + 1)
    pl = Image.new("RGB", (W, H), (255, 255, 255))
    y = ecart
    for b in bandes:
        pl.paste(b, (0, y)); y += b.height + ecart
    pl.save(dest)
    return True

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("photos", nargs="+", help="fichiers JPG de double page")
    ap.add_argument("--sortie", default="/tmp/bandeaux", help="dossier de destination")
    ap.add_argument("--par-planche", type=int, default=6)
    a = ap.parse_args()
    os.makedirs(a.sortie, exist_ok=True)
    total = 0
    for ph in a.photos:
        base = os.path.splitext(os.path.basename(ph))[0]
        for tag in ("G", "D"):
            try:
                bandes = extraire(ph, tag)
            except Exception as e:
                print(f"{base}{tag} : ERREUR {e}", file=sys.stderr); continue
            for i in range(0, len(bandes), a.par_planche):
                lot = bandes[i:i + a.par_planche]
                dest = os.path.join(a.sortie, f"{base}{tag}_{i//a.par_planche:02d}.png")
                if planche(lot, dest):
                    print(f"{dest} : {len(lot)} bandeau(x)")
                    total += len(lot)
    print(f"TOTAL : {total} bandeau(x) candidat(s)")

if __name__ == "__main__":
    main()
