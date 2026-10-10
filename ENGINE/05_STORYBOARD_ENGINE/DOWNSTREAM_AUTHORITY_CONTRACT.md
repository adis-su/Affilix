# Affilix — Storyboard Downstream Authority Contract

## Purpose

This contract defines the authority boundary between Stage 06 Storyboard and its downstream prompt stages.

The Storyboard is the canonical creative production blueprint. Visual Prompt, Video Prompt, and Voice Script are implementation layers that must execute the current Storyboard state without silently changing its meaning, action graph, reference state, or causal sequence.

## Authority Hierarchy

```text
STORYBOARD
    ↓
┌───────────────┬────────────────┬────────────────┐
↓               ↓                ↓
VISUAL PROMPT   VIDEO PROMPT    VOICE SCRIPT
```

The downstream stages may add implementation detail only when that detail preserves the Storyboard's declared semantics, state, timing, causality, continuity, and Content Format mechanism.

## Storyboard Owns

Storyboard is authoritative for:

- scene intent and sequence
- trigger and intention
- action graph
- action beats and narrative timing
- action priority
- product interaction and physical causality
- hand ownership and contact state
- gaze and expression intent
- camera behavior intent
- resulting states
- reference graph and reference versions
- transition contracts and invariants
- proof mechanism
- Content Format mechanism as staged through action
- dialogue anchors
- creative duration and narrative timing

Downstream stages MUST NOT reinterpret these as optional suggestions.

## Downstream Ownership

### Visual Prompt

Visual Prompt answers:

> What must this Storyboard state look like as one frozen frame?

It may elaborate:

- composition
- framing
- static camera perspective
- visible pose details
- lighting
- visual style
- supported environmental detail
- deterministic rendering of the referenced state

It MUST NOT:

- add a new action
- change product state without a Storyboard transition
- move the creator into an unapproved state
- change the reference graph
- encode temporal action
- replace the selected Content Format mechanism

### Video Prompt

Video Prompt answers:

> How does the current Storyboard transition happen over time within provider constraints?

It may elaborate:

- motion timing within Storyboard beat windows
- physical movement detail
- bounded natural micro-motion
- technical generation segmentation
- motivated camera response
- synchronization with the canonical Voice Script

It MUST NOT:

- invent an action absent from the Storyboard
- remove a story-critical action
- change trigger, intention, product job, or resulting state
- create an uncaused product state change
- change reference versions
- change creative duration
- substitute another Content Format mechanism

### Voice Script

Voice Script answers:

> What spoken language and delivery supports the current Storyboard action and dialogue anchors?

It may elaborate:

- wording
- phrasing
- pauses
- emphasis
- pronunciation
- delivery direction

It MUST NOT:

- invent an action the Storyboard does not stage
- claim proof the Storyboard does not demonstrate
- replace the Storyboard's dialogue anchor with an incompatible action
- change scene sequence or creative timing
- invent unsupported personal experience or product claims

## Allowed Elaboration Rule

Downstream implementation detail is valid only when:

```text
DOWNSTREAM DETAIL
      ↓
PRESERVES
      ↓
STORYBOARD SEMANTIC STATE
```

A downstream artifact may become more precise, but it may not become semantically different.

Example:

```text
Storyboard:
R02 → rotate serum → R03
```

Valid elaboration:

```text
R02
→ right-hand grip adjustment
→ controlled product rotation
→ gaze PRODUCT → CAMERA
→ motivated reframing
→ R03
```

Invalid elaboration:

```text
R02
→ open bottle
→ dispense serum
→ apply to face
→ R04
```

The second sequence is a new creative decision and therefore belongs in a Storyboard revision, not downstream prompt generation.

## Revision and Invalidation

If Storyboard changes any material field, affected downstream artifacts become STALE and must be regenerated or revalidated.

Material fields include:

- action graph
- action timing
- product state
- hand/contact state
- resulting state
- reference state/version
- transition contract
- proof mechanism
- Content Format mechanism
- dialogue anchor
- camera behavior when it changes the required state or transition
- creative duration

Downstream stages must never silently absorb a Storyboard revision while retaining a prior semantic state.

## Cross-Stage Lineage and Handoff Invariants

Every downstream artifact must identify the exact upstream artifact versions it consumed, including the canonical Stage 06 `storyboard_id`, `storyboard_version`, artifact ID/version, and pinned `source_commit_sha` where those fields are part of the runtime schema. Matching scene names, reference labels, or visually similar frames do not prove lineage.

- **Stage 07 Visual Prompt** validates the full Storyboard Reference Plan before generation and emits exactly one static prompt per unique canonical reference state. An immutable bridge referenced by two adjacent scenes remains one state and one prompt.
- **Stage 08 Voice Script** binds each dialogue line to a valid Storyboard scene, beat, and dialogue anchor; its timing must fit the anchor and scene windows. Stage 08 is a parallel descendant of Stage 06 and must not depend on Stage 07.
- **Stage 09 Video Prompt** consumes compatible current Stage 06 and Stage 07 artifacts, plus Stage 08 when dialogue is required. It verifies that Stage 07 and Stage 08 both identify the exact Storyboard artifact/version used by Stage 09. Its user-facing prompt count equals Storyboard scene count; technical generation segments do not change that count.
- **Stage 10 Production Output** assembles only current, validated artifacts from a compatible lineage. It verifies reference coverage, scene-to-prompt count, dialogue/scene timing, reference versions, immutable bridge identity, and exact duration composition before assembly.

A material Stage 06 revision invalidates affected Stage 07 prompts, Stage 08 dialogue/timing, Stage 09 motion prompts and transitions, and Stage 10 assembly. A Stage 07 revision invalidates Stage 09 and Stage 10. A Stage 08 revision invalidates Stage 09 dialogue synchronization and Stage 10. A Stage 09 revision invalidates Stage 10. Never silently mix artifacts from different Storyboard versions or pinned source snapshots.

## Validation Principle

The correct question for every downstream artifact is:

> Does this artifact faithfully implement the current Storyboard, or did it invent a new creative decision?

If it invented a new creative decision, the artifact fails downstream authority validation and the Storyboard must be revised instead.

## Final Rule

**Storyboard defines WHAT happens, WHY it happens, and WHICH STATE changes.**

**Visual Prompt defines HOW that state looks.**

**Video Prompt defines HOW that state changes through motion.**

**Voice Script defines HOW spoken content supports the action.**

No downstream stage may become a hidden Storyboard editor.
