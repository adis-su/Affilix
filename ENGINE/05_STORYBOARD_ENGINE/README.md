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

## Production Blueprint Contract

Storyboard output is the canonical production blueprint between Hook and downstream prompt stages. It must expose enough structure for Visual Prompt, Video Prompt, and Voice Script to execute the same action graph without inventing missing behavior.

Every scene MUST define:

- **scene timing:** scene duration plus beat-level timing windows where action order matters
- **trigger:** the event or observation that starts the action
- **intention:** what the creator is trying to accomplish
- **action graph:** ordered body, hand, product, gaze, expression, and camera channels
- **action priority:** primary action, secondary action, supporting motion, and micro-motion
- **product state:** position, orientation, open/closed state when applicable, and contact state
- **hand ownership:** which hand owns/manipulates the product at each meaningful state
- **contact state:** what physically touches what before, during, and after manipulation
- **resulting state:** the observable state produced by the action
- **transition contract:** allowed state changes and invariants that must persist
- **dialogue anchor:** the semantic moment an utterance belongs to, when spoken audio is required
- **proof mechanism:** the observable evidence the scene can legitimately establish
- **camera state:** framing, perspective, and motivated camera response
- **continuity invariants:** creator, wardrobe, product identity/geometry, environment, lighting, and other immutable properties
- **naturalism validation:** timing, causality, gaze, expression, micro-motion, and contextual motivation

### Action Graph

Use this canonical graph for each major beat:

```text
TRIGGER
  ↓
INTENTION
  ↓
BODY ACTION
  ↓
HAND ACTION
  ↓
PRODUCT INTERACTION
  ↓
GAZE / EXPRESSION RESPONSE
  ↓
CAMERA RESPONSE
  ↓
RESULTING STATE
```

Channels may overlap in time, but their causal relationship must remain explicit. Do not collapse the graph into a generic instruction such as "act naturally".

### Beat Timing

When a beat contains sequential actions, expose approximate timing windows:

```text
0.0–0.4s  → gaze shift
0.4–1.2s  → reach
1.2–1.6s  → grip/contact
1.6–2.3s  → lift
2.3–2.5s  → grip adjustment
```

Timing is narrative timing, not a provider segment boundary. It must preserve the requested campaign duration exactly.

### Action Priority

Every major scene must distinguish:

1. **Primary action** — the action that carries the story mechanism.
2. **Secondary action** — a directly responsive motion such as gaze following the product.
3. **Supporting motion** — posture, weight shift, or camera response that supports the action.
4. **Micro-motion** — bounded breathing, blinking, grip adjustment, or fabric response.

Lower-priority motion must never obscure, contradict, or invent the primary action.

### Product, Hand, and Contact State

For every meaningful product manipulation, preserve:

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

A product state change requires a corresponding physical action. Product position cannot change independently.

### Transition Contract

Each reference transition MUST declare:

- transition name or action
- allowed changes
- invariants
- resulting reference

Example:

```text
R02 → R03
Transition: inspect → present

Allowed changes:
- product rotation
- right-arm position
- gaze: PRODUCT → CAMERA
- camera framing

Invariants:
- creator identity
- wardrobe
- product geometry
- lighting
- environment

Result:
R03
```

This prevents downstream stages from silently inventing state changes.

### Proof and Format Mechanism

A scene is not valid merely because it contains the selected Content Format in metadata.

The storyboard must show:

```text
FORMAT MECHANISM
      ↓
ACTION
      ↓
OBSERVABLE PROOF / TASK STATE
```

For PRODUCT_HAS_A_JOB, for example:

```text
CONCRETE NEED
      ↓
PRODUCT PERFORMS ASSIGNED JOB
      ↓
RESULTING TASK STATE
```

A product reveal without a product job does not satisfy PRODUCT_HAS_A_JOB.

### Dialogue Anchors

Storyboard does not author the final Voice Script. It defines where spoken meaning belongs:

```yaml
dialogue_anchor:
  semantic_intent:
  action_window:
  target_reference:
```

Voice Script must bind spoken content to these anchors without narrating every physical movement.

### Camera State

Each meaningful reference should define camera state sufficiently for downstream prompts:

- framing
- camera height/perspective when relevant
- creator-to-camera relationship
- product framing when relevant
- motivated reframing or tracking response

Camera motion must respond to the action graph, not exist as decorative movement.

### Storyboard Validation Outcomes

```text
PASS
NEEDS_REFINEMENT
BLOCKED
```

**NEEDS_REFINEMENT** applies when the action is possible but timing, motivation, proof, state detail, or continuity is materially underspecified.

**BLOCKED** applies when the requested behavior is physically impossible, unsupported by available evidence, incompatible with the selected format, impossible to reconcile with reference continuity, or cannot satisfy exact duration requirements.

A storyboard must not be promoted to downstream prompt generation while material fields are missing or contradictory.

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
