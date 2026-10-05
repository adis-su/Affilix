# Affilix — Reference Transition Contract

## Purpose

Video Prompt converts reference states and action beats into controlled transitions.

## Transition Schema

```yaml
transition_id:
scene_id:
from_reference_id:
to_reference_id:

action_beats: []

action_causality:
  trigger:
  intention:
  physical_result:

primary_action:
secondary_motion: []

product_interaction:
gaze_path:
expression_behavior:
camera_behavior:

duration:
temporal_priority:
  critical_beats: []
  timing_guidance: []
continuity_requirements: []
negative_motion_constraints: []
```

## State Invariants

Every transition must define observable state invariants for its start and target references. Reference IDs are not sufficient on their own.

Minimum state variables:

- creator posture/body orientation
- acting hand and supporting hand ownership
- product position and orientation
- product open/closed state
- visible label orientation
- fingertip/product contact state
- gaze target
- facial expression
- camera framing/spatial relationship
- relevant environment and lighting continuity

A state variable must not change without a defined causal action. Target-state variables must not appear before the action that produces them.

## Temporal Priority

Temporal priority identifies the visually critical state changes inside a generation segment.

Use:

- `critical_beats`: beats that must visibly occur and must not be skipped, reversed, duplicated, or anticipated
- `timing_guidance`: bounded time ranges or relative pacing guidance when action density makes ordering alone insufficient

Temporal guidance must remain subordinate to the storyboard's canonical creative timing. It must not silently change the requested duration.

## State Transition Constraints

A valid transition must satisfy:

- every changed state variable has a physical cause
- intermediate states remain consistent with the preceding action
- target state is reached only after all required critical beats
- no state regression occurs after a completed transition
- no product state, hand ownership, gaze target, or camera relationship changes without an explicit cause
- start and target invariants remain compatible with the canonical reference graph

## Transition Invariant

Every transition must be physically and visually reachable:

```
START REFERENCE
+
CAUSAL ACTION
+
CONTROLLED MICRO-MOTION
+
PRODUCT / GAZE / CAMERA RESPONSE
=
TARGET REFERENCE
```

## Generation Segment Mapping

Generation segments are technical provider clips.

Each segment must identify:

- start reference
- target reference
- transition IDs covered
- exact provider duration

Provider durations remain exactly 4s, 6s, 8s, or 10s.

## Bridge Transition

When a scene starts from a bridge reference, the first transition must use the exact same bridge reference version that ended the previous scene.

## Provider Capability

Do not assume a provider supports both start-frame and end-frame conditioning.

Provider adapters must declare their actual capability. The semantic transition remains canonical even when a provider can only consume the start reference.

## Validation

Reject when:

- start or target reference is missing
- required state invariants are missing
- bridge versions differ
- action is not causally grounded
- action causality is incomplete
- critical beats are missing when the transition contains multiple visually material state changes
- temporal guidance is required by action density but absent
- target state is reachable only by skipping or anticipating a critical beat
- state regression is present
- product movement is physically impossible
- camera motion is unexplained
- micro-motion is unconstrained
- duration is not provider-compatible
