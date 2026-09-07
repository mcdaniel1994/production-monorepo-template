# `.agents/skills/`

Reusable coding-agent workflows for recurring repository maintenance tasks. Use a skill here when
its objective matches the task at hand.

## Catalog

| Skill | Objective |
|---|---|
| [`bootstrap`](bootstrap/SKILL.md) | Guide the owner through staged initial project setup. Automatically applicable while `BOOTSTRAP.md` exists; `/bootstrap` is the deterministic entry point. Temporary — remove at bootstrap finalization. |
| [`grill-me`](grill-me/SKILL.md) | Stress-test a plan, spec, or design by interrogating it until its weak points are exposed. Owner-invoked only. |
| [`journal`](journal/SKILL.md) | Append a dated entry to `docs/journal.md` recording a tradeoff navigated or a lesson learned. Owner-invoked only. |

The `bootstrap` skill is a deliberate temporary exception to this directory's otherwise durable
workflows. Its guide owns the deletion sequence: finalization removes the skill, this paragraph,
and its catalog row together.

## How agents invoke a skill

`.agents/skills/` is the canonical location — **edit skills here, never through any other path.**

- **Any agent** is routed here by [`../../AGENTS.md`](../../AGENTS.md). When a task matches a
  skill's frontmatter `description`, read that `SKILL.md` end-to-end and follow the workflow before
  acting.
- **Claude Code** additionally auto-discovers these through `.claude/skills`, which is a symlink to
  this directory. A skill whose invocation policy permits it may load when its description matches
  the request, and any skill can be invoked manually as `/skill-name`. The symlink exists purely for
  discovery; there is only ever one copy of a skill.

A skill must work for a fresh clone. Never point a `SKILL.md` at a skill in a personal
`~/.claude/` directory — it will silently do nothing for everyone else.

On a platform without symlink support (Windows without developer mode), `.claude/skills` may not
resolve. Recreate it locally, or copy the directory and do not commit the copy.

## Adding a new skill

Create `skill-name/SKILL.md` starting with YAML frontmatter. **The directory name must match the
frontmatter `name`** — invocation follows the frontmatter, so a mismatch leaves a directory nobody
can find by the name it advertises.

```yaml
---
name: skill-name
description: Use when <trigger condition>. <One-sentence summary of what the skill produces.>
---
```

Then the body sections:

- **Objective**
- **Required Inputs**
- **Workflow** (numbered steps)
- **Expected Output**
- **Acceptance Criteria**
- **Verification Method**

After adding, list the skill in the catalog above with a one-line objective.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../../docs/decisions/`](../../docs/decisions/).
