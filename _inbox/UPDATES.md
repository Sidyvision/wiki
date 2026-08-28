# UPDATES — Lot du 2026-08-27 : quatre propositions

> **Lot clos le 2026-08-27** : les quatre fiches ont reçu verdict explicite de
> Sidy (« Je valide l'ensemble des fiches propositions », précisions de
> portée par fiche) et ont été intégrées, chacune sous plan validé (Cmd 6).
> Plus aucune fiche en attente dans `_inbox/` pour ce lot.

Consigne d'origine pour la session d'intégration : **aucune intégration
automatique** pour les fiches restantes. Ce lot dépose quatre fiches de
proposition (`type: meta`), rédigées à la demande de Sidy. Conformément à
Cmd 6 (pas d'écriture sans plan validé) et Cmd 13 (porte humaine sur tout ce
qui engage), chacune n'est intégrée qu'après verdict explicite, fiche par
fiche.

## Statut du lot

1. **Queue de tâches** — **validée et intégrée le 2026-08-27.** Fiche de
   conception déplacée vers `meta/projet-unifie/proposition-queue-taches-
   2026-08-27.md` (archive), fichier réel créé :
   `meta/projet-unifie/queue-idees.md`. Deux points ouverts tranchés à la
   validation : champ `priorite` adopté, marqueur d'insertion `QUEUE`. Ne
   reste plus en attente dans `_inbox/`.

2. **`proposition-cycle-consultation-choura-2026-08-27.md`** — **validée et
   intégrée le 2026-08-27, exécution complète (wiki + cron réel).**
   `meta/projet-unifie/choura/cycle-2026-08-28.md` créé (premier cycle).
   Job cron ajouté aux 12 profils `.hermes` (cadence 2h, ordre zodiacal,
   Gardien en ouverture/clôture). Fiche déplacée vers `meta/projet-unifie/`.

3. **`proposition-pole-usul-2026-08-27.md`** — **validée et intégrée le
   2026-08-27.** Supersède `meta/projet-unifie/proposition-pole-fiqh-2026-07-06.md`
   (validée le 2026-07-06), désormais `deprecated` avec pointeur.
   `doctrinal/CLAUDE.md` amendé (action EXAMEN DE FIQH → EXAMEN D'USÛL, bloc
   générique `branche: fiqh | mantiq | mustalah-hadith`). Fiche déplacée vers
   `meta/projet-unifie/`. Ne reste plus en attente dans `_inbox/`.

4. **`proposition-discernement-image-organique-2026-08-27.md`** — **validée
   et intégrée le 2026-08-27, exécution partielle (gabarit seul).**
   `doctrinal/discernement/_template.md` amendé (champ `maturite`
   ajouté au Sceau). Rétroportage sur les ~38 fiches existantes différé
   explicitement (Sidy) : renseigné par les agents au fil de l'eau. Fiche
   déplacée vers `meta/projet-unifie/`.

## Action attendue

Lot clos — les quatre verdicts ont été rendus et exécutés le 2026-08-27 (voir
détail par item ci-dessus). Reste en périmètre pour une session ultérieure,
non fait ici : câblage effectif d'un canal Discord dédié pour la Choura (si
Sidy en crée un — les jobs cron sont posés sans `deliver` Discord tant que le
canal n'est pas communiqué), et toute décision de commit/push wiki ou de
redémarrage des services `hermes-gateway-*` (aucun des deux fait dans ce
chantier, sur consigne explicite).
