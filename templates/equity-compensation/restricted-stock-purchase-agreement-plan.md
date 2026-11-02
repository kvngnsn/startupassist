---
id: restricted-stock-purchase-agreement-plan
title: Restricted Stock Purchase Agreement (Under Equity Incentive Plan)
category: equity-compensation
stage: hiring
signers: [Company (by an officer), Purchaser, Purchaser's spouse (community property states), Escrow Agent]
authorities:
  - "26 U.S.C. § 83(a), (b); Treas. Reg. §§ 1.83-2, 1.83-3(b)–(d), (i)"
  - "26 U.S.C. § 1202(c)(1)(B) (QSBS original issuance for money, property, or services), as amended by P.L. 119-21, § 70431"
  - "17 C.F.R. § 230.701(d)(3)(ii) (sale date for non-option securities)"
  - "Cal. Corp. Code § 25102(o); Cal. Code Regs. tit. 10, §§ 260.140.42, 260.140.45, 260.140.46"
  - "8 Del. C. §§ 152, 153 (consideration; par value floor), 202 (transfer restrictions), 151(f) (uncertificated share notice)"
use_when: Selling (or granting for services) restricted Common Stock under the Company's equity incentive plan to an early employee, executive, director, or advisor, subject to vesting and a Company repurchase option.
do_not_use_when: Founders are buying stock at formation outside the plan (use founder-stock-purchase-agreement), the holder is exercising an option early (use the Exercise Agreement in stock-option-grant-package), or the award is an RSU (use rsu-award-agreement).
related: [equity-incentive-plan, board-consent-equity-grants, stock-option-grant-package, founder-stock-purchase-agreement, 83b-election-package]
sources:
  - name: "Treas. Reg. § 1.83-2 (eCFR)"
    url: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.83-2
  - name: "17 C.F.R. § 230.701 (eCFR)"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230/subject-group-ECFRd13a0e2e2fbd4b3/section-230.701
  - name: "Cal. Code Regs. tit. 10, § 260.140.42 (Cornell LII)"
    url: https://www.law.cornell.edu/regulations/california/10-CCR-260.140.42
  - name: "Law-firm restricted stock purchase forms (Cooley GO, Orrick, Clerky), structure and market terms only; no text copied"
    url: https://www.cooleygo.com/
last_verified: 2026-11-02
---

## About this template

**What it does.** This agreement sells (or grants for past services) shares of Common Stock under the Plan as a Restricted Stock Award (Plan § 8). The shares vest over time; unvested shares are subject to the Company's repurchase option at the lower of cost or fair market value if the purchaser's service ends; unvested shares are held in escrow; and the purchaser decides whether to file an 83(b) election within 30 days. It is the right instrument in the earliest months after formation, when the 409A value is still very low and the purchase price is affordable.

**Why restricted stock instead of options.** With a timely 83(b) election and a purchase price equal to FMV, the purchaser has no income at purchase or at vesting, capital-gain treatment begins immediately, and the I.R.C. § 1202 (QSBS) holding period begins on issuance. Under § 1202 as amended by P.L. 119-21 (stock issued after July 4, 2025), the exclusion is 50% after 3 years, 75% after 4, and 100% after 5. Options do not start the QSBS clock until exercise. The trade-offs: the purchaser must pay cash up front, and once the 409A value rises, the purchase becomes expensive (or taxable if the price is below FMV).

**Key requirements.**

- **Price and consideration.** The Plan (§ 8.2) defaults to a price not less than FMV on the Grant Date. Consideration must at least equal par value (8 Del. C. § 153); the Board's good-faith judgment of the value of non-cash consideration is conclusive absent actual fraud (8 Del. C. § 152). If the price is below FMV, the discount is compensation income: at purchase if an 83(b) election is filed, or at each vesting date (measured by the value then) if not, and wage withholding applies for employees.
- **§ 83(b).** 30 days after the purchase date; no extension; copy to the Company (Treas. Reg. § 1.83-2(b), (d)). Since January 1, 2016, a copy no longer needs to be attached to the tax return (Treas. Reg. § 1.83-2(c), (g)). IRS Form 15620 may be used.
- **Rule 701.** Restricted stock is "sold" on the purchase date at the purchase price (Rule 701(d)(3)(i)–(ii)); stock granted for services is valued by reference to the securities' value. Deliver a copy of the Plan before the sale, and Rule 701(e) information if the $10 million threshold is triggered.
- **California.** For a California purchaser, the plan must satisfy 10 CCR § 260.140.42 (number of securities and eligible persons, nontransferable purchase rights, capitalization adjustments, issuance within 10 years, stockholder approval with rescission, and § 260.140.46 information); Plan Appendix A covers these. The current regulations do not restrict a repurchase of unvested shares at cost.
- **Community property.** Obtain the spousal consent (Exhibit C).

**Market positions.** Vesting: 4 years with a 1-year cliff (market). Repurchase price: lower of cost or FMV (market and company-favorable; cost-only is holder-favorable). Automatic repurchase (company-favorable and avoids accidental vesting) versus optional repurchase. Acceleration is left to individual agreements; the Plan's corporate-transaction rules govern otherwise.

**Common mistakes.**

1. Missing the 30-day 83(b) deadline; the Company cannot cure it. Calendar it and send a reminder.
2. Selling shares at a stale price after the 409A value has increased (taxable discount; for employees, an unwithheld wage).
3. Not escrowing unvested shares, then being unable to enforce the repurchase after a departure.
4. Treating a "deemed" repurchase as complete without tendering payment.
5. Overlooking that stock issued under the Plan reduces the Share Reserve (Plan § 4.1); founder stock purchased outside the Plan does not.

**Deadlines triggered.** § 83(b) election within 30 days of the Purchase Date; § 25102(o) notice within 30 days after the first issuance under the Plan in California (if not already filed); repurchase option exercisable within 90 days after the later of termination and 6 months after purchase.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Company legal name | Northwind Robotics, Inc. | Shared |
| `{{plan_name}}` | Plan title | 2027 Equity Incentive Plan | Shared |
| `{{effective_date}}` | Date of this agreement | April 1, 2027 | Shared |
| `{{participant_name}}`, `{{participant_address}}`, `{{participant_email}}` | Purchaser | Casey Morgan | Shared |
| `{{grant_date}}` | Date the Board approved the award | March 15, 2027 | Shared |
| `{{grant_shares}}` | Shares purchased | 100,000 | Shared |
| `{{price_per_share}}` | Purchase price per share | $0.05 | Shared; ≥ FMV on Grant Date unless intentionally discounted |
| `{{aggregate_purchase_price}}` | grant_shares × price_per_share | $5,000.00 | Shared |
| `{{fmv_409a_value}}`, `{{valuation_date}}` | FMV basis | $0.05; January 31, 2027 | Shared |
| `{{vesting_commencement_date}}`, `{{cliff_months}}`, `{{vesting_months}}` | Vesting | March 1, 2027; 12; 48 | Shared |
| `{{custom_vesting_schedule}}` | Non-standard vesting (Alternative B) | | Optional |
| `{{acceleration_agreement_reference}}` | Agreement providing acceleration (§ 2.3, Alternative B) | Section 4 of the Offer Letter dated March 1, 2027 | Optional |
| `{{escrow_agent_name}}` | Escrow agent | Jordan Lee, Secretary | |
| `{{spouse_name}}` | Purchaser's spouse | | Exhibit C |
| `{{signatory_name}}`, `{{signatory_title}}` | Company signer | Alex Rivera, Chief Executive Officer | Shared |
| `{{governing_law_state}}`, `{{forum}}`, `{{company_notice_email}}` | Boilerplate | Delaware; Court of Chancery of the State of Delaware | Shared |

---

## Form

# {{company_name}}
# {{plan_name}}
# RESTRICTED STOCK PURCHASE AGREEMENT

This Restricted Stock Purchase Agreement (this "**Agreement**") is entered into as of {{effective_date}} (the "**Effective Date**") between {{company_name}}, a Delaware corporation (the "**Company**"), and {{participant_name}} ("**Purchaser**"), under the Company's {{plan_name}} (the "**Plan**"). Capitalized terms not defined in this Agreement have the meanings given in the Plan.

## 1. PURCHASE AND SALE OF SHARES

**1.1 Agreement to Purchase and Sell.** On the terms of this Agreement and the Plan, Purchaser agrees to purchase from the Company, and the Company agrees to sell and issue to Purchaser, {{grant_shares}} shares of Common Stock (the "**Shares**") at a purchase price of {{price_per_share}} per share, for an aggregate purchase price of {{aggregate_purchase_price}} (the "**Purchase Price**"). The Shares are granted as a Restricted Stock Award under Section 8 of the Plan on the Grant Date of {{grant_date}}.

**1.2 Fair Market Value.** The Board has determined that the Purchase Price per share is not less than the Fair Market Value of a share of Common Stock on the Grant Date, based on a Fair Market Value of {{fmv_409a_value}} per share as of {{valuation_date}}. [[Optional: The Board has determined that the purchase price is less than Fair Market Value, and Purchaser acknowledges that the difference is compensation income subject to Section 9.3.]]

**1.3 Closing.** The purchase and sale of the Shares will take place on the Effective Date or on another date the parties agree (the "**Purchase Date**"), by electronic exchange of documents and signatures. At the closing, (a) Purchaser shall deliver to the Company the Purchase Price by [[Alternative A: cash, check, or wire transfer]] [[Alternative B: cancellation of indebtedness of the Company to Purchaser in the amount of the Purchase Price]] [[Alternative C: past services rendered to the Company, which the Board has valued at not less than the Purchase Price and not less than the aggregate par value of the Shares]]; (b) Purchaser shall deliver executed copies of the Joint Escrow Instructions (Exhibit B), the Assignment Separate from Certificate (Exhibit A), and, if applicable, the Spousal Consent (Exhibit C); and (c) the Company shall issue the Shares in Purchaser's name in book-entry form (or, at the Company's election, by certificate delivered to the Escrow Agent), subject to Section 4.

