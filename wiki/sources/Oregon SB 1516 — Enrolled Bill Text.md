---
title: "Oregon SB 1516 (2026) — Enrolled Bill Text"
type: source
tags: [legislation, surveillance, alpr, vendor-liability, oregon, civil-liberties, public-safety, criminal-justice]
created: 2026-05-24
updated: 2026-05-24
sources: 12
raw: "raw/Oregon SB 1516 Enrolled.pdf"
source_url: "https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/SB1516/Enrolled"
author: "83rd Oregon Legislative Assembly — Senate Interim Committee on Judiciary"
published: 2026-03-05
---

[Original source — Oregon Legislative Information System (OLIS)](https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/SB1516/Enrolled)

## Summary
Oregon Senate Bill 1516, 83rd Legislative Assembly, 2026 Regular Session — an omnibus public safety act with three distinct parts (Pretrial Release; Automated License Plate Recognition Systems; Justice Reinvestment Equity Program). The ALPR sections (3–9) are the wiki-relevant core: they restrict law enforcement agency use of ALPR data, prohibit data sharing with non-Oregon government entities except for narrowly-defined law-enforcement purposes (and bar unrestricted or ongoing access in those exceptions), set a 30-day retention limit on non-investigative captured plate data, require monthly vendor audits and quarterly third-party-search audits with public posting within two days, and — most significantly for the wiki's vendor-workaround thread — **impose explicit vendor liability provisions in any ALPR contract**, including end-to-end encryption requirements, prohibition on vendor use or licensing of captured data, vendor data-ownership disclaimers, and a private right of civil action against vendors who improperly access, disclose, sell, share, or use captured plate data. Passed the Senate February 20, 2026 and the House March 5, 2026; emergency clause; signed by Governor Tina Kotek March 31, 2026 (per [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]]).

## Key Points

### Structure (three parts)
- **PRETRIAL RELEASE (§§1–2):** Amends ORS 135.230 and 135.233; standing pretrial release orders; presumption of release; "primary release criteria" defined. Tangential to the wiki's surveillance thread.
- **AUTOMATED LICENSE PLATE RECOGNITION SYSTEMS (§§3–9, §§10–11):** The wiki-relevant core; new statutory framework regulating ALPR use, data sharing, retention, vendor contracts, and creating a private right of action. *Effective on passage* under the emergency clause.
- **JUSTICE REINVESTMENT EQUITY PROGRAM (§12):** Amends section 15, chapter 78, Oregon Laws 2022; restructures grant administration to the Oregon Criminal Justice Commission via a culturally responsive technical assistance provider. Tangential to the wiki's surveillance thread.

### ALPR core provisions (§§3–9, §§10–11)

**§3 — Definitions.** "Automated license plate recognition system" defined as "one or more high-speed cameras combined with computer algorithms used to convert images of license plates or other vehicle characteristics into computer-readable data." Excludes photo red light and photo radar cameras. "Captured license plate data" includes GPS coordinates, date/time, video, photograph, license plate number, vehicle characteristics. "Hot list" defined.

**§4 — Authorized uses.** ALPR systems may be used ONLY for narrowly enumerated law-enforcement purposes: identifying vehicles used to facilitate crimes (Oregon crimes; out-of-state crimes substantially equivalent to Oregon crimes; federal crimes not contrary to ORS 24.500 or state restrictions on prohibited enforcement activities including ORS 181A.250, 181A.820, 181A.826); vehicles with outstanding criminal warrants; missing/endangered persons (AMBER/Silver Alert); uninsured vehicles; unregistered vehicles; parking facility regulation; controlling access to secured areas. **Retention cap (§4(3)(a)): 30 days** for captured plate data not related to a court proceeding or ongoing criminal investigation. Data may be compared only against ODOT records, NCIC, LEDS, FBI kidnapping/missing-persons records, missing children/adults clearinghouse (ORS 181A.300), or hot lists. Search-entry log required (authorized-user ID, agency, search inputs, date/time, case/reference number, law-enforcement purpose, crime/violation type if investigative). Pre-traffic-stop visual confirmation requirement (§4(6)).

**§5 — Data-sharing limitations.** A law enforcement agency may NOT provide access to captured license plate data to any government entity or agency not created pursuant to the Oregon Constitution, or the laws or regulations of this state, *except* for a law enforcement purpose under §§3–9; in those exceptions, the data must be limited to what's relevant to the law enforcement purpose, and **may not include unrestricted or ongoing access**. Search-entry log for cross-agency sharing must include the requesting agency, the government entity on whose behalf the search is conducted, and the number of cameras/devices accessed. Judicial subpoena exception preserved.

