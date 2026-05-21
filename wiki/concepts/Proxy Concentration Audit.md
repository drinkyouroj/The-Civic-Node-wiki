---
title: "Proxy Concentration Audit"
type: concept
tags: [depin, governance, dao, franchise, procedural-method]
created: 2026-05-21
updated: 2026-05-21
sources: 10
---

## Definition

The proxy concentration audit is a procedural test for any DAO governance vote that uses proxy delegation. It surfaces whether the entities benefiting from a proposal also cast the largest voting blocs that passed it. The audit's output is a single empirical question: **does the proposing entity, plus any co-author or coordinating proxies, control more than 50% of yes votes?** If yes, "community consensus" as the secondary press describes it is descriptively wrong. The vote may be a community ratification in form and a self-authorization in substance.

The audit is not a verdict; it's a measurement. The verdict — whether the concentration represents legitimate proposer-confidence or structural self-dealing — is downstream of the measurement, and depends on the [[Franchise vs. Business]] question of what the proposal actually authorizes.

## The Method

1. **Pull the on-chain vote receipt.** Most modern DAO governance portals (Snapshot, Tally, Helium Vote, etc.) publish a voter breakdown showing top voters by voting weight. For DAOs using veToken or staked-token systems, the breakdown is canonical — there is no off-chain interpretation needed.
2. **Identify the labels.** Most portals show wallet labels alongside voting weight for accounts that have set them. Unlabeled wallets are anonymous proxies; labeled wallets identify themselves (corporate counterparties, named individuals, foundations).
3. **Cross-reference the labels against the proposal authorship.** The proposal text lists authors and contributors. The audit checks whether any of the top voters share a name or known relationship with the listed authors.
4. **Sum the proposing-entity-aligned proxies as a share of yes votes (or, more conservatively, of total vote).** If the sum exceeds 50% of yes votes, the proposing entity carried the proposal. If it exceeds 50% of total vote, the proposing entity carried the proposal regardless of any opposition coordination.
5. **Compare to a baseline.** Earlier votes on the same DAO that pre-date the concentration pattern give a reference distribution. If the proposing-entity bloc represents a new concentration relative to prior votes, the audit has surfaced an inflection.
6. **Track veToken accumulation rate.** Lock-up-weighted voting systems compound: an entity that accumulates more veTokens between votes will hold a larger share of the next vote without having to win any new votes. Tracking the accumulation rate of the largest proxies between consecutive votes is the leading indicator of franchise-architecture entrenchment.

## Why It Matters for the Newsletter

**The default DAO-coverage narrative is wrong.** Most reporting on DAO governance treats vote percentages as community sentiment. The audit shows the vote percentage is the output of a structural process whose inputs (proxy concentration, lock-up accumulation, Foundation-endorsed delegation policies) determine the percentage before any voting begins. Reporting that quotes the headline tally without the proxy breakdown misses the substantive story.

**The audit is reusable across DePIN.** Every DePIN project that uses proxy-delegated DAO governance is subject to the audit. The procedure transfers exactly: pull the breakdown, identify the labels, sum the proposing-entity-aligned proxies, compare to baseline. Render, GEODNET, io.net, Filecoin, and any future operator-token network with a DAO can be audited the same way. The audit is the first move in any DePIN governance piece.

**It connects DePIN to broader securities-law and franchise-disclosure debates.** A vote in which 50–57% of the yes vote came from the proposing entity and its co-author would, in a corporate-securities context, raise affiliate-vote disclosure questions. DAO governance has no equivalent procedural standard. The audit surfaces what would be a disclosure requirement in adjacent regulated structures, and what isn't a requirement in DAO governance. The asymmetry is the editorial substance.

**It creates a quantitative spine for franchise architecture claims.** The [[Franchise vs. Business]] test is structural and qualitative. The proxy concentration audit makes it quantitative and primary-source. Together they give a defensible diagnosis that doesn't depend on the project's marketing language or the corporate counterparty's framing.

## Evidence & Examples

### Helium governance trajectory (2022–2025)

The cleanest reference series in the wiki. Four documented votes, two pre-concentration and two post-concentration:

| Vote | Date | Total veHNT | Top voter % | Proxy labels in top 12 | Proposing entity + co-author proxies | % of yes votes |
|---|---|---:|---:|---|---|---:|
| [[Helium HIP-53 Vote Results — Helium Vote - 2022-07-25\|HIP-53]] | Jul 25, 2022 | 2.44M | (not displayed in 2022 portal) | none | n/a (Joey Padden et al.; not [[Nova Labs]]) | 97.22% |
| [[Helium HIP-138 Vote Results — Helium Vote - 2024-11-22\|HIP-138]] | Nov 22, 2024 | 476.22M | 15% (anonymous wallet `HKcAP…NgsJ`) | none in top 12 | n/a (no proxy labels visible) | 92.54% |
| [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03\|HIP-143]] | Apr 3, 2025 | 763.50M | 26% (Nova Labs) | Nova Labs, ferebee, Jay M., others | **Nova Labs 26% + ferebee 24% = 50%** | 90.53% |
| [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10\|HIP-148]] | Oct 10, 2025 | 902.28M | 31% (ferebee) | ferebee, Nova Labs, Jay M., AndrewsMD, Keith Rettig | **ferebee 31% + Nova Labs 26% = 57% of total vote** | 96.72% |

