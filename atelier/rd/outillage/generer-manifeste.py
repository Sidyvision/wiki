#!/usr/bin/env python3
# =============================================================================
# generer-manifeste.py — Générateur déterministe du wiki-manifest (schéma v0.2.5)
#
#   Phase 1 de l'Instrument de la Tradition Primordiale.
#   Croise deux couches :
#     1. la vérité doctrinale : les fiches de doctrinal/ (labels, existence,
#        discernements « en cours ») — LECTURE SEULE ;
#     2. la déclaration applicative : atelier/rd/instrument/instrument-donnees.yaml
#        (nœuds, degrés verticaux, ancrages).
#   Produit : atelier/rd/instrument/wiki-manifest.json
#
#   AUCUN LLM dans la boucle. Parse mécanique uniquement.
#   Validations bloquantes : voir la spec (spec-generateur-manifeste.md §5).
#
#   Usage :
#     python3 generer-manifeste.py --repo /root/wiki
#     python3 generer-manifeste.py --repo /root/regression-test/sandbox   # bac à sable
# =============================================================================

import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # PyYAML : apt install python3-yaml
except ImportError:
    sys.exit("ERREUR : PyYAML manquant. Installer avec : apt install python3-yaml")

# --- Constantes du schéma v0.2.5 --------------------------------------------
#
#   v0.2.5 (2026-08-25) : propage le bloc `maisons:` d'instrument-donnees.yaml
#     (les 12 maisons astrologiques — thème, terme arabe, qualité
#     cardinale/succédante/mutable). Domification GÉNÉRIQUE : ni époque ni
#     lieu dans le manifeste, donc aucun thème daté individuel — seulement la
#     table générique des 12 maisons, telle que sourcée. Motif : demande Sidy
#     (bezel zodiacal de l'Instrument gradué « par cran — signe, maison,
#     etc. ») ; source désignée par Sidy : doctrinal/sources/fin-des-temps-
#     modernes-ilm-al-nujum-bases-mahdi-rouge.md (déjà au dépôt, 2026-07-01 —
#     source également des « Angles de l'Espace » déjà rendus). Validation
#     dédiée : liste de 12, `theme` non vide, `type` dans l'énumération
#     cardinale/succedante/mutable si fourni.
#
#   v0.2.4 (2026-08-20) : un ancrage peut désormais désigner, en source comme
#     en cible, soit un nœud (`noeuds:`), soit un domaine de registre
#     (`registres[].domaines[]`) — même espace d'identifiants, même validation.
#     Motif : un ancrage entre un nœud universel et un domaine de registre peut
#     être déjà établi par un discernement clos (ex. Homme Universel ↔
#     Vaishwânara, verdict du 2026-07-26) sans qu'aucune correspondance
#     inter-registres ne soit posée pour autant — seul CE domaine précis est
#     visé, jamais le registre entier. Les collisions d'id entre nœud et
#     domaine restent bloquantes.
#
#   v0.2.5 (2026-08-29) : garde inter-registres. Un ancrage dont les DEUX
#     extrémités sont des domaines de registres DISTINCTS exige désormais une
#     fiche `doctrinal/discernement/` en source — refus bloquant sinon.
#     Motif : le Cmd 3 réserve à un discernement tranché tout lien structurel
#     entre concepts de traditions distinctes ; la règle était écrite dans le
#     protocole et affirmée « appliquée par l'outil » (instruction phase 3
#     §2), mais l'outil ne l'appliquait en fait qu'au cas `rang`+`degres`
#     simultanés, jamais aux ancrages. Écart relevé le 2026-08-29 en préparant
#     la mise en regard du Majmaʿ al-Bahrayn (trois candidats d'ancrage
#     inter-registres alors sur la table, aucun tranché). Même forme que la
#     garde subversion/parodie. NE VISE PAS le cas nœud → domaine (v0.2.4).
#     Sortie inchangée sur les données réelles : aucun ancrage inter-registres
#     n'était déclaré (44 nœuds, 11 ancrages, 0 erreur avant comme après).
#
#   v0.2.3 (2026-08-20) : propage le bloc `registres:` — partitions de l'unique
#     axe vertical, une par tradition (voir instrument-donnees.yaml v0.4.0).
#     Validation dédiée : un domaine ne peut porter à la fois `degres` et
#     `rang`, ce qui reviendrait à déclarer en donnée une correspondance point
#     à point non tranchée (Cmd 3).
#
#   v0.2.2 (2026-08-20) : le bloc `zodiaque:` d'instrument-donnees.yaml (degrés
#     du falak al-burūj/al-manāzil, obliquité, époque de référence, signes) est
#     désormais propagé dans le manifeste (clé "zodiaque"), avec validations
#     mécaniques dédiées (§ci-dessous). Auparavant déclaré en YAML mais jamais
#     émis : le prototype le transcrivait à la main sans passer par le
#     manifeste — écart signalé dans rd/instrument/2026-08-20_etat-avancement-
#     pistes-developpement.md §5, fermé ici sur demande de Sidy.

