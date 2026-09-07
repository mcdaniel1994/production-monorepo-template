# Error Handling Standard

**Status:** Active · **Version:** 1.0 · **Last reviewed:** 2026-09-03 · **Next review:** 2026-12-03

**Applies to:** all code that validates input, talks to storage, calls another service, or returns
errors to a caller or UI.
**Does not apply to:** build scripts and local developer tooling, where a loud stack trace is the
correct outcome.

This file is the authority on how code handles failure — input validation, error responses, and
failures from databases and external services. It applies across every service, package, and app.

**The goal:** fail predictably, never leak sensitive detail, and give callers an actionable, safe
response.

---

## Before you start

- Read this file before adding or changing an API, a validation path, a persistence call, or any
  failure path.
- For every new behavior, handle and test the failure paths, not only the success path.
- Never expose internal detail (stack traces, queries, secrets, raw exceptions) in a response or
  client-visible error.
- Report which standards you reviewed.

**Examples:** adding an API route or changing its validation; calling an external service or
database; changing what a failure returns to a caller.

**Non-examples:** pure presentation changes with no failure path; formatting-only changes.

---

## 1. Error-Handling Patterns

- **Use typed domain exceptions**, then translate them at the boundary.
- **Catch narrowly.** Catch the specific exception you can handle; let unexpected errors propagate
  to a single boundary handler that returns a safe generic response and logs the detail server-side.
- **No silent failures.** Never swallow an exception without either handling it meaningfully or
  logging it. An empty `except`/`catch` is a defect.
- **Fail closed on security decisions.** When authorization or validation is uncertain, deny.

## 2. API Input Validation

- Validate at the boundary before doing work, using the unit's schema-validation mechanism. A
  request is either fully validated or rejected before any side effect occurs.
- Validate at every boundary a request crosses, not only the outermost one. A UI validating input
  does not excuse the service behind it from validating the same input.
- Reject invalid input with a clear, field-level message and the correct status code (`422`/`400`).
  Do not partially process invalid requests.
- Treat all client input as untrusted, including headers and IDs from authenticated callers.

## 3. Safe Error Responses

- **Map errors to correct status codes:** `400/422` invalid input, `401` unauthenticated, `403`
  unauthorized, `404` not found, `409` conflict/duplicate, `500` unexpected. `5xx` is for *our*
  faults, not the caller's.
- **Generic outward, detailed inward.** Return a stable, non-revealing message to the caller; log
  the full detail server-side with enough context to debug.
- **No sensitive data in responses or error bodies:** no secrets, tokens, password material, full
  PII, internal paths, queries, or stack traces.
- **Do not enable enumeration.** Where a response could reveal whether an account, record, or
  resource exists, return an identical response either way — same status, same message, and
  comparable timing. "Unknown email" and "wrong password" are the same response; a password-reset
  request answers the same regardless of whether the account exists.

## 4. Database & Storage Failures

- Assume storage can fail or be unavailable. Wrap storage calls so a failure becomes a typed error,
  not a leaked driver exception.
- Keep writes consistent: validate first, then write; avoid partial multi-step writes without a
  recovery path.
- Surface storage failures as `503`/`500` with a safe message; log the cause server-side.

## 5. External-Service Failures

- **Set timeouts** on every outbound call. A missing timeout is a defect.
- **Decide the failure mode explicitly:** retry (with backoff, only for idempotent calls), fall back
  to a safe default, or fail fast — and document which, in code.
- **Isolate the blast radius.** A dependency being down should degrade one feature, not crash the
  service. Do not let an external failure surface as an unhandled `500` with internal detail.
- Log the dependency, the operation, and the outcome (not the payload) for diagnosis.

---

## Required Tests

For each handled failure path, add a test that asserts the status code, the safe (non-leaking)
message, and that no sensitive data appears in the response or logs.

---

## Exceptions

Follow the exception mechanics in [`README.md`](README.md#exceptions).
