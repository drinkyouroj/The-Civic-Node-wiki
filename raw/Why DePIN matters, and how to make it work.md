---
title: "Why DePIN matters, and how to make it work"
source: "https://a16zcrypto.com/posts/listicles/why-depin-matters/"
link_text: "a16z crypto, “Why DePIN matters, and how to make it work”"
domain: "a16zcrypto.com"
author: "Guy Wuollet"
published: "2025-03-29"
fetched: 2026-04-07
tags: ["clippings"]
---

Existing physical infrastructure networks like telecommunications, energy, water, and transportation are often natural monopolies — markets where it’s cheaper for one company to deliver a good or service than it is to encourage competition. In most first world countries, they’re overseen through complex government oversight and regulatory capture. This creates little incentive for innovation — not to mention horrible customer experiences, bad user interfaces, lackluster service, and slow response times. These networks are also, perhaps not coincidentally, notoriously inefficient and poorly maintained. Look no further than the recent California wildfires that bankrupted PG&E, or regulations protecting incumbent telecom companies. In the developing world, the situation is even worse: Many of these services either don’t exist or are costly and scarce.

We can do better. The decentralization of physical infrastructure networks offers an opportunity to leapfrog atrophying incumbent monopolies and create networks that are more robust, easier to invest in, and more transparent. DePIN protocols are inherently user owned and operated services that allow anyone to contribute to the essential infrastructure that runs our daily lives. They have the potential to be a great democratizing force that makes our societies both more efficient and more open.

In this post I’ll explain what DePIN is, and why it matters. I’ll also share my framework for evaluating DePIN protocols and the questions to ask when building a DePIN protocol, focusing especially on the problem of verification.

Introducing DePIN

A Decentralized Physical Infrastructure Network (DePIN) is any sufficiently decentralized network that uses cryptography and mechanism design to ensure a client can request physical services from a set of providers — breaking the natural monopoly and providing the benefits of competition. (We’ll explore what this means in more detail below.) Clients are typically end users, but they could also be an application acting on behalf of its end users. Providers are often small businesses, but, depending on the network, they can vary from gig workers to massive incumbent corporations. “Decentralization” here means decentralization of power and control, not just of physical distribution or data structures.

Built correctly, DePIN protocols encourage users and small businesses to participate in physical infrastructure networks, and to govern their evolution over time while providing transparent incentives for contribution. Just as the Internet is dominated by user generated content, DePIN offers the opportunity for the physical world to be dominated by user generated services. Importantly, just as blockchains are helping to break the “attract extract” cycle of monopolistic big tech companies, DePIN protocols can help break utility monopolies in the physical world.

DePIN in practice: The energy grid

Let’s consider energy as an example. The energy grid in America is already decentralizing, even outside of a crypto context. Bottlenecked transmission and long delays to connect new generation capacity to the grid have created an incentive for decentralized generation capacity. Home and business owners can deploy solar panels to generate electricity at the edge of the grid, or install batteries to store it. This means they don’t just buy energy from the grid but also sell it back to the grid.

With the proliferation of edge generation and storage, many grid-connected devices are no longer owned by utilities. These user-owned devices could greatly benefit the grid by storing and discharging energy at crucial times, so why don’t they? Existing utilities don’t have a good way to access information about the state of user-owned devices, or to purchase control of them. Daylight, a protocol working to solve fragmentation in the energy industry, offers one solution. Daylight is building a decentralized network to enable users to sell information about the state of their grid-connected devices, and to allow energy companies to temporarily control them in exchange for a fee. Put more succinctly, Daylight is building a decentralized virtual power plant.

The result could be a more robust and efficient energy grid, user-owned power generation, better data, and fewer trust assumptions than exist in centralized monopolies. This is the promise of DePIN.

The DePIN cookbook

DePIN protocols have strong potential to improve the essential physical infrastructure we interact with each day, but realizing this goal requires overcoming at least three daunting challenges:

determining if decentralization is necessary in this particular case,

going to market, and

verification, the most daunting of these challenges.

I’m deliberately overlooking the specific technical challenges of any given physical infrastructure domain. That’s not because these challenges are unimportant, but because they are domain specific. I’m focused on building decentralized networks in the abstract, and focused in this piece on advice to all DePIN projects across vastly different physical industries.

1. Why DePIN?

