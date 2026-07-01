#!/usr/bin/env bash
# =============================================================================
# ornith-test-doctrinal.sh — Test de non-régression du CAS DOCTRINAL.
#   Jumeau de ornith-test.sh, mais sur le circuit doctrinal/ (Sceau Recteur).
#   Exige plus qu'une copie : RÉPARATION du frontmatter « mangé » (-----,
#   ## title:, guillemets courbes) + conformité au Sceau Recteur + maillage.
#
#   Témoin : doctrinal/symboles/nafs-qalb-irritation.md (golden = état committé).
#   Entrée _inbox : même contenu, frontmatter VOLONTAIREMENT corrompu.
#
#   Bac à sable ISOLÉ (copie du dépôt sans remote) → aucun risque de push.
#
#   Modèle sous test : neutre. Étiquette d'affichage via MODEL_LABEL, p. ex.
#     MODEL_LABEL="Qwen3.6-27B-FP8" bash ornith-test-doctrinal.sh prepare
#   (n'affecte QUE l'affichage ; le modèle réel est celui des variables ANTHROPIC_*.)
#
#   Sous-commandes : prepare | compare | selftest | clean
# =============================================================================
set -euo pipefail

WIKI=/root/wiki
ROOT=/root/ornith-test-doctrinal
SANDBOX="$ROOT/sandbox"
GOLDEN="$ROOT/golden"
MODEL_LABEL="${MODEL_LABEL:-le modèle local}"   # étiquette d'affichage, surchargeable

WITNESS="doctrinal/symboles/nafs-qalb-irritation.md"
SLUG="doctrinal/symboles/nafs-qalb-irritation"
INPUT_NAME="nafs-qalb-irritation.md"   # nom déposé dans _inbox (frontmatter corrompu)

say() { printf '\n\033[1m%s\033[0m\n' "$*"; }

