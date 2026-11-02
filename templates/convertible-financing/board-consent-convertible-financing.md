---
id: board-consent-convertible-financing
title: Board Consent Approving a SAFE or Convertible Note Financing
category: convertible-financing
stage: convertible
signers: [Each member of the Board of Directors]
authorities:
  - "8 Del. C. § 141(f) (action by unanimous written consent or electronic transmission; future-effective consents)"
  - "8 Del. C. § 122(13) (power to borrow and issue notes)"
  - "8 Del. C. §§ 152, 153 (consideration for stock), § 157 (rights and options; delegation under § 157(c)), § 161 (issuance of authorized shares)"
  - "8 Del. C. §§ 151, 242 (authorizing preferred stock; charter amendment)"
  - "8 Del. C. § 144 (interested director, officer, and controlling stockholder transactions, as amended by SB 21, 2025)"
  - "17 C.F.R. §§ 230.503, 230.506 (Form D within 15 calendar days after first sale; Rule 506(b)/(c))"
  - "Securities Act § 18(b)(4)(F); Cal. Corp. Code § 25102.1(d) (state notice filings)"
use_when: The board is approving the issuance of SAFEs or convertible promissory notes (with or without side letters) up to a maximum amount within a closing window.
do_not_use_when: The company is approving a priced preferred round (use the priced-financing board and stockholder consents) or a single SAFE to an insider that requires a separate interested-director process (adapt Section 9 or use a stand-alone § 144 approval).
related: [safe-guide, safe-side-letter, convertible-note-purchase-agreement, convertible-promissory-note, investor-questionnaire, convertible-financing-checklist]
sources:
  - name: "8 Del. C. ch. 1, subch. IV and V (§§ 141, 144, 151, 152, 153, 157, 161) — official Delaware Code (text of §§ 144, 152, 157 reviewed November 2, 2026)"
    url: https://delcode.delaware.gov/title8/c001/index.html
  - name: "Rutledge v. Clearway Energy Group LLC (Del. Feb. 27, 2026) — upholding the 2025 § 144 amendments (as reported by Delaware practitioners)"
    url: https://www.rlf.com/delaware-supreme-court-upholds-constitutionality-of-section-144s-statutory-safe-harbor-procedures-for-conflict-of-interest-transactions/
  - name: "Y Combinator — SAFE documents page and User Guide (board approval required before issuing SAFEs)"
    url: https://www.ycombinator.com/documents
  - name: "17 C.F.R. § 230.503 (Form D) — eCFR; SEC EDGAR Next fact sheet (account administrators)"
    url: https://www.sec.gov/files/33-11313-fact-sheet.pdf
  - name: "Series Seed documents (CC0 1.0) — board consent structure (reference)"
    url: https://www.seriesseed.com
last_verified: 2026-11-02
---

# Board Consent Approving a SAFE or Convertible Note Financing

## About this template

### 1. What this document does and where it sits

This unanimous written consent approves a convertible financing: either SAFEs on the official Y Combinator forms (Alternative A) or convertible promissory notes under a note purchase agreement (Alternative B). It fixes the maximum aggregate amount, the permitted economic terms, the approved forms, the side-letter parameters, the closing window, the officers authorized to sign, the securities filings, the share reservation approach, and the treatment of any insider participation. Sign it **before** the first SAFE or note is signed or funded; YC's user guide and FAQ state that the board must formally approve SAFEs before they are issued.

### 2. Statutory requirements

