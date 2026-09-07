# `docs/standards/`

Cross-cutting standards that apply across all development.

Standards live here when they govern how multiple apps, packages, or pipelines must behave — not spec-specific scope (which lives in `docs/build_specs/`).

Standards are the evolving, authoritative engineering requirements. The trigger table in
[`AGENTS.md`](../../AGENTS.md#what-to-read-before-you-change-code) says which standard applies to
which work; see [Standards](../../AGENTS.md#standards) for how they are meant to be used.

## Index

This table is the compliance snapshot: what the bar is, which version of it applies, and whether it
is current. A `Next review` date in the past means the standard has lapsed and needs a review, not
that it stopped applying.

| Standard | Status | Ver. | Last reviewed | Scope |
|---|---|---|---|---|
| [compliance-licensing-standard.md](compliance-licensing-standard.md) | Active | 1.0 | 2026-09-03 | Dependency and license classification, attribution/notice files, third-party service and AI model/provider evaluation, and the exception path for non-permissive dependencies |
| [visibility.md](visibility.md) | Active | 1.0 | 2026-09-03 | Public-facing pages: semantic HTML, WCAG 2.2 AA, SEO, GEO, AEO, Schema.org, Core Web Vitals, bot access |
| [configuration.md](configuration.md) | Active | 1.0 | 2026-09-03 | Configuration modules, startup validation, environment variables, secret handling and rotation |
| [testing.md](testing.md) | Active | 1.0 | 2026-09-03 | Test levels, what to test, coverage policy and ratcheting, local test workflow |
| [error-handling.md](error-handling.md) | Active | 1.0 | 2026-09-03 | Error patterns, API input validation, safe error responses, database and external-service failures |

A project records which versions it was built against in
[`../context/architecture.md`](../context/architecture.md).

## Conventions

- One topic per file.
- **Every standard uses the same header and section shape.** Start from
  [`standard-template.md`](standard-template.md) — the five standards above drifted into seven
  different header formats before that template existed.
- Each standard declares its status, version, scope, and review dates in its first lines.
- **Bump `Version` only when a normative requirement changes** — never for typos or rewording. A
  bump is a claim that something real changed, and projects pin against it.
- After adding a standard, list it above **and** add its trigger to the table in
  [`AGENTS.md`](../../AGENTS.md#what-to-read-before-you-change-code). A standard nothing routes to
  will not be found.
- Reference standards from a unit's own README (a public-facing app's README pointing at `visibility.md`, for example) so contributors find them at the point of work.
- Standards link to supporting implementation files; they must not duplicate
  normative content that another standard owns — link to it instead.

## Exceptions

Standards are the default, not an absolute. To deviate:

1. State the specific standard requirement, why compliance is infeasible or counter-productive for
   this change, and the scope of the exception.
2. Propose the safest compliant alternative considered and why it was not taken.
3. Get explicit approval from the repository owner before merging.
4. Record the exception and its rationale in the change's PR/description. Where a standard defines
   its own conflict-handling path — as [visibility.md](visibility.md#before-you-start) does for
   competing requirements within its scope — follow that first.

Silent non-compliance is not an exception — it is a defect.
