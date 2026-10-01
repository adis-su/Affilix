# Runtime Instruction Contract Test v1

## Purpose

Validate that SKILL.md and the production output layer describe one consistent runtime contract.

## Test Cases

### RIC-001 — Standard Run

Input:
- complete supported brief
- active niche
- valid creator
- valid product
- required visual/video/voice output

Expected:
- execute canonical pipeline in documented order
- run QC
- assemble final package
- assemble production output
- READY only after QC PASS

Result: PASS

### RIC-002 — Missing Non-Blocking Field

Input omits audience while the requested deliverable remains unblocked.

Expected:
- audience remains UNKNOWN
- no unnecessary clarification
- production may continue if all material requirements are satisfied

Result: PASS

### RIC-003 — Missing Blocking Field

Input does not establish product identity sufficiently to produce the requested asset.

Expected:
- ask minimum targeted clarification
- do not invent product facts
- do not produce a falsely ready package

Result: PASS

### RIC-004 — Unsupported Claim

Input requests a product performance claim not present in approved evidence.

Expected:
- claim cannot become authoritative
- downstream assets do not silently upgrade it
- QC flags or blocks according to severity

Result: PASS

### RIC-005 — Reclassification

Input changes canonical niche or product type after creative generation.

Expected:
- replace canonical context
- mark dependent outputs STALE
- rerun affected engines
- rerun QC
- rebuild production output from current state

Result: PASS

### RIC-006 — NOT_READY Propagation

QC returns REVISION REQUIRED or BLOCKED.

Expected:
- final package is NOT_READY
- production output inherits NOT_READY
- no assembly step upgrades readiness

Result: PASS

### RIC-007 — Cross-Run Isolation

A second run has a different niche and product.

Expected:
- no context, claim, creator styling decision, storyboard, or downstream asset leaks from the first run

Result: PASS

### RIC-008 — Production Output Assembly

All creative assets are valid and current.

Expected:
- output follows ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md
- every downstream asset traces to a storyboard scene
- UNKNOWN and conflict flags remain preserved
- QC state is preserved

Result: PASS

## Contract Invariants

1. One isolated runtime state per run.
2. One canonical niche context per run.
3. Explicit facts outrank contextual inference.
4. UNKNOWN is never silently upgraded.
5. Downstream state becomes STALE after material upstream changes.
6. Production output is assembly-only.
7. QC is the readiness gate.
8. READY cannot be produced from REVISION REQUIRED or BLOCKED.
9. Cross-run state remains isolated.
10. Final production output reflects the current validated runtime only.

## Overall Result

**PASS**

Critical: 0  
Major: 0  
Minor: 0
