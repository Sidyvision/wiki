---
title: "Brief technique — Incident ZWJ et mise à jour sécurité"
date: 2026-08-22
type: brief
status: transmis
destinataires: [studio, gardien]
references:
  - atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md
  - CLAUDE.md (Commandement 15)
---

# Brief technique — Incident ZWJ et mise à jour sécurité

## Objet

Signalement d'incident de sécurité résolu et mise à jour du protocole de sécurité. Nécessite prise en compte et intégration dans vos procédures respectives.

## Résumé de l'incident

**Nature** : Contamination par caractères Unicode Zero Width Joiner (U+200D) dans 31 fichiers du dépôt, totalisant 156 occurrences.

**Étendue** :
- `meta/` : 44 occurrences
- `atelier/` : 106 occurrences
- `doctrinal/` : 3 occurrences
- `_inbox/` : 1 occurrence

**Pattern** : caractères insérés systématiquement entre le "H" et "ermes" dans le mot "Hermes" (l'outil technique).

**Origine** : Artefact de formatage (probablement copier-coller depuis source externe ou éditeur configuré pour insertion automatique de ZWJ). Aucune preuve d'exploitation malveillante.

**Impact** : Aucun impact fonctionnel direct, mais risque de sécurité latent (dissimulation de code malveillant, contournement de filtres, exfiltration de données).

## Actions correctives appliquées

1. ✅ **Nettoyage complet** : 156 occurrences supprimées dans 31 fichiers
2. ✅ **Commandement 15 ajouté** au protocole racine CLAUDE.md (Hygiène Unicode)
3. ✅ **Pre-commit hook installé** : détection automatique bloquante avant commit
4. ✅ **Rapport d'incident consigné** : `atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`

## Ce qui change pour vous

### Pour Studio (R&D, exploration)

1. **Audit des outils d'édition** : identifier si l'un de vos outils (éditeur de texte, convertisseur PDF/DOCX → MD, clipboard manager) insère des caractères ZWJ
2. **Validation des fichiers externes** : tout fichier importé depuis `raw/` doit être scanné avant intégration
3. **Documentation** : ajouter une note dans vos procédures de travail sur l'interdiction des caractères invisibles

### Pour Gardien (vigilance, contrôle)

1. **Intégrer au périmètre de vigilance** : les caractères Unicode invisibles sont désormais un vecteur de risque à surveiller
2. **Vérification périodique** : lors des audits de sécurité, scanner pour U+200B, U+200C, U+200D, U+FEFF, U+200E, U+200F
3. **Pre-commit hook** : le hook est actif et bloquera tout commit contenant ces caractères. Si vous détectez un contournement, signaler immédiatement.

### Procédure de nettoyage (si contamination détectée à nouveau)

```bash
# Nettoyage ponctuel
perl -pi -e 's/[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{200E}\x{200F}]//g' <fichier>

# Nettoyage complet du dépôt
find /root/wiki -name '*.md' -exec perl -pi -e 's/[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{200E}\x{200F}]//g' {} \;

# Vérification
grep -rP '[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{200E}\x{200F}]' /root/wiki --include="*.md"
```

## Références

- **Rapport d'incident** : `atelier/rd/incidents/2026-08-22_zero-width-joiner-contamination.md`
- **Protocole mis à jour** : `CLAUDE.md` (Commandement 15, §X)
- **Pre-commit hook** : `.git/hooks/pre-commit` (actif, exécutable)

## Prochaines étapes

1. **Studio** : audit des outils d'édition, identification de la source de contamination
2. **Gardien** : intégration au périmètre de vigilance, documentation
3. **Sidy** : validation finale du brief et des recommandations

---

**Établi par** : Hermes Agent  
**Date** : 2026-08-22  
**Statut** : Transmis pour prise en compte
