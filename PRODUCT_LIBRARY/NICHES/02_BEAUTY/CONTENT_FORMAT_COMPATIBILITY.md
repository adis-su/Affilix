# Beauty — Content Format Compatibility

This file defines the initial Beauty compatibility guidance for Stage 04 Content Strategy.

It does not replace product-type evidence. Product-specific facts and claims remain authoritative.

## Product Behavior → Format Guidance

| Product behavior | Strong formats | Conditional formats | Usually weak |
|---|---|---|---|
| TESTABLE | Beauty Crime Scene, Beauty Myth Lab, Product Interrogation, Silent Beauty Test | Anti-Tutorial, Problem-Solution Mission | Lifestyle Integration |
| JOB_ORIENTED | Product Has a Job, Problem-Solution Mission, Beauty Crime Scene | Beauty Routine Under Pressure, Silent Beauty Test | One Product, Three Personalities |
| MULTI_MODE | One Product, Three Personalities, Lifestyle Integration | Demonstration, Silent Beauty Test | Product Interrogation |
| EXPERIENCE_LED | Lifestyle Integration, Silent Beauty Test | Beauty Routine Under Pressure, One Product, Three Personalities | Beauty Myth Lab, Product Interrogation |
| PROBLEM_SOLUTION | Product Has a Job, Problem-Solution Mission, Beauty Crime Scene | Beauty Myth Lab, Silent Beauty Test | One Product, Three Personalities |

## Beauty Product-Type Examples

These are format tendencies, not automatic selections.

| Product type / example | Strong candidate formats | Selection condition |
|---|---|---|
| sunscreen | Beauty Crime Scene, Beauty Myth Lab, Product Has a Job, Silent Beauty Test | Must use only supported protection/application/appearance claims. |
| foundation | Beauty Myth Lab, Beauty Crime Scene, One Product, Three Personalities | Test or mode must be observable and supported. |
| concealer | Product Has a Job, Problem-Solution Mission | Focus on a specific supported use case, not guaranteed correction. |
| lip tint | One Product, Three Personalities, Lifestyle Integration | Requires legitimate variation in context, finish, intensity, or styling. |
| mascara | Beauty Myth Lab, Product Interrogation | Test only observable, evidence-backed properties. |
| blush | One Product, Three Personalities, Lifestyle Integration | Use distinct legitimate looks or contexts. |
| skincare serum | Product Has a Job, Lifestyle Integration | Product role and claims must come from supplied evidence. |
| moisturizer | Product Has a Job, Silent Beauty Test, Lifestyle Integration | Keep observable texture/application/value distinct from unsupported treatment claims. |
| cleanser | Beauty Crime Scene, Product Has a Job, Problem-Solution Mission | Demonstrate cleansing action without inventing medical outcomes. |
| hair serum | Product Has a Job, Beauty Crime Scene, Lifestyle Integration | Focus on supported hair-use case and physical interaction. |
| hair mask | Beauty Routine Under Pressure, Product Has a Job, Problem-Solution Mission | Avoid unsupported transformation claims. |
| body lotion | Lifestyle Integration, Product Has a Job, Silent Beauty Test | Emphasize supported application/experience/use context. |
| perfume | Lifestyle Integration, One Product, Three Personalities | Use context, mood, occasion, or styling; avoid scientific-test framing unless evidence exists. |
| lip balm | Product Has a Job, Lifestyle Integration, Silent Beauty Test | Keep claims within supported moisturizing/protective/use evidence. |
| sheet mask | Lifestyle Integration, Beauty Routine Under Pressure, Product Has a Job | Do not invent before/after transformation. |

## Selection Rule

The engine should not output a format from this table solely because the product type matches.

Use:

```
PRODUCT TYPE
+ PRODUCT BEHAVIOR
+ CAMPAIGN OBJECTIVE
+ CREATOR FIT
+ PROOF OPPORTUNITY
+ PLATFORM
→ CONTENT FORMAT
```

If the product-specific source material conflicts with a generic tendency here, the product-specific source wins.

## Claim Safety

Never use a format to smuggle unsupported claims into the narrative.

In particular, do not infer:
- medical treatment
- cure
- guaranteed results
- percentage improvement
- clinical/testing claims
- certification
- expert endorsement
- personal experience
- unsupported before/after transformation
- superiority over alternatives

A creative format is not evidence. Humanity has unfortunately needed this sentence written down.
