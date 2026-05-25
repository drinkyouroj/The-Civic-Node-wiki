# The Bill of Rights Ends at the Contractor's Door

*Surveillance, speech, biometrics, health data — four domains where the government's constitutional limits come with a vendor workaround.*

**Status:** Draft v5 (review — post-fact-check reconciliation pass 4)
**Outline:** `workspace/outlines/private-vendor-workaround-constitutional-limits.md`
**Detailed outline:** `workspace/drafts/bill-of-rights-contractors-door/detailed-outline.md`
**Previous version:** `workspace/drafts/bill-of-rights-contractors-door/draft-v4.md`
**Template:** System Audit | **Trigger:** Named Hypocrisy
**Target length:** 1,500–1,600 words

---

Atlanta's [open-records response](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/), released in late 2025, contained two things. The first was a statement: APD (Atlanta Police Department) had not assisted federal immigration enforcement that year. The second was an audit showing 3,254 Border Patrol searches of APD cameras and 3,383 immigration-keyword searches by external agencies, all while the city's sanctuary policy was in effect.

Both are accurate. The statement governs what Atlanta officers did. The audit documents what the private network answered when federal agencies asked. The Fourth Amendment covers one of those things. The vendor contract covers the other.

---

## The Glitch: The audit said 3,254 searches. The ordinance said none.

An ATF intelligence specialist named Keya Chavies ran three searches tagged "ERO assist" using APD-issued Flock credentials. Chavies was a federal employee, not an Atlanta officer. Atlanta's sanctuary policy governs Atlanta officers; it says nothing about what a federal agent can do with Atlanta's account.

That's how Flock's "National Lookup" feature works. Enabling it to query other agencies' cameras also enables every other agency on the network to query yours. By design. Bend, Oregon Police Captain Brian Beekman discovered this three weeks after his department signed on in June 2025: "What we didn't know is that National Lookup is a reciprocal sharing feature — when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency."

In those three weeks, [federal agencies ran 279 immigration queries](https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/) into Bend's cameras. CBP (Customs and Border Protection) made 118 of them. Flock CEO Garrett Langley had [previously denied the company had federal contracts](https://www.npr.org/2026/02/17/nx-s1-5612825/flock-contracts-canceled-immigration-survillance-concerns); he later acknowledged the company had "inadvertently provided inaccurate information" about its relationship with federal agencies. The inaccuracy covered exactly the period when CBP and HSI (Homeland Security Investigations) pilot programs were running. [Pierce County, Georgia ran four searches](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/) tagged "Border Patrol Assist" on September 15, one month after Flock announced those pilots had ended.

