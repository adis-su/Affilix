# Affilix End-to-End Runtime Result

## Test ID
E2E-001

## Initial Run

Pipeline:
Fashion → Modest Fashion → Dress → Work → Minimalist → Rositasari

Status: PASS

Validated:
- Brief normalization: PASS
- Canonical context creation: PASS
- Context propagation: PASS
- Creator identity lock: PASS
- Product identity lock: PASS
- UNKNOWN preservation: PASS
- Strategy synchronization: PASS
- Hook synchronization: PASS
- Storyboard synchronization: PASS
- Visual synchronization: PASS
- Video synchronization: PASS
- Voice synchronization: PASS
- QC: PASS

## Reclassification

New context:
Beauty → Skincare → Skincare Product → Everyday Beauty → Natural Look

State transition:
ACTIVE FASHION CONTEXT → STALE → INVALIDATED → ACTIVE BEAUTY CONTEXT

Validated:
- Fashion-dependent outputs marked stale: PASS
- Canonical context replaced: PASS
- Dependent outputs regenerated: PASS
- No Fashion context leaked into active Beauty state: PASS
- Product/creator state follows current run requirements: PASS
- QC re-run after reclassification: PASS

## Final Status

PASS

## Critical Issues
0

## Major Issues
0

## Minor Issues
0

## Conclusion

E2E-001 validates the full runtime contract and the required stale-state behavior during material context reclassification.
