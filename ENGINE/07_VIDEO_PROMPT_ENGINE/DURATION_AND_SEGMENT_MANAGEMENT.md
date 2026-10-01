# Affilix — Duration & Segment Management Contract v1

## Purpose

Define how Affilix preserves a user's requested final video duration while adapting generation requests to the discrete duration capabilities of a selected video provider.

This is a production capability layer, not a creative replacement for the storyboard.

## Core Principle

**User duration is a campaign requirement. Provider duration is a generation constraint.**

Affilix must never silently change the requested final duration because a provider cannot generate that duration in one request.

## Duration Layers

### Requested Duration

The explicit final video duration supplied by the user or campaign.

Example:

`requested_duration = 18s`

### Creative Duration

The duration of the approved narrative sequence.

Unless explicitly changed and approved, it must equal the requested duration.

### Generation Duration

The technical duration of an individual video-generation request.

It must be selected from the active provider's supported durations.

### Final Duration

The duration after generated segments are assembled.

It must equal the approved requested duration.

## Provider Capability Profile

Provider capabilities must be represented separately from creative logic.

Example:

```yaml
provider:
  id: PROVIDER_A
  supported_durations: [4, 6, 8, 10]
```

Do not treat [4, 6, 8, 10] as a universal provider standard. Capabilities belong to the selected provider/model and may change.

Minimum required capability data:

- provider_id
- model_id when relevant
- supported_durations
- duration_limit_status
- capability_source
- capability_version or last_verified value when available

Unknown provider capabilities remain UNKNOWN.

## Segmentation Rules

If one generation cannot cover the required creative duration:

1. Preserve the approved final duration.
2. Identify natural creative beat boundaries.
3. Divide the storyboard into scenes or generation segments.
4. Assign each segment a provider-supported generation duration.
5. Ensure the sum of generation segment durations equals the approved final duration.
6. Preserve visual and narrative continuity between segments.
7. Record the mapping between creative scenes and technical segments.

Example:

```text
Requested final duration: 18s
Provider durations: 4s, 6s, 8s, 10s

Valid plan:
4s + 6s + 8s = 18s
```

Another valid plan:

```text
8s + 10s = 18s
```

The second plan is valid only when the storyboard contains two coherent beats that can support those segment boundaries.

## Duration Fitting

When a creative beat does not map exactly to provider durations:

- Prefer restructuring the beat at a natural narrative boundary.
- Redistribute time across adjacent scenes when this preserves the approved story.
- Preserve important dialogue timing.
- Preserve important product actions.
- Do not add meaningless filler.
- Do not silently remove meaningful actions.
- Do not silently shorten the final video.
- Do not silently lengthen the final video.

If no provider-compatible plan can preserve the approved creative sequence, the production state must indicate a duration feasibility issue and route the smallest affected stage for revision.

## Segment Record

Each technical segment should track:

- segment_id
- source_scene_id
- final_start_time
- final_end_time
- creative_duration
- generation_duration
- provider_id
- model_id when relevant
- start_visual_state
- end_visual_state
- continuity_anchor
- assembly_order
- status

## Continuity Requirements

Across segments preserve when applicable:

- Creator identity
- Face identity
- Body proportions
- Outfit
- Hijab styling
- Product identity
- Product state
- Environment
- Lighting
- Spatial direction
- Camera logic
- Narrative time

A segment boundary should ideally occur after a completed gesture, completed product interaction, or stable visual state.

## Voice and Audio Interaction

Voice Script timing is based on the creative/storyboard timeline, not on arbitrary provider segment boundaries.

A spoken line may span multiple technical video segments when the final assembled timing requires it.

Video Prompt controls visual synchronization. Voice Script controls wording and delivery.

## Revision and Stale-State Behavior

- Requested duration change → Storyboard and all dependent timing-sensitive assets become STALE.
- Storyboard timing change → affected Visual, Video, Voice, and QC outputs become STALE as applicable.
- Provider capability change → re-evaluate Video Prompt segmentation and dependent production/QC outputs; do not automatically change the approved storyboard duration.
- Video-only segment plan change → revise Video Prompt and revalidate assembly/QC; Voice Script does not become STALE unless creative timing changes.
- Voice-only change → visual assets do not become STALE.

## Validation

Before video generation, verify:

- requested duration is explicit
- creative duration equals approved requested duration
- provider capabilities are known when generation is required
- every generation duration is provider-supported
- segment durations sum to the final duration
- segment boundaries are coherent
- continuity anchors are defined
- no filler or silent duration changes were introduced

Before final packaging, verify:

- assembled final duration equals approved requested duration
- all required segments exist
- segment order is correct
- no segment is STALE
- QC passes timing and continuity validation
