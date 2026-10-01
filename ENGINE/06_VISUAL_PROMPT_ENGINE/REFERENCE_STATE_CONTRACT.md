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
  wardrobe:
  hijab:
  product:
    position:
    orientation:
    state:
    interaction:
  camera:
    framing:
    angle:
    orientation:
  environment:
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

When rendering a reference, preserve continuity-critical attributes from its predecessor unless the Storyboard explicitly changes them.

Continuity-critical examples:

- creator identity
- wardrobe and hijab
- product geometry
- product position
- hand ownership
- camera orientation
- environment
- lighting
