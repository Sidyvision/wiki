# Brouillons d'extension principielle des prompts — roue zodiacale (étape 2)

## Objet
Étendre les 12 prompts depuis l'étage principiel zodiacal, conformément à la
directive Sidy (2026-08-08) : la roue zodiacale est l'étage principiel, les rôles du
label en dérivent — les prompts s'étendent DEPUIS les principes, jamais l'inverse
(fonction de Barzakh, fiche 16 §IV).

## Sources
- meta/projet-unifie/16-mise-en-regard-theme-natal-roue-agents-2026-08-08.md (§V chantier)
- doctrinal/discernement/2026-07-05_correspondances-fonctions-initiatiques-entreprise.md
  (volet b, verdict Sidy 2026-07-14)
- doctrinal/discernement/2026-07-26_zodiaque-fonction-barzakh.md

## Convention
Chaque brouillon propose DEUX paragraphes à insérer après « ## Archetype served »,
avant « ## Scope ». Rien d'autre n'est modifié : rôles, périmètres, garde-fous,
handoffs intacts. Texte en anglais pour rester dans la langue des prompts.

1. « ## Zodiac principle » — l'étage principiel du signe, descente principe → rôle
   → « Daily work from this aspect ».
2. « ## Your sign in Sidy's natal chart (harmonization context) » — la situation
   natale DU SIGNE chez Sidy (fiche meta/personnel/2026-06-20_theme-astrologique.md,
   correctif éphéméride 2026-08-08, cadre traditionnel 7 planètes) + instruction
   d'harmonisation. Signes occupés par des planètes : Cancer (Soleil+Mercure),
   Capricorne (Lune+Mars exalté), Sagittaire (ASC+Saturne). Signes vides : état
   natal dérivé du maître traditionnel du signe.

## Contenu (9 brouillons, statuts du volet b respectés)
| Fichier | Agent | Position | Signe | Statut volet b |
|---|---|---|---|---|
| 01-ar-music-aries.md | ar-music | 1 | Bélier | cohérente |
| 02-visual-da-taurus.md | visual-da | 2 | Taureau | cohérente |
| 03-production-gemini.md | production | 3 | Gémeaux | cohérente |
| 04-admin-legal-cancer.md | admin-legal | 4 | Cancer | SOLIDE |
| 06-distribution-virgo.md | distribution | 6 | Vierge | cohérente |
| 07-marketing-libra.md | marketing | 7 | Balance | cohérente (tenue modeste, « correcte sans être frappante ») |
| 09-studio-sagittarius.md | studio | 9 | Sagittaire | cohérente |
| 10-gardien-capricorn.md | gardien | 10 | Capricorne | SOLIDE |
| 11-fanzine-aquarius.md | fanzine | 11 | Verseau | cohérente |

## Hors périmètre de ce lot (en attente de verdict)
- Position 5 (accounting) : échec documenté Lion/Comptabilité — instruction fiche 16
  §III propose Capricorne (axe solsticial) plutôt que Lion. Attend le verdict Sidy.
- Positions 8 (publication, Scorpion) et 12 (commerce, Poissons) : faibles, non
  acquises — à reprendre à nouveaux frais depuis les principes, après instruction.

## Procédure d'intégration (après relecture/verdict Sidy)
1. Claude Code ayant la main sur le wiki : intégrer seulement après sa fin (ou avec son accord).
2. Insérer le paragraphe dans chaque prompt source hermes-prompts/NN-*.md (bumped updated:).
3. Resynchroniser SOUL.md verbatim depuis le prompt source (règle fiche 15 §VIII.7).
4. Redémarrer le gateway du profil pour prise d'effet
   (systemctl --user restart hermes-gateway-<profil>).
5. Consigner au registre rd/ : extension principielle appliquée, positions traitées,
   positions en attente.
