---
title: "Oregon SB 1516"
type: entity
entity_type: legislation
tags: [legislation, surveillance, alpr, vendor-liability, oregon, civil-liberties, public-safety]
created: 2026-05-24
updated: 2026-05-24
sources: 10
---

## Overview
**Oregon Senate Bill 1516** (83rd Oregon Legislative Assembly, 2026 Regular Session) is an omnibus public safety act with three distinct parts — Pretrial Release, Automated License Plate Recognition (ALPR) Systems, and Justice Reinvestment Equity Program — passed February 20, 2026 by the Senate and March 5, 2026 by the House, signed by Governor [[Tina Kotek]] March 31, 2026 under an emergency clause taking effect on passage. The ALPR sections (§§3–9, §§10–11) are the wiki-relevant core. The bill is the **first state-level statutory regime in the wiki to write explicit vendor-side liability into ALPR contracts** — establishing mandatory contract terms (end-to-end encryption, vendor data-ownership disclaimers, exclusive routing of all data requests through the contracting law enforcement agency, FBI CJIS Security Policy compliance, vendor liability for misuse) plus a private right of civil action against any vendor that improperly accesses, discloses, sells, shares, or uses captured plate data. The structural reply to the [[National Lookup]] silent-reactivation failure mode documented at [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]] and the [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] default-on case.

