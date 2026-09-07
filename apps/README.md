# `apps/`

Deployable, user-facing surfaces — a public website, a back-office or admin UI, an authenticated
product UI. Each app is a self-contained unit with its own dependencies, tests, README, and
Dockerfile.

Shared code that more than one unit imports belongs in [`../packages/`](../packages/), not here.

Where an ambiguous unit belongs — a full-stack framework app doing real server-side work, a
backend-for-frontend, a unit that is both UI and API — is a judgment call for the project, not a
rule this repository imposes. Decide it deliberately and record the reasoning.

## Each app provides

- A `README.md` saying what it is, how to run it, and how to test it.
- A `Dockerfile`, so the unit can run alongside the rest of the stack locally and in deployment.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../docs/decisions/`](../docs/decisions/).
