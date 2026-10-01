# UGC Production Template Contract Test

## Purpose

Verify that the standardized production output template preserves the existing Affilix contracts.

## Checks

### TPL-001 — Required Sections

Expected sections:
- Run Metadata
- Creative Brief
- Creator
- Product
- Canonical Niche Context
- Content Strategy
- Hook
- Storyboard
- Visual Prompts
- Video Prompts
- Voice Script
- CTA
- QC
- Production Readiness Gate

Result: PASS

### TPL-002 — UNKNOWN Preservation

Missing material, size, branding, audience, platform, duration, or offer data must remain UNKNOWN.

Result: PASS

### TPL-003 — Identity Lock

Creator and product identity cannot be changed during assembly.

Result: PASS

### TPL-004 — Context Integrity

The package contains exactly one canonical niche context and does not reclassify during assembly.

Result: PASS

### TPL-005 — Storyboard Traceability

Every downstream visual/video/voice asset must reference a storyboard scene.

Result: PASS

### TPL-006 — Claim Integrity

Assembly cannot introduce unsupported claims, testimonials, offers, scarcity, guarantees, or performance claims.

Result: PASS

### TPL-007 — QC Gate

READY requires QC PASS, current canonical context, no STALE dependent state, valid identity, and complete final contract.

Result: PASS

### TPL-008 — NOT_READY Protection

REVISION, BLOCKED, stale state, identity failure, claim failure, or incomplete required data prevents READY status.

Result: PASS

## Overall Result

**PASS**

Critical: 0  
Major: 0  
Minor: 0
