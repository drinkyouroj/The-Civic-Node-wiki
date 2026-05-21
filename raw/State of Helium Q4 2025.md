---
title: "State of Helium Q4 2025"
source: "https://messari.io/report/state-of-helium-q4-2025"
author:
  - "[[Matthew Nay]]"
  - "[[Alexander Beaudry]]"
published: 2026-03-05
created: 2026-05-16
description: "An analysis of Helium's financial, network, and ecosystem activity in Q4 2025."
tags:
  - "clippings"
---
## Key Insights

- Helium Network offloaded 4,388 TB of data from major US mobile carriers in Q4 2025, up 60.7% from just 2,731 TB in Q3. By the end of Q4, the total amount of data offloaded since inception was over 9,840 TB.
- Average daily users of the network grew 32.4% QoQ to 1.6 million. The network set a new record in Q4, surpassing 2 million daily active users for the first time, and reaching a maximum of 2.5 million on December 20.
- Helium’s annualized revenue reached $11.0 million, when removing all discretionary subscriber revenue burn. Average daily total data credit (DC) burns grew 83.6% QoQ to $56,760.
- Over 595,800 total accounts have signed up for Helium Mobile as of December 31, a 29.1% QoQ increase.
- Helium partnered with Mambo WiFi in Brazil. Mambo WiFi supports major carriers and tens of millions of customers through 40K+ access points across the country, which will serve as the foundation for Helium's expansion into South America.

## Primer

