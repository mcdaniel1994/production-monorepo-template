# `docs/context/`

The durable "what" and "why" of this project: what the product is, who it serves, and how this
particular repository ended up shaped the way it is.

**This directory is not session context.** [`../../AGENTS.md`](../../AGENTS.md) is the only file
loaded automatically into an agent session. These files are the overflow for depth that does not fit
in a hundred-line map, read on demand when an agent needs the reasoning behind a decision rather
than the decision itself.

The two files below ship as placeholders. Product context is filled as part of Bootstrap core;
architecture is filled in stages, beginning with template lineage, standards applicability, and
explicitly deferred decisions — see [`../../BOOTSTRAP.md`](../../BOOTSTRAP.md). This table is not a
closed list: add a focused context document when coherent source material deserves to stay whole.

| File | Contents |
|---|---|
| [`product.md`](product.md) | What the product is, who uses it, what success looks like, and the domain glossary |
| [`architecture.md`](architecture.md) | Template lineage, standards applicability, open decisions, and how this project is shaped today |

## What belongs here, versus elsewhere

- **How code must behave** → [`../standards/`](../standards/)
- **What is in a directory** → that directory's own `README.md`
- **Why we chose something** → [`../decisions/`](../decisions/)
- **What to build next** → [`../build_specs/`](../build_specs/)
- **What the product is and how this repo is shaped** → here

## Keeping these honest

These are the files most likely to rot, because nothing breaks when they go stale. Two habits keep
them useful:

- **Describe current state.** `architecture.md` says how things *are*. Template lineage is current
  provenance metadata; historical reasoning and alternatives live in ADRs, which are dated and
  never edited.
- **Update them in the change that invalidates them.** A restructuring that leaves `architecture.md`
  describing the old shape is not finished.

Keep each file short. A context file nobody finishes reading provides no context. When source
material is too large to inline, preserve it intact and add a concise summary plus a pointer here or
in the closest context file. State what the summary leaves out.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../decisions/`](../decisions/).
