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

References represent meaningful visual states, not every micro-motion. A reference state is an ordered visual checkpoint tied to a meaningful Action Beat or critical transition.

A reference chain may be:

```
R01 → R02 → R03 → R04
```

A scene may contain many references. Reference density is determined by action complexity, not by scene count or provider segment count.

For high-complexity action scenes, Affilix should target six ordered reference states by default when six distinct states materially improve action control. Simpler scenes may use fewer references when additional states would be redundant. Affilix must never add references merely to reach a numeric quota.

A reference is not a generation segment. A reference state is a frozen visual state; the transition between references is the motion specification.

## Bridge Reference

At a scene boundary:

```
SCENE 01 END = R04
SCENE 02 START = R04
```

R04 is the single continuity source of truth.

Bridge references are immutable continuity anchors. A changed bridge requires a new version and invalidates dependent transitions.

## Production-Grade Beat Contract

For production use, an Action Beat must expose enough state and timing for downstream prompt engines to execute the same behavior without inventing missing motion.

### Required Beat Fields

```yaml
beat_id:
time_window:
trigger:
intention:
primary_action:
secondary_action:
supporting_motion:
micro_motion:
body_motion:
hand_motion:
product_interaction:
gaze:
expression:
camera_behavior:
resulting_state:
reference_after:
```

### Action Priority

Motion hierarchy is:

```text
PRIMARY ACTION
    ↓
SECONDARY RESPONSIVE ACTION
    ↓
SUPPORTING MOTION
    ↓
BOUNDED MICRO-MOTION
```

Lower-priority motion must not create a competing action or obscure the story mechanism.

### Timing Contract

When multiple actions occur sequentially, define approximate narrative windows. Timing windows describe action order and human timing; they are not provider generation segment boundaries.

A beat may overlap another channel in time, but the causal order must remain understandable. Allow small recognition, grip, adjustment, and reaction time when the context requires it.

### State Contract

For meaningful product interaction, preserve:

```yaml
hand_ownership:
  right: free | holding | manipulating
  left: free | holding | manipulating
contact_state:
  creator_to_product: none | approaching | touching | gripping | releasing
product_state:
  position:
  orientation:
  open_closed:
  surface_or_hand:
product_follows_hand: true | false
```

Any product state transition must be caused by a physical interaction. The storyboard must identify the hand responsible and the resulting product state.

### Transition Contract

Every meaningful reference transition should identify:

- transition/action name
- allowed changes
- invariants
- resulting reference

Example:

```text
R02 → R03
Transition: inspect → present

Allowed:
- product rotation
- arm position
- gaze PRODUCT → CAMERA
- motivated camera reframing

Invariant:
- creator identity
- wardrobe
- product geometry
- environment
- lighting
```

This contract prevents downstream stages from inventing state changes between references.

### Proof and Content Format

Action choreography must visibly execute the selected Content Format. Metadata alone is insufficient.

The canonical proof chain is:

```text
FORMAT MECHANISM
      ↓
ACTION
      ↓
OBSERVABLE PROOF / TASK STATE
```

For PRODUCT_HAS_A_JOB, the action must make the product perform a legitimate job in context. Merely picking up and presenting the product is not sufficient unless presentation itself is the defined job and supported by the selected format.

### Dialogue Anchors

Storyboard does not replace Voice Script. When spoken audio is required, a beat may expose:

```yaml
dialogue_anchor:
  semantic_intent:
  action_window:
  target_reference:
```

The anchor tells Voice Script where spoken meaning belongs without requiring narration of every physical movement.

### Camera State

Camera behavior must have a defined state and motivation when it materially affects continuity:

- framing
- perspective/height when relevant
- creator-to-camera relationship
- product framing
- motivated reframing or tracking response

Random shake, decorative zoom, and unexplained camera movement are invalid naturalism shortcuts.

### Validation Outcomes

```text
PASS
NEEDS_REFINEMENT
BLOCKED
```

Use NEEDS_REFINEMENT when action is feasible but timing, motivation, state detail, proof, or continuity is materially underspecified. Use BLOCKED when behavior is impossible, unsupported, incompatible with the selected format, or cannot preserve required reference continuity or exact duration.

## UGC Naturalism

Action Choreography is the primary temporal implementation layer for `ENGINE/UGC_NATURALISM_CONTRACT.md`. Naturalism is bounded and motivated, not random imperfection.

Use trigger → intention → micro-action → primary action → reaction → resulting state where context supports it. Never rely on `move naturally` or `make it look human` as the sole direction.

Naturalism validation must inspect physical plausibility, behavioral motivation, human timing, gaze realism, expression restraint, camera realism, bounded micro-motion, product causality, and reference-state integrity.

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
