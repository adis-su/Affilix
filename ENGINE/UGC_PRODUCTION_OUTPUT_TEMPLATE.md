# Affilix — UGC Production Output Template v4

## Content Format Traceability

Production Output must preserve the selected Content Format from Stage 04 as traceable metadata. Production Output assembles upstream artifacts and must not reinterpret or silently replace the selected format.

```yaml
content_format:
  format_id:
  format_name:
  format_fit: eligible | conditional
  format_requirements: []
  selection_status: SELECTED
content_format_propagation:
  hook: PRESERVED | NEEDS_REVALIDATION
  storyboard: PRESERVED | NEEDS_REVALIDATION
  visual_prompt: PRESERVED | NEEDS_REVALIDATION
  video_prompt: PRESERVED | NEEDS_REVALIDATION
  voice_script: PRESERVED | NEEDS_REVALIDATION | NOT_REQUIRED
```

Production Output is valid only when the selected Content Format is current and all required downstream artifacts preserve it. A format mismatch or stale dependent artifact blocks final assembly.

## UGC Naturalism Traceability

Production Output must preserve the naturalism state of required upstream artifacts. Naturalism is a cross-stage constraint, not a separate QC stage.

```yaml
ugc_naturalism:
  contract: ENGINE/UGC_NATURALISM_CONTRACT.md
  storyboard: PASS | NEEDS_REFINEMENT | BLOCKED
  visual_prompt: PASS | NEEDS_REFINEMENT | BLOCKED
  video_prompt: PASS | NEEDS_REFINEMENT | BLOCKED | NOT_REQUIRED
  voice_script: PASS | NEEDS_REFINEMENT | BLOCKED | NOT_REQUIRED
  propagation: PRESERVED | NEEDS_REVALIDATION
```

Final assembly must not silently "humanize" an upstream artifact. If required naturalism state is `BLOCKED` or `NEEDS_REVALIDATION`, Production Output remains blocked until the affected upstream artifact is corrected and revalidated.

## Video Duration

- requested_duration:
- creative_duration:
- duration_feasibility: PASS | BLOCKED
- provider_id:
- supported_generation_durations: [4, 6, 8, 10]
- generation_segments:

Every generation segment must use 4, 6, 8, or 10 seconds. The assembled final duration must equal requested_duration exactly.

## Video Segment Record

For each video segment:

- segment_id:
- source_scene_id:
- final_start_time:
- final_end_time:
- generation_duration:
- start_visual_state:
- primary_action:
- secondary_motion:
- camera_behavior:
- end_visual_state:
- continuity_anchor:

## Prompt Formatting

Image prompts and video prompts are user-facing generation artifacts and must each be delivered in a single standalone Markdown code block. Metadata remains outside the code block.

The remaining production output follows the current campaign, creator, product, niche context, strategy, selected Content Format, hook, storyboard, visual prompt, voice script, and video prompt state.

## Action and Reference Traceability

Final Production Output must retain the canonical action choreography and reference graph. Do not collapse a multi-reference scene into one generic scene description.

```yaml
scene_id:
action_beats: []
reference_sequence: []
bridge_reference_id:
transitions: []
```

The production output is an assembly of current upstream state, not a reinterpretation layer.
