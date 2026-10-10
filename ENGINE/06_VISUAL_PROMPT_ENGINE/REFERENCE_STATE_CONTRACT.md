# Affilix — Reference State Contract

## Purpose

The Visual Prompt Engine renders reference states produced by Storyboard.

A reference is a deterministic static visual state inside a scene.

## Reference Schema

```yaml
reference_id:
scene_id:
sequence_index:
role: START | INTERMEDIATE | END | BRIDGE
version:
status: CURRENT | STALE

state:
  creator:
    body_orientation:
    hand_positions:
    gaze:
    expression:
  wardrobe: INHERIT_LOCKED_CONFIGURATION | EXPLICIT_STATE_OVERRIDE | UNKNOWN
  hijab: INHERIT_LOCKED_CONFIGURATION | EXPLICIT_STATE_OVERRIDE | UNKNOWN
  product:
    position:
    orientation:
    state:
    interaction:
  camera:
    framing:
    angle:
    orientation:
  environment: INHERIT_LOCKED_CONFIGURATION | EXPLICIT_STATE_OVERRIDE | UNKNOWN
  lighting:

continuity_critical: []
```

## Bridge Rules

- The same reference ID and version must be used at both sides of a scene boundary.
- The bridge is the boundary source of truth.
- A bridge version cannot be silently modified after downstream use.
- A new bridge version invalidates transitions touching the old version.

## Prompt Rule

One reference produces one static image prompt.

The prompt describes the state, never the transition into or out of the state.

## Continuity

When rendering a reference, inherit the already-approved wardrobe and environment configuration instead of designing them again. Preserve continuity-critical attributes from the canonical configuration and predecessor unless the Storyboard or an explicit user instruction authorizes a specific change. If a required configuration is unavailable, mark it UNKNOWN and do not invent replacement details. An override must be explicit and limited to the affected attribute; it must not silently redesign unrelated visual attributes.

Continuity-critical examples:

- creator identity
- wardrobe and hijab
- product geometry
- product position
- hand ownership
- camera orientation
- environment
- lighting
