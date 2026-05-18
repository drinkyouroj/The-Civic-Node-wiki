---
title: "Bloom Energy"
type: entity
entity_type: organization
tags: [infrastructure, power, ai, energy, hyperscaler]
created: 2026-05-18
updated: 2026-05-18
sources: 6
---

## Overview

Bloom Energy is a solid-oxide fuel-cell manufacturer providing on-site power generation. Until 2025–2026, Bloom's installed base was concentrated in mid-scale commercial and industrial deployments. The April 2026 Oracle Project Jupiter announcement (up to 2.8 GW agreement, 1.2 GW already contracted) moves Bloom into the hyperscaler-primary-power category for the first time at GW scale.

## Key facts

- Fuel-cell technology operates without combustion; minimal water use [[Oracle Project Jupiter Bloom Fuel Cells — DCK - 2026-04-29]]
- NOx emissions reduced ~92% versus conventional gas turbine generation [[Oracle Project Jupiter Bloom Fuel Cells — DCK - 2026-04-29]]
- Oracle Project Jupiter agreement: up to 2.8 GW total, 1.2 GW already contracted [[Oracle Project Jupiter Bloom Fuel Cells — DCK - 2026-04-29]]
- Project Jupiter campus: up to 2.45 GW on-site microgrid capacity (single integrated microgrid) [[Oracle Project Jupiter Bloom Fuel Cells — DCK - 2026-04-29]]
- Operating constraint: fuel cells "have very limited capacity to handle overloading" and operate optimally at steady power consumption (Prithpal Khajuria, Intel) [[Oracle Project Jupiter Bloom Fuel Cells — DCK - 2026-04-29]]

## Newsletter relevance

Bloom is the operating partner for the most explicit hyperscaler-exits-the-grid move documented so far. The Oracle agreement makes fuel-cell microgrids the primary power architecture rather than the backup. This is the technology behind the [[Speed to Power]] story when the speed is being prioritized over grid resilience and overload protection.

## Connections

- [[Oracle]] — Project Jupiter anchor customer
- [[BorderPlex Digital Assets]] — Project Jupiter co-partner
- [[Speed to Power]] — concept the deployment exemplifies
- [[Behind the Meter Generation]] — architectural category
- [[AI Buildout Grid Constraint]]

## Source appearances

- [[Oracle Project Jupiter Bloom Fuel Cells — DCK - 2026-04-29]]

## Open questions

- What's Bloom's full 2026 backlog beyond the Oracle 2.8 GW commitment? Are other hyperscalers in similar-stage negotiations?
- How does Bloom's fuel-cell economics compare to behind-the-meter natural gas at GW scale? (The Enki AI piece's $1.6B for ~1 GW of Williams gas suggests fuel cells must be cost-competitive even before counting emissions reductions.)
- The Khajuria comment on overload limits is significant — has Oracle's design accounted for AI-workload spikes (training-run peaks, inference burst)? Or is the bet that AI workloads are steady enough that overload protection is no longer the binding constraint?
