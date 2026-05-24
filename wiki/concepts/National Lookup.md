---
title: "National Lookup"
type: concept
tags: [surveillance, alpr, infrastructure, vendor-architecture, immigration, politics]
created: 2026-05-24
updated: 2026-05-24
sources: 12
---

## Definition
**National Lookup** is the [[Flock Safety]] product feature that lets a participating agency query [[Automated License Plate Recognition]] (ALPR) data captured by other Flock agencies anywhere on the network. By design, the feature is **reciprocal**: enabling it to query out-of-state cameras simultaneously authorizes every other agency on the network to query the enabling department's cameras. National Lookup is the architectural mechanism that converts thousands of locally-deployed Flock camera installations into a single nationwide surveillance database — without any individual department choosing to deploy a nationwide surveillance database.

The feature is the operational layer behind the [[Flock Safety Surveillance Network]]: the network exists because National Lookup is the default routing protocol between Flock installations. Departments that disable National Lookup remove themselves from the reciprocal pool; departments that leave it on (or have it silently reactivated) become both a query source and a query target.

## Why It Matters for the Newsletter
National Lookup is **the cleanest single case study in the wiki of vendor defaults functioning as policy**. A city council that has passed a sanctuary resolution still has cameras whose responsiveness to federal-immigration queries is governed by a Flock feature toggle, not by the resolution. A department that affirmatively disables the feature — as Ventura County did in June 2023 — can have it silently reactivated by a process the vendor cannot or will not identify ([[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]]). A small department that turns it on to do basic out-of-state lookups becomes a federal-immigration query target within hours ([[Bend Source — Bend PD Flock 279 Federal Queries June 2025]]).

The feature is the structural reason the [[Vendor Workaround Pattern|vendor workaround pattern]] documented in [[The Bill of Rights Ends at the Contractor's Door]] reaches the Fourth Amendment layer specifically. A federal agency querying a private database of public-space recordings doesn't need a warrant; National Lookup makes 4,500+ private databases query-addressable from a single federal-agency seat.

## Evidence & Examples
- **Bend, Oregon (June 2025):** Captain Brian Beekman discovered the reciprocity default three weeks after deployment; **279 federal immigration queries** had already run against Bend's four cameras (118 from CBP, 161 from third-party out-of-state agencies acting on behalf of ICE, CBP, HSI). Beekman disabled it the same day he understood the architecture. [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]]
- **Ventura County, California (Feb 2025):** The Sheriff's Office had disabled National Lookup in June 2023 to comply with California law (SB 54 + Civil Code § 1798.90.55(b)). In early February 2025 deputies discovered it had been silently reactivated; an audit found **364,000+ out-of-state queries** between February and March 2025, 299 of them with immigration justifications. The department's own investigation determined no one on staff had reactivated it. Flock said the cause was impossible to determine because of logging limitations. [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]]
- **San Francisco PD (lawsuit, Feb 2026):** Gibbs Mura's amended complaint alleges **1.6 million federal-agency accesses** to SFPD's Flock data over seven months — at $2,500/violation statutory floor, $4 billion in California-state-law exposure. [[SFist — Flock lawsuit SFPD 1.6 million accesses]] / [[Gibbs Mura — Flock Safety Class Action California 2026]]
- **Beekman's architectural description (the canonical quote):** "What we didn't know is that National Lookup is a reciprocal sharing feature — when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency."
- **Flock's mitigation timeline (from [[Flock Safety — Does Flock Share Data With ICE]]):** March 2025 — California national lookup disabled at the state level; June 2025 — automatic immigration/reproductive-health keyword blocks; January 2026 — toggle to disable all federal sharing. Each mitigation addresses a specific failure mode; National Lookup as a reciprocal-by-default architecture persists.
- **Oregon's legislative response ([[Oregon SB 1516]], signed March 31, 2026):** Doesn't name "National Lookup" but addresses the architecture at three statutory layers: §5 prohibits LE agencies from sharing captured plate data with any government entity not created under the Oregon Constitution (except for narrowly-defined LE purposes with no "unrestricted or ongoing access"); §6(2) mandates quarterly vendor-provided audits of all searches conducted on the agency's system on behalf of any non-contracting government agency (the federal-pull audit, statutorily required); §9 creates a private right of civil action against any vendor that "accesses, discloses, sells, shares or otherwise uses" captured plate data — the silent-reactivation failure mode at Ventura would, in Oregon under SB 1516, generate individual civil standing against the vendor. The remedy follows the vendor architecture, not the contracting agency. [[Oregon SB 1516 — Enrolled Bill Text]]

## Tensions & Counterarguments
- **Flock's framing**: National Lookup is opt-in per department; each agency has sole authority over what they share. The architectural critique: "opt-in" is misleading when the default is reciprocal and reactivation occurs against department policy without an identifiable cause.
- **The crime-investigation utility**: National Lookup makes cross-jurisdictional vehicle searches efficient — stolen vehicles, AMBER alerts, fugitive recovery, multi-state crime patterns. The architecture's benefit case is real; the policy question is whether the federal-immigration footprint is a tolerable cost or a defining feature.
- **The audit-log limitations**: Flock's own statement that the cause of Ventura's reactivation was "impossible to determine" because of logging limitations is the structural critique in three words: a feature whose state changes cannot be attributed in the vendor's logs cannot be governed by departmental policy.

## Related Concepts
- [[Flock Safety Surveillance Network]] — the network exists because of National Lookup; the concept is the per-installation lever
- [[Vendor-State Governance]] — National Lookup is the cleanest single feature in the wiki demonstrating how vendor defaults function as policy
- [[Sanctuary City Policy]] — the policy regime National Lookup effectively bypasses
- [[Automated License Plate Recognition]] / ALPR — the underlying technology layer
- [[Open Records as Accountability Tool]] — the only working remedy when the feature defaults wrong (Atlanta audit, Ventura audit)

## Key Sources
- [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] — Peter Madsen, May 6, 2026; canonical operational case study; Beekman quote
- [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]] — Matthew Rodriguez, Feb 27, 2026; reactivation-against-policy case; 364k accesses; logging-limitations admission
- [[Gibbs Mura — Flock Safety Class Action California 2026]] — case page, April 3, 2026 amended complaint; statutory damages framework
- [[SFist — Flock lawsuit SFPD 1.6 million accesses]] — Leanne Maxwell, Feb 28, 2026; 1.6M SFPD accesses; class-action news framing
- [[Atlanta PD used Flock cameras to track migrants, records show]] — ACPC, Nov 13, 2025; 4,500-agency footprint; 3,254 Border Patrol searches against APD via National Lookup
- [[Why some cities are canceling Flock license plate reader contracts]] — NPR Joffe-Block, Feb 17, 2026; cancellation wave triggered in part by National Lookup architecture awareness; 30+ cities
- [[Oregon SB 1516 — Enrolled Bill Text]] — primary text of the Oregon statute responding to the National Lookup federal-pull architecture; §5 + §6(2) + §9 framework writes vendor-side liability directly into Oregon's ALPR regime