Two common reasons to build a DePIN protocol are reduced capital expenditure (capex) for hardware deployment, and aggregating fragmented capacity. DePIN protocols can also create neutral developer platforms on top of physical infrastructure — platforms that unlock permissionless innovation like open APIs for energy data or neutral ridesharing markets. Through decentralization, DePIN protocols enable censorship resistance, eliminate platform risk, and enable permissionless innovation, the same composability and permissionless innovation that have allowed Ethereum and Solana to thrive. Deploying a network for physical infrastructure is expensive and traditionally has required a centralized company, but with DePIN, decentralized ownership spreads out both the cost and the control.

1.1 Capex

Many DePIN protocols encourage users to own and operate the network by purchasing hardware and making contributions that would usually require large or even infeasible capital expenditures by some centralized company. Capex is one of the reasons many infrastructure projects are considered natural monopolies. Lower capex gives DePIN protocols a structural advantage.

Let’s get specific and consider the telecom industry. New networking standards are often hard to adopt because of the large capex involved in deploying the new hardware a standard relies upon. For example, one analysis predicted that 5G cellular would involve $275 billion private investment for deployment across the United States.

In contrast, the DePIN network Helium deployed one of the largest long-range, low-power (LoRaWAN) networks globally with no large, upfront hardware investment from a single entity. LoRaWAN is a standard well suited to Internet of Things (IoT) use cases. Helium worked with hardware manufacturers to create LoRaWAN routers, allowing users to directly purchase those routers from manufacturers. Users then became owners and operators of the network, providing LoRaWAN transit to clients who paid for the service. Helium is now focused on a growing 5G deployment for cellular coverage.

Deploying an IoT network as Helium did would’ve required significant up front capex, and taking the risk that a sufficiently large customer base was interested in purchasing connectivity on the new network. Helium was able to validate the supply side of its marketplace, and to reduce its cost structure, because it was a DePIN protocol.

1.2 Capacity

In some cases, a large amount of latent capacity for a physical resource already exists, but it’s been too complex for an existing business to aggregate. Consider empty space on hard drives. On any given hard drive, the space is small enough that it would not merit the attention of, say, a storage company like AWS. But when aggregated by a DePIN protocol like Filecoin, that space becomes a cloud storage provider. DePIN protocols can take advantage of blockchains to coordinate normal people and allow them to contribute to large scale networks.

1.3 Permissionless innovation

The most crucial feature unlocked by DePIN protocols is permissionless innovation: Anyone can build on the protocol, which stands in sharp contrast to, say, your local power company’s grid. This permissionless innovation is an underacknowledged feature relative to reducing capex or aggregating capacity.

Permissionless innovation allows physical infrastructure to evolve at the pace of software. It has become a common turn of phrase to complement the pace of innovation in “bits” and lament the pace of innovation in “atoms.” DePIN provides the most salient path towards making atoms look more like bits for builders and investors alike. When anyone with an Internet connection, anywhere in the world, can propose new ways to organize and coordinate the physical systems that run our world, brilliant and creative people can invent better solutions than exist today.

1.4 Composability

The reason permissionless innovation could speed up atoms into bits is composability. Composability allows builders to specialize in building the best point solution possible, and for that solution to be easily integrated. We’ve already seen the power of so-called money legos in DeFi. Infrastructure legos in DePIN can have a similar impact.

2. Going to market: opportunities and challenges

Building a DePIN protocol is harder than building a blockchain because it requires solving the challenges of building both a decentralized protocol and a traditional business. Bitcoin and Ethereum both began as separate from the worlds of traditional finance and cloud computing. Most DePIN protocols lack this luxury and are intimately tied to existing problems in the physical world.

Most DePIN domains must interact with existing centralized systems from day one. Consider utilities, cable companies, ride sharing services, and Internet service providers as examples. These existing networks often have both regulatory capture and strong network effects. New players can find it hard to compete. Just as decentralized networks can be the native antidote to monopolies on the Internet, DePIN networks can be the native antidote to physical infrastructure monopolies.

But DePIN builders need to figure out where they can add value first, with the goal of expanding to eventually challenge existing physical networks as a whole. Finding the right wedge is crucial to future success. DePIN builders also need to understand how their network will interface with the existing alternatives. Most traditional companies have balked at running blockchain full nodes, and often struggle with self-custody or issuing onchain transactions. They usually don’t understand what crypto is, or why it matters.

One approach can be to demonstrate the value your DePIN protocol can add — without mentioning it runs on crypto rails. Once existing players are seriously considering an integration or can understand the value the new protocol will add, they can be more receptive to the idea of crypto. To put it more broadly: Builders should be translating the value add of their protocol depending on the audience they’re engaging with, and crafting narratives that connect emotionally with that audience.

