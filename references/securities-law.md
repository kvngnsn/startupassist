# Securities Law for Startup Financings

Expert reference for Claude when advising on, structuring, or papering issuances of securities by a privately held Delaware C-corporation: founder stock, equity compensation, SAFEs, convertible notes, and priced preferred rounds. It covers the federal registration exemptions, the accredited investor definition, general solicitation, integration, Form D, state ("blue sky") notice filings, resale limits, finders, bad actors, anti-fraud exposure, and foreign-investor regimes (Regulation S, CFIUS, and the Outbound Investment Security Program).

**Last verified:** November 2, 2026. Primary sources were checked on eCFR, sec.gov, delcode.delaware.gov, and state regulator sites where noted. Items that could not be confirmed carry a `> **Verify:**` note.

---

## 1. Every startup equity issuance is a securities transaction

Section 5 of the Securities Act of 1933 (15 U.S.C. § 77e) prohibits offers and sales of securities unless a registration statement is in effect or an exemption applies. A private company therefore needs an exemption for **every** issuance, including founder stock, and must also satisfy the securities law of each state where an offeree or purchaser resides, unless federal law preempts it.

| Instrument | Security? | Usual federal exemption | Usual state treatment | Notes |
|---|---|---|---|---|
| Founder common stock (cash or IP) | Yes; stock is a security (*Landreth Timber Co. v. Landreth*, 471 U.S. 681 (1985)) | § 4(a)(2) (founders are insiders); Rule 701 if issued for services | California § 25102(f) for California founders (or § 25102(h) in limited cases); other states' isolated-transaction or limited-offering exemptions | No general solicitation issue; file a § 25102(f) notice in California if relied on |
| Options, RSUs, restricted stock to employees, directors, consultants | Yes (grant of an option is a "sale" for Rule 701 purposes) | Rule 701 (17 C.F.R. § 230.701) | California § 25102(o) with a notice filed after initial issuance; most states have a comparable compensatory-plan exemption | See the equity-compensation templates |
| SAFE | Yes; the SEC treats SAFEs as securities (SEC Office of Investor Education and Advocacy, *Investor Bulletin: Be Cautious of SAFEs in Crowdfunding* (May 2017)) | Rule 506(b) (most common) or 506(c); § 4(a)(2) alone is possible but loses state preemption | Covered security if sold under Rule 506; state notice filings | The underlying preferred stock is a security offered at the same time; Form D lists both |
| Convertible promissory note | Yes under the "family resemblance" test (*Reves v. Ernst & Young*, 494 U.S. 56 (1990)); notes sold to raise capital for investment are securities | Rule 506(b) or 506(c) | Same as SAFEs | Usury and lending law also apply |
| Preferred stock in a priced round | Yes | Rule 506(b) or 506(c) | Same | New offering; separate Form D unless continuing |
| Conversion of a SAFE, note, or preferred into stock | Exchange of one security for another of the same issuer | § 3(a)(9) (exchange with existing holders, no commission paid for soliciting the exchange) | Most states exempt § 3(a)(9)-type exchanges | Holding period tacks under Rule 144(d)(3)(ii) |
| Warrants issued with venture debt | Yes | § 4(a)(2) or Rule 506(b) | Lender is typically institutional | |

---

## 2. Section 4(a)(2): the statutory private placement

Section 4(a)(2) (15 U.S.C. § 77d(a)(2)) exempts "transactions by an issuer not involving any public offering." The Supreme Court asks whether the offerees need the protection of registration, i.e., whether they can "fend for themselves" and have access to registration-type information (*SEC v. Ralston Purina Co.*, 346 U.S. 119 (1953)). Courts weigh the number and sophistication of offerees, their access to information, the size and manner of the offering, and the steps taken to prevent redistribution (e.g., *Doran v. Petroleum Management Corp.*, 545 F.2d 893 (5th Cir. 1977)).

**Why companies prefer Rule 506 over bare § 4(a)(2):**

- **No bright lines.** Section 4(a)(2) turns on facts; Rule 506 is a safe harbor.
- **No state preemption.** Securities sold under SEC rules issued under § 4(a)(2), i.e., Rule 506, are "covered securities" (Securities Act § 18(b)(4)(F), 15 U.S.C. § 77r(b)(4)(F)), so states may require only notice filings and fees. A bare § 4(a)(2) offering is **not** a covered security; the company must find a state exemption in every state where it sells (e.g., California § 25102(f)).
- **General solicitation** destroys § 4(a)(2) and Rule 506(b); only Rule 506(c) (and Regulation CF / Regulation A) permits it.

**When bare § 4(a)(2) is still used:** founder stock at formation; a single sale to one sophisticated investor; issuances where a Form D filing is commercially undesirable. Pair it with the relevant state exemption and a California § 25102(f) notice when a California resident is involved.

---

## 3. Regulation D

Regulation D (17 C.F.R. §§ 230.500–230.508) contains the definitions (Rule 501), general conditions (Rule 502), the Form D notice requirement (Rule 503), two operative exemptions used by startups (Rules 504 and 506), the bad-actor rules (Rule 506(d)–(e)), the disqualification for Form D injunctions (Rule 507), and the insignificant-deviation defense (Rule 508).

### 3.1 Rule 506(b): the default for SAFE, note, and priced rounds

| Condition | Rule | Detail |
|---|---|---|
| Amount | Rule 506 | No limit |
| Accredited purchasers | Rule 506(b) | Unlimited |
| Non-accredited purchasers | Rule 506(b)(2)(i) | No more than 35 in any 90-calendar-day period (counting rules in Rule 501(e); accredited investors and certain relatives and controlled entities are excluded from the count) |
| Sophistication | Rule 506(b)(2)(ii) | Each non-accredited purchaser, alone or with a purchaser representative (Rule 501(i)), must have such knowledge and experience in financial and business matters that it can evaluate the merits and risks, or the issuer must reasonably believe so immediately before the sale |
| Information | Rule 502(b) | If **any** non-accredited purchaser buys, the issuer must furnish disclosure a reasonable time before sale (Section 5 below). No mandated disclosure if all purchasers are accredited, but anti-fraud rules still apply |
| Manner of offering | Rule 502(c) | **No general solicitation or general advertising** by the issuer or anyone acting on its behalf |
| Resale limits | Rule 502(d) | Securities are "restricted"; the issuer must take reasonable care that purchasers are not underwriters (inquiry into investment intent, written disclosure of resale limits, legends) |
| Integration | Rules 502(a), 152 | See Section 7 |
| Bad actors | Rule 506(d)–(e) | No disqualifying events for covered persons; disclose pre-September 23, 2013 events |
| Form D | Rule 503 | Within 15 calendar days after the first sale (not a condition of the exemption; see Section 8) |

