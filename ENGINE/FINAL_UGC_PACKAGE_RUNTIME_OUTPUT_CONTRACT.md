# Affilix — Final UGC Package Runtime Output Contract

## Purpose

Stage 10 is the final synthesis gate. It assembles only the current run's validated artifacts into the canonical Final UGC Package. It does not create or repair creative content.

## Gate

QC must exist and have `overall_status: PASS`. Any `BLOCKED`, `REVISION REQUIRED`, missing required artifact, or stale required artifact prevents production-ready status.

## Output

```yaml
stage: 10_FINAL_UGC_PACKAGE
status: PRODUCTION_READY | REVISION_REQUIRED | BLOCKED
package:
  package_id:
  version: v1.0
  campaign: {}
  creator: {}
  product: {}
  niche_context: {}
  strategy: {}
  hook: {}
  storyboard: {}
  visual_prompts: []
  video_prompts: []
  video_generation_segments: []
  voice_script: {}
  qc: {}
  traceability: []
delivery_readiness: READY | NOT_READY
source_commit_sha:
```

## Invariants

- Current run only.
- Canonical source-of-truth fields are preserved.
- UNKNOWN remains UNKNOWN.
- No unsupported claims are introduced.
- No conflict is silently resolved.
- Requested, creative, and final duration remain equal unless explicitly approved otherwise.
- Video generation segments remain technical implementation details and must sum to final duration.
- Scene IDs must remain synchronized across storyboard, visual, video, and voice assets.
- No stale required asset may enter the package.

## Status Mapping

| QC | Package | Delivery |
|---|---|---|
| PASS | PRODUCTION_READY | READY |
| REVISION REQUIRED | REVISION_REQUIRED | NOT_READY |
| BLOCKED | BLOCKED | NOT_READY |

## Traceability

Preserve the chain: Brief → Niche Context → Creator/Product → Strategy → Hook → Storyboard → Visual/Video/Voice → QC → Final Package.

## Handoff

This artifact is the final production contract. Downstream interfaces must consume the package rather than reconstructing it independently.