Tactically, interfaces with existing networks often require some level of early intermediation and thoughtful entity structuring that can be highly dependent on the specific physical domain the protocol is targeting.

Enterprise sales are also a challenge for DePIN protocols. Enterprise sales is often a white-glove, time-consuming, and custom process. Customers want a “throat to choke,” a directly responsible individual. In DePIN networks, no one person or company can represent the network as a whole, or run a traditional enterprise sales process. One solution is DePIN protocols having centralized companies as initial distribution partners that resell the service. Take for instance, a centralized cellular company that sells directly to normal consumers and charges USD while using a decentralized telecom network under the hood to actually provide the service. This abstracts the complexity of crypto wallets and self-custodial wallets, and hides the “crypto” aspect of the product. The idea of a centralized company distributing the service of a DePIN network could be called a “DePIN mullet,” just like the “DeFi mullet” has become a popular model for financial services.

3. The hard things about DePIN: Verification

The hardest part of building a DePIN protocol is verification. And verification matters: It is the only clear way to ensure that clients receive the service they pay for, and that providers are correctly paid for their work.

3.1 Peer to pool vs. peer to peer

Most DePIN projects have adopted a peer-to-pool model, where the client makes a request to the network, and the network selects a provider to respond to the client. Importantly, this also means that the client is paying the network, and that the network pays the provider.

The alternative is a peer-to-peer model, where the client requests service directly from a provider. This means that the client must have some way to discover a set of providers and pick the one they’d like to work with. It also means the client pays the provider directly.

Verification is more important in the peer-to-pool model than in the peer-to-peer model. In the latter, it’s possible for the provider or the client to lie, but because the client directly pays the provider, either party can detect the other party’s lie without needing to prove the lie to the network and can choose to stop transacting. In the peer-to-pool model, the network needs a way to adjudicate disputes between the client and provider. Providers usually agree to serve any client the network assigns as a condition of joining the network, and so the only way to prevent or remediate a client/provider dispute is with some decentralized verification method.

DePIN projects choose a peer-to-pool design for two reasons. Peer-to-pool enables the project to more easily provide a subsidy through the use of a native token. It also enables better UX and reduces the amount of offchain infrastructure required to use the network. A good example of this dynamic outside of DePIN is the distinction between peer-to-pool DEXs (like Uniswap) and peer-to-peer DEXs (like 0x).

Tokens matter because they can help solve the cold start problem in building a network. To build a network effect (in both web2 and web3), projects usually provide strong value to the user in the form of some subsidy. Sometimes this subsidy is a direct financial incentive like a lower cost, and sometimes it’s a value additive service that doesn’t scale. Tokens usually provide a financial subsidy, even as they help build community and give clients a say in how the network develops.

A peer-to-pool model allows the user to pay X, and for the provider to receive a payment of Y, where X < Y. Usually this is possible because the DePIN project creates a native token and rewards providers in the native token. The native token rewards Y can be greater than the client’s payment X because speculators buy the token and value it above its initial worth (which is usually very low or zero before the network has any usage). The goal ultimately is that providers become more efficient in providing the service and the DePIN project builds a network effect so that X > Y and the DePIN project can capture the difference between X and Y as protocol revenue.

A peer-to-peer model makes token rewards as a subsidy much harder. If a client can pay X and a provider receives Y, where X < Y, and the client and provider can interact directly, then providers will pretend to buy services from themselves — an instance of “self-dealing.” As DePIN protocols are permissionless, there currently isn’t a good way to solve the problem without adding centralization or a peer-to-pool model.

3.2 Self dealing

Self dealing is when a user acts as both the client and the provider, aiming to transact with themselves towards the goal of extracting value from the network. This is self-evidently pernicious and most DePIN projects attempt to address self dealing. The simplest solution is to not provide a subsidy or token incentive, but that makes solving the cold start problem much harder.

Self dealing can be particularly harmful if the cost for the self dealer to provide service to themself is zero, which is usually the case. One of the most common solutions to ameliorate self dealing is to require providers to stake a token, often a native token, and allocate client requests to providers based on stake weight.