- **Written consent.** Under 8 Del. C. § 141(f), the board may act without a meeting if all directors consent in writing or by electronic transmission. A consent may be made effective at a future time (including on the happening of an event) no more than 60 days after it is given. This form states a definite effective date.
- **Authority for the instruments.** Notes: 8 Del. C. § 122(13). SAFEs and the conversion feature of notes are rights to acquire stock; under § 157(b) the board sets the terms of rights by resolution. If officers will choose the investors and individual amounts, § 157(c) requires the resolution to fix (i) the maximum number of shares issuable on exercise of the rights, (ii) the time periods during which the rights may be issued and the shares issued on exercise, and (iii) the minimum consideration for the rights and for the shares; § 157(d) lets those terms depend on facts ascertainable outside the resolution (such as capitalization at conversion), but not on a determination by the delegate itself. Section 6 does this. Shares issued on conversion must be issued for consideration the board determines adequate (§§ 152, 153) and at not less than par value.
- **Reservation, and why preferred cannot be reserved now.** A corporation may issue only shares its certificate of incorporation authorizes (§§ 151(a), 161). Most startups authorize only common stock at formation (the shared variable `authorized_preferred_shares` is usually 0), and the SAFE or note will convert into a series of preferred whose rights, price, and share count are set in the next priced round. That series does not exist and cannot be reserved; it is created later by an amended and restated certificate of incorporation adopted by the board and stockholders under § 242 (or, if the charter authorizes blank-check preferred, by a certificate of designations under § 151(g)). The consent therefore (a) reserves common stock where a conversion into common is possible (notes at maturity or on a change of control), and (b) directs the officers to propose the charter amendment at the Equity Financing or Qualified Financing.
- **Insider participation (8 Del. C. § 144, as amended March 25, 2025).** If a director, an officer, or an entity in which one has a financial interest buys SAFEs or notes, the transaction is protected from equitable relief and damages claims against directors and officers if (1) the material facts are disclosed to or known by the board and a majority of the **disinterested** directors approves in good faith and without gross negligence (if a majority of the directors are not disinterested, a committee of **two or more** disinterested directors must approve or recommend); or (2) a majority of the votes cast by disinterested stockholders approves or ratifies; or (3) the transaction is fair to the corporation and its stockholders (§ 144(a)). A transaction with a **controlling stockholder** must instead use the § 144(b) procedures (a committee of two or more disinterested directors with negotiating authority, or a vote of disinterested stockholders conditioned up front, or fairness). The Delaware Supreme Court upheld these amendments in *Rutledge v. Clearway Energy Group LLC* (Feb. 27, 2026).
  - *Two-director boards:* if one of two directors is investing, the remaining disinterested director is not a majority of the board, and a two-member disinterested committee is impossible; use stockholder approval under § 144(a)(2) or rely on fairness, documented by offering the insider identical terms to unaffiliated investors.
  - *Founder-controlled companies:* founders who together hold a majority of voting power may be a "control group." If they invest, consider the § 144(b) route.

> **Verify:** Confirm the current statutory definitions of "disinterested director," "controlling stockholder," and "control group" in 8 Del. C. § 144 before relying on a safe harbor for an insider's participation.

- **Existing preferred stock and investor agreements.** If any preferred is outstanding, check the charter's protective provisions (many require preferred-holder consent to issue senior or pari passu securities or debt above a threshold) and any investors' rights agreement (pre-emptive or participation rights, information rights).
- **Securities filings.** The consent authorizes the Form D (due 15 calendar days after the first sale), state notices (e.g., California § 25102.1(d): 15 days after the first California sale, $300), and EDGAR access (under EDGAR Next, each filer must authorize at least two account administrators, or one if the filer is an individual or single-member company, using individual Login.gov credentials).

### 3. Key business decisions

| Decision | Common choices | Notes |
|---|---|---|
| Instrument | SAFE (default); note | Alternatives A and B |
| Maximum amount | Target raise plus 10%–25% headroom | Above the maximum, a new board approval is needed |
| Terms the officers may agree | Exact cap and discount, or a band (e.g., post-money cap of $8,000,000–$10,000,000) | Bands give flexibility but complicate § 157(c) and pre-/post-money modeling |
| Side letters | None; YC pro rata letter only; the skill's side letter above a threshold | Set the threshold and maximum aggregate participation rights |
| Closing window | 90–180 days | Long windows create continuing-offering issues (Form D annual amendment) |
| Insiders | Excluded; permitted with § 144 approval | Section 9 |
| Exemption | Rule 506(b); Rule 506(c) if general solicitation | Section 10 |

