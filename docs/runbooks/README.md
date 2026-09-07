# `docs/runbooks/`

Operational procedures for the running system: how to deploy, how to roll back, what to check when
something is wrong, and how to recover from the failures that are known to happen.

**Incident runbooks are empty by design.** They describe a specific deployed system, and no
deployment target is selected yet — see [`../../infra/README.md`](../../infra/README.md). Write them
as the system becomes real.

Two files ship regardless, because neither needs a platform to be true:

| File | Purpose |
|---|---|
| [`runbook-template.md`](runbook-template.md) | Start here when writing one |
| [`maintenance-calendar.md`](maintenance-calendar.md) | Recurring obligations the standards already impose |

## Runbooks this system will owe

Not a checklist to complete now — a list of what to write as each becomes real. Every one is
traceable to a document that already assumes it exists.

| Runbook | Owed to |
|---|---|
| Deploy and roll back | [`deploy.yml`](../../.github/workflows/deploy.yml) — "document the rollback procedure before the first production deploy" |
| Rotate a credential | [configuration §7](../standards/configuration.md#7-rotation-and-scanning) — "record credential ownership and rotation procedure in runbooks" |
| Respond to a leaked secret | [configuration §7](../standards/configuration.md#7-rotation-and-scanning) and [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) both say rotate first; neither says how |
| A unit will not start | [configuration §2](../standards/configuration.md#2-validate-at-startup-fail-fast) makes this a designed failure naming the variable |
| A dependency is down or degraded | [error-handling §5](../standards/error-handling.md#5-external-service-failures) |
| Storage is failing | [error-handling §4](../standards/error-handling.md#4-database--storage-failures) |
| A certificate or domain is expiring | any public surface under [visibility](../standards/visibility.md) |
| Restore from backup | nothing yet — see [known gaps](maintenance-calendar.md#known-gaps) |

The first two are the most overdue: both are promises made in writing by files that ship today.

## What makes a runbook useful

A runbook is read by someone under time pressure who may not have built the thing. That constrains
the format more than most documentation:

- **One scenario per file**, named after the symptom, not the subsystem — the reader knows what they
  are seeing, not what is broken.
- **Ordered steps with concrete commands**, not prose describing an approach.
- **Say what a healthy result looks like** at each step, so the reader knows whether to continue.
- **State the escalation point** — when to stop and get help rather than trying the next thing.
- **Prefer accuracy over completeness.** A short runbook that is true beats a thorough one that has
  drifted; a stale runbook is worse than none, because it is trusted.

Design and architecture rationale belongs in [`../decisions/`](../decisions/). This directory is
for what to *do*.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../decisions/`](../decisions/).