Staking doesn’t completely solve the self dealing problem as it’s possible for large providers (those staking many tokens) to still profit from the portion of client requests routed to themself. For example, if the provider reward is five times greater than the cost paid by the client, a provider with 25% of staked tokens will receive five tokens in rewards for every four it spends. This assumes the cost for the self dealing provider to provide the service to itself is zero, and the benefit the self dealer derives from requests to other providers is zero. If a self dealer can derive some benefit or value from requests allocated to other providers, then for a given client cost to provider reward ratio it’s possible for the self dealer to extract more value.

3.3 Verification approaches

Now that we have an idea for why verification is such a crucial problem, let’s discuss the different verification mechanisms that DePIN projects could consider.

Consensus

Proofs

Random sampling

Trusted hardware

Whitelisting + auditing

Trust assumptions

Medium (honest majority assumption)

Low (cryptography)

Medium (game theoretic)

High (dependent on the manufacturer)

High (game theoretic and governance)

Security

High

High

Medium

Medium

Low

Performance

Low

Low

Medium

High

High

Fit for DePIN projects

Low

Very low

High

High

Medium

Consensus

Most blockchains use consensus (combined with a sybil resistance mechanism like PoW or PoS). It’s useful to rephrase “consensus” as “re-execution” because it highlights that every node in a blockchain network forming consensus typically has to re-execute each computation processed by the network. (This is not necessarily true for modular blockchains or blockchain architectures that separate out consensus, execution, and data availability.) Re-execution is usually required because every node in the network is generally assumed to exhibit Byzantine behavior. Put another way, nodes must check each other’s work because they can’t trust each other. When there is a newly proposed state change, every node validating the blockchain must execute that state change. This can be a lot of re-execution! Ethereum, for instance, had more than 6000 nodes at the time of this writing.

Proof of Correct Execution (validity roll ups, ZEXE, etc.)

Instead of asking each node in a blockchain network to re-execute every state change, it’s possible to have a single node execute a given state change and produce a proof that the node executed the state change correctly. The proof of correct execution is faster to verify than executing the computation itself (this property makes the proof succinct). The most common form of such a proof is a SNARK (succinct non-interactive argument of knowledge), or a STARK (succinct transparent argument of knowledge). SNARKs and STARKs are often extended to be proven in zero knowledge, revealing no information about the statement being proven. As such, you often hear SNARKs/STARKs and ZK proofs conflated when used for the purpose of compressing proofs of computation.

Likely the most well known type of blockchain using proofs of correct execution is a zero knowledge rollup (ZKR). A ZKR is an L2 blockchain that inherits the security of some underlying blockchain. The ZKR batches transactions, creates a proof that said transactions were executed correctly, and then posts the proof on an L1 for verification.

Proofs of correct execution are often used for scalability and performance, for privacy, or for both. zkSync, Aztec, Aleo, and Ironfish are all good examples. Proofs of correct execution can be used in other contexts. Filecoin uses ZK-SNARKs as part of their Proof of Storage. Proofs of correct execution have begun to be implemented for ML inference, ML training, identity, and more.

Random sampling / statistical measurement

Another approach to addressing verification for DePIN projects is to randomly sample providers and measure whether they are correctly responding to client requests. Often these “challenge” requests are allocating pro rata to a providers’ stakeweight in the network, which helps to address both verification and self dealing. Because many DePIN projects provide a large reward for provider availability (the reward to providers for availability is often greater than the reward for serving client requests), random sampling allows the network to ensure a provider is actually available. A challenge request is occasionally routed to a provider, and if the provider answers the request correctly, and the request hashes beyond some difficulty threshold, then that provider receives the equivalent of a block reward. This incentivizes rational providers to answer client requests correctly if providers can’t distinguish between a client request and a challenge request. Some version of random sampling has seen the greatest adoption amongst networking focused DePIN projects like Nym, Orchid, Helium.

Random sampling can be more scalable than consensus because the number of samples can be very small in proportion to the number of state changes in the network.

Trusted hardware

Trusted hardware can be useful for privacy (as discussed above), but it can also be useful for verifying sensor data. One of the biggest challenges in decentralized verification for DePIN projects is that DePIN projects must inherently deal with the oracle problem (bringing data from meatspace on the blockchain in a trustless or trust-minimized fashion). Trusted hardware allows for the network to adjudicate any client/provider dispute based on the result of meatspace sensor data.

Trusted hardware usually has vulnerabilities, and is likely best used as a pragmatic solution in the short to medium term, or as another layer for defense in depth. The most common trusted execution environments are Intel SGX, Intel TDX, and ARM TrustZone . Blockchains such as Oasis, Secret Network, and Phala all use TEEs, and SAUVE plans to use TEEs.