**1.4 Plan Governs.** The Shares are issued under and subject to the Plan, which is incorporated into this Agreement by reference. If this Agreement conflicts with the Plan, the Plan controls, except as provided in Section 16.16 of the Plan. Purchaser acknowledges receipt of a copy of the Plan.

## 2. VESTING

**2.1 Vesting Schedule.** Subject to Purchaser's Continuous Service through each applicable vesting date, the Shares will vest as follows: [[Alternative A: {{cliff_months}}/{{vesting_months}}ths of the Shares will vest on the date that is {{cliff_months}} months after {{vesting_commencement_date}} (the "**Vesting Commencement Date**"), and 1/{{vesting_months}}th of the Shares will vest on the same day of each month thereafter (or, if there is no corresponding day, on the last day of the month), so that all of the Shares are vested on the date that is {{vesting_months}} months after the Vesting Commencement Date.]] [[Alternative B: {{custom_vesting_schedule}}]] Shares that have vested are "**Vested Shares**"; Shares that have not vested are "**Unvested Shares**." Fractional shares resulting from the vesting schedule will be rounded down to the nearest whole share, with any remainder vesting on the final vesting date.

**2.2 No Vesting after Termination.** Vesting ceases on the date Purchaser's Continuous Service ends. No Shares vest after that date unless the Plan or a written agreement between Purchaser and the Company expressly provides for acceleration.

