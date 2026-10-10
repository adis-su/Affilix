#!/usr/bin/env python3
"""Static contract checks for Affilix.

These checks verify repository wiring and critical documented invariants.
They do not execute the conversational Skill runtime or external media providers.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "ENGINE/WORKFLOW.md",
    "ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md",
    "ENGINE/AFFILIX_ENTRY_POINT/README.md",
    "ENGINE/01_BRIEF_ANALYZER/README.md",
    "ENGINE/08_VOICE_SCRIPT_ENGINE/QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md",
    "ENGINE/05_STORYBOARD_ENGINE/QUOTE_CONTENT_STORYBOARD_CONTRACT.md",
    "ENGINE/06_VISUAL_PROMPT_ENGINE/QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md",
    "ENGINE/07_VIDEO_PROMPT_ENGINE/QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md",
    "ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md",
    "ENGINE/05_STORYBOARD_ENGINE/DOWNSTREAM_AUTHORITY_CONTRACT.md",
    "ENGINE/07_VIDEO_PROMPT_ENGINE/RUNTIME_OUTPUT_CONTRACT.md",
    "ENGINE/08_VOICE_SCRIPT_ENGINE/RUNTIME_OUTPUT_CONTRACT.md",
    "EXAMPLES/QUOTE_CONTENT_REGRESSION_MATRIX.md",
]

errors = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if condition:
        print(f"PASS: {message}")
    else:
        errors.append(message)
        print(f"FAIL: {message}")


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


for relative in REQUIRED_FILES:
    check((ROOT / relative).is_file(), f"required contract exists: {relative}")

workflow = read("ENGINE/WORKFLOW.md")
routing = read("ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md")
skill = read("SKILL.md")
storyboard = read("ENGINE/05_STORYBOARD_ENGINE/QUOTE_CONTENT_STORYBOARD_CONTRACT.md")
visual = read("ENGINE/06_VISUAL_PROMPT_ENGINE/QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md")
video = read("ENGINE/07_VIDEO_PROMPT_ENGINE/QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md")
output = read("ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md")
matrix = read("EXAMPLES/QUOTE_CONTENT_REGRESSION_MATRIX.md")
entry = read("ENGINE/AFFILIX_ENTRY_POINT/README.md")
brief = read("ENGINE/01_BRIEF_ANALYZER/README.md")
voice = read("ENGINE/08_VOICE_SCRIPT_ENGINE/QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md")
authority = read("ENGINE/05_STORYBOARD_ENGINE/DOWNSTREAM_AUTHORITY_CONTRACT.md")
video_runtime = read("ENGINE/07_VIDEO_PROMPT_ENGINE/RUNTIME_OUTPUT_CONTRACT.md")
voice_runtime = read("ENGINE/08_VOICE_SCRIPT_ENGINE/RUNTIME_OUTPUT_CONTRACT.md")

# Canonical registry identity and the non-numeric engine-to-stage mappings.
stage_rows = [match.group(1) for match in re.finditer(r"^\|\s*(\d{2})\s*\|[^\n]*ENGINE/", workflow, flags=re.MULTILINE)]
check(stage_rows[:10] == [f"{i:02d}" for i in range(1, 11)],
      "canonical workflow registry lists stages 01–10 in order")
check("08 | Voice Script" in workflow and "ENGINE/08_VOICE_SCRIPT_ENGINE/" in workflow,
      "Stage 08 maps to the Voice Script engine")
check("09 | Video Prompt" in workflow and "ENGINE/07_VIDEO_PROMPT_ENGINE/" in workflow,
      "Stage 09 maps to the Video Prompt engine")
check("No QC stage, Final UGC Package stage, or approval gate exists." in workflow,
      "canonical workflow excludes QC, Final UGC Package, and approval gate")
check("engine directory prefixes" in skill.lower() and "must not" in skill.lower(),
      "Skill documents that engine directory prefixes do not define stage order")

# Mode routing and the static-image branch.
check("UGC_AFFILIATE" in routing and "QUOTE_CONTENT" in routing,
      "both supported content modes are registered")
check("never fall back to ugc template" in routing.lower(),
      "Quote Content cannot silently fall back to the UGC output template")
for relative, content in [
    ("Storyboard", storyboard),
    ("Video Prompt", video),
]:
    check("STATIC_IMAGE_FORMAT" in content and "QUOTE_IMAGE" in content,
          f"{relative} contract defines the static-image skip")
check("Stage 06, 08, and 09 must be `SKIPPED` with `STATIC_IMAGE_FORMAT`" in output,
      "Production Output enforces Quote Image skip states")

# Reference-state coverage and prompt/scene cardinality.
check("target_reference_count" in storyboard and "reference_version" in storyboard,
      "Storyboard declares reference counts and versioned reference states")
check("one image prompt for each Storyboard-declared reference state" in visual,
      "Visual Prompt requires one image prompt per declared reference state")
check("video_prompt_count = storyboard_scene_count" in video,
      "Video Prompt count equals Storyboard scene count")
check("bridge" in storyboard.lower() and "reference_version" in storyboard and "exact same" in storyboard.lower(),
      "Storyboard protects immutable bridge references")

# Exact duration and honest regression reporting.
for content, label in [(storyboard, "Storyboard"), (video, "Video Prompt"), (output, "Production Output")]:
    exact_duration = "sum exactly" in content.lower() or "must equal" in content.lower()
    blocked_duration = "duration_feasibility" in content and "BLOCKED" in content
    check(all(token in content for token in ("4", "6", "8", "10")) and
          exact_duration and blocked_duration,
          f"{label} contract preserves exact segment duration and infeasible-duration blocking")
check("NOT RUN as an end-to-end runtime suite" in matrix,
      "regression matrix clearly distinguishes test specifications from runtime execution")
check(all(f"QCR-{i:03d}" in matrix for i in range(1, 27)),
      "Quote Content regression matrix includes QCR-001 through QCR-026")

# Quote Content intake and duration-bound script rules.
check("20 seconds" in entry and "20 seconds" in routing and "20 seconds" in voice,
      "Quote Content fixed 20-second duration is documented across intake, routing, and voice contract")
check("Segment 1 = 10 seconds" in entry and "10 + 10" in voice,
      "Quote Content uses exactly two 10-second generation segments")
check("content quantity" in entry.lower() and "user-selected CTA" in entry,
      "Quote Content intake excludes content quantity and user-selected CTA fields")
check("38–44" in voice,
      "Quote Content voice contract defines the 20-second spoken-word target")

# Cross-stage timing and source-integrity invariants.
check("time_window:" in storyboard and "start_time:" in storyboard and "end_time:" in storyboard,
      "Quote Content Storyboard schema exposes explicit beat timing windows")
check("dialogue_anchor:" in storyboard and "semantic_intent:" in storyboard and "action_window:" in storyboard and "target_reference:" in storyboard,
      "Quote Content Storyboard schema exposes resolvable dialogue anchors")
check("anchor_resolution: PASS | NEEDS_REFINEMENT | BLOCKED" in voice and "source_freshness: PASS | BLOCKED" in voice,
      "Quote Content Voice Script requires anchor-resolution and source-freshness validation")
check("action_window" in voice and "target_reference" in voice and "protected pause" in voice.lower(),
      "Voice Script validates line timing, target references, and protected visual beats")
check("source_freshness: PASS | BLOCKED" in video and "dependency_alignment: PASS | BLOCKED" in video,
      "Video Prompt blocks stale or mismatched Storyboard, Visual Prompt, and Voice Script sources")
check("QCR-024" in matrix and "QCR-025" in matrix and "QCR-026" in matrix,
      "Regression matrix includes timing, dialogue-anchor, and stale-source integration cases")

# Storyboard authority and Quote Content run-wide production invariants.
check("Cross-Stage Lineage and Handoff Invariants" in authority and
      "Stage 08 is a parallel descendant of Stage 06" in authority,
      "Storyboard authority contract defines lineage and parallel Stage 07/08 branches")
check("exactly two segments total" in video and "[0, 10]" in video and "[10, 20]" in video,
      "Quote Content Video Prompt enforces a run-wide 10s + 10s timeline")
check("source_scene_ids: []" in video and "run_wide_segment_composition: PASS | BLOCKED" in video,
      "Video Prompt segment schema can identify source scenes and validate run-wide composition")
check("reference_coverage: PASS | BLOCKED | NOT_APPLICABLE" in output and
      "storyboard_lineage: PASS | BLOCKED" in output,
      "Production Output validates canonical reference coverage and Storyboard lineage")
check("exactly two segments total" in output and "no gaps or overlaps" in output,
      "Production Output blocks segment count, duration, gap, and overlap mismatches")
check("exact Storyboard artifact/version" in authority and
      "Never silently mix artifacts from different Storyboard versions" in authority,
      "Downstream stages must pin the same exact Storyboard version")
check("Storyboard owns creative scene intent and timing" in video_runtime and "Video Prompt owns motion and technical generation segmentation" in video_runtime and
      "Voice Script owns spoken language and delivery direction only" in voice_runtime,
      "Stage 08/09 runtime contracts preserve field ownership")
check(all(f"QCR-{i:03d}" in matrix for i in range(27, 33)),
      "Regression matrix includes QCR-027 through QCR-032 for downstream integration")
check("final video duration" in brief.lower() and "NOT_APPLICABLE" in brief,
      "Brief Analyzer normalizes video duration and static-image not-applicable state")

print(f"\nStatic contract checks: {checks - len(errors)}/{checks} passed.")
if errors:
    print(f"Failures: {len(errors)}")
    sys.exit(1)
print("Scope note: static contract consistency only; no end-to-end runtime test was executed.")
