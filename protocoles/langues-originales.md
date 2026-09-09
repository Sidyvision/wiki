# Discipline des langues originales — mesure, appariements, garde

> **Rattachement** : `CLAUDE.md`, §VII, *Discipline des langues originales* (points 1 à 7). Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

**Ce qui a motivé la règle** (mesuré le 2026-09-08, non allégué). Le tokeniseur de
`atelier/rd/outillage/index-lexical/` employait `[^\W\d_]+` ; or le `\w` de Python **exclut**
les marques combinantes (catégories Unicode Mn/Mc). Toute écriture qui en emploie était donc
éclatée en débris, quand l'arabe non vocalisé et le han, qui n'en emploient pas, passaient
intacts : **la richesse apparente de l'index masquait exactement l'angle mort qu'il aurait dû
lever.** Corrigé le jour même, avec deux correctifs — récolte du `title:` du Sceau, des H1 et
des H2 (le point 3 est ainsi tenu au site qu'il déclare canonique), et champ `apparie` portant
la réciprocité du point 6 **dans les deux sens**, renseigné uniquement sur une paire que le
texte du dépôt **énonce lui-même** ; là où le dépôt se tait, le champ reste vide et la clé est
déclarée orpheline plutôt que complétée — aucune translittération n'est devinée par un modèle,
application au lexique de la règle « établi vs suggéré ». **Chiffres de mesure et récit du
correctif : `atelier/annales.md`, entrée du 2026-09-08** (Cmd 9 — le protocole porte la règle,
les annales portent la mesure).

Un **second champ**, `jurjani`, porte le **rang 2** : les appariements qu'une autorité
textuelle transcrite au dépôt établit — le *Kitāb al-Taʿrīfāt* d'al-Jurjānī —, chacun
avec son **numéro de définition**, qui est sa source (verdict Sidy, 2026-09-08 ; 132
appariements, dont 84 réciproques). Les deux champs ne se fondent **jamais** : le rang 1
prime, et le condensé les distingue à l'œil. Un troisième rang — la translittération
produite par la machine — resterait dû d'un `to-source` ; la passe du 2026-09-08 l'a
trouvé **vide**, aucune forme n'ayant eu à être devinée.

**Le champ `original:` porte les appariements de SYNTAGMES ; l'index ne porte que des
tokens** (clarification 2026-09-09, verdict Sidy). Les clés de l'index lexical sont des
**tokens** : il ne peut structurellement pas apparier `chikai to seiyaku` à `誓約と制約`,
qui est une paire de **syntagmes**. Trois voies d'élargissement ont été essayées et
**mesurées** — élargir le côté latin de la regex d'appariement, l'ancrer sur le slug de
la fiche, admettre la barre oblique. Les trois produisent **plus de déchet que de
signal** : la regex avale l'article et la conjonction (`et Muraqaba`, `Le Shintō`), le
slug se méprend sur les fiches qui traitent **deux** termes (`merkavah-muraqaba`), et la
barre oblique n'a donné aucune paire vraie pour une fausse.

Et le gisement réel est **nul** : les deux seules paires de syntagmes légitimes du
dépôt — `hideo-kojima ↔ 小島秀夫`, `yoji-shinkawa ↔ 新川洋司` — sont **déjà appariées**
par leur nom de famille, le syntagme n'ajoutant que le prénom.

**La réciprocité d'un syntagme se porte donc là où elle est ancrée et sourcée : dans le
champ `original:` du Sceau** (§IV). Une fiche dont le sujet est un syntagme y déclare la
chaîne entière — `original: ["誓約と制約"]` —, ce qui l'immunise à la fois contre la
gourmandise d'une regex et contre la découpe en tokens. **Aucun outillage n'est à bâtir
pour cela** : le porteur existe, il attend seulement d'être rempli, au fil des sessions
et jamais en passe de masse (point 5).

**L'axe de la LANGUE, distinct de celui de la tradition** (verdict Sidy, 2026-09-09 :
« une alternative serait de classifier par langue plutôt que par tradition, puisque chaque
tradition trouve son véhicule en une langue »). Le principe est **ontologiquement plus
juste** que la tradition, et il explique un échec mesuré : **la langue est une propriété
du TERME, la tradition une propriété du CADRE où on le cite**. C'est pourquoi compter les
`tradition_cadre` des fiches qui mentionnent un terme ne donne rien — `barzakh` y sort
`islam 36 / universel 12 / kabbale 2`, non par accident mais parce que les fiches
comparatives déclarent `universel` comme cadre de *leur propos*.

L'index porte donc **deux champs distincts, jamais fondus** : `tradition` (le cadre,
sourcé par la fiche qui a le terme pour sujet, ou par verdict) et `langue` (la langue du
terme). La langue n'est posée que sur trois sources, chacune **déclarée avec la valeur** :
le champ **`original:` du Sceau** (§IV) de la fiche dont le slug est le terme — l'écriture
y donne la langue ; la langue **énoncée en prose** (« **Buddhi** (Sanskrit : बुद्धि) ») ;
ou l'écriture de la **forme appariée**. Aucune quatrième voie, et en particulier **aucune
déduction depuis la graphie de la translittération** (`al-`, `ḥ`, `ṣ`) : ce serait une
heuristique d'orthographe, et une heuristique n'est pas une source.

**Seules les écritures exclusives donnent la langue.** Le **han** en est écarté : il sert
le chinois *et* le japonais, et `巴` y aurait été déclaré « chinois » alors que le terme
est japonais. *Une écriture partagée ne source pas une langue — elle source une écriture,
ce qui n'est pas la même chose.*

**Conséquence architecturale, et c'est le fait à retenir** : la couverture de l'axe langue
est aujourd'hui faible parce que le dépôt n'énonce presque jamais la langue de ses termes.
Mais il a déjà l'endroit pour le faire — **le champ `original:`**. **L'axe de la langue se
renforce donc exactement au rythme de la discipline des langues originales**, sans travail
propre : chaque `original:` posé sur une fiche donne la langue de son terme.

**Garde mécanique du marqueur** (câblée le même jour, verdict Sidy). Le champ
`original:` du §IV est contrôlé par `verifier-invariants.py` sous trois codes, tous
éprouvés sur faute fabriquée : **B5** — le marqueur `to-original` déclare une absence
que le `title:` ou le H1 dément déjà ; **B6** — graphie fautive du marqueur
(`to_original`, `tooriginal`, `to-originel`), qui le rendrait invisible ; **B7** — forme
du champ : liste YAML de chaînes, marqueur et formes jamais mêlés, et une
translittération refusée comme forme originale. La définition canonique d'« écriture
originale » vit dans `verifier-invariants.py` et l'index l'en **importe**, sans repli
possible sur une copie locale — deux définitions divergentes seraient la dérive même
que ce partage empêche.

**Ce que la garde ne fait pas, et ne peut pas faire** : exiger le champ. Savoir si le
sujet d'une fiche *appelle* une écriture d'origine demande la perception du sujet, non
la lecture de sa forme — c'est un jugement, il revient à Sidy (Cmd 12), et le point 5
l'interdit d'ailleurs de toute façon. La garde est un contrôle de **cohérence**, jamais
de complétude ; l'écart de couverture du dépôt se rapporte, il ne se comble pas
d'office.
