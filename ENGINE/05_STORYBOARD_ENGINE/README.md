# Affilix — Storyboard Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 06 — Storyboard
- Implementation path: `ENGINE/05_STORYBOARD_ENGINE/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Provider-Aware Duration Planning

The storyboard owns creative duration, while the current video provider accepts generation clips of exactly 4s, 6s, 8s, or 10s.

Plan the narrative first, then map it to those technical clip sizes.

Rules:

- requested final duration must be preserved exactly
- generation segments may span one or multiple storyboard beats
- segment durations must be 4, 6, 8, or 10 seconds
- segment boundaries should follow natural creative beats
- never add filler solely to reach a provider duration
- never silently shorten or lengthen the campaign
- if exact composition is impossible, flag duration feasibility as BLOCKED

Examples:

```text
14s → 6s + 8s
18s → 8s + 10s
20s → 10s + 10s
```

A creative scene may contain multiple generation segments. The technical segment plan belongs to Video Prompt; the storyboard remains responsible for narrative timing.


## Action Choreography Architecture

A scene is a process of action over time, not a single pose. The canonical structure is:

```text
SCENE
  ↓
ACTION GRAPH
  ↓
ACTION BEATS
  ↓
REFERENCE STATES
  ↓
TRANSITIONS
  ↓
GENERATION SEGMENTS
```

Major action beats should capture trigger, intention, action, resulting state, body/hand motion, product interaction, gaze, expression, camera behavior, and bounded human micro-motion. See `ACTION_CHOREOGRAPHY_CONTRACT.md` for the canonical contract.

### Reference Graph

A scene may contain multiple visual states:

```text
SCENE 01
R01 → R02 → R03 → R04 [BRIDGE]
                         ↓
SCENE 02
                    R04 → R05 → R06
```

A bridge reference is the shared, immutable boundary state. Reference states and provider generation segments are separate concepts.
