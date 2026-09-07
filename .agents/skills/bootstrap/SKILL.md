---
name: bootstrap
description: Guide a new project through the repository's initial bootstrap. Use when BOOTSTRAP.md exists and the owner is starting, continuing, or finalizing project setup, including sharing source files, notes, requirements, or other project context. Do not use after BOOTSTRAP.md has been deleted.
---

# Bootstrap

## Objective

Guide the owner from a fresh template snapshot to a project-specific repository without forcing
decisions before they are due. `BOOTSTRAP.md` owns the requirements and exit condition; this skill
owns the interactive workflow.

This skill is temporary. Remove it during bootstrap finalization as `BOOTSTRAP.md` directs.

## Activation and authority

1. Confirm that `BOOTSTRAP.md` exists at the repository root. If it does not, stop using this skill;
   bootstrap has already been finalized.
2. Read `AGENTS.md` and `BOOTSTRAP.md` in full before doing anything else. Then inspect the current
   repository structure, working-tree status, and existing context without modifying files.
3. Treat automatic or explicit skill invocation as permission to orient and advise only. It is not
   permission to edit files, select a stack, delete directories, commit, push, or finalize.
4. Preserve existing user changes. If the working tree is not clean, identify relevant overlaps
   before proposing work.

## Required inputs

- A fresh project repository in which `BOOTSTRAP.md` is still present.
- The owner's existing project material, supplied immediately or across multiple messages.
- Explicit owner approval before implementation and before finalization.

## Workflow

### 1. Orient

Explain briefly:

- what the repository already provides;
- which information is required for Bootstrap core;
- which decisions can remain deferred; and
- how the owner can provide existing material.

Do not turn the guide into a questionnaire that must be completed in one sitting. Ask only the
questions needed to receive and understand the owner's existing context.

### 2. Receive context

Invite the owner to send notes, requirements, diagrams, files, links, prior documentation, and
rough thoughts across as many messages as needed.

- Acknowledge each batch and retain its relationship to earlier batches.
- Inspect material when necessary to understand it, but do not modify repository files.
- Do not assume the intake is finished because one batch arrived.
- Wait for `CONTEXT COMPLETE`, or an equally explicit statement from the owner, before producing the
  consolidated placement proposal.
- If the owner asks for analysis of one batch before intake is complete, provide it while keeping
  the overall intake open.

### 3. Synthesize and route

After intake is complete, summarize the project and propose where each durable piece of context
belongs using the routing table in `BOOTSTRAP.md`.

- Preserve coherent source documents when splitting them would remove useful context.
- Distinguish known facts, owner preferences, assumptions, conflicts, and open decisions.
- Give every deferred decision a concrete trigger and owner.
- Identify material that should remain outside the repository.
- Flag questions whose answers would materially change the proposed structure.

Do not write files during this phase.

### 4. Plan

Produce a project-specific bootstrap plan that names the files to change, what will change, what
will remain deferred, and how the result will be verified. Preserve the shipped directory roots
unless project evidence supports a different structure and the owner approves the departure.

Wait for explicit approval before implementation.

### 5. Implement

Apply only the approved plan. Follow the tiers and lifecycle-marker rules in `BOOTSTRAP.md`; an
unchecked triggered item is allowed when it is irrelevant or durably deferred. Keep the owner
informed when new evidence requires a material change to the approved plan.

Do not finalize merely because Bootstrap core appears complete. Report what was completed, what was
deferred, and any remaining cleanup, then wait for explicit approval to finalize unless the owner
already approved finalization as part of the plan.

### 6. Finalize

Follow `BOOTSTRAP.md`'s cleanup sequence exactly. In addition:

1. Replace the root template README with the project README, including removal of its onboarding
   workflow.
2. Remove this skill's row and temporary-skill explanation from `.agents/skills/README.md`.
3. Delete `.agents/skills/bootstrap/` only after its earlier work and pre-deletion checks are
   complete. Its loaded instructions remain available for the rest of the current session.
4. Remove every remaining operational reference to this skill and the bootstrap workflow.
5. Delete `BOOTSTRAP.md`, run the post-deletion searches and invariant checker, and report any
   valid `PROJECT_TRIGGER` entries that remain.

## Expected output by phase

- **Orientation:** a short repository assessment and instructions for sending context.
- **Intake:** concise batch acknowledgements and only necessary follow-up questions.
- **Synthesis:** a placement proposal, open decisions, conflicts, and material questions.
- **Planning:** an implementation plan with verification and explicit approval boundary.
- **Implementation:** approved repository changes plus verification results.
- **Finalization:** a project-specific repository with no bootstrap skill, guide, onboarding
  language, unresolved bootstrap markers, or stale references.

## Acceptance criteria

- No repository mutation occurs before explicit owner approval.
- Supplemental material is considered as a whole before final placement is proposed.
- Deferred choices have triggers and owners instead of invented answers.
- Standard directory roots are not removed merely because they are unused at project start.
- Finalization happens only after Bootstrap core is complete and the owner authorizes it.
- Both hard invariant checks pass after temporary bootstrap material is removed.

## Verification method

Before implementation, compare the proposed plan with the complete intake and confirm that every
change is approved or explicitly deferred. During finalization, run the pre-deletion and
post-deletion checks in `BOOTSTRAP.md`; confirm that the guide, this skill, its catalog entry, the
root onboarding workflow, unresolved bootstrap markers, and stale references are gone while valid
project triggers and durable agent infrastructure remain.
