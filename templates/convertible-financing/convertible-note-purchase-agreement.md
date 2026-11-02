---
id: convertible-note-purchase-agreement
title: Convertible Note Purchase Agreement
category: convertible-financing
stage: convertible
signers: [Company (by an officer), each Purchaser (counterpart signature page)]
authorities:
  - "8 Del. C. §§ 122(13), 141(f), 152, 153, 157, 161 (borrowing; board approval; rights to acquire stock; issuance)"
  - "8 Del. C. § 144 (interested director and officer transactions, as amended 2025)"
  - "Securities Act § 4(a)(2); 17 C.F.R. §§ 230.501–230.506 (Regulation D), including Rule 506(d) (bad actors)"
  - "17 C.F.R. § 230.503 (Form D within 15 calendar days after first sale)"
  - "Securities Act § 18(b)(4)(F); Cal. Corp. Code § 25102.1(d) (state notice filings)"
  - "31 C.F.R. Parts 800 (CFIUS) and 850 (Outbound Investment Security Program); 31 C.F.R. ch. V (OFAC)"
  - "26 U.S.C. § 1202 (QSBS information covenant)"
use_when: The company is selling a series of convertible promissory notes to one or more accredited investors, with an initial closing and optional additional closings up to a maximum principal amount.
do_not_use_when: The investors will take SAFEs (use the YC SAFE via safe-guide), the financing is a priced preferred round (use the priced-financing templates), or the lender is a bank or venture-debt fund (use a loan agreement).
related: [convertible-promissory-note, board-consent-convertible-financing, investor-questionnaire, safe-side-letter, convertible-financing-checklist]
sources:
  - name: "Series Seed documents (CC0 1.0) — structure of company and purchaser representations and closing mechanics (reference; adapted concepts, original language)"
    url: https://www.seriesseed.com
  - name: "17 C.F.R. Part 230 (Regulation D) — eCFR, current text"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230
  - name: "8 Del. C. § 144 (as amended by SB 21, 2025) — official Delaware Code; Rutledge v. Clearway Energy Group LLC (Del. Feb. 27, 2026) (upholding amendments)"
    url: https://delcode.delaware.gov/title8/c001/sc04/index.html
  - name: "31 C.F.R. §§ 800.211, 800.401 and Part 850 — eCFR"
    url: https://www.ecfr.gov/current/title-31
  - name: "SEC staff no-action letter (Latham & Watkins, Mar. 12, 2025) — Rule 506(c) minimum-investment verification"
    url: https://www.sec.gov/rules-regulations/no-action-interpretive-exemptive-letters/division-corporation-finance-no-action/latham-watkins-503c-031225
last_verified: 2026-11-02
---

# Convertible Note Purchase Agreement

## About this template

### 1. What this document does and where it sits

The Note Purchase Agreement ("NPA") is the contract under which the Company sells a series of identical convertible promissory notes (the [convertible-promissory-note](convertible-promissory-note.md) form, attached as Exhibit A) to the purchasers listed on the Schedule of Purchasers. It provides for an **Initial Closing** and **Additional Closings** up to a **Maximum Amount** within a stated window, contains the Company's and purchasers' representations, closing conditions, covenants, and Majority-Holder amendment mechanics, and binds holders to the note's conversion, subordination, and transfer terms.

Order of signing: (1) board consent approving the note financing ([board-consent-convertible-financing](board-consent-convertible-financing.md)); (2) investor questionnaires ([investor-questionnaire](investor-questionnaire.md)); (3) NPA signed by the Company and the initial purchasers; (4) funds received; (5) Notes issued; (6) Form D within 15 calendar days after the first sale and state notices; (7) Additional Closings by counterpart signature pages and an updated Schedule of Purchasers.

### 2. Key business decisions and market positions

| Issue | Company-favorable | Market | Purchaser-favorable | Form default |
|---|---|---|---|---|
| Company representations | Short list; knowledge-qualified | Organization, capitalization, authorization, valid issuance, no conflicts, consents, litigation, IP, compliance, private offering, bad actor | Full Series A-style reps with financial statements and a "10b-5" disclosure rep | Market list; optional financial statements, disclosure, and QSBS reps |
| Survival of reps | 6–12 months | 12–18 months | Until conversion or longer | `{{rep_survival_months}}` months |
| Additional Closings | Unlimited time; any purchaser | Within 90–180 days; same terms; up to a maximum | Lead approval of each additional purchaser | `{{additional_closing_deadline}}` and `{{maximum_amount}}` |
| Amendment | Company + Majority Holders | Majority with protections against disproportionate treatment | Each holder | Majority with protections |
| Lead counsel fees | None | Capped reimbursement for the lead | Uncapped | Optional cap |
| Information rights | None | Annual financials to "Major Purchasers" | Quarterly + budget | Optional |
| MFN on later convertibles | None | Common in early notes | Full MFN | Optional |
| Subordination | Agree in advance to subordinate to future senior debt | Same | Negotiate case by case | Optional |

### 3. Statutory and regulatory points

- **Exemption.** The NPA is drafted for **Rule 506(b)** (no general solicitation; all purchasers accredited), with an alternative for **Rule 506(c)** (Section 4.5 and Exhibit C verification). If any purchaser is not accredited, Rule 502(b) disclosure and sophistication requirements apply; the form assumes they do not. See [references/securities-law.md](../../references/securities-law.md).
- **Bad actor.** Rule 506(d) disqualifies the offering if a covered person (including any purchaser who will own 20% or more of voting equity on an as-converted basis, and any compensated solicitor) has a disqualifying event. The Company rep (Section 3.15) and the purchaser rep (Section 4.9) cover both sides.
- **Insider participation.** If directors, officers, or their affiliates buy notes, approve under 8 Del. C. § 144(a) as amended in 2025: approval by a majority of the disinterested directors after disclosure of the material facts (if a majority of the board is not disinterested, a committee of two or more disinterested directors must approve or recommend), or approval by a majority of the votes cast by disinterested stockholders, or fairness. Different safe harbors apply to controlling-stockholder transactions (§ 144(b)). The Delaware Supreme Court upheld the 2025 § 144 amendments in *Rutledge v. Clearway Energy Group LLC* (Feb. 27, 2026). Offering the notes to all existing holders pro rata on identical terms helps establish fairness.
- **CFIUS and outbound investment.** Section 4.10 requires each purchaser to disclose foreign-person status; Section 6.9 prevents the Company from giving foreign persons board, observer, or technical-information rights without a CFIUS analysis. Section 3.20 (optional) addresses the Company's own outbound-investment status.
- **Usury, tax, OID, and the AFR:** see the note template's About section.
- **Jury waivers in California.** Pre-dispute contractual jury waivers are unenforceable in California courts (*Grafton Partners L.P. v. Superior Court*, 36 Cal. 4th 944 (2005)); the NPA selects a Delaware forum and applies the waiver to the extent permitted.

