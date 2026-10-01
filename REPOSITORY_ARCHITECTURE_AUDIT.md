# Affilix — Repository Architecture Audit v1

## Audit Scope

Repository: adis-su/Affilix

Snapshot:
- 148 tracked tree entries
- 5 top-level roots: SKILL.md, ENGINE, CREATOR_LIBRARY, PRODUCT_LIBRARY, EXAMPLES
- 9 production/runtime engines plus niche context loader, workflow, and final package contract
- 10 registered niches
- 4 active niches: Fashion, Beauty, Food & Beverage, Home & Living
- 6 planned niches: Electronics, Lifestyle, Baby & Kids, Pet, Sports & Outdoor, Automotive

## Findings

### A01 — Runtime entry point alignment
Status: PASS

SKILL.md follows the canonical runtime order: Brief → Niche Context → Creator → Strategy → Hook → Storyboard → Production Prompts → QC → Final Package.

### A02 — Universal engine architecture
Status: PASS

Creative engines remain universal. Niche and product-type behavior is loaded as runtime context rather than duplicated into separate engines.

### A03 — Canonical context dependency
Status: PASS

NICHE_CONTEXT_LOADER is positioned before downstream creative decisions and is referenced by SKILL.md and WORKFLOW.md.

### A04 — State invalidation
Status: PASS

WORKFLOW.md, QC, and SKILL.md agree that material upstream changes create STALE dependent state and require regeneration before delivery.

### A05 — Final output contract
Status: PASS

ENGINE/FINAL_UGC_PACKAGE_CONTRACT.md is part of the runtime pipeline and defines production-readiness behavior.

### A06 — Regression coverage
Status: PASS

Regression artifacts cover niche context, cross-run isolation, reclassification, UNKNOWN preservation, final package contract, and runtime entry point behavior.

### A07 — Niche registry coverage
Status: PASS

The repository contains ten registered niche directories. Active/planned separation is preserved. Planned niches do not receive fabricated detailed runtime rules.

### A08 — Creator library structure
Status: PASS

Rositasari has separated identity, profile, visual references, wardrobe, expressions, and poses. This matches the creator loading contract.

### A09 — Naming consistency
Status: PASS WITH NOTES

The engine numbering is coherent for the nine production engines. Supporting runtime components are intentionally named by function rather than forced into the numeric sequence.

Examples contain broad matrix files and per-case fixtures. This is acceptable. Future regression artifacts should prefer:
- MATRIX for matrices
- FIXTURE for inputs
- RESULT for results
- CONTRACT_TEST for contract validation

Existing files should not be renamed merely for cosmetic consistency.

### A10 — Documentation completeness
Status: PASS WITH NOTES

Core runtime documentation exists for the current architecture.

One structural improvement remains: add a single repository map/index so a future maintainer can understand where to start without traversing the repository manually.

## Redundancy Review

No deletion is justified by this audit.

The apparent duplication between universal runtime matrices, niche test matrices, E2E tests, and golden package tests serves different validation scopes and should remain.

## Dependency Review

Canonical dependency chain:

SKILL.md
→ BRIEF ANALYZER
→ NICHE CONTEXT LOADER
→ CREATOR SELECTOR
→ CONTENT STRATEGY
→ HOOK
→ STORYBOARD
→ VISUAL / VIDEO / VOICE
→ QC
→ FINAL PACKAGE CONTRACT

This matches the current documented workflow.

## Risk Register

| Risk | Severity | Current State |
|---|---|---|
| Cross-run context leakage | Critical | Covered by tests |
| Stale output after reclassification | Critical | Covered by workflow + tests |
| Product/creator identity drift | Critical | Covered by library + QC |
| Unsupported claims | Major | Covered by Product Library + QC |
| UNKNOWN becoming invented fact | Major | Covered by runtime tests |
| Inconsistent regression naming | Minor | Documented convention |
| Maintainer navigation cost | Minor | Repository map recommended |

## Audit Conclusion

Architecture status: PASS

No destructive cleanup is recommended.

The repository is structurally aligned with the current Affilix architecture. The remaining improvement is navigational rather than architectural: provide one concise repository map/index and use the documented regression naming convention for future additions.

## Next Maintenance Rule

Before adding a new engine, niche, product type, or major runtime rule:

1. identify its source of truth
2. update the relevant schema/registry
3. update runtime dependencies
4. add or update a regression fixture
5. validate final package compatibility
6. update the repository map when structure changes
