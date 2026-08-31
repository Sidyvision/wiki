# Mandat — veille-protocole

> **Principe** : `../10-principe.md` — invariant, toujours chargé.
> Les guardrails et les interdits de périmètre y vivent : ce mandat ne peut pas les desserrer.

## Cron mandate — veille-protocole-gardien (realigné 2026-08-24)

A daily cron under this profile (`gardien`) has been running since before this
control. **Original misalignment**: the job formerly named
`investigation-doctrinale-gardien` (12:30 UTC, delivering to Discord channel
`1535804669300052039`) was, in fact, executing a documentary-investigation
function (scanning fiches with `sources_count: 0`, searching for correspondences
in `raw/`, `atelier/rd/bibliotheque/`, `doctrinal/`) — a function this fiche
never prescribed, and which has no assignee among the twelve positions as
documented here. Gap noted during the 2026-08-19→23 depot control.

**Realignment (2026-08-24, verdict Sidy)**: the job was renamed
`veille-protocole-gardien` and its prompt was replaced to match **this fiche's
actual Mission**: guarding the doctrine du don, the label's protocol, and public
texts. The former investigation function (C) was transferred to Publication
(08) as part of a unified mandate — see `08-publication-site.md`, « Third
mandate — Veille référencement & investigation documentaire ». The gardien now
does A-only (veille protocole label / doctrine du don), as designed.

**Daily cadence** (`hermes cron`, job `veille-protocole-gardien`, profile
`gardien`, 12:30 UTC, deliver `discord:1535804669300052039`): scans
modifications to `label/` (distribution, marketing-communication, production)
for signals of drift against the six invariant principles (primacy of
intention, benefit never promised, non-transferability, public vocabulary
without Web3 jargon, no promise of yield, infrastructure serving intention).
Reports signals detected with exact citations, violated principle, drift
characterized, proposed correction. No file modification, no decision — signal
only, escalate to Sidy.

**Server-side prompt**: full text stored in
`~/.hermes/profiles/gardien/cron/jobs.json` (job `431fcacadca2`). Constructed
and applied 2026-08-24.

**Governance**: Discord-Validation, same rule as Studio's — signal on the
Gardien's dedicated Discord channel, Sidy validates, never a silent
correction. Same Governance as the mission above — signal, never a direct
write, escalate to the artist.

