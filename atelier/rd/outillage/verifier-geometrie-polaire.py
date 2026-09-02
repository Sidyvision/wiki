#!/usr/bin/env python3
# =============================================================================
# verifier-geometrie-polaire.py — contrôle NUMÉRIQUE de la géométrie polaire
#
#   Chantier INS-15. Versé au dépôt le 2026-09-02 (étape 6 bis du plan visé).
#
#   POURQUOI IL EST ICI ET NON DANS UN BAC À SABLE. Les critères d'acceptation
#   du chantier désignaient d'abord des scripts vivant dans /root/sandbox-rd/,
#   déclaré jetable. Une phase ultérieure — menée par une autre session, ou par
#   celle-ci après nettoyage — aurait trouvé une section « Vérification » dont
#   AUCUNE commande n'existe, et l'épreuve des contrôles ne serait attestée nulle
#   part. C'est la forme même de PRO-01 : une garde qu'on croit tenir parce
#   qu'un rapport l'a dit une fois. D'où le versement.
#
#   Ce script existe pour une raison précise : la justesse d'une scène 3D ne se
#   vérifie pas à l'œil. Il confronte les formules de la scène à des valeurs
#   connues d'avance par la géométrie sphérique — indépendamment de Tilak, qui
#   n'est ici ni invoqué ni cru.
#
#   Épreuve des contrôles (§VII du protocole racine, motif PRO-01) : chaque
#   contrôle est REJOUÉ avec un biais volontaire, et doit alors ÉCHOUER. Un
#   contrôle dont on n'a pas vu l'échec n'est pas vérifié.
#
#   Usage :  python3 atelier/rd/outillage/verifier-geometrie-polaire.py
# =============================================================================

import math
import sys

EPS_DEG = 23.44          # obliquité de l'écliptique (zodiaque.obliquite_deg au dépôt)
ARCTIQUE_DEG = 90.0 - EPS_DEG    # 66.56 — le cercle arctique EST 90 - obliquité
ANNEE_JOURS = 365.24
TOLERANCE_DEG = 0.1

d2r = math.radians
r2d = math.degrees


# --- Les formules, identiques à celles du prototype -------------------------

def declinaison(jour):
    """Déclinaison solaire, jour compté depuis l'équinoxe de printemps.
    Modèle circulaire (orbite supposée circulaire) : suffisant ici, car ce
    qu'on vérifie est la GÉOMÉTRIE de la sphère céleste, pas l'éphéméride."""
    return EPS_DEG * math.sin(2 * math.pi * jour / ANNEE_JOURS)


def base_locale(lat_deg):
    """Repère orthonormé du lieu. Convention de scène : X = est, Y = zénith,
    Z = sud. Retourne (m, e, p) : m = point de l'équateur céleste au méridien
    sud, e = est, p = pôle céleste."""
    phi = d2r(lat_deg)
    m = (0.0, math.cos(phi), math.sin(phi))     # équateur au méridien, côté sud
    e = (1.0, 0.0, 0.0)                          # est
    p = (0.0, math.sin(phi), -math.cos(phi))     # pôle céleste (altitude = phi)
    return m, e, p


def soleil(lat_deg, dec_deg, angle_horaire_deg):
    """Vecteur unitaire du soleil dans le repère de scène.
    L'angle horaire croît vers l'OUEST ; 0 = culmination au méridien sud."""
    m, e, p = base_locale(lat_deg)
    d, H = d2r(dec_deg), d2r(angle_horaire_deg)
    cd, sd, cH, sH = math.cos(d), math.sin(d), math.cos(H), math.sin(H)
    return tuple(cd * cH * m[i] - cd * sH * e[i] + sd * p[i] for i in range(3))


def hauteur(lat_deg, dec_deg, angle_horaire_deg):
    """Hauteur du soleil sur l'horizon, en degrés (négative = sous l'horizon)."""
    v = soleil(lat_deg, dec_deg, angle_horaire_deg)
    return r2d(math.asin(max(-1.0, min(1.0, v[1]))))


def azimut(lat_deg, dec_deg, angle_horaire_deg):
    """Azimut compté depuis le NORD, vers l'est. Nord = -Z, est = +X."""
    v = soleil(lat_deg, dec_deg, angle_horaire_deg)
    return r2d(math.atan2(v[0], -v[2])) % 360.0


# --- Les contrôles ----------------------------------------------------------
#
#   Chaque contrôle rend (nom, ecart_mesure_en_degres, ecart_tolere).
#   Le biais est un décalage volontaire injecté pour éprouver le contrôle.

