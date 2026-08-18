---
title: Infrastructure — Audit de santé Claude Code (/doctor, 2026-08-11)
type: infrastructure
tags:
- rd
- infrastructure
- claude-code
- outillage
- contexte
created: 2026-08-11
updated: 2026-08-11
sources: []
links:
- atelier/rd/infrastructure/etat-serveur-hermes-2026-08-11
statut_experience: exploratoire
---

# Claude Code Health Check Report

> Produit par Sidy le 2026-08-11 via la commande `/doctor` de l'outil CLI Claude
> Code — diagnostic mécanique de l'installation, non un jugement sur le
> contenu doctrinal. Rapport brut conservé tel quel (anglais d'origine) ;
> recommandations d'action non exécutées (Cmd 6 : aucun plan validé ne les
> couvre à ce jour — notamment le point « trimmer `CLAUDE.md` », sans objet
> après l'éclatement en protocoles locaux du 2026-08-12).

**Date:** 2026-08-11  
**Scope:** Installation and configuration audit  
**Status:** Healthy with optimization opportunities

---

## Executive Summary

Claude Code installation is functional and up-to-date, but operating with unnecessary context overhead. Two CLAUDE.md files in the wiki directories consume ~28k est. tokens (~14% of available context) due to potentially derivable content. Permission mode and auto-updates are not configured. No critical issues detected.

---

## Findings by Check

### ✅ Check 0: Installation Health

**Status:** Healthy

- **Version:** 2.1.227 (Claude Code)
- **Install Method:** npm global (`/usr/bin/claude`)
- **Config Files:** All valid JSON
- **Agent Definitions:** None (expected)
- **Hooks:** None configured (expected)
- **Note:** Install method not recorded in `~/.claude.json`; should be set to `npm` for future reference

### ✅ Check 1: Unused Extensions

**Status:** Clean — no unused extensions to remove

- Skills: 0 installed
- Plugins: 0 installed  
- MCP Servers: 0 configured
- Tool Usage: 887 Bash invocations, 527 Read, 285 Edit over recent session window

### ✅ Check 2: LOCAL CLAUDE.md Deduplication

**Status:** No duplicates detected

- `/root/wiki/CLAUDE.md` (user-scope) and `./wiki/CLAUDE.md` (checked-in) represent the same content state
- No contradictions between local and checked-in guidance

### ⚠️ Check 3: Trim Derivable Content

**Status:** Review recommended

| File | Size | Lines | Est. Tokens | Status |
|------|------|-------|-------------|--------|
| `./wiki/CLAUDE.md` | 56.8 KB | 912 | ~14.2k | **EXCEEDS THRESHOLD** (>40KB) |
| `./regression-test/sandbox/CLAUDE.md` | 32.8 KB | 553 | ~8.2k | Borderline |
| `./regression-test-doctrinal/sandbox/CLAUDE.md` | 32.8 KB | 553 | ~8.2k | Borderline |

**Recommendation:** Audit `./wiki/CLAUDE.md` for derivable content (tech stack listed in `package.json`, directory layouts visible via `ls`, build/test commands in manifest scripts, API signatures copied from source code, generic best practices). Content trim could reclaim ~5-8k tokens per session.

### ⏸️ Check 4: Lazy-Load Migration

**Status:** Deferred until Check 3 cuts complete

After trimming derivable content, remaining task-specific workflows and subdirectory guidance candidates for migration to `.claude/skills/` as lazy-loaded skills.

### ✅ Check 5: Hook Performance

**Status:** No hooks configured — nothing to audit

### 📊 Check 6: Context Usage Summary

**Always-Resident Components:**

| Component | Est. Tokens | % of ~5% Budget |
|-----------|-------------|-----------------|
| `./wiki/CLAUDE.md` | ~14.2k | 7.1% |
| `./regression-test/sandbox/CLAUDE.md` | ~8.2k | 4.1% |
| `./regression-test-doctrinal/sandbox/CLAUDE.md` | ~8.2k | 4.1% |
| **Subtotal CLAUDE.md** | **~30.6k** | **15.3%** |
| Skills listing | 0 | 0% |
| MCP servers (deferred) | 0 | 0% |
| Plugins | 0 | 0% |

**Total resident overhead:** ~30.6k est. tokens (~15% of a 200k context window), concentrated in three CLAUDE.md files.

### ✅ Check 7: Version Currency

**Status:** Up to date

- **Installed:** 2.1.227
- **Latest Available:** 2.1.227 (npm latest channel)
- **Status:** Current
- **Auto-Updates:** Disabled (proposal below)

### ⚠️ Check 8: Auto Mode Configuration

**Status:** Not configured — permission mode not set

- **Current Default:** Falls back to `default` mode (prompts for each action)
- **Recommendation:** Set `permissions.defaultMode` to `auto` in `~/.claude/settings.json`
- **Benefit:** Safety classifier auto-approves routine actions; reduces permission prompts

### ✅ Check 9: Pre-Approve Read-Only Commands

**Status:** No action needed

- **Transcript scan window:** 50 recent sessions
- **Tool denials found:** 0
- **Most-used commands:** `ls`, `grep`, `git status`, `git diff`, `git log` — all auto-allowed
- **Conclusion:** No pre-approval rules needed; read-only validation is adequate

---

## Recommended Actions

### Priority 1: Address Context Overhead
1. Read `./wiki/CLAUDE.md` to identify derivable sections (directory layout, tech stack, build commands in `package.json`, API signatures, generic best practices)
2. Propose and apply cuts to recover ~5-8k tokens per session
3. After trim, consider migrating task-specific workflows to lazy-loaded skills

### Priority 2: Configure Permissions & Updates
1. Enable auto mode: add `"permissions": {"defaultMode": "auto"}` to `~/.claude/settings.json`
2. Enable auto-updates: set `autoUpdates: true` in `~/.claude.json`

### Priority 3: Clarify Install Metadata
- Set `installMethod: "npm"` in `~/.claude.json` for accurate tracking in future audits

---

## How to Undo Changes

All proposed actions are reversible:
- **Context trims:** Remove deleted lines from `./wiki/CLAUDE.md` (exact deletions will be quoted in the proposal)
- **Auto mode:** Delete the `permissions.defaultMode` key from `~/.claude/settings.json`
- **Auto-updates:** Set `autoUpdates: false` in `~/.claude.json`

---

## Next Steps

Awaiting R&D approval on:
1. Whether to trim wiki CLAUDE.md (requires review of file content)
2. Whether to enable auto mode and auto-updates

All findings are read-only diagnostic data; no changes have been made to the system.
