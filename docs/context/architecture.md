# Architecture

> **BOOTSTRAP_PLACEHOLDER:** Record template lineage, standards applicability, and open decisions;
> fill the remaining sections as their decisions are triggered, then replace this block with the
> project's current architectural state and explicit deferrals.
>
> This file ships with the repository template and contains no real content yet. It is where a
> project records the decisions the template deliberately does not make: languages, toolchain,
> deployment target, and any departure from the default structure.
>
> Describe the system in the **present tense** — how it is, not how it came to be. The reasoning
> belongs in [`../decisions/`](../decisions/), where it is dated and immutable.

Bootstrap fills **Template lineage**, **Standards**, and **Open decisions**. The other sections are
completed when their underlying choices are made; an undecided choice belongs in Open decisions,
not in prose that makes it look settled.

## Template lineage

Current repository provenance. Keep these fields here after bootstrap so upstream improvements can
be evaluated against the exact template revision this project started from.

| Field | Value |
|---|---|
| Template repository | `<repository URL>` |
| Template commit | `<full commit SHA>` |
| Project started | `YYYY-MM-DD` |

## Shape

The units that exist and what each is responsible for. One line each. Link to each unit's README
rather than restating it.

| Unit | Responsibility |
|---|---|
| | |

## Toolchain

The choices this project made that the template left open. Record them here so no one has to infer
them from lockfiles. Complete this section before the first implementation unit is added:

- **Languages and runtimes**
- **Package manager(s)**
- **Task runner**, if any, and the commands it exposes
- **Test runners**
- **Lint and formatting**

## Deployment

Complete this section when a deployment platform is selected, and no later than the first
production deployment.

- **Target platform** — and the ADR that records why.
- **How units are built and shipped.**
- **Environments** that exist, and how they differ.

## Data

Stores in use, what lives in each, and how schema changes are applied. Note anything with retention
or residency obligations, and cross-reference the constraint in
[`product.md`](product.md#constraints) rather than restating it. Complete this section before the
first persistent data store is introduced.

## Standards

Record each standard's version, whether it applies, and the project's conformance separately.
Update these fields when the project deliberately adopts a newer version — not automatically when
a standard changes, since adoption may require work.

Use these values:

- **Applicability:** `Applicable`, `Conditional — <trigger>`, or `Not applicable — <reason>`.
- **Conformance:** `Adopted`, `Adopted with exception — <link>`, or `Not adopted — <ADR>`.
- Record conformance for both Applicable and Conditional standards. For Not applicable standards,
  use `—` in both the Conformance and Adopted columns. `Not adopted` is a deliberate standards
  exception and requires an ADR.

| Standard | Version | Applicability | Conformance | Adopted |
|---|---|---|---|---|
| compliance-licensing | 1.0 | | | YYYY-MM-DD |
| configuration | 1.0 | | | YYYY-MM-DD |
| error-handling | 1.0 | | | YYYY-MM-DD |
| testing | 1.0 | | | YYYY-MM-DD |
| visibility | 1.0 | | | YYYY-MM-DD |

## Open decisions

Choices intentionally deferred during bootstrap. Every row needs an event that makes the decision
due and a person or team responsible for noticing it. Remove a row when it is resolved, update the
relevant present-tense section, and link the resulting ADR there when the decision warrants one.

| Decision | Why deferred | Trigger | Owner |
|---|---|---|---|
| | | | |

## Cross-cutting decisions

Choices that constrain every unit — authentication approach, inter-service communication, shared
configuration, logging and observability. Each should have a corresponding ADR.

## Departures from the template

Where this project's structure differs from the template default, and the ADR that records the
decision. This section existing is the point: departing is expected, departing silently is not.

| Departure | ADR |
|---|---|
| | |
