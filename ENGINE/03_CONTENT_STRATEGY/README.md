# Affilix — Content Strategy Engine

## Purpose

The Content Strategy Engine turns the normalized brief, selected creator, and verified product information into a clear UGC content strategy before scripting or visual prompt generation.

Its job is to decide what the content should communicate and demonstrate, not to write the final scene-by-scene script.

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

### Content Angle

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

Do not select an angle that requires unsupported claims.

### Core Message

Define one concise message that the viewer should remember after watching.

### Supporting Messages

List only the messages that materially support the primary message.

Avoid overcrowding short-form content with unnecessary talking points.

### Proof Strategy

Determine how the product claim or benefit can be demonstrated.

Possible proof types:

- Visual demonstration
- Product close-up
- Feature demonstration
- Usage sequence
- Before/after visual, when supported
- Creator-provided experience
- Official product information
- No proof available

When no valid proof exists, do not fabricate one.

### Emotional Strategy

Define the intended viewer response without manufacturing false urgency.

Possible states:

- Curiosity
- Recognition
- Relief
- Confidence
- Interest
- Delight
- Trust
- Desire to explore

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

The structure may be shortened or rearranged when the brief requires it.

### CTA Strategy

Define the desired action:

- Learn more
- View product
- Shop
- Visit product page
- Save
- Follow
- Comment
- Other explicit campaign action

Never invent discounts, urgency, scarcity, or promotional terms.

## Strategy Rules

### 1. Objective Before Creativity

Every creative choice must support the campaign objective.

### 2. Audience Relevance

Prioritize product information that matters to the target audience and their stated context.

### 3. Product Truth

Use only verified product facts and supported benefits.

### 4. Creator Fit

The strategy should fit the selected creator's approved persona, visual identity, communication style, and content capabilities.

### 5. Demonstrability

Prefer benefits that can be shown clearly in UGC when the campaign depends on product understanding.

### 6. Platform Fit

Adapt pacing, framing, information density, and CTA to the requested platform without inventing platform rules.

### 7. One Primary Message

Short-form content should have one dominant takeaway. Secondary points must support it rather than compete with it.

### 8. No Fake Experience

The strategy must not imply the creator personally used, tested, purchased, or endorsed a product unless that experience is explicitly provided.

### 9. No Unsupported Transformation

Do not create a before/after structure when the product data does not support a meaningful before/after comparison.

### 10. No Unsupported Superiority

Do not claim the product is the best, fastest, safest, cheapest, most comfortable, or superior to competitors unless supported by evidence.

## Angle Selection Logic

Evaluate candidate angles against:

1. Campaign objective
2. Audience need
3. Product evidence
4. Demonstration potential
5. Creator fit
6. Platform format
7. Claim risk
8. Production feasibility

The engine may identify multiple viable angles internally, but the final strategy should identify one primary angle unless the brief explicitly requests multiple concepts.

## Strategy Confidence

Record:

- High: objective, product facts, audience, and evidence are sufficiently defined.
- Medium: strategy is viable but one or more non-critical inputs are uncertain.
- Low: a missing critical input materially affects the strategy.

Low confidence should trigger clarification before downstream production when necessary.

## Handoff

The final strategy is passed to:

- 04_HOOK_ENGINE
- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
- 09_QUALITY_CONTROL