Whitelisting and auditing

Often the most pragmatic, and least technically complex solution for verification, is to whitelist specific physical devices to participate in the DePIN protocol, and to ensure that providers are correctly serving clients by having human auditors review logs and telemetry data.

More tangibly this often involves building custom hardware with an embedded signing key, requiring all hardware participating in the network to be purchased from a verified manufacturer. The manufacturer then whitelists the set of embedded keys. Only data signed with a whitelisted keypair is accepted by the network. This also assumes that it’s very hard to extract an embedded key from a device, and that the manufacturer is accurately reporting which keys are embedded in which devices. Human auditing is often required to address these challenges.

Finally, to ensure that service is being correctly provided oftentimes a DePIN protocol will use protocol governance to elect an “auditor” that will look for malicious behavior and report its finding to the protocol. The auditor is a human and able to detect clever attacks that would elude a standardized protocol, but appear relatively obvious to a human once identified. Usually this auditor is empowered to submit potential punishments (such as slashing) to protocol governance, or to directly trigger slashing events themselves. This also assumes that protocol governance will act in the best interests of the protocol, and faces the human incentive challenges involved in any social consensus.

The best approach?

Given the wide range of potential verification choices, it’s often difficult to decide the best approach for a new DePIN protocol.

Consensus and proofs are often infeasible for verification. DePIN protocols deal with physical services, and consensus or proofs can only provide strong guarantees about computational (digital, not physical) state changes. To use consensus or proofs for verification of a DePIN protocol, you must also use an oracle that comes with its own set of (usually weaker) trust assumptions.

Random sampling is a good fit for DePIN protocols because it’s highly efficient and game theoretic, allowing it to operate well on physical services. Trusted hardware and whitelisting are usually the best way to start because they’re the simplest, but they are also the most centralized and least likely to work long term.

Why DePIN Matters

Crypto became popular out of a desire to remove monetary control from the hands of nation states, but far more important services — basic Internet connectivity, electricity, and access to water — centralize power in the hands of a select few. By decentralizing these networks, we can not only create a more free society, but a more efficient and prosperous one.

A decentralized future means that many people — not just that select few — can contribute to proposing better solutions. It’s rooted in the idea that latent human capital exists everywhere. If you’re excited by the idea of a decentralized financial system, or a decentralized developer platform, examine the many other essential network-based services we all use on a daily basis.

***

Guy Wuollet is a partner on the a16z crypto investment team. He focuses on investing across crypto at all layers of the stack. Prior to joining a16z, Guy worked on independent research in concert with Protocol Labs. His work focused on building decentralized networking protocols and upgrading Internet infrastructure. He holds a B.S. in Computer Science from Stanford University, where he rowed on the Varsity Crew team.

***

The views expressed here are those of the individual AH Capital Management, L.L.C. (“a16z”) personnel quoted and are not the views of a16z or its affiliates. Certain information contained in here has been obtained from third-party sources, including from portfolio companies of funds managed by a16z. While taken from sources believed to be reliable, a16z has not independently verified such information and makes no representations about the current or enduring accuracy of the information or its appropriateness for a given situation. In addition, this content may include third-party advertisements; a16z has not reviewed such advertisements and does not endorse any advertising content contained therein.

This content is provided for informational purposes only, and should not be relied upon as legal, business, investment, or tax advice. You should consult your own advisers as to those matters. References to any securities or digital assets are for illustrative purposes only, and do not constitute an investment recommendation or offer to provide investment advisory services. Furthermore, this content is not directed at nor intended for use by any investors or prospective investors, and may not under any circumstances be relied upon when making a decision to invest in any fund managed by a16z. (An offering to invest in an a16z fund will be made only by the private placement memorandum, subscription agreement, and other relevant documentation of any such fund and should be read in their entirety.) Any investments or portfolio companies mentioned, referred to, or described are not representative of all investments in vehicles managed by a16z, and there can be no assurance that the investments will be profitable or that other investments made in the future will have similar characteristics or results. A list of investments made by funds managed by Andreessen Horowitz (excluding investments for which the issuer has not provided permission for a16z to disclose publicly as well as unannounced investments in publicly traded digital assets) is available at https://a16z.com/investments/.

The content speaks only as of the date indicated. Any projections, estimates, forecasts, targets, prospects, and/or opinions expressed in these materials are subject to change without notice and may differ or be contrary to opinions expressed by others. Please see https://a16z.com/disclosuresfor additional important information.