### 4. Common mistakes this form avoids

1. Officers sign SAFEs before board approval, or above the approved maximum.
2. Resolutions that purport to "reserve" preferred stock that is not authorized.
3. No authority to file Form ID or Form D, so the 15-day deadline is missed.
4. Insider participation approved by a conflicted board without disclosure.
5. Side letters granted without limits, overcommitting the next round.
6. No closing window, leaving a stale approval open indefinitely.

### 5. Deadlines triggered

| Trigger | Deadline |
|---|---|
| Effective date of consent | Before the first SAFE or note is signed or funded |
| First sale | Form D within 15 calendar days (next business day if weekend or holiday) |
| First sale in each state | State notice deadline (commonly 15 days) |
| End of closing window | `{{closing_window_end_date}}` |
| Equity Financing / Qualified Financing | Charter amendment authorizing the conversion series before or at the initial closing |

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | Shared |
| `{{effective_date}}` | Effective date of the consent | February 20, 2027 | Shared; definite date |
| `{{board_size}}` | Authorized number of directors | 2 | Shared |
| `{{offering_name}}` | Name for the financing | 2027 Seed SAFE Financing | |
| `{{board_max_amount}}` | Maximum aggregate Purchase Amount or principal | $2,000,000 | |
| `{{valuation_cap}}` | Post-money cap (SAFEs) or note cap | $10,000,000 | Shared |
| `{{valuation_cap_minimum}}` | Lowest cap officers may accept (if a band) | $8,000,000 | Optional |
| `{{discount_rate}}` | Discount | 20% discount | Shared; state as the discount |
| `{{minimum_investment}}` | Minimum check size | $25,000 | Optional |
| `{{closing_window_end_date}}` | Last date to sign and fund | May 31, 2027 | |
| `{{side_letter_threshold}}` | Minimum investment to receive a side letter | $250,000 | |
| `{{max_participation_percent}}` | Cap on aggregate participation rights in the next round, as % of new money | 25% | Optional |
| `{{max_conversion_shares}}` | Maximum shares issuable on conversion (§ 157(c)) | 4,000,000 | Alternative A of Section 6.1 |
| `{{par_value}}` | Par value | $0.00001 | Shared |
| `{{interest_rate}}`, `{{maturity_date}}`, `{{qualified_financing_amount}}` | Note terms | 6%; January 15, 2029; $2,000,000 | Alternative B |
| `{{authorized_common_shares}}`, `{{common_outstanding}}`, `{{common_reserved_plan}}` | Share counts for the reservation analysis | 10,000,000; 8,000,000; 1,500,000 | |
| `{{common_reserved_for_notes}}` | Common reserved for note conversions | 400,000 | Alternative B |
| `{{authorized_officers}}` | Officers authorized to sign | Chief Executive Officer; President; Secretary | |
| `{{interested_party_name}}`, `{{interested_party_relationship}}`, `{{interested_party_amount}}` | Insider investor details | Jordan Lee (director); $50,000 | Section 9 |
| `{{disinterested_director_names}}` | Directors approving under § 144(a)(1) | | Section 9 |
| `{{use_of_proceeds}}` | Approved use of proceeds | product development and general working capital | |
| `{{edgar_account_administrators}}` | EDGAR Next account administrators | Alex Rivera; Jordan Lee | At least two (one for single-member filers) |
| `{{company_counsel}}` | Counsel authorized to make filings | | Optional |
| `{{director_name_1}}`, `{{director_name_2}}`, `{{director_name_3}}` | Each director (one signature block each) | Alex Rivera; Jordan Lee | Add or delete blocks to match the board |
| `{{director_signature_date_1}}`, `{{director_signature_date_2}}`, `{{director_signature_date_3}}` | Date each director signs | February 20, 2027 | Within 60 days before the effective date |
| `{{authorized_preferred_shares}}`, `{{preferred_outstanding_description}}` | Preferred authorized and outstanding | 0 | Shared; Alternative B of the third recital |
| `{{interested_party_involvement}}` | Insider's role in initiating or negotiating terms | None; terms set by the CEO before the insider's participation was proposed | Exhibit B |
| `{{yc_cap_form_version}}`, `{{yc_discount_form_version}}`, `{{yc_mfn_form_version}}`, `{{yc_side_letter_version}}`, `{{yc_form_download_date}}` | YC form versions approved and download date | 1.2; 1.2; 1.3; 1.0; February 15, 2027 | Verify on download |
| `{{yc_discount_rate}}` | YC "Discount Rate" (100 minus discount) | 80% | |
| `{{mfn_cutoff_date}}` | Last date MFN SAFEs may be issued | March 31, 2027 | |
| `{{cap_capitalization_alternative}}` | Note cap basis selected (A–D) | A | Notes only |
| `{{coc_premium_multiple}}` | Note change-of-control repayment multiple | 2 | Notes only |

