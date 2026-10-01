# Universal Runtime U005 Fixture

Test: U005
Scenario: Cross-Niche Context Isolation

Run A:
- Niche: Fashion
- Sub-Niche: Streetwear
- Product Type: Top
- Use Case: Everyday
- Style: Street

Run B:
- Niche: Beauty
- Sub-Niche: Skincare
- Product Type: Skincare Product
- Use Case: Everyday Beauty
- Style: Natural Look

Required behavior:
- Run B must contain only its own canonical context.
- Fashion context from Run A must not affect Beauty strategy, hook, storyboard, visual, video, voice, or QC.
- Product and creator identity must remain sourced from the current run.
- No stale context may survive reinitialization.
