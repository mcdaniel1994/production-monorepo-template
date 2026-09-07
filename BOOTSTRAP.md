# Bootstrap Guide

> **BOOTSTRAP_PLACEHOLDER:** Complete Bootstrap core, reconcile the repository, then delete this
> guide.

Use this guide to turn the template into a project without forcing decisions before they are due.
Its checkboxes are guidance, not a gate that makes every possible setup task mandatory.

The temporary [`bootstrap` skill](.agents/skills/bootstrap/SKILL.md) guides the conversation around
this file. Claude Code may load it when a setup request matches its description; `/bootstrap` is the
deterministic entry point. Invocation begins in read-only orientation mode and never grants
permission to edit, commit, or finalize. The root [`README.md`](README.md) gives the complete owner
workflow.

Bootstrap is finished when every **Bootstrap core** item is complete, and every remaining item is
either irrelevant to this project or recorded in **Open decisions** with a trigger and an owner.
Unchecked is a valid end state. Unrecorded is not.

## The three tiers

| Tier | Meaning |
|---|---|
| **Bootstrap core** | Required to finish bootstrap |
| **Decide when triggered** | Required only when the named event occurs |
| **Before production** | Required before the first production deployment |

Files use `BOOTSTRAP_PLACEHOLDER` only for content that must be replaced during bootstrap. A project
trigger combines `PROJECT_TRIGGER` with `[trigger: <event>]: <future action>` to record localized
work whose decision is not yet due. Project triggers may survive bootstrap; bootstrap placeholders
may not.

[`docs/context/architecture.md`](docs/context/architecture.md) is intentionally only partially
filled during bootstrap. Lineage, standards applicability, and Open decisions are core. Toolchain,
deployment, data, and other present-tense sections wait for the events that make those choices real.

## Bootstrap core

### 1. Intake supplemental material

Before filling project files, ask the owner for the notes, requirements, diagrams, prior documents,
and other context they already have. Read the material as a set, then propose where it belongs based
on the question it answers and how long that answer should remain true.

| Material answers | Destination | Lifespan |
|---|---|---|
| What are we building, and for whom? | [`docs/context/product.md`](docs/context/product.md) | Current product intent |
| How is the system shaped today? | [`docs/context/architecture.md`](docs/context/architecture.md) | Current system state |
| Why did we choose X over Y? | An ADR in [`docs/decisions/`](docs/decisions/) | Permanent, append-only record |
| What should be built next, concretely? | A spec in [`docs/build_specs/active/`](docs/build_specs/active/) | Moved to `completed/` and frozen after implementation |
| How is the system operated or recovered? | A runbook in [`docs/runbooks/`](docs/runbooks/) | While the procedure remains current |
| How must code behave everywhere? | A file in [`docs/standards/`](docs/standards/) — rare; read its invariance and exception rules first | Cross-project requirement |
| None of the above | Keep it out of the repository | No durable repository value |

Preserve coherent source material in its existing shape. Adding another focused file to
`docs/context/` is normal when one document deserves to stay whole; the two shipped files are not a
closed list. For large source material, keep the source intact and add a concise summary plus a
pointer from the appropriate context file. State what the summary omits. Ask before routing material
whose purpose or lifespan is unclear.

### 2. Establish identity

- [ ] Rename the repository and update its description.
- [ ] Choose a license and fill [`LICENSE`](LICENSE). It ships empty deliberately; the choice is the
      owner's.
- [ ] Rewrite [`README.md`](README.md) for this project: what it is, how to use it, and where to
      start. Do not imply that deferred architecture has already been chosen.
- [ ] Replace the reporting contact and supported-versions placeholders in
      [`SECURITY.md`](SECURITY.md).
- [ ] Replace `@owner` in [`.github/CODEOWNERS`](.github/CODEOWNERS).

### 3. Record product and durable bootstrap state

- [ ] Fill [`docs/context/product.md`](docs/context/product.md) with product identity, users,
      outcomes, constraints, non-goals, and domain language. Replace its placeholder block.
