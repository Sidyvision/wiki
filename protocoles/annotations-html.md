# Annotations HTML — mesure, vocabulaire, garde, signalements

> **Rattachement** : `CLAUDE.md`, §VII, *Règles de placement des annotations HTML* (les 6 règles). Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

**Ce que la mesure a écarté.** Une première rédaction de la règle 5 disait « jamais dans
une citation », entendue comme « jamais dans un blockquote ». Relevé sur `doctrinal/` :
les blocs `>` y sont **massivement la voix propre du dépôt** — `> **Statut**` (53),
`> **Généalogie des idées**` (53), `> **Examen formel**` (50), `> **Conclusion**` (50),
`> 🔍 **Discernement — Spéculation Personnelle**` (49), et les blocs
`> 🌐 **Forme Traditionnelle Divergente**` / `> ⚠️ **Déviation Profane**` que le §VII
prescrit lui-même. Ces blocs sont **les plus denses en terminologie de tout le circuit** :
les interdire à l'annotation aurait fermé la porte principale, et l'aurait fermée en
silence. La règle a donc été resserrée sur le **texte reçu**, qui est le motif réel.

**Vocabulaire de `data-genre` : clos, et scopé par circuit** (étendu 2026-09-09, verdict
Sidy). Les sept valeurs transversales — `autorite`, `lieu`, `ouvrage`, `entite`,
`ecole`, `cycle`, `principe` — valent dans les cinq circuits. `hermeneutique/` en reçoit
**six de plus, admises chez lui seul** : `oeuvre`, `auteur`, `figure`, `dispositif`,
`concept` et `categorie-editoriale`. Les cinq premières ne sont pas des mots nouveaux
mais, terme pour terme, les valeurs du champ `type:` que `hermeneutique/CLAUDE.md`
déclare déjà — l'annotation emprunte au circuit son
propre vocabulaire avec la garde Cmd 3 qui y est attachée : `oeuvre` ne se fond **jamais**
dans `ouvrage`, réservé au traité traditionnel, et `auteur` ne confère aucun statut
d'autorité. `categorie-editoriale` (2026-09-09) est le **seul mot ajouté** de tout ce vocabulaire, et
donc le seul à devoir porter sa limite dans son nom : *éditoriale* dit que la catégorie
est celle du marché du livre, **jamais une catégorie de connaissance** — un *shōnen*
n'est pas une `ecole`. Un genre valide **posé hors de son circuit** est refusé (D6). La
lettre du vocabulaire herméneutique vit dans son `CLAUDE.md` local (§II bis).

**Une limite du masquage, rapportée et non corrigée** (Cmd 12) : le motif de code inline
n'admet pas de retour à la ligne, de sorte qu'un incise de code **coupé en deux lignes**
n'est pas masqué et peut être lu comme une annotation. Constaté sur la présente section
même, à sa rédaction. Le correctif évident — tolérer le retour à la ligne — a été
**mesuré et écarté** : rendu glouton par les backticks orphelins du dépôt, il avalerait
186 819 caractères de `doctrinal/annales.md`. La règle est donc tenue par le rédacteur :
**ne jamais couper un incise de code sur deux lignes**.
**Garde mécanique** : `atelier/rd/outillage/index-lexical/valider-annotations.py`, refus
D1 (appariement), D2 (Unicode invisible, Cmd 15), D3 (plancher de non-vacuité), D4
(placement), D5 (occurrence unique), D6 (genre hors de son circuit), plus le contrôle de
vocabulaire clos.

**Un signalement, non un refus — `S1`, doublon de référent possible** (ouvert 2026-09-09).
**D5 garantit l'unicité de la clé, jamais celle du référent** : `burckhardt` et
`titus-burckhardt` désignent la même personne sous deux clés, et D5 ne le voit pas, car
il compte par clé. `S1` relève les paires coannotées dans une même fiche dont l'une est
**composant** de l'autre. Ce n'est **pas** un refus, et ce ne doit pas en devenir un : la
même forme couvre un rapport parfaitement légitime — `yuga` et `kali-yuga` sont un
**genre et une espèce**, non un doublon. Distinguer les deux est un **jugement réservé**
(Cmd 12) : le contrôle montre la paire, il ne tranche pas. Les signalements s'impriment
**toujours**, y compris quand tout est vert, et ne changent pas le code de sortie — *un
signalement tu est un signalement perdu*. Les règles 1,
2 et 4 sont **outillées et éprouvées** ; la règle 3 est tenue par le masquage amont ; la
règle 5 ne l'est pas, et le dit.
