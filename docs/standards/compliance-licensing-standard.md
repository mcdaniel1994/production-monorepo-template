# Compliance & Licensing Standard

**Status:** Active · **Version:** 1.0 · **Last reviewed:** 2026-09-03 · **Next review:** 2026-12-03

**Applies to:** every third-party dependency, asset, external service, and AI model or provider
brought into this repository — across every dependency manifest and lockfile, whatever the language.
**Does not apply to:** code written in this repository, which is governed by the root `LICENSE`.

This file is the authority on license classification, attribution, and the approval path for
non-permissive dependencies. It covers third-party code, assets, hosted services, and AI providers,
including any AI agents or capabilities that ship as part of the product in `apps/`, `services/`, or
`packages/`.

**The goal:** every dependency's license is known and permitted before it is adopted, never after.

---

## Before you start

- **Read this before** adding, upgrading, replacing, or removing a dependency; adopting a
  third-party service or AI provider; vendoring code or assets; or editing `LICENSE` or
  `THIRD_PARTY_LICENSES.md`.
- Determine the license of everything being added and classify it against the categories below.
- **Stop and escalate to the repository owner *before* adoption** for strong-copyleft,
  non-commercial, custom-licensed, or unlicensed dependencies. Escalate first; do not adopt and
  flag afterwards.
- Record attribution in `THIRD_PARTY_LICENSES.md` where this standard requires it.
- Report which dependencies were added and how each was classified.

**Examples:** adding a charting library; switching AI provider or model; vendoring an icon set or
font; adopting a hosted error-tracking service.

**Non-examples:** changing application code without touching a manifest; a patch-version bump of a
dependency already classified as permissive whose license is unchanged; editing documentation.

---

## License Categories

| Category | Examples | Commercial use | Action required |
|---|---|---|---|
| Permissive | MIT, BSD-2/3-Clause, ISC, Apache-2.0 | Yes | None beyond attribution; approved by default |
| Weak copyleft | LGPL-2.1/3.0, MPL-2.0 | Yes, conditionally | Acceptable when used unmodified/dynamically linked; must be listed in `THIRD_PARTY_LICENSES.md` |
| Strong copyleft | GPL-2.0/3.0, AGPL-3.0 | Conditional | Repository-owner approval required before adoption |
| Non-commercial | CC-BY-NC-*, evaluation-only licenses | No | Must not be used; find a permissive/paid alternative |
| Proprietary / custom | Vendor EULAs, model-specific community licenses | Per agreement | Read the terms; record the determination in `THIRD_PARTY_LICENSES.md` |
| No license declared | Unlicensed repo, unattributed snippet | Assume all-rights-reserved | Must not be used without obtaining an explicit license |

## Default Policy

- This repository's own license is whatever the root [`LICENSE`](../../LICENSE) declares. The choice
  is made during bootstrap; until it is made, treat the code as all-rights-reserved.
- Every manifest's `license` field must match the root `LICENSE`, expressed in whatever form that
  ecosystem's manifest format requires. Check how the format is validated — some ecosystems accept
  only an SPDX expression in the plain string form, and a proprietary declaration needs their
  alternative syntax.
- Permissive dependencies are approved by default.
- Weak-copyleft dependencies are acceptable provided they are
  documented in [`THIRD_PARTY_LICENSES.md`](../../THIRD_PARTY_LICENSES.md).
- Strong copyleft, non-commercial, custom-licensed, and unlicensed dependencies require explicit
  repository-owner approval before adoption. Treat "no license found" as all-rights-reserved and do not
  use the resource until a license is obtained.

## Attribution

- `THIRD_PARTY_LICENSES.md` at the repo root is the single register of every dependency that is not
  permissively licensed (permissive dependencies are covered in bulk by re-running the ecosystem's
  license scanner, not enumerated individually). Update it whenever a non-permissive dependency is
  added, removed, or changes license across a version bump.
- Every manifest's `license` field must stay consistent with the root `LICENSE`. A manifest declaring a
  different license than the repo (e.g. a stray `"MIT"`) is a defect — fix it, don't work around it.

## Dependency Workflow

When adding, upgrading, or removing a dependency, third-party asset, API/SDK integration, or AI
model/provider:

1. **Identify** — name, version, publisher, source URL, and type.
2. **Verify the license** — locate the license file, SPDX identifier, or terms of service. No license
   found → stop, do not use, escalate to the repository owner if there's a real need.
3. **Check commercial rights** — confirm the license permits commercial use, redistribution, and
   modification as this project requires. Non-commercial or unclear → stop, escalate.
4. **Check transitive dependencies** — a dependency's sub-dependencies carry their own licenses;
   periodically re-scan the full tree with the ecosystem's license scanner, not just top-level
   manifests.
5. **Record attribution** — add non-permissive dependencies to `THIRD_PARTY_LICENSES.md` with license,
   version, direct/transitive status, and a link to the license text.
6. **Escalate if unresolved** — copyleft (GPL/AGPL/LGPL/MPL), non-commercial, custom-licensed, or
   unlicensed resources require repository-owner sign-off before merging. Permissive dependencies do
   not require prior approval as long as step 5 is done.

## Supply-Chain Baseline

- Lockfiles are committed and kept in sync with their manifests. An uncommitted lockfile means no
  two installs are provably the same.
- Install only from the ecosystem's official registry. Do not add packages from unverified sources,
  personal forks, or unvetted archives.
- Run the ecosystem's vulnerability audit before release, and address or consciously accept every
  finding. Record accepted findings and why.
- Run a full dependency/license audit (all manifests, transitive trees, and `THIRD_PARTY_LICENSES.md`
  reconciliation) at least annually, and before any major release.

## AI Models and Providers

Model and API-provider terms are separate from code licenses and are not covered by an OSS license at
all — they're governed by the provider's terms of service and usage policy. Before adopting a new model
or provider anywhere in product code:

- Confirm the license/terms explicitly permit commercial use for this product.
- Check data-handling terms — whether the provider logs, retains, or trains on submitted data — and
  note any opt-outs taken.
- Record the provider, model, terms version, and date reviewed in `THIRD_PARTY_LICENSES.md`.

## Exceptions

Follow the standard exception mechanics defined in [`README.md`](README.md#exceptions):
state the requirement, why compliance is infeasible, the safest alternative considered, get explicit
repository-owner approval before merging, and record the rationale in the PR description. Silent
non-compliance is a defect, not an exception.
