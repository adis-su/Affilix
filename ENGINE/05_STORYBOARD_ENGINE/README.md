# Affilix — Storyboard Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 06 — Storyboard
- Implementation path: `ENGINE/05_STORYBOARD_ENGINE/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## UGC Naturalism Constraint

Storyboard must implement the cross-stage naturalism contract in `ENGINE/UGC_NATURALISM_CONTRACT.md`. Naturalism is expressed through motivated action, believable timing, bounded micro-motion, gaze, expression, product causality, and camera behavior. It must not be reduced to generic realism language.

For each major action beat, validate:
- trigger and intention are understandable
- body and hand motion are physically plausible
- product interaction has a causal result
- gaze and expression respond to the active action
- timing allows believable recognition, adjustment, and reaction when context supports them
- secondary micro-motion is bounded and does not invent new actions
- the resulting state matches the reference graph

If naturalism is materially weak, mark the storyboard `NEEDS_REFINEMENT`; if it requires impossible or unsupported behavior, mark it `BLOCKED`. A naturalism change makes affected downstream visual, video, voice, and production artifacts STALE as required.

## Content Format Continuity

Storyboard consumes the selected Content Format from Stage 04 and the selected Hook from Stage 05.

The storyboard MUST preserve the format's story mechanism across scenes. The format is not decorative metadata. It determines how the problem, product role, action sequence, proof, and CTA are staged when those elements are part of the registered format.

For every scene, validate:

- format-consistent action purpose
- format-consistent product role
- format-consistent proof mechanism
- format-consistent transition into the next beat

Do not silently convert one format into another during storyboard generation.

If Stage 04 format is revised, the storyboard becomes STALE and must be regenerated or revalidated.

## Format Mechanism Validation

Content Format must materially shape the storyboard, not merely appear in `metadata.primary_content_format`.

For the selected format, validate every scene against:

- **Story mechanism:** the scene advances the registered format rather than a generic UGC sequence.
- **Product role:** the product performs the role defined by the format.
- **Proof mechanism:** any required proof is staged through an observable, evidence-supported action.
- **Action purpose:** each major beat has a format-specific reason to exist.
- **Transition:** the resulting state naturally advances the same format mechanism into the next beat.
- **Hook continuity:** the first storyboard beat continues the selected Hook mechanism instead of replacing it with a generic product reveal.

### Format-specific storyboard tests

| Content Format | Storyboard must materially stage |
|---|---|
| BEAUTY_CRIME_SCENE | case/problem → inspection or intervention → observable result state |
| PRODUCT_HAS_A_JOB | concrete need → product performs its assigned job → resulting task state |
| BEAUTY_MYTH_LAB | test question → controlled action → observable test state |
| PRODUCT_INTERROGATION | product question → inspection/demonstration → evidence state |
| ONE_PRODUCT_THREE_PERSONALITIES | one product identity → distinct mode/context beats → preserved product continuity |
| SILENT_BEAUTY_TEST | visually legible action → observable state change without dependence on dialogue |
| BEAUTY_ROUTINE_UNDER_PRESSURE | situational pressure → constrained routine action → usable resulting state |
| ANTI_TUTORIAL | expectation/reframe → practical demonstration or qualification → grounded conclusion |
| LIFESTYLE_INTEGRATION | believable context → product naturally enters action → contextual resulting state |
| PROBLEM_SOLUTION_MISSION | concrete problem → mission-oriented action → resolved task state |

A storyboard that only copies the selected format into metadata while using generic scenes does not pass validation.

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
