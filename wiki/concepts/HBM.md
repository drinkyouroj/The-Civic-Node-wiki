---
title: "HBM"
type: concept
tags: [technology, infrastructure, ai, supply-chain]
created: 2026-05-18
updated: 2026-05-18
sources: 7
---

## Definition

HBM (High Bandwidth Memory) is a stacked-die DRAM architecture used as the memory layer for AI accelerators. HBM is physically packaged adjacent to the GPU or accelerator die (often via 2.5D interposer or 3D stacking) to deliver the memory bandwidth modern AI workloads require. Without HBM, accelerators cannot run at scale. Production is concentrated in a small number of Korean fabs operated by [[Samsung]] and [[SK Hynix]], with [[Micron]] as a third entrant.

## Why it matters for the newsletter

HBM is the supply layer of the AI buildout that mainstream coverage tracks least, but which has the highest concentration risk. Compute (GPUs) and grid (power/interconnect) get most of the coverage. Memory — specifically HBM — is the binding constraint that makes the entire stack work, and it sits in a handful of Korean fabs subject to Korean labor relations, Korean industrial policy, and (per the [[2026 Global Helium Supply Crisis]]) Korean helium imports from Qatar.

The four-layer chokepoint vocabulary (compute, memory, packaging, grid) makes HBM the second of four AI-supply chokepoints worth tracking by name.

## Evidence & examples

- Q1 2025 HBM market share: [[Samsung]] 17%, [[SK Hynix]] 62%, [[Micron]] 21% [[Samsung HBM Strike Could Wrench AI Boom — Fortune - 2026-05-17]]
- [[Samsung]] HBM4 production run "already sold out" [[Samsung HBM Strike Could Wrench AI Boom — Fortune - 2026-05-17]]
- [[Apple]] negotiated emergency memory contracts at 100% price increase [[Samsung HBM Strike Could Wrench AI Boom — Fortune - 2026-05-17]]
- The struck plants in the May 2026 [[Samsung]] union walkout are the HBM memory lines specifically [[Samsung Partial Injunction Against Union — Korea Herald - 2026-05-18]]
- Memory fab is helium-intensive due to repeated high-heat etching and deposition steps for 3D stacking [[Samsung]] entity page

## Tensions & counterarguments

- HBM concentration is sometimes argued to be reducing — Micron's 21% Q1 2025 share is up from prior years. The counter is that the AI demand growth rate exceeds the rate at which Micron and others can take share, so concentration remains structurally high in absolute terms even if market share is shifting at the margins.
- An offsetting argument from the chip side: as AI workloads diversify (inference vs. training), memory bandwidth requirements diverge, and HBM may matter less for inference-heavy deployments. The counter is that frontier training (the most-discussed AI capex driver) still depends on HBM.

## Related concepts

- [[Chokepoint Control]] — HBM is the memory chokepoint in the AI supply stack
- [[AI Buildout Grid Constraint]] — the grid chokepoint, paired with HBM as memory chokepoint
- [[2026 Global Helium Supply Crisis]] — helium supply is upstream of HBM fabrication

## Key sources

- [[Samsung HBM Strike Could Wrench AI Boom — Fortune - 2026-05-17]]
- [[Samsung Partial Injunction Against Union — Korea Herald - 2026-05-18]]