def c1_hauteur_egale_declinaison(biais=0.0):
    """AU PÔLE, la hauteur du soleil EST sa déclinaison, à toute heure.
    C'est la forme exacte de « les astres tournent en plans horizontaux » :
    la hauteur ne dépend plus de l'angle horaire. Tilak, ch. III, I (2)."""
    pire = 0.0
    for jour in range(0, 366, 7):
        dec = declinaison(jour)
        for H in range(0, 360, 15):
            h = hauteur(90.0 + biais, dec, H)
            pire = max(pire, abs(h - dec))
    return "Pôle : hauteur du soleil = déclinaison, à toute heure", pire, TOLERANCE_DEG


def c2_revolution_uniforme_de_l_azimut(biais=0.0):
    """AU PÔLE, l'azimut du soleil avance UNIFORMÉMENT : 15° par heure, un tour
    complet par 24 h, sans jamais que la hauteur bouge. C'est la « roue de
    potier » de Tilak (ch. III, I (4)) — et c'est ce que « le soleil se lève au
    sud » veut dire au pôle, où TOUTE direction horizontale est le sud.

    PREMIÈRE VERSION FAUSSE, conservée en mémoire. Ce contrôle exigeait d'abord
    que la composante nord du soleil ne soit jamais positive — c'est-à-dire que
    le soleil reste du côté +Z de la scène. Il tombait à 90° d'écart, et il
    avait tort : au pôle exact, le repère d'azimut est DÉGÉNÉRÉ (le méridien
    n'est plus défini), et le soleil parcourt bel et bien les 360° d'azimut. La
    formule « le soleil se lève au sud » est une proposition de géographie, pas
    de trigonométrie : elle dit que l'équateur est dans toutes les directions.
    Le traduire en contrainte sur un axe de la scène était une erreur de
    catégorie — la scène a un +Z, la situation polaire n'en a pas."""
    pire = 0.0
    for jour in range(0, 366, 30):
        dec = declinaison(jour)
        for H in range(0, 360, 15):
            a1 = azimut(90.0 + biais, dec, H)
            a2 = azimut(90.0 + biais, dec, H + 15.0)
            avance = (a2 - a1) % 360.0            # attendu : 15° exactement
            pire = max(pire, abs(avance - 15.0))
    return "Pôle : l'azimut avance de 15°/h, un tour par 24 h (roue de potier)", pire, TOLERANCE_DEG


def c2b_soleil_au_sud_du_zenith(biais=0.0):
    """EN RÉGIME CIRCUM-POLAIRE (sous le pôle, au-dessus du cercle arctique), le
    soleil est toujours AU SUD du zénith : à la culmination, son azimut vaut
    180°. Tilak, ch. III, II (1) — qui note lui-même que ce trait, partagé avec
    la zone tempérée, n'est pas un caractère distinctif. Il est vérifié ici
    parce que c'est le trait qui SÉPARE le régime circum-polaire du régime
    polaire, où l'azimut n'a plus de sens (voir c2)."""
    pire = 0.0
    for lat in (67.0, 70.0, 75.0, 80.0, 89.0):
        for jour in range(0, 366, 30):
            dec = declinaison(jour)
            lat_obs = lat + biais           # le biais DÉPLACE L'OBSERVATEUR, pas le ciel
            if dec >= lat_obs:              # le soleil culminerait au nord du zénith
                pass                        # cas licite sous les tropiques : on le MESURE
            pire = max(pire, abs(azimut(lat_obs, dec, 0.0) - 180.0))
    return "Circum-polaire : à la culmination, le soleil est plein sud", pire, TOLERANCE_DEG


def c3_rasance_au_cercle_arctique(biais=0.0):
    """AU CERCLE ARCTIQUE, au solstice d'été, le soleil RASE l'horizon à minuit :
    hauteur minimale = 0. C'est la définition même du cercle arctique, et c'est
    la borne du régime circum-polaire. Tilak, ch. III, II (3)."""
    lat = ARCTIQUE_DEG + biais
    dec = EPS_DEG                                  # solstice d'été
    h_min = min(hauteur(lat, dec, H) for H in range(0, 360))
    return "Cercle arctique : au solstice, le soleil rase l'horizon (h_min = 0)", abs(h_min), TOLERANCE_DEG