**§6 — Vendor-provided audits.** A vendor that contracts with an Oregon LE agency for an ALPR system shall provide:
- **Monthly searchable audit** for the preceding 30-day period (§6(1)) — installed systems, locations, search counts, agency-access list, authorized-user counts, unique vehicles captured, alerts generated, cameras/devices accessed, per-search authorized-user ID, date/time, law-enforcement purpose
- **Quarterly searchable audit** (§6(2)) of all searches conducted on the LE agency's system on behalf of any government agency that is NOT the LE agency — per-search authorized-user ID, employing agency, government entity on whose behalf, date/time, purpose, cameras/devices accessed
- **Public posting within two days** of receiving the audit (§6(3)), in compliance with the new public-records exemption framework added by §11 (ORS 192.345(44))

**§7 — Agency policies and procedures.** Before deployment, a LE agency must establish and publish policies/procedures including security, hot-list information accuracy, training, retention, **mandatory contract terms with any third-party vendor**:
- **§7(2)(e)(A)** — Captured license plate data is the property of the law enforcement agency, **is not owned by the vendor and may not be used by or licensed to the vendor for any purpose** inconsistent with the agency's policies or §§3–9
- **§7(2)(e)(B)** — Any request received by the vendor for access to captured license plate data, including through judicial warrant, judicial subpoena, or administrative subpoena, **must be directed exclusively to the law enforcement agency that owns the captured license plate data**
- **§7(2)(e)(C)** — Captured license plate data **must be encrypted using, at a minimum, end-to-end encryption**
- **§7(2)(e)(D)** — Vendor must comply with the most current version of the FBI Criminal Justice Information Services Security Policy, including the CJIS Security Addendum, audit rights, and prompt notification of security incidents
- **§7(2)(e)(E)** — **The vendor may be held liable for the vendor's misuse or improper release** of captured license plate data, including damages for misuse or improper release

**§8 — Exception for existing contracts.** Existing ALPR contracts in force before the effective date may continue under their original terms for the duration of the contract; agencies may not extend, renew, or enter into new contracts unless the new instrument complies with §§3–9. §4 (authorized-uses) applies to existing contracts regardless of contract date.

**§9 — Action for improper access or disclosure of captured license plate data.** **A vendor may not access, disclose, sell, share or otherwise use captured license plate data** collected by an ALPR system, except for limited technical-support purposes (with express agency consent for the duration of support) or to provide the §6 audit information. **§9(2): If a vendor intentionally or with gross negligence accesses, discloses, sells, shares or otherwise uses captured plate data related to an individual in violation of §9(1)(a), the individual may bring a civil action against the vendor for economic and noneconomic damages and equitable relief**, with attorney fees available. §9(3): Any person may bring a civil action to enjoin a §9(1)(a) violation. §9(4): The §9 causes of action are the **exclusive remedies** in law or equity for §9(1)(a) violations.

**§10 — ORS 137.865 amended.** Organized Retail Theft Grant Program — ALPR equipment purchased under this grant must comply with §§3–9.

**§11 — ORS 192.345 amended.** Adds subsection (44) to the public records conditional-disclosure list:
- (44)(a) Captured license plate data collected by ALPR systems used by LE agencies is conditionally exempt from disclosure, except that audits described in §6 shall be disclosed (with personally identifiable information including license plate numbers or vehicle characteristics edited out)
- (44)(b) Requests for disclosure must identify approximate date/time of collection and be reasonably tailored; video/image must be edited to render faces unidentifiable
- (44)(c) Court-sealed data may not be disclosed unless contained in a §6 audit
- (c) Nothing in this subsection limits any right constitutionally guaranteed, or granted by statute, to disclosure or discovery in criminal cases

### Procedural and other
- **Sponsor**: Senate Interim Committee on Judiciary (at request of)
- **Passed Senate**: February 20, 2026 — Rob Wagner, President of Senate; Obadiah Rutledge, Secretary of Senate
- **Passed House**: March 5, 2026 — Julie Fahey, Speaker of House
- **Emergency clause (§14)**: "This 2026 Act being necessary for the immediate preservation of the public peace, health and safety, an emergency is declared to exist, and this 2026 Act takes effect on its passage."
- **Governor signature**: March 31, 2026 per [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]] (PDF as filed has blank governor signature fields, indicating the PDF is the as-enrolled version)
- **Filed**: with Secretary of State Tobias Read (signature line blank on enrolled PDF)

