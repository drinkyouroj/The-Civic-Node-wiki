---
title: "The $71 Billion Bluff"
subtitle: "OpenAI's letter of intent was non-binding. The market panic it triggered wasn't. Inside the deal that broke DRAM pricing for three years."
type: draft
version: 6
template: system-audit
trigger: named-hypocrisy
status: review
created: 2026-04-11
word_count: ~1,480
article_series: "DRAM Crisis (1 of 2)"
---

# The $71 Billion Bluff

## OpenAI's letter of intent was non-binding. The market panic it triggered wasn't. Inside the deal that broke DRAM pricing for three years.

There's a number that doesn't make sense right now, and it's $400.

That's what a 32GB DDR5 memory kit costs in April 2026.[^1] It was $120 eighteen months ago. In the interim, OpenAI cut its spending target by 57%.[^2] Its flagship data center expansion is dead.[^3] Its video platform is dead. Google published a technique that compresses AI memory needs by a factor of six.[^4] Half of all planned US data centers have been delayed or cancelled.[^5] Chinese memory stockpilers are panic-selling at losses.[^6]

Every signal in the market says DDR5 should be falling. It's not. HP says memory now accounts for 35% of a PC's build cost, up from 15%.[^7] Gartner projects the sub-$500 entry-level PC segment will disappear by 2028.[^8] Micron exited its consumer Crucial brand entirely.[^9] Phone prices are climbing 6-8% with no ceiling in sight.[^10]

The price is $400 because last October, one man signed a piece of paper worth $71.3 billion that carried no legal obligation[^11] — and the panic it caused is still locked into binding contracts that won't expire until 2028.

---

## The Source Code: How a Non-Binding Letter Became a Binding Market

On October 1, 2025, Sam Altman signed simultaneous letters of intent with Samsung and SK Hynix — the two companies that, together with Micron, control 95% of the world's memory production.[^12] The deals reserved approximately 900,000 DRAM wafer starts per month out of roughly 2.2 million in global capacity. OpenAI had just claimed 40% of it.[^12]

Neither supplier knew about the other's deal.[^13]

The LOIs were non-binding. That distinction matters legally and matters almost nowhere else. Analyst estimates valued the combined commitment at $71.3 billion over four years.[^11] The market didn't pause to check whether the signature carried legal weight; it treated the demand signal as real and priced accordingly. DRAM contract prices rose 171% year-over-year by Q3 2025.[^14] A 64GB DDR5 kit went from $180 in May to $710 by December — a 294% increase in seven months.[^15]

Then came the panic buying. As suppliers tightened validity periods on quotes,[^21] Apple stationed purchasing executives in extended hotel stays near Samsung's Hwaseong fabrication complex, negotiating two- to three-year binding supply agreements.[^16] LPDDR5X prices hit $70 per unit — a 230% increase — and Samsung became Apple's largest DRAM supplier, accounting for 60-70% of iPhone 17 series memory.[^16] AMD's Lisa Su flew to South Korea personally and met Samsung Vice Chairman Lee Jae-yong to sign a memorandum of understanding for HBM4 and DDR5 supply.[^17] Amazon and Microsoft ran the same playbook. Everyone was locking in multi-year contracts at peak prices because nobody could afford to be the company that didn't.

Here's the part that should bother you: OpenAI's demand signal was, by every subsequent indication, a bluff.

By February 2026, OpenAI had cut its compute spending target from $1.4 trillion to $600 billion — a 57% reduction.[^2] In March, the Stargate data center expansion in Abilene, Texas was killed after Oracle's financing collapsed.[^3] The Sora video platform was shuttered. The company was burning $8 billion a year against $13.1 billion in revenue[^2] and had just acquired a podcast with 58,000 YouTube subscribers for a reported sum in the low hundreds of millions. Samsung quietly shifted 80,000 wafer starts back to standard DDR5 production.[^18] The LOIs are, by all functional measures, abandoned.

But the contracts Apple, Amazon, and Microsoft signed during the panic are real. They're binding. They run through 2027 and 2028. The bluffer walked away; the damage is structural.

Samsung, for its part, posted Q1 2026 operating profit of 57.2 trillion won — $37.92 billion, an 8.5x jump year-over-year.[^19] The chip division generated 95% of it.[^19] That's not a technology company posting strong earnings. That's a memory company printing money because a non-binding letter rearranged the global supply chain in its favor.

