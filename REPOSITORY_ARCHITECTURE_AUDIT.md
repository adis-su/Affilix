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
