# <Symptom, worded the way the reader encounters it>

**Applies to:** <which unit or surface>
**User impact:** <what is broken for people while this is happening>
**Escalate to:** <who, and after how long>
**Last verified:** YYYY-MM-DD — <who walked it>

---

## Symptom

What brought the reader here: the alert text, the error message, the shape of the graph. Describe it
as it actually appears, not as the system is organised internally.

## Before you start

- Access or credentials needed, and where to get them.
- Anything that makes this worse if done out of order.
- Whether it is safe to proceed alone or someone should be paged first.

## Diagnose

Ordered checks that narrow the cause. For each one give the command **and what a healthy result
looks like**, so the reader can tell whether to continue or branch.

1. `<command>` — healthy: `<what good output looks like>`. If not, go to step `<N>`.

## Fix

Ordered steps with concrete commands. Say what has changed after each one.

1. `<command>` — expected: `<result>`

## Verify

How to confirm it is genuinely fixed, checked from the user's side rather than the system's.

## If this does not work

The escalation point: who to contact, what to tell them, and what *not* to try next.

## Afterwards

- What to record, and where.
- Whether this needs an ADR, a code change, or a correction to this runbook.
- If the cause was novel, add it to **Diagnose** so the next reader finds it faster.

---

## Notes for the author — delete this section before committing

- **Name the file after the symptom, not the subsystem.** The reader knows what they are seeing;
  they do not yet know what is broken.
- **One scenario per file.** A runbook covering three failures gets read during none of them.
- **Concrete commands, not an approach.** "Restart the worker" is not a step.
- **State what healthy looks like at each step**, or the reader cannot tell whether to continue.
- **Prefer accuracy over completeness.** A stale runbook is worse than none, because it is trusted.
- Re-verify on a cadence and update `Last verified` — see
  [`maintenance-calendar.md`](maintenance-calendar.md).