**Reasonable belief.** The accredited investor definition covers anyone who meets a category **or whom the issuer reasonably believes** meets one at the time of sale (Rule 501(a)). In Rule 506(b) offerings issuers typically rely on a written questionnaire (see the skill's investor questionnaire); verification is not required, but red flags must be followed up.

### 3.2 Rule 506(c): general solicitation permitted

| Condition | Rule | Detail |
|---|---|---|
| General solicitation | Rule 506(c) | Permitted (Rule 502(c) does not apply) |
| Purchasers | Rule 506(c)(2)(i) | **All** purchasers must be accredited investors (reasonable belief still protects against a purchaser who fooled the issuer despite verification) |
| Verification | Rule 506(c)(2)(ii) | The issuer must take **reasonable steps to verify** accredited status; an objective, facts-and-circumstances determination |
| Other conditions | Rule 506(c)(1) | Rules 501, 502(a) and 502(d) apply; bad-actor rules apply; Form D required |

**Non-exclusive verification methods for natural persons (Rule 506(c)(2)(ii)(A)–(E)):**

1. **Income:** review IRS forms reporting income for the two most recent years (Forms W-2, 1099, Schedule K-1 to Form 1065, Form 1040) plus a written representation of a reasonable expectation of reaching the threshold in the current year. For joint income, review both spouses' forms and obtain both representations.
2. **Net worth:** review documentation dated within the prior three months (assets: bank and brokerage statements, certificates of deposit, tax assessments, independent appraisals; liabilities: a consumer report from at least one nationwide consumer reporting agency) plus a written representation that all liabilities have been disclosed.
3. **Third-party confirmation:** a written confirmation from a registered broker-dealer, an SEC-registered investment adviser, a licensed attorney in good standing, or a registered CPA in good standing that it has taken reasonable steps to verify accredited status within the prior three months and determined that the purchaser is accredited.
4. **Legacy 506(b) investors:** for a person who bought in the issuer's Rule 506(b) offering as an accredited investor before September 23, 2013 and still holds those securities, a certification at the time of sale.
5. **Previously verified purchasers:** a written representation at the time of sale from a person the issuer verified within the prior **five years**, absent contrary information.

**Minimum-investment verification (staff no-action letter, March 12, 2025).** In a letter to Latham & Watkins LLP dated March 12, 2025 (responding to a March 6, 2025 request), the staff of the Division of Corporation Finance agreed that a high minimum investment amount is a relevant verification factor and that an issuer could reasonably conclude it has taken reasonable steps to verify where:

| Purchaser | Minimum investment (binding commitment, including capital calls) | Written representations | Issuer knowledge |
|---|---|---|---|
| Natural person (accredited under Rule 501(a)(5) or (a)(6)) | At least **$200,000** | (i) is an accredited investor; (ii) the minimum investment is not financed in whole or in part by a third party for the specific purpose of making the investment | No actual knowledge of facts indicating the purchaser is not accredited or that the minimum is third-party financed for that purpose |
| Entity accredited by total assets or investments (Rule 501(a)(3), (7), (9) or (12)) | At least **$1,000,000** | Same | Same |
| Entity accredited only because all equity owners are accredited (Rule 501(a)(8)) | At least **$1,000,000**, or **$200,000 per equity owner** if the owners are fewer than five natural persons | Same, plus that each equity owner has a minimum commitment to the entity of $200,000 (natural persons) or $1,000,000 (entities) not third-party financed for that purpose | Same, including as to each owner's commitment |

The staff simultaneously issued Securities Act Rules Compliance and Disclosure Interpretations 256.35 (the listed methods are non-exclusive and non-mandatory; verification is principles-based) and 256.36 (minimum investment amounts may be considered). The letter is staff guidance with no legal force and turns on its stated facts. Startups rarely raise SAFE checks of $200,000 or more from every individual; the method is most useful for fund investors and larger angels. Issuers below the thresholds use the traditional methods.

> **Verify:** Before relying on the minimum-investment approach, check the SEC's Securities Act Rules C&DIs (Section 256) and no-action letter index for any later staff statement or Commission rulemaking modifying it.

**When to use 506(c):** the founders will speak publicly about the raise (demo days outside Rule 148, social media, a public website "raise" page, podcasts, or platform listings), or general solicitation has already occurred and 506(b) is no longer available (Section 7). Never "flip" to 506(b) after a general solicitation without the Rule 152(a)(1) analysis.

### 3.3 Rule 504: up to $10,000,000

Rule 504 exempts offerings by non-reporting, non-investment-company issuers that are not blank-check companies, up to **$10,000,000 in any 12 months** (less amounts sold under Rule 504 or in violation of § 5 during the 12 months before and during the offering) (Rule 504(b)(2)). General solicitation is permitted only under specified state registration or state-exemption conditions (Rule 504(b)(1)). Bad-actor disqualification applies (Rule 504(b)(3)). Rule 504 securities are **not** covered securities, so state registration or exemption is required. Venture-backed startups rarely use it.

### 3.4 Rule 508: insignificant deviations

A failure to comply with a Regulation D condition does not lose the exemption as to a particular purchaser if the failure did not pertain to a requirement directly intended to protect that purchaser, was insignificant to the offering as a whole, and the issuer made a good-faith and reasonable attempt to comply. Failures of the general solicitation prohibition, the offering-amount limits, and the purchaser-number limits are deemed significant. The SEC can still bring an enforcement action.

---

## 4. The accredited investor definition (17 C.F.R. § 230.501(a), current text)

The definition was last substantively amended in 2020 (Release No. 33-10824, effective December 8, 2020); a February 2025 amendment corrected cross-references only. Status is measured **at the time of sale**. Dollar thresholds are **not** indexed for inflation.

| Rule 501(a) | Category | Key conditions |
|---|---|---|
| (1) | Institutions | Banks; savings and loan associations; registered broker-dealers; SEC- or state-registered investment advisers; **exempt reporting advisers** (§ 203(l) or (m) of the Advisers Act); insurance companies; registered investment companies and BDCs; licensed SBICs; **Rural Business Investment Companies**; state and political-subdivision plans with total assets over $5,000,000; ERISA plans if a bank, insurance company, or registered adviser fiduciary makes the decision, or total assets over $5,000,000, or a self-directed plan whose decisions are made solely by accredited investors |
| (2) | Private business development companies | As defined in § 202(a)(22) of the Advisers Act |
| (3) | Certain entities with assets over $5,000,000 | § 501(c)(3) organizations, corporations, Massachusetts or similar business trusts, partnerships, or **LLCs**, not formed for the specific purpose of acquiring the securities offered |
| (4) | Insiders of the issuer | Any director, executive officer, or general partner of the issuer (or of its general partner) |
| (5) | Net worth | Natural person whose individual net worth, or joint net worth with a **spouse or spousal equivalent**, exceeds **$1,000,000**, excluding the primary residence as an asset; mortgage debt on the residence is excluded up to its fair market value, except that any increase in that debt in the 60 days before the sale (other than to acquire the residence) counts as a liability; debt above fair market value counts as a liability. Joint net worth can aggregate both persons' assets, which need not be jointly held, and the securities need not be bought jointly |
| (6) | Income | Natural person with individual income over **$200,000** in each of the two most recent years, or joint income with a spouse or spousal equivalent over **$300,000** in each of those years, and a reasonable expectation of the same level in the current year |
| (7) | Trusts | Total assets over $5,000,000, not formed for the specific purpose, and the purchase is directed by a sophisticated person (Rule 506(b)(2)(ii)) |
| (8) | Entities owned by accredited investors | Every equity owner is an accredited investor (look-through to natural persons is permitted) |
| (9) | Other entities owning investments over $5,000,000 | Any entity type not listed in (1), (2), (3), (7) or (8) (e.g., Indian tribes, governmental bodies, funds), not formed for the specific purpose, owning **investments** (as defined in Investment Company Act Rule 2a51-1(b)) over $5,000,000 |
| (10) | Professional certifications | Natural persons holding in good standing a certification, designation, or credential designated by SEC order. **Currently designated: the Series 7 (General Securities Representative), Series 65 (Investment Adviser Representative), and Series 82 (Private Securities Offerings Representative) licenses** (order issued with the 2020 amendments) |
| (11) | Knowledgeable employees | Natural persons who are "knowledgeable employees" (Investment Company Act Rule 3c-5(a)(4)) of the issuer, where the issuer would be an investment company but for § 3(c)(1) or § 3(c)(7). **Relevant only to private funds**, not operating startups |
| (12) | Family offices | A family office (Advisers Act Rule 202(a)(11)(G)-1) with assets under management over $5,000,000, not formed for the specific purpose, whose investment is directed by a person with sufficient knowledge and experience |
| (13) | Family clients | A family client of a qualifying family office whose investment is directed by that family office |

**Spousal equivalent** (Rule 501(j)): a cohabitant occupying a relationship generally equivalent to that of a spouse.

**Pending proposals.** On September 30, 2026 the SEC issued five notices (Release Nos. 33-11445 through 33-11449; published in the Federal Register on October 5, 2026; comments due December 4, 2026) considering whether to designate additional Rule 501(a)(10) credentials: a FINRA-developed accredited investor examination, the U.S. CPA license, the CFA charter, the CFP certification, and the Series 79 and Series 86/87 licenses. None is effective until the Commission issues an order.

> **Verify:** Before relying on Rule 501(a)(10), check the SEC's list of designated professional credentials for any order issued after November 2, 2026 under these notices.

---

## 5. Non-accredited investors: the disclosure burden

If any non-accredited investor buys in a Rule 506(b) offering, Rule 502(b) requires the issuer to furnish, a reasonable time before the sale and to the extent material:

- **Non-financial information** of the kind required in Part II of Form 1-A (Regulation A), if the issuer is eligible for Regulation A; otherwise the information required in Part I of an available registration statement form.
- **Financial statements** under Part F/S of Form 1-A: paragraph (b) for offerings up to $20,000,000 and paragraph (c) for offerings over $20,000,000 (Rule 502(b)(2)(i)(B)).
- A written description of material written information given to accredited investors, the opportunity to ask questions and obtain additional information, a description of resale limits, and any Rule 241 solicitation materials used within 30 days before the sale (Rule 502(b)(2)(iv), (v), (vii), (viii)).

> **Verify:** Confirm the current audit requirements of Form 1-A Part F/S paragraphs (b) and (c) before advising on the financial statements a non-accredited purchaser must receive.

Each non-accredited purchaser must also be sophisticated (alone or with a purchaser representative). **Practice:** startups almost always limit SAFE and note rounds to accredited investors; the YC SAFE contains an accredited-investor representation and lets the company void the SAFE and return the money if the holder is not accredited at the Equity Financing. If a non-accredited friend or employee must participate, consider Rule 701 (for service providers), Regulation CF, or a carefully prepared Rule 506(b) disclosure package with counsel.

The SEC's note to Rule 502(b)(1) reminds issuers to consider giving accredited investors the same information, because of the anti-fraud provisions (Section 15).

---

## 6. General solicitation

### 6.1 What it is

Rule 502(c) bars "any form of general solicitation or general advertising," including advertisements, articles, notices, or other communications in newspapers, magazines, or similar media, broadcasts, and seminars or meetings whose attendees were invited by general solicitation. The SEC treats an unrestricted website, public social media posts, and press interviews that discuss a current or planned offering as general solicitation. A communication is not general solicitation if made only to persons with whom the issuer (or its agent) has a **pre-existing, substantive relationship**, i.e., one that lets the issuer evaluate the person's sophistication and financial circumstances before the offering (see the general-solicitation interpretations in Section 256 of the SEC's Securities Act Rules C&DIs and the staff's *Citizen VC, Inc.* no-action letter (Aug. 6, 2015)).

Posting a Form D or a Rule 135c notice is not general solicitation (Rule 502(c) proviso).

### 6.2 Rule 148: demo days

A communication made at a seminar or meeting with **more than one issuer** participating, sponsored by a college or university, a state or local government, a nonprofit, an angel investor group, an incubator, or an accelerator, is not general solicitation if (17 C.F.R. § 230.148):

1. no advertising for the event references a specific offering by the issuer;
2. the sponsor does not make investment recommendations, negotiate between issuers and investors, charge attendees more than reasonable administrative fees, receive compensation for introductions or negotiations, or receive compensation that would require broker-dealer or investment adviser registration;
3. information about the offering is limited to: that the issuer is offering or planning to offer securities, the type and amount, the intended use of proceeds, and the unsubscribed amount; and
4. virtual attendance is limited to the sponsor's members or associates, persons the sponsor reasonably believes are accredited, or persons invited based on industry or investment experience reasonably selected in good faith and disclosed in the event's public communications.

An "angel investor group" is a group of accredited investors that holds regular meetings, has defined decision-making processes, and is not associated or affiliated with brokers, dealers, or investment advisers. **Pitch decks shown at a Rule 148 event should not state terms beyond the four permitted items** (no valuation cap, no price) or the communication may fall outside the rule.

### 6.3 Rule 241: generic solicitation of interest

Rule 241 lets an issuer test the waters before deciding which exemption to use, subject to legends and other conditions; the offering is treated as commenced on the generic solicitation (Rule 152(c)(1)), and the solicitation is general solicitation. A later Rule 506(b) offering then needs the Rule 152(a)(1) analysis for each purchaser.

---

## 7. Integration (Rule 152, effective March 2021)

Rule 152 governs whether separate offerings are treated as one (Rule 502(a) cross-references it).

- **General principle (Rule 152(a)):** offerings are not integrated if the issuer can establish that each offering either complies with registration or has its own exemption. For an exempt offering that **prohibits** general solicitation (e.g., Rule 506(b)), the issuer must reasonably believe, for each purchaser, that it did not solicit that purchaser through general solicitation **or** established a substantive relationship with the purchaser before the offering commenced. For concurrent offerings that **permit** general solicitation, offering materials for one that include the material terms of another may be an offer in the other, which must then satisfy that exemption's conditions (including legends).
- **Safe harbors (Rule 152(b)):**
  1. Offerings more than **30 calendar days** apart are not integrated (with the Rule 152(a)(1) condition when a no-general-solicitation offering follows a general-solicitation offering).
  2. Rule 701 and employee benefit plan offers and sales, and Regulation S offers and sales, are not integrated with other offerings.
  3. Registered offerings after certain terminated or completed private offerings are not integrated.
  4. Offers and sales under an exemption permitting general solicitation are not integrated with any **terminated or completed** earlier offering.
- **Commencement and termination (Rule 152(c)–(d)):** a § 4(a)(2) or Regulation D offering commences on the first offer; it terminates on the later of a binding commitment to sell all securities (subject only to conditions outside the investor's control) or cessation of offering efforts.

**Application to startup rounds.** A rolling SAFE round, a later bridge on different terms, and the priced round are usually separate offerings with separate exemptions; each must stand on its own. A SAFE round that remains open for months is one continuing offering for Form D purposes (Section 8.3). Equity grants under Rule 701 do not integrate with a concurrent SAFE round.

---

## 8. Form D

### 8.1 Deadline and mechanics (Rule 503)

- File **no later than 15 calendar days after the first sale** in the offering; if the 15th day falls on a Saturday, Sunday, or holiday, the deadline is the next business day (Rule 503(a)(1)). The SEC's Form D guide treats the **date of first sale** as the date on which the first investor is **irrevocably contractually committed** to invest, which depends on the subscription documents (for a SAFE, typically the later of the parties' signatures and, where the instrument says it is not binding until funded, receipt of funds).
- A Form D may be filed before any sale.
- File electronically on EDGAR (Rule 503(b)(1)); a duly authorized person signs (Rule 503(b)(2)).
- **No SEC filing fee** for Form D or its amendments (SEC, *Filing and Amending a Form D Notice*).

### 8.2 Amendments (Rule 503(a)(3))

The issuer must amend:

1. to correct a **material mistake of fact or error**, as soon as practicable after discovery;
2. to reflect a **change in information**, as soon as practicable, **except** changes after the offering terminates and changes solely in: related persons' addresses or relationships; revenue or net asset value; the minimum investment (increases, or decreases of 10% or less cumulatively); addresses or states of solicitation; the total offering amount (decreases, or increases of 10% or less cumulatively); amounts sold or remaining; the number of non-accredited investors (if not above 35); the total number of investors; or sales commissions, finders' fees, or use of proceeds for insiders (decreases, or increases of 10% or less cumulatively); and
3. **annually**, on or before the first anniversary of the most recent filing, if the offering is continuing.

Every amendment must restate current information in full (Rule 503(a)(4)).

### 8.3 Practice points

- **Consequences of a late or missed filing.** Filing is not a condition of the Rule 506 exemption, and a missed Form D does not cost the offering covered-security status (Securities Act Rules C&DIs 257.07, 257.08), but Rule 507 disqualifies an issuer subject to a court injunction for failing to file, states require their notices on time (and charge late fees), and the SEC can bring enforcement actions. File late rather than not at all.
- **Item 3 (related persons)** publicly lists executive officers, directors, and promoters. **Item 9 (type of securities):** for SAFEs, practice varies (many check "Other" and describe "Simple Agreement for Future Equity," together with "Security to be Acquired Upon Exercise of Option, Warrant or Other Right to Acquire Security" for the underlying preferred); for notes, check "Debt" and the underlying-security box. **Item 12 (sales compensation)** requires every person paid transaction-based compensation to be named (a red flag for unregistered brokers). **Item 16 (use of proceeds)** discloses payments to insiders.
- **Publicity.** Form D is public and is scraped by press and data services. Total offering amount and amount sold become public within days.
- **One Form D per offering.** A SAFE round and a later priced round are separate offerings and need separate Forms D.

### 8.4 EDGAR access (EDGAR Next)

Under the SEC's EDGAR Next amendments (Release No. 33-11313, adopted September 27, 2024): the new Filer Management dashboard went live March 24, 2025 (also the compliance date for amended Form ID); most other requirements took effect **September 15, 2025**; enrollment for legacy filers closed in December 2025. Today:

- A company without EDGAR access applies on **Form ID** through the EDGAR Filer Management website to obtain a CIK.
- Every individual acting for the filer must use **individual Login.gov credentials with multifactor authentication**.
- Each filer must authorize at least **two account administrators** (one if the filer is an individual or single-member company), who manage users and filing-agent delegations and must **confirm annually** that everyone listed on the dashboard is authorized and that the filer's information is accurate.
- Law firms and filing agents act through delegated authority on the dashboard.

> **Verify:** Confirm current Form ID requirements (including the notarized authentication document) and typical SEC processing time on sec.gov's EDGAR Next pages before the first closing. Apply for EDGAR access as soon as the round is approved, because Form ID review can take days or longer and the 15-day clock does not stop.

---

## 9. State securities ("blue sky") law

### 9.1 Preemption and what states may still require

Securities sold under Rule 506 are covered securities (Securities Act § 18(b)(4)(F)), so states cannot require registration or merit review. States may still require **notice filings, consent to service of process, and fees** (§ 18(c)(2)) and may enforce their **anti-fraud** laws (§ 18(c)(1)). Rule 504 offerings and bare § 4(a)(2) offerings are **not** preempted; they need a state exemption or registration.

Most states accept Rule 506 notices (a copy of the Form D) through NASAA's **Electronic Filing Depository (EFD)** (nasaaefd.org), which charges a **$160 system use fee** on each initial Form D notice filing (no further system fee for amendments or renewals of that filing), in addition to state fees. State requirements key off the **state of residence of each purchaser** (for entities, generally the principal place of business), and in some states off offers as well as sales.

### 9.2 Key states

| State | Rule 506 notice | Deadline | Fee | Source |
|---|---|---|---|---|
| California | Notice under Cal. Corp. Code § 25102.1(d) (Form D) via DFPI's online system or EFD; no notarized consent to service if the Form D was filed electronically with the SEC | 15 days after the first sale in California | $300 (Cal. Corp. Code § 25608.1(c)) | DFPI Securities FAQ; DFPI fee index (ADM 510, rev. 10/25) |
| New York | Form D notice via EFD (General Business Law § 359-e; 13 NYCRR Part 10) | Within 15 days after the first sale in or from New York | $300 if the offering is $500,000 or less; $1,200 if over $500,000; amendments with updated information are supplemental filings ($30) | 13 NYCRR § 10.8; NYAG EFD guidance |
| Texas | Form D notice and fee via EFD (7 Tex. Admin. Code § 114.4) | No later than 15 calendar days after the first sale in Texas (next business day if a weekend or holiday) | 1/10 of 1% of the aggregate offering amount, maximum $500; amendments filed with each SEC amendment; excess sales trigger a fee of three times the difference plus interest | Texas State Securities Board, "Filing Requirements for Regulation D Offerings in Texas" |
| Washington | Form D notice via EFD (WAC 460-44A-503) | Within 15 days after the first sale in Washington | $300; no fee for amendments | Washington DFI; WAC 460-44A-503 |

> **Verify:** Confirm New York's current deadline, fees, and supplemental-filing fee against 13 NYCRR Part 10 and the NYAG's EFD guidance, and Washington's current fee against WAC 460-44A-503, before filing. For every other state, check the NASAA EFD fee and requirements matrix for that state on the filing date (some states, including Florida, reportedly require no Rule 506 notice; others charge graduated fees or late fees).

### 9.3 California § 25102(f) (non-Regulation D offerings)

When a California issuance relies on § 4(a)(2) without Regulation D (for example, founder stock or a small SAFE sale where the company does not want a public Form D), California's limited-offering exemption, Cal. Corp. Code § 25102(f), requires:

1. sales to no more than 35 persons (accredited investors and certain others are excluded from the count under 10 Cal. Code Regs. § 260.102.13);
2. each purchaser either has a pre-existing personal or business relationship with the issuer or its officers, directors, or controlling persons, or by reason of business or financial experience (alone or with an unaffiliated professional adviser) could reasonably be assumed to have the capacity to protect its own interests;
3. each purchaser represents that it is buying for its own account and not with a view to distribution; and
4. no advertising.

A **Limited Offering Exemption Notice** is filed online with the DFPI **within 15 calendar days after the first sale in California** (it may be filed earlier). Fees under § 25608(c) are graduated by the value of securities sold: $25 ($25,000 or less), $35 ($25,001–$100,000), $50 ($100,001–$500,000), $150 ($500,001–$1,000,000), and $300 (over $1,000,000). A late notice (§ 25102(f)(4)) costs $200 plus 1/5 of 1% of value, up to $2,500, and is due within 15 business days after discovery of the failure or a DFPI demand. (DFPI Securities FAQ; DFPI fee index ADM 510, rev. 10/25.)

### 9.4 California anti-fraud and finder rules

California's anti-fraud statutes apply even to covered securities: Cal. Corp. Code § 25401 (misstatements and omissions in the offer or sale of a security) with civil liability under § 25501 (rescission or damages; the defendant may defend by proving it did not know and in the exercise of reasonable care could not have known of the untruth or omission) and joint and several control-person liability under § 25504. These provisions reach private placements that federal § 12(a)(2) does not.

---

## 10. Rule 701 (cross-reference)

Rule 701 exempts offers and sales by non-reporting issuers under written compensatory benefit plans or contracts to employees, directors, general partners, officers, and natural-person consultants and advisors who provide bona fide services not connected with capital raising (17 C.F.R. § 230.701).

- **Sales cap in any consecutive 12 months:** the greatest of $1,000,000; 15% of total assets; or 15% of the outstanding class (measured at the most recent balance sheet date, if no older than the last fiscal year end) (Rule 701(d)(2)). Options count at grant, valued at exercise price (Rule 701(d)(3)).
- **Enhanced disclosure** (plan summary, risk factors, financial statements under Form 1-A Part F/S, and a copy of the plan or contract) if sales in a 12-month period exceed **$10,000,000** (Rule 701(e)), delivered a reasonable period before sale (for options, before exercise).
- Rule 701 securities are restricted; Rule 701(g) provides resale relief 90 days after an IPO.
- Rule 701 offerings are not integrated with other offerings (Rule 152(b)(2)).
- **Do not** issue SAFEs or notes as compensation; the tax treatment (§ 83, § 409A) is unfavorable and Rule 701 compliance becomes awkward.

See the equity-compensation templates for California § 25102(o) and plan-level compliance.

---

## 11. Regulation Crowdfunding and Regulation A (brief)

**Regulation Crowdfunding** (Securities Act § 4(a)(6); 17 C.F.R. Part 227): up to **$5,000,000** in 12 months (Rule 100(a)(1)), sold only through a single registered funding portal or broker-dealer, with a Form C disclosure document, financial statements whose level of review depends on offering size, and annual reports. Non-accredited investors are limited across all Reg CF offerings in 12 months to the greater of $2,500 or 5% of the greater of annual income or net worth if either is below $124,000, or 10% of the greater of the two (capped at $124,000) if both are at least $124,000; accredited investors have no limit (Rule 100(a)(2)). SAFEs are sold in Reg CF offerings (often as "Crowd SAFEs"); the SEC has warned retail investors about their risks. Reg CF securities are covered securities; the holders are counted for Exchange Act § 12(g) only if conditions in Rule 12g-6 are not met. A Reg CF round can affect later VC rounds (hundreds of small holders; proxy and information demands); many companies use an SPV/crowdfunding vehicle structure.

**Regulation A** (17 C.F.R. §§ 230.251–230.263): Tier 1 up to **$20,000,000** in 12 months (state registration required) and Tier 2 up to **$75,000,000** (state preemption; audited financials; ongoing reporting) (Rule 251(a)). Requires SEC qualification of a Form 1-A offering statement; rarely used by venture-backed startups.

---

## 12. Resales and transfer restrictions

- Securities acquired under Regulation D or § 4(a)(2) are **restricted securities** (Rule 502(d); Rule 144(a)(3)) and cannot be resold without registration or an exemption.
- **Rule 144 holding periods (Rule 144(d)(1)):** one year from acquisition from the issuer or an affiliate (full payment required) for a non-reporting issuer; six months if the issuer has been reporting for at least 90 days.
- **Tacking on conversion (Rule 144(d)(3)(ii)):** securities acquired from the issuer solely in exchange for other securities of the same issuer (e.g., preferred stock on conversion of a SAFE or note, or common on conversion of preferred) are deemed acquired when the surrendered securities were acquired. If the holder pays additional consideration to amend the instrument to permit a cashless conversion, the holding period restarts (note to Rule 144(d)(3)(ii)).
- **Private resales:** the "§ 4(a)(1½)" doctrine and the statutory § 4(a)(7) exemption (accredited purchasers, no general solicitation, specified information for non-reporting issuers, the class outstanding at least 90 days, and other conditions).
- **Contractual restrictions** layer on top: SAFEs require company consent to transfer (except to affiliates and on death or disability); notes should do the same; bylaws often contain a right of first refusal and lock-up; the priced round's investor agreements add co-sale and drag-along obligations.
- **Legends:** Rule 502(d)(3) legends on the instrument and the stock; state legends where required.

---

## 13. Finders and unregistered broker-dealers

- **Exchange Act § 15(a)** (15 U.S.C. § 78o(a)) requires anyone "engaged in the business of effecting transactions in securities for the account of others" to register as a broker-dealer. The SEC treats **transaction-based compensation** (a percentage of money raised, a success fee, or equity tied to the amount raised) as the hallmark of broker activity, together with soliciting investors, negotiating terms, advising on value, and handling funds.
- **No federal finder exemption exists.** The SEC proposed a limited exemption for natural-person finders in October 2020 (Release No. 34-90112); it has not been adopted. The M&A broker exemption (Exchange Act § 15(b)(13), enacted December 2022) covers sales of privately held companies, not capital raising.
- **Consequences:** contracts made in violation of the Exchange Act are voidable at the option of the innocent party (Exchange Act § 29(b)); investors may seek rescission under state law (e.g., Cal. Corp. Code § 25501.5 for purchases from or through an unlicensed broker-dealer); state and SEC enforcement; the finder is a **covered person** under Rule 506(d), so its bad-actor history can disqualify the offering; Form D Item 12 must name it.
- **California's finder statute (Cal. Corp. Code § 25206.1).** A natural person who, for compensation, only introduces accredited investors to an issuer (or vice versa) in an issuer transaction in California is exempt from broker-dealer licensing if, among other conditions, the transaction (or series) does not exceed **$15,000,000** in aggregate purchase price; the finder does not negotiate terms, advise on value or advisability, conduct due diligence, sell its own securities in the transaction, or take custody of funds; disclosure to investors is limited to the issuer's name and contact information, the name, type, price and aggregate amount of the securities, and the issuer's industry, location, and years in business; and the finder files an initial statement of information with the DFPI before acting (fee $300) and annual renewals (fee $275 per the DFPI fee index).

> **Verify:** Read the remaining conditions of § 25206.1 (written agreement, investor disclosure, recordkeeping, and disqualification provisions) and any other state's finder rules (e.g., Texas, Michigan) before advising a client to pay a finder.

- **Practice:** pay no transaction-based compensation to unregistered persons; if an introducer must be paid, use a registered broker-dealer or (in California) a compliant § 25206.1 finder, and document the arrangement.

---

## 14. Bad-actor disqualification (Rule 506(d)–(e))

**Covered persons (Rule 506(d)(1)):** the issuer and its predecessors and affiliated issuers; directors, executive officers, other officers participating in the offering, general partners, and managing members; **beneficial owners of 20% or more of outstanding voting equity** (by voting power); promoters; investment managers of pooled fund issuers; **any person paid (directly or indirectly) for soliciting purchasers**, and their general partners, managing members, directors, executive officers, and participating officers.

**Disqualifying events (summarized):** criminal convictions within 10 years (5 for the issuer and its predecessors and affiliated issuers) in connection with securities, false SEC filings, or the securities business; court injunctions within 5 years; final orders of state securities, banking, or insurance regulators, federal banking agencies, the CFTC, or the NCUA (bars, or orders based on fraudulent, manipulative, or deceptive conduct within 10 years); SEC disciplinary orders; SEC cease-and-desist orders within 5 years for scienter-based anti-fraud or § 5 violations; SRO suspensions or expulsions; stop orders or Reg A suspensions within 5 years; and U.S. Postal Service false-representation orders within 5 years.

**Reasonable-care exception (Rule 506(d)(2)(iv)):** the exemption is not lost if the issuer shows it did not know and, despite reasonable care, could not have known of a disqualification. Reasonable care means factual inquiry, typically questionnaires to directors, officers, 20% holders, and placement agents, refreshed before each offering.

**Pre-September 23, 2013 events** are not disqualifying but must be disclosed in writing to purchasers a reasonable time before sale (Rule 506(e)). The SEC may waive disqualification for good cause (Rule 506(d)(2)(ii)).

**Startup practice:** the skill's investor questionnaire includes a bad-actor certification for investors who will hold 20% or more of voting equity, and the board consent directs officers to obtain D&O bad-actor questionnaires.

---

## 15. Anti-fraud: why disclosure matters even in exempt offerings

- **Rule 10b-5** (17 C.F.R. § 240.10b-5) and Exchange Act § 10(b) apply to every purchase or sale of a security, registered or exempt, public or private. Private plaintiffs must show a material misstatement or omission, scienter, reliance, loss causation, and damages; the SEC need not show reliance or loss.
- **Securities Act § 17(a)** (15 U.S.C. § 77q(a)) applies to every offer or sale; the SEC can proceed under § 17(a)(2) and (3) on a negligence theory.
- **Securities Act § 12(a)(2)** generally does **not** reach private placements (*Gustafson v. Alloyd Co.*, 513 U.S. 561 (1995)), but state statutes such as Cal. Corp. Code §§ 25401/25501 do, often on a negligence standard.
- **Practical exposure** in SAFE and note rounds comes from pitch decks (traction, revenue, customer logos, pipeline), financial projections without reasonable basis, undisclosed related-party arrangements, cap table misstatements, undisclosed litigation or IP ownership defects, and statements about other investors' participation.
- **Mitigation:** make the deck accurate and dated; label projections as forward-looking with meaningful cautionary language; give investors a short risk-factor summary and the opportunity to ask questions; keep a data room; use investor representations of independent investigation and non-reliance (helpful but not a complete defense, particularly against fraud claims); and make sure the company's representations in the instrument are true at signing. The YC SAFE's company representations are limited; the skill's note purchase agreement contains fuller ones.

---

## 16. Foreign investors

### 16.1 Regulation D still works

Regulation D is available to non-U.S. investors who are accredited; most startups simply include foreign investors in the Rule 506(b) offering and file Form D. Local law of the investor's country may impose its own private-placement requirements; ask local counsel for large or repeated sales into a single country.

### 16.2 Regulation S (17 C.F.R. §§ 230.901–230.905)

Regulation S exempts offers and sales made in **offshore transactions** with **no directed selling efforts** in the United States. Equity securities of a non-reporting U.S. issuer fall in **Category 3** (Rule 903(b)(3)): offering restrictions; a **one-year distribution compliance period** (six months for reporting issuers) during which sales may not be made to U.S. persons; purchaser certifications of non-U.S. status; purchaser agreement to resell only under Regulation S, registration, or an exemption; restrictive legends; and stop-transfer instructions. Equity securities of domestic issuers sold under Regulation S are restricted securities (Rule 905). Regulation S offerings are not integrated with other offerings (Rule 152(b)(2)). Use it principally for non-accredited foreign investors.

### 16.3 CFIUS (31 C.F.R. Part 800)

- **Jurisdiction:** control transactions by foreign persons in any U.S. business, and **covered investments** (non-controlling) by foreign persons (other than excepted investors) in a **TID U.S. business** (one that produces, designs, tests, manufactures, fabricates, or develops **critical technologies**; performs specified functions for covered investment critical infrastructure; or maintains or collects **sensitive personal data** of U.S. citizens) (31 C.F.R. §§ 800.211, 800.248).
- **Covered investment** = a non-controlling investment that affords the foreign person (1) access to **material nonpublic technical information**, (2) **board membership or observer rights**, or the right to nominate a director, or (3) involvement (other than through voting shares) in substantive decision-making about sensitive personal data, critical technologies, or covered infrastructure (§ 800.211).
- **Contingent equity interests** (financial instruments convertible into equity on a contingency, such as SAFEs and notes) are a defined term (§ 800.207); CFIUS assesses the rights the instrument confers and the timing of conversion, so a SAFE or note can be a covered transaction, and conversion can be one.
- **Mandatory declarations (§ 800.401):** required for (a) a covered transaction in which a foreign person in which a single foreign government holds a substantial interest acquires a substantial interest in a TID U.S. business, and (b) a covered transaction involving a TID U.S. business that deals in critical technologies for which a **U.S. export authorization would be required** to export them to the foreign investor (determined without most license exceptions), subject to exceptions (e.g., certain investment funds managed by U.S. general partners, and excepted investors). File **at least 30 days before completion** (§ 800.401(g)). Failure to file can draw a civil penalty up to the **greater of $5,000,000 or the value of the transaction** (§ 800.901(b)).
- **Startup practice:** ask every foreign investor's nationality and ownership (the questionnaire does); determine whether the company is a TID U.S. business (export classification of its technology under the EAR/ITAR is the first step); for foreign SAFE and note investors, **withhold** board, observer, and access-to-technical-information rights (draft information rights to exclude material nonpublic technical information for foreign persons), which usually keeps a minority investment outside "covered investment"; and condition closing on any required declaration.

> **Verify:** Check 31 C.F.R. Part 800 and Treasury's CFIUS website for amendments after November 2, 2026, the current list of excepted foreign states and excepted investors, and any updated penalty guidance before advising on a foreign investment in a TID U.S. business.

### 16.4 Outbound Investment Security Program (31 C.F.R. Part 850)

Effective **January 2, 2025** (Treasury final rule of October 28, 2024), this program prohibits or requires notification of certain investments by **U.S. persons** in **covered foreign persons**, i.e., persons of a country of concern (currently the PRC, including Hong Kong and Macau) engaged in covered activities involving semiconductors and microelectronics, quantum information technologies, and artificial intelligence, and persons deriving more than 50% of revenue, net income, capital expenditure, or operating expenses from such persons (§ 850.209).

- **Covered transactions** include acquisitions of equity **or contingent equity** (SAFEs, convertible notes), certain debt with equity-like rights, **conversion of contingent equity acquired on or after January 2, 2025**, greenfield and brownfield investments, and joint ventures (§ 850.210). Excepted transactions include publicly traded securities and certain limited partner investments of $2,000,000 or less (§ 850.501).
- **Notifications** are due **no later than 30 calendar days after completion** of a notifiable transaction, through Treasury's Outbound Notification System (§§ 850.401, 850.404 and related provisions).
- **Why a U.S. startup cares:** (1) a U.S. startup with a PRC subsidiary or affiliate engaged in a covered activity (or deriving more than half its revenue or expenses from one) may itself be a covered foreign person, making its U.S. investors' SAFEs or notes covered transactions; (2) a startup that invests in or forms a joint venture with a PRC entity is itself a U.S. person subject to the rules; (3) U.S. fund investors will ask for representations on these points.
- **COINS Act.** On December 18, 2025, Congress enacted the Comprehensive Outbound Investment National Security Act as part of the FY2026 National Defense Authorization Act, codified at Title VIII of the Defense Production Act. It codifies and expands the program (reported expansions include additional countries of concern and sectors such as hypersonics and high-performance computing). Treasury's website reports a notice of proposed rulemaking issued **October 22, 2026** (comments due December 7, 2026). The existing Part 850 rules remain in effect until Treasury's implementing rules take effect.

> **Verify:** Check Treasury's Outbound Investment Security Program page for the status and content of the COINS Act rulemaking, the final list of countries of concern, and covered sectors before advising on any transaction with a nexus to a country of concern.

### 16.5 Sanctions and AML

Screen every investor (and, for entities, controlling owners) against OFAC's Specially Designated Nationals and other lists, applying OFAC's 50% rule; do not accept funds from comprehensively sanctioned jurisdictions; ask about the source of funds where facts suggest risk. The investor questionnaire contains these representations.

### 16.6 Tax documentation for foreign holders

Collect IRS Form W-8BEN or W-8BEN-E (or W-9 for U.S. persons) at closing. Interest on convertible notes paid to foreign holders may qualify for the portfolio interest exemption only if the note is in **registered form** and other conditions are met (I.R.C. §§ 871(h), 881(c)), which is why the note template keeps a note register.

> **Verify:** Confirm with tax counsel whether a foreign noteholder's conversion rights cause it to be treated as a 10% shareholder (which defeats the portfolio interest exemption) and whether withholding applies to accrued interest that converts into stock.

---

## 17. Compliance path for a typical SAFE or note round

1. **Board approval** of the instruments, maximum amount, form documents, closing window, and filings (board consent template); for notes, reserve or confirm authorized common; preferred cannot be reserved until it is authorized in the priced round's charter.
2. **Choose the exemption:** Rule 506(b) (default, no general solicitation, all accredited) or Rule 506(c) (if there has been or will be general solicitation; verify every purchaser).
3. **EDGAR access:** apply on Form ID immediately if the company has no CIK.
4. **Investor diligence:** questionnaire (accredited status, bad-actor certification for 20% holders, foreign person/CFIUS, OFAC, ERISA, FINRA affiliation); verification documents for 506(c).
5. **Disclosure hygiene:** accurate deck, risk summary, data room, opportunity for questions.
6. **Sign and fund;** countersign only on receipt of funds; record the date of first sale.
7. **Form D** within 15 calendar days after the first sale; **state notices** within each state's deadline (15 days in California, New York, Texas, and Washington); calendar the **annual amendment** if the round stays open beyond a year.
8. **Foreign investors:** CFIUS analysis before signing; outbound analysis if any China nexus; W-8 forms.
9. **Post-closing:** cap table and ledger updates, legends, data room, and tax reporting for notes.

---

## Sources

**Primary (federal):**
- Securities Act §§ 2(a)(1), 3(a)(9), 4(a)(2), 4(a)(6), 4(a)(7), 5, 12(a)(2), 17(a), 18 (15 U.S.C. §§ 77b, 77c, 77d, 77e, 77l, 77q, 77r); Exchange Act §§ 10(b), 15(a), 15(b)(13), 29(b).
- 17 C.F.R. §§ 230.144, 230.148, 230.152, 230.241, 230.251, 230.501–230.508, 230.701, 230.901–230.905; 17 C.F.R. § 227.100; 17 C.F.R. § 240.10b-5. Current text retrieved from eCFR (ecfr.gov) on November 2, 2026; Rule 501 last amended February 18, 2025 (90 FR 9687, cross-reference corrections only).
- SEC staff no-action letter to Latham & Watkins LLP (Mar. 12, 2025): https://www.sec.gov/rules-regulations/no-action-interpretive-exemptive-letters/division-corporation-finance-no-action/latham-watkins-503c-031225 and incoming letter https://www.sec.gov/files/corpfin/no-action/latham-watkins506c-031225-incoming.pdf
- SEC, Potential Designations of the Series 79 and Series 86/87 Licenses (Release No. 33-11449, Sept. 30, 2026; 4-935): https://www.sec.gov/files/rules/other/2026/33-11449.pdf (and companion notices 33-11445 to 33-11448 as summarized by Latham & Watkins, https://www.lw.com/en/insights/sec-proposes-sweeping-performance-fee-eligibility-reforms-and-new-accredited-investor-pathways).
- SEC, Filing and Amending a Form D Notice: https://www.sec.gov/info/smallbus/secg/formdguide
- SEC, EDGAR Next fact sheet (Release No. 33-11313): https://www.sec.gov/files/33-11313-fact-sheet.pdf; EDGAR Next page: https://www.sec.gov/submit-filings/improving-edgar/edgar-next-improving-filer-access-account-management
- SEC Investor Bulletin on SAFEs (May 2017): https://www.sec.gov/oiea/investor-alerts-and-bulletins/ib_safes
- 31 C.F.R. Part 800 (§§ 800.207, 800.211, 800.248, 800.401, 800.901) and Part 850 (§§ 850.209, 850.210, 850.401–850.404, 850.501), from eCFR; Treasury Outbound Investment Security Program: https://home.treasury.gov/policy-issues/international/outbound-investment-program
- Cases: *SEC v. Ralston Purina Co.*, 346 U.S. 119 (1953); *Landreth Timber Co. v. Landreth*, 471 U.S. 681 (1985); *Reves v. Ernst & Young*, 494 U.S. 56 (1990); *Gustafson v. Alloyd Co.*, 513 U.S. 561 (1995); *Doran v. Petroleum Mgmt. Corp.*, 545 F.2d 893 (5th Cir. 1977).

**Primary (state):**
- California DFPI Securities FAQ: https://dfpi.ca.gov/rules-enforcement/laws-and-regulations/law-and-regulations-corporate-securities-law/securities-frequently-asked-questions-and-answers/ ; DFPI fee index (ADM 510, rev. 10/25): https://dfpi.ca.gov/wp-content/uploads/2025/10/DFPI-ADM-510-Index-of-Fees_-Fines-and-Penalties-Rev.-10-25.pdf ; Cal. Corp. Code §§ 25102(f), 25102.1(d), 25206.1, 25401, 25501, 25501.5, 25504, 25608, 25608.1.
- Texas State Securities Board, Regulation D filing requirements: https://ssb.texas.gov/securities-professionals/regulation-securities/filing-requirements-regulation-d-offerings-texas
- Washington DFI, Rule 506 filing FAQ: https://dfi.wa.gov/node/3009 ; WAC 460-44A-503.
- New York: 13 NYCRR § 10.8 (fees); NYAG EFD Form D guidance: https://ag.ny.gov/sites/default/files/part10-efd-formd-guidance.pdf
- NASAA EFD fee FAQ: https://www.nasaaefd.org/FAQ/answer?faq=4 (system use fee $160 per initial Form D notice).

**Secondary (used for context and cross-checking only):** Cahill (June 11, 2025), Akin Gump, Paul Hastings, and Morgan Lewis alerts on the March 2025 Rule 506(c) guidance; Arnold & Porter, Akin Gump, and Mayer Brown alerts on the COINS Act (Dec. 2025–Jan. 2026).
