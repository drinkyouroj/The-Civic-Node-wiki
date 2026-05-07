---
title: "Interconnection Queue"
type: concept
tags: [power, infrastructure, grid, regulation, ferc]
created: 2026-05-07
updated: 2026-05-07
sources: 7
---

## Definition

The administrative and engineering process by which proposed power generation, storage, or large-load projects request connection to the US transmission grid. Each Regional Transmission Organization (RTO) — PJM, ERCOT, MISO, SPP, ISO-NE, NYISO — maintains its own queue. Projects are studied for grid impact, assigned interconnection costs, and scheduled for energization. The queue is public, updated quarterly or annually, and dispositive: a project with PPAs but no queue position is a press release; a project with queue position is real.

## Why It Matters for the Newsletter

The interconnection queue is the document class that decides which AI data center projects actually deliver in 2026-2030. Financial press AI capex coverage rarely cites it; the queue is the first place the binding constraint shows up and the last place chip-layer analysts look. Vocabulary central to the [[AI Buildout Grid Constraint]] thesis. Provides the analytical edge for the operator-class reader: read the PUC and FERC filings, track the queue depth, ignore the press release.

## Evidence & Examples

- **Total queue size.** ~2,300-2,600 GW in US queues vs. ~1,279 GW installed capacity (as of 2024) — roughly twice the entire installed grid. [[US Interconnection Queue Twice Installed Capacity — Latitude Media - 2024-04-11]]
- **Active projects.** ~11,600 projects total seeking interconnection.
- **Wait time evolution.** Renewable projects completed in 2008 waited under 2 years; in 2015, 3 years; in 2023, 5 years. Northern Virginia now at 7 years; California at 9+ years. [[Google Intersect Power Acquisition — Introl - 2026-01-20]]
- **Completion rates.** Only 20% of projects requesting interconnection between 2000-2018 were operational by end of 2023. Solar 14%; battery 11%.
- **Withdrawal rate.** ~70% of projects ultimately withdraw during the wait. In 2023 alone, 1,250+ requests representing 200+ GW withdrew.
- **Project size growth (2015 → 2023).** Mean solar plants 250% larger; standalone batteries 330% larger; wind 66% larger.
- **Cost data.** Interconnection costs in 2019-2023 were 44% greater than during the preceding 5 years.
- **Regulatory recognition.** FERC ordered PJM (Dec 18, 2025) to overhaul rules for co-located and behind-the-meter large loads — first major regulatory acknowledgment that the queue mechanism cannot keep pace with hyperscaler demand. [[Microsoft Electricity Cost Recovery Commitment — POWER Magazine - 2026-01-22]]

## Tensions & Counterarguments

- **Vertical integration as queue bypass.** Google's acquisition of Intersect Power and Microsoft's Brookfield deal both sidestep traditional interconnection queues by co-locating generation with load (behind-the-meter). Whether this becomes the dominant pattern or remains supplemental to grid-scale connection is open.
- **Withdrawal-rate framing.** The 70% withdrawal rate is sometimes cited as evidence the queue is "self-cleansing." LBNL's analysis suggests instead that withdrawal indicates structural failure: projects reach the front of the queue at price points or timelines that no longer support the economics that justified them.
- **The queue isn't a single entity.** "The queue" is shorthand for seven different RTO queues running on different rules; reform of one (FERC's December 2025 PJM order) doesn't reform the others. Cross-RTO comparison requires reading each separately.

## Related Concepts

- [[AI Buildout Grid Constraint]] — master concept; this concept is the document-class layer of that bottleneck
- [[Chokepoint Control]] — the queue functions as a chokepoint specifically because RTOs are the sole legitimate path to grid-scale generation deployment
- [[Hyperscaler Vertical Integration]] — the dominant workaround pattern (deferred stub)

## Key Sources

- [[US Interconnection Queue Twice Installed Capacity — Latitude Media - 2024-04-11]]
- [[Google Intersect Power Acquisition — Introl - 2026-01-20]]
- [[Microsoft Electricity Cost Recovery Commitment — POWER Magazine - 2026-01-22]]
- [[Big Tech Promised $650B Data Centers Most Not Being Built — Bricks & Bytes - 2026-04-28]]
