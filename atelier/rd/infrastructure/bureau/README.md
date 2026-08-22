# Bureau TUI

Tableau de bord unique, exécutable depuis un terminal SSH sur le serveur :
état de l'Instrument, état des 12 agents Hermès, lecteur de textes/images,
lecteur vidéo (rendu ANSI), streaming audio, chat local. Voir
`../bureau-tui-architecture.md` pour l'architecture complète et son état
d'avancement.

## Installation (mode pédagogique)

```bash
cd atelier/rd/infrastructure/bureau
python3 -m venv .venv
```
Crée un environnement Python isolé (`.venv/`) pour ne pas mélanger les
dépendances du bureau avec celles du système — même logique que
`hermes-agent/venv`. Gitignored (`.gitignore`), jamais commité.

```bash
.venv/bin/pip install -r requirements.txt
```
Installe `textual` (interface), `websockets` (chat), `Pillow` (images),
`pypdf` (extraction PDF), `PyYAML` (lecture du manifeste Instrument), à
l'intérieur du `.venv` uniquement.

## Lancement

```bash
.venv/bin/python app.py
```
Ouvre le tableau de bord dans le terminal courant. Nécessite un vrai
terminal SSH (pas d'émulation dans un IDE) pour un rendu couleur/ANSI
correct.

## Navigation

- **Flèches** : déplacer le focus entre les tuiles de la grille.
- **Entrée** : agrandir la tuile focalisée en plein panneau (« monocle »).
- **Échap** : revenir à la grille depuis le mode monocle.
- **q** : quitter.

## Accès distant (audio, chat)

Le bureau tourne sur le serveur ; l'audio et le chat exposent un serveur
local (bind `127.0.0.1`, jamais de port ouvert publiquement — §VIII.8 du
protocole du dépôt). Pour y accéder depuis un autre appareil (iPad) :

```bash
ssh -L 8765:127.0.0.1:8765 -L 8766:127.0.0.1:8766 <utilisateur>@<serveur>
```
Ouvre un tunnel SSH : le port 8765 (chat) et 8766 (audio) de la machine
locale sont redirigés vers ceux du serveur. Un navigateur ou client local
peut alors se connecter à `http://127.0.0.1:8766/current` (audio) comme si
le serveur tournait sur l'appareil lui-même. Tailscale est une alternative
équivalente si déjà configuré.

## Modularité

Ajouter un module futur = un fichier de plus dans `modules/`, héritant de
`modules.base.Module` (`summary_widget()`, `full_widget()`,
`refresh_interval()`, `refresh()`), puis une ligne de plus dans `MODULES`
(`app.py`). Rien d'autre à modifier.

## Tests

```bash
.venv/bin/pip install pytest
.venv/bin/python -m pytest tests/
```