- [ ] Record the template repository, full source commit SHA, and project start date in
      [`architecture.md#template-lineage`](docs/context/architecture.md#template-lineage). GitHub's
      “Use this template” creates no durable link back to its source; architecture owns that link.
- [ ] Complete [`architecture.md#standards`](docs/context/architecture.md#standards):
  - Use `Applicable`, `Conditional — <trigger>`, or `Not applicable — <reason>`.
  - Record conformance for Applicable and Conditional standards.
  - Use `—` for the Conformance and Adopted fields when a standard is Not applicable.
  - Use `Not adopted — <ADR>` only through the standards exception and approval path.
- [ ] Reconcile [`docs/runbooks/maintenance-calendar.md`](docs/runbooks/maintenance-calendar.md)
      with standards applicability. Activate rows for Applicable standards, keep Conditional rows
      dormant under the same trigger, and remove rows sourced only from a Not applicable standard.
- [ ] Seed [`architecture.md#open-decisions`](docs/context/architecture.md#open-decisions) with each
      project decision that constrains other work but is not due yet. Every row needs the decision,
      why it is deferred, the event that makes it due, and an owner. Features, general backlog work,
      and tasks do not belong there.
- [ ] Replace the architecture placeholder block after these core sections describe what is known
      and the relevant unknowns are explicitly deferred. Do not invent toolchain, deployment, data,
      or authentication answers to make the file look complete.

### 4. Confirm the starting structure

- [ ] Keep the shipped `apps/`, `services/`, `packages/`, and `infra/` roots, along with the reserved
      `apps/website/` location. They can remain unused until project work gives them a concrete role;
      do not create placeholder application code merely to populate them.
- [ ] Do not remove a directory during bootstrap merely because it is not needed yet. If project
      evidence later supports a different structure, record the departure as an owner-approved ADR,
      then update the [`AGENTS.md`](AGENTS.md) map, affected trigger-table rows, sibling READMEs,
      links, and comments in the same change.
- [ ] Keep a `README.md` in every reserved or active directory so its purpose survives a clone.

### 5. Reconcile agent instructions

- [ ] Reconcile [`AGENTS.md`](AGENTS.md) line by line; do not assume every template statement still
      describes the project:
  - Always replace **What this is** with the project's identity.
  - Make the repository map match every retained top-level directory and actual responsibility.
  - Update the `infra/` row when a deployment platform is chosen.
  - Update the `.github/workflows/` row when lint, test, and build jobs become real.
  - Update the root `compose.yaml` guidance when the first unit or Compose file lands.
  - Remove or rewrite bootstrap-placeholder and empty-license guidance after placeholders are
    resolved and `LICENSE` is filled. Keep the durable project-trigger rule.
  - Preserve all five standards trigger rows. Applicability does not remove the route that finds a
    standard when later work enters its scope.
- [ ] Keep [`CLAUDE.md`](CLAUDE.md) as a pointer to `AGENTS.md`. Agent-specific entry points must not
      acquire separate instructions.

### 6. Clean up and exit

Do this after the durable state above is recorded:

1. Run `python3 .github/scripts/check-invariants.py` and clear both hard failures if either appears.
2. Resolve every `UNRESOLVED` or `MALFORMED` lifecycle-marker finding. A `PROJECT_TRIGGER` may remain
   only when it names a concrete event and localized future action. Put decisions that constrain
   later work in Open decisions instead of leaving in-place reminders.
3. Search all file types, including hidden configuration and workflow files, for both
   `TEMPLATE.md` and `BOOTSTRAP.md`. Before deletion, this guide may refer to itself; remove every
   other operational reference that will become stale.
4. Search for prose that still claims the current repository is a template, ships with a template,
   or is still in bootstrap. Remove stale claims while retaining intentional template-lineage and
   invariance guidance.
5. Recheck the repository map, standards trigger table, directory READMEs, workflow and
   configuration comments, maintenance owners, and active build-spec queue. Update everything made
   stale by bootstrap.
6. Replace the root template README with the project README so none of its setup workflow remains.
7. Remove the `bootstrap` entry and temporary-skill explanation from `.agents/skills/README.md`, then
   delete `.agents/skills/bootstrap/`. Keep the generic skill-routing instructions and the
   `.claude/skills` symlink.
8. Delete this guide.
9. Search both filenames, the deleted skill path, `/bootstrap`, and `BOOTSTRAP_PLACEHOLDER` again; no
   match should remain. Run the invariant
   checker again and clear both hard failures. Valid `PROJECT_TRIGGER` findings may remain.

Do not write a journal entry merely to complete bootstrap. Keep its project trigger
until there is a meaningful tradeoff or lesson worth recording.

## Decide when triggered

For each triggered choice, update the present-tense architecture section, remove its Open decisions
row, and write an ADR when the decision meets the threshold in `docs/decisions/README.md`.

| Decision or work | Trigger |
|---|---|
| Language and runtime | Before adding the first implementation unit |
| Package manager, task runner, test runner, lint, and formatting | Before the first implementation unit needs them |
| First unit and its placement under `apps/`, `services/`, or `packages/` | When the first product behavior is ready to be implemented |
| Root `compose.yaml` | When the first runnable unit exists |
| Real lint, test, and build CI jobs | When the first implementation unit lands |
| `.env.example` scope and variables | Before the first unit reads configuration |
| Dependency-update configuration | When the first non-GitHub-Actions dependency manifest lands |
| Data store, migrations, retention, backups, RPO, and RTO | Before persistent product data is introduced |
| Authentication and authorization | Before access or protected data requires an identity boundary |
| Deployment platform and scheduled-job mechanism | When deployment work begins; no later than the first production deployment |
| Public-surface visibility obligations | When a public surface is planned or introduced |

When a trigger fires, resolve the whole decision rather than merely removing its marker. Update any
affected map rows, READMEs, workflow comments, standards applicability, and maintenance gates in the
same change.

## Before production

- [ ] Accept the deployment ADR, complete [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml),
      and write and verify the rollback runbook.
- [ ] Make every deployed unit expose build provenance: commit SHA, build time, and image digest.
- [ ] Pin base images by digest, generate an SBOM, and run vulnerability and license checks against
      the actual dependency graph.
- [ ] Validate configuration at startup, complete `.env.example`, and verify that no secret is
      committed, logged, or returned.
- [ ] For persistent data, document retention, backup, RPO, and RTO, then perform and time a restore.
- [ ] Establish production access ownership and the access-review obligation.
- [ ] Assign owners to every retained maintenance-calendar row.
- [ ] Require lint, test, and build checks for protected branches only after those jobs perform real
      work and cannot pass unconditionally.

## Keeping standards upgradable

[`docs/standards/`](docs/standards/) and durable [`.agents/`](.agents/) assets are invariant across
projects built from this template. The bootstrap skill is explicitly temporary and is removed only
through the finalization sequence above. A structural default may yield to project needs through an
owner-approved ADR. An applicable engineering standard uses its own exception and approval path;
structural flexibility does not weaken security, licensing, testing, or other normative
requirements.

Improvements that are genuinely general belong upstream in the template. Evaluate upstream drift
against the lineage recorded in architecture rather than editing invariant files locally.
