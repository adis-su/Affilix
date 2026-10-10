#!/usr/bin/env python3
"""Validate a serialized Quote Content artifact bundle across Stages 06–10.

This is a deterministic integration harness for artifact contracts. It does not
invoke the ChatGPT Skill runtime or a video provider. Input is JSON so the
validator has no third-party dependencies.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def validate_bundle(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("storyboard", "visual_prompt", "voice_script", "video_prompt", "production_output")
    for name in required:
        if not isinstance(bundle.get(name), dict):
            errors.append(f"missing_or_invalid_artifact:{name}")
    if errors:
        return errors

    sb = bundle["storyboard"]
    vp = bundle["visual_prompt"]
    vs = bundle["voice_script"]
    video = bundle["video_prompt"]
    output = bundle["production_output"]

    sb_id, sb_version = sb.get("storyboard_id"), sb.get("storyboard_version")
    sb_commit = sb.get("source_commit_sha")
    if not sb_id or not sb_version or not sb_commit:
        errors.append("storyboard_identity_incomplete")

    scenes = sb.get("scenes", [])
    states = sb.get("reference_plan", {}).get("states", [])
    transitions = sb.get("reference_trajectory", {}).get("transitions", [])
    scene_ids = [s.get("scene_id") for s in scenes]
    state_keys = {(s.get("reference_id"), s.get("reference_version")) for s in states}
    if not scenes or any(not x for x in scene_ids) or len(set(scene_ids)) != len(scene_ids):
        errors.append("storyboard_scene_ids_missing_or_duplicate")
    if not states or any(not rid or not ver for rid, ver in state_keys):
        errors.append("storyboard_reference_states_incomplete")
    if not isinstance(transitions, list):
        errors.append("storyboard_transitions_invalid")
        transitions = []

    def source_matches(artifact: dict[str, Any], artifact_name: str) -> bool:
        sources = artifact.get("source_artifacts", [])
        ok = any(
            x.get("artifact_type") == "STORYBOARD"
            and x.get("artifact_id") == sb_id
            and x.get("artifact_version") == sb_version
            and x.get("source_commit_sha") == sb_commit
            for x in sources if isinstance(x, dict)
        )
        if not ok:
            errors.append(f"{artifact_name}_storyboard_lineage_mismatch")
        if artifact.get("status") == "STALE":
            errors.append(f"{artifact_name}_is_stale")
        return ok

    for artifact, name in ((vp, "visual_prompt"), (vs, "voice_script"), (video, "video_prompt"), (output, "production_output")):
        source_matches(artifact, name)

    # Stage 07: exactly one static prompt for each unique canonical reference state.
    prompts = vp.get("prompts", [])
    prompt_keys = [(p.get("reference_id"), p.get("reference_version")) for p in prompts]
    if set(prompt_keys) != state_keys or len(prompt_keys) != len(state_keys) or len(set(prompt_keys)) != len(prompt_keys):
        errors.append("visual_prompt_reference_coverage_mismatch")

    # Stage 08: every dialogue line resolves to a real scene, beat, and exact reference state.
    beats_by_scene = {
        s.get("scene_id"): {b.get("beat_id"): b for b in s.get("beats", [])}
        for s in scenes
    }
    for line in vs.get("lines", []):
        scene_id, beat_id = line.get("scene_id"), line.get("source_beat_id")
        if scene_id not in beats_by_scene or beat_id not in beats_by_scene.get(scene_id, {}):
            errors.append("voice_line_anchor_unresolved")
            continue
        beat = beats_by_scene[scene_id][beat_id]
        target = (line.get("target_reference_id"), line.get("target_reference_version"))
        if target not in state_keys or target != (beat.get("reference_after", {}).get("reference_id"), beat.get("reference_after", {}).get("reference_version")):
            errors.append("voice_line_reference_anchor_mismatch")
        window, scene_window = line.get("time_window", {}), next((s.get("time_window", {}) for s in scenes if s.get("scene_id") == scene_id), {})
        try:
            start, end = float(window["start_time"]), float(window["end_time"])
            sstart, send = float(scene_window["start_time"]), float(scene_window["end_time"])
            bwindow = beat.get("time_window", {})
            bstart, bend = float(bwindow["start_time"]), float(bwindow["end_time"])
            if not (sstart <= start < end <= send and bstart <= start < end <= bend):
                errors.append("voice_line_timing_outside_scene_or_anchor")
        except (KeyError, TypeError, ValueError):
            errors.append("voice_line_timing_missing_or_invalid")

    # Stage 09: one prompt per storyboard scene; exactly two run-wide 10-second segments.
    video_scenes = video.get("scenes", [])
    video_scene_ids = [s.get("scene_id") for s in video_scenes]
    if video_scene_ids != scene_ids or len(video_scene_ids) != len(scene_ids):
        errors.append("video_prompt_scene_count_or_order_mismatch")
    segments = video.get("generation_segments", [])
    if len(segments) != 2:
        errors.append("generation_segment_count_not_two")
    expected_windows = [(0.0, 10.0, 10.0), (10.0, 20.0, 10.0)]
    actual = []
    for segment in segments:
        try:
            start, end = float(segment["final_start_time"]), float(segment["final_end_time"])
            duration = float(segment["generation_duration"])
            actual.append((start, end, duration))
            if duration != end - start:
                errors.append("generation_segment_duration_window_mismatch")
            if not segment.get("source_scene_ids") or any(sid not in scene_ids for sid in segment["source_scene_ids"]):
                errors.append("generation_segment_scene_mapping_invalid")
            for key in ("start_reference_id", "start_reference_version", "target_reference_id", "target_reference_version"):
                if not segment.get(key):
                    errors.append("generation_segment_reference_metadata_missing")
                    break
            if not isinstance(segment.get("transition_ids"), list):
                errors.append("generation_segment_transition_mapping_missing")
        except (KeyError, TypeError, ValueError):
            errors.append("generation_segment_timing_invalid")
    if actual != expected_windows:
        errors.append("generation_segment_composition_not_exact_10_plus_10")

    transition_ids = {t.get("transition_id") for t in transitions}
    for segment in segments:
        for tid in segment.get("transition_ids", []):
            if tid not in transition_ids:
                errors.append("generation_segment_transition_unresolved")

    # Stage 10 must assemble the exact current upstream artifacts and cannot conceal stale inputs.
    expected_types = {
        "STORYBOARD": (sb_id, sb_version),
        "VISUAL_PROMPT": (vp.get("artifact_id"), vp.get("artifact_version")),
        "VOICE_SCRIPT": (vs.get("artifact_id"), vs.get("artifact_version")),
        "VIDEO_PROMPT": (video.get("artifact_id"), video.get("artifact_version")),
    }
    out_sources = {x.get("artifact_type"): x for x in output.get("source_artifacts", []) if isinstance(x, dict)}
    for kind, identity in expected_types.items():
        source = out_sources.get(kind)
        if not source or (source.get("artifact_id"), source.get("artifact_version")) != identity:
            errors.append(f"production_output_{kind.lower()}_lineage_mismatch")
    if output.get("reference_coverage") != "PASS":
        errors.append("production_output_reference_coverage_not_pass")
    if output.get("duration_integrity") != "PASS":
        errors.append("production_output_duration_integrity_not_pass")

    return sorted(set(errors))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_quote_content_artifacts.py path/to/bundle.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        bundle = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read JSON bundle: {exc}", file=sys.stderr)
        return 2
    errors = validate_bundle(bundle)
    if errors:
        print("BLOCKED: Quote Content artifact bundle failed validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: Quote Content artifact bundle satisfies Stage 06–10 integration invariants")
    print("Scope note: validates serialized artifacts; does not execute the conversational Skill or video provider.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