## Form

---

# {{company_name}}

## ACTION BY UNANIMOUS WRITTEN CONSENT OF THE BOARD OF DIRECTORS

**Effective Date: {{effective_date}}**

The undersigned, constituting all of the members of the Board of Directors (the "**Board**") of {{company_name}}, a Delaware corporation (the "**Company**"), acting under Section 141(f) of the Delaware General Corporation Law (the "**DGCL**") and the Company's Bylaws, hereby adopt the following resolutions by written consent, effective as of the Effective Date stated above, with the same force and effect as if duly adopted at a meeting of the Board at which a quorum was present and acting throughout.

### 1. Approval of the Financing

WHEREAS, the Board has determined that it is advisable and in the best interests of the Company and its stockholders to raise capital for the Company's operations through the issuance of [[Alternative A: simple agreements for future equity]] [[Alternative B: convertible promissory notes]] in a financing to be known as the {{offering_name}} (the "**Financing**");

WHEREAS, the Board has reviewed the terms of the Financing described in these resolutions and in Exhibit A, has had the opportunity to ask questions of management and counsel, and has considered the dilutive effect of the Financing on the Company's stockholders, including the conversion modeling presented to it; and

WHEREAS, the Company's Certificate of Incorporation currently authorizes {{authorized_common_shares}} shares of Common Stock, par value {{par_value}} per share (the "**Common Stock**"), of which {{common_outstanding}} shares are issued and outstanding and {{common_reserved_plan}} shares are reserved under the Company's equity incentive plan, and [[Alternative A: does not authorize any Preferred Stock]] [[Alternative B: authorizes {{authorized_preferred_shares}} shares of Preferred Stock, of which {{preferred_outstanding_description}}]].

NOW, THEREFORE, BE IT RESOLVED, that the Financing is hereby authorized and approved on the terms set forth in these resolutions;

