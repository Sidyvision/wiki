#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
comparer-prompts-hermes.py — Juge de paix des prompts d'agents Hermes.

Deux contrôles déterministes, sans LLM et sans réseau, dans la famille de
verifier-invariants.py et verifier-coherence-infrastructure.py :

1. CONSERVATION (--conservation) — après l'éclatement d'un prompt monolithique
   en `principe` + `mandats/`, prouve qu'aucune ligne n'a été perdue,
   qu'aucune n'a été ajoutée hors de la liste déclarée, et qu'aucune ligne ne
   se retrouve dans deux mandats à la fois (fuite de périmètre). Remplace le
   `grep -c "## Mission"` de la fiche d'origine, que trois titres vides
   suffisaient à satisfaire (CLAUDE.md §VIII.2 : fiabilité d'action ≠
   fiabilité narrative — la passe se clôt sur une vérification mécanique
   indépendante, au résultat BRUT).

2. DÉRIVE (--derive) — compare chaque fiche du wiki au prompt réellement
   chargé par le moteur (`~/.hermes/profiles/<profil>/SOUL.md`). Constat du
   2026-08-31 : onze agents sur douze tournent sur un prompt antérieur aux
   mandats et aux calibrations zodiacales votés dans le dépôt. Le wiki décide,
   le moteur ne le sait pas.

Le script ne corrige rien — il constate. Il refuse par ailleurs tout fichier
porteur d'un caractère Unicode invisible (Cmd 15, incident ZWJ 2026-08-22).

Usage :
    python3 comparer-prompts-hermes.py --derive
    python3 comparer-prompts-hermes.py --conservation 08-publication-site \
        --source-git HEAD:meta/projet-unifie/hermes-prompts/08-publication-site.md

Codes de sortie :
    0  contrôle conforme
    1  écart constaté
    2  erreur d'exécution du script lui-même
"""

import argparse
import pathlib
import re
import subprocess
import sys
import unicodedata

RACINE_DEFAUT = pathlib.Path("/root/wiki")
PROMPTS_REL = "meta/projet-unifie/hermes-prompts"
PROFILS_DEFAUT = pathlib.Path.home() / ".hermes" / "profiles"

# profil moteur -> fiche wiki (miroir de bureau/modules/hermes_status.py)
PROFILS = [
    ("ar-music", "01-ar-music-artistic-direction.md"),
    ("visual-da", "02-visual-editorial-artistic-direction.md"),
    ("production", "03-production-manager.md"),
    ("admin-legal", "04-administration-legal.md"),
    ("accounting", "05-accounting-management.md"),
    ("distribution", "06-distribution.md"),
    ("marketing", "07-marketing-communication.md"),
    ("publication", "08-publication-site.md"),
    ("studio", "09-studio-sound-engineer.md"),
    ("gardien", "10-protocol-guardian.md"),
    ("fanzine", "11-fanzine-editor.md"),
    ("commerce", "12-commerce-profitability.md"),
]

INVISIBLES = {"\u200b", "\u200c", "\u200d", "\u200e", "\u200f"}
"""U+200B/C/D/E/F écrits en séquences d'échappement : ce fichier ne doit
lui-même porter aucun caractère invisible (Cmd 15)."""

# Lignes que l'éclatement a le droit d'ajouter : en-têtes de fichier issus de
# la découpe, renvois vers le principe, et le sommaire des mandats. Toute autre
# ligne ajoutée est un changement de fond déguisé en réorganisation.
RE_AJOUTS_AUTORISES = re.compile(
    r"^(#{1,6}\s|>\s|\*\*Principe\*\*|\*\*Mandat\b|\*\*Déployé\b|- \[|\|)"
)


def lignes_utiles(texte):
    """Normalise pour la comparaison : lignes non vides, marges retirées."""
    return [l.strip() for l in texte.splitlines() if l.strip()]


def controler_invisibles(chemin, texte, rapport):
    for num, ligne in enumerate(texte.splitlines(), 1):
        for car in ligne:
            if car in INVISIBLES:
                nom = unicodedata.name(car, "?")
                rapport.append(
                    f"[U+{ord(car):04X}] {chemin} l.{num} — caractère invisible "
                    f"interdit ({nom}) — Cmd 15"
                )
                break


def lire_source(racine, agent, source_git):
    """Le monolithe d'origine : depuis git si l'éclatement l'a déjà retiré."""
    if source_git:
        try:
            return subprocess.run(
                ["git", "-C", str(racine), "show", source_git],
                capture_output=True, text=True, check=True,
            ).stdout
        except subprocess.CalledProcessError as err:
            print(f"ERREUR : `git show {source_git}` a échoué :\n{err.stderr}",
                  file=sys.stderr)
            sys.exit(2)
    chemin = racine / PROMPTS_REL / f"{agent}.md"
    if not chemin.exists():
        print(f"ERREUR : source introuvable : {chemin}\n"
              f"        (l'éclatement l'a-t-il déjà retirée ? utiliser --source-git)",
              file=sys.stderr)
        sys.exit(2)
    return chemin.read_text(encoding="utf-8")


