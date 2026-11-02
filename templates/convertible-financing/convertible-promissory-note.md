---
id: convertible-promissory-note
title: Convertible Promissory Note
category: convertible-financing
stage: convertible
signers: [Company (by an officer)]
authorities:
  - "8 Del. C. §§ 122(13) (power to borrow and issue notes), 141(f), 152, 153, 157 (conversion right as a right to acquire stock), 161"
  - "8 Del. C. §§ 151, 242 (authorizing a new series of preferred into which notes convert)"
  - "Securities Act §§ 3(a)(9), 4(a)(2); 17 C.F.R. §§ 230.502(d), 230.506; 17 C.F.R. § 230.144(d)(3)(ii)"
  - "6 Del. C. §§ 2301(c), 2306 (Delaware usury; corporate borrowers); Cal. Const. art. XV § 1; Cal. Corp. Code § 25118; N.Y. Gen. Oblig. Law § 5-521; N.Y. Penal Law § 190.40"
  - "26 U.S.C. §§ 163(e), 1272, 1273 (OID), 7872 (below-market loans), 871(h), 881(c) (portfolio interest; registered form), 1202(i)(1)"
  - "Treas. Reg. §§ 1.1273-1(c), 1.1275-2(h), 1.1275-4(a)(4), 5f.103-1"
use_when: The company is selling convertible debt to investors under a note purchase agreement and needs the note itself, converting automatically in a priced preferred financing at the lesser of a discount price and a cap price.
do_not_use_when: The investors will accept a SAFE (use the YC forms via safe-guide), the instrument is a simple loan with no conversion (use a promissory note form), or the lender is a bank or venture lender (use a loan and security agreement).
related: [convertible-note-purchase-agreement, board-consent-convertible-financing, investor-questionnaire, safe-guide, convertible-financing-checklist]
sources:
  - name: "Series Seed documents (CC0 1.0) — structure of the priced alternative and conversion-share terms (reference)"
    url: https://www.seriesseed.com
  - name: "Y Combinator — Post-Money SAFE and User Guide (definitions of Company Capitalization and shadow series used for comparison; not copied)"
    url: https://www.ycombinator.com/documents
  - name: "6 Del. C. ch. 23 (interest; usury) — official Delaware Code"
    url: https://delcode.delaware.gov/title6/c023/index.html
  - name: "Cal. Corp. Code § 25118 (usury exemption for evidences of indebtedness)"
    url: https://california.public.law/codes/ca_corp_code_section_25118
  - name: "17 C.F.R. § 230.144 (Rule 144 holding period and conversion tacking) — eCFR"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230/section-230.144
  - name: "Carta, State of Pre-Seed Q1 2025 (median note interest rate) and Osler 2025 Deal Points (median discount) — market terms (see references/convertible-instruments.md § 13)"
    url: https://carta.com/data/state-of-pre-seed-q1-2025/
last_verified: 2026-11-02
---

# Convertible Promissory Note

## About this template

### 1. What this document does

This is the debt instrument issued to each purchaser under the [convertible-note-purchase-agreement](convertible-note-purchase-agreement.md) (the "Purchase Agreement"). Every note in the series uses this same form, differing only in holder, principal, and issue date. The note:

- evidences a loan of the principal amount, accruing **simple, non-compounding interest** computed on actual days elapsed over a 365-day year;
- matures on a stated date unless earlier converted or repaid;
- **converts automatically** at the initial closing of a **Qualified Financing** (a priced preferred round of at least a stated amount of new money) at the **lesser of the Discount Price and the Cap Price**, with the cap measured against a capitalization definition the parties choose from four alternatives;
- gives the holder a choice on a **Change of Control** (repayment plus a premium, or conversion into common at the cap);
- provides for **conversion or repayment at maturity**;
- prohibits prepayment without Majority Holder consent;
- contains events of default, waiver of presentment, a usury savings clause, transfer restrictions, a note register, legends, no stockholder rights, and Majority Holder amendment with protections against disproportionate treatment.

