# Configuration & Secrets Standard

**Status:** Active · **Version:** 1.0 · **Last reviewed:** 2026-09-03 · **Next review:** 2026-12-03

**Applies to:** all code that reads an environment variable, holds a credential, connects to a
database or external service, or differs in behavior between environments.
**Does not apply to:** values that are genuinely constant across every environment — those are code,
not configuration.

This file is the authority on how units read configuration and handle secrets. It applies to every
app, service, and package in the repository, in every language.

**The goal:** a unit either starts correctly or refuses to start, never leaks a credential, and
behaves identically everywhere except for the values it is given.

---

## Before you start

- **Read this before** adding a configuration value, a credential, or an integration.
- Add every new variable to `.env.example` in the same change.
- Never commit a real secret, and never print one — not in logs, error responses, or test output.
- Report which configuration values a change introduces and where they are consumed.

**Examples:** introducing an environment variable; wiring a database or external API; changing how
a unit is configured per environment.

**Non-examples:** renaming a local variable; changing a hard-coded value that is the same in every
environment.

---

## 1. One Config Module Per Unit

- Each unit reads its environment in **exactly one module**. Everything else imports typed values
  from that module.
- Direct environment access scattered through application code is a defect. It makes the unit's real
  configuration surface impossible to determine without reading every file, and it is how required
  variables end up undocumented.
- The config module is the single place to look to answer "what does this unit need to run?"

## 2. Validate at Startup, Fail Fast

- Required configuration is validated **when the process starts**, not when a request arrives.
- A missing or malformed required value is a startup failure with a clear message naming the
  variable. Do not substitute a default and continue.
- A unit that boots with broken configuration and fails on first request has converted a deploy-time
  error into a 3am production incident. This rule exists to prevent exactly that.
- The error message names the variable and what was wrong with it. It never prints the value.

## 3. Typed and Explicit

- Every setting has a declared type and is parsed once, at the boundary. Downstream code receives a
  port as a number and a flag as a boolean, not strings.
- Non-secret settings may have safe defaults. **Secrets never have defaults** — a default credential
  is a credential that reaches production unnoticed.
- Prefer failing on an unknown or misspelled variable over silently ignoring it, where the language
  makes that practical.

## 4. `.env.example` Is Committed and Complete

- **One `.env.example` at the repository root is the default**, listing every variable any unit
  reads. A project whose units have genuinely disjoint configuration surfaces may keep one per unit
  instead — record that as a departure in [`../context/architecture.md`](../context/architecture.md).
  Either way, exactly one file is authoritative for a given variable.
- Every variable the unit reads appears in it with a placeholder or safe default and a one-line
  comment explaining it.
- A real `.env` is never committed. It is gitignored at the repository root.
- Adding a variable without adding it to `.env.example` is an incomplete change — the next person to
  clone the repository cannot start the unit.

## 5. Secrets Are Injected, Never Stored

- No secrets in the repository, in image layers, in build arguments, in CI logs, or in error
  responses. Build arguments and image layers are readable by anyone who can pull the image.
- Secrets are supplied by the runtime environment or a secrets manager, and read only through the
  config module (§1).
- Secrets never appear in logs or client-visible errors. See
  [`error-handling.md`](error-handling.md#3-safe-error-responses) for what may be returned to a
  caller.
- Where a secret must be held in memory, do not log the object holding it. Give config objects a
  representation that redacts secret fields, so an incidental log statement cannot leak one.

## 6. Configuration Varies; Code Does Not

- Environments differ by **values**, not by branches. Code that switches behavior on an environment
  name (`if env == "production"`) means the path running in production is not the path tested
  anywhere else.
- Express the difference as configuration: a feature flag, a timeout, an endpoint, a log level.
- Anything that must differ structurally between environments is an architecture decision — record
  it in [`../decisions/`](../decisions/).

## 7. Rotation and Scanning

- **Secret scanning runs in CI** on every pull request. See
  [`../../.github/workflows/`](../../.github/workflows/).
- **A secret that reaches a commit is compromised.** Rotate it. Do not merely delete the line —
  git history retains it, and on a pushed branch it has already been distributed.
- Treat a leaked credential as an incident: rotate first, then clean up, then work out how it got
  there.
- Record credential ownership and rotation procedure in [`../runbooks/`](../runbooks/) once the
  system is deployed.

---

## Required Tests

- A unit fails to start when a required variable is missing, with an error naming the variable.
- Malformed values (a non-numeric port, an invalid URL) are rejected at startup.
- No configuration object serializes a secret into a log line or an error response.

---

## Exceptions

Follow the exception mechanics in [`README.md`](README.md#exceptions).
