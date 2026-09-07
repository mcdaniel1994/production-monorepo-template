---
name: journal
description: Append a dated entry to docs/journal.md recording one tradeoff navigated or one lesson learned. Use when a decision has just been made, an ADR accepted, a spec finished, or something turned out differently than expected. Owner-invoked only.
disable-model-invocation: true
---

# Journal

## Objective

Capture one lesson or one tradeoff in `docs/journal.md` while the reasoning is still fresh, in a
form that later becomes source material for writing.

The value is entirely in what a diff cannot show: what was nearly chosen, what was believed first,
what turned out to be wrong. Capture that, or the entry is a changelog.

This skill is invoked deliberately by the repository owner. Do not run it unprompted — an agent that
decides on its own to journal writes filler, and spends a budget that exists to stay small.

## Required inputs

- The work just done, from this session's context.
- The owner's answers to the questions in step 3. These are not optional; they are the entry.

## Workflow

1. **Read `docs/journal.md` in full**, conventions and existing entries alike. If the placeholder
   block is still present and there are no entries, this is entry one — remove that block as part of
   writing it.

2. **Draft from what you observed.** From this session work out what was being attempted, what was
   decided, and what it links to — ADR, spec, commit, file. Fill in as much of the format as the
   session genuinely supports, and invent none of the rest.

3. **Ask the owner two or three questions**, and only ones the session cannot answer:
   - What surprised you, or what did you get wrong first?
   - What was the closest alternative you did not take, and why?
   - Is there anything here you would tell someone else to avoid?

   Ask them together and briefly. This step is the whole difference between a journal and a
   changelog — but it is not an interview. Two or three questions, then write.

4. **Apply the significance filter.** If the honest answer is "nothing surprised me and there was no
   real tradeoff," say so and write nothing. A skipped entry costs nothing. A filler entry spends
   part of a deliberately small file and makes the rest less worth reading.

5. **Write one entry** in the format `docs/journal.md` documents, appended at the very bottom of the
   file. Roughly 150–200 words. One lesson — if there are two, that is two entries, or one of them
   is not ready yet.

6. **Link, do not restate.** Where a decision has an ADR, link it and write what the ADR
   deliberately leaves out. Restating an ADR duplicates a fact that already has an owner.

7. **Keep it raw.** Do not polish for an audience. Choosing voice, framing, and length for a
   particular reader is a separate job done later; polishing now loses the specifics that make the
   entry usable then.

8. **Check the size.** If the file has passed roughly five pages, roll it over as the conventions
   describe — rename to the next `journal-NN.md`, start a fresh `journal.md` with the same header —
   and append the entry to the new file.

## Expected output

One entry appended to the bottom of `docs/journal.md`, in the documented format, with each field
filled or deliberately omitted. Nothing else in the file changes.

Then tell the owner in one line what was recorded, and what was deliberately left out.

## Acceptance criteria

- Everything above the insertion point is **byte-identical** to before — the entry-one placeholder
  block being the only permitted removal.
- The entry has a real `What surprised me`, or no entry was written.
- Exactly one lesson or tradeoff. Not a summary of the session.
- Any decision referenced is linked, not restated.
- Length is roughly 150–200 words.
- The content is true. This file is source material for writing that gets published, and
  [`visibility.md`](../../../docs/standards/visibility.md) §5 governs what may be claimed publicly:
  never record experience that did not happen, or planned work as though it shipped. An honest log
  now is what makes the eventual piece defensible.

## Verification method

Re-read `docs/journal.md` after writing. Confirm the new entry is last, that the entry above it is
unchanged, and that the entry stands on its own — readable a year from now by someone with no
memory of this session and no way to recover it.
