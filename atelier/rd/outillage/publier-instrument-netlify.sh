#!/usr/bin/env bash
# =============================================================================
# publier-instrument-netlify.sh — déploie le rendu sous sidyvision.com/instrument
#
#   Chantier INF-14. Troisième et dernier étage du flux du §VII :
#     instrument-donnees.yaml → generer-manifeste.py → wiki-manifest.json
#       → dépôt Sidyvision/instrument → sidyvision.com/instrument/
#
#   Le site sidyvision.com n'a AUCUNE source versionnée : c'est un déploiement
#   manuel Netlify. Ce script est donc, à lui seul, la reproductibilité du
#   déploiement — sans lui, le site ne serait redéployable que par des clics que
#   personne n'aurait documentés.
#
#   PORTE HUMAINE (Cmd 13 ; Action PUBLICATION du label, point 4, non négociable) :
#   par défaut ce script produit une PRÉVERSION et ne publie RIEN. La mise en
#   production exige --production ET une validation explicite de Sidy dans la
#   session courante.
#
#   Le jeton vit hors du dépôt, dans ~/.netlify-token (permissions 600). Il n'est
#   jamais écrit dans le dépôt, jamais affiché, jamais journalisé.
#
#   Usage :
#     bash publier-instrument-netlify.sh                # préversion (défaut)
#     bash publier-instrument-netlify.sh --production   # publie, après validation
# =============================================================================
set -euo pipefail

SITE="${SITE:-b82794eb-436e-40b5-a168-96c14a1d510f}"   # lively-mousse-a649f7 = sidyvision.com
WIKI="${WIKI:-/root/wiki}"
FRERE="${FRERE:-/root/instrument}"
RACINE="$WIKI/atelier/rd/infrastructure/captures/2026-09-01_sidyvision-com-racine.html"
JETON="${JETON:-$HOME/.netlify-token}"
PROD=0; [ "${1:-}" = "--production" ] && PROD=1

[ -f "$JETON" ] || { echo "ERREUR : jeton absent — $JETON" >&2; exit 2; }
# shellcheck disable=SC1090
set -a; . "$JETON"; set +a
[ -n "${NETLIFY_AUTH_TOKEN:-}" ] || { echo "ERREUR : NETLIFY_AUTH_TOKEN vide." >&2; exit 2; }

# --- Garde-fou : la page d'accueil doit être celle de la capture de référence ---
#   Le déploiement par empreintes REMPLACE l'intégralité du site : tout fichier
#   non listé disparaît. La page d'accueil est donc redéployée à l'identique à
#   chaque passe, et son empreinte est vérifiée avant l'envoi. Sans ce contrôle,
#   une capture altérée effacerait silencieusement le site (Cmd 10).
ATTENDU="6814d7f4846b6683e3854e6fa1a62df886723334"
OBTENU="$(sha1sum "$RACINE" | cut -d' ' -f1)"
if [ "$OBTENU" != "$ATTENDU" ]; then
  echo "ERREUR : la capture de la page d'accueil ne correspond plus à la référence." >&2
  echo "  attendu : $ATTENDU" >&2
  echo "  obtenu  : $OBTENU" >&2
  echo "  Refus — publier ainsi remplacerait la page d'accueil du site." >&2
  exit 3
fi
echo "✓ page d'accueil conforme à la capture de référence"

PROD=$PROD SITE=$SITE RACINE=$RACINE FRERE=$FRERE python3 - <<'PY'
import json,os,hashlib,urllib.request,time,sys
T=os.environ['NETLIFY_AUTH_TOKEN']; API="https://api.netlify.com/api/v1"
S=os.environ['SITE']; PROD=os.environ['PROD']=="1"
def req(m,u,d=None,raw=False):
    r=urllib.request.Request(API+u,method=m,data=(d if raw else (json.dumps(d).encode() if d is not None else None)))
    r.add_header("Authorization","Bearer "+T)
    if d is not None: r.add_header("Content-Type","application/octet-stream" if raw else "application/json")
    with urllib.request.urlopen(r,timeout=90) as f:
        b=f.read(); return json.loads(b) if b else {}
srcs={"/index.html":os.environ['RACINE'],
      "/instrument/index.html":os.environ['FRERE']+"/src/index.html",
      "/instrument/wiki-manifest.json":os.environ['FRERE']+"/src/wiki-manifest.json"}
files={k:hashlib.sha1(open(v,'rb').read()).hexdigest() for k,v in srcs.items()}
dep=req("POST",f"/sites/{S}/deploys",{"files":files,"draft":not PROD})
for k,sha in files.items():
    if sha in dep.get("required",[]):
        req("PUT",f"/deploys/{dep['id']}/files{k}",open(srcs[k],'rb').read(),raw=True)
for _ in range(45):
    d=req("GET",f"/deploys/{dep['id']}")
    if d["state"] in ("ready","error"): break
    time.sleep(2)
if d["state"]!="ready": sys.exit(f"ERREUR : déploiement en état {d['state']}")
if PROD:
    print("✓ PRODUCTION publiée — https://sidyvision.com/instrument/")
else:
    print("✓ préversion prête (production intacte) :")
    print("   "+(d.get("deploy_ssl_url") or d.get("deploy_url"))+"/instrument/")
PY
