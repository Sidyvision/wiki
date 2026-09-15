---
title: "Index de conversion — Xī Yóu Jì 西遊記 (Wú Chéng'ēn), chinois traditionnel"
type: ressource
tags: [conversion, chine, roman, xiyouji, chinois-traditionnel, gutenberg]
created: 2026-09-15
sources:
  - "raw/xi-you-ji-wu-chengen-traditionnel-gutenberg-23962.txt"
---

# Xī Yóu Jì 西遊記 — Wú Chéng'ēn 吳承恩

Conversion texte → Markdown de `raw/xi-you-ji-wu-chengen-traditionnel-gutenberg-23962.txt`,
**un fichier par 回** (verdict Sidy du 2026-09-15 : « un fichier par 回 »).

**Source** : Project Gutenberg n° 23962, publié le 22 décembre 2007, transcrit par
Leong Joana Kit Ieng, UTF-8, **chinois traditionnel**. Œuvre du XVIᵉ siècle, domaine
public. Un `.epub` du même dépôt accompagne le `.txt` dans `raw/`.

**Chaîne** : `atelier/rd/outillage/convertir-xiyouji-gutenberg.py` — déterministe,
sans LLM, sans réseau, rapport seul par défaut (`--appliquer` requis pour écrire). Il
ne touche jamais à `raw/`.

## Ce qui a été retiré, et rien d'autre

**19 184 caractères** : l'en-tête et le pied de Project Gutenberg, délimités par les
bornes `*** START OF THE PROJECT GUTENBERG EBOOK 西遊記 ***` et `*** END ... ***`.

Ce n'est **pas** une correction du texte, que la règle d'immuabilité de `textes/`
interdirait (CLAUDE.md racine, §II). C'est la **couche de diffusion** — notice de
licence, adresses du site, appel aux dons —, qui n'appartient pas à l'œuvre : même
motif que le retrait des contrôles bidirectionnels dans l'Ihyâ' arabe
(`textes/ghazali-ihya-ulum-al-din-arabe/index-conversion.md`, étape 3) et des sauts de
page U+000C du dictionnaire Shintō.

**Retiré mais reporté ici, non effacé** — la ligne de crédit du transcripteur, qui
suivait la borne d'ouverture : `Produced by Leong Joana Kit Ieng`.

## Ce qui n'a pas été touché

Aucune correction, aucune normalisation, aucune conversion de caractères. En
particulier, **l'espace initiale parasite du titre du 第八三回** (`' 第八三回     心猿識得丹頭…'`)
est conservée telle quelle : une conversion reçoit, elle ne redresse pas.

Sont également conservés les espaces idéographiques U+3000 qui séparent les deux
hémistiches de chaque titre (13 306 occurrences), et la ponctuation d'origine.

## Garde-fous, et leur épreuve

Quatre refus, **chacun vu échouer sur une faute fabriquée** dans un bac à sable avant
emploi (CLAUDE.md racine §VII, épreuve des contrôles). Aucun fichier n'est écrit si
l'un cède — vérifié : 0 fichier produit dans les quatre cas.

| Garde | Ce qu'il attrape | Cas fabriqué | Refus observé |
|---|---|---|---|
| G1 | bornes Gutenberg absentes ou inversées | bornes supprimées | `G1 — borne(s) Gutenberg absente(s) : START, END` |
| G2 | nombre ou numérotation des 回 non conformes | 50ᵉ 回 retiré | `G2 — 99 回 trouvés, 100 attendus` |
| G3 | invisible du Cmd 15 en sortie | U+200D injecté au 回 5 | `G3 — … U+200D dans les 回 [5]` |
| G4 | matière non reconnue avant le premier 回 | préface apocryphe insérée | `G4 — matière non reconnue avant le premier 回` |

Sur l'état sain, les quatre passent au vert.

## Contrôles après coup (résultats bruts)

- **100 fichiers** écrits, `xiyouji-hui-001.md` à `xiyouji-hui-100.md`, 2 216 710 octets.
- **100 回**, numérotés de 1 à 100, strictement croissants, sans doublon ni lacune ;
  exactement **1 titre de 回 par fichier**, conforme au numéro porté par le nom.
