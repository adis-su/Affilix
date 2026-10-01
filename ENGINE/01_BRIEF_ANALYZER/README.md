# Affilix — Brief Analyzer

## Purpose

The Brief Analyzer converts an unstructured user brief into a structured production brief that downstream Affilix engines can process.

It is the first normalization layer between human input and the UGC production pipeline.

## Input

The user may provide:

- Product information
- Creator requirements
- Campaign objective
- Target audience
- Platform
- Content format
- Key message
- Required talking points
- Offer information
- CTA
- Visual references
- Script requirements
- Duration
- Aspect ratio
- Brand requirements
- Restrictions
- Example content
- Any other campaign context

Input may be incomplete, informal, mixed-language, or poorly structured.

## Output

The analyzer should normalize the brief into:

### Campaign

- Campaign ID: [GENERATE OR DEFINE]
- Campaign objective: [DEFINE]
- Platform: [DEFINE]
- Content format: [DEFINE]
- Duration: [DEFINE]
- Aspect ratio: [DEFINE]

### Product

- Product ID: [DEFINE]
- Product name: [DEFINE]
- Brand: [DEFINE]
- Category: [DEFINE]
- Product information status: Complete / Partial / Missing

### Audience

- Target audience: [DEFINE]
- Audience problem/need: [DEFINE]
- Audience context: [DEFINE]

### Messaging

- Primary message: [DEFINE]
- Secondary messages: [DEFINE]
- Required talking points: [DEFINE]
- CTA: [DEFINE]

### Creator

- Creator ID: [DEFINE]
- Creator requirements: [DEFINE]
- Creator reference: [DEFINE]

### Creative Direction

- Content angle: [DEFINE]
- Desired tone: [DEFINE]
- Visual direction: [DEFINE]
- Story direction: [DEFINE]

### Constraints

- Mandatory requirements: [DEFINE]
- Prohibited elements: [DEFINE]
- Brand restrictions: [DEFINE]
- Claim restrictions: [DEFINE]
- Platform restrictions: [DEFINE]

### References

- Product references: [DEFINE]
- Creator references: [DEFINE]
- Style references: [DEFINE]
- Example content: [DEFINE]

### Missing Information

List only information that is genuinely required for the next production stage.

## Normalization Rules

1. Preserve user intent.
2. Separate explicit requirements from inferred context.
3. Never turn an assumption into a fact.
4. Never invent product claims.
5. Never invent creator attributes.
6. Preserve exact user-provided constraints.
7. Resolve obvious duplicates without changing meaning.
8. Normalize terminology where possible.
9. Keep uncertain information explicitly marked as unknown.
10. Do not ask for information that downstream production does not actually need.

## Requirement Classification

Every important input should be classified as:

- EXPLICIT: directly stated by the user.
- REFERENCE: supplied through an approved reference.
- SUPPORTED: supported by known product/creator data.
- INFERRED: reasonable interpretation that has not been confirmed.
- UNKNOWN: information not available.

Only EXPLICIT, REFERENCE, and SUPPORTED information should be treated as authoritative production constraints.

INFERRED information may guide reasoning but must not silently become a hard requirement.

## Missing Information Policy

Use the minimum-question principle.

Ask for clarification only when missing information would materially affect:

- Product identity
- Creator identity
- Core campaign objective
- Required deliverable
- Safety/compliance
- A mandatory brand constraint
- A required factual claim

Otherwise continue with the available information and mark the uncertainty.

## Conflict Resolution

When instructions conflict, prioritize:

1. Latest explicit user instruction
2. Explicit campaign requirements
3. Approved canonical product data
4. Approved canonical creator data
5. Platform requirements
6. Creative interpretation

Do not silently override an explicit user instruction.

## Handoff

The normalized brief becomes the input for:

- 02_CREATOR_SELECTOR
- 03_CONTENT_STRATEGY
- 04_HOOK_ENGINE
- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
- 09_QUALITY_CONTROL

## Example

Raw input:

"bikin video affiliate 30 detik buat hijab ini, cewek muda, style clean, fokus nyaman dipakai, upload TikTok."

Normalized interpretation:

- Platform: TikTok
- Duration: 30 seconds
- Format: Affiliate UGC video
- Creator requirement: Young female creator
- Style: Clean
- Product: Hijab, identity details still require product data/reference
- Primary message: Comfort, but exact comfort claim requires product evidence
- CTA: Affiliate-oriented CTA, exact wording to be determined later
- Missing: Product identity/reference and any required factual support for comfort claim

The analyzer must not transform "fokus nyaman" into an unsupported guarantee such as "pasti nyaman seharian."