def c4_duree_jour_polaire(biais=0.0):
    """AU PÔLE, le soleil est au-dessus de l'horizon exactement la moitié de
    l'année : un jour de six mois, une nuit de six mois. Tilak, ch. III, I (3).
    Contrôle : écart entre la durée mesurée et 365.24 / 2."""
    lat = 90.0 + biais
    pas = 0.01                       # l'échantillonnage borne l'écart mesurable
    jours_clairs = sum(pas for i in range(int(ANNEE_JOURS / pas))
                       if hauteur(lat, declinaison(i * pas), 0.0) > 0)
    attendu = ANNEE_JOURS / 2
    # écart converti en degrés d'arc annuel, pour rester homogène à la tolérance
    return ("Pôle : le jour dure six mois (et la nuit autant)",
            abs(jours_clairs - attendu) * 360.0 / ANNEE_JOURS, TOLERANCE_DEG)


def c5_secteurs_des_yugas(biais=0.0):
    """La roue du Manvantara : les quatre Yuga en proportion 4:3:2:1, donc en
    secteurs de 144° / 108° / 72° / 36°, somme exacte 360°.
    Source : doctrinal/symboles/manvantara (25 920 / 19 440 / 12 960 / 6 480) ;
    figure au dépôt : raw/assets/Manvantara - Yuga.JPG."""
    durees = [25920, 19440, 12960, 6480]
    total = sum(durees) + biais
    secteurs = [360.0 * d / total for d in durees]
    attendus = [144.0, 108.0, 72.0, 36.0]
    pire = max(abs(a - b) for a, b in zip(secteurs, attendus))
    pire = max(pire, abs(sum(secteurs) - 360.0))
    return "Roue du Manvantara : secteurs 144/108/72/36, somme 360°", pire, 0.001


def c6_grande_annee_est_satya_yuga(biais=0.0):
    """Le Satya-Yuga (25 920 ans) a la durée de la précession des équinoxes.
    C'est la charnière entre la couche polaire et la couche cyclique : le cône
    précessionnel de l'axe du monde accomplit un tour par Satya-Yuga.
    Coïncidence RELEVÉE par la fiche manvantara du dépôt, non inventée ici ;
    l'articulation doctrinale qu'on peut en tirer n'est PAS tranchée (Cmd 3)."""
    satya, precession = 25920, 25920 + biais
    ecart_relatif = abs(satya - precession) / satya
    return "Satya-Yuga = période de précession (25 920 ans)", ecart_relatif * 360.0, 0.001


def c7_aurore_encadree_par_les_seuils(biais=0.0):
    """La durée de l'aurore polaire n'est PAS une constante : elle est fonction du
    seuil crépusculaire adopté. Tilak le dit lui-même (ch. III, p. 78) : « The exact
    duration of this morning or evening twilight is, however, still a matter of
    uncertainty » ; il nomme 16° pour la zone tropicale, « from 18° to 20° » pour les
    hautes latitudes.

    Ce contrôle vérifie que les seuils QU'IL NOMME encadrent la fourchette QU'IL
    ANNONCE (« Dawn lasting from 45 to 60 days ») : 16° -> 43.7 j, 20° -> 59.4 j.

    ⚠ Ce que ce contrôle établit, et pas davantage : la fourchette de Tilak est
    l'image de sa propre hypothèse de seuil. La géométrie ne CONFIRME donc pas son
    chiffre de façon indépendante — elle montre d'où il vient. La formulation
    inverse, d'abord retenue (« la géométrie donne son chiffre sans qu'on ait à le
    croire sur parole »), était trop forte : elle prenait pour une vérification ce
    qui est une cohérence interne."""
    borne_basse = ANNEE_JOURS / (2 * math.pi) * math.asin(16.0 / EPS_DEG)
    borne_haute = ANNEE_JOURS / (2 * math.pi) * math.asin((20.0 + biais) / EPS_DEG)
    # Attendu : borne basse sous 45 j, borne haute au-dessus de 60 j... ou tout près.
    # Tilak annonce 45-60 ; on exige que l'intervalle calculé RECOUVRE cette annonce
    # à moins d'un jour et demi près à chaque bout.
    ecart = max(borne_basse - 45.0, 0.0) + max(60.0 - borne_haute, 0.0)
    return ("Aurore : les seuils 16°-20° de Tilak encadrent ses « 45 to 60 days »",
            ecart, 1.5)


def duree_du_jour(lat_deg, dec_deg):
    """Durée du jour en heures, à latitude et déclinaison données."""
    c = -math.tan(d2r(lat_deg)) * math.tan(d2r(dec_deg))
    if c <= -1: return 24.0
    if c >= 1:  return 0.0
    return 2 * r2d(math.acos(c)) / 15.0


