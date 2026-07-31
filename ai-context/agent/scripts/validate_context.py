#!/usr/bin/env python3
"""Deterministic consistency checks for a generated ai-context directory.

Replaces LLM re-reading of every file with fast, reliable, mechanical
checks (AGENTS.md Rules 11-14, 16). Standard library only — no install step,
consistent with AGENTS.md Rule 3 (no downloads/installs).

Usage:
    python3 scripts/validate_context.py <path-to-ai-context-directory>

Exit code is 0 when no errors are found, 1 otherwise. Warnings do not affect
the exit code.
"""

import json
import re
import sys
from pathlib import Path

MAX_FILE_LINES = 500
MIN_DUPLICATE_LINE_LENGTH = 40
PROVENANCE_KEYWORDS = re.compile(r"\[(VERIFIED|POLICY|Not confirmed)", re.IGNORECASE)
VALID_PROVENANCE_TAGS = re.compile(
    r"\[VERIFIED: [^\]@]+@[^\]]+\]|\[POLICY: [^\]]+\]|\[Not confirmed\]"
)
STRUCTURAL_LINE = re.compile(r"^(#{1,6}\s|\|[\s\-:|]+\|$|```|---$)")


def load_manifest(context_dir):
    manifest_path = context_dir / "manifest.json"
    if not manifest_path.is_file():
        return None, [f"manifest.json not found in {context_dir}"]
    try:
        return json.loads(manifest_path.read_text()), []
    except json.JSONDecodeError as exc:
        return None, [f"manifest.json is not valid JSON: {exc}"]


def check_manifest_schema(manifest):
    errors = []
    required_top_level = [
        "formatVersion",
        "directory",
        "generatedAt",
        "lastUpdatedAt",
        "project",
        "documents",
        "topics",
    ]
    for key in required_top_level:
        if key not in manifest:
            errors.append(f"manifest.json missing required key: {key}")
    return errors


def check_document_paths(manifest, context_dir):
    errors = []
    known_paths = set()
    for doc in manifest.get("documents", []):
        path = doc.get("path")
        if not path:
            errors.append(f"manifest.json document entry missing 'path': {doc}")
            continue
        known_paths.add(path)
        if not (context_dir / path).is_file():
            errors.append(f"manifest.json references missing file: {path}")
    return errors, known_paths


def check_topics(manifest, known_paths):
    errors = []
    for topic, files in manifest.get("topics", {}).items():
        for path in files:
            if path not in known_paths:
                errors.append(
                    f"topics['{topic}'] references '{path}', which is not "
                    f"listed in manifest.json documents"
                )
    return errors


def check_provenance_tags(md_files):
    warnings = []
    for path in md_files:
        for lineno, line in enumerate(path.read_text().splitlines(), start=1):
            if not PROVENANCE_KEYWORDS.search(line):
                continue
            if not VALID_PROVENANCE_TAGS.search(line):
                warnings.append(
                    f"{path.name}:{lineno}: provenance-looking tag does not "
                    f"match the required format — {line.strip()}"
                )
    return warnings


def check_file_length(md_files):
    warnings = []
    for path in md_files:
        line_count = len(path.read_text().splitlines())
        if line_count > MAX_FILE_LINES:
            warnings.append(
                f"{path.name}: {line_count} lines exceeds the {MAX_FILE_LINES}-line "
                f"budget — consider splitting and adding a manifest.json topic entry"
            )
    return warnings


def check_duplicate_facts(md_files):
    warnings = []
    seen = {}
    for path in md_files:
        for line in path.read_text().splitlines():
            stripped = line.strip()
            if len(stripped) < MIN_DUPLICATE_LINE_LENGTH:
                continue
            if STRUCTURAL_LINE.match(stripped):
                continue
            normalized = re.sub(r"\s+", " ", stripped.lower())
            seen.setdefault(normalized, set()).add(path.name)
    for normalized, files in seen.items():
        if len(files) > 1:
            warnings.append(
                f"possible duplicated fact across {sorted(files)}: {normalized[:120]}"
            )
    return warnings


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    context_dir = Path(sys.argv[1])
    if not context_dir.is_dir():
        print(f"error: {context_dir} is not a directory")
        return 1

    errors = []
    warnings = []

    manifest, manifest_errors = load_manifest(context_dir)
    errors.extend(manifest_errors)

    if manifest is not None:
        errors.extend(check_manifest_schema(manifest))
        path_errors, known_paths = check_document_paths(manifest, context_dir)
        errors.extend(path_errors)
        errors.extend(check_topics(manifest, known_paths))

    md_files = sorted(context_dir.glob("*.md"))
    warnings.extend(check_provenance_tags(md_files))
    warnings.extend(check_file_length(md_files))
    warnings.extend(check_duplicate_facts(md_files))

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    if not errors and not warnings:
        print(f"OK: {context_dir} passed all checks")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
