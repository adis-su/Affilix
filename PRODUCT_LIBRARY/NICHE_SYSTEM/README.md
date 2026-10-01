# Affilix Niche System

## Purpose
The Niche System lets Affilix support multiple UGC affiliate product categories without creating a separate engine for every niche. Niche is runtime context; core UGC engines remain reusable.

## Architecture
USER BRIEF → BRIEF ANALYSIS → NICHE DETECTION → NICHE RULES → PRODUCT TYPE RULES → UNIVERSAL ENGINE → QC

## Rule layers
### Universal
- product identity lock
- source-of-truth hierarchy
- claim verification
- no invented specifications
- no invented testimonials or personal experience
- visual consistency
- production feasibility

### Niche
Rules and creative patterns for a broad product category:
- content patterns
- visual considerations
- interaction patterns
- claim sensitivity
- storyboard considerations
- QC considerations

### Product type
Rules for a specific product form:
- physical attributes
- interaction model
- demonstration requirements
- continuity risks
- product-specific QC

## Initial supported niches
1. Fashion
2. Beauty
3. Food & Beverage
4. Home & Living
5. Electronics
6. Lifestyle
7. Baby & Kids
8. Pet
9. Sports & Outdoor
10. Automotive

A niche may be PLANNED until its rules are explicitly defined. Affilix must not fabricate niche-specific rules.

## Detection principle
Infer niche from explicit product information or supplied references when confidence is sufficient. If niche or product type materially affects the output and cannot be determined safely, ask a targeted clarification.

## Runtime principle
Do not create separate storyboard, visual, video, or voice engines per niche. Load niche/product-type context into the existing engines.
