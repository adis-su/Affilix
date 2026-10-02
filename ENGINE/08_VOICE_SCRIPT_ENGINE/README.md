# Affilix — Voice Script Engine

## Purpose

The Voice Script Engine converts the validated content strategy and storyboard into spoken dialogue, voice-over, and delivery instructions.

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



## UGC Conversationality Rules

The Voice Script is spoken creator content, not a product-page rewrite or a feature-to-benefit advertisement.

Convert supported product facts into natural spoken language without weakening factual accuracy:

**PRODUCT FACT → CONVERSATIONAL INTERPRETATION → SPOKEN LINE**

Prefer a human conversational progression such as:

**PERSONAL/RELATABLE CONTEXT → PRODUCT OBSERVATION → REASON/BENEFIT → NATURAL CTA**

Do not default to:

**FEATURE STACK → BENEFIT STACK → PROMOTIONAL CLAIM → HARD CTA**

### Conversational Language

Prefer:
- short spoken sentences
- contractions or everyday Indonesian phrasing when consistent with the creator profile
- specific observations grounded in available product facts
- natural transitions between context, product, and CTA
- restrained repetition and emphasis
- wording that sounds plausible when spoken aloud

Avoid by default:
- brochure-like feature lists
- stacked benefit clauses
- formal product-page phrasing
- generic marketing filler
- exaggerated superlatives
- forced English marketing phrases when they are not part of the creator profile or campaign requirement

A hard CTA such as "Buy now" is allowed when explicitly selected or required by the campaign. It must not be inserted merely because the script contains a product benefit. When a softer delivery is compatible with the selected CTA, preserve the CTA intent while making the spoken transition natural.

Examples:

Less conversational:
"Memiliki ceramide complex untuk membantu hidrasi dan mendukung skin barrier dengan sensasi ringan untuk rutinitas skincare. Buy now."

More conversational:
"Yang aku suka dari ini, ada ceramide complex-nya dan teksturnya juga ringan. Jadi enak dipakai sehari-hari."

The example demonstrates style only. Product facts must still come from validated evidence, and first-person product experience may only be used when explicitly supplied.

### Conversationality Boundaries

Natural UGC language must never become a license to invent experience.

Do not generate unsupported statements such as:
- "Aku sudah pakai ini seminggu."
- "Kulitku langsung jauh lebih lembap."
- "Ini paling cocok buat aku."

unless the underlying experience or claim is explicitly supported.

Likewise, do not convert a verified product fact into a stronger efficacy claim merely to make the line sound conversational.


## Spoken Naturalization Rules

Voice Script must distinguish canonical written dialogue from how that dialogue is naturally delivered by a human voice.

Use the following transformation:

**PRODUCT FACT → CONVERSATIONAL INTERPRETATION → SPOKEN LANGUAGE NORMALIZATION → CANONICAL DIALOGUE + DELIVERY NOTES**

Spoken naturalization is a delivery layer, not a license to change factual meaning, invent experience, or rewrite the canonical dialogue downstream.

### Spoken Term Handling

For each non-trivial spoken term, determine when needed:

- written term
- spoken language
- pronunciation note
- emphasis level
- delivery context

Established niche terminology may remain in its original language when it is natural for the selected creator and audience.

Examples in beauty/skincare include:
- skin barrier
- ceramide
- ceramide complex
- niacinamide
- hyaluronic acid

Do not automatically translate established niche terminology into formal Indonesian merely to avoid English words.

### Natural Pronunciation

Pronunciation guidance must:

- preserve the intended lexical identity
- use the natural pronunciation of the selected language
- avoid letter-by-letter spelling unless the term is an acronym
- avoid forced Indonesian phonetics for established English terminology
- avoid exaggerated foreign accents
- avoid over-emphasizing technical terminology
- remain compatible with the available voice synthesis system

Pronunciation notes are delivery instructions. They must not replace or mutate the canonical dialogue text.

Example:

Canonical dialogue:
"Yang aku suka dari ini, ada ceramide complex-nya, jadi bantu jaga skin barrier."

The words "ceramide complex" and "skin barrier" remain unchanged in the canonical dialogue. If needed, pronunciation guidance is attached as delivery metadata.

### Spoken Naturalness

