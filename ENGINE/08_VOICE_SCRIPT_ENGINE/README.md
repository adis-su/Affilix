# Affilix — Voice Script Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 09 — Voice Script
- Implementation path: `ENGINE/08_VOICE_SCRIPT_ENGINE/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Content Format Continuity

The selected Content Format from Stage 04 is an upstream narrative constraint for spoken content. Voice Script must support the format's story mechanism through dialogue structure, product reveal, proof language, and CTA when applicable.

Content Format does not authorize unsupported claims or invented experience. It shapes how validated facts are spoken, while Content Angle and Campaign Objective remain authoritative for the message.

If the Content Format changes, affected Voice Script artifacts become STALE and require revalidation.

## Content Format Mechanism Validation

Content Format must materially shape spoken content. Recording the selected format in metadata is not sufficient.

Validate each Voice Script against:

1. **Format mechanism** — dialogue establishes or supports the selected format's narrative mechanism.
2. **Product role** — spoken content gives the product the role required by the format.
3. **Proof language** — dialogue describes only evidence that the storyboard can actually demonstrate or that is explicitly supported.
4. **Action/dialogue alignment** — spoken lines explain, frame, or react to the action without replacing visual proof with unsupported claims.
5. **CTA continuity** — CTA wording remains compatible with the selected format and campaign objective.
6. **Format preservation** — dialogue must not imply a different content format.

Format-specific voice mechanisms:

| Content Format | Required spoken mechanism |
|---|---|
| BEAUTY_CRIME_SCENE | Establish the recognizable beauty problem/case, frame the investigation or intervention, then describe the observable result without inventing performance. |
| PRODUCT_HAS_A_JOB | State the concrete need/task, identify the product's job, and connect the spoken line to the resulting task state. |
| BEAUTY_MYTH_LAB | State a testable beauty question or assumption, describe the controlled test, and interpret only the evidence actually available. |
| PRODUCT_INTERROGATION | Pose the product question/property being inspected, narrate the inspection/demo, and state only the resulting evidence. |
| ONE_PRODUCT_THREE_PERSONALITIES | Keep one product identity while verbally distinguishing legitimate modes/contexts; do not imply three different products. |
| SILENT_BEAUTY_TEST | Spoken content is optional and must not be required to make the core visual test understandable; when present, it supports rather than substitutes for visible evidence. |
| BEAUTY_ROUTINE_UNDER_PRESSURE | Establish the situational pressure, explain the constrained routine task, and connect the product to the usable resulting state. |
| ANTI_TUTORIAL | State or reframe the expectation, explain the grounded qualification/demo, and avoid turning the reframe into unsupported superiority. |
| LIFESTYLE_INTEGRATION | Anchor the product in a believable routine/context and explain its contextual role without inventing personal experience. |
| PROBLEM_SOLUTION_MISSION | Name the concrete problem, frame the product action as the mission step, and connect the line to the resolved task state. |

A generic product introduction, feature stack, testimonial-style reaction, or CTA cannot pass Content Format validation merely because the selected format appears in metadata.

For NO_SPOKEN_VOICE, this validation is NOT_REQUIRED because Stage 09 is skipped. For spoken modes, a format-specific mechanism failure is NEEDS_REFINEMENT; if the format cannot be expressed without unsupported claims or required proof is unavailable, the Voice Script is BLOCKED.

### Format Mechanism Validation Checklist

- format_mechanism_present: true | false
- product_role_preserved: true | false
- proof_language_supported: true | false
- action_dialogue_aligned: true | false
- cta_compatible: true | false | NOT_APPLICABLE
- format_preserved: true | false
- validation_status: PASS | NEEDS_REFINEMENT | BLOCKED

## Purpose

The Voice Script Engine converts the validated content strategy and storyboard into spoken dialogue, voice-over, and delivery instructions.

It controls what the creator says and how the delivery should align with the creator profile, scene timing, product evidence, and CTA.

## Input

- Normalized campaign brief
- Selected creator profile
- Product facts
- Approved selling points
- Content strategy, including selected Content Format
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

## Voice Performance Plan

The Voice Script Engine owns not only the canonical words that are spoken, but also a structured performance plan describing how those words should be delivered by a human-like voice generator.

The Voice Performance Plan is downstream of canonical dialogue and must never rewrite the spoken wording.

Use the following transformation:

**CANONICAL DIALOGUE → VOICE PERFORMANCE PLAN → VOICE GENERATION**

### Performance Dimensions

When material to the scene, define:

- speaking rate
- phrase grouping
- pause type and placement
- emphasis hierarchy
- pitch variation
- rhythm
- breath opportunities
- emotional intensity
- warmth / intimacy
- articulation clarity
- sentence-ending contour
- on-camera vs voice-over delivery

Do not specify every dimension for every line. Only add direction that materially improves natural delivery or is required by the selected voice system.

### Human Conversational Delivery

Default UGC delivery should sound like a person speaking to another person, not an announcer reading copy.

Prefer:
- conversational pacing
- uneven but controlled emphasis
- natural phrase grouping
- restrained pitch variation
- subtle pauses at semantic boundaries
- natural sentence endings
- clear articulation without over-enunciation
- restrained enthusiasm appropriate to the creator and scene

Avoid:
- equal stress on every word
- perfectly uniform pacing
- constant pitch
- exaggerated commercial-announcer delivery
- excessive pauses after every punctuation mark
- artificial excitement
- theatrical acting unless explicitly required by the scene

### Emphasis Hierarchy

Emphasis should be sparse and intentional.

Use at most a small number of materially important emphasis targets per sentence. Technical terms such as "ceramide complex" or "skin barrier" may receive restrained emphasis when they are the intended information focus, but must not be delivered like advertising keywords.

### Pause Design

Pause metadata must distinguish at least when needed:

- micro pause: brief phrase boundary
- short pause: semantic transition
- breath pause: natural respiratory opportunity
- sentence pause: completed thought

Do not insert a pause mechanically at every comma. Pauses must support meaning, action timing, and natural breathing.

### Breathing

Breathing is a physiological realism cue, not a sound effect.

Use subtle breath opportunities at natural phrase boundaries when the spoken duration or sentence length warrants them.

Avoid exaggerated audible breathing, repeated artificial inhales, or breaths inserted inside a semantic phrase.

### Emotional Intensity

Emotion must be bounded by creator profile, scene objective, and campaign context.

For standard beauty UGC, default toward conversational warmth and restrained enthusiasm rather than maximum excitement.

Do not encode vague instructions such as "sound human" as the sole performance direction. Convert them into observable delivery constraints.

### Voice Profile vs Voice Performance

Separate persistent voice characteristics from per-line performance direction.

**VOICE PROFILE** describes the selected voice identity characteristics, such as:
- language / locale
- vocal warmth
- brightness
- softness
- clarity
- breathiness
- resonance
- baseline energy

**VOICE PERFORMANCE** describes how the current line is delivered, such as:
- pace
- emphasis
- pauses
- pitch movement
- emotional intensity
- phrase grouping
- delivery context

A voice profile must not be inferred from a real person's name or celebrity identity. Specific-person voice imitation is not a substitute for an authorized voice reference or an explicitly defined synthetic voice profile.

### Voice Identity Safety Boundary

Campaign data may reference an authorized voice asset or a repository-defined synthetic voice profile.

Do not transform a celebrity or other real person's name into a voice-cloning instruction. If a voice reference is explicitly authorized, preserve the authorized reference as an identifier or asset reference and apply the provider's permitted voice controls.

### Voice Performance and Video Synchronization

Voice Performance must remain compatible with storyboard timing and Video Prompt dialogue synchronization.

The plan must not:
- change canonical dialogue
- exceed the scene or generation-segment duration
- introduce unsupported personal experience
- conflict with product interaction timing
- require visual mouth movement outside spoken intervals

When dialogue is on-camera, the downstream Video Prompt must use the canonical dialogue and performance timing as its speech synchronization source.

### Voice Performance Validation

Flag NEEDS_REFINEMENT when the performance direction contains one or more of these patterns without a clear reason:
- uniform emphasis across the whole sentence
- monotone or fixed-pitch direction
- unnaturally fast delivery required to fit the scene
- excessive pause density
- exaggerated enthusiasm for a low-energy UGC scene
- announcer or commercial delivery inconsistent with the creator profile
- breathing instructions that are repetitive or conspicuous
- performance instructions that conflict with dialogue timing

Validation is advisory unless the resulting delivery makes the exact dialogue impossible to fit inside the scene duration. Timing infeasibility remains a blocking condition.

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
