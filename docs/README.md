# `docs/`

Documentation that does not belong next to a single unit. Each subdirectory answers a different
question, and keeping them separate is what stops any one of them from becoming a dumping ground.

| Path | Answers | Lifespan |
|---|---|---|
| [`context/`](context/) | What is this product, and how is this project shaped? | Long-lived; edited when the product or architecture changes |
| [`standards/`](standards/) | How must code behave? | Long-lived; invariant across projects built from this template |
| [`decisions/`](decisions/) | Why did we choose this? | Permanent and append-only |
| [`build_specs/`](build_specs/) | What should be built? | Active until implemented; retained frozen in `completed/` |
| [`runbooks/`](runbooks/) | How do we operate and debug it in production? | Tracks the running system |
| [`journal.md`](journal.md) | What did we learn building this? | Permanent and append-only |

Documentation about *a specific unit* — how to run it, how to test it, what it does — lives in that
unit's own `README.md`, not here. It stays accurate because it is updated by the same change that
invalidates it.

The repository map lives in [`../AGENTS.md`](../AGENTS.md) and only there.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`decisions/`](decisions/).