SCHEMA_VERSION = "0.2.5"
TYPES_ANCRAGE = {"equivalence", "complementarite", "subversion", "parodie"}
ETATS_ANCRAGE = {"etabli", "suggere", "identifie"}
DIRECTIONNALITES = {"none", "ascendant", "descendant"}
TYPES_MAISON = {"cardinale", "succedante", "mutable"}

# Frontmatter : bloc YAML entre deux lignes `---` en tête de fichier.
RE_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
# Bloc 🔍 normalisé des discernements : ligne « **Statut** : en cours | validée | invalidée »
RE_STATUT_DISCERNEMENT = re.compile(
    r"\*\*Statut\*\*\s*:\s*(en cours|valid[ée]e|invalid[ée]e)", re.I
)
# Wikilink : [[chemin/ou/slug]] — on ne garde que le slug final pour comparer.
RE_WIKILINK = re.compile(r"\[\[([^\]|]+)")


# --- Petites fonctions utilitaires -------------------------------------------

def lire_frontmatter(chemin: Path):
    """Retourne (frontmatter dict, corps str) d'une fiche, ou (None, texte) si absent/invalide."""
    texte = chemin.read_text(encoding="utf-8", errors="replace")
    m = RE_FRONTMATTER.match(texte)
    if not m:
        return None, texte
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None, texte
    return (fm if isinstance(fm, dict) else None), texte[m.end():]


def slug_de(wikilink_ou_chemin: str) -> str:
    """« doctrinal/symboles/barzakh » ou « [[…/barzakh]] » → « barzakh »."""
    s = wikilink_ou_chemin.strip().strip("[]").split("|")[0]
    return s.rstrip("/").split("/")[-1].removesuffix(".md")


def sha_git(repo: Path) -> str:
    """SHA du commit courant du dépôt, ou « inconnu » hors dépôt git."""
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        return r.stdout.strip() if r.returncode == 0 else "inconnu"
    except Exception:
        return "inconnu"


# --- Cœur du générateur -------------------------------------------------------

def indexer_fiches_doctrinales(repo: Path) -> dict:
    """Index {slug: (chemin relatif, frontmatter)} de toutes les fiches doctrinal/."""
    index = {}
    for f in sorted((repo / "doctrinal").rglob("*.md")):
        fm, _ = lire_frontmatter(f)
        index[f.stem] = (f.relative_to(repo).as_posix(), fm or {})
    return index


def discernements_en_cours(repo: Path) -> list:
    """Liste [(chemin relatif sans .md, {slugs cibles des cross_links})] des
    discernements dont le bloc 🔍 porte « Statut : en cours »."""
    resultats = []
    dossier = repo / "doctrinal" / "discernement"
    if not dossier.is_dir():
        return resultats
    for f in sorted(dossier.glob("*.md")):
        fm, corps = lire_frontmatter(f)
        m = RE_STATUT_DISCERNEMENT.search(corps)
        if not m or "en cours" not in m.group(1).lower():
            continue
        cibles = set()
        for lien in (fm or {}).get("cross_links", []) or []:
            if isinstance(lien, str):
                cibles.add(slug_de(lien))
        chemin_sans_ext = f.relative_to(repo).as_posix().removesuffix(".md")
        resultats.append((chemin_sans_ext, cibles))
    return resultats


