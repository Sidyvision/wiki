# Épreuve des contrôles — le récit des deux incidents

> **Rattachement** : `CLAUDE.md`, §VII, *Épreuve des contrôles*. Le **principe** est énoncé à la racine ; ce
> fichier en porte la **procédure**, appelée nominativement et inconditionnellement
> (Cmd 14, discipline du renvoi). Sortie de la racine le 2026-09-09, Phase 2, verdict
> Sidy — **texte inchangé**. `protocoles/` n'est pas un circuit : aucun Sceau, aucun
> régime de liens, cible d'aucun wikilink.

-----

**Pourquoi cette règle existe.** Le dépôt a payé **deux fois la même erreur à un jour
d'intervalle** : un contrôle `lint` obligatoire qui parcourait une arborescence abandonnée et
imprimait « Frontmatter OK » sur zéro fichier (**PRO-01**, 2026-08-31), puis un hook dont le
motif ne correspondait à aucun appel réel (**INF-14**, 2026-09-01), écrit le jour même par la
machine qui venait de consigner PRO-01, et découvert par accident. Récit complet des deux :
`atelier/rd/registre-chantiers.md` et `atelier/annales.md`.

**La forme de la faute est toujours la même** : le contrôle est **muet**, non pas faux.
Il ne se plaint jamais, donc il paraît vert. Un motif qui ne correspond à rien, une
liste de fichiers vide, une dépendance absente (`file` manquant sur le serveur a rendu
un filtrage silencieusement inopérant le 2026-09-01), un chemin qui n'existe plus : dans
tous les cas la sortie est rassurante et le contrôle ne regarde rien.
