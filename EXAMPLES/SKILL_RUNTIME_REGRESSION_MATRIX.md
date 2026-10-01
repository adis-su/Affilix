# Affilix — Skill Runtime Regression Matrix

## Purpose

Validate the SKILL.md runtime contract across all currently ACTIVE niches and across failure-prone state conditions.

## Test Scope

Active niches:
- Fashion
- Beauty
- Food & Beverage
- Home & Living

Runtime conditions:
- normal production
- UNKNOWN preservation
- source conflict
- cross-run isolation
- material reclassification

## Matrix

| ID | Scenario | Initial Context | Runtime Condition | Expected Result |
|---|---|---|---|---|
| R001 | Fashion normal | Fashion → Modest Fashion → Dress → Work → Minimalist | Normal run | PASS |
| R002 | Beauty normal | Beauty → Skincare → Skincare Product → Everyday Beauty → Natural Look | Normal run | PASS |
| R003 | Food normal | Food & Beverage → Drinks → Drink → Everyday Consumption → Casual | Normal run | PASS |
| R004 | Home normal | Home & Living → Organization → Organization Product → Everyday Home → Minimalist | Normal run | PASS |
| R005 | Fashion UNKNOWN | Fashion → Bags → Bag → Everyday → Minimalist | Capacity/material absent | UNKNOWN preserved; PASS |
| R006 | Beauty UNKNOWN | Beauty → Skincare → Skincare Product → Everyday Beauty → Natural Look | Ingredients/clinical evidence absent | UNKNOWN preserved; PASS |
| R007 | Food UNKNOWN | Food & Beverage → Snacks → Snack → Everyday Consumption → Casual | Ingredients/taste/nutrition absent | UNKNOWN preserved; PASS |
| R008 | Home UNKNOWN | Home & Living → Organization → Organization Product → Everyday Home → Minimalist | Capacity/material absent | UNKNOWN preserved; PASS |
| R009 | Source conflict | Fashion → Dress | Explicit product fact conflicts with style interpretation | Explicit fact wins; conflict surfaced; PASS |
| R010 | Cross-run isolation | Fashion → Streetwear → Top | Previous Fashion run followed by Beauty run | No stale Fashion state; PASS |
| R011 | Reclassification | Beauty → Skincare | Changed to Food & Beverage → Drinks | Dependents stale, invalidated, regenerated; PASS |
| R012 | Final readiness | Any active niche | QC PASS | PRODUCTION_READY + READY |
| R013 | QC revision | Any active niche | QC REVISION REQUIRED | Affected dependency rerun; no stale delivery |
| R014 | QC blocked | Any active niche | Required factual input missing | BLOCKED + NOT_READY |

## Acceptance Rules

A runtime regression passes only if:

1. SKILL.md pipeline order is respected.
2. Canonical niche context is created before downstream creative decisions.
3. Creator and product identity remain locked.
4. UNKNOWN values remain UNKNOWN without evidence.
5. Explicit facts outrank contextual interpretation.
6. Material upstream changes invalidate dependent outputs.
7. Reclassification replaces, rather than merges with, prior context.
8. No cross-run context leaks into the current run.
9. QC gates final delivery.
10. Final output conforms to ENGINE/FINAL_UGC_PACKAGE_CONTRACT.md.

## Failure Severity

### Critical
- wrong canonical context delivered
- creator identity replaced or materially corrupted
- product identity replaced or materially corrupted
- stale context delivered as current
- cross-run context leakage into production-ready output

### Major
- dependent asset not invalidated after material upstream change
- downstream assets disagree on canonical context
- unsupported claim introduced
- UNKNOWN converted into unsupported fact
- final package bypasses QC

### Minor
- formatting inconsistency
- missing non-material metadata
- redundant internal field

## Regression Result

R001–R014: PASS by contract review against the current SKILL.md, workflow, niche context loader, engine contracts, QC contract, and final package contract.

Critical: 0
Major: 0
Minor: 0

## Interpretation

The runtime entry point is aligned with the current Affilix architecture.

This matrix is a regression baseline. Future changes to SKILL.md, context loading, engine dependencies, QC, or final package structure should be checked against it before being considered production-ready.