---

## The Bigger Picture: One Bluff Exposes a Structural Flaw

It would be convenient to frame this as an OpenAI story — one company's overreach, one executive's audacity. But the mechanism is more important than the actor.

Three companies control 95% of global memory production.[^12] In a market that concentrated, a single credible demand signal can break pricing for years. Altman didn't need a binding contract. He needed Samsung and SK Hynix to believe the demand was real long enough for everyone else to panic — and in a three-producer market, that threshold is remarkably low. The LOIs exploited a structural chokepoint the same way a state actor exploits a geographic one. Iran doesn't need to sink a tanker in the Strait of Hormuz; it needs to make insurers believe it might. The mechanism is identical: control the bottleneck, and the signal alone moves the market.

This is also a story about how speculative demand becomes real economic damage. The AI hype cycle produced demand projections that justified procurement frenzies that locked in prices that now persist regardless of whether the projections were right. The speculation collapsed. The contracts didn't. Consumers paying $400 for DDR5, or 6-8% more for a phone,[^10] are absorbing the cost of an investment thesis that no longer exists — but the supply agreements written during the thesis's peak are still governing prices.

The timeline for relief is mid-2027 at the earliest, when new factory capacity comes online. The real price correction probably arrives in 2028, when Chinese competitors CXMT and YMTC enter volume production[^20] and break the three-company stranglehold. That's the subject of a follow-up piece.

Until then, the price is $400 because a $71 billion letter of intent — non-binding, never fulfilled, functionally abandoned — panicked the world's largest technology companies into contracts they'll be paying on for three more years.

---

## My Debug: Decentralized Hardware, Centralized Supply Chain

I run DePIN infrastructure. The irony of operating decentralized hardware while the most centralized supply chain on earth dictates what that hardware costs is not lost on me.

The RAM in my nodes is the same RAM in your laptop, priced by the same three companies, moved by the same panic. The whole thesis of decentralized infrastructure is that no single actor should be able to hold the network hostage. And yet here we are: one man's non-binding signature on two pieces of paper, and every node operator, every PC builder, every phone buyer on the planet is paying the tax.

The question this newsletter keeps returning to is: who controls power, and do individuals have any recourse? In the DRAM market, the answer is three companies and no. The efficiency gains won't save you; the Chinese competition is two years away; the contracts are already signed.

The letter was non-binding. The price isn't.

---

