# Affilix — Duration & Segment Management Contract v2

## Purpose

Define how Affilix maps creative video duration to the selected AI video provider's supported generation durations.

## Canonical Provider Durations

For the current Affilix video provider configuration, the supported generation durations are:

`4s`, `6s`, `8s`, and `10s`.

These are the only valid generation durations unless the active provider capability profile is explicitly changed.

## Core Principle

**Creative duration is the story. Provider duration is the technical clip size.**

Affilix must never silently change the requested final duration.

### Duration Layers

- **Requested duration**: explicit final duration requested by the user.
- **Creative duration**: duration of the complete narrative. Normally equals requested duration.
- **Generation duration**: duration of one provider generation request. Must be 4, 6, 8, or 10 seconds under the current provider profile.
- **Final duration**: duration after generated clips are assembled. Must equal requested duration.

## Valid Segment Combinations

Because all supported durations are even numbers, the current provider can exactly compose any even final duration of at least 4 seconds.

Examples:

```text
8s  → 8
10s → 10
12s → 6 + 6
14s → 6 + 8
16s → 8 + 8
18s → 8 + 10
20s → 10 + 10
22s → 10 + 6 + 6
24s → 8 + 8 + 8
```

Choose the combination that best matches natural storyboard beats, not merely the mathematically shortest combination.

## Unsupported Durations

If the requested final duration cannot be represented exactly using 4/6/8/10-second generations:

- do not silently round up or down
- do not silently change the campaign duration
- do not add filler
- mark the duration as infeasible
- request a revised final duration or an explicitly supplied provider capability

For example, 5s, 7s, 9s, and 11s cannot be assembled exactly from the current duration set.

## Storyboard Integration

Storyboard creative timing remains the source of truth.

When provider segmentation is required:

1. design the narrative beats first
2. identify natural segment boundaries
3. assign each generation segment one of 4/6/8/10 seconds
4. preserve the requested final duration exactly
5. preserve dialogue and product-action timing
6. preserve continuity across segment boundaries

A single creative scene may use multiple technical generation segments when necessary.

## Segment Selection Priority

When multiple combinations are mathematically valid:

1. preserve natural scene/story beats
2. avoid splitting a critical action
3. avoid splitting a sentence when possible
4. minimize unnecessary segment count
5. preserve visual continuity
6. use longer segments when the scene benefits from uninterrupted motion
7. use shorter segments when a clean beat or transition exists

## Provider Capability Profile

Represent the active provider as:

```yaml
provider:
  provider_id: CURRENT_VIDEO_PROVIDER
  model_id:
  supported_generation_durations: [4, 6, 8, 10]
  duration_policy: EXACT_SEGMENT_COMPOSITION
```

The values are provider capability data, not creative defaults. If the provider changes, update the capability profile before generating Video Prompts.

## Segment Record

Each technical segment tracks:

- segment_id
- source_scene_id
- final_start_time
- final_end_time
- creative_duration
- generation_duration
- provider_id
- model_id
- start_visual_state
- end_visual_state
- continuity_anchor
- assembly_order
- status

## Validation

Before video generation:

- requested duration is explicit
- requested duration is exactly representable
- every generation duration is 4, 6, 8, or 10 seconds
- segment durations sum exactly to requested duration
- boundaries are coherent
- dialogue fits creative timing
- product actions remain executable
- no filler or silent duration changes exist

## Revision

- Duration change → Storyboard and all timing-sensitive downstream assets become STALE.
- Provider capability change → re-evaluate Video Prompt segmentation.
- Video-only segment change → revise Video Prompt only unless creative timing changes.
- Never silently alter the requested duration because of provider limits.