def c8_seconde_station_de_guenon(biais=0.0):
    """GUÉNON DONNE UNE SECONDE STATION, ET ELLE EST CALCULABLE.

    « Atlantide et Hyperborée » (Formes traditionnelles et Cycles cosmiques) :
    « La terre où le soleil faisait le tour de l'horizon sans se coucher devait être
    en effet située bien près du pôle, sinon au pôle même ; il est dit aussi que,
    plus tard, les représentants de la tradition se transportèrent en une région où
    LE JOUR LE PLUS LONG ÉTAIT DOUBLE DU JOUR LE PLUS COURT. »

    Par symétrie annuelle, jour_court = 24 - jour_long : la condition donne 16 h / 8 h,
    donc une latitude unique — 49,07° N. Ce contrôle vérifie que le rapport y vaut
    exactement 2.

    Ce que le contrôle établit : la phrase de Guénon est une SPÉCIFICATION
    GÉOMÉTRIQUE, pas une image. Ce qu'il n'établit pas : où se trouvait cette
    région, ni qu'aucun lieu réel y corresponde — Guénon ne la localise pas, et le
    rendu ne la localisera pas davantage (Cmd 3, Cmd 12)."""
    lat = 49.0704 + biais
    rapport = duree_du_jour(lat, EPS_DEG) / duree_du_jour(lat, -EPS_DEG)
    # écart ramené en degrés pour rester homogène : 1 % d'écart de rapport ~ 1°
    return ("Guénon : « le jour le plus long double du plus court » -> 49,07° N",
            abs(rapport - 2.0) * 100.0, 0.5)


def mois_de_soleil(lat_deg):
    """Nombre de mois de l'année où le soleil paraît, ne serait-ce qu'un instant.
    La nuit continue règne tant que la déclinaison est sous -(90 - latitude) ; sa
    part de l'année vaut 1/2 - arcsin(k)/pi, avec k = (90 - lat)/obliquité borné à 1."""
    k = min(1.0, max(0.0, (90.0 - lat_deg) / EPS_DEG))
    return 12.0 * (0.5 + math.asin(k) / math.pi)


def c9_mois_de_soleil_des_adityas(biais=0.0):
    """LES SEPT ADITYAS. Rig-Veda X, 72, 8-9 : « Des huit fils d'Aditi, nés de son
    corps, elle s'approcha des dieux avec sept, et rejeta Mârtânda. » Tilak lit les
    Adityas comme les MOIS DE SOLEIL (ch. VII), et pose que selon la latitude « the
    months of sunshine will vary from seven to eleven ».

    Ce contrôle vérifie les deux bornes que la géométrie connaît d'avance :
    au pôle, six mois de jour et six de nuit ; au cercle arctique, plus de nuit
    continue du tout, donc douze. La fourchette 7-11 de Tilak tombe alors
    nécessairement ENTRE les deux, c'est-à-dire dans la seule zone circum-polaire.

    PREMIÈRE VERSION FAUSSE, conservée. La part de nuit avait été écrite
    arcsin(k)/pi, ce qui donnait DOUZE mois au pôle — c'est-à-dire un pôle sans nuit.
    La bonne expression est 1/2 - arcsin(k)/pi. L'erreur n'aurait pas été vue à
    l'oeil : elle ne se voyait qu'en contrôlant les deux bornes connues d'avance."""
    ecart = abs(mois_de_soleil(90.0 + biais) - 6.0)
    ecart = max(ecart, abs(mois_de_soleil(ARCTIQUE_DEG - biais) - 12.0))
    return ("Adityas : 6 mois de soleil au pôle, 12 au cercle arctique", ecart, 0.05)


CONTROLES = [c1_hauteur_egale_declinaison, c2_revolution_uniforme_de_l_azimut,
             c2b_soleil_au_sud_du_zenith, c3_rasance_au_cercle_arctique,
             c4_duree_jour_polaire, c5_secteurs_des_yugas,
             c6_grande_annee_est_satya_yuga, c7_aurore_encadree_par_les_seuils,
             c8_seconde_station_de_guenon,
             c9_mois_de_soleil_des_adityas]

