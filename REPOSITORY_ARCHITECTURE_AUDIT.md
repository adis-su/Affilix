# Affilix — Repository Architecture Audit v2

## Audit Date
2026-10-01

## Audit Scope

Repository: adis-su/Affilix  
Canonical branch: main  
Audited HEAD: 2e3d0e148efa853cacd0e40129dd40b3f477c8f4

This audit validates the repository against the current canonical architecture:

```text
Brief & Product
→ Niche & Context
→ Creator
→ Content Strategy
→ Hook
→ Storyboard
→ Visual Prompt
→ Video Prompt
→ Voice Script
→ Production Output
```

## Findings

### A01 — Runtime entry point alignment
Status: PASS

`SKILL.md`, `ENGINE/WORKFLOW.md`, and the entry-point contract use the same ten-stage pipeline. `/next` is progression only.

### A02 — Universal engine architecture
Status: PASS

Creative engines remain universal. Niche and product-type behavior is loaded as runtime context.

### A03 — Canonical context dependency
Status: PASS

Niche Context Loader remains upstream of downstream creative decisions.

### A04 — State invalidation
Status: PASS

Material upstream changes mark affected downstream assets STALE and require regeneration. No approval gate is required.

### A05 — Action choreography and reference graph
Status: PASS

Storyboard owns action choreography, reference sequencing, bridge references, and creative timing. Visual Prompt renders reference states. Video Prompt generates reference-to-reference transitions.

### A06 — Duration integrity
Status: PASS

Video generation durations are constrained to `[4, 6, 8, 10]` and final composition must equal requested duration exactly. Provider limits cannot silently redefine campaign duration.

### A07 — Production output contract
Status: PASS

`ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md` is the final assembly contract. It assembles current upstream state and does not introduce a separate QC or Final UGC Package layer.

### A08 — Regression coverage
Status: PASS

Regression coverage exists for active niches, UNKNOWN preservation, source conflicts, cross-run isolation, reclassification, action choreography, reference transitions, and duration segmentation.

### A09 — Niche registry coverage
Status: PASS

Ten niches are registered. Four are active with detailed rules; six remain planned without fabricated detailed behavior.

### A10 — Creator library structure
Status: PASS

Rositasari identity, profile, visual references, wardrobe, expressions, and poses remain separated.

### A11 — Repository runtime isolation
Status: PASS

Each run pins one repository commit and keeps repository state separate from production-run state.

### A12 — Documentation consistency
Status: PASS

Active runtime contracts no longer depend on QC, Final UGC Package, Stage 11, Telegram, or Supabase runtime concepts. Legacy audit/test artifacts are treated as historical only where retained.

## Legacy Artifact Policy

Historical artifacts may preserve evidence of previous architecture, but they must not be cited as active runtime contracts.

The following concepts are not part of the canonical runtime:
- Quality Control stage
- Final UGC Package stage
- Approval Gate
- Stage 11
- Telegram runtime
- Supabase runtime

## Risk Register

| Risk | Severity | Current State |
|---|---|---|
| Cross-run context leakage | Critical | Covered |
| Stale output after upstream change | Critical | Covered |
| Product/creator identity drift | Critical | Covered |
| Unsupported claims | Major | Covered |
| UNKNOWN becoming invented fact | Major | Covered |
| Reference boundary drift | Major | Covered |
| Duration mismatch | Major | Covered |
| Maintainer navigation cost | Minor | Repository map exists in README |

## Audit Conclusion

Architecture status: PASS

The repository is aligned with the current Affilix architecture. The main remaining maintenance task is to keep future regression artifacts and audit snapshots aligned with the canonical ten-stage workflow.


---

## Mode Routing Addendum

### Addendum Date
2026-10-10

### Scope
Phase 01 — Content Mode Architecture.