def valider_zodiaque(zodiaque: dict, decl_noeuds: list, erreurs: list, avertissements: list):
    """Valide le bloc `zodiaque:` (peut être absent) et retourne la valeur à
    inscrire dans le manifeste, ou None si absente/invalide au point de ne
    rien produire. Erreurs bloquantes limitées aux malformations structurelles
    (types) ; le reste (12 signes attendus, degrés cohérents avec un nœud
    déclaré) reste un avertissement — ce ne sont pas des invariants du schéma,
    seulement des indices de dérive possible."""
    if not zodiaque:
        return None
    if not isinstance(zodiaque, dict):
        erreurs.append("zodiaque : doit être un mapping (dict)")
        return None

    degres_declares = {d.get("degre_vertical") for d in decl_noeuds
                        if d.get("degre_vertical") is not None}

    for cle in ("degre_falak_al_buruj", "degre_falak_al_manazil"):
        v = zodiaque.get(cle)
        if v is not None and not isinstance(v, int):
            erreurs.append(f"zodiaque.{cle} : doit être un entier ou null (reçu {v!r})")
        elif isinstance(v, int) and v not in degres_declares:
            avertissements.append(
                f"zodiaque.{cle} = {v} : aucun nœud déclaré ne porte ce degre_vertical"
            )

    obliquite = zodiaque.get("obliquite_deg")
    if obliquite is not None and not isinstance(obliquite, (int, float)):
        erreurs.append(f"zodiaque.obliquite_deg : doit être numérique (reçu {obliquite!r})")

    signes = zodiaque.get("signes")
    if signes is not None:
        if not isinstance(signes, list):
            erreurs.append("zodiaque.signes : doit être une liste")
        else:
            if len(signes) != 12:
                avertissements.append(
                    f"zodiaque.signes : {len(signes)} entrée(s) déclarée(s), 12 attendues"
                )
            for i, s in enumerate(signes):
                if not isinstance(s, dict) or not str(s.get("label", "")).strip():
                    erreurs.append(f"zodiaque.signes[{i}] : doit porter un « label » non vide")

    return zodiaque


def valider_maisons(maisons, erreurs, avertissements):
    """Valide le bloc `maisons:` (peut être absent) et retourne la valeur à
    inscrire dans le manifeste, ou None si absente/invalide. Domification
    GÉNÉRIQUE (aucune époque/lieu dans le manifeste, donc aucun thème daté
    individuel) : seulement la table des 12 maisons et leur qualité. Le
    nombre attendu (12) reste un avertissement, pas une erreur bloquante —
    ce n'est pas un invariant du schéma, seulement un indice de dérive."""
    if not maisons:
        return None
    if not isinstance(maisons, list):
        erreurs.append("maisons : doit être une liste")
        return None
    if len(maisons) != 12:
        avertissements.append(
            f"maisons : {len(maisons)} entrée(s) déclarée(s), 12 attendues"
        )
    for i, m in enumerate(maisons):
        if not isinstance(m, dict) or not str(m.get("theme", "")).strip():
            erreurs.append(f"maisons[{i}] : doit porter un « theme » non vide")
            continue
        t = m.get("type")
        if t is not None and t not in TYPES_MAISON:
            erreurs.append(
                f"maisons[{i}] : type invalide ({t!r}) — attendu {sorted(TYPES_MAISON)}"
            )
    return maisons


AXES_REGISTRE = {"principal", "parallele"}


