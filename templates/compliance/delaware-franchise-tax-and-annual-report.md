---
id: delaware-franchise-tax-and-annual-report
title: Delaware Franchise Tax and Annual Report — Guide, Worksheet, and Client Memo
category: compliance
stage: compliance
signers: [Officer or director who certifies the Annual Franchise Tax Report (8 Del. C. § 502(a))]
authorities:
  - "8 Del. C. § 501 (corporations subject to franchise tax)"
  - "8 Del. C. § 502 (annual franchise tax report due March 1; contents; $200 late penalty; no good standing while delinquent)"
  - "8 Del. C. § 503 (rates; authorized shares method; assumed par value capital method; $175/$400 minimums; $200,000 maximum; $250,000 large corporate filer; proration; half rate for inactive periods; 'total gross assets' from Form 1120 Schedule L)"
  - "8 Del. C. § 504 (due March 1; estimated installments for tax of $5,000 or more; 1.5% monthly interest)"
  - "8 Del. C. § 505 (petition for refund by March 1 of the second following year)"
  - "8 Del. C. § 510 (charter void after one year of nonpayment or non-filing)"
  - "8 Del. C. § 391(a)(18) ($50 annual report fee; $25 for exempt corporations)"
  - "8 Del. C. § 312 (revival of a void charter)"
use_when: A Delaware corporation must file its annual report and pay franchise tax (every year by March 1), has received an alarming franchise tax notice computed under the authorized shares method, is planning an authorized-share increase, or needs to restore good standing.
do_not_use_when: The entity is a Delaware LLC or limited partnership (they pay a flat annual tax due June 1, currently $400, under 6 Del. C. § 18-1107 or § 17-1109, and file no annual report), or the question is a foreign state's franchise or income tax (see foreign-qualification-guide).
related: [board-consent-resolution-library, certificate-of-amendment, section-204-ratification, dissolution-guide, foreign-qualification-guide]
sources:
  - name: "Delaware Code, Title 8, Chapter 5 (Corporation Franchise Tax), official text, read November 2, 2026"
    url: https://delcode.delaware.gov/title8/c005/index.html
  - name: "Delaware Division of Corporations — How to Calculate Franchise Taxes (methods, $400 APVC minimum, examples)"
    url: https://corp.delaware.gov/frtaxcalc/
  - name: "Delaware Division of Corporations — Annual Report and Tax Information (fees, March 1, $200 penalty, 1.5% interest, $250,000 large corporate filer)"
    url: https://corp.delaware.gov/paytaxes/
  - name: "Delaware Division of Corporations Fee Schedule, revised August 1, 2026 (revival; good standing)"
    url: https://corpfiles.delaware.gov/Fee_Schedule/AugustFee2026.pdf
  - name: "Delaware Code, Title 6, § 18-1107 (LLC annual tax $400; due June 1)"
    url: https://delcode.delaware.gov/title6/c018/sc11/index.html
  - name: "Clerky, Stripe Atlas, and Carta franchise-tax guides (consulted for common founder questions; no text copied)"
    url: https://stripe.com/atlas/guides
last_verified: 2026-11-02
---

## About this template

**What it does.** This file explains how Delaware's corporate franchise tax and annual report work, gives an exact worksheet for both computation methods, works a typical startup example, and includes a short client memo explaining why the bill the company received is too high. The skill's calculator, `python3 scripts/franchise_tax.py --authorized N --par P --issued N --gross-assets X`, implements the same formulas.

