# `packages/`

Shared libraries imported by units in [`../apps/`](../apps/) and [`../services/`](../services/).
Nothing here deploys on its own — a package with a deploy target is a service.

Extract a package when two units genuinely need the same code. Extracting earlier than that trades a
small duplication for a coupling that is harder to undo.

## Each package provides

- A `README.md` saying what it is, what depends on it, and how to test it.
- Its own tests. A shared package is the code most expensive to get wrong, because a defect reaches
  every consumer at once.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../docs/decisions/`](../docs/decisions/).