def valider_registres(registres, fiches: dict, erreurs: list, avertissements: list):
    """Valide le bloc `registres:` (schéma v0.2.3) et retourne la valeur à
    inscrire au manifeste, ou None si absent.

    Un registre déclare comment UNE tradition partitionne l'axe vertical unique.
    Deux formes de domaine, exclusives l'une de l'autre :
      - `degres: [a, b]` — la tradition situe le domaine sur l'échelle des 38
        degrés (elle en donne les bornes) ;
      - `rang: n` (+ `colonne:`) — la tradition donne un ordre le long de l'axe,
        sans échelle de degrés. Le rendu répartit alors le registre sur
        l'étendue de l'axe sans prétendre l'aligner sur les degrés.

    Un domaine portant LES DEUX formes est refusé : ce serait déclarer en
    donnée une correspondance point à point que la tradition ne donne pas —
    exactement ce que le Cmd 3 réserve à une fiche `discernement` tranchée.
    """
    if not registres:
        return None
    if not isinstance(registres, list):
        erreurs.append("registres : doit être une liste")
        return None

    vus_registre, vus_domaine = set(), set()
    for i, reg in enumerate(registres):
        ctx = f"registres[{i}]"
        if not isinstance(reg, dict):
            erreurs.append(f"{ctx} : doit être un mapping"); continue
        rid = str(reg.get("id", "")).strip()
        ctx = f"registre « {rid or i} »"
        if not rid:
            erreurs.append(f"{ctx} : « id » requis"); continue
        if rid in vus_registre:
            erreurs.append(f"{ctx} : id de registre dupliqué"); continue
        vus_registre.add(rid)

        if not str(reg.get("label", "")).strip():
            erreurs.append(f"{ctx} : « label » requis")

        axe = reg.get("axe")
        if axe not in AXES_REGISTRE:
            erreurs.append(f"{ctx} : « axe » doit valoir {sorted(AXES_REGISTRE)} (reçu {axe!r})")

        fiche = str(reg.get("fiche", "")).strip()
        if not fiche:
            erreurs.append(f"{ctx} : « fiche » requise (traçabilité, Cmd 5)")
        elif slug_de(fiche) not in fiches:
            erreurs.append(f"{ctx} : fiche doctrinale introuvable : {fiche}")

        domaines = reg.get("domaines")
        if not isinstance(domaines, list) or not domaines:
            erreurs.append(f"{ctx} : « domaines » doit être une liste non vide"); continue

        for j, d in enumerate(domaines):
            dctx = f"{ctx}, domaine[{j}]"
            if not isinstance(d, dict):
                erreurs.append(f"{dctx} : doit être un mapping"); continue
            did = str(d.get("id", "")).strip()
            if not did:
                erreurs.append(f"{dctx} : « id » requis"); continue
            dctx = f"{ctx}, domaine « {did} »"
            if did in vus_domaine:
                erreurs.append(f"{dctx} : id de domaine dupliqué"); continue
            vus_domaine.add(did)
            if not str(d.get("label", "")).strip():
                erreurs.append(f"{dctx} : « label » requis")

            degres, rang = d.get("degres"), d.get("rang")
            if degres is not None and rang is not None:
                erreurs.append(
                    f"{dctx} : « degres » et « rang » sont exclusifs — porter les deux "
                    f"déclarerait une correspondance point à point non tranchée (Cmd 3)"
                ); continue
            if degres is None and rang is None:
                erreurs.append(f"{dctx} : « degres » ou « rang » requis"); continue

            if degres is not None:
                if (not isinstance(degres, list) or len(degres) != 2
                        or not all(isinstance(v, int) for v in degres)):
                    erreurs.append(f"{dctx} : « degres » doit être [debut, fin] entiers")
                elif degres[0] > degres[1]:
                    erreurs.append(f"{dctx} : « degres » — début {degres[0]} > fin {degres[1]}")
            else:
                if not isinstance(rang, int) or rang < 1:
                    erreurs.append(f"{dctx} : « rang » doit être un entier ≥ 1")

        # Cohérence de forme : un registre mélangeant les deux formes est
        # légitime en principe, mais assez inhabituel pour mériter un signalement.
        formes = {("degres" if d.get("degres") is not None else "rang")
                  for d in domaines if isinstance(d, dict)}
        if len(formes) > 1:
            avertissements.append(
                f"{ctx} : domaines de formes mêlées (degres + rang) — vérifier l'intention"
            )

    return registres


