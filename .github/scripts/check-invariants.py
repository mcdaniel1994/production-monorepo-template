#!/usr/bin/env python3
"""Check the structural invariants this repository depends on.

Why this script exists
----------------------
Repository contracts that matter need executable feedback. This script keeps structural checks in
CI while leaving project-specific architectural choices to the project.

Why it is Python
----------------
This is repository-maintenance tooling, not product code, and `python3` is preinstalled on GitHub's
runners and on macOS. It is repository-maintenance tooling, not a language choice for product code —
see the `.github/scripts/` row in AGENTS.md. Do not "fix" it for neutrality.

Hard vs. advisory
-----------------
Two checks fail the build, because they guard repository coherence and cannot trap a project
in any direction it might legitimately go: broken internal links, and the AGENTS.md line budget.

The other four report and do not fail. They describe the starting shape, which a project is expected
to outgrow — the moment it picks a language, the neutrality check is supposed to go off. Narrow the
settings below or drop the check; that is the intended escape hatch, not a defect.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

# --- Settings a project is expected to adjust -------------------------------------------------

# Directories where naming a language, framework, or cloud provider is legitimate. A project that
# has chosen its stack should add its own paths here, or stop running the neutrality check.
NEUTRALITY_EXEMPT = (
    "docs/context/",
    "docs/decisions/",
    "docs/build_specs/",
    ".github/scripts/",
)

# Terms that would mean the starting repository had quietly committed to a stack.
NEUTRALITY_TERMS = (
    r"\bpython\b", r"\bpytest\b", r"\bconftest\b", r"\bnpm\b", r"\bpnpm\b", r"\byarn\b",
    r"\bfastapi\b", r"\bpydantic\b", r"\bvitest\b", r"\bplaywright\b", r"\btailwind\b",
    r"\bdjango\b", r"\brails\b", r"\bvercel\b", r"\bnetlify\b", r"\bterraform\b",
)

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build"}

BOOTSTRAP_TOKEN = "BOOTSTRAP" + "_PLACEHOLDER"
PROJECT_TRIGGER_TOKEN = "PROJECT_TRIGGER"
MARKER_CHECK_EXEMPT = {".github/scripts/check-invariants.py"}

# --- Plumbing ---------------------------------------------------------------------------------

failures: list[str] = []
warnings: list[str] = []


def repo_root() -> str:
    return subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def markdown_files(root: str) -> list[str]:
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                found.append(os.path.relpath(os.path.join(dirpath, name), root))
    return sorted(found)


def repository_text_files(root: str) -> list[tuple[str, str]]:
    """Return tracked and visible untracked UTF-8 text files.

    Git supplies the file list so ignored build output never becomes an advisory finding. Deleted
    tracked paths, symlinks, binary files, and reusable `*-template.md` files are skipped.
    """
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        capture_output=True, check=True, cwd=root,
    )
    found = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        path = os.fsdecode(raw_path)
        absolute = os.path.join(root, path)
        if (
            path in MARKER_CHECK_EXEMPT
            or os.path.basename(path).endswith("-template.md")
            or not os.path.isfile(absolute)
            or os.path.islink(absolute)
        ):
            continue
        try:
            with open(absolute, encoding="utf-8") as handle:
                found.append((path, handle.read()))
        except UnicodeDecodeError:
            continue
    return found


def heading_slug(heading: str) -> str:
    """Mirror GitHub's anchor generation.

    Each space becomes its own hyphen — GitHub does not collapse runs. A heading like
    "8. Machine-readable discovery & crawler access" loses the "&" and keeps the two spaces
    around it, yielding "...discovery--crawler-access" with a double hyphen.
    """
    slug = re.sub(r"[^\w\s-]", "", heading.strip().lower())
    return re.sub(r"\s", "-", slug).strip("-")


def section(title: str) -> None:
    print(f"\n--- {title} ---")


# --- 1. Links and anchors (HARD) ---------------------------------------------------------------

def check_links(root: str, files: list[str]) -> None:
    section("Links and anchors")
    anchors = {}
    for path in files:
        with open(os.path.join(root, path), encoding="utf-8") as handle:
            text = handle.read()
        anchors[path] = {heading_slug(m) for m in re.findall(r"^#{1,6}\s+(.*)$", text, re.M)}

    broken = []
    for path in files:
        directory = os.path.dirname(path)
        with open(os.path.join(root, path), encoding="utf-8") as handle:
            text = handle.read()
        for _label, link in re.findall(r"\[([^\]]*)\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            target_path, _, anchor = link.partition("#")
            if target_path:
                resolved = os.path.normpath(os.path.join(directory, target_path))
                if not os.path.exists(os.path.join(root, resolved)):
                    broken.append(f"{path} -> {link} (missing path)")
                    continue
            else:
                resolved = path
            if anchor:
                key = resolved
                if key not in anchors and os.path.isdir(os.path.join(root, resolved)):
                    key = os.path.join(resolved, "README.md")
                if key in anchors and anchor not in anchors[key]:
                    broken.append(f"{path} -> {link} (missing anchor)")

    if broken:
        for item in broken:
            print(f"  BROKEN  {item}")
        failures.append(f"{len(broken)} broken markdown link(s) across {len(files)} files")
    else:
        print(f"  OK  {len(files)} files, every link and anchor resolves")


# --- 2. AGENTS.md line budget (HARD) -----------------------------------------------------------

def check_line_budget(root: str) -> None:
    section("AGENTS.md line budget")
    agents = os.path.join(root, "AGENTS.md")
    if not os.path.exists(agents):
        failures.append("AGENTS.md is missing")
        print("  BROKEN  AGENTS.md not found")
        return

    with open(agents, encoding="utf-8") as handle:
        lines = handle.readlines()

    # The budget is declared in AGENTS.md itself so there is exactly one owner for the number.
    match = re.search(r"\*\*Line budget:\s*(\d+)\.\*\*", "".join(lines))
    if not match:
        failures.append("AGENTS.md no longer declares its line budget")
        print("  BROKEN  no '**Line budget: N.**' declaration found in AGENTS.md")
        return

    budget, actual = int(match.group(1)), len(lines)
    if actual > budget:
        failures.append(f"AGENTS.md is {actual} lines, over its declared budget of {budget}")
        print(f"  BROKEN  {actual} lines, budget {budget}")
    else:
        print(f"  OK  {actual} lines, budget {budget}")


# --- 3. Empty directories (ADVISORY) -----------------------------------------------------------

def check_empty_dirs(root: str) -> None:
    section("Empty directories")
    empty = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if not dirnames and not filenames:
            empty.append(os.path.relpath(dirpath, root))
    if empty:
        for item in empty:
            print(f"  WARN  {item} is empty and will not survive a clone")
        warnings.append(f"{len(empty)} empty director(ies)")
    else:
        print("  OK  no empty directories")


# --- 4. Language neutrality (ADVISORY) ---------------------------------------------------------

def check_neutrality(root: str, files: list[str]) -> None:
    section("Language and platform neutrality")
    pattern = re.compile("|".join(NEUTRALITY_TERMS), re.I)
    hits = []
    candidates = [f for f in files if not f.startswith(NEUTRALITY_EXEMPT)]
    for path in candidates:
        with open(os.path.join(root, path), encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                found = pattern.search(line)
                if found:
                    hits.append(f"{path}:{number} '{found.group(0)}'")
    if hits:
        for item in hits:
            print(f"  WARN  {item}")
        warnings.append(f"{len(hits)} stack-specific term(s) outside exempt paths")
        print("\n  If this project has chosen its stack, narrow NEUTRALITY_EXEMPT or drop this check.")
    else:
        print(f"  OK  {len(candidates)} files carry no stack-specific requirement")


# --- 5. Skills symlink (ADVISORY) --------------------------------------------------------------

def check_symlink(root: str) -> None:
    section("Claude Code skills symlink")
    result = subprocess.run(
        ["git", "ls-files", "-s", ".claude/skills"],
        capture_output=True, text=True, cwd=root,
    )
    output = result.stdout.strip()
    if not output:
        print("  WARN  .claude/skills is not tracked (fine if this project dropped it)")
        warnings.append(".claude/skills is not tracked")
    elif output.split()[0] == "120000":
        print("  OK  tracked as a symlink, not a copied tree")
    else:
        print(f"  WARN  .claude/skills is tracked as mode {output.split()[0]}, expected 120000")
        warnings.append(".claude/skills is a copy, not a symlink")


# --- 6. Bootstrap placeholders and project triggers (ADVISORY) -------------------------------

def check_lifecycle_markers(root: str) -> None:
    section("Bootstrap placeholders and project triggers")
    bootstrap_candidate = re.compile(rf"{BOOTSTRAP_TOKEN}\s*(?=[:\[])")
    trigger_candidate = re.compile(rf"{PROJECT_TRIGGER_TOKEN}\s*(?=[:\[])")
    bootstrap_pattern = re.compile(rf"{BOOTSTRAP_TOKEN}\s*:")
    trigger_pattern = re.compile(rf"{PROJECT_TRIGGER_TOKEN}\s+\[trigger:\s*([^\]]*)\]\s*:")
    unresolved = []
    malformed = []
    triggered = []

    for path, contents in repository_text_files(root):
        for number, line in enumerate(contents.splitlines(), 1):
            has_bootstrap_marker = bool(bootstrap_candidate.search(line))
            has_project_trigger = bool(trigger_candidate.search(line))
            if not has_bootstrap_marker and not has_project_trigger:
                continue
            if has_bootstrap_marker:
                if bootstrap_pattern.search(line):
                    unresolved.append(f"{path}:{number}")
                else:
                    malformed.append(f"{path}:{number}")
                continue
            match = trigger_pattern.search(line)
            if match and match.group(1).strip():
                trigger = match.group(1).strip()
                triggered.append(f"{path}:{number} trigger: {trigger}")
            else:
                malformed.append(f"{path}:{number}")

    for item in unresolved:
        print(f"  UNRESOLVED   {item}")
    for item in malformed:
        print(f"  MALFORMED    {item}")
    for item in triggered:
        print(f"  TRIGGERED    {item}")

    if unresolved or malformed or triggered:
        warnings.append(
            f"{len(unresolved)} unresolved bootstrap marker(s), "
            f"{len(malformed)} malformed lifecycle marker(s), and "
            f"{len(triggered)} project trigger(s)"
        )
        print(
            "\n  Resolve bootstrap and malformed markers during bootstrap; "
            "project triggers must keep their trigger."
        )
    else:
        print("  OK  no lifecycle markers")


# --- Entry point -------------------------------------------------------------------------------

def main() -> int:
    root = repo_root()
    files = markdown_files(root)

    check_links(root, files)
    check_line_budget(root)
    check_empty_dirs(root)
    check_neutrality(root, files)
    check_symlink(root)
    check_lifecycle_markers(root)

    section("Summary")
    for item in warnings:
        print(f"  advisory: {item}")
    for item in failures:
        print(f"  FAILED:   {item}")
    if not warnings and not failures:
        print("  all checks clean")

    if failures:
        print(f"\n{len(failures)} hard check(s) failed.")
        return 1
    print(f"\nHard checks passed ({len(warnings)} advisory note(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
