# Testing Standard

**Status:** Active · **Version:** 1.0 · **Last reviewed:** 2026-09-03 · **Next review:** 2026-12-03

**Applies to:** all production code, in every language — units under `apps/`, `services/`, and
`packages/`.
**Does not apply to:** throwaway scripts and scratch tooling that ship to no one.

This file is the authority on how code is tested — what kinds of tests to write, what coverage is
expected, and the workflow for running tests locally. It governs the *policy* (what and why);
concrete enforcement values (exact thresholds, runner flags) live in each unit's test configuration
and in CI — see [Coverage policy](#3-coverage-policy) and
[`../../.github/workflows/`](../../.github/workflows/).

**The goal:** when behavior changes, tests change with it — and a passing suite means the failure
paths work, not just the happy one.

---

## Before you start

- Read this file before planning or implementing a change that adds or alters behavior.
- Add or update tests in the same change as the behavior — never defer them.
- Cover both the success path and the failure paths (see [error-handling.md](error-handling.md)).
- Preserve or improve existing coverage; do not remove tests to make a change pass.
- Report which standards you reviewed and what tests you added or changed.

**Examples:** adding or changing a route, a validation path, or a shared package's public function;
fixing a bug.

**Non-examples:** formatting-only changes; renaming a variable with no behavior change; editing
documentation.

---

## 1. Test Levels

Write the cheapest test that meaningfully exercises the behavior; add higher levels when the risk
warrants it.

- **Unit** — pure logic, validation, mappers, single functions/classes in isolation. Fast, no I/O.
- **Integration** — a route or service method against its real collaborators (repository, storage,
  validation). The default level for API endpoints.
- **End-to-end (e2e)** — a user-visible flow exercised through a running app.
  Reserve e2e for critical journeys; do not duplicate logic already covered by unit/integration tests.

## 2. What Must Be Tested

- Every new or changed public function, route, or component behavior.
- Every failure path the code deliberately handles: validation rejection, not-found, auth failure,
  duplicate, external/database failure, timeout.
- Security-sensitive behavior: that secrets/tokens are **not** logged or returned.
- Regression: when fixing a bug, first add a test that fails for that bug.

## 3. Coverage Policy

- **Default expectation:** meaningful coverage of new and changed code — branches and error paths,
  not just the happy line. Coverage is a floor, not a goal; a green number with untested failure
  paths is not "done."
- **Ratcheting:** coverage should not regress. A change that lowers overall or per-package coverage
  needs a stated reason in the PR. Raise the floor opportunistically; never lower it silently.
- **Where the numbers live:** exact percentage thresholds and gating belong in test configuration
  and the CI workflow ([`../../.github/workflows/`](../../.github/workflows/)), not hard-coded in this prose, so
  policy and enforcement evolve independently. As of this writing no automated coverage gate is
  wired; until it is, reviewers enforce this policy manually.

## 4. Running Tests Locally

This repository does not prescribe a test runner or a task runner — those are per-project choices.

- **Each unit documents its own commands in its `README.md`**: how to install, run, test, and lint
  it. That README is the authority, because it sits next to the configuration it describes and is
  updated by the same change.
- **The project records its toolchain** in [`../context/architecture.md`](../context/architecture.md).
- **Before considering a change complete**, run that unit's tests, its linter, and its build. A
  change that passes tests but does not build is not done.

If a unit's README does not document how to test it, that is a defect in the unit — fix it as part
of the change.

## 5. Test Quality

- Tests assert behavior and contracts, not implementation details.
- Each test fails for exactly one reason; name it after the behavior under test.
- Use fixtures and factories over copy-pasted setup, following the shared-setup pattern each unit
  already establishes.
- Never test against real secrets, production data, or sensitive datasets — use safe fixtures and aggregate-only outputs.

---

## Exceptions

Follow the exception mechanics in [`README.md`](README.md#exceptions).

