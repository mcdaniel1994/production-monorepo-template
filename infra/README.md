# `infra/`

Infrastructure-as-code for the deployment platform.

> **PROJECT_TRIGGER [trigger: a deployment platform is selected]:** This directory is empty
> until that trigger. Record the choice as an ADR in
> [`../docs/decisions/`](../docs/decisions/), then replace this block with the infrastructure that
> exists here.

The platform-neutral commitments keep the choice open: a container per unit, a liveness signal per
service, configuration and secrets injected from the environment, structured logs to stdout, and
**every deployed unit able to state what it is** — the commit it was built from, when it was built,
and the digest of the image running. A project that holds to those can move between platforms
without restructuring.

That last one is build provenance, and it earns its place at 3am. Without it, "which build is
production actually running?" is an archaeology exercise across a deploy log, a registry, and a
branch. With it, it is one request. It is public build metadata, not configuration — it carries no
secrets and needs no protection.

Operational procedures — how to debug or recover the running system — belong in
[`../docs/runbooks/`](../docs/runbooks/), not here.

---

This is a starting convention, not a requirement. If a different structure fits this project
better, propose it and record the decision in [`../docs/decisions/`](../docs/decisions/).
