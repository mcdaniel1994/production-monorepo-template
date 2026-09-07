# Security Policy

> **BOOTSTRAP_PLACEHOLDER:** Fill in the contact and support window, then delete this block.
>
> This file ships with the repository template. The practices below are real and apply as written;
> only the reporting contact and the supported-versions table need this project's specifics.

## Reporting a vulnerability

**Do not open a public issue for a security vulnerability.** Report it privately:

- Preferred: GitHub's private vulnerability reporting (Security tab → Report a vulnerability).
- Alternative: `<security contact — fill in during bootstrap>`.

Include what you found, how to reproduce it, and what an attacker could do with it. You will get an
acknowledgement within `<N>` business days.

Please give us a reasonable window to ship a fix before disclosing publicly. We will credit you when
the fix ships, unless you would rather stay anonymous.

## Supported versions

| Version | Supported |
|---|---|
| | |

## What we commit to

- **Secret scanning runs on every pull request.** See [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
- **A leaked credential is rotated, not deleted.** Git history keeps it, and on a pushed branch it
  has already been distributed. See
  [`docs/standards/configuration.md`](docs/standards/configuration.md#7-rotation-and-scanning).
- **Errors never leak internal detail** — no stack traces, queries, tokens, or secrets in a
  client-visible response. See
  [`docs/standards/error-handling.md`](docs/standards/error-handling.md#3-safe-error-responses).
- **Dependencies are classified before adoption**, not after. See
  [`docs/standards/compliance-licensing-standard.md`](docs/standards/compliance-licensing-standard.md).

## Reporting something already committed

If you find a secret in this repository's history, treat it as compromised and say so immediately —
rotation comes first, cleanup second, and working out how it got there last.