[^1]: TrendForce, ["DDR5 Retail Prices Pullback Amid Market Correction,"](https://www.trendforce.com/news/2026/03/31/news-ddr5-retail-prices-pullback-amid-market-correction-but-industry-players-cite-stable-contract-trends/) March 31, 2026.
[^2]: Futurism, ["OpenAI Massively Cuts Spending Plan as Reality Closes In,"](https://futurism.com/artificial-intelligence/openai-cuts-spending-plan) February 2026.
[^3]: Bloomberg, ["Oracle and OpenAI End Plans to Expand Flagship Data Center,"](https://www.bloomberg.com/news/articles/2026-03-06/oracle-and-openai-end-plans-to-expand-flagship-data-center) March 6, 2026.
[^4]: Google Research Blog, "TurboQuant: 6x LLM Context Window Compression," March 25, 2026.
[^5]: Futurism / Sightline Climate, ["Almost Half of US Data Centers Slated to Be Canceled or Delayed,"](https://futurism.com/science-energy/data-centers-construction-supply) 2026.
[^6]: WCCFTech, ["Chinese Memory Vendors Are Claiming to Be Doomed,"](https://wccftech.com/chinese-memory-vendors-are-claiming-to-be-doomed/) March 2026.
[^7]: Tom's Hardware, ["HP says memory costs doubled to 35% of PC build materials,"](https://www.tomshardware.com/tech-industry/hp-says-memory-costs-doubled-to-35-percent-of-pc-build-materials-in-one-quarter) February 2026. HP Q1 2026 earnings call.
[^8]: Gartner, ["Surging Memory Costs Will Reduce Global PC and Smartphone Shipments in 2026,"](https://www.gartner.com/en/newsroom/press-releases/2026-02-26-gartner-says-surging-memory-costs-will-reduce-global-pc-and-smartphone-shipments-in-2026) February 26, 2026.
[^9]: Tom's Hardware, ["Micron is killing Crucial SSDs and memory in AI pivot,"](https://www.tomshardware.com/pc-components/dram/micron-is-killing-crucial-ssds-and-memory-in-ai-pivot-company-refocuses-on-hbm-and-enterprise-customers) December 2025. See also: [Micron investor relations announcement.](https://investors.micron.com/news-releases/news-release-details/micron-announces-exit-crucial-consumer-business)
[^10]: IDC, ["Global Memory Shortage Crisis: Market Analysis,"](https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/) 2026. Smartphone ASPs up 6-8% in pessimistic scenario. See also: [TechSpot coverage.](https://www.techspot.com/news/110679-memory-shortages-raise-pc-smartphone-prices-8-2026.html)
[^11]: Light Reading, ["OpenAI orders $71B in Korean memory chips,"](https://www.lightreading.com/ai-machine-learning/openai-orders-71b-in-korean-memory-chips) October 2, 2025. LOI valued at 100 trillion won ($71.3B) over four years; reported one day after signing.
[^12]: Bizety, ["The 'Dirty DRAM Deal' — How OpenAI Just Locked Up 40% of Global RAM,"](https://bizety.com/2025/12/28/the-dirty-dram-deal-how-openai-just-locked-up-40-of-global-ram/) December 28, 2025. Global capacity figures from TechInsights/TrendForce.
[^13]: Moore's Law Is Dead, ["Sam Altman's Dirty DRAM Deal,"](https://www.mooreslawisdead.com/post/sam-altman-s-dirty-dram-deal) 2025. Dual-deal structure; neither supplier aware of parallel agreement.
[^14]: Tom's Hardware, ["DRAM prices skyrocket 171% year-over-year,"](https://www.tomshardware.com/pc-components/dram/dram-prices-surge-171-percent-year-over-year-ai-demand-drives-a-higher-yoy-price-increase-than-gold) Q3 2025. TrendForce contract price data.
[^15]: Resell Calendar, ["The RAM Price Crisis is Getting Worse,"](https://resellcalendar.com/news/news/ram-price-december-2025-ai-spike-reseller/) December 19, 2025. DDR5-5600 64GB kit ~$180 (May) to ~$710 (December); PCPartPicker tracking data.
[^16]: WCCFTech / Korea Economic Daily, ["Apple Executives Booking Extended Hotel Stays for DRAM LTA,"](https://wccftech.com/apple-executives-booking-extended-hotel-stays-to-book-dram-lta-from-samsung-and-sk-hynix/) 2026.
[^17]: Samsung / AMD, ["Samsung and AMD Expand Strategic Collaboration,"](https://www.amd.com/en/newsroom/press-releases/2026-3-18-samsung-and-amd-expand-strategic-collaboratio.html) Press Release, March 18, 2026.
[^18]: Digitimes, ["Samsung shifts focus from HBM to DDR5 modules for higher profits,"](https://www.digitimes.com/news/a20251208PD214/samsung-hbm-ddr5-dram-capacity.html) December 2025. Samsung reallocated ~80,000 wafers/month from HBM to DDR5. See also: [TweakTown coverage.](https://www.tweaktown.com/news/109259/samsung-shifts-focus-from-hbm-to-ddr5-modules-ddr5-ram-results-in-far-more-profits-than-hbm/index.html)
[^19]: Reuters, ["Samsung flags eightfold jump in quarterly profit,"](https://www.reuters.com/sustainability/sustainable-finance-reporting/samsung-flags-eight-fold-jump-q1-profit-ai-chip-demand-drives-up-prices-2026-04-06/) April 6, 2026.
[^20]: Tom's Hardware / Nikkei Asia, ["China's CXMT and YMTC to Expand Memory Output,"](https://www.tomshardware.com/pc-components/dram/chinas-cxmt-and-ymtc-to-expand-memory-output) 2026.
[^21]: Sourceability, ["The Memory Shortage Is Driving Higher Costs for Buyers and Consumers,"](https://sourceability.com/post/the-memory-shortage-is-driving-higher-costs-for-buyers-and-consumers) 2026. Suppliers tightened validity periods on quotes; buyers shifted from quarterly pricing windows to expedited procurement cycles.
