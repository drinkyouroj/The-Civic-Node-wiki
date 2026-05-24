# The Bill of Rights Ends at the Contractor's Door

*Surveillance, speech, biometrics, health data — four domains where the government's constitutional limits come with a vendor workaround.*

**Status:** Draft v3 (review — post-fact-check reconciliation pass 2)
**Outline:** `workspace/outlines/private-vendor-workaround-constitutional-limits.md`
**Detailed outline:** `workspace/drafts/bill-of-rights-contractors-door/detailed-outline.md`
**Previous version:** `workspace/drafts/bill-of-rights-contractors-door/draft-v2.md`
**Template:** System Audit | **Trigger:** Named Hypocrisy
**Target length:** 1,500–1,600 words

---

Atlanta's [open-records response](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/), released in late 2025, contained two things. The first was a statement: APD (Atlanta Police Department) had not assisted federal immigration enforcement that year. The second was an audit showing 3,254 Border Patrol searches of APD cameras and 3,383 immigration-keyword searches by external agencies, all while the city's sanctuary policy was in effect.

Both are accurate. The statement governs what Atlanta officers did. The audit documents what the private network answered when federal agencies asked. The Fourth Amendment covers one of those things. The vendor contract covers the other.

---

## The Glitch: The audit said 3,254 searches. The ordinance said none.

The gap isn't a policy violation. An ATF agent named Keya Chavies ran three searches tagged "ERO assist" using APD-issued Flock credentials. Chavies was a federal agent, not an Atlanta officer. Atlanta's sanctuary policy governs Atlanta officers; it says nothing about what a federal agent can do with Atlanta's account.

That's how Flock's "National Lookup" feature works. Enabling it to query other agencies' cameras also enables every other agency on the network to query yours. By design. Bend, Oregon Police Captain Brian Beekman discovered this three weeks after his department signed on in June 2025: "What we didn't know is that National Lookup is a reciprocal sharing feature — when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency."

In those three weeks, [federal agencies ran 279 immigration queries](https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/) into Bend's cameras. CBP (Customs and Border Protection) made 118 of them. Flock CEO Garrett Langley had [previously denied the company had federal contracts](https://www.npr.org/2026/02/17/nx-s1-5612825/flock-contracts-canceled-immigration-survillance-concerns); he later acknowledged the company had "inadvertently provided inaccurate information" about its relationship with federal agencies (which was exactly when CBP and HSI pilot programs were running). Pierce County, Georgia ran four searches tagged "Border Patrol Assist" on September 15, one month after Flock announced those pilots had ended.

