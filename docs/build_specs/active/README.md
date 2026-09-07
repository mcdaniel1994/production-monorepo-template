# Active Build Specifications

Draft, ready, and in-progress specifications live here. This README is the single owner of their
mutable state and implementation order; individual specification headers carry only durable facts.

## Queue

No active specifications.

When work is queued, replace that sentence with an ordered table containing `Order`, `State`,
`Spec`, `Owner`, and `Why now`. Each spec name links to its file in this directory.

States:

- **Draft** — still being shaped; not authorized for implementation.
- **Ready** — authorized and available to implement.
- **In progress** — implementation has started. Keep at most one unless the work is genuinely
  independent.

`Next` is not a state. Queue order owns priority. Reordering work changes this table, not a
specification's permanent sequence number.

On completion, follow the freeze-and-move process in [`../README.md`](../README.md#lifecycle).
