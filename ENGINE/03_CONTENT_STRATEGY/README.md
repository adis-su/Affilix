# Affilix — Content Strategy Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 04 — Content Strategy
- Implementation path: `ENGINE/03_CONTENT_STRATEGY/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

The Content Strategy Engine turns the normalized brief, selected creator, verified product information, and loaded niche context into a clear UGC content strategy.

It decides what the content should communicate and demonstrate, not the final scene-by-scene script.\n\nIt also selects the **Content Format** that packages the content experience into a repeatable story mechanism. Content Format is distinct from Content Angle and becomes a downstream creative constraint. See `CONTENT_FORMAT_SYSTEM.md`.

## Input

- Normalized campaign brief
- Selected creator package
- Product identity
- Product features
- Supported benefits
- Selling points
- Available evidence
- Platform constraints
- Campaign requirements
- Loaded Niche Context

## Niche Context Use

When present, use:

- Niche
- Sub-Niche
- Product Type
- Use Case
- Style / Aesthetic
- Audience Context

Sub-niche and style context may shape angle framing, setting, pacing, styling, demonstration pattern, and visual language.

They must not invent product facts or claims.

Example:

`Fashion + Modest Fashion + Dress + Work + Minimalist`

may favor a simple workwear styling demonstration, but cannot invent fit, comfort, fabric, durability, or workplace requirements.

## Output

Return a structured strategy:

### Campaign Objective

- Primary objective
- Secondary objective
- Desired audience action

### Audience

- Target audience
- Audience context
- Core need/problem
- Relevant objection
- Awareness level when known

### Product Role

- Product function
- Most relevant verified feature
- Most relevant supported benefit
- Demonstration opportunity
- Evidence available

### Content Format\n\nSelect one eligible primary Content Format using product behavior, proof opportunity, creator fit, campaign objective, and platform fit. Do not select a format solely for novelty.\n\nRecord:\n\n- Content Format\n- Format Fit: eligible / conditional / ineligible\n- Format Rationale\n- Format Requirements\n- Product Behavior\n- Proof Opportunity\n\nThe registered formats and eligibility rules are defined in `CONTENT_FORMAT_SYSTEM.md`. Beauty-specific compatibility guidance is defined in `PRODUCT_LIBRARY/NICHES/02_BEAUTY/CONTENT_FORMAT_COMPATIBILITY.md`.\n\n### Content Angle

Choose one primary angle:

- Problem → Solution
- Demonstration
- Before → After, only when supported
- Try-on / Styling
- Review / Experience, only when experience is supplied
- How-to / Tutorial
- Comparison, only when factual comparison data exists
- Unboxing / First impression
- Lifestyle integration
- Objection handling
- Feature spotlight
- Other clearly defined angle

Sub-niche context may influence which angle is most natural, but product evidence and campaign requirements remain authoritative.

### Core Message

Define one concise message that the viewer should remember.

### Supporting Messages

List only messages that materially support the primary message.

### Proof Strategy

Determine how the product claim or benefit can be demonstrated.

When no valid proof exists, do not fabricate one.

### Emotional Strategy

Define the intended viewer response without manufacturing false urgency.

### Story Arc

Use a structure appropriate to the platform and objective.

Default UGC structure:

1. Hook
2. Relatable context
3. Product introduction
4. Demonstration
5. Benefit / proof
6. Personal reaction
7. CTA

### CTA Strategy

Define the desired action. Never invent discounts, urgency, scarcity, or promotional terms.

## Content Format Rules\n\n1. Product truth before format novelty.\n2. Reject formats whose required proof cannot be supplied.\n3. Conditional formats must record their explicit condition.\n4. A creative format is not evidence for a product claim.\n5. Once selected, Content Format constrains Hook, Storyboard, Visual Prompt, Video Prompt, and Voice Script.\n6. If no format is eligible, preserve the blocker rather than forcing a creative concept.\n\n## Strategy Rules

1. Objective Before Creativity.
2. Audience Relevance.
3. Product Truth.
4. Creator Fit.
5. Demonstrability.
6. Platform Fit.
7. One Primary Message.
8. No Fake Experience.
9. No Unsupported Transformation.
10. No Unsupported Superiority.
11. **Context Relevance:** use loaded sub-niche/use-case/style context when it is authoritative and compatible.
12. **Context Non-Invention:** never convert context labels into unsupported product claims.

## Strategy Confidence

Record:

- High: objective, product facts, audience, and context are sufficiently defined.
- Medium: strategy is viable but one or more non-critical inputs are uncertain.
- Low: a missing critical input materially affects strategy.

## Handoff

The final strategy passes Content Format and Content Angle downstream to:

- 04_HOOK_ENGINE
- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
