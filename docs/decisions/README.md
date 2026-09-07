# `docs/decisions/`

Architecture Decision Records — the durable answer to "why is it like this?"

An ADR captures one decision: the situation that forced it, what was chosen, what that costs, and
what else was considered. It is dated, and it is **never rewritten**. A decision that no longer
holds is marked superseded and linked forward to the one that replaced it. That is what makes this
directory trustworthy: reading it tells you not just what is true now, but what was believed then
and why it changed.

## Why this directory exists

The structure in this repository is a set of defaults, not a set of laws. A contributor or agent who
concludes that a different architecture fits this project better has a third option besides
restructuring silently and staying stuck: write an ADR, get it approved, and the deviation becomes a
recorded decision that every future reader inherits.

Departing from the defaults is expected. Departing without leaving a trace is not.

## When to write one

Write an ADR for any decision that constrains future work:

- Language, runtime, framework, or package manager
- Deployment target and environment topology
- Data store, schema-migration approach, or retention policy
- Authentication and authorization approach
- Inter-service communication patterns
- **Any departure from this repository's default structure**
- Adopting a dependency with a significant lock-in cost

Do not write one for a decision that is cheap to reverse. If changing your mind later costs an
afternoon, just change your mind later.

## Format

Copy [`adr-template.md`](adr-template.md) and name the file `NNNN-short-slug.md`, numbering
sequentially from `0001` and never reusing a number.

Statuses: **Proposed** → **Accepted** → **Superseded by [NNNN]** (or **Rejected**, which is worth
keeping — a recorded rejection stops the same idea being relitigated every six months).

## Rules

1. **Append-only.** Never edit the Context, Decision, or Consequences of an accepted ADR. Correcting
   a typo is fine; revising the reasoning is not.
2. **Supersede, don't delete.** Set the old ADR's status to superseded, link to the new one, and
   link back.
3. **One decision per record.** Two decisions in one ADR cannot be superseded independently.
4. **Write the consequences honestly, including the bad ones.** An ADR listing only benefits is
   marketing, and the next reader can tell.
5. **Link from [`../context/architecture.md`](../context/architecture.md)** so the present-tense
   description points at the reasoning.

## After one is accepted

An ADR reaching **Accepted** is a good moment for a journal entry — see
[`../journal.md`](../journal.md). The ADR records the decision; the journal records what the ADR
deliberately strips out, which is the half you will not remember in six months. Optional, and never
written on your behalf.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision here.
