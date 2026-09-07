---
name: grill-me
description: A relentless interview to sharpen a plan or design. Use when a plan, spec, or architecture is drafted but not yet stress-tested, and the goal is to find its weak points before implementation starts.
disable-model-invocation: true
---

# Grill Me

## Objective

Stress-test a plan, spec, or design by interrogating it until its weak points are exposed and either
fixed or consciously accepted. The output is a sharper plan and an explicit list of what remains
uncertain — not agreement.

This skill is invoked deliberately by the repository owner. Do not run it unprompted.

## Required inputs

- The plan, spec, or design under review — a file, a message, or a decision being weighed.
- What kind of feedback is wanted, if the owner has said. Default to all of it.

## Workflow

1. **Read the whole artifact first.** Do not begin questioning partway through; a question answered
   three paragraphs later wastes the owner's time and costs credibility.

2. **Restate the plan in your own words** — two or three sentences, including what you understand it
   is trying to achieve. If the restatement is wrong, the interview stops here and the real problem
   is that the plan is ambiguous. That is itself the most valuable finding.

3. **Interrogate along these axes.** Ask the sharpest question in each; skip an axis that genuinely
   does not apply rather than manufacturing a question for it.
   - **Premise** — is the problem real, and is it the problem worth solving now?
   - **Failure modes** — what breaks first under load, under partial failure, at 10x scale, at the
     boundaries?
   - **Reversibility** — what does this lock in? What does undoing it cost in six months?
   - **The unstated alternative** — what obvious simpler approach was skipped, and why?
   - **Evidence** — which claims are asserted rather than verified? What would falsify them?
   - **Scope** — what is being included that could be cut without harming the goal?
   - **Second-order effects** — what does this make harder elsewhere?
   - **Operability** — who runs this at 3am, and what do they see?

4. **One question at a time when a thread is live.** Follow a weak answer down rather than moving
   on. A batch of eight questions gets eight shallow answers.

5. **Push back on answers that do not hold.** Agreement is not the goal. Say specifically why an
   answer does not resolve the concern, and what would.

6. **Know when to stop.** Stop when remaining questions are matters of taste, or when the owner has
   heard the concern and made a decision. A decision made with the risk in view is a good outcome;
   re-raising it after that is noise.

## Expected output

A short written summary, not a transcript:

- **Holds up** — the parts that survived questioning, stated briefly.
- **Changed** — what the plan should now do differently, and why.
- **Accepted risks** — concerns raised, understood, and deliberately taken on.
- **Still open** — what could not be resolved and what information would resolve it.

## Acceptance criteria

- Every axis in step 3 was either explored or explicitly skipped as inapplicable.
- At least one concrete change or one explicitly accepted risk came out of it. An interview that
  concludes "looks good" either had nothing to work with or was not adversarial enough.
- No question was asked whose answer was already in the artifact.
- Open items are stated as questions with the information needed to close them, not as vague
  misgivings.

## Verification method

Re-read the original artifact against the summary. Every "changed" item must correspond to a
specific part of the plan, and every "accepted risk" must be one the owner actually saw and
responded to — not one inferred on their behalf.
