# `.agents/`

Coding-agent configuration for maintaining the repository.

This folder holds the reusable workflows that coding agents (Claude, Codex, and others) apply when
working in this repo. It is agent-neutral: nothing here is specific to one tool.

Engineering requirements are **not** here — they live in
[`../docs/standards/`](../docs/standards/), and [`../AGENTS.md`](../AGENTS.md) carries the trigger
table that says which standard applies to which work.

## Contents

- [`skills/`](skills/) — reusable coding-agent workflows for recurring repository maintenance tasks.
  See [`skills/README.md`](skills/README.md) for the catalog.

## How to use

- Use a skill in `skills/` when it fits the task, and follow its workflow end to end.
- Keep this folder focused on coding-agent behavior for maintaining this repo. AI agents that are
  part of the product are application code and belong in the unit they ship with — see
  [`../AGENTS.md`](../AGENTS.md).

## How agents get their instructions

Not evenly, and the file should say so rather than imply parity:

- **Claude Code** auto-loads only `CLAUDE.md`, which is a pointer. A `SessionStart` hook in
  `.claude/settings.json` injects `AGENTS.md` so it loads deterministically rather than on trust.
- **Codex, Cursor, and others following the `AGENTS.md` convention** read that file natively.
- Everything beyond it — directory READMEs, standards, context — is read on demand by every agent,
  triggered by the tables in `AGENTS.md`.

## Invariance

The durable contents of this directory and
[`../docs/standards/`](../docs/standards/) are meant to be identical across every project built from
this template. A project that needs to deviate records it in `docs/context/` or an ADR rather than
editing these files, so improvements can be copied forward later. A workflow that explicitly
identifies itself as temporary is removed only at the lifecycle boundary it declares.
