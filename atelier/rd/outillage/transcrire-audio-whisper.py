#!/usr/bin/env python3
# =============================================================================
# transcrire-audio-whisper.py — transcription automatique LOCALE d'un fichier
# audio de `raw/` (ASR), sans clé API ni réseau.
#
#   Ouvert le 2026-09-15 pour la vidéo de Curt Jaimungal (étude antagoniste) :
#   YouTube, Piped et Invidious refusent l'adresse du serveur ; l'audio a été
#   obtenu par notube (consigne de Sidy), la transcription se fait ici.
#   Conservé comme outil (« on conserve toute pièce d'outillage »).
#
#   MOTEUR : faster-whisper (CTranslate2), dans le venv isolé
#   `atelier/rd/outillage/.whisper-venv/` (non versionné, .gitignore). Modèle
#   par défaut `small`, déjà en cache Hugging Face sur le serveur ; calcul
#   `int8` sur CPU (2 cœurs, 3 Go de mémoire).
#
#   CE QU'IL PRODUIT : un Markdown horodaté, un segment par ligne
#   `[hh:mm:ss] texte`, précédé d'un cartouche qui dit TOUT ce qui a été fait
#   (modèle, langue, durée, paramètres). Aucune correction : c'est une sortie
#   de machine, à traiter comme telle — une transcription meilleure la
#   remplacera, datée (règle d'immuabilité).
#
#   GARDES : refus d'écraser ; refus si la sortie est vide (un fichier vide
#   n'est pas une transcription) ; écriture progressive dans un fichier
#   `.partiel`, renommé seulement à la fin — une interruption ne laisse jamais
#   passer une transcription tronquée pour complète.
#
#   Usage (dans le venv) :
#     atelier/rd/outillage/.whisper-venv/bin/python \
#       atelier/rd/outillage/transcrire-audio-whisper.py AUDIO SORTIE.md \
#       [--langue en] [--modele small] [--source URL] [--titre "..."] [--tranche 10]
# =============================================================================

import argparse
import datetime
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def hms(s):
    s = int(s)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("sortie")
    ap.add_argument("--langue", default="en")
    ap.add_argument("--modele", default="small")
    ap.add_argument("--source", default="")
    ap.add_argument("--titre", default="")
    ap.add_argument("--tranche", type=int, default=10, help="minutes par tranche (mémoire bornée)")
    a = ap.parse_args()

    from faster_whisper import WhisperModel

    sortie = Path(a.sortie)
    if sortie.exists():
        sys.exit(f"REFUS : {sortie} existe déjà (jamais d'écrasement)")
    partiel = sortie.with_suffix(sortie.suffix + ".partiel")

    # TRANCHES (ajout du 2026-09-15, après deux arrêts « Out of memory » du
    # noyau sur 56 min d'audio : 3,1 Go occupés sur 3 Go). L'audio est découpé
    # par ffmpeg en tranches WAV 16 kHz mono, transcrites l'une après l'autre
    # par le même modèle ; les horodatages sont recalés sur l'audio entier.
    # Une coupure peut tomber au milieu d'un mot : le prix de la mémoire bornée.
    duree = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.audio],
        capture_output=True, text=True, check=True).stdout.strip())
    pas = a.tranche * 60
    t0 = time.time()
    modele = WhisperModel(a.modele, device="cpu", compute_type="int8", cpu_threads=2)
    n = 0
    with tempfile.TemporaryDirectory(prefix="whisper-tranches-") as tmp, \
            partiel.open("w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f'titre: "{a.titre}"\n')
        f.write(f'source: "{a.source}"\n')
        f.write(f'audio: "{a.audio}"\n')
        f.write(f"moteur: faster-whisper, modele {a.modele}, int8 CPU, beam 1, VAD, "
                f"tranches de {a.tranche} min\n")
        f.write(f"langue: {a.langue}\n")
        f.write(f"duree_audio: {hms(duree)}\n")
        f.write(f"transcrit_le: {datetime.date.today().isoformat()}\n")
        f.write("statut: transcription automatique (ASR), non relue\n")
        f.write("---\n\n")
        debut = 0.0
        while debut < duree:
            wav = Path(tmp) / "tranche.wav"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(debut), "-t", str(pas),
                            "-i", a.audio, "-ac", "1", "-ar", "16000", str(wav)], check=True)
            segments, _ = modele.transcribe(str(wav), language=a.langue, beam_size=1,
                                            vad_filter=True, condition_on_previous_text=False)
            for seg in segments:
                f.write(f"[{hms(debut + seg.start)}] {seg.text.strip()}\n")
                n += 1
            f.flush()
            print(f"  {hms(min(debut + pas, duree))} / {hms(duree)}  ({n} segments, "
                  f"{(time.time() - t0) / 60:.1f} min)", flush=True)
            debut += pas
    if n == 0:
        sys.exit("REFUS : aucun segment transcrit — le fichier .partiel est laissé pour examen")
    partiel.rename(sortie)
    print(f"✓ {n} segments, audio {hms(duree)}, calcul {(time.time() - t0) / 60:.1f} min → {sortie}")


if __name__ == "__main__":
    main()
