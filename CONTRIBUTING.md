# Contributing

Applies to human contributors and AI coding agents alike. Agents should start with
[`AGENTS.md`](AGENTS.md), which carries the repository map and the reading triggers.

## Before you start

1. Read [`AGENTS.md`](AGENTS.md) for the repository map and the rules of engagement.
2. Read the `README.md` of the directory you are working in.
3. Match your work against the trigger table in [`AGENTS.md`](AGENTS.md) and read the applicable
   standard in [`docs/standards/`](docs/standards/) before you start.

## Branches and commits

- Work on a branch. Do not commit directly to `main`.
- Write commit messages in the imperative mood, explaining *why* rather than restating the diff.
  The diff already says what changed.
- Keep a commit to one logical change. A commit that has to be described with "and" is usually two.

## What a complete change includes

- **Tests, in the same commit as the behavior.** Cover the failure paths, not just the happy path.
  See [`docs/standards/testing.md`](docs/standards/testing.md).
- **Documentation updated where it is now wrong.** If a change invalidates a unit's README or
  [`docs/context/architecture.md`](docs/context/architecture.md), updating it is part of the change,
  not a follow-up.
- **New configuration added to [`.env.example`](.env.example).** See
  [`docs/standards/configuration.md`](docs/standards/configuration.md).
- **The unit's tests, linter, and build run clean.** A change that passes tests but does not build
  is not done.
- **A note of which standards you reviewed**, in the pull request description.

## Structural and architectural changes

Changing how the repository is organized, adopting a framework, choosing a platform, or departing
from a convention in a directory README requires an **ADR** in
[`docs/decisions/`](docs/decisions/), approved before merge.

Departing from the defaults is expected and legitimate. Departing silently is not — the next
contributor inherits the structure without the reasoning.

## Dependencies

Adding, upgrading, or replacing a dependency is governed by
[`docs/standards/compliance-licensing-standard.md`](docs/standards/compliance-licensing-standard.md).
Strong-copyleft, non-commercial, custom-licensed, and unlicensed dependencies need repository-owner
approval **before** adoption, not after.

## Deviating from a standard

Standards are the default, not an absolute. The exception path is defined in
[`docs/standards/README.md`](docs/standards/README.md#exceptions): state the requirement, why
compliance is infeasible here, the safest alternative you considered, get explicit approval, and
record the rationale.

Silent non-compliance is not an exception — it is a defect.

## Secrets

Never commit a secret. If one reaches a commit, treat it as compromised: **rotate it first**, then
clean up. Deleting the line does not help — git history retains it, and on a pushed branch it has
already been distributed.
