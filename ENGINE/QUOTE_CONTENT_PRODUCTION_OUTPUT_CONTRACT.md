# Affilix Quote Content Production Output Contract

## Canonical Identity

- Canonical workflow stage: Stage 10 — Production Output
- Content mode: `QUOTE_CONTENT`
- Canonical registry: `ENGINE/WORKFLOW.md`

This is the Quote Content output assembly contract. It is deliberately separate from `ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md`. Never apply product claims, product proof scoring, product demo, or UGC-only fields to an editorial Quote Content run unless the user explicitly reclassifies the brief and starts a clean UGC run.

## Required Inputs

Current Stage 01 editorial brief, Stage 02 editorial context, Stage 04 strategy, and all applicable current artifacts from Stages 05–09. Explicitly skipped stages must carry their reason. Any required stage that is missing, stale, blocked, or unsupported blocks final assembly with `QUOTE_CONTENT_OUTPUT_DEPENDENCY_BLOCKED`.

For `QUOTE_IMAGE`: Stage 06, 08, and 09 must be `SKIPPED` with `STATIC_IMAGE_FORMAT`; Stage 07 is required. Stage 05 may be skipped only with `EDITORIAL_FORMAT_CONTRACT_PERMITS_SKIP`.

For video formats: Stage 06 and 07 are required; Stage 09 is required. Stage 08 is required only when the audio mode/brief requires spoken or external dialogue. Stage 03 Creator may be skipped when no on-screen/persona identity is needed. A skipped artifact is never treated as generated output.

## Assembly Rules

Production Output assembles current, validated source artifacts without changing their meaning. It must preserve the exact selected format, pillar, primary message, takeaway, text, scene order, reference graph, immutable bridge references, video prompt count, audio mode, exact requested duration, and publishing constraints.

Do not invent quote attribution, lived experience, author identity, platform-performance claims, statistics, testimonials, or guaranteed outcomes. Keep original authored copy separate from any explicitly supplied third-party quotation and record provenance. When rights/attribution are uncertain, do not imply authorship by a named person.

For video, the number of user-facing Video Prompts must equal Storyboard scene count exactly, and Stage 07 must provide exactly one image prompt per unique canonical Storyboard reference state (count the immutable bridge state once, even when used at both adjacent scene boundaries). Technical generation segments do not increase prompt count. For Quote Content video, validate the run-wide generation plan across all scene records: exactly two segments total, each exactly 10 seconds, with final timeline windows `[0, 10]` and `[10, 20]`, no gaps or overlaps, and a total of exactly 20 seconds. Every segment must resolve its source scene(s), start/target reference IDs and versions, and transition IDs to the same current Stage 06 storyboard artifact used by Stage 07 and Stage 08. Any mismatch or infeasible composition blocks output; do not infer compatibility from matching names or silently reuse stale assets.

## Output Shape

```yaml
stage: 10_PRODUCTION_OUTPUT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED
metadata:
  run_id:
  campaign_id:
  platform:
  publishing_objective:
  pillar_id:
  format_id:
  primary_message:
  takeaway:
  requested_duration:
  creative_duration:
  duration_feasibility: PASS | BLOCKED | NOT_APPLICABLE
  source_commit_sha:
publishing:
  caption:
  post_copy:
  cta:
  hashtags: []
  publishing_notes: []
editorial_asset:
  asset_type: QUOTE_IMAGE | VIDEO
  exact_on_screen_text: []
  image_prompt_ids: []
  video_prompt_ids: []
  scene_count:
  video_prompt_count:
  reference_graph: []
  generation_segments: []
audio:
  mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE | NOT_APPLICABLE
  voice_script_status: COMPLETED | SKIPPED
  dialogue_delivery: NATIVE_PROVIDER | EXTERNAL_PROVIDER | NONE | NOT_APPLICABLE
source_artifacts:
  stage_01:
  stage_02:
  stage_03:
  stage_04:
  stage_05:
  stage_06:
  stage_07:
  stage_08:
  stage_09:
validation:
  dependencies_current: PASS | BLOCKED
  message_and_format_preserved: PASS | BLOCKED
  provenance_and_attribution: PASS | BLOCKED
  safety_and_sensitivity: PASS | BLOCKED
  prompt_count: PASS | BLOCKED | NOT_APPLICABLE
  reference_coverage: PASS | BLOCKED | NOT_APPLICABLE
  storyboard_lineage: PASS | BLOCKED
  duration_integrity: PASS | BLOCKED | NOT_APPLICABLE
unresolved_requirements: []
provenance: []
```

## Blocking Conditions

Block output if any required artifact is missing, stale, contradictory, unsupported, or unsafe; if quote attribution/provenance cannot be represented honestly; if prompt count differs from scene count; or if exact duration composition is infeasible. Do not convert a blocker into a warning or silently substitute UGC output.

## Completion

After successful assembly and validation, mark Stage 10 `COMPLETED` and stop. There is no additional QC, approval, or final-package stage.