[[Alternative A: **SAFE Financing**

RESOLVED FURTHER, that the Company is authorized to issue and sell simple agreements for future equity (each, a "**SAFE**") in the forms published by Y Combinator at https://www.ycombinator.com/documents identified in Exhibit A (the "**Approved SAFE Forms**"), completed only as to their blanks and bracketed terms (and, where an investor requires two signatories, with an additional signature block), and containing the economic terms permitted by Exhibit A; and that no officer is authorized to issue a SAFE that otherwise modifies an Approved SAFE Form without the further approval of the Board;]]

[[Alternative B: **Note Financing**

RESOLVED FURTHER, that the Company is authorized to enter into a Convertible Note Purchase Agreement substantially in the form presented to the Board (the "**Purchase Agreement**") and to issue and sell thereunder convertible promissory notes substantially in the form attached to the Purchase Agreement (each, a "**Note**"), bearing simple interest at {{interest_rate}} per annum, maturing on {{maturity_date}}, and converting on the terms set forth in Exhibit A, including automatic conversion in a Qualified Financing of at least {{qualified_financing_amount}}; and that the Purchase Agreement and the form of Note are hereby approved, with such changes as the Authorized Officer executing them approves as not materially adverse to the Company, that approval to be conclusively evidenced by that officer's execution;]]

### 2. Maximum Amount; Minimum Investment

RESOLVED FURTHER, that the aggregate [[Alternative A: Purchase Amount of all SAFEs]] [[Alternative B: principal amount of all Notes]] issued in the Financing shall not exceed {{board_max_amount}} (the "**Maximum Amount**"), and that [[Optional: no single investment shall be less than {{minimum_investment}} without the approval of the Chief Executive Officer, and]] any issuance in excess of the Maximum Amount shall require further approval of the Board;

### 3. Economic Terms

RESOLVED FURTHER, that each [[Alternative A: SAFE]] [[Alternative B: Note]] shall have the economic terms set forth in Exhibit A, and that [[Alternative A: the Authorized Officers may agree to a valuation cap no lower than {{valuation_cap_minimum}} and a discount no greater than {{discount_rate}}]] [[Alternative B: the Authorized Officers may not agree to any economic term different from those in Exhibit A]];

### 4. Side Letters

RESOLVED FURTHER, that the Authorized Officers are authorized to enter into [[Alternative A: the Pro Rata Side Letter published by Y Combinator, unmodified,]] [[Alternative B: side letters substantially in the form of the Company's SAFE Investor Side Letter presented to the Board,]] [[Alternative C: participation, information, and most-favored-nation rights substantially as provided in the Purchase Agreement,]] only with investors whose investment in the Financing (aggregated with their Affiliates) is at least {{side_letter_threshold}}, provided that [[Optional: the aggregate participation rights granted in the Financing shall not entitle holders to purchase, in the Company's next priced equity financing, more than {{max_participation_percent}} of the new money to be raised in that financing (as reasonably estimated by the Chief Executive Officer), and]] no side letter shall amend or purport to amend the economic or conversion terms of any SAFE or Note;

### 5. Investors; Exemption

RESOLVED FURTHER, that the [[Alternative A: SAFEs]] [[Alternative B: Notes]] shall be offered and sold only to persons that the Authorized Officers reasonably believe are "accredited investors" as defined in Rule 501(a) of Regulation D under the Securities Act of 1933, as amended (the "**Securities Act**"), each of whom shall complete the Company's investor questionnaire before purchasing, and that the Financing shall be conducted in reliance on [[Alternative A: Rule 506(b) of Regulation D, without any general solicitation or general advertising]] [[Alternative B: Rule 506(c) of Regulation D, and the Authorized Officers shall take reasonable steps to verify the accredited investor status of each purchaser as required by Rule 506(c)(2)(ii)]];

RESOLVED FURTHER, that the Authorized Officers shall not pay, or agree to pay, any commission, finder's fee, or other transaction-based compensation in connection with the Financing to any person that is not a broker-dealer registered under the Securities Exchange Act of 1934 and applicable state law, without the further approval of the Board;

### 6. DGCL Section 157 Parameters; Consideration

RESOLVED FURTHER, that, for purposes of Sections 152, 153, and 157 of the DGCL and to the extent the Authorized Officers determine the purchasers and individual amounts of the [[Alternative A: SAFEs]] [[Alternative B: Notes]] under these resolutions:

(a) the maximum number of shares of capital stock issuable on conversion of all [[Alternative A: SAFEs]] [[Alternative B: Notes]] issued in the Financing is [[Alternative A: {{max_conversion_shares}} shares]] [[Alternative B: the number of shares equal to the Maximum Amount (plus, for Notes, accrued interest) divided by the lowest conversion price permitted by Exhibit A, as determined from the Company's capitalization at the time of conversion in the manner set forth in the applicable instrument]];

(b) the [[Alternative A: SAFEs]] [[Alternative B: Notes]] may be issued only on or before {{closing_window_end_date}} (the "**Closing Window**"), and the shares issuable on their conversion may be issued at any time while the instruments remain outstanding in accordance with their terms;

(c) the minimum consideration for each [[Alternative A: SAFE]] [[Alternative B: Note]] is the cash purchase price or principal amount stated in the instrument[[Optional: , which shall be not less than {{minimum_investment}}]], and the minimum consideration for each share issued on conversion is the applicable conversion price determined under the instrument, which the Board hereby determines to be adequate and which shall in no event be less than the par value of the shares; and

(d) no Authorized Officer may issue a [[Alternative A: SAFE]] [[Alternative B: Note]] to himself or herself or to an entity he or she controls except as approved under Section 9 of these resolutions;

RESOLVED FURTHER, that the shares of capital stock issued on conversion of the [[Alternative A: SAFEs]] [[Alternative B: Notes]] in accordance with their terms, upon such conversion and the satisfaction of the conditions in the instrument, shall be duly authorized, validly issued, fully paid, and non-assessable, the cancellation of the converted instrument (including, for Notes, the principal and accrued interest converted) being adequate consideration for those shares;

### 7. Closing Window

RESOLVED FURTHER, that the Authorized Officers may hold one or more closings of the Financing during the Closing Window, provided that each [[Alternative A: SAFE shall be countersigned by the Company only after the Company has received the Purchase Amount]] [[Alternative B: Note shall be issued only against receipt of its principal amount]], and that any closing after the Closing Window shall require further approval of the Board;

### 8. Authorization and Reservation of Shares

[[Alternative A: **SAFEs**

RESOLVED FURTHER, that the Board acknowledges that the SAFEs convert into shares of a series of Preferred Stock to be designated in connection with the Company's next priced equity financing, that such series is not currently authorized by the Certificate of Incorporation and therefore cannot be reserved for issuance at this time, and that, in connection with the next Equity Financing (as defined in the SAFEs), the officers of the Company are directed to prepare, and present to the Board and the stockholders for approval under Section 242 of the DGCL, an amended and restated Certificate of Incorporation authorizing a sufficient number of shares of each series of Preferred Stock (including any series issued to SAFE holders with price-based terms determined by their conversion prices) into which the SAFEs will convert, and a sufficient number of shares of Common Stock for issuance on conversion of that Preferred Stock;]]

[[Alternative B: **Notes**

RESOLVED FURTHER, that {{common_reserved_for_notes}} shares of Common Stock, being a number the Board has determined to be sufficient for the conversion of the Maximum Amount of Notes (with accrued interest through the maturity date) into Common Stock at maturity or on a change of control in accordance with the Notes, are hereby reserved for issuance on conversion of the Notes, and the officers are directed to take such action as is necessary to increase the authorized Common Stock if that reservation becomes insufficient;

RESOLVED FURTHER, that the Board acknowledges that the Notes may convert into shares of a series of Preferred Stock to be designated in connection with a Qualified Financing, that such series is not currently authorized and therefore cannot be reserved for issuance at this time, and that the officers are directed to prepare and present to the Board and the stockholders for approval under Section 242 of the DGCL, at or before the initial closing of a Qualified Financing, an amended and restated Certificate of Incorporation authorizing a sufficient number of shares of each series into which the Notes will convert and of Common Stock issuable on conversion of that series;]]

### 9. Interested Directors, Officers, and Stockholders

[[Alternative A: RESOLVED FURTHER, that no director or officer of the Company, and no entity in which any of them has a material financial interest, shall purchase any instrument issued in the Financing without the further approval of the Board in accordance with Section 144 of the DGCL;]]

[[Alternative B: WHEREAS, {{interested_party_name}}, {{interested_party_relationship}}, proposes to purchase an instrument issued in the Financing in the amount of {{interested_party_amount}} on the same terms as unaffiliated investors (the "**Insider Purchase**"); the material facts as to that person's relationship and interest and as to the Insider Purchase, including that person's involvement in its initiation and negotiation, have been disclosed to the Board as set forth in Exhibit B; and {{disinterested_director_names}}, being all of the directors who are disinterested with respect to the Insider Purchase (and, where Section 144(a)(1) of the DGCL so requires, constituting a committee of the Board of two or more disinterested directors designated for this purpose), have reviewed the Insider Purchase;

RESOLVED FURTHER, that the Insider Purchase is hereby authorized and approved by the affirmative vote, evidenced by their signatures to this consent, of a majority of the disinterested directors then serving, acting in good faith, in accordance with Section 144(a)(1) of the DGCL, the Board having determined that the Insider Purchase is on terms no more favorable to the purchaser than those offered to unaffiliated investors in the Financing and is fair to the Company and its stockholders; and that the interested director's signature to this consent is given solely to evidence unanimity of the Board's action on the other matters in these resolutions and, as to the Insider Purchase, the interested director abstains;]]

> **Drafting note:** Under § 144(a)(1), if a majority of the directors are not disinterested, the approval must come from a committee of two or more disinterested directors. On a two-person board where one director invests, that is not possible: obtain approval of a majority of the votes cast by disinterested stockholders under § 144(a)(2) (a separate stockholder consent), or rely on fairness and document it. If the investor is a controlling stockholder or part of a control group, use § 144(b) instead.

### 10. Securities Filings; EDGAR Access

RESOLVED FURTHER, that the Authorized Officers are authorized and directed to (a) if the Company does not have EDGAR access, submit a Form ID application to the Securities and Exchange Commission and complete all related steps, including authorizing {{edgar_account_administrators}} as account administrators for the Company's EDGAR account and delegating filing authority to {{company_counsel}} or another filing agent; (b) file a notice of sales on Form D no later than fifteen (15) calendar days after the first sale of [[Alternative A: SAFEs]] [[Alternative B: Notes]] in the Financing (or the next business day if that day is a Saturday, Sunday, or holiday), and any required amendments, including an annual amendment if the Financing continues more than one year after the most recent filing; and (c) make all notice filings, consents to service of process, and fee payments required by the securities laws of each state in which [[Alternative A: SAFEs]] [[Alternative B: Notes]] are sold, including any notice required by Section 25102.1(d) of the California Corporations Code;

RESOLVED FURTHER, that the Authorized Officers are directed to obtain, before the first closing, written confirmation from each director, executive officer, other officer participating in the Financing, and beneficial owner of 20% or more of the Company's voting equity securities that such person is not subject to any disqualifying event described in Rule 506(d) of Regulation D, and to obtain a comparable certification from any purchaser that will become such a beneficial owner;

### 11. Foreign Investors; Sanctions

RESOLVED FURTHER, that the Authorized Officers shall not issue a [[Alternative A: SAFE]] [[Alternative B: Note]] to, or grant any side-letter right to, a person that is a "foreign person" within the meaning of 31 C.F.R. § 800.224 if that person would obtain any right described in 31 C.F.R. § 800.211(b), unless the Company has first determined, with the advice of counsel, whether a declaration or notice to the Committee on Foreign Investment in the United States is required or advisable and has complied with any requirement; and shall not accept funds from any person identified as a sanctioned person in the Company's screening against lists administered by the Office of Foreign Assets Control;

### 12. Use of Proceeds

RESOLVED FURTHER, that the proceeds of the Financing shall be used for {{use_of_proceeds}};

### 13. Authorized Officers; General Authority

RESOLVED FURTHER, that each of the {{authorized_officers}} of the Company (each, an "**Authorized Officer**") is authorized, acting alone, in the name and on behalf of the Company, to execute and deliver the [[Alternative A: SAFEs and permitted side letters]] [[Alternative B: Purchase Agreement, the Notes, and the other documents contemplated by the Purchase Agreement]], to deliver the Company's notices under them, and to take all other actions and pay all fees and expenses that the Authorized Officer considers necessary or advisable to carry out the purposes of these resolutions, the taking of any such action to be conclusive evidence of that authority;

RESOLVED FURTHER, that the Secretary of the Company is directed to maintain a register of all [[Alternative A: SAFEs]] [[Alternative B: Notes]] issued in the Financing, including the holder, amount, date, terms, and any side letter, and to report the aggregate amount issued to the Board at its next meeting;

RESOLVED FURTHER, that all actions previously taken by any director or officer of the Company in connection with the matters contemplated by these resolutions, to the extent consistent with them, are hereby ratified, confirmed, and approved in all respects.

### 14. Execution

This consent may be executed in counterparts and by electronic signature or other electronic transmission, each of which shall be deemed an original and all of which together constitute one consent. This consent shall be filed with the minutes of the proceedings of the Board. This consent is effective as of the Effective Date stated above, provided that each director's consent was given no more than sixty (60) days before that date.

---

IN WITNESS WHEREOF, the undersigned directors have executed this Action by Unanimous Written Consent as of the Effective Date.

______________________________
{{director_name_1}}

Date signed: {{director_signature_date_1}}

______________________________
{{director_name_2}}

Date signed: {{director_signature_date_2}}

[[Optional: ______________________________
{{director_name_3}}

Date signed: {{director_signature_date_3}}]]

> **Drafting note:** Add one signature block per director so that the number of blocks equals the number of directors then in office ({{board_size}} authorized). Every director must sign for a § 141(f) consent.

---

## Exhibit A: Approved Forms and Economic Terms

| Item | Approved term |
|---|---|
| Instrument | [[Alternative A: Y Combinator Post-Money SAFE]] [[Alternative B: Convertible Promissory Note under the Purchase Agreement]] |
| Approved forms | [[Alternative A: Valuation Cap (version {{yc_cap_form_version}}); Discount (version {{yc_discount_form_version}}); MFN (version {{yc_mfn_form_version}}); Pro Rata Side Letter (version {{yc_side_letter_version}}), each as published at https://www.ycombinator.com/documents on {{yc_form_download_date}}]] [[Alternative B: Purchase Agreement and form of Note presented to the Board on {{effective_date}}]] |
| Valuation cap | {{valuation_cap}} [[Optional: (officers may accept no lower than {{valuation_cap_minimum}})]]; [[Alternative A: post-money, as defined in the SAFE]] [[Alternative B: measured on the Cap Capitalization basis {{cap_capitalization_alternative}} in the Note]] |
| Discount | {{discount_rate}} (for a YC discount SAFE, entered as a "Discount Rate" of {{yc_discount_rate}}) |
| MFN | [[Alternative A: Permitted only for investments made before {{mfn_cutoff_date}}]] [[Alternative B: Not permitted]] |
| Interest; maturity; Qualified Financing (Notes) | {{interest_rate}} simple; {{maturity_date}}; {{qualified_financing_amount}} of new money |
| Change of control (Notes) | Holder election of repayment of {{coc_premium_multiple}} times principal plus accrued interest, or conversion into Common Stock at the valuation cap |
| Maximum Amount | {{board_max_amount}} |
| Closing Window | Through {{closing_window_end_date}} |
| Side letters | Investors of at least {{side_letter_threshold}} only |

## Exhibit B: Interested Party Disclosure (Section 9, if applicable)

| Item | Disclosure |
|---|---|
| Interested person and relationship to the Company | {{interested_party_name}}; {{interested_party_relationship}} |
| Nature of interest | Purchaser of a [[Alternative A: SAFE]] [[Alternative B: Note]] in the amount of {{interested_party_amount}} |
| Involvement in initiating or negotiating terms | {{interested_party_involvement}} |
| Terms compared with unaffiliated investors | Identical to the terms offered to unaffiliated investors in the Financing |
| Disinterested directors approving | {{disinterested_director_names}} |
