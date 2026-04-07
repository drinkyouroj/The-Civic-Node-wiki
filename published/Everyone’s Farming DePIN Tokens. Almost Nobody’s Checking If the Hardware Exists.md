---
title: "Everyone’s Farming DePIN Tokens. Almost Nobody’s Checking If the Hardware Exists."
source: "https://drinkyouroj.substack.com/p/everyone-is-farming-depin-tokens"
author:
  - "[[Justin Hearn]]"
published: 2025-12-12
created: 2026-04-07
description: "How token incentives turned “decentralized infrastructure” into the world’s most expensive theater production"
tags:
  - "clippings"
  - "system-audit"
---

## The Glitch

DePIN tokens led this week’s crypto bloodbath with the quiet efficiency of a system administrator discovering the servers were never actually plugged in.

Filecoin dropped 7.5%. Render fell 5.5%. Sector indices hemorrhaged 4-5% while mainstream crypto media scrolled past, barely registering that the “real utility” narrative had just face-planted into the verification problem everyone politely ignored during the bull run. The infrastructure revolution wasn’t collapsing. It was revealing that much of the infrastructure never existed in the first place.

Thanks for reading The Civic Node! This post is public so feel free to share it.

[Share](<https://drinkyouroj.substack.com/p/everyone-is-farming-depin-tokens?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

My dad’s frame shop taught me to recognize this pattern before I had language for it.

He let me help by organizing sample books when I was a kid. Not as child labor disguised as bonding, but because I genuinely loved it. The categorization satisfied something deep in my wiring. Finding patterns in visual chaos. Creating systems that made retrieval predictable. Imposing order on entropy. Other kids played video games. I alphabetized mat samples and felt my nervous system exhale.

Eventually I convinced him to buy point-of-sale software called Lifesaver. The pitch was irresistible: streamlined invoicing, consistent billing, professional receipts. Clean digital interfaces replacing handwritten carbon copies. Peak efficiency wrapped in a Windows 95 aesthetic.

The software worked exactly as advertised. Invoicing became faster. Customer data stayed organized. His workflow legitimately improved.

Except he’d click that “Discount” button on nearly every transaction.

The software included it for legitimate use cases. Customer loyalty. Volume discounts. Competitive matching. My dad used it because he felt uncomfortable charging full price. The system designed to create billing consistency became a tool for undermining that very consistency. Beautiful software. Professional interface. But underneath, the same operational chaos it was supposed to eliminate.

The frame shop itself remained a disaster. Samples scattered everywhere. Projects half-finished. Systems purchased then ignored. That gorgeous POS software sat atop the clutter like a tuxedo on a scarecrow. From the outside, peak organization. From the inside, the same entropy with better typography.

I couldn’t understand why the disorder didn’t bother him the way it gnawed at my nervous system. Why implement systems you won’t follow? Why buy software you’ll immediately subvert? The gap between appearance and function created cognitive dissonance I didn’t have tools to process.

Looking back, that tension taught me something crucial about systems design: interfaces that _look_ organized aren’t the same as systems that _work_. Appearances are cheap. Function is expensive. And humans will optimize for whichever one you actually measure.

This week’s DePIN crash exposed this dynamic at industrial scale.

Filecoin claiming decentralized storage supremacy. Render promising distributed GPU rendering. IO.net advertising over 500,000 GPUs available for computational hire. Helium boasting 1 million wireless hotspots providing global coverage. Beautiful dashboards. Impressive node counts. Professional tokenomics white papers. The appearance of infrastructure at unprecedented scale.

Then someone actually checked.

A wireless mapping enthusiast in Hong Kong spent hours driving through neighborhoods supposedly blanketed by dozens of active Helium hotspots. His mapper received exactly zero pings.1 The hotspots existed on-chain. They earned HNT rewards for “providing coverage.” They just weren’t physically present in the locations they claimed.

IO.net reported 600,000 active GPU connections powering decentralized AI compute. After implementing actual verification testing computational capacity, that number collapsed to 100,000. Then further investigation revealed those “verified” nodes had been gamed. Final count of legitimate, clusterable GPUs capable of performing actual work: around 12,000.2

Not a rounding error. An order of magnitude disconnect between claimed infrastructure and reality.

Fraudsters spoofed 1.8 million fake GPUs to farm rewards before anyone bothered checking if the hardware could perform the computations it advertised.3 They didn’t exploit sophisticated zero-day vulnerabilities. They recognized a simpler truth: if token rewards flow to self-reported metrics, rational actors will optimize self-reported metrics. The networks created systems where lying was cheaper than building.

[![Split image contrasting a perfect holographic network visualization with a messy warehouse containing disconnected cables, illustrating the gap between claimed DePIN infrastructure and physical reality.](https://substackcdn.com/image/fetch/$s_!gsja!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc3f2299-4f24-40ce-8ebc-2907cb745fa6_2688x1536.png)](<https://substackcdn.com/image/fetch/$s_!gsja!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc3f2299-4f24-40ce-8ebc-2907cb745fa6_2688x1536.png>)Dashboard: one million nodes. Warehouse: ethernet cables plugged into nothing.

Token incentives created the appearance of infrastructure without requiring anyone to verify the infrastructure actually functions. My dad’s frame shop dynamic, except instead of scattered mat samples and discount buttons undermining billing consistency, it’s scattered truth claims about physical hardware. And instead of disappointing one autistic kid with pattern-matching compulsions, it’s defrauding an entire sector worth billions.

The real question isn’t why this happened. The real question is why anyone expected different.

## The Source Code

Token incentives guarantee exactly one outcome regardless of your white paper’s stated intentions: people will optimize for tokens, not infrastructure.

Humans respond to the incentive structure you actually implement, not the one you wish existed. This isn’t cynicism. It’s elementary game theory applied to meatspace constraints.

Start with the economics. Helium hotspot owners who actually deploy hardware in good locations earn modest, variable rewards based on genuine network coverage and data transfer fees. Income fluctuates with actual usage. Revenue scales with real-world utility. Building legitimate infrastructure requires capital investment, site selection, maintenance, and exposure to weather, theft, and hardware failure.

[Subscribe now](<https://drinkyouroj.substack.com/subscribe?>)

Alternatively: Helium hotspot owners who spoof their locations into perfect geometric patterns across remote Belgian countryside earn consistent, predictable rewards while their hardware sits in Chinese warehouses connected by ethernet cables. No radio transmission required. No weather exposure. No site visits. No actual infrastructure deployed at claimed locations.

Just perfectly correlated RSSI and SNR readings that never vary the way real wireless signals bouncing off buildings, cars, and atmospheric conditions actually behave.4 Radio waves in the real world create signal variations of 10-30 dB as they interact with dynamic environments. Spoofed signals connected by cables show suspiciously perfect consistency. The physics doesn’t lie, but the token rewards don’t check physics.

The network paid both groups in HNT tokens based on Proof-of-Coverage challenges. Legitimate hotspots and spoofed hotspots received equivalent treatment. Guess which strategy scaled faster?

By the time Helium implemented a denylist for suspected spoofers, the damage was embedded in the economic model. Gaming the network wasn’t an exploit. It was responding rationally to the incentives the protocol actually created. The mysterious part isn’t why people spoofed locations. The mysterious part is why anyone expected them not to.

IO.net discovered this dynamic through expensive, public failure.

They launched with 600,000 claimed GPU connections. Impressive numbers attracted $30 million in Series A funding. The pitch was compelling: solve AI compute scarcity through decentralized GPU aggregation. The biggest decentralized GPU network ever built.

Except they hadn’t built it. They’d incentivized people to claim they’d built it.

After implementing Proof-of-Work verification that tested whether GPUs could actually perform computational work, reported connections collapsed to 100,000. Then security researchers discovered that “verified” count had been gamed through SQL injection attacks and metadata manipulation. Martin Shkreli, ever the antagonist, publicly challenged IO.net to explain why their explorer showed 564,000 GPUs but only 7,648 were actually deployable for real work.5

The final forensic accounting settled on approximately 12,000 clusterable, verifiably active, real GPUs.6

Not a rounding error. A 98% gap between marketing metrics and reality. The network hadn’t aggregated half a million GPUs. It had aggregated half a million claims about GPUs, most of which were either non-existent, inaccessible, or incapable of the work they advertised.

The fraudsters weren’t sophisticated hackers. They were economically rational actors recognizing that self-reported hardware metrics generated token rewards without requiring actual hardware. The network created a system where lying was cheaper than building. So people lied.

This is where DePIN advocates invoke their sophisticated verification mechanisms as salvation. Zero-knowledge proofs will solve everything. Cryptographic attestation. Trusted Execution Environments. Random sampling. Proof-of-Physical-Work protocols that tie consensus to verifiable physical activity.

Except zero-knowledge proofs excel at proving computational correctness, not physical presence.

ZKPs can demonstrate that a GPU solved a cryptographic puzzle without revealing details about how it solved the puzzle. Elegant. Privacy-preserving. Mathematically sound. But proving a GPU solved a puzzle doesn’t prove that GPU exists where you claimed, is available for rent, has the specifications you advertised, or can sustain workloads beyond passing verification checks.

A16z crypto’s framework for DePIN verification acknowledges this explicitly: “DePIN protocols must inherently deal with the oracle problem (bringing data from meatspace on the blockchain in a trustless or trust-minimized fashion).”7

The oracle problem isn’t a bug to patch. It’s the fundamental challenge of decentralized physical infrastructure. Blockchains achieve consensus about digital state transitions. Physical infrastructure exists in meatspace, where consensus mechanisms can’t directly verify location, performance, or availability without trusting oracles that import physical data onto the chain.

A16z’s recommended solutions? Trusted hardware whitelisting. Random sampling with game-theoretic incentives. Human auditors reviewing telemetry logs and usage data. Each approach trades decentralization for verification accuracy, or verification accuracy for cost efficiency, or both for pragmatic short-term functionality.

Notice what’s missing from this toolkit? An actually trustless solution. Because physical infrastructure verification requires physical verification. You can cryptographically prove a sensor generated data. You cannot cryptographically prove that sensor is deployed where claimed, functioning as specified, accessible for genuine work, and not sitting in a warehouse spoofing location metadata for token farming.

That verification requires checking. In meatspace. With actual humans or automated systems performing actual tests against actual hardware.

This costs money. It’s slow. It reduces reported node counts because fake nodes get filtered out. It’s boring infrastructure work with no token launch announcement.

Token farming, by contrast, is fast, cheap, scales beautifully, and generates dashboard metrics that look impressive in pitch decks.

Real infrastructure becomes invisible when it works correctly. You notice your electricity only during blackouts. Your internet only during outages. Your water pressure only when the shower disappoints you. Properly functioning infrastructure fades into environmental background. It’s the ultimate compliment: ignored because reliable.

Fake infrastructure requires constant performance to justify token rewards. Dashboards showing millions of nodes. Heatmaps displaying global coverage. Metrics broadcasting decentralization theater to anyone watching. The performance itself becomes the product, because the actual product — infrastructure doing work — doesn’t exist.

My dad’s frame shop taught me to distinguish these modes through direct experience. The Lifesaver software interface performed efficiency with clean windows and dropdown menus. The cluttered workspace revealed operational reality. The discount button undermined the billing consistency the software promised to deliver. The gap between interface and implementation was where my childhood frustration lived, watching a system designed to create order get subverted by the person who purchased it.

DePIN tokens created the same gap, just with more zeros and better branding.

[Share The Civic Node](<https://drinkyouroj.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

[![Overhead view of a game board showing abundant cryptocurrency tokens versus scarce actual hardware pieces, visualizing how token incentives prioritize appearances over real infrastructure.](https://substackcdn.com/image/fetch/$s_!WP9u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2179a5f7-fbd4-419d-97ff-4b776d9d642f_2688x1536.png)](<https://substackcdn.com/image/fetch/$s_!WP9u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2179a5f7-fbd4-419d-97ff-4b776d9d642f_2688x1536.png>)Reward self-reported metrics, get optimized self-reported metrics. The game theory writes itself.

## The Upgrade

Performance-based routing doesn’t ask hardware if it exists. It discovers what actually works by demanding hardware prove itself through continuous operational reality.

Datagram Network approaches verification differently than the self-reporting model that collapsed into fraud. Not through cryptographic attestation that proves computational work happened. Not through token-incentivized declarations that claim infrastructure exists. Through operational requirements that make fraud economically pointless because fake infrastructure can’t perform real work.

The network routes data around nodes that don’t meet bandwidth and hardware specifications. Not as punishment for dishonesty. Just as automatic optimization. If a node can’t handle the routing load when traffic arrives, the network discovers this immediately through performance degradation and routes around the bottleneck. The node stops earning because it stops being useful, not because some verification oracle caught it lying on a metadata form.

This resembles how BitTorrent naturally routes around slow peers without requiring peers to honestly self-report their bandwidth. Or how BGP routing discovers functional network paths through operational testing rather than trusting router declarations. The verification emerges from performance requirements, not from verification theater.

A node can claim whatever hardware specifications it wants. Falsify bandwidth reports. Spoof location metadata. Lie about available storage or computational capacity. None of it matters because when actual traffic arrives, fraudulent nodes fail to perform the work. The network learns through operational failure rather than through verification checkpoints.

This inverts the incentive structure. Fake nodes don’t just get caught eventually through forensic accounting. They fail to earn from day one because they can’t perform actual work. Real infrastructure wins by default because only real infrastructure can sustain network load under real-world conditions.

The model mirrors how my nervous system learned to distinguish my dad’s performance of organization from actual organizational functionality. The Lifesaver software looked efficient. The cluttered shop revealed dysfunction. The discount button undermined billing consistency. I couldn’t verify the gap through inspection. I learned through operational experience: trying to find specific frame samples in the chaos, watching the gap between quoted prices and final invoices, recognizing that systems don’t work just because they look right.

Datagram’s routing intelligence functions as distributed operational verification. Nodes prove capability through sustained performance, not through self-reported metrics. The verification is continuous, automatic, and expensive to fake because faking requires actually performing the work you claimed to perform, at which point you’re no longer faking.

The legitimate tier of DePIN projects shares this characteristic.

Bittensor’s subnet marketplace for machine learning models validates performance against benchmarks that test whether models actually perform the inference work they advertise.8 You can’t claim your subnet provides accurate image classification while returning garbage outputs. The benchmark catches performance failures immediately.

Render’s GPU rendering network partners with NVIDIA and Apple to verify that participating GPUs exist, are accessible, and can perform actual rendering work.9 The partnerships provide hardware authentication that makes spoofing expensive. Falsifying an NVIDIA GPU’s attestation requires compromising NVIDIA’s cryptographic keys, not just editing metadata.

Filecoin’s storage network requires cryptographic proof that data remains stored over time.10 Storage providers must prove they’re continuously storing the data they claim to store. The proofs are expensive to generate if you’re not actually storing data, making fraud cost more than honest participation.

Notice the pattern: verification through operational requirements, not through self-reported metrics that generate token rewards. The infrastructure proves itself by working, not by claiming to work. The systems distinguish function from performance by demanding continuous function.

[Share The Civic Node](<https://drinkyouroj.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

This approach costs money. It reduces reported network size because fake nodes can’t sustain the performance requirements. It’s not investor-friendly when you’re competing with projects claiming millions of nodes built in months.

But it’s the only approach that survives first contact with actual usage. Because eventually, someone tries to _use_ the infrastructure. Deploy an application on those GPUs. Store actual data on that decentralized storage. Send IoT traffic through those wireless hotspots. And then you discover whether those million nodes provide real infrastructure or whether they’re ethernet cables in warehouses performing coverage theater for token rewards.

The boring truth: real infrastructure is expensive, slow to deploy, and invisible when working correctly. These characteristics make it terrible for token farming but essential for actual utility. You can’t fake operational performance at scale without performing the operations you’re faking, at which point the distinction between real and fake collapses into identical functionality.

My dad never followed the organizational systems he purchased because following them was harder than maintaining familiar chaos. The Lifesaver software required discipline he didn’t have or want. The discount button provided an escape valve from the consistency the system promised. The gap between purchase and practice revealed preferences: appearance mattered more than function for his operational reality.

DePIN networks that survive will be the ones where function matters more than appearance because the incentive structure makes function profitable and appearance worthless. Where routing around dysfunctional nodes happens automatically. Where verification emerges from operational requirements rather than self-reporting. Where infrastructure proves itself through work rather than through claims about work.

[![Comparison of self-reporting verification \(left\) versus performance-based routing \(right\), showing how operational requirements naturally filter out non-functional nodes.](https://substackcdn.com/image/fetch/$s_!5-FY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6252da5a-14e2-4ada-bbbb-caf5f776ca6a_2688x1536.png)](<https://substackcdn.com/image/fetch/$s_!5-FY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6252da5a-14e2-4ada-bbbb-caf5f776ca6a_2688x1536.png>)Performance-based routing doesn’t ask if nodes exist. It discovers what works by demanding proof.

The networks that collapse will be the ones still optimizing for dashboard metrics and token farming. Where node counts matter more than node functionality. Where verification happens through attestation rather than through performance. Where appearance and function remain separated by implementation gaps that fraud exploits profitably.

## My Debug

I learned young that my nervous system couldn’t tolerate the gap between appearance and function. It’s why I obsessively organized sample books and begged for actual systems rather than system-shaped performances. It’s why watching DePIN theater triggers the same cognitive dissonance my dad’s cluttered frame shop generated decades ago.

That frame shop tension shaped how I process systems permanently. I see the gap between interface and implementation. Between claimed organization and actual chaos. Between performance and function. It’s not insight derived from careful analysis. It’s closer to involuntary pattern matching, the same way some people can’t unsee visual illusions once they’ve spotted them.

The pattern recognition isn’t optional. It’s how my nervous system maintains sanity in environments where appearance and reality diverge. Show me a beautiful interface and my brain immediately hunts for the cluttered workspace underneath. Show me impressive metrics and I start searching for the verification mechanism. Show me claimed functionality and I need to test whether the function actually exists or whether I’m looking at theater.

My dad probably saw me as overly focused on pointless details. Why did perfectly organized sample books matter if customers got their frames eventually? Why obsess over systems that mostly worked fine without strict adherence? Why care about billing consistency if the business remained profitable?

But I wasn’t obsessing over organization for its own sake. I was trying to reduce the cognitive load of navigating chaos that didn’t need to exist. The clutter wasn’t neutral. It was actively expensive, requiring constant mental overhead to navigate dysfunction that better systems would eliminate. Every sample book search required reconstructing the organizational logic from scratch. Every invoice calculation required double-checking against the discount button’s usage. The chaos wasn’t charming inefficiency. It was unnecessary friction.

The frame shop taught me that systems fail not through dramatic collapse but through quiet abandonment. You purchase software then subvert its functionality. You create organizational structures then ignore them when convenient. You claim efficiency then optimize for appearance over function. The gap between intention and implementation becomes normalized, accepted, invisible to everyone except those whose nervous systems register the dissonance as ongoing threat.

DePIN token farming isn’t evil. It’s predictable. You create token rewards for self-reported metrics, you get optimized self-reported metrics. The failure isn’t moral. It’s architectural. The networks designed systems that measured appearance rather than function, then acted surprised when participants optimized for what was actually measured.

Real infrastructure requires different incentives. Performance-based verification that emerges from operational requirements. Routing intelligence that discovers what works rather than trusting what claims to work. Reward structures that make fraud more expensive than honest participation.

The boring solution to infrastructure theater is actual infrastructure. Built slowly, verified continuously, invisible when working correctly. No token launch can shortcut that reality. No dashboard can substitute for operational verification. No white paper can cryptographically prove that hardware exists in claimed locations performing advertised work without checking whether hardware exists in claimed locations performing advertised work.

My childhood frame shop taught me to trust what works over what performs. To distinguish system-shaped appearances from actual systems. To recognize when organizational theater substitutes for organizational function.

DePIN is learning the same lesson, one fake node at a time. The expensive way, through billions in token value collapsing when someone finally checks if the infrastructure exists. The question isn’t whether this lesson gets learned. The question is whether it gets learned before “decentralized infrastructure” becomes synonymous with “expensive fraud” the way ICOs became synonymous with scams.

The networks that survive will be the ones that learned early. That built verification into operational requirements. That made function profitable and appearance worthless. That recognized infrastructure isn’t theater you perform for tokens. It’s work you do that becomes invisible when done correctly.

Everything else is just discount buttons on billing software, subverting the consistency the system promised to deliver.

[![Worn point-of-sale keyboard with overused discount button surrounded by organized papers and cluttered workshop, representing the gap between system design and actual usage patterns.](https://substackcdn.com/image/fetch/$s_!MY6J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cfa8b5a-c90b-44af-84d8-6e172464d7f4_2688x1536.png)](<https://substackcdn.com/image/fetch/$s_!MY6J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cfa8b5a-c90b-44af-84d8-6e172464d7f4_2688x1536.png>)The software promised consistency. The discount button delivered escape velocity from his own system.

The Civic Node is a reader-supported publication. To receive new posts and support my work, consider becoming a subscriber.

1

[Cassiopeia Ltd., “Trying out the Helium LoRaWAN network [scam alert]” (2022)](<https://cassiopeia.hk/trying-out-the-helium-lorawan-network-scam-alert/>)

2

[IO.net, “25th April Incident Report” (April 2024)](<https://ionet.medium.com/25th-april-incident-report-176e5fb5c576>)

3

[Crypto Daily, “Preventable Cyber Attack Impacts Io.net” (May 2024)](<https://cryptodaily.co.uk/2024/05/preventable-cyber-attack-impacts-ionet>)

4

[HNT News, “Helium’s Dirty Secret - POC Hacking Explained”](<https://hntnews.org/poc-hacking-explained/>)

5

[Protos, “Solana project CEO says ‘sybil attackers’ gamed metric hoping for airdrop” (April 2024)](<https://protos.com/solana-project-ceo-says-sybil-attackers-gamed-metric-hoping-for-airdrop/>)

6

[Protos, “Solana project CEO…” (Apr. 2024)](<https://protos.com/solana-project-ceo-says-sybil-attackers-gamed-metric-hoping-for-airdrop/>)

7

[a16z crypto, “Why DePIN matters, and how to make it work”](<https://a16zcrypto.com/posts/listicles/why-depin-matters/>)

8

[CryptoRank, “Best 20 DePIN projects tier list” (December 2025)](<https://investx.fr/en/crypto-news/crypto-pin-tier-list-top-20-projects-for-massive-gains/>)

9

[CryptoRank, “Best 20 DePIN…” (Dec. 2025)](<https://investx.fr/en/crypto-news/crypto-pin-tier-list-top-20-projects-for-massive-gains/>)

10

[CryptoRank, “Best 20 DePIN…” (Dec. 2025)](<https://investx.fr/en/crypto-news/crypto-pin-tier-list-top-20-projects-for-massive-gains/>)