Sign order: board consent → Purchase Agreement and investor questionnaires → funding → the Company signs and delivers this note. The note is signed by the Company only; the holder is bound by the Purchase Agreement (which incorporates the note's amendment and subordination terms).

### 2. Business terms and market positions

| Term | Company-favorable | Market | Holder-favorable | Form default |
|---|---|---|---|---|
| Interest rate | 2%–4% (at or above AFR) | 5%–8% (Carta reports a 7% median in Q1 2025; Osler reports medians of 8.0% for 2024 and 7.0% for 2025) | 8%+ | `{{interest_rate}}` simple |
| Maturity | 24–36 months | 18–24 months | 12 months | `{{maturity_date}}` |
| Discount | 10%–15% | 20% (Osler 2025 median) | 25%+ | `{{discount_rate}}` |
| Valuation cap | High, pre-money excluding new pool and converting securities | Negotiated; basis often unstated (a drafting error) | Low; fully diluted including pool increase and all converting securities | Alternatives A–D |
| Qualified Financing threshold | Low (e.g., aggregate note principal) | $1,000,000–$3,000,000 of new money | High (keeps optional conversion) | `{{qualified_financing_amount}}` |
| Change of Control | Repay principal + interest only | Holder elects 1×–2× principal premium or conversion at cap | Greater of 2× and as-converted value | Holder election; premium alternatives |
| Maturity outcome | Automatic conversion into common at cap | Holder (or Majority) election of conversion or repayment | Repayment on demand | Alternatives |
| Prepayment | Permitted on notice | Only with Majority Holder consent | Prohibited | Majority consent |
| Amendment | Company + Majority Holders, broad | Majority with sacred-rights protections | Each holder | Majority with protections |

### 3. Conversion math (stated precisely in Section 3 of the Form)

- **Conversion Amount** = Outstanding principal + accrued unpaid interest (or principal only, if the alternative paying interest in cash is chosen).
- **Discount Price** = Qualified Financing Price × (1 − Discount).
- **Cap Price** = Valuation Cap ÷ Cap Capitalization.
- **Conversion Price** = the lesser of the Discount Price and the Cap Price (and never more than the Qualified Financing Price).
- **Conversion Shares** = Conversion Amount ÷ Conversion Price, rounded down to a whole share.

**Cap Capitalization alternatives** (choose one; the calculator's `cap_basis` values are in brackets):

| Alternative | Includes the round's pool increase? | Includes Converting Securities? | Effect |
|---|---|---|---|
| A [`pre_money_excluding_new_pool`] | No | No | Company-favorable; highest Cap Price |
| B [`pre_money_including_new_pool`] | Yes | No | Holder protected from the pool top-up |
| C [`fully_diluted_including_converting`] | Yes | Yes | Holder-favorable; cap behaves like a post-money cap measured after the pool increase |
| D [`post_money`] | Only to the extent of promised grants exceeding the existing pool (YC-style) | Yes | Matches a post-money SAFE; use when notes and post-money SAFEs coexist |

Alternatives C and D are circular (the denominator includes the note's own conversion shares); the Form instructs a simultaneous calculation. References/convertible-instruments.md Examples 5 and 5B show the same $12,000,000 cap converting at $1.2000 (A) and $1.1470 (C). Model every case with `scripts/conversion_calculator.py`.

### 4. Statutory and regulatory requirements

- **Corporate authority.** Borrowing and issuing notes: 8 Del. C. § 122(13). The conversion feature is a right to acquire stock that the board should approve (8 Del. C. § 157). The board consent template authorizes the series and the maximum principal.
- **Shares into which the note converts.** A Delaware corporation cannot issue (or reserve) shares of a class or series its certificate of incorporation does not authorize (8 Del. C. §§ 151, 161). Most startups authorize only common at formation; the preferred (including any shadow series) is authorized in the amended and restated charter adopted at the Qualified Financing (8 Del. C. § 242: board and stockholder approval). Section 3.9 obligates the company to authorize enough shares then, and to keep enough common authorized and reserved for maturity and change-of-control conversions.
- **Securities law.** Notes are securities (*Reves v. Ernst & Young*, 494 U.S. 56 (1990)); the conversion shares are offered at the same time. Rule 506(b) or 506(c); Form D within 15 calendar days after the first sale; state notices. Conversion of a note into stock of the same issuer, with no commission paid, is exempt under Securities Act § 3(a)(9), and the Rule 144 holding period of the conversion shares tacks to the note's purchase date (17 C.F.R. § 230.144(d)(3)(ii)). Legends: Rule 502(d)(3).
- **Usury.**
  - *Delaware:* no corporation may interpose the defense of usury (6 Del. C. § 2306), and there is no rate ceiling for loans over $100,000 not secured by a mortgage on the borrower's principal residence (6 Del. C. § 2301(c)). Delaware governing law is the default.
  - *California:* the California Constitution caps non-exempt loans (art. XV, § 1); Cal. Corp. Code § 25118(b) exempts evidences of indebtedness aggregating at least $300,000 in original face amount at issuance, and § 25118(a) exempts issuers (or affiliate guarantors) with total assets of at least $2,000,000 on recent qualifying financial statements, in each case only if the lender and issuer have a preexisting relationship or the capacity to protect their own interests (§ 25118(f)). A small note round governed by California law may fall outside the exemption; keep the rate modest and the governing law Delaware.
  - *New York:* corporations may not plead civil usury (N.Y. Gen. Oblig. Law § 5-521) but may assert criminal usury (25% per annum, N.Y. Penal Law § 190.40), and the New York Court of Appeals has held that the value of a conversion discount can count toward interest and that a criminally usurious loan is void (*Adar Bays, LLC v. GeneSYS ID, Inc.*, 37 N.Y.3d 320 (2021)). Avoid New York governing law for discounted convertible notes.
  - The Form includes a usury savings clause (Article 11) as a backstop, not a substitute for a reasonable rate.
- **Tax.**
  - *OID.* Interest that accrues and is paid only at maturity or converts is not "qualified stated interest" (Treas. Reg. § 1.1273-1(c)), so the note has original issue discount; holders include it in income as it accrues (I.R.C. § 1272) and the company may deduct it as it accrues (I.R.C. § 163(e)). The company's accountant should confirm Form 1099-OID/1099-INT reporting.
  - *Contingent payment rules.* Debt convertible into the issuer's stock is generally excluded from the contingent payment debt instrument rules (Treas. Reg. § 1.1275-4(a)(4)); change-of-control premiums should be reviewed under the remote and incidental contingency rules (Treas. Reg. § 1.1275-2(h)).
  - *AFR / below-market loans.* Set the rate at or above the applicable federal rate for the note's term (short-term AFR for 3 years or less) when holders are or may become stockholders, to avoid § 7872 issues.
  - *QSBS.* Stock received on conversion is treated as acquired on the conversion date for § 1202 purposes (§ 1202(i)(1)(A)), with basis not less than the fair market value of the note (§ 1202(i)(1)(B)).
  - *Foreign holders.* The note register in Section 8.3 keeps the note in registered form, a condition of the portfolio interest exemption (I.R.C. §§ 871(h), 881(c); Treas. Reg. § 5f.103-1); collect Form W-8BEN or W-8BEN-E.

> **Verify:** Confirm the applicable federal rate for the month of issuance (IRS monthly revenue ruling) before fixing `{{interest_rate}}`, and confirm with the company's tax adviser the OID reporting position and whether any foreign holder's conversion right affects portfolio interest eligibility.

### 5. Common mistakes this form avoids

1. **Undefined cap basis** ("$8M cap" with no capitalization definition). Section 1 forces a choice among four definitions.
2. **Compounding interest by accident** ("interest at 6% per annum" with no method). Section 2.2 states simple, actual/365.
3. **Conversion into a series that does not exist.** Section 3.9 obligates authorization at the Qualified Financing; the drafting note explains why preferred cannot be reserved now.
4. **Liquidation-preference overhang.** Section 3.7 provides a shadow series (or the split-issuance alternative).
5. **No maturity outcome.** Section 3.3 specifies what happens if no Qualified Financing occurs.
6. **Individual holders blocking amendments,** or majorities stripping minorities. Section 7 sets Majority Holder amendment with sacred rights.
7. **Prepayment before an upside event.** Section 2.6 requires Majority Holder consent.
8. **Lost portfolio-interest eligibility** for foreign holders because the note is in bearer form. Section 8.3 keeps a register.

### 6. Deadlines triggered

| Trigger | Deadline | Source |
|---|---|---|
| First sale of notes | Form D within 15 calendar days; state notices (e.g., California 15 days, $300) | 17 C.F.R. § 230.503; Cal. Corp. Code § 25102.1(d) |
| Qualified Financing anticipated | Company notice to holders at least `{{financing_notice_days}}` days before closing | Section 3.8 |
| Change of Control anticipated | Company notice at least `{{coc_notice_days}}` days before closing; holder election within `{{coc_election_days}}` days | Section 3.4 |
| Maturity approaching | Company notice at least `{{maturity_notice_days}}` days before the Maturity Date | Section 3.3 |
| Annual tax reporting | OID/interest information returns (confirm with accountant) | I.R.C. § 6049 |

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | Shared |
| `{{company_address}}`, `{{company_notice_email}}` | Notice details | | Shared |
| `{{note_number}}` | Note serial number | CN-003 | Matches the note register |
| `{{investor_name}}` | Holder | Example Ventures Fund I, L.P. | Shared |
| `{{investor_address}}`, `{{investor_email}}` | Holder notice details | | Shared |
| `{{purchase_amount}}` | Original principal amount | $500,000 | Shared |
| `{{purchase_amount_words}}` | Principal in words | Five Hundred Thousand Dollars | |
| `{{issue_date}}` | Date of issuance (funding) | January 15, 2027 | Interest accrues from this date |
| `{{purchase_agreement_date}}` | Date of the Purchase Agreement | January 15, 2027 | |
| `{{interest_rate}}` | Simple annual interest rate | 6% | Shared; at or above AFR |
| `{{default_interest_increment}}` | Increase in rate after an Event of Default | 2% | Optional |
| `{{maturity_date}}` | Maturity Date | January 15, 2029 | Shared |
| `{{discount_rate}}` | Discount off the Qualified Financing Price | 20% discount | Shared; write as the discount |
| `{{valuation_cap}}` | Valuation cap | $12,000,000 | Shared |
| `{{qualified_financing_amount}}` | Minimum new money for a Qualified Financing | $2,000,000 | Excludes conversion of notes and SAFEs |
| `{{coc_premium_multiple}}` | Change of control repayment multiple of principal | 2 | e.g., 1 = principal only; 2 = 2× principal |
| `{{coc_notice_days}}`, `{{coc_election_days}}` | Change of control notice and election periods | 15; 10 | Days |
| `{{financing_notice_days}}` | Qualified Financing notice | 10 | Days |
| `{{maturity_notice_days}}` | Notice before maturity | 30 | Days |
| `{{maturity_election_days}}` | Holder election period at maturity | 15 | Days |
| `{{payment_default_grace_days}}` | Grace period for payment defaults | 5 | Business Days |
| `{{covenant_cure_days}}` | Cure period for covenant defaults | 30 | Optional |
| `{{cross_default_threshold}}` | Cross-default threshold | $250,000 | Optional |
| `{{senior_debt_description}}` | Debt to which notes are subordinated | indebtedness to banks, venture lenders, and equipment lessors | Optional Article 5 |
| `{{governing_law_state}}` | Governing law | Delaware | Shared |
| `{{forum}}` | Exclusive forum | Court of Chancery of the State of Delaware | Shared |
| `{{signatory_name}}`, `{{signatory_title}}` | Officer signing | Alex Rivera, Chief Executive Officer | Shared |
| `{{investor_signatory_name}}`, `{{investor_signatory_title}}` | Holder signatory for the optional acknowledgment | | Entities |
| `{{qualified_financing_price}}`, `{{discount_price}}`, `{{cap_capitalization}}`, `{{cap_capitalization_alternative}}`, `{{cap_price}}`, `{{conversion_price}}` | Exhibit B conversion statement values | $2.2985; $1.8388; 10,000,000; A; $1.2000; $1.2000 | From `scripts/conversion_calculator.py` |
| `{{interest_days}}`, `{{accrued_interest}}`, `{{conversion_amount}}` | Interest computation | 365; $30,000.00; $530,000.00 | Simple, actual/365 |
| `{{conversion_shares}}`, `{{conversion_series_name}}`, `{{cash_in_lieu}}` | Shares, series, and cash for fractions | 441,666; Series A-1 Preferred Stock; $0.80 | Series name must match the A&R charter |
| `{{model_run_date}}` | Date of the conversion model run | January 10, 2028 | |

## Form

---

THIS NOTE AND THE SECURITIES ISSUABLE ON ITS CONVERSION HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933, AS AMENDED (THE "SECURITIES ACT"), OR THE SECURITIES LAWS OF ANY STATE, AND ARE BEING OFFERED AND SOLD IN RELIANCE ON EXEMPTIONS FROM THOSE REQUIREMENTS. THEY MAY NOT BE SOLD, PLEDGED, OR OTHERWISE TRANSFERRED WITHOUT AN EFFECTIVE REGISTRATION STATEMENT UNDER THE SECURITIES ACT AND APPLICABLE STATE SECURITIES LAWS OR AN AVAILABLE EXEMPTION FROM REGISTRATION. THIS NOTE IS SUBJECT TO RESTRICTIONS ON TRANSFER SET FORTH IN SECTION 8 AND IN THE NOTE PURCHASE AGREEMENT REFERRED TO BELOW[[Optional: , AND IS SUBORDINATED TO SENIOR INDEBTEDNESS AS PROVIDED IN ARTICLE 5]].

# {{company_name}}

## CONVERTIBLE PROMISSORY NOTE

| | |
|---|---|
| Note No. | {{note_number}} |
| Original Principal Amount | {{purchase_amount}} |
| Issue Date | {{issue_date}} |
| Maturity Date | {{maturity_date}} |
| Holder | {{investor_name}} |

FOR VALUE RECEIVED, {{company_name}}, a Delaware corporation (the "**Company**"), promises to pay to {{investor_name}} or its registered assigns (the "**Holder**") the principal sum of {{purchase_amount_words}} ({{purchase_amount}}), or so much of it as remains outstanding, together with interest on the outstanding principal amount, in each case as and when provided in this Note.

This Note is one of a series of Convertible Promissory Notes of like tenor (except as to holder, principal amount, and issue date) (collectively, the "**Notes**") issued under the Note Purchase Agreement dated {{purchase_agreement_date}}, among the Company and the purchasers named in it (as amended from time to time, the "**Purchase Agreement**"). The Holder is entitled to the benefits of, and is bound by, the Purchase Agreement.

## ARTICLE 1. DEFINITIONS AND INTERPRETATION

**1.1 Definitions.** In this Note:

"**Affiliate**" means, with respect to a person, any other person that directly or indirectly controls, is controlled by, or is under common control with that person, including any investment fund managed or advised by the same general partner, managing member, or management company.

"**Business Day**" means any day other than a Saturday, Sunday, or day on which banks in New York, New York are authorized or required to close.

"**Cap Capitalization**" means:

[[Alternative A: the sum, as of immediately before the initial closing of the Qualified Financing, without duplication and on an as-converted-to-Common-Stock basis, of (a) all shares of Capital Stock issued and outstanding; (b) all shares of Capital Stock issuable on exercise or settlement of all outstanding options, warrants, restricted stock units, and other rights to acquire Capital Stock, whether or not vested or exercisable; and (c) all shares of Common Stock reserved and available for future grant under the Company's equity incentive plans immediately before that closing, **excluding** any increase in the reserve made in connection with the Qualified Financing; but **excluding** all shares issuable on conversion of the Notes and of any other Converting Securities.]]

[[Alternative B: the sum, as of immediately before the initial closing of the Qualified Financing, without duplication and on an as-converted-to-Common-Stock basis, of (a) all shares of Capital Stock issued and outstanding; (b) all shares of Capital Stock issuable on exercise or settlement of all outstanding options, warrants, restricted stock units, and other rights to acquire Capital Stock, whether or not vested or exercisable; and (c) all shares of Common Stock reserved and available for future grant under the Company's equity incentive plans, **including** any increase in the reserve made in connection with the Qualified Financing; but **excluding** all shares issuable on conversion of the Notes and of any other Converting Securities.]]

[[Alternative C: the sum, as of immediately before the initial closing of the Qualified Financing, without duplication and on an as-converted-to-Common-Stock basis, of (a) all shares of Capital Stock issued and outstanding; (b) all shares of Capital Stock issuable on exercise or settlement of all outstanding options, warrants, restricted stock units, and other rights to acquire Capital Stock, whether or not vested or exercisable; (c) all shares of Common Stock reserved and available for future grant under the Company's equity incentive plans, **including** any increase in the reserve made in connection with the Qualified Financing; and (d) all shares issuable on conversion of the Notes and of all other Converting Securities in connection with the Qualified Financing, at their actual conversion prices.]]

[[Alternative D: the sum, as of immediately before the initial closing of the Qualified Financing, without duplication and on an as-converted-to-Common-Stock basis, of (a) all shares of Capital Stock issued and outstanding; (b) all shares of Capital Stock issuable on exercise or settlement of all outstanding options, warrants, restricted stock units, and other rights to acquire Capital Stock, whether or not vested or exercisable, and all promised but ungranted awards; (c) all shares of Common Stock reserved and available for future grant under the Company's equity incentive plans immediately before that closing, **excluding** any increase in the reserve made in connection with the Qualified Financing except to the extent necessary to cover promised but ungranted awards that exceed the reserve before the increase; and (d) all shares issuable on conversion of the Notes and of all other Converting Securities in connection with the Qualified Financing, at their actual conversion prices.]]

> **Drafting note:** Alternative A is company-favorable; B protects the holder from the pool top-up; C is the most holder-favorable; D mirrors the YC post-money SAFE and suits a cap table that already has post-money SAFEs. Whichever is chosen, use the same definition in every Note in the series and say whether the cap is "pre-money" (A or B) or "post-money" (C or D) in the term sheet.

"**Cap Price**" means the Valuation Cap divided by the Cap Capitalization.

"**Capital Stock**" means the Common Stock, the Preferred Stock, and any other class or series of capital stock of the Company.

"**Change of Control**" means (a) a merger, consolidation, or other reorganization of the Company with or into another entity, other than one in which the holders of the Company's voting securities immediately before the transaction continue to hold, immediately after it and in substantially the same proportions, a majority of the voting power of the surviving or resulting entity (or its parent); (b) a transaction or series of related transactions in which any person or group (within the meaning of Section 13(d)(3) of the Securities Exchange Act of 1934) acquires beneficial ownership of more than fifty percent (50%) of the Company's outstanding voting power; or (c) a sale, lease, exclusive license, or other disposition of all or substantially all of the Company's assets (determined on a consolidated basis); except that none of the following is a Change of Control: (i) a bona fide equity financing for capital-raising purposes in which cash is received by the Company; (ii) a transaction whose sole purpose is to change the Company's jurisdiction of incorporation or to create a holding company owned in substantially the same proportions by the persons who held the Company's securities immediately before the transaction; or (iii) an initial public offering or direct listing.

"**Change of Control Capitalization**" means the sum, as of immediately before the closing of the Change of Control, without duplication and on an as-converted-to-Common-Stock basis, of all shares of Capital Stock issued and outstanding and all shares issuable on exercise or settlement of all outstanding options, warrants, restricted stock units, and other rights to acquire Capital Stock (whether or not vested or exercisable), but excluding unallocated shares reserved under equity incentive plans and shares issuable on conversion of the Notes and other Converting Securities.

"**Common Stock**" means the Company's common stock, par value as stated in its certificate of incorporation.

"**Conversion Amount**" means, as of any conversion, [[Alternative A: the Outstanding Balance]] [[Alternative B: the outstanding principal amount of this Note, with all accrued and unpaid interest payable in cash on the date of conversion]].

"**Conversion Price**" means the price per share determined under Section 3.1(b).

"**Converting Securities**" means the Notes and all other securities of the Company that are convertible into or exercisable for Capital Stock in connection with a Qualified Financing (including simple agreements for future equity and other convertible promissory notes), other than options and other awards under equity incentive plans and warrants issued to lenders.

"**Discount**" means {{discount_rate}}.

"**Discount Price**" means the Qualified Financing Price multiplied by one minus the Discount.

"**Equity Securities**" means Capital Stock and any securities convertible into, exercisable for, or exchangeable for Capital Stock, other than options and other awards under equity incentive plans approved by the Company's board of directors.

"**Event of Default**" has the meaning given in Section 4.1.

"**Majority Holders**" means the holders of Notes representing more than fifty percent (50%) of the aggregate outstanding principal amount of all Notes then outstanding.

"**Maturity Date**" means {{maturity_date}}, as it may be extended under Section 3.3(d) or Article 7.

"**New Money**" means cash received by the Company from the sale of Equity Securities in a financing, excluding amounts received on conversion or cancellation of the Notes or other Converting Securities.

"**Outstanding Balance**" means, at any time, the outstanding principal amount of this Note plus all accrued and unpaid interest on it.

"**Preferred Stock**" means the Company's preferred stock, of any series.

"**Qualified Financing**" means the first transaction or series of related transactions after the Issue Date in which the Company sells and issues shares of Preferred Stock for capital-raising purposes at a fixed price per share and receives aggregate New Money of at least {{qualified_financing_amount}} (including New Money received at closings that occur within ninety (90) days after the initial closing).

"**Qualified Financing Price**" means the lowest price per share at which the Company sells shares of Preferred Stock for cash to new-money investors in the Qualified Financing.

"**Qualified Financing Stock**" means the series of Preferred Stock sold to new-money investors in the Qualified Financing.

"**Senior Indebtedness**" has the meaning given in Article 5.

"**Shadow Preferred Stock**" has the meaning given in Section 3.7.

"**Valuation Cap**" means {{valuation_cap}}.

**1.2 Interpretation.** In this Note: "including" means "including without limitation"; "or" is not exclusive; references to Articles and Sections are to this Note; headings are for convenience only; "days" means calendar days unless Business Days are specified; references to an agreement or instrument include it as amended in accordance with its terms; and no provision is to be construed against a party because it drafted the provision.

## ARTICLE 2. PAYMENT TERMS

**2.1 Principal and Maturity.** Unless this Note has been converted under Article 3 or repaid, the Company shall pay the Outstanding Balance to the Holder on the Maturity Date (or on such earlier date as the Outstanding Balance becomes due under Section 3.4 or Article 4), subject to the conversion elections in Section 3.3.

**2.2 Interest.** Simple interest accrues on the outstanding principal amount of this Note from and including the Issue Date to but excluding the date on which the principal is paid in full or converted, at the rate of {{interest_rate}} per annum, computed on the basis of a 365-day year and the actual number of days elapsed. Interest does not compound. Accrued interest is payable on the Maturity Date (or on earlier payment of principal) unless it converts under Article 3.

**2.3 Default Interest.** [[Optional: While an Event of Default is continuing, the interest rate in Section 2.2 is increased by {{default_interest_increment}} per annum, computed in the same manner, but in no event above the maximum rate permitted under Article 11.]]

**2.4 Manner of Payment.** All payments shall be made in lawful money of the United States by wire transfer of immediately available funds to the account the Holder designates in writing, without set-off or counterclaim. A payment due on a day that is not a Business Day is due on the next Business Day, and interest accrues to that day. Each payment is applied first to costs of collection payable under Section 4.3, then to accrued interest, and then to principal.

**2.5 Pro Rata Treatment.** All payments of principal and interest on the Notes (other than payments on conversion) shall be made to the holders of the Notes pro rata in proportion to the Outstanding Balances then owed to them. If any holder receives a payment in excess of its pro rata share, it shall hold the excess in trust for, and promptly pay it over to, the other holders so that each receives its pro rata share.

**2.6 Prepayment.** The Company may not prepay this Note, in whole or in part, without the prior written consent of the Majority Holders. Any permitted prepayment shall be made on all Notes pro rata under Section 2.5 and shall include all accrued interest on the principal prepaid.

**2.7 Taxes.** The Company may deduct and withhold from any payment (including any issuance of shares in respect of accrued interest) amounts required to be withheld under applicable tax law; amounts so withheld and paid to the appropriate authority are treated as paid to the Holder. The Holder shall deliver to the Company a properly completed IRS Form W-9 or applicable Form W-8 on or before the Issue Date and an updated form when the prior form becomes obsolete or inaccurate.

## ARTICLE 3. CONVERSION

**3.1 Automatic Conversion in a Qualified Financing.**

(a) *Conversion.* Effective on the initial closing of a Qualified Financing that occurs before the Maturity Date and before the Outstanding Balance is paid in full, the Conversion Amount automatically converts, without any further action of the Holder, into the number of shares (the "**Conversion Shares**") of [[Alternative A: Shadow Preferred Stock]] [[Alternative B: Qualified Financing Stock]] [[Alternative C: Qualified Financing Stock and Common Stock allocated as provided in Section 3.7(b)]] equal to the Conversion Amount divided by the Conversion Price, rounded down to the nearest whole share.

(b) *Conversion Price.* The "**Conversion Price**" is the lesser of:

[[Alternative A: (i) the Discount Price; and (ii) the Cap Price.]]

[[Alternative B: (i) the Qualified Financing Price; and (ii) the Cap Price. (No discount applies.)]]

[[Alternative C: the Discount Price. (No valuation cap applies.)]]

Expressed as formulas:

> Conversion Shares = Conversion Amount ÷ Conversion Price
>
> Discount Price = Qualified Financing Price × (1 − Discount)
>
> Cap Price = Valuation Cap ÷ Cap Capitalization
>
> Conversion Price = the lesser of the Discount Price and the Cap Price

In no event shall the Conversion Price exceed the Qualified Financing Price.

(c) *Simultaneous determination.* If the Cap Capitalization includes shares issuable on conversion of the Notes or other Converting Securities, or the Qualified Financing Price depends on a fully diluted share count that includes those shares or an increase in the equity incentive plan reserve, the Qualified Financing Price, each Conversion Price, the Cap Capitalization, and the number of Conversion Shares shall be determined simultaneously, by algebraic solution or iterative calculation, so that each amount is consistent with all of the others.

(d) *Rounding.* Each of the Qualified Financing Price, the Discount Price, the Cap Price, and the Conversion Price shall be calculated using unrounded values and then rounded to four (4) decimal places [[Alternative A: (with $0.00005 rounded up)]] [[Alternative B: (rounded down)]]. The Conversion Shares shall be calculated using the rounded Conversion Price and rounded down to the nearest whole share. No fractional shares shall be issued; the Company shall pay the Holder cash equal to the fraction multiplied by the Conversion Price, unless that amount is less than one dollar.

(e) *Determination by the Company.* The Company's board of directors shall determine the Cap Capitalization and the resulting amounts in good faith, using the capitalization of the Company immediately before the initial closing, and shall deliver to the Holder, with the notice under Section 3.8, a statement of its calculations in reasonable detail. Absent manifest error, the calculation binds the Company and the Holder.

**3.2 Optional Conversion in a Non-Qualified Financing.** [[Optional: If, before the Maturity Date and before this Note has been converted or repaid, the Company sells Preferred Stock for capital-raising purposes in a financing that is not a Qualified Financing, the Majority Holders may elect, by written notice to the Company delivered before the initial closing of that financing (or within ten (10) days after receiving the Company's notice of it, if later), to convert all of the Notes, on the terms of Section 3.1, as if that financing were a Qualified Financing. An election by the Majority Holders binds all holders.]]

**3.3 Maturity.**

(a) *Notice.* The Company shall notify the Holder in writing at least {{maturity_notice_days}} days before the Maturity Date if this Note remains outstanding, stating the Outstanding Balance as of the Maturity Date and the Maturity Conversion Price calculated in good faith.

(b) *Election.* [[Alternative A: At any time during the {{maturity_election_days}} days ending on the Maturity Date, the Majority Holders may elect, by written notice to the Company, to convert all of the Notes, effective on the Maturity Date, into Maturity Conversion Shares at a price per share (the "**Maturity Conversion Price**") equal to the Valuation Cap divided by the Maturity Capitalization. If the Majority Holders do not so elect, the Outstanding Balance is due and payable on the Maturity Date.]] [[Alternative B: Unless the Majority Holders elect, by written notice to the Company delivered at least five (5) Business Days before the Maturity Date, to be repaid, the Outstanding Balance of each Note automatically converts on the Maturity Date into Maturity Conversion Shares at a price per share (the "**Maturity Conversion Price**") equal to the Valuation Cap divided by the Maturity Capitalization. If the Majority Holders elect repayment, the Outstanding Balance is due and payable on the Maturity Date.]] [[Alternative C: At any time during the {{maturity_election_days}} days ending on the Maturity Date, the Holder may elect, by written notice to the Company, to convert this Note, effective on the Maturity Date, into Maturity Conversion Shares at a price per share (the "**Maturity Conversion Price**") equal to the Valuation Cap divided by the Maturity Capitalization. If the Holder does not so elect, the Outstanding Balance is due and payable on the Maturity Date.]]

(c) *Maturity Capitalization.* "**Maturity Capitalization**" means the sum, as of immediately before the conversion, without duplication and on an as-converted-to-Common-Stock basis, of all shares of Capital Stock issued and outstanding, all shares issuable on exercise or settlement of outstanding options, warrants, restricted stock units, and other rights to acquire Capital Stock (whether or not vested or exercisable), and all shares reserved and available for future grant under equity incentive plans, but excluding shares issuable on conversion of the Notes and other Converting Securities. The Maturity Conversion Price shall be rounded as provided in Section 3.1(d).

(d) *Extension.* The Majority Holders may extend the Maturity Date of all Notes by written agreement with the Company, without the consent of any other holder.

(e) *Maturity Conversion Shares.* "**Maturity Conversion Shares**" means shares of [[Alternative A: Common Stock]] [[Alternative B: a newly authorized series of Preferred Stock having rights, preferences, and privileges substantially the same as those of the Company's most senior outstanding series of Preferred Stock (or, if none is outstanding, customary for a seed-stage preferred stock financing), with an original issue price equal to the Maturity Conversion Price, which series the Company shall use its best efforts to authorize under Section 3.9(b) before the Maturity Date; and, until that series is authorized, Common Stock]].

**3.4 Change of Control.**

(a) *Notice.* The Company shall notify the Holder in writing of a proposed Change of Control at least {{coc_notice_days}} days before its anticipated closing, describing its material terms and stating the amounts payable under each option in Section 3.4(b) calculated in good faith.

(b) *Holder Election.* If a Change of Control occurs before this Note has been converted or repaid in full, the Holder may elect, by written notice to the Company within {{coc_election_days}} days after receiving the notice under Section 3.4(a) (and in any event before the closing), to receive either:

(i) **Repayment:** in cash, at the closing of the Change of Control, [[Alternative A: the Outstanding Balance plus an amount equal to {{coc_premium_multiple}} times the outstanding principal amount less the outstanding principal amount (so that the Holder receives {{coc_premium_multiple}} times principal plus accrued interest)]] [[Alternative B: the Outstanding Balance]]; or

(ii) **Conversion:** conversion of the Outstanding Balance, effective immediately before and contingent on the closing of the Change of Control, into the number of shares of Common Stock equal to the Outstanding Balance divided by the price per share equal to the Valuation Cap divided by the Change of Control Capitalization (rounded as provided in Section 3.1(d)), entitling the Holder to receive the consideration payable on those shares in the Change of Control.

(c) *Default Election.* If the Holder does not timely elect, the Holder is deemed to have elected [[Alternative A: repayment under Section 3.4(b)(i)]] [[Alternative B: whichever of the options in Section 3.4(b) would result in the greater payment to the Holder, as determined in good faith by the Company's board of directors]].

(d) *Form of Consideration.* If the holders of Common Stock may elect the form of consideration in the Change of Control, the Holder may make the same election for any consideration payable under Section 3.4(b)(ii). [[Optional: If the Change of Control is intended to qualify as a tax-free reorganization, the Company may, with the consent of the Majority Holders, reduce the cash portion of any payment under Section 3.4(b)(i) and pay the reduction in the same form of non-cash consideration paid to the holders of Common Stock (valued as in the definitive agreement), so long as the total value payable to the Holder is not reduced.]]

(e) *Priority.* Amounts payable under Section 3.4(b)(i) are indebtedness of the Company and shall be paid before any distribution to the holders of Capital Stock in the Change of Control, subject to Article 5.

**3.5 Mechanics of Conversion.**

(a) *Conditions; Documents.* As a condition to receiving Conversion Shares in a Qualified Financing, the Holder shall execute and deliver the agreements entered into by the new-money investors in the Qualified Financing (including the stock purchase agreement, investors' rights agreement, voting agreement, and right of first refusal and co-sale agreement), on the same terms as those investors, except that the Holder's representations and warranties shall be limited to customary investor representations (organization, authority, investment intent, accredited status, and similar matters), the Holder shall have no indemnification obligation for the Company's representations, and any drag-along obligation shall contain customary limitations on the Holder's liability.

(b) *Surrender.* Upon conversion the Holder shall surrender this Note (or deliver a customary affidavit of loss and indemnity, without bond) to the Company. Conversion is effective, and this Note ceases to accrue interest and represents only the right to receive the Conversion Shares (and any cash payable under this Note), at the time stated in Section 3.1, 3.2, 3.3, or 3.4, whether or not the Note has been surrendered.

(c) *Issuance.* The Company shall issue the Conversion Shares in book-entry form (or by certificate, if the Company issues certificates) registered in the Holder's name promptly after the conversion and, if the Holder has not delivered the agreements described in Section 3.5(a), may withhold delivery of the Conversion Shares until it does.

(d) *Accrued Interest.* [[Alternative A: Accrued interest converts as part of the Conversion Amount.]] [[Alternative B: Accrued interest shall be paid in cash on the date of conversion.]]

(e) *Effect.* On conversion of the entire Conversion Amount (and payment of any cash due under this Note), this Note is cancelled and all of the Company's obligations under it are satisfied.

**3.6 Equal Treatment.** All Notes shall convert on the same basis at the same time, except to the extent that a holder agrees in writing to different treatment of its own Note.

**3.7 Shadow Series; Liquidation Preference.**

(a) *Shadow Preferred Stock.* [[Alternative A: The Conversion Shares shall be shares of a separate series of Preferred Stock (the "**Shadow Preferred Stock**") having the same rights, preferences, privileges, and restrictions as the Qualified Financing Stock, except that the original issue price, the per-share liquidation preference, the initial conversion price for purposes of conversion into Common Stock and anti-dilution adjustment, and the per-share dividend rate (if any) of the Shadow Preferred Stock shall each be based on the Conversion Price rather than the Qualified Financing Price. The Shadow Preferred Stock shall vote together with the Qualified Financing Stock as a single series on all matters on which the Qualified Financing Stock votes as a separate series.]] [[Alternative B: The Conversion Shares shall be shares of Qualified Financing Stock, with the full rights, preferences, and privileges of that series.]]

(b) *Split Issuance.* [[Optional: If Alternative C of Section 3.1(a) applies, the Conversion Shares shall consist of (i) the number of shares of Qualified Financing Stock equal to the Conversion Amount divided by the Qualified Financing Price, rounded down to the nearest whole share, and (ii) a number of shares of Common Stock equal to the total number of Conversion Shares determined under Section 3.1(a) minus the number of shares issued under clause (i).]]

> **Drafting note:** Alternative A (shadow series) gives the holder a 1× preference equal to its Conversion Amount. The priced-round charter must authorize the Shadow Preferred Stock (e.g., "Series A-1 Preferred Stock") with its own original issue price; give the priced-round drafter the series name, original issue price (the Conversion Price, to four decimals), and share count. See references/convertible-instruments.md § 8.

**3.8 Notice of Qualified Financing.** The Company shall notify the Holder in writing at least {{financing_notice_days}} days before the anticipated initial closing of a Qualified Financing (or any financing that may permit an election under Section 3.2), describing its material terms (including the anticipated Qualified Financing Price, the pre-money valuation, and any increase in the equity incentive plan reserve) and stating the Company's good-faith calculation of the Conversion Price and Conversion Shares.

**3.9 Authorization and Reservation of Shares.**

(a) *Common Stock.* The Company shall at all times while this Note is outstanding keep authorized and reserved, out of its authorized but unissued Common Stock, a number of shares sufficient to effect the conversion of the Outstanding Balance of all Notes into Common Stock under Sections 3.3 and 3.4 (calculated at the Valuation Cap divided by the Company's then fully diluted capitalization), and shall take all corporate action necessary to increase its authorized Common Stock if at any time the authorized but unissued and unreserved Common Stock is insufficient for that purpose.

(b) *Preferred Stock.* Before or at the initial closing of a Qualified Financing (and before any conversion into Preferred Stock under Section 3.2 or 3.3), the Company shall take all corporate action necessary, including the adoption by its board of directors and stockholders of an amendment to or restatement of its certificate of incorporation under 8 Del. C. § 242 (or, if its certificate of incorporation so permits, a certificate of designations under 8 Del. C. § 151(g)), to authorize a sufficient number of shares of each series of Preferred Stock into which the Notes will convert, and of Common Stock issuable on conversion of that Preferred Stock.

> **Drafting note:** Preferred stock cannot be reserved for conversion of the Notes now because the series into which they convert does not yet exist and its terms will be set in the Qualified Financing. Unless the charter already authorizes "blank check" preferred, no preferred is authorized at all. The covenant in Section 3.9(b) is the substitute, and the board consent approving the Notes records it.

(c) *Validly Issued.* All Conversion Shares, when issued in accordance with this Note, shall be duly authorized, validly issued, fully paid, and non-assessable, free of preemptive rights (other than rights waived or satisfied) and of liens created by the Company, and the issuance shall be exempt from registration under the Securities Act as an exchange under Section 3(a)(9) or otherwise.

**3.10 Adjustments.** If, while this Note is outstanding and before the determination of any conversion price, the Company effects a stock split, reverse stock split, stock dividend, recapitalization, or similar transaction affecting the Common Stock, the conversion mechanics in this Article 3 shall be applied so that the Holder receives the same economic benefit it would have received had the transaction not occurred, it being understood that the Valuation Cap is a dollar amount that is not itself adjusted.

## ARTICLE 4. EVENTS OF DEFAULT AND REMEDIES

**4.1 Events of Default.** Each of the following is an "**Event of Default**":

(a) the Company fails to pay any principal or interest on any Note within {{payment_default_grace_days}} Business Days after it becomes due;

(b) the Company commences a voluntary case or proceeding under any bankruptcy, insolvency, reorganization, receivership, or similar law; consents to the entry of an order for relief in an involuntary case; consents to the appointment of a receiver, trustee, custodian, or similar official for itself or a substantial part of its property; or takes corporate action to authorize any of the foregoing;

(c) an involuntary case or proceeding is commenced against the Company under any bankruptcy, insolvency, reorganization, receivership, or similar law and is not dismissed within sixty (60) days, or an order for relief is entered against the Company in any such case;

(d) the Company makes a general assignment for the benefit of creditors, or admits in writing its inability to pay its debts generally as they become due;

(e) the Company dissolves, liquidates, or winds up, or its board of directors or stockholders approve any of the foregoing, or the Company ceases to conduct its business in the ordinary course for more than thirty (30) consecutive days;

(f) [[Optional: the Company fails to perform any covenant in this Note or in the Purchase Agreement (other than one covered by Section 4.1(a)), and the failure continues for {{covenant_cure_days}} days after the Company receives written notice of it from the Majority Holders;]]

(g) [[Optional: any representation or warranty of the Company in the Purchase Agreement was materially untrue when made, and, if capable of cure, remains uncured {{covenant_cure_days}} days after the Company receives written notice from the Majority Holders;]] and

(h) [[Optional: the Company defaults in the payment of indebtedness for borrowed money (other than the Notes) in an aggregate principal amount exceeding {{cross_default_threshold}}, and the default results in the acceleration of that indebtedness.]]

**4.2 Remedies.**

(a) *Automatic Acceleration.* On the occurrence of an Event of Default under Section 4.1(b), 4.1(c), or 4.1(d), the Outstanding Balance of all Notes automatically becomes immediately due and payable, without notice or any other action by any holder.

(b) *Optional Acceleration.* While any other Event of Default is continuing, the Majority Holders may, by written notice to the Company, declare the Outstanding Balance of all Notes immediately due and payable.

(c) *Collective Action.* Except for a suit to collect amounts that have become due and remain unpaid after acceleration under Section 4.2(a) or 4.2(b) or after the Maturity Date, no holder may exercise any remedy in respect of an Event of Default without the written consent of the Majority Holders. The Majority Holders may, by written notice to the Company, rescind an acceleration (other than an acceleration due solely to non-payment of principal or interest that remains unpaid) and waive any Event of Default.

(d) *Remedies Cumulative.* Subject to Section 4.2(c) and Article 5, the rights and remedies of the holders are cumulative and in addition to any other rights and remedies available at law or in equity.

**4.3 Costs of Collection.** If an Event of Default occurs, the Company shall pay the Holder's reasonable and documented costs of collection and enforcement, including reasonable attorneys' fees.

**4.4 Notice of Default.** The Company shall notify the Holder in writing within five (5) Business Days after any officer of the Company becomes aware of an Event of Default or of any event that, with notice or lapse of time, would become an Event of Default.

## ARTICLE 5. SUBORDINATION

[[Optional: **5.1 Agreement to Subordinate.** The indebtedness evidenced by this Note is subordinated in right of payment to the prior payment in full of all {{senior_debt_description}} for borrowed money, whether outstanding on the Issue Date or incurred later, and all refinancings of it (the "**Senior Indebtedness**"), to the extent and in the manner provided in this Article 5. The Notes rank equally with each other and senior to all Capital Stock and to all simple agreements for future equity.

**5.2 Subordination Agreement.** The Holder shall execute and deliver any subordination or intercreditor agreement reasonably requested by a holder of Senior Indebtedness that is on customary terms for subordinated convertible notes, does not reduce the principal or interest rate of this Note or extend its maturity, and is executed by the holders of all other Notes; and, if the Majority Holders execute such an agreement, the Holder's execution is deemed given.

**5.3 Conversion Not Restricted.** Nothing in this Article 5 restricts the conversion of this Note into Capital Stock or the issuance of Conversion Shares.]]

> **Drafting note:** Subordination is usually unnecessary at signing but becomes necessary if the Company later takes venture debt; providing for it in advance avoids a holder-by-holder consent later. If Article 5 is deleted, delete the reference to it in the legend and in Section 4.2(d), and renumber.

## ARTICLE 6. RANKING

The Notes rank equally and ratably with each other, without preference or priority, and (subject to Article 5) constitute general unsecured obligations of the Company senior to all Capital Stock and to all simple agreements for future equity.

## ARTICLE 7. AMENDMENT AND WAIVER

**7.1 Majority Holder Consent.** Any provision of this Note and of all other Notes may be amended or waived, and the observance of any term may be waived, by a written instrument signed by the Company and the Majority Holders, and any amendment or waiver so effected binds every holder of Notes, except as provided in Section 7.2.

**7.2 Protections.** Without the written consent of each holder adversely affected, no amendment or waiver shall:

(a) reduce the principal amount of any Note, or forgive accrued interest, other than by payment or conversion in accordance with the Notes;

(b) [[Optional: reduce the rate of interest on any Note;]]

(c) change the currency of payment;

(d) treat any holder differently, in any material respect, from other holders of Notes in the same position (taking into account differences in principal amount and issue date), unless the holder consents;

(e) impair the right of any holder to receive payment of amounts that have become due and payable, or to receive Conversion Shares to which it has become entitled; or

(f) amend this Article 7 or the definition of "Majority Holders."

**7.3 Process.** The Company shall solicit the consent of every holder of Notes to any amendment or waiver under Section 7.1 and shall promptly deliver a copy of any amendment or waiver to each holder that did not consent. An extension of the Maturity Date, a change to the Qualified Financing threshold, or a change to the conversion terms that applies equally to all Notes may be effected under Section 7.1.

## ARTICLE 8. TRANSFER; REGISTER; REPLACEMENT

**8.1 Restrictions.** The Holder may not sell, assign, pledge, or otherwise transfer this Note or any interest in it without the Company's prior written consent, which the Company shall not unreasonably withhold, except to (a) an Affiliate of the Holder, (b) the Holder's estate, heirs, or legatees on death or incapacity, or (c) a trust or family entity for estate-planning purposes; in each case only if the transferee agrees in writing to be bound by this Note and the Purchase Agreement and the transfer complies with the Securities Act and applicable state securities laws. The Company may require, at the transferor's expense, an opinion of counsel reasonably satisfactory to it that the transfer is exempt from registration. Any transfer in violation of this Section 8.1 is void.

**8.2 Market Stand-Off.** The Holder shall be bound by any market stand-off or lock-up agreement in connection with the Company's initial public offering to the same extent as the purchasers of Qualified Financing Stock, as provided in the Purchase Agreement.

**8.3 Register.** The Company shall maintain at its principal office a register in which it records the name and address of each holder of Notes, the principal amount and issue date of each Note, and each transfer, payment, and conversion. The Company may treat the person in whose name a Note is registered as its owner for all purposes. A Note may be transferred only by registration of the transfer in the register, upon surrender of the Note (or delivery of an affidavit of loss) and issuance of a new Note to the transferee. This Note is intended to be in "registered form" within the meaning of Treas. Reg. § 5f.103-1(c), and this Section 8.3 shall be construed accordingly.

**8.4 Lost Notes.** On receipt of evidence reasonably satisfactory to the Company of the loss, theft, destruction, or mutilation of this Note and of an indemnity reasonably satisfactory to it (without bond, if the Holder is an institutional investor or an original purchaser), the Company shall issue a new Note of like tenor.

## ARTICLE 9. LEGENDS; SECURITIES LAW

**9.1 Legends.** This Note bears, and each certificate or book-entry notation for the Conversion Shares shall bear, the legend on the first page of this Note (or a legend to substantially the same effect) and any legend required by the Company's bylaws, the agreements entered into in the Qualified Financing, or applicable state securities laws, until the legend is no longer required by law.

**9.2 Exemption.** The Company has issued this Note in reliance on the Holder's representations in the Purchase Agreement, including that the Holder is an "accredited investor" under Rule 501(a) of Regulation D.

## ARTICLE 10. NO STOCKHOLDER RIGHTS

Until the issuance of Conversion Shares, this Note does not entitle the Holder to any right of a stockholder of the Company, including any right to vote, to receive dividends, to consent to any corporate action, or to receive notice of meetings of stockholders, and the Holder is not a holder of Capital Stock for any purpose. Nothing in this Article 10 limits the Holder's rights to notice under this Note.

## ARTICLE 11. USURY SAVINGS

The Company and the Holder intend to comply with all applicable usury laws. Nothing in this Note or the Purchase Agreement requires the payment, or permits the collection, of interest (including any amount deemed interest under applicable law, such as the value of the conversion features of this Note) in excess of the maximum amount permitted by applicable law. If any such excess is contracted for, charged, or received, (a) the provisions of this Article 11 govern and control; (b) the Company is not obligated to pay the excess; (c) any excess received shall, at the Holder's option, be applied to reduce principal or be refunded to the Company; and (d) the effective rate of interest shall be automatically reduced to the maximum lawful rate, with all amounts deemed interest spread over the full stated term of this Note to the extent permitted by law.

## ARTICLE 12. WAIVERS

The Company waives presentment, demand for payment, protest, notice of dishonor, notice of protest, notice of acceleration, notice of intent to accelerate, and all other notices and demands in connection with the delivery, acceptance, performance, default, or enforcement of this Note, except notices expressly required by this Note. No delay or failure by the Holder in exercising any right under this Note operates as a waiver of it, and no single or partial exercise of a right precludes any other or further exercise of it.

## ARTICLE 13. TAX TREATMENT

The Company and the Holder intend that this Note be treated as indebtedness for U.S. federal and applicable state and local income tax purposes, and shall file all tax returns consistently with that treatment unless otherwise required by a final determination of a taxing authority. The Company shall furnish to the Holder any information return required by law with respect to interest or original issue discount on this Note.

## ARTICLE 14. GENERAL PROVISIONS

**14.1 Governing Law.** This Note and all claims arising out of or relating to it are governed by the laws of the State of {{governing_law_state}}, without regard to conflict-of-laws principles that would require the application of the laws of another jurisdiction.

**14.2 Forum.** The Company and the Holder irrevocably submit to the exclusive jurisdiction of the {{forum}} (or, if that court lacks subject-matter jurisdiction, the Superior Court of the State of Delaware or the United States District Court for the District of Delaware) for any action arising out of or relating to this Note, waive any objection to venue there, and agree that service of process may be made in the manner provided for notices in Section 14.4 or in any other manner permitted by law.

**14.3 Waiver of Jury Trial.** TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, THE COMPANY AND THE HOLDER EACH WAIVE THE RIGHT TO A JURY TRIAL IN ANY ACTION ARISING OUT OF OR RELATING TO THIS NOTE.

**14.4 Notices.** Notices under this Note shall be given in the manner, and are effective at the times, provided in the Purchase Agreement, to the Company at {{company_address}} (email: {{company_notice_email}}) and to the Holder at {{investor_address}} (email: {{investor_email}}), or to another address designated by notice.

**14.5 Entire Agreement.** This Note and the Purchase Agreement constitute the entire agreement between the Company and the Holder about their subject matter and supersede all prior understandings about it.

**14.6 Successors and Assigns.** This Note binds the Company and its successors and assigns and benefits the Holder and its permitted assigns. The Company may not assign its obligations under this Note without the consent of the Majority Holders, except to a successor in a Change of Control that assumes them in writing (without prejudice to Section 3.4).

**14.7 Severability.** If any provision of this Note is held invalid or unenforceable, that provision shall be enforced to the maximum extent permitted and the remaining provisions remain in full force.

**14.8 Electronic Signatures.** This Note may be executed and delivered by electronic signature complying with the U.S. federal ESIGN Act of 2000 (15 U.S.C. § 7001 et seq.) or the Delaware Uniform Electronic Transactions Act (6 Del. C. ch. 12A), and an electronically signed copy is an original for all purposes, including Section 8.4.

**14.9 No Recourse.** No past, present, or future stockholder, director, officer, or employee of the Company has any personal liability for the obligations of the Company under this Note.

**14.10 Specific Performance.** The Company acknowledges that the Holder would be irreparably harmed by a failure to issue Conversion Shares when required, and the Holder is entitled to specific performance of Article 3 without posting a bond, in addition to any other remedy.

**14.11 Further Assurances.** The Company shall execute and deliver all further documents and take all further actions reasonably necessary to carry out this Note, including the corporate actions described in Section 3.9.

**14.12 Construction.** The Company and the original purchasers of the Notes negotiated this Note with the advice of counsel, and no rule of construction against the drafter applies.

*(Signature page follows.)*

---

IN WITNESS WHEREOF, the Company has caused this Convertible Promissory Note to be executed by its duly authorized officer as of the Issue Date.

{{company_name}}

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

Address for notices: {{company_address}}
Email: {{company_notice_email}}

**HOLDER ACKNOWLEDGMENT** [[Optional: The Holder acknowledges receipt of this Note and agrees to be bound by Sections 3.5, 5.2, 7, and 8.

{{investor_name}}

By: ______________________________
Name: {{investor_signatory_name}}
Title: {{investor_signatory_title}}]]

---

## Exhibit A: Form of Conversion or Repayment Election

To: {{company_name}}

The undersigned holder of Convertible Promissory Note No. {{note_number}} (the "**Note**") elects as follows (check one):

- ☐ **Maturity conversion** (Section 3.3): to convert the Outstanding Balance of the Note on the Maturity Date at the Maturity Conversion Price.
- ☐ **Change of Control repayment** (Section 3.4(b)(i)): to receive the cash payment provided in Section 3.4(b)(i).
- ☐ **Change of Control conversion** (Section 3.4(b)(ii)): to convert the Outstanding Balance into Common Stock immediately before, and contingent on, the closing of the Change of Control.
- ☐ **Optional conversion in a non-qualified financing** (Section 3.2, if applicable): as a holder joining the Majority Holders' election.

Capitalized terms have the meanings given in the Note. The undersigned confirms that its representations in the Purchase Agreement remain true as of the date below.

Holder: {{investor_name}}

By: ______________________________
Name:
Title:
Date:

> **Drafting note:** Delete the election options that do not apply to the alternatives chosen in Sections 3.2 through 3.4.

## Exhibit B: Conversion Calculation Statement (delivered under Sections 3.1(e) and 3.8)

| Item | Amount |
|---|---|
| Qualified Financing Price (unrounded and rounded) | {{qualified_financing_price}} |
| Discount Price | {{discount_price}} |
| Cap Capitalization (Alternative selected: {{cap_capitalization_alternative}}) | {{cap_capitalization}} shares |
| Cap Price | {{cap_price}} |
| Conversion Price (lesser of Discount Price and Cap Price) | {{conversion_price}} |
| Principal | {{purchase_amount}} |
| Accrued interest ({{interest_days}} days at {{interest_rate}} simple, actual/365) | {{accrued_interest}} |
| Conversion Amount | {{conversion_amount}} |
| Conversion Shares (rounded down) | {{conversion_shares}} shares of {{conversion_series_name}} |
| Cash in lieu of fractional share | {{cash_in_lieu}} |
| Model reference | `scripts/conversion_calculator.py` run dated {{model_run_date}} |