### 4. Common mistakes this form avoids

1. Additional closings without a deadline or maximum (Section 2.3 caps both).
2. Schedule of Purchasers not updated at each closing (Section 2.3(c)).
3. Capitalization rep that omits SAFEs, notes, and promised options (Section 3.2 requires them).
4. Amendments that can strip a minority holder's economics (Section 7.2 lists protected rights).
5. No covenant to authorize the preferred into which notes convert (Section 6.2).
6. Missing Form D and state filings covenant (Section 6.4).
7. Purchasers who later claim they relied on other purchasers or on the lead (Section 4.12, exculpation among purchasers).

### 5. Deadlines triggered

| Trigger | Deadline |
|---|---|
| First sale (Initial Closing) | Form D within 15 calendar days (17 C.F.R. § 230.503(a)(1)); state notices (e.g., California § 25102.1(d), 15 days, $300) |
| Each Additional Closing in a new state | That state's notice deadline |
| Offering still open one year after the last Form D | Annual Form D amendment (17 C.F.R. § 230.503(a)(3)(iii)) |
| Final Additional Closing deadline | `{{additional_closing_deadline}}` |
| Annual financial statements (if Section 6.6 used) | `{{annual_info_days}}` days after fiscal year end |

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | Shared |
| `{{company_address}}`, `{{company_notice_email}}` | Company notice details | | Shared |
| `{{effective_date}}` | Date of the NPA | January 15, 2027 | Shared |
| `{{initial_closing_date}}` | Initial Closing date | January 15, 2027 | Shared |
| `{{additional_closing_deadline}}` | Last date for Additional Closings | April 15, 2027 | Shared |
| `{{maximum_amount}}` | Maximum aggregate principal of all Notes | $3,000,000 | Must not exceed board approval |
| `{{minimum_initial_closing_amount}}` | Minimum aggregate principal at Initial Closing | $1,000,000 | Optional condition |
| `{{interest_rate}}`, `{{maturity_date}}`, `{{valuation_cap}}`, `{{discount_rate}}`, `{{qualified_financing_amount}}` | Note economic terms (summarized in Recital B) | 6%; January 15, 2029; $12,000,000; 20% discount; $2,000,000 | Shared; must match the Note |
| `{{authorized_common_shares}}`, `{{authorized_preferred_shares}}` | Authorized shares | 10,000,000; 0 | Shared |
| `{{common_outstanding}}` | Common outstanding | 8,000,000 | |
| `{{plan_name}}`, `{{plan_reserve_shares}}` | Equity plan and reserve | 2027 Equity Incentive Plan; 1,500,000 | Shared |
| `{{options_outstanding}}` | Awards outstanding under the plan | 1,000,000 | |
| `{{plan_available_shares}}` | Shares available for grant | 500,000 | |
| `{{other_convertibles_description}}` | SAFEs, notes, warrants outstanding | SAFEs with aggregate Purchase Amount of $750,000 | "None" if none |
| `{{financial_statements_date}}` | Balance sheet date (optional rep) | December 31, 2026 | |
| `{{rep_survival_months}}` | Survival period for representations | 12 | |
| `{{major_purchaser_threshold}}` | Principal needed for information rights | $250,000 | Optional Section 6.6 |
| `{{annual_info_days}}`, `{{quarterly_info_days}}` | Information delivery periods | 120; 45 | Optional |
| `{{lead_purchaser_name}}`, `{{lead_counsel_fee_cap}}` | Lead purchaser and fee cap | Example Ventures Fund I, L.P.; $15,000 | Optional Section 9.10 |
| `{{governing_law_state}}`, `{{forum}}` | Governing law and forum | Delaware; Court of Chancery of the State of Delaware | Shared |
| `{{signatory_name}}`, `{{signatory_title}}` | Company signatory | Alex Rivera, Chief Executive Officer | Shared |
| `{{investor_name}}`, `{{investor_address}}`, `{{investor_email}}`, `{{investor_entity_type}}`, `{{purchase_amount}}` | Purchaser counterpart details | | Shared; one counterpart page per purchaser |
| `{{investor_signatory_name}}`, `{{investor_signatory_title}}` | Purchaser signatory | | Entities |
| `{{investor_tax_id_form}}` | W-9 or W-8 delivered | Form W-9 | |
| `{{knowledge_individuals}}` | Individuals whose knowledge is the Company's Knowledge | Alex Rivera and Jordan Lee | |
| `{{voting_agreements_description}}` | Voting or registration rights agreements | none | |
| `{{permitted_insider_payments}}` | Permitted payments to insiders from proceeds | accrued salary in the ordinary course | Optional |
| `{{closing_date}}` | Closing date for a counterpart page or Schedule row | January 15, 2027 | Shared |
| `{{note_number}}` | Note number for the Schedule row | CN-001 | Matches the Note |
| `{{investor_residence_state}}` | Purchaser's state or country of residence | California | Blue-sky filings |
| `{{aggregate_principal}}` | Total principal sold to date | $1,500,000 | Must not exceed `{{maximum_amount}}` |
| `{{promised_awards_description}}`, `{{other_convertibles_detail}}`, `{{acceleration_description}}`, `{{litigation_description}}`, `{{related_party_description}}`, `{{other_disclosures}}` | Disclosure Schedule entries | | "None" where nothing to disclose |

## Form

---

# {{company_name}}

## CONVERTIBLE NOTE PURCHASE AGREEMENT

This Convertible Note Purchase Agreement (this "**Agreement**") is entered into as of {{effective_date}} by and among {{company_name}}, a Delaware corporation (the "**Company**"), and the persons listed on the Schedule of Purchasers attached as Schedule A (each, a "**Purchaser**" and together, the "**Purchasers**").

### RECITALS

A. The Company desires to raise up to {{maximum_amount}} by issuing and selling Convertible Promissory Notes in the form attached as Exhibit A (each, a "**Note**" and together, the "**Notes**"), and each Purchaser desires to purchase a Note in the principal amount set forth opposite its name on the Schedule of Purchasers, on the terms of this Agreement.

B. The Notes bear simple interest at {{interest_rate}} per annum, mature on {{maturity_date}}, and convert into equity securities of the Company on the terms set forth in the Notes, including automatic conversion in a Qualified Financing (a financing with aggregate New Money of at least {{qualified_financing_amount}}) at the lesser of a price reflecting a discount of {{discount_rate}} and a price based on a valuation cap of {{valuation_cap}}. If this Recital conflicts with the Notes, the Notes control.

NOW, THEREFORE, in consideration of the mutual promises in this Agreement, the parties agree as follows.

## ARTICLE 1. DEFINITIONS AND INTERPRETATION

**1.1 Definitions.** Capitalized terms used but not defined in this Agreement have the meanings given in the Notes. In addition:

