# <Topic> Standard

**Status:** Draft · **Version:** 0.1 · **Last reviewed:** YYYY-MM-DD · **Next review:** YYYY-MM-DD

**Applies to:** <one line — the code and surfaces this governs>
**Does not apply to:** <one line — the nearest thing it does NOT govern, or "—">

<One paragraph: what this file is the authority on, and where it applies.>

**The goal:** <one sentence — what good looks like when this standard is followed.>

---

## Before you start

- **Read this before** <the trigger — the concrete action that brings someone here>.
- <2–5 imperative non-negotiables. The things most often got wrong.>
- Report which standards you reviewed.

**Examples:** <changes that clearly fall inside this standard>

**Non-examples:** <the nearest changes that do not, so it is not over-applied>

---

## 1. <Requirement group>

- State requirements as imperatives, not descriptions.
- Give the reason where the reason changes behavior at the margin. A rule someone understands is a
  rule they apply correctly in the case you did not anticipate.
- Link to another standard rather than restating it.

## 2. <Requirement group>

…

---

## Required Tests

What must be proven, not how to prove it. Runner-agnostic.

---

## Exceptions

Follow the exception mechanics in [`README.md`](README.md#exceptions).

---

## Writing a standard — notes for the author

Delete this section before committing.

- **Header fields are fixed.** Every standard carries the same `Status · Version · Last reviewed ·
  Next review` line and the `Applies to:` / `Does not apply to:` pair. The five existing standards
  drifted into seven different header shapes before this template existed.
- **`Does not apply to:` is the most valuable line in the file.** It is what stops a standard being
  applied where it does not belong — SEO rules on an admin dashboard, error-response rules on a
  build script.
- **Two audiences.** The header serves reviewers, contributors, and clients who need to know what
  bar the application is held to. "Before you start" serves whoever is doing the work, agent or
  human. Do not address one to the exclusion of the other.
- **Version, not just dates.** Bump `Version` only when a normative requirement changes — never for
  typos or rewording. Projects record which versions they were built against in
  `docs/context/architecture.md`, so a bump is a claim that something real changed.
- **Policy here, values elsewhere.** Thresholds, flags, and tool names belong in configuration and
  CI, not in this prose. This file should survive a change of toolchain.
- **Language-neutral.** Name no language, package manager, or framework as a requirement.
- **One owner per fact.** If another standard already says it, link to it.
- After adding a standard, list it in [`README.md`](README.md) and add its trigger to the table in
  [`../../AGENTS.md`](../../AGENTS.md) — that table is how anyone finds out this file exists.
