---
title: "From ground to orbit: China eyes computing in space"
type: source
tags: [technology, ai, china, space, infrastructure, geopolitics]
created: 2026-04-27
updated: 2026-04-27
sources: 14
raw: "raw/From ground to orbit China eyes computing in space.md"
source_url: "http://english.scio.gov.cn/chinavoices/2026-04/27/content_118464689.html"
author: "Zheng Chengqiong (郑成琼) — China State Council Information Office"
published: 2026-04-27
---

[Original source](http://english.scio.gov.cn/chinavoices/2026-04/27/content_118464689.html)

## Summary
Chinese state media (SCIO) profile of China's emerging **space-based computing infrastructure**. Chengdu-based [[ADAspace]] is building a 2,800-satellite "star compute" constellation: 2,400 inference satellites + 400 training satellites in dawn-dusk, sun-synchronous, and low-inclination orbits at 500–1,000 km. First batch launched May 2025; goal is 1,000-satellite scale by 2030, full 2,800 by 2035. Compute targets: hundred-thousand-petaflop inference, million-petaflop training. Already deployed: [[Alibaba]]'s Qwen3 LLM in orbit (in-orbit inference <2 minutes); first space-to-ground robot control (with Shanghai Jiao Tong University); the **Prometheus** commercial cloud platform (March 26, 2026). [[Zhejiang Lab]]'s parallel "Three-Body Computing Constellation" — 12 satellites in May 2025, 100 by 2027, with 10 AI models already validated in orbit. China's space computing industry projected at **¥250B (~$36.6B) by 2030** (CAICT).

## Key Points
- ADAspace "star compute": 2,800 satellites total — 2,400 inference + 400 training
- Orbit profile: 500–1,000 km, dawn-dusk + sun-synchronous + low-inclination
- Compute targets: 10⁵-petaflop inference, 10⁶-petaflop training; goal full 2,800 by 2035
- May 2025: first batch launched
- November 2025: Alibaba Qwen3 LLM deployed in orbit; in-orbit inference <2 minutes — claimed first ever
- March 26, 2026: Prometheus space-computing cloud platform launched (with MIIT)
- First-ever space-based computing power controlling a ground robot (with Shanghai Jiao Tong University)
- Zhejiang Lab "Three-Body Computing Constellation": 12 satellites May 2025; 100 satellites by 2027; 10 AI models already validated
- Industry rationale per researcher Yan Zhiyong (China Telecom Cloud):
  - Global data centers consume 1.5% of world electricity; 40% of that is cooling
  - 70% of land + 95% of oceans are network blind zones for ground compute
  - Transoceanic fiber struggles with real-time interaction
  - Ground centers vulnerable to natural disasters
  - Space: solar generation efficiency several × ground photovoltaics; near-absolute-zero cooling = energy savings
- Constraints (per Yan): vacuum, extreme temperature, microgravity, radiation; chip cooling on board; **post-launch maintenance is prohibitively expensive or impossible** (load-bearing limitation)
- Zhejiang Lab's Li Chao: traditional satellites are "severely deficient in downlinking" — up to 90% of space-generated data is lost
- CAICT estimate: ¥250B (~$36.6B USD) Chinese space-compute industry by 2030
- China National Space Administration (CNSA) running pre-project assessment for state-level intelligent computing constellation
- MIIT actively building standards system + radiation-resistant chip + inter-satellite laser comms R&D

## Newsletter Angles
- **The chokepoint workaround.** While the wiki's [[AI DRAM Crisis]] and [[Helium]] clusters document terrestrial-compute supply choke (OpenAI's Samsung/SK Hynix lockup, Qatar helium offline), China is building *the architectural workaround* — placing compute beyond the terrestrial supply chain entirely. This is a structural, not rhetorical, response to U.S. export controls and chokepoint pressure. The "intelligent computing as public utility, like water and electricity" framing (Zhao quote at end) is the strategic vision.
- **In-orbit deployment of Qwen3 in November 2025 is a generational technical milestone** — first general-purpose LLM running entirely in orbit. It validates the architecture before the constellation is built out. The wiki should track when comparable Western (NASA/SpaceX/Anthropic/OpenAI) demonstrations occur or fail to occur.
- **State-media framing matters.** SCIO is the China State Council Information Office — this is *self-reported* progress, optimistic by design. Treat ADAspace's targets (2,800 satellites by 2035) as aspirational; treat the milestones already achieved (12 satellites in orbit, Qwen3 inference, Prometheus launch) as more reliable. The industry-projection figure (¥250B by 2030) is a CAICT estimate — also optimistic.
- **The maintenance constraint is the structural weak point.** Yan's "prohibitively expensive or impossible" line on satellite repair is the limit Western analysis should focus on. Once on orbit, hardware can't be patched the way ground compute can. Failure modes are different from "data center power outage."

## Entities Mentioned
- [[ADAspace]] — Chengdu commercial aerospace; "star compute" lead
- Zhao Hongjie — ADAspace executive VP
- [[Zhejiang Lab]] — Hangzhou; "Three-Body Computing Constellation"
- Li Chao — Zhejiang Lab space-based computing research center director
- [[Alibaba]] — Qwen3 LLM deployed in orbit
- [[Shanghai Jiao Tong University]] — partner on space-to-ground robot control
- [[China Telecom Cloud]] — Yan Zhiyong's affiliation
- [[CAICT]] — China Academy of Information and Communications Technology; ¥250B estimate
- Xie Lina — CAICT researcher
- [[CNSA]] — China National Space Administration; pre-project assessment
- Yu Guobin — CNSA deputy director, commercial space
- [[MIIT]] — Ministry of Industry and Information Technology
- [[Jiuquan Satellite Launch Center]] — May 2025 launch site

## Concepts Mentioned
- [[Space-Based Computing]] — emerging concept
- [[AI DRAM Crisis]] — the terrestrial chokepoint this is structurally answering
- [[Frontier AI]]
- [[Tech-State Conflict]] — China's state-orchestrated answer to U.S. export controls
- [[Computing as Public Utility]] — the strategic vision Zhao articulates

## Quotes
> "This technological validation means that in the future, when ground networks are unavailable, we can directly call upon space-based computing power via satellites to command intelligent agents like humanoid robots, quadruped robot dogs, autonomous vehicles and drones, enabling operations without blind spots." — Zhao Hongjie, ADAspace EVP

> "In the future, space-based computing power will become a universal public service, just like water and electricity." — Zhao Hongjie

> "Currently, up to 90 percent of the data generated in space is lost and never effectively processed." — Li Chao, Zhejiang Lab

## Notes
Chinese state-media source (SCIO) — primary purpose is industrial promotion, not neutral reporting. Treat the technical milestones (Qwen3 in orbit, Prometheus platform, robot control) as reliable but the constellation timelines (2030/2035) and industry-size projections (¥250B by 2030) as aspirational. **No Western-source corroboration is in the wiki yet** — Source Gap: track for confirmation by Reuters / FT / Bloomberg / NASA-side analysts. Specific load-bearing claims to verify externally: (a) Qwen3-in-orbit inference latency; (b) the May 2025 Jiuquan launch; (c) the Prometheus platform's actual customer base.
