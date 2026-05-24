---
title: "Federal Immigration Officials Made 279 Queries into Bend's Flock Safety Data in its First Three Weeks"
type: source
tags: [surveillance, immigration, alpr, infrastructure, politics, oregon, civil-liberties]
created: 2026-05-24
updated: 2026-05-24
sources: 9
raw: "raw/Bend PD Flock 279 federal queries June 2025.md"
source_url: "https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/"
author: "Peter Madsen"
published: 2026-05-06
---

[Original source](https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/)

## Summary
Bend, Oregon's police department signed on to [[Flock Safety]]'s ALPR network in early June 2025 and discovered three weeks later that the "National Lookup" feature was reciprocal by default — enabling other agencies to query Bend's cameras as soon as Bend turned on the ability to query theirs. In those three weeks, federal immigration officials ran **279 queries** against Bend's four cameras: 118 directly from CBP, 161 from third-party out-of-state agencies acting on behalf of ICE, CBP, and HSI. Captain Brian Beekman, who oversaw the program, disabled the feature on June 25, 2025 — the same day the department understood the default architecture. The piece documents the cleanest single-source case of how Flock's National Lookup design exports a small department's surveillance footprint to federal immigration enforcement before the department can audit its own configuration.

## Key Points
- **279 federal immigration queries** ran against Bend's four Flock cameras between June 4 and June 25, 2025 — the first three weeks the cameras were online
- **118 of the 279 queries came directly from US Customs and Border Protection**; the remaining 161 were from third-party out-of-state law enforcement agencies "acting on behalf of ICE, CBP, and HSI"
- **National Lookup is reciprocal by default**: Captain Brian Beekman discovered on June 25, 2025 that turning on the ability to query other agencies' cameras automatically turned on every other agency's ability to query Bend's
- **Audit-log gap**: Bend PD says there is no evidence federal agencies actually extracted data from query results; Flock's logging at the time was insufficient to determine what was retrieved versus what was merely searched
- **Catalina Sánchez Frank (Latino Community Association):** "The timing represents a concerning overlap, as June 2025 was an intense period of immigration law enforcement in our area"
- **Police Chief Mike Krantz and Mayor Melanie Kebler** characterized the incident as a configuration error, not a privacy breach
- **Bend City Council voted January 7, 2026 to immediately shut down** the Flock cameras and let the contract expire May 1, 2026
- **Oregon SB 1516, signed March 31, 2026**, restricts ALPR data sharing to Oregon agencies only and mandates public audit reports every 30 days — Bend's incident is the documented driver. (Bill text now in wiki via [[Oregon SB 1516 — Enrolled Bill Text]]; the bill is structurally broader than Bend Source's description — includes mandatory vendor-contract terms with end-to-end encryption and an exclusive §9 private right of civil action against vendors)

## Newsletter Angles
- **The "default-on" architecture is the entire story.** Bend deployed four cameras for a service it understood to be local; the network deployed it as a federal-immigration node before the department could audit the configuration. The vendor's default settings — not the contract, not the city's policy — determined what surveillance was actually delivered. Pair with [[Atlanta PD used Flock cameras to track migrants]] for the same architectural pattern at scale.
- **279 in three weeks is the federal-pull baseline.** Whatever Flock's stated position about federal cooperation, this is what 21 days of National Lookup actually produces on four cameras in a small Oregon city. Multiply by 4,500+ agencies and the network's federal-throughput becomes the salient design feature, not the bug.
- **Oregon SB 1516 as the legislative response template.** State-level fix (ALPR-sharing restricted to in-state agencies, 30-day public audit cadence) addresses the instance — Bend's specific contract — while leaving the architectural default intact for every other state.
- **Beekman's quote is the cleanest published statement of the design pattern** from a department that just got burned by it: "What we didn't know is that National Lookup is a reciprocal sharing feature — when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency."

## Entities Mentioned
- [[Flock Safety]] — vendor; National Lookup architecture is the center of the story
- [[US Customs and Border Protection]] — 118 of 279 queries; direct federal user
- [[ICE]] — beneficiary of third-party-proxy queries
- [[Homeland Security Investigations]] — beneficiary of third-party-proxy queries
- Captain Brian Beekman — Bend PD; discovered and disabled National Lookup; named source for the architectural quote
- Police Chief Mike Krantz — Bend PD
- Mayor Melanie Kebler — Bend, Oregon
- Catalina Sánchez Frank — Executive Director, Latino Community Association (Bend); named civil-society source
- Peter Madsen — author; The Source (Bend, OR)

## Concepts Mentioned
- [[National Lookup]] — Flock's reciprocal cross-agency sharing feature; central architectural mechanism documented here
- [[Flock Safety Surveillance Network]] — Bend is one of the 4,500+ nodes
- [[Automated License Plate Recognition]] / ALPR — underlying technology
- [[Sanctuary City Policy]] — Bend wasn't a declared sanctuary city, but the city government's response treats the queries as inconsistent with local values
- [[Vendor-State Governance]] — the gap between what the city contracted for and what the vendor's defaults delivered

## Quotes
> "What we didn't know is that National Lookup is a reciprocal sharing feature... when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency." — Capt. Brian Beekman, Bend PD

> "The timing represents a concerning overlap, as June 2025 was an intense period of immigration law enforcement in our area." — Catalina Sánchez Frank, Latino Community Association

> "[A] 'privacy breach' implies the overriding of security systems or someone gaining unauthorized access" — Mayor Melanie Kebler, framing the incident as a configuration error rather than a breach

## Notes
Primary local reporting; named on-record sources for both the technical detail (Beekman) and the civil-society response (Sánchez Frank); city official commentary on record. The article is the cleanest published statement of the National Lookup reciprocity architecture from a department on the receiving end of the federal pull. Cited as a primary source in [[The Bill of Rights Ends at the Contractor's Door]] (TCN draft, May 2026). Pairs with [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]] for the second documented case of the same architectural failure at a much larger scale.