The pre-concentration baseline (HIP-138, Nov 2024) shows the top 12 voters with no labeled proxies. The post-concentration votes (HIP-143 and HIP-148) show the proposing entity and its co-author appearing as the top two labeled proxies, with combined shares above 50%. The compression of the concentration window (five months between HIP-138 and HIP-143) makes the inflection load-bearing.

**veHNT accumulation rate finding** (HIP-143 → HIP-148, six months): the Nova Labs proxy grew +21% in absolute veHNT; the ferebee proxy grew +55.5%. Both substantially faster than network average. The franchise architecture compounds through the lock-up mechanism: future HIPs will be progressively easier to pass without operator participation.

### The Foundation policy mechanism that enables the concentration

The audit explains the concentration pattern but does not by itself explain how it emerged. The mechanism is documented separately: the [[Helium Network|Helium Foundation]]'s official explainer on the August 2025 halving recommends operators "set a proxy as a backup to ensure you don't miss out on rewards" [[Helium Halving 2025 — Helium Blog - 2025-07-24]]. Foundation policy normalizes proxy delegation; the August 1, 2025 veHNT reset required re-delegation OR proxy assignment to retain reward eligibility. Operators who took the path of least resistance assigned a proxy. The largest proxies (Nova Labs, ferebee) are the residual concentration. The policy and the concentration are not coincidental; they are causally linked.

### Caveats specific to the Helium series

- **HIP-138's blank label column may be a portal-display difference**, not a "no labels existed in 2024" difference. The April-2025 HIP-143 portal may have begun displaying labels for proxies that existed (and voted) earlier but weren't shown. The audit should note this ambiguity. Resolving it would require querying the on-chain proxy registry for label-setting timestamps.
- **The single named "Against" voter in HIP-148 — Keith Rettig at 1.00%** — is a documented dissent that the audit should surface alongside the concentration finding. Naming Rettig publicly is the audit's accountability counter-move; concentration is more easily defended in the abstract than against named labeled opposition.
- **The ferebee–Nova Labs relationship is undisclosed.** The audit can document that the two proxies vote in alignment on every HIP that affects the franchise architecture. The audit cannot prove they are coordinating; it can show that the on-chain pattern is structurally identical to coordination. The downstream question (formal coordination vs. structural alignment) is open. Either answer is unflattering.

## Tensions & Counterarguments

- **"Proxies with large voting weight are vote consolidation, not coordination."** Sometimes true. The audit's response is the comparison to baseline (HIP-138 shows the network's voting weight wasn't always this concentrated) and the alignment record (the two proxies vote together on every HIP affecting the franchise architecture; never on opposite sides of any structural vote).
- **"This is how every shareholder vote works."** Closer to true than DAO advocates usually acknowledge. The audit's framing actually surfaces the symmetry: DAO governance votes look more like affiliated-shareholder votes than the "community consensus" framing claims. The editorial move is to make the symmetry explicit — and note that affiliated shareholder votes have disclosure regimes (SEC Rule 14a-6, related-party transaction rules) that DAO votes don't.
- **"The audit attacks legitimate large stakeholders."** The audit doesn't attack anyone. It surfaces the structure. The structure may or may not be defensible — that depends on the [[Franchise vs. Business]] question downstream of the audit.
- **"Anonymous wallets could be coordinating in the other direction."** Possible. The audit acknowledges this when noting Keith Rettig's named dissent is the only labeled opposition above 1% on HIP-148. The audit doesn't claim concentration is one-sided; it claims it's measurable. Symmetric concentration (organized opposition matching organized proposing entities) would be a different finding, equally surfaceable from the on-chain record.

## Related Concepts

- [[Franchise vs. Business]] — the substantive test the audit serves
- [[Auto-Renewal by Inaction]] — the design pattern that compounds the audit's findings: once a concentrated bloc passes a HIP with a sunset that re-arms by default, the concentration's influence compounds without requiring further votes
- [[Chokepoint Control]] — the audit surfaces a pricing-authority chokepoint at the DAO-procedural layer
- [[DePIN]] — the category most exposed to this pattern

## Key Sources

- [[Helium HIP-143 and the DePIN Franchise Architecture]] — the synthesis that names the audit
- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — worked example #1 (50% of yes votes)
- [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] — worked example #2 (57% of total vote; veHNT accumulation rate evidence)
- [[Helium HIP-138 Vote Results — Helium Vote - 2024-11-22]] — pre-concentration baseline
- [[Helium HIP-53 Vote Results — Helium Vote - 2022-07-25]] — historical baseline before proxy-display was standard
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]] — Foundation policy on proxy delegation; the mechanism behind the concentration
