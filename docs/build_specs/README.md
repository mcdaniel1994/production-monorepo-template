# `docs/build_specs/`

Specifications for work to be built: what should exist, why, and how to tell when it is done.

Lifecycle is visible from the directory structure:

| Path | Contains |
|---|---|
| [`active/`](active/) | Draft, ready, and in-progress specifications, plus their ordered queue |
| [`completed/`](completed/) | Implemented specifications, frozen as historical records |

Only specifications for this project belong here. Historical setup notes from before this
repository became the project are source history, not project build context.

## Lifecycle

1. Create a specification in `active/` and add it to the queue in
   [`active/README.md`](active/README.md).
2. Keep mutable state and priority only in that queue. The first `Ready` row is next unless a row is
   already `In progress`.
3. When implementation is complete, add `**Implementation:** Implemented YYYY-MM-DD — frozen` to
   the specification, move it once into `completed/`, remove its queue row, and update direct links
   in the same change.
4. Never edit a completed specification to match later reality. Write a new specification instead.

The move into `completed/` is the freeze boundary. Once there, the filename and contents are stable.

## What belongs in a spec

- **Purpose** — the problem, in a paragraph.
- **Scope** — what is in, and explicitly what is out and must not be touched.
- **Work items** — concrete enough to execute without re-deriving the intent.
- **Acceptance criteria** — checkable, not aspirational.
- **Verification** — how to prove the criteria are met.

## What does not belong here

- How code must behave in general → [`../standards/`](../standards/)
- Why an architectural choice was made → [`../decisions/`](../decisions/)
- How the system works today → [`../context/architecture.md`](../context/architecture.md)
- Step-by-step task tracking during implementation → not committed
- Historical setup specifications that do not describe this project's work → source history, not
  project build context

Finishing a spec is a good moment for a journal entry — see [`../journal.md`](../journal.md). What
turned out differently from the plan may be worth recording. This is optional and is never written
on someone else's behalf.

## Naming

Use `NNNN-short-descriptive-slug.md`, assigning the next unused four-digit sequence across both
folders. The number is a permanent identity and creation sequence, not priority. Priority belongs in
the active queue, where it can change without renaming files.

Keep a spec in one file. If it is too large for one file, it is probably two specs.

## References to temporary paths

Write a path expected to be renamed or deleted as inline code, not as a Markdown link. The hard link
check evaluates completed specifications too; linking a temporary path would make a correct later
deletion fail CI. Use Markdown links for targets the project is expected to keep.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../decisions/`](../decisions/).
