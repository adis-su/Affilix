# Affilix — Brief Analyzer

## Canonical Stage Identity

- Canonical workflow stage: Stage 01 — Brief & Product
- Implementation path: `ENGINE/01_BRIEF_ANALYZER/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

The Brief Analyzer converts the selected mode's unstructured user brief and available references into a structured Stage 01 artifact that downstream Affilix engines can process.

For `UGC_AFFILIATE`, it remains the product and campaign normalization layer. For `QUOTE_CONTENT`, it normalizes an editorial brief without requiring a product. Mode selection and mode-specific required fields are defined by `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`.

## Input

When `content_mode` is `UGC_AFFILIATE` and the user provides a product link/reference, the analyzer must actively inspect and extract available product information from that reference before asking for additional product details. The link is an evidence source to investigate, not merely a field to acknowledge. When `content_mode` is `QUOTE_CONTENT`, do not require or invent a product reference.

The user may provide mode-specific information, including an editorial topic/theme and audience context for `QUOTE_CONTENT`, or product information and campaign requirements for `UGC_AFFILIATE`.

For `UGC_AFFILIATE`, the user may provide:

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

## Product Reference Research

This section applies only when `content_mode` is `UGC_AFFILIATE` or the user explicitly includes a product as part of the selected brief. For a supplied product URL or reference, Stage 01 should research the accessible source as deeply as reasonably possible and extract all materially useful product information available from it, including where present:

- exact product name and brand
- category and product type
- size/variant/flavor/shade
- stated ingredients/materials/components
- stated product benefits and supported selling points
- usage/how-to-use information
- packaging/product form
- official price or offer information when explicitly shown
- manufacturer/brand information
- warnings, restrictions, or usage notes
- source URLs or reference locations
- other factual product details relevant to downstream UGC production

Classify each finding as EXPLICIT, REFERENCE, SUPPORTED, INFERRED, or UNKNOWN. Preserve the source and distinguish sourced facts from marketing language. Never manufacture missing facts or convert an unsupported claim into a product fact.

If the reference is inaccessible, incomplete, blocked, or ambiguous, record the limitation and continue with whatever evidence is available rather than pretending that the link was fully inspected.

For `UGC_AFFILIATE`, Stage 01 output should present a useful product research summary after processing. For `QUOTE_CONTENT`, Stage 01 output should present the normalized editorial brief and its provenance. In both modes, render only fields owned by the active stage.

## Output

The analyzer must persist `content_mode` and normalize the brief according to the selected mode.

For `QUOTE_CONTENT`, normalize at minimum:

### Editorial Brief
- Platform: [DEFINE / UNKNOWN]
- Topic/theme or audience situation: [DEFINE / UNKNOWN]
- Audience context: [DEFINE / UNKNOWN]
- Publishing objective: [DEFINE / UNKNOWN]
- Format preference: [EXPLICIT FORMAT / AUTO]
- Editorial pillar preference: [EXPLICIT PILLAR / AUTO]
- Requested video duration: [18 / 28 / 30 seconds / NOT_APPLICABLE for static `QUOTE_IMAGE`]
- Audio/voice preference: [AUTO / TEXT_ONLY / VOICE_OVER / DIALOGUE]
- Intended emotional response: [DEFINE / UNKNOWN]
- Intended takeaway: [DEFINE / UNKNOWN]
- Additional user context or constraints: [DEFINE / NONE]
- Source/provenance for explicit and inferred fields

Do not collect or require a content quantity/batch-count field or a user-selected CTA field. CTA strategy is decided downstream only when it serves the publishing objective. For video formats, preserve the requested duration as a hard constraint and pass it to Voice Script so spoken wording can be budgeted and timing-validated. Do not require product identity, product facts, product claims, creator identity, or product proof in this branch unless the user explicitly requests product-centered content.

For `UGC_AFFILIATE`, normalize the existing product-centered brief:

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
- Niche: [DETECT / DEFINE / UNKNOWN]
- Product type: [DETECT / DEFINE / UNKNOWN]
- Niche classification confidence: High / Medium / Low / Unknown

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
2. Inspect supplied product references before declaring product information missing.
3. Extract and normalize materially useful product facts from accessible references.
4. Separate explicit requirements from inferred context.
3. Never turn an assumption into a fact.
4. Never invent product claims.
5. Never invent creator attributes.
6. Preserve exact user-provided constraints.
7. Resolve obvious duplicates without changing meaning.
8. Normalize terminology where possible.
9. Keep uncertain information explicitly marked as unknown.
10. Do not ask for information that downstream production does not actually need.
11. Do not ask the user to repeat product facts that can be reliably obtained from the supplied product reference.
12. Detect niche and product type when the product information supports a reliable classification.
13. Keep niche classification separate from product claims. A classification is not evidence for a product attribute.

## Editorial Brief Normalization

For `QUOTE_CONTENT`, normalize platform, editorial topic, audience context, publishing objective, format/pillar preference, requested duration, audio/voice preference, intended emotional response, takeaway, and optional context. Preserve explicit versus inferred provenance. For video formats, accept only 18, 28, or 30 seconds; for static `QUOTE_IMAGE`, set duration to `NOT_APPLICABLE`. Do not create input requirements for content quantity or CTA. Do not convert a broad audience label into unsupported demographic facts, and do not frame harmful or abusive relationship dynamics as ordinary communication problems. Missing non-critical details remain `UNKNOWN`.

## Niche Detection

For `UGC_AFFILIATE`, use this order:

1. Explicit category/product type in the user brief.
2. Approved Product Library category/type.
3. Supplied product reference or structured product metadata.
4. Clear terminology that reliably identifies the category.

Do not classify from visual aesthetics alone when the classification is materially uncertain.

Return:
- niche
- product type
- confidence
- evidence/source

If confidence is low or the product could reasonably belong to multiple materially different types, mark UNKNOWN and defer to the Niche Context Loader.

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
- Niche/product-type behavior that cannot be safely determined

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

- NICHE_CONTEXT_LOADER
- 02_CREATOR_SELECTOR
- 03_CONTENT_STRATEGY
- 04_HOOK_ENGINE
- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE

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
- Niche: Fashion
- Product type: Hijab
- Primary message: Comfort, but exact comfort claim requires product evidence
- CTA: Affiliate-oriented CTA, exact wording to be determined later
- Missing: Product identity/reference and any required factual support for comfort claim

The analyzer must not transform "fokus nyaman" into an unsupported guarantee such as "pasti nyaman seharian."
