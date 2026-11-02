---
id: board-consent-adopt-plan
title: Board Consent Adopting Equity Incentive Plan
category: equity-compensation
stage: equity
signers: [All directors (unanimous written consent)]
authorities:
  - "8 Del. C. § 141(f) (board action by unanimous consent; future effectiveness up to 60 days)"
  - "8 Del. C. §§ 141(c) (committees), 152, 153, 157 (issuance of stock and options; delegation within fixed limits), 161 (issuance of authorized shares), 116 (electronic signatures)"
  - "26 U.S.C. § 422(b)(1), (b)(2); Treas. Reg. §§ 1.422-2(b)(2)–(4), 1.422-3"
  - "26 U.S.C. § 409A; Treas. Reg. § 1.409A-1(b)(5)(iv)(B)"
  - "17 C.F.R. § 230.701(c)–(e)"
  - "Cal. Corp. Code §§ 25102(o), 25608(e), (y); Cal. Code Regs. tit. 10, §§ 260.140.41, .42, .45, .46"
use_when: The Board is adopting the Company's equity incentive plan, reserving shares, approving forms of award agreements, and sending the plan to stockholders.
do_not_use_when: Approving individual grants (use board-consent-equity-grants) or increasing an existing reserve (use plan-share-increase-and-option-amendment).
related: [equity-incentive-plan, stockholder-consent-approve-plan, board-consent-equity-grants, stock-option-grant-package, restricted-stock-purchase-agreement-plan, rsu-award-agreement, initial-board-consent]
sources:
  - name: "8 Del. C. ch. 1, subch. IV (directors and officers), Delaware Code Online"
    url: https://delcode.delaware.gov/title8/c001/sc04/index.html
  - name: "8 Del. C. ch. 1, subch. V (stock), Delaware Code Online"
    url: https://delcode.delaware.gov/title8/c001/sc05/index.html
  - name: "Treas. Reg. § 1.422-2 (eCFR)"
    url: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR6ecd7af0d8a3ff8/section-1.422-2
  - name: "17 C.F.R. § 230.701 (eCFR)"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230/subject-group-ECFRd13a0e2e2fbd4b3/section-230.701
  - name: "Cal. Corp. Code §§ 25102(o), 25608 (California Public Law mirror of leginfo)"
    url: https://california.public.law/codes/ca_corp_code_section_25608
  - name: "Law-firm board consent forms (Cooley GO, Orrick, Clerky), structure only; no text copied"
    url: https://www.cooleygo.com/
last_verified: 2026-11-02
---

## About this template

**What it does.** The Board adopts the Plan, reserves the Share Reserve out of authorized but unissued Common Stock, approves the standard forms of award agreements, directs a 409A valuation before any option grant, sets up Rule 701 and state blue-sky compliance, optionally delegates limited grant authority, and submits the Plan to stockholders.

**Sequence and timing.**

1. Confirm the charter authorizes enough Common Stock for the reserve plus every other reservation (Preferred conversion, warrants, SAFEs, convertible notes). If not, a charter amendment (8 Del. C. § 242) must be adopted first or in the same package.
2. Board adoption (this consent). For ISO purposes, the adoption date is the date of Board action unless the Board conditions adoption on stockholder approval without fixing the adoption date (Treas. Reg. § 1.422-2(b)(2)(i)); this consent fixes the date.
3. 409A valuation delivered and accepted by the Board before the first option grant (the Board may approve grants in the same consent only if it already has a valid valuation).
4. Stockholder approval within 12 months before or after adoption ([stockholder-consent-approve-plan](stockholder-consent-approve-plan.md)).
5. First grants ([board-consent-equity-grants](board-consent-equity-grants.md)).
6. California § 25102(o) notice within 30 days after the first issuance to a California resident.