- Comparaison **ligne non vide à ligne non vide** entre le corps de la source et la
  concaténation des 100 fichiers : 23 387 lignes de part et d'autre, **0 écart de contenu**.
- **Aucun caractère invisible** du Cmd 15 (contrôle propre dès la source).
- Taille des fichiers : 5 260 à 9 869 caractères, 7 576 en moyenne.

## Réserve sur l'édition

**Project Gutenberg ne déclare pas l'édition de base** de cette transcription. Ce
n'est donc **pas une édition critique identifiable** (ni 世德堂本 ni autre témoin
nommé), et elle n'a été collationnée avec aucune autre. Pour un travail portant sur la
lettre, un témoin nommé est requis — le Chinese Text Project donne le 世德堂本
(`ctext.org/wiki.pl?if=gb&res=340509`). La présente conversion vaut pour la lecture et
la recherche plein texte, non pour l'établissement du texte.

## Nommage

`xiyouji-hui-NNN.md`, où `NNN` est le numéro du 回 sur trois chiffres : la règle est
sans exception, `xiyouji-hui-083.md` porte le 第八三回 et `xiyouji-hui-100.md` le
第一○○回. Chaque fichier s'ouvre sur la ligne de titre du 回, telle quelle.

Le fichier original reste la source de vérité :
`raw/xi-you-ji-wu-chengen-traditionnel-gutenberg-23962.txt`. Le dossier `textes/` est
versionné ; `raw/` est hors git.

Ce qui se **dit** de l'ouvrage — sa valeur, son statut, ce que le dépôt en retient —
n'a pas sa place ici : cela se dira dans une fiche portant le Sceau, non encore
ouverte au 2026-09-15.

## Défauts de l'édition relevés (constatés, non corrigés)

