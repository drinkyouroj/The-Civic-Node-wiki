---
title: "Interconnection Queue"
type: concept
tags: [power, infrastructure, grid, regulation, ferc]
created: 2026-05-07
updated: 2026-05-13
sources: 8
---

## Definition

The administrative and engineering process by which proposed power generation, storage, or large-load projects request connection to the US transmission grid. Each Regional Transmission Organization (RTO) — PJM, ERCOT, MISO, SPP, ISO-NE, NYISO — maintains its own queue. Projects are studied for grid impact, assigned interconnection costs, and scheduled for energization. The queue is public, updated quarterly or annually, and dispositive: a project with PPAs but no queue position is a press release; a project with queue position is real.

## Why It Matters for the Newsletter

The interconnection queue is the document class that decides which AI data center projects actually deliver in 2026-2030. Financial press AI capex coverage rarely cites it; the queue is the first place the binding constraint shows up and the last place chip-layer analysts look. Vocabulary central to the [[AI Buildout Grid Constraint]] thesis. Provides the analytical edge for the operator-class reader: read the PUC and FERC filings, track the queue depth, ignore the press release.

## Evidence & Examples

- **Total queue size (2025 edition).** ~2,290 GW active queue vs. ~1,322 GW installed capacity — LBNL framing: "nearly twice" installed capacity. [[Queued Up 2025 Edition — LBNL - 2025-12-15]]
- **Prior edition (2024).** ~2,600 GW queued vs. ~1,279 GW installed; the 12% queue decrease is attributed to FERC Order 2023 forcing withdrawal of speculative projects, not reduced demand. [[US Interconnection Queue Twice Installed Capacity — Latitude Media - 2024-04-11]]
- **Active project count.** 10,303 active projects; ~1,400 GW generation + ~890 GW storage.
- **Wait time — US average.** Median IR-to-COD for 2024 completions: 55 months (4.6 years); LBNL frames as "over 4 years" for 2018–2024 cohort. Projects completed in 2008 waited under 2 years; 2015: 3 years; 2023: 5 years. [[Queued Up 2025 Edition — LBNL - 2025-12-15]]
- **Wait time — regional.** Northern Virginia now at 7 years; California at 9+ years. [[Google Intersect Power Acquisition — Introl - 2026-01-20]]. CAISO median ~75–94 months (~6–8 years); PJM median ~68 months (~5.7 years) for 2024 cohort. [[Queued Up 2025 Edition — LBNL - 2025-12-15]]
- **Completion rates.** 19% of projects (13% of capacity) from 2000–2019 cohort reached commercial operation by end of 2024. Solar 14%; battery 11% (2024 edition figures). [[Queued Up 2025 Edition — LBNL - 2025-12-15]]
- **Withdrawal rate.** ~70% of projects ultimately withdraw; 77% of capacity from 2000–2019 cohort withdrew. ~700+ GW withdrew in 2024; ~500 GW new requests submitted same year. [[Queued Up 2025 Edition — LBNL - 2025-12-15]]
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

- [[Queued Up 2025 Edition — LBNL - 2025-12-15]] ← primary; most current authoritative data
- [[US Interconnection Queue Twice Installed Capacity — Latitude Media - 2024-04-11]] ← 2024 edition figures
- [[Google Intersect Power Acquisition — Introl - 2026-01-20]]
- [[Microsoft Electricity Cost Recovery Commitment — POWER Magazine - 2026-01-22]]
- [[Big Tech Promised $650B Data Centers Most Not Being Built — Bricks & Bytes - 2026-04-28]]
