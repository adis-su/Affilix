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

primary_action:
secondary_motion: []

product_interaction:
gaze_path:
expression_behavior:
camera_behavior:

duration:
continuity_requirements: []
negative_motion_constraints: []
```

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
- bridge versions differ
- action is not causally grounded
- product movement is physically impossible
- camera motion is unexplained
- micro-motion is unconstrained
- duration is not provider-compatible
