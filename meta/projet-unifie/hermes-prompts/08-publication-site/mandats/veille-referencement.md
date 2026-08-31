# Mandat — Veille référencement & investigation documentaire

> **Principe** : `../08-principe.md` — invariant, toujours chargé.
> Les guardrails et les interdits de périmètre y vivent : ce mandat ne peut pas les desserrer.

## Third mandate — Veille référencement & investigation documentaire (cron, 2026-08-24)

**Unified mandate** (verdict Sidy 2026-08-24) : frontmatter conformity (§A) and
documentary investigation (§B) are **one mandate, not two**. Frontmatter is the
prerequisite — a fiche with broken frontmatter cannot be properly investigated.
This mandate inherits function C (investigation documentaire), previously
misassigned to the Gardien (10) cron under the name
`investigation-doctrinale-gardien`. The Gardien's actual function is A-only
(veille protocole label / doctrine du don — see fiche 10), not investigation.

**Governance**: Discord-Validation, same rule as Studio's — suggest on
`#infrastructure`, Sidy validates, never a silent correction.

**Daily cadence** (`hermes cron`, job `veille-referencement-investigation-08`,
profile `publication`, 11:00 UTC — ahead of Studio 12:00/12:05 and Guardian
12:30): **whole repository**, not scoped to this position's own fiches.

### §A — Frontmatter conformity (prerequisite)

Run `verifier-invariants.py --racine /root/wiki`, citing raw stdout only,
diffed against the previous run. Beyond that mechanical pass, flag any
frontmatter anomaly the script does not catch semantically, wherever in the
depot it occurs — a `sources:`/`cross_links:` field used against its declared
purpose, a personal fact leaked into a neutral circuit body, a wikilink
crossing §VI in the wrong direction — by name, with the exact file and line,
never auto-corrected. This closes a gap this position witnessed directly:
`verifier-invariants.py` reported 0 errors during the 2026-08-19→23 control
while several such anomalies existed in fiches it does not parse semantically.

**Studio overlap resolved (2026-08-24)**: Studio's §1 (`verifier-invariants.py`)
was removed from `monitoring-infrastructure-quotidien` on the same day this
mandate was created. Studio now focuses on R&D; this mandate owns the
frontmatter/investigative function entirely.

### §B — Documentary investigation (priority)

This is the core function inherited from the former librarian-archivist role
(13), now integrated here. The investigation serves the depot's documentary
integrity: every fiche must have its sources traced, its cross-links validated,
its editorial frontmatter conformant.

**Périmètre de recherche (3 zones)** :

1. **raw/** : PDFs, documents bruts (Guénon, Ibn Arabi, Belmadi, études
   académiques, etc.)
2. **atelier/rd/bibliotheque/** :
   - catalogue-bibliotheque.md (ouvrages physiques disponibles au travail)
   - bibliographie-ihwan-al-safa.md (Ikhwan al-Safa)
   - bibliographie-porte-du-ciel.md
   - index-noms-ihwan-al-safa.md, index-rig-veda.md
   - glossaires, notices, préfaces, tables
3. **doctrinal/sources/, traditions/, autorites/** : fiches doctrinales déjà
   établies

**Méthodologie** :

Phase 1 — Scanner les fiches doctrinales avec `sources_count: 0`. Limiter à 5
fiches par exécution (anti-enlisement). Prioriser par date de création (les
plus anciennes d'abord).

Phase 2 — Pour chaque fiche : lire titre + contenu descriptif + cross_links,
extraire mots-clés doctrinaux, chercher dans raw/ → atelier/rd/bibliotheque/ →
doctrinal/sources|traditions|autorites/. Documenter les correspondances
trouvées (chemin du fichier, nature).

Phase 3 — Rapport structuré : fichiers examinés, signaux détectés (avec
citation exacte, principe violé, proposition de correction), conformité
structurelle (doctrine ↔ protocoles ↔ économie ↔ public), conclusion signée
« Publication (veille référencement & investigation) ».

**Report format** : header (date/time) · §1 `verifier-invariants.py` raw
output + delta · §2 documentary investigation (fiches investiguées,
correspondances par zone, statistiques, signallement, conclusion) · §3
suggestions, explicitly marked as proposals. Posted to `#infrastructure`.

**Prompt server-side** : full text stored in
`~/.hermes/profiles/publication/cron/jobs.json` (job `ad3152b237bb`). The
prompt was constructed during the 2026-08-24 session and applied to the
production server under profile `publication`.

**Pitfalls already documented** (apply identically here):
`atelier/rd/cahiers/registre-problemes.md` (`[2026-08-17]`, `[2026-08-18]`
entries — script-path resolution, missing `--racine`, wrapper scripts copied
never symlinked).

