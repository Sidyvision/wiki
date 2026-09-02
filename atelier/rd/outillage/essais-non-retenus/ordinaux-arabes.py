"""Analyseur d'ordinaux arabes ecrits en toutes lettres, tolerant a l'OCR.
Bac a sable : mis au point contre l'index des Futuhat (p.27-46) avant emploi.
"""
import re

# Normalisation : l'OCR confond les formes de alif/ya/ta, et insere des espaces
# au milieu des mots ('العشيرون' pour 'العشرون', 'الثالك' pour 'الثالث').
def norm(s):
    s = re.sub(r'[\u064B-\u0652\u0670\u200e\u200f]', '', s)   # diacritiques, marques bidi
    s = s.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
    s = s.replace('ى', 'ي').replace('ة', 'ه')
    return s

def variants(s):
    """Lectures alternatives d'un mot OCR : le kaf final est le grand ambigu
    ('الثالك' = الثالث, mais 'الاوك' = الاول). On ne substitue pas, on enumere —
    meme lecon que AMBIG pour les romains."""
    s = norm(s)
    out = {s}
    if 'ك' in s:
        out.add(s.replace('ك', 'ث'))
        out.add(s.replace('ك', 'ل'))
    return out

# Unites 1..10 : plusieurs graphies OCR par valeur.
# ATTENTION : en composition (11, 21, 31...), l'unite 1 n'est PAS 'الاول'
# mais 'الحادي' — omission qui coutait 343 babs au premier essai.
UNITS = {
    1:  ['الاول', 'الاولى', 'اول', 'الحادي', 'الحادى', 'الخادى', 'الحاد ى',
         'الحادئ', 'الجادى', 'الحإدى', 'حادى'],
    2:  ['الثاني', 'الثانى', 'الثاق', 'الثاى', 'الثائي', 'الثانئ', 'الثاتى',
         'الثاثى', 'الثانئ', 'الناك', 'الثاك'],
    3:  ['الثالث', 'الثالت', 'الثلث', 'الثالك', 'الثالن', 'الثالب'],
    4:  ['الرابع', 'الراببع', 'الرابيع', 'لرابع', 'الرايع', 'الرابءع', 'الراب'],
    5:  ['الخامس', 'الحامس', 'الهامس', 'الخاس', 'الحاس', 'خامس',
         'الخادس', 'الحامسر'],
    6:  ['السادس', 'الساد س', 'السادسر', 'السادن'],
    7:  ['السابع', 'السابيع', 'لسابع', 'السايع', 'السالع'],
    8:  ['الثامن', 'الثامنن', 'الثانن', 'الثامرن'],
    9:  ['التاسع', 'الناسع', 'التاسم', 'التسع', 'النسع', 'المؤف', 'الموف',
         'الموؤ', 'المو ف'],
    10: ['العاشر', 'العاشس', 'العاش'],
}
TEENS_MARK = ['عشر', 'عشسر', 'عشير', 'عشرر', 'عشس', 'عشمر', 'عثمر', 'عشسير']
TENS = {
    20: ['العشرون', 'العشرين', 'العشيرون', 'العشرون', 'عشرين', 'عشرون', 'العشيرين'],
    30: ['الثلاثون', 'الثلاثين', 'الثلانون', 'الثلثون', 'ثلاثين', 'الثلابون', 'الثلانين'],
    40: ['الاربعون', 'الاربعين', 'الار بعون', 'اربعين', 'الاربيعون', 'لاربعون'],
    50: ['الخمسون', 'الخمسين', 'الحسون', 'الجسون', 'الحمسون', 'الخسون', 'اللحسون', 'الحسين'],
    60: ['الستون', 'الستين', 'السنون', 'الستتون'],
    70: ['السبعون', 'السبعين', 'السبعو ن', 'السبعين'],
    80: ['الثمانون', 'الثمانين', 'المانون', 'العانون', 'الثمانو ن', 'المانو'],
    90: ['التسعون', 'التسعين', 'النسعون', 'التسعو ن'],
}
HUNDREDS = {
    100: ['ماثه', 'مائه', 'ماته', 'مئه'],
    200: ['مائتان', 'مائتين', 'ماثتان', 'مائتنان', 'مائتيين', 'ماتتان'],
    300: ['ثلثمائه', 'ثلثماثه', 'ثلاثمائه', 'ثلئمائه', 'ثلهائه', 'ثلثمائة', 'ثلئانه', 'ثلها نه'],
    400: ['اربعمائه', 'ار بعمائه', 'اربعماثه', 'ار بعماثه', 'ربعمائه'],
    500: ['خمسمائه', 'خسمائه', 'حمسمائه', 'خسماثه'],
}