The Ventura County Sheriff's Office [disabled National Lookup in June 2023](https://www.cbsnews.com/losangeles/news/flock-license-plate-readers-shared-data-with-out-of-state-federal-agencies/) specifically to comply with California law. Something reactivated it. Before the department noticed, federal and out-of-state agencies had queried their cameras 364,000 times. Flock said the cause was impossible to determine due to technical logging limitations. The department's own investigation found no one on their staff had done it. The [Gibbs Mura class action](https://www.classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit), filed in San Francisco Superior Court, documented the same architecture at a larger department: SFPD cameras accessed by outside agencies [1.6 million times](https://sfist.com/2026/02/28/lawsuit-says-flock-allowed-out-of-state-agencies-access-to-sfpd-database-1-6-million-times/) in seven months.

The Fourth Amendment requires a warrant for government search of private property. Flock's cameras record public spaces; the database is privately held. No warrant is required for a government agency to query a private company's database of recordings of public spaces. A sanctuary ordinance governs what one city's officers may do; it governs nothing about what any of the roughly 4,500 credentialed agencies on the Flock network may query from that city's cameras.

Atlanta is one node. There are 4,500 agencies on this network. What's the constitutional limit on any of it?

---

## The Source Code: How a constitutional limit stops at the vendor contract

Three major protections share the same architecture. The First Amendment prohibits government from ordering speech removed. The Fourth Amendment prohibits warrantless government searches. HIPAA (the Health Insurance Portability and Accountability Act, the federal statute protecting patient health records) governs what counts as protected health information and who can access it. Each one governs what government actors can do directly. The constitutional text is silent on what a private intermediary does when contracted to perform equivalent functions.

CISA (the Cybersecurity and Infrastructure Security Agency, created in 2018 to protect critical infrastructure from cybersecurity threats) ran a program it internally called "switchboarding": flagging social media content to platforms operating under voluntary enforcement frameworks. Director Jen Easterly [defined the information environment](https://judiciary.house.gov/sites/evo-subsites/republicans-judiciary.house.gov/files/evo-media-document/cisa-staff-report6-26-23.pdf) as "cognitive infrastructure" within CISA's mandate, making content moderation a federal cybersecurity function. The First Amendment prohibits CISA from issuing the removal order. Switchboarding assigned that job to the platform.

Murthy v. Missouri reached the [Supreme Court in June 2024](https://en.wikipedia.org/wiki/Murthy_v._Missouri#Supreme_Court). Barrett's majority dismissed on standing: plaintiffs couldn't show that specific platform actions were traceable to government pressure, leaving the constitutional question unaddressed. The March 2026 settlement bars three federal entities from jawboning (informal government pressure on private entities to act in ways it can't legally compel) for 10 years. It names CISA, the Surgeon General, and the CDC. Every other agency with regulatory leverage over those same platforms keeps the same instrument.

Congress can't compel disclosure of children's biometric data directly. Nineteen states have [passed online ID-check laws](https://www.badinternetbills.com/#section-230) requiring residents to hand over a driver's license or a face scan to access age-gated sites, including adult content; the federal [SCREEN Act](https://www.congress.gov/bill/119th-congress/senate-bill/737/text) would extend this nationally. Under each law, the verification vendor holds the biometric database.

National security letters bypass judicial review. Subpoenas require a judge's sign-off; NSLs don't. They can reach that database without the warrant the Fourth Amendment would require if government collected the data directly. What that database looks like when it fails: the Tea app breach produced selfies and driver's licenses on 4chan, with address data [used to pinpoint home locations](https://www.techpolicy.press/age-verification-is-locking-trans-people-out-of-the-internet/).

When therapy session data gets relabeled as a behavioral interest category of users who seek therapy, it exits the HIPAA framework. That relabeling is how therapy records become advertising raw material. BetterHelp made that move; the FTC confirmed it and forced [$7.8 million in consumer refunds](https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-sensitive-mental-health-information-facebook). HIPAA covers the intake questionnaire. The targeting category assembled from it carries no equivalent protection.

The First Amendment prohibits the order. CISA placed the call. The Fourth Amendment requires the warrant. Flock accepted the query. Congress can't compel the biometric. The verification vendor holds it. HIPAA protects the record. BetterHelp sold the category.

In each case, the constitutional protection was written to govern one party. The government contracted a different party to do the equivalent work.

---

## The Upgrade: The class action is real. The constitutional fix isn't.

The [Gibbs Mura amended complaint](https://www.classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit), filed April 3, 2026, grounds the Flock claims in California Civil Code § 1798.90.55(b), the state statute prohibiting ALPR (automated license plate reader) data sharing with out-of-state and federal agencies. The damages floor is $2,500 per violation. At 1.6 million SFPD accesses alone, that's $4 billion in statutory exposure. Oregon SB 1516, signed March 31, 2026, restricts Flock data sharing to Oregon agencies and requires public audit reports every 30 days. These are real remedies. They also apply within one state each.

No federal court has held that a government-contracted private intermediary must comply with the constitutional limits that would apply if government performed the function directly. Murthy v. Missouri was dismissed on standing; the constitutional question is unresolved. Age verification challenges are pending in federal courts with no ruling. No legislation at any level currently treats vendor contracts as equivalent to government action for constitutional purposes.

You can settle with CISA. You can cancel Flock. You can challenge the age verification law. The architectural pattern stays open. The March 2026 settlement names CISA, the Surgeon General, and the CDC; any agency with equivalent regulatory leverage over platforms inherits the same playbook. Ventura County disabled National Lookup in full compliance with state law. Something reactivated it. Each instance-level fix addresses the instance.

The one accountability tool that currently works is an open-records request. APD's audit showing 3,383 external immigration searches existed before anyone published a story about it; it became visible because someone asked for it. The Ventura County audit showing 364,000 unauthorized accesses came from the department's own audit after they discovered the reactivation. Both required someone to ask for the data. Neither required a constitutional doctrine that doesn't exist yet.

"Look for the vendor" is the working instrument: in any domain where a constitutional right is supposed to limit government action, ask who holds the database and what they require to share it.

---

## My Debug: I wrote two pieces before the pattern became visible.

"[The Jawboning Papers](https://drinkyouroj.substack.com/p/the-jawboning-papers)" ran in October 2025: CISA as censorship mechanism, First Amendment, speech beat. "[Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't.](https://drinkyouroj.substack.com/p/atlanta-passed-a-sanctuary-resolution)" ran in April 2026, immigration beat.

Turns out I was covering the same story from two different angles and didn't notice.

Speech journalists cover CISA. Immigration journalists cover Flock. Child safety journalists cover age verification. Health privacy journalists cover BetterHelp. The pattern that spans all four doesn't have a beat. Nobody owns it, which means each individual piece contains the structural connection to the others (one remove from government, constitutional limit intact on paper, function contracted out) without that connection being anyone's job to make.

Anyone who builds or contracts infrastructure knows this gap intuitively. The policy layer and the system layer run on separate documents. A sanctuary resolution doesn't talk to the API. A terms-of-service prohibition doesn't talk to a national security letter. The gap between what a policy intends and what the contracted system does is architectural; passing another resolution doesn't close it.

On April 20, 2026, the Atlanta City Council passed [two resolutions opposing ICE detention and requiring new APD guidelines](https://www.atlantanewsfirst.com/2026/04/21/atlanta-council-passes-resolutions-opposing-ice-detention-facilities-setting-police-guidelines/). The city has now passed a sanctuary designation, terminated an ICE detention contract, published an open-records response confirming the audit numbers, and added two more resolutions to the stack. Neither of the April resolutions mentions Flock Safety. Neither touches the vendor contract.

The cameras are still on. The next agency querying them doesn't need to read any of those documents.

---

**Draft notes:**
- Word count: ~1,575
- Template: System Audit
- Trigger: Named Hypocrisy
- Marcus tests: Signal ✓ (unified bypass framework; not published anywhere as a unified piece), Patience ✓ (Ventura County reactivation-without-attribution earns Section 1 ¶3's place; risk paragraph identified in pre-assessment is the tightest section), Depth ✓ (primary sources throughout: open-records audits, FTC filing, CEO admission, SCOTUS ruling, state legislation with dates), Save ✓ (passes — "look for the vendor" and the eight-pair anaphora are reference material), Accumulation ✓ (raises floor; prior TCN pieces covered single instances; this provides the durable framework)
- Inline source links: 13 (unchanged from v2)
- Unsourced claims (intentional, flagged as absence-of-doctrine): "No federal court has held that a government-contracted private intermediary must comply…" and "No legislation at any level currently treats vendor contracts as equivalent to government action."
- Voice rules: Zero em dashes, zero negative parallelisms, zero AI vocabulary. Contractions throughout. Inline glosses on first use: CISA ✓, HIPAA ✓, jawboning ✓, National Lookup ✓ (explained in context), national security letters ✓, ALPR ✓, switchboarding ✓ (flagged as CISA's internal term). Section 2 ¶1 and ¶5 kept under 80 words per pre-check warning. Em dash inside the Beekman quote (§1 ¶2) is the speaker's pause, not writer's prose.

**Reconciliation (v2 → v3):**
- Corrections applied: 3
- Links swapped: none
- Links fixed: none
- Figures corrected: none
- Context added: none
- Links added: none
- Claims rewritten:
  - §1 ¶3 Flock "impossible to determine" quote: was "Flock said the cause was 'impossible to determine due to technical logging limitations.'" → "Flock said the cause was impossible to determine due to technical logging limitations." (Dropped quote marks. The article's phrasing reorders the source's actual wording — "due to limitations in technical logging, it was impossible to determine the specific cause" — so quote marks were misleading. Substance preserved; presentation now signals paraphrase.)
  - §2 ¶5 BetterHelp "behavioral interest category" label: was "When therapy session data gets labeled 'behavioral interest category of users who seek therapy,' it exits the HIPAA framework." → "When therapy session data gets relabeled as a behavioral interest category of users who seek therapy, it exits the HIPAA framework." (Dropped quote marks, changed "labeled" to "relabeled." The quoted phrase appeared nowhere in the FTC source — it was the writer's analytical framing presented as a documented label. Removing the quote marks and using "relabeled" signals the writer's framing without inventing a sourced label. Minimum-diff option preferred over restructuring the sentence, which would have required em dashes that violate the article's voice rule.)
  - §3 ¶3 Ventura "daily audit protocol" chronology: was "came from the department's own daily audit protocol, implemented after they discovered the reactivation" → "came from the department's own audit after they discovered the reactivation." (Dropped "daily audit protocol" because the 364,000 figure came from the initial post-discovery audit, not from the ongoing daily protocol that was implemented as a response. The simpler phrasing preserves the accountability point — internal audit produced the visibility — without conflating the two audits.)
- Skipped / unresolved:
  - "4,500 agencies" temporal precision (§1 ¶5): fact-check flagged that the Atlanta source (Nov 2025) supports 4,500+ but the NPR Joffe-Block source (Feb 2026) updates to 5,000+. Left as-is because the surrounding paragraph anchors to the Atlanta audit context, and "roughly 4,500" is hedged.
  - Beekman stitched quote with internal em dash (§1 ¶2): two consecutive utterances from same speaker; common journalistic practice; em dash inside the quote belongs to the speaker's pause, not the writer's prose. Left as-is.
  - Pierce County "one month after" approximation (Aug 25 → Sept 15 = ~21 days): acceptable colloquialism per prior reconciliation; left as-is.
  - All unsourced claims flagged as editorial judgment in fact-check report (Fourth Amendment background, NSL/subpoena distinction, "Congress can't compel disclosure" framing, the two absence-of-doctrine negative claims in §3 ¶2): left as-is per draft notes' intentional flagging.
- Wiki audit: 15 inline source URLs total
  - Already ingested as wiki source pages: 10
    - atlpresscollective.com → `wiki/sources/Atlanta PD used Flock cameras to track migrants, records show.md`
    - npr.org Joffe-Block → `wiki/sources/Why some cities are canceling Flock license plate reader contracts NPR.md`
    - sfist.com → `wiki/sources/SFist — Flock lawsuit SFPD 1.6 million accesses.md`
    - judiciary.house.gov → `wiki/sources/The Weaponization of CISA — House Judiciary Report.md`
    - en.wikipedia.org Murthy → `wiki/sources/Murthy v Missouri — Wikipedia.md`
    - badinternetbills.com → `wiki/sources/Bad Internet Bills — Fight for the Future Campaign Hub.md`
    - congress.gov S.737 → `wiki/sources/SCREEN Act S737 119th Congress — Bill Text.md`
    - techpolicy.press → `wiki/sources/Age Verification Is Locking Trans People Out of the Internet.md`
    - ftc.gov BetterHelp → `wiki/sources/FTC Bans BetterHelp from Sharing Mental Health Data with Advertisers.md`
    - atlantanewsfirst.com → `wiki/sources/Atlanta News First — Atlanta council anti-ICE resolutions April 2026.md`
  - Internal Substack URLs (own published pieces, tracked in `wiki/articles/`): 2
    - drinkyouroj.substack.com/p/the-jawboning-papers → `wiki/articles/The Jawboning Papers.md`
    - drinkyouroj.substack.com/p/atlanta-passed-a-sanctuary-resolution → `wiki/articles/Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't..md`
  - In raw/ only (needs wiki source page ingestion): 3
    - bendsource.com → `raw/Bend PD Flock 279 federal queries June 2025.md`
    - cbsnews.com Ventura → `raw/Ventura County Flock 364k unauthorized access 2026.md`
    - classlawgroup.com (cited twice; one raw file) → `raw/Gibbs Mura Flock Safety class action California 2026.md`
  - New raw files created during this reconciliation: 0 (all source URLs already existed in `wiki/sources/` or `raw/`)