Technical terms should normally appear inside a natural sentence rather than as isolated marketing keywords.

Prefer:
"Yang aku suka dari ini, ada ceramide complex-nya, jadi bantu jaga skin barrier."

Avoid by default:
"Ceramide complex. Skin barrier. Lightweight texture."

unless the storyboard or creator delivery explicitly requires short fragmented speech.

### Mixed-Language Delivery

Indonesian-English mixing is allowed when:

- the terminology is established in the selected niche
- the creator profile supports the language mix
- the audience/context makes the term natural
- the campaign does not require strict single-language delivery

Do not insert English terminology merely to make the script sound premium, modern, or persuasive.

### Acronyms

Acronyms such as SPF, PA++, and pH must receive explicit spoken treatment when pronunciation is ambiguous or likely to be mishandled by voice synthesis.

Do not assume an acronym should always be spelled out or pronounced as a word.

### Brand and Product Names

Brand and product names must preserve their canonical written identity.

If pronunciation is non-obvious, add a pronunciation note rather than changing the canonical name.

### Spoken Naturalization Boundaries

Spoken naturalization must not:

- invent words that are not supported by the intended dialogue
- strengthen or weaken a product claim
- invent personal experience
- change product or brand identity
- silently translate or replace established technical terms
- introduce unnecessary English marketing language
- alter exact dialogue required by campaign constraints

### Spoken Delivery Metadata

When needed, each scene may include:

- Written term
- Spoken language
- Pronunciation note
- Emphasis
- Delivery context

Do not generate pronunciation notes for every ordinary word. Add them only when pronunciation, language mixing, or TTS handling could materially affect natural delivery.

## CTA Delivery Rules

CTA selection comes from Campaign Intake and CTA strategy. Voice Script owns how that CTA is spoken.

The script should distinguish:
- **CTA intent**: the action requested by the campaign
- **CTA wording**: the exact spoken wording
- **CTA delivery**: how naturally the creator says it

Examples of natural delivery:
- Buy now → "Kalau memang cocok, langsung cek produknya."
- Check the product → "Kalau penasaran, coba cek produknya."
- Learn more → "Kalau mau lihat detailnya, bisa cek produknya."
- Add to cart → "Kalau lagi cari yang seperti ini, bisa masukin ke keranjang."

These are delivery examples, not mandatory rewrites. If the campaign explicitly requires the exact CTA text, preserve that wording.

Never fabricate urgency, scarcity, discount, or promotional pressure.

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

## Conversationality Validation

In addition to factual and timing validation, inspect the spoken script for UGC naturalness.

Flag `NEEDS_REFINEMENT` when the dialogue shows one or more of these patterns without a clear campaign reason:
- stacked feature and benefit clauses
- brochure-like product description
- repeated marketing terminology
- abrupt hard CTA after a dense product-information sentence
- promotional phrasing that does not match the selected creator voice
- dialogue that reads naturally as written copy but awkwardly when spoken aloud

Conversationality validation must be advisory rather than a blanket ban. A hard CTA, technical terminology, or concise product claim may remain when required by the campaign, platform, creator profile, or approved wording.

A refinement should preserve:
- supported product facts
- approved claims
- creator constraints
- campaign objective
- selected CTA intent
- storyboard timing

Do not "humanize" a script by inventing personal experience, unsupported outcomes, or unverified claims.

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

The final Voice Script is passed to the Video Prompt Engine when video output requires spoken content, and to the voice synthesis workflow when available.

Video Prompt consumes this Voice Script as the canonical source for exact spoken wording, speaker, delivery, and speech timing. It must not independently rewrite dialogue.

The storyboard remains the canonical scene sequence and temporal source. The Voice Script Engine owns spoken language and delivery direction. Downstream Video Prompt owns synchronization of this canonical voice content with visual action.


## Layered Niche Context Integration

Voice scripts now receive Loaded Niche Context. Context may influence vocabulary, scenario framing, pacing, and delivery intent. It must not be converted into unsupported product claims or personal experience.


## Downstream Contract

For video output, Voice Script is upstream of Video Prompt. A Voice Script revision makes affected Video Prompt artifacts STALE and requires revalidation. Visual Prompt is a parallel Storyboard-derived artifact and is not automatically regenerated by a dialogue-only revision unless visual or action timing is affected.
