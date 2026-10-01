# Affilix — Action Choreography Contract

## Canonical Principle

A scene is a process of action over time, not a single pose.

The canonical model is:

```
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

## Action Beat

An Action Beat is the smallest meaningful unit of visible action that materially advances the scene.

Each major beat should define:

- trigger
- intention
- action
- resulting state
- body motion
- hand motion
- product interaction when applicable
- gaze
- expression
- camera behavior
- bounded micro-motion
- reference after the beat when a meaningful visual state is reached

## Causality

Every major action should have a reason:

```yaml
trigger:
intention:
action:
resulting_state:
```

Affilix must avoid disconnected motion, unexplained product changes, or arbitrary camera movement.

## Human Micro-Motion

Use controlled micro-motion where visually appropriate:

- breathing
- weight shifting
- posture adjustment
- grip adjustment
- blinking
- small head movement
- restrained expression changes
- realistic clothing and hijab response

Never use unconstrained instructions such as "move naturally" as the only direction.

## Physical Interaction

When a product is manipulated:

```yaml
contact_hand:
grip_type:
contact_points: []
product_state_before:
product_state_after:
product_follows_hand: true | false
```

The product must not independently drift, morph, duplicate, or change state without an explicit physical action.

## Gaze Path

Gaze is an explicit motion channel.

Example:

```
PRODUCT → CAMERA
```

Gaze changes should have a reason within the action.

## Camera Behavior

Human-shot UGC may use controlled handheld behavior:

- subtle reframing
- minor natural drift
- product-following adjustment
- restrained perspective correction

Avoid random shake, excessive jitter, unexplained zoom, or abrupt movement.

## Reference State Rule

References represent meaningful visual states, not every micro-motion.

A reference chain may be:

```
R01 → R02 → R03 → R04
```

A scene may contain many references.

A reference is not a generation segment.

## Bridge Reference

At a scene boundary:

```
SCENE 01 END = R04
SCENE 02 START = R04
```

R04 is the single continuity source of truth.

Bridge references are immutable continuity anchors. A changed bridge requires a new version and invalidates dependent transitions.

## Validation

A valid action choreography must pass:

- action causality
- physical plausibility
- product interaction consistency
- gaze coherence
- bounded micro-motion
- camera motivation
- reference continuity
- bridge consistency
