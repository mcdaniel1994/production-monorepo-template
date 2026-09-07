# Monorepo Template

A production-oriented monorepo template for full-stack applications, designed to be understood by
both human developers and AI coding agents.

It ships structure, engineering standards, agent instructions, and a bootstrap path — and no
application code.

> **BOOTSTRAP_PLACEHOLDER:** Replace this README during bootstrap with a description of the project.
> See [`BOOTSTRAP.md`](BOOTSTRAP.md).

## What it deliberately does not decide

The template is language- and platform-neutral. It does not choose:

- a programming language, runtime, or framework
- a package manager or task runner
- a deployment platform or cloud provider
- a database

Those differ per project, and baking them in is what makes a template stop being reusable. During
bootstrap, a project records which choices are already known and gives each deferred decision a
trigger and an owner. It records a choice in
[`docs/context/architecture.md`](docs/context/architecture.md), with an
[ADR](docs/decisions/) when warranted, when that choice becomes due.

## What it does commit to

Conventions that hold regardless of the stack, and that keep the platform choice open:

- **A container per unit**, so the stack runs the same locally and in deployment.
- **Configuration and secrets from the environment**, read through one module per unit, validated at
  startup. See [`docs/standards/configuration.md`](docs/standards/configuration.md).
- **Tests change with behavior**, covering failure paths and not just the happy path. See
  [`docs/standards/testing.md`](docs/standards/testing.md).
- **Errors fail predictably and leak nothing.** See
  [`docs/standards/error-handling.md`](docs/standards/error-handling.md).
- **Every deployed unit can state what it is** — the commit it was built from, when it was built,
  and the digest of the image running. See [`infra/README.md`](infra/README.md).
- **Decisions are recorded, not remembered.** See [`docs/decisions/`](docs/decisions/).
- **What was learned is written down as it happens**, not reconstructed at the end. See
  [`docs/journal.md`](docs/journal.md).

The template also checks its own structure in CI — links, neutrality, and the size of the one file
every agent loads — because the checks that were only written down are the ones that drifted.

## Starting a project from this template

### 1. Create the project repository

On GitHub, choose **Use this template → Create a new repository**, then clone that newly created
repository to your computer. Do not fork the template, and do not clone the template repository as
the working project. A repository created with GitHub's template flow starts with one project-owned
commit instead of inheriting the template's commit history. See
[GitHub's template instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

### 2. Start the guided bootstrap

In Claude Code, open the new repository and enter:

```text
/bootstrap
```

The temporary bootstrap skill may also load automatically when the first request clearly asks to
start or continue project setup. Using `/bootstrap` is preferred because it is explicit and
deterministic.

For another coding agent, use this first message instead:

```text
Start the project bootstrap in read-only orientation mode. Read AGENTS.md,
BOOTSTRAP.md, and .agents/skills/bootstrap/SKILL.md in full, then inspect the
repository without modifying anything. Explain what is already in place and how
I should provide my files, notes, requirements, and other project context.
```

The first response should orient you and ask for existing context. It should not edit the
repository, choose a stack, or turn every bootstrap checkpoint into an immediate requirement.

### 3. Provide project context

Send existing files, notes, diagrams, requirements, links, and rough thoughts in as many messages
as necessary. The agent may acknowledge or clarify each batch, but it will keep intake open until
you say:

```text
CONTEXT COMPLETE
```

The agent then analyzes the material as a whole and recommends what belongs in product context,
architecture, ADRs, active build specifications, runbooks, or another focused location. It should
preserve coherent source documents and identify anything that should stay outside the repository.

### 4. Review before anything changes

The agent next proposes a bootstrap plan: files to change, context placement, decisions that can be
deferred, and verification. Correct or approve that plan before authorizing edits. Automatic skill
invocation is never permission to modify the repository.

### 5. Implement, review, and finalize

After implementation, review the project identity, routed context, open decisions, and remaining
project triggers. Finalization is a separate approval: it removes `BOOTSTRAP.md`, the temporary
bootstrap skill, this onboarding workflow, bootstrap-only language, and stale references, then runs
the repository checks again. The generic agent instructions, standards, durable skills, and valid
project triggers remain.

## Where things live

The repository map lives in [`AGENTS.md`](AGENTS.md) and only there, so there is exactly one place
to update when the structure changes. Start there — it is also the file every coding agent reads
first.

Each directory has a `README.md` describing what belongs in it. Read the nearest one before working
in a directory.

## Structure is a default, not a law

Every directory README ends with the same clause: the convention is a starting point, and a
different structure that fits the project better is a legitimate outcome — provided the decision is
recorded as an ADR rather than made silently. The goal is to give agents and developers enough
shape to work confidently, without preventing either from thinking.
