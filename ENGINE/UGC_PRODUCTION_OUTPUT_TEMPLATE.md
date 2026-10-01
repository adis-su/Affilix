# Affilix — UGC Production Output Template v3

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

The remaining production output follows the current campaign, creator, product, niche context, strategy, hook, storyboard, visual prompt, video prompt, and voice script state.

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