# Biais d'épreuve : de quoi fausser CHAQUE contrôle assez pour qu'il tombe.
BIAIS = {c1_hauteur_egale_declinaison: -1.0,       # observateur à 89° au lieu de 90°
         c2_revolution_uniforme_de_l_azimut: -3.0,  # observateur à 87° : l'azimut n'avance plus uniformément
         c2b_soleil_au_sud_du_zenith: -60.0,        # observateur descendu sous les tropiques
         c3_rasance_au_cercle_arctique: -1.0,       # latitude sous le cercle arctique
         c4_duree_jour_polaire: -10.0,             # observateur à 80°
         c5_secteurs_des_yugas: 6480,              # un cinquième Yuga fictif
         c6_grande_annee_est_satya_yuga: 800,       # précession à 26 720 ans
         c7_aurore_encadree_par_les_seuils: -8.0,   # seuil haut ramené à 12°
         c8_seconde_station_de_guenon: -4.0,        # observateur descendu à 45°
         c9_mois_de_soleil_des_adityas: -3.0}       # les deux bornes déplacées de 3°


def passe(titre, biais_actif):
    print("\n" + titre)
    print("-" * len(titre))
    resultats = []
    for f in CONTROLES:
        biais = BIAIS[f] if biais_actif else 0.0
        nom, ecart, tol = f(biais)
        ok = ecart <= tol
        resultats.append(ok)
        print("  {}  {:<62} écart {:.4f}° (toléré {:.3f}°)".format(
            "OK  " if ok else "ÉCHEC", nom, ecart, tol))
    return resultats


def main():
    print("=" * 92)
    print("INS-15 — contrôle numérique de la géométrie polaire")
    print("obliquité {}° · cercle arctique {}° · tolérance {}°".format(
        EPS_DEG, ARCTIQUE_DEG, TOLERANCE_DEG))
    print("=" * 92)

    vrais = passe("PASSE 1 — géométrie réelle : tout doit PASSER", False)
    faux = passe("PASSE 2 — épreuve des contrôles : tout doit ÉCHOUER (§VII, motif PRO-01)", True)

    print("\n" + "=" * 92)
    tout_bon = all(vrais) and not any(faux)
    if tout_bon:
        print("VERDICT : {} contrôles passent sur la géométrie réelle, et les {} "
              "tombent quand on la fausse.".format(len(vrais), len(faux)))
        print("          Les contrôles observent donc quelque chose de réel.")
    else:
        if not all(vrais):
            print("VERDICT : la géométrie est FAUSSE — contrôle(s) en échec passe 1.")
        if any(faux):
            print("VERDICT : contrôle(s) INOPÉRANT(S) — passe 2 aurait dû tout faire tomber.")
    print("=" * 92)

    # Quelques valeurs remarquables, pour la spec.
    print("\nValeurs dérivées (elles alimenteront les critères d'acceptation du spec.md) :")
    print("  · Aurore polaire, selon le SEUIL crépusculaire adopté :")
    for seuil in (16, 18, 20):
        j = ANNEE_JOURS / (2 * math.pi) * math.asin(seuil / EPS_DEG)
        print("        seuil -{:2d}°  ->  {:5.1f} jours".format(seuil, j))
    print("    Tilak nomme ces trois seuils (16° en zone tropicale, « from 18° to 20° »")
    print("    aux hautes latitudes) et annonce « Dawn lasting from 45 to 60 days ».")
    print("    Sa fourchette est donc l'IMAGE de son hypothèse de seuil : la géométrie")
    print("    montre d'où vient son chiffre, elle ne le confirme pas indépendamment.")
    print("  · Culmination au pôle au solstice d'été       : {:.2f}°".format(hauteur(90, EPS_DEG, 0)))
    print("  · Culmination au cercle arctique, solstice    : {:.2f}°".format(hauteur(ARCTIQUE_DEG, EPS_DEG, 0)))
    print("  · Seconde station (Guénon, « jour double du plus court ») : {:.2f}° N"
          .format(49.0704))
    print("        jour au solstice d'été {:.2f} h · d'hiver {:.2f} h"
          .format(duree_du_jour(49.0704, EPS_DEG), duree_du_jour(49.0704, -EPS_DEG)))
    print("  · Mois de soleil (Adityas) — Tilak annonce « from seven to eleven » :")
    for m in (7, 8, 9, 10, 11):
        lo, hi = ARCTIQUE_DEG, 90.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if mois_de_soleil(mid) > m: lo = mid
            else: hi = mid
        print("        {:2d} mois  ->  {:5.2f}° N".format(m, (lo + hi) / 2))
    print("  · Secteurs de la roue du Manvantara           : {}".format(
        " / ".join("{:.0f}°".format(360.0 * d / 64800) for d in (25920, 19440, 12960, 6480))))

    return 0 if tout_bon else 1


if __name__ == "__main__":
    sys.exit(main())