"**Affiliate**" means, with respect to a person, any other person that directly or indirectly controls, is controlled by, or is under common control with that person, including any investment fund managed or advised by the same general partner, managing member, or management company.

"**Bad Actor Event**" means any event described in Rule 506(d)(1)(i)–(viii) under the Securities Act.

"**Closing**" means the Initial Closing or any Additional Closing.

"**Code**" means the Internal Revenue Code of 1986, as amended.

"**Disclosure Schedule**" means the disclosure schedule delivered by the Company to the Purchasers at the Initial Closing, as supplemented at any Additional Closing under Section 2.3(d).

"**Foreign Person**" has the meaning given in 31 C.F.R. § 800.224.

"**Governmental Authority**" means any federal, state, local, or foreign government, regulatory or administrative agency, court, or self-regulatory organization.

"**Knowledge**," with respect to the Company, means the actual knowledge of {{knowledge_individuals}}, after reasonable inquiry of the employees who report directly to them.

"**Liens**" means liens, security interests, pledges, charges, and encumbrances.

"**Majority Holders**" has the meaning given in the Notes.

"**Material Adverse Effect**" means a material adverse effect on the business, assets, liabilities, financial condition, or results of operations of the Company, taken as a whole, or on the Company's ability to perform this Agreement or the Notes.

"**Securities Act**" means the Securities Act of 1933, as amended, and the rules and regulations of the Securities and Exchange Commission (the "**SEC**") under it.

"**Transaction Documents**" means this Agreement and the Notes.

**1.2 Interpretation.** In this Agreement: "including" means "including without limitation"; "or" is not exclusive; references to Articles, Sections, Schedules, and Exhibits are to this Agreement; headings are for convenience only; the singular includes the plural; "days" means calendar days unless Business Days are specified; and no provision is to be construed against a party because that party drafted it.

## ARTICLE 2. PURCHASE AND SALE OF NOTES; CLOSINGS

**2.1 Sale and Issuance of Notes.** Subject to this Agreement, the Company shall issue and sell to each Purchaser, and each Purchaser severally (and not jointly) agrees to purchase from the Company, at the applicable Closing, a Note in the principal amount set forth opposite that Purchaser's name on the Schedule of Purchasers, for a purchase price equal to that principal amount.

**2.2 Initial Closing.** The initial purchase and sale of Notes (the "**Initial Closing**") shall take place remotely by electronic exchange of documents and signatures on {{initial_closing_date}}, or at another time and place the Company and the Purchasers purchasing a majority of the principal amount to be sold at the Initial Closing agree in writing.

**2.3 Additional Closings.**

(a) *Right to Hold Additional Closings.* At any time after the Initial Closing and on or before {{additional_closing_deadline}}, the Company may sell additional Notes, on the same terms as the Notes sold at the Initial Closing, to one or more additional purchasers (each, an "**Additional Closing**"), provided that the aggregate principal amount of all Notes sold under this Agreement does not exceed {{maximum_amount}} [[Optional: and that each additional purchaser is approved in writing by {{lead_purchaser_name}}, which approval shall not be unreasonably withheld]].

(b) *Joinder.* Each additional purchaser shall become a party to this Agreement as a "Purchaser" by executing a counterpart signature page to this Agreement and an investor questionnaire, and shall have the rights and obligations of a Purchaser under this Agreement.

(c) *Schedule of Purchasers.* The Company shall update the Schedule of Purchasers at each Additional Closing to add each additional purchaser and the principal amount of its Note, without the need for the consent of any other Purchaser, and shall deliver the updated Schedule to each Purchaser within ten (10) Business Days after the Additional Closing.

(d) *Bring-Down.* At each Additional Closing, the Company's representations and warranties in Article 3 shall be made to the additional purchasers as of the date of that Additional Closing, subject to any supplement to the Disclosure Schedule delivered to those purchasers. A supplement does not cure any inaccuracy in a representation made at an earlier Closing.

**2.4 Deliveries at Each Closing.**

(a) *By the Company.* The Company shall deliver to each Purchaser purchasing at that Closing (i) its Note, duly executed by the Company, in electronic form (with an original delivered on request); (ii) at the Initial Closing, a copy of the resolutions of the Company's board of directors approving the Transaction Documents, certified by the Company's secretary; and (iii) [[Optional: a certificate of good standing of the Company issued by the Delaware Secretary of State dated within ten (10) Business Days before the Initial Closing]].

(b) *By each Purchaser.* Each Purchaser purchasing at that Closing shall deliver to the Company (i) the purchase price of its Note by wire transfer of immediately available funds to the account the Company designates in writing (with call-back verification of wire instructions by telephone to a known number); (ii) a counterpart signature page to this Agreement; (iii) a completed investor questionnaire in the form provided by the Company; (iv) a properly completed IRS Form W-9 or applicable Form W-8; and (v) [[Alternative A: nothing further]] [[Alternative B: the verification materials required by Section 4.5(b)]].

**2.5 Use of Proceeds.** The Company shall use the proceeds from the sale of the Notes for product development, working capital, and other general corporate purposes, and not to repay indebtedness owed to, or redeem securities held by, any officer, director, or stockholder of the Company [[Optional: , other than {{permitted_insider_payments}}]].

## ARTICLE 3. REPRESENTATIONS AND WARRANTIES OF THE COMPANY

Except as set forth in the Disclosure Schedule (which identifies the Section to which each exception relates, and an exception in one section qualifies another section only where its relevance is reasonably apparent on its face), the Company represents and warrants to each Purchaser as of the Initial Closing (and, for Purchasers at an Additional Closing, as of that Additional Closing) as follows.

**3.1 Organization; Good Standing; Power.** The Company is a corporation duly organized, validly existing, and in good standing under the laws of the State of Delaware, has all requisite corporate power and authority to own and operate its properties and assets, to carry on its business as now conducted, and to execute, deliver, and perform the Transaction Documents, and is duly qualified to transact business and in good standing in each jurisdiction where the failure to qualify would have a Material Adverse Effect.

**3.2 Capitalization.**

(a) *Authorized and Outstanding Stock.* The authorized capital stock of the Company consists of {{authorized_common_shares}} shares of Common Stock and {{authorized_preferred_shares}} shares of Preferred Stock. As of immediately before the Initial Closing, {{common_outstanding}} shares of Common Stock and no shares of Preferred Stock are issued and outstanding. All outstanding shares are duly authorized, validly issued, fully paid, and non-assessable, and were issued in compliance with applicable federal and state securities laws.

(b) *Equity Plan.* The Company has reserved {{plan_reserve_shares}} shares of Common Stock for issuance under its {{plan_name}} (the "**Plan**"), under which options and other awards covering {{options_outstanding}} shares are outstanding and {{plan_available_shares}} shares remain available for grant. Section 3.2(b) of the Disclosure Schedule lists all promises of equity awards not yet granted.