# ---------------------------------------------------------------------------
cmd_prepare() {
  command -v git >/dev/null || { echo "git requis"; exit 1; }
  rm -rf "$ROOT"; mkdir -p "$GOLDEN/$(dirname "$WITNESS")" "$SANDBOX"

  say "[1/5] Capture de la RÉFÉRENCE Opus (fiche doctrinale committée + index + annales)"
  cp "$WIKI/$WITNESS"            "$GOLDEN/$WITNESS"
  cp "$WIKI/doctrinal/index.md"  "$GOLDEN/index.md"
  cp "$WIKI/doctrinal/annales.md" "$GOLDEN/annales.md"

  say "[2/5] Copie ISOLÉE du dépôt (sans .git, sans remote)"
  cp -a "$WIKI/." "$SANDBOX/"; rm -rf "$SANDBOX/.git"

  say "[3/5] Rembobinage : suppression de la fiche + de son entrée d'index §II"
  rm -f "$SANDBOX/$WITNESS"
  python3 - "$SANDBOX/doctrinal/index.md" "$SLUG" <<'PY'
import sys
p,slug=sys.argv[1],sys.argv[2]
lines=open(p,encoding="utf-8").read().split("\n")
open(p,"w",encoding="utf-8").write("\n".join(l for l in lines if slug not in l))
PY

  say "[4/5] Dépôt dans _inbox d'une version au frontmatter CORROMPU (à réparer)"
  find "$SANDBOX/_inbox" -maxdepth 1 -type f ! -name 'README.md' -delete 2>/dev/null || true
  python3 - "$GOLDEN/$WITNESS" "$SANDBOX/_inbox/$INPUT_NAME" <<'PY'
import sys
src,dst=sys.argv[1],sys.argv[2]
lines=open(src,encoding="utf-8").read().split("\n")
assert lines[0]=="---", "frontmatter golden inattendu"
close=lines.index("---",1)
fm,body=lines[1:close],lines[close+1:]
dmg=[]
for l in fm:
    if l.startswith("title:"):
        l="## "+l                              # title: -> ## title:
        i=l.find('"'); j=l.rfind('"')
        if i!=-1 and j!=i:                      # guillemets droits -> courbes
            l=l[:i]+"“"+l[i+1:j]+"”"+l[j+1:]
    dmg.append(l)
# délimiteurs --- -> ----- (corruption classique du transfert iPad)
open(dst,"w",encoding="utf-8").write("\n".join(["-----"]+dmg+["-----"]+body))
PY
  cat > "$SANDBOX/_inbox/UPDATES.md" <<UP
# UPDATES — Lot témoin DOCTRINAL de test (Sceau Recteur)

> ⚠️ TEST DE NON-RÉGRESSION. Intègre selon CLAUDE.md, mais **NE COMMIT PAS, NE PUSH PAS**.

## Page à classer (1)
- \`$INPUT_NAME\` → \`$WITNESS\`
  - Circuit doctrinal : **Sceau Recteur obligatoire**.
  - Le frontmatter a été **abîmé par le transfert** : réparer (\`-----\`→\`---\`,
    \`## title:\`→\`title:\`, guillemets courbes “ ” → guillemets droits ").
  - NE PAS modifier le corps de la fiche.
  - Vérifier que les cibles \`cross_links\` existent (al-ghazali, ibn-arabi) — signaler sinon.

## Catalogue (doctrinal/index.md, §II → « Vertus et états spirituels (fiqh du cœur) »)
- [[$SLUG|Discerner l'irritation du nafs et celle du qalb]]

## Annales
Ajouter une entrée datée \`## [YYYY-MM-DD] archivage | …\` mentionnant nafs/qalb.
UP

  git -C "$SANDBOX" init -q
  git -C "$SANDBOX" -c user.email=test@local -c user.name=test add -A
  git -C "$SANDBOX" -c user.email=test@local -c user.name=test commit -q -m "baseline pre-integration doctrinale (test)"

  say "[5/5] Bac à sable doctrinal prêt : $SANDBOX"
  cat <<EOF

PROCHAINE ÉTAPE (test réel avec $MODEL_LABEL, en session FRAÎCHE) :
  1) Tunnel SSH + variables ANTHROPIC_* pour $MODEL_LABEL (cf. 05-runbook §4-5).
  2) cd $SANDBOX && claude
     puis : « intègre _inbox/ selon UPDATES.md et CLAUDE.md » (NE PAS committer/pusher)
     ⚠️ relire chaque écriture (PAS d'auto-accept) ; ne pas se fier à l'auto-rapport du modèle.
  3) bash $WIKI/meta/projet-unifie/ornith-test-doctrinal.sh compare
EOF
}

# ---------------------------------------------------------------------------
cmd_compare() {
  [ -d "$SANDBOX" ] || { echo "Pas de bac à sable. Lance 'prepare' d'abord."; exit 1; }
  python3 - "$SANDBOX" "$GOLDEN" "$WITNESS" "$SLUG" "$MODEL_LABEL" <<'PY'
import sys,subprocess,re,os
SANDBOX,GOLDEN,WITNESS,SLUG,LABEL=sys.argv[1:6]
P=os.path.join(SANDBOX,WITNESS); G=os.path.join(GOLDEN,WITNESS)
pas=[0]; fail=[0]
def ok(m): print("  ✓",m); pas[0]+=1
def ko(m): print("  ✗",m); fail[0]+=1
def head(m): print("\n\033[1m%s\033[0m"%m)

def split_fm(path):
    t=open(path,encoding="utf-8").read(); ls=t.split("\n")
    if ls[0].strip("-")=="" and ls[0].startswith("---") and ls[0]=="---":
        c=ls.index("---",1); return ls[1:c],"\n".join(ls[c+1:]),ls[0]
    # tolère délimiteur non standard pour diagnostic
    first=ls[0]
    try: c=next(i for i,l in enumerate(ls[1:],1) if set(l)=={"-"} and len(l)>=3)
    except StopIteration: return None,None,first
    return ls[1:c],"\n".join(ls[c+1:]),first

REQ=["title","type","status","tradition_cadre","tags","created","updated","sources","sources_count","cross_links"]

head("A. Présence et routage de la fiche doctrinale")
if not os.path.exists(P): ko("fiche absente : %s"%WITNESS)
else:
    ok("fiche présente au bon emplacement")
    fm,body,first=split_fm(P)
    head("B. Sceau Recteur (frontmatter)")
    if first=="---": ok("délimiteur d'ouverture '---' correct")
    else: ko("délimiteur d'ouverture incorrect : %r (corruption ----- non réparée ?)"%first)
    if fm is None:
        ko("frontmatter introuvable/illisible")
    else:
        fmtxt="\n".join(fm)
        if not any(l.startswith("## title:") for l in fm): ok("pas de '## title:'")
        else: ko("'## title:' non réparé")
        if not re.search(r"[“”‘’]",fmtxt): ok("aucun guillemet courbe")
        else: ko("guillemets courbes restants dans le frontmatter")
        keys=[l.split(":",1)[0].strip() for l in fm if re.match(r"^[a-z_]+:",l)]
        miss=[k for k in REQ if k not in keys]
        if not miss: ok("toutes les clés du Sceau Recteur présentes")
        else: ko("clés manquantes : %s"%", ".join(miss))
        # sources_count == nb d'items de sources
        def line(k):
            for l in fm:
                if l.startswith(k+":"): return l
            return ""
        sc=line("sources_count"); src=line("sources")
        m=re.search(r"\d+",sc); n_items=src.count("[[")
        if m and int(m.group())==n_items: ok("sources_count (%s) == nb de sources (%d)"%(m.group(),n_items))
        else: ko("sources_count incohérent (%r vs %d sources)"%(sc,n_items))
        if 'type: symbole' in fmtxt: ok("type: symbole")
        else: ko("type incorrect")
        if "nafs" in line("title").lower(): ok("titre préservé")
        else: ko("titre altéré/perdu")

    head("C. Corps de la fiche inchangé (vs référence Opus)")
    gfm,gbody,_=split_fm(G)
    if body is not None and gbody is not None and body.strip()==gbody.strip():
        ok("corps identique à la référence")
    else:
        ko("corps modifié par rapport à la référence")

head("D. Étanchéité (un symbole ne pointe pas vers un discernement)")
txt=open(P,encoding="utf-8").read() if os.path.exists(P) else ""
if "doctrinal/discernement" not in txt: ok("aucun lien vers discernement (conforme)")
else: ko("lien interdit vers discernement détecté")

head("E. Catalogue (doctrinal/index.md §II)")
idx=open(os.path.join(SANDBOX,"doctrinal/index.md"),encoding="utf-8").read()
if SLUG in idx: ok("lien présent dans l'index")
else: ko("lien absent de l'index")

head("F. Annales (nouvelle entrée mentionnant le lot)")
changed = subprocess.run(["git","-C",SANDBOX,"diff","--quiet","--","doctrinal/annales.md"]).returncode!=0
an=open(os.path.join(SANDBOX,"doctrinal/annales.md"),encoding="utf-8").read()
if changed and re.search(r"nafs|qalb|irritation",an,re.I): ok("annales modifiées + mention du lot")
else: ko("pas de nouvelle entrée d'annales mentionnant le lot")

head("G. Effets de bord (git status)")
out=subprocess.run(["git","-C",SANDBOX,"status","--short"],capture_output=True,text=True).stdout
for l in out.splitlines(): print("    "+l)
print("    (attendu : 1 fiche créée + index.md + annales.md + _inbox vidé)")

head("VERDICT : %d ✓ / %d ✗"%(pas[0],fail[0]))
if fail[0]==0:
    print("  ✅ %s gère le cas DOCTRINAL (Sceau Recteur + réparation) — équivalent Opus sur ce lot."%LABEL)
else:
    print("  ⚠️  Écarts sur le cas doctrinal — supervision humaine renforcée requise ; ne pas confier l'intégration doctrinale à %s en autonomie."%LABEL)
PY
}

# ---------------------------------------------------------------------------
cmd_selftest() {
  say "SELFTEST DOCTRINAL — intégration simulée PARFAITE (copie de la référence) → doit tout PASSER"
  cmd_prepare >/dev/null
  mkdir -p "$SANDBOX/$(dirname "$WITNESS")"
  cp "$GOLDEN/$WITNESS"   "$SANDBOX/$WITNESS"
  cp "$GOLDEN/index.md"   "$SANDBOX/doctrinal/index.md"
  # simuler l'AJOUT d'une nouvelle entrée d'annales (ce que fait une intégration réelle)
  python3 - "$SANDBOX/doctrinal/annales.md" <<'PY'
import sys
p=sys.argv[1]; ls=open(p,encoding="utf-8").read().split("\n")
i=next(k for k,l in enumerate(ls) if l.startswith("## ["))
entry=["## [2026-06-29] archivage | nafs-qalb-irritation (selftest)",
       "- Entrée synthétique de validation du harnais.",""]
ls[i:i]=entry
open(p,"w",encoding="utf-8").write("\n".join(ls))
PY
  find "$SANDBOX/_inbox" -maxdepth 1 -type f ! -name 'README.md' -delete 2>/dev/null || true
  cmd_compare
}

cmd_clean() { rm -rf "$ROOT"; echo "Bac à sable doctrinal supprimé."; }

case "${1:-}" in
  prepare)  cmd_prepare ;;
  compare)  cmd_compare ;;
  selftest) cmd_selftest ;;
  clean)    cmd_clean ;;
  *) echo "Usage: $0 {prepare|compare|selftest|clean}"; exit 1 ;;
esac