def conservation(racine, agent, source_git):
    rapport = []
    dossier = racine / PROMPTS_REL / agent
    if not dossier.is_dir():
        print(f"ERREUR : dossier d'agent introuvable : {dossier}", file=sys.stderr)
        sys.exit(2)

    source = lire_source(racine, agent, source_git)
    controler_invisibles(f"{agent}.md (source)", source, rapport)
    avant = lignes_utiles(source)

    # Le README documente le contrat de chargement, il ne porte pas de prompt :
    # il est hors du périmètre de conservation.
    morceaux = sorted(
        p for p in dossier.rglob("*.md") if p.name.lower() != "readme.md"
    )
    if not morceaux:
        print(f"ERREUR : aucun morceau .md sous {dossier}", file=sys.stderr)
        sys.exit(2)

    apres = []
    par_morceau = {}
    for chemin in morceaux:
        texte = chemin.read_text(encoding="utf-8")
        rel = chemin.relative_to(racine)
        controler_invisibles(str(rel), texte, rapport)
        lignes = lignes_utiles(texte)
        par_morceau[rel] = lignes
        apres.extend(lignes)

    avant_set, apres_set = set(avant), set(apres)

    perdues = [l for l in avant if l not in apres_set]
    ajoutees = [l for l in apres if l not in avant_set]
    non_declarees = [l for l in ajoutees if not RE_AJOUTS_AUTORISES.match(l)]

    # Fuite de périmètre : une même ligne dans deux mandats distincts.
    fuites = []
    noms = list(par_morceau)
    for i, a in enumerate(noms):
        for b in noms[i + 1:]:
            communes = (set(par_morceau[a]) & set(par_morceau[b])) & avant_set
            for ligne in sorted(communes):
                fuites.append(f"{a} ∩ {b} : {ligne[:90]}")

    print(f"=== CONSERVATION — {agent} ===")
    print(f"source           : {source_git or (PROMPTS_REL + '/' + agent + '.md')}")
    print(f"lignes utiles    : {len(avant)} avant → {len(apres)} après")
    for rel, lignes in par_morceau.items():
        print(f"  {len(lignes):4d}  {rel}")
    print()
    print(f"PERDUES          : {len(perdues)}")
    for l in perdues:
        print(f"  ⛔ {l[:100]}")
    print(f"AJOUTÉES         : {len(ajoutees)} "
          f"({len(ajoutees) - len(non_declarees)} déclarées, "
          f"{len(non_declarees)} non déclarées)")
    for l in non_declarees:
        print(f"  ⛔ {l[:100]}")
    print(f"FUITES DE PÉRIMÈTRE : {len(fuites)}")
    for f in fuites:
        print(f"  ⚠️  {f}")
    print(f"UNICODE INVISIBLE   : {len(rapport)}")
    for r in rapport:
        print(f"  ⛔ {r}")

    ok = not (perdues or non_declarees or fuites or rapport)
    print()
    print("VERDICT : " + ("✅ conservation intégrale"
                          if ok else "⛔ écart constaté"))
    return 0 if ok else 1


def derive(racine, profils_dir):
    print("=== DÉRIVE wiki ↔ moteur ===")
    print(f"wiki   : {racine / PROMPTS_REL}")
    print(f"moteur : {profils_dir}")
    print()
    print(f"{'profil':<13} {'wiki':>8} {'SOUL.md':>8}  état")
    ecarts = 0
    for profil, fiche in PROFILS:
        chemin_wiki = racine / PROMPTS_REL / fiche
        chemin_soul = profils_dir / profil / "SOUL.md"
        if not chemin_wiki.exists():
            print(f"{profil:<13} {'—':>8} {'—':>8}  ⛔ fiche wiki introuvable ({fiche})")
            ecarts += 1
            continue
        if not chemin_soul.exists():
            print(f"{profil:<13} {chemin_wiki.stat().st_size:>8} {'—':>8}  "
                  f"⛔ SOUL.md absent (agent non déployé)")
            ecarts += 1
            continue
        t_wiki = chemin_wiki.read_text(encoding="utf-8")
        t_soul = chemin_soul.read_text(encoding="utf-8")
        l_wiki, l_soul = lignes_utiles(t_wiki), lignes_utiles(t_soul)
        manquantes = [l for l in l_wiki if l not in set(l_soul)]
        invisibles = []
        controler_invisibles(str(chemin_soul), t_soul, invisibles)
        if not manquantes and not invisibles:
            etat = "✅ synchronisé"
        else:
            etat = f"⛔ {len(manquantes)} l. du wiki absentes du moteur"
            if invisibles:
                etat += f" · {len(invisibles)} Unicode invisible (Cmd 15)"
            ecarts += 1
        print(f"{profil:<13} {len(t_wiki):>8} {len(t_soul):>8}  {etat}")
    print()
    print(f"VERDICT : {ecarts} agent(s) en écart sur {len(PROFILS)}.")
    print("Le déploiement wiki → moteur n'est pas automatisé : ce qui est décidé")
    print("dans le dépôt n'atteint l'agent que par un acte explicite (Cmd 13).")
    return 0 if ecarts == 0 else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--racine", type=pathlib.Path, default=RACINE_DEFAUT)
    ap.add_argument("--profils", type=pathlib.Path, default=PROFILS_DEFAUT)
    ap.add_argument("--conservation", metavar="AGENT",
                    help="dossier d'agent éclaté, ex. 08-publication-site")
    ap.add_argument("--source-git", metavar="REF",
                    help="monolithe d'origine à lire dans git, "
                         "ex. HEAD:meta/.../08-publication-site.md")
    ap.add_argument("--derive", action="store_true",
                    help="compare les 12 fiches wiki aux SOUL.md du moteur")
    args = ap.parse_args()

    if not args.conservation and not args.derive:
        ap.error("choisir au moins --conservation AGENT ou --derive")

    code = 0
    if args.conservation:
        code |= conservation(args.racine, args.conservation, args.source_git)
    if args.derive:
        if args.conservation:
            print()
        code |= derive(args.racine, args.profils)
    return code


if __name__ == "__main__":
    sys.exit(main())