(c) *Other Rights.* Except for the Notes, the Plan awards described in Section 3.2(b), and {{other_convertibles_description}} (each of which is described, with its material economic terms, in Section 3.2(c) of the Disclosure Schedule), there are no outstanding options, warrants, rights (including conversion, preemptive, or participation rights, rights of first refusal, and simple agreements for future equity), convertible securities, or agreements for the purchase or acquisition from the Company of any of its capital stock or securities convertible into its capital stock.

(d) *Vesting and Acceleration.* Section 3.2(d) of the Disclosure Schedule describes any acceleration of vesting of any outstanding stock or award on a change of control or termination of service, other than as provided in the Plan's standard forms.

(e) *Voting and Registration Rights.* The Company is not a party to any agreement relating to the voting of its capital stock or granting registration rights, other than {{voting_agreements_description}}.

**3.3 Authorization.** All corporate action required of the Company's board of directors and stockholders for the authorization, execution, delivery, and performance of the Transaction Documents and the issuance of the Notes has been taken. The Transaction Documents, when executed and delivered by the Company, constitute valid and legally binding obligations of the Company, enforceable in accordance with their terms, except as limited by bankruptcy, insolvency, reorganization, and similar laws of general application affecting creditors' rights, by general principles of equity, and by limitations on the enforceability of indemnification provisions.

**3.4 Valid Issuance.** The Notes, when issued and paid for under this Agreement, will be validly issued and free of Liens created by the Company and restrictions on transfer other than those under the Transaction Documents and applicable securities laws. The equity securities issuable on conversion of the Notes, when issued in accordance with the Notes and the Company's certificate of incorporation as then in effect, will be duly authorized, validly issued, fully paid, and non-assessable. Based in part on the Purchasers' representations in Article 4, and assuming the accuracy of those representations, the offer, sale, and issuance of the Notes are, and the issuance of the conversion securities will be, exempt from registration under the Securities Act and from qualification or registration under applicable state securities laws.

**3.5 No Conflicts.** The Company's execution, delivery, and performance of the Transaction Documents and issuance of the Notes do not and will not (a) violate its certificate of incorporation or bylaws; (b) violate any judgment, order, statute, rule, or regulation applicable to the Company; or (c) conflict with, breach, constitute a default under, or give rise to a right of termination or acceleration or the creation of any Lien under, any material agreement to which the Company is a party, except, in the case of clauses (b) and (c), as would not have a Material Adverse Effect.

**3.6 Governmental Consents.** No consent, approval, order, or authorization of, or registration, qualification, or filing with, any Governmental Authority is required for the Company's valid execution, delivery, and performance of the Transaction Documents, except (a) the filing of a notice of sales on Form D with the SEC under Regulation D and notice filings under applicable state securities laws, which the Company will timely make, and (b) any action required to authorize the equity securities issuable on conversion of the Notes, which will be taken before conversion.

**3.7 Litigation.** There is no action, suit, proceeding, or investigation pending or, to the Company's Knowledge, threatened in writing against the Company, its properties, or (in their capacities as such) its officers or directors that (a) questions the validity of the Transaction Documents or the Company's right to enter into them, or (b) would reasonably be expected to have a Material Adverse Effect.

**3.8 Intellectual Property.** To the Company's Knowledge, the Company owns or possesses, or can obtain on commercially reasonable terms, sufficient legal rights to all patents, trademarks, service marks, trade names, copyrights, trade secrets, software, and other intellectual property necessary for its business as now conducted and as currently proposed to be conducted, without any known conflict with or infringement of the rights of others. Each current and former employee and consultant who has contributed to the creation or development of the Company's material intellectual property has executed an agreement assigning to the Company all of that person's rights in it and agreeing to maintain the confidentiality of the Company's confidential information, and each founder has assigned to the Company all intellectual property relating to the Company's business that the founder developed before the Company's formation.

**3.9 Compliance with Laws and Documents.** The Company is not in violation of its certificate of incorporation or bylaws, or, to its Knowledge, of any statute, rule, regulation, or order applicable to it, or in default under any material agreement, in each case where the violation or default would reasonably be expected to have a Material Adverse Effect.

