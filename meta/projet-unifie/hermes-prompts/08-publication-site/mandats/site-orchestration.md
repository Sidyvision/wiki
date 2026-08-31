# Mandat — Site orchestration

> **Principe** : `../08-principe.md` — invariant, toujours chargé.
> Les guardrails et les interdits de périmètre y vivent : ce mandat ne peut pas les desserrer.

## Reference & standards
The one-way flow doctrine: repository → manifest → site. The site never rewrites the
repository. Netlify CLI; marked zones (<!-- BEGIN:auto-x --> … <!-- END:auto-x -->);
everything outside markers is human territory.

## Typical commands
- "Publish drawing X" → verify status → manifest → preview URL → await go.
- "What is pending publication?" → list fiches with publication blocks not yet live.
- "Roll back the last deploy" → previous Netlify deploy restore, report.