def generer(repo: Path, chemin_donnees: Path, chemin_sortie: Path) -> int:
    erreurs, avertissements = [], []

    # 1. Charger la déclaration applicative.
    if not chemin_donnees.is_file():
        sys.exit(f"ERREUR : fichier déclaratif introuvable : {chemin_donnees}")
    donnees = yaml.safe_load(chemin_donnees.read_text(encoding="utf-8")) or {}
    decl_noeuds = donnees.get("noeuds", []) or []
    decl_ancrages = donnees.get("ancrages", []) or []
    decl_zodiaque = donnees.get("zodiaque") or {}
    decl_maisons = donnees.get("maisons") or []
    decl_registres = donnees.get("registres") or []

    # 2. Indexer la vérité doctrinale.
    fiches = indexer_fiches_doctrinales(repo)
    en_cours = discernements_en_cours(repo)

    # 3. Construire les nœuds.
    noeuds, ids = [], set()
    for d in decl_noeuds:
        tradition = d.get("tradition", "").strip()
        fiche = d.get("fiche", "").strip()          # ex. doctrinal/symboles/barzakh
        slug = slug_de(fiche)
        # id : déclaré si fourni (cas des nœuds-degrés partageant une même fiche
        # source), sinon <tradition>/<slug de la fiche>.
        node_id = d.get("id") or f"{tradition}/{slug}"

        if not tradition or not fiche:
            erreurs.append(f"nœud incomplet (tradition/fiche requis) : {d}")
            continue
        if node_id in ids:
            erreurs.append(f"id de nœud dupliqué : {node_id}")
            continue
        if slug not in fiches:
            erreurs.append(f"fiche doctrinale introuvable pour le nœud {node_id} : {fiche}")
            continue

        chemin_rel, fm = fiches[slug]
        # Libellé : déclaré si fourni (idem), sinon le title de la fiche
        # (jamais retapé à la main).
        label = d.get("label") or fm.get("title") or slug

        # question_ouverte : premier discernement « en cours » qui pointe ce slug.
        question = False
        for chemin_disc, cibles in en_cours:
            if slug in cibles:
                question = f"[[{chemin_disc}]]"
                break

        ids.add(node_id)
        noeuds.append({
            "id": node_id,
            "tradition": tradition,
            "label": label,
            "source": f"[[{chemin_rel.removesuffix('.md')}]]",
            "degre_vertical": d.get("degre_vertical", None),
            "question_ouverte": question,
            "ancrages": [],
        })
    par_id = {n["id"]: n for n in noeuds}

    # 3 bis. Valider les registres AVANT les ancrages : un domaine de registre
    # peut être source ou cible d'un ancrage (v0.2.4) — ses identifiants
    # doivent donc rejoindre `par_id` avant que la boucle des ancrages ne
    # s'exécute. Une collision d'id entre un nœud et un domaine est bloquante.
    registres_valides = valider_registres(decl_registres, fiches, erreurs, avertissements)
    # Registre d'appartenance de chaque domaine — sert à la garde
    # inter-registres de la boucle des ancrages (v0.2.5, voir §4).
    registre_de_domaine = {}
    for reg in (registres_valides or []):
        if not isinstance(reg, dict):
            continue
        rid = str(reg.get("id", "")).strip()
        for d in (reg.get("domaines") or []):
            if not isinstance(d, dict):
                continue
            did = str(d.get("id", "")).strip()
            if not did:
                continue
            if did in par_id:
                erreurs.append(f"id « {did} » : collision entre un nœud et un domaine de registre")
                continue
            d.setdefault("ancrages", [])
            par_id[did] = d
            registre_de_domaine[did] = rid

    # 4. Valider et rattacher les ancrages (stockage à sens unique sur la source,
    # nœud ou domaine de registre — même espace d'identifiants, v0.2.4).
    for a in decl_ancrages:
        src, typ = a.get("noeud", ""), a.get("type", "")
        etat = a.get("etat", "")
        cible = a.get("cible", None)
        direction = a.get("directionnalite", "none")
        source_doc = a.get("source", None)
        contexte = f"ancrage {src} → {cible} ({typ}/{etat})"

        if src not in par_id:
            erreurs.append(f"{contexte} : source non déclarée (ni nœud, ni domaine de registre)"); continue
        if typ not in TYPES_ANCRAGE:
            erreurs.append(f"{contexte} : type invalide"); continue
        if etat not in ETATS_ANCRAGE:
            erreurs.append(f"{contexte} : etat invalide"); continue
        if direction not in DIRECTIONNALITES:
            erreurs.append(f"{contexte} : directionnalite invalide"); continue
        if cible is not None and cible not in par_id:
            erreurs.append(f"{contexte} : cible non déclarée (ni nœud, ni domaine de registre)"); continue
        if etat == "etabli" and not source_doc:
            erreurs.append(f"{contexte} : un ancrage etabli DOIT être sourcé (Cmd 5)"); continue
        if typ in ("subversion", "parodie") and cible is not None:
            # Correctif waswâs/Qliphoth (architecture v0.2 §2/§6) : jamais de pont
            # inter-traditions structurel — cible non nulle SEULEMENT si un
            # discernement l'a spécifiquement établi.
            if not (source_doc and "discernement" in str(source_doc)):
                erreurs.append(
                    f"{contexte} : subversion/parodie avec cible exige une fiche "
                    f"doctrinal/discernement/ en source (correctif v0.2 §2)"
                ); continue
        # Garde inter-registres (v0.2.5, Cmd 3) : un ancrage dont les DEUX
        # extrémités sont des domaines de registres DISTINCTS déclare une
        # correspondance structurelle entre deux traditions — ce que le Cmd 3
        # réserve à une fiche `discernement` tranchée. Même forme que la garde
        # subversion/parodie ci-dessous. Ne vise PAS le cas nœud → domaine
        # (ex. Homme Universel ↔ Vaishwânara, v0.2.4) : un nœud universel n'est
        # pas un registre, et ce cas reste couvert par sa propre source.
        reg_src = registre_de_domaine.get(src)
        reg_cible = registre_de_domaine.get(cible) if cible is not None else None
        if reg_src and reg_cible and reg_src != reg_cible:
            if not (source_doc and "discernement" in str(source_doc)):
                erreurs.append(
                    f"{contexte} : ancrage inter-registres ({reg_src} → {reg_cible}) "
                    f"exige une fiche doctrinal/discernement/ en source (Cmd 3)"
                ); continue
        if direction != "none" and typ != "complementarite":
            avertissements.append(f"{contexte} : directionnalite sur un type non-complementarite")
        if source_doc and slug_de(str(source_doc)) not in fiches:
            avertissements.append(f"{contexte} : fiche source introuvable au dépôt : {source_doc}")

        par_id[src]["ancrages"].append({
            "type": typ,
            "etat": etat,
            "directionnalite": direction,
            "cible": cible,
            "source": source_doc,
            "note": a.get("note", ""),
        })

    # 5. Valider et intégrer le bloc zodiaque (indépendant des nœuds/ancrages/registres).
    zodiaque_valide = valider_zodiaque(decl_zodiaque, decl_noeuds, erreurs, avertissements)

    # 5 bis. Valider et intégrer le bloc maisons (indépendant, domification générique).
    maisons_valide = valider_maisons(decl_maisons, erreurs, avertissements)

    # 6. Rapport et sortie.
    for w in avertissements:
        print(f"⚠ AVERTISSEMENT : {w}")
    if erreurs:
        for e in erreurs:
            print(f"✗ ERREUR : {e}")
        print(f"\nVERDICT : {len(erreurs)} erreur(s) — manifeste NON produit.")
        return 1

    manifeste = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.datetime.now(datetime.timezone.utc)
                        .isoformat(timespec="seconds"),
        "source_commit": sha_git(repo),
        "nodes": noeuds,
    }
    if zodiaque_valide is not None:
        manifeste["zodiaque"] = zodiaque_valide
    if maisons_valide is not None:
        manifeste["maisons"] = maisons_valide
    if registres_valides is not None:
        manifeste["registres"] = registres_valides
    chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
    chemin_sortie.write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    # v0.2.5 : compter AUSSI les ancrages portés par un domaine de registre.
    # Le compteur ne sommait que les nœuds : depuis l'ouverture des ancrages
    # inter-registres (2026-08-29), il masquait la moitié du total, ce qui
    # contredit la règle de vérification mécanique indépendante (§VIII.2 du
    # protocole racine : ne jamais se fier à l'auto-rapport). Affichage seul,
    # le manifeste produit était correct.
    nb_ancrages = sum(len(n["ancrages"]) for n in noeuds) + sum(
        len(d.get("ancrages") or [])
        for reg in (registres_valides or [])
        for d in (reg.get("domaines") or [])
    )
    print(f"✓ Manifeste produit : {chemin_sortie}")
    print(f"  {len(noeuds)} nœud(s), {nb_ancrages} ancrage(s), "
          f"zodiaque {'inclus' if zodiaque_valide is not None else 'absent'}, "
          f"maisons {'incluses' if maisons_valide is not None else 'absentes'}, "
          f"{len(registres_valides or [])} registre(s), "
          f"{len(avertissements)} avertissement(s), commit {manifeste['source_commit'][:12]}")
    return 0


# --- Point d'entrée -----------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Générateur du wiki-manifest (v0.2.1), déterministe.")
    p.add_argument("--repo", default="/root/wiki", help="racine du dépôt wiki")
    p.add_argument("--donnees", default=None,
                   help="fichier déclaratif (défaut : <repo>/atelier/rd/instrument/instrument-donnees.yaml)")
    p.add_argument("--sortie", default=None,
                   help="manifeste produit (défaut : <repo>/atelier/rd/instrument/wiki-manifest.json)")
    args = p.parse_args()

    repo = Path(args.repo).resolve()
    if not (repo / "doctrinal").is_dir():
        sys.exit(f"ERREUR : {repo} ne ressemble pas au dépôt (doctrinal/ absent).")
    donnees = Path(args.donnees) if args.donnees else repo / "atelier/rd/instrument/instrument-donnees.yaml"
    sortie = Path(args.sortie) if args.sortie else repo / "atelier/rd/instrument/wiki-manifest.json"

    sys.exit(generer(repo, donnees, sortie))


if __name__ == "__main__":
    main()