## Newsletter Angles
- **This is the first state-level statutory regime that names vendor liability as the structural fix, not the user-side opt-out.** Every prior remedy in the wiki's Flock coverage operated on the access-restriction layer — cities cancelling contracts, agencies turning off National Lookup, sanctuary policies governing officer behavior. SB 1516 instead writes **vendor-side prohibitions and vendor-side civil liability** into statute: §9 creates a private right of action against any vendor that "accesses, discloses, sells, shares or otherwise uses" captured plate data, with the §9 causes of action being the exclusive remedies for that prohibition. The remedy follows the vendor, not the contracting agency. This is the legislative structural answer to the [[National Lookup]] silent-reactivation problem that the [[CBS LA — Ventura County Flock 364k Unauthorized Access 2026]] case documented.
- **The mandatory-contract-terms framework (§7(2)(e)) is unusually pointed.** End-to-end encryption (§7(2)(e)(C)); vendor cannot own, license, or use captured data (§7(2)(e)(A)); all data requests must be routed to the LE agency, not the vendor (§7(2)(e)(B)); CJIS compliance with audit rights and security-incident notification (§7(2)(e)(D)); explicit vendor liability for misuse (§7(2)(e)(E)). The wiki holds no prior state law with this combination of provisions. Worth treating as a template that other states may copy.
- **The "third-party search audit" (§6(2)) is the structural reply to Ventura.** Quarterly audit of all searches conducted on behalf of any government agency that is NOT the contracting LE agency — exactly the federal-pull pattern documented at Ventura (out-of-state and federal agency queries running against Ventura's cameras while the department had its own access turned off). The bill makes this auditable by statute, with public posting within two days.
- **The data-sharing prohibition (§5) cleanly forbids federal pull.** No access to government entities not created under Oregon's Constitution or state law, **except** for law-enforcement purposes that meet specific limitations including "may not include unrestricted or ongoing access." This is the legislative equivalent of the National Lookup default-off — but it survives silent reactivation because the prohibition runs on the *data-sharing* layer, not the *feature-toggle* layer.
- **The §11 public-records carveout matters operationally.** Captured plate data is conditionally exempt from disclosure (so the surveillance database isn't searchable by anyone with an open-records request), but the §6 vendor audits MUST be disclosed (with PII redacted). The bill thus creates the accountability tool — public, regular vendor audits — while keeping the plate data itself out of public reach. This is the architectural distinction that [[The Bill of Rights Ends at the Contractor's Door]] argues the open-records request alone cannot accomplish: SB 1516 codifies the audit-as-the-only-working-accountability-tool finding directly into state law.
- **Existing-contract grandfather (§8) limits near-term effect.** Existing contracts may continue under their original terms; only extensions, renewals, and new contracts must comply with §§3–9. But §4 (authorized uses) applies regardless of contract date. The legislative bet is that contract terms expire on a rolling basis, so the law's compliance footprint grows over time without forcing immediate breach-and-renegotiate.
- **The bill is an omnibus.** The ALPR sections are §§3–11; pretrial release is §§1–2; Justice Reinvestment Equity Program is §12. Newsletter framing as "Oregon's Flock-restriction bill" is partial — accurate as to the wiki-relevant sections but not the whole bill. Worth flagging when citing.

## Entities Mentioned
- [[Oregon SB 1516]] — this bill, as the legislative entity
- [[Tina Kotek]] — Governor of Oregon; signed the bill March 31, 2026 per secondary sources
- Rob Wagner — Oregon Senate President; signed enrolled bill
- Julie Fahey — Oregon Speaker of the House; signed enrolled bill
- Obadiah Rutledge — Secretary of the Oregon Senate; signed enrolled bill
- Tobias Read — Oregon Secretary of State; signature line on enrolled PDF
- Senate Interim Committee on Judiciary — sponsor
- [[Flock Safety]] — the dominant ALPR vendor; the law's structural target even though never named
- [[FBI]] — referenced via CJIS Security Policy compliance requirement (§7(2)(e)(D))
- [[Oregon Department of Transportation]] — ODOT records named as authorized data-comparison source (§4(4)(a)(A))
- [[Oregon Criminal Justice Commission]] — administers the Justice Reinvestment Equity Program (§12; tangential to wiki thread)