## Key Facts
- **Sponsor**: Senate Interim Committee on Judiciary (at request of)
- **Procedural history**: Passed Senate February 20, 2026; passed House March 5, 2026; signed by Governor [[Tina Kotek]] March 31, 2026 (per [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]]); emergency clause makes the law effective on passage
- **Senate signatories on the enrolled bill**: Rob Wagner (Senate President); Obadiah Rutledge (Secretary of the Senate)
- **House signatories**: Julie Fahey (Speaker of the House)
- **Secretary of State**: Tobias Read
- **Three parts**:
  - **§§1–2 — Pretrial Release**: Amends ORS 135.230 and 135.233; standing pretrial release orders; presumption-of-release framework (tangential to the wiki's surveillance thread)
  - **§§3–9 + §§10–11 — Automated License Plate Recognition Systems**: The wiki-relevant core
  - **§12 — Justice Reinvestment Equity Program**: Amends section 15, chapter 78, Oregon Laws 2022 (tangential to surveillance thread)

### ALPR provisions in summary

- **§4 — Authorized uses + 30-day retention**: ALPR may be used only for narrowly enumerated law-enforcement purposes (Oregon crimes, out-of-state crimes equivalent to Oregon crimes, federal crimes not contrary to state restrictions on prohibited enforcement activities including the Oregon sanctuary statutes ORS 181A.250/820/826, outstanding warrants, missing/endangered persons, AMBER/Silver Alerts, uninsured/unregistered vehicles, parking facility regulation, secured-area access control). **Retention cap of 30 days** for captured plate data not related to a court proceeding or ongoing criminal investigation
- **§5 — Data-sharing limitations**: LE agency may not provide access to captured plate data to any government entity or agency not created under the Oregon Constitution or state law, except for narrowly-defined law enforcement purposes that meet specific limitations including **"may not include unrestricted or ongoing access"**
- **§6 — Vendor-provided audits**:
  - Monthly searchable audit (preceding 30-day period) — system counts, locations, search counts, agency access list, authorized-user counts, vehicles captured, alerts, cameras accessed, per-search authorized-user ID/date/time/purpose
  - Quarterly searchable audit of all searches conducted on the LE agency's system on behalf of any government agency that is NOT the contracting LE agency (the federal-pull audit)
  - LE agency must publish audit results on its website within **two days** of receiving the audit
- **§7 — Mandatory contract terms (the structural innovation)**:
  - **§7(2)(e)(A)** — Captured plate data is property of the LE agency, **not owned by the vendor, may not be used or licensed by the vendor**
  - **§7(2)(e)(B)** — All requests received by the vendor (including warrants, subpoenas) **must be directed exclusively to the LE agency** that owns the data
  - **§7(2)(e)(C)** — **End-to-end encryption required**
  - **§7(2)(e)(D)** — FBI CJIS Security Policy compliance + CJIS Security Addendum + audit rights + prompt security-incident notification
  - **§7(2)(e)(E)** — **Vendor may be held liable for misuse or improper release**, including damages
- **§8 — Existing-contract grandfather**: Existing contracts may continue under their original terms for the duration of the contract; extensions/renewals/new contracts must comply; §4 (authorized-uses) applies regardless of contract date
- **§9 — Private right of action against vendors**:
  - §9(1)(a): Vendor **may not access, disclose, sell, share or otherwise use** captured plate data, except for limited technical-support (with express agency consent) or to provide §6 audits
  - §9(2): Individual victim of intentional or grossly-negligent §9(1)(a) violation may bring civil action against the vendor for economic and noneconomic damages, equitable relief, and reasonable attorney fees
  - §9(3): Any person may bring civil action to enjoin a §9(1)(a) violation
  - §9(4): §9 causes of action are the **exclusive remedies** in law or equity for §9(1)(a) violations
- **§11 — Public records carveout**: Captured plate data is conditionally exempt from disclosure under ORS 192.345(44), **except** the §6 vendor audits, which must be disclosed (with PII redaction). The bill thus codifies the audit-as-accountability-tool finding into the public records framework

## Newsletter Relevance
SB 1516 is **the cleanest state-level legislative response in the wiki to the vendor-workaround pattern**. Every prior remedy operated on the user-side / access-restriction layer; SB 1516 operates on the **vendor-side liability layer**. It is the statutory expression of the [[The Bill of Rights Ends at the Contractor's Door]] thesis that real remedies for vendor surveillance exist at the state-statutory layer, not the federal constitutional layer — and it goes further than the parallel [[Gibbs Mura — Flock Safety Class Action California 2026]] private-class-action route by writing vendor liability directly into Oregon's ALPR statute rather than relying on California Civil Code §1798.90.55 enforcement.

The bill should be treated as a **legislative template** for the wiki's surveillance cluster — other states may borrow its language, particularly the §7(2)(e) mandatory contract terms and the §9 private right of action. The combination of (a) prohibiting vendor use, license, or sharing of captured data, (b) routing all third-party data requests through the contracting agency, (c) mandating end-to-end encryption, (d) requiring CJIS compliance with audit rights, (e) creating individual civil standing, and (f) making §9 the exclusive remedy for §9(1)(a) violations is **structurally novel** — the wiki holds no other state statute with this configuration.

## Connections
- [[Flock Safety]] — the dominant ALPR vendor; the bill's structural target even though never named in the text
- [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] — Bend's June 2025 default-on incident is the case study most directly motivating the bill
- [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]] — the parallel California silent-reactivation incident; SB 1516's §5 + §6 + §9 framework directly addresses this failure mode
- [[Gibbs Mura — Flock Safety Class Action California 2026]] — California's parallel private-class-action track; SB 1516 is the statutory complement
- [[National Lookup]] — not named in the bill but the architectural target of §5 (data-sharing limitations) and §6(2) (quarterly third-party-search audit)
- [[Tina Kotek]] — Governor of Oregon; signed the bill
- [[SCREEN Act]] — sibling legislative-text entity in the wiki's surveillance/vendor cluster; both ingested 2026-05-24
- [[Vendor-State Governance]] — the concept the bill operationalizes (deferred concept page; this entity is one of multiple referents)
- [[FBI]] — referenced via CJIS Security Policy compliance requirement

## Source Appearances
- [[Oregon SB 1516 — Enrolled Bill Text]] — primary; full statutory text; 16 pages; passed Feb 20 / March 5 2026; enrolled bill as filed with Secretary of State
- [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] — secondary; mentions the bill in the legislative-response section, references Governor Kotek signature March 31, 2026; characterizes the bill as "restricts ALPR data sharing to Oregon agencies only and requires public audit reports every 30 days" — accurate but understates the vendor-liability scope

## Open Questions
- **Governor's signature confirmation**: The enrolled PDF shows blank signature fields for the Governor; secondary reporting (Bend Source) says signed March 31, 2026. Wiki needs a primary-source confirmation (Oregon governor's office release, OLIS final entry, or Oregon Laws 2026 chapter assignment) — flagged as a deferred lookup.
- **Companion or sibling bills**: Are there other 2026 Oregon ALPR-related bills? The Senate Interim Committee on Judiciary often introduces packages; possible companion measures worth a lookup.
- **Implementing administrative rules**: Section 7 requires LE agencies to publish policies and procedures; will the Oregon Department of Justice issue model policies? Worth tracking.
- **Compliance footprint**: How many Oregon LE agencies are currently using Flock or comparable ALPR systems, and what fraction of those contracts are subject to the existing-contract grandfather (§8) versus the new compliance regime? Bend's contract expired May 1, 2026 per the [[Bend Source]] page — so Bend itself wouldn't be relevant for grandfather analysis; but Portland, Eugene, and Salem deployments would be.
- **Out-of-Oregon adoption**: Will California, Washington, or other West Coast states pattern after SB 1516's §7(2)(e) mandatory-contract-terms framework? Worth flagging for the next ingest cycle if a comparable bill appears in another state.

## Wiki audit
- Wiki has TWO sources for this entity: the primary bill text and the secondary Bend Source piece. Source threshold met.
- The bill is referenced by wikilink in [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]], [[Flock Safety]], [[Flock Safety Surveillance Network]], [[National Lookup]], and (after this ingest) [[The Bill of Rights Ends at the Contractor's Door]] is the article context. The entity page resolves all these dangling links.
