# Affilix — Storyboard Runtime Output Contract

## Stage Gate

Stage 06 executes only after current Stage 05 Hook is APPROVED.

## Output

```yaml
stage: 06_STORYBOARD
status: REVIEW
metadata:
  storyboard_id:
  campaign_id:
  creator_id:
  product_id:
  platform:
  requested_duration:
  creative_duration:
  generation_segmentation_plan: []
  aspect_ratio:
  scene_count:
  primary_content_angle:
  primary_message:
  approved_hook_id:
scenes: []
validation:
  narrative: PASS | REVIEW
  identity: PASS | REVIEW
  product: PASS | REVIEW
  timing: PASS | REVIEW
  production: PASS | REVIEW
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Timing Invariant

Creative scene durations must sum exactly to requested_duration. Provider generation durations are technical metadata and cannot change the approved creative duration.

## Rules

Storyboard is the canonical scene sequence for downstream Visual Prompt, Video Prompt, and Voice Script. Every scene has one primary purpose and physically executable actions. Creator and product identity remain locked.

No unsupported claims, personal experience, guarantees, discounts, scarcity, or promotional terms may be introduced.

The artifact enters REVIEW and waits for approval before downstream production specifications execute.

## Invalidation

Changes to Hook, Strategy, Creator, Context, Product, requested duration, aspect ratio, or other material campaign constraints mark the Storyboard and all dependent production artifacts as STALE.