### Changes Verified
- Added `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md` as the single mode-routing contract.
- Registered `UGC_AFFILIATE` and `QUOTE_CONTENT` as the only supported mode values.
- Updated `SKILL.md`, `ENGINE/AFFILIX_ENTRY_POINT/README.md`, `ENGINE/01_BRIEF_ANALYZER/README.md`, `ENGINE/WORKFLOW.md`, and repository runtime contracts to persist and route by mode.
- Preserved the canonical Stage 01–10 registry and existing UGC engine mappings.
- Defined explicit blockers for Quote Content stages whose mode-specific implementation is not yet available.
- Added `EXAMPLES/CONTENT_MODE_ROUTING_FIXTURES.md` for routing, isolation, blocking, and backward-compatibility checks.
- Updated the repository map and runtime loading order.

### Phase 01 Status
**PASS — routing foundation only.**

The repository now defines the mode-selection boundary and mode-specific intake/dependency behavior. This does not mean Quote Content can yet be produced end-to-end. Quote Content strategy and production remain pending Phases 02 and 03; unsupported downstream stages must block with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED` and must not fall back to UGC logic.

### Required Next Work
1. Implement the Quote Content strategy, pillar, format, and editorial validation contracts.
2. Implement mode-aware image/video/voice and production-output behavior.
3. Add end-to-end Quote Content regression fixtures and validate existing UGC regressions.


---

## Quote Content Strategy Addendum

### Addendum Date
2026-10-10

### Scope
Phase 02 — Editorial Context, Strategy, and Hook Contracts.

### Changes
- Added `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_STRATEGY_CONTRACT.md` with three editorial pillars, a five-format registry, strategy selection, validation, provenance, and invalidation rules.
- Added `ENGINE/04_HOOK_ENGINE/QUOTE_CONTENT_HOOK_CONTRACT.md` with editorial hook families, format-specific opening requirements, and safety/accuracy rules.
- Added the `QUOTE_CONTENT` editorial context branch to `ENGINE/NICHE_CONTEXT_LOADER/README.md`.
- Added mode-specific Stage 04 and Stage 05 runtime output shapes.
- Updated the canonical workflow, mode-routing readiness, repository index, and regression fixtures.
- Kept the canonical ten-stage registry unchanged and retained the UGC strategy/hook branches.

### Phase 02 Status
**PASS — editorial context, strategy, and hook contracts added.**

This phase does not certify end-to-end Quote Content production. Stage 06 Storyboard, Stage 07 Visual Prompt, Stage 08 conditional Voice Script, Stage 09 Video Prompt, and Stage 10 Quote Content assembly remain mode-specific implementation work. Required unsupported stages must block rather than invoke UGC behavior.

### Regression Coverage
Fixtures CM-007 through CM-011 cover product-free editorial context, pillar/format selection, hook alignment, static-image skips, and batch-mix semantics. These are repository fixtures; they have not been represented as a completed automated runtime test suite.


---

## Quote Content Production Addendum

### Addendum Date
2026-10-10

### Scope
Phase 03 — Quote Content production contracts.

### Changes
- Added mode-specific Storyboard contract with editorial story mechanisms, action causality, reference graph, bridge immutability, and exact duration rules.
- Added mode-specific Visual Prompt contract for static quote images and one prompt per Storyboard reference state.
- Added conditional Quote Content Voice Script contract with non-fabrication and dialogue ownership rules.
- Added mode-specific Video Prompt contract with exactly one user-facing prompt per Storyboard scene and exact generation-segment composition.
- Added a distinct Quote Content Production Output contract, separate from the UGC template.
- Wired mode-specific dispatch into the canonical workflow, routing readiness, runtime loader, engine READMEs/runtime contracts, repository index, and regression fixtures CM-012–CM-016.

### Phase 03 Status
**PASS — CONTRACTS ADDED AND STATIC CONSISTENCY CHECKS PASSED; AUTOMATED REGRESSION NOT CLAIMED.**

This addendum records repository contract changes only. It does not claim that image/video generation or end-to-end campaign execution was run. Phase 04 regression and hardening remains pending.