**2.3 Acceleration.** [[Alternative A: None, except as the Board may determine under the Plan.]] [[Alternative B: The vesting of the Shares will accelerate as provided in {{acceleration_agreement_reference}}, which is incorporated by reference and controls under Section 16.16 of the Plan.]]

**2.4 Leaves; Change in Time Commitment.** Sections 16.4 and 16.5 of the Plan apply to the vesting of the Shares.

## 3. REPURCHASE OPTION

**3.1 Grant of Repurchase Option.** If Purchaser's Continuous Service terminates for any reason, voluntary or involuntary, with or without Cause, including death or Disability (the date of termination, the "**Termination Date**"), the Company (or its assignee) has an irrevocable, exclusive option (the "**Repurchase Option**") to repurchase all or any portion of the Shares that are Unvested Shares on the Termination Date, at a price per share (the "**Repurchase Price**") equal to the lower of (a) the price per share Purchaser paid for those Shares and (b) the Fair Market Value of a share of Common Stock on the date of repurchase, in each case as adjusted for Capitalization Adjustments.

> **Drafting note:** If the Shares were issued for past services rather than cash, replace the Repurchase Option with automatic forfeiture without consideration (Plan § 8.4(a)(i)): there is nothing to "repurchase" at cost. Forfeited service shares are a capital loss only to the extent of any amount paid and any income recognized under an 83(b) election (Treas. Reg. § 1.83-2(a)).

