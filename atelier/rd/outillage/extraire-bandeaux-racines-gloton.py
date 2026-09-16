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

def recadrer(chemin, zone, echelle, dest):
    """Recadrage cible dans la photographie SOURCE, en coordonnees relatives.

    Pourquoi cette fonction existe : la planche de bandeaux suffit a lire la
    plupart des case 4, mais pas toutes. Quand une case 4 est longue, elle
    deborde le cadrage de la planche -- a DROITE (le bord de page est coupe) ou
    en BAS (la derniere ligne du bandeau est mangee par la marge). La planche
    est alors muette sur la fin du sens, et la transcription serait tronquee
    sans qu'on le voie.

    Le recours est de revenir a l'original 5712x4284 et d'y decouper la zone
    exacte, agrandie. Cela a servi quatre fois a la passe de cloture du
    2026-09-16 (entrees 1446, 1458, 1698/1700 et 0518), chaque fois en
    `python3 -c` jetable, donc chaque fois reecrit de memoire. C'est ce
    gaspillage que la fonction supprime.

    Coordonnees RELATIVES (0.0 a 1.0) et non en pixels : elles se lisent
    directement sur un apercu de la photographie, sans connaitre sa taille, et
    restent valables si la campagne est un jour rephotographiee a une autre
    definition.

    Echelle 2.6 a 4.0 selon la finesse du corps imprime ; en dessous de 2.5 les
    accents francais deviennent ambigus (e/e/e), au-dela de 4.0 on n'agrandit
    plus que le grain du capteur.
    """
    im = Image.open(chemin)
    w, h = im.size
    x0, y0, x1, y1 = zone
    c = im.crop((int(w * x0), int(h * y0), int(w * x1), int(h * y1)))
    c = c.resize((int(c.width * echelle), int(c.height * echelle)), Image.LANCZOS)
    c.save(dest)
    return c.size

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
    ap.add_argument("--marge", type=int, default=26,
                    help="marge de recadrage autour du bandeau, en pixels "
                         "(elargir pour rattraper une case 2 ou une case 4 rognee)")
    ap.add_argument("--recadrer", metavar="x0,y0,x1,y1", default=None,
                    help="MODE RECADRAGE CIBLE : au lieu de decouper les bandeaux, "
                         "extrait une seule zone de chaque photographie, en "
                         "coordonnees RELATIVES (0.0 a 1.0), et l'agrandit. Sert a "
                         "lire une case 4 que la planche tronque a droite ou en bas. "
                         "Dans ce mode --sortie designe un FICHIER .png, pas un dossier.")
    ap.add_argument("--echelle", type=float, default=3.0,
                    help="facteur d'agrandissement du mode --recadrer (defaut 3.0 ; "
                         "2.6 a 4.0 utile, en dessous les accents deviennent ambigus)")
    a = ap.parse_args()
    if a.recadrer:
        try:
            zone = tuple(float(v) for v in a.recadrer.split(","))
            assert len(zone) == 4 and all(0.0 <= v <= 1.0 for v in zone)
            assert zone[0] < zone[2] and zone[1] < zone[3]
        except (ValueError, AssertionError):
            print("--recadrer attend x0,y0,x1,y1 entre 0.0 et 1.0, x0<x1 et y0<y1",
                  file=sys.stderr)
            return 2
        d = os.path.dirname(a.sortie)
        if d:
            os.makedirs(d, exist_ok=True)
        for i, ph in enumerate(a.photos):
            dest = a.sortie if len(a.photos) == 1 else \
                "%s_%02d%s" % (os.path.splitext(a.sortie)[0], i,
                                os.path.splitext(a.sortie)[1] or ".png")
            taille = recadrer(ph, zone, a.echelle, dest)
            print("%s : %dx%d" % (dest, taille[0], taille[1]))
        return 0
    os.makedirs(a.sortie, exist_ok=True)
    total = 0
    for ph in a.photos:
        base = os.path.splitext(os.path.basename(ph))[0]
        for tag in ("G", "D"):
            try:
                bandes = extraire(ph, tag, marge=a.marge)
            except Exception as e:
                print(f"{base}{tag} : ERREUR {e}", file=sys.stderr); continue
            for i in range(0, len(bandes), a.par_planche):
                lot = bandes[i:i + a.par_planche]
                dest = os.path.join(a.sortie, f"{base}{tag}_{i//a.par_planche:02d}.png")
                if planche(lot, dest):
                    print(f"{dest} : {len(lot)} bandeau(x)")
                    total += len(lot)
    print(f"TOTAL : {total} bandeau(x) candidat(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
