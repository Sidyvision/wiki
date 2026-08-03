# Session suivante — Tâches restantes (2026-07-27)

## État: Travail suspendu pour manque de crédit API

Session 2026-07-27 a progresse jusqu'au **commit/push du Lot Zodiaque+Référentiels stellaires**. Fiche discernement unique reste à rédiger.

---

## Tâches à compléter

### 1. Rédaction fiche discernement (PRIORITÉ HAUTE)

**Fiche** : `doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil.md`

**Plan** : `/root/wiki/meta/plan-fiche-discernement-septenaire-transversal-2026-07-27.md` (détaillé, ~1000 lignes attendues)

**Matière source dans _inbox/** (conserver pour cette session) :
- `2026-07-27_investigation-referentiels-stellaires-passe-2.md` — §0 à §5 (contexte complet, sources)
- `2026-07-27_investigation-passe-2-1-verification-gloton.md` — vérifications textuelles
- `2026-07-27_note-integration-sept-ancrages-dedoublement.md` — contexte verdicts Sidy

**Après rédaction** :
- Ajouter ligne à `doctrinal/index.md` (§VII) avec statut final (close ou en cours)
- Ajouter entrée à `doctrinal/annales.md` (append-only, verdict final)
- **Ne pas toucher à `instrument-donnees.yaml`** tant que fiche non close

---

### 2. Validation manifeste & commit final (PRIORITÉ BASSE, Phase 3)

Une fois fiche discernement close (statut: traditionnel) :

```bash
cd /root/wiki
python3 atelier/projets/generer-manifeste.py --repo . --manifeste wiki-manifest.json
git diff --stat
git add wiki-manifest.json instrument-donnees.yaml
git commit -m "ARCHIVAGE: Lot B fermeture — manifeste v0.3.2 validé"
git push
```

**Validation avant commit** :
- ✅ Manifeste génère sans erreur (`generer-manifeste.py` doit refuser les non-close)
- ✅ 0 anomalies cartographie (script Gloton/Mahdi Rouge)
- ✅ Aucun ancrage dans YAML pour fiche discernement si elle est en `en cours` (Cmd 13)

---

## Fichiers à nettoyer (_inbox/)

Après session suivante, supprimer :
- `UPDATES.md` (2026-07-27) — intégré
- `2026-07-26 zodiaque-fonction-barzakh.md` — copié & renommé
- `2026-07-27_investigation-*.md` — matière brute, peut être archivée en `meta/` si utile
- `2026-07-27_note-integration-*.md` — idem
- `spec-anneau-zodiacal.md` — copié à `atelier/projets/`
- Fichiers outils résiduels : `generer-cartographie.py`, `tradition-primordiale-graphe-live.html` (ne pas supprimer si utiles ailleurs)

Garde en attente pour analyse future (hors scope 2026-07-27) :
- `2026-07-26_investigation-referentiels-stellaires-cycles.md` (cycles, non traité cette session)

---

## Points critiques pour la prochaine session

1. **Hermès = Idrîs** : doit être sourcée sur texte primaire attesté (pas supposée) — vérifier en session
2. **Degré 24 ↔ Gizeh** : statut final *kari-kumi* (pièces s'emboîtent, non collées) — verdict Sidy attendu
3. **Confrontation Gizeh** : consignée, aucun ancrage établi (polaire/solaire distinctes)
4. **Qualification sashimono** : hozo (Ourse→Pléiades, septénaire verdict Sidy) vs kari-kumi (Balance polaire/zodiacale, degré 24)
5. **Non-conflation** : avec quaternaire Homme Universel (2026-07-26) ; avec conflation polaire/solaire ; avec écarts 12/28 et 78000/77760

---

## Crédit API estimé pour la prochaine session

**Rédaction fiche discernement** (~1000 lignes) : ~2000 tokens (faible à modéré)
**Validation & commit** : ~200 tokens

**Total** : ~2200 tokens — faible consommation, largement accessible.

---

## Commandes rapides pour la prochaine session

```bash
# Lire le plan
cat /root/wiki/meta/plan-fiche-discernement-septenaire-transversal-2026-07-27.md

# Lancer la rédaction (CLI ou direct Write tool)
# Fichier cible: /root/wiki/doctrinal/discernement/2026-07-27_septenaire-transversal-balance-degre-soleil.md

# Après rédaction : vérification
python3 /root/wiki/Graphe/generer-cartographie.py --depot /root/wiki --verifier

# Commit & push
cd /root/wiki && git add doctrinal/discernement/2026-07-27_*.md doctrinal/index.md doctrinal/annales.md
git commit -m "ARCHIVAGE: Lot B fermeture — fiche discernement septénaire transversal close"
git push
```

---

## État final (session 2026-07-27)

✅ **Complété** :
- Lot A (Zodiaque=Barzakh) : clos
- Fiches source (Guénon RdM ch10, Mahdi Rouge I-II) : créées
- Spec-anneau-zodiacal.md : 4 amendements appliqués
- instrument-donnees.yaml : 7 ancrages + zodiaque (19/20) + époque
- Annales/index : MAJ pour lots A et B

❌ **En suspens** :
- Fiche discernement unique : plan documenté, rédaction déléguée (crédit API insuffisant)
- Manifeste v0.3.2 : validation dépendante de fiche discernement close
- Nettoyage _inbox/ : à effectuer après

**Commit actuel** : 2655260 (2026-07-27 Lot Zodiaque+Référentiels)

**Branche** : main (à jour avec remote)
