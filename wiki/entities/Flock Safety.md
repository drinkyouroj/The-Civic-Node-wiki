---
title: "Flock Safety"
type: entity
entity_type: organization
tags: [surveillance, infrastructure, technology, immigration, power]
created: 2026-04-19
updated: 2026-05-24
sources: 22
---

## Overview
Flock Safety is an Atlanta-based private surveillance technology company providing automated license plate readers (ALPRs), vehicle "fingerprint" recognition, and related capture systems to more than 5,000 US law enforcement and private agencies. Operates a connected nationwide network through which any participating agency can query data captured by any other — making the [[Flock Safety Surveillance Network]] *de facto* nationwide surveillance infrastructure with no federal warrant requirement. Central character in the contemporary debate over how privately operated surveillance vendors enable federal immigration enforcement to circumvent local sanctuary policies.

## Key Facts
- **5,000+ agencies** participate in Flock's connected network as of Feb 2026 ([[Why some cities are canceling Flock license plate reader contracts]]); earlier reporting cited ~4,500 ([[Atlanta PD used Flock cameras to track migrants]])
- **10.6 million searches** of Atlanta PD's cameras alone in 2025; APD itself ran 323,292 searches; 3,254 by US Border Patrol; 3,383 with immigration keywords from external agencies
- **Camera capabilities:** License plate, vehicle make/model, bumper stickers, body damage — composite "vehicle fingerprint"
- **CBP/HSI pilots admitted Aug 2025** — CEO Garrett Langley had previously denied federal contracts; admitted in August that Flock had pilot programs with both U.S. Customs and Border Protection and Homeland Security Investigations. Statement: "some of our public statements inadvertently provided inaccurate information. We clearly communicated poorly." ([[Why some cities are canceling Flock license plate reader contracts]])
- **Workaround documented:** Pierce County (GA) Sheriff ran 4 "Border Patrol Assist" searches on Sept 15, 2025, providing cross-jurisdictional bypass even after pilots "ended"
- **ICE proxy searches:** Local police conducting searches on behalf of federal agencies, listing "ICE" or "immigration" as search reason in audit logs — not direct ICE access but effective workaround ([[Why some cities are canceling Flock license plate reader contracts]])
- **Technical responses:** Keyword filters blocking immigration/reproductive healthcare search terms (Oct 2025); "offense type" dropdown menu added later — critics note trivially circumventable by choosing a "more palatable" option
- **At least 30 localities cancelled or deactivated** contracts since early 2025, accelerating sharply in late 2025 through Feb 2026 ([[Why some cities are canceling Flock license plate reader contracts]]); includes Flagstaff AZ, Cambridge MA, Eugene OR, Santa Cruz CA, Hillsborough NC, Staunton VA
- **Austin City Council** declined to renew (June 2025); **Denver City Council** unanimously rejected extension but Mayor [[Mike Johnston]] unilaterally signed a smaller contract under cost threshold
- **Campus expansion:** [[Emory University]] deployed 7+ Flock cameras since 2024; April 2026 student/faculty walkout demanded contract termination
- **Contractual prohibition confirmed:** Flock's terms of service explicitly prohibit agencies from using Flock data for immigration enforcement — this prohibition predates the June 2025 technical safeguards ([[Flock Safety — Does Flock Share Data With ICE]])
- **Complete federal pilot program history (from Flock's own blog):** FBI (2021–2023), National Park Service (2021–2024), ATF Louisville (2022–2025), ATF Nashville (2023–2025), NCIS (2025), HSI (2025), CBP (2025). "In August of 2025, Flock publicly announced it would no longer conduct pilot projects with federal agencies."
- **Technical safeguards timeline (from Flock's own blog):** June 2024 — Illinois attestation; March 2025 — California national lookup disabled; June 2025 — automatic immigration/reproductive-health keyword blocks; July 2025 — Virginia restrictions + case number requirements; August 2025 — federal agencies separated into restricted org type; January 2026 — toggle to disable all federal sharing
- **Stated position (Jan 6 / Apr 8, 2026 blog):** No partnership with ICE; access requires explicit customer grant + applicable law
- **CEO rhetoric:** Langley called DeFlock.me (crowdsourced ALPR mapping site) "terroristic" in September Forbes interview; October email to customers characterized critics as "defund the police" activists — prompted Staunton VA police chief Jim Williams to cancel contract, calling the citizens' concerns "democracy in action" ([[Why some cities are canceling Flock license plate reader contracts]])
- **Renée Good connection:** Santa Cruz council member Susie O'Hara cited the January 7, 2026 killing of [[Renée Good]] in Minneapolis as a turning point; Santa Cruz voted to end contract January 13 — six days after Good's death ([[Why some cities are canceling Flock license plate reader contracts]])
- **National Lookup default-on architecture (Bend, OR, June 2025):** Captain Brian Beekman discovered three weeks after deployment that [[National Lookup]] is reciprocal by default; in those 3 weeks, 279 federal immigration queries had run against Bend's four cameras (118 directly from CBP; 161 from third-party agencies acting for ICE/CBP/HSI). Beekman: "What we didn't know is that National Lookup is a reciprocal sharing feature... when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency." ([[Bend Source — Bend PD Flock 279 Federal Queries June 2025]])
- **Silent reactivation against department policy (Ventura County, CA, Feb 2025):** Ventura County Sheriff's Office had disabled National Lookup in June 2023 to comply with California law; deputies discovered in early Feb 2025 it had been silently reactivated. An audit found **364,000+ out-of-state queries** between Feb–March 2025; 299 query justifications referenced immigration enforcement. The Sheriff's Office's internal investigation determined no one from the department had reactivated the feature; Flock stated the cause was "impossible to determine" due to "limitations in technical logging." ([[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]])
- **Gibbs Mura amended class action (April 3, 2026):** Filed in San Francisco Superior Court (co-counsel Milberg PLLC); grounded in California Civil Code § 1798.90.55(b), § 1798.90.51, § 1798.90.52, and SB 54 — no federal constitutional claims asserted. Statutory damages floor $2,500/violation under § 1798.90.54; SFPD 1.6M accesses alone implies ~$4B statutory exposure. ([[Gibbs Mura — Flock Safety Class Action California 2026]])

## Newsletter Relevance
Flock is the **clearest case study of "private vendor as policy-laundering vehicle"** in this wiki's surveillance coverage. The architecture is the story: local sanctuary policies become functionally meaningless when local cameras feed a nationwide network that ICE-cooperative neighboring agencies can query. Connects directly to [[Operation Metro Surge]] and [[Killing of Renée Good]] as parallel "federal-immigration-via-local-infrastructure" cases.

The contradiction between Flock's stated non-cooperation policy and the documented operational reality (Atlanta audit; Pierce County workaround; Illinois SoS audit) is the editorial center.

## Connections
- [[Atlanta Police Department]] — primary documented misuse case
- [[Atlanta Community Press Collective]] — primary investigative outlet
- [[US Customs and Border Protection]] — major external user (pilots officially ended)
- [[ICE]] — central concern
- [[Enforcement and Removal Operations (ERO)]] — search-keyword origin
- [[Sandy Springs Police Department]] — also documented running ERO queries
- [[Pierce County Sheriff's Department (GA)]] — post-pilot CBP workaround
- [[Austin City Council]] / [[Denver City Council]] — local political opposition
- [[Illinois Secretary of State]] — Flock audit finding illegal CBP access
- [[Emory University]] — campus deployment under protest
- [[Gibbs Mura]] — Oakland plaintiff's firm; lead California class-action counsel
- [[Ventura County Sheriff's Office]] — case study in silent National Lookup reactivation against department policy
- [[San Francisco Police Department]] — primary documented violation site in Gibbs Mura complaint (1.6M federal accesses)
- [[Rob Bonta]] — California AG; parallel state-AG enforcement track via El Cajon case (Oct 2025)

## Source Appearances
- [[Atlanta PD used Flock cameras to track migrants]] — primary investigative document
- [[Community members protest Flock Safety cameras at Emory]] — campus expansion under protest
- [[Why some cities are canceling Flock license plate reader contracts]] — NPR Feb 2026; 30+ cancellations, CEO admission, Santa Cruz/Renée Good connection
- [[Flock Safety — Does Flock Share Data With ICE]] — Flock's own blog; confirms contractual prohibition + complete federal pilot history + technical safeguards timeline
- [[SFist — Flock lawsuit SFPD 1.6 million accesses]] — Feb 2026 class action; 1.6M accesses by federal/out-of-state agencies in seven months; California state law violation alleged
- [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] — Peter Madsen, May 2026; 279 federal immigration queries in three weeks; Beekman's canonical statement of the National Lookup reciprocity architecture
- [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]] — Matthew Rodriguez, Feb 2026; 364k accesses after silent National Lookup reactivation; Flock's "impossible to determine" admission
- [[Gibbs Mura — Flock Safety Class Action California 2026]] — case page, April 2026 amended complaint; statutory grounds; $2,500/violation framework; 200+ California-department class scope

## Open Questions
- Funding and ownership structure — Flock has raised significant venture capital; understanding the investor pressure to expand the agency network is key to predicting how seriously they'll enforce non-cooperation pledges.
- Technical architecture of "ending CBP pilots" — what changed materially? The Pierce County workaround suggests very little.
- Analogous private-vendor surveillance systems (e.g., Axon, Palantir) — how does Flock's business model compare to broader police-tech sector consolidation?
- The water/energy footprint of Flock's AI infrastructure — flagged at the Emory protest, but lacks a hard public number specific to Flock.
