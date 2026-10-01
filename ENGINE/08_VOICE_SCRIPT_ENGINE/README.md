# Affilix — Voice Script Engine

## Purpose

The Voice Script Engine converts the approved content strategy and storyboard into spoken dialogue, voice-over, and delivery instructions.

It controls what the creator says and how the delivery should align with the creator profile, scene timing, product evidence, and CTA.

## Input

- Normalized campaign brief
- Selected creator profile
- Product facts
- Approved selling points
- Content strategy
- Approved hook
- Storyboard
- Scene durations
- Platform requirements
- Campaign constraints

## Output

Return:

### Voice Metadata

- Script ID
- Creator ID
- Campaign ID
- Language
- Language mix when explicitly supported
- Delivery style
- Overall tone
- Approximate speaking pace
- Total spoken duration

### Scene Dialogue

For each scene:

- Scene ID
- Dialogue type: Spoken / Voice-over / None
- Exact dialogue
- Delivery intent
- Emotion
- Pace
- Emphasis
- Pause points
- Pronunciation notes when needed
- Lip-sync priority
- CTA role when applicable

## Script Structure

Use the approved storyboard as the source sequence.

Default structure:

1. Hook
2. Relatable context
3. Product introduction
4. Demonstration
5. Benefit / proof
6. Personal reaction
7. CTA

The structure may be shortened or rearranged when required.

## Creator Voice Rules

Follow the selected creator profile for:

- Language
- Vocabulary
- Sentence length
- Delivery speed
- Tone
- Formality
- Humor
- Filler usage
- Signature phrases, only when actually defined in the creator profile

Do not invent a creator's speaking habits or personal history.

## Claim Rules

Dialogue may contain only claims supported by:

- User-provided campaign information
- Approved product data
- Approved references
- Verified evidence
- Explicitly supplied creator experience

Do not invent:

- Product performance
- Medical outcomes
- Guarantees
- Reviews
- Testimonials
- Personal usage history
- Discounts
- Scarcity
- Promotional terms
- Comparative superiority

## Personal Experience

A creator may speak in first person only when the underlying experience is explicitly provided.

Allowed when supplied:
- "Aku sudah pakai ini selama..."
- "Menurut pengalamanku..."

Not allowed when unsupported:
- "Aku sudah pakai ini berbulan-bulan."
- "Aku selalu pakai ini setiap hari."
- "Aku benar-benar merasakan hasilnya."

## Benefit Language

Separate factual product information from subjective reaction.

### Factual

"Materialnya tercantum sebagai [verified material]."

### Subjective

"Menurutku tampilannya jadi lebih clean."

Subjective language must not be used to disguise an unsupported factual claim.

## Dialogue Timing

The script must fit the storyboard duration.

Consider:

- Speaking speed
- Pauses
- Emphasis
- Natural breathing
- Product demonstration timing
- Lip-sync requirements

Do not overload a short scene with excessive dialogue.

When timing is uncertain, shorten the script rather than assuming an unrealistically fast delivery.

## Delivery Direction

Use concise direction such as:

- Calm
- Conversational
- Warm
- Curious
- Confident
- Excited
- Reassuring
- Thoughtful

Delivery direction must match the creator profile and scene objective.

## Emphasis

Mark only words or phrases that materially matter to the message.

Avoid excessive emphasis.

## Pause Design

Use pauses to support:

- Hook impact
- Product reveal
- Key benefit
- Demonstration
- Emotional reaction
- CTA

Pauses should remain natural.

## CTA

CTA must follow the approved campaign objective.

Possible CTA roles:

- Explore the product
- View product details
- Shop
- Visit product page
- Save
- Comment
- Follow
- Other explicit campaign action

Never fabricate promotional urgency.

## Voice-Video Synchronization

Coordinate dialogue with:

- Mouth visibility
- Creator gaze
- Hand movement
- Product demonstration
- Camera movement
- Scene transitions

When a scene contains important product interaction, dialogue should not obscure the visual proof.

## Script Validation

Before handoff, verify:

### Accuracy

- Every product claim has support.
- No fabricated experience exists.
- No unsupported promotional language exists.

### Creator

- Language and delivery match creator profile.
- Persona remains consistent.
- No invented signature phrases.

### Timing

- Dialogue fits scene duration.
- Pauses are plausible.
- CTA has enough time.

### Narrative

- Dialogue follows storyboard.
- Hook connects to the content strategy.
- Product explanation supports the selected angle.
- CTA follows naturally.

## Handoff

The final voice package is passed to:

- Video generation workflow
- Voice synthesis workflow when available
- 09_QUALITY_CONTROL

The storyboard remains the canonical scene sequence. The Voice Script Engine owns spoken language and delivery direction.
