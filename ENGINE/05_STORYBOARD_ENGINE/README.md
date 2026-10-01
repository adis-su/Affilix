# Affilix — Storyboard Engine

## Purpose

The Storyboard Engine converts the approved content strategy and hook into a scene-by-scene production plan.

The storyboard is the structural bridge between creative strategy and visual, video, and voice generation.

It must describe one coherent sequence, not a collection of unrelated shots.

## Input

- Normalized campaign brief
- Selected creator package
- Product identity
- Product facts and approved selling points
- Content strategy
- Approved hook
- Platform requirements
- Duration
- Aspect ratio
- Brand and campaign constraints

## Output

Return:

### Storyboard Metadata

- Storyboard ID
- Campaign ID
- Creator ID
- Product ID
- Platform
- Total duration
- Aspect ratio
- Scene count
- Primary content angle
- Primary message
- Approved hook

### Scene Record

Every scene should contain:

- Scene ID
- Timecode
- Duration
- Story purpose
- Narrative beat
- Location/environment
- Shot type
- Camera framing
- Camera angle
- Camera movement
- Creator action
- Body orientation
- Pose
- Hand gesture
- Facial expression
- Eye direction
- Product interaction
- Product visibility
- Outfit
- Hijab styling when applicable
- Lighting
- Background
- Dialogue/voice intent
- On-screen text
- Sound/action cue
- Transition
- Continuity requirements
- Required references
- Claim/evidence dependency

## Default UGC Story Structure

Use this structure as a starting point:

1. Hook
2. Relatable context
3. Product introduction
4. Product demonstration
5. Benefit / proof
6. Personal reaction
7. CTA

The structure may be compressed, expanded, or rearranged according to the campaign brief.

## Scene Design Rules

### 1. One Scene, One Primary Purpose

Each scene should have a clear job.

Avoid scenes that attempt to introduce the product, explain three benefits, show a demonstration, deliver the CTA, and somehow perform interpretive dance simultaneously.

### 2. Scene Continuity

Maintain continuity of:

- Creator identity
- Product identity
- Outfit
- Hijab styling
- Accessories
- Location
- Lighting
- Product state
- Hand position when relevant
- Spatial orientation
- Narrative time

A change is allowed when explicitly scripted or logically caused by the action.

### 3. Physical Plausibility

Actions must be physically executable.

Product interactions should account for:

- Hand placement
- Product orientation
- Object scale
- Body position
- Camera position
- Movement direction

### 4. Creator Identity

Every scene uses the selected creator identity unless the brief explicitly introduces another person.

Preserve canonical identity attributes across changes in:

- Pose
- Expression
- Outfit
- Hijab styling
- Camera angle
- Lighting

### 5. Product Identity

The product must remain visually consistent.

Do not change:

- Product shape
- Color
- Material appearance
- Branding
- Labels
- Key physical features
- Configuration

unless explicitly requested.

### 6. Product Visibility

The product should be visible enough for its narrative role.

Use:

- Wider shots for context
- Medium shots for interaction
- Close-ups for product details
- Detail shots for features that require visual proof

Do not hide the product behind unnecessary styling or props.

## Timing Rules

Duration should be allocated according to narrative importance.

Suggested short-form distribution:

- Hook: approximately 0–3 seconds
- Context: approximately 2–7 seconds
- Product introduction: approximately 5–10 seconds
- Demonstration/proof: approximately 8–20 seconds
- Reaction: approximately 15–25 seconds
- CTA: final approximately 2–5 seconds

These are planning ranges, not rigid platform requirements.

Total scene duration must match the requested video duration.

## Dialogue Rules

Storyboard dialogue should capture intent and essential wording.

Do not fabricate:

- Personal experience
- Reviews
- Results
- Guarantees
- Discounts
- Scarcity
- Promotional terms

unless supplied and approved.

Exact final dialogue can be finalized by the Voice Script Engine.

## Visual References

Each scene should identify the reference types it needs:

- Creator identity reference
- Product reference
- Outfit reference
- Pose reference
- Environment reference
- Style reference

Do not let an environment or style reference silently replace creator identity.

## Transition Logic

Transitions must be explainable.

Examples:

- Cut after completed gesture
- Camera push-in toward product
- Match movement from one shot to another
- Hand movement revealing product detail
- Change of framing during explanation

Avoid arbitrary transitions that break physical or narrative continuity.

## Storyboard Validation

Before handoff, check:

### Narrative

- Hook leads naturally into context.
- Product appears at a useful moment.
- Demonstration supports the selected angle.
- CTA follows the content logic.

### Identity

- Creator identity remains stable.
- Hijab identity remains stable when applicable.
- Outfit continuity is intentional.

### Product

- Product identity remains stable.
- Product interaction is plausible.
- Claims have evidence dependencies.

### Timing

- Scene durations add up to the requested duration.
- Dialogue can reasonably fit the scene duration.
- No scene is overloaded.

### Production

- Every required shot is visually executable.
- Camera instructions are clear.
- References are identifiable.
- Transitions are physically plausible.

## Handoff

The completed storyboard becomes the source structure for:

- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
- 09_QUALITY_CONTROL

The storyboard should be treated as the canonical scene sequence for downstream generation.


## Layered Niche Context Integration

Scene records now include Niche Context and Context Requirements. Sub-niche, use case, style, and audience context may shape setting, styling, interaction pattern, pacing, and scene purpose when authoritative. They must not invent product facts. Continuity validation must include context consistency across scenes.
