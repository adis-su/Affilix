# Affilix — Hook Engine

## Purpose

The Hook Engine generates opening concepts that capture attention while remaining faithful to the approved content strategy, creator identity, product facts, and campaign constraints.

A hook is the entry point to the story. It must create a reason to continue watching without relying on unsupported claims, fake urgency, or misleading framing.

## Input

- Content strategy from 03_CONTENT_STRATEGY
- Normalized campaign brief
- Selected creator
- Product identity
- Verified product facts
- Supported benefits
- Available evidence
- Platform requirements
- Campaign constraints

## Output

Each hook candidate should contain:

- Hook ID
- Hook type
- Hook text or visual concept
- Delivery mode: Spoken / On-screen text / Visual / Hybrid
- Audience trigger
- Product connection
- Strategy connection
- Required visual action
- Required proof
- Claim risk: Low / Medium / High
- Status: Draft / Approved / Rejected

## Hook Types

### Problem Hook

Starts from a recognizable audience problem.

Use only when the problem is relevant to the target audience and product.

### Curiosity Hook

Creates an information gap that the content can actually resolve.

Do not create fake mystery or promise information that the video does not provide.

### Relatable Hook

Uses a familiar situation, behavior, or frustration.

The situation must be plausible for the target audience.

### Demonstration Hook

Opens with the product being used or a feature being demonstrated.

Useful when the product benefit is visually demonstrable.

### Product Hook

Introduces the product immediately.

Useful when product recognition is more important than narrative setup.

### Pattern Interrupt

Uses an unexpected but relevant visual, movement, framing, or statement.

The interruption must remain connected to the product or story.

### Question Hook

Opens with a question the audience is likely to care about.

The content must answer or meaningfully address the question.

### Story Hook

Starts in the middle of a relatable situation, action, or mini-story.

### Objection Hook

Addresses a known audience concern before presenting the product solution.

The objection must be grounded in the brief or known audience context.

## Hook Construction

A hook can be constructed from:

Audience Trigger + Context + Product Relevance + Open Loop

Not every hook requires all four components.

## Hook Selection Logic

Evaluate candidates against:

1. Alignment with campaign objective
2. Audience relevance
3. Content-angle alignment
4. Product relevance
5. Evidence availability
6. Creator fit
7. Platform suitability
8. Clarity
9. Claim safety
10. Ease of visual execution

Do not rank hooks as objectively best or worst.

Instead, return viable candidates with factual rationale describing what each candidate emphasizes.

## Hook Truth Rules

Never use unsupported:

- Superlatives
- Guaranteed outcomes
- Exact performance numbers
- Medical outcomes
- Fabricated testimonials
- Fake scarcity
- Fake discounts
- Fake urgency
- False comparisons
- False personal experience

Avoid clickbait that creates an expectation the rest of the content cannot fulfill.

## Creator Fit

Hooks must sound and look compatible with the selected creator.

Respect:

- Creator persona
- Speaking style
- Visual identity
- Hijab identity when applicable
- Approved expression range
- Approved pose range

Do not invent signature phrases or personal experiences.

## Visual Hook

When the hook is visual, specify:

- Initial frame
- Creator action
- Product visibility
- Camera framing
- Viewer-facing action
- Transition into the next beat

The hook must be physically and visually executable.

## Hook Variants

For a normal concept, generate a small set of meaningfully different candidates rather than many superficial rewrites.

Suggested default:

- 3 to 5 hook candidates
- At least 2 different hook types when the brief allows it

## Handoff

The approved hook becomes the opening beat for:

- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE

## Example

Strategy:

- Audience: viewers looking for a modest fashion product
- Objective: product discovery
- Angle: demonstration
- Verified product fact: product has a specified construction detail
- Evidence: product reference

Possible hook:

"Kalau kamu sering memperhatikan bagian ini saat pilih hijab, lihat yang ini."

This creates curiosity while leaving the actual product feature to the demonstration.

Avoid:

"Ini hijab paling nyaman yang pernah ada."

unless such a claim is explicitly supported.