The Ventura County Sheriff's Office [disabled National Lookup in June 2023](https://www.cbsnews.com/losangeles/news/flock-license-plate-readers-shared-data-with-out-of-state-federal-agencies/) specifically to comply with California law. Something reactivated it. Without departmental approval or knowledge, federal and out-of-state agencies queried their cameras 364,000 times. Flock said the cause was impossible to determine due to technical logging limitations. The department's own investigation found no one on their staff had done it. The [Gibbs Mura class action](https://www.classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit), filed in San Francisco Superior Court, documented the same architecture at a larger department: SFPD cameras accessed by outside agencies [1.6 million times](https://sfist.com/2026/02/28/lawsuit-says-flock-allowed-out-of-state-agencies-access-to-sfpd-database-1-6-million-times/) in seven months.

The Fourth Amendment requires a warrant for government search of private property. Flock's cameras record public spaces; the database is privately held. No warrant is required for a government agency to query a private company's database of recordings of public spaces. A sanctuary ordinance governs what one city's officers may do; it governs nothing about what any of the [roughly 4,500 credentialed agencies](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/) on the Flock network may query from that city's cameras.

Atlanta is one node. There are [4,500 agencies](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/) on this network. What's the constitutional limit on any of it?

---

## The Source Code: How a constitutional limit stops at the vendor contract

Three major protections share the same architecture. The First Amendment prohibits government from ordering speech removed. The Fourth Amendment prohibits warrantless government searches. HIPAA (the Health Insurance Portability and Accountability Act, the federal statute protecting patient health records) governs what counts as protected health information and who can access it. Each one governs what government actors can do directly. The constitutional text is silent on what a private intermediary does when contracted to perform equivalent functions.

CISA (the Cybersecurity and Infrastructure Security Agency, created in 2018 to protect critical infrastructure from cybersecurity threats) ran a program it internally called "[switchboarding](https://judiciary.house.gov/sites/evo-subsites/republicans-judiciary.house.gov/files/evo-media-document/cisa-staff-report6-26-23.pdf)": flagging social media content to platforms that acted on it under their own content policies. Director Jen Easterly [defined the information environment](https://judiciary.house.gov/sites/evo-subsites/republicans-judiciary.house.gov/files/evo-media-document/cisa-staff-report6-26-23.pdf) as "cognitive infrastructure" within CISA's mandate, making content moderation a federal cybersecurity function. The First Amendment prohibits CISA from issuing the removal order. Switchboarding assigned that job to the platform.

Murthy v. Missouri reached the [Supreme Court in June 2024](https://en.wikipedia.org/wiki/Murthy_v._Missouri#Supreme_Court). Barrett's majority dismissed on standing: plaintiffs couldn't show that specific platform actions were traceable to government pressure, leaving the constitutional question unaddressed. The [March 2026 settlement](https://en.wikipedia.org/wiki/Murthy_v._Missouri#Supreme_Court) bars three federal entities from jawboning (informal government pressure on private entities to act in ways it can't legally compel) for 10 years. It names CISA, the Surgeon General, and the CDC. Every other agency with regulatory leverage over those same platforms keeps the same instrument.

Congress can't compel disclosure of children's biometric data directly. Nineteen states have [passed online ID-check laws](https://www.badinternetbills.com/) requiring residents to hand over a driver's license or a face scan to access age-gated sites, including adult content; the federal [SCREEN Act](https://www.congress.gov/bill/119th-congress/senate-bill/737/text) would extend this nationally. Under each law, the verification vendor holds the biometric database.

National security letters bypass judicial review. Subpoenas require a judge's sign-off; NSLs don't. They can reach that database without the warrant the Fourth Amendment would require if government collected the data directly. What that database looks like when it fails: the Tea app breach produced selfies and driver's licenses on 4chan, with address data [used to pinpoint home locations](https://www.techpolicy.press/age-verification-is-locking-trans-people-out-of-the-internet/).

When therapy session data gets relabeled as a behavioral interest category of users who seek therapy, it exits the HIPAA framework. That relabeling is how therapy records become advertising raw material. BetterHelp made that move; the FTC confirmed it and forced [$7.8 million in consumer refunds](https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-sensitive-mental-health-information-facebook). HIPAA covers the intake questionnaire. The targeting category assembled from it carries no equivalent protection.

The First Amendment prohibits the order. CISA placed the call. The Fourth Amendment requires the warrant. Flock accepted the query. Congress can't compel the biometric. The verification vendor holds it. HIPAA protects the record. BetterHelp sold the category.

In each case, the constitutional protection was written to govern one party. The government contracted a different party to do the equivalent work.

---

## The Upgrade: The class action is real. The constitutional fix isn't.

The [Gibbs Mura amended complaint](https://www.classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit) (filed April 3, 2026) grounds the Flock claims in California Civil Code § 1798.90.55(b), the state statute prohibiting ALPR (automated license plate reader) data sharing with out-of-state and federal agencies. The damages floor is $2,500 per violation. At 1.6 million SFPD accesses alone, that's $4 billion in statutory exposure. [Oregon SB 1516](https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/SB1516/Enrolled), signed March 31, 2026, restricts Flock data sharing to Oregon agencies and requires public audit reports every 30 days. These are real remedies. They also apply within one state each.

No federal court has held that a government-contracted private intermediary must comply with the constitutional limits that would apply if government performed the function directly. Murthy v. Missouri was dismissed on standing; the constitutional question is unresolved. No legislation at any level currently treats vendor contracts as equivalent to government action for constitutional purposes.

You can settle with CISA. You can cancel Flock. You can challenge the age verification law. The architectural pattern stays open. The March 2026 settlement names CISA, the Surgeon General, and the CDC; any agency with equivalent regulatory leverage over platforms inherits the same playbook. Ventura County disabled National Lookup in full compliance with state law. Something reactivated it. Each instance-level fix addresses the instance.

Right now, the only accountability tool that works is an open-records request. APD's audit showing 3,383 external immigration searches existed before anyone published a story about it; it became visible because someone asked for it. The Ventura County audit showing 364,000 unauthorized accesses came from the department's own audit after they discovered the reactivation. Both required someone to ask for the data. Neither required a constitutional doctrine that doesn't exist yet.

"Look for the vendor" is the working instrument: in any domain where a constitutional right is supposed to limit government action, ask who holds the database and what they require to share it.

---

## My Debug: I wrote two pieces before the pattern became visible.

"[The Jawboning Papers](https://drinkyouroj.substack.com/p/the-jawboning-papers)" ran in October 2025: CISA as censorship mechanism, First Amendment, speech beat. "[Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't.](https://drinkyouroj.substack.com/p/atlanta-passed-a-sanctuary-resolution)" ran in April 2026, immigration beat.

Turns out I was covering the same story from two different angles and didn't notice.

Speech journalists cover CISA. Immigration journalists cover Flock. Child safety journalists cover age verification. Health privacy journalists cover BetterHelp. The pattern that spans all four doesn't have a beat. Nobody owns it. Each individual piece contains the structural connection to the others (one remove from government, constitutional limit intact on paper, function contracted out), but making that connection is nobody's job.

Anyone who builds or contracts infrastructure knows this gap intuitively. The policy layer and the system layer run on separate documents. A sanctuary resolution doesn't talk to the API. A terms-of-service prohibition doesn't talk to a national security letter. The gap between what a policy intends and what the contracted system does is architectural; passing another resolution doesn't close it.

On April 20, 2026, the Atlanta City Council passed [two resolutions opposing ICE detention and requiring new APD guidelines](https://www.atlantanewsfirst.com/2026/04/21/atlanta-council-passes-resolutions-opposing-ice-detention-facilities-setting-police-guidelines/). The city has now passed a sanctuary designation, terminated an ICE detention contract, published an open-records response confirming the audit numbers, and added two more resolutions to the stack. Neither of the April resolutions mentions Flock Safety. Neither touches the vendor contract.

The cameras are still on. The next agency querying them doesn't need to read any of those documents.

---

**Draft notes:**
- Word count: ~1,567 (unchanged from v4)
- Template: System Audit
- Trigger: Named Hypocrisy
- Marcus tests: Signal ✓ (unified bypass framework; not published anywhere as a unified piece), Patience ✓ (Ventura County reactivation-without-attribution earns Section 1 ¶3's place; risk paragraph identified in pre-assessment is the tightest section), Depth ✓ (primary sources throughout: open-records audits, FTC filing, CEO admission, SCOTUS ruling, state legislation with dates), Save ✓ (passes — "look for the vendor" and the eight-pair anaphora are reference material), Accumulation ✓ (raises floor; prior TCN pieces covered single instances; this provides the durable framework)
- Inline source links: 18 (was 14 in v4; +4 from fact-check reconciliation pass 4 — see Reconciliation v4→v5 below)
- Unsourced claims (intentional, flagged as absence-of-doctrine): "No federal court has held that a government-contracted private intermediary must comply…" and "No legislation at any level currently treats vendor contracts as equivalent to government action."
- Voice rules: Zero em dashes, zero negative parallelisms, zero AI vocabulary. Contractions throughout. Inline glosses on first use: CISA ✓, HIPAA ✓, jawboning ✓, National Lookup ✓ (explained in context), national security letters ✓, ALPR ✓, switchboarding ✓ (flagged as CISA's internal term, now linked). Section 2 ¶1 and ¶5 kept under 80 words per pre-check warning. Em dash inside the Beekman quote (§1 ¶2) is the speaker's pause, not writer's prose.

**Reconciliation (v4 → v5):**
- Corrections applied: 4
- Links swapped: 0
- Links fixed: 0
- Figures corrected: 0
- Context added: 0
- Links added: 4
  - "switchboarding" (§2 ¶1): added inline link to House Judiciary PDF (judiciary.house.gov). Term confirmed in source as Section I.A heading ("Switchboarding: CISA's coordination with Big Tech to censor Americans") and in Scully deposition transcript ("in a process known as 'switchboarding'"). Same URL as the existing "defined the information environment" link one sentence later — two links, same source, different anchored claims.
  - "roughly 4,500 credentialed agencies" (§1 ¶4): added inline link to Atlanta open-records source (atlpresscollective.com). Source confirms "nearly 4,500 different agencies have conducted over 10.6 million searches that used APD's Flock cameras since the beginning of 2025."
  - "4,500 agencies" (§1 ¶5): added inline link to Atlanta open-records source (atlpresscollective.com). Same source as above; second occurrence in §1 now linked.
  - "Pierce County, Georgia ran four searches" (§1 ¶3): added inline link to Atlanta open-records source (atlpresscollective.com). Raw source confirms verbatim: "The Sheriff's Department for Pierce County in southeastern Georgia conducted four searches that hit Atlanta's network on Sept. 15. The reason for each of those searches was labeled in the audit as 'Border Patrol Assist.'" Count of four verified in raw file.
- Claims rewritten: 0
- Skipped / unresolved (carried forward from prior reconciliations):
  - Chavies sentence (§2 ¶1): no inline link on "Keya Chavies" or "ATF intelligence specialist." Acceptable as editorial continuation of the Atlanta source linked in §1 opener. Left as-is per fact-check U1 finding (low priority).
  - "4,500 agencies" vs. "5,000+" count tension: NPR Joffe-Block source (Feb 2026) says 5,000+; Atlanta source (Nov 2025) says ~4,500. "Roughly 4,500" remains appropriate to the Atlanta audit context with hedging preserved. Left as-is.
  - Pierce County "one month after" approximation (Aug 25 → Sept 15 = ~21 days): acceptable colloquialism per prior reconciliation. Left as-is.
  - All unsourced claims flagged as editorial judgment (Fourth Amendment background, NSL/subpoena distinction, "Congress can't compel disclosure" framing, the two absence-of-doctrine negative claims in §3 ¶2): left as-is.
- Wiki audit: 18 inline source link occurrences, 14 unique source URLs (was 14 occurrences / 14 unique URLs in v4). No new source URLs introduced; all new links reuse already-tracked sources. No new raw files needed.
  - atlpresscollective.com → `wiki/sources/Atlanta PD used Flock cameras to track migrants, records show.md` ✓ (now cited 4×: intro + §1 ¶3 Pierce County + §1 ¶4 "4,500 credentialed" + §1 ¶5 "4,500 agencies")
  - judiciary.house.gov → `wiki/sources/The Weaponization of CISA — House Judiciary Report.md` ✓ (now cited 2×: §2 ¶1 "switchboarding" + §2 ¶1 "defined the information environment")
  - bendsource.com → `raw/Bend PD Flock 279 federal queries June 2025.md` ✓
  - npr.org → `wiki/sources/Why some cities are canceling Flock license plate reader contracts NPR.md` ✓
  - cbsnews.com → `raw/Ventura County Flock 364k unauthorized access 2026.md` ✓
  - classlawgroup.com → `raw/Gibbs Mura Flock Safety class action California 2026.md` ✓ (cited 2×)
  - sfist.com → `wiki/sources/SFist — Flock lawsuit SFPD 1.6 million accesses.md` ✓
  - en.wikipedia.org → `wiki/sources/Murthy v Missouri — Wikipedia.md` ✓
  - badinternetbills.com → `wiki/sources/Bad Internet Bills — Fight for the Future Campaign Hub.md` ✓
  - congress.gov → `wiki/sources/SCREEN Act S737 119th Congress — Bill Text.md` ✓
  - techpolicy.press → `wiki/sources/Age Verification Is Locking Trans People Out of the Internet.md` ✓
  - ftc.gov → `wiki/sources/FTC Bans BetterHelp from Sharing Mental Health Data with Advertisers.md` ✓
  - olis.oregonlegislature.gov → `wiki/sources/Oregon SB 1516 — Enrolled Bill Text.md` ✓
  - atlantanewsfirst.com → `wiki/sources/Atlanta News First — Atlanta council anti-ICE resolutions April 2026.md` ✓

**Reconciliation (v3 → v4):**
- Corrections applied: 3
- Links swapped: 0
- Links fixed: 1 (badinternetbills.com fragment dropped)
- Links added: 1 (Oregon SB 1516 → OLIS primary text)
- Figures corrected: 0
- Context added: 0
- Claims rewritten:
  - §2 ¶1 Chavies title: was "An ATF agent named Keya Chavies… Chavies was a federal agent, not an Atlanta officer." → "An ATF intelligence specialist named Keya Chavies… Chavies was a federal employee, not an Atlanta officer." (Source [[Atlanta PD used Flock cameras to track migrants, records show]] identifies Chavies as ATF Intelligence Specialist, a civilian analyst role rather than a sworn Special Agent. "Federal employee" replaces "federal agent" in the immediately following sentence to maintain internal consistency about Chavies specifically. The generic third reference — "what a federal agent can do with Atlanta's account" — left unchanged because it refers to any federal-credentialed actor, not Chavies specifically; "agent" as loose journalistic shorthand for the abstract case is acceptable.)
  - §2 ¶3 Ventura temporal framing: was "Before the department noticed, federal and out-of-state agencies had queried their cameras 364,000 times." → "Without departmental approval or knowledge, federal and out-of-state agencies queried their cameras 364,000 times." (The CBS source frames the 364,000 figure as occurring February–March 2025 "without departmental approval or knowledge," while discovery itself was in early February. Replaced the "Before noticed" framing — which read as if all 364k accesses happened before discovery — with the source's exact phrasing. Past perfect "had queried" → simple past "queried" because the temporal anchor is gone.)
  - §4 ¶2 deleted sentence: removed "Age verification challenges are pending in federal courts with no ruling." (Free Speech Coalition v. Paxton was decided by SCOTUS in June 2025 upholding Texas's age-verification law under intermediate scrutiny. The sentence's intended meaning — no ruling on whether the verification vendor inherits constitutional limits — is covered by the preceding two sentences about Murthy and absence of doctrine. Deletion eliminates the FSC v. Paxton exposure without losing argumentative ground.)
- Links updated:
  - §3 ¶4 badinternetbills.com URL: dropped `#section-230` fragment. The anchor pointed to the Section 230 portion of the page, but the cited claim is about the Online ID Checks section. Bare URL lands on the page where the reader can see both.
  - §4 ¶1 Oregon SB 1516: added inline link to OLIS primary-text URL (`https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/SB1516/Enrolled`). Matches the article's pattern of linking primary statutory text where available (congress.gov for SCREEN Act, judiciary.house.gov for CISA report). Primary-text wiki source page is `wiki/sources/Oregon SB 1516 — Enrolled Bill Text.md`.
- Skipped / unresolved (carried forward from prior reconciliations):
  - "4,500 agencies" temporal precision (§1 ¶5): NPR Joffe-Block source (Feb 2026) updates to 5,000+; Atlanta source (Nov 2025) supports 4,500+. Left as-is because the surrounding paragraph anchors to the Atlanta audit context, and "roughly 4,500" is hedged.
  - Beekman stitched quote with internal em dash (§1 ¶2): two consecutive utterances from same speaker; common journalistic practice; em dash inside the quote belongs to the speaker's pause, not the writer's prose. Left as-is.
  - Pierce County "one month after" approximation (Aug 25 → Sept 15 = ~21 days): acceptable colloquialism per prior reconciliation; left as-is.
  - All unsourced claims flagged as editorial judgment (Fourth Amendment background, NSL/subpoena distinction, "Congress can't compel disclosure" framing, the two absence-of-doctrine negative claims in §3 ¶2): left as-is per draft notes' intentional flagging.
- Wiki audit: 14 inline source URLs total (was 13 in v3; +1 Oregon SB 1516 OLIS)
  - Already ingested as wiki source pages: 11 (was 10; +1 Oregon SB 1516 enrolled bill text)
  - Internal Substack URLs (own published pieces, tracked in `wiki/articles/`): 2
  - In raw/ only (needs wiki source page ingestion): 3
