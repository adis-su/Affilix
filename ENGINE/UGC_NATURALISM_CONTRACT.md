# Affilix — UGC Naturalism Contract v1

## Purpose

UGC Naturalism is a cross-stage production constraint for making generated UGC behave like believable human-created content rather than merely photorealistic synthetic media.

Naturalism is not a separate workflow stage and not a generic negative-prompt block. Validation happens inside each affected stage.

## Core Principle

**Human-looking ≠ photorealistic.**

**Human-looking = physically plausible + behaviorally coherent + temporally imperfect + contextually motivated.**

A natural UGC scene should communicate that the creator is doing something for a reason, reacting to what is happening, and moving through a believable sequence of states.

## Canonical Model

```text
CAMPAIGN
  ↓
SCENE
  ↓
ACTION GRAPH
  ↓
ACTION BEATS
  ├─ Body Motion
  ├─ Hand Motion
  ├─ Product Interaction
  ├─ Gaze
  ├─ Expression
  └─ Camera Behavior
  ↓
REFERENCE STATES
  ↓
TRANSITIONS
  ↓
GENERATION SEGMENTS
  ↓
FINAL VIDEO
```

For temporal action, use:

```text
TRIGGER
  ↓
INTENTION
  ↓
MICRO-ACTION
  ↓
PRIMARY ACTION
  ↓
REACTION
  ↓
RESULTING STATE
```

## Naturalism Dimensions

Every applicable downstream artifact should preserve these dimensions:

1. **Physical plausibility** — bodies, hands, products, clothing, and camera obey believable physical relationships.
2. **Behavioral coherence** — movement has a reason tied to the scene, product, creator intention, or environment.
3. **Human timing** — actions are not machine-perfect; allow brief recognition, hesitation, adjustment, reaction, and return to a relaxed state when context supports them.
4. **Contextual motivation** — gaze, gesture, expression, and camera response are motivated by what the creator is doing.
5. **Interaction continuity** — product state, hand ownership, contact, grip, and resulting state remain consistent.
6. **Gaze realism** — gaze may move between product, mirror/environment, and camera when motivated; it is not permanently locked to lens.
7. **Expression restraint** — reactions are proportionate to the situation; avoid constant exaggerated smiling or frozen expressions.
8. **Camera realism** — handheld behavior is controlled and purposeful, not random shake or synthetic jitter.
9. **Micro-motion bounds** — breathing, blinking, weight shifts, posture/grip adjustments, small head movement, and realistic fabric/hijab response may be used as bounded support motion. They must not invent new actions.
10. **Voice naturalness** — spoken delivery may use conversational phrasing, pauses, breathing, emphasis, and imperfect rhythm without inventing experience or claims.

## Natural Human Timing

When context supports it, prefer an intentional sequence such as:

```text
notice → brief hesitation → reach → grip adjustment → lift → look → small reaction → present/use → return to relaxed state
```

This is a timing pattern, not a mandatory checklist. Do not add hesitation, reaction, or imperfection merely to make a scene look "human".

## Controlled Imperfection

Naturalism is **bounded**, not random.

Do:

- use small motivated adjustments
- preserve reference-state invariants
- vary timing only where the action permits it
- let gaze and camera behavior respond to the active interaction
- keep expression changes restrained

Do not:

- add random gestures
- add arbitrary head turns
- add random camera shake
- introduce unexplained pauses
- make the creator fidget continuously
- use "move naturally" as the sole motion instruction
- use generic "make it look human" language as a substitute for action design

## Product Causality

Product interaction must follow:

```text
TRIGGER → INTENTION → CONTACT → MANIPULATION → PRODUCT STATE CHANGE → RESULT
```

A product must not drift, teleport, duplicate, morph, change orientation without cause, or change state without a physical action.

## Reference-State Integrity

Naturalism must never override continuity.

A reference state is a frozen state, not a generation segment. Micro-motion may occur between references, but all generation must resolve to the defined target state.

Bridge references remain immutable. If a naturalism revision changes a bridge state, affected transitions and downstream artifacts become STALE.

## Stage Validation

### Stage 04 — Content Strategy
Naturalism should be compatible with the selected content format, creator behavior, proof mechanism, and physical action opportunity. Reject concepts that require artificial motion or unsupported behavior to communicate the strategy.

### Stage 05 — Hook
The hook should be executable as a believable human action or reaction. Attention must come from the situation, intention, or product interaction, not unexplained motion.

### Stage 06 — Storyboard
Action beats must include motivated body/hand motion, product interaction, gaze, expression, camera behavior, and bounded micro-motion where applicable. Validate trigger → intention → action → resulting state.

### Stage 07 — Visual Prompt
Each frozen state must show a plausible human posture, grip, gaze, expression, product relationship, clothing/hijab state, and environment. Do not encode motion into the static frame.

### Stage 09 — Video Prompt
Motion must be causal, temporally believable, physically plausible, reference-safe, and bounded. Secondary natural motion supports the primary action and must never compete with it.

### Stage 08 — Voice Script
Spoken delivery should sound conversational rather than brochure-like or mechanically paced. Naturalization must preserve exact factual meaning, supported claims, creator constraints, and campaign intent.

### Stage 10 — Production Output
Final assembly must preserve naturalism constraints and traceability from the current upstream artifacts. Production Output does not invent or "humanize" missing upstream work.

## Validation Outcomes

Naturalism validation is stage-local:

- `PASS` — naturalism constraints are materially satisfied.
- `NEEDS_REFINEMENT` — the artifact is usable but contains avoidable synthetic-looking behavior or weak human timing/motivation.
- `BLOCKED` — the requested natural behavior cannot be expressed without unsupported claims, impossible physical behavior, unavailable evidence, or contradictory constraints.

A stage must not silently downgrade a blocked naturalism condition to a generic prompt instruction.

## Example

Weak:

```text
Creator moves naturally, smiles, picks up the product, and presents it to camera.
```

Stronger:

```text
The creator notices the product beside the sink, keeps her attention on the mirror for a brief moment, reaches with her right hand, closes her fingers around the container, adjusts her grip once, glances at the label, then turns the product toward the camera. Her shoulders shift slightly forward as she brings it closer. After the brief presentation, she lowers the hand back toward a relaxed position instead of freezing in the presentation pose.
```

The stronger version defines motivation, causality, timing, gaze, grip, posture, and resulting state instead of outsourcing "human behavior" to the generator.

## Non-Goals

UGC Naturalism does not:

- guarantee that a provider will produce artifact-free video
- replace creator identity locks
- replace product identity locks
- replace Content Format constraints
- replace Action Choreography
- replace reference continuity
- justify unsupported product claims or invented creator experience
- create a new QC, approval, or workflow stage