def _mk(table):
    out = {}
    for val, forms in table.items():
        for f in forms:
            out[norm(f).replace(' ', '')] = val
    return out

U, T, H = _mk(UNITS), _mk(TENS), _mk(HUNDREDS)
TEENS_N = {norm(x).replace(' ', '') for x in TEENS_MARK}

def _components(txt):
    """Composants detectes : (unite, dizaine, centaine, teen).
    Teste toutes les lectures du kaf ambigu."""
    unit = ten = hund = None
    teen = False
    for s in variants(txt.replace(' ', '')):
        if unit is None:
            for form, val in sorted(U.items(), key=lambda kv: -len(kv[0])):
                if form in s:
                    unit = val; break
        if not teen:
            for form in sorted(TEENS_N, key=len, reverse=True):
                if form in s:
                    teen = True; break
        if ten is None:
            for form, val in sorted(T.items(), key=lambda kv: -len(kv[0])):
                if form in s:
                    ten = val; break
        if hund is None:
            for form, val in sorted(H.items(), key=lambda kv: -len(kv[0])):
                if form in s:
                    hund = val; break
    return unit, ten, hund, teen

def candidates(txt, maxnum=560):
    """Toutes les valeurs plausibles d'un ordinal arabe OCR-bruite.

    Principe (cf. rom_candidates pour les romains) : n'elargir QUE sur ce que
    l'OCR a pu detruire, jamais sur ce qu'il a lu. Elargir a l'aveugle rend
    toute ligne compatible avec tout rang et fait deriver la contrainte de
    sequence — c'est l'echec constate au premier essai (bab 1 accroche au
    onzieme bab de l'index).

    Regle : une dizaine/centaine n'est supposee perdue que si le texte porte
    la trace d'une conjonction ('و' isole, '...ون'/'...ين', 'مائة') sans
    qu'on ait su la lire.
    """
    unit, ten, hund, teen = _components(txt)
    if unit is None and ten is None and hund is None and not teen:
        return set()
    s = norm(txt).replace(' ', '')

    bases = set()
    if unit is not None and teen:
        bases.add(10 + unit)          # 'الخامس عشر' = 15
    elif teen:
        bases.add(10)
    if unit is not None and ten is not None:
        bases.add(ten + unit)         # 'الحادى والخمسون' = 51
    if unit is not None and ten is None and not teen:
        bases.add(unit)
    if ten is not None and unit is None:
        bases.add(ten)
    if not bases:
        return set()

    # Dizaine possiblement perdue : seulement si une conjonction traine.
    if ten is None and not teen and unit is not None and re.search(r'و', s):
        bases |= {t + unit for t in range(10, 100, 10)}

    hund_opts = {0}
    if hund is not None:
        hund_opts = {hund}
    elif re.search(r'مائ|ماث|مئ|مانه|ماته', s):
        hund_opts = {100, 200, 300, 400, 500}

    out = {h + b for b in bases for h in hund_opts}
    return {n for n in out if 1 <= n <= maxnum}

def parse_ordinal(txt, maxnum=560):
    """Lecture 'stricte' : seuls les composants effectivement lus."""
    unit, ten, hund, teen = _components(txt)
    if unit is None and ten is None and hund is None:
        return None
    n = 0
    if hund: n += hund
    if ten:  n += ten
    if unit:
        n += 10 + unit if (teen and not ten) else unit
    elif teen and not ten:
        n += 10
    return n if 1 <= n <= maxnum else None