**3.10 Financial Statements.** [[Optional: The Company has delivered to the Purchasers its unaudited balance sheet as of {{financial_statements_date}} and the related statement of operations for the period then ended (the "**Financial Statements**"). The Financial Statements fairly present in all material respects the Company's financial condition and results of operations as of their date and for the period covered, in accordance with U.S. generally accepted accounting principles applied on a consistent basis (except for the absence of footnotes and normal year-end adjustments). Since the date of the balance sheet, there has been no Material Adverse Effect, and the Company has no liabilities other than those reflected in the Financial Statements, those incurred in the ordinary course of business since their date, and obligations under contracts not required to be reflected in financial statements.]]

**3.11 Taxes.** The Company has timely filed all income and other material tax returns required to be filed by it and has paid all taxes shown as due on them, and there is no pending or, to the Company's Knowledge, threatened tax audit or deficiency against the Company.

**3.12 Employees.** To the Company's Knowledge, no employee or consultant of the Company is in violation of any term of any employment, consulting, confidentiality, non-competition, or invention-assignment agreement with a former employer or other third party relating to that person's right to be engaged by the Company or to use trade secrets or proprietary information of others. All current employees and consultants are engaged under written agreements or offer letters that the Company has made available to the Purchasers on request.

**3.13 Related-Party Transactions.** Except as described in Section 3.13 of the Disclosure Schedule, no director, officer, or stockholder holding five percent (5%) or more of the Company's capital stock, or any member of that person's immediate family or any entity that person controls, is indebted to the Company, is owed money by the Company (other than for accrued compensation and reimbursable expenses in the ordinary course), or is a party to any material agreement or transaction with the Company (other than employment, consulting, equity award, and indemnification agreements on the Company's standard forms). Any participation in the purchase of Notes by a director or officer of the Company, or by an Affiliate of either, has been approved in accordance with 8 Del. C. § 144.

**3.14 Private Offering.** [[Alternative A: Neither the Company nor anyone acting on its behalf has offered or sold the Notes by any form of general solicitation or general advertising within the meaning of Rule 502(c) under the Securities Act, and, assuming the accuracy of the Purchasers' representations in Article 4, the offer and sale of the Notes satisfy the conditions of Rule 506(b).]] [[Alternative B: The Company is offering the Notes in reliance on Rule 506(c) under the Securities Act and has taken, and will take, reasonable steps to verify that each Purchaser is an accredited investor, as required by Rule 506(c)(2)(ii).]] Neither the Company nor anyone acting on its behalf has taken any action that would cause the offer and sale of the Notes to be integrated with any other offering in a manner that would require registration under the Securities Act.

**3.15 No Bad Actor Disqualification.** No "Company Covered Person" (meaning the Company, any predecessor or affiliated issuer, any director, executive officer, or other officer participating in the offering, any beneficial owner of twenty percent (20%) or more of the Company's outstanding voting equity securities (calculated on the basis of voting power), any promoter connected with the Company, and any person that has been or will be paid, directly or indirectly, remuneration for soliciting purchasers of the Notes) is subject to a Bad Actor Event, except a Bad Actor Event covered by Rule 506(d)(2)(ii) or (iii) or (d)(3). The Company has exercised reasonable care to determine whether any Company Covered Person is subject to a Bad Actor Event and has furnished to each Purchaser, a reasonable time before the sale, any disclosure required by Rule 506(e).

**3.16 No Brokers.** No broker, finder, or placement agent is entitled to any brokerage commission, finder's fee, or similar compensation from the Company in connection with the sale of the Notes, and the Company has not paid or agreed to pay transaction-based compensation to any person in connection with that sale.

**3.17 Investment Company.** The Company is not, and after giving effect to the sale of the Notes and the application of the proceeds will not be, required to register as an "investment company" under the Investment Company Act of 1940.

**3.18 Data Privacy and Security.** [[Optional: The Company complies in all material respects with its published privacy policies and applicable data privacy and security laws, and to its Knowledge there has been no material unauthorized access to or breach of personal information or confidential information in its possession or control.]]

**3.19 Qualified Small Business.** [[Optional: To the Company's Knowledge, as of the Initial Closing (a) the Company is a "qualified small business" within the meaning of Section 1202(d) of the Code, and (b) the aggregate gross assets of the Company (as defined in Section 1202(d)(2) of the Code) have not exceeded the amount specified in Section 1202(d)(1) of the Code at any time since its formation. The Company makes no representation that any Purchaser's Note, or the stock issuable on its conversion, will qualify as "qualified small business stock" or as to the holding period for that purpose.]]

**3.20 Foreign Investment and Outbound Matters.** [[Alternative A: The Company does not produce, design, test, manufacture, fabricate, or develop any "critical technologies" within the meaning of 31 C.F.R. § 800.215, and the Company is not a "covered foreign person" within the meaning of 31 C.F.R. § 850.209.]] [[Alternative B: The Company produces, designs, tests, manufactures, fabricates, or develops the "critical technologies" (within the meaning of 31 C.F.R. § 800.215) described in Section 3.20 of the Disclosure Schedule, and the Company is not a "covered foreign person" within the meaning of 31 C.F.R. § 850.209.]] [[Alternative C: Intentionally omitted.]]

> **Drafting note:** Before giving Alternative A or B, have the Company confirm the export classification of its technology under the EAR and ITAR and that it has no subsidiary, and derives no majority of revenue, net income, capital expenditure, or operating expense from any person, in a country of concern engaged in a covered activity. Choose Alternative C if that diligence has not been done.

**3.21 Disclosure.** [[Optional: The Company has made available to each Purchaser all information the Purchaser has reasonably requested in deciding whether to purchase a Note. To the Company's Knowledge, the representations and warranties in this Article 3 (as qualified by the Disclosure Schedule), taken together, do not contain any untrue statement of a material fact or omit to state a material fact necessary to make them, in light of the circumstances under which they were made, not misleading. The Company makes no representation as to any financial projections or forward-looking statements, which were prepared in good faith on assumptions believed reasonable when made, but as to which the Purchasers acknowledge that actual results may differ materially.]]

## ARTICLE 4. REPRESENTATIONS AND WARRANTIES OF THE PURCHASERS

Each Purchaser, severally and only as to itself, represents and warrants to the Company as of the Closing at which it purchases a Note as follows.

**4.1 Authorization.** The Purchaser has full power and authority (and, if an individual, legal capacity) to enter into and perform this Agreement. This Agreement, when executed and delivered by the Purchaser, constitutes its valid and legally binding obligation, enforceable in accordance with its terms, subject to bankruptcy, insolvency, and similar laws affecting creditors' rights and to general principles of equity.

**4.2 Purchase Entirely for Own Account.** The Purchaser is acquiring its Note and the securities issuable on its conversion (together, the "**Securities**") for investment for its own account, not as a nominee or agent, and not with a view to the resale or distribution of any part of them in violation of the Securities Act, and has no present intention of selling, granting any participation in, or otherwise distributing them. The Purchaser was not formed for the specific purpose of acquiring the Securities [[Optional: , or, if it was, each of its equity owners is an accredited investor and the Purchaser has so disclosed in its investor questionnaire]].

**4.3 Disclosure of Information; Independent Investigation.** The Purchaser has had an opportunity to ask questions of, and receive answers from, the Company's management about the terms and conditions of the offering and the Company's business, properties, prospects, and financial condition, and to obtain any additional information it considered necessary to verify the information provided. The Purchaser has relied solely on its own investigation, the representations and warranties of the Company in Article 3, and its own advisers in deciding to invest, and not on any other statement, projection, or information.

**4.4 Restricted Securities; No Public Market.** The Purchaser understands that the Securities have not been registered under the Securities Act or any state securities law, in reliance on exemptions that depend on, among other things, the bona fide nature of the Purchaser's investment intent and the accuracy of its representations; that the Securities are "restricted securities" under the federal securities laws and must be held indefinitely unless registered or an exemption is available; that the Company has no obligation to register them; that no public market exists for the Securities and none may ever exist; and that Rule 144 is available, if at all, only after the applicable holding period and subject to its conditions.

**4.5 Accredited Investor; Verification.**

(a) The Purchaser is an "accredited investor" as defined in Rule 501(a) under the Securities Act, on the basis stated in its investor questionnaire, which is true and complete.

(b) [[Alternative A: Not applicable (Rule 506(b) offering).]] [[Alternative B: The Purchaser has delivered to the Company the verification materials described in Exhibit C (Rule 506(c) Verification) and consents to the Company's review of them and to the Company's reliance on any third-party verification letter delivered on its behalf. If the Purchaser relies on a minimum investment amount for verification, the Purchaser represents that its principal amount is not financed, in whole or in part, by any third party for the specific purpose of making this investment.]]

**4.6 Investment Experience; Risk.** The Purchaser can bear the economic risk of losing its entire investment, has such knowledge and experience in financial and business matters that it is capable of evaluating the merits and risks of the investment, and has not been organized for the purpose of acquiring the Securities. The Purchaser understands that the Company is an early-stage company whose business is subject to substantial risk.

**4.7 Legends.** The Purchaser understands that the Notes and any certificate or book-entry notation for the conversion securities will bear the legend on the Note and any legend required by state securities laws, the Company's bylaws, or agreements to which the Purchaser becomes party.

**4.8 No General Solicitation.** [[Alternative A: The Purchaser did not learn of the investment opportunity through, and is not purchasing the Securities as a result of, any general solicitation or general advertising, including any advertisement, article, notice, or other communication published in any newspaper, magazine, website, or similar media, broadcast over television or radio, or presented at any seminar or meeting whose attendees were invited by general solicitation or general advertising.]] [[Alternative B: Not applicable (Rule 506(c) offering).]]

**4.9 Bad Actor.** If the Purchaser, together with its Affiliates, will beneficially own twenty percent (20%) or more of the Company's outstanding voting equity securities (calculated on the basis of voting power and on an as-converted basis assuming conversion of the Notes at the Valuation Cap), or will receive compensation for soliciting purchasers, then neither the Purchaser nor any person that would be a "covered person" under Rule 506(d) by reason of its relationship with the Purchaser is subject to any Bad Actor Event, except as disclosed to the Company in writing before the Closing. The Purchaser shall notify the Company promptly if this representation ceases to be true while it holds a Note.

**4.10 Foreign Person; Outbound Investment.** The Purchaser [[Alternative A: is not a Foreign Person]] [[Alternative B: is a Foreign Person and has disclosed to the Company in its investor questionnaire its jurisdiction of organization or nationality, its ultimate beneficial owners, and any foreign-government ownership interest]]. The Purchaser is not acquiring, through its Note or the conversion securities, any right described in 31 C.F.R. § 800.211(b), except as the Company has expressly agreed in writing after considering the requirements of 31 C.F.R. Part 800. If the Purchaser is a "U.S. person" as defined in 31 C.F.R. § 850.229, it has made its own determination of whether its investment is subject to 31 C.F.R. Part 850.

**4.11 Sanctions; Anti-Money Laundering.** Neither the Purchaser nor, to its knowledge, any person that controls or owns fifty percent (50%) or more of it, or any beneficial owner of the Purchaser for whom it is acting, is (a) named on, or owned fifty percent (50%) or more by one or more persons named on, the Specially Designated Nationals and Blocked Persons List or any other sanctions list administered by the U.S. Department of the Treasury's Office of Foreign Assets Control or the U.S. Department of State; (b) organized, resident, or located in a country or territory subject to comprehensive U.S. sanctions; or (c) otherwise a person with whom U.S. persons are prohibited from transacting. The funds used to purchase the Note are not derived from unlawful activity.

**4.12 Exculpation Among Purchasers.** The Purchaser is not relying on any other Purchaser, or on any officer, director, employee, partner, agent, or counsel of any other Purchaser, in making its investment decision. No other Purchaser (or any of those persons) is liable to it for any action taken or omitted in connection with the purchase of the Notes.

**4.13 Residence.** The Purchaser's principal residence (if an individual) or principal place of business (if an entity) is located at the address stated on its signature page, which is also the state or country of residence it has identified in its investor questionnaire.

**4.14 Foreign Investors.** If the Purchaser is not a United States person (as defined in Section 7701(a)(30) of the Code), it has satisfied itself as to the full observance of the laws of its jurisdiction in connection with any invitation to subscribe for the Securities, including any foreign legal requirements, governmental or other consents, and formalities, and any tax consequences in that jurisdiction.

**4.15 Tax Advisers.** The Purchaser has reviewed with its own tax advisers the U.S. federal, state, local, and foreign tax consequences of the investment, including the treatment of interest and original issue discount, and the uncertainty of qualified small business stock treatment and holding periods, and is relying solely on those advisers and not on any statement of the Company or its agents.

**4.16 No Brokers.** No broker, finder, or agent engaged by the Purchaser is entitled to any compensation from the Company in connection with the sale of the Notes.

## ARTICLE 5. CONDITIONS TO CLOSING

**5.1 Conditions to the Purchasers' Obligations.** Each Purchaser's obligation to purchase its Note at a Closing is subject to the fulfillment (or waiver by that Purchaser) of the following conditions:

(a) the Company's representations and warranties in Article 3 are true and correct in all material respects (or, if qualified by materiality or Material Adverse Effect, in all respects) as of that Closing;

(b) the Company has performed in all material respects all obligations required to be performed by it at or before that Closing;

(c) all qualifications, permits, and filings required to be obtained or made before the Closing under applicable securities laws for the lawful issuance of the Notes have been obtained or made;

(d) the Company's board of directors has approved the Transaction Documents [[Optional: , and any participation by a director, officer, or Affiliate of either has been approved in accordance with 8 Del. C. § 144]];

(e) [[Optional: at the Initial Closing, Purchasers have agreed to purchase Notes in an aggregate principal amount of at least {{minimum_initial_closing_amount}}]]; and

(f) the Company has delivered the items in Section 2.4(a).

**5.2 Conditions to the Company's Obligations.** The Company's obligation to sell a Note to a Purchaser at a Closing is subject to the fulfillment (or waiver by the Company) of the following conditions:

(a) the Purchaser's representations and warranties in Article 4 are true and correct in all material respects as of that Closing;

(b) the Purchaser has delivered the items in Section 2.4(b), including payment of the purchase price in full; and

(c) the offer and sale of the Note to the Purchaser are exempt from registration under the Securities Act and from qualification or registration under applicable state securities laws, and do not require a declaration or notice to the Committee on Foreign Investment in the United States that has not been made and cleared.

## ARTICLE 6. COVENANTS

**6.1 Use of Proceeds.** The Company shall use the proceeds of the Notes as provided in Section 2.5.

**6.2 Authorization and Reservation of Conversion Securities.** The Company shall comply with Section 3.9 of the Notes, including by keeping authorized and reserved sufficient Common Stock for conversion of the Notes into Common Stock and by taking all corporate action necessary, at or before the initial closing of a Qualified Financing, to authorize a sufficient number of shares of each series of Preferred Stock into which the Notes will convert.

**6.3 Notices.** The Company shall give the holders of Notes the notices of Qualified Financings, Changes of Control, maturity, and Events of Default required by the Notes.

**6.4 Securities Filings.** The Company shall file a notice of sales on Form D with the SEC no later than fifteen (15) calendar days after the first sale of Notes (or the next business day if that day is a Saturday, Sunday, or holiday), shall file any required amendments (including an annual amendment if the offering continues more than one year after the last filing), and shall timely make all notice filings and pay all fees required by the securities laws of each state in which Notes are sold. The Company shall provide copies of those filings to any Purchaser on request.

**6.5 Qualified Small Business Stock Information.** [[Optional: For so long as any Purchaser holds a Note or securities issued on its conversion, the Company shall use commercially reasonable efforts to provide, within thirty (30) days after a written request, information reasonably necessary for the Purchaser to determine whether those securities are "qualified small business stock" under Section 1202 of the Code, including whether the Company's aggregate gross assets exceeded the limit in Section 1202(d) at the relevant times, and shall comply with any reporting requirements applicable to it under Section 1202(d)(1)(C) of the Code and the regulations under it.]]

**6.6 Information Rights.** [[Optional: The Company shall deliver to each Purchaser holding Notes with an aggregate outstanding principal amount of at least {{major_purchaser_threshold}} (together with its Affiliates) (a) within {{annual_info_days}} days after the end of each fiscal year, an unaudited balance sheet as of the end of that year and unaudited statements of income and cash flows for that year; and (b) within {{quarterly_info_days}} days after the end of each of the first three quarters of each fiscal year, unaudited quarterly financial statements; subject to the confidentiality obligations in Section 6.8 and to the limitations in Section 6.9. These rights terminate on conversion or repayment of the Purchaser's Notes.]]

**6.7 Most-Favored-Nation.** [[Optional: If, before the earlier of the conversion of the Notes and the Maturity Date, the Company issues any convertible promissory notes, simple agreements for future equity, or other convertible securities for capital-raising purposes (other than securities issued under this Agreement and other than securities excluded from the definition of "Subsequent Convertible Securities" in the Company's form of SAFE side letter) on economic terms more favorable to the holder than those of the Notes, the Company shall promptly notify the holders of Notes, and the Majority Holders may elect, within fifteen (15) days after the notice, to amend all of the Notes to incorporate those more favorable economic terms.]]

**6.8 Confidentiality.** Each Purchaser shall keep confidential, and use only for monitoring its investment, any confidential information it receives from the Company, subject to customary exceptions for information that is or becomes public through no breach, information already known or independently developed or received from a third party without restriction, disclosures to its Affiliates, partners, advisers, and prospective permitted transferees bound by confidentiality, customary summary disclosures to its existing and prospective limited partners, and disclosures required by law (after notice to the Company where lawful).

**6.9 Foreign Persons.** The Company shall not grant to any Purchaser that is a Foreign Person any right described in 31 C.F.R. § 800.211(b) (including access to material nonpublic technical information, board membership or observer rights, or involvement in substantive decision-making) unless the Company has first determined, with the advice of counsel, whether a declaration or notice to the Committee on Foreign Investment in the United States is required or advisable and has complied with any requirement.

**6.10 Market Stand-Off.** Each Purchaser agrees that, in connection with the Company's initial underwritten public offering under the Securities Act, it shall not sell, transfer, or otherwise dispose of any securities of the Company held by it (other than securities purchased in or after that offering) for the period requested by the managing underwriters, not exceeding one hundred eighty (180) days after the effective date of the registration statement, on terms no less favorable to the Purchaser than those applicable to the Company's officers and directors and holders of one percent (1%) or more of its outstanding stock, all of whom must be similarly bound.

**6.11 Further Assurances.** Each party shall execute and deliver further documents and take further actions reasonably necessary to carry out the Transaction Documents, including, for each Purchaser, the documents described in Section 3.5(a) of the Notes on conversion.

## ARTICLE 7. AMENDMENT AND WAIVER

**7.1 Majority Holder Consent.** Except as provided in Section 7.2, any term of this Agreement or of the Notes may be amended or waived (either generally or in a particular instance, and either retroactively or prospectively) only with the written consent of the Company and the Majority Holders (or, before the Initial Closing, the Purchasers who have agreed to purchase a majority of the aggregate principal amount to be sold at the Initial Closing). Any amendment or waiver so effected binds the Company, every Purchaser, and every holder of a Note, whether or not that person consented.

**7.2 Protections Against Disproportionate Treatment.** Notwithstanding Section 7.1:

(a) any amendment or waiver that would reduce the principal amount of a Note, forgive accrued interest, change the currency of payment, or impair a holder's right to receive amounts that have become due or securities to which it has become entitled requires the consent of each holder adversely affected;

(b) [[Optional: any amendment that reduces the interest rate on the Notes requires the consent of each holder;]]

(c) any amendment or waiver that by its terms adversely affects the rights or obligations of a Purchaser or holder in a manner materially and disproportionately different from its effect on the other Purchasers or holders of the same class (taking into account differences in principal amount and issue date) requires that Purchaser's or holder's consent;

(d) any amendment that increases the Maximum Amount or extends the deadline for Additional Closings requires the consent of the Majority Holders and, if it changes the economic terms of the Notes to be sold, applies only to Notes sold after the amendment; and

(e) any amendment of this Article 7 or of the definition of "Majority Holders" requires the consent of each holder.

**7.3 Process.** The Company shall solicit the consent of all holders of Notes for any amendment or waiver under Section 7.1 and shall give prompt written notice of any amendment or waiver to each holder that did not consent. A Purchaser may waive any of its own rights under this Agreement, and any condition for its own benefit, without the consent of any other Purchaser.

## ARTICLE 8. SUBORDINATION

[[Optional: Each Purchaser acknowledges that the Notes are subordinated to Senior Indebtedness to the extent provided in Article 5 of the Notes and agrees to execute and deliver any subordination or intercreditor agreement described in Section 5.2 of the Notes. The execution of such an agreement by the Majority Holders binds all holders as provided in that Section.]]

> **Drafting note:** If the Notes omit Article 5 (subordination), delete this Article 8 and renumber, and delete the cross-reference in the legend of the Note.

## ARTICLE 9. GENERAL PROVISIONS

**9.1 Survival.** The representations and warranties in this Agreement survive each Closing for {{rep_survival_months}} months, and the covenants survive in accordance with their terms. No claim for breach of a representation or warranty may be brought after the end of the survival period unless notice of the claim, describing it in reasonable detail, was given before then.

**9.2 Successors and Assigns.** This Agreement binds and benefits the parties and their respective successors and permitted assigns. No Purchaser may assign its rights under this Agreement except together with a Note transferred in compliance with Section 8 of the Notes. The Company may not assign this Agreement without the consent of the Majority Holders, except to a successor in a Change of Control that assumes the Notes.

**9.3 Governing Law.** This Agreement and all claims arising out of or relating to it are governed by the laws of the State of {{governing_law_state}}, without regard to conflict-of-laws principles that would require the application of the laws of another jurisdiction.

**9.4 Forum.** Each party irrevocably submits to the exclusive jurisdiction of the {{forum}} (or, if that court lacks subject-matter jurisdiction, the Superior Court of the State of Delaware or the United States District Court for the District of Delaware) for any action arising out of or relating to the Transaction Documents, waives any objection to venue there, and agrees that service of process may be made in the manner provided for notices in Section 9.6 or in any other manner permitted by law.

**9.5 Waiver of Jury Trial.** TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, EACH PARTY WAIVES ITS RIGHT TO A JURY TRIAL IN ANY ACTION ARISING OUT OF OR RELATING TO THE TRANSACTION DOCUMENTS OR THE TRANSACTIONS THEY CONTEMPLATE.

**9.6 Notices.** All notices and other communications under the Transaction Documents shall be in writing and are deemed given (a) when delivered personally; (b) one (1) Business Day after deposit with a nationally recognized overnight courier, with delivery confirmation; (c) when sent by email, if sent before 5:00 p.m. in the recipient's time zone on a Business Day (and otherwise on the next Business Day), provided that no automated notice of delivery failure is received by the sender; or (d) three (3) Business Days after mailing by certified or registered mail, return receipt requested, postage prepaid; in each case addressed to the Company at {{company_address}}, email {{company_notice_email}}, Attention: {{signatory_title}}, and to a Purchaser at the address and email on its signature page or the Schedule of Purchasers, or to another address designated by notice. Each Purchaser consents to the delivery of notices, information, and stockholder communications by electronic transmission in accordance with 8 Del. C. § 232, to the extent applicable.

**9.7 Entire Agreement.** The Transaction Documents, together with the Schedule of Purchasers, the Disclosure Schedule, and the investor questionnaires, constitute the entire agreement among the parties about their subject matter and supersede all prior and contemporaneous agreements, term sheets, and understandings about it.

**9.8 Severability.** If any provision of this Agreement is held invalid or unenforceable, that provision shall be enforced to the maximum extent permitted and the remaining provisions remain in full force.

**9.9 Counterparts; Electronic Signatures.** This Agreement may be executed in counterparts (including by counterpart signature pages delivered at Additional Closings), each of which is an original and all of which constitute one instrument. Signatures delivered by email in portable document format or through an electronic signature service complying with the U.S. federal ESIGN Act of 2000 (15 U.S.C. § 7001 et seq.) or the Delaware Uniform Electronic Transactions Act (6 Del. C. ch. 12A) are effective as originals.

**9.10 Expenses.** Each party shall bear its own fees and expenses in connection with the Transaction Documents[[Optional: , except that the Company shall reimburse {{lead_purchaser_name}} at the Initial Closing for the reasonable and documented fees and expenses of one counsel, not to exceed {{lead_counsel_fee_cap}}]]. If any action is brought to enforce the Transaction Documents, the prevailing party is entitled to its reasonable attorneys' fees, costs, and expenses.

**9.11 Finder's Fees.** Each party shall indemnify and hold harmless the other parties from any liability for any commission or compensation in the nature of a finder's or broker's fee arising out of the transactions contemplated by this Agreement for which the indemnifying party (or any of its officers, employees, or representatives) is responsible.

**9.12 Delays or Omissions.** No delay or omission in exercising any right, power, or remedy under the Transaction Documents impairs it or is a waiver of any breach or default, and no waiver of a single breach or default is a waiver of any other.

**9.13 Specific Performance.** The parties agree that irreparable damage would occur if the Company failed to issue securities on conversion of the Notes as required, and each holder is entitled to specific performance of that obligation, without posting a bond, in addition to any other remedy.

**9.14 Aggregation.** All Notes held or acquired by Affiliated persons are aggregated for purposes of determining the availability of any rights under this Agreement that depend on principal amount.

**9.15 Further Assurances.** Section 6.11 applies.

**9.16 Construction.** The parties negotiated this Agreement with the advice of counsel, and no rule of construction against the drafter applies.

*(Signature pages follow.)*

---

IN WITNESS WHEREOF, the parties have executed this Convertible Note Purchase Agreement as of the date first written above.

**COMPANY:**

{{company_name}}

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

Address: {{company_address}}
Email: {{company_notice_email}}

---

**PURCHASER COUNTERPART SIGNATURE PAGE**

By signing below, the undersigned agrees to purchase a Note in the principal amount stated below and to become a party to the Convertible Note Purchase Agreement of {{company_name}} dated {{effective_date}} as a "Purchaser."

Principal amount of Note: {{purchase_amount}}

[[Alternative A: **Entity Purchaser**

{{investor_name}}, {{investor_entity_type}}

By: ______________________________
Name: {{investor_signatory_name}}
Title: {{investor_signatory_title}}]]

[[Alternative B: **Individual Purchaser**

______________________________
{{investor_name}}]]

Address: {{investor_address}}
Email: {{investor_email}}
Tax form delivered: {{investor_tax_id_form}}

ACCEPTED as of {{closing_date}}:

{{company_name}}

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

---

## Schedule A: Schedule of Purchasers

| Note No. | Purchaser | Address and email | State or country of residence | Principal amount | Closing date |
|---|---|---|---|---|---|
| {{note_number}} | {{investor_name}} | {{investor_address}}; {{investor_email}} | {{investor_residence_state}} | {{purchase_amount}} | {{closing_date}} |
| | **Total** | | | {{aggregate_principal}} | |

> **Drafting note:** Add one row per Note. The total may not exceed {{maximum_amount}} or the maximum approved by the board. Update and recirculate after each Additional Closing (Section 2.3(c)).

## Exhibit A: Form of Convertible Promissory Note

The form of Note is the skill's [convertible-promissory-note](convertible-promissory-note.md) template, completed with the economic terms in Recital B and identical for every Purchaser except as to holder, principal amount, note number, and issue date.

## Exhibit B: Disclosure Schedule

The Company's Disclosure Schedule, delivered at the Initial Closing and supplemented at each Additional Closing, organized by Section number of Article 3:

| Section | Disclosure |
|---|---|
| 3.2(b) | Promised but ungranted equity awards: {{promised_awards_description}} |
| 3.2(c) | Other outstanding rights (SAFEs, notes, warrants), with holder, amount, cap, discount, and date: {{other_convertibles_detail}} |
| 3.2(d) | Acceleration provisions: {{acceleration_description}} |
| 3.7 | Litigation: {{litigation_description}} |
| 3.13 | Related-party transactions: {{related_party_description}} |
| Other | {{other_disclosures}} |

## Exhibit C: Rule 506(c) Verification

[[Optional: Use only if Section 3.14 Alternative B (Rule 506(c)) applies. Each Purchaser shall deliver one of the following, as described in the investor questionnaire: (1) a written confirmation from a registered broker-dealer, an SEC-registered investment adviser, a licensed attorney, or a certified public accountant, dated within three (3) months before the Closing, that it has taken reasonable steps to verify, and has determined, that the Purchaser is an accredited investor; (2) for natural persons qualifying on income, copies of IRS forms reporting income for the two most recent years and a written representation of expected current-year income; (3) for natural persons qualifying on net worth, asset statements dated within three (3) months and a consumer report, with a representation that all liabilities have been disclosed; (4) a written representation, if the Company verified the Purchaser within the prior five (5) years; or (5) if the Company so permits, a commitment to purchase a Note in a principal amount of at least $200,000 (natural persons) or $1,000,000 (entities, or as otherwise provided for entities owned by accredited investors), with written representations that the Purchaser is accredited and that the investment is not financed by a third party for the specific purpose of the investment, and with no actual knowledge to the contrary by the Company.]]
