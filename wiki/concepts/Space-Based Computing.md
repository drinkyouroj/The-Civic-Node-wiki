---
title: "Space-Based Computing"
type: concept
tags: [technology, ai, infrastructure, space, china]
created: 2026-04-27
updated: 2026-04-27
sources: 6
---

## Definition
AI compute infrastructure deployed on satellites in orbit, performing inference and training in space rather than in terrestrial data centers. The architecture targets: (1) energy efficiency (space solar panels several × ground photovoltaics; near-absolute-zero passive cooling); (2) coverage (70% of land + 95% of oceans are network blind zones for ground compute); (3) supply-chain insulation (compute not subject to terrestrial DRAM / helium / power-grid chokepoints). China is the first nation building this at scale: [[ADAspace]]'s 2,800-satellite "star compute" plan + [[Zhejiang Lab]]'s "Three-Body Computing Constellation" (100 satellites by 2027).

## Why It Matters for the Newsletter
The architectural workaround to the wiki's [[AI DRAM Crisis]] and [[Helium]] terrestrial-chokepoint coverage. The Chinese strategic vision — "intelligent computing as universal public service, like water and electricity" (Zhao Hongjie, ADAspace) — is the most ambitious challenge yet to U.S.-controlled compute supply chains. If the architecture works at scale, U.S. export controls on semiconductors become structurally less binding. Newsletter angle: track the technology from "claimed working in orbit" (Nov 2025: Qwen3 in-orbit inference) through "delivering inference and training at promised scale" (claimed: 10⁵-petaflop inference, 10⁶-petaflop training by 2035).

## Evidence & Examples
- **ADAspace** (Chengdu): 2,800-satellite constellation; first batch May 2025; Qwen3 LLM deployed in orbit November 2025; **Prometheus** commercial cloud platform launched March 26, 2026; first space-to-ground robot control demo with [[Shanghai Jiao Tong University]]
- **Zhejiang Lab** "Three-Body Computing Constellation": 12 satellites May 2025; 100 by 2027; 10 AI models validated in orbit
- **State support**: [[MIIT]] standards system, [[CNSA]] pre-project assessment for state constellation, CAICT industry estimate ¥250B (~$36.6B) by 2030
- The downlink problem: Zhejiang Lab's Li Chao reports "up to 90 percent of the data generated in space is lost and never effectively processed" with traditional satellites — solved by in-orbit AI processing

## Tensions & Counterarguments
- **The maintenance constraint is structural.** Yan Zhiyong (China Telecom Cloud): "Post-launch maintenance of satellites is, notably, prohibitively expensive or even impossible." Once on orbit, hardware can't be patched, repaired, or upgraded. Failure modes are different from "data center power outage" — and the failure cost (replacement satellite launch) is higher.
- **State-media optimism bias.** Source ([[China Space Computing Constellation — SCIO]]) is the China State Council Information Office — promotional by design. Treat 2030 / 2035 timelines as aspirational. Treat technical milestones already achieved (Qwen3-in-orbit, Prometheus, robot control) as more reliable.
- **Western counterpart absent — partial answer.** The wiki now includes a U.S. *doctrinal* counterpart: the Space Force's "Future Operating Environment 2040" report ([[Space Force Future Operating Environment 2040 — Washington Times]]) frames the same orbital domain as a battlefield and forecasts Chinese in-orbit AI, brain-computer interfaces, and metamaterial satellite "invisibility" as 2040 capabilities. **Doctrinal awareness is U.S.; civilian compute-in-orbit infrastructure is Chinese.** Whether U.S. or European labs are pursuing comparable civilian deployments quietly remains unconfirmed.
- **Latency and bandwidth.** Inter-satellite laser links are claimed but unproven at constellation scale. The published "<2 minutes" Qwen3 inference figure in November 2025 isn't competitive with terrestrial data center inference (sub-second); the value proposition lives in coverage, not in raw speed.

## Related Concepts
- [[AI DRAM Crisis]] — the chokepoint this answers
- [[Helium]] — secondary terrestrial chokepoint
- [[Frontier AI]]
- [[Tech-State Conflict]] — China's response to U.S. export controls

## Key Sources
- [[China Space Computing Constellation — SCIO]] — civilian architecture; ADAspace, Zhejiang Lab, Qwen3-in-orbit
- [[Space Force Future Operating Environment 2040 — Washington Times]] — U.S. military doctrinal counterpart; "unrestricted spectrum warfare" framing; forecast of PLA in-orbit AI, BCI, metamaterials