## Concepts Mentioned
- [[Automated License Plate Recognition]] / ALPR — primary subject
- [[National Lookup]] — not named in the bill but the architectural target of §5's data-sharing limitations
- [[Vendor-State Governance]] — the bill's mandatory-contract-terms framework (§7(2)(e)) and §9 private right of action are the cleanest legislative codification of vendor-state governance the wiki has yet sourced
- [[Sanctuary City Policy]] — adjacent; the bill operates on the data-sharing layer rather than the officer-conduct layer
- [[Surveillance Capitalism]] — the §9 prohibition on vendor "use" or "license" of captured data is directly aimed at the secondary-data-market layer
- [[Open Records as Accountability Tool]] — §11 codifies the accountability-via-audit structure (audits public, data confidential)
- Justice Reinvestment Equity Program — §12 amends; tangential to wiki thread; flagged for potential separate page if a second source surfaces

## Quotes (statutory text, not editorial quotes)
> "Captured license plate data collected by the automated license plate recognition system is the property of the law enforcement agency, is not owned by the vendor and may not be used by or licensed to the vendor for any purpose inconsistent with the policies and procedures of the law enforcement agency or the provisions of sections 3 to 9 of this 2026 Act." — §7(2)(e)(A)

> "Any request received by the vendor for access to captured license plate data collected by the automated license plate recognition system, including through a judicial warrant, judicial subpoena or administrative subpoena, must be directed exclusively to the law enforcement agency that owns the captured license plate data." — §7(2)(e)(B)

> "Captured license plate data must be encrypted using, at a minimum, end-to-end encryption." — §7(2)(e)(C)

> "The vendor may be held liable for the vendor's misuse or improper release of captured license plate data collected by the automated license plate recognition system, including damages for the misuse or improper release." — §7(2)(e)(E)

> "A vendor that contracts with a law enforcement agency to provide an automated license plate recognition system or related services may not access, disclose, sell, share or otherwise use captured license plate data collected by the automated license plate recognition system." — §9(1)(a)

> "If a vendor intentionally or with gross negligence accesses, discloses, sells, shares or otherwise uses captured license plate data related to an individual in violation of subsection (1)(a) of this section, the individual may bring a civil action against the vendor for economic and noneconomic damages and equitable relief. If a court awards damages or equitable relief to the individual, the court may award reasonable attorney fees to the individual." — §9(2)

> "The causes of action provided in this section are the exclusive remedies in law or equity for violation of subsection (1)(a) of this section." — §9(4)

> "This 2026 Act being necessary for the immediate preservation of the public peace, health and safety, an emergency is declared to exist, and this 2026 Act takes effect on its passage." — §14 (Emergency Clause)

## Notes
**Primary source**: enrolled bill text as filed with Oregon Secretary of State, 16 pages. PDF was provided by user 2026-05-24; supersedes the secondary-source description of SB 1516 in [[Bend Source — Bend PD Flock 279 Federal Queries June 2025]], which characterized the bill as "restricts ALPR data sharing to Oregon agencies only and requires public audit reports every 30 days" — that description is accurate as far as it goes but understates the bill's substantive scope (the vendor-liability sections §7(2)(e) and §9 are the structurally novel contribution).

**Procedural posture**: Enrolled bill (passed both chambers, awaiting governor signature when PDF was generated). Bend Source secondary reporting says Kotek signed March 31, 2026. Wiki should treat March 31, 2026 as the operational effective date pending direct confirmation of signature from a primary source (governor's office, OLIS).

**Wiki implication**: This source converts the SB 1516 wikilink references throughout the surveillance cluster from secondary-source citations to a primary-text anchor. The article [[The Bill of Rights Ends at the Contractor's Door]] cites SB 1516 as a state-level structural fix; with the primary text in the wiki, the article's citation now resolves to a directly-readable statutory framework.

**Naming conventions in the bill**: The bill consistently refers to "captured license plate data" rather than "ALPR data" or "Flock data." Wiki pages should preserve the bill's terminology when citing §§ specifically.

**Cross-references to other Oregon statutes** (ORS sections amended or referenced by this bill): 135.230, 135.233, 137.865 (Organized Retail Theft), 192.345 (public records), 24.500 (state policies on prohibited enforcement activities), 181A.250 / 181A.820 / 181A.826 (state restrictions on use of public resources for prohibited enforcement), 181A.300 (missing children clearinghouse), 181A.775 (LE agency definition), section 15 chapter 78 of Oregon Laws 2022 (Justice Reinvestment Equity Program). The 181A.250/820/826 references are particularly notable — they're Oregon's existing statutory framework restricting use of public resources for federal immigration enforcement, and §4(2)(a)(C) explicitly incorporates them by reference into the ALPR-use authorization framework. This is the textual hook that makes SB 1516 a *sanctuary* statute applied to ALPR data, not just a generic data-protection statute.