**3.2 Exercise.** The Company (or its assignee) may exercise the Repurchase Option by delivering written notice of exercise to Purchaser (or Purchaser's executor, administrator, or other legal representative) within ninety (90) days after the later of (a) the Termination Date and (b) the date that is six (6) months after the Purchase Date (the "**Repurchase Period**"). The notice will state the number of Unvested Shares being repurchased and the closing date, which will be no later than the last day of the Repurchase Period.

**3.3 Automatic Exercise.** [[Alternative A: Unless the Company notifies Purchaser before the end of the Repurchase Period that it elects not to repurchase some or all of the Unvested Shares, the Repurchase Option will be deemed automatically exercised for all Unvested Shares on the last day of the Repurchase Period, and the Company shall tender the Repurchase Price within thirty (30) days after that date.]] [[Alternative B: If the Company does not exercise the Repurchase Option within the Repurchase Period, the Repurchase Option terminates for any Unvested Shares not repurchased, and those Shares become Vested Shares.]]

**3.4 Payment.** The Company shall pay the Repurchase Price, at its option, by check, wire transfer, cancellation of any indebtedness of Purchaser to the Company, or a combination of them. If the Repurchase Price is tendered and Purchaser fails or refuses to deliver the Shares, the Company may deposit the Repurchase Price with the Escrow Agent or another third party for Purchaser's account, and the Shares will be deemed repurchased and cancelled on that deposit.

**3.5 Effect of Repurchase.** From and after the closing (or deemed exercise and tender), Purchaser has no further rights as a holder of the repurchased Shares other than the right to receive the Repurchase Price, and the Company may record the repurchase on its books without further action by Purchaser.

**3.6 Assignment of Repurchase Option.** The Company may assign the Repurchase Option, in whole or in part, to any person or persons. If the Fair Market Value of the Unvested Shares on the date of assignment exceeds the Repurchase Price, any assignee other than a wholly owned Subsidiary shall pay the Company cash equal to the excess, as determined by the Board.

**3.7 Additional Securities.** Any securities or other property (other than ordinary cash dividends) issued or distributed with respect to Unvested Shares, including by reason of a Capitalization Adjustment, or in exchange for Unvested Shares in a Corporate Transaction, are Unvested Shares for purposes of this Agreement, subject to the Repurchase Option and escrow, with the Repurchase Price appropriately adjusted, unless the Board provides otherwise under Section 11.3 of the Plan.

**3.8 Termination of Repurchase Option.** The Repurchase Option terminates as to Shares as they vest, and in full on the earliest of (a) the date all Shares have vested, (b) the closing of a Corporate Transaction in which the Repurchase Option is not assigned to the successor, and (c) the date the Board waives it in writing.

## 4. ESCROW

**4.1 Deposit.** As security for the Repurchase Option, Purchaser shall deposit the Unvested Shares with {{escrow_agent_name}} (or a successor under Exhibit B, the "**Escrow Agent**"), together with the executed Assignment Separate from Certificate (Exhibit A) in blank, under the Joint Escrow Instructions (Exhibit B). If the Shares are uncertificated, the Company may record the Unvested Shares in a restricted book-entry position, and the Joint Escrow Instructions will apply to that position.

**4.2 Release.** As Shares vest, the Escrow Agent shall release them to Purchaser on the schedule in Exhibit B. The escrow terminates when all Shares have vested or been repurchased.

**4.3 Stockholder Rights.** While the Unvested Shares are in escrow, Purchaser may vote them and receive ordinary cash dividends on them, subject to Section 3.7 and Section 8.7 of the Plan.

## 5. TRANSFER RESTRICTIONS; RIGHT OF FIRST REFUSAL; MARKET STAND-OFF

**5.1 Unvested Shares.** Purchaser shall not sell, assign, transfer, pledge, hypothecate, or otherwise dispose of any Unvested Shares or any interest in them, except to the Company or its assignee under Section 3, and any purported transfer in violation of this Section 5.1 is void.

**5.2 Vested Shares.** Vested Shares are subject to the transfer restrictions, the Company's right of first refusal, and the market stand-off provisions in Section 12 of the Plan, which are incorporated into this Agreement by reference.

**5.3 Stockholder Agreements.** At the Company's request, Purchaser shall become a party to any voting agreement, right of first refusal and co-sale agreement, or similar agreement described in Section 10.7 of the Plan.

**5.4 Compliance with Law.** No Shares may be transferred unless the transfer is registered under the Securities Act or exempt from registration, and complies with applicable state securities laws, and the Company may require an opinion of counsel reasonably satisfactory to it to that effect.

**5.5 Refusal to Transfer.** The Company is not required to transfer on its books any Shares sold or transferred in violation of this Agreement, or to treat the purported transferee as the owner of those Shares or accord it voting or dividend rights.

## 6. CAPITALIZATION ADJUSTMENTS; CORPORATE TRANSACTIONS

The number of Shares subject to the Repurchase Option and the Repurchase Price will be adjusted for Capitalization Adjustments under Section 11.1 of the Plan. In a Corporate Transaction, the Shares (including Unvested Shares and the Repurchase Option) will be treated as provided in Section 11.3 of the Plan, including assignment of the Repurchase Option to the successor, or lapse of the Repurchase Option, as the Board determines.

## 7. REPRESENTATIONS AND WARRANTIES OF PURCHASER

Purchaser represents and warrants to the Company as of the Purchase Date that:

**7.1 Investment Intent.** Purchaser is acquiring the Shares for Purchaser's own account for investment and not with a view to, or for resale in connection with, any distribution in violation of the Securities Act.

**7.2 Access to Information; Sophistication.** Purchaser has received a copy of the Plan and, if required by Rule 701(e), the information described in Section 10.3 of the Plan. Purchaser has had the opportunity to ask questions of and receive answers from the Company, and (alone or with Purchaser's advisers) has the knowledge and experience in financial and business matters to evaluate the merits and risks of the investment.

**7.3 Risk.** Purchaser understands that an investment in the Shares is speculative and involves a high degree of risk, including the risk of total loss, and that there is no public market for the Shares.

**7.4 Restricted Securities.** Purchaser understands that the Shares have not been registered under the Securities Act or any state securities law and are being issued in reliance on exemptions (including Rule 701 and, for California residents, Section 25102(o) of the California Corporations Code), that the Shares are "restricted securities" that must be held indefinitely unless registered or exempt, and that the Company has no obligation to register them or to make Rule 144 available.

**7.5 No Reliance.** Purchaser is not relying on any statement or representation by the Company or its agents other than those in this Agreement, including any statement about the future value of the Shares or the tax consequences of the purchase.

**7.6 Residence.** Purchaser's principal residence is in the state or country stated below Purchaser's signature.

## 8. LEGENDS

Each certificate or book-entry notation representing the Shares will bear legends substantially in the following form, together with any legend required by state securities law or any agreement described in Section 5.3:

(a) "THE SECURITIES REPRESENTED HEREBY HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933, AS AMENDED (THE "ACT"), AND HAVE BEEN ACQUIRED FOR INVESTMENT AND NOT WITH A VIEW TO, OR IN CONNECTION WITH, THE SALE OR DISTRIBUTION THEREOF. NO SUCH SALE OR DISTRIBUTION MAY BE EFFECTED WITHOUT AN EFFECTIVE REGISTRATION STATEMENT RELATED THERETO OR AN EXEMPTION FROM REGISTRATION UNDER THE ACT."

(b) "THE SHARES REPRESENTED HEREBY ARE SUBJECT TO A REPURCHASE OPTION, RESTRICTIONS ON TRANSFER, AND A RIGHT OF FIRST REFUSAL HELD BY THE ISSUER OR ITS ASSIGNEE(S) AS SET FORTH IN THE ISSUER'S EQUITY INCENTIVE PLAN AND AN AGREEMENT BETWEEN THE ISSUER AND THE ORIGINAL HOLDER OF THESE SHARES, COPIES OF WHICH MAY BE OBTAINED AT THE PRINCIPAL OFFICE OF THE ISSUER. SUCH REPURCHASE OPTION, RESTRICTIONS, AND RIGHT OF FIRST REFUSAL ARE BINDING ON TRANSFEREES OF THESE SHARES."

(c) "THE SHARES REPRESENTED HEREBY ARE SUBJECT TO A LOCK-UP PERIOD OF UP TO 180 DAYS FOLLOWING THE EFFECTIVE DATE OF A REGISTRATION STATEMENT OF THE ISSUER FILED UNDER THE ACT, AS SET FORTH IN AN AGREEMENT BETWEEN THE ISSUER AND THE ORIGINAL HOLDER OF THESE SHARES, AND MAY NOT BE SOLD OR OTHERWISE DISPOSED OF BY THE HOLDER PRIOR TO THE EXPIRATION OF SUCH PERIOD WITHOUT THE CONSENT OF THE ISSUER OR THE MANAGING UNDERWRITER."

For uncertificated Shares, the Company will deliver the notice required by Section 151(f) of the Delaware General Corporation Law. The Company may remove legend (b) from Vested Shares after the right of first refusal terminates, and may issue stop-transfer instructions to enforce this Agreement.

## 9. TAX MATTERS

**9.1 Tax Advice.** Purchaser has reviewed with Purchaser's own tax advisers the federal, state, local, and non-U.S. tax consequences of this investment and the transactions contemplated by this Agreement, and is relying solely on those advisers and not on any statement of the Company or its agents. Purchaser (and not the Company) is responsible for Purchaser's own tax liability.

**9.2 Section 83(b) Election.** Purchaser understands that under Section 83 of the Code, the excess of the fair market value of the Shares on each date they vest over the amount paid for them will be taxable as ordinary income on that date. Purchaser may instead elect under Section 83(b) of the Code to be taxed at the time of purchase on the excess (if any) of the fair market value of the Shares on the Purchase Date over the Purchase Price. THE ELECTION MUST BE FILED WITH THE INTERNAL REVENUE SERVICE WITHIN THIRTY (30) DAYS AFTER THE PURCHASE DATE; THE DEADLINE CANNOT BE EXTENDED. A form of election is described in Exhibit D. PURCHASER ACKNOWLEDGES THAT IT IS PURCHASER'S SOLE RESPONSIBILITY, AND NOT THE COMPANY'S, TO FILE A TIMELY ELECTION, EVEN IF PURCHASER REQUESTS THE COMPANY OR ITS REPRESENTATIVES TO MAKE THE FILING ON PURCHASER'S BEHALF. Purchaser shall deliver a copy of any election to the Company within ten (10) days after filing.

**9.3 Withholding.** If Purchaser is or was an Employee and recognizes compensation income in connection with the Shares (including on a Section 83(b) election for Shares purchased below Fair Market Value or on vesting without an election), Purchaser shall pay the Company, or make arrangements satisfactory to the Company for, any resulting Withholding Obligation. The Company may satisfy that obligation by any method permitted by Section 13.1 of the Plan, including withholding from Purchaser's wages. The Company is not required to release Shares from escrow until the Withholding Obligation is satisfied.

**9.4 No Representation as to Value or Tax Treatment.** Purchaser acknowledges that the Company has not represented that the Internal Revenue Service will accept the Board's determination of Fair Market Value, that the Shares will qualify as "qualified small business stock" under Section 1202 of the Code, or that any other tax treatment will apply.

## 10. SPOUSAL CONSENT; NO EMPLOYMENT RIGHTS

**10.1 Spousal Consent.** If Purchaser is married or in a registered domestic partnership and resides in a community property jurisdiction, Purchaser shall deliver a Spousal Consent in the form of Exhibit C executed by Purchaser's spouse or partner.

**10.2 No Employment Rights.** Nothing in this Agreement confers on Purchaser any right to continue in the employ or service of the Company or any Affiliate, or affects the right of the Company or any Affiliate to terminate Purchaser's employment or service at any time, with or without Cause, subject to Applicable Law and any written agreement. Purchaser acknowledges that the vesting schedule does not guarantee service for any period.

## 11. GENERAL PROVISIONS

**11.1 Governing Law.** This Agreement is governed by the laws of the State of {{governing_law_state}}, without regard to conflict-of-laws principles that would require the application of the laws of another jurisdiction.

**11.2 Forum.** Each party submits to the exclusive jurisdiction of the {{forum}} (or, if that court lacks subject-matter jurisdiction, the federal or state courts located in the State of Delaware) for any action arising out of or relating to this Agreement. [[Optional: If Purchaser primarily resides and works in California when an action is brought, any claim arising in California may be brought in a state or federal court in California, and nothing in this Agreement deprives Purchaser of the substantive protection of California law with respect to a controversy arising in California.]]

**11.3 Notices.** Notices under this Agreement must be in writing and delivered personally, by email, by nationally recognized overnight courier, or by certified mail, to the Company at its principal executive office, attention: Secretary, with a copy to {{company_notice_email}}, and to Purchaser at the address or email below Purchaser's signature (or another address a party designates by notice). Notices are effective as provided in Section 16.9 of the Plan.

**11.4 Entire Agreement.** This Agreement (including its exhibits) and the Plan constitute the entire agreement of the parties about the Shares and supersede all prior and contemporaneous agreements and understandings about them, other than any written agreement providing for acceleration of vesting referred to in Section 2.3.

**11.5 Amendment and Waiver.** This Agreement may be amended only by a writing signed by the Company and Purchaser, except as permitted by Section 15.4 of the Plan. No waiver is effective unless in writing and signed by the party against whom it is asserted.

**11.6 Successors and Assigns.** The Company may assign any of its rights under this Agreement. Subject to the transfer restrictions in it, this Agreement binds and benefits the parties and their respective successors and assigns, and Purchaser's heirs, executors, administrators, and legal representatives.

**11.7 Severability.** If any provision of this Agreement is held invalid or unenforceable, it will be enforced to the maximum extent permissible and the remaining provisions will remain in full force and effect.

**11.8 Counterparts; Electronic Signatures.** This Agreement may be executed in counterparts, each of which is an original and all of which together are one instrument. Electronic signatures are effective to the same extent as manual signatures under the Electronic Signatures in Global and National Commerce Act (15 U.S.C. § 7001 et seq.), the Delaware Uniform Electronic Transactions Act (6 Del. C. ch. 12A), and Section 116 of the Delaware General Corporation Law.

**11.9 Specific Performance.** Purchaser agrees that the Company would be irreparably harmed by a breach of Sections 3, 4, or 5 and is entitled to specific performance and injunctive relief, without posting a bond, in addition to any other remedy.

**11.10 Further Assurances.** Each party shall execute any further documents and take any further action reasonably requested by the other to carry out this Agreement, including any lock-up agreement requested by underwriters under Section 12.3 of the Plan.

**11.11 Construction.** Headings are for convenience only. "Including" means "including without limitation." "Or" is not exclusive. References to Sections and Exhibits are to sections of and exhibits to this Agreement unless otherwise stated.

**11.12 Expenses.** Each party bears its own expenses in connection with this Agreement.

**11.13 Independent Counsel.** Purchaser acknowledges that the Company's counsel represents the Company and not Purchaser, and that Purchaser has had the opportunity to consult Purchaser's own legal, tax, and financial advisers.

| {{company_name}} | PURCHASER |
|---|---|
| By: ______________________________ | ______________________________ |
| Name: {{signatory_name}} | {{participant_name}} |
| Title: {{signatory_title}} | Address: {{participant_address}} |
| Date: ____________________ | Email: {{participant_email}} |
| | State or country of residence: __________ |

---

## EXHIBIT A — ASSIGNMENT SEPARATE FROM CERTIFICATE

FOR VALUE RECEIVED, and under the Restricted Stock Purchase Agreement dated {{effective_date}} (the "**Agreement**"), the undersigned sells, assigns, and transfers to {{company_name}}, a Delaware corporation (the "**Company**"), or its assignee, __________ shares of the Common Stock of the Company standing in the undersigned's name on the books of the Company [[Optional: represented by Certificate No. ______]], and irrevocably appoints the Secretary of the Company, with full power of substitution, as attorney-in-fact to transfer those shares on the books of the Company.

Dated: ____________________

______________________________
{{participant_name}}

*Instruction: Do not fill in any blank other than the signature line. This assignment is used only to exercise the Repurchase Option under the Agreement.*

---

## EXHIBIT B — JOINT ESCROW INSTRUCTIONS

To: {{escrow_agent_name}}, as Escrow Agent, c/o {{company_name}}

Dated: {{effective_date}}

The undersigned Purchaser and {{company_name}}, a Delaware corporation (the "**Company**"), instruct you (the "**Escrow Agent**") to hold, as escrow agent, the Unvested Shares purchased under the Restricted Stock Purchase Agreement dated {{effective_date}} (the "**Agreement**") and the Assignment Separate from Certificate delivered with it, on the following terms. Capitalized terms not defined here have the meanings given in the Agreement.

1. **Repurchase.** If the Company (or its assignee) exercises, or is deemed to exercise, the Repurchase Option, the Company shall give Purchaser and you written notice specifying the number of Unvested Shares to be repurchased, the Repurchase Price, and the time for a closing. Purchaser and the Company irrevocably authorize and direct you to close the transaction contemplated by that notice in accordance with the Agreement.

2. **Closing.** At the closing, you shall (a) date the Assignment Separate from Certificate as necessary, (b) fill in the number of Shares being transferred, (c) deliver it, together with any certificate evidencing the Shares, to the Company or its assignee against the simultaneous delivery to you of the Repurchase Price, and (d) deliver the Repurchase Price to Purchaser.

3. **Power of Attorney.** Purchaser irrevocably appoints you as Purchaser's attorney-in-fact and agent for the term of this escrow to execute, with respect to the Unvested Shares, all documents necessary or appropriate to make them negotiable and to complete any transaction contemplated by these instructions. This power of attorney is coupled with an interest.

4. **Release.** On written request of Purchaser, but no more than once per calendar year (unless the Company agrees otherwise), you shall deliver to Purchaser the Shares that have vested. Within one hundred twenty (120) days after the termination of Purchaser's Continuous Service, you shall deliver to Purchaser all vested Shares not repurchased.

5. **Duties; Liability; Indemnity.** Your duties are only those expressly set out in these instructions. You may rely on any notice, signature, or document you believe in good faith to be genuine and are not liable for any act or omission made in good faith. If you receive conflicting instructions, you may refrain from acting until the conflict is resolved by the parties or by a court. The Company shall indemnify you against any loss, cost, or expense (including reasonable attorneys' fees) arising out of your service as Escrow Agent, other than from your gross negligence or willful misconduct.

6. **Successor.** You may resign on ten (10) days' written notice. If you resign or cease to be an Officer or employee of the Company, the Company's Secretary (or, if you were the Secretary, the Chief Executive Officer) will become successor Escrow Agent.

7. **Termination.** This escrow terminates when all Shares have been released or repurchased.

8. **Governing Law; Counterparts.** These instructions are governed by the laws of the State of {{governing_law_state}} and may be signed in counterparts and by electronic signature.

| {{company_name}} | PURCHASER | ESCROW AGENT |
|---|---|---|
| By: ____________________ | ____________________ | ____________________ |
| Name: {{signatory_name}} | {{participant_name}} | {{escrow_agent_name}} |
| Title: {{signatory_title}} | | |

---

## EXHIBIT C — SPOUSAL CONSENT

I, {{spouse_name}}, am the spouse or registered domestic partner of {{participant_name}}. I acknowledge that I have read the {{plan_name}} of {{company_name}} (the "**Company**") and the Restricted Stock Purchase Agreement dated {{effective_date}} (together, the "**Agreements**"), and that I know their contents. I am aware that the Agreements give the Company a Repurchase Option on Unvested Shares and a right of first refusal, and impose transfer restrictions and a market stand-off on the shares my spouse or partner purchased (the "**Shares**"), including any interest I may have in them.

I agree that my spouse's or partner's interest in the Shares is subject to the Agreements, and that any interest I may have in the Shares (including any community property interest) is irrevocably bound by the Agreements. I appoint my spouse or partner as my attorney-in-fact with respect to the exercise of any rights and the giving of any consents under the Agreements, and I agree to take any further action necessary to make the Agreements binding on my interest. I understand that I may seek independent legal advice before signing this consent, and I have either done so or freely chosen not to.

Dated: ____________________

______________________________
{{spouse_name}}

---

## EXHIBIT D — SECTION 83(b) ELECTION

Use the Section 83(b) election form in [83b-election-package](../founders/83b-election-package.md) (or IRS Form 15620), completed for the Shares. The election must include the information required by Treasury Regulations Section 1.83-2(e) (taxpayer name, address, and taxpayer identification number; description of the Shares; date of transfer and taxable year; the nature of the restrictions, here the Repurchase Option; the fair market value at transfer determined without regard to lapse restrictions; the amount paid; and a statement that copies have been furnished as required). File it with the Internal Revenue Service within thirty (30) days after the Purchase Date and deliver a copy to the Company.

> **Drafting note:** If the purchase price equals FMV, the election reports $0 of income and costs nothing; failing to file means ordinary income on each vesting date measured at the then-current value. Update the link if the 83(b) package lives at a different path.
