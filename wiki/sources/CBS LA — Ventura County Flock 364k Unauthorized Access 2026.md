---
title: "Flock License Plate Readers Shared Data with Out-of-State Agencies, Ventura County Audit Finds"
type: source
tags: [surveillance, immigration, alpr, california, infrastructure, civil-liberties, politics]
created: 2026-05-24
updated: 2026-05-24
sources: 10
raw: "raw/Ventura County Flock 364k unauthorized access 2026.md"
source_url: "https://www.cbsnews.com/losangeles/news/flock-license-plate-readers-shared-data-with-out-of-state-federal-agencies/"
author: "Matthew Rodriguez"
published: 2026-02-27
---

[Original source](https://www.cbsnews.com/losangeles/news/flock-license-plate-readers-shared-data-with-out-of-state-federal-agencies/)

## Summary
The Ventura County Sheriff's Office disabled [[Flock Safety]]'s "National Lookup" feature in June 2023 specifically to comply with California law prohibiting local agencies from sharing ALPR data with out-of-state and federal law enforcement. In early February 2025 — twenty months later — deputies discovered the feature had been reactivated without explanation. An audit found that out-of-state agencies had queried Ventura's cameras **more than 364,000 times** between February and March 2025; 299 of those query justifications referenced immigration enforcement. The Sheriff's Office's internal investigation determined that no one from their agency had reactivated the feature. Flock offered three possible explanations — Sheriff's Office staff, Flock staff, or a system bug — and said the cause was impossible to determine because of technical logging limitations. The case is the largest single documented instance of Flock's National Lookup architecture defaulting back on against express department policy.

## Key Points
- **364,000+ unauthorized accesses** by out-of-state agencies between February and March 2025
- **299 of those query justifications referenced immigration enforcement** — less than 1% of total searches, but a non-trivial federal-immigration footprint embedded in a county that had explicitly opted out
- **National Lookup had been disabled in June 2023** to comply with California law; reactivation discovered early February 2025 — the feature had been live again for an unknown period before discovery
- **Three Flock-offered explanations**: (1) a Sheriff's Office employee reactivated it, (2) a Flock employee activated it, (3) a system bug automatically reactivated it
- **Sheriff's Office internal investigation**: "determined that no one from our agency activated the national lookup feature"
- **Flock's position**: "due to limitations in technical logging, it was impossible to determine the specific cause"
- **Department response**: implemented daily independent audits; began evaluating alternative vendors; emphasized ALPR "remains a powerful and critical tool in combating crime"
- **Flock's subsequent technical responses**: blocked federal-California sharing; verified California agencies can't share with out-of-state law enforcement; auto-blocking of immigration-related search justifications
- **Nearly all Ventura County law enforcement agencies took similar suspension measures** in response
- **Class action connection**: Article notes Oakland-based Gibbs Mura filed the parallel class action alleging California-law violations

## Newsletter Angles
- **"Something reactivated it" is the load-bearing fact of the entire vendor-workaround thesis.** A department that explicitly turned off National Lookup to comply with state law had the feature reactivated, no employee did it according to the department's own investigation, and the vendor cannot or will not say who or what did. The architectural finding is that compliance with the vendor's default state is the only stable equilibrium; opting out fails silently.
- **364,000 in two months is the federal-pull baseline at scale.** Pair with [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] for the same architectural failure on four cameras in three weeks — the per-camera throughput rate scales remarkably well.
- **The "299 immigration justifications" figure is the rare case where the audit log itself documents federal-immigration use against the department's stated policy.** Useful as a primary citation when arguing that "we don't share with ICE" claims are unfalsifiable without an audit, and falsifiable with one.
- **Daily independent audits as the working accountability tool.** Per the article, Ventura's response was to implement what amounts to the only thing that survives the failure mode — continuous internal audit. Anchors the "open records and audits are the one tool that currently works" argument in [[The Bill of Rights Ends at the Contractor's Door]].

## Entities Mentioned
- [[Flock Safety]] — vendor; National Lookup reactivation is the center of the story
- [[Ventura County Sheriff's Office]] — the department whose feature was reactivated against its own policy
- Oxnard Police Chief Jason Benites — named local-LE source: "Proper guardrails must not only be in place, but they must work reliably"
- [[Gibbs Mura]] — Oakland law firm; referenced as plaintiff's counsel in the parallel California class action
- [[ICE]] — beneficiary referenced via 299 immigration-justified queries
- [[Department of Homeland Security]] — Flock disclaims contracts with DHS sub-agencies
- Matthew Rodriguez — author; CBS Los Angeles

## Concepts Mentioned
- [[National Lookup]] — the reciprocal feature whose silent reactivation is the entire story
- [[Flock Safety Surveillance Network]] — Ventura is a major California node
- [[Automated License Plate Recognition]] / ALPR
- [[Sanctuary City Policy]] — California's state-level sanctuary architecture (the law Ventura was complying with when it disabled the feature)
- [[Vendor-State Governance]] — the case for treating vendor defaults as policy choices

## Quotes
> "Determined that no one from our agency activated the national lookup feature." — Ventura County Sheriff's Office internal investigation finding

> "Due to limitations in technical logging, it was impossible to determine the specific cause." — Flock Safety statement on the reactivation

> "Proper guardrails must not only be in place, but they must work reliably." — Oxnard Police Chief Jason Benites

> "[Flock Safety] does not have any contracts with ICE or any sub-agency of the Department of Homeland Security." — Flock's stated position quoted in the article

## Notes
Major-market local TV reporting (CBS Los Angeles); the 364,000 figure has been widely cited in subsequent coverage but this is the original source. Named department source (Sheriff's Office investigation), named civil-society-adjacent source (Oxnard PC Benites), corporate statement on record. The article's central architectural finding — that the department's own opt-out failed silently — is the wiki's strongest single piece of evidence that Flock's National Lookup defaults override department-level policy choices. Cited as a primary source in [[The Bill of Rights Ends at the Contractor's Door]] (TCN draft, May 2026). Pairs with [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] (same architecture, smaller deployment, faster detection) and [[SFist — Flock lawsuit SFPD 1.6 million accesses]] (same architecture, larger department, lawsuit response).
