---
title: "SCREEN Act (S.737, 119th Congress) — Bill Text"
type: source
tags: [legislation, age-verification, censorship, surveillance, technology, politics, power, lgbtq]
created: 2026-05-24
updated: 2026-05-24
sources: 8
raw: "raw/Text - S.737 - 119th Congress (2025-2026) SCREEN Act.md"
source_url: "https://www.congress.gov/bill/119th-congress/senate-bill/737/text"
author: "Sen. Mike Lee (R-UT) — sponsor; Sens. Curtis and Banks — cosponsors"
published: 2025-02-26
---

[Original source](https://www.congress.gov/bill/119th-congress/senate-bill/737/text)

## Summary
S.737 ("Shielding Children's Retinas from Egregious Exposure on the Net Act," or SCREEN Act) is the leading federal vehicle to nationalize age verification for any online platform that creates, hosts, or makes available content "harmful to minors" with a profit motive. Introduced by Sen. Mike Lee (R-UT) on February 26, 2025, the bill mandates that covered platforms adopt "technology verification measures" within one year of enactment, explicitly bars self-attestation as sufficient compliance, and routes IP-based verification through every U.S. user (including known VPN IPs). Enforcement vests in the FTC under its Section 5 unfair-or-deceptive-practices authority. The bill explicitly permits — and is architected around — third-party verification vendors, while preserving covered-platform liability. As of late May 2026 the bill remains in the Senate Commerce Committee.

## Key Points
- **Covered platforms** are defined broadly: any interactive computer service engaged in interstate commerce that creates, hosts, or makes available "harmful to minors" content as a regular course of business — *regardless of whether that content is the entity's sole or principal source of income* (§3(3)(B)).
- **"Harmful to minors"** pulls directly from existing obscenity law (§3(4)): patently offensive, appeals to prurient interest, lacks serious literary/artistic/political/scientific value as to minors. Also includes anything "obscene" or "child pornography."
- **Self-attestation is explicitly insufficient** (§4(b)(2)) — the verification must be technological. The bill defines a "technology verification measure" as any system that determines "whether it is more likely than not that a user… is a minor" (§3(7)).
- **All U.S. IPs are subject** (§4(b)(4)) — including "known virtual proxy network IP addresses." Only users the platform can determine are outside the U.S. are exempt.
- **Third-party verification vendors are explicitly authorized** (§4(d)): "A covered platform may contract with a third party to employ technology verification measures… but the use of such a third party shall not relieve the covered platform of its obligations under this Act or from liability." Note the asymmetry — platform liability is preserved, vendor liability is unaddressed.
- **Data security** language (§4(f)) requires "reasonable data security" and a retention limit of "no longer than is reasonably necessary." No specific encryption, audit, breach-notification, or deletion standards.
- **The bill avoids submitting user data to the Commission** (§4(e)) — but says nothing about what the verification vendor must (or must not) do with the same data internally.
- **FTC enforces** (§7) — violations treated as unfair or deceptive acts under 15 U.S.C. 57a(a)(1)(B). FTC must issue guidance within 180 days of enactment (§6(b)(1)) and consult with computer scientists, child safety advocates, consumer/privacy experts, age-verification vendors, and cryptographers (§5).
- **GAO study** due two years after the compliance date (§8) — covers effectiveness, compliance rates, data-security measures, and behavioral/economic/psychological/societal effects.
- **Severability clause** (§9) — if any provision held unconstitutional, the rest survives.
- **Findings** (§2) explicitly position SCREEN as Congress's third attempt at this regulatory pattern after the Communications Decency Act (Title V of P.L. 104-104) and the Child Online Protection Act (47 U.S.C. 231), both struck down by SCOTUS in *Ashcroft v. ACLU*, 542 U.S. 656 (2004). The Findings argue that the technology has now evolved enough to make age verification the "least restrictive means" — a legal claim, not a technical one.
- **Findings cite**: 17 states have declared pornography a public health hazard; 80% of minors 12–17 have been exposed to pornography (54% sought it out); only 39% of parents use blocking/filtering software; Kaiser Family Foundation finding that filters fail on ~10% of intentionally accessed and ~33% of unintentionally accessed pornography sites.

## Newsletter Angles
- **Federal-level confirmation of the vendor-workaround pattern** documented in [[The Bill of Rights Ends at the Contractor's Door]]. SCREEN explicitly authorizes third-party verification vendors to hold the biometric/ID database; the constitutional limit (Congress can't compel disclosure of children's biometric data directly) lands on the platform; the database itself sits with a vendor unaddressed by the bill's liability framework. The structural pair is the entire thesis of that article: government contracts the function it can't perform directly.
- **The "least restrictive means" claim is the constitutional attack surface.** Past attempts (CDA, COPA) failed the *Ashcroft* test because filtering software was the less-restrictive alternative. SCREEN's §2 Findings explicitly preempt this by arguing technology has changed. But Findings are not evidence; the implementing record is what would survive an *as-applied* First Amendment challenge, and the implementing record is bound to include known VPN IPs being verified, biometric data sitting with private vendors, and breach histories like [[Age Verification Is Locking Trans People Out of the Internet|the Tea app leak]].
- **FTC enforcement parallels the BetterHelp pattern.** Like the BetterHelp action under FTC Section 5, this routes around HIPAA-style sectoral privacy law. The bill never amends HIPAA, the Communications Decency Act, or the Children's Online Privacy Protection Act — it bolts a new vendor-mediated verification regime onto Section 230's existing platform architecture.
- **IP-blanket framing erases the consent layer.** §4(b)(4)'s sweep through all U.S. IPs, including VPN IPs, means there is no opt-out for adults. This is the operational truth of "the verification vendor holds the biometric database" in [[The Bill of Rights Ends at the Contractor's Door]]: every U.S. adult who wants to access a covered platform sits in the vendor's database by default.

## Entities Mentioned
- [[SCREEN Act]] — this bill (federal age-verification mandate)
- [[Mike Lee]] — sponsor (R-UT); first appearance, deferred stub
- [[Federal Trade Commission]] — enforcement agency
- [[Kids Online Safety Act (KOSA)]] — sibling federal vehicle in the child-safety legislative cluster
- [[Fight for the Future]] — primary opposition coalition organizer

## Concepts Mentioned
- [[Age Verification]] — operational mechanism the bill mandates
- [[Section 230]] — bill imports its definitions ("interactive computer service," "information content provider") from 47 U.S.C. 230(f)
- [[Surveillance infrastructure]] — vendor-held biometric/ID databases as new infrastructure
- "Least restrictive means" — the constitutional test the bill is engineered to satisfy
- "Harmful to minors" — pulled wholesale from existing obscenity law

## Quotes
> "Beginning on the date that is 1 year after the date of enactment of this Act, a covered platform shall adopt and utilize technology verification measures on the platform to ensure that— (1) users of the covered platform are not minors; and (2) minors are prevented from accessing any content on the covered platform that is harmful to minors." — §4(a)

> "A covered platform may contract with a third party to employ technology verification measures for purposes of complying with subsection (a), but the use of such a third party shall not relieve the covered platform of its obligations under this Act or from liability under this Act." — §4(d)

> "Subject the Internet Protocol (IP) addresses, including known virtual proxy network IP addresses, of all users of a covered platform to the technology verification measure described in paragraph (1) unless the covered platform determines based on available technology that a user is not located within the United States." — §4(b)(4)

> "[R]equiring interactive computer services that are in the business of creating, hosting, or making available pornographic content to enact technological measures that shield minors from accessing pornographic content on their platforms is the least restrictive means for Congress to achieve its compelling government interest." — §2(b)(2)

## Notes
This is the primary text of S.737 as introduced on 2026-02-26 (note: bill year 2025; the text predates the Trump II administration but is the active text in the 119th Congress as of May 2026). No companion House bill identified in this raw file. Status: Introduced, referred to Senate Commerce, Science, and Transportation. No committee action yet recorded.

Cited in [[Bad Internet Bills — Fight for the Future Campaign Hub]] as the federal extension of the 19-state online ID-check laws. Cited in [[The Bill of Rights Ends at the Contractor's Door]] (TCN article, in draft v2 reconciliation as of 2026-05-24) as the federal-level instance of the vendor-workaround pattern.

The bill's structural logic — government can't compel the biometric → vendor holds it — is the cleanest legislative-text-level confirmation the wiki holds for that pattern. Should anchor any future synthesis on the [[Vendor Workaround Pattern|vendor workaround as a federal-statute design choice]].
