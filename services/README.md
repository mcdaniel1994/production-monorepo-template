# `services/`

Backend units: APIs, workers, scheduled jobs, and data pipelines. Each service is a self-contained
unit with its own dependencies, tests, README, and Dockerfile.

A data or ETL pipeline is a service — it has dependencies, tests, a runtime, and a deploy target.
It does not need a separate top-level home.

Shared code that more than one unit imports belongs in [`../packages/`](../packages/). User-facing
surfaces belong in [`../apps/`](../apps/), though see that directory's note on ambiguous units.

## Each service provides

- A `README.md` saying what it is, how to run it, and how to test it.
- A `Dockerfile`, so the unit can run alongside the rest of the stack locally and in deployment.
- A health endpoint or equivalent liveness signal, per [`../docs/standards/error-handling.md`](../docs/standards/error-handling.md).
  It reports build provenance as well — the commit, the build time, the image digest. See
  [`../infra/README.md`](../infra/README.md).
- Configuration through a single config module, per [`../docs/standards/configuration.md`](../docs/standards/configuration.md).

## Scheduled jobs

**A recurring job that touches product data is a service, not a script.** It belongs in the unit
that owns the data it operates on — the one holding that schema and its migrations — where it
inherits that unit's tests, container, config module, and error handling.

| The work | Where it lives |
|---|---|
| Touches product data — pruning, backfills, rollups | A job in the service that owns that data |
| Touches only the repository — link checks, audits, reminders | CI, in `.github/` |
| A human runs it during an incident | The command ships in the unit; the runbook invokes it |

There is deliberately no root `scripts/` directory. A directory that cannot say what does *not* go
in it becomes a junk drawer, and it would be the first thing here to quietly pick a language.

**The scheduler triggers; it never contains the logic.** Keeping the work inside the unit's
container is what makes it tested, versioned, and rolled back with everything else. On most
platforms the platform's own scheduler beats a CI cron — it runs inside the network boundary, needs
no long-lived cloud credentials held by a CI provider, and does not make data pruning depend on that
provider being up. Record the choice as an ADR.

Whatever runs it, a scheduled job needs idempotency (at-least-once is the only guarantee any
scheduler earns), a bounded blast radius that fails loudly at its cap rather than quietly deleting a
million rows, a dry run used for the first production execution, a concurrency guard so run N+1
cannot overlap N, explicit timeouts, and **an alert on absence rather than only on failure** — a job
that silently stops is worse than no job, because you believe it ran.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../docs/decisions/`](../docs/decisions/).
