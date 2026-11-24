# Contribution 001 — Fund authorization freshness before expanding AI retrieval

**Executive decision brief, 24 November 2026.** Prepared by Ashish Srivastava. This is an original synthetic-case decision aid, not an account of a bank engagement or client outcome.

## Decision requested

Approve a bounded review of the current permission decision at document hydration, cache return and final disclosure before increasing the reach of an AI knowledge service. Assign a business-service owner and a security/identity owner. Keep the first pilot read-only.

## Business condition

A service can approve a document search and later return its cached content after customer rights, employee access or a document's status changes. The relevant risk is disclosure under stale authority. A model's useful answer and a cache hit do not establish current permission.

The commercial consequence depends on the real data, users and affected services. No breach probability, avoided loss, regulatory penalty, customer adoption or ROI is claimed here.

## Evidence available now

The owned [revocation-gap lab](https://github.com/cybersmeashish/vulnerability-research-and-disclosures) exercises eight synthetic cases. Its deliberately flawed baseline permits six cases annotated as denied; the corrected function permits no denied fixture case. Valid access and fresh re-authorisation remain available.

This is an inspectable local reproduction, not evidence that the same gap exists in an enterprise estate. The correction assumes authoritative grants/epochs and does not implement distributed identity or atomic revocation. The [detection contribution](https://github.com/cybersmeashish/security-detections-and-fixes) is an experimental proposal; deployed backend parity remains untested.

## Proposed work and acceptance

Use a proposed ten-working-day review window **after** the bank/company accepts the scope, owners, data access and test environment. Actual effort and delivery terms must be agreed for that estate.

1. Map lookup, hydration, cache, citation display, tools and restore paths; identify the authority used at each.
2. Reproduce legitimate, revoked, expired, cross-case and restored-state cases in an authorised test environment.
3. Correct one bounded path and review telemetry/schema, outages, cancellation and cache invalidation.
4. Publish the agreed measurement report with actual successes, failures, unresolved gaps and rollback conditions.

Acceptance requires demonstrable legitimate access and denied stale/cross-case disclosures in the intended environment, plus current grants on restored/cache paths. A passing local unit test cannot substitute for that integration evidence.

## Accountable owners

The business owner accepts impact and permitted uses; identity/data owners establish current grants and record rights; the application team implements the boundary; the CISO reviews security evidence; SRE owns availability, restoration and rollback; legal/privacy reviews applicable data/disclosure obligations. Independent assurance reviews the scope and unresolved findings.

## Next investment

Expand only after the intended-environment boundary works and observation gaps are recorded. Budget the next increment for distributed revocation/restore assurance, representative workload measurements and independent review. Use the [decision template](../templates/decision-brief.md) and [published evidence](../evidence/README.md) to keep the investment traceable.
