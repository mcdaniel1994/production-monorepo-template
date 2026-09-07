# Maintenance Calendar

> **BOOTSTRAP_PLACEHOLDER:** Assign owners during bootstrap, then delete this block.
>
> The obligations below become binding when their source standard applies and their gate is open.
> Only the Owner column is empty, because a template cannot know who you are.

Recurring obligations gathered in one place. This file **schedules** them; it does not invent or own
them. Every row cites the document that imposes it, and that document stays the authority. The Gate
column keeps an obligation dormant until the project condition that makes it relevant exists.

## Why this exists

These obligations were spread across five documents, so in practice none of them fired. The most
visible symptom: **all five standards carry `Next review: 2026-12-03`.** They lapse on the same day,
and nothing currently notices.

An unowned row does not happen. Filling the Owner column is what turns this from a list into a
calendar.

## Cadence

| Cadence | Obligation | Source | Gate | Owner |
|---|---|---|---|---|
| Monthly | Organic traffic, queries and CTR, indexing status, Core Web Vitals | [visibility §11](../standards/visibility.md#11-measurement--review-cadence) | Public surface exists | |
| Quarterly | Review each standard; a `Next review` date in the past means it has lapsed, not that it stopped applying | [standards/README](../standards/README.md) | At least one standard is Applicable or Conditional | |
| Quarterly | AI citation tracking, schema validation, crawler access, content older than 12 months | [visibility §11](../standards/visibility.md#11-measurement--review-cadence) | Public surface exists | |
| Quarterly | Training-crawler access policy — a per-project decision, re-taken deliberately | [visibility §8](../standards/visibility.md#8-machine-readable-discovery--crawler-access) | Public surface exists | |
| Quarterly | Restore from backup and time it. An untested backup is a hypothesis | *see gap below* | Persistent product data exists | |
| Quarterly | Access review — who can reach production, and should they still | *see gap below* | Production access exists | |
| Annually | Full dependency and license audit: all manifests, transitive trees, `THIRD_PARTY_LICENSES.md` reconciliation | [compliance §Supply-Chain Baseline](../standards/compliance-licensing-standard.md#supply-chain-baseline) | Recordable third-party items exist | |
| Annually | Full visibility audit and competitive analysis | [visibility §11](../standards/visibility.md#11-measurement--review-cadence) | Public surface exists | |
| Per release | Vulnerability audit; address or consciously accept every finding, and record what was accepted | [compliance §Supply-Chain Baseline](../standards/compliance-licensing-standard.md#supply-chain-baseline) | A release contains third-party dependencies | |
| Per release | Re-verify the runbooks this release invalidated | [README](README.md) | A release invalidates a runbook | |
| Triggered | Major platform change, traffic or citation drop, structural issue, new public surface | [visibility §11](../standards/visibility.md#11-measurement--review-cadence) | Public surface exists | |

Reconcile this table with [`architecture.md#standards`](../context/architecture.md#standards):

- Remove obligations sourced only from a standard marked Not applicable.
- Keep an obligation from a Conditional standard dormant under the same trigger.
- When a trigger fires, mark the standard Applicable and activate its rows in the same change.

## Known gaps

Two rows above cite no standard because none exists yet:

- **Backup, retention, RPO and RTO.** Nothing in this repository currently states them. The data
  store ADR is the place to decide them. Until then, track the deferral in
  [`architecture.md#open-decisions`](../context/architecture.md#open-decisions).
- **Access review.** No standard governs who holds production credentials or how often that is
  re-examined. Worth an ADR once a platform exists.

## Upstream template drift

This project's source template and commit are recorded in
[`architecture.md#template-lineage`](../context/architecture.md#template-lineage). Nothing compares
the two automatically, so improvements made upstream never arrive on their own.

Once or twice a year, check whether the template has moved: compare the recorded commit against the
template repository, and look at whether any standard's `Version` was bumped. A bump is a claim that
a normative requirement changed, so adopting it may be real work — record the new version in
[`../context/architecture.md`](../context/architecture.md) when you take it.

This is the mechanism that makes the invariance rule pay off. Without it, "don't edit the standards
locally so improvements can be copied forward" is a cost with no benefit.