**Why stockholders approve the Plan — get this right.** Rule 701 does **not** require stockholder approval. The reasons are (a) I.R.C. § 422(b)(1) (ISOs require a plan approved by stockholders within 12 months before or after adoption); (b) California's § 25102(o) exemption (10 CCR §§ 260.140.41(g), 260.140.42(e)), which requires approval by a majority of outstanding voting securities and rescission of California exercises made before approval if approval fails; and (c) any charter protective provision, voting agreement, or investor rights agreement that requires approval. A recital or resolution that says the approval is "for purposes of Rule 701" is a drafting error that diligence reviewers flag; this consent states the correct reasons.

**§ 141(f) mechanics.** A unanimous written consent is effective when the last director signs and delivers it, unless it specifies a later effective time (up to 60 days after the consent is given). This consent states a definite effective date. If any director signs after that date, the consent is effective on the later signature date, and any grant date tied to it moves too. Electronic signatures and delivery are valid under 8 Del. C. § 116.

**Delegation.** If the Board delegates grant authority to an officer (often the CEO for non-officer hires), the resolution must fix the maximum number of shares, the time period, and the minimum consideration (8 Del. C. §§ 152(b), 157(c)). The officer cannot grant to themself. Keep a written log of delegated grants. Most venture investors expect delegation to be narrow (for example, up to a guideline matrix and a per-grant cap) and reported at each Board meeting.

**Interested directors.** Adopting a plan under which directors may receive awards is not, by itself, a self-dealing transaction, but grants to directors are. See the grants consent for 8 Del. C. § 144 (as amended in 2025) and director-compensation considerations.

**Common mistakes this consent avoids.** A blank reserve; reserving more shares than are authorized; omitting the ISO limit; saying stockholder approval is "for Rule 701"; granting before a 409A valuation; delegating without the § 157(c) limits; failing to calendar the 12-month approval deadline and the 30-day California notice.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Company legal name | Northwind Robotics, Inc. | Shared |
| `{{plan_name}}` | Plan title | 2027 Equity Incentive Plan | Shared |
| `{{board_adoption_date}}` | Effective date of this consent | February 1, 2027 | Shared |
| `{{plan_reserve_shares}}` | Share Reserve | 1,500,000 | Shared |
| `{{iso_limit_shares}}` | ISO limit | 1,500,000 | Must match the Plan |
| `{{authorized_common_shares}}` | Authorized Common Stock under the charter | 10,000,000 | Shared |
| `{{outstanding_common_shares}}` | Common Stock outstanding | 6,000,000 | |
| `{{other_reserved_shares}}` | Common Stock reserved for other purposes (Preferred conversion, warrants, SAFEs) | 0 | |
| `{{par_value}}` | Par value of Common Stock | $0.00001 | Shared |
| `{{director_1_name}}`, `{{director_2_name}}`, `{{director_3_name}}` | Each director's name | Alex Rivera; Jordan Lee | Shared `initial_directors`; one signature row each |
| `{{valuation_provider}}` | Independent appraiser | Example Valuation Advisors LLC | Shared |
| `{{delegate_name}}`, `{{delegate_title}}` | Officer receiving delegated authority (optional) | Alex Rivera, Chief Executive Officer | |
| `{{delegation_max_shares}}` | Aggregate cap on delegated grants | 200,000 | § 157(c)(i) |
| `{{delegation_per_grant_max}}` | Per-person cap on delegated grants | 25,000 | |
| `{{delegation_end_date}}` | Last date for delegated grants | January 31, 2028 | § 157(c)(ii) |
| `{{prior_plan_name}}` | Predecessor plan (optional) | 2025 Stock Plan | |

---

## Form

# ACTION BY UNANIMOUS WRITTEN CONSENT OF THE BOARD OF DIRECTORS OF {{company_name}}

**Adoption of {{plan_name}}**

**Effective Date: {{board_adoption_date}}**

The undersigned, constituting all of the members of the Board of Directors (the "**Board**") of {{company_name}}, a Delaware corporation (the "**Company**"), acting under Section 141(f) of the Delaware General Corporation Law (the "**DGCL**") and the Company's Bylaws, consent to the adoption of the following resolutions, effective as of the Effective Date stated above (or, if later, the date on which the last director signs this consent), with the same force and effect as if adopted at a duly called meeting of the Board at which a quorum was present and acting throughout.