Ces défauts appartiennent à la **transcription Gutenberg**, non à la conversion : la
comparaison ligne non vide à ligne non vide donne 0 écart avec la source. Ils sont
**consignés et laissés en place** (règle d'immuabilité, §II) — un texte de `textes/`
ne se corrige pas dans sa substance ; ce qui appelle mieux appelle une conversion
meilleure, depuis un témoin nommé.

1. **第四七回 — titre mutilé.** La source porte `聖僧夜阻通天水` seul sur la ligne de
   titre, puis, après deux lignes vides, `木垂慈救小童`. Deux défauts cumulés : le
   second hémistiche est **rejeté hors de la ligne de titre**, et il est **amputé de
   son premier caractère**. Collationné le 2026-09-15 sur 維基文庫 (zh.wikisource.org,
   西遊記) : le titre reçu est `聖僧夜阻通天水　金木垂慈救小童` — le `金` manque.
   C'est le titre le plus gravement atteint, **non le seul** : la collation ci-dessous
   en relève quatre autres qui perdent de la matière.

2. **第一三回 — double espace.** La ligne de titre porte **deux** U+3000 entre les
   hémistiches là où le témoin Wikisource n'en porte qu'un. Écart de blanc, sans
   effet sur la lettre.

3. **Numérotation non homogène.** La source écrit 95 titres sans `十`
   (`第一五回`, `第九九回`) et 5 avec — relevé exhaustif : `第十四回`, `第十六回`,
   `第十八回`, `第十九回` et `第八十七回`. Le nommage des fichiers, lui, est
   régulier : `xiyouji-hui-NNN.md` sur trois chiffres, sans exception.

**Ce qui a été vérifié et n'est PAS un défaut** : les lignes courtes isolées des 回 7,
16, 62 et 75 (`上下亂規箴。`, `清虛有道果清虛。`, `跨鶴赴瀛洲。`, `門。`) sont des fins de
vers ou de paragraphe repliés — la source justifie à 35 caractères (11 096 lignes de
cette largeur). Inspectées une à une : rien d'amputé.

## Collation des 100 titres (2026-09-15)

**Témoin** : 維基文庫 (zh.wikisource.org), page `西遊記`, wikitexte brut obtenu par
`curl` et dépouillé par script — les lectures variantes qu'il porte en gabarit
`{{另|A|B}}` sont développées et **toutes** admises. Aucun modèle dans la boucle.

**Résultat brut : 87 titres sur 100 identiques à une lecture du témoin, 13 écarts.**

| 回 | Dépôt (Gutenberg) | Témoin (維基文庫) | Nature mécanique |
|---|---|---|---|
| 18 | 高老莊大聖除魔 | 高老莊行者降魔 | hémistiche entier différent |
| 36 | 劈破傍門見月明 | 劈破旁門見月明 | substitution, même longueur |
| 39 | 一粒丹砂天上得 | 一粒金丹天上得 | substitution, même longueur |
| 42 | 大聖慇懃拜南海 | 大聖慇勤拜南海 | substitution, même longueur |
| 47 | 聖僧夜阻通天水 | 聖僧夜阻通天水　金木垂慈救小童 | **8 caractères tombés** |
| 52 | 悟空大鬧金洞 | 悟空大鬧金兜洞 | **`兜` tombé** |
| 56 | 道迷放心猿 | 道昧放心猿 | substitution, même longueur |
| 62 | 縛魔歸主乃修身 | 縛魔歸正乃修身 | substitution, même longueur |
| 71 | 行者假名降怪 ／ 觀音現像伏妖王 | 行者假名降怪犼 ／ 觀音現象伏妖王 | **`犼` tombé** + substitution `像`/`象` |
| 75 | 心猿鑽透陰陽體 | 心猿鑽透陰陽竅 | substitution, même longueur |
| 80 | 女育陽求配偶 | 姹女育陽求配偶 | **`姹` tombé** |
| 87 | 孫大圣勸善施霖 | 孫大聖勸善施霖 | **caractère simplifié** `圣` pour `聖` |
| 97 | 金酬外護遭魔蟄 | 金酬外護遭魔毒 | substitution, même longueur |

**Ce que la mesure établit, et ce qu'elle ne tranche pas.** Elle établit qu'en cinq
endroits la source **perd de la matière** — 回 47, 52, 71, 80 (caractères absents) et
回 87 (forme simplifiée dans une édition traditionnelle). Les substitutions de même
longueur, elles, peuvent être des **lectures de recension** légitimes autant que des
fautes : la machine les rapporte, elle ne les arbitre pas (Cmd 12). Le verdict
appartient à qui dispose d'un témoin nommé.

**Caractères simplifiés dans tout le corpus** : deux, `圣` et `万`, tous deux au
`xiyouji-hui-087.md` — relevé exhaustif par balayage des 100 fichiers.

**Portée de ce relevé** : il porte sur les **titres**, désormais collationnés un à un,
et sur les anomalies de structure détectables par mesure. Le **corps** du texte n'a été
collationné avec **aucun** témoin — et la collation des titres montre que ce n'est pas
une précaution de style : une édition qui laisse tomber `姹`, `犼` et `兜` dans ses
titres peut en laisser tomber ailleurs sans que rien ne le signale. C'est la limite
exacte de cette conversion, et le motif de la réserve ci-dessus sur l'édition.

**Contrôle de la queue du texte** : le garde-fou G4 protège le prélude, rien ne protège
ce qui suivrait le dernier 回. Vérifié à la main : `xiyouji-hui-100.md` s'achève sur
`《西遊記》至此終。` et ne porte **aucune** mention de Gutenberg ni ligne de crédit.

## Table des 100 回
Titres reproduits **tels que la source les porte** ; `／` figure l'espace
idéographique U+3000 qui sépare les hémistiches.

| Fichier | 回 | Titre |
|---|---|---|
| `xiyouji-hui-001.md` | 第一回 | 靈根育孕源流出 ／ 心性修持大道生 |
| `xiyouji-hui-002.md` | 第二回 | 悟徹菩提真妙理 ／ 斷魔歸本合元神 |
| `xiyouji-hui-003.md` | 第三回 | 四海千山皆拱伏 ／ 九幽十類盡除名 |
| `xiyouji-hui-004.md` | 第四回 | 官封弼馬心何足 ／ 名注齊天意未寧 |
| `xiyouji-hui-005.md` | 第五回 | 亂蟠桃大聖偷丹 ／ 反天宮諸神捉怪 |
| `xiyouji-hui-006.md` | 第六回 | 觀音赴會問原因 ／ 小聖施威降大聖 |
| `xiyouji-hui-007.md` | 第七回 | 八卦爐中逃大聖 ／ 五行山下定心猿 |
| `xiyouji-hui-008.md` | 第八回 | 我佛造經傳極樂 ／ 觀音奉旨上長安 |
| `xiyouji-hui-009.md` | 第九回 | 陳光蕊赴任逢災 ／ 江流僧復讎報本 |
| `xiyouji-hui-010.md` | 第一○回 | 老龍王拙計犯天條 ／ 魏丞相遺書託冥吏 |
| `xiyouji-hui-011.md` | 第一一回 | 遊地府太宗還魂 ／ 進瓜果劉全續配 |
| `xiyouji-hui-012.md` | 第一二回 | 唐王秉誠修大會 ／ 觀音顯聖化金蟬 |
| `xiyouji-hui-013.md` | 第一三回 | 陷虎穴金星解厄 ／ 雙叉嶺伯欽留僧 |
| `xiyouji-hui-014.md` | 第十四回 | 心猿歸正 ／ 六賊無蹤 |
| `xiyouji-hui-015.md` | 第一五回 | 蛇盤山諸神暗佑 ／ 鷹愁澗意馬收韁 |
| `xiyouji-hui-016.md` | 第十六回 | 觀音院僧謀寶貝 ／ 黑風山怪竊袈裟 |
| `xiyouji-hui-017.md` | 第一七回 | 孫行者大鬧黑風山 ／ 觀世音收伏熊羆怪 |
| `xiyouji-hui-018.md` | 第十八回 | 觀音院唐僧脫難 ／ 高老莊大聖除魔 |
| `xiyouji-hui-019.md` | 第十九回 | 雲棧洞悟空收八戒 ／ 浮屠山玄奘受心經 |
| `xiyouji-hui-020.md` | 第二○回 | 黃風嶺唐僧有難 ／ 半山中八戒爭先 |
| `xiyouji-hui-021.md` | 第二一回 | 護法設莊留大聖 ／ 須彌靈吉定風魔 |
| `xiyouji-hui-022.md` | 第二二回 | 八戒大戰流沙河 ／ 木叉奉法收悟淨 |
| `xiyouji-hui-023.md` | 第二三回 | 三藏不忘本 ／ 四聖試禪心 |
| `xiyouji-hui-024.md` | 第二四回 | 萬壽山大仙留故友 ／ 五莊觀行者竊人參 |
| `xiyouji-hui-025.md` | 第二五回 | 鎮元仙趕捉取經僧 ／ 孫行者大鬧五莊觀 |
| `xiyouji-hui-026.md` | 第二六回 | 孫悟空三島求方 ／ 觀世音甘泉活樹 |
| `xiyouji-hui-027.md` | 第二七回 | 屍魔三戲唐三藏 ／ 聖僧恨逐美猴王 |
| `xiyouji-hui-028.md` | 第二八回 | 花果山群妖聚義 ／ 黑松林三藏逢魔 |
| `xiyouji-hui-029.md` | 第二九回 | 脫難江流來國土 ／ 承恩八戒轉山林 |
| `xiyouji-hui-030.md` | 第三○回 | 邪魔侵正法 ／ 意馬憶心猿 |
| `xiyouji-hui-031.md` | 第三一回 | 豬八戒義激猴王 ／ 孫行者智降妖怪 |
| `xiyouji-hui-032.md` | 第三二回 | 平頂山功曹傳信 ／ 蓮花洞木母逢災 |
| `xiyouji-hui-033.md` | 第三三回 | 外道迷真性 ／ 元神助本心 |
| `xiyouji-hui-034.md` | 第三四回 | 魔王巧算困心猿 ／ 大聖騰那騙寶貝 |
| `xiyouji-hui-035.md` | 第三五回 | 外道施威欺正性 ／ 心猿獲寶伏邪魔 |
| `xiyouji-hui-036.md` | 第三六回 | 心猿正處諸緣伏 ／ 劈破傍門見月明 |
| `xiyouji-hui-037.md` | 第三七回 | 鬼王夜謁唐三藏 ／ 悟空神化引嬰兒 |
| `xiyouji-hui-038.md` | 第三八回 | 嬰兒問母知邪正 ／ 金木參玄見假真 |
| `xiyouji-hui-039.md` | 第三九回 | 一粒丹砂天上得 ／ 三年故主世間生 |
| `xiyouji-hui-040.md` | 第四○回 | 嬰兒戲化禪心亂 ／ 猿馬刀歸木母空 |
| `xiyouji-hui-041.md` | 第四一回 | 心猿遭火敗 ／ 木母被魔擒 |
| `xiyouji-hui-042.md` | 第四二回 | 大聖慇懃拜南海 ／ 觀音慈善縛紅孩 |
| `xiyouji-hui-043.md` | 第四三回 | 黑河妖孽擒僧去 ／ 西洋龍子捉鼉回 |
| `xiyouji-hui-044.md` | 第四四回 | 法身元運逢車力 ／ 心正妖邪度脊關 |
| `xiyouji-hui-045.md` | 第四五回 | 三清觀大聖留名 ／ 車遲國猴王顯法 |
| `xiyouji-hui-046.md` | 第四六回 | 外道弄強欺正法 ／ 心猿顯聖滅諸邪 |
| `xiyouji-hui-047.md` | 第四七回 | 聖僧夜阻通天水 ⚠️ *(second hémistiche cassé et amputé — voir « Défauts de l'édition »)* |
| `xiyouji-hui-048.md` | 第四八回 | 魔弄寒風飄大雪 ／ 僧思拜佛履層冰 |
| `xiyouji-hui-049.md` | 第四九回 | 三藏有災沉水宅 ／ 觀音救難現魚籃 |
| `xiyouji-hui-050.md` | 第五○回 | 情亂性從因愛慾 ／ 神昏心動遇魔頭 |
| `xiyouji-hui-051.md` | 第五一回 | 心猿空用千般計 ／ 水火無功難煉魔 |
| `xiyouji-hui-052.md` | 第五二回 | 悟空大鬧金洞 ／ 如來暗示主人公 |
| `xiyouji-hui-053.md` | 第五三回 | 禪主吞餐懷鬼孕 ／ 黃婆運水解邪胎 |
| `xiyouji-hui-054.md` | 第五四回 | 法性西來逢女國 ／ 心猿定計脫煙花 |
| `xiyouji-hui-055.md` | 第五五回 | 色邪淫戲唐三藏 ／ 性正修持不壞身 |
| `xiyouji-hui-056.md` | 第五六回 | 神狂誅草寇 ／ 道迷放心猿 |
| `xiyouji-hui-057.md` | 第五七回 | 真行者落伽山訴苦 ／ 假猴王水簾洞謄文 |
| `xiyouji-hui-058.md` | 第五八回 | 二心攪亂大乾坤 ／ 一體難修真寂滅 |
| `xiyouji-hui-059.md` | 第五九回 | 唐三藏路阻火焰山 ／ 孫行者一調芭蕉扇 |
| `xiyouji-hui-060.md` | 第六○回 | 牛魔王罷戰赴華筵 ／ 孫行者二調芭蕉扇 |
| `xiyouji-hui-061.md` | 第六一回 | 豬八戒助力敗魔王 ／ 孫行者三調芭蕉扇 |
| `xiyouji-hui-062.md` | 第六二回 | 滌垢洗心惟掃塔 ／ 縛魔歸主乃修身 |
| `xiyouji-hui-063.md` | 第六三回 | 二僧蕩怪鬧龍宮 ／ 群聖除邪獲寶貝 |
| `xiyouji-hui-064.md` | 第六四回 | 荊棘嶺悟能努力 ／ 木仙庵三藏談詩 |
| `xiyouji-hui-065.md` | 第六五回 | 妖邪假設小雷音 ／ 四眾皆遭大厄難 |
| `xiyouji-hui-066.md` | 第六六回 | 諸神遭毒手 ／ 彌勒縛妖魔 |
| `xiyouji-hui-067.md` | 第六七回 | 拯救駝羅禪性穩 ／ 脫離穢污道心清 |
| `xiyouji-hui-068.md` | 第六八回 | 朱紫國唐僧論前世 ／ 孫行者施為三折肱 |
| `xiyouji-hui-069.md` | 第六九回 | 心主夜間修藥物 ／ 君王筵上論妖邪 |
| `xiyouji-hui-070.md` | 第七○回 | 妖魔寶放煙沙火 ／ 悟空計盜紫金鈴 |
| `xiyouji-hui-071.md` | 第七一回 | 行者假名降怪 ／ 觀音現像伏妖王 |
| `xiyouji-hui-072.md` | 第七二回 | 盤絲洞七情迷本 ／ 濯垢泉八戒忘形 |
| `xiyouji-hui-073.md` | 第七三回 | 情因舊恨生災毒 ／ 心主遭魔幸破光 |
| `xiyouji-hui-074.md` | 第七四回 | 長庚傳報魔頭狠 ／ 行者施為變化能 |
| `xiyouji-hui-075.md` | 第七五回 | 心猿鑽透陰陽體 ／ 魔王還歸大道真 |
| `xiyouji-hui-076.md` | 第七六回 | 心神居舍魔歸性 ／ 木母同降怪體真 |
| `xiyouji-hui-077.md` | 第七七回 | 群魔欺本性 ／ 一體拜真如 |
| `xiyouji-hui-078.md` | 第七八回 | 比丘憐子遣陰神 ／ 金殿識魔談道德 |
| `xiyouji-hui-079.md` | 第七九回 | 尋洞擒妖逢老壽 ／ 當朝正主救嬰兒 |
| `xiyouji-hui-080.md` | 第八○回 | 女育陽求配偶 ／ 心猿護主識妖邪 |
| `xiyouji-hui-081.md` | 第八一回 | 鎮海寺心猿知怪 ／ 黑松林三眾尋師 |
| `xiyouji-hui-082.md` | 第八二回 | 姹女求陽 ／ 元神護道 |
| `xiyouji-hui-083.md` | 第八三回 | 心猿識得丹頭 ／ 姹女還歸本性 |
| `xiyouji-hui-084.md` | 第八四回 | 難滅伽持圓大覺 ／ 法王成正體天然 |
| `xiyouji-hui-085.md` | 第八五回 | 心猿妒木母 ／ 魔主計吞禪 |
| `xiyouji-hui-086.md` | 第八六回 | 木母助威征怪物 ／ 金公施法滅妖邪 |
| `xiyouji-hui-087.md` | 第八十七回 | 鳳仙郡冒天止雨 ／ 孫大圣勸善施霖 |
| `xiyouji-hui-088.md` | 第八八回 | 禪到玉華施法會 ／ 心猿木母授門人 |
| `xiyouji-hui-089.md` | 第八九回 | 黃獅精虛設釘鈀宴 ／ 金木土計鬧豹頭山 |
| `xiyouji-hui-090.md` | 第九○回 | 師獅授受同歸一 ／ 盜道纏禪靜九靈 |
| `xiyouji-hui-091.md` | 第九一回 | 金平府元夜觀燈 ／ 玄英洞唐僧供狀 |
| `xiyouji-hui-092.md` | 第九二回 | 三僧大戰青龍山 ／ 四星挾捉犀牛怪 |
| `xiyouji-hui-093.md` | 第九三回 | 給孤園問古談因 ／ 天竺國朝王遇偶 |
| `xiyouji-hui-094.md` | 第九四回 | 四僧宴樂御花園 ／ 一怪空懷情慾喜 |
| `xiyouji-hui-095.md` | 第九五回 | 假合真形擒玉兔 ／ 真陰歸正會靈元 |
| `xiyouji-hui-096.md` | 第九六回 | 寇員外喜待高僧 ／ 唐長老不貪富貴 |
| `xiyouji-hui-097.md` | 第九七回 | 金酬外護遭魔蟄 ／ 聖顯幽魂救本原 |
| `xiyouji-hui-098.md` | 第九八回 | 猿熟馬馴方脫殼 ／ 功成行滿見真如 |
| `xiyouji-hui-099.md` | 第九九回 | 九九數完魔滅盡 ／ 三三行滿道歸根 |
| `xiyouji-hui-100.md` | 第一○○回 | 徑回東土 ／ 五聖成真 |
