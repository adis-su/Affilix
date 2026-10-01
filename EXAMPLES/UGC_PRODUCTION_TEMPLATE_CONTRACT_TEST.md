# UGC Production Output Template Contract Test

## Purpose

Verify that the standardized Production Output template preserves current Affilix contracts.

## Checks

### TPL-001 — Required Sections
Expected:
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
- Video Duration / Segment Records when applicable
- Action / Reference Traceability

Result: PASS

### TPL-002 — UNKNOWN Preservation
Missing material, size, branding, audience, offer, or other unsupported data remains UNKNOWN.

Result: PASS

### TPL-003 — Identity Lock
Creator and product identity cannot change during assembly.

Result: PASS

### TPL-004 — Context Integrity
Production Output contains exactly one current canonical niche context.

Result: PASS

### TPL-005 — Storyboard Traceability
Every downstream visual/video/voice asset references a storyboard scene where applicable.

Result: PASS

### TPL-006 — Action and Reference Integrity
Action beats, reference sequences, bridge references, transitions, and resulting states remain traceable.

Result: PASS

### TPL-007 — Duration Integrity
When video is required, generation segments use only 4, 6, 8, or 10 seconds and sum exactly to requested duration.

Result: PASS

### TPL-008 — Assembly Integrity
Production Output assembles current upstream state and cannot introduce unsupported claims or silently upgrade UNKNOWN values.

Result: PASS

## Overall Result

**PASS**