## 1. ADOPTION OF THE EQUITY INCENTIVE PLAN

**WHEREAS**, the Board believes it is in the best interests of the Company and its stockholders to adopt an equity incentive plan to attract, retain, and motivate employees, directors, and consultants of the Company and its affiliates by giving them the opportunity to acquire an equity interest in the Company;

**WHEREAS**, there has been presented to the Board the {{plan_name}} in the form attached as **Exhibit A** (the "**Plan**"), which provides for the grant of incentive stock options, nonstatutory stock options, restricted stock awards, restricted stock units, [[Optional: and stock appreciation rights,]] and which includes a supplement intended to satisfy Section 25102(o) of the California Corporations Code and Sections 260.140.41, 260.140.42, 260.140.45, and 260.140.46 of Title 10 of the California Code of Regulations; and

**WHEREAS**, the Board has reviewed the Plan and determined that its adoption is advisable and in the best interests of the Company and its stockholders.

**NOW, THEREFORE, BE IT RESOLVED**, that the Plan, in the form attached as Exhibit A, is adopted and approved, effective as of the Effective Date (which is the date of the Board's adoption of the Plan for purposes of Section 422(b)(1) of the Internal Revenue Code of 1986, as amended (the "**Code**"), and Treasury Regulations Section 1.422-2(b)(2)(i)), subject to stockholder approval as provided in these resolutions;

**RESOLVED FURTHER**, that the Board will administer the Plan, with full authority to act under it as the "Administrator," until the Board delegates administration to a committee or officer in accordance with the Plan and these resolutions;

**RESOLVED FURTHER**, that the Plan will terminate on the day before the tenth (10th) anniversary of the earlier of the Effective Date and the date the Company's stockholders approve the Plan, unless the Board terminates it earlier; and

[[Optional: **RESOLVED FURTHER**, that, effective as of the Effective Date, no further awards will be granted under the Company's {{prior_plan_name}} (the "**Prior Plan**"), and awards outstanding under the Prior Plan will remain outstanding under their terms, with shares that would otherwise return to the Prior Plan's reserve added to the Plan's Share Reserve to the extent provided in Section 1.4 of the Plan.]]

## 2. RESERVATION OF SHARES

**WHEREAS**, the Company's Certificate of Incorporation, as currently in effect, authorizes the issuance of {{authorized_common_shares}} shares of Common Stock, par value {{par_value}} per share ("**Common Stock**"), of which {{outstanding_common_shares}} shares are issued and outstanding and {{other_reserved_shares}} shares are reserved for issuance for purposes other than the Plan (including on conversion of outstanding Preferred Stock and on exercise or conversion of outstanding warrants, convertible notes, and simple agreements for future equity); and

**WHEREAS**, the Board has determined that a sufficient number of authorized but unissued and unreserved shares of Common Stock is available to reserve the Share Reserve.

**RESOLVED**, that {{plan_reserve_shares}} shares of Common Stock (the "**Share Reserve**") are reserved for issuance under the Plan, subject to adjustment as provided in the Plan, and the Company shall at all times keep available a number of authorized but unissued shares of Common Stock sufficient to satisfy the Share Reserve;

**RESOLVED FURTHER**, that the maximum aggregate number of shares of Common Stock that may be issued on the exercise of incentive stock options under the Plan is {{iso_limit_shares}} shares, subject to adjustment as provided in the Plan; and

**RESOLVED FURTHER**, that when issued and delivered in accordance with the Plan and the applicable award agreement, against receipt of the consideration the Plan and the applicable award agreement require (which the Board has determined will be not less than the par value of the shares), the shares of Common Stock issued under the Plan will be duly authorized, validly issued, fully paid, and nonassessable.

> **Drafting note:** Confirm the arithmetic before signing: authorized Common Stock must be at least outstanding Common Stock + `{{other_reserved_shares}}` + `{{plan_reserve_shares}}` (plus any evergreen headroom). If the Preferred is convertible 1:1, every share of Preferred outstanding requires a share of reserved Common. Under-reservation is a common diligence finding that requires a charter amendment and sometimes § 204 ratification of over-issued shares.

## 3. FORMS OF AWARD AGREEMENTS

**RESOLVED**, that the following forms are approved for use under the Plan, with such changes as the Administrator (or a duly authorized delegate) approves that are consistent with the Plan and these resolutions: (a) the Notice of Stock Option Grant, Stock Option Agreement, and Exercise Notice and Stock Purchase Agreement (with early exercise provisions, joint escrow instructions, assignment separate from certificate, and spousal consent), attached as **Exhibit B**; (b) the Restricted Stock Purchase Agreement, attached as **Exhibit C**; and (c) the Restricted Stock Unit Grant Notice and Restricted Stock Unit Award Agreement, attached as **Exhibit D** (together, the "**Award Agreements**").

## 4. FAIR MARKET VALUE; SECTION 409A VALUATION

**WHEREAS**, the Plan requires that the exercise price of each option be not less than the fair market value of the Common Stock on the date of grant, determined in a manner consistent with Sections 409A and 422 of the Code.

**RESOLVED**, that the officers of the Company are authorized and directed to engage {{valuation_provider}}, or another independent appraiser the officers determine is qualified, to prepare an independent appraisal of the fair market value of the Common Stock intended to satisfy the presumption of reasonableness in Treasury Regulations Section 1.409A-1(b)(5)(iv)(B)(2)(i), and to deliver the appraisal to the Board;

**RESOLVED FURTHER**, that no option [[Optional: or stock appreciation right]] will be granted under the Plan until the Board (or, if the Board has delegated that authority, the Compensation Committee) has reviewed and accepted a valuation and determined the fair market value of the Common Stock as of the grant date;

**RESOLVED FURTHER**, that the officers are directed to (a) obtain an updated valuation at least once every twelve (12) months while the Company makes grants, and (b) promptly notify the Board of any event that may materially affect the value of the Common Stock (including the receipt of a term sheet for an equity financing, an acquisition proposal, a material change in revenue, a significant customer, product, regulatory, or litigation development, or the commencement of IPO preparations), so that the Board may determine whether a new valuation is needed before further grants; and

**RESOLVED FURTHER**, that the officers are directed to maintain in the Company's records each valuation report, the Board's determination of fair market value for each grant date, and the materials the Board considered.

## 5. SECURITIES LAW COMPLIANCE

**WHEREAS**, the Company intends that offers and sales of securities under the Plan be exempt from registration under the Securities Act of 1933, as amended (the "**Securities Act**"), under Rule 701 under the Securities Act ("**Rule 701**") to the extent available, and exempt from qualification or registration under applicable state securities laws.

**RESOLVED**, that the Plan is adopted as a written compensatory benefit plan within the meaning of Rule 701;

**RESOLVED FURTHER**, that the officers are directed to (a) deliver a copy of the Plan to each recipient of an award before or at the time of grant; (b) track, for each consecutive twelve (12)-month period (using a method applied consistently), the aggregate sales price and amount of securities sold under the Plan and all other compensatory arrangements in reliance on Rule 701, counting options at their aggregate exercise price on the grant date and other awards on their date of sale; (c) confirm before each grant that the grant is within the greatest of the limits in Rule 701(d)(2) ($1,000,000; fifteen percent (15%) of the Company's total assets; or fifteen percent (15%) of the outstanding amount of the class of securities being offered), measured at the Company's most recent balance sheet date; (d) notify the Board when sales in any twelve (12)-month period are reasonably expected to exceed $10,000,000 and, if so, prepare and deliver the disclosure required by Rule 701(e) (a summary of the Plan's material terms, risk factors, and financial statements as of a date no more than one hundred eighty (180) days before the sale) a reasonable period of time before each sale (for options, before exercise; for restricted stock units, before grant), subject to appropriate confidentiality arrangements; and (e) confirm that each consultant or advisor who receives an award is a natural person providing bona fide services not connected with capital raising or market-making;

**RESOLVED FURTHER**, that, for each award to a resident of California, the officers are authorized and directed to file with the California Department of Financial Protection and Innovation a notice of transaction under Section 25102(o) of the California Corporations Code no later than thirty (30) days after the initial issuance of any security under the Plan to a California resident, and to pay the filing fee prescribed by Section 25608(y) of the California Corporations Code;

**RESOLVED FURTHER**, that, before the first award to a resident of any other state or of any country outside the United States, the officers are directed to determine, with the advice of counsel, whether any securities filing, notice, fee, or exemption application is required in that jurisdiction, and to make any required filing;

**RESOLVED FURTHER**, that the officers are directed to monitor the number of holders of options and other securities of the Company for purposes of Section 12(g) of the Securities Exchange Act of 1934, as amended, and Rule 12h-1(f) under it, and to report to the Board if the number of holders of record of any class of equity security approaches the thresholds in Section 12(g)(1)(A); and

**RESOLVED FURTHER**, that the officers are directed to implement procedures to (a) furnish Form 3921 to each person who exercises an incentive stock option by January 31 of the following year and file Forms 3921 with the Internal Revenue Service by the applicable due date, and (b) remind each recipient of restricted stock, and each optionholder who early exercises, of the thirty (30)-day deadline for an election under Section 83(b) of the Code, while making clear that the filing is the recipient's responsibility.

## 6. DELEGATION OF GRANT AUTHORITY

[[Alternative A: **RESOLVED**, that the Board does not delegate authority to grant awards under the Plan at this time, and all awards will be approved by the Board (or a committee of the Board to which the Board delegates that authority).]]

[[Alternative B: **RESOLVED**, that, in accordance with Sections 152 and 157 of the DGCL and Section 3.4 of the Plan, the Board delegates to {{delegate_name}}, the Company's {{delegate_title}} (the "**Delegate**"), the authority to grant options and restricted stock units under the Plan to newly hired or promoted employees and to consultants of the Company and its subsidiaries who are not officers or directors of the Company or holders of more than ten percent (10%) of the Company's outstanding capital stock, and to determine the number of shares subject to each such award, subject to the following limits:

(a) **Maximum Shares.** The maximum aggregate number of shares of Common Stock that may be subject to awards granted under this delegation, and issued on exercise or settlement of those awards, is {{delegation_max_shares}} shares, and no individual may receive awards under this delegation covering more than {{delegation_per_grant_max}} shares in any calendar year;

(b) **Time Period.** Awards may be granted under this delegation only during the period from the Effective Date through {{delegation_end_date}}, and the shares underlying those awards may be issued at any time during the term of the awards;

(c) **Minimum Consideration.** The exercise price of each option granted under this delegation will be not less than one hundred percent (100%) of the fair market value of a share of Common Stock on the grant date as most recently determined by the Board under Section 4 of these resolutions (and the Delegate may not grant any option if the valuation underlying that determination is as of a date more than twelve (12) months before the grant date or if the Delegate is aware of any event described in clause (b) of the third resolution in Section 4 of these resolutions that has occurred since that determination), and the consideration for shares issued on settlement of restricted stock units will be past services having a value not less than the par value of the shares;

(d) **Form and Terms.** Each award will be on the applicable form of Award Agreement approved in Section 3, with the standard vesting schedule approved by the Board (four (4) years, with a one (1)-year cliff and monthly vesting thereafter for options; and the schedule in the approved form for restricted stock units), without acceleration or early exercise unless approved by the Board;

(e) **No Self-Grants.** The Delegate may not grant any award to the Delegate; and

(f) **Reporting.** The Delegate shall report each award granted under this delegation (including the recipient, grant date, number of shares, exercise price, and vesting schedule) to the Board at or before its next regular meeting, and shall maintain a written record of each grant, including the date on which the Delegate's action was completed.]]

> **Drafting note:** A delegation that omits any of the three statutory limits (maximum shares, time period, minimum consideration) is outside 8 Del. C. § 157(c) and risks void awards. The minimum-consideration limit may be set by formula (2022 amendments), but the formula cannot depend on the delegate's own determination (§ 157(d)); tying it to the Board's most recent FMV determination satisfies this. Never let a delegate determine FMV.

## 7. SUBMISSION TO STOCKHOLDERS

**WHEREAS**, stockholder approval of the Plan is required (a) for options granted under the Plan to qualify as incentive stock options under Section 422(b)(1) of the Code, which requires approval by the stockholders within twelve (12) months before or after the date the Board adopts the Plan; (b) for awards to residents of California under Section 25102(o) of the California Corporations Code and Sections 260.140.41(g) and 260.140.42(e) of Title 10 of the California Code of Regulations, which require approval by a majority of the outstanding securities entitled to vote; and (c) [[Optional: under Section ___ of the Company's Certificate of Incorporation and Section ___ of the Voting Agreement dated ___, which require the approval of the holders of the Company's Preferred Stock for the adoption of any equity incentive plan or the reservation of shares under it]].

**RESOLVED**, that the Board recommends that the Company's stockholders approve the Plan, including the Share Reserve, the incentive stock option limit, and the class of employees eligible to receive incentive stock options, and directs that the Plan be submitted to the stockholders for approval by written consent under Section 228 of the DGCL or at a meeting of stockholders;

**RESOLVED FURTHER**, that the officers are directed to obtain that approval no later than the first anniversary of the Effective Date, and to give prompt notice of any action taken by less than unanimous written consent to the non-consenting stockholders entitled to it under Section 228(e) of the DGCL;

**RESOLVED FURTHER**, that awards may be granted under the Plan before stockholder approval, provided that (a) any incentive stock option granted before approval will be treated as a nonstatutory stock option if approval is not obtained within twelve (12) months after the Effective Date, and (b) no option granted to a California resident may be exercised, and no restricted stock may be issued to a California resident, before approval, unless the award provides that it will be rescinded if approval is not obtained within the period required by Appendix A to the Plan; and

**RESOLVED FURTHER**, that the Board notes that Rule 701 does not itself require stockholder approval of the Plan, and that the approval is sought for the reasons stated in the recitals to this Section 7.

## 8. EQUITY ADMINISTRATION

**RESOLVED**, that the officers are authorized to engage an equity administration platform to maintain the Company's capitalization records, issue electronic award agreements and uncertificated shares, deliver the notices required by Section 151(f) of the DGCL for uncertificated shares, and track vesting, exercises, and Rule 701 compliance, and to cause the Company's stock ledger to reflect the Share Reserve and all awards and issuances under the Plan.

## 9. GENERAL AUTHORITY

**RESOLVED**, that the officers of the Company are each authorized and directed, for and on behalf of the Company, to take all actions and to execute and deliver all agreements, notices, filings, certificates, and other documents, and to pay all fees and expenses, that any of them determines necessary or advisable to carry out the purposes of the foregoing resolutions, the taking of any such action or the execution and delivery of any such document to be conclusive evidence of that determination; and

**RESOLVED FURTHER**, that all actions previously taken by any director, officer, or agent of the Company in connection with the matters contemplated by the foregoing resolutions, to the extent consistent with them, are ratified, confirmed, and approved in all respects.

## 10. MISCELLANEOUS

This consent may be executed in counterparts, each of which is an original and all of which together are one instrument, and may be executed and delivered by electronic signature or electronic transmission in accordance with Section 116 of the DGCL. This consent will be filed with the minutes of the proceedings of the Board.

| Director | Signature | Date signed |
|---|---|---|
| {{director_1_name}} | ______________________________ | ____________ |
| {{director_2_name}} | ______________________________ | ____________ |
| [[Optional: {{director_3_name}}]] | ______________________________ | ____________ |

> **Drafting note:** Add one row per director; every director must sign for a § 141(f) consent. If a director is conflicted on another item in the same consent, that does not defeat unanimous-consent validity, but consider separating director-specific grants into their own consent with appropriate disclosure.

**Exhibits:** Exhibit A — {{plan_name}}; Exhibit B — Form of Stock Option Grant Package; Exhibit C — Form of Restricted Stock Purchase Agreement; Exhibit D — Form of Restricted Stock Unit Grant Notice and Award Agreement.
