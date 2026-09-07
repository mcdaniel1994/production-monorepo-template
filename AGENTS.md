# AGENTS.md

## What this is

> **BOOTSTRAP_PLACEHOLDER:** Replace the identity paragraph below during bootstrap.

This repository is a **language-neutral monorepo template** for production full-stack applications.
It ships structure, standards, and agent instructions — no application code. See `BOOTSTRAP.md` for
the one-time setup. Depth lives in `docs/context/product.md`; this file is the map.

## Start here

**Read this file first, in full.** Agents following the `AGENTS.md` convention read it natively.
Claude Code auto-loads only `CLAUDE.md`, which points here, and a `SessionStart` hook in
`.claude/settings.json` injects this file so it is not left to chance.

**Line budget: 150.** This is the only file loaded into every agent session, so it stays scannable —
depth belongs in the files it routes to. CI checks this number by reading it from this sentence, so
a project that genuinely needs more edits it here and the check follows.

Nothing else loads automatically. Everything below is read on demand:

- Read a directory's `README.md` before working in that directory.
- Read a standard when the table below says your work touches it.
- Read `docs/context/` when you need the *why* behind a decision.
- Read the relevant `docs/build_specs/` entry when implementing a specced change.
- When a skill is explicitly invoked — or its own instructions permit automatic use — read its
  `SKILL.md` in full before acting.
- Read the existing implementation before changing it.

## What to read before you change code

Match what you are about to do against this table and read that standard before planning. Do not
read them all — the triggers exist so you carry only what the task needs.

| If you are touching | Read |
|---|---|
| A dependency, lockfile, license, third-party service, or AI provider | `docs/standards/compliance-licensing-standard.md` |
| A public-facing page, metadata, sitemap, or `robots.txt` | `docs/standards/visibility.md` |
| Config, environment variables, or secrets | `docs/standards/configuration.md` |
| APIs, validation, persistence, or failure paths | `docs/standards/error-handling.md` |
| Any behavior change | `docs/standards/testing.md` |

More than one row can apply. This table is a terse index; each standard defines its own scope in its
first lines, and where the two disagree, **the standard wins**.

## Repository map

This is the only place in the repository that enumerates the top-level directories.

| Path | Contains |
|---|---|
| `apps/` | Deployable user-facing surfaces — public site, back-office, admin UI |
| `services/` | Backend units — APIs, workers, scheduled jobs, data pipelines |
| `packages/` | Shared libraries imported by other units; nothing that deploys on its own |
| `infra/` | Infrastructure-as-code. Empty until a deployment platform is chosen |
| `.agents/skills/` | Reusable coding-agent workflows. Canonical location — edit here |
| `.claude/` | Claude Code specifics only: the `SessionStart` hook that injects this file, and `skills` — a symlink to `.agents/skills`, not a second copy |
| `.github/workflows/` | CI. Secret scanning and the template invariant checks are live; lint/test/build are bootstrap placeholders |
| `.github/scripts/` | Tooling the CI workflows run. Repository maintenance only — never product code |
| `docs/context/` | What the product is and how this project is shaped |
| `docs/standards/` | How code must behave. Invariant across projects |
| `docs/decisions/` | ADRs — why we chose this. Append-only |
| `docs/build_specs/` | Active work and completed specifications, separated by lifecycle |
| `docs/runbooks/` | How to operate and debug the running system |

Each unit owns its README, tests, and Dockerfile. There is no root `compose.yaml` yet — create one
when the first unit lands, since a compose file with no services fails on `docker compose up`.

## Rules of engagement

- **Stop and ask rather than invent.** When intent is unclear, ask. A wrong guess that looks
  confident costs more than a question.
- **Do not add a dependency** without following `docs/standards/compliance-licensing-standard.md`.
  Copyleft, non-commercial, custom-licensed, and unlicensed dependencies need owner approval
  *before* adoption.
- **Tests change with behavior**, in the same change. Cover the failure paths.
- **Never commit a secret**, and never log or return one. A leaked credential is rotated, not
  deleted — git history keeps it.
- **When project needs conflict with structural defaults, project needs win.** Record the departure
  as an owner-approved ADR.
- **When an applicable engineering standard cannot be followed**, use its exception and approval
  path in `docs/standards/README.md#exceptions`.
- **Update what your change invalidates.** A unit README or `docs/context/architecture.md` left
  describing the old state means the change is not finished.
- **Clean up resolved provisional state.** When resolving a deferred decision or replacing a
  placeholder, update or remove its provisional language and tracking entry in the same change.
- **Report which standards you reviewed** and what you changed.
- **Placeholder files declare themselves.** A file whose opening block says it is a bootstrap
  placeholder contains no real content — do not treat it as fact. The one exception is `LICENSE`,
  which ships empty because an empty file cannot declare anything; until it is filled, treat this
  repository's code as all-rights-reserved.
- **Project triggers are not bootstrap leftovers.** `PROJECT_TRIGGER` marks localized work that
  becomes due only when its named event occurs; complete and remove it when that trigger fires.

## Architecture is a default, not a law

The structure above is a starting convention. If a different shape genuinely fits a project better,
that is a legitimate conclusion — say so rather than conforming silently or stalling.

The way to act on it is an ADR in `docs/decisions/`, approved by the repository owner. Every
directory README repeats this. Departing from the defaults is expected; departing without leaving
the reasoning behind is not.

## Standards

`docs/standards/` holds the authoritative engineering requirements. They serve two audiences at
once: whoever is doing the work — agent or human — who must read the applicable standard before
planning; and reviewers, contributors, and clients, who need to know what bar the application is
held to.

- Each standard declares its **status, version, review date, and scope** in its first lines. Reading
  the first fifteen lines is enough to know whether it applies and what it demands.
- Standards evolve as technology, official guidance, and production needs change. `Version` is
  bumped only when a normative requirement changes — so a project can record which versions it was
  built against in `docs/context/architecture.md`.
- Deviating requires the exception path in `docs/standards/README.md#exceptions`. Silent
  non-compliance is not an exception — it is a defect.
- Add a new standard from `docs/standards/standard-template.md`, then add its trigger to the table
  above. A standard nothing routes to will not be found.

Standards and durable `.agents/` assets are **invariant** across projects built from this template.
A project that needs to deviate records it in `docs/context/` or an ADR rather than editing them, so
improved standards can be copied forward later. A workflow that identifies itself as temporary is
removed only at the lifecycle boundary it declares.

## Coding-agent infrastructure vs. product agents

`.agents/` holds configuration for the coding agents that **maintain** this repository — reusable
workflows about how to work here.

AI agents that are **part of the product** are application code. They live in the `apps/`,
`services/`, or `packages/` unit they belong to, and are governed by the same standards as any other
code. The two must never be mixed: product behavior does not belong in `.agents/`, and repository
conventions do not ship to users.

Agent-specific entry points (`CLAUDE.md`, and any equivalent) are **pointers to this file and
nothing else**. Instruction content placed in one of them is invisible to every other agent.