**Who files, when, and what.**
- Every Delaware stock corporation files an Annual Franchise Tax Report and pays franchise tax "annually on or before March 1" for the preceding calendar year (§§ 502(a), 504(a)), regardless of its fiscal year, and regardless of whether it does business in Delaware or has any income. Filing is online through the Division of Corporations; the annual report filing fee is $50 ($25 for exempt corporations) (§ 391(a)(18)).
- The report states the registered office and agent, the nature of the business, the principal place of business (which may not be the registered agent's address unless the company is its own agent in Delaware), the names and addresses of all directors as of the filing date, the name and address of the officer signing, and the authorized shares and par value of each class (§ 502(a)(1)–(6)). To use the assumed par value capital method, it must also report issued shares and total gross assets (§ 503(b)). It is signed by the president, secretary, treasurer, another proper officer, or a director; a knowingly false statement is perjury (§ 502(a)–(b)).
- Corporations whose franchise tax for the current year is estimated at $5,000 or more pay estimated installments: 40% by June 1, 20% by September 1, 20% by December 1, and the remainder with the report by March 1 of the next year (§ 504(a)); the installments are based on the preceding year's tax (§ 504(e)).

**Method 1: Authorized Shares Method (the default) (§ 503(a)(1)).**

| Authorized shares (all classes) | Tax |
|---|---|
| 5,000 or fewer | $175 (minimum) |
| 5,001 to 10,000 | $250 |
| Each additional 10,000 shares or part thereof above 10,000 | add $85 |
| Maximum | $200,000 |

Formula for more than 10,000 shares: $250 + $85 × ceiling((authorized shares − 10,000) ÷ 10,000). For 10,000,000 authorized shares: $250 + $85 × 999 = **$85,165**. All authorized shares count, whether or not issued (§ 503(g)).

**Method 2: Assumed Par Value Capital Method (§ 503(a)(2)).** The corporation pays the lesser of the two methods (§ 503(a)), but the Division bills under Method 1 unless the report states issued shares and total gross assets (§ 503(b)). The steps, as the Division states them:
1. **Assumed par** = total gross assets ÷ total issued shares (all classes), carried to six decimal places.
2. For each class whose par value is **less than** the assumed par, multiply its authorized shares by the assumed par.
3. For each class whose par value is **greater than** the assumed par, multiply its authorized shares by its par value.
4. **Assumed par value capital (APVC)** = sum of steps 2 and 3.
5. **Tax** = $400 for each $1,000,000 of APVC or part thereof (round APVC up to the next million if it exceeds $1,000,000, divide by 1,000,000, multiply by $400). Minimum $400; maximum $200,000 (§ 503(c)). Where APVC is under $1,000,000, the statute prorates against $400, but the $400 minimum applies.

No-par stock is taxed under a separate assumed no-par capital computation ($100 per no-par share) in § 503(a)(2); startups should use par-value stock.

**Definitions that drive the number.**
- **Total gross assets** means all assets, net only of allowances for bad debts and accumulated depreciation, depletion, and amortization, and must be the "total assets" reported on federal Form 1120, Schedule L, for the fiscal year ending in the calendar year before filing; interests in consolidated entities are included (§ 503(i)). If the Form 1120 has not been prepared by March 1, use the year-end balance sheet total that will be reported. (Small corporations are not required to complete Schedule L when total receipts and total assets are both under $250,000, but they still report balance-sheet total assets to Delaware.)
- **Issued shares** means all issued shares of all classes, including unvested restricted stock; unexercised options, warrants, and SAFEs are not issued shares.
- **Authorized shares** means the total number the charter authorizes, whether or not a smaller number may be outstanding (§ 503(g)).

> **Verify:** The statute uses "issued shares," which in Delaware usage includes treasury shares (issued but not outstanding). Confirm with the Division's current annual report instructions whether to include treasury shares in the issued-share count before relying on them to lower the assumed par.

**Large corporate filers.** A corporation listed on a national securities exchange with consolidated revenues or assets of $750,000,000 or more (and both at least $250,000,000) whose tax would otherwise be $200,000 pays $250,000 (§ 503(c)). Irrelevant to private startups.

**Partial and inactive years.** In the first year, the tax is prorated for the part of the year the corporation existed (§ 503(d)). If authorized shares change mid-year, the tax is prorated across the periods (§ 503(e)). A corporation that reports it was not engaged in any of its business activities pays half rate for that portion of the year (§ 503(f)); the Division may require a supporting affidavit. Do not claim the half rate for a startup that is building product.

**Penalties and consequences.**

| Failure | Consequence | Authority |
|---|---|---|
| Report not filed by March 1 | $200 penalty added to the tax | § 502(c) |
| Tax not paid when due (including estimated installments) | Interest at 1.5% per month or part of a month on the unpaid tax (the Division applies it to tax and penalty) | § 504(c), (f); corp.delaware.gov/paytaxes |
| Delinquency of any length | No certificate of good standing; financings, bank accounts, and foreign qualifications stall | § 502(f) |
| Delinquency of one year | Charter void; powers inoperative; Governor's proclamation; acting under a proclaimed charter is a crime (fine up to $1,000 or imprisonment up to 1 year) | §§ 510–513 |
| Registered agent lapse while delinquent | Process may be served on the Secretary of State | § 502(d) |
| Revival | Certificate of revival under § 312 with all back taxes, penalties, and interest; fee $189 plus taxes (fee schedule revised August 1, 2026) | § 312 |
| Overpayment (for example, paid the authorized-shares bill) | Petition for refund by March 1 of the second calendar year after the tax year | § 505(a) |

**Why the alarming bill arrives, and how to avoid it.** The Division (and many registered agents' reminders) compute the tax under the authorized shares method because that method needs no information beyond the charter. A startup with 10,000,000 authorized shares sees $85,165; with 20,000,000 shares, $170,165. Filing the report with issued shares and gross assets recomputes the tax under the APVC method, which is usually the $400 minimum to a few thousand dollars for seed and Series A companies. Practical rules:
1. Always file the report with issued shares and total gross assets. Never pay an authorized-shares bill without recomputing.
2. Keep authorized shares in reasonable proportion to issued shares. APVC is assumed par × authorized shares; authorizing many times the issued shares inflates the tax as assets grow (100,000,000 authorized, 10,000,000 issued, $5,000,000 of assets: $20,000; with 15,000,000 authorized, $3,200).
3. Use low par value ($0.00001 or $0.0001) so the step 3 par-value multiplication does not dominate.
4. Calendar the estimated installments once the tax reaches $5,000 (often after a large priced round increases gross assets).
5. If a prior year was paid under the authorized shares method, file a refund petition by the § 505(a) deadline.

**Interaction with other documents.** A charter amendment changing authorized shares or a certificate of validation changes the tax for the affected periods (§ 503(e)). A dissolving or converting corporation must pay all franchise taxes (including for the month of dissolution) and file a final report before the certificate is filed (§ 277). The annual report's director list must match the minute book.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `company_name` | Exact legal name | Northwind Robotics, Inc. | Shared |
| `tax_year` | Calendar year covered | 2026 | |
| `filing_deadline` | March 1 of the following year | March 1, 2027 | Next business day practice varies; file early |
| `authorized_common_shares`, `authorized_preferred_shares` | Authorized shares by class | 10,000,000; 0 | Shared |
| `total_authorized_shares` | All classes | 10,000,000 | |
| `par_value` | Par value per share | $0.00001 | Shared |
| `issued_shares_total` | All issued shares at fiscal year end | 9,000,000 | |
| `gross_assets` | Total assets per Form 1120 Schedule L at fiscal year end | $250,000 | |
| `assumed_par` | gross_assets ÷ issued_shares_total | $0.027778 | Six decimals |
| `apvc` | Assumed par value capital | $277,777.78 | |
| `asm_tax`, `apvc_tax`, `tax_due` | Tax under each method; lower one | $85,165; $400; $400 | |
| `annual_report_fee` | Filing fee | $50 | § 391(a)(18) |
| `ceo_name`, `signatory_name`, `signatory_title` | Officer certifying the report | | Shared |
| `director_names` | Directors as of filing date | | § 502(a)(5) |
| `registered_agent_name`, `registered_agent_address` | Registered agent and office | | Shared |
| `company_address` | Principal place of business | | Shared; not the agent's address |
| `client_contact_name` | Recipient of the client memo | | |

## Form

---

# PART 1. FRANCHISE TAX WORKSHEET

**{{company_name}} — Delaware Franchise Tax Worksheet for {{tax_year}} (due {{filing_deadline}})**

**A. Inputs (as of December 31, {{tax_year}})**

| Line | Item | Amount |
|---|---|---|
| A1 | Authorized Common Stock | {{authorized_common_shares}} |
| A2 | Authorized Preferred Stock | {{authorized_preferred_shares}} |
| A3 | Total authorized shares (A1 + A2) | {{total_authorized_shares}} |
| A4 | Par value per share (each class) | {{par_value}} |
| A5 | Total issued shares, all classes | {{issued_shares_total}} |
| A6 | Total gross assets (Form 1120, Schedule L, "total assets") | {{gross_assets}} |

**B. Authorized Shares Method**

| Line | Computation | Amount |
|---|---|---|
| B1 | If A3 ≤ 5,000: $175. If 5,001–10,000: $250. Otherwise: $250 + $85 × ceiling((A3 − 10,000) ÷ 10,000) | {{asm_tax}} |
| B2 | Lesser of B1 and $200,000 | {{asm_tax}} |

**C. Assumed Par Value Capital Method**

| Line | Computation | Amount |
|---|---|---|
| C1 | Assumed par = A6 ÷ A5 (six decimal places) | {{assumed_par}} |
| C2 | For each class with par below C1: authorized shares × C1 | |
| C3 | For each class with par above C1: authorized shares × par | |
| C4 | APVC = C2 + C3 | {{apvc}} |
| C5 | If C4 ≤ $1,000,000: $400. Otherwise: $400 × ceiling(C4 ÷ 1,000,000) | {{apvc_tax}} |
| C6 | Lesser of C5 and $200,000 | {{apvc_tax}} |

**D. Amount Due**

| Line | Item | Amount |
|---|---|---|
| D1 | Franchise tax: lesser of B2 and C6 | {{tax_due}} |
| D2 | Annual report filing fee | {{annual_report_fee}} |
| D3 | Total due by {{filing_deadline}} (before any penalty or interest) | |
| D4 | If D1 for next year is expected to be $5,000 or more: estimated installments of 40% (June 1), 20% (September 1), and 20% (December 1) | |

---

# PART 2. WORKED EXAMPLES (FICTIONAL COMPANY)

**Example 1 — Typical seed-stage company.** Northwind Robotics, Inc. has 10,000,000 authorized shares of Common Stock at $0.00001 par, 9,000,000 shares issued at December 31, and $250,000 of total assets.

| Step | Computation | Result |
|---|---|---|
| Authorized shares method | $250 + $85 × ceiling(9,990,000 ÷ 10,000) = $250 + $85 × 999 | $85,165 |
| Assumed par | $250,000 ÷ 9,000,000 | $0.027778 |
| APVC | $0.027778 × 10,000,000 (par $0.00001 is below assumed par) | $277,778 |
| APVC tax | APVC under $1,000,000; minimum applies | $400 |
| Tax due | Lesser of $85,165 and $400 | $400 |
| Plus annual report fee | | $50 |
| **Total** | | **$450** |

**Example 2 — After a seed round.** Same company, with $3,200,000 of total assets.

| Step | Computation | Result |
|---|---|---|
| Assumed par | $3,200,000 ÷ 9,000,000 | $0.355556 |
| APVC | $0.355556 × 10,000,000 | $3,555,556 |
| APVC tax | $400 × ceiling(3.555556) = $400 × 4 | $1,600 |
| **Total with fee** | | **$1,650** |

**Example 3 — After a Series A with Preferred Stock.** 15,000,000 Common and 5,000,000 Preferred authorized (20,000,000 total), all at $0.00001 par; 9,000,000 Common and 4,000,000 Preferred issued (13,000,000); $12,000,000 of total assets.

| Step | Computation | Result |
|---|---|---|
| Authorized shares method | $250 + $85 × 1,999 | $170,165 |
| Assumed par | $12,000,000 ÷ 13,000,000 | $0.923077 |
| APVC | $0.923077 × 20,000,000 | $18,461,538 |
| APVC tax | $400 × 19 | $7,600 |
| **Total with fee** | | **$7,650** |
| Next year | Tax ≥ $5,000, so estimated installments of $3,040 (June 1), $1,520 (September 1), and $1,520 (December 1), based on the preceding year's tax, with the balance on March 1 | |

> **Drafting note:** Run `python3 scripts/franchise_tax.py` with the client's numbers and attach the output. In the first year, Delaware prorates the tax for the part of the year the company existed (§ 503(d)); the online filing system computes the proration.

---

# PART 3. ANNUAL REPORT FILING CHECKLIST

| No. | Item | Source | Done |
|---|---|---|---|
| 1 | Delaware file number and current registered agent and office | Registered agent; {{registered_agent_name}}, {{registered_agent_address}} | ☐ |
| 2 | Principal place of business (street, city, state, ZIP; not the agent's address) | {{company_address}} | ☐ |
| 3 | Names and addresses of all directors as of the filing date | Minute book; {{director_names}} | ☐ |
| 4 | Name, title, and address of the certifying officer | {{signatory_name}}, {{signatory_title}} | ☐ |
| 5 | Authorized shares and par value of each class, with dates of any change during the year | Certified charter | ☐ |
| 6 | Total issued shares of all classes at fiscal year end | Stock ledger | ☐ |
| 7 | Total gross assets at fiscal year end, matching Form 1120 Schedule L | CFO or tax preparer | ☐ |
| 8 | Nature of business | | ☐ |
| 9 | Confirm the tax computed online equals the APVC result (or the lower method) | Part 1 | ☐ |
| 10 | Pay tax and $50 fee by {{filing_deadline}}; save the filed report and receipt to the minute book | | ☐ |
| 11 | Calendar estimated installments if next year's tax is $5,000 or more | § 504(a) | ☐ |

---

# PART 4. CLIENT MEMO: "WHY IS OUR DELAWARE TAX BILL $85,165?"

**To:** {{client_contact_name}}, {{company_name}}
**Re:** Delaware franchise tax for {{tax_year}}

The notice you received computes Delaware franchise tax using the "authorized shares method," which charges by the number of shares your charter authorizes ({{total_authorized_shares}}) regardless of the company's size. Delaware law lets the company pay the lower amount computed under the "assumed par value capital method," which is based on your total assets ({{gross_assets}}) and issued shares ({{issued_shares_total}}). Under that method, the tax is {{apvc_tax}}, and the total due with the {{annual_report_fee}} annual report fee is shown in the attached worksheet.

To get the lower amount, the annual report filed online by {{filing_deadline}} must state the company's issued shares and total gross assets as of December 31, {{tax_year}}. Please do not pay the amount on the notice. If the company has paid an authorized-shares bill in a prior year, it may petition for a refund by March 1 of the second year after that tax year.

If the report and tax are late, Delaware adds a $200 penalty and interest of 1.5% per month, will not issue a certificate of good standing (which investors, lenders, and banks require), and after one year the company's charter becomes void.
