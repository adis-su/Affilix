# Production Hardening — Edge Case Matrix v1

## Purpose

Stress-test Affilix against ambiguous, conflicting, incomplete, and unsafe-to-infer inputs.

Expected behavior: preserve UNKNOWN, surface conflicts, ask only the minimum necessary clarification, invalidate stale downstream state after material changes, and never invent facts to complete a package.

## Cases

### EH-001 — Missing Product Type
Fashion product is identified, but product type is not established.

Expected: Niche may resolve to Fashion; Product Type remains UNKNOWN unless supported; no product-type rules are fabricated; ask only if product type materially changes output.

### EH-002 — Conflicting Context
Brief says daily_casual while an approved campaign requirement requires formal_event.

Expected: conflict is visible; campaign requirement outranks contextual inference; canonical context uses the authoritative supported value; dependent creative output follows it.

### EH-003 — Unsupported Product Claim
Brief says a product is very comfortable, but no approved comfort claim or supplied personal experience exists.

Expected: claim is not treated as an authoritative fact; downstream output must not present it as verified; QC flags it if it reaches production assets.

### EH-004 — Missing Creator Attribute
Brief requests a hairstyle detail that Rositasari's canonical identity does not define and that conflicts with canonical hijabi identity.

Expected: canonical creator identity wins; missing attribute remains UNKNOWN; no hair visibility is invented.

### EH-005 — Reclassification Mid-Run
Run begins as Fashion/modest_fashion and later changes to Beauty/skincare.

Expected: canonical context is replaced; Fashion-dependent outputs become STALE; affected downstream engines rerun; no Fashion context leaks into Beauty outputs.

### EH-006 — Incomplete Campaign Brief
Platform, duration, CTA, and audience are absent.

Expected: missing fields remain UNKNOWN; ask only for fields that materially block the requested deliverable; no platform constraints, duration, urgency, or audience are invented.

### EH-007 — Unsupported Offer
Brief requests a 50% discount, but no approved offer exists.

Expected: discount is not invented or treated as verified; QC blocks or requires revision depending on whether the claim is mandatory to the requested deliverable.

### EH-008 — Cross-Run Contamination
Run A uses Fashion/minimalist. Run B uses Home & Living/organization.

Expected: Run B cannot inherit Fashion context, creator styling decisions, product claims, or storyboard state from Run A.

### EH-009 — Product Identity Conflict
Brief describes a beige product, while an approved product reference identifies the product as black.

Expected: source-of-truth hierarchy is applied; conflict is surfaced; product identity is not silently merged.

### EH-010 — Planned Niche
Brief identifies Automotive, but no active detailed niche rules exist.

Expected: Automotive may be classified as PLANNED; no fabricated Automotive behavior; universal rules apply; ask only if missing Automotive behavior materially blocks production.

## Acceptance Criteria

All cases must satisfy:
1. No invented facts.
2. UNKNOWN is preserved where evidence is absent.
3. Explicit authoritative sources outrank creative inference.
4. Material reclassification invalidates dependent state.
5. Cross-run state remains isolated.
6. Unsupported claims cannot silently become approved claims.
7. Final package cannot become READY with unresolved blocking issues.
