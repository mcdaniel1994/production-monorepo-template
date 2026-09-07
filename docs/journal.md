# Build Journal

> **PROJECT_TRIGGER [trigger: the first meaningful journal entry is written]:** Delete this
> block when the trigger occurs. No entry exists yet.
>
> The conventions below are active; only the entries are missing.

An append-only log of what was learned and what was traded off while building this. Written in the
moment, because the reasoning is richest then and mostly gone by the end.

**Add an entry with the `journal` skill** —
see [`../.agents/skills/journal/SKILL.md`](../.agents/skills/journal/SKILL.md). Entries already
here are never edited.

## What goes here

One lesson or one tradeoff per entry, recorded when it happened. Write an entry because something
taught you something — not because a day passed.

## What does not

- **The decision itself** → [`decisions/`](decisions/). An entry *links* to an ADR, it never
  restates one. An ADR is deliberately impersonal, and what it strips out is exactly what belongs
  here.
- **Status updates** — what got finished this week.
- **Task tracking** → not committed at all, per [`build_specs/README.md`](build_specs/README.md).

## Conventions

- **Append at the bottom**, newest last, so the file reads forward as a narrative.
- **Never modify an existing entry.** A later entry may correct an earlier one, and that correction
  is itself worth reading.
- **Roughly 150–200 words per entry.** The constraint is the point.
- **One lesson per entry.** A long-form piece may cluster five of them; a short note may use one.
  Both only work if entries stand alone.
- **When this file passes about five pages, roll it over:** rename it to `journal-01.md` (then
  `-02`, and so on) and start a fresh `journal.md`. Roll over rather than compressing — compressing
  means editing, and editing is what this file does not do.

## Entry format

    ## YYYY-MM-DD — the hook, not the topic

    **Tags:** comma, separated

    **Trying to:** what you set out to do

    **The tradeoff:** what was on the table, what you picked, and why

    **What surprised me:** or what you got wrong, or what you believed first

    **Links:** ADR, commit, file, spec

**What surprised me** is the field that decays fastest and the one that makes an entry worth reading
a year later. An entry with nothing to put there may not be an entry worth writing.

---

<!-- Entries begin below this line. Append only; nothing above is ever edited. -->