Helium ([HNT](https://messari.io/project/helium)) is a decentralized wireless network that provides both cellular ([Mobile](https://www.helium.com/mobile)) and low-power Internet of Things ([IoT](https://www.helium.com/iot)) connectivity. It is the world’s first “people-built” wireless network and addresses the challenge of high 5G infrastructure costs faced by traditional mobile carriers. By decentralizing coverage through a token-based model, it enables high-density cellular coverage without the typical expenses of real estate or site management. Participants who deploy hotspots earn [HNT tokens](https://docs.helium.com/tokens/hnt-token#hnt-usage) as incentives for expanding network coverage. The primary growth driver for the [Helium Network](https://docs.helium.com/mobile/5g-on-helium) has been its [Carrier Offload Program](https://messari.io/copilot/share/understanding-helium-s-carrier-offload-145bb322-e5ba-4c87-9c69-dafc35296a28#:~:text=Carrier%20Offload%20Program%3A%20This%20program,utilizing%20Helium's%20network%2012.), which establishes partnerships with telecom companies. The program allows mobile customers of legacy telecom companies such as AT&T and Telefónica’s Movistar to connect to Helium Hotspots in areas where the community network extends carriers’ service at a lower cost. End users, through partner carriers, seamlessly connect to a nearby community-deployed Mobile Hotspot (which acts like a mini cell tower).

Another growth area driving Network use is the eponymous [Helium Mobile](https://heliummobile.com/), a unique Mobile Virtual Network Operator (MVNO) that provides its service by blending two sources of coverage: the community-powered network of Helium Mobile Hotspots and T-Mobile’s nationwide 5G network. Helium Mobile is directly aligned to the Helium Network as increased utilization of the community-powered network lowers its cost per user.

The Helium Network [launched](https://techcrunch.com/2019/06/12/helium-network/) in 2019 with an IoT network on its purpose-built Layer-1 blockchain for peer-to-peer wireless infrastructure. Users could send data to and from the Internet, and protocol miners were rewarded with HNT tokens for providing wireless network coverage. [Notable examples](https://www.helium.foundation/protocol-report) include its use in flood detection in Portugal and monitoring humidity and temperature for museums. What began as a purpose-built IoT network has since expanded into a broader wireless ecosystem, with Helium’s Mobile Network as the flagship offering, and several enterprise carriers actively utilizing Helium for mobile offload.

Helium’s founding team has [raised](https://messari.io/project/helium/fundraising) over $360 million to date, including $200 million in its latest round in March 2022. For a full primer on the Helium Network, refer to our Initiation of Coverage [report](https://messari.io/report/understanding-helium-a-comprehensive-overview).

[Website](https://www.helium.com/) / [X](https://x.com/helium) / [Discord](https://discord.com/invite/helium)

## Key Metrics

![](https://cdn.sanity.io/images/2bt0j8lu/production/4994c6e3108ca0aa9b551e7964da0116b04e2415-2048x1168.png?w=714&fit=max&auto=format&dpr=3 "View full size")

## The Helium Team Commentary

*The Project Team Commentary section of this report was written by the Helium team and reflects the views, opinions, and forward-looking statements of Helium. This section is included to provide additional context on the project’s strategy, priorities, and outlook and does not necessarily reflect the views or opinions of Messari, Inc.*

The last three months have marked a definitive shift for Helium. The network has clearly moved beyond concept into a period of sustained operational maturity. Consistent growth in daily active usage from carrier partners confirms that the network is functioning as a trusted, production-grade extension of legacy telecommunications infrastructure.

### Solving the "Indoor Blind Spot"

Helium’s primary value proposition lies in its ability to solve the telecom industry’s most persistent margin-killer: the high cost of densification. Traditional carriers struggle with the prohibitive CAPEX and OPEX required to blanket high-traffic, indoor environments like transit hubs, casinos, and stadiums.

Helium effectively "crowdsources" this infrastructure, offering several strategic advantages:

Cost Efficiency: Carriers can bypass traditional deployment hurdles by tapping into a distributed network of community-managed hardware.

Hardware Versatility: The protocol’s ability to convert existing wireless hardware into the ecosystem accelerates time-to-market, also turning a historical cost into a productive asset for venue owners..

Data Granularity: Unlike traditional roaming or tower setups, Helium Hotspots deliver precise, localized Quality of Service (QoS) data and telemetry, providing carriers with visibility into the customer experience in indoor dead zones that were previously opaque or too expensive to monitor.

### Investor Outlook

From a macro perspective, Helium offers a unique play on the structural decentralization of wireless assets. The model successfully aligns the economic interests of individual operators with the cost-cutting mandates of major carriers. As the industry pivots toward extreme cost discipline and superior network intelligence, Helium stands as a leading example of how decentralized physical infrastructure (DePIN) can absorb traditional telecom overhead.

## Performance Analysis

### HNT Token

The Helium Network token ([HNT](https://messari.io/project/helium)) is the network’s primary token. It is distributed from the Helium DAO, minted through [inflationary emissions](https://docs.helium.com/tokens/hnt-token/#net-emissions), then [distributed](https://github.com/helium/HIP/blob/main/files/0077/token-emissions-as-of-solana-migration.pdf) to the network based on data offload and coverage. There are [three main functionalities](https://docs.helium.com/tokens/hnt-token/) for HNT:

1. Earn HNT by supplying network coverage and data transfer: Hotspot hosts and operators are [rewarded](https://docs.helium.com/tokens/hnt-token/#hnt-usage) in HNT for deploying and maintaining wireless infrastructure. Emissions are distributed based on validated coverage (Proof-of-Coverage) and data transfer activity, aligning token rewards with measurable network utility.
2. Buy [Data Credits](https://docs.helium.com/tokens/data-credit/) ([DC](https://solscan.io/token/dcuc8Amr83Wz27ZkQ2K9NS6r8zRpf1J6cvArEBDZDmm)) to access network functionalities: HNT can be [burned](https://docs.helium.com/tokens/hnt-token/#burn-and-mint-economics) to receive DC through the [Helium Wallet App](https://docs.helium.com/wallets/helium-wallet-app/), [Helium CLI](https://docs.helium.com/wallets/cli-wallet/), or [Data Credit Portal](https://docs.helium.com/tokens/data-credit-portal/). The value of a DC is fixed at $0.00001. The amount of DC users receive from burning HNT will be [determined](https://docs.helium.com/oracles/price-oracles/) by the [current price](https://www.pyth.network/price-feeds/crypto-hnt-usd) of HNT. In practice, this is seamless for customers, as most HNT burning and DC usage are handled by Helium Mobile, especially for the Carrier Offloading program. Carriers are billed for their usage in USD, then Helium burns the necessary HNT.
3. [Stake](https://docs.helium.com/governance/staking-with-helium-vote/) to receive veHNT and gain [governance votes](https://github.com/helium/HIP/blob/main/0051-helium-dao.md#vehnt-and-governance) for the [Helium DAO](https://heliumvote.com/hnt): Since the Helium Network acts as an overarching structure for its subnetworks, it requires its own governance mechanism. Members of the Helium DAO (i.e., HNT tokenholders) can participate in governance by staking HNT to receive veHNT. Under this structure, the longer HNT is staked, the more veHNT is received. This veHNT provides [proportional](https://docs.helium.com/governance/staking-with-helium-vote/#vote-power-multiplier) voting power to approve or reject proposals, such as [Helium Release Proposals](https://heliumvote.com/hnt) (HRPs) and Helium Improvement Proposals (HIPs), that shape the network’s future.

HNT is essential for using the network. Helium Network users must buy and “burn” HNT in order to receive Data Credits, which they can use to transfer data. Meanwhile, Helium Mobile subscribers have the crypto components abstracted away and simply pay for their monthly subscription in USD. The Helium Mobile entity then burns the required HNT for each subscriber's usage.

![](https://cdn.sanity.io/images/2bt0j8lu/production/99819817113812ceea8fab0e47d122bad1e5bc50-2048x1111.png?w=714&fit=max&auto=format&dpr=3 "View full size")

In Q4 2025, HNT’s [circulating market cap](https://messari.io/project/helium/charts/market) (USD) decreased 43.9% QoQ from $453.9 million to $254.7 million, resulting in its price falling from $2.44 to $1.37. The drop in market cap showed no correlation with Helium’s daily active users or DC consumption, both of which increased in Q4. Instead, it mirrored the broader crypto market, which declined 23.7% over the same period, indicating that price is still more closely tied to speculation than it is to real network usage. By the end of the quarter, HNT’s market cap ranked [136th](https://coinmarketcap.com/historical/20251231/) among all other crypto assets, down from [128th](https://coinmarketcap.com/historical/20250930/) place at the end of Q3.

### Data Credits

![](https://cdn.sanity.io/images/2bt0j8lu/production/6750f6d1044a56a102efc0573e8d4c4d58dd33f8-2048x1144.png?w=714&fit=max&auto=format&dpr=3 "View full size")

[Data Credits (DC)](https://dune.com/queries/2476191/4073489) have a fixed price of $0.00001 and are used to pay for data transfers and Hotspot onboarding fees for IoT or Mobile. The cumulative total all-time [DC burned](https://dune.com/queries/3565935/6001618) by the end of Q4 2025 was $11.4 million. Average daily DC burns increased 83.6% QoQ from $30,920 to $56,760. The Mobile Network accounted for $56,635 of the average daily DC burns, representing 99.8% of the quarter's total, while IoT use contributed just $124.77. Of the $56,635 mobile daily DC burn, 43.9% came from Mobile Offloading.

Of note, [beginning](https://x.com/amirhaleem/status/1957200674539581521?s=20) in August 2025, Helium Mobile routed 100% of its subscriber revenue to HNT purchases in the open market, which were then burned to get Data Credits. The goal of the experiment was to gauge whether predictable purchases, in tandem with reduced emissions, would translate to more accurate ties across network usage and token value. In Q4, the experiment produced $2.9 million in discretionary burns, equivalent to $31,765 in DC burns per day. Meanwhile, Helium’s annualized revenue, excluding discretionary burns, reached $11.0 million. The discretionary burn, alongside organic protocol revenue, resulted in DC burn exceeding HNT emissions for the first time. On January 2, 2026, Helium’s CEO, Amir Haleem, [announced](https://x.com/amirhaleem/status/2007203633532989883?s=20) the suspension of this experiment to focus on user growth and carrier offload rather than discretionary burn.

### Network

#### Carrier Offloading

![](https://cdn.sanity.io/images/2bt0j8lu/production/329d7bd1f30c4b4f31e36d1d4e94c13ff4c77603-2048x1185.png?w=714&fit=max&auto=format&dpr=3 "View full size")

In [June 2024](https://blog.heliummobile.com/helium-mobile-network-roadmap-progress-july/), Helium began partnering with large telecom carriers to use the Helium Network to provide coverage for their users. Subscribers from several carriers are able to offload user data, including [Movistar](https://www.helium.com/mexico), [AT&T](https://blog.helium.com/helium-network-brings-wi-fi-connectivity-to-att-a8fa5b1da1e9), [Google Orion](https://x.com/rawrmaan/status/1784692741961592849), and [Wefi](https://wefitec.com/).

[Offloaded data](https://dune.com/queries/4884362) is the amount of production data users from other carriers have transferred through the Helium Network. In Q4 2025, Helium offloaded 4,388 TB of data from other carriers, a 60.7% QoQ increase from 2,731 TB in Q3. By the end of Q4, the total cumulative data offloaded since inception totaled 9,839 TB. Up-to-date statistics can be viewed [here](https://world.helium.com/en/mobile/stats).

#### Paid Traffic

![](https://cdn.sanity.io/images/2bt0j8lu/production/b43c69e82f34ffbff8dd3477747d43ec065ed9bc-2048x1152.png?w=714&fit=max&auto=format&dpr=3 "View full size")

[Paid traffic](https://dune.com/queries/4185153/7043579) is the amount of paid data sent through Helium Hotspots. In Q3 2025, average daily mobile paid traffic grew 52.9% QoQ from 32.4 TB to 49.6 TB. This growth brought the cumulative all-time paid traffic to 13,069.4 TB, a 53.7% QoQ increase. As one of the Helium Network's main revenue drivers, this metric is expected to continue growing as more users join the network and carrier offloading partnerships expand.

#### Users

![](https://cdn.sanity.io/images/2bt0j8lu/production/84a5cd7a608822851482fc3ae829133a9cfa199d-2048x1152.png?w=714&fit=max&auto=format&dpr=3 "View full size")

Due to the carrier offloading program, cell phones from multiple carriers can connect to the Helium Network. In Q4 2025, [average daily users](https://world.helium.com/en/network/mobile/stats) of the network grew 32.4% QoQ from 1.2 million to 1.6 million, representing nearly 0.5% of the United States’ population. The network first surpassed 2 million users on November 22, 2025, and was above that for 15 days in Q4.

#### IoT Hotspots

![](https://cdn.sanity.io/images/2bt0j8lu/production/10e3336ae10251b9b7a18a251d16af7f228786c8-2048x1185.png?w=714&fit=max&auto=format&dpr=3 "View full size")

IoT Hotspots grew 0.9% QoQ, ending Q3 2025 with 43,033 [hotspots onboarded](https://dune.com/queries/2470060/6031112) since the Solana migration in April 2023. Before the migration, Helium had [over 342,000](https://explorer.helium.com/stats) active hotspots, bringing the network total to over 385,000.

To promote network growth in underserved geographies, the IoT Network's unique [Proof-of-Coverage](https://github.com/helium/HIP/blob/main/0005-poc-fairness.md) (PoC) model adjusts the rewards mechanism based on density to encourage more strategic deployments. As of December 31, 2025, coverage is [strongest](https://world.helium.com/en/network/iot) in major cities across North America, Europe, and Southeast Asia.

### Helium Mobile

#### Helium Mobile Signups

![](https://cdn.sanity.io/images/2bt0j8lu/production/3b2793281664905f050892abda638b345032489f-2048x1152.png?w=714&fit=max&auto=format&dpr=3 "View full size")

Helium Mobile is the eponymous carrier built by the Helium team to leverage the Network as much as possible. The model supports lower operating margins for the Helium Mobile carrier while also being a growth driver for Network use and coverage deployments. Helium Mobile users automatically connect to Helium Hotspots when they are available and seamlessly switch to [T-Mobile’s network](https://www.fierce-network.com/5g/t-mobile-allows-helium-mobile-crypto-carrier-ride-its-5g-network) when hotspot coverage isn't available.

When onboarding to Helium Mobile, users receive a Mobile NFT in their wallet, which is used to track [Helium Mobile signups](https://analytics.topledger.xyz/helium/public/dashboards/81P8F2a40psaWv9qvVvcRuPErNeUgHClqmkuJtUo). Average daily new signups increased 11.1% QoQ from 1,634 to 1,815, as cumulative account signups reached 595,800 at the end of Q4, up 29.1% QoQ from 461,500.

Helium Mobile now offers four different tiers of [plans](https://heliummobile.com/#plans):

- Zero: $0/month with 1GB Nationwide + 2GB Helium Hotspot data
- Sprout (Kids Plan): $5/month with 3GB of data
- Air: $15/month with 10GB of data
- Infinity: $30/month with unlimited data

All of these plans are eligible to earn Cloud Points.

#### Mobile Hotspots

![](https://cdn.sanity.io/images/2bt0j8lu/production/2c30ee9f88f5a2c05a2fd7a9e494f0dd8cdfd58b-2048x1185.png?w=714&fit=max&auto=format&dpr=3 "View full size")

In Q4 2025, the number of hotspots on Helium’s mobile network totaled 121,138, an 8.5% QoQ increase. The [number](https://dune.com/queries/2470067/6031144) of new [Helium Mobile hotspots](https://store.hellohelium.com/products/helium-mobile-hotspot) (Helium’s custom hotspot device) increased 5.6% QoQ from 33,710 to 35,595, representing 29.5% of the total. The [remainder](https://world.helium.com/en/network/mobile/stats) consists of [Helium Plus hotspots](https://www.helium.com/plus), which are hotspots from non-Helium manufacturers. The number of Helium Plus hotspots grew 9.7% QoQ from 77,957 to 85,553, representing 70.5% of the total.

Helium Mobile’s unlimited plan ($30/month) costs considerably less than the average [three-figure plans](https://www.moneylion.com/learn/average-cell-phone-bill-per-month/#:~:text=As%20of%202024%2C%20CNBC%20reported,in%20the%20monthly%20budget%20league.) offered by American telecoms. Subscribers can lower their bill further by earning [Cloud Points](https://blog.heliummobile.com/cloudstore/), rewards Helium Mobile subscribers [earn](https://blog.heliummobile.com/cloudstore/) for referring friends and using cellular data each month. Cloud Points can be redeemed for eGift cards or donated to nonprofit organizations.

## Qualitative Analysis

### International Expansion

On December 10, 2025, Helium [announced](https://blog.helium.com/mambo-c5cf3d64fb47) a partnership with [Mambo WiFi](https://mambowifi.com/) to expand people-powered connectivity in Brazil. Through this joint initiative, Mambo WiFi’s existing base of approximately 40,000 access points will serve as an initial foundation for carrier offload and broader network expansion. In parallel, Helium launched an international waitlist for organizations interested in deploying Helium infrastructure in additional countries, signaling growing global demand for the model.

### Mobile Network Enhancements

Helium [launched](https://world.helium.com/en/network/mobile) live demand sampling data within Helium World, enabling deployers to better understand where traffic demand is concentrated. Newly added hotspots now automatically begin serving traffic for major U.S. carriers at no cost during the sampling phase, allowing carriers to evaluate performance and identify high-usage locations before transitioning deployments into paid traffic routing.

### HIP-148: Reallocate Mobile Mapping Rewards

[HIP-148](https://heliumvote.com/hnt/proposals/2PEJVC3nc2EncXMeyAzwYexRQmBSv6JyvBCJqNWHg76v) eliminated Mobile Mapping rewards following evidence of gaming behavior, low verification adoption, and limited practical utility. The 20% of HNT emissions previously allocated to mapping rewards was reallocated evenly between the Service Provider Pool and the Data Transfer Pool, increasing incentives for active network usage and for deployers to route traffic. As part of this change, Service Provider tokenomics were simplified by consolidating Oracle Operator rewards and allocating the full amount to Helium, streamlining emissions and incentive distribution. Subscribers to Helium Mobile used to earn HNT for sharing their mapping data. Now they can earn Cloud Points redeemable for e-gift cards. This reward pool was previously only accessible to Helium hotspot deployers.

## Closing Summary

Q4 2025 marked a step-change in Helium’s transition from infrastructure buildout to sustained network utilization. Carrier offloading continued to scale meaningfully, with cumulative all-time offloaded data reaching 9,839 TB, up 80.5% QoQ, supported by growing subscriber connections from carriers including AT&T, and Telefónica’s Movistar. This growth translated directly into higher paid traffic and user engagement, as average daily mobile paid traffic rose to 49.6 TB and average daily users increased 32.4% QoQ to 1.6 million, with the network surpassing 2 million daily users for the first time in November.

Average daily Data Credit burns increased to $56,760, driving record monthly revenue of $1.9 million in December and an annualized run rate of $22.4 million. These dynamics reinforce HNT’s role as a pure utility asset, tying token demand directly to real network usage.

Operationally, Helium continued to refine incentives and expand its addressable market. HIP-148 reallocated Mobile Mapping rewards toward active service providers and data transfer, improving capital efficiency and discouraging unproductive behavior. International expansion also gained momentum through new partnerships, including Mambo WiFi in Brazil, signaling growing global interest in Helium’s carrier offload model as the network enters its next phase of adoption-driven growth.

Let us know what you loved about the report, what may be missing, or share any other feedback by [filling out this short form](https://06jiny4c1wy.typeform.com/to/DsmsVsUp?typeform-source=www.google.com#research=state-of-helium-q4-2025). All responses are subject to our [Privacy Policy](https://messari.s3.amazonaws.com/privacy.html) and [Terms of Service](https://messari.s3.amazonaws.com/termsofuse.html).

Mentioned Assets

[HNT$0.825 \-3.08%](https://messari.io/project/helium)

Outline

- [Key Insights](#key-insights-4b56ecff3b64)
- [Primer](#primer-2bed65d38d33)
- [Key Metrics](#key-metrics-7ba37f71306b)
- [The Helium Team Commentary](#the-helium-team-commentary-b4792c684b38)
- [Performance Analysis](#performance-analysis-8f5789b4e699)
- [Qualitative Analysis](#qualitative-analysis-e0582d345fde)
- [Closing Summary](#closing-summary-f4cec39bd90c)[Matthew Nay](https://messari.io/research/matthew-nay)

Matthew is a Research Analyst in Protocol Research. He graduated from MIT with a Master's and Bachelor's in Comp Sci, Economics, and Data Science where he wrote his thesis on DeSoc. Matthew also has previous experience as an Analyst at Goldentree's crypto fund.[Alexander Beaudry](https://messari.io/research/alexander-beaudry)

Alexander is a protocol researcher specializing in Layer-1 and Layer-2 infrastructure, as well as RWA's and Stablecoins. Before Messari, he worked at Jump Trading and Bull-Moose Consulting. He graduated from Northeastern University with a degree in Economics and Data Science, and helped run Northeastern's blockchain club.

Mentioned Assets

[HNT$0.825 \-3.08%](https://messari.io/project/helium)